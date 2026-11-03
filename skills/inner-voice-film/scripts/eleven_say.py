"""Shadow-twin lines with the channel's fixed ElevenLabs voice (voice.json).

  python scripts/eleven_say.py src/films/<slug>/voice-lines.json [--force]
    lines = [{"n": 1, "text": "just check the time...", "style": "whisper", "spoken": "optional TTS text"}]
  -> public/audio/voice/<slug>/raw11/v<n>.mp3 , processed to public/audio/voice/<slug>/v<n>.wav (mono 48 kHz, loudnorm -18).
Needs env ELEVENLABS_API_KEY.
"""
import json, os, subprocess, sys, urllib.request, urllib.error

KEY = os.environ.get('ELEVENLABS_API_KEY') or sys.exit('ELEVENLABS_API_KEY not set')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CFG = json.load(open(os.path.join(ROOT, 'voice.json'), encoding='utf-8'))
LINES = sys.argv[1]
SLUG = os.path.basename(os.path.dirname(os.path.abspath(LINES)))
OUT = os.path.join(ROOT, 'public', 'audio', 'voice', SLUG)
RAW = os.path.join(OUT, 'raw11')
os.makedirs(RAW, exist_ok=True)


def tts(text, style):
    body = {'text': text, 'model_id': CFG['model_id'], 'voice_settings': CFG['styles'][style]}
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{CFG["voice_id"]}?output_format=mp3_44100_192',
                                 data=json.dumps(body).encode(), method='POST',
                                 headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f'HTTP {e.code}: {e.read()[:400].decode(errors="replace")}')


for ln in json.load(open(LINES, encoding='utf-8')):
    mp3 = os.path.join(RAW, f'v{ln["n"]}.mp3')
    if not os.path.exists(mp3) or '--force' in sys.argv:
        open(mp3, 'wb').write(tts(ln.get('spoken', ln['text']), ln.get('style', 'whisper')))
        print('+', ln['n'], repr(ln.get('spoken', ln['text'])))
    fx = 'aecho=0.8:0.6:90|180:0.35|0.2,' if ln.get('style') == 'boss' else ''
    trim = 'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,'
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', mp3, '-af',
                    f'{trim}highpass=f=70,{fx}loudnorm=I=-18:TP=-2',
                    '-ac', '1', '-ar', '48000', '-c:a', 'pcm_s16le', os.path.join(OUT, f'v{ln["n"]}.wav')], check=True)
    print('  ', f'v{ln["n"]}.wav', f'{(os.path.getsize(os.path.join(OUT, f"v{ln['n']}.wav")) - 44) / 96000:.2f}s')
print('done ->', OUT)
