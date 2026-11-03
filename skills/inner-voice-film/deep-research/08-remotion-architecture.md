# 08 — Remotion Production Architecture

Research agent 08 of 10 · Specialty: the engineering backbone of the future skill (Remotion + React + SVG, deterministic, data-driven).
Researched on 2026-10-14 against the live docs at remotion.dev and the npm registry.

> **Verified version:** `remotion@4.0.535` (npm `latest`, checked with `https://registry.npmjs.org/remotion/latest`).
> `@remotion/media@4.0.535` is also current and depends on `remotion@4.0.535` exactly.
> **All `@remotion/*` packages must have the same version.** Install them with `npx remotion add …` so the versions stay in lockstep.

Legend: **[V]** means I confirmed it in the current docs or registry during this research. **[M]** means it comes from my prior knowledge of Remotion v4 and should be checked once with `--help` or the docs page before the skill relies on it.

---

## 0. Key facts verified in the current docs

| Topic | Current fact | Source |
|---|---|---|
| Scaffold | `npx create-video@latest --yes --blank <dir>` runs without prompts. `--yes` needs a template flag and a directory (available since v4.0.439). The command fails if run inside an existing git repo. **[V]** | https://www.remotion.dev/docs/cli/create-video |
| Tailwind | As of **v4.0.534**, Tailwind is **not** installed by default. Pass `--tailwind` to get it; `--no-tailwind` is the default. **[V]** We do not need Tailwind because the work is pure SVG. | same |
| Agent skills | `--yes` skips skill installation. Install them later with `npx skills add remotion-dev/skills`. **[V]** | https://www.remotion.dev/docs/ai/skills |
| Node | Node 16+ (or Bun 1.0.3+). Node 24.19 works. **[V]** | https://www.remotion.dev/docs |
| Blank template deps | `remotion`, `@remotion/cli`, `react@19.2.3`, `react-dom@19.2.3`; dev: `typescript@5.9.3`, `@remotion/eslint-config-flat`, `eslint@9`, `prettier`, `@types/react`, `@types/web`. **[V]** | github.com/remotion-dev/template-empty |
| Template config | `remotion.config.ts`: `Config.setRspack(true)`, `Config.setVideoImageFormat("jpeg")`, `Config.setOverwriteOutput(true)`, `Config.setDefaultPremountInSeconds(2)`. **[V]** | same |
| Audio | **`<Audio>` from `@remotion/media` is the recommended component.** The old `<Audio>` from `remotion` was renamed to **`<Html5Audio>`**, and the media Audio falls back to it automatically. The `volume={(f)=>…}` callback is "no longer recommended". Compute a **number** with `useCurrentFrame()` + `interpolate()` instead. `trimAfter` is deprecated; use `trimBefore` + `durationInFrames`. **[V]** | https://www.remotion.dev/docs/media/audio · https://www.remotion.dev/docs/html5-audio |
| Transitions | `TransitionSeries` with `.Sequence`, `.Transition` and `.Overlay` (the overlay arrived in 4.0.415). Total length = Σ sequences − Σ transitions; overlays do not shorten the film. A transition must not be longer than either neighbouring sequence. Two transitions or overlays may not sit next to each other. `layout="none"` is deprecated and will throw in v5. **[V]** | https://www.remotion.dev/docs/transitions/transitionseries |
| Timings | `linearTiming({durationInFrames})` and `springTiming({config:{damping:200}})`. For example, `springTiming({config:{damping:200}}).getDurationInFrames({fps:30})` returns `23`. **[V]** | same |
| Presentations | `fade` from `@remotion/transitions/fade`. `slide({direction})` from `/slide`, where direction is `from-left/right/top/bottom`. `wipe({direction})` from `/wipe`, which also accepts diagonals such as `from-top-left`. **[V]** `flip`, `clockWipe` (`/clock-wipe`), `iris` and `none` **[M]**. | /docs/transitions/presentations/slide, /wipe |
| Fonts | `import {loadFont} from '@remotion/google-fonts/<Font>'`, then `loadFont('normal', {weights:['400'], subsets:['latin']})`. This **blocks the render automatically** until the font is ready. Weights and subsets become **required in v5**, so always pass them. **[V]** | https://www.remotion.dev/docs/google-fonts/load-font |
| delayRender | Prefer the `useDelayRender()` hook, which returns `{delayRender, continueRender, cancelRender}`. Create the handle inside `useState`. The timeout defaults to 30 s and can be changed per call with `timeoutInMilliseconds`; `{retries}` is also available. **[V]** | https://www.remotion.dev/docs/delay-render |
| random | `random(seed: string\|number)` returns a value in [0, 1]. `Math.random()` gives different values in different render threads, and the Remotion ESLint config warns about it. **[V]** | https://www.remotion.dev/docs/random |
| noise | `noise2D(seed, x, y)` returns a value in [-1, 1]; `noise3D` and `noise4D` also exist. Import from `@remotion/noise`. **[V]** | https://www.remotion.dev/docs/noise/noise-2d |
| paths | `evolvePath(progress, d)` returns `{strokeDasharray, strokeDashoffset}`. Import from `@remotion/paths`. **[V]** | https://www.remotion.dev/docs/paths/evolve-path |
| spring | Defaults are `mass 1, damping 10, stiffness 100, overshootClamping false`. Options include `durationInFrames`, `delay` and `reverse`, applied in the order durationInFrames, then reverse, then delay. **[V]** | https://www.remotion.dev/docs/spring |
| calculateMetadata | `CalculateMetadataFunction<Props>` receives `({props, defaultProps, abortSignal, compositionId, isRendering})` and returns `{durationInFrames, width, height, fps, props, defaultOutName, defaultCodec, …}`. **[V]** | https://www.remotion.dev/docs/calculate-metadata |
| Sequence premount | In the Studio, the default `premountFor` is 2 s (since 4.0.535). **[V]** | https://www.remotion.dev/docs/sequence |
| Render CLI | `npx remotion render <entry>? <comp-id> <out>`. The default codec is h264 and the default CRF is **18** (range 1–51). `--scale` accepts values from 0 to 16. `--frames=0,30,60` writes an image sequence, while `--frames=0-99` writes a video. **On Windows shells, inline JSON in `--props` is not supported, so pass a file.** **[V]** | https://www.remotion.dev/docs/cli/render · /docs/encoding |
| Still CLI | `npx remotion still <entry>? <comp-id> <out.png> --frame=N --scale=… --image-format=png`. **[V]** | https://www.remotion.dev/docs/cli/still |
| Performance | Use `npx remotion benchmark` to choose `--concurrency`. `filter: blur()`, `drop-shadow`, `box-shadow`, `text-shadow` and gradients all depend on the GPU, so replace them with **precomputed images** where you can. JPEG frames render faster than PNG. Use `--log=verbose` to see the slowest frames. **[V]** | https://www.remotion.dev/docs/performance |
| `--gl` | Locally the 4.x default is `null`, which lets Chrome decide; 5.0 will default to `angle`. Only change it if you use WebGL. **[V]** | https://www.remotion.dev/docs/gl-options |
| `npx remotion add` | `npx remotion add pkgA pkgB …` installs packages at the same version as your existing Remotion install and accepts several packages at once. **[V]** | https://www.remotion.dev/docs/cli/add |
| License | Free for individuals, for-profit companies with **3 or fewer staff**, non-profits, and evaluation. Anyone else needs a Company License (remotion.pro/license). A solo YouTube creator qualifies for the free license. **[V]** | https://github.com/remotion-dev/remotion/blob/main/LICENSE.md |

---

## 1. Recommended project structure (multi-film studio repo)

> ⚠️ **Create the Remotion project OUTSIDE OneDrive**, for example at `C:\dev\dayone-studio`. OneDrive sync locks files in `node_modules` and `out/`, which causes EBUSY/EPERM errors and slows `npm i` and renders badly. The folder path also contains a space ("2d animation"), which forces quoting everywhere. If it must stay in the current folder, pause OneDrive sync while installing and rendering.

```
dayone-studio/
├─ package.json
├─ remotion.config.ts
├─ tsconfig.json
├─ eslint.config.mjs
├─ public/
│  ├─ audio/
│  │  ├─ music/              # discipline-theme.mp3 …  (kebab-case, ASCII names only)
│  │  └─ sfx/                # alarm-ring.mp3, slap.mp3, whoosh.mp3, punch.mp3, glass-shatter.mp3, heartbeat.mp3
│  └─ img/                   # pre-blurred glow sprites (glow-red-512.png), grain.png, vignette.png
├─ props/                    # JSON prop files for CLI (--props=props/x.json) — Windows needs files, not inline JSON
├─ scripts/
│  ├─ keyframes.mjs          # prints QA frame list from a film script
│  └─ qa.ps1                 # tsc → stills → draft render pipeline
├─ out/                      # renders (gitignored)
└─ src/
   ├─ index.ts               # registerRoot(RemotionRoot)
   ├─ Root.tsx               # one <Composition> per film + per-scene comps + <Still>s for thumbnails
   ├─ films/
   │  ├─ registry.ts         # export const FILMS = [discipline, loneliness, …]
   │  ├─ discipline/
   │  │  ├─ script.ts        # FilmScript data — SINGLE SOURCE OF TRUTH
   │  │  └─ scenes/          # film-specific scene components (only if not generic)
   │  │     ├─ BedroomAlarm.tsx
   │  │     ├─ PunchingBag.tsx
   │  │     └─ Summit.tsx
   │  └─ loneliness/
   │     ├─ script.ts
   │     └─ scenes/…
   └─ lib/
      ├─ timeline/
      │  ├─ types.ts         # FilmScript, SceneSpec, TextCue, SfxCue, TransitionSpec
      │  ├─ time.ts          # sec(), fps constant, beats helpers
      │  ├─ compute.ts       # sceneStarts(), filmDuration(), validateScript()
      │  └─ FilmRenderer.tsx # script → TransitionSeries
      ├─ scenes/
      │  ├─ registry.ts      # kind → component map (generic reusable scenes)
      │  ├─ BlackHookText.tsx
      │  ├─ SpotlightRockBottom.tsx
      │  ├─ MirrorScene.tsx
      │  └─ EndCard.tsx
      ├─ character/
      │  ├─ Hero.tsx         # rigged hero (pose props → joint angles), pivots via transform-origin in SVG coords
      │  ├─ poses.ts         # named poses: sleep, sit, run1..n, pushupUp/Down, punch…
      │  ├─ Face.tsx         # brows/eyes/mouth expressions + sweat drop
      │  └─ Shadow.tsx       # red-glow antagonist (scale prop: giant → tiny)
      ├─ text/
      │  ├─ fonts.ts         # loadFont() once, export fontFamily
      │  ├─ CaptionText.tsx  # narrator (white) / voice (red) / info roles
      │  ├─ DayCounter.tsx   # top-left gray "DAY 47"
      │  ├─ InnerVoice.tsx   # red text + shadow mouth sync
      │  ├─ ShatterText.tsx  # per-letter break-apart on impact frame
      │  └─ BigCounter.tsx   # glowing push-up counter
      ├─ sets/               # Bedroom, Desk, CityParallax, Stairs, Summit, Gym, Mirror (pure SVG, memoized)
      ├─ fx/
      │  ├─ Vignette.tsx     # radialGradient — no CSS blur
      │  ├─ Glow.tsx         # gradient/sprite-based glow
      │  ├─ Dust.tsx         # seeded particles
      │  ├─ SpeedLines.tsx
      │  └─ Boil.tsx         # hand-drawn line jitter via noise2D (stepped 12fps)
      ├─ camera/
      │  ├─ Camera.tsx       # keyframed pan/zoom/shake wrapper
      │  └─ Parallax.tsx     # depth-factor layers
      ├─ audio/
      │  ├─ Sfx.tsx
      │  └─ Music.tsx        # numeric volume with fade in/out/ducking
      ├─ anim/
      │  ├─ easing.ts        # named Easing presets
      │  └─ helpers.ts       # fadeInOut(), pop(), clampInterp(), stepped(), shake()
      └─ theme.ts            # palette tokens (#0d0d0d bg, #e8e4d8 hero, #ff3b30 red …)
```

### `src/index.ts`

```ts
import {registerRoot} from 'remotion';
import {RemotionRoot} from './Root';

registerRoot(RemotionRoot);
```

### `src/Root.tsx`: one composition per film, per-scene compositions, and thumbnails

Composition IDs may contain only `a-z A-Z 0-9 -` (plus CJK characters), so **do not use underscores or dots** **[M]**. Use `<Folder>` to group compositions in the Studio sidebar.

```tsx
import React from 'react';
import {Composition, Folder, Still} from 'remotion';
import {FILMS} from './films/registry';
import {FilmRenderer, SceneOnly} from './lib/timeline/FilmRenderer';
import {filmDuration} from './lib/timeline/compute';
import {FPS, WIDTH, HEIGHT} from './lib/timeline/time';
import {Thumbnail} from './lib/scenes/Thumbnail';

export const RemotionRoot: React.FC = () => (
  <>
    {FILMS.map((film) => (
      <Folder key={film.slug} name={film.slug}>
        {/* Full film. Duration is derived from the script, which is the single source of truth. */}
        <Composition
          id={`${film.slug}-film`}
          component={FilmRenderer}
          defaultProps={{slug: film.slug}}
          durationInFrames={filmDuration(film)}
          fps={FPS}
          width={WIDTH}
          height={HEIGHT}
        />
        {/* One composition per scene for fast preview and stills (no transitions). */}
        {film.scenes.map((scene) => (
          <Composition
            key={scene.id}
            id={`${film.slug}-${scene.id}`}
            component={SceneOnly}
            defaultProps={{slug: film.slug, sceneId: scene.id}}
            durationInFrames={scene.durationInFrames}
            fps={FPS}
            width={WIDTH}
            height={HEIGHT}
          />
        ))}
        <Still
          id={`${film.slug}-thumb`}
          component={Thumbnail}
          defaultProps={{slug: film.slug}}
          width={1280}
          height={720}
        />
      </Folder>
    ))}
  </>
);
```

> We pass only `{slug}` as props and look the script up in the registry instead of passing the whole script object. This keeps props tiny and JSON-serializable, avoids Studio serialisation problems, and means a single edit to `script.ts` updates the film, the scene compositions and the duration. If the skill should later render films from a JSON file passed with `--props`, switch to `calculateMetadata`, as shown in §2.6.

---

## 2. Data-driven timeline pattern

### 2.1 `src/lib/timeline/time.ts`

```ts
export const FPS = 30;
export const WIDTH = 1920;
export const HEIGHT = 1080;

/** seconds → frames (rounded, always integer) */
export const sec = (s: number): number => Math.round(s * FPS);
/** "m:ss.f" → frames — handy for copying timestamps from reference scripts */
export const tc = (t: string): number => {
  const [m, s] = t.split(':');
  return sec(Number(m) * 60 + Number(s));
};
/** Lay out N consecutive text beats inside a scene, each `len` long with `gap` between */
export const beats = (start: number, len: number, gap: number, n: number) =>
  Array.from({length: n}, (_, i) => ({start: start + i * (len + gap), end: start + i * (len + gap) + len}));
```

### 2.2 `src/lib/timeline/types.ts`

```ts
/** All frame numbers in a SceneSpec are LOCAL to the scene (0 = first frame of the scene). */
export type Frame = number;

export type TextRole =
  | 'narrator'   // white, centered/lower — lesson lines ("He believed it.")
  | 'voice'      // red — inner voice ("skip the gym.")
  | 'info'       // red/white small — situational info ("just 5 more minutes...", "again.")
  | 'title'      // end-card title ("DISCIPLINE")
  | 'tagline';   // end-card tagline ("Day one, or one day.")

export type TextAnim = 'fade' | 'typewriter' | 'pop' | 'wobble' | 'shatter' | 'whisper';

export type TextPosition =
  | 'center' | 'upper' | 'lower' | 'top-left'
  | {x: number; y: number}; // px in 1920x1080 space (anchor = center)

export interface TextCue {
  id: string;
  text: string;
  role: TextRole;
  start: Frame;
  end: Frame;                 // exclusive
  position?: TextPosition;
  size?: number;              // px; defaults by role
  anim?: TextAnim;
  /** For 'shatter': local frame of impact (text breaks apart) */
  impactAt?: Frame;
  /** Character mouth/eyes react while visible (InnerVoice glow pulse) */
  speaker?: 'hero' | 'shadow' | 'none';
}

export interface DayCounterCue {
  label: string;              // "DAY 1", "DAY 47", "DAY 270"
  start?: Frame;              // default 0
  end?: Frame;                // default scene end
  /** count-up animation e.g. DAY 30 → DAY 365 for montage */
  countTo?: number;
}

export interface SfxCue {
  src: string;                // path under public/, e.g. 'audio/sfx/alarm-ring.mp3'
  at: Frame;
  volume?: number;            // 0..1
  durationInFrames?: number;  // trim length
  trimBefore?: Frame;
}

export type TransitionKind = 'cut' | 'fade' | 'slide' | 'wipe' | 'fadeThroughBlack';

export interface TransitionSpec {
  kind: TransitionKind;
  durationInFrames: number;   // ignored for 'cut'
  direction?: 'from-left' | 'from-right' | 'from-top' | 'from-bottom';
  timing?: 'linear' | 'spring';
}

export interface CameraKey {
  at: Frame;
  x?: number;                 // pan px
  y?: number;
  zoom?: number;              // 1 = none
  ease?: 'inOut' | 'out' | 'in' | 'linear';
}

export interface ShakeCue {at: Frame; durationInFrames: number; intensity: number}

export interface SceneSpec<P extends Record<string, unknown> = Record<string, unknown>> {
  id: string;                 // kebab-case, unique within film → composition id `${slug}-${id}`
  kind: string;               // key in scene registry (generic or film-specific)
  durationInFrames: number;
  /** transition INTO this scene from previous one (ignored for first scene) */
  transitionIn?: TransitionSpec;
  dayCounter?: DayCounterCue;
  texts?: TextCue[];
  sfx?: SfxCue[];
  camera?: CameraKey[];
  shakes?: ShakeCue[];
  /** free per-kind parameters (pose sequence, clock times, lighting mood, shadow scale …) */
  params?: P;
  /** chapter marker for YouTube description, e.g. "The mirror" */
  chapter?: string;
}

export interface MusicCue {
  src: string;
  start: Frame;               // GLOBAL frame
  end?: Frame;                // GLOBAL frame
  volume: number;
  fadeIn?: number;
  fadeOut?: number;
  /** global frame ranges where music ducks (e.g. impact silence) */
  duck?: {from: Frame; to: Frame; level: number}[];
}

export interface FilmScript {
  slug: string;               // kebab-case
  title: string;              // "DISCIPLINE"
  tagline: string;            // "Day one, or one day."
  theme?: Partial<Record<'accent' | 'bg' | 'hero', string>>;
  music?: MusicCue[];
  scenes: SceneSpec[];
}
```

### 2.3 `src/lib/timeline/compute.ts`: duration, scene offsets, validation

```ts
import type {FilmScript, SceneSpec} from './types';

const tLen = (s: SceneSpec, i: number) =>
  i === 0 || !s.transitionIn || s.transitionIn.kind === 'cut' ? 0 : s.transitionIn.durationInFrames;

/** TransitionSeries rule: total = Σ sequences − Σ transitions (docs-verified) */
export const filmDuration = (f: FilmScript): number =>
  f.scenes.reduce((acc, s, i) => acc + s.durationInFrames - tLen(s, i), 0);

/** Global start frame of every scene (needed for music ducking, chapters, QA keyframes) */
export const sceneStarts = (f: FilmScript): number[] => {
  const starts: number[] = [];
  let cursor = 0;
  f.scenes.forEach((s, i) => {
    cursor -= tLen(s, i);
    starts.push(cursor);
    cursor += s.durationInFrames;
  });
  return starts;
};

export const validateScript = (f: FilmScript): string[] => {
  const errs: string[] = [];
  const ids = new Set<string>();
  f.scenes.forEach((s, i) => {
    if (!/^[a-z0-9-]+$/.test(s.id)) errs.push(`${s.id}: id must be kebab-case`);
    if (ids.has(s.id)) errs.push(`${s.id}: duplicate id`);
    ids.add(s.id);
    if (!Number.isInteger(s.durationInFrames) || s.durationInFrames <= 0)
      errs.push(`${s.id}: durationInFrames must be positive int`);
    const t = tLen(s, i);
    const prev = f.scenes[i - 1];
    if (t > s.durationInFrames || (prev && t > prev.durationInFrames))
      errs.push(`${s.id}: transition longer than adjacent scene (TransitionSeries will throw)`);
    for (const c of s.texts ?? []) {
      if (c.start < 0 || c.end > s.durationInFrames || c.end <= c.start)
        errs.push(`${s.id}/${c.id}: text out of scene bounds [${c.start},${c.end})`);
      // readability: ≥ 0.25s per word + 0.6s base (30fps)
      const minLen = Math.round(18 + 7.5 * c.text.split(/\s+/).length);
      if (c.end - c.start < minLen) errs.push(`${s.id}/${c.id}: on screen too short (<${minLen}f)`);
    }
    for (const x of s.sfx ?? []) if (x.at < 0 || x.at >= s.durationInFrames)
      errs.push(`${s.id}: sfx ${x.src} at ${x.at} outside scene`);
  });
  return errs;
};
```

Run `validateScript` at module load in `Root.tsx` and **throw** if it returns any errors. The Studio then shows them immediately, and `npx tsc` together with a single still render will catch them in CI or QA.

### 2.4 `src/lib/timeline/FilmRenderer.tsx`: script to TransitionSeries

```tsx
import React from 'react';
import {AbsoluteFill, Sequence} from 'remotion';
import {Audio} from '@remotion/media';
import {staticFile} from 'remotion';
import {TransitionSeries, linearTiming, springTiming} from '@remotion/transitions';
import {fade} from '@remotion/transitions/fade';
import {slide} from '@remotion/transitions/slide';
import {wipe} from '@remotion/transitions/wipe';
import {getFilm} from '../../films/registry';
import {SCENES} from '../scenes/registry';
import type {SceneSpec, TransitionSpec} from './types';
import {CaptionLayer} from '../text/CaptionLayer';
import {DayCounter} from '../text/DayCounter';
import {Music} from '../audio/Music';
import {Vignette} from '../fx/Vignette';
import {theme} from '../theme';

const presentationOf = (t: TransitionSpec) => {
  switch (t.kind) {
    case 'slide': return slide({direction: t.direction ?? 'from-right'});
    case 'wipe': return wipe({direction: t.direction ?? 'from-left'});
    default: return fade(); // 'fade' and 'fadeThroughBlack' (bg is black → fade reads as dip)
  }
};
const timingOf = (t: TransitionSpec) =>
  t.timing === 'spring'
    ? springTiming({config: {damping: 200}, durationInFrames: t.durationInFrames})
    : linearTiming({durationInFrames: t.durationInFrames});

/** Everything a scene needs, layered: set/character (kind) → captions → day counter → sfx */
const SceneShell: React.FC<{scene: SceneSpec}> = ({scene}) => {
  const Body = SCENES[scene.kind];
  if (!Body) throw new Error(`Unknown scene kind "${scene.kind}"`);
  return (
    <AbsoluteFill style={{backgroundColor: theme.bg}}>
      <Body scene={scene} />
      <Vignette />
      {scene.dayCounter && <DayCounter cue={scene.dayCounter} sceneLength={scene.durationInFrames} />}
      <CaptionLayer cues={scene.texts ?? []} />
      {(scene.sfx ?? []).map((s, i) => (
        <Sequence key={i} from={s.at} durationInFrames={s.durationInFrames} layout="none" name={`sfx:${s.src}`}>
          <Audio src={staticFile(s.src)} volume={s.volume ?? 1} trimBefore={s.trimBefore} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};

export const FilmRenderer: React.FC<{slug: string}> = ({slug}) => {
  const film = getFilm(slug);
  return (
    <AbsoluteFill style={{backgroundColor: theme.bg}}>
      <TransitionSeries>
        {film.scenes.flatMap((scene, i) => {
          const nodes: React.ReactNode[] = [];
          const t = scene.transitionIn;
          if (i > 0 && t && t.kind !== 'cut') {
            nodes.push(
              <TransitionSeries.Transition key={`t-${scene.id}`} presentation={presentationOf(t)} timing={timingOf(t)} />,
            );
          }
          nodes.push(
            <TransitionSeries.Sequence key={scene.id} durationInFrames={scene.durationInFrames} name={scene.id}>
              <SceneShell scene={scene} />
            </TransitionSeries.Sequence>,
          );
          return nodes;
        })}
      </TransitionSeries>
      {(film.music ?? []).map((m, i) => <Music key={i} cue={m} />)}
    </AbsoluteFill>
  );
};

/** Single-scene preview composition (no transitions) */
export const SceneOnly: React.FC<{slug: string; sceneId: string}> = ({slug, sceneId}) => {
  const scene = getFilm(slug).scenes.find((s) => s.id === sceneId)!;
  return <SceneShell scene={scene} />;
};
```

Notes:
- Inside a `TransitionSeries.Sequence`, `useCurrentFrame()` is **local** to the scene, so every frame number in `SceneSpec` is local. **[V]** (the Sequence docs: children see frame 0 at `from`, and this cascades).
- For `springTiming`, passing `durationInFrames` forces the spring to stretch to the declared length **[M]**. Without it, the length depends on the spring config (23 frames for damping 200 at 30 fps **[V]**), and `filmDuration` would drift. The skill should **always declare an explicit transition duration**.
- Sfx `<Sequence layout="none">` is fine for audio. The `layout="none"` deprecation applies only to `TransitionSeries` scenes **[V]**.
- Hard cuts are simply consecutive sequences with no `.Transition` between them. Most of the reference film uses hard cuts plus fades on black.

### 2.5 `src/films/discipline/script.ts`: a sample (first act and ending, abridged)

```ts
import type {FilmScript} from '../../lib/timeline/types';
import {sec, beats} from '../../lib/timeline/time';

const fadeIn = (s = 0.5) => ({kind: 'fade' as const, durationInFrames: sec(s)});

export const discipline: FilmScript = {
  slug: 'discipline',
  title: 'DISCIPLINE',
  tagline: 'Day one, or one day.',
  music: [{src: 'audio/music/discipline-theme.mp3', start: 0, volume: 0.6, fadeIn: sec(2), fadeOut: sec(3),
    duck: [{from: sec(48), to: sec(56), level: 0.15}]}],
  scenes: [
    {
      id: 'hook', kind: 'blackHookText', durationInFrames: sec(3.5), chapter: 'Every day started the same',
      texts: [{id: 'h1', text: 'Every day started the same.', role: 'narrator', start: sec(0.3), end: sec(3.2), anim: 'typewriter', position: 'center'}],
    },
    {
      id: 'alarm', kind: 'bedroomAlarm', durationInFrames: sec(5), transitionIn: fadeIn(),
      params: {clock: '5:00', action: 'slap', light: 'night'},
      texts: [{id: 'i1', text: 'just 5 more minutes...', role: 'info', start: sec(2.2), end: sec(4.8), anim: 'fade', position: 'upper'}],
      sfx: [{src: 'audio/sfx/alarm-ring.mp3', at: 0, durationInFrames: sec(1.6)},
            {src: 'audio/sfx/slap.mp3', at: sec(1.6), volume: 0.9}],
    },
    {
      id: 'oversleep', kind: 'bedroomAlarm', durationInFrames: sec(3.5),
      params: {clock: '8:47', clockSpinFrom: '5:00', expression: 'panic', sweat: true},
      texts: [{id: 'i2', text: 'again.', role: 'info', start: sec(1.6), end: sec(3.4), anim: 'pop', position: 'upper'}],
      shakes: [{at: sec(1.2), durationInFrames: 8, intensity: 6}],
    },
    {
      id: 'couch-day1', kind: 'couchPhone', durationInFrames: sec(5), transitionIn: fadeIn(0.4),
      dayCounter: {label: 'DAY 1'},
      texts: [{id: 'v1', text: 'skip the gym.', role: 'voice', speaker: 'shadow', start: sec(1.5), end: sec(4.5), anim: 'whisper'}],
      params: {shadowScale: 1},
    },
    {
      id: 'montage-fail', kind: 'montage', durationInFrames: sec(6),
      dayCounter: {label: 'DAY 30', countTo: 365},
      params: {shots: ['snooze', 'phoneNight', 'lateEating', 'deskAsleep'], shotLen: sec(1.5)},
    },
    // … mirror, rock-bottom spotlight, 5:00 calm wake, run, push-ups, bag (shatter), stairs, summit …
    {
      id: 'bag-day64', kind: 'punchingBag', durationInFrames: sec(7), transitionIn: fadeIn(0.3),
      dayCounter: {label: 'DAY 64'},
      texts: beats(sec(0.5), sec(1.6), sec(0.3), 3).map((b, i) => ({
        id: `w${i}`, text: ["you're lazy", 'nobody cares', 'quit'][i], role: 'voice' as const,
        start: b.start, end: b.end + sec(0.6), anim: 'shatter' as const, impactAt: b.end,
        size: 120, position: 'upper' as const,
      })),
      sfx: [0, 1, 2].map((i) => ({src: 'audio/sfx/punch.mp3', at: sec(0.5) + i * sec(1.9) + sec(1.6), volume: 1})),
    },
    {
      id: 'end-card', kind: 'endCard', durationInFrames: sec(8), transitionIn: fadeIn(1),
      texts: [
        {id: 't', text: 'DISCIPLINE', role: 'title', start: sec(0.5), end: sec(8), anim: 'fade'},
        {id: 'tg', text: 'Day one, or one day.', role: 'tagline', start: sec(2.5), end: sec(8), anim: 'typewriter'},
      ],
    },
  ],
};
```

`src/films/registry.ts`:

```ts
import {discipline} from './discipline/script';
import {validateScript} from '../lib/timeline/compute';
import type {FilmScript} from '../lib/timeline/types';

export const FILMS: FilmScript[] = [discipline];
for (const f of FILMS) {
  const errs = validateScript(f);
  if (errs.length) throw new Error(`Script "${f.slug}" invalid:\n` + errs.join('\n'));
}
export const getFilm = (slug: string) => {
  const f = FILMS.find((x) => x.slug === slug);
  if (!f) throw new Error(`Unknown film ${slug}`);
  return f;
};
```

`src/lib/scenes/registry.ts` (generic scenes and film-specific scenes share one map, so the skill can reuse kinds across topics):

```ts
import type React from 'react';
import type {SceneSpec} from '../timeline/types';
import {BlackHookText} from './BlackHookText';
import {SpotlightRockBottom} from './SpotlightRockBottom';
import {EndCard} from './EndCard';
import {BedroomAlarm} from '../../films/discipline/scenes/BedroomAlarm';
// …
export type SceneComponent = React.FC<{scene: SceneSpec}>;
export const SCENES: Record<string, SceneComponent> = {
  blackHookText: BlackHookText,
  spotlight: SpotlightRockBottom,
  endCard: EndCard,
  bedroomAlarm: BedroomAlarm,
  // couchPhone, montage, mirror, run, pushup, punchingBag, stairs, summit …
};
```

### 2.6 Optional: a JSON-driven film through `calculateMetadata`, so the skill can render a script with no code change

```tsx
import {CalculateMetadataFunction, Composition} from 'remotion';
import type {FilmScript} from './lib/timeline/types';
import {filmDuration, validateScript} from './lib/timeline/compute';
import {FilmFromProps} from './lib/timeline/FilmFromProps'; // same as FilmRenderer but takes {film}

const calc: CalculateMetadataFunction<{film: FilmScript}> = async ({props}) => {
  const errs = validateScript(props.film);
  if (errs.length) throw new Error(errs.join('\n'));
  return {durationInFrames: filmDuration(props.film), defaultOutName: props.film.slug, defaultCodec: 'h264'};
};

<Composition id="dynamic-film" component={FilmFromProps} calculateMetadata={calc}
  durationInFrames={1} fps={30} width={1920} height={1080}
  defaultProps={{film: placeholderFilm}} />
```

```powershell
npx remotion render dynamic-film out\loneliness.mp4 --props=props\loneliness.json   # file, NOT inline JSON (Windows)
```

### 2.7 Helper libraries (skeletons the skill should generate)

`src/lib/anim/easing.ts`

```ts
import {Easing} from 'remotion';
export const EASE = {
  inOut: Easing.inOut(Easing.cubic),
  out: Easing.out(Easing.cubic),
  in: Easing.in(Easing.cubic),
  snap: Easing.bezier(0.2, 0.9, 0.1, 1),      // UI-like pop
  heavy: Easing.bezier(0.7, 0, 0.84, 0),      // slow then fall (despair)
  anticipate: Easing.bezier(0.36, 0, 0.66, -0.56), // wind-up before punch
  overshoot: Easing.bezier(0.34, 1.56, 0.64, 1),
} as const;
export const SPRING = {
  gentle: {damping: 200},                       // no bounce (text fades, camera)
  snappy: {damping: 20, stiffness: 200},        // character hits, slaps
  bouncy: {damping: 8},                         // pop-in counters
} as const;
```

`src/lib/anim/helpers.ts`

```ts
import {interpolate, random} from 'remotion';
import {noise2D} from '@remotion/noise';
const CL = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

export const lerp = (f: number, i: [number, number], o: [number, number], easing?: (t: number) => number) =>
  interpolate(f, i, o, {...CL, easing});

/** opacity for a cue [start,end) with fade frames each side */
export const fadeInOut = (f: number, start: number, end: number, fade = 8) =>
  interpolate(f, [start, start + fade, end - fade, end], [0, 1, 1, 0], CL);

/** step the frame to a lower "drawing rate" (hand-animated feel, e.g. 12fps on 30fps timeline) */
export const stepped = (f: number, fps: number, drawFps = 12) => Math.floor((f * drawFps) / fps);

/** deterministic camera shake */
export const shake = (f: number, at: number, dur: number, amp: number, seed = 'shake') => {
  const t = f - at;
  if (t < 0 || t > dur) return {x: 0, y: 0};
  const decay = 1 - t / dur;
  return {x: noise2D(seed, t * 0.6, 0) * amp * decay, y: noise2D(seed, 0, t * 0.6) * amp * decay};
};

/** hand-drawn "boil": jitter a point by ≤ amp px, changing only on drawn frames */
export const boil = (f: number, fps: number, key: string, amp = 1.2) => {
  const s = stepped(f, fps, 8);
  return {dx: (random(`${key}-x-${s}`) - 0.5) * 2 * amp, dy: (random(`${key}-y-${s}`) - 0.5) * 2 * amp};
};
```

`src/lib/text/fonts.ts`. The brief calls for a rounded, Comic-Sans-like hand font. Candidates on Google Fonts include `Patrick Hand`, `Gochi Hand`, `Short Stack` and `Comic Neue`; agent 04 decides which one.

```ts
import {loadFont} from '@remotion/google-fonts/ComicNeue';
// weights+subsets explicit → fewer requests, v5-proof; blocks render until loaded (docs)
export const {fontFamily: HAND} = loadFont('normal', {weights: ['400', '700'], subsets: ['latin']});
```

`src/lib/audio/Music.tsx` (numeric volume, as the docs now recommend):

```tsx
import {Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {Audio} from '@remotion/media';
import type {MusicCue} from '../timeline/types';

const MusicInner: React.FC<{cue: MusicCue; len: number}> = ({cue, len}) => {
  const f = useCurrentFrame(); // local to the Sequence
  const fi = cue.fadeIn ?? 0, fo = cue.fadeOut ?? 0;
  let v = interpolate(f, [0, Math.max(1, fi), len - Math.max(1, fo), len], [0, 1, 1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  for (const d of cue.duck ?? []) {
    const lf = f + cue.start; // back to global
    v *= interpolate(lf, [d.from - 6, d.from, d.to, d.to + 6], [1, d.level, d.level, 1],
      {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  }
  return <Audio src={staticFile(cue.src)} volume={v * cue.volume} />;
};

export const Music: React.FC<{cue: MusicCue}> = ({cue}) => {
  const {durationInFrames} = useVideoConfig();
  const len = (cue.end ?? durationInFrames) - cue.start;
  return (
    <Sequence from={cue.start} durationInFrames={len} layout="none" name={`music:${cue.src}`}>
      <MusicInner cue={cue} len={len} />
    </Sequence>
  );
};
```

`src/lib/camera/Camera.tsx` (keyframed pan, zoom and shake, wrapping an SVG set):

```tsx
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import type {CameraKey, ShakeCue} from '../timeline/types';
import {EASE} from '../anim/easing';
import {shake} from '../anim/helpers';

export const Camera: React.FC<{keys?: CameraKey[]; shakes?: ShakeCue[]; children: React.ReactNode}> = ({keys = [], shakes = [], children}) => {
  const f = useCurrentFrame();
  const k = keys.length ? keys : [{at: 0}];
  const frames = k.map((x) => x.at);
  const pick = (p: 'x' | 'y' | 'zoom', d: number) =>
    k.length < 2 ? (k[0][p] ?? d)
      : interpolate(f, frames, k.map((x) => x[p] ?? d), {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: EASE.inOut});
  const s = shakes.reduce((a, c) => { const o = shake(f, c.at, c.durationInFrames, c.intensity); return {x: a.x + o.x, y: a.y + o.y}; }, {x: 0, y: 0});
  return (
    <AbsoluteFill style={{transform: `translate(${-pick('x', 0) + s.x}px, ${-pick('y', 0) + s.y}px) scale(${pick('zoom', 1)})`, transformOrigin: '50% 50%'}}>
      {children}
    </AbsoluteFill>
  );
};
```

Parallax: each layer gets `translateX(-camX * depth)`, where `depth` runs from 0 for the sky to 1 for the foreground. For the city run, drive `camX = frame * speed` instead of keyframes.

Line drawing (the red wavy underline on the end card, and title strokes):

```tsx
import {evolvePath} from '@remotion/paths';
const d = 'M 660 640 Q 760 610 860 640 T 1060 640 T 1260 640';
const p = interpolate(frame, [sec(1.2), sec(2.2)], [0, 1], {extrapolateLeft:'clamp', extrapolateRight:'clamp', easing: EASE.out});
const {strokeDasharray, strokeDashoffset} = evolvePath(p, d);
<path d={d} stroke="#ff3b30" strokeWidth={8} strokeLinecap="round" fill="none"
      strokeDasharray={strokeDasharray} strokeDashoffset={strokeDashoffset} />
```

Install the extra packages with `npx remotion add @remotion/paths @remotion/noise`.

---

## 3. Determinism and performance rules (hard rules for the skill)

### Determinism. Every frame must be a pure function of `(frame, props)`.
1. **Never use** `Math.random()`, `Date.now()`, `new Date()`, `performance.now()`, `setTimeout`/`setInterval`/`requestAnimationFrame`-driven state, CSS `@keyframes`/`animation`/`transition`, SMIL `<animate>`, `useEffect`-driven animation state, or GIFs that are not driven through Remotion APIs. Several Chrome tabs render frames out of order and in parallel, so any time-based or stateful animation will flicker or desync. **[V]** (the random docs)
2. Use `random('seed-string')` for scatter, particle positions and per-letter shatter vectors. Derive the seed from stable IDs, such as `` `${cue.id}-${letterIndex}-vx` ``. Never use an array index alone, because the indices shift when the script is edited.
3. Use `noise2D/3D(seed, x, y)` for organic motion such as breathing, idle sway, shadow flicker and line boil.
4. Derive every value from `useCurrentFrame()` with `interpolate`, `spring` or `Easing`, and **clamp every interpolate** (`extrapolateLeft/Right: 'clamp'`) unless extrapolation is intentional.
5. Keep the ESLint config from the template (`@remotion/eslint-config-flat`). It warns on `Math.random` and similar patterns.
6. Frames must be integers: write `sec()` with `Math.round`. `durationInFrames` must be a positive integer.

### Performance
| Problem | Why | Do this instead |
|---|---|---|
| `filter: blur()` / `<feGaussianBlur>` on big layers every frame | GPU-dependent and heavy per frame, as the docs say **[V]** | **Glows**: a `<radialGradient>` with stops from `rgba(255,59,48,.6)` to `0`, or a **pre-blurred PNG sprite** in `public/img/` (`<Img src={staticFile('img/glow-red-512.png')}>`) whose opacity and scale you animate. **Vignette**: a radialGradient rect. **Depth-of-field**: avoid it; use darker, lower-contrast background colours. |
| Red outer glow on the shadow silhouette | Animated drop-shadow is costly | Draw the silhouette path twice: a back copy with a thick red stroke (`strokeWidth 18`, `strokeOpacity .35`, `strokeLinejoin round`) plus a gradient halo, then the black fill on top. This is cheap and gives a crisp look. If you must use an SVG filter, define it **once** with a constant `stdDeviation`, animate only `opacity`, and keep the filtered region small (set `filterUnits` to a tight box). |
| `feTurbulence` + `feDisplacementMap` for a wobbly hand-drawn line | Very expensive per frame | Jitter the path points in JS with `noise2D`/`random`, stepped at 8–12 drawing fps (`boil()` helper), or pre-author 3 path variants and cycle them. |
| Large static sets (bedroom, city) re-rendering every frame | React reconciles big SVG trees | Make set components `React.memo` with **no frame prop**, and apply movement only through a wrapper `<g transform>` or a CSS transform on the parent. Precompute heavy path strings with `useMemo`. |
| Text shadows and box shadows | GPU-dependent **[V]** | Use a stacked duplicate text with an offset and lower opacity, or a gradient sprite. |
| Many particles | Thousands of DOM nodes | Keep dust to about 40–80 small `<circle>`s generated once by `useMemo` with `random(seed)`; only their transforms depend on the frame. |
| PNG frame format | Slower than JPEG **[V]** | Keep the template's `setVideoImageFormat('jpeg')`. Use PNG only for alpha output. |

### Format and time budgets
- **1920×1080 @ 30 fps** is the default (the brief allows 60, but 30 halves render time and matches the hand-drawn feel; the stepped "on twos" boil looks better at 30). A 2:40 film is 4,800 frames.
- **Render time estimate [M, not measured]:** flat-SVG scenes take roughly 15–60 ms per frame per tab. With `--concurrency` at about half the logical cores on an 8-core or 16-thread desktop, a 4,800-frame film should take about **3–8 minutes** at full resolution and about 1–3 minutes as a `--scale=0.5` draft. Blur-heavy frames can be 5–10 times slower. Run `npx remotion benchmark` once per machine and `--log=verbose` to find the slowest frames. **[V]**
- Fonts: `@remotion/google-fonts` `loadFont()` blocks the render on its own. For a **local** font in `public/fonts/` use `@remotion/fonts` `loadFont({family, url: staticFile(...)})` **[M]**, or a manual `FontFace` wrapped in `useDelayRender()`:

```tsx
import {useDelayRender, staticFile} from 'remotion';
import {useState, useEffect} from 'react';
export const useLocalFont = (family: string, file: string) => {
  const {delayRender, continueRender, cancelRender} = useDelayRender();
  const [h] = useState(() => delayRender(`font ${family}`));
  useEffect(() => {
    const ff = new FontFace(family, `url(${staticFile(file)})`);
    ff.load().then((f) => { document.fonts.add(f); continueRender(h); }).catch(cancelRender);
  }, []);
};
```

- Load fonts at **module top-level** in `fonts.ts`, not inside a component, so they load only once.
- `staticFile()` paths are relative to `public/`. Use ASCII kebab-case file names with no spaces.

---

## 4. QA workflow (the skill MUST follow it in this order)

```powershell
# 0) from project root (quote paths with spaces!)
Set-Location "C:\dev\dayone-studio"

# 1) Type-check — must be zero errors
npx tsc --noEmit

# 2) Lint (template script: eslint src && tsc)
npx eslint src

# 3) List compositions — verifies Root.tsx + validateScript() didn't throw, shows durations
npx remotion compositions src/index.ts

# 4) Key-frame stills → LOOK AT EVERY PNG (Read tool) before full render
npx remotion still src/index.ts discipline-film out/qa/f0090.png --frame=90 --scale=0.5
npx remotion still src/index.ts discipline-bag-day64 out/qa/bag-impact.png --frame=48

#    Faster: many key frames in ONE invocation (one bundle) → image sequence
npx remotion render src/index.ts discipline-film out/qa/seq "--frames=15,90,180,330,600,1500,3000,4700" --scale=0.5 --image-format=jpeg

# 5) Draft render (half-res, fast encode) — watch it end-to-end for timing/audio
npx remotion render src/index.ts discipline-film out/draft/discipline-draft.mp4 --scale=0.5 --crf=28 --x264-preset=veryfast

#    Render only a range (e.g. a scene being iterated) as video
npx remotion render src/index.ts discipline-film out/draft/range.mp4 "--frames=1800-2400" --scale=0.5

# 6) Final master
npx remotion render src/index.ts discipline-film out/discipline.mp4 --codec=h264 --crf=18 --concurrency=50%
```

Notes on the commands:
- **Quote any argument that contains commas** in PowerShell, for example `"--frames=0,30"`. PowerShell treats an unquoted comma as its array operator, which can mangle the argument.
- `--frame=N` is zero-based. Take key frames from the script itself: `scripts/keyframes.mjs` should print, for each scene, its start + 5, the midpoint of every TextCue, every `impactAt`, and its end − 2, all converted to global frames with `sceneStarts()`.
- Visual inspection checklist for each still: text stays inside the 1920×1080 safe area (≥ 96 px margin) and does not overlap the character; the DAY counter sits top-left in gray; limbs stay attached at the joints (compare shoulder and hip pivots); the shadow glow is not clipped; contrast is adequate; nothing renders as unstyled black or white because of missing fonts or assets.
- `--crf` and hardware acceleration are mutually exclusive **[V]**. Keep CPU x264.
- `--concurrency` accepts a number or a percentage such as `50%` **[M]**. Find the optimum with `npx remotion benchmark`.
- For YouTube, h264 with crf 18 (the default) is fine **[V]**. `yuv420p` is the h264 default pixel format **[M]**.

### Common errors (Windows) and fixes
| Symptom | Fix |
|---|---|
| `npx : File C:\Program Files\nodejs\npx.ps1 cannot be loaded because running scripts is disabled` | Call `npx.cmd …` instead (or `npm exec`). Changing the execution policy is a security setting, so leave that decision to the user. |
| `EBUSY` / `EPERM` / `ENOTEMPTY` during `npm i` or while writing `out/` | OneDrive or antivirus is locking files. Move the project to `C:\dev\…` (preferred) or pause OneDrive. Close the video player that holds the old `out/*.mp4` before re-rendering. |
| `--props` JSON parse error | Inline JSON is not supported in Windows shells **[V]**. Write `props\x.json` and pass `--props=props\x.json`. |
| Path with spaces breaks a command | Quote it: `"~\OneDrive\Desktop\2d animation\…"`. |
| First render pauses or downloads | Remotion downloads Chrome Headless Shell on first use, so a network connection is needed once. `npx remotion browser ensure` pre-fetches it **[M]**. "Failed to launch the browser process" means you should rerun with `--log=verbose` **[V]**. |
| `Version mismatch` warnings or strange runtime errors | All `remotion` and `@remotion/*` packages must have the same version. Run `npx remotion versions` **[M]**, and only ever add packages with `npx remotion add`. |
| `delayRender() … was not cleared after 30000ms` | A font or asset failed to load: check the `staticFile` path and its case. Raise the limit with `--timeout=60000` **[M]** only as a last resort. |
| Flicker between frames or differences between renders | Something non-deterministic: Math.random, Date, CSS animation, or state set in an effect. See §3. |
| A transition throws "longer than sequence" | `validateScript` should have caught it. Shorten the transition. |
| Audio missing or silent at the start | The audio file sits outside `public/`, or `volume` is a function (deprecated). Use a number with interpolate. Fade-ins need a `Sequence` so the frame is local. |
| PowerShell turns native stderr into red "errors" | Remotion logs progress to stderr. In PowerShell 5.1, don't use `2>&1`; judge success by the exit code (`$LASTEXITCODE -eq 0`). |
| Out-of-memory or slowdown on long renders | Lower `--concurrency`, or render in chunks with `--frames=a-b` and concatenate them with ffmpeg (`ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4`). |

`scripts/qa.ps1` (PowerShell 5.1 compatible, so no `&&`):

```powershell
param([string]$Film = 'discipline', [string]$Frames = '15,90,180,600,1500,3000')
$ErrorActionPreference = 'Stop'
npx tsc --noEmit;                    if ($LASTEXITCODE -ne 0) { throw 'tsc failed' }
npx remotion render src/index.ts "$Film-film" "out/qa/$Film" "--frames=$Frames" --scale=0.5 --image-format=jpeg
if ($LASTEXITCODE -ne 0) { throw 'stills failed' }
Write-Output "Inspect out/qa/$Film then run draft render."
```

---

## 5. Scaffolding checklist (exact commands, PowerShell)

Do not run these yet; this section is documentation only.

```powershell
# 1. Location outside OneDrive (avoids file locks + spaces in path)
New-Item -ItemType Directory -Force C:\dev | Out-Null
Set-Location C:\dev

# 2. Scaffold — non-interactive, blank, no Tailwind (default since 4.0.534); must NOT be inside a git repo
npx create-video@latest --yes --blank dayone-studio
Set-Location .\dayone-studio
npm i

# 3. Remotion packages (version-locked to installed remotion)
npx remotion add @remotion/transitions @remotion/media @remotion/google-fonts @remotion/paths @remotion/noise @remotion/shapes @remotion/fonts

# 4. (optional) official agent skills for Claude Code
npx skills add remotion-dev/skills

# 5. Sanity checks
npx remotion versions          # all equal (expected 4.0.535 at time of writing) [M: command]
npx tsc --noEmit
npx remotion studio            # opens http://localhost:3000
npx remotion benchmark         # once per machine → pick --concurrency
```

Expected `package.json` after scaffolding (versions as of 2026-10-14; `^4.0.0` in the template resolves to 4.0.535):

```json
{
  "name": "dayone-studio",
  "private": true,
  "scripts": {
    "dev": "remotion studio",
    "build": "remotion bundle",
    "upgrade": "remotion upgrade",
    "lint": "eslint src && tsc",
    "typecheck": "tsc --noEmit",
    "still": "remotion still src/index.ts",
    "draft": "remotion render src/index.ts --scale=0.5 --crf=28 --x264-preset=veryfast",
    "render": "remotion render src/index.ts --codec=h264 --crf=18"
  },
  "dependencies": {
    "@remotion/cli": "4.0.535",
    "@remotion/fonts": "4.0.535",
    "@remotion/google-fonts": "4.0.535",
    "@remotion/media": "4.0.535",
    "@remotion/noise": "4.0.535",
    "@remotion/paths": "4.0.535",
    "@remotion/shapes": "4.0.535",
    "@remotion/transitions": "4.0.535",
    "react": "19.2.3",
    "react-dom": "19.2.3",
    "remotion": "4.0.535"
  },
  "devDependencies": {
    "@remotion/eslint-config-flat": "4.0.535",
    "@types/react": "19.2.7",
    "@types/web": "0.0.166",
    "eslint": "9.39.5",
    "prettier": "3.8.1",
    "typescript": "5.9.3"
  }
}
```

Pin exact versions (remove the `^`) once the project works, so every film renders identically later. Upgrade deliberately with `npx remotion upgrade`.

`remotion.config.ts` (template defaults plus our additions):

```ts
import {Config} from '@remotion/cli/config';
Config.setRspack(true);
Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
Config.setDefaultPremountInSeconds(2);
Config.setCodec('h264');          // [M] explicit default
Config.setCrf(18);                // [M]
// Config.setConcurrency('50%');  // [M] set after `npx remotion benchmark`
```

### Checklist
- [ ] Project created outside OneDrive with `--yes --blank`; `npm i` is clean.
- [ ] All `@remotion/*` packages are at the same version (`npx remotion versions`).
- [ ] `src/lib/timeline/{types,time,compute,FilmRenderer}.ts(x)` are in place; `validateScript` runs in the registry.
- [ ] Theme tokens, fonts (`loadFont` with explicit weights and subsets) and the scene registry are set up.
- [ ] Each film has `src/films/<slug>/script.ts` registered in `FILMS`, which gives `<slug>-film`, `<slug>-<scene>` and `<slug>-thumb` compositions.
- [ ] Audio lives in `public/audio/{music,sfx}` with kebab-case names and uses `<Audio>` from `@remotion/media` with numeric volume.
- [ ] No Math.random, Date, CSS animation or animated blur; ESLint is clean.
- [ ] QA: tsc, then compositions, then key-frame stills (inspected), then a `--scale=0.5` draft (watched), then the final `crf 18` h264.
- [ ] License: the user is an individual creator, so the free license applies (a company with more than 3 staff would need a Company License).

---

## Doc URLs used
- https://www.remotion.dev/docs (getting started)
- https://www.remotion.dev/docs/cli/create-video
- https://www.remotion.dev/docs/ai/skills
- https://www.remotion.dev/docs/transitions/transitionseries
- https://www.remotion.dev/docs/transitions/presentations/slide · /wipe
- https://www.remotion.dev/docs/sequence · https://www.remotion.dev/docs/series
- https://www.remotion.dev/docs/spring · https://www.remotion.dev/docs/random
- https://www.remotion.dev/docs/noise/noise-2d · https://www.remotion.dev/docs/paths/evolve-path
- https://www.remotion.dev/docs/google-fonts/load-font · https://www.remotion.dev/docs/delay-render
- https://www.remotion.dev/docs/media/audio · https://www.remotion.dev/docs/html5-audio
- https://www.remotion.dev/docs/calculate-metadata · https://www.remotion.dev/docs/still
- https://www.remotion.dev/docs/cli/render · https://www.remotion.dev/docs/cli/still · https://www.remotion.dev/docs/cli/add
- https://www.remotion.dev/docs/performance · https://www.remotion.dev/docs/encoding · https://www.remotion.dev/docs/gl-options
- https://www.remotion.dev/docs/troubleshooting/browser-launch
- https://github.com/remotion-dev/template-empty (package.json, remotion.config.ts)
- https://github.com/remotion-dev/remotion/blob/main/LICENSE.md
- https://registry.npmjs.org/remotion/latest · https://registry.npmjs.org/@remotion/media/latest
