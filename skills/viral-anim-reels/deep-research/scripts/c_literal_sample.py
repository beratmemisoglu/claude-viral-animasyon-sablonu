"""Sample 40 spoken content words (2 per core Ricks video) and grab the frame shown
0.3 s after word onset, for manual literal-visualisation coding.
Usage: python -I c_literal_sample.py <research_root>"""
import sys, os, json, glob, random, subprocess
from PIL import Image, ImageDraw
ROOT = sys.argv[1]; OUT = os.path.join(ROOT, 'analysis', 'scripts', 'out')
STOP = set("the a an and or but of to in on at for with by from is was were be been are it its this that these those he she they them his her their you your we our i me my as so if then than there here what who why how when where which not no just only also very all any one into out up down over after before about would could should every even still because said says said thing things something really never always".split())
vids = []
for d in glob.glob(os.path.join(ROOT, 'videos', 'ricksclips', '*')):
    m = json.load(open(os.path.join(d, 'meta.json'), encoding='utf8'))
    if m['upload_date'] >= '20261007': vids.append((m['upload_date'], d, m))
vids.sort(); random.seed(7)
sel = []
for _, d, m in vids[-20:]:
    sp = [p for p in glob.glob(os.path.join(d, '*.json3'))]
    if not sp: continue
    js = json.load(open(sp[0], encoding='utf8'))
    ws = []
    for ev in js['events']:
        for s in ev.get('segs', []) or []:
            w = s.get('utf8', '').strip().strip('.,!?"\'').lower()
            if w and w not in STOP and len(w) >= 4 and not w.endswith('ly') and not w.endswith('ing') and not w.endswith('ed'):
                ws.append(((ev['tStartMs'] + s.get('tOffsetMs', 0)) / 1000, w))
    for t, w in random.sample(ws, 2):
        sel.append((os.path.basename(d), m['view_count'], t, w))
tiles = []
for vid, v, t, w in sel:
    p = os.path.join(OUT, f'lit_{vid}_{t:.1f}.png')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t + 0.3), '-i', os.path.join(ROOT, 'videos', 'ricksclips', vid, 'video.mp4'), '-frames:v', '1', '-vf', 'scale=216:384', p])
    tiles.append((vid, v, t, w, p))
json.dump(sel, open(os.path.join(OUT, 'c_literal_sample.json'), 'w'), indent=1)
for k in range(4):
    im = Image.new('RGB', (216 * 5, 404 * 2), 'black'); dr = ImageDraw.Draw(im)
    for j, (vid, v, t, w, p) in enumerate(tiles[k * 10:(k + 1) * 10]):
        x, y = (j % 5) * 216, (j // 5) * 404
        im.paste(Image.open(p), (x, y + 20)); dr.rectangle((x, y, x + 215, y + 19), fill='black')
        dr.text((x + 3, y + 3), f'{k*10+j+1}. "{w}" {t:.1f}s', fill='yellow')
    im.save(os.path.join(OUT, f'c_literal_{k+1}.png'))
for i, s in enumerate(sel): print(i + 1, s)
