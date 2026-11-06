#!/usr/bin/env python3
"""Veri klasörünü ve çevre ayarlarını bağlar.

Render motoru (appcore/main/index.js), node_modules ve templates/ repoda bulunur.
Bu betik sadece kullanıcıya özgü veri klasörlerini (Flow profili, konuşma modelleri, Blender) bağlar
ve studio.json ile .mcp.json dosyalarını yazar.

  python setup_from_app.py --data "<kurulumun veri klasörü>" [--workspace D:\\ToonStudio-Projects]

--data: config.json, flow-chrome, speech ve blender klasörlerinin olduğu veri klasörü.
Gerekenler: Python 3.10+, Google Chrome.
Tekrar çalıştırmak güvenlidir: studio.json ve .mcp.json güncellenir, appdata/config.json korunur.
"""
import argparse, json, os, platform, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
WIN = platform.system() == 'Windows'
for s in (sys.stdout, sys.stderr):
    try: s.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass


def link(target, at):
    """`at` konumunda `target` klasörüne giden bağlantı (Windows'ta junction: yönetici izni gerekmez)."""
    if not os.path.isdir(target): return False
    if os.path.lexists(at):
        if os.path.islink(at) or (WIN and os.path.isdir(at) and not os.listdir(at)): os.rmdir(at) if WIN else os.unlink(at)
        else: return True
    os.makedirs(os.path.dirname(at), exist_ok=True)
    if WIN: subprocess.run(['cmd', '/c', 'mklink', '/J', at, target], check=True, stdout=subprocess.DEVNULL)
    else: os.symlink(target, at)
    return True


def chrome():
    c = [os.path.join(os.environ.get(v, ''), 'Google', 'Chrome', 'Application', 'chrome.exe')
         for v in ('PROGRAMFILES', 'PROGRAMFILES(X86)', 'LOCALAPPDATA')] if WIN else \
        ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', shutil.which('google-chrome') or '', shutil.which('chromium') or '']
    return next((p for p in c if p and os.path.isfile(p)), '')


def main():
    ap = argparse.ArgumentParser(description='Veri klasörünü bağlar, studio.json ve .mcp.json yazar.')
    ap.add_argument('--data', required=True, help='veri klasörü (config.json, flow-chrome, speech, blender)')
    ap.add_argument('--workspace', default=os.path.join(os.path.expanduser('~'), 'ToonStudio-Projects'),
                    help='projelerin tutulacağı çalışma alanı')
    a = ap.parse_args()
    ud = a.data

    print('1/2 veri: ayarlar, Flow profili, konuşma modelleri, Blender')
    ad = os.path.join(ROOT, 'appdata')
    os.makedirs(ad, exist_ok=True)
    if not os.path.exists(os.path.join(ad, 'config.json')) and os.path.isfile(os.path.join(ud, 'config.json')):
        shutil.copy2(os.path.join(ud, 'config.json'), os.path.join(ad, 'config.json'))
    for d in ('flow-chrome', 'speech'): link(os.path.join(ud, d), os.path.join(ad, d))
    link(os.path.join(ROOT, 'templates', 'blender'), os.path.join(ad, 'blender', 'blender'))
    if not link(os.path.join(ud, 'blender', '5.2.3'), os.path.join(ad, 'blender', '5.2.3')):
        print('    Blender 5.2.3 veri klasöründe yok (blender/5.2.3): Blender stilleri için onu oraya kur, '
              'sonra bu betiği tekrar çalıştır.')

    print('2/2 studio.json ve .mcp.json')
    cfg = {'python': sys.executable, 'chrome': chrome(), 'workspace': a.workspace}
    with open(os.path.join(ROOT, 'studio.json'), 'w', encoding='utf-8') as f: json.dump(cfg, f, indent=1)
    mcp = {'mcpServers': {'suite': {'type': 'stdio', 'command': 'node', 'args': [os.path.join(ROOT, 'appcore', 'mcp.cjs')]}}}
    with open(os.path.join(ROOT, '.mcp.json'), 'w', encoding='utf-8') as f: json.dump(mcp, f, indent=2)
    if not cfg['chrome']: print('    Google Chrome bulunamadı: studio.json içinde "chrome" yolunu ayarla.')
    print('\nHazır. Dene:  python studio.py styles')


if __name__ == '__main__':
    main()
