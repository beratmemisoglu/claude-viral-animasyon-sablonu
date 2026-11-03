#!/usr/bin/env bash
# Preflight for the daily film run. Prints OK/FAIL lines; exit 1 if anything blocks production.
ROOT=~/the-other-self
fail=0
ok()   { echo "OK   $*"; }
bad()  { echo "FAIL $*"; fail=1; }
TODAY=$(date -u +%F)
if grep -q "^| $TODAY |" "$ROOT/project/films/PUBLISHED.md" 2>/dev/null; then bad "a film was already published today ($TODAY) — one per day"; else ok "no film yet today ($TODAY)"; fi
if [ -n "$ELEVENLABS_API_KEY" ] || grep -q '^ELEVENLABS_API_KEY=.\+' ~/.hermes/.env 2>/dev/null; then ok "ElevenLabs key present"; else bad "ELEVENLABS_API_KEY missing (add it to ~/.hermes/.env)"; fi
if (cd "$ROOT/studio/scripts/youtube" && "$ROOT/.venv-yt/bin/python" -c "from yt_common import youtube; print(youtube().channels().list(part='id', mine=True).execute()['items'][0]['id'])" >/tmp/yt_ok 2>&1); then ok "YouTube token valid (channel $(cat /tmp/yt_ok))"; else bad "YouTube token invalid/expired — re-run yt_auth.py: $(tail -1 /tmp/yt_ok)"; fi
FREE=$(df -BG --output=avail ~ | tail -1 | tr -dc 0-9)
[ "${FREE:-0}" -ge 5 ] && ok "disk free ${FREE} GB" || bad "disk free only ${FREE} GB"
if (cd "$ROOT/studio" && npx tsc --noEmit >/tmp/tsc.log 2>&1); then ok "studio typecheck"; else bad "studio typecheck failed: $(head -3 /tmp/tsc.log)"; fi
command -v ffmpeg >/dev/null && ok "ffmpeg" || bad "ffmpeg missing"
exit $fail
