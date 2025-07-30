import requests
import re
from collections import defaultdict
from openai import OpenAI
import json


TOKEN = "SECRET"
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
OPENAI_KEY = "SECRET"



README_URL = "https://raw.githubusercontent.com/choubari/Awesome-Muslims/master/README.md"
OUTPUT_FILE = "awesome_muslims_projects.md"

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
        "description": "Parse a URL and extract structured metadata. The required description field is a single line description of this project. No technical details, just the goal and value. The top2 field describes the top 2 differentiators, the top 2 features and/or edges. The deployement is one of: Web, Desktop, Mobile, TV, others ",
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
        
        # Get additional metadata from ChatGPT
        gpt_meta = get_project_info(d["html_url"])

        # Merge and return combined metadata
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

# 1. Download README
resp = requests.get(README_URL)
if resp.status_code != 200:
    raise RuntimeError("Failed to download README")
readme = resp.text

# 2. Extract GitHub links
links = re.findall(r"-\s*\[.*?\]\((https?://[^\s)]+)\)", readme)
links = list(set(links))

# 3. Fetch metadata
projects = []
for i, link in enumerate(links, 1):
    print(f"🔍 [{i}/{len(links)}] Fetching {link}")
    info = fetch_repo(link)
    if info:
        projects.append(info)

# 4. Organize into tree
tree = defaultdict(lambda: defaultdict(list))
for p in projects:
    tree[p["category"]][p["language"]].append(p)

# Sort each language list by stars
for cat in tree:
    for lang in tree[cat]:
        tree[cat][lang].sort(key=lambda x: x["stars"], reverse=True)

# Sort languages inside each category by total items
for cat in tree:
    tree[cat] = dict(
        sorted(
            tree[cat].items(),
            key=lambda item: len(item[1]),  # number of items in this lang
            reverse=True,
        )
    )

# Sort categories by total items across all languages
tree = dict(
    sorted(
        tree.items(),
        key=lambda item: sum(len(lst) for lst in item[1].values()),  # total per cat
        reverse=True,
    )
)


# 5. Write Markdown
md = "# 📚 Open Source Islamic Projects (from Awesome-Muslims)\n\n# Table of Contents\n\n- [Prayer Times](#prayer-times)\n- [Quran](#quran)\n- [Islamic Calendar](#islamic-calendar)\n- [Hadith](#hadith)\n- [Azkar & Dua](#azkar--dua)\n- [Other](#other)\n\n"
for category, langs in tree.items():
    total = sum(len(items) for items in tree[category].values())
    md += f"## {category} ({total} projects)\n"
    for lang, repos in langs.items():
        md += f"### {lang}\n"
        for r in repos:
            md += f"- **[{r['name']}]({r['html_url']})** – ⭐ {r['stars']}\n"
            md += f"  *{r['description']}"
            md += f"  *{re.sub(r'\b(1\.|2\.)', '👍', r['top2']).replace('\n', ' ')}\n"
            md += f"  *Deployment:* {r['deployment']}\n\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(md)

print(f"✅ Done! Projects found: {len(projects)} → Saved to {OUTPUT_FILE}")
