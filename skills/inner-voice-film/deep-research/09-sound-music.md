# 09 — Sound Design, Music Score & Audio-Visual Pacing/Sync

Research agent 09/10. Sources: `00-brief/BRIEF.md`, `script-DISCIPLINE.txt` and `script-DOPAMINE.txt` (both carry music/SFX notes), reference frames 1–20, and the Remotion v4 docs, which I checked live on 2026-10-14 (see §4.0).
The films have no voice-over. Music and SFX carry all the emotion, and on-screen text stands in for dialogue. The channel claims *"every frame, sound and note of music was made from scratch"*. The procedural toolkit in §5 makes that claim literally true for us.

---

## 0. Core principles (what the audio is doing in this format)

1. **Music is the narrator.** Each act has its own sonic identity: sparse piano (Act 1), silence plus a heartbeat (the pivot), driving percussion (Act 3), then open air (the resolution). A viewer with eyes closed should still be able to follow the arc.
2. **Red text has a sound and white text does not.** Red inner-voice text always comes with a low "whisper" layer: a sub rumble plus filtered breath noise, never real words. White narrator or lesson text appears in near-silence, or on a clean musical downbeat with a soft whoosh at most. The audio repeats the colour code the visuals use.
3. **Silence is the strongest cue.** Rock bottom (0:50–1:00) and the beat just before the climax hit ("you can't.") are deliberate drop-outs. Silence works only because everything around it is dense.
4. **One motif, three moods.** The Act 1 piano motif (A minor) comes back in the summit/finale as a warm major or Picardy version. This is the cheapest and most effective payoff in a 2:40 film.
5. **Everything is quantized to a frame grid.** Pick BPMs whose beat lands on a whole number of frames (§3.1), so text, cuts and SFX all lock to the same grid in Remotion.

---

## 1. Music map — master structure (2:40 = 160 s = 4800 frames @ 30 fps)

The timings follow the DISCIPLINE chapter markers (0:00 / 0:40 mirror / 0:50 rock bottom / 1:00 Day 1 / 1:12 grind / 1:49 final fight / 2:04 summit / 2:25 title) and the script's music notes.

**Global key plan:** **A minor** throughout (melancholic, with the comfortable piano register A2–E5). Act 3 stays in A minor, played aeolian/dorian so it sounds aggressive rather than sad. The summit moves to the **relative major (C major / F major colours)**. The finale ends on **A major (Picardy third)** or a C major chord. Any minor key works for new topics as long as you keep the minor → relative-major move.

**Frame-friendly tempos @30 fps:** 72 BPM = 25 f/beat (bar 100 f) · 60 BPM = 30 f/beat · 120 BPM = 15 f/beat (bar 60 f = 2 s) · 90 BPM = 20 f/beat. @60 fps: 72 → 50, 120 → 30, 144 → 25.

| # | Time (s) | Frames @30 | Section / picture | Music | Key / BPM | Level (rel. to −14 LUFS mix) |
|---|---|---|---|---|---|---|
| M0 | 0:00–0:04 | 0–120 | Hook text on black, "Every day started the same." | Room tone only, then **one soft piano note (A4 + A2)** exactly when the text appears. Reverb tail rings into the cut. | A minor, free time | Very quiet (−30 dBFS room tone) |
| M1 | 0:04–0:13 | 120–390 | Bedroom, 5:00 alarm, snooze, "just 5 more minutes…", zZ | **Sparse piano motif** enters (Am–F–C–G, arpeggiated, felt piano, lots of space). The alarm beeps sit on top, and the motif *ducks* while the alarm plays. | A minor, **72 BPM** | Piano −22 LUFS-ish, alarm on top |
| M2 | 0:13–0:21 | 390–630 | DAY 1 couch, phone glow, shadow appears, "skip the gym." | **Bass drone** (A1 + E2 fifth, slow LFO) fades in under the piano when the shadow appears. Low rumble swells on the shadow's red-glow reveal. | A minor, 72 | Drone −28, rumble peak −20 |
| M3 | 0:21–0:40 | 630–1200 | Time-skip loop DAY 25/47/88…365 (desk, fridge, phone, sleepless) | The motif repeats and adds a **cello/pad line**. Each DAY cut lands on a **bar downbeat** (every 100 f). Every repetition is a little thicker (a "loop of misery"). | A minor, 72 | Slowly rising |
| M4 | 0:40–0:50 | 1200–1500 | **Mirror**: reflection turns red, glass cracks, "You're lazy. You'll never change." | **Emotional swell**: piano in octaves, a pad crescendo, a reverse-cymbal/riser into the **glass crack (~1410)**, then **hard cut to silence** on the black transition. | A minor, 72 → rubato | Loudest point of Act 1 (≈ −16 LUFS short-term) |
| M5 | 0:50–1:00 | 1500–1800 | **Rock bottom**: spotlight, curled up, dust, "He believed it. Day after day." / "But lazy isn't who you are…" | **Near-silence**: room tone plus 3–5 single piano notes far apart (A3… E4… C4), each placed where a text line appears. No drone. Maybe one very soft high pad on the "But…" line as the first hint of hope. | A minor, free | −30 to −24 |
| M6 | 1:00–1:12 | 1800–2160 | **Pivot**: close-up clock 4:59 → 5:00, **CLACK**, headband, stands up, "DAY 1" | **Heartbeat "thump-thump"** starts in silence at 60 BPM and accelerates to 120 BPM over ~8 s (or in two steps: 60 → 90 → 120). A sub riser runs underneath. **CLACK on the downbeat** where the heartbeat locks into the 120 BPM groove. "DAY 1" appears on the next downbeat. | A minor, 60 → 120 | Builds from −30 to −16 |
| M7 | 1:12–1:24 | 2160–2520 | DAY 3 night run, city parallax, panting | **Act 3 groove starts**: kick on 1 & 3, snare/clap on 2 & 4, 8th-note synth bass on A, palm-muted guitar or saw synth. Footsteps sit on the 8th-note grid. | A minor, **120 BPM** | −14 |
| M8 | 1:24–1:34 | 2520–2820 | DAY 12 push-ups, "told you." red text, counter 1…3…5 | Groove continues. **At "told you." the drums drop out for 1 bar** (only the drone and whisper layer remain). Drums **slam back in** on the next downbeat as he pushes through. Counter numbers tick on kicks. | 120 | −14 (dip to −22 for 1 bar) |
| M9 | 1:34–1:49 | 2820–3270 | DAY 64 punching bag, red words SHATTER on each punch; quick discipline montage (calendar Xs, mirror with headband) | Fullest arrangement so far (add toms and a lead line). **Every punch = a kick or snare hit** (punch SFX layered on the drum transient). Montage cards change on kicks. | 120 | −13 |
| M10 | 1:49–2:04 | 3270–3720 | **Final fight**: DAY 270 stairs, "Motivation gets you started." / "Discipline keeps you going.", giant shadow "you can't.", he splits it | A 4–8 bar build (risers, snare roll, toms) under the lesson text. **"you can't." = full stop**: 0.5–1 s of silence with only the low rumble and the whisper layer. Then **the climax hit** (huge impact, cymbal crash, sub drop) on the frame the shadow splits (~3600). After it: one big sustained chord ring-out. | A minor → pivot chord F/G | Peak of film (≈ −11 LUFS short-term, true peak ≤ −1 dBTP) |
| M11 | 2:04–2:17 | 3720–4110 | **Summit at dawn**, headband flutters, "Nobody is coming to save you." / "So save yourself." | **Wind** bed plus **warm resolved chords**: Fmaj7 → C → G → C (or Am → F → C), slow strings or pad with soft piano. **Sunrise shimmer** (high bell sparkle) when the sun breaks. Text lines land on chord changes. | C major / A minor relative, **~66–72 BPM** half-time feel | −18 |
| M12 | 2:17–2:25 | 4110–4350 | Bedroom 5:00 again, dawn window, tiny powerless shadow, character smiles and walks out | **Reprise of the Act 1 piano motif in major** (A major or C major voicing). One gentle alarm beep that he silences with a soft **click** (no slap), which mirrors the opening. Wind fades out. | A major (Picardy) / C, 72 | −20 |
| M13 | 2:25–2:40 | 4350–4800 | End card: "DISCIPLINE" title, red underline draw, "Day one, or one day." | **Title THUD** (low boom, no music) on the title reveal. A soft whoosh or pen-scratch under the red underline draw. **One final soft piano chord** on the subtitle. Then the tail decays to **true silence for the last ~1.5–2 s** (frames ~4740–4800). | A major / C | −22 → silence |

**DOPAMINE variant (same template, different instrumentation):** The happy intro (0:00–0:15) uses a light acoustic guitar/ukulele in a major key (the character literally plays guitar), with music notes as visual particles. Phone/slot-machine notifications become a **rhythmic, addictive pattern of dings**. The "colour loss" crash uses a **pitch-down / tape-stop** on the music. The Day-1-to-Day-26 recovery reintroduces the guitar motif one instrument at a time, and the music "gains colour" as the picture does. Lesson: **map the topic's metaphor onto the sound** (colour ↔ timbre richness, loneliness ↔ reverb space / a single instrument, anxiety ↔ ticking clock / tremolo).

**Generalised template for new topics** (for the skill):
`hook-note → sparse-motif(minor, 60–76 BPM) → antagonist-drone → loop-thickens → swell → SILENCE → pulse(heartbeat/clock/breath) → groove(110–140 BPM) → dropout-on-antagonist-line → climax-hit → open-air resolution(relative major) → motif reprise(major) → title thud → silence`.

---

## 2. SFX catalog

**Global rules**
- Place SFX **on the visual contact frame**, never on the anticipation frame. For impacts, the audio transient starts **0–1 frame before** the contact frame. Audio heard slightly early reads as "tight"; audio heard late reads as "laggy".
- Every SFX gets a short fade (≥ 4 ms) at the edges to avoid clicks. All library files are peak-normalized to −1 dBFS, and the mix gain sits in the cue's `volume`.
- Pick SFX timbres in the same key as the score (or atonal ones). For example, tune the title thud to A1 and the alarm beep to a pitch in the A-minor family (e.g. E6 ≈ 1319 Hz or A6 ≈ 1760 Hz instead of a random 2 kHz) so they don't clash with the piano.
- Mono SFX are fine. Pan slightly toward the on-screen source (Remotion has no pan prop, so bake the panning into the WAV, or keep everything mono-centred, which is the simplest option).

| SFX | Where (DISCIPLINE) | Timing rule | Procedural recipe (see §5) | Royalty-free search terms |
|---|---|---|---|---|
| **Alarm beeps** | 0:04 bedroom 5:00; 1:00 pivot; 2:17 finale | Beep groups of 4 × (90 ms on / 70 ms off), repeating. The first beep lands on the frame the clock reads 5:00. Duck the music −6 dB while it plays. In the finale use a single, softer beep (−10 dB). | `alarmBeep()` softened square wave + LP 6 kHz | "digital alarm clock beep" |
| **Slap / snooze** | Act 1 snooze press | A dull, lazy "thup" on hand contact plus a small plastic click. The beeps cut **on the same frame**: an abrupt stop is the joke. | `impact({body:300, click:1.5})` pitched lower, quieter | "button press plastic", "hand slap table" |
| **CLACK** (determined) | 1:00 pivot | Sharper and louder than the snooze. Lands **on a music downbeat**, the heartbeat locks into the groove here. Beep cut on the same frame. | `impact` with high click amount + a short high-pass | "switch clack", "heavy button" |
| **Phone taps / scroll / notification** | DAY 1 couch, DAY 88 montage; DOPAMINE heavily | Taps every 10–15 frames during scrolling, very quiet (−30). A notification "ding" on screen-light-up frames. In DOPAMINE, put the dings on the beat so they become the addictive rhythm. | Short 1–2 kHz sine blips (8 ms); ding = 2 sines (E6+B6) with exp decay | "phone tap", "notification ding" |
| **Glass crack** | 0:47 mirror | Crack **at the peak of the music swell**. The visual crack lines grow over 6–10 frames while the audio tick cluster plays front-loaded. Then a hard cut to silence. | `glassCrack()` clustered high ticks + ringing partials | "glass crack", "mirror crack" |
| **Whoosh on text** | Every white lesson line, DAY counters | Use sparingly, for white text only (not every line). The whoosh **peak** (≈40% into the file) lands on the frame the text reaches full opacity, so the file starts ~0.2 s before. Volume −24 to −20. **No whoosh in the rock-bottom section.** | `whoosh({sec:0.5, peak:0.4})` LP-swept noise | "soft whoosh", "swish" |
| **Low rumble (shadow)** | Shadow appears (0:13, 0:30, 0:40, 1:49) | Starts **12–20 frames before** the shadow is visible (dread before sight). Peaks on full reveal and fades over 1–2 s. Follows the shadow's glow opacity. | `rumble()` double-LP noise ≤ 120 Hz | "sub rumble", "dark drone hit" |
| **Red-text "whisper" layer** | Every red line ("skip the gym.", "you're tired.", "told you.", "you can't.") | Starts on the first frame of the text and lasts as long as the text stays on screen. The **whisper is texture, not words**: band-passed breath noise (1–4 kHz, amplitude-modulated at ~6 Hz) + rumble + a quiet reversed reverb tail. Optional: a pitched-down "sss" swell. | noise → band-pass → AM 6 Hz + `rumble()` | "dark whisper texture", "breath reverse" |
| **Footsteps** | Night run, stairs climb, finale walk-out | **One step per foot-contact frame of the run cycle.** Make the cycle length a multiple of the beat: at 120 BPM, a step every 15 f (quarter notes) or 7.5 → alternate 7/8 f (eighths). Alternate 2–3 sample variations and ±1 dB to avoid machine-gunning. | short LP noise burst + 100 Hz thump, 3 random variations | "footstep concrete", "running steps" |
| **Breath / panting** | Run (tired stop), push-ups | Inhale/exhale loops tied to the body's squash/stretch. The exhale lands on the effort frame. Gets heavier as fatigue builds and stops when he stops. | band-passed noise 500–2500 Hz with breath-shaped envelope | "panting", "heavy breathing" |
| **Push-up grunt** | DAY 12, on "told you." and the last rep | **No real voice** (the format has none). Use a breath burst + low tonal "hmph" (filtered noise + 120 Hz short sine). Peaks on the top of the rep. The counter number "pops" on the same frame. | breath burst + `impact({body:120, click:0})` | (record yourself) "effort grunt" |
| **Punch impacts + bag chains** | DAY 64 bag | Punch transient **= contact frame**, layered on the kick/snare of the groove. The bag chain jingle comes **4–8 frames after** (inertia) and decays with the bag swing. Alternate 3 punch variations, and the last punch of a phrase gets the biggest one. | `impact({body:70})` + metallic chain = several 3–6 kHz inharmonic sine blips with random jitter | "punch heavy bag", "chain rattle" |
| **Letter shatter** | Red words exploding on punches | Starts on the punch frame (shares the transient), then 300–600 ms of a crumbling glassy tail while the letters fly out. Pitch it slightly down for big words. | `glassCrack()` shortened + a whoosh layer for the flying letters | "glass shatter small", "debris" |
| **Climax hit** (shadow split) | ~2:00 | Biggest sound in the film: sub drop (A0/A1 sine sweep down) + crash + impact + reversed swell feeding into it. Comes **after 0.5–1 s of silence**. Pair it with a 2–4 frame white flash and a hit-stop. | `impact({body:42})` + `rumble` + noise crash | "cinematic boom", "impact hit" |
| **Wind** | Summit 2:04–2:17 | Loop bed starting 0.5 s before the cut to the summit (pre-lap / J-cut). The headband flutter syncs with wind gusts (modulate the flutter amplitude with the same LFO idea). | `wind()` LFO-modulated LP noise | "mountain wind loop" |
| **Sunrise shimmer** | Summit, sun breaks horizon | 2–4 s rising sparkle in the key (A5/C6/E6/G6). Starts when the sun's edge appears and peaks at full glow. | `shimmer()` slow-tremolo sines + reverb | "magic shimmer", "bell sparkle" |
| **Title "thud"** | 2:25 end card | One deep thud **on the exact frame "DISCIPLINE" appears**. No music under it. The subtitle gets a soft piano chord, not another thud. | `impact({body:42, click:0.2})` + reverb | "cinematic thud", "trailer boom" |
| **Room tone** | Under everything quiet | A constant −40 dBFS pink-ish noise bed. Pure digital silence sounds like an error, room tone sounds like "silence". Only the very last frames go to true zero. | LP noise 4 kHz, very quiet | "room tone" |
| **zZ / clock tick / fast-forward** | Act 1 sleep, clock 5:05 → 8:47 | zZ: a soft descending "boop" per Z. Fast-forward: accelerating ticks (or a tape-speed-up whoosh) plus a panic "sting" (a tritone piano stab) on "again." | sine blips; tick = 1 ms click + 3 kHz ring | "clock ticking", "time lapse" |

### 2.1 Sourcing royalty-free assets (fallback / layering)

| Source | License | Notes |
|---|---|---|
| **Pixabay Sound Effects & Music** | Pixabay Content License: free for commercial use, no attribution required. You may not redistribute the files standalone or sell them unmodified. | Good alarm, whoosh, impact and wind packs. Some music on Pixabay is registered with Content ID, so check before using it on YouTube. |
| **Freesound.org** | Per-file: filter by **"Creative Commons 0"** for no attribution. CC-BY needs credit in the description, avoid CC-BY-NC for monetized videos. | Best for raw foley (breaths, footsteps, chains, room tone). |
| **YouTube Audio Library** (YouTube Studio → Audio Library) | Free for use **in YouTube videos**. Some tracks need attribution (filterable). | Safe from Content ID claims on YouTube. Not suitable if the video is also distributed elsewhere. |
| **Sonniss GDC Game Audio Bundle** (yearly free bundle) | Royalty-free, commercial use | High-quality impacts, whooshes and ambiences. |

Per the brief: **do not download during research**. The orchestrator or user decides later. If sourced audio is used, keep a `public/sfx/LICENSES.md` with the URL, author and license of each file. To keep the "made from scratch" claim honest, prefer §5's procedural renders and only layer recorded foley the user records themselves (breaths, taps and footsteps take five minutes with a phone).

### 2.2 AI music / audio generation (optional)

- **Higgsfield MCP** is connected in this environment and exposes `generate_audio` / `generate_audio_batch` (plus `list_voices`, `create_voice`). It could generate score cues ("sparse melancholic felt piano in A minor, 72 BPM, 16 bars, no drums") or SFX. I haven't tested it; check credits and output license first. AI output is **not** "made from scratch" in the channel's sense, so use it for drafts or temp tracks.
- Other options: Suno / Udio (full songs, check commercial terms per plan tier), Stable Audio (SFX and loops, text-to-audio with BPM control), ElevenLabs Sound Effects (text-to-SFX), and Meta AudioCraft/MusicGen (open weights, local, MIT code / CC-BY-NC weights, so it is **non-commercial**, beware).
- Practical hybrid: AI or human composes the **piano motif as MIDI**, and our procedural renderer (§5) or a free sampler (Spitfire LABS, Decent Sampler) plays it. This keeps the timing frame-exact and the result original.

---

## 3. Sync rules

### 3.1 BPM → frames
```
framesPerBeat = 60 / BPM * fps          // 72 BPM @30fps = 25 f; 120 BPM @30fps = 15 f
framesPerBar  = framesPerBeat * beatsPerBar
beatFrame(n)  = musicStartFrame + round(n * framesPerBeat)   // n = beat index (can be fractional for 8ths)
```
- **Choose BPMs that give whole numbers**: 30 fps → 60, 72, 90, 100, 120, 150 BPM (1800/BPM is an integer). 60 fps → 60, 72, 75, 80, 90, 100, 120, 144 BPM. Avoid 128 BPM @30 fps (14.06 f, so the grid drifts by a frame every ~16 beats). If you must use it, always `Math.round` from the absolute beat index, never accumulate.
- With a tempo ramp (the heartbeat 60 → 120), precompute the beat frames as an array: `beats = cumulativeSum(1800 / bpmAt(t))`. Store them in the data cue list instead of deriving them on the fly.
- Shared helper: `const beat = (n: number) => MUSIC_START + Math.round(n * (60 / BPM) * fps);` Every scene file imports `beat()` and `bar()`, so text and cuts snap to the music.

### 3.2 Picture rules
1. **Cut on the beat**, ideally on bar downbeats (beat 1). In Act 1 (72 BPM) that means cuts every 100 f. In montages, cut every beat or every 2 beats (15/30 f at 120 BPM).
2. **Text appears on downbeats.** The text *starts* its fade/scale-in 3–5 frames **before** the beat so it is fully readable on the beat. Red inner-voice text can land **off-beat** (on the "and"), which makes it feel intrusive and wrong, a nice subtle trick.
3. **DAY counter changes on kick hits** in the montage. The number swaps on the kick frame with a 2–3 frame scale pop (1.15 → 1.0). The push-up counter "1…3…5" also pops on kicks.
4. **Hit-stop on punches matches the impact transient**: freeze the pose for 2–4 frames (@30 fps) starting on the contact frame. The audio transient starts on that same frame and is **not** paused (audio keeps flowing, only the picture holds). Add a 1–2 frame camera shake *after* the freeze. The climax hit gets a 4–6 frame hold plus a 2-frame white flash.
5. **Animation cycles are tempo-locked**: run cycle = 2 beats (30 f at 120 BPM) with foot contacts on 0 and 15. Push-up rep = 1 bar (60 f). Bag swing period ≈ 2 bars.
6. **Pre-lap (J-cut) ambience** 6–15 frames before a scene cut (wind before the summit, alarm before the bedroom). Post-lap reverb tails across cuts into silence.
7. **Hard cut to silence** on emotional transitions (mirror → rock bottom). Cut the audio on the same frame as the picture, with a 2–4 ms fade only.

### 3.3 Ducking (no VO, but text is the "dialogue")
- While important **white** text is fully visible, duck the music **−4 to −6 dB** (attack 6 f, release 12 f). For **red** text, duck the music but *raise* the whisper/rumble layer.
- Duck the music −6 dB under the alarm and the climax impact, so the SFX punch through without raising the overall loudness.
- Implement it as a function of frame (see §4.3, `duckGain(frame, textWindows)`).

### 3.4 Silence as a tool
- Rock bottom: room tone only plus single notes. Text appears **in** silence, so the viewer reads in their own voice.
- "you can't.": 0.5–1 s of drop-out before the climax hit. Silence before an impact makes it feel ~2× louder.
- End card: the final 1.5–2 s are silent, which gives the "Day one, or one day." line its weight and helps the loop into YouTube's end screen.

### 3.5 Loudness / delivery
- YouTube normalizes to about **−14 LUFS integrated**. Mix the master to −14 LUFS with a **true peak ≤ −1 dBTP** (`ffmpeg -af loudnorm=I=-14:TP=-1:LRA=11` as a 2-pass after the Remotion render, or keep levels conservative and only normalize).
- Use a dynamic range of LRA ~10–14 LU. The contrast between rock bottom (quiet) and the climax (loud) *is* the film, so don't over-compress.
- Render 48 kHz audio. Remotion's default AAC is fine. Use `--audio-bitrate=320k` for a cleaner piano.

---

## 4. Remotion implementation (v4, verified 2026-10-14)

### 4.0 Current API facts (from remotion.dev/docs/audio, /docs/media/audio, /docs/visualize-audio, /docs/use-windowed-audio-data, /docs/get-audio-duration-in-seconds)
- **Recommended:** `import {Audio} from '@remotion/media'`. The old `<Audio>` from `remotion` is now named **`<Html5Audio>`** (the legacy component). `@remotion/media`'s `<Audio>` also works with client-side rendering.
- Trimming: **`startFrom`/`endAt` are deprecated** (since 4.0.319) and were renamed to **`trimBefore`/`trimAfter`** (in frames). In recent versions **`trimAfter` is deprecated as well**, in favour of **`durationInFrames`**, which counts source frames starting at `trimBefore` (4.0.530 per /docs/audio). `<Audio>` from `@remotion/media` also has `from` (4.0.446+) for the start frame on the timeline, though wrapping it in `<Sequence from>` remains the portable pattern.
- **`volume`**: `number | (frame) => number`. The docs now **recommend a numeric value computed with `useCurrentFrame()` + `interpolate()`**. The callback form still works but is "no longer recommended". Volume is capped at 0–1 by default.
- Other props: `loop`, `muted`, `playbackRate` (also changes pitch), `toneFrequency` (0.01–2, constant per asset, render-only), `premountFor`/`postmountFor` (4.0.495+), `name` (Studio timeline label), `showInTimeline`.
- `staticFile('sfx/punch.wav')` for files in `public/`.
- `@remotion/media-utils`: `useAudioData(src)`, `useWindowedAudioData({src, frame, fps, windowInSeconds})` → `{audioData, dataOffsetInSeconds}`, and `visualizeAudio({audioData, frame, fps, numberOfSamples /*power of 2*/, smoothing?, optimizeFor?: 'accuracy'|'speed', dataOffsetInSeconds?})` → `number[]` in 0..1, lows on the left.
- **`getAudioDurationInSeconds()` is deprecated.** The docs recommend Mediabunny's metadata instead:
  ```ts
  import {Input, ALL_FORMATS, UrlSource} from 'mediabunny';
  const input = new Input({formats: ALL_FORMATS, source: new UrlSource(src)});
  const durationInSeconds = await input.computeDuration();
  ```
  Use this in `calculateMetadata()` if a composition's length must follow the score's length.
- Pin all `remotion` / `@remotion/*` packages to the **same exact version** (Remotion requirement). Run `npx remotion versions` to check.

### 4.1 Data model — SFX and music as cues
```ts
// src/audio/types.ts
export type SfxId =
  | 'alarm_beep' | 'slap_clack' | 'punch' | 'glass_crack' | 'whoosh_text' | 'whoosh_cut'
  | 'rumble_low' | 'heartbeat_60' | 'heartbeat_120' | 'wind_loop' | 'sunrise_shimmer' | 'title_thud';

export type SfxCue = {
  frame: number;          // absolute composition frame where the sound STARTS
  file: SfxId;            // -> staticFile(`sfx/${file}.wav`)
  volume?: number;        // 0..1, default 1
  durationInFrames?: number; // cut it short (e.g. alarm stops on the slap frame)
  trimBefore?: number;    // skip the start of the file (frames)
  fadeOutFrames?: number; // fade at the end of durationInFrames
  offsetToPeak?: number;  // for whooshes: frames from file start to loudest point -> lets you anchor on the peak
};

export type MusicCue = {
  id: string; file: string;      // 'music/act1_piano_Am_72.wav'
  from: number; durationInFrames: number;
  baseVolume: number;
  fadeIn?: number; fadeOut?: number;
  bpm: number; beatOffsetFrames?: number; // where beat 0 sits inside the file
};

export type DuckWindow = {from: number; to: number; depthDb: number}; // music ducking under text / alarm / impact
```
Scenes **export their cues** next to their animation timings (single source of truth). For example, `PunchScene.cues = [{frame: beat(4), file: 'punch'}, …]` and the punch animation uses the same `beat(4)` for its contact frame. The master composition concatenates and offsets them.

### 4.2 Rendering cues
```tsx
// src/audio/SfxLayer.tsx
import {Audio} from '@remotion/media';
import {Sequence, staticFile, useCurrentFrame, interpolate} from 'remotion';
import type {SfxCue} from './types';

const SfxClip: React.FC<{cue: SfxCue}> = ({cue}) => {
  const f = useCurrentFrame();               // local to the <Sequence>, starts at 0
  const dur = cue.durationInFrames ?? 9999;
  const fo = cue.fadeOutFrames ?? 0;
  const v = (cue.volume ?? 1) *
    (fo > 0 ? interpolate(f, [dur - fo, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 1);
  return <Audio src={staticFile(`sfx/${cue.file}.wav`)} volume={v} trimBefore={cue.trimBefore} />;
};

export const SfxLayer: React.FC<{cues: SfxCue[]}> = ({cues}) => (
  <>
    {cues.map((c, i) => (
      <Sequence key={i} from={c.frame - (c.offsetToPeak ?? 0)} durationInFrames={c.durationInFrames}
                name={`sfx:${c.file}`} layout="none">
        <SfxClip cue={c} />
      </Sequence>
    ))}
  </>
);
```
- `<Sequence durationInFrames>` hard-stops the sound, which is how the alarm "cuts" on the slap frame. Add a 1–2 frame fade-out to avoid a click.
- `offsetToPeak` lets you author whooshes and risers by **where they peak** (text full opacity / impact frame) instead of where they start.

### 4.3 Music with fades + ducking (numeric volume, the recommended style)
```tsx
// src/audio/MusicLayer.tsx
import {Audio} from '@remotion/media';
import {Sequence, staticFile, useCurrentFrame, interpolate} from 'remotion';
import type {MusicCue, DuckWindow} from './types';

const dbToGain = (db: number) => 10 ** (db / 20);
export const duckGain = (frame: number, windows: DuckWindow[], atk = 6, rel = 12) => {
  let g = 1;
  for (const w of windows) {
    const amt = interpolate(frame, [w.from - atk, w.from, w.to, w.to + rel], [0, 1, 1, 0],
      {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
    g = Math.min(g, 1 - amt * (1 - dbToGain(w.depthDb)));
  }
  return g;
};

const MusicClip: React.FC<{cue: MusicCue; ducks: DuckWindow[]}> = ({cue, ducks}) => {
  const local = useCurrentFrame();            // 0..durationInFrames
  const absolute = local + cue.from;          // ducks are authored in absolute frames
  const fade = interpolate(local,
    [0, cue.fadeIn ?? 1, cue.durationInFrames - (cue.fadeOut ?? 1), cue.durationInFrames],
    [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <Audio src={staticFile(cue.file)} volume={cue.baseVolume * fade * duckGain(absolute, ducks)} name={cue.id} />;
};

export const MusicLayer: React.FC<{cues: MusicCue[]; ducks: DuckWindow[]}> = ({cues, ducks}) => (
  <>{cues.map((c) => (
    <Sequence key={c.id} from={c.from} durationInFrames={c.durationInFrames} layout="none" name={`music:${c.id}`}>
      <MusicClip cue={c} ducks={ducks} />
    </Sequence>
  ))}</>
);
```
Crossfades between acts are just two overlapping `MusicCue`s with matching `fadeOut`/`fadeIn`. A hard cut to silence is `fadeOut: 1`.

### 4.4 Beat grid helper (shared by animation + audio)
```ts
// src/audio/beat.ts
export const makeGrid = (startFrame: number, bpm: number, fps: number, beatsPerBar = 4) => {
  const fpb = (60 / bpm) * fps;
  return {
    fpb,
    beat: (n: number) => startFrame + Math.round(n * fpb),
    bar: (n: number, beatInBar = 0) => startFrame + Math.round((n * beatsPerBar + beatInBar) * fpb),
    // phase 0..1 within current beat — drive pulses/glow without audio analysis
    phase: (frame: number) => (((frame - startFrame) / fpb) % 1 + 1) % 1,
  };
};
// ACT3 = makeGrid(2160, 120, 30) -> ACT3.beat(0) = 2160, ACT3.bar(1) = 2220
```
A deterministic **beat pulse** without any audio analysis: `glow = 1 + 0.25 * Math.exp(-ACT3.phase(frame) * 6)`. This is cheaper and fully deterministic, so prefer it for the red glow / day counter pulses.

### 4.5 Audio-reactive glow (optional, from the actual waveform)
```tsx
import {useWindowedAudioData, visualizeAudio} from '@remotion/media-utils';
import {staticFile, useCurrentFrame, useVideoConfig} from 'remotion';

export const useBassLevel = (src: string, musicStartFrame: number) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const audioFrame = frame - musicStartFrame;       // visualizeAudio wants the frame *inside the audio file*
  const {audioData, dataOffsetInSeconds} = useWindowedAudioData({src: staticFile(src), frame: audioFrame, fps, windowInSeconds: 10});
  if (!audioData || audioFrame < 0) return 0;
  const bins = visualizeAudio({audioData, frame: audioFrame, fps, numberOfSamples: 32, dataOffsetInSeconds, optimizeFor: 'speed'});
  return Math.min(1, (bins[0] + bins[1]) * 1.5);    // lows are on the left; scale/log as needed
};
// usage: <ShadowGlow intensity={0.6 + 0.4 * useBassLevel('music/act3_drive_120.wav', 2160)} />
```
Uses: the shadow's red glow breathes with the drone/rumble, the summit sun's bloom swells with the pad, and the heartbeat drives a vignette pulse at the pivot. Remember: the `frame` passed in must be relative to the audio (account for `<Sequence from>` and `trimBefore`).

### 4.6 Master composition layout
```tsx
<AbsoluteFill>
  <Scenes />                                     {/* visuals */}
  <MusicLayer cues={MUSIC_CUES} ducks={DUCKS} /> {/* stems: act1_piano, drone, heartbeat, act3_drive, summit_pad, finale */}
  <SfxLayer cues={ALL_SFX_CUES} />               {/* concatenated from all scenes */}
</AbsoluteFill>
```
Recommended stem split (instead of one score file): `act1_piano`, `drone`, `heartbeat`, `act3_drums`, `act3_bass_synth`, `summit_pad`, `motif_reprise`, `room_tone`. Stems let you duck and fade per instrument (e.g. at "told you." drop only the drum stem).

---

## 5. Procedural audio toolkit (the "made from scratch" path)

### 5.1 Plan
- **Language:** Node (≥ 18), **zero dependencies**, so it lives in the same repo as Remotion: `scripts/audio/sfxgen.mjs` → writes `public/sfx/*.wav` (48 kHz / 16-bit mono). Run with `npm run audio` (`"audio": "node scripts/audio/sfxgen.mjs public/sfx"`).
- **Deterministic:** a seeded LCG for all noise, so the same input gives byte-identical WAVs and renders are reproducible (Remotion's determinism philosophy carried over to audio). Note that the seed is global, so changing the generation order changes the noise. If you need per-asset stability, reseed in each generator.
- **Building blocks:** oscillators (sine/softened square), seeded noise, a one-pole low-pass with a time-varying cutoff (clamped ≥ 20 Hz), high-pass = x − LP(x), attack/exp-decay envelopes, a pitch-drop envelope for thumps, an additive "felt piano" (8 slightly inharmonic decaying partials + hammer noise), a cheap comb reverb, peak-normalize to −1 dBFS, and 4 ms edge fades.
- **Score rendering:** `pianoPhrase(notes, bpm)` takes `[beat, midi, lenBeats, vel]` lists, the *same beat units* the Remotion grid uses, so music and picture share one timeline. Extend it with `drumPattern(steps, bpm)` (kick = `heartbeat`-style pitch-drop sine, snare = noise burst + 180 Hz sine, hat = HP noise 8 ms) and `saw bass` (PolyBLEP saw → LP) for Act 3.
- **Later upgrades:**
  - (a) `node-web-audio-api` (an OfflineAudioContext in Node) or Tone.js `Tone.Offline` in a headless browser, for richer synthesis (biquad filters, convolution reverb with a generated impulse response).
  - (b) Python + numpy/scipy (`scipy.signal.butter`, `soundfile`) if the team prefers Python.
  - (c) Render MIDI through a free sample library for a real piano timbre.
  - (d) A post-mix `ffmpeg loudnorm` pass.
- **Outputs:** `public/sfx/*.wav`, `public/music/*.wav` stems, and optionally a `cues.json` export (beat → frame) consumed by `SfxLayer`.

**Status:** I wrote the script below and **test-ran it** (Node v24, ~0.9 s for all 14 files). Every file had non-zero peak/RMS. One bug was found and fixed: a negative LP cutoff in `wind()` produced NaN, so the `lp()` clamp was added. The test WAVs were written to scratch only, not to the project.

### 5.2 Code — `scripts/audio/sfxgen.mjs`
```js
// sfxgen.mjs — zero-dependency procedural SFX/music-stem generator (Node >= 18)
// usage: node sfxgen.mjs <outDir>
import fs from 'node:fs';
import path from 'node:path';

const SR = 48000;
const OUT = process.argv[2] ?? 'public/sfx';
fs.mkdirSync(OUT, {recursive: true});

// ---------- utilities ----------
let seed = 1337; // deterministic noise => identical renders every time
const rnd = () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296) * 2 - 1;
const buf = (sec) => new Float32Array(Math.ceil(sec * SR));
const TAU = Math.PI * 2;
const mtof = (m) => 440 * 2 ** ((m - 69) / 12);
const env = (t, a, d) => (t < a ? t / a : Math.exp(-(t - a) / d)); // attack-lin, exp decay
function lp(x, cutoff) { // one-pole low-pass, cutoff may be fn(i)
  let y = 0; const o = new Float32Array(x.length);
  for (let i = 0; i < x.length; i++) {
    const fc = Math.max(20, typeof cutoff === 'function' ? cutoff(i) : cutoff); // clamp: negative fc = unstable
    const a = 1 - Math.exp((-TAU * fc) / SR); y += a * (x[i] - y); o[i] = y;
  }
  return o;
}
const hp = (x, fc) => { const l = lp(x, fc); return x.map((v, i) => v - l[i]); };
function normalize(x, peakDb = -1) {
  let m = 0; for (const v of x) m = Math.max(m, Math.abs(v));
  const g = m ? 10 ** (peakDb / 20) / m : 1; return x.map((v) => v * g);
}
function fadeEdges(x, ms = 4) { const n = Math.floor((ms / 1000) * SR);
  for (let i = 0; i < n && i < x.length; i++) { x[i] *= i / n; x[x.length - 1 - i] *= i / n; } return x; }
function writeWav(name, x, peakDb = -1) {
  x = fadeEdges(normalize(x, peakDb));
  const b = Buffer.alloc(44 + x.length * 2);
  b.write('RIFF', 0); b.writeUInt32LE(36 + x.length * 2, 4); b.write('WAVE', 8);
  b.write('fmt ', 12); b.writeUInt32LE(16, 16); b.writeUInt16LE(1, 20); b.writeUInt16LE(1, 22);
  b.writeUInt32LE(SR, 24); b.writeUInt32LE(SR * 2, 28); b.writeUInt16LE(2, 32); b.writeUInt16LE(16, 34);
  b.write('data', 36); b.writeUInt32LE(x.length * 2, 40);
  x.forEach((v, i) => b.writeInt16LE(Math.max(-32768, Math.min(32767, Math.round(v * 32767))), 44 + i * 2));
  fs.writeFileSync(path.join(OUT, name), b); console.log('wrote', name, (x.length / SR).toFixed(2) + 's');
}

// ---------- generators ----------
function alarmBeep({beeps = 4, freq = 2000, on = 0.09, gap = 0.07, rest = 0.5} = {}) {
  const x = buf(beeps * (on + gap) + rest);
  for (let b = 0; b < beeps; b++) {
    const s = Math.floor(b * (on + gap) * SR);
    for (let i = 0; i < on * SR; i++) { const t = i / SR;
      const sq = Math.sign(Math.sin(TAU * freq * t)) * 0.5 + Math.sin(TAU * freq * t) * 0.5; // softened square
      x[s + i] += sq * Math.min(1, t / 0.003, (on - t) / 0.003); }
  }
  return lp(x, 6000);
}
function heartbeat({bpm = 60, beats = 4} = {}) {
  const per = 60 / bpm, x = buf(beats * per + 0.5);
  const thump = (start, amp) => { for (let i = 0; i < 0.25 * SR; i++) { const t = i / SR;
      const f = 45 + 50 * Math.exp(-t / 0.03); // pitch drop = "chest" thump
      x[start + i] += amp * Math.sin(TAU * f * t) * env(t, 0.004, 0.07); } };
  for (let b = 0; b < beats; b++) { const s = Math.floor(b * per * SR);
    thump(s, 1); thump(s + Math.floor(0.22 * SR), 0.7); } // lub ... dub
  return lp(x, 400);
}
function drone({midi = 33, sec = 8} = {}) { // A1
  const x = buf(sec), f = mtof(midi);
  for (let i = 0; i < x.length; i++) { const t = i / SR;
    const lfo = 1 + 0.003 * Math.sin(TAU * 0.13 * t);
    x[i] = Math.sin(TAU * f * lfo * t) + 0.5 * Math.sin(TAU * f * 1.5 * t + 0.3) + 0.25 * Math.sin(TAU * f * 2.003 * t)
      + 0.08 * rnd();
    x[i] *= Math.min(1, t / 2, (sec - t) / 2); } // 2 s fade in/out so it loops/crossfades
  return lp(x, 300);
}
function whoosh({sec = 0.7, peak = 0.55} = {}) { // filtered noise sweep, peak = position of loudest point (0..1)
  const x = buf(sec), n = x.length;
  for (let i = 0; i < n; i++) x[i] = rnd();
  const y = lp(x, (i) => 300 + 5000 * Math.sin(Math.PI * Math.min(1, i / n / peak / 2 + 0.0001)) ** 2);
  return hp(y.map((v, i) => { const p = i / n; return v * (p < peak ? (p / peak) ** 2 : ((1 - p) / (1 - peak)) ** 1.5); }), 150);
}
function impact({sec = 0.6, body = 70, click = 1} = {}) { // punch / slap / clack depending on params
  const x = buf(sec);
  for (let i = 0; i < x.length; i++) { const t = i / SR;
    const f = body + body * 2 * Math.exp(-t / 0.02);
    x[i] = Math.sin(TAU * f * t) * env(t, 0.001, 0.09) + click * rnd() * env(t, 0.0005, 0.012); }
  return x;
}
function rumble({sec = 4} = {}) { const x = buf(sec);
  for (let i = 0; i < x.length; i++) x[i] = rnd() * Math.min(1, (i / SR) / 1.5, (sec - i / SR) / 1.5);
  return lp(lp(x, 80), 120); }
function glassCrack({sec = 1.2} = {}) { const x = buf(sec);
  for (let k = 0; k < 40; k++) { // random tiny ticks clustered at the front + ringing partials
    const s = Math.floor(Math.abs(rnd()) ** 2 * 0.5 * SR), f = 2500 + Math.abs(rnd()) * 6000, a = Math.abs(rnd());
    for (let i = 0; i < 0.15 * SR && s + i < x.length; i++) { const t = i / SR;
      x[s + i] += a * (Math.sin(TAU * f * t) * env(t, 0.0005, 0.03) + rnd() * env(t, 0.0002, 0.004)); } }
  return hp(x, 1500);
}
function pianoNote(midi, sec = 3, vel = 1) { // additive "felt piano": decaying partials, slight inharmonicity
  const x = buf(sec), f = mtof(midi);
  for (let h = 1; h <= 8; h++) { const fh = f * h * Math.sqrt(1 + 0.0004 * h * h), amp = vel / h ** 1.3, dec = 1.6 / h ** 0.6;
    if (fh > SR / 2.2) break;
    for (let i = 0; i < x.length; i++) { const t = i / SR; x[i] += amp * Math.sin(TAU * fh * t) * env(t, 0.006, dec); } }
  for (let i = 0; i < 0.01 * SR; i++) x[i] += 0.05 * vel * rnd(); // hammer/felt noise
  return lp(x, 3500);
}
function mixInto(dst, src, atSec, gain = 1) { const s = Math.floor(atSec * SR);
  for (let i = 0; i < src.length && s + i < dst.length; i++) dst[s + i] += src[i] * gain; return dst; }
function pianoPhrase(notes, bpm, tailSec = 3) { // notes: [beat, midi, lenBeats, vel]
  const spb = 60 / bpm, end = Math.max(...notes.map((n) => (n[0] + n[2]) * spb)) + tailSec, x = buf(end);
  for (const [beat, m, len, vel = 0.8] of notes) mixInto(x, pianoNote(m, len * spb + tailSec, vel), beat * spb);
  return x;
}
function reverb(x, mix = 0.3) { // cheap Schroeder-ish comb reverb
  const y = Float32Array.from(x);
  for (const [d, g] of [[1557, 0.8], [1617, 0.79], [1491, 0.78], [1422, 0.77]]) { const c = new Float32Array(x.length);
    for (let i = 0; i < x.length; i++) c[i] = x[i] + (i >= d * 2 ? g * c[i - d * 2] : 0);
    for (let i = 0; i < x.length; i++) y[i] += (mix / 4) * c[i]; }
  return y;
}
function wind({sec = 10} = {}) { const x = buf(sec); for (let i = 0; i < x.length; i++) x[i] = rnd();
  return lp(x, (i) => 700 + 350 * Math.sin(TAU * 0.11 * (i / SR)) + 200 * Math.sin(TAU * 0.37 * (i / SR)))
    .map((v, i) => v * Math.min(1, (i / SR) / 2, (sec - i / SR) / 2)); }
function shimmer({sec = 4} = {}) { const notes = [81, 84, 88, 91, 93]; const x = buf(sec); // A5 C6 E6 G6 A6 sparkles
  notes.forEach((m, k) => { for (let i = 0; i < x.length; i++) { const t = i / SR;
    x[i] += 0.3 * Math.sin(TAU * mtof(m) * t) * Math.sin(TAU * (0.5 + 0.17 * k) * t) ** 2 * Math.min(1, t / 1.5, (sec - t) / 1.5); } });
  return reverb(x, 0.4); }

// ---------- render the library ----------
writeWav('alarm_beep.wav', alarmBeep());                 // tip: freq: 1760 (A6) to sit in-key
writeWav('heartbeat_60.wav', heartbeat({bpm: 60, beats: 4}));
writeWav('heartbeat_120.wav', heartbeat({bpm: 120, beats: 8}));
writeWav('drone_A1.wav', drone({midi: 33, sec: 12}), -6);
writeWav('whoosh_text.wav', whoosh({sec: 0.5, peak: 0.4}), -6);   // offsetToPeak = 0.2 s = 6 f @30fps
writeWav('whoosh_cut.wav', whoosh({sec: 0.9, peak: 0.7}), -3);
writeWav('punch.wav', impact({body: 70, click: 0.8}));
writeWav('slap_clack.wav', impact({sec: 0.25, body: 300, click: 1.5}));
writeWav('title_thud.wav', reverb(impact({sec: 2.5, body: 42, click: 0.2}), 0.25));
writeWav('rumble_low.wav', rumble({sec: 6}), -4);
writeWav('glass_crack.wav', glassCrack());
writeWav('wind_loop.wav', wind({sec: 12}), -8);
writeWav('sunrise_shimmer.wav', shimmer(), -6);
// Act-1 motif: A minor, 72 BPM (25 frames/beat @30fps). [beat, midi, lenBeats, vel]
writeWav('piano_motif_Am_72.wav', reverb(pianoPhrase([
  [0, 45, 4, 0.6], [0, 69, 1, 0.7], [1, 72, 1, 0.6], [2, 76, 2, 0.7],        // Am
  [4, 41, 4, 0.6], [4, 69, 1, 0.6], [5, 72, 1, 0.5], [6, 77, 2, 0.6],        // F
  [8, 48, 4, 0.6], [8, 67, 1, 0.6], [9, 72, 1, 0.5], [10, 76, 2, 0.6],       // C
  [12, 43, 4, 0.6], [12, 67, 1, 0.6], [13, 71, 1, 0.5], [14, 74, 2, 0.6],    // G
], 72), 0.35), -3);
// Finale reprise (major): same rhythm, swap C->C# (A major) in the first bar, end on A major chord.
```

### 5.3 Missing generators to add next (short specs)
- **`whisperLayer(sec)`**: noise → band-pass (HP 1 kHz then LP 4 kHz) × (0.6 + 0.4·sin(2π·6t)) + `rumble` × 0.5, then reversed reverb (render, reverse, reverb, reverse back).
- **`drumKit`**: kick = `heartbeat` single thump with f 50 → 150 Hz drop and a 0.12 s decay. Snare = `impact({body:180, click:1.2})` + 0.15 s HP noise. Hat = 8 ms HP(7 kHz) noise. Plus `pattern('x...x...x...x...', bpm)` step sequencing with 16th steps.
- **`sawBass(midi, sec)`**: naive or PolyBLEP saw → LP 400–900 Hz with a per-note envelope. Act 3: 8ths on A1 with a G1–F1 movement.
- **`chainRattle()`**: 10–20 inharmonic sine blips (3–7 kHz, 15 ms decay) jittered over 300 ms with a decaying density.
- **`breath(sec, exhale=true)`**: band-pass noise 500–2500 Hz with a rise-fall envelope (inhale: slow attack; exhale: faster attack, longer tail).
- **`roomTone(sec)`**: LP 4 kHz noise at −40 dBFS (render quiet, don't normalize to −1).
- **`riser(sec)`**: noise LP sweep 200 → 8000 Hz + an upward sine glide, for builds into the mirror crack and the climax.
- **Stems at 48 kHz stereo**: add a simple stereo writer (2 channels, interleaved) plus Haas-style width for pads and wind.

---

## 6. Checklist for the final skill
- [ ] Every scene exports `SfxCue[]` built from the shared `makeGrid()` beat helper. No magic frame numbers.
- [ ] Music stems split by act/instrument, numeric `volume` with fades and `duckGain`, using `@remotion/media` `<Audio>`.
- [ ] Red text → whisper + rumble. White text → silence or a soft whoosh on a downbeat. DAY counter → kick.
- [ ] Hit-stop frames = punch transient frames. Climax = silence (0.5–1 s) → biggest hit.
- [ ] Rock bottom = room tone + single notes. End card = thud → final chord → 1.5–2 s silence.
- [ ] `npm run audio` regenerates all procedural WAVs deterministically, and LICENSES.md lists any non-procedural audio.
- [ ] Master −14 LUFS integrated, ≤ −1 dBTP, 48 kHz.
