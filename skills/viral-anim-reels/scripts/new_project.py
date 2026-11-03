"""Create a new Reel project folder from templates.

  python -I new_project.py <slug> [--case 14] [--series "Small Print"] [--root C:\\dev\\viral-reels]

Creates <root>/<slug>/ with script.json, package.json, brief.md and folders
shots/ audio/ music/ build/ qa/. Also ensures <root>/ideas_log.csv and metrics.csv exist.
"""
import argparse, csv, datetime, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SKILL, ROOT_DEFAULT, load, save

ap = argparse.ArgumentParser()
ap.add_argument("slug")
ap.add_argument("--case", type=int, default=None)
ap.add_argument("--series", default="")
ap.add_argument("--lang", default="en", choices=["en", "tr"])
ap.add_argument("--root", default=ROOT_DEFAULT)
a = ap.parse_args()

root = os.path.abspath(a.root)
d = os.path.join(root, a.slug)
if os.path.exists(os.path.join(d, "script.json")):
    sys.exit(f"already exists: {d}")
for sub in ["shots", "audio", "music", "build", "qa"]:
    os.makedirs(os.path.join(d, sub), exist_ok=True)

log = os.path.join(root, "ideas_log.csv")
if not os.path.exists(log):
    csv.writer(open(log, "w", newline="", encoding="utf-8")).writerow(
        ["date", "case_no", "slug", "series", "title", "archetype", "hook_type", "fact_flag", "status"])
met = os.path.join(root, "metrics.csv")
if not os.path.exists(met):
    shutil.copy(os.path.join(SKILL, "templates", "metrics.template.csv"), met)

case = a.case
if case is None:  # next free case number
    rows = list(csv.DictReader(open(log, encoding="utf-8")))
    case = max([int(r["case_no"]) for r in rows if r.get("case_no", "").isdigit()] + [0]) + 1

s = load(os.path.join(SKILL, "templates", "script.template.json"))
s.update(slug=a.slug, case_no=case, series=a.series, lang=a.lang)
save(os.path.join(d, "script.json"), s)
p = load(os.path.join(SKILL, "templates", "package.template.json"))
p.update(case_no=case, series=a.series)
save(os.path.join(d, "package.json"), p)
open(os.path.join(d, "brief.md"), "w", encoding="utf-8").write(
    f"# {a.slug} — Case #{case:03d}\n\nCreated {datetime.date.today()}\n\n## Idea + rubric score\n\n## Research notes (2 sources per claim)\n\n")
csv.writer(open(log, "a", newline="", encoding="utf-8")).writerow(
    [datetime.date.today(), case, a.slug, a.series, "", "", "", "", "draft"])
print(d)
