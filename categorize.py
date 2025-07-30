import requests
import re
from collections import defaultdict

TOKEN = "MY_SECRET"
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

README_URL = "https://raw.githubusercontent.com/choubari/Awesome-Muslims/master/README.md"
OUTPUT_FILE = "awesome_muslims_projects.md"

CATEGORIES = {
    "Quran": ["quran", "mushaf"],
    "Prayer Times": ["adhan", "athan", "prayer", "times", "salat", "namaz", "salah", "qibla"],
    "Hadith": ["hadith", "sunnah"],
    "Azkar & Dua": ["azkar", "adhkar", "dua", "hisn"],
    "Islamic Calendar": ["hijri", "calendar"],
    "Library": ["developers", "API"],
    "Other": []
}

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
        return {
            "name": d["name"],
            "html_url": d["html_url"],
            "description": d.get("description") or "",
            "stars": d.get("stargazers_count", 0),
            "language": d.get("language") or "Unknown",
            "category": classify_category(d["name"], d.get("description"))
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

for cat in tree:
    for lang in tree[cat]:
        tree[cat][lang].sort(key=lambda x: x["stars"], reverse=True)

# 5. Write Markdown
md = "# 📚 Open Source Islamic Projects (from Awesome-Muslims)\n\n"
for category, langs in tree.items():
    md += f"## {category}\n"
    for lang, repos in langs.items():
        md += f"### {lang}\n"
        for r in repos:
            md += f"- **[{r['name']}]({r['html_url']})** – ⭐ {r['stars']}\n"
            md += f"  *Deployment:* _TBD_\n"
            md += f"  *Description:* {r['description']}\n"
            md += f"  *Features:* _(Add 2 standout features manually)_\n\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(md)

print(f"✅ Done! Projects found: {len(projects)} → Saved to {OUTPUT_FILE}")
