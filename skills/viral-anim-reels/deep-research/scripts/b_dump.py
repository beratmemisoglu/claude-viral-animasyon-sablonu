"""B: dump word-level transcripts -> analysis/scripts/out/words_<ch>_<id>.json + plain text with [s] markers per sentence."""
import json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'analysis', 'scripts', 'out'); os.makedirs(OUT, exist_ok=True)

def words(path):
    d = json.load(open(path, encoding='utf8'))
    w = []
    for ev in d.get('events', []):
        t0 = ev.get('tStartMs', 0)
        for s in ev.get('segs', []) or []:
            txt = s.get('utf8', '').strip()
            if not txt: continue
            w.append((round((t0 + s.get('tOffsetMs', 0)) / 1000, 2), txt))
    return w

def sentences(w):
    out, cur, st = [], [], None
    for t, x in w:
        if x.startswith('[') and x.endswith(']'): continue
        if st is None: st = t
        cur.append(x)
        if re.search(r'[.?!]["\u201d]?$', x):
            out.append((st, ' '.join(cur))); cur, st = [], None
    if cur: out.append((st, ' '.join(cur)))
    return out

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    allm = {}
    for ch in ('ricksclips', 'competitors'):
        base = os.path.join(ROOT, 'videos', ch)
        for vid in sorted(os.listdir(base)):
            p = os.path.join(base, vid)
            f = next((os.path.join(p, n) for n in ('video.en-orig.json3', 'subs.en-orig.json3', 'subs.en.json3') if os.path.exists(os.path.join(p, n))), None)
            meta = json.load(open(os.path.join(p, 'meta.json'), encoding='utf8'))
            w = words(f) if f else []
            allm[vid] = dict(ch=ch, title=meta['title'], views=meta['view_count'], dur=meta['duration'], date=meta['upload_date'], channel=meta.get('channel'), src=os.path.basename(f) if f else None)
            json.dump(w, open(os.path.join(OUT, f'words_{vid}.json'), 'w', encoding='utf8'))
            with open(os.path.join(OUT, f'sent_{vid}.txt'), 'w', encoding='utf8') as fh:
                for st, s in sentences(w): fh.write(f'[{st:5.1f}] {s}\n')
    json.dump(allm, open(os.path.join(OUT, 'index.json'), 'w', encoding='utf8'), indent=1)
    for k, v in sorted(allm.items(), key=lambda kv: (kv[1]['ch'], kv[1]['date'])):
        print(v['ch'][:4], k, v['date'], v['views'], v['dur'], v['src'], v['channel'], '|', v['title'])
