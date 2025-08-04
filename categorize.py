import requests
import re
from collections import defaultdict
from openai import OpenAI
import json
import os
import argparse

# Fetch secrets from environment
TOKEN = os.getenv("GITHUB_TOKEN", "")
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

extra_topics = ["muslim-app", "islamic", "islamic-app"]
README_URL = "https://raw.githubusercontent.com/choubari/Awesome-Muslims/master/README.md"
OUTPUT_FILE = "README.md"
CACHE_FILE = "repo_cache.json"


CATEGORIES = {
    "Quran": ["quran", "mushaf"],
    "Prayer Times": ["adhan", "athan", "prayer", "times", "salat", "namaz", "salah", "qibla"],
    "Hadith": ["hadith", "sunnah"],
    "Azkar & Dua": ["azkar", "adhkar", "dua", "hisn"],
    "Islamic Calendar": ["hijri", "calendar"],
    "Library": ["library", "developers", "api"],
    "Other": []
}

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
            projects.append(cache[link])
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
    tree = dict(sorted(tree.items(), key=lambda item: sum(len(lst) for lst in item[1].values()), reverse=True))

    # Step 6: Write Markdown
    md = "# 📚 Open Source Islamic Projects\n\nAuto-Categorized, then sorted by ⭐s.\n\nSource: (from [Awesome-Muslims](https://github.com/choubari/Awesome-Muslims/))\n\n## Table of Contents\n\n"
    for category in tree:
        anchor = category.lower().replace(" ", "-")
        md += f"- [{category}](#{anchor})\n"
    md += "\n"
    for category, langs in tree.items():
        total = sum(len(items) for items in langs.values())
        md += f"## {category} ({total} projects)\n"
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

    # Format: name: description
    items = [
        f"- {v['name']}: {v.get('description', '')}" for v in cached.values()
    ]
    joined = "\n".join(items[:1000])  # Limit to 100? for token size

    client = OpenAI(api_key=OPENAI_KEY)
    messages = [
        {
            "role": "system",
            "content": "You are an expert taxonomist and product categorizer for open source Islamic software projects.",
        },
        {
            "role": "user",
            "content": f"""The following is a list of Islamic open source projects with their names and descriptions. Group them into exactly 9 smart and intuitive categories (plus an 'Other' bucket). Each category should include a short title and a few example apps from the list. Be smart — use purpose, audience, or deployment as hints.\n\n{joined}""",
        },
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    print("🧠 Proposed Categories:\n")
    print(response.choices[0].message.content)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Awesome Islamic Open-source Apps -- Fetch and Catogorizer")
    parser.add_argument("--propose-categories", action="store_true", help="Analyze cache and propose 9 categories + Other")

    args = parser.parse_args()
    print(f"{parser.description}\n")
    
    if args.propose_categories:
        propose_categories_from_cache()
    else:
        do_default() # Fetch, categorize, update cache.

