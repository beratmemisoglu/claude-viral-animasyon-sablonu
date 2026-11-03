# 09 — Remotion Build & QA

Contents: 1 Studio setup · 2 Project structure · 3 Data-driven timeline · 4 Global layers & dips ·
5 Determinism & performance · 6 QA loop · 7 Windows gotchas

Full code (types, `validateScript`, FilmRenderer, Music/Camera helpers, package.json): 
`deep-research/08-remotion-architecture.md`. Verified on 2026-10-14: `remotion@4.0.535`.

---

## 1. Studio setup (once per machine)

The studio is **one Remotion project that holds every film**. Put it **outside OneDrive** (OneDrive locks
`node_modules`/`out` → EBUSY/EPERM) and away from paths with spaces. Default: `C:\dev\dayone-studio`.
If it already exists, reuse it — never re-scaffold. Ask the user once before creating it.

```powershell
New-Item -ItemType Directory -Force C:\dev | Out-Null
Set-Location C:\dev
npx create-video@latest --yes --blank dayone-studio     # fails inside a git repo
Set-Location .\dayone-studio
npm i
npx remotion add @remotion/transitions @remotion/media @remotion/google-fonts @remotion/paths @remotion/noise @remotion/layout-utils
npx tsc --noEmit
```
All `remotion`/`@remotion/*` versions must be identical — add packages only via `npx remotion add`.
Licence: free for individuals / ≤ 3-person companies.

## 2. Project structure

```
dayone-studio/
  public/sfx/  public/music/  public/img/
  scripts/sfxgen.mjs  scripts/qa.ps1
  src/index.ts  src/Root.tsx            # <Folder> per film: <slug>-film, <slug>-<scene>, <slug>-thumb (<Still> 1280x720)
  src/films/<slug>/script.ts            # FilmScript data = single source of truth
  src/films/<slug>/scenes/*.tsx         # only film-specific scenes
  src/lib/timeline/  (types, time, compute: filmDuration/sceneStarts/validateScript, FilmRenderer)
  src/lib/character/ (Hero, Face, expressions, poses, rig math fk/ik)
  src/lib/voice/     (InnerVoice)
  src/lib/text/      (fonts, HookCard, NarratorText, InfoText, VoiceText, DayCounter, CountUp, ShatterText, TitleCard)
  src/lib/sets/      (Bedroom, Couch, Desk, Mirror, Spotlight, CityRun, VoidStage, PunchingBag, Stairs, Summit, Calendar, EndCard, ...)
  src/lib/fx/        (Backdrop/Vignette, Glow, Dust, SpeedLines, Particles, RewardBurst)
  src/lib/camera/    (Camera push/pan/shake, Parallax)
  src/lib/hud/       (TopicHUD, ClockHUD)
  src/lib/audio/     (SfxLayer, MusicLayer, makeGrid, duckGain)
  src/lib/theme.ts   (palette + accent per film)
```
Composition ids: kebab-case only (`loneliness-film`, `loneliness-mirror`).
The `lib/` grows across films: before writing a component, check whether it exists and reuse/extend it.
Film #1 builds the core library; later films should mostly be a new `script.ts` + a few new sets.

## 3. Data-driven timeline

`FilmScript { slug, title, slogan, accent, hud?, music[], scenes: SceneSpec[] }`
`SceneSpec { id, kind, durationInFrames, transitionIn: 'dip'|'cut'|'cutSettle'|'fadeCut', day?, dayRoll?, texts[], sfx[], camera?, shakes?, params }`
- All frames inside a scene are **local** (0 = first frame of the scene).
- `sec()` rounds to integers. Durations positive integers.
- `validateScript()` runs at module load and throws (ids kebab-case/unique, texts inside the scene and long
  enough to read: ≥ 18 + 7.5 × words frames, sfx inside the scene).
- Beat/BPM helpers (`makeGrid`) produce the frame numbers used by both animation and audio cues.
- The screenplay from `01-story-engine.md` §6 maps 1:1 onto `scenes[]` (one shot block = one SceneSpec).

## 4. Global layers & dips (how to reproduce the measured transitions)

Use `<Series>` (hard cuts) for the scenes and draw transitions yourself rather than TransitionSeries
crossfades — the measured "dip" has no hold and asymmetric timing:
```
<AbsoluteFill>
  <Series> ...scenes (each: camera group + screen-space text + DAY counter)... </Series>
  <DipOverlay boundaries={sceneStarts} out={10} in={20} />   // black rect, opacity from global frame
  <TopicHUD />  <ClockHUD />                                  // above the dip: never fades
  <Letterbox />                                               // 96 px bars, top-most
  <MusicLayer/> <SfxLayer/>
</AbsoluteFill>
```
DipOverlay: for a boundary at frame b: opacity = interpolate(f, [b−out, b], [0,1], ease-in) then
interpolate(f, [b, b+in], [1,0], linear). For `cutSettle` scenes add a 9 f camera scale 1.04→1.00 instead.
If you prefer TransitionSeries, remember total = Σ sequences − Σ transitions and never put two transitions
next to each other; but the custom overlay matches the reference better.

## 5. Determinism & performance

Library choice: plain SVG + Remotion `interpolate`/`spring`/`Easing` + `@remotion/paths`/`noise`/`shapes`.
**Do not use framer-motion, GSAP, CSS transitions/Tailwind animations** — they run on wall-clock time and
break frame-accurate rendering. Formats: 1920×1080 @30 fps films; Shorts = separate 1080×1920 compositions
with reflowed layout (not a crop). Timestamp → frame: `Math.round(sec * fps)`.
Particles: keep SVG nodes ≲ 150 and generate them with `useMemo` + `random(seed)`; for dense effects (confetti,
heart rain, slot sparkles, rain) draw on a `<canvas>` inside the frame (redraw from the frame number with a
`useEffect` keyed on `frame`, wrapped in `useDelayRender` only if loading images).

- Banned: `Math.random`, `Date`, timers, CSS `@keyframes`/`transition`, SMIL, effect-driven state, GIFs.
- `random('stable-seed')`, `noise2D(seed,x,y)`; seeds from stable ids (`${cue.id}-${i}`), not array indices alone.
- Clamp every `interpolate`. Springs start with `delay`.
- Glows via gradients / stacked copies; ≤ 2 small blur filters per frame; never animate stdDeviation.
- Memoise static sets (`React.memo`, `useMemo` for paths); particles ≤ ~150 nodes.
- 1920×1080 @ 30 fps; JPEG frames (template default); fonts via `loadFont` with explicit weights + subsets at module top level.

## 6. QA loop (do not skip — look at the pictures)

```powershell
npx tsc --noEmit
npx remotion compositions src/index.ts
# key-frame stills: start+5 and end-2 of every scene, every text midpoint, every impact frame
npx remotion render src/index.ts <slug>-film out/qa/<slug> "--frames=15,90,222,396,500,1500,1800,3600,4400" --scale=0.5 --image-format=jpeg
```
Open every still with the Read tool and check against `03-visual-canon.md`:
- letterbox 96/96 · background near-black with vignette · floor line present
- text: correct role colour, position, size; one message at a time; inside safe area; not over the hero's face
- DAY counter gray at top-left · HUD under the top bar
- limbs attached at shoulders/hips; near limbs outlined, far limbs translucent; body has no outline
- shadow glow not clipped, accent correct, face state right
- composition leaves the upper third free for text; nothing in the bottom 8 %
- no unstyled/missing font or asset (black or white boxes)

Fix → re-render stills → then a draft: 
`npx remotion render src/index.ts <slug>-film out/draft/<slug>.mp4 --scale=0.5 --crf=28 --x264-preset=veryfast`
Check the draft for timing (pull frames with ffmpeg at the milestone timestamps if needed, e.g.
`ffmpeg -ss 00:00:13 -i out/draft/x.mp4 -frames:v 1 out/qa/t13.png`). Final master:
`npx remotion render src/index.ts <slug>-film out/<slug>.mp4 --codec=h264 --crf=18`
Optional loudness pass: `ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -c:v copy out.mp4`.
Scene iteration: render a single scene composition (`<slug>-<scene>`) instead of the full film.

## 7. Windows / PowerShell gotchas

- `npx.ps1 cannot be loaded` → use `npx.cmd`.
- Quote arguments containing commas: `"--frames=0,30,60"`.
- `--props` needs a JSON file, not inline JSON.
- Remotion logs to stderr: judge success by `$LASTEXITCODE`, don't use `2>&1`.
- First render downloads Chrome Headless Shell (network needed once).
- EBUSY/EPERM → OneDrive/antivirus or an open player holding `out/*.mp4`.
- Long renders/OOM → lower `--concurrency` or render `--frames=a-b` chunks and concat with ffmpeg.
