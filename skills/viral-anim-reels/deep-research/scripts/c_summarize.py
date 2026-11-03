"""Summarise out/c_measure.json into tables. Usage: python -I c_summarize.py"""
import json, os, statistics as st
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'c_measure.json')))
V = D['videos']
def row(k, r):
    c = r['cls']; cam = c.get('zoom_in', 0) + c.get('zoom_out', 0) + c.get('pan_h', 0) + c.get('pan_v', 0)
    return f"{k} | {r['ch'][:12]} | {r['views']/1e6:.2f}M | {r['dur']} | cuts {r['cuts']} shot {r['shot_len']}s | chg {r['changes']} ({r['changes_per10']}/10s) chg40 {r['changes40']} | gap med {r['median_gap']} | cam {cam:.0f}% zin {c.get('zoom_in',0)} zout {c.get('zoom_out',0)} pan {c.get('pan_h',0)+c.get('pan_v',0):.0f} other {c.get('other_motion',0)} static {c.get('static',0)} | hold {r['hold_total']}s max {r['longest_hold']} | B {r['bri']} S {r['sat']} | align {r['align_content']} chance {r['align_content_chance']} | win {r['win']} | {r['title'][:40]}"
for k, r in sorted(V.items(), key=lambda x: (x[1]['ch'], -x[1]['views'])):
    print(row(k, r))
def agg(name, sel):
    rs = [V[k] for k in sel]
    f = lambda key: round(st.median([r[key] for r in rs]), 2)
    cam = st.median([sum(r['cls'].get(x, 0) for x in ('zoom_in','zoom_out','pan_h','pan_v')) for r in rs])
    oth = st.median([r['cls'].get('other_motion', 0) for r in rs]); sta = st.median([r['cls'].get('static', 0) for r in rs])
    al = [r['align_content'] for r in rs if r['align_content'] is not None]; ch = [r['align_content_chance'] for r in rs if r['align_content_chance'] is not None]
    print(f"\n## {name} n={len(rs)} dur {f('dur')} cuts {f('cuts')} shot_len {f('shot_len')} chg/10s {f('changes_per10')} chg40/10s {round(st.median([r['changes40']/r['dur']*10 for r in rs]),2)} median_gap {f('median_gap')} cam% {cam} other% {oth} static% {sta} holdtotal {f('hold_total')} bri {f('bri')} sat {f('sat')} align {round(st.median(al),2) if al else None} chance {round(st.median(ch),2) if ch else None}")
    # per-10s window curve (changes per window, first 6 windows)
    for w in range(7):
        xs = [r['win'][w] for r in rs if len(r['win']) > w and r['dur'] >= (w + 1) * 10]
        if xs: print(f"  win{w*10}-{w*10+10}s median {st.median(xs)} mean {round(st.mean(xs),1)} n={len(xs)}")
rk = [k for k, r in V.items() if r['ch'] == 'Ricks Clips' and r['date'] >= '20261007']
agg('Ricks core 22', rk)
agg('Ricks hits >=5M', [k for k in rk if V[k]['views'] >= 5e6])
agg('Ricks mid 1-5M', [k for k in rk if 1e6 < V[k]['views'] < 5e6])
agg('Ricks flops <=1M', [k for k in rk if V[k]['views'] <= 1e6])
agg('Ricks old', [k for k, r in V.items() if r['ch'] == 'Ricks Clips' and r['date'] < '20261007'])
for ch in sorted(set(r['ch'] for r in V.values()) - {'Ricks Clips'}):
    agg(ch, [k for k, r in V.items() if r['ch'] == ch])
# correlation views vs chg/10s in core
import math
xs = [math.log10(V[k]['views']) for k in rk]
for key in ('changes_per10', 'cuts', 'shot_len', 'sat', 'bri', 'dur'):
    ys = [V[k][key] for k in rk]
    mx, my = st.mean(xs), st.mean(ys)
    r = sum((a-mx)*(b-my) for a, b in zip(xs, ys)) / math.sqrt(sum((a-mx)**2 for a in xs) * sum((b-my)**2 for b in ys))
    print('corr log10(views) vs', key, round(r, 2))
print(json.dumps(D['palettes']))
