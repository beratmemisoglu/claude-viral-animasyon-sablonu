"""make_thumbnail.py — templates/thumbnail.svg → 1280x720 PNG (+ 320x180 telefon önizlemesi).

  python make_thumbnail.py --text "1.204 YALAN" --layout A --label 1.204 --label-tone bad --expr shocked --bg street --out thumbs/x-A.png
                           [--sub "herkes görüyor"] [--base-image C:/.../higgsfield.png] [--no-text] [--engine edge|resvg]

SVG→PNG motoru: bu makinede cairosvg/resvg/rsvg-convert/ImageMagick YOK, ffmpeg'de svg decoder YOK (kontrol edildi
2026-10-28). other-self-thumbnail/generator/render.py ile aynı kanıtlanmış yol: headless Microsoft Edge screenshot.
Alternatif: `npm i -g @resvg/resvg-js` sonra --engine resvg (fontu sisteme kurmak gerekir).
Karakter: StickFigure.tsx ile aynı rig geometrisi (Python'da yeniden çizilir; thumbnail'da kafa 4x büyük).
"""
import sys
for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass

import argparse, math, os, shutil, subprocess, sys, tempfile, urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
TPL = HERE.parent / 'templates' / 'thumbnail.svg'
EDGE = os.environ.get('THUMB_BROWSER') or (r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' if os.name == 'nt'
                                           else shutil.which('google-chrome') or shutil.which('chromium') or 'chrome')
TONES = {'good': '#2EB872', 'bad': '#E03E3E', 'neutral': '#6B7280', 'accent': '#2F6BFF', 'gold': '#F2B705'}
BG = {
    'street': {'sky': ('#CFE8FF', '#F4EFE6'), 'ground': '#8C8C8C', 'scene': ''.join(
        f'<rect x="{-40 + i * 150}" y="{520 - (180 + (i * 37) % 300)}" width="{90 + (i * 53) % 120}" height="{180 + (i * 37) % 300}" fill="{"#B9B1A3" if i % 2 else "#D9D2C5"}"/>' for i in range(10))},
    'office': {'sky': ('#EFE7D8', '#E6DCC8'), 'ground': '#D8D1C4', 'scene': ''.join(f'<rect x="{x}" y="120" width="220" height="180" rx="6" fill="#CFE8FF" stroke="#5A5A66" stroke-width="4"/>' for x in (80, 500, 920))},
    'home': {'sky': ('#F3E6D3', '#EAD8BE'), 'ground': '#C9A77C', 'scene': '<rect x="840" y="110" width="300" height="240" rx="8" fill="#CFE8FF" stroke="#5A5A66" stroke-width="5"/><rect x="380" y="430" width="360" height="70" rx="16" fill="#5B7FA6"/>'},
    'night': {'sky': ('#0F1220', '#2A2F4A'), 'ground': '#3A3D47', 'scene': ''.join(f'<circle cx="{(i * 97) % 1280}" cy="{(i * 61) % 300}" r="2" fill="#fff"/>' for i in range(40))},
}


def stick(expr: str, scale: float, face_big=True, color='#1E1E24', scarf='#FF6B35', pose='shock') -> str:
    """StickFigure.tsx rig'inin thumbnail sürümü: kafa büyük, kollar yukarı/işaret. (0,0) = ayak zemini."""
    headR, headY, neckY, hipY = (52 if face_big else 26), -150, -122, -80
    def limb(sx, sy, a1, a2, l1, l2):
        j = (sx + math.sin(math.radians(a1)) * l1, sy + math.cos(math.radians(a1)) * l1)
        e = (j[0] + math.sin(math.radians(a1 + a2)) * l2, j[1] + math.cos(math.radians(a1 + a2)) * l2)
        return f'M {sx:.1f} {sy:.1f} L {j[0]:.1f} {j[1]:.1f} L {e[0]:.1f} {e[1]:.1f}'
    arms = {'shock': ((150, 20), (-150, -20)), 'point': ((95, 0), (-8, 6)), 'slump': ((12, 4), (-10, 3))}[pose]
    st = f'fill="none" stroke="{color}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"'
    face = {
        'shocked': '<circle cx="-16" cy="-6" r="7"/><circle cx="16" cy="-6" r="7"/><path d="M -12 -26 L 0 -24 M 12 -26 L 0 -24" stroke-width="5" fill="none" stroke="INK"/><ellipse cx="0" cy="18" rx="9" ry="12"/>',
        'happy': '<circle cx="-16" cy="-6" r="5"/><circle cx="16" cy="-6" r="5"/><path d="M -18 12 Q 0 30 18 12" stroke-width="5" fill="none" stroke="INK"/>',
        'sad': '<circle cx="-16" cy="-4" r="5"/><circle cx="16" cy="-4" r="5"/><path d="M -16 -20 L -4 -14 M 16 -20 L 4 -14 M -14 22 Q 0 10 14 22" stroke-width="5" fill="none" stroke="INK"/>',
        'angry': '<circle cx="-16" cy="-4" r="5"/><circle cx="16" cy="-4" r="5"/><path d="M -20 -20 L -6 -12 M 20 -20 L 6 -12 M -14 20 Q 0 12 14 20" stroke-width="5" fill="none" stroke="INK"/>',
        'worried': '<circle cx="-16" cy="-4" r="5"/><circle cx="16" cy="-4" r="5"/><path d="M -18 -18 L -6 -12 M 18 -18 L 6 -12 M -12 18 Q -6 14 0 18 Q 6 22 12 18" stroke-width="5" fill="none" stroke="INK"/>',
    }.get(expr, '<circle cx="-16" cy="-6" r="5"/><circle cx="16" cy="-6" r="5"/><path d="M -10 18 L 10 18" stroke-width="5" fill="none" stroke="INK"/>').replace('INK', color)
    return (f'<g transform="scale({scale})">'
            f'<g opacity="0.55"><path d="{limb(0, neckY, *arms[1], 34, 32)}" {st}/><path d="{limb(0, hipY, -6, 0, 40, 40)}" {st}/></g>'
            f'<path d="M 0 {hipY} L 0 {neckY}" {st}/><path d="M -12 {neckY + 3} L 12 {neckY + 3}" stroke="{scarf}" stroke-width="12" stroke-linecap="round"/>'
            f'<path d="{limb(0, hipY, 6, 0, 40, 40)}" {st}/><path d="{limb(0, neckY, *arms[0], 34, 32)}" {st}/>'
            f'<g transform="translate(0 {headY - (headR - 26)})"><circle r="{headR}" fill="#FFFFFF" stroke="{color}" stroke-width="6"/><g fill="{color}">{face}</g></g></g>')


def build_svg(a) -> str:
    bg = BG.get(a.bg, BG['street'])
    tone = TONES.get(a.label_tone, TONES['bad'])
    tr_upper = lambda t: t.replace('i', 'İ').replace('ı', 'I').upper()  # Türkçe büyük harf (Python upper: i→I yanlış)
    text = '' if a.no_text else tr_upper(a.text)
    lines = text.split('\n') if '\n' in text else ([text] if len(text) <= 14 else [' '.join(text.split()[:len(text.split()) // 2]), ' '.join(text.split()[len(text.split()) // 2:])])
    fs = 150 if max((len(l) for l in lines), default=1) <= 9 else 118 if max(len(l) for l in lines) <= 13 else 92
    L = a.layout.upper()
    v = {'SKY0': bg['sky'][0], 'SKY1': bg['sky'][1], 'GROUND': bg['ground'], 'BG_SCENE': bg['scene'], 'FLOOR': 520, 'FLOOR_H': 200,
         'BG_OPACITY': '0' if a.base_image else '1', 'BASE_IMAGE': '', 'CROWD': '', 'SUB': '' if a.no_text else (a.sub or ''), 'SUB_COLOR': tone, 'SUB_Y': fs * 0.75 + 20,
         'LABEL': a.label, 'LABEL_COLOR': tone}
    if a.base_image:
        p = Path(a.base_image).resolve()
        v['BASE_IMAGE'] = f'<image href="{p.as_uri()}" width="1280" height="720" preserveAspectRatio="xMidYMid slice"/>'
    lw = max(220, len(a.label) * 62 + 70)
    v.update({'LABEL_W': lw, 'LABEL_W2': lw // 2, 'LABEL_FS': 96 if len(a.label) <= 6 else 72})
    if L == 'A':  # karakter sol, etiket kafa üstü büyük, yazı sağ blok
        v.update({'HERO': stick(a.expr, 1.0, pose='shock'), 'HERO_X': 330, 'HERO_Y': 640, 'HERO_S': 2.3,
                  'LABEL_X': 330, 'LABEL_Y': 130, 'TEXT_X': 1220, 'TEXT_Y': 300, 'TEXT_ANCHOR': 'end'})
    elif L == 'B':  # kalabalık gri + kahraman ortada + tek kırmızı etiket
        crowd = ''.join(f'<g transform="translate({120 + i * 135} {560 + (i % 3) * 30}) scale({1.1 + (i % 3) * 0.15})">{stick("neutral", 1.0, face_big=False, color="#6B7280", scarf="#6B7280", pose="slump")}</g>' for i in range(9) if i not in (4,))
        v.update({'CROWD': crowd, 'HERO': stick(a.expr, 1.0, pose='point'), 'HERO_X': 660, 'HERO_Y': 660, 'HERO_S': 2.0,
                  'LABEL_X': 660, 'LABEL_Y': 170, 'TEXT_X': 640, 'TEXT_Y': 640 + 40, 'TEXT_ANCHOR': 'middle'})
        v['BG_OPACITY'] = '0.6' if not a.base_image else '0'
    else:  # C: yakın yüz, yazı üstte
        v.update({'HERO': stick(a.expr, 1.0, pose='shock'), 'HERO_X': 820, 'HERO_Y': 1000, 'HERO_S': 3.6,
                  'LABEL_X': 300, 'LABEL_Y': 430, 'TEXT_X': 640, 'TEXT_Y': 150, 'TEXT_ANCHOR': 'middle'})
    v['TEXT_FS'] = fs
    v['TEXT_LINES'] = ''.join(f'<tspan x="0" dy="{0 if i == 0 else fs * 1.02}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    svg = TPL.read_text(encoding='utf-8')
    for k, val in v.items():
        svg = svg.replace('{{' + k + '}}', str(val))
    return svg


def esc(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def render(svg_path: Path, png: Path, engine: str):
    if engine == 'resvg':
        subprocess.run(['resvg', '-w', '1280', str(svg_path), str(png)], check=True); return
    html = svg_path.with_suffix('.html')
    html.write_text('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#000;overflow:hidden}svg{display:block}</style></head><body>'
                    + svg_path.read_text(encoding='utf-8') + '</body></html>', encoding='utf-8')
    # Edge headless bazen süreç dönmeden önce PNG'yi yazmaz (başka Edge açıkken) → dosyayı bekle, gerekirse eski headless ile tekrar dene
    import time
    png.unlink(missing_ok=True)
    for mode in ('--headless=new', '--headless'):
        subprocess.run([EDGE, mode, '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', '--window-size=1280,720',
                        '--virtual-time-budget=8000', '--allow-file-access-from-files', f'--screenshot={png}', html.resolve().as_uri()], check=False, capture_output=True, timeout=120)
        for _ in range(60):
            if png.exists() and png.stat().st_size > 1000:
                return
            time.sleep(0.25)
    raise RuntimeError(f'Edge PNG üretmedi: {png} (THUMB_BROWSER ile başka Chrome/Edge yolu ver veya --engine resvg)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--text', required=True); ap.add_argument('--sub', default='')
    ap.add_argument('--layout', default='A', choices=['A', 'B', 'C', 'a', 'b', 'c'])
    ap.add_argument('--label', default='?'); ap.add_argument('--label-tone', default='bad', choices=list(TONES))
    ap.add_argument('--expr', default='shocked'); ap.add_argument('--bg', default='street', choices=list(BG))
    ap.add_argument('--base-image'); ap.add_argument('--no-text', action='store_true')
    ap.add_argument('--out', required=True); ap.add_argument('--engine', default='edge', choices=['edge', 'resvg'])
    ap.add_argument('--keep-svg', action='store_true')
    a = ap.parse_args()
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    svg = build_svg(a)
    svg_path = out.with_suffix('.svg')
    svg_path.write_text(svg, encoding='utf-8')
    render(svg_path, out, a.engine)
    try:
        from PIL import Image
        im = Image.open(out).convert('RGB')
        if im.size != (1280, 720):
            im = im.crop((0, 0, 1280, 720))
            im.save(out)
        im.resize((320, 180), Image.LANCZOS).save(out.with_name(out.stem + '_320.png'))
    except ImportError:
        print('Pillow yok; 320 önizleme atlandı')
    if not a.keep_svg:
        svg_path.with_suffix('.html').unlink(missing_ok=True)
    print('ok', out, '(+ _320 önizleme). Kaynak SVG:', svg_path)


if __name__ == '__main__':
    sys.exit(main())
