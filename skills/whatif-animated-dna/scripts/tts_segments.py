"""tts_segments.py — vuruş (segment) bazlı ElevenLabs TTS + kelime zamanlaması + timeline.json

inner-voice-film/scripts/eleven_say.py'nin mantığı (voice.json + /v1/text-to-speech + ffmpeg loudnorm) yeniden
kullanıldı; farklar: (1) /with-timestamps uç noktası ile kelime zamanları (eleven_say.py'de yok), (2) segment
başına idempotent (metin hash'i değişmediyse atlar), (3) ffprobe ile süre ölçümü, (4) timeline.json çıktısı.

Kullanım:
  python tts_segments.py <proje>/script.json --out <proje>/audio --timeline <proje>/timeline.json [--voice whatif_voice.json]
                         [--gap 0.35] [--no-timestamps] [--force] [--dry-run]
  python tts_segments.py --list-voices        # GET /v1/voices → ad + voice_id + diller (anahtar yazdırılmaz)

script.json:
  {"slug": "...", "segments": [{"id": "v01", "text": "ekrandaki/altyazı metni", "spoken": "TTS'e giden metin (opsiyonel; rakamlar yazıyla)",
                                 "style": "narrator|hook|calm", "pause_after": 0.6}]}
timeline.json (WhatIfFilm.tsx + Caption.tsx okur):
  {"slug", "fps", "total_sec", "segments": [{"id", "text", "file": "audio/whatif/<slug>/v01.mp3", "start", "dur", "words": [{"w","s","e"}]}]}
Env: ELEVENLABS_API_KEY (asla yazdırılmaz).
"""
import sys
for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass

import argparse, base64, hashlib, json, os, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
API = 'https://api.elevenlabs.io/v1'


def key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if not k:
        sys.exit('ELEVENLABS_API_KEY not set')
    return k


def req(path, body=None, method=None, accept='application/json'):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(API + path, data=data, method=method or ('POST' if data else 'GET'),
                               headers={'xi-api-key': key(), 'Content-Type': 'application/json', 'Accept': accept})
    try:
        with urllib.request.urlopen(r, timeout=300) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'HTTP {e.code} {path}: {e.read()[:300].decode(errors="replace")}') from None


def list_voices():
    v = json.loads(req('/voices'))
    for x in v.get('voices', []):
        labels = x.get('labels') or {}
        langs = ','.join(sorted({l.get('language', '') for l in x.get('verified_languages', []) if l.get('language')})) or labels.get('language', '')
        print(f"{x['voice_id']}  {x['name']:<32} {labels.get('gender', ''):<7} {labels.get('accent', ''):<14} langs={langs}  cat={x.get('category', '')}")
    print('\nTürkçe erkek anlatıcı için: Voice Library\'de "Turkish" filtresiyle bir ses ekle (Add to my voices), sonra voice_id\'yi whatif_voice.json\'a yaz.')


def ffprobe_dur(p: Path) -> float:
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)], capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def words_from_alignment(al: dict):
    """ElevenLabs alignment {characters[], character_start_times_seconds[], character_end_times_seconds[]} → kelimeler."""
    chars, st, en = al['characters'], al['character_start_times_seconds'], al['character_end_times_seconds']
    words, cur, s0 = [], '', None
    for c, s, e in zip(chars, st, en):
        if c.isspace():
            if cur:
                words.append({'w': cur, 's': round(s0, 3), 'e': round(last_e, 3)}); cur = ''
            continue
        if not cur:
            s0 = s
        cur += c; last_e = e
    if cur:
        words.append({'w': cur, 's': round(s0, 3), 'e': round(last_e, 3)})
    return words


def estimate_words(text: str, dur: float):
    """Timestamps yoksa: kelimeleri karakter uzunluğuna orantılı dağıt (altyazı için 'yeterince iyi' fallback)."""
    ws = text.split()
    total = sum(len(w) + 1 for w in ws) or 1
    t, out = 0.0, []
    for w in ws:
        d = dur * (len(w) + 1) / total
        out.append({'w': w, 's': round(t, 3), 'e': round(t + d, 3)}); t += d
    return out


def tts_one(text: str, cfg: dict, style: str, use_ts: bool):
    vs = dict(cfg['styles'].get(style) or cfg['styles']['narrator'])
    body = {'text': text, 'model_id': cfg['model_id'], 'voice_settings': vs}
    if cfg.get('language_code') and 'multilingual' not in cfg['model_id']:
        body['language_code'] = cfg['language_code']  # multilingual_v2 language_code kabul etmez; turbo/flash v2.5 eder
    q = f"?output_format={cfg.get('output_format', 'mp3_44100_128')}"
    if use_ts:
        try:
            j = json.loads(req(f"/text-to-speech/{cfg['voice_id']}/with-timestamps{q}", body))
            return base64.b64decode(j['audio_base64']), j.get('alignment') or j.get('normalized_alignment')
        except RuntimeError as e:
            print('  with-timestamps başarısız, düz TTS + tahmini kelime zamanı:', str(e)[:120])
    return req(f"/text-to-speech/{cfg['voice_id']}{q}", body, accept='audio/mpeg'), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('script', nargs='?')
    ap.add_argument('--out', help='mp3 klasörü (proje/audio)')
    ap.add_argument('--timeline', help='timeline.json yolu')
    ap.add_argument('--voice', default=str(HERE / 'whatif_voice.json'))
    ap.add_argument('--gap', type=float, default=None, help='segmentler arası boşluk sn (voice.json gap_sec)')
    ap.add_argument('--public-prefix', default=None, help="timeline 'file' alanı için önek, vars. audio/whatif/<slug>")
    ap.add_argument('--no-timestamps', action='store_true')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--list-voices', action='store_true')
    a = ap.parse_args()
    if a.list_voices:
        return list_voices()
    if not a.script:
        ap.error('script.json gerekli')
    cfg = json.loads(Path(a.voice).read_text(encoding='utf-8'))
    if cfg['voice_id'].startswith('PUT_'):
        sys.exit(f'voice_id placeholder — {a.voice} içine Türkçe anlatıcı voice_id yaz (python tts_segments.py --list-voices)')
    sc = json.loads(Path(a.script).read_text(encoding='utf-8-sig'))
    slug = sc.get('slug', Path(a.script).parent.name)
    out = Path(a.out or Path(a.script).parent / 'audio'); out.mkdir(parents=True, exist_ok=True)
    tl_path = Path(a.timeline or Path(a.script).parent / 'timeline.json')
    gap = a.gap if a.gap is not None else float(cfg.get('gap_sec', 0.35))
    prefix = a.public_prefix or f'audio/whatif/{slug}'
    fps = int(sc.get('fps', 30))
    t = 0.0
    segs = []
    for s in sc['segments']:
        sid = s['id']; spoken = s.get('spoken') or s['text']; style = s.get('style', 'narrator')
        h = hashlib.sha1(f"{cfg['voice_id']}|{cfg['model_id']}|{style}|{spoken}".encode()).hexdigest()[:12]
        mp3 = out / f'{sid}.mp3'; meta = out / f'{sid}.json'
        fresh = mp3.exists() and meta.exists() and json.loads(meta.read_text(encoding='utf-8')).get('hash') == h and not a.force
        if a.dry_run:
            print(('skip ' if fresh else 'TTS  ') + sid, repr(spoken[:60])); continue
        if not fresh:
            print('+', sid, repr(spoken[:70]))
            audio, al = tts_one(spoken, cfg, style, not a.no_timestamps)
            raw = out / f'{sid}.raw.mp3'; raw.write_bytes(audio)
            # loudnorm + baş/son sessizlik kırpma (eleven_say.py ile aynı reçete), mp3 çıktı (Remotion <Audio> için)
            trim = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,'
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(raw), '-af', f"{trim}highpass=f=60,loudnorm={cfg.get('loudnorm', 'I=-16:TP=-1.5:LRA=9')}",
                            '-ar', '44100', '-ac', '1', '-c:a', 'libmp3lame', '-b:a', '160k', str(mp3)], check=True)
            dur = ffprobe_dur(mp3)
            if al:
                words = words_from_alignment(al)
                # kırpma sonrası ölçek: alignment ham sese göre; kırpılmış süreye oransal sığdır
                raw_dur = ffprobe_dur(raw)
                lead = words[0]['s'] if words else 0.0
                k = dur / max(0.01, (words[-1]['e'] - lead)) if words else 1.0
                k = min(k, 1.0)
                words = [{'w': w['w'], 's': round(max(0.0, (w['s'] - lead) * k), 3), 'e': round(min(dur, (w['e'] - lead) * k), 3)} for w in words]
                src = 'elevenlabs-timestamps'
                _ = raw_dur
            else:
                words = estimate_words(s['text'], dur); src = 'estimate'
            meta.write_text(json.dumps({'hash': h, 'dur': dur, 'words': words, 'words_src': src, 'style': style}, ensure_ascii=False, indent=1), encoding='utf-8')
            raw.unlink(missing_ok=True)
        m = json.loads(meta.read_text(encoding='utf-8'))
        dur = float(m['dur'])
        words = [{'w': w['w'], 's': round(t + w['s'], 3), 'e': round(t + w['e'], 3)} for w in m['words']]
        segs.append({'id': sid, 'text': s['text'], 'file': f'{prefix}/{sid}.mp3', 'start': round(t, 3), 'dur': round(dur, 3), 'words': words, 'words_src': m.get('words_src')})
        t += dur + float(s.get('pause_after', gap))
    if a.dry_run:
        return
    tl = {'slug': slug, 'fps': fps, 'total_sec': round(t, 3), 'segments': segs}
    tl_path.write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'timeline -> {tl_path}  segments={len(segs)}  total={t:.1f}s  ({t/60:.1f} dk)')


if __name__ == '__main__':
    main()
