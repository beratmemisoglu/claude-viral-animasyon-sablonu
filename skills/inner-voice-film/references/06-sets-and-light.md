# 06 — Sets, Light, Colour Script & Palette

Contents: 1 Layer order · 2 Set rules · 3 Set catalog · 4 Lighting recipes · 5 Colour script · 6 Palette tokens ·
7 New-topic sets

Full SVG construction specs (coordinates, wobbly-path generator, 7-segment digits, mirror clip + crack
generator, parallax city, stairs path, summit hills, calendar X): `deep-research/07-environments-lighting.md`.
Overrides from measurement: letterbox is 96 px top **and** bottom (not a 64 px top bar); line boil OFF; lamp =
radial pool; floor line at 68–75 % of full frame height; DAY counter box at x 150, y ≈147.

---

## 1. Layer order (every scene)

`backdrop (grade + vignette)` → far set (window/city/hills) → light volumes (beams, pools, screen blend) →
floor line → props → shadow figure → hero → foreground glows (phone, rim) → particles → **[camera group ends]**
→ text → DAY counter → topic HUD → fade overlay (scene) → letterbox → (grain).
Text/counter/HUD/letterbox are screen-space; the topic HUD and letterbox sit **above** the fade overlay.

## 2. Set rules

- One prop cluster, 3–5 props max, gray rounded hand-drawn outlines (`#737373–#8A8A8E`, 2.75–4.5 px), flat dark fills, **one accent light per scene**.
- Floor line always present except abstract voids (it *is* the void stage for push-ups/boxing).
- Keep the **upper third (y 96–360) free** whenever text is scheduled; DAY counter safe box top-left (x 70–420, y 96–190); hero heads below ≈ 40 % H in wide shots; nothing important in the bottom 8 %.
- Hand-drawn feel = slightly jittered control points smoothed with Catmull-Rom (seeded, static), small overshoot on structural line ends. No `feTurbulence`, no per-frame boil.
- Build sets with ~6 % bleed so the push-in never reveals edges. Memoise static set SVG.

## 3. Set catalog (DISCIPLINE/DOPAMINE vocabulary)

| Set | Essentials |
|---|---|
| **Bedroom** (ritual, bookend) | nightstand left with red 7-segment clock (digits `#D04D43`, slight bloom; red `〃` ticks when ringing), headboard post, mattress + rail + legs, gray pillow, navy blanket (wobbly bumps, one fold line), 4-pane window upper right: night glass gradient + moon + faint diagonal moonbeam (≈3–4 % white) / dawn glass gradient (indigo → mauve → peach) for the bookend |
| Couch | 3-seat slate-purple couch, thin legs, floor line. **Nothing else.** Blue phone halo. Shadow rises behind the right arm |
| Desk | thin plank desk, chair back post, olive/blue/red pill book stack, desk lamp angled toward the hero, open book/papers, wall clock (white hands spinning). Warm radial lamp pool |
| Mirror | oval mirror on a 2-tier stand, glass radial gradient, reflection inside a clipPath, crack lines drawn on with stroke-dashoffset |
| Spotlight (rock bottom) | pure black, narrow-top cone (white 0.04 → 0.14), floor pool ellipse, slow dust motes inside the cone only, floor line brighter inside the pool. No colour. |
| Night city run | 4–6 parallax layers: sky + speed lines, far dim buildings, mid buildings with sparse warm windows, streetlamps with bulb halos + ground pools, road dashes, foreground speed lines |
| Void stage | floor line only, slightly darker vignette (push-ups, boxing) |
| Punching bag | red capsule `#D42E1E` with hand-drawn darker hatch dashes + highlight stroke, rope off-frame top; glows red on hit |
| Stairs | diagonal wavy-nosed stair edge from bottom-left to top-right, gray fill gradient below; scroll diagonally for endless climb |
| Summit | dawn sky gradient `#1E120E → #B25E2C`, sun bloom low right (screen blend), 4 hill layers with smooth curves, rim-light stroke on the summit edge, warm rim on the hero (offset silhouette copy, not blur), wind streaks |
| Calendar | card with 7×5 grid, red hand-drawn X's drawn on in sequence, accelerating cadence |
| End card | `#0A0A0A` + vignette, no floor; title + red wavy underline + embers |
| DOPAMINE studio | black stage + saturated hobby props: easel/canvas, rainbow bottle shelf, sun-and-sea poster (waves animate), stool, potted plant, daylight window + warm light shaft |
| Park | saturated sky gradient, sun disc, clouds, hills, tiled round trees, grass with confetti flower dots, birds |

## 4. Lighting recipes (gradients, not blur filters)

- Generic `Glow`: radialGradient stops intensity → 45 % → 12 % → 0, `mix-blend-mode: screen`. Stable ids (prefix + key), not a global counter.
- Phone: `#4A7FE0` r ≈ 120–150 around face + tighter `#8AB4FF` at the screen; flicker ±10 % every 3 f (seeded); moves with the phone.
- Lamp: warm pool `#FFCF8A` on the desk + bulb core `#FFF2CC`; ramps up 3–6 f after the scene fades in.
- Streetlamp: bulb halo `#FFF0C0` + wide halo + ground pool `#C8A060` ellipse.
- Shadow glow: stacked silhouette copies (see 04 §2); ambient accent spill on nearby floor/props 0.08–0.15.
- Pressure tint: radial vignette of a dark accent (`#3A0A08`) at 0 → 0.35 on edges during "told you."/boss.
- Spotlight: see set catalog. Rim light: offset warm silhouette copy + pre-shaped gradient ellipse.
- Performance: no full-frame `feGaussianBlur`, never animate stdDeviation, ≤ 2 blur filters per frame (small elements only: digits, text, phone).

## 5. Colour script (topic-agnostic arc)

| Beat | Mood | Key light | Accent | Background |
|---|---|---|---|---|
| Hook | neutral | — | white text (optional tinted keyword) | `#0B0B0B` + vignette |
| Act 1 ritual/seduction | sleepy, numb, cool | moon (cool), phone blue | accent digits / excuse text | slightly cool `#0E0E10` |
| Decay | heavier | small warm lamp, far | accent shadow more frequent | `#0B0B0B` |
| Mirror | oppressive | backlight | accent glow inside glass | dark |
| **Rock bottom** | despair, quiet | white spotlight only | **none** | `#0A0A0A → #030303` |
| Turn | sudden | accent digits fill the frame | accent | black |
| Grind | aggressive | streetlights / void | **accent becomes the hero's** (token, bag, words) | `#101010` |
| Summit | release | low warm sun | orange rim | dawn gradient — the only warm full frame |
| Bookend | quiet victory | dawn window | tiny dim shadow | Act-1 bg warm-shifted `#141210` |
| End card | resolve | text glow | accent underline + embers | `#0A0A0A` |

The window/main light is the barometer (moon → dawn in the same window). Archetype B variant: colourful
props first → tinted darkness (plum for phone, teal for gaming) → gray (desaturate per layer) → colour earned back.

## 6. Palette tokens (`theme.ts`)

```ts
export const palette = {
  letterbox: '#000000', bgCenter: '#0E0E0E', bgMid: '#0B0B0B', bgEdge: '#050505', endcard: '#0A0A0A',
  floor: '#8E8E8E', floorLit: '#A8A8A8', stroke: '#8A8A8A', strokeDim: '#38383C',
  propDark: '#262628', propMid: '#333338', wood: '#2A2522', couch: '#2E2C36', blanket: '#2B3247', blanketStroke: '#6D7593', pillow: '#4A4A50',
  glassNightTop: '#1D2130', glassNightBot: '#10121A', glassDawn: ['#3A3F6E', '#7A5A72', '#C27A5C'], moon: '#D6D6DC', moonBeam: '#C8D0E6',
  phone: '#4A7FE0', phoneCore: '#8AB4FF', lamp: '#FFCF8A', bulb: '#FFF0C8', pool: '#C8A060', dust: '#8A8A8A', ember: '#B8693A',
  hero: '#E9C9A2', heroInk: '#2B1F17', sweat: '#A9CFF2', blush: '#E9A99C',   // Moon head (brand)
  textWhite: '#FFFFFF', textNarratorSoft: '#F2EFE6', textDay: '#BBBBBB', zz: '#B1B1B1',
  digits: '#D04D43', bag: '#D42E1E', bagHatch: '#7E1A10', underline: '#E8463A',
  dawn: ['#1E120E', '#3E2118', '#6A3520', '#9A5028', '#B25E2C'], dawnSun: '#F0A060', dawnRim: '#C97A48', heroRim: '#FFB070',
  rewardHeart: '#FD4C76', rewardSpark: ['#3FE0D0', '#FF5A9E', '#FF9A3C', '#7CE07C'],
  rainbow: ['#F8523C', '#FE981E', '#FED33A', '#43B054', '#3495FC', '#9866D0'],
};
export const accent = { // per film — `brand` is the DEFAULT for The Other Self
  brand:      { glow: '#2F6BFF', rim: '#7FA6FF', text: '#6E9BFF', eyes: '#D6E4FF', info: '#7DA5FF', underline: '#4F86FF', shadowFill: '#04050B' },
  // reference films (analysis only — do not ship red as our default, it is the competitor's signature):
  discipline: { glow: '#E8381F', rim: '#FF4A2E', text: '#F94E46', eyes: '#FF836C', info: '#FF4F58', underline: '#E8463A' },
  dopamine:   { glow: '#F860A9', rim: '#FF7FC0', text: '#F860A9', eyes: '#83E4F0', info: '#F860A9' },
};
// The transformation token (headband, scarf…) keeps its own colour per film; red is fine for a token.
```

## 7. New-topic sets (same language)

Loneliness: café table for two (one empty chair under a cool beam, only one cup steams), rainy window
(pre-blurred bokeh circles, rain streaks in a clip), crowd of faceless gray hero-silhouettes that never turn.
Love/heartbreak: park bench under a lamp, falling leaves, two mugs with intertwining steam.
Overthinking: tangled scribble ball above the head (seeded random walk) that straightens into the floor line.
Grief: empty armchair in a window beam with a folded blanket, photo frame, unfinished cup; warm flashback variant.
Comparison: phone feed of glowing perfect beans; his own running lane with ghost runners.
Code sketches: `deep-research/07` §2.13.
