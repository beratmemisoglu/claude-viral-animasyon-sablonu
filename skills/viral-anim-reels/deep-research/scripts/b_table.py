"""B: print markdown stats table from out/stats.json"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
rows = json.load(open(os.path.join(OUT, 'stats.json'), encoding='utf8'))
LOOP = {'seamless': 'EVET (kesik cümle)', 'callback': 'kısmi (geri çağrı)', 'no': 'hayır'}
def tbl(sel):
    print('| # | Video | İzlenme | Süre | Kelime | K/dk | Ort. cümle | Soru | Pivot (adet @ sn) | Twist % | Açıklama/cevap % | Döngü | Son satır tipi |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for i, r in enumerate(sorted(sel, key=lambda r: -r['views']), 1):
        p = r['piv']
        parts = []
        for k in ('but', 'yet', 'except', 'instead', 'wait', 'so', 'turns out', 'you see'):
            if p[k]: parts.append(f"{k} {len(p[k])}@" + ','.join(f'{t:.0f}' for t in p[k]))
        v = r['views']; vs = f'{v/1e6:.1f}M' if v >= 1e6 else f'{v/1e3:.0f}K'
        print(f"| {i} | {r['title']} (`{r['vid']}`) | {vs} | {r['dur']} sn | {r['words']} | {r['wpm_speech']} | {r['avg_sent']} | {r['nq']} | {'; '.join(parts)} (Σ{r['piv_total']}) | {r['twist_pct'] if r['twist_pct'] is not None else '–'} | {r['rev_pct'] if r['rev_pct'] is not None else '–'} | {LOOP[r['loop']]} | {r['end']} |")
tbl([r for r in rows if r['core']]); print(); tbl([r for r in rows if r['ch'] != 'Ricks Clips'])
