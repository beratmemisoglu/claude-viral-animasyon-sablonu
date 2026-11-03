#!/usr/bin/env python3
"""Toon Studio'nun render motoruna ait parçalarını SENİN lisanslı kurulumundan doldurur.

Bu repo sadece Toon Studio'nun kendi kodunu (studio.py, appcore/*.cjs), skill'leri ve dmscales stilini içerir.
Motorun ana kodu, stil motorları (templates/) ve node_modules yayınlanmaz: üçüncü tarafa aittir. Bu betik onları
senin kurulumundan kopyalar, motorun veri klasörlerini bağlar ve studio.json ile .mcp.json dosyalarını yazar.

  python setup_from_app.py --app "<kurulumun resources klasörü>" --data "<kurulumun veri klasörü>" [--workspace D:\\ToonStudio-Projects]

--app: app.asar ve templates/ klasörünün olduğu resources klasörü. --data: ayarların (config.json) olduğu veri klasörü.
Gerekenler: kurulu (ve en az bir kez açılmış) motor, Node.js >= 22 (npx), Python 3.10+, Google Chrome.
Tekrar çalıştırmak güvenlidir: kopyalanan motor dosyalarını yeniler, appdata/config.json dosyanı korur.
"""
import argparse, json, os, platform, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
WIN = platform.system() == 'Windows'
for s in (sys.stdout, sys.stderr):                                # Türkçe mesajlar Windows konsolunda da yazılsın
    try: s.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass


def find_app(arg):
    if os.path.isfile(os.path.join(arg, 'app.asar')): return arg
    sys.exit(f"{arg} içinde app.asar yok: --app <resources klasörü> ver (app.asar'ın olduğu klasör).")


def link(target, at):
    """`at` konumunda `target` klasörüne giden bağlantı (Windows'ta junction: yönetici izni gerekmez)."""
    if not os.path.isdir(target): return False
    if os.path.lexists(at):
        if os.path.islink(at) or (WIN and os.path.isdir(at) and not os.listdir(at)): os.rmdir(at) if WIN else os.unlink(at)
        else: return True                                        # orada gerçek bir klasör var: koru
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
    ap = argparse.ArgumentParser(description='Render motorunun parçalarını kendi kurulumundan kopyalar.')
    ap.add_argument('--app', required=True, help="kurulumun resources klasörü (app.asar'ın olduğu)")
    ap.add_argument('--data', required=True, help='kurulumun veri klasörü (config.json, flow-chrome, speech, blender)')
    ap.add_argument('--workspace', default=os.path.join(os.path.expanduser('~'), 'ToonStudio-Projects'),
                    help='projelerin tutulacağı çalışma alanı')
    a = ap.parse_args()
    res = find_app(a.app)
    npx = shutil.which('npx') or sys.exit('Node.js (npx) gerekli: https://nodejs.org')

    print(f'1/4 motor kodu: {os.path.join(res, "app.asar")}')
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, 'app')
        subprocess.run([npx, '--yes', '@electron/asar', 'extract', os.path.join(res, 'app.asar'), out], check=True, shell=WIN)
        os.makedirs(os.path.join(ROOT, 'appcore', 'main'), exist_ok=True)
        shutil.copy2(os.path.join(out, 'out', 'main', 'index.js'), os.path.join(ROOT, 'appcore', 'main', 'index.js'))
        for d in ('node_modules', 'pipeline-scripts'):
            shutil.rmtree(os.path.join(ROOT, 'appcore', d), ignore_errors=True)
            shutil.copytree(os.path.join(out, d), os.path.join(ROOT, 'appcore', d))

    print("2/4 stil motorları ve skill'leri (templates/)")
    shutil.copytree(os.path.join(res, 'templates'), os.path.join(ROOT, 'templates'), dirs_exist_ok=True)

    print('3/4 veri: ayarlar, Flow profili, konuşma modelleri, Blender')
    ad, ud = os.path.join(ROOT, 'appdata'), a.data
    os.makedirs(ad, exist_ok=True)
    if not os.path.exists(os.path.join(ad, 'config.json')) and os.path.isfile(os.path.join(ud, 'config.json')):
        shutil.copy2(os.path.join(ud, 'config.json'), os.path.join(ad, 'config.json'))   # ses / müzik / Claude ayarların
    for d in ('flow-chrome', 'speech'): link(os.path.join(ud, d), os.path.join(ad, d))
    link(os.path.join(ROOT, 'templates', 'blender'), os.path.join(ad, 'blender', 'blender'))
    if not link(os.path.join(ud, 'blender', '5.2.3'), os.path.join(ad, 'blender', '5.2.3')):
        print('    Blender 5.2.3 veri klasöründe yok (blender/5.2.3): Blender stilleri için onu oraya kur, '
              'sonra bu betiği tekrar çalıştır.')

    print('4/4 studio.json ve .mcp.json')
    cfg = {'python': sys.executable, 'chrome': chrome(), 'workspace': a.workspace}
    with open(os.path.join(ROOT, 'studio.json'), 'w', encoding='utf-8') as f: json.dump(cfg, f, indent=1)
    mcp = {'mcpServers': {'suite': {'type': 'stdio', 'command': 'node', 'args': [os.path.join(ROOT, 'appcore', 'mcp.cjs')]}}}
    with open(os.path.join(ROOT, '.mcp.json'), 'w', encoding='utf-8') as f: json.dump(mcp, f, indent=2)
    if not cfg['chrome']: print('    Google Chrome bulunamadı: studio.json içinde "chrome" yolunu ayarla.')
    print('\nHazır. Dene:  python studio.py styles')


if __name__ == '__main__':
    main()
