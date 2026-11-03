# 07 — Environments, Props, Lighting, Color Grading & Camera/Composition

Research agent 07/10. Source: `00-brief/BRIEF.md`, both scripts, and close inspection of all 20 reference frames.
All coordinates use a **1920x1080** canvas. All hex values are **estimated by eye** from compressed screenshots, so treat them as starting tokens and tune them once.
The target stack is Remotion + SVG with deterministic, frame-driven animation (no CSS keyframes, no `Math.random()` at render time).

---

## 0. TL;DR, the look in one paragraph

Near-black stage (`#0e0e0e` center → `#060606` edges) with a large, soft **elliptical vignette**. A single thin gray **floor line** sits around 80–86% of frame height. The props are flat dark fills with **2.5–3px light-gray rounded outlines** that look hand-drawn: slightly uneven, round caps and joins, and never perfectly straight. Glows are the only real light sources: moon (cool white), phone (blue), desk lamp and streetlights (warm amber), antagonist (red), spotlight (neutral white), dawn (orange). Each scene has exactly **one** accent light. Most shots are static wide shots. Emotional beats get a slow push-in, the training act uses hard cuts, and acts are separated by fades to black. Text sits in the upper third, and the DAY counter is top-left.

---

## 1. Global look

### 1.1 Background and vignette (observed: frames 1, 9, 11, 13, 20)
- Frame center is about `#0f0f0f`–`#121212`, edges/corners about `#050505`–`#080808`.
- The vignette is a **wide ellipse** (rx ≈ 0.62·W, ry ≈ 0.75·H). Frame 1 shows faint concentric banding, which means a radial gradient was used. Add grain so we don't reproduce the banding.
- A dimmer variant appears in "dark acts" (frames 7, 8, 17): center about `#0c0c0c`.

```tsx
// <Backdrop/>: always the first layer
<defs>
  <radialGradient id="bgVignette" cx="50%" cy="48%" r="65%" gradientUnits="objectBoundingBox">
    <stop offset="0%"   stopColor="#131313"/>
    <stop offset="55%"  stopColor="#0e0e0e"/>
    <stop offset="85%"  stopColor="#090909"/>
    <stop offset="100%" stopColor="#050505"/>
  </radialGradient>
</defs>
<rect width={1920} height={1080} fill="url(#bgVignette)"/>
```
Make the stops theme tokens (`bg.center`, `bg.mid`, `bg.edge`) so the summit/dawn scenes can swap them.

### 1.2 Letterbox bar
- Frames 1, 2, 5, 9, 10, 14, 16 show a **pure black `#000` bar at the top**, roughly 4–9% of height. The amount varies, probably because the screenshots were cropped differently. The bottom bar is thinner or absent.
- Recommendation: an optional `<Letterbox top={64} bottom={0}/>`, `#000000`, drawn **above** everything except text. Let it slide in (0→64px over 20f) at the start of the "Rock bottom" beat for a cinematic squeeze. Default is a constant 64px top bar so the frame reads as "a film".

### 1.3 Floor line
| Frame | floor y / H |
|---|---|
| 2 bedroom | 0.86 |
| 4 bedroom (pushed-in) | 0.85 |
| 5 couch | 0.81 |
| 9 spotlight | 0.79 |
| 10 city | 0.79 (curb) + road dashes at 0.86 |
| 11 push-up | 0.72 (pushed-in) |
| 19 bedroom dawn | 0.85 |

- Token: `FLOOR_Y = 900` (0.833·H) default; `FLOOR_Y_WIDE = 920`; `FLOOR_Y_STAGE = 860`.
- Color `#4a4a4a`–`#5c5c5c`, width **2–2.5px**, full-bleed (x from −20 to 1940). It must not look ruled: it gets a ±1.5px wobble over long wavelength (see 1.4).
- Nothing below the floor; it's the same background color. (In the bedroom, the floor area is very slightly darker, `#0a0a0a`.)

### 1.4 Hand-drawn outline style
Observed: strokes are light gray (`#6b6b6b`–`#8a8a8a`), about 2.5–3px at 1080p, `stroke-linecap/linejoin="round"`, corners heavily rounded (r ≈ 12–24px on furniture). Lines bend slightly (blanket top, stairs, couch back) and are never mechanical. In frame 2 the bed rail extends a little past the leg, an "overshoot" as if drawn freehand.

**Simulation recipe (deterministic):**
1. Build every prop from a **polyline of control points** and render it as a Catmull-Rom/quadratic-smoothed path, not `<rect>`.
2. Jitter each control point with a **seeded value noise**: amplitude 1–2.5px, keyed by `(seed, pointIndex)`.
3. Optional **line boil**: change the noise seed every `BOIL_STEP = 4` frames (≈7.5 fps "on fours") with amplitude ≤0.8px. The reference looks mostly *static* and clean, so default to `boil = false` and turn it on only in tense scenes (mirror crack, giant shadow) for subtle unease.
4. Slight **overshoot**: extend line ends by 3–6px past corners on straight structural lines (bed rails, desk legs, lamp posts).

```ts
// lib/wobble.ts: zero dependencies, deterministic
export const hash = (n: number) => {
  const s = Math.sin(n * 127.1 + 311.7) * 43758.5453;
  return s - Math.floor(s);               // 0..1
};
export const noise1 = (seed: number, i: number) => hash(seed * 1000 + i) * 2 - 1; // -1..1

type P = [number, number];
/** jitter points then smooth with Catmull-Rom -> cubic Bézier */
export function wobblyPath(pts: P[], {seed = 1, amp = 1.6, closed = false, frame = 0, boil = false, boilStep = 4} = {}) {
  const s = seed + (boil ? Math.floor(frame / boilStep) * 17 : 0);
  const j = pts.map(([x, y], i) => [x + noise1(s, i * 2) * amp, y + noise1(s, i * 2 + 1) * amp] as P);
  const n = j.length, at = (k: number) => j[closed ? (k + n) % n : Math.max(0, Math.min(n - 1, k))];
  let d = `M${j[0][0].toFixed(1)},${j[0][1].toFixed(1)}`;
  const last = closed ? n : n - 1;
  for (let i = 0; i < last; i++) {
    const p0 = at(i - 1), p1 = at(i), p2 = at(i + 1), p3 = at(i + 2);
    const c1: P = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
    const c2: P = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
    d += ` C${c1[0].toFixed(1)},${c1[1].toFixed(1)} ${c2[0].toFixed(1)},${c2[1].toFixed(1)} ${p2[0].toFixed(1)},${p2[1].toFixed(1)}`;
  }
  return closed ? d + 'Z' : d;
}

/** Rounded rectangle as wobbly closed path (corner radius r, k points per side) */
export function wobblyRoundRect(x: number, y: number, w: number, h: number, r: number, opt = {}) {
  const pts: P[] = [];
  const arc = (cx: number, cy: number, a0: number) => {
    for (let t = 0; t <= 2; t++) { const a = a0 + (t / 2) * (Math.PI / 2); pts.push([cx + Math.cos(a) * r, cy + Math.sin(a) * r]); }
  };
  arc(x + w - r, y + r, -Math.PI / 2);      // top-right
  pts.push([x + w, y + h / 2]);
  arc(x + w - r, y + h - r, 0);             // bottom-right
  pts.push([x + w / 2, y + h]);
  arc(x + r, y + h - r, Math.PI / 2);       // bottom-left
  pts.push([x, y + h / 2]);
  arc(x + r, y + r, Math.PI);               // top-left
  pts.push([x + w / 2, y]);
  return wobblyPath(pts, {...opt, closed: true});
}

/** long line with low-frequency wobble (floor, horizon) */
export function wobblyLine(x0: number, y0: number, x1: number, y1: number, segs = 12, opt = {}) {
  const pts: P[] = Array.from({length: segs + 1}, (_, i) => [x0 + (x1 - x0) * i / segs, y0 + (y1 - y0) * i / segs]);
  return wobblyPath(pts, opt);
}
```
Standard stroke props: `stroke="#7a7a7a" strokeWidth={2.75} strokeLinecap="round" strokeLinejoin="round"`.
**Memoize paths with `useMemo`** keyed on seed (and boil tick). Rebuilding paths every frame is fine at this scale, but there's no need.

Optional "pencil" texture (expensive, use sparingly): `filter` with `feTurbulence baseFrequency=0.9` + `feDisplacementMap scale=1.5`. **Don't** use it globally; the wobble functions give 95% of the effect at near-zero cost.

### 1.5 Film grain and dust specks
- Frame 20 shows sparse warm **specks** (`#b06a3a`/`#8a5a3a`, 2–4px, opacity 0.3–0.7) drifting slowly. Frames 9 and 15 have floating particles too. A very light luminance grain is plausible (it hides gradient banding).
- **Grain (cheap):** ship 4 pre-rendered 512x512 noise PNGs (`public/grain/0..3.png`, monochrome, alpha ≈ 6%). Tile them over the frame with `mix-blend-mode: overlay` (HTML layer above the SVG) and cycle `frame % 4`, offset by a hashed (x, y) each frame. Avoid per-frame `feTurbulence` on the full 1920x1080 frame, which is slow.
- **Dust/specks:** a `<DustField count={40} seed={7} color="#9a9a9a" drift={[0.15, -0.25]}/>` where each particle's position is `(x0 + vx·frame) mod W`, opacity `0.25 + 0.35·(0.5+0.5·sin(frame·0.05 + i))`. That's a pure function of the frame, so it's deterministic.

```tsx
export const DustField: React.FC<{count: number; seed: number; color: string; area: [number, number, number, number]; vx?: number; vy?: number; r?: [number, number]}> =
({count, seed, color, area: [ax, ay, aw, ah], vx = 0.1, vy = -0.2, r = [1.5, 3.5]}) => {
  const f = useCurrentFrame();
  return <g>{Array.from({length: count}, (_, i) => {
    const x = ax + ((hash(seed + i) * aw + vx * f * (0.5 + hash(seed + i + 99))) % aw + aw) % aw;
    const y = ay + ((hash(seed + i + 7) * ah + vy * f * (0.5 + hash(seed + i + 31))) % ah + ah) % ah;
    const o = 0.25 + 0.35 * (0.5 + 0.5 * Math.sin(f * 0.05 + i * 1.7));
    return <circle key={i} cx={x} cy={y} r={r[0] + hash(seed + i + 3) * (r[1] - r[0])} fill={color} opacity={o}/>;
  })}</g>;
};
```

### 1.6 Layer order (every scene)
`Backdrop → far set (window/city/hills) → light volumes (beams, cones, screen blend) → floor line → props → character(s)/shadow → foreground glows (phone, rim) → particles → text → letterbox → grain → fade overlay`

---

## 2. Set catalog (SVG construction specs)

General prop fill/stroke tokens: `prop.fill.dark #262628`, `prop.fill.mid #333338`, `prop.stroke #737373`, `prop.stroke.light #8a8a8e`. Stroke width 2.75 unless noted.

### 2.1 Bedroom (frames 2, 3, 4, 19)
Wide shot. Floor y = 930. Nightstand left (x≈360), bed center-left, window upper-right. The upper-center third stays empty for red info text.

| Element | Geometry (1920x1080) | Fill | Stroke |
|---|---|---|---|
| Nightstand | rect x 368, y 775, w 180, h 155, r 22 | `#2a2522` (warm dark brown-gray) | `#6e6e6e` |
| Nightstand drawer line | line x 385→530 at y 852 | – | `#6e6e6e` 2px |
| Knob | circle (458, 812) r 5 | `#8a8a8a` | – |
| Alarm clock body | rect x 392, y 712, w 132, h 60, r 22 | `#2b2b2d` | `#7a7a7a` |
| Digits | 7-seg, 4 digits, height 40, center (458, 742) | `#e8432f` ON / `#3a1a16` OFF (optional ghost) | – |
| Headboard | rect x 565, y 645, w 40, h 285, r 20 | `#2c2c30` | `#6b6b6b` |
| Mattress | rect x 585, y 725, w 870, h 50, r 25 | `#2a2a2e` | `#6b6b6b` |
| Bed frame rail | rect x 570, y 775, w 905, h 22, r 11 | `#232326` | `#6b6b6b` |
| Legs | lines (600,797)→(600,935), (1445,797)→(1445,935) | – | `#6b6b6b` 4px |
| Pillow | ellipse cx 680, cy 712, rx 85, ry 22 | `#4a4a50` | none |
| Blanket | closed wobbly path (below) | `#2b3247` (navy) | `#6d7593` 3px |
| Blanket fold | open path (965,680)→(1040,712)→(1110,700) | – | `#6d7593` 2px |
| Window | rect x 1530, y 135, w 285, h 265, r 22; cross mullions | glass gradient | `#7a7a80` 3.5px |
| Moon | circle (1715, 210) r 32 | `#d6d6dc` | – |

Blanket shape (top edge with soft bumps, rounded right end tucked over mattress):
```tsx
const blanketPts: P[] = [[760,770],[770,640],[880,610],[1000,618],[1120,605],[1240,612],[1360,630],[1430,660],[1440,712],[1420,770]];
<path d={wobblyPath(blanketPts, {seed: 21, amp: 2, closed: true})} fill="#2b3247" stroke="#6d7593" strokeWidth={3}/>
```
The character's head (cream circle) sits on the pillow at about (700, 670), r ≈ 55. When he sits up (frame 19), the blanket is gone and a second pillow `#2e3448` lies at the foot end.

**Window glass:**
```tsx
<linearGradient id="nightGlass" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stopColor="#1d2130"/><stop offset="1" stopColor="#10121a"/>
</linearGradient>
<linearGradient id="dawnGlass" x1="0" y1="0" x2="0" y2="1">      {/* frame 19 */}
  <stop offset="0" stopColor="#3a3f6e"/><stop offset="0.55" stopColor="#7a5a72"/><stop offset="1" stopColor="#c27a5c"/>
</linearGradient>
```
Interpolate night→dawn by stacking both rects and animating the dawn rect's opacity.

**Moon glow + moonlight beam** (frame 2: a faint diagonal shaft going down-left from the window to the floor around x 900–1300):
```tsx
<radialGradient id="moonGlow"><stop offset="0" stopColor="#e6e8f0" stopOpacity="0.55"/><stop offset="1" stopColor="#e6e8f0" stopOpacity="0"/></radialGradient>
<circle cx={1715} cy={210} r={80} fill="url(#moonGlow)"/>

<linearGradient id="beam" x1="1" y1="0" x2="0" y2="1">
  <stop offset="0" stopColor="#c8d0e6" stopOpacity="0.10"/>
  <stop offset="1" stopColor="#c8d0e6" stopOpacity="0"/>
</linearGradient>
{/* quad from window bottom-left/right edges down to floor, skewed left */}
<path d="M1530,400 L1815,400 L1380,930 L980,930 Z" fill="url(#beam)" style={{mixBlendMode:'screen'}}/>
```
For dawn, the beam color changes to `#e8a07a` at opacity 0.12. A warm floor pool `ellipse cx 1180 cy 930 rx 260 ry 30` (`#d08a60`, 0.08) is optional.

**7-segment digits in SVG.** Each digit is 7 rounded-cap line segments in a 24x40 cell, plus a colon of two small squares. The frames show slightly slanted, thin segments with rounded ends (they read as a font, "DSEG7"-like).
```tsx
const SEG: Record<string, [number,number,number,number]> = { // x1,y1,x2,y2 in a 24x40 cell
  a:[4,2,20,2], b:[22,4,22,18], c:[22,22,22,36], d:[4,38,20,38], e:[2,22,2,36], f:[2,4,2,18], g:[4,20,20,20],
};
const MAP: Record<string,string> = {'0':'abcdef','1':'bc','2':'abged','3':'abgcd','4':'fgbc','5':'afgcd','6':'afgedc','7':'abc','8':'abcdefg','9':'abcdfg'};
export const SevenSeg: React.FC<{text: string; x: number; y: number; h?: number; color?: string; ghost?: string; glow?: boolean}> =
({text, x, y, h = 40, color = '#e8432f', ghost = '#2a1512', glow = true}) => {
  const s = h / 40; let cx = 0;
  return <g transform={`translate(${x},${y}) scale(${s}) skewX(-6)`} filter={glow ? 'url(#digitGlow)' : undefined}>
    {text.split('').map((ch, i) => {
      if (ch === ':') { const g = <g key={i} transform={`translate(${cx},0)`}><rect x={2} y={11} width={4} height={4} rx={1} fill={color}/><rect x={2} y={25} width={4} height={4} rx={1} fill={color}/></g>; cx += 10; return g; }
      const on = MAP[ch] ?? '';
      const g = <g key={i} transform={`translate(${cx},0)`}>{Object.entries(SEG).map(([k,[x1,y1,x2,y2]]) =>
        <line key={k} x1={x1} y1={y1} x2={x2} y2={y2} stroke={on.includes(k) ? color : ghost} strokeWidth={3.6} strokeLinecap="round"/>)}</g>;
      cx += 30; return g;
    })}
  </g>;
};
// digitGlow: cheap, small area only, so the blur is OK here
<filter id="digitGlow" x="-20%" y="-50%" width="140%" height="200%">
  <feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
```
Alarm "ringing": blink digits at `Math.floor(frame/8)%2` and shake the clock body ±3px rotation ±2°. The fast-forward 5:00→8:47 is `minutes = interpolate(frame,[a,b],[300,527],{extrapolateRight:'clamp'})` with `Easing.in(Easing.quad)`, formatted as `H:MM`, with a 1-frame white flash on the end value.

### 2.2 Couch (frames 5, 6)
Centered, floor y = 905. The character sits left-of-center; the shadow enters from the right side behind the couch.

| Element | Geometry | Fill | Stroke |
|---|---|---|---|
| Back cushion | rect x 690, y 595, w 820, h 215, r 26 | `#2e2a33` | `#8a8690` |
| Seat | rect x 690, y 770, w 820, h 75, r 18 | `#332f38` | `#8a8690` |
| Seat split line | (700,790)→(1500,790) | – | `#8a8690` 2px |
| Arm L | rect x 625, y 685, w 105, h 205, r 40 | `#2a2630` | `#8a8690` |
| Arm R | rect x 1470, y 685, w 105, h 205, r 40 | `#2a2630` | `#8a8690` |
| Base | rect x 618, y 860, w 965, h 38, r 19 | `#2b2730` | `#8a8690` |
| Legs | 4 short lines, h 18, at x 660, 1540 | – | `#8a8690` 4px |

Lighting: phone glow (see 3.2) on the face, plus a faint blue spill ellipse on the couch back behind the head (`#4a78d0`, 0.12). The couch is purple-gray (cooler than the warm nightstand), which supports Act 1's cold tone.

### 2.3 Desk + chair + lamp + books + wall clock (frame 7)
Composition: shadow at the left third, character center, desk extends right, wall clock top-center-right. Floor y = 1025 (lower in this framing).

| Element | Geometry | Fill | Stroke |
|---|---|---|---|
| Desktop | rect x 1180, y 830, w 1080 (bleeds right), h 26, r 13 | `#2a2620` | `#7a7266` |
| Desk legs | (1225,856)→(1225,1025), (2010,856)→(2010,1025) | – | `#7a7266` 4px |
| Chair back | line (785,615)→(785,1025) + seat rect x 775, y 860, w 260, h 14, r 7 | `#222` | `#6e6e6e` |
| Chair legs | 3 vertical lines to floor | – | `#6e6e6e` 3.5px |
| Book stack | 3 pill rects, each w 260, h 40, r 20, stacked from y 740 | `#6a6a3a` olive, `#3d507e` blue, `#8a3436` red | `#9a9a9a` 2.5px |
| Lamp base | small ellipse on top book | `#5e5e62` | `#8a8a8e` |
| Lamp arm | path (1890,745)→(1870,690)→(1815,620) | – | `#9a9a9e` 4px |
| Lamp shade | rounded trapezoid, ~110x70, rotated −35°, centered (1775,575) | `#6a6a70` with linear gradient to `#4a4a50` | none |
| Papers | 2 flat pills on desk, w 170, h 14 | `#cfcbbd` | `#8a8a8a` |
| Wall clock | circle (1450, 240) r 105, inner face r 95 | `#1c1c1e` | `#6e6e6e` 5px |
| Clock hands | hour (L 45, w 6), minute (L 78, w 5), round caps | `#e6e6e6` | – |

**Moving clock hands** (time passing inside a shot):
```tsx
const f = useCurrentFrame();
const minuteDeg = (startMin + f * minutesPerFrame) * 6;        // 360/60
const hourDeg   = (startHour * 60 + startMin + f * minutesPerFrame) * 0.5; // 360/720
<g transform="translate(1450,240)">
  <line x1={0} y1={0} x2={0} y2={-45} stroke="#e6e6e6" strokeWidth={6} strokeLinecap="round" transform={`rotate(${hourDeg})`}/>
  <line x1={0} y1={0} x2={0} y2={-78} stroke="#e6e6e6" strokeWidth={5} strokeLinecap="round" transform={`rotate(${minuteDeg})`}/>
</g>
```
For a "time-lapse" feel, use `minutesPerFrame = 2` and add a faint motion-trail copy of the minute hand at opacity 0.25, 8° behind.

**Lamp cone (warm):** see 3.3. In the frame the cone points down-left from the shade toward the papers and character's head; the light falls off well before the shadow figure. *Darkness is where the shadow lives.*

### 2.4 Mirror on stand (frame 8) + reflection trick + crack
Composition: character at the left third (x≈640), mirror right of center (x≈1290). Floor y = 1000.

| Element | Geometry | Fill | Stroke |
|---|---|---|---|
| Mirror frame | ellipse cx 1300, cy 590, rx 270, ry 360 | – | `#8a8a8e` 9px + inner `#5a5a5e` 2px at rx−8 |
| Glass | ellipse rx 262, ry 352 | radial `#1a1a1c`→`#0c0c0e` | – |
| Glass sheen | path arc inside upper-left, opacity 0.06 white | `#ffffff` | – |
| Stand top | rect x 1040, y 880, w 520, h 58, r 29 | `#3c3c40` | `#8a8a8e` |
| Stand bottom | rect x 1090, y 935, w 420, h 68, r 28 | `#46464a` | `#8a8a8e` |

**Reflection via clipPath:** render the reflected figure inside the glass clip. The reflection doesn't mirror the hero; it's the **shadow silhouette** (black + red glow) standing slightly deeper (scale 0.95, y offset +10).
```tsx
<defs><clipPath id="mirrorClip"><ellipse cx={1300} cy={590} rx={262} ry={352}/></clipPath></defs>
<ellipse cx={1300} cy={590} rx={262} ry={352} fill="url(#mirrorGlass)"/>
<g clipPath="url(#mirrorClip)">
  {/* reflection: hero mirrored around mirror center OR antagonist */}
  <g transform={`translate(${2*1300},0) scale(-1,1)`} opacity={heroReflOpacity}><Hero {...pose}/></g>
  <g opacity={shadowReflOpacity}><ShadowFigure x={1300} y={980} scale={0.95}/></g>
  {/* inner darkening at glass rim */}
  <ellipse cx={1300} cy={590} rx={262} ry={352} fill="url(#glassRimShade)"/>
</g>
<ellipse cx={1300} cy={590} rx={270} ry={360} fill="none" stroke="#8a8a8e" strokeWidth={9}/>
```
Transition: cross-fade `heroRefl` → `shadowRefl` over 18 frames with a 2-frame red flash on the glass (`#e8432f` at 0.15). The DAY-190 "redemption" variant mirrors the hero with a headband.

**Crack effect:** pre-author 6–9 jagged polylines radiating from an impact point (e.g. (1360, 470)), drawn with `stroke="#cfd2d8"` 2px, opacity 0.85, plus 2 thin concentric broken arcs. Animate them with `strokeDasharray = length; strokeDashoffset = length·(1−p)`, where `p = spring({frame: f - crackStart, fps, config: {damping: 200}})`. Generate the polylines deterministically:
```ts
function crackLines(cx: number, cy: number, n = 8, seed = 3): string[] {
  return Array.from({length: n}, (_, i) => {
    let a = (i / n) * Math.PI * 2 + noise1(seed, i) * 0.3, x = cx, y = cy, d = `M${cx},${cy}`;
    const segs = 4 + Math.floor(hash(seed + i) * 3);
    for (let s = 0; s < segs; s++) { const L = 30 + hash(seed * 7 + i * 13 + s) * 55; a += noise1(seed + 5, i * 10 + s) * 0.45;
      x += Math.cos(a) * L; y += Math.sin(a) * L; d += ` L${x.toFixed(1)},${y.toFixed(1)}`; }
    return d;
  });
}
```
Keep the cracks inside `mirrorClip`. On impact frame: camera shake (5.3) + 1-frame white glass flash at 0.25.

### 2.5 Spotlight rock bottom (frame 9)
Pure monochrome, no props, floor y = 850. The character is curled at center (x≈960).
```tsx
<defs>
  <linearGradient id="spotCone" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stopColor="#ffffff" stopOpacity="0.04"/>
    <stop offset="0.7" stopColor="#ffffff" stopOpacity="0.10"/>
    <stop offset="1"   stopColor="#ffffff" stopOpacity="0.14"/>
  </linearGradient>
  {/* soften the cone edges horizontally */}
  <linearGradient id="spotEdge" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stopColor="#fff" stopOpacity="0"/><stop offset="0.25" stopColor="#fff" stopOpacity="1"/>
    <stop offset="0.75" stopColor="#fff" stopOpacity="1"/><stop offset="1" stopColor="#fff" stopOpacity="0"/>
  </linearGradient>
  <mask id="spotMask"><rect x={560} y={0} width={800} height={1080} fill="url(#spotEdge)"/></mask>
  <radialGradient id="spotPool" cx="50%" cy="50%" r="50%">
    <stop offset="0" stopColor="#ffffff" stopOpacity="0.22"/><stop offset="1" stopColor="#ffffff" stopOpacity="0"/>
  </radialGradient>
</defs>
<path d="M880,0 L1040,0 L1290,850 L630,850 Z" fill="url(#spotCone)" mask="url(#spotMask)"/>
<ellipse cx={960} cy={852} rx={330} ry={48} fill="url(#spotPool)"/>
<DustField count={28} seed={9} color="#8a8a8a" area={[700, 120, 520, 700]} vx={0.05} vy={0.18} r={[1.5, 3]}/>
```
- The cone top is narrow (~160px), the bottom about 660px. The floor line stays visible across the frame, brighter inside the pool (overlay a second short floor-line segment `#8a8a8a` from x 680→1240).
- Dust motes: gray `#8a8a8a`–`#a0a0a0`, falling slowly, only inside the cone (mask them with the same cone path).
- Entry: the scene is black, the cone "switches on" over 6 frames (opacity 0→1 with a 1-frame overshoot to 1.15, like a stage light catching), and a low "thunk" SFX lands in sync.
- Character underside gets a dark contact shadow: ellipse `#000` 0.45, rx 120, ry 10.

### 2.6 Night city run (frame 10)
Horizon/curb y = 840, road dashes y = 912. The character runs in place around x = 820 (left of center, facing right, with run-space ahead). The world scrolls right-to-left.

**Parallax layers (speed ratios relative to the ground, `groundSpeed = 14 px/frame` at 30fps):**
| Layer | Content | Speed ratio | Notes |
|---|---|---|---|
| L0 sky | vignette bg + 3–4 long thin speed lines | 0 (static) / lines 2.2 | lines `#5a5a5a` 1.5px, len 150–300, random y in 120–520 |
| L1 far buildings | very dim rounded rects, `#141416`, stroke `#262628` | 0.15 | optional, adds depth |
| L2 mid buildings | rounded rects w 130–210, h 250–420, r 16, `#19191c`, stroke `#38383c` 2px; windows | 0.35 | windows 14x16, `#6b5a3e` @0.65, sparse (~30% lit) |
| L3 streetlamps + glows | post + arm + bulb, every 640px | 1.0 | warm pools on ground |
| L4 road | dashes 115x3 `#5a5a5a`, gap 115 | 1.0 | |
| L5 foreground speed lines | 2–3 lines crossing the character | 2.5 | `#7a7a7a` 1px, opacity 0.5 |

Tiling: `x = ((baseX - f * speed * ratio) % tileW + tileW) % tileW - margin`. Render 2 copies per tile.

Building (with hand-drawn windows):
```tsx
const Building = ({x, w, h, seed}) => {
  const y = 840 - h;
  const cols = Math.floor((w - 30) / 38), rows = Math.floor((h - 40) / 52);
  return <g>
    <path d={wobblyRoundRect(x, y, w, h + 10, 16, {seed, amp: 1})} fill="#19191c" stroke="#38383c" strokeWidth={2}/>
    {Array.from({length: cols * rows}, (_, k) => hash(seed * 31 + k) < 0.3 &&
      <rect key={k} x={x + 22 + (k % cols) * 38} y={y + 30 + Math.floor(k / cols) * 52} width={14} height={16} rx={2} fill="#6b5a3e" opacity={0.65}/>)}
  </g>;
};
```
Streetlamp: post `(x,840)→(x,425)`, arm `(x,425)→(x+55,425)`, stroke `#7a7a7a` 4px; bulb circle r 9 `#fff0c8`. Glows: see 3.4. The ground pool is centered under the bulb at the curb, an ellipse rx 210, ry 95, extending *below* the curb line (it also lights the road).

Character extras: speed lines behind him (3 horizontal strokes trailing from his back, length 80–140, opacity flicker), and a sweat drop. The camera gets a run-bob (see 5.3).

### 2.7 Push-up / boxing void stage (frames 11–13)
- **Only the floor line**, y = 780 (pushed-in, 0.72·H) and full bleed. Nothing else.
- The vignette darkens slightly (`bg.edge #040404`) to make the stage feel isolating.
- Counter number ("3"): centered at x 960, y 300, font size ~140, `#f0ece0`, with a soft glow (3.6 "text glow"). Pop-in: scale 1.4→1.0 with `spring({damping: 12})` and opacity 0→1 over 4f. The previous number fades/drops by 20px.
- Strain beat ("told you." in red at the upper-right third): add red vignette tint `#3a0d0a` at 0.0→0.25 on the edges (3.5).

### 2.8 Punching bag (frames 14, 15)
Bag right of center (x 1430–1700), top y 210, hanging from a rope that goes off the top of the frame.
```tsx
// body: soft rounded capsule, slightly irregular
<path d={wobblyRoundRect(1440, 215, 255, 610, 40, {seed: 64, amp: 2.5})} fill="#d42e1e"/>
// hatch strokes: hand-drawn short horizontal dashes, darker red
{Array.from({length: 26}, (_, i) => {
  const y = 250 + i * 22 + noise1(64, i) * 6, x = 1465 + hash(64 + i) * 120, L = 30 + hash(80 + i) * 55;
  return <line key={i} x1={x} y1={y} x2={x + L} y2={y + noise1(70, i) * 3} stroke="#7e1a10" strokeWidth={2.5} strokeLinecap="round" opacity={0.85}/>;
})}
// right-side highlight
<path d="M1665,250 Q1675,520 1662,800" stroke="#ff6a52" strokeWidth={3} fill="none" strokeLinecap="round" opacity={0.8}/>
// rope + ring
<line x1={1568} y1={-20} x2={1568} y2={185} stroke="#9a9a9a" strokeWidth={3}/>
<path d="M1548,215 Q1568,175 1588,215" stroke="#9a9a9a" strokeWidth={3} fill="none"/>
```
- The bag swings as a pendulum. Pivot at the rope top (1568, −20): `rotate(θ, 1568, -20)`, with `θ = A·e^(−t/τ)·sin(ωt)` after each hit, A = 6°, τ = 25f, ω = 0.35 rad/f.
- On impact (frame 15): the bag glows red (3.5 red glow, opacity 0→0.9→0.4), 2–3 frames of camera shake, shattered letters (agent-text domain) fly outward as dim red `#6a2622` at 0.6 with slow rotation, and red embers (`DustField` color `#c0392b`, r 2–4) appear around the frame.

### 2.9 Stairs (frames 16, 17)
A diagonal staircase from bottom-left (x≈330, y 1080) up to top-right (x 1920, y≈140). Above the edge is background; below is a gray fill `#1c1c1e` → `#232326` (gradient toward the bottom-right). The edge stroke is `#8a8a8a` 2.75px. The steps are **rounded "wavy" steps** (each step is a smooth S-curve, not a sharp corner).
```ts
function stairEdge(x0 = 330, y0 = 1090, x1 = 1960, y1 = 140, steps = 19, seed = 270) {
  const dx = (x1 - x0) / steps, dy = (y1 - y0) / steps;      // dy < 0
  let d = `M${x0},${y0}`;
  for (let i = 0; i < steps; i++) {
    const sx = x0 + i * dx + noise1(seed, i) * 3, sy = y0 + i * dy + noise1(seed, i + 50) * 3;
    // riser (up) with rounded nose, then tread (right)
    d += ` C${sx + dx*0.15},${sy} ${sx + dx*0.12},${sy + dy} ${sx + dx*0.35},${sy + dy}`;
    d += ` L${sx + dx},${sy + dy}`;
  }
  return d;
}
const edge = stairEdge();
<path d={`${edge} L1960,1100 L330,1100 Z`} fill="url(#stairFill)"/>
<path d={edge} fill="none" stroke="#8a8a8a" strokeWidth={2.75} strokeLinecap="round"/>
<linearGradient id="stairFill" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#1a1a1c"/><stop offset="1" stopColor="#252528"/></linearGradient>
```
- Climbing: the hero stays in place around x 620–760 while the **whole stairs group translates** (−dx, −dy) per step cycle, so the stairs scroll diagonally down-left. That gives an "endless stairs" feel; tile by wrapping every N steps.
- Giant-shadow variant (frame 17): the shadow stands on the stairs at upper right, about 3.3x hero height. Add a red tint to the vignette and a red glow under its feet that spills onto the stair edge (`#e8432f` at 0.25 in a radial pool).

### 2.10 Sunrise summit (frame 18)
The only warm full-frame scene. Sun just below the horizon at the right (≈ x 1500, y 830).
```tsx
<linearGradient id="dawnSky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0"    stopColor="#1e120e"/>
  <stop offset="0.35" stopColor="#3e2118"/>
  <stop offset="0.65" stopColor="#6a3520"/>
  <stop offset="0.85" stopColor="#9a5028"/>
  <stop offset="1"    stopColor="#b25e2c"/>
</linearGradient>
<radialGradient id="sunBloom" cx="0.78" cy="0.78" r="0.35">
  <stop offset="0" stopColor="#f0a060" stopOpacity="0.55"/><stop offset="1" stopColor="#f0a060" stopOpacity="0"/>
</radialGradient>
<rect width={1920} height={1080} fill="url(#dawnSky)"/>
<rect width={1920} height={1080} fill="url(#sunBloom)" style={{mixBlendMode:'screen'}}/>
```
Hills (back→front), all with smooth, low-frequency curves:
| Layer | Fill | Top edge y range | Parallax (if panning) |
|---|---|---|---|
| H1 far ridge | `#5a2e1e` @0.85 | 560–640 | 0.1 |
| H2 mid | `#3e1f16` | 620–720 | 0.25 |
| H3 near rolling | `#2a1510` | 700–820 | 0.5 |
| H4 summit (hero stands on it) | `#150b08` | peak at (770, 600), falls off to (0, 1000) and (1180, 1080) | 1.0 |

The summit's top edge has a **rim-light stroke** `#c97a48` 2.5px, brightest near the peak (use a stroke gradient: `#e08a50` at the peak → `#5a2e1e` at the ends). There's a short gray ground mark under the feet (`#6a6a6a` 2px, 160 long), reusing the floor-line language.

**Rim light on the character:** a duplicate of the hero silhouette, filled `#ffb070`, offset +3px toward the sun, behind the hero at opacity 0.7. Plus an outer glow made with pre-blurred radial gradient ellipses behind the body (`#ffa860` at 0.35). Don't blur the character itself.
Wind: horizontal streaks `#d8a080` 1.5px opacity 0.4 drifting left (frame 18 shows one). The headband tail flutters (character agent).

### 2.11 Calendar with red X (DAY 150, from the script)
Centered card x 560, y 190, w 800, h 700, r 24, fill `#1c1c1e`, stroke `#8a8a8e` 3px. Header strip 90px `#2a2a2e` with month text (gray). Grid 7x5 cells (≈ 104x104), day numbers `#6a6a6a` size 26 at the top-left of each cell. Ring binders: 2–3 small rounded rects on top `#8a8a8e`.
Red X per cell (hand-drawn, two strokes, slight overshoot), animated sequentially every 2–3 frames:
```tsx
const X = ({cx, cy, s = 34, p, seed}) => {          // p 0..1 draw progress
  const a = `M${cx - s + noise1(seed,1)*4},${cy - s} L${cx + s},${cy + s + noise1(seed,2)*4}`;
  const b = `M${cx + s},${cy - s + noise1(seed,3)*4} L${cx - s + noise1(seed,4)*4},${cy + s}`;
  const L = s * 2.9;
  return <g stroke="#e8432f" strokeWidth={7} strokeLinecap="round" fill="none">
    <path d={a} strokeDasharray={L} strokeDashoffset={L * (1 - Math.min(1, p * 2))}/>
    <path d={b} strokeDasharray={L} strokeDashoffset={L * (1 - Math.max(0, p * 2 - 1))}/>
  </g>;
};
```
Accelerate the X cadence (6f → 1f between marks) and add a slow push-in 1.0→1.06.

### 2.12 End card (frame 20)
- Background `#0a0a0a` with the standard vignette, no floor line.
- Title `#f0ece0`, about 190px font, centered at y ≈ 480, with a soft white glow (blurred duplicate, `#ffffff` at 0.18, or a text-shadow on an HTML layer).
- Red wavy underline `#e84a35`, 7px, round caps, sine wave amplitude 4px, wavelength ~110px, drawn left→right with a dash offset over 20 frames.
- Tagline `#e8e4d8` about 52px, y ≈ 700, fades in 12f after the underline completes.
- Embers: `DustField count=22 color="#b8693a" r=[1.5,3]` rising slowly (vy −0.25). Each ember fades in and out.

```ts
const wavy = (x0: number, x1: number, y: number, amp = 4, wl = 110) =>
  'M' + Array.from({length: Math.ceil((x1 - x0) / 6) + 1}, (_, i) => { const x = x0 + i * 6; return `${x},${(y + Math.sin((x - x0) / wl * Math.PI * 2) * amp).toFixed(1)}`; }).join(' L');
```

### 2.13 New-topic sets (same minimal language)
Rules for new topics: one hero prop cluster, maximum 3–5 props, gray strokes on dark fills, **one accent light**, floor line always present (except abstract/void scenes), and the upper third left empty for text.

**Loneliness: table for two** (`SetTableForTwo`)
- Round café table: top = ellipse cx 960, cy 745, rx 230, ry 34, fill `#2a2622`, stroke `#7a7266`; pedestal line (960,780)→(960,900) + foot ellipse rx 70, ry 10.
- Two chairs: left chair (hero sits, x≈690) and right chair **empty** (x≈1230), same construction as the desk chair. The empty chair gets a faint cool spotlight (`#b8c4dc` cone at 0.06).
- Two cups: hero's cup steams (3 wavy lines rising, `#8a8a8a` opacity 0.4, drift via sin(frame)); the other cup has no steam. Cups: rect w 40, h 46, r 8, fill `#d8d4c8`, handle arc.
- Pendant lamp from the top: line (960,−10)→(960,300), shade half-ellipse, warm cone `#ffcf8a` onto the table only. Everything else stays black.

**Loneliness: rainy window** (`SetRainWindow`)
- Large window (x 1150–1700, y 170–720, r 24) with cross mullions. Glass gradient `#151a26`→`#0d1018`. Blurred city lights behind: 10 circles r 18–40, warm `#c89a5a` and cool `#5a7ab0` at 0.12–0.25 (pre-blurred radial gradients, *not* feGaussianBlur).
- Rain: 70 streaks inside the window clip, line length 26–48, `#9aa6bc` opacity 0.35, slant 8°, `y = (y0 + f*vy) % H`. Plus 6 slow droplet trails (vertical paths with dash animation).
- Cold window light spills down-left onto the floor (beam like 2.1, color `#8aa0c8`, 0.07). The hero sits on the sill/floor in silhouette-light.

**Loneliness: crowd that ignores** (`SetCrowd`)
- 10–14 **gray hero-shaped silhouettes** (`#3a3a3e` fill, no face, stroke `#4a4a4e`) walking across the frame at different speeds and scales (0.85–1.1) on the same floor line. Parallax: back row at scale 0.85 and speed ×0.7, darker `#2a2a2e`.
- The hero is the only lit figure (cream). His local light is a soft radial `#ffffff` at 0.06. The crowd passes *in front of* and behind him and never turns. Speech bubbles above the crowd stay empty (stroke-only ellipses).

**Love: park bench** (`SetParkBench`)
- Bench: 3 slats (rounded rects w 520, h 16, r 8) at y 730/755 (back) and seat at 800; 2 side legs/armrests as rounded paths. Fill `#3a2e26` (warm wood-dark), stroke `#8a7a6a`.
- Lamp post at the left (like the city lamp, taller) with a warm pool covering the bench (`#ffcf8a`). A tree at the right: trunk path + 3–4 overlapping canopy blobs `#1f2420`, stroke `#3a423a`. Falling leaves (DustField variant with rotation, `#b86a3a`).
- Night sky has 20 static stars (`#cfcfcf` r 1.5, twinkle via sin).

**Love: two cups** (`SetTwoCups`, insert/close-up)
- Push-in close-up on a table edge: two mugs (w 120, h 140, r 18, fill `#d8d4c8` and `#e8432f`), steam lines that **intertwine** (two sine paths with phase offset converging upward). Warm key light from the right: radial `#ffcf8a` 0.18.

**Overthinking: tangled thought-lines** (`SetThoughtTangle`)
- Hero at the bottom-center sits on a chair or the floor. Above his head, a **tangled scribble ball** of 1–3 long paths generated by a seeded random walk with high curvature, stroke `#8a8a8a` 2px. Its bounding radius grows over time (180→420px), and the line draws in via strokeDashoffset.
- Inner-voice red fragments ("what if", "they hate you") orbit inside the scribble at low opacity.
- Resolution beat: the tangle **straightens** by interpolating each point toward a straight line (lerp the noise amplitude to 0) and turns white, becoming a single calm line that becomes the floor line. That's a strong visual metaphor and cheap to animate.
```ts
function tangle(seed: number, n = 160, cx = 960, cy = 380, R = 300, calm = 0) {
  let a = 0, x = cx, y = cy; const pts: P[] = [];
  for (let i = 0; i < n; i++) { a += noise1(seed, i) * 1.4 * (1 - calm); const step = 22;
    x += Math.cos(a) * step; y += Math.sin(a) * step;
    const dx = x - cx, dy = y - cy, d = Math.hypot(dx, dy); if (d > R) { x = cx + dx / d * R; y = cy + dy / d * R; a += Math.PI * 0.8; }
    pts.push([x * (1 - calm) + (200 + i * (1520 / n)) * calm, y * (1 - calm) + 900 * calm]); }
  return wobblyPath(pts, {seed, amp: 0.8});
}
```

**Grief: empty chair** (`SetEmptyChair`)
- Armchair (couch construction, single seat, w 300) at the right third, lit by a soft cool window beam. A folded blanket/jacket draped on it (navy `#2b3247`, same as the bed blanket, visual rhyme). A small side table with an unfinished cup and a framed photo (rect with a tiny two-heads silhouette inside).
- The hero stands at the left third, half outside the light. Dust motes float only in the beam. The color script desaturates further: no red at all in grief scenes; the accent is the warm memory light (`#ffcf8a`) in flashbacks only.
- Flashback variant: the same set with a warm palette (lamp on, second figure in the chair in a softer gray `#bdb8aa`) and a cross-dissolve back to the cold empty version (same camera, so the cut does the emotional work).

---

## 3. Lighting recipes (SVG)

**Golden rule:** build light from **pre-shaped gradients** (radialGradient / linearGradient with alpha stops) blended with `mix-blend-mode: screen` (or `plus-lighter`). Avoid `feGaussianBlur` on large regions. A gradient whose last stop has opacity 0 already looks blurred, at almost no cost.

### 3.1 Generic glow component
```tsx
let glowId = 0;
export const Glow: React.FC<{cx: number; cy: number; rx: number; ry?: number; color: string; intensity?: number; falloff?: number; blend?: 'screen' | 'normal' | 'plus-lighter'}> =
({cx, cy, rx, ry = rx, color, intensity = 0.5, falloff = 0.55, blend = 'screen'}) => {
  const id = React.useMemo(() => `glow${glowId++}`, []);
  return <>
    <defs><radialGradient id={id}>
      <stop offset="0" stopColor={color} stopOpacity={intensity}/>
      <stop offset={falloff * 0.5} stopColor={color} stopOpacity={intensity * 0.45}/>
      <stop offset={falloff} stopColor={color} stopOpacity={intensity * 0.12}/>
      <stop offset="1" stopColor={color} stopOpacity={0}/>
    </radialGradient></defs>
    <ellipse cx={cx} cy={cy} rx={rx} ry={ry} fill={`url(#${id})`} style={{mixBlendMode: blend}}/>
  </>;
};
```
(In Remotion, generate ids with a stable prefix + index, not a global counter, to avoid SSR/concurrency mismatch: `useMemo(() => 'glow-' + props.key)`.) A three-stop curve (intensity → 45% → 12% → 0) approximates a Gaussian falloff and hides the gradient's "disc edge".

### 3.2 Phone blue on face (frames 5, 6)
- Glow source = phone screen position. `Glow color="#4a7fe0" intensity=0.45 rx=150` centered between phone and face. Second tighter layer: `#8ab4ff` 0.35 rx 45 at the screen.
- The phone itself: rounded rect 26x44 r 5, fill `#5a8ee8`, stroke `#2a3a60`. Flicker as scrolling: `intensity *= 0.9 + 0.1 * (0.5 + 0.5 * sin(f * 0.9))`, plus a brighter flash pulse on "swipe" frames.
- Optionally tint the face: a clipped `<rect fill="#4a7fe0" opacity=0.15>` inside the head clip, applied only to the side facing the phone (linearGradient).

### 3.3 Lamp cone (frame 7)
```tsx
<linearGradient id="lampCone" gradientUnits="userSpaceOnUse" x1={1775} y1={590} x2={1450} y2={860}>
  <stop offset="0" stopColor="#ffd28a" stopOpacity="0.28"/>
  <stop offset="0.6" stopColor="#e8b070" stopOpacity="0.10"/>
  <stop offset="1" stopColor="#e8b070" stopOpacity="0"/>
</linearGradient>
<path d="M1745,600 L1810,620 L1600,880 L1180,860 Z" fill="url(#lampCone)" style={{mixBlendMode:'screen'}}/>
<Glow cx={1420} cy={835} rx={330} ry={70} color="#ffcf8a" intensity={0.22}/>   {/* pool on desk */}
<Glow cx={1775} cy={600} rx={60} color="#fff2cc" intensity={0.6}/>             {/* bulb */}
```
Soft cone edges: either mask the cone with a horizontal-across-axis gradient (as in the spotlight), or draw 2 cones (wide at 0.5× intensity, narrow at 1×), which is cheap and looks soft.

### 3.4 Streetlight pools (frame 10)
```tsx
<Glow cx={lampX + 50} cy={432} rx={48} color="#fff0c0" intensity={0.75}/>          {/* bulb halo */}
<Glow cx={lampX + 50} cy={432} rx={130} color="#ffd890" intensity={0.15}/>         {/* wide halo */}
<Glow cx={lampX + 50} cy={860} rx={230} ry={110} color="#c8a060" intensity={0.28}/>{/* ground pool */}
```
Pools are lightly visible behind buildings too (screen blend lifts dark fills). When the hero passes through a pool, raise his cream fill brightness by +6% (interpolate on distance) for interaction.

### 3.5 Red shadow glow (antagonist, frames 5–8, 15, 17)
Observed: a tight saturated red halo hugging the black silhouette (~25–40px spread) that fades fast, with the hottest red at the contour.
Two options:
1. **Recommended (cheap):** draw the silhouette 3 times behind itself: stroke-only copies with `stroke="#ff3b20"`, widths 60/34/14 px, opacities 0.12/0.25/0.55, round joins, then the black fill on top. This gives a halo that follows the shape, with no filter, and can be animated by pulsing the opacities.
2. **Filter (quality, costlier):** `feMorphology dilate r=4 → feGaussianBlur std=14 → feFlood #ff3b20 → feComposite in → merge`. Only apply it to the figure's bbox. Cache: keep std constant (animating stdDeviation forces re-raster each frame anyway; animate the group opacity instead).
```tsx
<filter id="redHalo" x="-40%" y="-30%" width="180%" height="160%" colorInterpolationFilters="sRGB">
  <feMorphology in="SourceAlpha" operator="dilate" radius="3" result="d"/>
  <feGaussianBlur in="d" stdDeviation="14" result="b"/>
  <feFlood floodColor="#ff3b20" floodOpacity="0.95"/><feComposite in2="b" operator="in" result="g"/>
  <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
```
Ambient red spill: a radial `#e8432f` at 0.08–0.15, rx about 2× figure width, on the floor and props near the shadow. **Red vignette tint** for emotional pressure (frames 12, 17):
```tsx
<radialGradient id="redVignette" r="75%"><stop offset="0.55" stopColor="#3a0a08" stopOpacity="0"/><stop offset="1" stopColor="#3a0a08" stopOpacity="1"/></radialGradient>
<rect width={1920} height={1080} fill="url(#redVignette)" opacity={pressure /* 0..0.5 */}/>
```

### 3.6 Spotlight
See 2.5. Values: cone white 0.04→0.14, pool 0.22, dust inside the cone. Also add **text glow** for narrator lines in the spotlight and counters: duplicate text `fill="#fff"` with `opacity 0.15` and `filter: blur(6px)` (text is small, so the blur is cheap), or an HTML `text-shadow: 0 0 12px rgba(255,255,255,.25)`.

### 3.7 Rim light (summit, final bedroom)
Offset silhouette copy (warm `#ffb070`, +3px toward the light) behind the body + glow ellipse. In the final bedroom (frame 19) the dawn beam just brightens the floor and the bed. The hero gets a faint warm rim on the window side (`#e8a07a`, 0.4).

### 3.8 Blend-mode notes
- `mix-blend-mode: screen` on SVG elements works in Chromium (Remotion's renderer). It lightens without clipping, which is ideal for light over dark backgrounds.
- `plus-lighter` gives additive, harder light (good for bulbs and the impact flash).
- Plain `opacity` is fine for lights over pure black (screen ≈ normal over black). Use screen when light falls over props/characters.
- Avoid `multiply` darkening layers over the whole frame; use the vignette rect with alpha instead.

### 3.9 Performance warnings
| Technique | Cost | Guidance |
|---|---|---|
| `feGaussianBlur` on full-frame or large elements | **High** (re-rasterized every frame, scales with stdDeviation × area) | Avoid. Use radial gradients. |
| Blur on small elements (digits, text, phone) | Low–Medium | OK. Set a tight filter region (`x,y,width,height`). |
| Animated stdDeviation | High | Never. Animate opacity/scale of a pre-blurred element instead. |
| `feTurbulence` grain full-frame | High | Use pre-rendered PNG tiles (1.5). |
| `mix-blend-mode` | Low–Medium | Fine; limit to ~10 blended elements per frame. |
| Many particles (<200 circles) | Low | Fine. |
| Long wobbly paths recomputed per frame | Low | `useMemo` unless boiling. |
| Red-halo filter on giant shadow (frame 17, large bbox) | High | Use the stacked-stroke halo method. |
Render target: keep each frame under about 150 ms in `npx remotion render` on 1080p. If a scene uses more than 2 blur filters, convert them to gradients.

---

## 4. Color script and palette tokens

### 4.1 Color script per act
| Act / beat | Frames | Mood | Key light | Accent | Bg center/edge | Notes |
|---|---|---|---|---|---|---|
| **Hook** (black title) | 1 | neutral | none | white text | `#121212`/`#060606` | Fade text in 15f, hold, fade out |
| **Act 1: cold night routine** (bedroom, couch) | 2–6 | sleepy, numb | moon (cool white-blue), phone blue | red digits, red info text | `#121214`/`#070708` (very slightly cool) | Navy blanket, purple-gray couch. Cool bias overall |
| **Act 2: descent** (desk, montage, mirror) | 7–8 | heavier, oppressive | single warm lamp, small and far | red shadow, more frequent | `#0e0e0e`/`#050505` | Light pools shrink; shadow occupies the dark half of frame |
| **Rock bottom** | 9 | despair, quiet | white spotlight only | none (no red, no color) | `#0a0a0a`/`#030303` | Pure monochrome. The only color-free scene |
| **Turning point** (5:00 close-up, CLACK) | – | sudden | red digits fill the frame | red | black | Hard cut in, heartbeat sync |
| **Act 3: grind** (run, push-ups, bag, stairs) | 10–17 | determined, aggressive | warm streetlights / void | **red energy** (headband, bag, shattered words, giant shadow) | `#101010`/`#050505` | Contrast increases; red becomes the hero's color (headband), no longer only the enemy's |
| **Summit** | 18 | release, warmth | sun bloom low right | orange rim | sky gradient `#1e120e`→`#b25e2c` | Only full-color scene. Shift the white text to `#f6efe0` |
| **Finale** (same bedroom at dawn) | 19 | quiet victory | dawn window (indigo→peach) | tiny red shadow (weak glow, 0.4) | Act 1 bg but warm-shifted `#121110`/`#070605` | Same set as the opening = bookend. The window is the barometer |
| **End card** | 20 | resolve | text glow | red underline, ember specks | `#0b0b0b`/`#040404` | |

Principle: **the window and the accent light carry the story.** The moon (cold) becomes the dawn (warm) in the same window. Red starts as the enemy's color and ends on the hero's headband and the title underline.

For new topics, map the same arc: *cold/numb → darker + antagonist color → monochrome bottom → energy (antagonist color reclaimed) → warm release → same opening set, warm.* Swap the antagonist accent per topic if desired (default stays red for brand consistency): anxiety = red, grief = no antagonist color (cold blue `#5a7ab0` as "absence"), love = warm amber as the reward color.

### 4.2 Palette tokens (use these names in the skill)
| Token | Hex | Use |
|---|---|---|
| `bg.black` | `#000000` | letterbox, hard blacks |
| `bg.center` | `#131313` | vignette center |
| `bg.mid` | `#0e0e0e` | vignette mid |
| `bg.edge` | `#050505` | vignette edge |
| `bg.endcard` | `#0a0a0a` | end card |
| `floor.line` | `#525252` | floor line |
| `floor.lineLit` | `#8a8a8a` | floor inside light pools |
| `stroke.prop` | `#737373` | default prop outline |
| `stroke.propLight` | `#8a8a8e` | mirror, couch, stairs edge |
| `stroke.dim` | `#38383c` | city buildings |
| `prop.dark` | `#262628` | generic dark fill |
| `prop.mid` | `#333338` | generic mid fill |
| `prop.wood` | `#2a2522` | nightstand, desk |
| `prop.couch` | `#2e2a33` | couch |
| `prop.mirrorBase` | `#3c3c40` | mirror stand |
| `prop.stairs` | `#1c1c1e` | stairs fill top-left |
| `prop.stairs2` | `#252528` | stairs fill bottom-right |
| `prop.building` | `#19191c` | city buildings |
| `prop.window.warm` | `#6b5a3e` | lit building windows |
| `blanket.fill` | `#2b3247` | blanket/navy fabric |
| `blanket.stroke` | `#6d7593` | blanket outline |
| `pillow` | `#4a4a50` | pillow |
| `glass.night.top` | `#1d2130` | window glass |
| `glass.night.bot` | `#10121a` | window glass |
| `glass.dawn.top` | `#3a3f6e` | dawn window |
| `glass.dawn.mid` | `#7a5a72` | dawn window |
| `glass.dawn.bot` | `#c27a5c` | dawn window |
| `moon` | `#d6d6dc` | moon disc |
| `light.moon` | `#c8d0e6` | moon beam/glow |
| `light.phone` | `#4a7fe0` | phone glow |
| `light.phoneCore` | `#8ab4ff` | phone screen |
| `light.lamp` | `#ffcf8a` | desk lamp, streetlights |
| `light.bulb` | `#fff0c8` | bulb cores |
| `light.pool` | `#c8a060` | ground light pools |
| `light.spot` | `#ffffff` | spotlight (use with low alpha) |
| `dust` | `#8a8a8a` | dust motes |
| `ember` | `#b8693a` | end-card ember specks |
| `red.primary` | `#e8432f` | clock digits, X marks, underline, voice text |
| `red.glow` | `#ff3b20` | antagonist halo |
| `red.bag` | `#d42e1e` | punching bag |
| `red.bagHatch` | `#7e1a10` | bag hatch strokes |
| `red.bagHi` | `#ff6a52` | bag highlight |
| `red.shatter` | `#6a2622` | shattered word fragments |
| `red.vignette` | `#3a0a08` | pressure tint |
| `hero.body` | `#e6e1d3` | (from character agent; listed for lighting math) |
| `hero.far` | `#a9a597` | far limbs |
| `text.white` | `#efeadf` | narrator text |
| `text.gray` | `#b4b4b4` | DAY counter |
| `sweat.blue` | `#7fb2e6` | sweat drop |
| `dawn.sky0` | `#1e120e` | summit sky top |
| `dawn.sky1` | `#3e2118` | |
| `dawn.sky2` | `#6a3520` | |
| `dawn.sky3` | `#9a5028` | |
| `dawn.sky4` | `#b25e2c` | horizon |
| `dawn.sun` | `#f0a060` | sun bloom |
| `dawn.hill1` | `#5a2e1e` | far ridge |
| `dawn.hill2` | `#3e1f16` | |
| `dawn.hill3` | `#2a1510` | |
| `dawn.hill4` | `#150b08` | summit foreground |
| `dawn.rim` | `#c97a48` | rim stroke / character rim `#ffb070` |

Implement as `theme.ts` exporting `palette` + per-act `grade` objects:
```ts
export const grades = {
  act1:   {bg: ['#131315', '#0e0e10', '#060607'], tint: null},
  act2:   {bg: ['#101010', '#0b0b0b', '#040404'], tint: null},
  bottom: {bg: ['#0c0c0c', '#080808', '#030303'], tint: null, monochrome: true},
  act3:   {bg: ['#131313', '#0e0e0e', '#050505'], tint: {color: '#3a0a08', max: 0.35}},
  summit: {bg: null /* sky gradient */, tint: null},
  finale: {bg: ['#141210', '#0e0c0b', '#060504'], tint: null},
};
```
Grade transitions between acts happen under a fade to black, so you never need to interpolate a gradient live (though `interpolateColors` works if needed).

---

## 5. Camera and composition

### 5.1 Camera rig (Remotion)
Wrap each scene in a `<Camera>` group that applies `translate(W/2,H/2) scale(s) rotate(r) translate(-W/2 + x, -H/2 + y)` around a configurable focus point. **Text and DAY counter render outside the camera** (screen-space), and so do letterbox and grain.
```tsx
export const Camera: React.FC<{focus?: [number, number]; zoom?: number; x?: number; y?: number; rot?: number; children: React.ReactNode}> =
({focus = [960, 540], zoom = 1, x = 0, y = 0, rot = 0, children}) =>
  <g transform={`translate(${focus[0] + x},${focus[1] + y}) scale(${zoom}) rotate(${rot}) translate(${-focus[0]},${-focus[1]})`}>{children}</g>;
```
Build sets with ~6% bleed beyond 1920x1080 (backgrounds, floor) so zoom/shake never reveals edges.

### 5.2 Shot grammar observed
- **Static wide shots** dominate (frames 2, 5, 7, 8, 9, 10, 14, 16, 19). The full set is visible, the character is small (about 25–35% of frame height), and there's lots of negative space.
- **Thirds placement:** couch hero at 0.45 W; desk hero at 0.45 W with the shadow at the left third (0.25 W); mirror hero at the left third (0.33 W) facing the mirror at the right of center; run hero at 0.45 W facing right with run-space; summit hero at 0.40 W on the peak, sun at the right third; bag hero center with the bag at the right third.
- **Push-in progression:** frames 2→3→4 show the bedroom getting progressively tighter (window cropped by frame 4), as does frame 11→12→13 (push-up gets closer). So: **one slow continuous push-in per scene**, ending on the emotional beat.
- **Low angle / scale for threat:** the giant shadow is about 3x hero height, and the hero is placed bottom-left (frame 17).
- The camera rarely pans. The city run uses parallax in a locked-off frame instead.

### 5.3 Moves (deterministic recipes)
**Slow push-in (emotional beat):**
```ts
const p = interpolate(f, [start, start + N], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.bezier(0.33, 0, 0.2, 1)});
const zoom = 1 + 0.08 * p;            // 1.00 -> 1.08 (subtle); up to 1.25 for the 5:00->8:47 panic beat
// N: 90–150 frames (3–5 s) at 30fps. Focus = character's face.
```
Use `zoom 1.0→1.08` for spotlight / mirror / summit, and `1.0→1.25` across the 3-shot bedroom alarm sequence (can be split into cuts at 1.0, 1.12, 1.25 to match frames 2/3/4).

**Snap zoom (shock: "again.", turning-point clock):** zoom 1.0→1.15 in 4 frames with `Easing.out(Easing.cubic)`, hold.

**Handheld drift (keeps static frames alive):** low-frequency sum of sines, amplitude 2–4px, rotation ±0.15°.
```ts
const drift = (f: number, seed = 1) => ({
  x: 3 * Math.sin(f * 0.021 + seed) + 1.2 * Math.sin(f * 0.053 + seed * 2),
  y: 2 * Math.sin(f * 0.017 + seed * 3) + 1.0 * Math.sin(f * 0.047 + seed),
  rot: 0.12 * Math.sin(f * 0.013 + seed * 5),
});
```
Turn drift **off** for hook text, end card, and the rock-bottom spotlight (stillness = despair). Turn it **on** at 1.5× in Act 3.

**Impact shake (punch, mirror crack, CLACK, shadow split):** decaying shake from deterministic noise, 8–12 frames.
```ts
const shake = (f: number, hitFrame: number, amp = 14, dur = 10) => {
  const t = f - hitFrame; if (t < 0 || t > dur) return {x: 0, y: 0, rot: 0};
  const k = amp * Math.pow(1 - t / dur, 2);
  return {x: noise1(hitFrame, t * 2) * k, y: noise1(hitFrame, t * 2 + 1) * k, rot: noise1(hitFrame + 9, t) * k * 0.05};
};
```
Pair it with a 1–2 frame zoom kick (+0.03) and an optional 1-frame flash (white 0.15 or red 0.2).

**Run bob (city):** `y = 4 * Math.abs(Math.sin(f * Math.PI / stridePeriod))` on the camera, opposite phase to the hero's bounce, plus speed lines.

**Whip transitions (montage):** horizontal camera x 0→−2200 over 6 frames with `Easing.in(Easing.quad)`, plus motion-blur faking (3 ghost copies of the layer at 0.25 opacity offset by 40/80/120px). The next scene enters from +2200→0 with `Easing.out`. Use this sparingly; the reference's fast montages mostly use **hard cuts every 12–24 frames**.

### 5.4 Cuts vs fades
| Transition | Where | Spec |
|---|---|---|
| Fade from black | Hook text in; after hook into bedroom | 15–20f |
| **Fade to black** | Between acts: Act1→Act2, Mirror→Rock bottom, Summit→Finale, Finale→End card | out 12–20f, hold black 6–15f, in 12–20f |
| **Hard cut** | Within acts; DAY-counter montages (DAY 25 → 47 → 88 → 365); training montage | 0f; cut on action or on beat |
| Smash cut | Rock bottom → 5:00 clock close-up (silence → CLACK) | 0f + 1-frame white or red flash |
| Cross-dissolve | Mirror reflection swap (inside the mirror only); dawn window brightening; grief flashback | 10–18f |
| Match cut | Bedroom open ↔ bedroom finale (same framing, same clock position) | hard cut or fade, same camera |

Use a single `<FadeOverlay>` black rect at the top of the stack driven by `interpolate`. Don't fade individual layers for act transitions.

### 5.5 Framing rules for text space
- **Upper third (y 80–360) stays clear of props and heads** whenever a line of text is scheduled. Observed: all narrator/voice lines sit at y ≈ 0.15–0.30 H (frames 3, 4, 9, 12, 16, 18). The window (frame 2) is the only prop in the upper third and sits in the far right corner.
- **DAY counter safe box:** top-left, x 70–380, y 70–150 (below the letterbox). Never put props there (frame 7's wall clock is center-right for this reason).
- Red voice text sits **near the antagonist** (frames 6, 7, 17) or above the hero's struggle (12). White narrator text is **centered horizontally**.
- Big voice text (frames 14, 17) may occupy upper-left/center at about 90–110px. Make sure the set leaves a 900x260 empty block there.
- Character heads should stay below y ≈ 0.40 H in wide shots, so the push-in focus point rises with the face rather than pushing the head into the text zone.
- Bottom 8% stays empty (YouTube UI / captions). The floor line and below are "dead" space.
- Composition validator idea for the skill: each set exports `textSafeRect` and `dayCounterRect`; a dev-mode check asserts no prop bbox intersects them when text is active.

---

## 6. Suggested component API (for the orchestrator)
```
sets/
  Backdrop.tsx        (grade, vignette, optional red tint)
  FloorLine.tsx       (y, lit ranges)
  Letterbox.tsx, Grain.tsx, DustField.tsx, FadeOverlay.tsx, Camera.tsx
  Bedroom.tsx         ({time: 'night'|'dawn', clockText, alarmRinging, blanket: boolean})
  Couch.tsx, Desk.tsx ({clockStart, minutesPerFrame, lampOn}), Mirror.tsx ({reflection:'hero'|'shadow'|'heroBand', crackAt?})
  Spotlight.tsx, CityRun.tsx ({speed}), VoidStage.tsx, PunchingBag.tsx ({hits: number[]}), Stairs.tsx ({climbSpeed}),
  Summit.tsx, Calendar.tsx ({filled, startFrame}), EndCard.tsx ({title, tagline})
  TableForTwo.tsx, RainWindow.tsx, Crowd.tsx, ParkBench.tsx, TwoCups.tsx, ThoughtTangle.tsx ({calm}), EmptyChair.tsx ({flashback})
lib/ wobble.ts, sevenSeg.tsx, glow.tsx, camera.ts (pushIn, drift, shake), theme.ts (palette, grades)
```
Every set takes `{seed, boil?}` and must render purely from `useCurrentFrame()` plus props.
