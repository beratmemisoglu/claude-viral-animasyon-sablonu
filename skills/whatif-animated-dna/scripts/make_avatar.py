#!/usr/bin/env python3
"""make_avatar.py — "Görebilseydin" kanal profil resmi (SVG → PNG, headless Edge).

Karakter = videodaki kahraman (references/05 §10): krem yumurta kafa, koyu mor-gri kontur, turuncu atkı.
Kanal imzası: nane-turkuaz parlayan gözler (gizli sayıyı gören güç) + kafa üstü turkuaz etiket.
Palet: templates/remotion/theme.ts ile aynı.

Kullanım:
  python make_avatar.py --out <klasör> [--variants A,B,C] [--size 800]
Çıktı: avatar_<V>.png (800×800), avatar_<V>_circle_preview.png (çember maske + 48/98 px okunurluk önizlemesi)
  A: kafa üstünde "?" etiketi       (önerilen: 48 px'te en okunur)
  B: etiket yok, gözlerden turkuaz ışık halkası (en sade)
  C: kafa üstünde "+1" etiketi      (yalan/sayı ailesine gönderme)
"""
import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
EDGE = os.environ.get('THUMB_BROWSER') or r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

P = dict(sky_top='#3B2558', sky_bot='#D9894A', ink='#2A2433', skin='#F2E6D8', hero='#FF6B35',
         signal='#2EE6C5', rim='#FFC98A', vest='#5E3F73', navy='#141B33')


def svg(v: str, s: int = 800) -> str:
    c = s / 2
    # kafa: dikey elips (yumurta), merkez biraz aşağıda → üstte etiket için yer
    hx, hy, rx, ry = c, c + 40, 210, 240
    label = ''
    if v in ('A', 'C'):
        txt = '?' if v == 'A' else '+1'
        w = 150 if v == 'A' else 190
        ly = hy - ry - 105
        label = (f'<g filter="url(#glow)"><rect x="{c - w / 2}" y="{ly}" width="{w}" height="112" rx="30" fill="{P["signal"]}"/></g>'
                 f'<rect x="{c - w / 2}" y="{ly}" width="{w}" height="112" rx="30" fill="{P["signal"]}" stroke="{P["ink"]}" stroke-width="10"/>'
                 f'<path d="M {c - 22} {ly + 110} L {c} {ly + 140} L {c + 22} {ly + 110} Z" fill="{P["signal"]}" stroke="{P["ink"]}" stroke-width="10" stroke-linejoin="round"/>'
                 f'<rect x="{c - 24}" y="{ly + 100}" width="48" height="14" fill="{P["signal"]}"/>'
                 f'<text x="{c}" y="{ly + 88}" text-anchor="middle" font-family="Fredoka, \'Segoe UI\', Arial, sans-serif" font-weight="700" font-size="92" fill="{P["ink"]}">{txt}</text>')
    halo = ''
    if v == 'B':
        halo = (f'<circle cx="{hx - 78}" cy="{hy - 20}" r="86" fill="{P["signal"]}" opacity="0.22" filter="url(#blur)"/>'
                f'<circle cx="{hx + 78}" cy="{hy - 20}" r="86" fill="{P["signal"]}" opacity="0.22" filter="url(#blur)"/>')

    def eye(x, y):
        return (f'<circle cx="{x}" cy="{y}" r="46" fill="{P["signal"]}" filter="url(#glow)" opacity="0.9"/>'
                f'<circle cx="{x}" cy="{y}" r="40" fill="{P["signal"]}" stroke="{P["ink"]}" stroke-width="9"/>'
                f'<circle cx="{x + 6}" cy="{y + 4}" r="17" fill="{P["ink"]}"/>'
                f'<circle cx="{x - 10}" cy="{y - 12}" r="8" fill="#FFFFFF"/>')

    face = (eye(hx - 78, hy - 20) + eye(hx + 78, hy - 20) +
            # "biliyorum" yarım gülüş: sağ köşe yukarı
            f'<path d="M {hx - 60} {hy + 92} Q {hx + 5} {hy + 118} {hx + 70} {hy + 72}" stroke="{P["ink"]}" stroke-width="14" fill="none" stroke-linecap="round"/>'
            # sağ kaş hafif kalkık (smug), sol düz
            f'<path d="M {hx - 120} {hy - 92} L {hx - 40} {hy - 96}" stroke="{P["ink"]}" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="M {hx + 40} {hy - 104} Q {hx + 80} {hy - 122} {hx + 120} {hy - 108}" stroke="{P["ink"]}" stroke-width="13" fill="none" stroke-linecap="round"/>')
    body = (  # yelek omuzları + atkı (kadraj altında kesilir)
        f'<path d="M {c - 300} {s + 20} Q {c - 280} {hy + ry - 10} {c} {hy + ry - 20} Q {c + 280} {hy + ry - 10} {c + 300} {s + 20} Z" fill="{P["vest"]}" stroke="{P["ink"]}" stroke-width="12"/>'
        f'<path d="M {c - 190} {hy + ry - 40} Q {c} {hy + ry + 40} {c + 190} {hy + ry - 40} L {c + 175} {hy + ry + 25} Q {c} {hy + ry + 100} {c - 175} {hy + ry + 25} Z" fill="{P["hero"]}" stroke="{P["ink"]}" stroke-width="12" stroke-linejoin="round"/>'
        f'<path d="M {c + 95} {hy + ry + 40} L {c + 140} {s + 20} L {c + 60} {s + 20} L {c + 50} {hy + ry + 55} Z" fill="{P["hero"]}" stroke="{P["ink"]}" stroke-width="12" stroke-linejoin="round"/>')
    head = (f'<ellipse cx="{hx + 10}" cy="{hy + 8}" rx="{rx}" ry="{ry}" fill="{P["rim"]}" opacity="0.55"/>'  # amber rim ışığı
            f'<ellipse cx="{hx}" cy="{hy}" rx="{rx}" ry="{ry}" fill="{P["skin"]}" stroke="{P["ink"]}" stroke-width="14"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 {s} {s}">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P["sky_top"]}"/><stop offset="1" stop-color="{P["sky_bot"]}"/></linearGradient>
  <radialGradient id="vig" cx="0.5" cy="0.45" r="0.7"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.35"/></radialGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>
</defs>
<rect width="{s}" height="{s}" fill="url(#bg)"/>
<rect width="{s}" height="{s}" fill="url(#vig)"/>
{halo}{body}{head}{face}{label}
</svg>'''


def render(svg_text: str, png: Path, size: int):
    html = png.with_suffix('.html')
    html.write_text('<!doctype html><html><head><meta charset="utf-8">'
                    '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@700&display=block" rel="stylesheet">'
                    '<style>html,body{margin:0;overflow:hidden}svg{display:block}</style></head><body>' + svg_text + '</body></html>', encoding='utf-8')
    png.unlink(missing_ok=True)
    for mode in ('--headless=new', '--headless'):
        subprocess.run([EDGE, mode, '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', f'--window-size={size},{size}',
                        '--virtual-time-budget=8000', f'--screenshot={png}', html.resolve().as_uri()], check=False, capture_output=True, timeout=120)
        for _ in range(60):
            if png.exists() and png.stat().st_size > 1000:
                return
            time.sleep(0.25)
    raise RuntimeError(f'Edge PNG üretmedi: {png}')


def preview(png: Path, out: Path):
    """YouTube çember kırpması + gerçek boyut önizlemesi (98 px kanal sayfası, 48 px yorum/öneri)."""
    from PIL import Image, ImageDraw
    im = Image.open(png).convert('RGBA')
    n = im.size[0]
    mask = Image.new('L', (n, n), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, n - 1, n - 1), fill=255)
    circ = Image.new('RGBA', (n, n), (0, 0, 0, 0)); circ.paste(im, (0, 0), mask)
    sheet = Image.new('RGBA', (n + 260, n), (255, 255, 255, 255))
    sheet.paste(circ, (0, 0), circ)
    for px, y in ((98, 40), (48, 420)):  # açık ve koyu zemin üstünde gerçek boyut
        small = circ.resize((px, px), Image.LANCZOS)
        sheet.paste(small, (n + 60, y), small)
        dark = Image.new('RGBA', (px + 20, px + 20), (24, 24, 24, 255)); dark.paste(small, (10, 10), small)
        sheet.paste(dark, (n + 50, y + px + 40))
    sheet.convert('RGB').save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--variants', default='A,B,C')
    ap.add_argument('--size', type=int, default=800)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    for v in a.variants.split(','):
        s = svg(v, a.size)
        (out / f'avatar_{v}.svg').write_text(s, encoding='utf-8')
        png = out / f'avatar_{v}.png'
        render(s, png, a.size)
        preview(png, out / f'avatar_{v}_circle_preview.png')
        print('OK', png)


if __name__ == '__main__':
    main()
