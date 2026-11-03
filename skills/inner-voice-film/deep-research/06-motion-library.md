# 06 — Motion / Action Library & Animation Math (Remotion v4)

Research agent 06/10. Scope: every hero action in *DISCIPLINE* (and the reusable set needed for new topics) as
**deterministic, frame-pure pose functions** for a forward-kinematics (FK) bean rig, plus the global motion rules
(anticipation, follow-through, hit-stop, smears, camera shake, noise) with exact Remotion v4 APIs.

Sources: `00-brief/BRIEF.md`, both scripts, the 20 reference frames (observations below), and the Remotion docs
(`/docs/interpolate`, `/docs/spring`, `/docs/measure-spring`, `/docs/easing`, `/docs/random`, `/docs/noise/noise-2d`, `/docs/paths`), checked 2026-10-14.

---

## 0. What the reference frames tell us about motion

| Frame | Motion read | Library consequence |
|---|---|---|
| 2–4 bed | Only the head is visible. The body is a blanket shape, and the clock sits **left of the headboard**. 4 = pupils become small dots, brows go up, an "o" mouth, a blue sweat drop at the top right of the head. | Blanket-breath path morph. The arm must **stretch** (rubber-hose ×1.4–1.7) to reach over the headboard. Shock = eye pop + sweat spawn. |
| 3 | A small "z" sits above a larger "Z", gray, beside the head. | zZ particles shrink as they rise. Newest = biggest = lowest. |
| 5–6 couch | Leans back about 14°. Near leg is straight and diagonal to the floor. Far leg is bent down (darker gray, no outline). Both hands hold the phone at the chin. Blue radial glow. | Static slouch pose plus a small thumb/screen loop. The glow pulses on each scroll. |
| 7 desk | Torso pitched about 50° forward, chin at desk height, both arms straight along the desk. | Hands are IK-locked to the desk while lean and head nod change. |
| 8 mirror | Shoulders dropped, near arm hanging in front of the torso, sad brows, half-lidded eyes. | "Sad" idle and sad walk parameters. |
| 9 | Seated ball, knees to chest, near hand on face, spotlight with dust motes. | Curl pose, sob shudder, dust particle field. |
| 10 run | Torso lean about 15°. Near arm bent about 90° and pumping. Far leg trailing far back. Horizontal speed lines at random heights. Sweat drop. Headband tail. | 18-frame run cycle, speed-line field, parallax ratios. |
| 11–13 push-up | A rigid plank pivoting at the toes. Pitch only about 5–18°. Near arm folded with the elbow up and back. Gritted teeth, anger mark, sweat. Counter "3" glows. | Plank-pitch α drives everything. Arms use IK to fixed hand points. Tremble noise. Counter pop spring. |
| 14–15 boxing | Staggered stance with the near fist at the chin. The near arm extends on the punch. The bag is red, hangs from a line, and glows on hit. Letters float **rotated and dimmed** after shattering. | Guard bounce, jab/cross, damped-pendulum bag, letter-shard particles with drag. |
| 16–17 stairs | Steps of about 1:2 rise:run with rounded nosings. Strong forward lean (~15°), arms forward. | Step-synced foot targets plus IK. |
| 18 summit | Upright and still, warm rim glow, a single wind speed line. | Wind idle plus ribbon chain. |
| 19 bed edge | Seated with thighs horizontal and shins vertical, hands at the knees. Headband knot tail toward the back. | Sit → stand → exit. |

**Rig proportions measured from frames 8/10/18 (normalised to a 360 px standing height at 1080p):**

```ts
// motion/rig.ts — numbers used by every table in this document
export const RIG = {
  H: 360,            // standing height (feet → top of head)
  bodyW: 150,        // bean width
  bodyH: 235,        // bean height (head merged)
  shoulderUp: 118,   // shoulder pivot distance from pelvis along torso axis
  headUp: 175,       // head-centre distance from pelvis along torso axis (face anchor)
  hipSide: 7,        // near hip +7 px, far hip -7 px (x, before facing flip)
  upperArm: 62, foreArm: 58,
  thigh: 70, shin: 66,
  limbW: 26,         // tube thickness (stroke width)
  outline: 3.5,      // dark outline (#1b1b1b) — near limbs only
  pelvisH: 70 + 66 + 13, // 149: standing pelvis height above ground (thigh+shin+limbW/2)
} as const;
```

---

## 1. Conventions (read first — every table depends on them)

* **Screen space**: SVG, x right, **y down**. The character faces **+x** before the `facing` flip (`scale(facing,1)` about the pelvis).
* **Angle convention**: `0°` = pointing straight **down**, `+90°` = pointing **forward** (+x), `-90°` = backward, `180°` = up.
  The direction vector is `dir(θ) = (sin θ, cos θ)`, so `atan2(dx, dy)` recovers θ.
* **Torso `lean`**: + = top of the bean tips forward. Torso up-vector `up(θ) = (sin θ, −cos θ)`.
* **Arms inherit lean**: `upperArmAbs = lean + shoulder`, `foreArmAbs = upperArmAbs + elbow`. Positive elbow means the forearm folds forward/up.
* **Legs are world-space** (the pelvis is a ball and legs do not inherit lean): `thighAbs = hip`, `shinAbs = hip − knee`. Positive knee means the shin folds backward, which is the normal knee.
* **`y` in poses is an offset from standing pelvis height**. 0 = standing tall, + = lower (crouch/seated), − = higher (jump).
* **Squash/stretch** `sx, sy` scales the **body bean only**, pivoting at the bean bottom. The shoulder height is multiplied by `sy` so limbs stay attached. Area is preserved: `sx = 1/sy` unless a table states otherwise.
* **Limb table notation** is `a/b`: shoulder/elbow for arms, hip/knee for legs. **N** = near (cream, outlined, drawn last). **F** = far (gray `#a9a596`, no outline, drawn first).
* **Easing column** = the easing used to **arrive at** that key (After Effects style).
* All timing is **@30 fps**. "f" = frame inside the action (Sequence-local).

### Draw order (prevents "limb detachment")
`farArm → farLeg → body(bean+face) → nearLeg → nearArm → headband`. Each limb is **one** `<path d="M root L joint L end">`
with `strokeLinecap="round" strokeLinejoin="round"`. Draw the outline first as a stroke of `limbW + 2*outline` in `#1b1b1b`, then the fill as a stroke of `limbW` in `#e8e4d8`. Because a single path goes from root to end, joints can never separate.

---

## 2. Core math library (`motion/core.ts`)

Everything below is pure (`frame → value`). Nothing reads `Math.random`, `Date`, or React state.

```ts
import {interpolate, Easing, spring, random} from 'remotion';
import {noise2D} from '@remotion/noise';

export const FPS = 30;
export const CLAMP = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
export type Ease = (t: number) => number;
export type V2 = {x: number; y: number};

// ---------- easing presets (Easing.bezier(x1,y1,x2,y2); x in [0,1], y may overshoot) ----------
export const E = {
  linear: Easing.linear,
  inOut:   Easing.bezier(0.45, 0, 0.55, 1),     // default for poses
  soft:    Easing.bezier(0.37, 0, 0.63, 1),     // sine-like, breathing, sways
  out:     Easing.bezier(0.22, 1, 0.36, 1),     // quint-out: settle, recoil, "arrive"
  in:      Easing.bezier(0.55, 0, 1, 0.45),     // gravity / falling
  snap:    Easing.bezier(0.7, 0, 0.84, 0),      // expo-in: accelerate INTO an impact
  whip:    Easing.bezier(0.9, 0, 0.1, 1),       // very fast middle: 2–3 frame strikes
  backOut: Easing.bezier(0.34, 1.56, 0.64, 1),  // overshoot then settle (pop-in)
  backIn:  Easing.bezier(0.36, 0, 0.66, -0.56), // dips backward first = built-in anticipation
  hold:    Easing.step1,                        // jump at the end of the segment
} satisfies Record<string, Ease>;

// ---------- keyframe tracks (version-proof: one interpolate() per segment) ----------
export function track(f: number, frames: number[], values: number[], ease: Ease | Ease[] = E.inOut): number {
  const n = frames.length;
  if (f <= frames[0]) return values[0];
  if (f >= frames[n - 1]) return values[n - 1];
  let i = 0;
  while (f > frames[i + 1]) i++;
  const e = Array.isArray(ease) ? ease[i] : ease;
  return interpolate(f, [frames[i], frames[i + 1]], [values[i], values[i + 1]], {...CLAMP, easing: e});
}

// Row-based tables: {f, e?, ...numericFields}. e = easing used to ARRIVE at this row.
export type Row = {f: number; e?: Ease} & Record<string, number | Ease | undefined>;
export function sample(f: number, rows: Row[], key: string): number {
  const fr: number[] = [], vs: number[] = [], es: Ease[] = [];
  let last: number | undefined;
  for (const r of rows) {
    const v = r[key] as number | undefined;
    const val = v ?? last;                 // a missing value = hold the previous value
    if (val === undefined) continue;
    fr.push(r.f); vs.push(val); es.push((r.e as Ease) ?? E.inOut);
    last = val;
  }
  if (fr.length === 0) return NaN;          // field absent from this table → caller falls back (`|| 1`)
  return track(f, fr, vs, es.slice(1));
}

// ---------- cycles ----------
export const cyc = (f: number, len: number) => ((f % len) + len) % len;
export const phase01 = (f: number, len: number, offset = 0) => cyc(f + offset, len) / len;
// Sample a looping table whose rows run 0..len (the last row must equal the first).
export const sampleLoop = (f: number, len: number, rows: Row[], key: string) => sample(cyc(f, len), rows, key);

// Variable-speed cycle: cycle length changes linearly c0→c1 over [f0,f1]. Exact integral of 1/c(f).
export function cyclePhase(f: number, f0: number, f1: number, c0: number, c1: number): number {
  if (f <= f0) return (f - f0) / c0;
  const k = (c1 - c0) / (f1 - f0);
  const g = Math.min(f, f1) - f0;
  let p = Math.abs(k) < 1e-6 ? g / c0 : Math.log((c0 + k * g) / c0) / k;
  if (f > f1) p += (f - f1) / c1;
  return p; // in cycles; use (p % 1) as normalised phase
}

// ---------- springs (Remotion spring(): defaults mass 1, damping 10, stiffness 100) ----------
export const SPR = {
  pop:    {damping: 8,   mass: 0.6, stiffness: 180}, // ζ≈0.38, ~27% overshoot, ≈24f — eyes, text, counters
  settle: {damping: 14,  mass: 1,   stiffness: 120}, // ζ≈0.64, ~7% overshoot, ≈23f — body arrives in pose
  snap:   {damping: 20,  mass: 0.5, stiffness: 300}, // ζ≈0.82, ~1% overshoot, ≈8f  — head jerk, button
  wobble: {damping: 6,   mass: 1,   stiffness: 160}, // ζ≈0.24, ~46% overshoot, ≈50f — jelly squash recovery
  heavy:  {damping: 18,  mass: 3,   stiffness: 90},  // ζ≈0.55, slow & weighty, ≈50f — giant shadow, bag
  smooth: {damping: 200, mass: 1,   stiffness: 100}, // no bounce (docs: measureSpring → 23f @30fps)
} as const;
// ζ = damping / (2·sqrt(stiffness·mass)); settle frames ≈ 30·ln(200)/(damping/(2·mass)). Verify with measureSpring({fps:30, config}).
export const spr = (f: number, at: number, config: (typeof SPR)[keyof typeof SPR], from = 0, to = 1) =>
  spring({frame: f, fps: FPS, delay: at, config, from, to});

// ---------- deterministic noise ----------
export const rnd = (seed: string | number) => random(seed);            // [0,1)
export const nz = (seed: string, f: number, speed = 0.05, y = 0) => noise2D(seed, f * speed, y); // [-1,1]
// Tremble: high speed = jitter, low speed = drift. onTwos=true → changes every 2 frames (hand-made feel).
export const tremble = (seed: string, f: number, amp: number, speed = 0.8, onTwos = false) =>
  amp * noise2D(seed, (onTwos ? Math.floor(f / 2) * 2 : f) * speed, 0);

// ---------- vectors ----------
const D2R = Math.PI / 180;
export const dir = (deg: number): V2 => ({x: Math.sin(deg * D2R), y: Math.cos(deg * D2R)});
export const up  = (deg: number): V2 => ({x: Math.sin(deg * D2R), y: -Math.cos(deg * D2R)});
export const add = (a: V2, b: V2): V2 => ({x: a.x + b.x, y: a.y + b.y});
export const mul = (a: V2, s: number): V2 => ({x: a.x * s, y: a.y * s});
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
export const clamp01 = (t: number) => Math.min(1, Math.max(0, t));
```

### 2.1 Pose type, FK, IK, ground-plant, blending

```ts
// motion/pose.ts
import {RIG} from './rig';
import {V2, dir, up, add, mul, lerp} from './core';

export type Limb = {a: number; b: number; s?: number}; // a=shoulder|hip, b=elbow|knee, s=stretch (1 = normal)
export type Pose = {
  x: number; y: number;          // pelvis offset (px). y: 0 = standing height, + = lower
  lean: number;                  // torso pitch, + forward
  sx: number; sy: number;        // body squash/stretch
  armN: Limb; armF: Limb; legN: Limb; legF: Limb;
  headTilt: number;              // deg, + = chin down
  headBob: number;               // px along torso axis (+ = up)
  eye: number;                   // 0 closed … 1 open
  eyeScale: number;              // 1 normal, 1.35 shocked
  pupil: number;                 // 1 normal, 0.6 shock dots
  brow: number;                  // -1 angry(down/in) … 0 neutral … +1 worried(up/in)
  mouth: 'flat' | 'smile' | 'o' | 'teeth' | 'frown' | 'pant';
  faceX: number;                 // -1 profile-left … 0 front … +1 profile-right (turnaround)
  facing: 1 | -1;
};

export const NEUTRAL: Pose = {
  x: 0, y: 0, lean: 0, sx: 1, sy: 1,
  armN: {a: 4, b: 8}, armF: {a: -4, b: 8}, legN: {a: 3, b: 0}, legF: {a: -3, b: 0},
  headTilt: 0, headBob: 0, eye: 1, eyeScale: 1, pupil: 1, brow: 0, mouth: 'flat', faceX: 0.35, facing: 1,
};

export type Joints = {pelvis: V2; shoulder: V2; head: V2;
  armN: [V2, V2, V2]; armF: [V2, V2, V2]; legN: [V2, V2, V2]; legF: [V2, V2, V2]};

export function fk(p: Pose, ground: V2): Joints {
  const pelvis = {x: ground.x + p.x, y: ground.y - RIG.pelvisH + p.y};
  const u = up(p.lean);
  const shoulder = add(pelvis, mul(u, RIG.shoulderUp * p.sy));
  const head = add(pelvis, mul(u, RIG.headUp * p.sy + p.headBob));
  const arm = (l: Limb): [V2, V2, V2] => {
    const a1 = p.lean + l.a, a2 = a1 + l.b, s = l.s ?? 1;
    const e = add(shoulder, mul(dir(a1), RIG.upperArm * s));
    return [shoulder, e, add(e, mul(dir(a2), RIG.foreArm * s))];
  };
  const leg = (l: Limb, side: number): [V2, V2, V2] => {
    const hip = {x: pelvis.x + side * RIG.hipSide, y: pelvis.y};
    const k = add(hip, mul(dir(l.a), RIG.thigh * (l.s ?? 1)));
    return [hip, k, add(k, mul(dir(l.a - l.b), RIG.shin * (l.s ?? 1)))];
  };
  return {pelvis, shoulder, head, armN: arm(p.armN), armF: arm(p.armF), legN: leg(p.legN, 1), legF: leg(p.legF, -1)};
}
// NOTE: fk runs in the un-flipped space. Render inside <g transform={`translate(${px} 0) scale(${facing} 1) translate(${-px} 0)`}>.

// Analytic 2-bone IK in OUR angle convention. bend=+1 → joint ahead of the root→target line
// (knees), bend=-1 → joint behind (elbows). Returns ABSOLUTE angles.
export function ik2(root: V2, target: V2, L1: number, L2: number, bend: 1 | -1) {
  const dx = target.x - root.x, dy = target.y - root.y;
  const d = Math.min(Math.max(Math.hypot(dx, dy), Math.abs(L1 - L2) + 1e-3), L1 + L2 - 1e-3);
  const base = Math.atan2(dx, dy);
  const A = Math.acos(Math.min(1, Math.max(-1, (L1 * L1 + d * d - L2 * L2) / (2 * L1 * d))));
  const a1 = base + bend * A;
  const j = {x: root.x + Math.sin(a1) * L1, y: root.y + Math.cos(a1) * L1};
  const a2 = Math.atan2(target.x - j.x, target.y - j.y);
  return {a1: a1 * 180 / Math.PI, a2: a2 * 180 / Math.PI};
}
// Convert to relative pose values:
export const ikLeg = (hip: V2, foot: V2): Limb => { const r = ik2(hip, foot, RIG.thigh, RIG.shin, 1); return {a: r.a1, b: r.a1 - r.a2}; };
export const ikArm = (sh: V2, hand: V2, lean: number, s = 1): Limb => {
  const r = ik2(sh, hand, RIG.upperArm * s, RIG.foreArm * s, -1); return {a: r.a1 - lean, b: r.a2 - r.a1, s};
};

// Ground plant: choose pelvis y so the LOWEST foot touches groundY. Use this for walks and runs to kill floating/sinking.
export function plantY(p: Pose): number {
  const j = fk({...p, y: 0}, {x: 0, y: 0});
  const lowest = Math.max(j.legN[2].y, j.legF[2].y) + RIG.limbW / 2;
  return -lowest; // add to p.y (ground y = 0 in that local frame)
}

// Pose blending: transitions between actions (6–10 f crossfade with E.inOut).
export function mixPose(a: Pose, b: Pose, t: number): Pose {
  const L = (x: Limb, y: Limb): Limb => ({a: lerp(x.a, y.a, t), b: lerp(x.b, y.b, t), s: lerp(x.s ?? 1, y.s ?? 1, t)});
  return {...(t < 0.5 ? a : b),
    x: lerp(a.x, b.x, t), y: lerp(a.y, b.y, t), lean: lerp(a.lean, b.lean, t), sx: lerp(a.sx, b.sx, t), sy: lerp(a.sy, b.sy, t),
    armN: L(a.armN, b.armN), armF: L(a.armF, b.armF), legN: L(a.legN, b.legN), legF: L(a.legF, b.legF),
    headTilt: lerp(a.headTilt, b.headTilt, t), headBob: lerp(a.headBob, b.headBob, t), eye: lerp(a.eye, b.eye, t),
    eyeScale: lerp(a.eyeScale, b.eyeScale, t), pupil: lerp(a.pupil, b.pupil, t), brow: lerp(a.brow, b.brow, t),
    faceX: lerp(a.faceX, b.faceX, t)};
}
```

### 2.2 Action contract

```ts
export type MotionEvent = {f: number; type: 'impact' | 'shake' | 'hitstop' | 'sfx' | 'spawn'; data?: Record<string, unknown>};
export type Action = {
  id: string;
  len: number;              // frames (loop length if loop)
  loop: boolean;
  poseAt: (f: number) => Pose;   // PURE. f is action-local
  events: MotionEvent[];    // impacts → camera shake, hit-stop, SFX, particles (single source of truth)
};
```
`events` lets the scene compose camera shake, hit-stop, particles and the audio track from the **same** frame numbers, so sound and picture can never drift.

---

## 3. Global animation principles (enforced by the library)

| Principle | Rule (30 fps) | Implementation |
|---|---|---|
| **Anticipation** | Small 3–4 f · medium 6–8 f · big 10–14 f. Amplitude is 10–25% of the action, in the **opposite** direction. | A pre-key in the table, or `E.backIn` on the action segment |
| **Fast action** | Strikes 2–3 f, slaps 3 f, flinches 2 f. | `E.snap` / `E.whip` |
| **Follow-through / settle** | 6–20 f after the action. Overshoot 5–15%. | `E.out`, `E.backOut`, or `SPR.settle` |
| **Ease in/out** | Never use linear on character joints. Linear only for parallax/camera trucks and constant-speed travel. | default `E.inOut` |
| **Holds** | Minimum 6 f for a read, 12–20 f for an emotional beat. **Moving hold**: keep breathing/blinks running and drift ≤0.5° so it never freezes dead. | two keys with the same value + idle layer |
| **Overlapping action** | Head lags the body by 2–3 f, headband tail by 3–6 f (more per segment), arms by 1–2 f in cycles, sweat/zZ by spawn. | `poseAt(f - lag)` sampling (pure, free) |
| **Squash & stretch** | Land/impact `sy` 0.88–0.95. Launch/stretch `sy` 1.04–1.08. Keep the area (`sx = 1/sy`). | body bean only |
| **Arcs** | Root paths use sine bobs, never linear y. Hands arc naturally via FK. | — |
| **Smears / speed lines** | When a hand travels > 25 px/frame, draw a smear for that frame. Speed lines when the scene moves > 12 px/f. | §3.3 |
| **Hit-stop** | 2 f (light) / 3 f (heavy) freeze of **character time** at contact. Camera shake and particles keep running in screen time. | §3.2 |
| **Camera shake** | A decaying sine, directional on the first frame. | §3.1 |
| **Staging** | One action at a time. Text beats get a hold on the character (idle only) so the eye reads the text. | — |
| **Timing contrast** | Act 1 (lazy) moves are slow, low amplitude, soft easing. Act 3 (disciplined) moves are crisp, with snap easing and holds before decisive moves. | mood presets §5 |

### 3.1 Camera shake — exact formula

Per impact *i* at screen frame `h_i`, with `t = (f − h_i)/fps` seconds:

```
x(t) = dX · A · e^(−t/τ) · cos(2π·F·t)                 (first frame = full kick in the hit direction dX)
y(t) =      0.6A · e^(−t/τ) · sin(2π·1.37F·t + φ_i)
r(t) =      R · e^(−t/τ) · sin(2π·0.8F·t + 2φ_i)        (degrees)
φ_i = 2π·random(`shake-${h_i}`)
```
Keep **F ≤ 12 Hz** at 30 fps (Nyquist is 15 Hz; above it the shake aliases into slow wobble). The visible length is `t_end = τ·ln(A / 0.5px)`.

| Preset | A (px @1080p) | τ (s) | F (Hz) | R (°) | visible frames | Use |
|---|---|---|---|---|---|---|
| `tap` | 3 | 0.08 | 10 | 0 | ≈4 | calm alarm press, counter pop |
| `hit` | 7 | 0.12 | 9 | 0.3 | ≈10 | jab, slap on clock, body collapse |
| `heavy` | 14 | 0.18 | 8 | 0.8 | ≈18 | cross on bag, shatter words |
| `quake` | 18 | 0.28 | 7 | 1.2 | ≈30 | giant shadow split, mirror crack |

```ts
export type Shake = {at: number; A: number; tau: number; F: number; R?: number; dX?: 1 | -1};
export function cameraShake(f: number, shakes: Shake[]) {
  let x = 0, y = 0, r = 0;
  for (const s of shakes) {
    const t = (f - s.at) / FPS;
    if (t < 0) continue;
    const env = Math.exp(-t / s.tau);
    if (s.A * env < 0.3) continue;
    const ph = 2 * Math.PI * random(`shake-${s.at}`);
    x += (s.dX ?? 1) * s.A * env * Math.cos(2 * Math.PI * s.F * t);
    y += 0.6 * s.A * env * Math.sin(2 * Math.PI * 1.37 * s.F * t + ph);
    r += (s.R ?? 0) * env * Math.sin(2 * Math.PI * 0.8 * s.F * t + 2 * ph);
  }
  return {x, y, r}; // apply to the CAMERA group: translate(x,y) rotate(r) about frame centre; scale 1.02 to hide edges
}
```

### 3.2 Hit-stop (time remap)

Stops are authored in **action time** ("impact happens at action frame 6, hold 3"). The function maps screen frame → action frame:

```ts
export function hitStop(screenF: number, stops: {at: number; hold: number}[]): number {
  let acc = 0;
  for (const s of [...stops].sort((a, b) => a.at - b.at)) {
    const start = s.at + acc;                   // screen frame where the impact appears
    if (screenF < start) break;
    if (screenF < start + s.hold) return s.at;  // frozen
    acc += s.hold;
  }
  return screenF - acc;
}
// usage: const af = hitStop(frame, action.events.filter(e=>e.type==='hitstop').map(e=>({at:e.f, hold:e.data!.hold as number})));
//        pose = action.poseAt(af); shake uses screen frames (impact screen frame = s.at + acc).
```
During the freeze, add a 1-frame white flash at the contact point (a circle r = 40 → 0, opacity 0.9) and freeze the bag too.

### 3.3 Smears and speed lines

```ts
// Smear: a tapered capsule from the hand's previous position to its current one (sampled from the pure poseAt).
export function smear(prev: V2, cur: V2, width: number, minSpeed = 25) {
  const v = Math.hypot(cur.x - prev.x, cur.y - prev.y);
  if (v < minSpeed) return null;
  const nx = -(cur.y - prev.y) / v, ny = (cur.x - prev.x) / v, w = width * 0.5;
  const d = `M ${prev.x} ${prev.y} L ${cur.x + nx * w} ${cur.y + ny * w} L ${cur.x - nx * w} ${cur.y - ny * w} Z`;
  return {d, opacity: Math.min(0.85, (v - minSpeed) / 40)};   // fill = limb colour, no outline
}
// Also stretch the forearm on that frame: s = 1 + min(0.35, v/300). Never smear on calm (Act 3 alarm) actions.

// Speed-line field (frame 10): thin gray horizontal lines at random heights moving faster than the ground.
export function speedLines(f: number, n: number, v: number, W: number, H: number, seed = 'sl') {
  return Array.from({length: n}, (_, i) => {
    const r = (k: string) => random(`${seed}-${i}-${k}`);
    const len = 90 + r('l') * 180, speed = v * (1.3 + r('s') * 0.8);
    const span = W + len * 2;
    const x = W + len - cyc(r('x') * span + f * speed, span);  // travels right→left
    return {x1: x, x2: x + len, y: 80 + r('y') * (H - 260), opacity: 0.25 + r('o') * 0.35, w: 1.5};
  });
}
```

### 3.4 Hand-drawn line boil

The reference strokes wobble slightly. Do it **on threes**, which reads as hand-drawn without looking noisy:

```tsx
// Option A — SVG filter (cheap to author). The seed changes every 3 frames, so it is deterministic.
<filter id="boil"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves={2} seed={Math.floor(frame / 3)} />
  <feDisplacementMap in="SourceGraphic" scale={2.2} /></filter>
// Apply to OUTLINE groups only (furniture, floor, limb outlines), not to text. Heavy on render time at 1080p: use it on small groups.

// Option B — vertex jitter (exact, fast): perturb path points.
export const boil = (id: string, i: number, f: number, amp = 1.1, step = 3) => {
  const k = Math.floor(f / step);
  return {dx: amp * noise2D(`${id}-x`, i * 0.7, k * 0.9), dy: amp * noise2D(`${id}-y`, i * 0.7, k * 0.9)};
};
```

### 3.5 Interpolation rules (lint list)

1. **Always clamp** (`CLAMP`). Never rely on the default `extend`.
2. `inputRange` must be strictly increasing with the same length as `outputRange`. A hold = two keys at different frames with the same value.
3. Use one easing per segment via `track()`/`sample()`. Recent v4 releases accept an `easing` array, but `track()` works on every v4 version.
4. Overshoot comes from the **easing** (`E.backOut`) or a spring, not from extrapolation. Clamping limits the input only, so the bezier's overshoot still shows.
5. Start springs with `delay`, not with negative frames. Use `durationInFrames` when the edit needs an exact length. Get lengths with `measureSpring({fps, config})`.
6. Compose **additively**: `base pose (table) + cycle + secondary lag + noise`. Use `mixPose` for action-to-action transitions (6–10 f, `E.inOut`).
7. Angles are unwrapped. Never `% 360` a joint angle mid-animation.
8. `poseAt(f)` receives Sequence-local frames as a **parameter**. Do not call `useCurrentFrame()` inside motion code; this keeps it pure and testable, and it can be sampled at `f-1` for smears and `f-lag` for overlap.
9. No `Math.random()`, `Date.now()`, CSS keyframes or CSS transitions. Use `random(seed)` / `noise2D(seed, …)` with string seeds named after the action (`'pushup-tremble'`).
10. Optional "on twos" for the character only: `f2 = Math.floor(f/2)*2` (or `interpolate(..., {posterize: 2})` on ≥4.0.470). Keep the camera, parallax and text on ones.

---

## 4. Shared secondary-motion modules

### 4.1 Breath (asymmetric: inhale 40%, exhale 60%)

```ts
export function breath(f: number, len = 90, inhale = 0.42): number { // 0 → 1 → 0
  const p = phase01(f, len);
  return p < inhale ? E.soft(p / inhale) : 1 - E.soft((p - inhale) / (1 - inhale));
}
```

### 4.2 Deterministic irregular blinks

```ts
export function makeBlinks(seed: string, duration: number, minGap = 54, maxGap = 150, dbl = 0.18): number[] {
  const out: number[] = [];
  let t = 12 + Math.floor(random(`${seed}-first`) * 40), i = 0;
  while (t < duration) {
    out.push(t);
    if (random(`${seed}-dbl-${i}`) < dbl) out.push(t + 9);          // double blink
    t += minGap + Math.floor(random(`${seed}-gap-${i}`) * (maxGap - minGap));
    i++;
  }
  return out; // memoise with useMemo per shot
}
export function eyeOpen(f: number, blinks: number[], close = 3, hold = 1, open = 4): number {
  let v = 1;
  for (const b of blinks) {
    const d = f - b;
    if (d < 0 || d >= close + hold + open) continue;
    v = Math.min(v, d < close ? 1 - E.in(d / close) : d < close + hold ? 0 : E.out((d - close - hold) / open));
  }
  return v;
}
// Render: eye scaleY = max(0.08, eye). Below 0.15, swap to a 2px arc (closed lid). Sleepy/couch: close=5, hold=3, open=7, cap eye at 0.45.
```

| Mood | gap (f) | close/hold/open | double % | max eye |
|---|---|---|---|---|
| neutral | 54–150 | 3/1/4 | 18 | 1.0 |
| sleepy / phone-numb | 70–200 | 5/3/7 | 5 | 0.45 |
| anxious | 30–80 | 2/1/3 | 30 | 1.0 |
| determined (Act 3) | 90–200 | 2/1/3 | 0 | 0.85 (squint) |

### 4.3 Overlap helper and stop-settle

```ts
export const lagged = <T,>(fn: (f: number) => T, f: number, lag: number) => fn(f - lag);
// Decaying settle after a motion stops (antenna, band, cheeks): amp in deg or px
export const settle = (f: number, at: number, amp: number, hz = 3, tau = 0.15) =>
  f < at ? 0 : amp * Math.exp(-(f - at) / FPS / tau) * Math.cos(2 * Math.PI * hz * (f - at) / FPS);
```

### 4.4 Headband tail — travelling-wave ribbon (deterministic, no simulation)

```ts
export type RibbonOpts = {n: number; seg: number; base: number; ampMin: number; amp: number; taper: number;
  hz: number; k: number; phase: number; velLag?: number};
// Each segment angle = base + amplitude(i)·sin(ωf − k·i + phase) + velocity drag (sampled with growing lag).
export function ribbon(f: number, anchorAt: (f: number) => V2, o: RibbonOpts): V2[] {
  const omega = (2 * Math.PI * o.hz) / FPS;
  let p = anchorAt(f);
  const pts = [p];
  for (let i = 1; i <= o.n; i++) {
    const w = Math.pow(i / o.n, o.taper);
    const lagF = f - i * (o.velLag ?? 0.7);
    const v = anchorAt(lagF).x - anchorAt(lagF - 1).x;                // px/frame of the knot
    const drag = Math.max(-45, Math.min(45, -v * 2.2));               // moving forward → tail streams back
    const a = o.base + drag + (o.ampMin + o.amp * w) * Math.sin(omega * f - o.k * i + o.phase);
    p = add(p, mul(dir(a), o.seg));
    pts.push(p);
  }
  return pts; // render: Catmull-Rom → cubic Bezier, stroke #ff3b30, width tapering 10 → 6 px, round caps
}
export const BAND = {
  still:  {n: 6, seg: 11, base: -25, ampMin: 1, amp: 4,  taper: 1.2, hz: 0.5, k: 0.5, phase: 0},     // hangs back-down
  walk:   {n: 6, seg: 12, base: -55, ampMin: 2, amp: 10, taper: 1.3, hz: 1.6, k: 0.7, phase: 0},
  run:    {n: 7, seg: 13, base: -92, ampMin: 3, amp: 18, taper: 1.4, hz: 3.0, k: 0.8, phase: 0},     // streams horizontally
  summit: {n: 8, seg: 13, base: -95, ampMin: 4, amp: 22, taper: 1.5, hz: 2.2, k: 0.75, phase: 0},
} satisfies Record<string, RibbonOpts>;
// Angles are in the un-flipped space (−90 = backward). The second ribbon = same opts, phase +1.3, seg ×0.8.
```

---

## 5. Mood presets (same action, different person)

| Param | Lazy / sad (Act 1–2) | Neutral | Determined (Act 3) |
|---|---|---|---|
| Default easing | `E.soft` | `E.inOut` | `E.inOut` + `E.snap` on strikes |
| Anticipation length | none or 10 f+ (sluggish) | 6 f | 4 f, crisp |
| Hold before decisive move | — | 6 f | 8–12 f ("decision beat") |
| Lean bias | +6..+10 (slumped) | 0..+3 | +3..+6 (forward intent), chest up |
| Head tilt bias | +8..+12 (down) | 0 | −2 (chin up) |
| Arm swing scale | 0.25 | 0.6 | 0.8–1.0 |
| Eye | 0.45–0.6 | 1 | 0.85 squint, brow −0.7 |
| Breath cycle | 120 f / 1.5% | 90 f / 2.5% | 75 f / 2.5% |
| Band | — | — | always on, ribbon preset by speed |

---

## 6. Action library

Every action lists the **keyframe table**, **easing**, **loop length**, **secondary motion** and a `poseAt` sketch.
Unlisted pose fields default to `NEUTRAL`.

### 6.1 Idle breathing (loop 90 f) + blink

| f | breath b | sy | sx | lean | armN a/b | armF a/b | headBob (6 f lag) | notes |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.00 | 1.000 | 1.000 | −0.5 | 4/8 | −4/8 | 0 | exhale bottom |
| 19 | 0.50 | 1.0125 | 0.994 | 0.0 | 3.3/9 | −4.7/9 | −0.9 | inhaling (E.soft) |
| 38 | 1.00 | 1.025 | 0.988 | +0.5 | 2.5/10 | −5.5/10 | −2.3 | peak; shoulders ≈ +3 px via sy |
| 64 | 0.50 | 1.0125 | 0.994 | 0.0 | 3.3/9 | −4.7/9 | −2.2 | exhaling (longer) |
| 90 | 0.00 | 1.000 | 1.000 | −0.5 | 4/8 | −4/8 | 0 | loop |

Secondary: a slow weight sway `x = 1.5·sin(2πf/240)`, `lean += 0.6·sin(2πf/240 + 1)`. Arms lag the breath by 8/10 f. Blinks come from `makeBlinks`. Band `BAND.still`.

```ts
export const idle = (mood: 'sad' | 'neutral' | 'determined' = 'neutral', seed = 'idle'): Action => {
  const len = mood === 'sad' ? 120 : mood === 'determined' ? 75 : 90;
  const amp = mood === 'sad' ? 0.015 : 0.025;
  const blinks = makeBlinks(seed, 5400);
  return {id: `idle-${mood}`, len, loop: true, events: [],
    poseAt: (f) => {
      const b = breath(f, len), bh = breath(f - 6, len);
      return {...NEUTRAL,
        x: 1.5 * Math.sin((2 * Math.PI * f) / 240),
        lean: -0.5 + b + 0.6 * Math.sin((2 * Math.PI * f) / 240 + 1) + (mood === 'sad' ? 8 : 0),
        sy: 1 + amp * b, sx: 1 - amp * 0.48 * b,
        armN: {a: 4 - 1.5 * breath(f - 8, len), b: 8 + 2 * b}, armF: {a: -4 - 1.5 * breath(f - 10, len), b: 8 + 2 * b},
        headBob: -2.5 * bh, headTilt: -1 * bh + (mood === 'sad' ? 10 : mood === 'determined' ? -2 : 0),
        eye: eyeOpen(f, blinks) * (mood === 'sad' ? 0.55 : mood === 'determined' ? 0.85 : 1),
        brow: mood === 'sad' ? 0.6 : mood === 'determined' ? -0.7 : 0,
        mouth: mood === 'sad' ? 'frown' : 'flat'};
    }};
};
```

### 6.2 Asleep under blanket (loop 120 f) + zZ particles

Only the head and blanket are visible (frames 2–3). The pose here is a **bed rig**, not a full-body pose.

| f | b = breath(f,120,0.45) | blanket chest Δy | belly Δy (10 f lag) | head Δy (8 f lag) | head rot | mouth |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0° | smile |
| 27 | 0.5 | −2.5 | −0.8 | −0.4 | 0.3° | smile |
| 54 | 1 | −5 | −2.3 | −1.3 | 1.0° | smile |
| 87 | 0.5 | −2.5 | −2.6 | −1.3 | 0.9° | smile |
| 120 | 0 | 0 | 0 | 0 | 0° | loop |

Blanket: author two paths with **identical command structure** (`blanketExhale`, `blanketInhale`) and use `interpolatePath(b, blanketExhale, blanketInhale)` from `@remotion/paths`. Easing is built into `breath` (`E.soft`).

**zZ loop** (spawn every 40 f, life 100 f, 3 alive at once):

| param | formula (age a = f − k·40, u = a/100) |
|---|---|
| x | `hx + 14 + 26u + 5·sin(2π·1.5u + k)` |
| y | `hy − 34 − 95·(1 − (1−u)^1.6)` (decelerating rise) |
| scale | `interpolate(u,[0,0.15,1],[0.4,1,0.6])`. Newest/lowest = biggest (frame 3) |
| rot | `−12 + 22u` deg |
| opacity | `interpolate(a,[0,10,70,100],[0,1,1,0])` |
| glyph | `k % 2 ? 'z' : 'Z'`, font 34 px, `#9a9a9a` |

```ts
export function zzz(f: number, head: V2, every = 40, life = 100) {
  const out = [];
  for (let k = Math.max(0, Math.floor((f - life) / every) + 1); k <= Math.floor(f / every); k++) {
    const a = f - k * every; if (a < 0 || a >= life) continue; const u = a / life;
    out.push({k, glyph: k % 2 ? 'z' : 'Z',
      x: head.x + 14 + 26 * u + 5 * Math.sin(2 * Math.PI * 1.5 * u + k),
      y: head.y - 34 - 95 * (1 - Math.pow(1 - u, 1.6)),
      s: interpolate(u, [0, 0.15, 1], [0.4, 1, 0.6], CLAMP), r: -12 + 22 * u,
      o: interpolate(a, [0, 10, 70, 100], [0, 1, 1, 0], CLAMP)});
  }
  return out;
}
```

### 6.3 Alarm SLAP — Act 1 (one-shot, 110 f)

The bed rig: the shoulder is hidden under the blanket edge at `S = head + (40, 30)`. The arm uses **world** angles here (lying body), `0` = down and `−90` = left. Arm stretch `s` is the cartoon reach over the headboard. Final values come from `ikArm(S, clockButton, 0, s)`; the table below is for a clock 170 px left of and 60 px above the head centre.

| f | ease→ | phase | arm world a | elbow b | stretch s | eye | brow | other |
|---|---|---|---|---|---|---|---|---|
| 0 | — | alarm starts | −10 | 100 | 1.0 | 0 | 0 | clock jitters ±3 px every 2 f; digits blink 15 f on/off; SFX `beep` loop |
| 6 | soft | annoyed | −10 | 100 | 1.0 | 0 | −0.6 | mouth flat → frown |
| 14 | soft | blanket wiggle | −30 | 90 | 1.0 | 0.2 | −0.8 | blanket path += `tremble('blk', f, 3)` |
| 24 | out | arm emerges | −100 | 50 | 1.15 | 0.15 | −0.8 | hand clipped by the blanket mask until f20 |
| 32 | inOut | **anticipation** up/back | −165 | 25 | 1.45 | 0.15 | −1 | — |
| 40 | soft | antic hold (moving) | −170 | 30 | 1.5 | 0.15 | −1 | 8 f hold = comedic beat |
| 43 | **snap** | **SLAP** | −118 | 5 | 1.65 | 0.15 | −1 | smear on f41–42; `impact` event at f43 |
| 43–45 | — | **hit-stop 2 f** | — | — | — | — | — | white flash at hand |
| 45 | — | clock squash | −116 | 8 | 1.62 | 0.15 | −1 | clock `sy` 0.72 / `sx` 1.22, recovery `SPR.wobble`; shake `hit` (dX −1); beep stops; 5:00→5:05 |
| 58 | out | hand rests on clock | −117 | 12 | 1.6 | 0 | 0 | — |
| 66 | — | hold | −117 | 12 | 1.6 | 0 | 0 | — |
| 88 | inOut | lazy retract | −10 | 100 | 1.0 | 0 | 0.2 | — |
| 96 | out | relax | −10 | 100 | 1.0 | 0 | 0.3 | mouth smile, head sinks 3 px into pillow |
| 100+ | — | — | — | — | — | — | — | zZ starts; text "just 5 more minutes..." |

```ts
const SLAP: Row[] = [
  {f: 0, a: -10, b: 100, s: 1, eye: 0, brow: 0}, {f: 6, e: E.soft, brow: -0.6},
  {f: 14, e: E.soft, a: -30, b: 90, eye: 0.2, brow: -0.8}, {f: 24, e: E.out, a: -100, b: 50, s: 1.15, eye: 0.15},
  {f: 32, e: E.inOut, a: -165, b: 25, s: 1.45, brow: -1}, {f: 40, e: E.soft, a: -170, b: 30, s: 1.5},
  {f: 43, e: E.snap, a: -118, b: 5, s: 1.65}, {f: 45, e: E.out, a: -116, b: 8, s: 1.62},
  {f: 58, e: E.out, a: -117, b: 12, s: 1.6, eye: 0, brow: 0}, {f: 66, e: E.hold},
  {f: 88, e: E.inOut, a: -10, b: 100, s: 1, brow: 0.2}, {f: 96, e: E.out, brow: 0.3},
];
export const alarmSlap: Action = {id: 'alarm-slap', len: 110, loop: false,
  events: [{f: 43, type: 'impact'}, {f: 43, type: 'hitstop', data: {hold: 2}},
           {f: 43, type: 'shake', data: {A: 7, tau: 0.12, F: 9, dX: -1}}, {f: 43, type: 'sfx', data: {id: 'slap'}}],
  poseAt: (f) => ({...NEUTRAL, lean: -90 /* lying, head left */,
    armN: {a: sample(f, SLAP, 'a') + 90 /* world→relative to lean -90 */, b: sample(f, SLAP, 'b'), s: sample(f, SLAP, 's')},
    eye: sample(f, SLAP, 'eye'), brow: sample(f, SLAP, 'brow'), mouth: f > 90 ? 'smile' : f > 6 ? 'frown' : 'flat'})};
// Clock squash: sy = 1 - 0.28 * (1 - spr(f, 45, SPR.wobble)) for f>=45; pivot = clock bottom centre.
```

### 6.4 Calm WAKE & turn off — Act 3 (one-shot, 80 f)

The contrast with 6.3: **no stretch, no smear, no hit-stop**. A decision hold before moving, a deliberate press, and a hold on the button.

| f | ease→ | lean | armN a/b (rel) | s | eye | faceX | headTilt | events |
|---|---|---|---|---|---|---|---|---|
| 0 | — | −90 (lying) | hidden | 1 | 0 | 0.3 | 0 | 4:59→5:00, beep starts |
| 3 | `SPR.snap` | −90 | — | 1 | 1 | 0.3 | 0 | eyes open fully, no squint, brow −0.5 |
| 8 | hold | −90 | — | 1 | 1 | 0.3 | 0 | **decision beat** (5 f stillness) |
| 22 | `SPR.settle` from 8 | 0 (overshoot +4 at ~f17) | 10/10 | 1 | 1 | 0.3 | 0 | sit-up; blanket slides to waist (`interpolatePath`) |
| 26 | inOut | 0 | 10/10 | 1 | 1 | −0.6 | 0 | head turns toward the clock first (head leads by 2 f) |
| 36 | inOut | −4 (twist back) | −125/20 | 1.25 | 1 | −0.6 | 0 | deliberate reach (10 f, not 3) |
| 40 | in | −4 | −118/28 | 1.25 | 1 | −0.6 | 2 | **press**: contact at f40, `clack`, button `sy` 0.85 → `SPR.snap`, shake `tap` |
| 50 | hold | −4 | −118/28 | 1.25 | 1 | −0.6 | 4→0 | **10 f hold on the button** + one firm nod (+4° at 42 → 0 at 50) |
| 64 | inOut | 0 | 5/10 | 1 | 1 | 0.3 | 0 | arm returns; face forward at 58 |
| 80 | — | 0 | 5/10 | 1 | 0.85 | 0.3 | −2 | determined idle; then cut to bed edge (6.16) |

```ts
export const calmWake: Action = {id: 'calm-wake', len: 80, loop: false,
  events: [{f: 40, type: 'sfx', data: {id: 'clack'}}, {f: 40, type: 'shake', data: {A: 3, tau: 0.08, F: 10}}],
  poseAt: (f) => {
    const sit = spr(f, 8, SPR.settle);                 // 0 → 1 with ~7% overshoot
    const R: Row[] = [{f: 22, a: 10, b: 10, s: 1, fx: 0.3, lean: 0}, {f: 26, fx: -0.6},
      {f: 36, a: -125, b: 20, s: 1.25, lean: -4}, {f: 40, e: E.in, a: -118, b: 28},
      {f: 50, e: E.hold}, {f: 58, fx: 0.3}, {f: 64, a: 5, b: 10, s: 1, lean: 0}];
    return {...NEUTRAL, lean: f < 22 ? lerp(-90, 0, sit) : sample(f, R, 'lean'),
      armN: {a: sample(f, R, 'a'), b: sample(f, R, 'b'), s: sample(f, R, 's')},
      legN: {a: 90, b: 0}, legF: {a: 88, b: 0},
      eye: f < 3 ? spr(f, 0, SPR.snap) : f > 64 ? 0.85 : 1, brow: -0.5, faceX: sample(f, R, 'fx'),
      headTilt: track(f, [40, 42, 50], [0, 4, 0], [E.out, E.inOut]) - (f > 64 ? 2 : 0), mouth: 'flat'};
  }};
```

### 6.5 Panic jolt (one-shot, 60 f) — frame 4

| f | ease→ | y (px, lying: − = up off pillow) | sy | eye | eyeScale | pupil | brow | mouth | spawn |
|---|---|---|---|---|---|---|---|---|---|
| 0 | — | 0 | 1 | 0 | 1 | 1 | 0 | smile | cut to 8:47 |
| 4 | hold | 0 | 1 | 0 | 1 | 1 | 0 | smile | 4 f "realisation" beat |
| 6 | snap | +2 (antic) | 0.92 | 1 | `SPR.pop`→1.35 | 0.6 | +1 | o (scale pop) | — |
| 12 | out | −22 | 1.12 | 1 | 1.3 | 0.6 | +1 | o | **sweat drop** at f8 (head top-right) |
| 18 | in | 0 | 0.9 | 1 | 1.2 | 0.6 | +0.9 | o | land: shake `tap` vertical |
| 30 | `SPR.settle` | 0 | 1 | 1 | 1.15 | 0.65 | +0.8 | o | text "again." at f20 |
| 30–60 | — | tremble ±1 px (decays) | 1 | 1 | 1.15 | 0.65 | +0.8 | o | — |

Sweat drop: `scale = spr(f, 8, SPR.pop)`, `y = 12·E.in(clamp01((f−14)/30))`, `opacity = interpolate(f,[36,44],[1,0])`, colour `#7fb6ff` with a white highlight.
Tremble: `x += tremble('panic', f, 1.2·exp(−(f−30)/20))` for f > 30.

```ts
export const panicJolt: Action = {id: 'panic', len: 60, loop: false,
  events: [{f: 8, type: 'spawn', data: {kind: 'sweat'}}, {f: 18, type: 'shake', data: {A: 3, tau: 0.08, F: 10}}],
  poseAt: (f) => {
    const R: Row[] = [{f: 0, y: 0, sy: 1}, {f: 4}, {f: 6, e: E.snap, y: 2, sy: 0.92}, {f: 12, e: E.out, y: -22, sy: 1.12},
      {f: 18, e: E.in, y: 0, sy: 0.9}];
    const settled = f > 18 ? lerp(0.9, 1, spr(f, 18, SPR.settle)) : sample(f, R, 'sy');
    return {...NEUTRAL, lean: -90, y: sample(f, R, 'y') + (f > 30 ? tremble('panic', f, 1.2 * Math.exp(-(f - 30) / 20)) : 0),
      sy: settled, sx: 1 / settled, eye: f < 5 ? 0 : 1, eyeScale: f < 5 ? 1 : lerp(1, 1.35, spr(f, 5, SPR.pop)) - (f > 18 ? 0.2 * clamp01((f - 18) / 12) : 0),
      pupil: f < 5 ? 1 : 0.6, brow: f < 5 ? 0 : 1, mouth: f < 5 ? 'smile' : 'o'};
  }};
```

### 6.6 Couch slouch + thumb-scroll loop — frames 5–6

**Static base pose** (seated): `y +70`, `lean −14`, legN 62/8 (straight to the floor), legF 80/85, armN 25/135, armF 35/140 (hands meet at the chin), headTilt +8, eye 0.45 (sleepy blinks), brow 0.2, mouth flat, faceX 0.6.

**Scroll loop**: cycle lengths are irregular, `len_k = 36 + floor(random('scroll-'+k)·30)` (36–65 f). Precompute the cycle starts.

| f in cycle | ease→ | thumb rot | armN b | headTilt | screen offset | glow opacity |
|---|---|---|---|---|---|---|
| 0 | — | 0° | 135 | +8 | n·40 | 0.55 |
| 3 | out | −35° (flick up) | 132 | +8 | n·40 | 0.55 |
| 5 | — | −30 | 132 | +9 (2 f lag) | n·40 + 40·E.out(..) | 0.67 |
| 11 | inOut | 0 | 135 | +8 | (n+1)·40 at f10 | decays `0.55 + 0.12·e^(−age/8)` |
| len_k | hold | 0 | 135 | +8 | — | 0.55 |

Secondary: breath 120 f / 1.5%. The blue glow is a radial gradient `#4da3ff` centred on the phone, r = 160 px, layered under the face. Each new screen also shifts the glow hue ±4% (`random`).

```ts
export function couchScroll(seed = 'scroll', total = 1800): Action {
  const starts: number[] = []; for (let t = 0, k = 0; t < total; k++) { starts.push(t); t += 36 + Math.floor(random(`${seed}-${k}`) * 30); }
  const blinks = makeBlinks(`${seed}-bl`, total, 70, 200, 0.05);
  return {id: 'couch-scroll', len: total, loop: false, events: [],
    poseAt: (f) => {
      let k = 0; while (k + 1 < starts.length && starts[k + 1] <= f) k++;
      const c = f - starts[k];
      const thumb = track(c, [0, 3, 11], [0, -35, 0], [E.out, E.inOut]);   // render-only param (store in a side channel)
      const b = breath(f, 120);
      return {...NEUTRAL, y: 70, lean: -14 + 0.8 * b, sy: 1 + 0.015 * b, sx: 1 - 0.007 * b,
        legN: {a: 62, b: 8}, legF: {a: 80, b: 85},
        armN: {a: 25, b: 135 - 3 * Math.sin(Math.PI * clamp01(c / 6))}, armF: {a: 35, b: 140},
        headTilt: 8 + track(c, [2, 5, 13], [0, 1, 0]), eye: 0.45 * eyeOpen(f, blinks, 5, 3, 7), brow: 0.2, faceX: 0.6};
    }};
}
```

### 6.7 Desk: fall-asleep head drop — frame 7

Seated base: `y +70`. legN 85/80, legF 85/95. Hands are **IK-locked** on the desk at `H_N`, `H_F` via `ikArm(shoulder, H, lean)`, so arms slide naturally as the torso nods. Nod cycle (repeat 2× with lengths 72/84 f from `random`, then the final drop):

| f | ease→ | lean | headTilt | eye | brow | notes |
|---|---|---|---|---|---|---|
| 0 | — | 38 | 0 | 0.55 | 0.3 | fighting sleep |
| 36 | in | 46 | 12 | 0.15 | 0.4 | slow sink, accelerating |
| 40 | in | 58 | 24 | 0 | 0.4 | **drop** (gravity) |
| 44 | backOut | 47 | 4 | 0.7 | 0.8 | **jerk awake** (head lags torso 1 f) |
| 56 | out | 44 | 6 | 0.5 | 0.4 | — |
| 72 | inOut | 38 | 0 | 0.55 | 0.3 | loop to start |
| **final** 0→40 | in | 40→50 | 4→14 | 0.5→0.1 | — | — |
| final 46 | in | 62 | 28 | 0 | 0 | head lands on the arms |
| final 50 | `SPR.settle` | 60 | 26 | 0 | 0 | 2° rebound, then sleep breath 120 f |

```ts
const NOD: Row[] = [{f: 0, lean: 38, ht: 0, eye: 0.55}, {f: 36, e: E.in, lean: 46, ht: 12, eye: 0.15},
  {f: 40, e: E.in, lean: 58, ht: 24, eye: 0}, {f: 44, e: E.backOut, lean: 47, ht: 4, eye: 0.7},
  {f: 56, e: E.out, lean: 44, ht: 6, eye: 0.5}, {f: 72, e: E.inOut, lean: 38, ht: 0, eye: 0.55}];
export const deskNod = (handsN: V2, handsF: V2, ground: V2): Action => ({id: 'desk-nod', len: 72, loop: true, events: [],
  poseAt: (f) => {
    const lean = sample(f, NOD, 'lean');
    const base: Pose = {...NEUTRAL, y: 70, lean, legN: {a: 85, b: 80}, legF: {a: 85, b: 95},
      headTilt: sample(f - 1, NOD, 'ht'), eye: sample(f, NOD, 'eye'), brow: 0.3};
    const j = fk(base, ground);
    return {...base, armN: ikArm(j.shoulder, handsN, lean), armF: ikArm(j.shoulder, handsF, lean)};
  }});
```

### 6.8 Walk cycles — sad (40 f) vs confident (26 f)

One **normalised-phase** table drives both. The far leg = the same table at `p + 0.5`. Values are hip/knee for the **near leg**.

| phase p | key | Confident hip/knee | Sad hip/knee | root y conf | root y sad |
|---|---|---|---|---|---|
| 0.00 | contact (heel) | 24/2 | 14/2 | +2 | +1 |
| 0.10 | down (absorb) | 16/16 | 10/12 | +6 | +4 |
| 0.25 | passing (support) | 2/6 | 1/5 | 0 | 0 |
| 0.36 | up (push-off) | −12/4 | −7/3 | −5 | −2 |
| 0.50 | opposite contact | −24/14 | −14/8 | +2 | +1 |
| 0.60 | lift | −16/45 | −9/24 | +6 | +4 |
| 0.75 | swing passing | 4/62 | 3/32 (feet drag) | 0 | 0 |
| 0.86 | reach | 20/28 | 12/14 | −5 | −2 |
| 1.00 | = 0.00 | 24/2 | 14/2 | +2 | +1 |

| Param | Confident | Sad |
|---|---|---|
| cycle | 26 f (two steps) | 40 f |
| easing between keys | `E.inOut` | `E.soft` |
| lean | +3 (+1 on "up" keys) | +9 |
| headTilt / headBob | −2 / root y lagged 3 f ×0.6 | +10 / lagged 4 f ×0.4 |
| arms | `armN.a = −0.8·hipN(p−0.06)`, `b = 12 + max(0, armN.a)·0.5` | `armN.a = −0.25·hipN(p−0.08)`, `b = 6` (dead arms) |
| sy on "down" | 0.97 | 0.99 |
| ground speed (stance foot sweep) | `v = 4·L·sin(24°)/26 ≈ 8.5 px/f` | `v = 4·L·sin(14°)/40 ≈ 3.3 px/f` |
| band | `BAND.walk` | — |

`L = thigh + shin = 136`. Move the root at `v` px/f (or move the world at −v). For zero foot-slide, use the `plantY` vertical fix and add the table's y × 0.5 as style bob.

```ts
const WALK_P = [0, 0.1, 0.25, 0.36, 0.5, 0.6, 0.75, 0.86, 1];
const WALK = {
  confident: {len: 26, hip: [24, 16, 2, -12, -24, -16, 4, 20, 24], knee: [2, 16, 6, 4, 14, 45, 62, 28, 2], y: [2, 6, 0, -5, 2, 6, 0, -5, 2], lean: 3, arm: 0.8, ht: -2, ease: E.inOut},
  sad:       {len: 40, hip: [14, 10, 1, -7, -14, -9, 3, 12, 14],  knee: [2, 12, 5, 3, 8, 24, 32, 14, 2],  y: [1, 4, 0, -2, 1, 4, 0, -2, 1],  lean: 9, arm: 0.25, ht: 10, ease: E.soft},
};
export const walk = (style: keyof typeof WALK, ampRamp: (f: number) => number = () => 1): Action => {
  const W = WALK[style];
  const at = (arr: number[], p: number) => track(((p % 1) + 1) % 1, WALK_P, arr, W.ease);
  return {id: `walk-${style}`, len: W.len, loop: true, events: [],
    poseAt: (f) => {
      const p = f / W.len, k = ampRamp(f);
      const hipN = at(W.hip, p) * k, hipF = at(W.hip, p + 0.5) * k;
      const armA = (q: number) => -W.arm * at(W.hip, q) * k;
      const aN = armA(p - 0.06), aF = armA(p + 0.5 - 0.06);
      return {...NEUTRAL, lean: W.lean, headTilt: W.ht, y: at(W.y, p) * k, headBob: -0.6 * at(W.y, p - 3 / W.len),
        legN: {a: hipN, b: at(W.knee, p) * k}, legF: {a: hipF, b: at(W.knee, p + 0.5) * k},
        armN: {a: aN, b: 12 + Math.max(0, aN) * 0.5}, armF: {a: aF, b: 12 + Math.max(0, aF) * 0.5},
        sy: 1 - (style === 'confident' ? 0.03 : 0.01) * Math.max(0, at(W.y, p) / 6),
        brow: style === 'sad' ? 0.6 : -0.4, eye: style === 'sad' ? 0.55 : 0.9, mouth: style === 'sad' ? 'frown' : 'flat'};
    }};
};
export const walkSpeed = (hipAmpDeg: number, len: number) => (4 * 136 * Math.sin((hipAmpDeg * Math.PI) / 180)) / len;
```

### 6.9 Turn-around (one-shot, 12 f)

2D trick: pass through a **symmetric front view** and flip `facing` on the frame where front view is reached (the flip is then invisible).

| f | ease→ | faceX | facing | armN / armF | legs | sy | band |
|---|---|---|---|---|---|---|---|
| 0 | — | +0.6 | +1 | 4/8 · −4/8 | 3/0 · −3/0 | 1 | trailing |
| 3 | inOut | +0.25 | +1 | 0/6 · 0/6 | 0/0 · 0/0 | 0.97 (antic dip) | starts swinging (lags 3 f) |
| 5 | inOut | 0 (front) | +1 | 0/6 both visible | 0/0 | 0.98 | — |
| 6 | **step** | 0 | **−1** | — | — | 0.99 | — |
| 9 | out | −0.6·… (new profile) | −1 | 4/8 · −4/8 | 3/0 · −3/0 | 1.02 | swings across (`settle(f,6,25°,2.5)`) |
| 12 | `SPR.settle` | final | −1 | — | — | 1 | settles |

Rule: the head (faceX) leads the body by 2 f, and the band lags by 3 f. For a 180° turn while walking, insert it on a passing key (p = 0.25 or 0.75).

```ts
export const turnAround: Action = {id: 'turn', len: 12, loop: false, events: [],
  poseAt: (f) => ({...NEUTRAL,
    faceX: track(f + 2, [0, 3, 5, 6, 9], [0.6, 0.25, 0, 0, 0.6], [E.inOut, E.inOut, E.hold, E.out]), // magnitude; sign via facing
    facing: f < 6 ? 1 : -1,
    sy: track(f, [0, 3, 6, 9, 12], [1, 0.97, 0.99, 1.02, 1], [E.inOut, E.inOut, E.out, E.inOut]),
    armN: {a: track(f, [0, 5, 9], [4, 0, 4]), b: track(f, [0, 5, 9], [8, 6, 8])},
    armF: {a: track(f, [0, 5, 9], [-4, 0, -4]), b: track(f, [0, 5, 9], [8, 6, 8])}})};
```

### 6.10 Curl into a ball (rock bottom) + sob shudder — frame 9

Transition (one-shot, 40 f) then the sob loop (open-ended).

| f | ease→ | y | lean | legN a/b | legF a/b | armN a/b | armF a/b | sy/sx | headTilt | events |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | — | 0 | 8 | 3/0 | −3/0 | 4/8 | −4/8 | 1/1 | 10 | sad idle |
| 8 | inOut | +12 | 10 | 10/25 | 5/25 | 6/10 | −2/10 | 0.96/1.04 | 12 | knees buckle (antic) |
| 20 | in | +100 | 20 | 60/100 | 55/100 | 20/30 | 10/30 | 1.03/0.97 | 14 | fall to sitting |
| 22 | — | +115 | 24 | 95/140 | 90/135 | 30/50 | 20/50 | 0.9/1.1 | 15 | **land**: shake `hit` vertical A4, dust puff |
| 34 | out | +115 | 32 | 105/150 | 100/145 | 70/60 | 40/130 | 1/1 | 18 | curled: near arm hugs knees, far hand to face |
| 40 | `SPR.settle` | +115 | 32 | — | — | — | — | 1/1 | 18 | eye 0, brow 1, mouth frown |

**Sob shudder**: sob events at `makeEvents('sob', gap 45–80 f)`. Age `a`:

```
a ∈ [0,3):   sy += 0.04·E.out(a/3);  y −= 2·E.out(a/3)                (gasp / inhale jerk)
a ∈ [3,20):  e = exp(−(a−3)/6)
             y        += 2.5·e·sin(2π(a−3)/4)                          (4-frame shudder period)
             sy       += 0.02·e·sin(2π(a−3)/4 + π/2)
             headTilt += 3·e·sin(2π(a−3)/4 + 0.6)                      (head lags)
             armF.a   += 2·e·sin(2π(a−3)/4 + 1.0)
between:     breath(f, 100) at 1.5%
```

Dust motes in the spotlight: 30 particles, `x = cx + (random(i)−0.5)·380 + 8·noise2D('dust', i, f·0.01)`, `y = top + cyc(random(i+'y')·H − f·0.15, H)`, `opacity = 0.15 + 0.35·(0.5+0.5·noise2D('tw', i, f·0.03))`, r = 1.5–3 px.

```ts
export function makeEvents(seed: string, total: number, minGap: number, maxGap: number) {
  const out: number[] = []; for (let t = 20, i = 0; t < total; i++) { out.push(t); t += minGap + Math.floor(random(`${seed}-${i}`) * (maxGap - minGap)); } return out;
}
export const sobLoop = (total = 900): Action => {
  const sobs = makeEvents('sob', total, 45, 80);
  const CURL: Pose = {...NEUTRAL, y: 115, lean: 32, legN: {a: 105, b: 150}, legF: {a: 100, b: 145},
    armN: {a: 70, b: 60}, armF: {a: 40, b: 130}, headTilt: 18, eye: 0, brow: 1, mouth: 'frown'};
  return {id: 'sob', len: total, loop: false, events: [],
    poseAt: (f) => {
      const b = breath(f, 100); let y = 0, sy = 0.015 * b, ht = 0, af = 0;
      for (const s of sobs) { const a = f - s; if (a < 0 || a >= 20) continue;
        if (a < 3) { sy += 0.04 * E.out(a / 3); y -= 2 * E.out(a / 3); }
        else { const e = Math.exp(-(a - 3) / 6), w = (2 * Math.PI * (a - 3)) / 4;
          y += 2.5 * e * Math.sin(w); sy += 0.02 * e * Math.sin(w + Math.PI / 2); ht += 3 * e * Math.sin(w + 0.6); af += 2 * e * Math.sin(w + 1); } }
      return {...CURL, y: CURL.y + y, sy: 1 + sy, sx: 1 / (1 + sy), headTilt: CURL.headTilt + ht, armF: {a: CURL.armF.a + af, b: CURL.armF.b}};
    }};
};
```

### 6.11 Run cycle — determined, against the wind (loop 18 f) — frame 10

Near-leg table. Far leg = `f + 9`. Root y / squash repeat every **9 f** (one step).

| f | key | legN hip/knee | armN a/b (1 f lag) | root y (mod 9) | sy / sx |
|---|---|---|---|---|---|
| 0 | contact (leg extended forward) | 32/12 | −45/80 | +5 | 1.00/1.00 |
| 2 | down (absorb) | 20/40 | −30/88 | +11 | 0.95/1.04 |
| 4 | passing (support under hip) | 2/28 | −5/95 | +3 | 1.00/1.00 |
| 6 | toe-off (drive) | −28/14 | 25/105 | −6 | 1.04/0.97 |
| 7.5 | flight apex | — | — | −10 | 1.03/0.98 |
| 9 | follow-through (other foot contacts) | −44/50 | 45/110 | +5 | 1.00 |
| 11 | heel to butt | −30/105 | 30/100 | (repeat) | — |
| 14 | knee drive passing | 12/110 | 5/95 | — | — |
| 16 | high knee | 46/65 | −30/85 | — | — |
| 18 | = 0 | 32/12 | −45/80 | — | — |

Easing between keys: `E.inOut`, except 4→6 (`E.in`, the push accelerates) and 6→9 (`E.out`). Lean `15 + 2·noise2D('gust', f·0.02, 0)`, plus 2° extra on toe-off frames (drive). Head: bob lags root y by 2 f ×0.5, tilt −3 (looking ahead), brow −1, mouth `teeth`/`pant` alternating every 9 f, sweat drop flies back (`x −= 3a`, `y += 0.3a²/10`).
**Ground speed**: the stance foot sweeps `L·(sin32° + sin28°) ≈ 136 px` in 6 f, so **v ≈ 22 px/f**. Parallax: road/lamps 1.0v, buildings 0.35v, skyline 0.12v, speed lines 1.3–2.1v (`speedLines(f, 14, 22, …)`). Band `BAND.run` (drag from v is built in because the camera follows: pass `vWorld` into the ribbon base: `base = −92`).

```ts
const RUN: Row[] = [
  {f: 0, hip: 32, knee: 12}, {f: 2, hip: 20, knee: 40}, {f: 4, hip: 2, knee: 28},
  {f: 6, e: E.in, hip: -28, knee: 14}, {f: 9, e: E.out, hip: -44, knee: 50}, {f: 11, hip: -30, knee: 105},
  {f: 14, hip: 12, knee: 110}, {f: 16, hip: 46, knee: 65}, {f: 18, hip: 32, knee: 12}];
const RUN_ARM: Row[] = [{f: 0, a: -45, b: 80}, {f: 4, a: -5, b: 95}, {f: 9, a: 45, b: 110}, {f: 14, a: 5, b: 95}, {f: 18, a: -45, b: 80}];
const RUN_Y: Row[] = [{f: 0, y: 5, sy: 1}, {f: 2, y: 11, sy: 0.95}, {f: 4, y: 3, sy: 1}, {f: 6, y: -6, sy: 1.04},
  {f: 7.5, e: E.out, y: -10, sy: 1.03}, {f: 9, e: E.in, y: 5, sy: 1}];
export const runCycle = (lenScale: (f: number) => number = () => 1): Action => ({id: 'run', len: 18, loop: true, events: [],
  poseAt: (f) => {
    const L = (rows: Row[], k: string, g: number, len = 18) => sampleLoop(g, len, rows, k);
    const sy = L(RUN_Y, 'sy', f, 9);
    return {...NEUTRAL,
      lean: 15 + 2 * nz('gust', f, 0.02) + (cyc(f, 9) > 4 && cyc(f, 9) < 7 ? 2 : 0),
      y: L(RUN_Y, 'y', f, 9), sy, sx: 1 / sy, headBob: -0.5 * L(RUN_Y, 'y', f - 2, 9), headTilt: -3,
      legN: {a: L(RUN, 'hip', f), b: L(RUN, 'knee', f)}, legF: {a: L(RUN, 'hip', f + 9), b: L(RUN, 'knee', f + 9)},
      armN: {a: L(RUN_ARM, 'a', f - 1), b: L(RUN_ARM, 'b', f - 1)}, armF: {a: L(RUN_ARM, 'a', f + 8), b: L(RUN_ARM, 'b', f + 8)},
      brow: -1, eye: 0.85, mouth: cyc(f, 18) < 9 ? 'teeth' : 'pant'};
  }});
```

#### 6.11b Tiring → stop → hands on knees → restart (one-shot, ≈ 340 f)

| f range | phase | what changes | easing / math |
|---|---|---|---|
| 0–120 | **tiring** | cycle 18→26 f via `cyclePhase(f,0,120,18,26)`. Hip amp ×1→0.75, knee lift ×1→0.7, lean 15→22, headTilt 0→10, eye 0.85→0.6, mouth `pant`, v ∝ amp/cycle (22→12 px/f) | `p = cyclePhase(...)`, sample `RUN` at `(p%1)·18` |
| 120–160 | **stop** | 2 decelerating walk steps (20 f each, stride ×0.6 then ×0.3). Last plant at 158 with `sy 0.92` | `E.out` on v→0; `SPR.settle` on sy |
| 160–176 | **hands on knees** | lean 22→52, legs both 0/30 (hips back), x −12, y +18. Hands IK to `knee + (6,−4)` | `E.out` |
| 176–266 | **pant** | pant cycle 18 f: `b = breath(f,18,0.35)`, sy 1±0.035, y ±2, headBob lag 2 f, armN b ±4. Sweat drips every 30 f, falling `y = ½·g·a²` with `g = 0.6 px/f²` | additive loop |
| 266–282 | **look up** | headTilt 15→−5, brow 0.3→−1, eye 0.6→1, mouth pant→flat | `E.out`, head leads the torso by 3 f |
| 282–290 | **decision hold** | still (moving hold: pant amplitude ×0.4) | — |
| 290–296 | **anticipation** | lean 52→40, knees 30→45, y +24, sy 0.93 | `E.inOut` |
| 296–300 | **launch** | lean 40→20, legF −35/10 (toe-off), sy 1.06, x +20, stretch | `E.snap` → `E.out` |
| 300–330 | **re-accelerate** | run with cycle 22→18 (`cyclePhase(f,300,330,22,18)`), lean 20→15, v 0→22 | v via `E.in` |

```ts
// tiring phase sampler (shared by any accelerating/decelerating cycle)
const runAtPhase = (p: number, amp: number, knee: number): Pick<Pose, 'legN' | 'legF'> => {
  const g = (p % 1) * 18;
  return {legN: {a: sampleLoop(g, 18, RUN, 'hip') * amp, b: sampleLoop(g, 18, RUN, 'knee') * knee},
          legF: {a: sampleLoop(g + 9, 18, RUN, 'hip') * amp, b: sampleLoop(g + 9, 18, RUN, 'knee') * knee}};
};
// inside poseAt(f) for f<120:
//   const t = f/120, p = cyclePhase(f, 0, 120, 18, 26);
//   return {...runPose, ...runAtPhase(p, lerp(1,0.75,t), lerp(1,0.7,t)), lean: lerp(15,22,E.inOut(t)), headTilt: 10*t};
```

### 6.12 Push-up — rep, failing rep, collapse and re-push (frames 11–13)

**Rig mode "plank"**: the character pivots at the toes `T` (ground). The body is rigid at pitch `α` (degrees above horizontal, head right).
`legs abs = α − 90` (both legs straight: hip = α−90, knee 0), `pelvis = T − dir(α−90)·136`, `lean = 90 − α`. Hands are fixed on the floor at `Hn = (shoulderX@α=18, groundY − 13)`. Arms use `ikArm(shoulder, Hn, lean)` with elbows behind/up (frame 11).

**Normal rep (loop 26 f; the down/up split is 12/12 plus a 2 f bottom hold):**

| f | ease→ | α | sy / sx | face | events |
|---|---|---|---|---|---|
| 0 | — | 18 | 1.00/1.00 | teeth, brow −1 | — |
| 12 | inOut | 5 | 0.98/1.02 | teeth | controlled descent |
| 14 | hold | 5 | 0.98 | teeth | bottom |
| 25 | out | 19 (lock overshoot) | 1.02/0.98 | teeth | — |
| 26 | inOut | 18 | 1.00 | teeth | **counter pop** (`SPR.pop` scale 0→1, glow), shake `tap` |

**Failing rep (64 f).** Strain `s ∈ [0,1]` drives the tremble:

| f | ease→ | α | strain | face / overlay | events |
|---|---|---|---|---|---|
| 0 | — | 18 | 0.2 | teeth | — |
| 12 | inOut | 5 | 0.3 | teeth | — |
| 22 | hold | 5 | 0.6 | sweat spawn at 16 | — |
| 32 | soft | 8.5 | 0.9 | eyes squeeze 0.5 | — |
| 38 | soft | 9 | 1.0 | **stall** | — |
| 42 | in | 7.5 | 1.0 | slip back | **"told you."** red text at 40 |
| 46 | hold | 7.5 | 1.0 | anger vein pops (`SPR.pop` at 44), brow −1, eye 1 | — |
| 58 | inOut | 14 | 0.8 | — | — |
| 64 | out | 18 | 0.0 | — | counter pop, shake `tap` |

Tremble layers (added on top of the table):
```
α        += s·0.6·noise2D('pu-a', f·0.7, 0)
y(px)    += s·1.8·noise2D('pu-y', f·0.9, 0)
armN.b   += s·3·noise2D('pu-e', f·0.8, 5)       (after IK)
headTilt += s·1.5·noise2D('pu-h', f·0.6, 2)
```

**Collapse and re-push (90 f):**

| f | ease→ | α | strain | body sy/sx | events |
|---|---|---|---|---|---|
| 0 | — | 6 | 1.0 | 1 | — |
| 4 | in (gravity) | 0 | 0 | 0.9/1.08 → `SPR.wobble` | impact: shake `hit` vertical, 5 dust puffs, `thud` |
| 24 | hold | 0 | 0 | 1 | eyes shut, fast breath (18 f) |
| 26 | snap | 0 | 0 | 1 | eyes open, brow −1 (decision) |
| 30 | out | 0 (headTilt −10, lifts) | 0 | 1 | — |
| 74 | `bezier(.6,0,.4,1)` | 18 | 1→0.4 | 1 | the slow grind up |
| 78 | backOut | 19→18 | 0 | 1.03 | **counter "3"** pop + glow + shake `tap` |

```ts
const REP: Row[] = [{f: 0, al: 18, sy: 1}, {f: 12, al: 5, sy: 0.98}, {f: 14, e: E.hold}, {f: 25, e: E.out, al: 19, sy: 1.02}, {f: 26, al: 18, sy: 1}];
export const pushup = (rows: Row[], toes: V2, handN: V2, handF: V2, len: number, seed = 'pu'): Action => ({
  id: 'pushup', len, loop: rows === REP, events: [{f: len, type: 'spawn', data: {kind: 'counter'}}],
  poseAt: (f) => {
    const s = rows[0].strain !== undefined ? sample(f, rows, 'strain') : 0;
    const al = sample(f, rows, 'al') + s * 0.6 * nz(`${seed}-a`, f, 0.7);
    const sy = sample(f, rows, 'sy') || 1;
    const legA = al - 90, pelvis = add(toes, mul(dir(legA), -136));
    const base: Pose = {...NEUTRAL, lean: 90 - al, sy, sx: 1 / sy,
      x: pelvis.x - toes.x, y: pelvis.y - (toes.y - RIG.pelvisH) + s * 1.8 * nz(`${seed}-y`, f, 0.9),
      legN: {a: legA, b: 0}, legF: {a: legA, b: 0}, brow: -1, mouth: 'teeth', faceX: 0.8,
      headTilt: -4 + s * 1.5 * nz(`${seed}-h`, f, 0.6)};
    const j = fk(base, toes);
    const aN = ikArm(j.shoulder, handN, base.lean), aF = ikArm(j.shoulder, handF, base.lean);
    return {...base, armN: {...aN, b: aN.b + s * 3 * nz(`${seed}-e`, f, 0.8)}, armF: aF};
  }});
```

### 6.13 Boxing — guard bounce, jab, cross, bag physics (frames 14–15)

**Guard (loop 16 f)**: lean 6, y +8, legN (front) 14/12, legF (back) −20/14, armN 35/125 (fist at chin), armF 50/135, brow −1, mouth teeth.

| f | y | sy | armN b (1 f lag) | headBob (2 f lag) |
|---|---|---|---|---|
| 0 | +8 (land) | 0.97 | 129 | 0 |
| 4 | +5 | 1.00 | 127 | −1.5 |
| 8 | +2 (top) | 1.01 | 121 | −3 |
| 12 | +5 | 1.00 | 123 | −1.5 |
| 16 | +8 | 0.97 | 129 | 0 |

Formula: `y = 8 − 6·(0.5 − 0.5cos(2πp))`, `sy = 1 − 0.03·(0.5+0.5cos(2πp))^4`, `armN.b = 125 + 4·sin(2π(p − 1/16))`.

**Jab (lead = near arm, 12 f)**

| f | ease→ | armN a/b | lean | x | notes |
|---|---|---|---|---|---|
| 0 | — | 35/125 | 6 | 0 | guard |
| 2 | inOut | 30/130 | 4 | −2 | small antic |
| 4 | **snap** | 88/4 | 12 | +8 | **impact** f4, hit-stop 2, smear on f3, shake `hit` dX +1 |
| 8 | out | 80/20 | 10 | +6 | recoil |
| 12 | inOut | 35/125 | 6 | 0 | guard |

**Cross (rear = far arm, power, 16 f)**

| f | ease→ | armF a/b | lean | x | legF a/b | legN a/b | notes |
|---|---|---|---|---|---|---|---|
| 0 | — | 50/135 | 6 | 0 | −20/14 | 14/12 | guard |
| 3 | inOut | 25/140 | 2 | −4 | −20/18 | 14/12 | wind back (antic) |
| 4 | hold | 25/140 | 2 | −4 | — | — | 1 f coil |
| 6 | **whip** | 92/2 | 18 | +16 | −30/4 (heel up / pivot) | 16/18 | **impact** f6, hit-stop 3, smear f5 (rear hand and forearm stretch 1.25), shake `heavy` dX +1, flash, **word shatter** |
| 10 | out | 75/30 | 12 | +12 | −26/8 | 15/15 | follow-through |
| 16 | inOut | 50/135 | 6 | 0 | −20/14 | 14/12 | guard |

Combo "jab-cross": jab at 0, cross at 12 (it overlaps the jab's recovery). Rhythm in the montage: `[jab 0, cross 12, jab 34, cross 46, cross 64]`.

**Bag: damped pendulum, superposed impulses (small-angle linear ⇒ exact superposition):**

```
θ(f) = Σ_i (J_i / ω_d) · e^(−ζ·ω·t_i) · sin(ω_d · t_i),   t_i = (f − h_i)/fps  for f ≥ h_i
ω = 2π / T,   ω_d = ω·sqrt(1 − ζ²)
T = 1.6 s (stylised heavy bag), ζ = 0.08
Peak ≈ J/ω  ⇒  jab J = 5°·ω ≈ 19.6 °/s  (5° swing),  cross J = 11°·ω ≈ 43 °/s (11° swing)
```
The bag rotates about the rope pivot at the top. On impact, also dent the bag: local `sx 0.92` on the hit side for 4 f (`SPR.wobble`) plus a red glow `opacity 1 → 0.35` over 12 f (frame 15). During hit-stop, freeze the bag too (feed it hit-stopped action time).

```ts
export function bagAngle(f: number, hits: {f: number; J: number}[], T = 1.6, zeta = 0.08): number {
  const w = (2 * Math.PI) / T, wd = w * Math.sqrt(1 - zeta * zeta);
  let th = 0;
  for (const h of hits) { const t = (f - h.f) / FPS; if (t < 0) continue; th += (h.J / wd) * Math.exp(-zeta * w * t) * Math.sin(wd * t); }
  return th; // degrees; rotate(<th>, pivot)
}
```

**Word shatter (frame 15)**: each letter j becomes a shard at impact `h`:
```
angle = 2π·random(`w-${j}-a`) ; speed v0 = 6 + 8·random(`w-${j}-v`) px/f ; τ = 10 f (drag)
pos(t)  = p0 + v0·dir2D(angle)·τ·(1 − e^(−t/τ)) + (0, −0.2·t)        (drifts up slowly, keeps floating)
rot(t)  = r0 + ω0·τ·(1 − e^(−t/τ)),  ω0 = (random−0.5)·30 °/f
scale   = interpolate(t,[0,20],[1,0.6]) ; opacity = interpolate(t,[0,3,25],[1,1,0.25])   (dim floaters, as in the frame)
```
Before the shatter, add a 2 f "crack": letters jitter `tremble(…, 3px, onTwos)`.

### 6.14 Stair climb (step-synced) + pushing through the giant shadow (frames 16–17)

**Stair geometry**: rise `R = 46`, run `D = 92` (≈26.6°, as in frame 16). Tread k centre `S_k = origin + (k·D + D/2, −k·R)`.
**Cycle** = 2 steps = 32 f (16 f per step). Per foot: swing 12 f, stance 20 f (4 f double support). The near foot lands on even steps, the far foot on odd steps.

| f (in 32) | near foot | far foot | root (pelvis) | lean | arms |
|---|---|---|---|---|---|
| 0 | lands on S_{2m} | stance S_{2m−1} | slope line + 0 | 14 | armN back (−20/30) |
| 4 | stance | swing starts (toe-off) | push up −4 px | 15 | — |
| 10 | stance | swing apex (clears nosing by 18 px) | −2 | 14 | armN fwd (25/40) |
| 16 | stance | lands on S_{2m+1} | 0 | 14 | — |
| 20 | swing starts | stance | −4 | 15 | — |
| 26 | swing apex | stance | −2 | 14 | armN back |
| 32 | lands on S_{2m+2} | stance | 0 | 14 | loop |

**Exact sync (IK-driven, guarantees no foot sliding).** The near foot swings tread `2m → 2m+2` and the far foot swings `2m+1 → 2m+3`, half a cycle later.
The ankle target is the tread surface minus `limbW/2`. The pelvis rides `h = 105 px` above the line through the tread centres and leads by `1.1·D`. This was checked: every stance-phase hip→ankle distance stays ≤ 132 px < L = 136, so the IK never hyper-extends.
```
slopeY(x)   = y0 − (x − x0 − D/2)·R/D
pelvis.x(f) = x0 + D·(f/16 + 1.1)
pelvis.y(f) = slopeY(pelvis.x) − 105 − 4·sin²(π·cyc(f,16)/16)
swing u∈[0,1] (12 f):  s = E.inOut(u)
foot.x = lerp(S_from.x, S_to.x, s)
foot.y = lerp(S_from.y, S_to.y, s) − 13 − (R + 18)·sin(πu)^0.8
leg = ikLeg(hip, foot)  (bend +1)
```

```ts
export const stairClimb = (origin: V2, R = 46, D = 92, cycle = 32): Action => ({id: 'stairs', len: cycle, loop: false, events: [],
  poseAt: (f) => {
    const half = cycle / 2, swing = half * 0.75;   // 12 f swing when cycle 32
    const tread = (k: number): V2 => ({x: origin.x + k * D + D / 2, y: origin.y - k * R - RIG.limbW / 2}); // ankle target
    const footAt = (offset: number): V2 => {         // offset 0 = near (even treads), half = far (odd treads)
      const g = f + offset, step = Math.floor(g / cycle) * 2, c = cyc(g, cycle);
      const k0 = offset ? step - 1 : step;              // near: step→step+2 ; far: step-1→step+1
      const from = tread(k0), to = tread(k0 + 2);
      if (c >= swing) return to;                        // stance on the landed tread
      const u = c / swing, s = E.inOut(u);
      return {x: lerp(from.x, to.x, s), y: lerp(from.y, to.y, s) - (R + 18) * Math.pow(Math.sin(Math.PI * u), 0.8)};
    };
    const slopeY = (x: number) => origin.y - ((x - origin.x - D / 2) * R) / D;
    const px = origin.x + D * (f / half + 1.1);
    const py = slopeY(px) - 105 - 4 * Math.sin((Math.PI * cyc(f, half)) / half) ** 2;
    const pelvis = {x: px, y: py};
    const legN = ikLeg({x: px + RIG.hipSide, y: py}, footAt(0)), legF = ikLeg({x: px - RIG.hipSide, y: py}, footAt(half));
    const armSw = (q: number) => 22 * Math.sin(2 * Math.PI * q);
    return {...NEUTRAL, x: pelvis.x - origin.x, y: pelvis.y - (origin.y - RIG.pelvisH), lean: 14 + Math.sin(2 * Math.PI * f / half),
      legN, legF, armN: {a: 5 - armSw(f / cycle), b: 35}, armF: {a: 5 + armSw(f / cycle), b: 35}, brow: -0.8, mouth: 'flat', eye: 0.85};
  }}); // NOTE: fk(pose, origin) with ground = origin; compute x/y as pelvis offsets from that ground anchor.
```

**Pushing through the giant shadow** (≈140 f):

| f | phase | changes |
|---|---|---|
| 0–40 | resistance | cycle 32→48 (`cyclePhase`), lean 14→26, arms shield: armN 75/70, armF 85/60, strain 0.6 tremble (`tremble('push', f, 1.5)`), eye 0.6 squint, band streams **backward** hard (`base −100`, amp ×1.3), shadow leans in (`SPR.heavy`) |
| 40–70 | grind | step progress continues slowly, root x per step ×0.7, red ember particles stream past (wind) |
| 70 | **split** | hit-stop 3 f, hero rim glow 0→1→0 over 10 f (white `#fff6e0`), shake `quake`, SFX rip |
| 70–94 | shadow halves | `x ±140·E.out(u)`, `rot ∓10°`, `opacity 1→0` over 24 f, 30 ember shards (word-shatter math, red) |
| 94–140 | recovery | cycle 48→30 via `SPR.settle` remap, lean 26→14, arms back to the climb swing (6 f `mixPose`) |

### 6.15 Summit: standing with the headband flapping (loop: none; procedural) — frame 18

Pose: `NEUTRAL` + determined idle (75 f breath), lean `2 + 1.2·noise2D('wind', f·0.01, 0)`, headTilt −2, eye 0.8 (wind squint), brow −0.6.

Ribbon (`BAND.summit`), per segment i = 1..8:
```
g(f)    = 0.75 + 0.25·noise2D('gust', f·0.015, 0)                  (gust envelope)
a_i(f)  = base + 25·(1−g) + g·(4 + 22·(i/8)^1.5) · sin(ω f − 0.75 i + φ)
base    = −95° (streaming backward, slightly up), ω = 2π·2.2/30 rad/frame
point_i = point_{i−1} + 13px · dir(a_i)
```
The second tail uses `φ + 1.3` and `seg × 0.8`. Wind also adds a horizontal speed line every 40–90 f (frame 18) and ±1 px body sway.

```ts
export const summit = (anchorAt: (f: number) => V2) => ({
  poseAt: (f: number): Pose => ({...NEUTRAL, lean: 2 + 1.2 * nz('wind', f, 0.01), headTilt: -2, eye: 0.8, brow: -0.6,
    sy: 1 + 0.025 * breath(f, 75), sx: 1 - 0.012 * breath(f, 75), x: 1 * nz('sway', f, 0.02)}),
  band: (f: number) => {
    const g = 0.75 + 0.25 * nz('gust', f, 0.015);
    return ribbon(f, anchorAt, {...BAND.summit, base: -95 + 25 * (1 - g), amp: 22 * g, ampMin: 4 * g});
  }});
```

### 6.16 Sitting on bed edge → stand up → exit walk (≈ 90 f + walk) — frame 19

| f | ease→ | y | lean | legN a/b | legF a/b | armN a/b | armF a/b | sy | headTilt | face |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | — | +62 | 4 | 88/92 | 84/88 | 30/40 (hand on knee) | 25/35 | 1 | 0 | smile, brow −0.6 |
| 12 | hold | +62 | 4 | — | — | — | — | 1 | 0 | blink at 6 (determined set) |
| 20 | inOut | +64 | 32 | 88/105 (feet pulled back) | 84/100 | 40/20 | 35/20 | 0.97 | 6 | **anticipation**: weight over feet |
| 30 | `bezier(.2,.8,.3,1)` | −4 | 6 | 6/4 | −2/4 | −10/10 | −14/10 | 1.04 | −2 | rise + stretch overshoot |
| 38 | `SPR.settle` | 0 | 3 | 4/2 | −3/2 | 4/8 | −4/8 | 1 | −2 | — |
| 46 | hold | 0 | 2 | — | — | — | — | 1 | −2 | chest up (lean −1 pulse) |
| 48+ | — | walk `confident` with `ampRamp = f ⇒ E.out(clamp01((f−48)/14))`, root speed ramps to 8.5 px/f over 20 f; first step = near leg; exits frame right | | | | | | | | |

The tiny shadow by the nightstand (frame 19) does not react; it only sags over 30 f (scaleY 1→0.92, `E.soft`), which is a nice contrast. The band uses `BAND.still` while seated and `BAND.walk` on exit (velocity drag from the ribbon).

```ts
const STAND: Row[] = [
  {f: 0, y: 62, lean: 4, nA: 88, nB: 92, fA: 84, fB: 88, aA: 30, aB: 40, bA: 25, bB: 35, sy: 1, ht: 0},
  {f: 12, e: E.hold},
  {f: 20, e: E.inOut, y: 64, lean: 32, nB: 105, fB: 100, aA: 40, aB: 20, bA: 35, bB: 20, sy: 0.97, ht: 6},
  {f: 30, e: Easing.bezier(0.2, 0.8, 0.3, 1), y: -4, lean: 6, nA: 6, nB: 4, fA: -2, fB: 4, aA: -10, aB: 10, bA: -14, bB: 10, sy: 1.04, ht: -2},
  {f: 38, e: E.out, y: 0, lean: 3, nA: 4, nB: 2, fA: -3, fB: 2, aA: 4, aB: 8, bA: -4, bB: 8, sy: 1},
];
export const bedEdgeStand: Action = {id: 'bed-stand', len: 48, loop: false, events: [],
  poseAt: (f) => { const s = (k: string) => sample(f, STAND, k);
    return {...NEUTRAL, y: s('y'), lean: s('lean'), sy: s('sy'), sx: 1 / s('sy'), headTilt: s('ht'),
      legN: {a: s('nA'), b: s('nB')}, legF: {a: s('fA'), b: s('fB')}, armN: {a: s('aA'), b: s('aB')}, armF: {a: s('bA'), b: s('bB')},
      brow: -0.6, mouth: 'smile', eye: 0.9}; }};
// Sequence: <Sequence durationInFrames={48}>bedEdgeStand</Sequence> then walk('confident', ramp) with a 6 f mixPose crossfade.
```

---

## 7. Extra reusable actions for new topics (same math, parameter presets)

| Action | Built from | Key numbers |
|---|---|---|
| Sigh | idle + one breath event | inhale 12 f (sy +0.05, lean −3), hold 6, exhale 24 f (sy −0.02, lean +6, headTilt +8) |
| Head-shake "no" | faceX oscillation | `faceX = 0.4·e^(−t/0.4s)·sin(2π·2.5Hz·t)`, 3 swings |
| Nod "yes" | headTilt | `+8° · e^(−t/0.3s)·|sin(2π·2Hz·t)|` |
| Shoulder slump (giving up) | armN/F a +6, lean +10, sy 0.96 | 20 f `E.soft`, no overshoot |
| Look back over shoulder | faceX → −0.6, lean −3 | head leads by 3 f, 8 f |
| Reach for the phone (temptation) | ikArm to the phone | 14 f `E.soft`, hesitation hold 8 f at 70% reach |
| Shadow lean-in (antagonist) | heavy spring | `SPR.heavy`, scale 1→1.08, eye glow pulse `0.7 + 0.3·sin(2πf/45)` |

---

## 8. Putting it together in a Remotion component (sketch)

```tsx
import {useCurrentFrame, AbsoluteFill} from 'remotion';
export const ActorShot: React.FC<{action: Action; ground: V2}> = ({action, ground}) => {
  const frame = useCurrentFrame();
  const stops = action.events.filter(e => e.type === 'hitstop').map(e => ({at: e.f, hold: (e.data!.hold as number)}));
  const af = hitStop(frame, stops);                                  // character time
  const pose = action.poseAt(action.loop ? cyc(af, action.len) : af);
  const prev = action.poseAt(action.loop ? cyc(af - 1, action.len) : af - 1);
  const j = fk(pose, ground), jp = fk(prev, ground);
  // shake events are authored in action time → convert to screen time (shift by holds of EARLIER stops)
  const shakes = action.events.filter(e => e.type === 'shake').map(e => {
    const before = stops.filter(s => s.at < e.f).reduce((sum, x) => sum + x.hold, 0);
    return {at: e.f + before, ...(e.data as {A: number; tau: number; F: number; dX?: 1 | -1})};
  });
  const cam = cameraShake(frame, shakes);
  const sm = smear(jp.armN[2], j.armN[2], RIG.limbW);
  return (
    <AbsoluteFill style={{background: '#0e0e0e'}}>
      <svg viewBox="0 0 1920 1080">
        <g transform={`translate(${cam.x} ${cam.y}) rotate(${cam.r} 960 540)`}>
          {/* far arm, far leg, body, near leg, near arm, smear, band — renderer owned by agent 05/08 */}
          {sm && <path d={sm.d} fill="#e8e4d8" opacity={sm.opacity} />}
        </g>
      </svg>
    </AbsoluteFill>
  );
};
```

---

## 9. QA checklist for every generated shot

1. `poseAt` is pure: the same `f` gives an identical pose (snapshot test 3 random frames twice).
2. No joint angle jump > 40°/frame unless it is a flagged strike frame (smear expected).
3. Feet: in walks and runs, the stance foot's world x drift is < 2 px/frame (`plantY` + speed formula). Stairs: the foot on the tread has zero drift (IK).
4. Every impact has: an anticipation ≥ 2 f before it, hit-stop 2–3 f (Act 3 fights; **not** calm actions), a shake preset, an SFX event on the same frame, and follow-through ≥ 6 f.
5. Every text beat gets ≥ 12 f where the character is on an idle/moving hold.
6. Loops: `poseAt(0)` equals `poseAt(len)` (tables end with a row equal to the first).
7. The squash area check `sx·sy ∈ [0.97, 1.03]` unless a table says otherwise.
8. All `interpolate` calls are clamped, and all springs use `delay`.
9. No `Math.random`, `Date`, CSS animation or `transition`.
10. Shake F ≤ 12 Hz. Shakes are applied to the camera group, not to the character.

---

## 10. Remotion v4 API reference used here (verified 2026-10-14)

| API | Signature / notes |
|---|---|
| `interpolate(input, inputRange, outputRange, {extrapolateLeft, extrapolateRight, easing, posterize?, output?})` | extrapolate: `'extend'` (default) \| `'clamp'` \| `'wrap'` \| `'identity'`. Ranges have the same length. Newer 4.0.x versions also accept an `easing` array (one per segment), `posterize` (≥4.0.470) and `output: 'perceptual-scale'` (≥4.0.490). `track()` above avoids version dependence. |
| `spring({frame, fps, config:{mass=1, damping=10, stiffness=100, overshootClamping=false}, from=0, to=1, reverse=false, delay, durationInFrames, durationRestThreshold})` | Order of operations: duration stretch → reverse → delay. |
| `measureSpring({fps, config, threshold=0.005})` | returns frames to settle (e.g. damping 200 @30 fps → 23) |
| `Easing.bezier(x1,y1,x2,y2)`, `Easing.in/out/inOut(fn)`, `Easing.back(s)`, `Easing.elastic(b)`, `Easing.bounce`, `Easing.poly(n)`, `quad`, `cubic`, `sin`, `circle`, `exp`, `linear`, `step0`, `step1` | the bezier y-values may exceed [0,1] (overshoot) |
| `random(seed: number \| string \| null)` | [0,1), deterministic per seed. `null` = truly random (**never use**) |
| `noise2D(seed, x, y)`, `noise3D(seed, x, y, z)` from `@remotion/noise` | returns [−1, 1]; seed is a string or number |
| `@remotion/paths`: `interpolatePath(value, pathA, pathB)`, `evolvePath(progress, path)` → `{strokeDasharray, strokeDashoffset}`, `getLength`, `getPointAtLength`, `getTangentAtLength`, `parsePath`, `reversePath`, `translatePath`, `scalePath` | blanket breath morph, the ribbon/underline draw-on, motion paths (zZ, sweat) |
