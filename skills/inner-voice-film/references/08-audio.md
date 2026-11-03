# 08 — Sound, Music & Sync

Contents: 1 Principles · 2 Music map · 3 SFX rules · 4 Frame grid · 5 Remotion audio API · 6 Making the audio

Full SFX table, procedural recipes, ducking code and Remotion components: `deep-research/09-sound-music.md`.
Generator script (tested, zero deps): `scripts/sfxgen.mjs`.

---

## 0. Channel override (user decision 2026-10-15) — READ FIRST

- **The inner voice is SPOKEN with ElevenLabs.** Every blue line of the shadow twin (typed excuse, verdict word, VOICE
  lines, the boss line) is voiced with the user's own ElevenLabs voice **"Second Self - Solitude"**
  (`voice_id PL7EYPTnZppHWj5yLiVI`, model `eleven_v3`; config in the studio's `voice.json`; key in env
  `ELEVENLABS_API_KEY` — never print it). Styles: `whisper` (stability .35, style .6, speed .85) for bahane/seduction,
  `taunt` (.3/.75/.9) for verdicts, mirror and "told you.", `boss` (.25/.9/.8 + echo) for the boss line.
- Tool: `python scripts/eleven_say.py src/films/<slug>/voice-lines.json` → `public/audio/voice/<slug>/v<n>.wav`
  (leading/trailing silence trimmed, loudnorm −18). Numbers go in `spoken` as words ("only four hours left.").
- Do NOT use Higgsfield TTS or any other voice for the twin. Never change the voice without the user's OK.
- The **white narrator stays silent** (text only). The hero never speaks.
- Placement: the line starts on the first frame of its blue text; a reused excuse later in the film plays at ~0.7 gain;
  floating "word objects" in the grind play at ~0.5 gain as they appear.
- Music must be **calm** (the user found the procedural music box/ticks/drums "çok gıcık"): soft felt piano + warm pads,
  slow piano arpeggio in the grind, no detuned music box, no constant clock tick, no noise "whisper bed", no drums.
  Music ducks −8 dB under every voiced line (attack 0.15 s, release 0.5 s). Master: compressor + loudnorm −15 LUFS.
- Reference implementations: studio `scripts/insomnia-cues.mjs`, `scripts/procrastination-cues.mjs` (copy one for a new film).
- Rules 1–2 below (no VO, whisper texture instead of words) are SUPERSEDED by this section.

## 1. Principles

1. ~~Music is the narrator (no VO).~~ (superseded by §0: the twin speaks; the narrator stays text-only.) Each act has its own sound: sparse piano → silence + heartbeat → calm piano pulse → open air.
2. ~~Red text has a sound… never words.~~ (superseded by §0: blue lines are spoken with ElevenLabs.) White lines land in near-silence or on a clean downbeat.
3. **Silence is the strongest cue**: rock bottom, the beat before the boss line, the last 1.5–2 s.
4. One motif, three moods: the Act-1 minor piano motif returns in major at the bookend.
5. Everything sits on a frame grid.

## 2. Music map (2:40, generalised)

`hook-note (one soft piano note when the hook appears) → sparse motif in minor, 72 BPM (ducks under the alarm)
→ antagonist drone (A1+E2) fading in as the shadow rises, rumble 12–20 f before it's visible → loop thickens
each DAY cut (cuts on bar downbeats, 100 f) → swell + riser into the mirror crack → HARD CUT to near-silence
(room tone + 3–5 single notes placed on text lines) → heartbeat 60 → 120 BPM, CLACK on the downbeat where it
locks → groove at 120 BPM (kick 1&3, snare 2&4, 8th bass) → drums drop for one bar on "told you." and slam back
→ every punch = a drum hit → build under couplet 1 → 0.5–1 s silence on the boss line → biggest hit on the split
frame → summit: wind + relative-major chords, shimmer at sunrise → bookend: motif in major, one soft beep +
click → title THUD (no music) → final chord on the slogan → true silence.`

DOPAMINE flavour: happy acoustic guitar/ukulele intro, notification dings on the beat as an addictive rhythm,
tape-stop/pitch-down on the crash, instruments return one by one as colour returns. Map the topic's metaphor
onto timbre (loneliness ↔ one instrument + big reverb space; anxiety ↔ ticking/tremolo).

## 3. SFX rules

- SFX on the **visual contact frame** (transient 0–1 f early), never on the anticipation frame.
- Alarm: groups of 4 beeps, first beep on the frame the clock shows the time; beeps cut on the slap frame (the abrupt stop is the joke). Tune beeps/thuds to the key (A6 1760 Hz, title thud on A1).
- Act-1 slap = dull lazy "thup" + plastic click; Act-3 CLACK = sharper, on a downbeat.
- Glass crack at the peak of the mirror swell, then hard cut to silence.
- Whoosh only under white text, peak on full opacity, none at rock bottom.
- Rumble starts 12–20 f before the shadow is visible and follows its glow.
- Footsteps on every foot-contact frame (run cycle locked to the tempo); breaths tied to squash/stretch; no real voices (grunt = breath burst + low tonal hmph).
- Punch transient = contact frame layered on the kick/snare; bag chain 4–8 f later; letter shatter = short glassy tail.
- Wind pre-laps the summit by 0.5 s; room tone (−40 dBFS) under every quiet moment.
- Hit-stop freezes the picture, never the audio.

## 4. Frame grid

`framesPerBeat = 1800 / BPM` at 30 fps → choose BPMs where this is an integer: 60 (30 f), 72 (25 f), 90 (20 f),
100 (18 f), 120 (15 f), 150 (12 f). Avoid 128. Always `Math.round` from the absolute beat index.
Shared helper used by both animation and audio:
```ts
export const makeGrid = (startFrame: number, bpm: number, fps = 30, beatsPerBar = 4) => {
  const fpb = (60 / bpm) * fps;
  return { fpb,
    beat: (n: number) => startFrame + Math.round(n * fpb),
    bar: (n: number, b = 0) => startFrame + Math.round((n * beatsPerBar + b) * fpb),
    phase: (f: number) => ((((f - startFrame) / fpb) % 1) + 1) % 1 };
};
```
Cut on bar downbeats; text starts fading 3–5 f before the beat; red text may land off-beat (feels intrusive);
DAY counter swaps on kicks; run cycle = 2 beats; push-up rep = 1 bar.
Ducking: music −4…−6 dB under white text (attack 6 f, release 12 f), raise the whisper layer under red text,
−6 dB under alarm and climax. Master −14 LUFS integrated, ≤ −1 dBTP, 48 kHz.

## 5. Remotion audio API (verified v4.0.535)

- `import {Audio} from '@remotion/media'` (the old one is `<Html5Audio>`).
- `volume` = a **number** computed per frame with `interpolate` (callbacks no longer recommended).
- `trimBefore` + `durationInFrames` (startFrom/endAt/trimAfter deprecated).
- Wrap each cue in `<Sequence from durationInFrames layout="none">` so `useCurrentFrame()` is local; `durationInFrames` hard-stops a sound (alarm cut on slap; add a 1–2 f fade).
- Files in `public/`, referenced with `staticFile()`, ASCII kebab-case names.
- Beat-locked pulses without audio analysis: `glow = 1 + 0.25 * Math.exp(-grid.phase(frame) * 6)`.

## 6. Making the audio ("made from scratch")

1. Run `node scripts/sfxgen.mjs public/sfx` (copy from the skill into the project) → alarm, heartbeats, drone,
   whooshes, punch, slap/clack, title thud, rumble, glass crack, wind, shimmer, A-minor piano motif (72 BPM).
   Deterministic (seeded). Extend with the generators listed in `deep-research/09` §5.3 (whisper layer, drum kit,
   saw bass, chain rattle, breath, room tone, riser).
2. Optional: user-recorded foley (breaths, taps, footsteps) layered on top.
3. Optional drafts only: AI music (e.g. a connected audio-generation tool). AI output does not satisfy the "made
   from scratch" claim — if used, change the description's credibility line.
4. Never download/stream copyrighted music. Royalty-free sources (Pixabay, Freesound CC0, YouTube Audio Library)
   only with the user's permission, logged in `public/sfx/LICENSES.md`.
