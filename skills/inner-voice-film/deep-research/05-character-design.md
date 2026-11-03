# 05 — Hero Character Design, SVG Rig & Facial Expression Library

Agent 05 / 10 · Source: `research/00-brief/BRIEF.md` + all 20 reference frames (faces cropped and upscaled 4x, pixel colors sampled from PNGs).

---

## 0. TL;DR (the 10 rules that make it look right)

1. Body = **one cream capsule (stadium) with the head merged on top**. Head width = body width, no neck. A very slight "light-bulb" bulge at the head is optional.
2. **The body and head have NO dark outline.** Only the **near-side limbs** get a dark outline. This is the key to the look, and it also means the head can tilt with no visible seam.
3. Sampled colors: body `#dddacb`, far limbs `#a5a295`, ink/outline `#141210`, headband `#ef4b37` (range #eb4f39 to #f74a37), sweat `#bcd8f4`, blush `#e9a99c` at about 55% opacity, background `#0a0a0a`.
4. Limbs are **one SVG path per limb (shoulder→elbow→wrist)** with `stroke-linecap="round"` and `stroke-linejoin="round"`. Draw it twice: an ink stroke at width `w+2o`, then a cream stroke at width `w`. That gives an outlined tube with **no elbow seam**.
5. Hands are mittens: the round end of the tube plus a slightly larger blob. Feet are horizontal ellipses that point the way the character faces.
6. Draw order: far leg → far arm → body+head(face, headband) → near leg → near arm.
7. Joint positions are computed in TypeScript with **forward kinematics** (plus 2-bone IK for planted hands and feet). Limbs are drawn between those computed points. Nested `<g transform>` is used only for rigid parts (torso, head, face, accessories) and for placing the whole character. Limbs therefore cannot detach.
8. The face is very small. It sits in the upper half of the head, shifted about 6 units toward the facing side (a 3/4 read). Features: thick rounded bar brows, dot eyes, a single-stroke mouth. Expressions come almost entirely from **brow angle + eye type + mouth**.
9. The red headband is a sloppy thick stroke that overshoots the head silhouette, with a flapping tail on the back side. It is the "transformation symbol": it appears at the turning point and stays until the end.
10. Everything is frame-driven (`useCurrentFrame`, `interpolate`, `random(seed)`), with no CSS animation. Hand-drawn "boil" is used only on accessories, changing every 3 frames.

---

## 1. Anatomy spec

### 1.1 Measurements from the frames

The cleanest full-body reads are frame 8 (mirror, 1328 px wide) and frames 14 and 18. All rig units below use **body width = 100 units**, so **head radius = 50**. This matches the expression coordinate system.

| Part | Measured (f8, px @1328w) | Rig units | Notes |
|---|---|---|---|
| Total standing height | ~375 | **330** | ≈ 3.3 body widths |
| Body (head+torso capsule) width | ~115 | **100** | head ≈ torso width; head can bulge +2–4% |
| Head cap (top hemisphere) | — | r = 50, centre 280 above ground | merged, no neck, no chin |
| Capsule bottom | ~600 | 115 above ground | rounded bottom (bean) |
| Pelvis / hip joints | — | 130 above ground | hips sit inside the capsule bottom |
| Shoulder joint | ~chin level | 215 above ground (85 above pelvis) | near shoulder x=+10, far x=−4 |
| Limb thickness | ~30–32 | **26** | same for arms and legs |
| Upper arm / forearm | ~155 total | **62 / 58** | hanging hand ≈ 95 above ground (mid-thigh) |
| Thigh / shin | ~120 total | **60 / 58** | ankle 12 above ground |
| Hand (mitten) | slightly bulbous | circle r = 16 at wrist + 4 along forearm | no fingers ever |
| Foot | ~50 wide oval | ellipse rx 18, ry 11, centre = ankle + (8, 2) | points to facing side |
| Outline (near limbs only) | ~2–3 px | **2.6** | ≈ 4 px at 1080p when the hero is ~540 px tall |

Ratios: **head : torso : legs ≈ 1 : 1.15 : 1.15** by height (head cap 100, visible torso ≈ 115, visible legs ≈ 115). Arms hang to mid-thigh. Characters are about 1.5–1.7 rig units per px in medium shots (hero ≈ 500–550 px tall at 1080p). Wide shots use about 0.9 (≈ 300 px).

### 1.2 Colours (sampled)

| Token | Hex | Where |
|---|---|---|
| `fill` | `#dddacb` (brief estimate #e6e2d6 is slightly too light) | head, torso, near limbs |
| `farFill` | `#a5a295` | far arm, far leg (no outline) |
| `ink` | `#141210` (warm near-black) | near-limb outline, brows, eyes, mouth |
| `lidShadow` | `rgba(70,66,52,.45)` | under-eye bags (tired / sad) |
| `headband` | `#ef4b37` | transformation symbol |
| `sweat` / `tear` | `#bcd8f4` / `#9cc8f2` | drops |
| `blush` | `#e9a99c` @ .55 | straining, happy, in love |
| `teeth` | `#f3f0e6` | gritted teeth fill |
| `glow.phone` | `#5a8cff` @ .35 radial | face lit from phone (f5/f6) |
| `glow.dawn` | `#ff9a4a` drop-shadow 6–10 px | summit rim light (f18) |

Body edge: no ink outline. Against light-grey props (pillow, f2) a faint 1 px lighter rim (`#ecE9dc`) is visible. This is optional and looks like anti-aliasing.

### 1.3 Silhouettes per pose (from the frames)

| Pose | Frame | Silhouette description |
|---|---|---|
| **Lying in bed** | 2, 3, 4 | **Only the head circle** shows, resting on a flat grey pillow, with the blanket covering the rest. Head r is the same as standing. The face is shifted toward the camera/clock side. No limbs. |
| **Standing / sad** | 8 | Upright capsule with a slight forward hunch (lean 4°) and the head tipped down. The near arm hangs straight down in front of the body (outlined tube over the cream). The far leg (grey) is half a step behind. Feet are flat blobs. |
| **Sitting slouched with phone** | 5, 6 | On a couch, torso leaning back about 12°. The near leg is almost straight, running diagonally down to the floor. The far leg (grey) is bent down at the knee. The near forearm folds up across the chest, with the hand at the chin holding a small blue rounded-rect phone. A blue glow sits around the face. |
| **Desk slump** | 7 | Seated on a chair, torso tipped forward about 55° over the desk, head resting near the hand. The near arm reaches straight forward along the desktop. The legs fold under the seat (thigh forward, shin swung back). |
| **Curled, rock bottom** | 9 | Sitting on the floor. The capsule is tilted so the head leans forward and down. Knees are pulled up to the chest: thigh pointing up and forward, shin back down to a foot in front. One arm wraps over the shins; the other forearm goes up to the face, with the mitten covering eyes and nose. **Both arms are outlined** here (the far arm is promoted to near style for readability). The far leg is a grey wedge below. A spotlight and dust sit on top. |
| **Running** | 10 | Torso leans forward about 15–20°. The near leg is forward (thigh down and forward, shin vertical). The far leg is fully extended behind (grey, straight). The near arm is bent about 90° with the elbow back; the far arm is bent forward and shows behind the head as a grey stub. Speed lines are horizontal. |
| **Push-up plank** | 11, 12, 13 | The whole capsule is almost horizontal (root rotation about 78–82°), head at the front end, slightly raised. The legs are one straight tube trailing back to the toes; the far leg shows as a grey wedge under it. The near arm is short and bent. In the down phase the elbow pokes up and back in a "<" shape, with the mitten flat on the floor under the chest. |
| **Boxing guard** | 14 | Upright, lean about 8°. The near arm is folded tight with the fist at the chin (elbow down). The legs are in stance: near leg forward, far grey leg back, both nearly straight. |
| **Punch** | 15 | The near arm is extended forward and slightly up, almost straight. The body stays upright and the head leans in. The anger face has blush and stress marks. |
| **Climbing stairs** | 16, 17 | Torso leans forward about 20°. The near leg is lifted onto the next step (deep knee bend, knee in front of the belly). The far leg (grey) is extended back and down, pushing. Both arms are bent forward in a pumping/balancing position. |
| **Summit** | 18 | Tall and upright (lean −2°, chest slightly proud). The arms hang straight, the near leg is straight, and the far leg is slightly behind. There is a warm orange rim glow around the whole silhouette. |
| **Sitting on bed edge** | 19 | Upright torso. The thigh is horizontal forward and the shin vertical down to the floor. The near forearm rests along the thigh with the hand on the knee. Calm, determined face and headband. |

---

## 2. SVG rig design

### 2.1 Hierarchy (logical)

```
root (ground anchor x,y; rot pivots at pelvis)
└─ pelvis ── hipNear ─ thighNear ─ shinNear ─ footNear
│          └ hipFar  ─ thighFar  ─ shinFar  ─ footFar
└─ torso (lean, pivot = pelvis; breathing offset)
   ├─ shoulderNear ─ upperArmNear ─ forearmNear ─ handNear
   ├─ shoulderFar  ─ upperArmFar  ─ forearmFar  ─ handFar
   └─ neck pivot (0,-105) ─ head (tilt) ─ face (lookAt offset) + headband
```

### 2.2 Pivots (local coordinates, units; y is down, +x is the facing direction)

| Joint | Parent | Local position | Notes |
|---|---|---|---|
| ground anchor | — | (0,0) | the character's feet line |
| pelvis | root | (0, −130) | pivot for `root.rot` and `lean` |
| torso capsule | torso | rect x −50…50, y −175…+15, rx 50 | cream, no stroke |
| neck pivot | torso | (0, −105) | head tilt pivot |
| head centre | torso | (0, −150) | circle r 50, face origin |
| shoulderNear / Far | torso | (10, −85) / (−4, −88) | |
| hipNear / Far | pelvis (root frame) | (10, 0) / (−10, 0) | hips do **not** follow `lean` |
| elbow / wrist | chain | upper 62, fore 58 | |
| knee / ankle | chain | thigh 60, shin 58 | |

### 2.3 Angle convention (for the motion agent)

- `dir(a) = (sin a, cos a)`: **0° points straight down, +90° points forward** (toward the facing side).
- `root.rot` and `lean` are positive when the top tips **forward** (this equals SVG `rotate(+deg)`).
- A frame rotated by `θ` has "down" = `dir(−θ)`. Limb absolute angle = `−(root.rot+lean) + shoulder` for arms and `−root.rot + hip` for legs. Child = parent absolute + relative.
- **Elbow is positive** (forearm swings forward) when bent naturally. **Knee is negative** (shin swings back) when bent naturally.
- `facing="left"` is a `scale(-1,1)` around the character, so pose data never changes with facing.

### 2.4 FK-in-TypeScript vs nested `<g transform>` (recommendation)

| | Nested `<g transform>` per bone | **FK in TS, limbs drawn as one path between computed points** (recommended) |
|---|---|---|
| Elbow/knee seam | Two outlined capsules overlap, so the outline arc shows inside the joint. Fixing it needs a two-pass render with duplicated hierarchy. | One path with `linejoin=round`, so it is seamless by construction |
| Detachment | Safe only if every child sits exactly at the parent's end | Impossible: the child start **is** the parent end point |
| IK (planted hands/feet: push-ups, stairs, bed sitting) | Hard | Trivial (2-bone law of cosines, below) |
| Props attached to hands (phone, glove), contact points, text anchors | Need `getCTM` hacks | Joint world positions are plain numbers |
| Interpolating poses | Fine | Fine (same numbers) |
| Rigid parts (head, face, headband) | **Ideal** | Overkill |

**Recommendation: use a hybrid.** Compute all joint world positions once per frame with `solvePose()`. Draw limbs as paths through those points. Use nested transforms only for the torso capsule, the head (tilt about the neck pivot) and everything inside the head. The torso and limbs are computed from the same `pelvis + rotate(local, torsoRot)` math, so shoulders always land on the body. Add a dev assertion: `|elbow − shoulder| == upperLen ± 0.01`.

### 2.5 FK / IK helpers (TypeScript)

```ts
export type Vec = { x: number; y: number };
const R = Math.PI / 180;
export const dir = (deg: number): Vec => ({ x: Math.sin(deg * R), y: Math.cos(deg * R) }); // 0 = down, +90 = forward
export const add = (a: Vec, b: Vec): Vec => ({ x: a.x + b.x, y: a.y + b.y });
export const mul = (a: Vec, s: number): Vec => ({ x: a.x * s, y: a.y * s });
/** SVG-style clockwise rotation (y down). rot(v, θ) == what <g transform="rotate(θ)"> does. */
export const rot = (v: Vec, deg: number): Vec => {
  const c = Math.cos(deg * R), s = Math.sin(deg * R);
  return { x: v.x * c - v.y * s, y: v.x * s + v.y * c };
};

/** Forward kinematics for a 2-bone chain. baseAbs = absolute angle of the parent's "down". */
export function fk2(start: Vec, baseAbs: number, a: number, b: number, l1: number, l2: number) {
  const upper = baseAbs + a;
  const joint = add(start, mul(dir(upper), l1));
  const lower = upper + b;
  const end = add(joint, mul(dir(lower), l2));
  return { start, joint, end, upper, lower };
}

/** Analytic 2-bone IK. bend = +1 → joint pushed forward (knees), −1 → backward (elbows). */
export function ik2(start: Vec, target: Vec, l1: number, l2: number, bend: 1 | -1) {
  const dx = target.x - start.x, dy = target.y - start.y;
  const d = Math.min(Math.max(Math.hypot(dx, dy), Math.abs(l1 - l2) + 1e-3), l1 + l2 - 1e-3);
  const base = Math.atan2(dx, dy) / R;                       // same convention as dir()
  const cosA = (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d);
  const A = Math.acos(Math.max(-1, Math.min(1, cosA))) / R;
  const upper = base + bend * A;
  const joint = add(start, mul(dir(upper), l1));
  const end = add(start, mul(dir(base), d));
  const lower = Math.atan2(end.x - joint.x, end.y - joint.y) / R;
  return { start, joint, end, upper, lower };                 // upper/lower are absolute angles
}
```

Convert IK back to relative angles (if the motion agent wants to store them) with `a = upper − baseAbs` and `b = lower − upper`.

### 2.6 Limb drawing technique

```
path d = "M shoulder L elbow L wrist"
1) stroke ink,  width = 26 + 2*2.6, linecap/linejoin round   (near limbs only)
   + ink circle at hand, r = 16 + 2.6 (or ink ellipse for foot)
2) stroke fill, width = 26,          linecap/linejoin round
   + fill circle at hand, r = 16
```

Far limbs use a single pass in `#a5a295` with no ink. Very acute bends (over ~150°, as in the curled pose) still look right because of the round join.

---

## 3. Expression library

### 3.1 Face coordinate system

- Head centre (0,0), radius 50, facing **+x** (the whole character is mirrored for facing left).
- Face is offset toward the facing side. **Far eye centre (−12,−3)**, **near eye centre (24,−3)**, mouth centred at **x = 6, y ≈ 21**, brows at y ≈ −19, spanning x −23…−2 (far) and 13…35 (near).
- Stroke widths: brows **5.5**, mouth **3.6**, lid line **4.2**, eye-bag **3** (lidShadow), extras 2–2.5. All caps and joins are round, colour `ink`.
- Brows are always written as `M x1 y1 Q cx cy x2 y2` (far brow outer→inner, near brow inner→outer). Every brow has the same command structure, so `interpolatePath()` from `@remotion/paths` can morph between any two expressions. Mouths morph cleanly within the same family (line/curve); otherwise crossfade over 3–4 frames.
- Eye types: `dot` (solid ink circle), `wide` (bigger dot + white highlight top-left), `lid` (half-lidded: horizontal lid line with a lower-half pupil hanging under it, plus optional bags), `closed` (two arc paths).
- `lookAt` moves pupils up to ±2.5 units and the whole face up to ±4 units (a pseudo head turn).
- Blink: scale the eye group `scaleY(0.08)` about the eye centre over frames [0,2,4,6] → [1,.08,.08,1]. Blink every ~3–4 s, deterministic via `random(seed+cycle)`. Not used for `closed` eyes.

### 3.2 Expression table (what each one reads as)

| Name | Brows | Eyes | Mouth | Extras | Ref |
|---|---|---|---|---|---|
| `neutral` | flat | dot r5.5 | short flat line | — | — |
| `bored` / `sleepy` | flat, heavy | `lid` with bags | flat line | — | f2 |
| `asleep` | flat, relaxed, lower | closed ‿ arcs | soft smile | zZ rising (grey `#9a9a9a`) | f3 |
| `shocked` | raised, inner ends up | wide r8 + highlight | small filled "o" | sweat drop | f4 |
| `numb` (phone scroll) | flat, low | `lid`, pupils down, bags | flat (often hidden by hand) | blue phone glow | f5/f6 |
| `exhausted` | outer ends drooping | heavy `lid` (lower), small pupils, bags | slack slight frown | optional sweat | f7 |
| `sad` (defeated) | inner ends up, near brow arched | `lid` with bags | frown arc | — | f8 |
| `crying` (hidden) | strong inner up | closed ‿ arcs | small frown | tear streak, hand over face | f9 |
| `determined` | V (inner down ~20°) | dot r5.5 | short flat line | headband | f10/16/18 |
| `straining` | steep V (~30°) | dot r6 | gritted-teeth box with grid | sweat, stress `//` both cheeks, blush, anger vein | f11–15 |
| `confident` (quiet) | mild V | dot r5 | tiny closed smile | headband | f19 |
| `happy` | raised soft arcs | closed happy ∩ | open filled smile | blush | end |
| `lonely` | slight inner up | small dots looking down | tiny short line | — | new |
| `longing` | inner up, raised | wide r6.5 + highlight, looking up | tiny "o" | — | new |
| `inLove` | high soft arcs | wide r7, big highlight | gentle smile | blush, floating heart (`#ff8a80`) | new |
| `heartbroken` | very strong inner up | wide wet eyes + blue lower-lid pool | wobbly frown | tear | new |
| `anxious` | inner up, tense | small shiny dots (darting lookAt) | wavy line | sweat, stress marks | new |
| `overthinking` | asymmetric (near brow raised) | dots looking up-side | slanted line | grey scribble cloud above head | new |
| `hopeful` | raised gentle | wide r6.5 + highlight, looking slightly up | small smile | warm rim glow suggested | new |

### 3.3 Expression data (path data, head at (0,0) r 50)

```ts
export type EyeSpec =
  | { kind: 'dot'; r: number; dx?: number; dy?: number }
  | { kind: 'wide'; r: number; hl: number; dx?: number; dy?: number }
  | { kind: 'lid'; lidY: number; pupilR: number; bags: boolean }
  | { kind: 'closed'; d: [string, string] };

export type Extra =
  | 'sweat' | 'blush' | 'stress' | 'vein' | 'tear' | 'tearPool'
  | 'zz' | 'heart' | 'scribble' | 'phoneGlow';

export interface Expression {
  brows: [string, string];
  eyes: EyeSpec;
  mouth: { d: string; fill?: boolean; teeth?: boolean };
  extras?: Extra[];
}

const CLOSED_DOWN: [string, string] = ['M-19 -3 Q-12 3 -5 -3', 'M17 -3 Q24 3 31 -3']; // ‿ content / crying
const CLOSED_UP: [string, string] = ['M-19 0 Q-12 -7 -5 0', 'M17 0 Q24 -7 31 0'];    // ∩ happy

export const TEETH_BOX = 'M-7 14 H19 Q22 14 22 17 V25 Q22 28 19 28 H-7 Q-10 28 -10 25 V17 Q-10 14 -7 14 Z';
export const TEETH_GRID = 'M-10 21 H22 M-1 14 V28 M7 14 V28 M15 14 V28';

export const EXPRESSIONS = {
  neutral: {
    brows: ['M-23 -19 Q-12.5 -19 -2 -19', 'M13 -19 Q24 -19 35 -19'],
    eyes: { kind: 'dot', r: 5.5 },
    mouth: { d: 'M0 21 Q6 21 12 21' },
  },
  sleepy: {
    brows: ['M-23 -18 Q-12.5 -19 -2 -18', 'M13 -18 Q24 -19 35 -18'],
    eyes: { kind: 'lid', lidY: -4, pupilR: 5, bags: true },
    mouth: { d: 'M0 21 Q6.5 21 13 21' },
  },
  asleep: {
    brows: ['M-23 -16 Q-12.5 -17 -2 -16', 'M13 -16 Q24 -17 35 -16'],
    eyes: { kind: 'closed', d: CLOSED_DOWN },
    mouth: { d: 'M0 18 Q6 23 12 18' },
    extras: ['zz'],
  },
  shocked: {
    brows: ['M-24 -21 Q-13 -25 -3 -25', 'M14 -25 Q25 -25 35 -21'],
    eyes: { kind: 'wide', r: 8, hl: 2.4 },
    mouth: { d: 'M1 22 A5 6 0 1 0 11 22 A5 6 0 1 0 1 22 Z', fill: true },
    extras: ['sweat'],
  },
  numb: {
    brows: ['M-23 -17 Q-12.5 -17 -2 -17', 'M13 -17 Q24 -17 35 -17'],
    eyes: { kind: 'lid', lidY: -3, pupilR: 4.5, bags: true },
    mouth: { d: 'M1 22 Q6 22 11 22' },
    extras: ['phoneGlow'],
  },
  exhausted: {
    brows: ['M-23 -15 Q-13 -18 -2 -19', 'M13 -19 Q24 -18 35 -15'],
    eyes: { kind: 'lid', lidY: -1, pupilR: 4, bags: true },
    mouth: { d: 'M1 22 Q6 21 11 23' },
  },
  sad: {
    brows: ['M-23 -17 Q-13 -20 -2 -22', 'M13 -22 Q25 -23 35 -16'],
    eyes: { kind: 'lid', lidY: -4, pupilR: 5, bags: true },
    mouth: { d: 'M-1 25 Q6 18 13 25' },
  },
  crying: {
    brows: ['M-23 -16 Q-13 -19 -2 -22', 'M13 -22 Q24 -20 35 -16'],
    eyes: { kind: 'closed', d: CLOSED_DOWN },
    mouth: { d: 'M1 24 Q6 20 11 24' },
    extras: ['tear'],
  },
  determined: {
    brows: ['M-24 -24 Q-14 -21 -4 -16', 'M16 -16 Q26 -21 36 -24'],
    eyes: { kind: 'dot', r: 5.5 },
    mouth: { d: 'M1 21 Q6 21 11 21' },
  },
  straining: {
    brows: ['M-25 -27 Q-14 -22 -3 -14', 'M15 -14 Q26 -22 37 -27'],
    eyes: { kind: 'dot', r: 6 },
    mouth: { d: TEETH_BOX, teeth: true },
    extras: ['sweat', 'stress', 'blush', 'vein'],
  },
  confident: {
    brows: ['M-23 -22 Q-13 -20 -3 -17', 'M15 -17 Q25 -20 35 -22'],
    eyes: { kind: 'dot', r: 5 },
    mouth: { d: 'M0 20 Q6 23.5 12 20' },
  },
  happy: {
    brows: ['M-23 -21 Q-12.5 -26 -2 -22', 'M13 -22 Q24 -26 35 -21'],
    eyes: { kind: 'closed', d: CLOSED_UP },
    mouth: { d: 'M-3 16 Q6 18 15 16 Q14 28 6 28 Q-2 28 -3 16 Z', fill: true },
    extras: ['blush'],
  },
  lonely: {
    brows: ['M-23 -17 Q-13 -19 -2 -21', 'M13 -21 Q24 -19 35 -17'],
    eyes: { kind: 'dot', r: 4.5, dy: 2 },
    mouth: { d: 'M3 22 Q6 22 9 22' },
  },
  longing: {
    brows: ['M-23 -19 Q-13 -23 -2 -24', 'M13 -24 Q24 -23 35 -19'],
    eyes: { kind: 'wide', r: 6.5, hl: 2, dx: 1.5, dy: -2 },
    mouth: { d: 'M4 22 A2.5 3 0 1 0 9 22 A2.5 3 0 1 0 4 22 Z', fill: true },
  },
  inLove: {
    brows: ['M-23 -22 Q-12.5 -27 -2 -23', 'M13 -23 Q24 -27 35 -22'],
    eyes: { kind: 'wide', r: 7, hl: 3 },
    mouth: { d: 'M-1 19 Q6 25 13 19' },
    extras: ['blush', 'heart'],
  },
  heartbroken: {
    brows: ['M-23 -16 Q-12 -21 -1 -26', 'M13 -26 Q24 -21 35 -16'],
    eyes: { kind: 'wide', r: 7, hl: 2.5 },
    mouth: { d: 'M-3 25 Q0 20 3 22 Q6 24 9 21 Q12 19 15 25' },
    extras: ['tearPool', 'tear'],
  },
  anxious: {
    brows: ['M-23 -18 Q-12 -21 -2 -25', 'M13 -25 Q24 -21 35 -18'],
    eyes: { kind: 'wide', r: 5, hl: 1.6 },
    mouth: { d: 'M-3 22 Q0 19 3 22 Q6 25 9 22 Q12 19 15 22' },
    extras: ['sweat', 'stress'],
  },
  overthinking: {
    brows: ['M-23 -18 Q-12.5 -18 -2 -17', 'M13 -24 Q24 -29 35 -26'],
    eyes: { kind: 'dot', r: 5, dx: 2, dy: -3 },
    mouth: { d: 'M2 23 Q7.5 21.5 13 20' },
    extras: ['scribble'],
  },
  hopeful: {
    brows: ['M-23 -21 Q-13 -25 -2 -25', 'M13 -25 Q24 -25 35 -21'],
    eyes: { kind: 'wide', r: 6.5, hl: 2.2, dy: -1 },
    mouth: { d: 'M1 20 Q6 24 11 20' },
  },
} satisfies Record<string, Expression>;
export type ExpressionName = keyof typeof EXPRESSIONS;

/** Extras: path data (head-local, facing +x). */
export const EXTRA_PATHS = {
  sweat: 'M36 -36 Q31 -27 33 -24 A4 4 0 0 0 39 -24 Q41 -27 36 -36 Z',      // fill #bcd8f4
  sweatHi: 'M35 -28 A1.2 1.6 0 1 0 35.1 -28 Z',                             // fill #ffffff .8
  blush: [{ cx: -20, cy: 9, r: 4.5 }, { cx: 33, cy: 9, r: 4.5 }],             // fill #e9a99c .55
  stress: 'M-31 5 L-26 0 M-30 10 L-25 5 M38 5 L43 0 M39 10 L44 5',          // ink, sw 2.2 ("//" on both cheeks)
  vein: 'M21 -40 Q26 -37 24 -42 M33 -40 Q28 -37 30 -42 M21 -30 Q26 -33 24 -28 M33 -30 Q28 -33 30 -28', // ink (on band) or #c9372a, sw 2.4
  tear: 'M-12 2 Q-13 9 -12 15',                                              // #9cc8f2 sw 2.5 + drop below
  tearDrop: 'M-12 15 Q-16 23 -12 26 Q-8 23 -12 15 Z',                        // fill #9cc8f2 (animate y with gravity)
  tearPool: 'M-19 4 Q-12 8 -5 4 M17 4 Q24 8 31 4',                           // #9cc8f2 sw 2
  heart: 'M0 3 C-2 -2 -9 -1 -9 4 C-9 9 -2 12 0 15 C2 12 9 9 9 4 C9 -1 2 -2 0 3 Z', // translate(42 -52), fill #ff8a80
  scribble: 'M-10 -78 C-30 -90 -5 -110 10 -95 C25 -80 -20 -75 0 -100 C15 -118 40 -95 20 -85 C5 -78 30 -70 35 -90', // #8a8a8a sw 2, animate with evolvePath
  // zz: two <text> "z" (size 12, 16) at (30,-62) and (40,-84), fill #9a9a9a, float up and fade, counter-flipped
  // phoneGlow: radialGradient centre (10, 40) r 70, #5a8cff .35 → 0, clipped to head circle
};
```

Lid-eye construction (for eye centre `c`): lid `M(c.x−10) lidY L(c.x+10) lidY` at sw 4.2. Pupil `M(c.x−r) lidY A r r 0 0 0 (c.x+r) lidY Z` filled; with sweep 0 this is the lower half disc. Bag `M(c.x−8) (lidY+9) Q c.x (lidY+12) (c.x+8) (lidY+9)` at sw 3 in lidShadow.

Gritted teeth: `TEETH_BOX` filled `#f3f0e6` with an ink stroke of 3, then `TEETH_GRID` in ink at sw 2. This matches f11–f15 (one horizontal line and three vertical lines).

---

## 4. Accessory system and transformation symbols

### 4.1 The red headband (DISCIPLINE)

- **Shape:** a thick stroke (sw 8 in head units, round caps, `#ef4b37`) across the forehead: `M-57 -29 Q0 -42 55 -25`. It is tilted (front lower) and **overshoots the head silhouette on both ends**, which is the sloppy hand-drawn look in f15 and f19. It sits just above the brows. Straining brows touch it, which reads well.
- **Tail:** a 6-segment polyline from the back end (−55,−28) trailing backward and down (sw 6). Each point's y gets `sin(frame*0.45 − i*0.9) * t * (3 + wind*8)`, so the flap grows toward the tip. `wind` goes from 0 (idle; the tail droops down as in f19) to 1 (running; the tail streams horizontal).
- **Boil:** control points jitter ±0.6 units with `random(seed+floor(frame/3))`. Only accessories boil; the body stays clean as in the reference.
- **Anger vein marks** can be drawn **on** the band in ink (f15).
- **Story function:** it is absent in all "failure" shots (f2–f9). It appears the moment the hero chooses (the 5:00 calm wake-up / Day 1) and is present in every later shot, including the final 5:00 shot (f19). The end-card underline is the same red with the same wavy hand-drawn stroke, so **the symbol and the title share colour and stroke style.**

### 4.2 Rule set for new topics

Each film gets **one** transformation symbol that:
1. is a **single colour** that does not clash with the antagonist's red glow. Red is acceptable only when the story is about reclaiming power from the inner voice.
2. reads at 300 px character height (thick stroke, simple silhouette).
3. attaches to a rig slot that **moves with secondary motion** (head, neck or wrist) so it feels alive.
4. appears exactly at the turning point and never leaves.
5. is echoed in the end-card underline or title colour.

| Topic | Symbol | Slot | Colour | Secondary motion |
|---|---|---|---|---|
| Discipline | headband | head | `#ef4b37` | flapping tail |
| Loneliness | knitted scarf (given by someone) | neck | warm amber `#f2a541` | two tails flap |
| Love | red thread tied to the wrist, leading off-screen | wrist | `#ff6b6b` | catenary sag + sway |
| Grief | a small flower held or tucked behind the ear | hand / head | soft white-yellow `#f5e6a8` | petals sway, one petal falls |
| Anxiety | glowing breath light / small lantern | hand | pale cyan `#9fe3ff` | pulsing glow synced to "breathe" |
| Overthinking | pencil behind the ear / notebook | head / hand | `#ffd166` | scribbles collapse into one straight line |
| Dopamine | phone left face-down, then a book | hand | (absence) / `#ffd166` | — |
| Hope / ready | small sprout or sunrise rim light | hand / rim | `#ffb56b` | grows across acts |

Slot API: `accessories={[{ type: 'headband', color, wind }, { type: 'scarf', ... }]}`. Each accessory is a component that receives `(frame, joints)` and draws in head-local space (head slot) or world space at a joint (wrist/hand slots). This is one reason FK points in TS are needed.

---

## 5. React component API and pose format

### 5.1 API

```tsx
<Hero
  pose={POSES.standing}                // or a lerped / procedural Pose
  expression="determined"              // ExpressionName
  prevExpression="sad" exprProgress={t} // optional 3–4 frame crossfade
  headband={{ wind: 0.8 }}             // true | false | {color, wind}
  blink                                 // auto deterministic blink
  lookAt={{ x: 0.3, y: -0.2 }}         // −1..1
  breathing                             // true | amplitude in units (default 2)
  facing="right"                        // 'right' | 'left'
  scale={1.6}  x={960} y={900}         // y = ground line in px
  glow="#ff9a4a"                        // optional rim glow (summit / spotlight)
  mode="full"                           // 'full' | 'headOnly' (in bed)
  seed="hero"
/>
```

### 5.2 Pose data format (what the motion agent animates)

```ts
export interface LimbPose { a: number; b: number; ik?: { x: number; y: number; bend: 1 | -1 } }
export interface Pose {
  root: { x: number; y: number; rot: number }; // ground-relative offset (units) and whole-body tip
  lean: number;      // torso about pelvis, + = forward
  headTilt: number;  // about neck, + = nod forward/down
  armNear: LimbPose; armFar: LimbPose;  // a = shoulder, b = elbow (+ = natural bend)
  legNear: LimbPose; legFar: LimbPose;  // a = hip,      b = knee  (− = natural bend)
  footNear?: number; footFar?: number;  // absolute foot angle, 0 = flat
  farArmOutlined?: boolean;             // f9 curled pose
}
```

All poses are plain numbers. `lerpPose(p1, p2, t)` interpolates every field, and `spring()` drives `t`. IK targets are in the same ground-relative units. When `ik` is set it overrides `a`/`b` (push-up hands, stair feet, sitting feet).

### 5.3 Pose library (starting values)

| Pose | root (x,y,rot) | lean | head | armNear a/b | armFar a/b | legNear a/b | legFar a/b | feet |
|---|---|---|---|---|---|---|---|---|
| `standing` | 0,0,0 | 0 | 0 | 4/6 | −4/6 | 3/−2 | −4/−2 | 0 |
| `sadStand` (f8) | 0,0,0 | 4 | 8 | 6/2 | −2/4 | 2/0 | −6/0 | 0 |
| `sitBedEdge` (f19) | 0,55,0 | −2 | 0 | 25/45 | 15/40 | 88/−88 | 82/−84 | 0 |
| `couchPhone` (f5) | 0,55,0 | −12 | 8 | 20/140 | 5/30 | 55/−10 | 80/−80 | 0 |
| `deskSlump` (f7) | 0,55,0 | 55 | 10 | 75/15 | 70/10 | 80/−110 | 75/−105 | 0 |
| `curled` (f9) | 0,115,0 | 22 | 15 | 105/65 | 40/150 | 150/−150 | 140/−140 | 20 (far arm outlined) |
| `pushupUp` | 0,95,80 | 0 | −12 | ik hand (40,−2), bend −1 | hidden | 0/0 | 0/−2 | 70 |
| `pushupDown` | 0,108,82 | 0 | −8 | ik hand (40,−2), bend −1 | hidden | 0/0 | 0/−2 | 70 |
| `run(φ)` | 0, 4·|sin φ|, 0 | 16 | −4 | −35·sin φ / 85 | 35·sin φ / 85 | 35·sin φ / −(10+60·max(0,−cos φ)) | mirrored (φ+π) | 0 |
| `guard` (f14) | 0,0,0 | 8 | 4 | −10/140 | 20/120 | 18/−5 | −18/−3 | 0 |
| `punch` (f15) | 0,0,0 | 12 | 6 | 85/5 | 20/120 | 20/−5 | −20/−3 | 0 |
| `climb` (f16) | 0,0,0 | 20 | −4 | 30/70 | −20/60 | ik foot on next step, bend +1 | −25/−10 | 0 |
| `summit` (f18) | 0,0,0 | −2 | −3 | 2/4 | −2/4 | 2/0 | −8/0 | 0 |
| `lyingInBed` | mode `headOnly`, head rot −10…10, face shifted toward the clock | | | | | | | |

Motion notes for agent 06: snooze **slap** = arm IK to the clock over 4 frames with overshoot. Calm wake-up = a 20-frame ease. Run cycle about 16 frames per stride at 30 fps. Breathing = 0.25 Hz sine, ±2 units on the shoulders and head. Head bob in the run = 4·|sin φ|.

---

## 6. Complete example — `Hero.tsx` (standing pose + face)

```tsx
// src/hero/Hero.tsx
import React from 'react';
import { useCurrentFrame, useVideoConfig, interpolate, random } from 'remotion';
import { EXPRESSIONS, ExpressionName, EyeSpec, EXTRA_PATHS, TEETH_GRID } from './expressions';

/* ---------- constants ---------- */
export const HERO = {
  fill: '#dddacb',
  farFill: '#a5a295',
  ink: '#141210',
  lidShadow: 'rgba(70,66,52,0.45)',
  band: '#ef4b37',
  outline: 2.6,
  limbW: 26,
  headR: 50,
  pelvisH: 130,
  upperArm: 62, foreArm: 58, thigh: 60, shin: 58,
  handR: 16,
  shoulderNear: { x: 10, y: -85 }, shoulderFar: { x: -4, y: -88 },
  hipNear: { x: 10, y: 0 }, hipFar: { x: -10, y: 0 },
  neck: { x: 0, y: -105 }, headC: { x: 0, y: -150 },
} as const;

/* ---------- math ---------- */
export type Vec = { x: number; y: number };
const DEG = Math.PI / 180;
const dir = (d: number): Vec => ({ x: Math.sin(d * DEG), y: Math.cos(d * DEG) });
const add = (a: Vec, b: Vec): Vec => ({ x: a.x + b.x, y: a.y + b.y });
const mul = (a: Vec, s: number): Vec => ({ x: a.x * s, y: a.y * s });
const rot = (v: Vec, d: number): Vec => {
  const c = Math.cos(d * DEG), s = Math.sin(d * DEG);
  return { x: v.x * c - v.y * s, y: v.x * s + v.y * c };
};

export interface LimbPose { a: number; b: number; ik?: { x: number; y: number; bend: 1 | -1 } }
export interface Pose {
  root: { x: number; y: number; rot: number };
  lean: number; headTilt: number;
  armNear: LimbPose; armFar: LimbPose; legNear: LimbPose; legFar: LimbPose;
  footNear?: number; footFar?: number; farArmOutlined?: boolean;
}

export const POSES: Record<'standing', Pose> = {
  standing: {
    root: { x: 0, y: 0, rot: 0 }, lean: 0, headTilt: 0,
    armNear: { a: 4, b: 6 }, armFar: { a: -4, b: 6 },
    legNear: { a: 3, b: -2 }, legFar: { a: -4, b: -2 },
  },
};

type Chain = { start: Vec; joint: Vec; end: Vec; lower: number };

function chain(start: Vec, baseAbs: number, lp: LimbPose, l1: number, l2: number): Chain {
  if (lp.ik) {
    const t = { x: lp.ik.x, y: lp.ik.y };
    const dx = t.x - start.x, dy = t.y - start.y;
    const d = Math.min(Math.max(Math.hypot(dx, dy), Math.abs(l1 - l2) + 1e-3), l1 + l2 - 1e-3);
    const base = Math.atan2(dx, dy) / DEG;
    const A = Math.acos(Math.max(-1, Math.min(1, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d)))) / DEG;
    const joint = add(start, mul(dir(base + lp.ik.bend * A), l1));
    const end = add(start, mul(dir(base), d));
    return { start, joint, end, lower: Math.atan2(end.x - joint.x, end.y - joint.y) / DEG };
  }
  const upper = baseAbs + lp.a;
  const joint = add(start, mul(dir(upper), l1));
  const lower = upper + lp.b;
  return { start, joint, end: add(joint, mul(dir(lower), l2)), lower };
}

export function solvePose(p: Pose, breathe = 0) {
  const pelvis: Vec = { x: p.root.x, y: p.root.y - HERO.pelvisH };
  const torsoRot = p.root.rot + p.lean;
  const T = (v: Vec) => add(pelvis, rot(v, torsoRot));
  const Rt = (v: Vec) => add(pelvis, rot(v, p.root.rot));
  const lift = (v: Vec): Vec => ({ x: v.x, y: v.y - breathe * 0.8 });
  return {
    pelvis, torsoRot,
    armNear: chain(T(lift(HERO.shoulderNear)), -torsoRot, p.armNear, HERO.upperArm, HERO.foreArm),
    armFar: chain(T(lift(HERO.shoulderFar)), -torsoRot, p.armFar, HERO.upperArm, HERO.foreArm),
    legNear: chain(Rt(HERO.hipNear), -p.root.rot, p.legNear, HERO.thigh, HERO.shin),
    legFar: chain(Rt(HERO.hipFar), -p.root.rot, p.legFar, HERO.thigh, HERO.shin),
  };
}

/* ---------- limbs ---------- */
const pathOf = (pts: Vec[]) =>
  pts.map((q, i) => `${i ? 'L' : 'M'}${q.x.toFixed(2)} ${q.y.toFixed(2)}`).join(' ');

const Limb: React.FC<{ c: Chain; near: boolean; kind: 'arm' | 'leg'; footAngle?: number }> = ({
  c, near, kind, footAngle = 0,
}) => {
  const d = pathOf([c.start, c.joint, c.end]);
  const w = HERO.limbW, o = HERO.outline;
  const hand = add(c.end, mul(dir(c.lower), 4));
  const foot = add(c.end, rot({ x: 8, y: 2 }, footAngle));
  const End = ({ grow, fill }: { grow: number; fill: string }) =>
    kind === 'arm' ? (
      <circle cx={hand.x} cy={hand.y} r={HERO.handR + grow} fill={fill} />
    ) : (
      <ellipse cx={foot.x} cy={foot.y} rx={18 + grow} ry={11 + grow} fill={fill}
        transform={`rotate(${footAngle} ${foot.x} ${foot.y})`} />
    );
  const stroke = { fill: 'none', strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const };
  if (!near) {
    return (<g><path d={d} {...stroke} stroke={HERO.farFill} strokeWidth={w} /><End grow={0} fill={HERO.farFill} /></g>);
  }
  return (
    <g>
      <path d={d} {...stroke} stroke={HERO.ink} strokeWidth={w + 2 * o} />
      <End grow={o} fill={HERO.ink} />
      <path d={d} {...stroke} stroke={HERO.fill} strokeWidth={w} />
      <End grow={0} fill={HERO.fill} />
    </g>
  );
};

/* ---------- face ---------- */
const EYE_C: [Vec, Vec] = [{ x: -12, y: -3 }, { x: 24, y: -3 }];

const Eye: React.FC<{ i: 0 | 1; spec: EyeSpec; blink: number; look: Vec }> = ({ i, spec, blink, look }) => {
  const c = EYE_C[i];
  const ink = HERO.ink;
  if (spec.kind === 'closed') {
    return <path d={spec.d[i]} fill="none" stroke={ink} strokeWidth={4.2} strokeLinecap="round" />;
  }
  if (spec.kind === 'lid') {
    const r = spec.pupilR, y = spec.lidY;
    return (
      <g>
        <g transform={`translate(${c.x + look.x * 1.5} 0)`}>
          <g transform={`translate(0 ${y}) scale(1 ${blink}) translate(0 ${-y})`}>
            <path d={`M${-r} ${y} A${r} ${r} 0 0 0 ${r} ${y} Z`} fill={ink} />
          </g>
        </g>
        <path d={`M${c.x - 10} ${y} L${c.x + 10} ${y}`} stroke={ink} strokeWidth={4.2} strokeLinecap="round" />
        {spec.bags && (
          <path d={`M${c.x - 8} ${y + 9} Q${c.x} ${y + 12} ${c.x + 8} ${y + 9}`}
            fill="none" stroke={HERO.lidShadow} strokeWidth={3} strokeLinecap="round" />
        )}
      </g>
    );
  }
  const ex = c.x + (spec.dx ?? 0) + look.x * 2.5;
  const ey = c.y + (spec.dy ?? 0) + look.y * 2.5;
  return (
    <g transform={`translate(${ex} ${ey}) scale(1 ${blink})`}>
      <circle r={spec.r} fill={ink} />
      {spec.kind === 'wide' && <circle cx={-spec.r * 0.32} cy={-spec.r * 0.32} r={spec.hl} fill="#ffffff" />}
    </g>
  );
};

export const Face: React.FC<{
  expression: ExpressionName; frame: number; blink?: number; look?: Vec; flipped?: boolean;
}> = ({ expression, frame, blink = 1, look = { x: 0, y: 0 }, flipped = false }) => {
  const e = EXPRESSIONS[expression];
  const extras = e.extras ?? [];
  const ink = HERO.ink;
  const has = (x: string) => (extras as string[]).includes(x);
  const bob = Math.sin(frame / 6) * 1.2; // sweat/heart float
  return (
    <g transform={`translate(${look.x * 4} ${look.y * 3})`}>
      {has('phoneGlow') && (
        <>
          <defs>
            <radialGradient id="phoneGlow" cx="0.6" cy="0.9" r="0.8">
              <stop offset="0" stopColor="#5a8cff" stopOpacity={0.35} />
              <stop offset="1" stopColor="#5a8cff" stopOpacity={0} />
            </radialGradient>
          </defs>
          <circle r={50} fill="url(#phoneGlow)" />
        </>
      )}
      {has('blush') && EXTRA_PATHS.blush.map((b, k) => (
        <circle key={k} cx={b.cx} cy={b.cy} r={b.r} fill="#e9a99c" opacity={0.55} />
      ))}
      {e.brows.map((d, k) => (
        <path key={k} d={d} fill="none" stroke={ink} strokeWidth={5.5} strokeLinecap="round" />
      ))}
      <Eye i={0} spec={e.eyes} blink={blink} look={look} />
      <Eye i={1} spec={e.eyes} blink={blink} look={look} />
      {'teeth' in e.mouth && e.mouth.teeth ? (
        <g>
          <path d={e.mouth.d} fill="#f3f0e6" stroke={ink} strokeWidth={3} strokeLinejoin="round" />
          <path d={TEETH_GRID} stroke={ink} strokeWidth={2} />
        </g>
      ) : (
        <path d={e.mouth.d} fill={'fill' in e.mouth && e.mouth.fill ? ink : 'none'}
          stroke={ink} strokeWidth={3.6} strokeLinecap="round" strokeLinejoin="round" />
      )}
      {has('stress') && <path d={EXTRA_PATHS.stress} stroke={ink} strokeWidth={2.2} strokeLinecap="round" />}
      {has('vein') && <path d={EXTRA_PATHS.vein} fill="none" stroke={ink} strokeWidth={2.4} strokeLinecap="round" />}
      {has('sweat') && (
        <g transform={`translate(0 ${Math.max(0, bob)})`}>
          <path d={EXTRA_PATHS.sweat} fill="#bcd8f4" />
          <path d={EXTRA_PATHS.sweatHi} fill="#ffffff" opacity={0.8} />
        </g>
      )}
      {has('tearPool') && <path d={EXTRA_PATHS.tearPool} fill="none" stroke="#9cc8f2" strokeWidth={2} strokeLinecap="round" />}
      {has('tear') && (
        <g>
          <path d={EXTRA_PATHS.tear} fill="none" stroke="#9cc8f2" strokeWidth={2.5} strokeLinecap="round" opacity={0.85} />
          <g transform={`translate(0 ${(frame % 30) * 0.8})`} opacity={interpolate(frame % 30, [0, 25, 30], [1, 1, 0])}>
            <path d={EXTRA_PATHS.tearDrop} fill="#9cc8f2" />
          </g>
        </g>
      )}
      {has('heart') && (
        <g transform={`translate(42 ${-52 + bob})`}><path d={EXTRA_PATHS.heart} fill="#ff8a80" /></g>
      )}
      {has('scribble') && <path d={EXTRA_PATHS.scribble} fill="none" stroke="#8a8a8a" strokeWidth={2} strokeLinecap="round" />}
      {has('zz') && (
        <g transform={flipped ? 'scale(-1 1)' : undefined}>
          {[0, 1].map((k) => {
            const t = ((frame + k * 20) % 40) / 40;
            return (
              <text key={k} x={(flipped ? -1 : 1) * (30 + k * 10) + t * 6} y={-62 - k * 20 - t * 12}
                fontSize={12 + k * 4} fontFamily="'Comic Neue', 'Comic Sans MS', cursive" fontWeight={700}
                fill="#9a9a9a" opacity={interpolate(t, [0, 0.2, 0.8, 1], [0, 1, 1, 0])}>z</text>
            );
          })}
        </g>
      )}
    </g>
  );
};

/* ---------- headband ---------- */
export const Headband: React.FC<{ frame: number; color?: string; wind?: number; seed?: string }> = ({
  frame, color = HERO.band, wind = 0.3, seed = 'band',
}) => {
  const step = Math.floor(frame / 3);
  const j = (k: string) => (random(`${seed}-${k}-${step}`) - 0.5) * 1.2;
  const band = `M${-57 + j('a')} ${-29 + j('b')} Q${j('c')} ${-42 + j('d')} ${55 + j('e')} ${-25 + j('f')}`;
  const N = 6;
  const tail = Array.from({ length: N + 1 }, (_, i) => {
    const t = i / N;
    const flap = Math.sin(frame * 0.45 - i * 0.9) * t * (3 + wind * 8);
    return { x: -55 - t * (24 + wind * 14), y: -28 + t * (16 - wind * 12) + flap };
  });
  return (
    <g fill="none" stroke={color} strokeLinecap="round" strokeLinejoin="round">
      <path d={pathOf(tail)} strokeWidth={6} />
      <path d={band} strokeWidth={8} />
    </g>
  );
};

/* ---------- blink ---------- */
export const blinkAmount = (frame: number, seed: string, period = 105) => {
  const k = Math.floor(frame / period);
  const t = frame - k * period - Math.floor(random(`${seed}-blink-${k}`) * (period - 10));
  return t < 0 || t > 6 ? 1 : interpolate(t, [0, 2, 4, 6], [1, 0.08, 0.08, 1]);
};

/* ---------- Hero ---------- */
export interface HeroProps {
  pose?: Pose;
  expression?: ExpressionName;
  prevExpression?: ExpressionName;
  exprProgress?: number;              // 0..1 crossfade prev → expression
  headband?: boolean | { color?: string; wind?: number };
  blink?: boolean;
  lookAt?: Vec;
  breathing?: boolean | number;
  facing?: 'right' | 'left';
  scale?: number;
  x?: number; y?: number;              // px, y = ground line
  glow?: string;
  mode?: 'full' | 'headOnly';
  headRot?: number;                    // headOnly
  seed?: string;
}

export const Hero: React.FC<HeroProps> = ({
  pose = POSES.standing, expression = 'neutral', prevExpression, exprProgress = 1,
  headband = false, blink = true, lookAt = { x: 0, y: 0 }, breathing = true,
  facing = 'right', scale = 1.6, x = 960, y = 900, glow, mode = 'full', headRot = 0, seed = 'hero',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const amp = typeof breathing === 'number' ? breathing : breathing ? 2 : 0;
  const b = amp * Math.sin((frame / fps) * Math.PI * 2 * 0.25);
  const bl = blink ? blinkAmount(frame, seed) : 1;
  const flip = facing === 'left';
  const band = headband ? (typeof headband === 'object' ? headband : {}) : null;

  const head = (
    <>
      <circle r={HERO.headR} fill={HERO.fill} />
      {prevExpression && exprProgress < 1 && (
        <g opacity={1 - exprProgress}>
          <Face expression={prevExpression} frame={frame} blink={bl} look={lookAt} flipped={flip} />
        </g>
      )}
      <g opacity={prevExpression ? exprProgress : 1}>
        <Face expression={expression} frame={frame} blink={bl} look={lookAt} flipped={flip} />
      </g>
      {band && <Headband frame={frame} color={band.color} wind={band.wind} seed={`${seed}-band`} />}
    </>
  );

  const style = glow ? { filter: `drop-shadow(0 0 8px ${glow})` } : undefined;

  if (mode === 'headOnly') {
    return (
      <g transform={`translate(${x} ${y}) scale(${flip ? -scale : scale} ${scale}) rotate(${headRot})`} style={style}>
        {head}
      </g>
    );
  }

  const J = solvePose(pose, b);
  const torso = (
    <g transform={`translate(${J.pelvis.x} ${J.pelvis.y}) rotate(${J.torsoRot})`}>
      <rect x={-50} y={-175 - b} width={100} height={190 + b} rx={50} fill={HERO.fill} />
      <g transform={`rotate(${pose.headTilt} ${HERO.neck.x} ${HERO.neck.y - b})`}>
        <g transform={`translate(${HERO.headC.x} ${HERO.headC.y - b})`}>{head}</g>
      </g>
    </g>
  );

  return (
    <g transform={`translate(${x} ${y}) scale(${flip ? -scale : scale} ${scale})`} style={style}>
      <Limb c={J.legFar} near={false} kind="leg" footAngle={pose.footFar ?? 0} />
      <Limb c={J.armFar} near={!!pose.farArmOutlined} kind="arm" />
      {torso}
      <Limb c={J.legNear} near kind="leg" footAngle={pose.footNear ?? 0} />
      <Limb c={J.armNear} near kind="arm" />
    </g>
  );
};

/* ---------- usage ---------- */
// <svg viewBox="0 0 1920 1080"><Hero pose={POSES.standing} expression="determined" headband={{ wind: 0.2 }} /></svg>
```

`expressions.ts` contains section 3.3 verbatim (`EXPRESSIONS`, `EyeSpec`, `EXTRA_PATHS`, `TEETH_GRID`, `ExpressionName`).

Notes on the code:
- `Face` gets `frame` explicitly, so it can be reused in `headOnly` bed shots and in the mirror reflection.
- `zZ` is counter-flipped so the letters are never mirrored. Any other text must live outside the Hero group.
- The phone-glow gradient id should be suffixed with `seed` if two heroes are on screen.
- Utilities still to add: `lerpPose(a, b, t)` (field-wise `interpolate`), `runPose(phase)` (formulas in 5.3), and `interpolatePath` brow morphing (`@remotion/paths`) as an alternative to crossfade.

---

## 7. Handoff checklist for other agents

- **Motion (06):** animate only `Pose` numbers, `lookAt`, `expression` swaps (with a 3–4 frame crossfade) and `headband.wind`. Never animate SVG transforms on limbs directly.
- **Antagonist:** the red shadow can reuse the exact same rig. Use the body fill `#000`, no near-limb outline, a red `drop-shadow` glow, and a face with only two short red slits and a red smile arc (stroke `#ff5a4a`, sw 4). One rig serves both characters, so the mirror shot (f8) is just `<Hero>` with a shadow skin.
- **Layout:** hero height ≈ 500–550 px (scale 1.6) in medium shots, ≈ 300 px (0.9) in wide shots, head r ≈ 35 px in bed shots (`headOnly`, scale 0.7). The ground line is a 2 px `#6b6b6b` stroke at the hero's `y`.
