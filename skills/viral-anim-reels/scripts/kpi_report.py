"""KPI report from <root>/metrics.csv against the 90-day phase targets (references/06 §4).

  python -I kpi_report.py [--root C:\\dev\\viral-reels] [--phase 1|2|3]

Per Reel: skip %, avg watch %, sends/reach %, likes/reach %, follows per 1K reach, verdict vs phase targets.
Then winners by series and hook type, and the pop candidates (to double down within 24-72 h).
"""
import argparse, csv, os, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT_DEFAULT

T = {1: dict(skip=55, watch=45, sends=0.5, likes=3, f1k=2), 2: dict(skip=45, watch=55, sends=1.0, likes=3, f1k=4),
     3: dict(skip=40, watch=60, sends=1.5, likes=3, f1k=5)}
ap = argparse.ArgumentParser()
ap.add_argument("--root", default=ROOT_DEFAULT)
ap.add_argument("--phase", type=int, default=None)
a = ap.parse_args()
path = os.path.join(a.root, "metrics.csv")
rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r.get("reach")]
if not rows:
    sys.exit(f"no rows with reach in {path}")
phase = a.phase or (1 if len(rows) <= 14 else 2 if len(rows) <= 40 else 3)
t = T[phase]

def num(r, k):
    try:
        return float(r.get(k) or 0)
    except ValueError:
        return 0.0

out = []
for r in rows:
    reach = max(num(r, "reach"), 1)
    m = dict(case=r["case_no"], slug=r["slug"], series=r["series"], hook=r["hook_type"], views=num(r, "views"),
             skip=num(r, "skip_rate_pct"), watch=num(r, "avg_watch_pct"), sends=num(r, "sends") / reach * 100,
             likes=num(r, "likes") / reach * 100, f1k=num(r, "follows") / reach * 1000, trial=r.get("is_trial") == "1")
    m["ok"] = sum([m["skip"] <= t["skip"], m["watch"] >= t["watch"], m["sends"] >= t["sends"], m["likes"] >= t["likes"], m["f1k"] >= t["f1k"]])
    out.append(m)

print(f"Phase {phase} targets: skip<={t['skip']}% · watch>={t['watch']}% · sends/reach>={t['sends']}% · likes/reach>={t['likes']}% · follows/1K>={t['f1k']}\n")
print(f"{'case':>4} {'slug':28} {'views':>9} {'skip':>5} {'watch':>5} {'send%':>6} {'like%':>6} {'f/1K':>5}  hit")
for m in sorted(out, key=lambda x: -x["views"]):
    print(f"{m['case']:>4} {m['slug'][:28]:28} {m['views']:>9.0f} {m['skip']:>5.0f} {m['watch']:>5.0f} {m['sends']:>6.2f} {m['likes']:>6.2f} {m['f1k']:>5.1f}  {m['ok']}/5{' (trial)' if m['trial'] else ''}")

def group(key):
    g = {}
    for m in out:
        g.setdefault(m[key] or "-", []).append(m)
    print(f"\nby {key}:")
    for k, v in sorted(g.items(), key=lambda kv: -statistics.median(x["views"] for x in kv[1])):
        print(f"  {k:24} n={len(v):2}  median views {statistics.median(x['views'] for x in v):>9.0f}  median sends% {statistics.median(x['sends'] for x in v):.2f}  median f/1K {statistics.median(x['f1k'] for x in v):.1f}")
group("series"); group("hook")
med = statistics.median(x["views"] for x in out)
pops = [m for m in out if m["views"] >= 3 * med or m["sends"] >= 2]
print("\nPOP candidates (>=3x median views or sends/reach >=2%): " + (", ".join(f"#{m['case']} {m['slug']}" for m in pops) or "none"))
print("-> run the 24-72 h protocol (references/06 §5): Part 2 + 2 sibling topics as Trial Reels.")
