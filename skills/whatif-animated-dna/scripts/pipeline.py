"""pipeline.py — "What If" Türkçe animasyon videosu için kaldığı yerden devam edebilen stage runner.

  python pipeline.py <slug> [--from STAGE] [--only STAGE] [--to STAGE] [--dry-run] [--idea "Ya ... olsaydı?"]
                     [--root C:/dev/whatif-projects] [--studio C:/dev/the-other-self] [--llm "claude -p"] [--draft-only]
                     [--yt-python <python>] [--captions word|line|off]
  python pipeline.py <slug> --status

Stage'ler (sıra sabit):  idea | package | script | tts | shots | render | thumb | meta | upload
  LLM stage'leri (idea, package, script, shots, meta): çıktı dosyası yoksa prompt dosyası yazılır ve runner
  exit code 3 ile durur ("needs_llm") → Claude (orkestratör) dosyayı üretir → `pipeline.py <slug> --from <stage>`.
  `--llm "<komut>"` verilirse prompt stdin'den komuta verilir, stdout çıktı dosyasına yazılır (ör. `claude -p`).
  Deterministik stage'ler (tts, render, thumb, upload) doğrudan çalışır; her stage idempotenttir (çıktı varsa ve
  --from ile sıfırlanmadıysa atlanır). Durum: <root>/<slug>/state.json, log: <root>/<slug>/pipeline.log.

Proje klasörü: <root>/<slug>/
  idea.md · package.json · script.md + script.json · audio/*.mp3 · timeline.json · shots.json · props.json
  render/<slug>-draft.mp4 · render/<slug>.mp4 · qa/*.jpeg · thumbs/*.png · meta.json · description.txt · upload.json
Gizli değer yazdırılmaz. Higgsfield/NexLev MCP çağrıları bu dosyada YOK (Claude çağırır; bkz. E-pipeline.md).
"""
import sys
for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass

import argparse, datetime as dt, json, os, re, shutil, statistics, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
PROMPTS = SKILL / 'templates' / 'prompts'
STAGES = ['idea', 'package', 'script', 'tts', 'shots', 'render', 'thumb', 'meta', 'upload']
LLM_STAGES = {'idea': 'idea.md', 'package': 'package.json', 'script': 'script.json', 'shots': 'shots.json', 'meta': 'meta.json'}
EXIT_NEEDS_LLM = 3
IS_WIN = os.name == 'nt'
NPX = 'npx.cmd' if IS_WIN else 'npx'


def now():
    return dt.datetime.now().isoformat(timespec='seconds')


class Ctx:
    def __init__(self, a):
        self.a = a
        self.slug = a.slug
        self.root = Path(a.root)
        self.proj = self.root / a.slug
        self.proj.mkdir(parents=True, exist_ok=True)
        self.studio = Path(a.studio)
        self.state_path = self.proj / 'state.json'
        self.log_path = self.proj / 'pipeline.log'
        self.state = json.loads(self.state_path.read_text(encoding='utf-8')) if self.state_path.exists() else {'slug': a.slug, 'created': now(), 'stages': {}}

    def log(self, *m):
        line = f'[{now()}] ' + ' '.join(str(x) for x in m)
        print(line, flush=True)
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(line + '\n')

    def save(self):
        self.state['updated'] = now()
        self.state_path.write_text(json.dumps(self.state, ensure_ascii=False, indent=1), encoding='utf-8')

    def st(self, stage):
        return self.state['stages'].setdefault(stage, {'status': 'pending'})

    def p(self, rel):
        return self.proj / rel

    def read_json(self, rel):
        return json.loads(self.p(rel).read_text(encoding='utf-8-sig'))

    def run(self, cmd, cwd=None, check=True, env=None):
        self.log('$', ' '.join(str(c) for c in cmd), f'(cwd={cwd})' if cwd else '')
        if self.a.dry_run:
            return subprocess.CompletedProcess(cmd, 0, '', '')
        r = subprocess.run([str(c) for c in cmd], cwd=cwd, text=True, capture_output=True, encoding='utf-8', errors='replace', env=env)
        if r.stdout.strip():
            self.log(r.stdout.strip()[-3000:])
        if r.returncode != 0:
            self.log('STDERR:', r.stderr.strip()[-3000:])
            if check:
                raise RuntimeError(f'command failed ({r.returncode}): {cmd[0]}')
        return r


# ------------------------------------------------------------------ LLM stage helper
def fill_prompt(ctx: Ctx, stage: str) -> str:
    tpl = (PROMPTS / f'{stage}.md').read_text(encoding='utf-8')
    vals = {
        'slug': ctx.slug, 'idea': ctx.a.idea or '', 'today': dt.date.today().isoformat(),
        'idea_md': ctx.p('idea.md').read_text(encoding='utf-8') if ctx.p('idea.md').exists() else '',
        'package_json': ctx.p('package.json').read_text(encoding='utf-8') if ctx.p('package.json').exists() else '',
        'script_md': ctx.p('script.md').read_text(encoding='utf-8') if ctx.p('script.md').exists() else '',
        'script_json': ctx.p('script.json').read_text(encoding='utf-8') if ctx.p('script.json').exists() else '',
        'timeline_json': ctx.p('timeline.json').read_text(encoding='utf-8') if ctx.p('timeline.json').exists() else '',
        'shots_json': ctx.p('shots.json').read_text(encoding='utf-8') if ctx.p('shots.json').exists() else '',
        'schema_json': (HERE / 'shots_schema.json').read_text(encoding='utf-8'),
        'skill_dir': str(SKILL),
    }
    return re.sub(r'\{\{(\w+)\}\}', lambda m: vals.get(m.group(1), m.group(0)), tpl)


def llm_stage(ctx: Ctx, stage: str, validate):
    out = ctx.p(LLM_STAGES[stage])
    if out.exists():
        err = validate(ctx)
        if err:
            raise RuntimeError(f'{out.name} geçersiz: {err}')
        ctx.log(f'{stage}: {out.name} mevcut ve geçerli')
        return
    prompt = fill_prompt(ctx, stage)
    pf = ctx.p(f'prompts/{stage}.prompt.md'); pf.parent.mkdir(exist_ok=True)
    pf.write_text(prompt, encoding='utf-8')
    if ctx.a.llm and not ctx.a.dry_run:
        ctx.log(f'{stage}: LLM komutu çalıştırılıyor → {out.name}')
        r = subprocess.run(ctx.a.llm, input=prompt, shell=True, text=True, capture_output=True, encoding='utf-8', errors='replace')
        if r.returncode != 0:
            raise RuntimeError(f'LLM komutu hata: {r.stderr[-500:]}')
        txt = r.stdout.strip()
        m = re.search(r'```(?:json|markdown|md)?\s*(.*?)```', txt, re.S)
        if m and out.suffix == '.json':
            txt = m.group(1)
        out.write_text(txt, encoding='utf-8')
        err = validate(ctx)
        if err:
            raise RuntimeError(f'LLM çıktısı geçersiz: {err}')
        return
    ctx.st(stage).update({'status': 'needs_llm', 'prompt': str(pf), 'expects': str(out)})
    ctx.save()
    ctx.log(f'{stage}: NEEDS_LLM → prompt: {pf}\n   Claude bu promptu uygulayıp {out} dosyasını yazmalı, sonra: python pipeline.py {ctx.slug} --from {stage}')
    sys.exit(EXIT_NEEDS_LLM)


# ------------------------------------------------------------------ validators
def v_idea(ctx):
    t = ctx.p('idea.md').read_text(encoding='utf-8')
    return None if len(t.strip()) > 80 and 'Ya ' in t else 'idea.md kısa ya da "Ya ... olsaydı?" sorusu yok'


def v_package(ctx):
    j = ctx.read_json('package.json')
    need = ['title', 'title_alts', 'hook', 'thumb']
    miss = [k for k in need if k not in j]
    if miss:
        return f'eksik alan: {miss}'
    t = j['title'].strip()
    if not (15 <= len(t) <= 55):
        return f"title uzunluğu {len(t)} (15–55 olmalı; references/02 §5)"
    if len(t.split()) > 8:
        return f"title {len(t.split())} kelime (≤8 olmalı)"
    if not t.endswith('?'):
        return "title soru işaretiyle bitmeli"
    sc = (j.get('title_scores') or {}).get('main')
    if sc is not None and sc < 5:
        return f"ana başlık rubrik puanı {sc} (<5 → mutasyon kurallarıyla düzelt; references/02 §3–4)"
    th = j['thumb']
    if not th.get('text') or len(th['text'].split()) > 4:
        return 'thumb.text 1–4 kelime olmalı'
    # Türkçe küçültme: Python lower() "I"→"i" yapar; Türkçede "I"→"ı", "İ"→"i".
    def tr_words(s):
        s = s.replace('I', 'ı').replace('İ', 'i').lower()
        return [w[:5] for w in re.findall(r'[a-zçğıöşü0-9]+', s) if len(w) >= 3 and w not in ('ya', 'bir', 'her')]
    tw, tt = tr_words(th['text']), set(tr_words(t))
    if tw and sum(w in tt for w in tw) / len(tw) >= 0.6:
        return 'thumb.text başlığı tekrar ediyor (ikinci soru olmalı; references/03 §1)'
    if not j.get('contradiction'):
        return 'contradiction alanı yok (thumbnail çelişkisi; references/03)'
    return None


def v_script(ctx):
    j = ctx.read_json('script.json')
    segs = j.get('segments') or []
    if len(segs) < 20:
        return f'çok az segment ({len(segs)}); 8–10 dk için 60–120 vuruş beklenir'
    ids = [s.get('id') for s in segs]
    if len(set(ids)) != len(ids) or any(not re.match(r'^v\d{2,3}$', i or '') for i in ids):
        return 'segment id formatı v01.. ve benzersiz olmalı'
    words = sum(len(s['text'].split()) for s in segs)
    # Türkçe anlatım 135–155 kelime/dk (references/04 §6). İlk gerçek TTS'ten sonra ölçülen hızı
    # WHATIF_WPM env'ine yaz; tts stage ölçülen hızı loglar.
    wpm = float(os.environ.get('WHATIF_WPM', '145'))
    pauses = sum(float(s.get('pause_after', 0.35)) for s in segs) / 60
    est = words / wpm + pauses
    ctx.log(f'script: {len(segs)} segment, {words} kelime, {wpm:.0f} kelime/dk varsayımı ≈ {est:.1f} dk')
    if est > 11.0:
        return f'tahmini süre {est:.1f} dk > 11 dk tavanı (references/04 §10); vuruş kes'
    if not (7.5 <= est <= 10.5):
        ctx.log('UYARI: tahmini süre 8–10 dk hedefinin dışında')
    return None


def v_shots(ctx):
    j = ctx.read_json('shots.json')
    schema = json.loads((HERE / 'shots_schema.json').read_text(encoding='utf-8'))
    try:
        import jsonschema  # type: ignore
        jsonschema.validate(j, schema)
    except ImportError:
        ctx.log('not: jsonschema kurulu değil (pip install jsonschema) → yalnız yapısal kontrol')
    except Exception as e:  # noqa
        return f'schema: {str(e)[:300]}'
    shots = j['shots']
    t = 0.0; errs = []
    tl = ctx.read_json('timeline.json') if ctx.p('timeline.json').exists() else None
    seg_ids = {s['id'] for s in tl['segments']} if tl else set()
    for s in shots:
        if abs(s['t_start'] - t) > 0.02:
            errs.append(f"{s['id']}: t_start {s['t_start']} ≠ önceki bitiş {t:.2f}")
        t = s['t_start'] + s['dur']
        if tl and s.get('vo_segment') and s['vo_segment'] not in seg_ids:
            errs.append(f"{s['id']}: vo_segment {s['vo_segment']} timeline'da yok")
        if s['scene'] not in ('street', 'office', 'home', 'school', 'transit', 'wedding', 'infocard'):
            errs.append(f"{s['id']}: bilinmeyen sahne {s['scene']}")
        if s['scene'] == 'infocard' and not s.get('card'):
            errs.append(f"{s['id']}: infocard sahnesinde card yok")
        # references/05 §2 kural 7: 10 sn'den uzun planda en az bir değişim olmalı
        if s['dur'] > 10:
            moving = (s.get('camera') or {}).get('type', 'push') != 'static'
            changing = bool(s.get('overlay')) or any(c.get('label') or c.get('poseAt') or c.get('move') for c in s.get('characters') or [])
            if not (moving and changing):
                errs.append(f"{s['id']}: {s['dur']:.1f} sn plan ama kamera hareketi + etiket/overlay/poz değişimi yok")
    if tl and abs(t - tl['total_sec']) > 1.5:
        errs.append(f"toplam {t:.1f}s ≠ timeline {tl['total_sec']}s")

    # Ritim profili (references/05 §2, C raporu ölçümü): A hızlı hikâye, B anlatı. Video boyunca sabit.
    prof = j.get('profile', 'A')
    lim = {'A': {'cpm': (18, 26), 'med': (1.7, 3.0), 'hook15': (5, 8)},
           'B': {'cpm': (8, 13), 'med': (3.9, 5.5), 'hook15': (3, 6)}}[prof]
    durs = [s['dur'] for s in shots]
    med = statistics.median(durs); cpm = len(shots) / (t / 60) if t else 0
    hook15 = sum(1 for s in shots if 0 < s['t_start'] < 15)
    infocards = sum(1 for s in shots if s['scene'] == 'infocard')
    ctx.log(f'shots: profil {prof}, {len(shots)} shot, toplam {t:.1f}s, plan medyanı {med:.2f}s, {cpm:.1f} kesme/dk, '
            f'ilk 15 sn {hook15} kesme, {infocards} infografik kart '
            f'(hedef: {lim["cpm"][0]}–{lim["cpm"][1]}/dk, medyan {lim["med"][0]}–{lim["med"][1]} sn, ilk 15 sn {lim["hook15"][0]}–{lim["hook15"][1]})')
    # Sert sınırlar (flop kanıtı): >30 kesme/dk veya medyan <1,5 sn (Tesla flop); ilk 15 sn >10 kesme
    if cpm > 30 or med < 1.5:
        errs.append(f'aşırı hızlı kurgu: {cpm:.1f} kesme/dk, medyan {med:.2f} sn (sınır: ≤30/dk, medyan ≥1,5 sn)')
    if hook15 > 10:
        errs.append(f'ilk 15 sn {hook15} kesme (>10)')
    if not (lim['cpm'][0] * 0.85 <= cpm <= lim['cpm'][1] * 1.15):
        ctx.log(f'UYARI: kesme/dk profil {prof} aralığı dışında')
    if t >= 240 and infocards < max(3, int(t / 120)):
        ctx.log(f'UYARI: {infocards} infografik kart; her 60–120 sn\'de bir önerilir (references/05 §4)')
    return '; '.join(errs[:8]) if errs else None


def v_meta(ctx):
    j = ctx.read_json('meta.json')
    miss = [k for k in ('title', 'description', 'tags') if k not in j]
    return f'eksik: {miss}' if miss else None


# ------------------------------------------------------------------ stages
def s_idea(ctx):
    llm_stage(ctx, 'idea', v_idea)


def s_package(ctx):
    llm_stage(ctx, 'package', v_package)


def s_script(ctx):
    llm_stage(ctx, 'script', v_script)


def s_tts(ctx):
    cmd = [sys.executable, HERE / 'tts_segments.py', ctx.p('script.json'), '--out', ctx.p('audio'), '--timeline', ctx.p('timeline.json'),
           '--voice', ctx.a.voice, '--public-prefix', f'audio/whatif/{ctx.slug}']
    if ctx.a.dry_run:
        cmd.append('--dry-run')
    ctx.run(cmd)
    if not ctx.a.dry_run:
        tl = ctx.read_json('timeline.json')
        ctx.log(f"tts: {len(tl['segments'])} segment, {tl['total_sec']/60:.1f} dk")
        try:
            sj = ctx.read_json('script.json')
            words = sum(len(s['text'].split()) for s in sj['segments'])
            speech = sum(float(s.get('dur', 0)) for s in tl['segments']) or tl['total_sec']
            ctx.log(f'tts: ölçülen hız ≈ {words / (speech / 60):.0f} kelime/dk → sonraki videolar için WHATIF_WPM')
        except Exception:
            pass
        if tl['total_sec'] > 11 * 60:
            raise RuntimeError(f"toplam süre {tl['total_sec']/60:.1f} dk > 11 dk tavanı; script'te vuruş kes, --from script")
        if not (7.5 * 60 <= tl['total_sec'] <= 10.5 * 60):
            ctx.log('UYARI: toplam süre 8–10 dk hedefinin dışında; script stage\'ine dönüp vuruş ekle/çıkar')


def s_shots(ctx):
    if not ctx.p('timeline.json').exists():
        raise RuntimeError('timeline.json yok — önce tts')
    llm_stage(ctx, 'shots', v_shots)


def s_render(ctx):
    lib = ctx.studio / 'src' / 'lib' / 'whatif' / 'WhatIfFilm.tsx'
    if not lib.exists():
        raise RuntimeError(f'Stüdyoda {lib} yok. templates/remotion/register.ts adımlarını uygula (kopyala + Root.tsx\'e Folder ekle).')
    # ses dosyaları → studio/public/audio/whatif/<slug>/
    dst = ctx.studio / 'public' / 'audio' / 'whatif' / ctx.slug
    if not ctx.a.dry_run:
        dst.mkdir(parents=True, exist_ok=True)
        for f in ctx.p('audio').glob('*.mp3'):
            if not (dst / f.name).exists() or (dst / f.name).stat().st_mtime < f.stat().st_mtime:
                shutil.copy2(f, dst / f.name)
    props = {'shots': ctx.read_json('shots.json'), 'timeline': ctx.read_json('timeline.json'), 'audio': True, 'captions': ctx.a.captions}
    ctx.p('props.json').write_text(json.dumps(props, ensure_ascii=False), encoding='utf-8')
    out = ctx.p('render'); out.mkdir(exist_ok=True)
    draft = out / f'{ctx.slug}-draft.mp4'; final = out / f'{ctx.slug}.mp4'
    base = [NPX, 'remotion', 'render', 'src/index.ts', 'whatif-film']
    if os.environ.get('WHATIF_BROWSER'):  # junction/symlink'li kurulumda chrome-headless-shell spawn ENOENT verir → gerçek yolu ver
        base.append(f"--browser-executable={os.environ['WHATIF_BROWSER']}")
    if not draft.exists():
        ctx.run(base + [draft, f'--props={ctx.p("props.json")}', '--scale=0.5', '--crf=28', '--x264-preset=veryfast', '--log=error'], cwd=ctx.studio)
    else:
        ctx.log('render: draft mevcut, atlandı')
    # QA still'leri: her shot'ın start+5 karesi (en fazla 24 kare)
    shots = props['shots']['shots']; fps = props['shots'].get('fps', 30)
    frames = sorted({int(round(s['t_start'] * fps)) + 5 for s in shots})
    step = max(1, len(frames) // 24)
    qa = ctx.p('qa'); qa.mkdir(exist_ok=True)
    if not any(qa.glob('*.jpeg')):
        ctx.run(base + [qa, '--frames=' + ','.join(str(f) for f in frames[::step]), f'--props={ctx.p("props.json")}', '--scale=0.5', '--image-format=jpeg', '--log=error'], cwd=ctx.studio)
        ctx.log(f'render: QA kareleri → {qa} (Claude bunlara BAKMALI: etiket çakışması, metin güvenli alan, boş kare)')
    if ctx.a.draft_only:
        ctx.log('render: --draft-only, final atlandı'); return
    if not final.exists():
        ctx.run(base + [final, f'--props={ctx.p("props.json")}', '--codec=h264', '--crf=18', '--pixel-format=yuv420p', '--audio-codec=aac', '--audio-bitrate=320k', '--log=error'], cwd=ctx.studio)
    if not ctx.a.dry_run:
        r = ctx.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,width,height', '-of', 'json', final])
        info = json.loads(r.stdout)
        ctx.log('render: final', json.dumps(info['format']), [s.get('codec_type') for s in info['streams']])
        if not any(s.get('codec_type') == 'audio' for s in info['streams']):
            raise RuntimeError('final mp4\'te ses yok')
    ctx.st('render')['outputs'] = [str(draft), str(final), str(qa)]


def s_thumb(ctx):
    pk = ctx.read_json('package.json')
    th = pk['thumb']
    out = ctx.p('thumbs'); out.mkdir(exist_ok=True)
    layouts = th.get('layouts') or ['A', 'B', 'C']
    for L in layouts:
        png = out / f'{ctx.slug}-{L}.png'
        if png.exists():
            continue
        cmd = [sys.executable, HERE / 'make_thumbnail.py', '--text', th['text'], '--layout', L, '--out', png,
               '--label', th.get('label', '?'), '--label-tone', th.get('label_tone', 'bad'), '--expr', th.get('expr', 'shocked'), '--bg', th.get('bg', 'street')]
        if th.get('sub'):
            cmd += ['--sub', th['sub']]
        if th.get('base_image'):
            cmd += ['--base-image', th['base_image']]
        ctx.run(cmd)
    pick = th.get('pick', layouts[0])
    final = out / f'{ctx.slug}-final.png'
    src = out / f'{ctx.slug}-{pick}.png'
    if src.exists() and not ctx.a.dry_run:
        shutil.copy2(src, final)
    ctx.log(f'thumb: varyantlar {layouts}, seçilen {pick} → {final}. Opsiyonel Higgsfield polish: Claude {src.name} (yazısız: --no-text) yükler, img2img, sonra --base-image ile yazıyı basar.')


def s_meta(ctx):
    llm_stage(ctx, 'meta', v_meta)
    m = ctx.read_json('meta.json')
    shots = ctx.read_json('shots.json')['shots']
    # bölümler: kind=card/title overlay'li shot'lar (ilk 0:00 zorunlu)
    chapters = []
    for s in shots:
        ovs = s.get('overlay') or []
        ovs = ovs if isinstance(ovs, list) else [ovs]
        for o in ovs:
            if o.get('kind') in ('card', 'title') and len(o['text']) <= 40:
                chapters.append((s['t_start'], o['text'].replace('\n', ' ')))
                break
    if not chapters or chapters[0][0] > 0:
        chapters.insert(0, (0, 'Giriş'))
    seen = set(); lines = []
    for t, name in chapters:
        if name in seen:
            continue
        seen.add(name)
        lines.append(f'{int(t)//60:d}:{int(t)%60:02d} {name}')
    desc = m['description'].rstrip() + '\n\nBölümler:\n' + '\n'.join(lines[:20]) + '\n\n' + ' '.join(m.get('hashtags', ['#animasyon', '#yaolsaydı']))
    ctx.p('description.txt').write_text(desc[:4900], encoding='utf-8')
    up = {
        'file': str(ctx.p('render') / f'{ctx.slug}.mp4'), 'thumbnail': str(ctx.p('thumbs') / f'{ctx.slug}-final.png'),
        'title': m['title'][:100], 'description_file': str(ctx.p('description.txt')), 'tags': m.get('tags', [])[:30],
        'privacy': m.get('privacy', 'private'), 'publish_at': m.get('publish_at'), 'category': m.get('category', '1'),
        'synthetic': True, 'language': 'tr', 'playlist_id': m.get('playlist_id'),
    }
    ctx.p('upload.json').write_text(json.dumps(up, ensure_ascii=False, indent=1), encoding='utf-8')
    ctx.log(f"meta: description.txt ({len(lines)} bölüm) + upload.json yazıldı")


def s_upload(ctx):
    up = ctx.read_json('upload.json')
    for k in ('file', 'thumbnail'):
        if not Path(up[k]).exists() and not ctx.a.dry_run:
            raise RuntimeError(f'upload: {k} yok: {up[k]}')
    uploader = ctx.studio / 'scripts' / 'youtube' / 'youtube_upload.py'
    token = ctx.studio.parent / 'secrets' / 'youtube_token.json'  # yt_common.py: ROOT = parents[3] → studio/..
    if not uploader.exists():
        raise RuntimeError(f'{uploader} yok (daily-film-pipeline / the-other-self stüdyosu gerekli)')
    if not token.exists():
        raise RuntimeError(f'YouTube token yok: {token} — önce yt_auth.py (bkz. E-pipeline.md §upload)')
    cmd = [ctx.a.yt_python, uploader, '--meta', ctx.p('upload.json')]
    if ctx.a.dry_run:
        cmd.append('--dry-run')
    r = ctx.run(cmd, cwd=uploader.parent)
    m = re.search(r'VIDEO (\S+) (https://youtu\.be/\S+)', r.stdout or '')
    if m:
        ctx.st('upload')['video_id'] = m.group(1); ctx.st('upload')['url'] = m.group(2)
        ctx.log('upload:', m.group(2))
    pub = ctx.root / 'PUBLISHED.md'
    if not ctx.a.dry_run:
        with open(pub, 'a', encoding='utf-8') as f:
            f.write(f"| {dt.date.today()} | {ctx.slug} | {up['title']} | {ctx.st('upload').get('url', '?')} | {up['privacy']} |\n")


RUN = {'idea': s_idea, 'package': s_package, 'script': s_script, 'tts': s_tts, 'shots': s_shots, 'render': s_render, 'thumb': s_thumb, 'meta': s_meta, 'upload': s_upload}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slug')
    ap.add_argument('--from', dest='from_', choices=STAGES, help='bu stage ve sonrasını sıfırla ve çalıştır')
    ap.add_argument('--only', choices=STAGES)
    ap.add_argument('--to', choices=STAGES, help='bu stage\'de dur (dahil)')
    ap.add_argument('--root', default=os.environ.get('WHATIF_ROOT', 'C:/dev/whatif-projects' if IS_WIN else str(Path.home() / 'whatif-projects')))
    ap.add_argument('--studio', default=os.environ.get('WHATIF_STUDIO', 'C:/dev/the-other-self' if IS_WIN else str(Path.home() / 'the-other-self' / 'studio')))
    ap.add_argument('--voice', default=str(HERE / 'whatif_voice.json'))
    ap.add_argument('--idea', help='idea stage için konu/soru ("Ya herkesin yalan sayısını görebilseydin?")')
    ap.add_argument('--llm', help='LLM komutu (prompt stdin → çıktı stdout), ör. "claude -p"')
    ap.add_argument('--captions', default='off', choices=['word', 'line', 'off'])
    ap.add_argument('--draft-only', action='store_true')
    ap.add_argument('--yt-python', default=os.environ.get('WHATIF_YT_PYTHON', sys.executable))
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--status', action='store_true')
    a = ap.parse_args()
    if not re.match(r'^[a-z0-9-]+$', a.slug):
        ap.error('slug: küçük harf, rakam, tire')
    ctx = Ctx(a)
    if a.status:
        for s in STAGES:
            st = ctx.state['stages'].get(s, {'status': 'pending'})
            print(f"{s:<8} {st.get('status'):<10} {st.get('finished', st.get('started', ''))}  {st.get('error', '')[:80] if st.get('error') else ''}")
        return
    if a.from_:
        for s in STAGES[STAGES.index(a.from_):]:
            ctx.state['stages'][s] = {'status': 'pending'}
        ctx.save()
    todo = [a.only] if a.only else STAGES
    if a.to and not a.only:
        todo = todo[:STAGES.index(a.to) + 1]
    ctx.log(f'=== pipeline {a.slug} todo={todo} dry_run={a.dry_run}')
    for s in todo:
        st = ctx.st(s)
        if st.get('status') == 'done' and not a.only:
            ctx.log(f'--- {s}: done (atlandı)'); continue
        st.update({'status': 'running', 'started': now(), 'error': None}); ctx.save()
        ctx.log(f'--- {s}')
        try:
            RUN[s](ctx)
        except SystemExit as e:
            if e.code == EXIT_NEEDS_LLM:
                raise
            st.update({'status': 'failed', 'error': f'exit {e.code}'}); ctx.save(); raise
        except Exception as e:  # noqa
            st.update({'status': 'failed', 'error': str(e), 'finished': now()}); ctx.save()
            ctx.log(f'FAILED {s}: {e}\n   devam: python pipeline.py {a.slug} --from {s}')
            sys.exit(1)
        st.update({'status': 'done' if not a.dry_run else 'dry', 'finished': now()}); ctx.save()
    ctx.log('=== bitti')


if __name__ == '__main__':
    main()
