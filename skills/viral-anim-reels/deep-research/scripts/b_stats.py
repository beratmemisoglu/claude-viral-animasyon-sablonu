"""B: per-video script stats. Requires b_dump.py output (analysis/scripts/out).
Manual annotations (TWIST/EXPLAIN seconds, END type, LOOP) come from reading sent_<id>.txt.
Run: python -I analysis/scripts/b_stats.py"""
import json, os, re, sys, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'analysis', 'scripts', 'out')
idx = json.load(open(os.path.join(OUT, 'index.json'), encoding='utf8'))
# vid: (twist_s, explain_s, end_type, loop)
# loop: 'seamless' (cut mid-sentence -> flows into line 1), 'callback' (echoes opening image/words), 'no'
ANN = {
 'WbRdDyaPuAU': (21.1, 37.0, 'soru (seçim)', 'callback'),
 'eSRnuL-fVSE': (44.1, 47.5, 'soru (seçim)', 'no'),
 'uRkLhDrKQeU': (54.5, 19.6, 'espri/ders', 'callback'),
 'PL-Yro2meY4': (13.2, 23.0, 'punchline', 'callback'),
 'TgyHSIttwdM': (35.2, 24.4, 'seamless kesik', 'seamless'),
 'hdhggSABEws': (28.5, 31.8, 'açıklama', 'no'),
 'CJwgTrfrHL0': (23.2, 17.9, 'açıklama', 'no'),
 'eQR3pgMiUF0': (26.8, 30.3, 'punchline', 'callback'),
 'PLe2Gu3FDuA': (29.1, 32.9, 'punchline (sonuç)', 'no'),
 '_sUAXTvJquk': (25.5, 25.5, 'açıklama', 'no'),
 'jpFJ8Z_F-qU': (29.7, 36.7, 'punchline', 'callback'),
 'VS1Z_Q-Klt8': (45.8, 48.5, 'punchline (mekanizma)', 'no'),
 'lnYLIWP2l-I': (37.1, None, 'bilgi (seviye)', 'no'),
 'nzbkkEZFM8g': (47.8, 50.8, 'punchline', 'callback'),
 '0m6G8pDtzNs': (42.2, 49.1, 'ahlak/sonuç', 'no'),
 'VKsamN3Fk4U': (37.5, 43.6, 'açıklama', 'no'),
 'GM9UKnZ6JFw': (36.9, 36.9, 'punchline (ikinci twist)', 'no'),
 'DEe0iKH4KIw': (39.2, 31.6, 'sonuç', 'no'),
 't3OXkhlI6NQ': (70.6, None, 'dram (trajik)', 'callback'),
 'LC8hYwUZ-kU': (31.0, 36.4, 'açıklama', 'no'),
 'ZDy3xXA2iHk': (57.7, None, 'cliffhanger/döngü', 'callback'),
 '5WMQhPObNqQ': (34.6, 45.2, 'punchline', 'no'),
 'mSJCcf5Robg': (21.8, None, 'soru', 'no'), 'fHhJ8jJ2pU0': (22.2, None, 'soru', 'no'),
 'JpC3f1cYYnM': (18.5, None, 'punchline', 'no'), 'NCl7daUhvsM': (39.3, 7.3, 'punchline', 'no'),
 'aVeX3-5K33Q': (44.4, 22.1, 'sonuç', 'no'), 'B5fQLSLsXCw': (71.1, 63.8, 'punchline', 'no'),
 'Rzu4ZNnaTb8': (18.6, 23.1, 'açıklama', 'no'), 'JsmBio-bQkg': (27.4, 13.5, 'açıklama', 'no'),
 'lWz9YjJ7H4E': (37.7, 6.7, 'seamless kesik', 'seamless'), 'WMF3reQPqfk': (17.7, 17.7, 'açıklama', 'no'),
 'S0sf_K08twQ': (16.1, 16.1, 'açıklama', 'no'), 'pY_bADpW_aw': (21.1, 21.1, 'açıklama', 'no'),
 'rv6qAgdPsXw': (20.6, 23.6, 'punchline (genelleme)', 'callback'), 'vxnnsMcoCMs': (20.5, 23.0, 'punchline (paradoks)', 'callback'),
 'fM-_0tJG8Eo': (42.9, 44.2, 'punchline (görsel)', 'no'),
}
PIV = ['but', 'yet', 'except', 'instead', 'wait', 'so', 'turns out', 'you see', 'then']
CORE_EXCLUDE = {'LUGcyIwlcto', 'Ta_XWO7d0ec', 'RVnC1DSfK30', '_pmioleoeAE'}
STOP = set('a an the and of to in on is it was he she you your i his her that this for with but so if be would at by from they we there'.split())


def load(vid):
    w = [(t, x) for t, x in json.load(open(os.path.join(OUT, f'words_{vid}.json'), encoding='utf8'))
         if not (x.startswith('[') or x.startswith('>>'))]
    sents = []
    for l in open(os.path.join(OUT, f'sent_{vid}.txt'), encoding='utf8'):
        if l.strip():
            sents.append((float(l[1:6]), l[8:].rstrip('\n')))
    return w, sents


rows = []
for vid, m in idx.items():
    w, sents = load(vid)
    if not w:
        continue
    words = [x for _, x in w]
    span = w[-1][0] - w[0][0] + 0.4
    dur = m['dur']
    toks = [(t, re.sub(r"[^a-z']", '', x.lower())) for t, x in w]
    piv = {}
    for p in PIV:
        p1 = p.split(); ts = []
        for i, (t, x) in enumerate(toks):
            nxt = toks[i + 1][1] if i + 1 < len(toks) else ''
            if (len(p1) == 1 and x == p1[0]) or (len(p1) == 2 and x == p1[0] and nxt == p1[1]):
                ts.append(t)
        piv[p] = ts
    nq = sum(1 for _, s in sents if '?' in s)
    sl = [len(s.split()) for _, s in sents]
    tw, ex, endt, loop = ANN.get(vid, (None, None, '?', '?'))
    rev = ex if ex is not None else tw
    cut = not re.search(r'[.?!]["”]?$', sents[-1][1].strip())
    fw = set(re.findall(r"[a-z']+", sents[0][1].lower())); lw = set(re.findall(r"[a-z']+", sents[-1][1].lower()))
    rows.append(dict(vid=vid, ch=m['channel'], title=m['title'], views=m['views'], date=m['date'], dur=dur, words=len(words),
        wpm_dur=round(len(words) / dur * 60), wpm_speech=round(len(words) / span * 60), nsent=len(sents),
        avg_sent=round(st.mean(sl), 1), max_sent=max(sl), nq=nq, piv=piv,
        piv_total=sum(len(v) for k, v in piv.items() if k != 'then'),
        twist=tw, explain=ex, rev_pct=round(rev / dur * 100) if rev is not None else None,
        twist_pct=round(tw / dur * 100) if tw is not None else None,
        end=endt, loop=loop, cut_end=cut, overlap=sorted((fw & lw) - STOP), tail_gap=round(dur - w[-1][0], 1),
        first=sents[0][1], last=sents[-1][1], first_len=len(sents[0][1].split()),
        core=(m['ch'] == 'ricksclips' and vid not in CORE_EXCLUDE)))
json.dump(rows, open(os.path.join(OUT, 'stats.json'), 'w', encoding='utf8'), indent=1, ensure_ascii=False)


def show(sel, label):
    print(f'\n## {label}')
    for r in sorted(sel, key=lambda r: -r['views']):
        pv = '; '.join(f"{k}:{len(v)}@" + ','.join(f'{t:.0f}' for t in v) for k, v in r['piv'].items() if v and k != 'then')
        print(f"{r['vid']}|{r['views']/1e6:.2f}M|{r['dur']}s|{r['words']}w|{r['wpm_dur']}/{r['wpm_speech']}wpm|{r['nsent']}s avg{r['avg_sent']} max{r['max_sent']}|q{r['nq']}|then{len(r['piv']['then'])}|pivT{r['piv_total']} [{pv}]|tw{r['twist_pct']}% rev{r['rev_pct']}%|{r['end']}|{r['loop']} cut={r['cut_end']} ov={r['overlap']}|gap{r['tail_gap']}|h{r['first_len']}")


def agg(sel, label):
    f = lambda k: round(st.median([r[k] for r in sel if r[k] is not None]), 1)
    print(label, 'n', len(sel), 'medViews', round(st.median([r['views'] for r in sel]) / 1e6, 2), 'meanViews', round(st.mean([r['views'] for r in sel]) / 1e6, 2),
          'dur', f('dur'), 'words', f('words'), 'wpm', f('wpm_speech'), 'avgSent', f('avg_sent'), 'hookLen', f('first_len'), 'q', f('nq'), 'piv', f('piv_total'),
          'twist%', f('twist_pct'), 'rev%', f('rev_pct'),
          'pivPerMin', round(st.median([r['piv_total'] / r['dur'] * 60 for r in sel]), 1),
          'youseeN', sum(1 for r in sel if r['piv']['you see']), 'withQ', sum(1 for r in sel if r['nq']),
          'loopN', sum(1 for r in sel if r['loop'] != 'no'), 'quoteN', sum(1 for r in sel if '"' in ' '.join(s for s in [r['first'], r['last']])))


if __name__ == '__main__':
    core = [r for r in rows if r['core']]
    show(core, 'Ricks core 22'); show([r for r in rows if r['ch'] != 'Ricks Clips'], 'competitors')
    print()
    hits = [r for r in core if r['views'] >= 5e6]; mid = [r for r in core if 1e6 < r['views'] < 5e6]; low = [r for r in core if r['views'] <= 1e6]
    agg(hits, 'HIT>=5M'); agg(mid, 'MID 1-5M'); agg(low, 'LOW<=1M'); agg(core, 'CORE'); agg([r for r in rows if r['ch'] != 'Ricks Clips'], 'COMP')
    # dialogue lines (quoted speech) per video
    print()
    for r in sorted(core, key=lambda r: -r['views']):
        _, s = load(r['vid'])
        nquote = sum(1 for _, x in s if '"' in x)
        print(f"{r['vid']} {r['views']/1e6:.2f}M quotes={nquote} you/your={sum(1 for _, x in load(r['vid'])[0] if re.sub(r'[^a-z]', '', x.lower()) in ('you', 'your', "youre", 'yours'))} he/she={sum(1 for _, x in load(r['vid'])[0] if re.sub(r'[^a-z]', '', x.lower()) in ('he', 'she', 'his', 'her', 'him'))}")
