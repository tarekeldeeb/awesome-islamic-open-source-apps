import requests
import re
from collections import defaultdict
from openai import OpenAI
import json
import os
import argparse
import threading
import itertools
import sys
import time

# Fetch secrets from environment
TOKEN = os.getenv("GITHUB_TOKEN", "")
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

extra_topics = ["muslim-app", "islamic", "islamic-app"]
README_URL = "https://raw.githubusercontent.com/choubari/Awesome-Muslims/master/README.md"
OUTPUT_FILE = "README.md"
CACHE_FILE = "repo_cache.json"


CATEGORIES = {
    "Quranic Text and Reading": ['quran', 'qurani', 'verses', 'mushaf', 'surah'],
    "Hadith Collection and Study": ['hadith', 'sunnah', 'narration', 'sayings', 'prophet'],
    "Prayer Times Calculation and Display": ['prayer', 'salat', 'mussalla', 'mosque', 'azan'],
    "Islamic Events and Reminders": ['reminder', 'event', 'ramadan', 'eid', 'hijri'],
    "Quranic Learning and Study Tools": ['learn', 'study', 'recite', 'tafsir', 'translation'],
    "Islamic Resources and Community": ['community', 'muslim', 'resource', 'hub', 'open'],
    "Hadith Search and API": ['api', 'search', 'repository', 'collect', 'retrieve'],
    "Qibla Direction and Finder": ['qibla', 'direction', 'compass', 'finder', 'kaaba'],
    "Dua Collection and Reminders": ['dua', 'supplication', 'adhkar', 'remembrance', 'azkar'],
    "Other": ['other', 'misc', 'general', 'various', 'assorted']
}

class Spinner:
    def __init__(self, message="Loading..."):
        self.spinner = itertools.cycle(['|', '/', '-', '\\'])
        self.stop_running = False
        self.message = message

    def start(self):
        def run():
            while not self.stop_running:
                sys.stdout.write(f"\r{self.message} {next(self.spinner)}")
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\r' + ' ' * (len(self.message) + 2) + '\r')  # Clear line

        self.thread = threading.Thread(target=run)
        self.thread.start()

    def stop(self):
        self.stop_running = True
        self.thread.join()

def get_project_info(url):
    functions = [
      {
        "name": "parse_link",
        "description": "Parse a URL and extract structured metadata. The required description field is a single line description of this project with no '*' allowed. The top2 field is a single line with '👍' as a bullet symbol to describes the top 2 differentiators, the top 2 features and/or edges. The deployement is one of: (🌐, 🖥️, 📱, 📺, 🛠️) for Web, Desktop, Mobile, TV, others ",
        "parameters": {
          "type": "object",
          "properties": {
            "description": {"type": "string"},
            "top2": {"type": "string"},
            "deployment": {"type": "string"}
          },
          "required": ["description", "deployment", "top2"]
        }
      }
    ]
    client = OpenAI(api_key=OPENAI_KEY)
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You parse links."},
        {"role": "user", "content": f"Parse {url}"}
      ],
      functions=functions,
      function_call={"name": "parse_link"}
    )
    func_args = response.choices[0].message.function_call.arguments
    return json.loads(func_args)

def classify_category(name, description):
    if not description:
        return "Other"
    n = " ".join([name, description]).lower()
    for cat, kws in CATEGORIES.items():
        if any(kw in n for kw in kws):
            return cat
    print(f"❌ Cannot classify {name}: {description}")
    return "Other"

def fetch_repo(url):
    m = re.match(r"https://github.com/([^/]+)/([^/]+)", url)
    if not m:
        return None
    owner, repo = m.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(api_url, headers=HEADERS)
    if r.status_code == 200:
        d = r.json()
        gpt_meta = get_project_info(d["html_url"])
        return {
            "name": d["name"],
            "html_url": d["html_url"],
            "description": gpt_meta.get("description") or d.get("description") or "",
            "stars": d.get("stargazers_count", 0),
            "language": d.get("language") or "Unknown",
            "category": classify_category(d["name"], d.get("description")),
            "deployment": gpt_meta.get("deployment", ""),
            "top2": gpt_meta.get("top2", "")
        }
    else:
        print(f"❌ Skipping {url} ({r.status_code})")
        return None

def fetch_repos_by_topic(topic, max_pages=10):
    print(f"🔍 Fetching topic: {topic}")
    all_links = []
    for page in range(1, max_pages + 1):
        url = f"https://api.github.com/search/repositories?q=topic:{topic}&sort=stars&order=desc&page={page}&per_page=100"
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            print(f"⚠️ GitHub API error for topic '{topic}' on page {page}: {r.status_code}")
            break
        data = r.json()
        items = data.get("items", [])
        if not items:
            break
        for repo in items:
            html_url = repo.get("html_url")
            if html_url:
                all_links.append(html_url)
    return all_links

def do_default():
    # 🧠 Caching layer
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
    else:
        cache = {}

    # Step 1: Download main README
    resp = requests.get(README_URL)
    if resp.status_code != 200:
        raise RuntimeError("Failed to download README")
    readme = resp.text
    links = re.findall(r"-\s*\[.*?\]\((https?://[^\s)]+)\)", readme)

    # Step 2: Add links from GitHub topic pages
    for topic in extra_topics:
        links += fetch_repos_by_topic(topic)

    # Step 3: Deduplicate links
    links = list(set(links))
            
    # Step 4: Fetch metadata
    projects = []
    for i, link in enumerate(links, 1):
        print(f"🔍 [{i}/{len(links)}] Fetching {link}")
        if link in cache:
            print("   ⚡ Using cached version")
            d = cache[link]

            # Always reclassify using the latest CATEGORIES
            d["category"] = classify_category(d["name"], d["description"])

            projects.append(d)
            cache[link] = d  # Save updated category back to cache
        else:
            info = fetch_repo(link)
            if info:
                projects.append(info)
                cache[link] = info  # ✅ Add to cache
            
    # Step 5: Organize by category and language
    tree = defaultdict(lambda: defaultdict(list))
    for p in projects:
        tree[p["category"]][p["language"]].append(p)
    for cat in tree:
        for lang in tree[cat]:
            tree[cat][lang].sort(key=lambda x: x["stars"], reverse=True)
        tree[cat] = dict(sorted(tree[cat].items(), key=lambda item: len(item[1]), reverse=True))
    tree = dict(
        sorted(
            tree.items(),
            key=lambda item: (
                float('inf') if item[0].lower() == "other" else -sum(len(lst) for lst in item[1].values())
            )
        )
    )
    
    # Step 6: Write Markdown
    md = "# 📚 Open Source Islamic Projects\n\nAuto-Categorized, then sorted by ⭐s.\n\nSource: from [Awesome-Muslims](https://github.com/choubari/Awesome-Muslims/) and other Github lists.\n\n## Table of Contents\n\n"
    for category in tree:
        anchor = category.lower().replace(" ", "-")
        md += f"- [{category}](#{anchor})\n"
    md += "\n"
    for category, langs in tree.items():
        total = sum(len(items) for items in langs.values())
        md += f"<a name='{category.lower().replace(" ", "-")}'></a>\n## {category} ({total} projects)\n"
        for lang, repos in langs.items():
            md += f"### {lang}\n"
            for r in repos:
                top2 = re.sub(r"\\b(1\\.|2\\.|\\*)", "👍", r["top2"]).replace("\n", " ")
                md += f"{r['deployment']} **[{r['name']}]({r['html_url']})** ⭐ {r['stars']} – {r['description']}  {top2}\n\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md)

    # 💾 Save updated cache
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    print(f"✅ Done! Projects found: {len(projects)} → Saved to {OUTPUT_FILE}")

def propose_categories_from_cache():
    if not os.path.exists(CACHE_FILE):
        print("❌ Cache file not found.")
        return

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cached = json.load(f)

    spinner = Spinner("🧠 Categorizing projects with GPT...")
    spinner.start()
    
    try:
        # Format: name: description
        items = [
            f"- {v['name']}: {v.get('description', '')}" for v in cached.values()
        ]
        joined = "\n".join(items[:300])  # Limit to 100? for token size

        client = OpenAI(api_key=OPENAI_KEY)
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert product categorizer for open-source Islamic software. "
                    "Your task is to output two sections:\n\n"
                    "1. A concise list of **exactly 10 categories** (9 + 'Other'), each with a name and 3–5 example project names from the list below.\n\n"
                    "2. A valid Python dictionary named `CATEGORIES = { ... }` where:\n"
                    "   - Each key is one of the category names.\n"
                    "   - Each value is a list of **unique keywords** for classification (e.g., ['quran', 'mushaf']).\n"
                    "   - **No keyword may appear in more than one category.** All keywords must be lowercase.\n"
                    "   - Keywords should be generalizable triggers found in project names or descriptions.\n\n"
                    "⚠️ Do not reuse the same keyword in more than one category. The dictionary will be used for strict matching."
                )
            },
            {
                "role": "user",
                "content": (
                    f"The following is a list of Islamic open source projects with their names and descriptions:\n\n{joined}\n\n"
                    "Please propose categories and generate the CATEGORIES dictionary as described above."
                )
            },
        ]

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
    finally:
        spinner.stop()

    print("🧠 Proposed Categories:\n")
    print(response.choices[0].message.content)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Awesome Islamic Open-source Apps -- Fetch and Catogorize")
    parser.add_argument("--propose-categories", action="store_true", help="Analyze cache and propose 9 categories + Other")

    args = parser.parse_args()
    print(f"{parser.description}\n")
    
    if args.propose_categories:
        propose_categories_from_cache()
    else:
        do_default() # Fetch, categorize, update cache.

