"""Competitor scan for The Other Self (YouTube Data API v3, OAuth token of our channel; read-only calls).

  ~/the-other-self/.venv-yt/bin/python competitor_scan.py [--date YYYY-MM-DD] [--no-thumbs]

Writes (under ~/the-other-self/project/competitors/):
  data/<date>.json            raw snapshot (every recent video of every competitor + our channel)
  <date>.md                   metrics report for the agent
  thumbs/<date>/*.jpg         top thumbnails (analysis only — never feed them to an image generator)
Metrics: views/day since upload, 24h view gain vs the previous snapshot (velocity), outlier score = views / channel
median of the last uploads, engagement, duration bucket (short <= 60 s, long), upload cadence, title patterns.
"""
import argparse, datetime as dt, json, re, statistics, sys, urllib.request
from collections import Counter
from pathlib import Path

HOME = Path.home()
ROOT = HOME / 'the-other-self'
sys.path.insert(0, str(ROOT / 'studio' / 'scripts' / 'youtube'))
from yt_common import youtube  # noqa: E402

SKILL = Path(__file__).resolve().parents[1]
CFG = json.loads((SKILL / 'competitors.json').read_text(encoding='utf-8'))
OUT = ROOT / 'project' / 'competitors'

ap = argparse.ArgumentParser()
ap.add_argument('--date', default=dt.date.today().isoformat())
ap.add_argument('--no-thumbs', action='store_true')
a = ap.parse_args()
NOW = dt.datetime.now(dt.timezone.utc)


def iso_dur(s):
    m = re.match(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', s or '')
    if not m: return 0
    d, h, mi, se = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


yt = youtube()


def channel(handle=None, cid=None):
    kw = {'forHandle': handle} if handle else {'id': cid}
    r = yt.channels().list(part='snippet,statistics,contentDetails', **kw).execute()
    return (r.get('items') or [None])[0]


def recent_videos(ch, n):
    up = ch['contentDetails']['relatedPlaylists']['uploads']
    ids, tok = [], None
    while len(ids) < n:
        r = yt.playlistItems().list(part='contentDetails', playlistId=up, maxResults=min(50, n - len(ids)), pageToken=tok).execute()
        ids += [i['contentDetails']['videoId'] for i in r.get('items', [])]
        tok = r.get('nextPageToken')
        if not tok: break
    vids = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part='snippet,statistics,contentDetails', id=','.join(ids[i:i + 50])).execute()
        for v in r.get('items', []):
            st, sn = v.get('statistics', {}), v['snippet']
            pub = dt.datetime.fromisoformat(sn['publishedAt'].replace('Z', '+00:00'))
            age = max((NOW - pub).total_seconds() / 86400, 0.05)
            views = int(st.get('viewCount', 0))
            thumbs = sn.get('thumbnails', {})
            vids.append({
                'id': v['id'], 'title': sn['title'], 'published': sn['publishedAt'], 'age_days': round(age, 2),
                'views': views, 'likes': int(st.get('likeCount', 0)), 'comments': int(st.get('commentCount', 0)),
                'duration_s': iso_dur(v['contentDetails'].get('duration')), 'views_per_day': round(views / age, 1),
                'tags': sn.get('tags', [])[:15], 'desc_head': (sn.get('description') or '')[:200],
                'thumb': (thumbs.get('maxres') or thumbs.get('high') or thumbs.get('medium') or {}).get('url'),
            })
    return vids


snap = {'date': a.date, 'taken_at': NOW.isoformat(), 'channels': []}
for c in CFG['competitors']:
    try:
        ch = channel(handle=c['handle'])
        if not ch:
            snap['channels'].append({'handle': c['handle'], 'error': 'not found'}); continue
        vids = recent_videos(ch, CFG.get('videos_per_channel', 50))
        snap['channels'].append({'handle': c['handle'], 'name': ch['snippet']['title'], 'id': ch['id'], 'main': c.get('main', False),
                                 'subs': int(ch['statistics'].get('subscriberCount', 0)), 'total_views': int(ch['statistics'].get('viewCount', 0)),
                                 'video_count': int(ch['statistics'].get('videoCount', 0)), 'videos': vids})
    except Exception as e:  # keep scanning the others
        snap['channels'].append({'handle': c['handle'], 'error': str(e)[:200]})
ours = channel(cid=CFG['our_channel_id'])
if ours:
    snap['ours'] = {'name': ours['snippet']['title'], 'subs': int(ours['statistics'].get('subscriberCount', 0)),
                    'videos': recent_videos(ours, 20)}

# ---------------------------------------------------------------- metrics vs previous snapshot
(OUT / 'data').mkdir(parents=True, exist_ok=True)
prev_files = sorted(p for p in (OUT / 'data').glob('*.json') if p.stem < a.date)
prev = json.loads(prev_files[-1].read_text()) if prev_files else None
prev_views = {}
if prev:
    for ch in prev.get('channels', []):
        for v in ch.get('videos', []): prev_views[v['id']] = (v['views'], prev['taken_at'])
rows = []
for ch in snap['channels']:
    vids = ch.get('videos') or []
    longs = [v for v in vids if v['duration_s'] > 60]
    med = statistics.median([v['views'] for v in longs]) if longs else 0
    ch['median_views_long'] = med
    for v in vids:
        v['outlier'] = round(v['views'] / med, 2) if med and v['duration_s'] > 60 else None
        if v['id'] in prev_views:
            pv, pt = prev_views[v['id']]
            hrs = max((NOW - dt.datetime.fromisoformat(pt)).total_seconds() / 3600, 1)
            v['gain_24h'] = round((v['views'] - pv) * 24 / hrs)
        v['engagement'] = round((v['likes'] + v['comments']) / v['views'] * 100, 2) if v['views'] else 0
        rows.append({**v, 'channel': ch.get('name', ch['handle']), 'subs': ch.get('subs', 0)})
(OUT / 'data' / f'{a.date}.json').write_text(json.dumps(snap, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- report
fmt = lambda n: f'{n:,}'.replace(',', '.')
mins = lambda s: f'{s // 60}:{s % 60:02d}'
L = [f'# Competitor radar — {a.date}', '', f'Snapshot: {NOW:%Y-%m-%d %H:%M} UTC · previous: {prev["date"] if prev else "none (velocity starts tomorrow)"}', '']
L += ['## Channels', '', '| Channel | Subs | Videos | Median views (long, last 50) | Uploads last 30 d | Shorts share | Avg long length |', '|---|---|---|---|---|---|---|']
for ch in snap['channels']:
    if ch.get('error'):
        L.append(f'| {ch["handle"]} | ERROR: {ch["error"]} | | | | | |'); continue
    vids = ch['videos']; longs = [v for v in vids if v['duration_s'] > 60]
    last30 = sum(1 for v in vids if v['age_days'] <= 30)
    shorts = sum(1 for v in vids if v['duration_s'] <= 60)
    avg = int(statistics.mean([v['duration_s'] for v in longs])) if longs else 0
    L.append(f'| {ch["name"]}{" (MAIN)" if ch.get("main") else ""} | {fmt(ch["subs"])} | {ch["video_count"]} | {fmt(int(ch["median_views_long"]))} | {last30} | {shorts}/{len(vids)} | {mins(avg)} |')

def table(title, items, cols):
    out = ['', f'## {title}', '', '| ' + ' | '.join(c[0] for c in cols) + ' |', '|' + '---|' * len(cols)]
    for v in items:
        out.append('| ' + ' | '.join(str(c[1](v)) for c in cols) + ' |')
    return out

base_cols = [('Channel', lambda v: v['channel']), ('Title', lambda v: v['title'][:70]), ('Views', lambda v: fmt(v['views'])),
             ('Age d', lambda v: v['age_days']), ('Views/day', lambda v: fmt(int(v['views_per_day']))), ('Len', lambda v: mins(v['duration_s'])),
             ('Outlier×', lambda v: v['outlier'] if v['outlier'] is not None else '–'), ('Eng %', lambda v: v['engagement']), ('id', lambda v: v['id'])]
vel = [r for r in rows if r.get('gain_24h') is not None]
if vel:
    L += table('Fastest right now — views gained in the last 24 h', sorted(vel, key=lambda r: -r['gain_24h'])[:15],
               [('24h gain', lambda v: fmt(v['gain_24h']))] + base_cols)
L += table('Hot new uploads (≤ 14 days) by views/day', sorted([r for r in rows if r['age_days'] <= 14], key=lambda r: -r['views_per_day'])[:15], base_cols)
L += table('Outliers (long videos, last 50 per channel) — views ÷ channel median', sorted([r for r in rows if r.get('outlier')], key=lambda r: -r['outlier'])[:15], base_cols)
L += table('All-time leaders in the scanned window', sorted(rows, key=lambda r: -r['views'])[:10], base_cols)

words = Counter()
for r in rows:
    head = re.split(r'[|:\-–(]', r['title'])[0]
    for w in re.findall(r"[A-Za-z']{3,}", head.lower()):
        if w not in {'the', 'and', 'you', 'your', 'for', 'with', 'animated', 'short', 'film', 'animation', 'this', 'that', 'are', 'what', 'how', 'from'}:
            words[w] += r['views']
forms = Counter()
for r in rows:
    t = r['title']
    forms['ONE WORD | An Animated Short Film' if re.match(r'^[A-Z][A-Z\s]{2,20}\s*\|', t) else
          'question' if '?' in t else 'If … (hypothetical)' if t.lower().startswith('if ') else
          'When/How … (situation)' if re.match(r'^(when|how|why)\b', t.lower()) else 'other'] += 1
L += ['', '## Title signals', '', 'Top title words weighted by views: ' + ', '.join(f'{w} ({fmt(v)})' for w, v in words.most_common(25)),
      '', 'Title forms: ' + ', '.join(f'{k}: {v}' for k, v in forms.most_common())]
if snap.get('ours'):
    L += ['', '## Our channel', '', f'Subs: {snap["ours"]["subs"]}', '']
    for v in snap['ours']['videos'][:10]:
        L.append(f'- {v["title"]} — {fmt(v["views"])} views, {v["age_days"]} d, {fmt(int(v["views_per_day"]))}/day')
(OUT / f'{a.date}.md').write_text('\n'.join(L) + '\n', encoding='utf-8')

# ---------------------------------------------------------------- thumbnails of the winners (analysis only)
if not a.no_thumbs:
    td = OUT / 'thumbs' / a.date; td.mkdir(parents=True, exist_ok=True)
    pick = sorted(rows, key=lambda r: -(r.get('gain_24h') or r['views_per_day']))[:CFG.get('thumbs_to_download', 12)]
    for i, r in enumerate(pick):
        if r.get('thumb'):
            try:
                urllib.request.urlretrieve(r['thumb'], td / f'{i + 1:02d}_{r["id"]}.jpg')
            except Exception:
                pass
print('report:', OUT / f'{a.date}.md')
print('channels ok:', sum(1 for c in snap['channels'] if not c.get('error')), '/', len(snap['channels']), '| videos:', len(rows))
