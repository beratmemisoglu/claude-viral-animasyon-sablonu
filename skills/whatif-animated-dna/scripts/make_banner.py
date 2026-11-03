#!/usr/bin/env python3
"""make_banner.py — "Görebilseydin" YouTube kanal banner'ı (2560×1440, SVG → PNG, headless Edge).

YouTube ölçüleri (2026 itibarıyla geçerli resmi şablon):
  tam görsel / TV ........ 2560×1440
  masaüstü (max) ......... 2560×423, dikey ortada (y 508–931)
  tablet ................. 1855×423, ortada
  GÜVENLİ ALAN (her cihaz) 1546×423, ortada (x 507–2053, y 508–931)  ← logo + yazı yalnız burada
Dosya ≤ 6 MB.

Kullanım: python make_banner.py --out <klasör> [--slogan "..."]
Çıktı: banner.png (yüklenecek), banner_guides.png (güvenli alan çizgili), banner_crop_{mobile,tablet,desktop}.png
"""
import argparse
import os
import random
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from make_avatar import EDGE, P as _P  # noqa: E402

P = {**_P, 'bad': '#FF4D5E'}  # tehlike/azalış (templates/remotion/theme.ts ile aynı)

sys.stdout.reconfigure(encoding='utf-8')
W, H = 2560, 1440
SAFE = (507, 508, 2053, 931)        # x0, y0, x1, y1
TABLET = (352, 508, 2207, 931)
DESK = (0, 508, 2560, 931)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def figure(x, floor, sc, label=None, tone=None, hero=False):
    """Videodaki çöp adamın sade hali (kafa elips, gövde çizgi, atkı yalnız kahramanda)."""
    ink = P['ink']
    head_r, body = 26 * sc, 70 * sc
    hy = floor - body - 60 * sc - head_r
    g = [f'<g stroke="{ink}" stroke-width="{7 * sc:.1f}" stroke-linecap="round" fill="none">',
         f'<path d="M {x} {floor - 60 * sc} L {x - 14 * sc} {floor} M {x} {floor - 60 * sc} L {x + 16 * sc} {floor}"/>',
         f'<path d="M {x} {hy + head_r} L {x} {floor - 60 * sc}"/>',
         f'<path d="M {x} {hy + head_r + 18 * sc} L {x - 24 * sc} {hy + head_r + 62 * sc} M {x} {hy + head_r + 18 * sc} L {x + 24 * sc} {hy + head_r + 60 * sc}"/>',
         '</g>']
    if hero:
        g.append(f'<path d="M {x - 16 * sc} {hy + head_r + 4 * sc} L {x + 16 * sc} {hy + head_r + 4 * sc}" stroke="{P["hero"]}" stroke-width="{10 * sc:.1f}" stroke-linecap="round"/>')
    g.append(f'<ellipse cx="{x}" cy="{hy}" rx="{head_r * 0.9:.1f}" ry="{head_r:.1f}" fill="{P["skin"]}" stroke="{ink}" stroke-width="{5 * sc:.1f}"/>')
    g.append(f'<circle cx="{x - 8 * sc}" cy="{hy - 2 * sc}" r="{3 * sc:.1f}" fill="{ink}"/><circle cx="{x + 8 * sc}" cy="{hy - 2 * sc}" r="{3 * sc:.1f}" fill="{ink}"/>')
    if label:
        fs = 26 * sc
        w = max(54 * sc, len(label) * fs * 0.66 + 26 * sc)
        ly = hy - head_r - 22 * sc - 40 * sc
        g.append(f'<rect x="{x - w / 2:.1f}" y="{ly:.1f}" width="{w:.1f}" height="{40 * sc:.1f}" rx="{12 * sc:.1f}" fill="{tone}"/>'
                 f'<text x="{x}" y="{ly + 29 * sc:.1f}" text-anchor="middle" font-family="Fredoka, Arial, sans-serif" font-weight="700" font-size="{fs:.1f}" fill="#FFFFFF">{esc(label)}</text>')
    return ''.join(g)


def svg(slogan: str) -> str:
    rnd = random.Random(7)
    # 1) gökyüzü + şehir silüeti (tüm genişlik; TV'de tamamı, masaüstünde bant görünür)
    sky = (f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
           f'<stop offset="0" stop-color="#2A1B42"/><stop offset="0.42" stop-color="{P["sky_top"]}"/>'
           f'<stop offset="0.72" stop-color="#9A5A5C"/><stop offset="1" stop-color="{P["sky_bot"]}"/></linearGradient>'
           f'<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="16"/></filter>'
           f'<radialGradient id="spot" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFC98A" stop-opacity="0.35"/><stop offset="1" stop-color="#FFC98A" stop-opacity="0"/></radialGradient>'
           f'</defs><rect width="{W}" height="{H}" fill="url(#sky)"/>')
    floor = 1010
    bld = []
    x = -40
    while x < W + 40:
        w = rnd.randint(110, 230); h = rnd.randint(260, 620)
        col = '#5E3F73' if rnd.random() > 0.5 else '#43305E'
        bld.append(f'<rect x="{x}" y="{floor - h}" width="{w}" height="{h}" fill="{col}"/>')
        for wy in range(floor - h + 30, floor - 40, 56):
            for wx in range(x + 18, x + w - 30, 44):
                if rnd.random() > 0.35:
                    bld.append(f'<rect x="{wx}" y="{wy}" width="20" height="26" rx="3" fill="#F2E6D8" opacity="{0.55 if rnd.random() > 0.3 else 0.9}"/>')
        x += w + rnd.randint(8, 30)
    ground = f'<rect x="0" y="{floor}" width="{W}" height="{H - floor}" fill="#2E2840"/><rect x="0" y="{floor}" width="{W}" height="10" fill="#CDBFA8" opacity="0.8"/>'
    # 2) kalabalık: güvenli alanın DIŞINDA (sol ve sağ kanat); etiketler kanalın motifi
    crowd = []
    # Kısa etiketler + boy sırayla küçük/büyük → etiketler dikeyde ayrışır, üst üste binmez.
    # Kanat sınırı: etiketin yarı genişliği dahil hiçbir öğe güvenli alana (x 507–2053) girmez.
    left = [(75, 1.85, '9.317', P['bad']), (190, 1.35, '41', '#2B2730'), (300, 1.85, '0', P['signal']), (405, 1.35, '1.204', P['bad'])]
    right = [(2160, 1.35, '88', '#2B2730'), (2270, 1.85, '?', P['signal']), (2380, 1.35, '512', P['bad']), (2490, 1.85, '3', P['signal'])]
    for cx, sc, lab, tone in left + right:
        crowd.append(figure(cx, floor, sc, lab, tone))
    # 3) güvenli alan içeriği: kahraman kafası (avatarla aynı) + yazı
    hx, hy, rx, ry = 700, 748, 110, 127  # etiket tepesi y≈553 → güvenli alan üstünden 45 px pay
    spot = f'<ellipse cx="1280" cy="720" rx="900" ry="260" fill="url(#spot)"/>'
    panel = f'<rect x="{SAFE[0] + 20}" y="{SAFE[1] + 28}" width="{SAFE[2] - SAFE[0] - 40}" height="{SAFE[3] - SAFE[1] - 56}" rx="44" fill="#141B33" opacity="0.72"/>'

    def eye(x, y, r):
        return (f'<circle cx="{x}" cy="{y}" r="{r + 6}" fill="{P["signal"]}" filter="url(#glow)" opacity="0.9"/>'
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="{P["signal"]}" stroke="{P["ink"]}" stroke-width="6"/>'
                f'<circle cx="{x + 4}" cy="{y + 2}" r="{r * 0.42:.1f}" fill="{P["ink"]}"/><circle cx="{x - 6}" cy="{y - 7}" r="5" fill="#FFF"/>')
    hero = (f'<ellipse cx="{hx + 6}" cy="{hy + 5}" rx="{rx}" ry="{ry}" fill="{P["rim"]}" opacity="0.55"/>'
            f'<ellipse cx="{hx}" cy="{hy}" rx="{rx}" ry="{ry}" fill="{P["skin"]}" stroke="{P["ink"]}" stroke-width="9"/>'
            + eye(hx - 44, hy - 12, 23) + eye(hx + 44, hy - 12, 23) +
            f'<path d="M {hx - 34} {hy + 52} Q {hx + 3} {hy + 67} {hx + 40} {hy + 41}" stroke="{P["ink"]}" stroke-width="8" fill="none" stroke-linecap="round"/>'
            f'<path d="M {hx - 68} {hy - 52} L {hx - 22} {hy - 55}" stroke="{P["ink"]}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M {hx + 22} {hy - 60} Q {hx + 45} {hy - 70} {hx + 68} {hy - 62}" stroke="{P["ink"]}" stroke-width="8" fill="none" stroke-linecap="round"/>')
    tag_y = hy - ry - 78
    tag = (f'<rect x="{hx - 46}" y="{tag_y}" width="92" height="66" rx="18" fill="{P["signal"]}" filter="url(#glow)"/>'
           f'<rect x="{hx - 46}" y="{tag_y}" width="92" height="66" rx="18" fill="{P["signal"]}" stroke="{P["ink"]}" stroke-width="6"/>'
           f'<path d="M {hx - 13} {tag_y + 64} L {hx} {tag_y + 82} L {hx + 13} {tag_y + 64} Z" fill="{P["signal"]}" stroke="{P["ink"]}" stroke-width="6" stroke-linejoin="round"/>'
           f'<rect x="{hx - 15}" y="{tag_y + 58}" width="30" height="9" fill="{P["signal"]}"/>'
           f'<text x="{hx}" y="{tag_y + 53}" text-anchor="middle" font-family="Fredoka, Arial, sans-serif" font-weight="700" font-size="56" fill="{P["ink"]}">?</text>')
    tx = 880
    title = (f'<text x="{tx}" y="738" font-family="Fredoka, Arial, sans-serif" font-weight="700" font-size="158" '
             f'fill="{P["skin"]}" stroke="{P["ink"]}" stroke-width="14" paint-order="stroke" letter-spacing="1">Görebilseydin</text>')
    sub = (f'<text x="{tx + 6}" y="826" font-family="Fredoka, Arial, sans-serif" font-weight="600" font-size="54" fill="{P["signal"]}">{esc(slogan)}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            + sky + ''.join(bld) + ground + spot + ''.join(crowd) + panel + hero + tag + title + sub + '</svg>')


def render(svg_text: str, png: Path):
    html = png.with_suffix('.html')
    html.write_text('<!doctype html><html><head><meta charset="utf-8">'
                    '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&display=block" rel="stylesheet">'
                    '<style>html,body{margin:0;overflow:hidden}svg{display:block}</style></head><body>' + svg_text + '</body></html>', encoding='utf-8')
    png.unlink(missing_ok=True)
    for mode in ('--headless=new', '--headless'):
        subprocess.run([EDGE, mode, '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', f'--window-size={W},{H}',
                        '--virtual-time-budget=8000', f'--screenshot={png}', html.resolve().as_uri()], check=False, capture_output=True, timeout=180)
        for _ in range(80):
            if png.exists() and png.stat().st_size > 1000:
                html.unlink(missing_ok=True)
                return
            time.sleep(0.25)
    raise RuntimeError(f'Edge PNG üretmedi: {png}')


def outputs(png: Path, out: Path):
    from PIL import Image, ImageDraw
    im = Image.open(png).convert('RGB')
    g = im.copy(); d = ImageDraw.Draw(g)
    for box, col, name in ((DESK, (255, 255, 0), 'DESKTOP 2560x423'), (TABLET, (0, 200, 255), 'TABLET 1855x423'), (SAFE, (255, 60, 60), 'SAFE AREA 1546x423')):
        d.rectangle(box, outline=col, width=6); d.text((box[0] + 14, box[1] + 10), name, fill=col)
    g.save(out / 'banner_guides.png')
    for name, box in (('mobile', SAFE), ('tablet', TABLET), ('desktop', DESK)):
        im.crop(box).save(out / f'banner_crop_{name}.png')
    im.save(out / 'banner.png', optimize=True)
    print('banner.png', round(os.path.getsize(out / 'banner.png') / 1024), 'KB (sınır 6144 KB)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--slogan', default='Ya herkesin gizli sayısını görebilseydin?')
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    s = svg(a.slogan)
    (out / 'banner.svg').write_text(s, encoding='utf-8')
    raw = out / 'banner_raw.png'
    render(s, raw)
    outputs(raw, out)
    raw.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
