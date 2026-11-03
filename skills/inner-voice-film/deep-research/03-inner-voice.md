# 03 — The Inner-Voice Antagonist (red-glow shadow figure)

Research agent 03. Sources: `00-brief/BRIEF.md`, `script-DISCIPLINE.txt`, `script-DOPAMINE.txt`, and the 20 reference frames.
I measured frames 5, 6, 7, 8, 12, 14, 15, 17 and 19 directly (pixel sampling with System.Drawing). Every number below
is either **measured** (M) or a **production choice** (P) made to match the measurements.

---

## 0. TL;DR (the ten rules)

1. The shadow is the **hero's silhouette with a slightly thinner, longer-legged build**. Fill is pure near-black `#050505` (M), which is *darker* than the
   background (`#0c0c0c`). It reads as a hole cut into the dark.
2. The glow is a **red-orange outer glow, not a stroke**. The rim is about `#D1422D` (M) and fades to background over about 50 px at 1080p for a 450 px-tall figure (M).
3. The face is only **two glowing salmon arcs and a smile** (`#FF836C` with a hot center `#FFA090`, M). It never frowns, and the expression stays **smug and serene**.
4. The size tracks how much power it has over the hero: **1.1× → 1.2× → 0.9× (mirror) → 2.4–2.6× (stairs) → 0.5× (final)** of the hero's standing height (M).
5. Glow intensity also tracks that power: desk 0.65, couch/stairs 1.0, final 0.25 (M, peak rim brightness ratios).
6. The voice is **red text `#F2473A`** (M) in the channel's Comic-style font. It is **lowercase, short and ends in a period**, with no exclamation marks.
7. The voice exists before the figure does. "just 5 more minutes..." and "again." are already red in frames 3–4, before the shadow ever appears.
8. The line ladder runs **comfort → fake care → futility → identity → gloat → command/desperation → silence**.
9. The words become objects. Hitting them shatters them into **dim (≈20% opacity), rotated, slowly floating glyphs** (frame 15, M: shard color `#301010`).
10. **Keep the same design for every topic.** It is the channel's recurring villain and brand asset. Topics change its words, props and defeat method, never its body.

---

## 1. Visual specification

### 1.1 Measured facts from the frames

| Frame | Scene | Shadow height (px, frame-native) | Hero standing-height equivalent | Ratio | Glow rim peak | Face |
|---|---|---|---|---|---|---|
| 5/6 | DAY 1 couch, standing behind right armrest | 265 (1125 w) | ≈241 | **1.1×** | `#D1422D` (strong) | eyes = two flat dashes drooping outward, smile in 6 |
| 7 | DAY 47 desk, leaning, hand on chair back | 422 (1462 w) | ≈359 | **1.18×** | `#8D3228` (≈0.65) | ∩ arcs (closed-smug) + ‿ smile |
| 8 | Mirror reflection | 335 (1328 w), legs cut by frame | 375 (hero) | **≈0.9×** (inside mirror) | backlight, sides + legs only | **faceless** |
| 17 | DAY 270 stairs, arms wide blocking | 390 (1091 w) | ≈166 | **≈2.4×** (≈2.6× with glow) | `#A13626` on arm, wide spread | smug arcs + wide V smile |
| 19 | Final 5:00, beside nightstand | 150 (1268 w) | ≈286 | **≈0.5×** | `#3F1D1A` (≈0.25), thin | sad: outer ends down, no smile |

How I got the hero-equivalent: I used the hero's head width as the scale reference against frame 8, where the hero stands full height at 0.282 × frame width.

**Glow falloff (M):** in frame 5 at y = 380 the edge pixel is `#D1422D`. It drops to `#892F24` at +12 px, `#3A1917` at +21 px and background at about +35 px (1125-wide frame). At 1920 wide that is roughly **60 px of visible bloom with a sharp, bright rim in the first ~8 px**.

**Eye core (M, frame 17):** `#FF836C`/`#FF8571`, with brighter centers up to `#FFA090`. Each eye is about 4.5% of the figure's height wide.

**Fill (M):** `#050505`, while the background vignette center is `#0c0c0c`–`#111`. The figure is a deeper black than the room.

### 1.2 Canonical rig (local units, standing height H = 600)

Origin is **at the ground between the feet**, y is negative upward, and the figure faces **+x** by default (mirror with `scale(-1,1)`).
At `scale = 1` it should be the **same height as the hero's standing height** (`HERO_H`). Render transform: `scale(scale * HERO_H / 600)`.

```
Part          Geometry (canonical units)                                     Notes
------------  -------------------------------------------------------------  ------------------------------
Head          circle cx=0 cy=-505 r=95  (top = -600)                         0.32 H diameter (M: frame 17)
Torso (bean)  top -445, bottom -198, width 180                              overlaps head; NO neck
Hips          (-32,-215) / (32,-215)
Legs          hip → knee (±34,-112) → ankle (±36,-20), stroke 36, round cap   thinner than hero's legs
Feet          ellipse rx=32 ry=18 at (ankle.x + 10*facing, -16)              small mitten feet
Shoulders     (-78,-388) / (78,-388)
Arms          upper 95, forearm 90, stroke 30, round cap                     "tube" limbs
Hands         circle r=26 at wrist                                           round mitts, larger than arm
Eyes          centers (-38,-516), (38,-516), width 46                        stroke 10, round cap
Mouth         center (0,-466), width 52                                      stroke 8, round cap
Pivots        root=(0,0) feet; hip=(0,-215); neck=(0,-430); shoulder L/R     for sway / lean / head bob
```

Compared with the hero, the shadow's **torso is narrower (0.30 H vs hero ≈0.38 H), its legs are longer (0.33 H) and its limbs are thinner**. It reads as a stretched, more "adult/threatening" version of the hero. In the mirror (frame 8) it uses **the hero's own silhouette** (bean body, stubby legs), because there it *is* the hero's reflection. Make the body path swappable (`build="voice" | "reflection"`).

### 1.3 Exact SVG (copy-paste reference, standing idle, facing right)

```svg
<svg viewBox="-200 -680 400 720" width="400" height="720" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Two-layer outer glow built from the silhouette's alpha (no double glow where limbs overlap) -->
    <filter id="iv-glow" x="-60%" y="-40%" width="220%" height="180%" color-interpolation-filters="sRGB">
      <feMorphology in="SourceAlpha" operator="dilate" radius="2" result="fat"/>
      <!-- outer bloom -->
      <feGaussianBlur in="fat" stdDeviation="21" result="b1"/>
      <feFlood flood-color="#E8381F" flood-opacity="0.85"/>
      <feComposite in2="b1" operator="in" result="g1"/>
      <!-- hot rim -->
      <feGaussianBlur in="fat" stdDeviation="5" result="b2"/>
      <feFlood flood-color="#FF4A2E" flood-opacity="1"/>
      <feComposite in2="b2" operator="in" result="g2"/>
      <feMerge>
        <feMergeNode in="g1"/>
        <feMergeNode in="g2"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <!-- small glow for eyes/mouth -->
    <filter id="iv-face-glow" x="-100%" y="-300%" width="300%" height="700%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- BODY: everything opaque #050505 inside ONE filtered group -->
  <g filter="url(#iv-glow)" fill="#050505" stroke="#050505" stroke-linecap="round" stroke-linejoin="round">
    <!-- legs (far leg first) -->
    <path d="M -32 -215 L -34 -112 L -36 -20" fill="none" stroke-width="36"/>
    <path d="M  32 -215 L  34 -112 L  36 -20" fill="none" stroke-width="36"/>
    <ellipse cx="-26" cy="-16" rx="32" ry="18" stroke="none"/>
    <ellipse cx="46"  cy="-16" rx="32" ry="18" stroke="none"/>
    <!-- torso bean -->
    <path stroke="none" d="M -90 -330 C -92 -410 -60 -445 0 -445 C 60 -445 92 -410 90 -330
                           C 88 -245 62 -198 0 -198 C -62 -198 -88 -245 -90 -330 Z"/>
    <!-- head -->
    <circle cx="0" cy="-505" r="95" stroke="none"/>
    <!-- arms: idle hanging, slight elbow bend -->
    <path d="M -78 -388 L -92 -295 L -86 -205" fill="none" stroke-width="30"/>
    <path d="M  78 -388 L  92 -295 L  86 -205" fill="none" stroke-width="30"/>
    <circle cx="-86" cy="-205" r="26" stroke="none"/>
    <circle cx="86"  cy="-205" r="26" stroke="none"/>
  </g>

  <!-- FACE: drawn ABOVE the glow group, own small glow -->
  <g filter="url(#iv-face-glow)" fill="none" stroke="#FF7E66" stroke-linecap="round">
    <!-- smug closed arcs (∩, outer ends drooping) -->
    <path d="M -61 -510 Q -38 -527 -15 -514" stroke-width="10"/>
    <path d="M  15 -514 Q  38 -527  61 -510" stroke-width="10"/>
    <!-- smile -->
    <path d="M -26 -470 Q 0 -452 26 -470" stroke-width="8"/>
  </g>
  <!-- optional hot core on the eyes -->
  <g fill="none" stroke="#FFB4A0" stroke-linecap="round" stroke-width="3" opacity="0.8">
    <path d="M -55 -514 Q -38 -524 -21 -515"/>
    <path d="M  21 -515 Q  38 -524  55 -514"/>
  </g>
</svg>
```

**Scaling the glow:** the blur must follow *rendered* size. A figure that renders H<sub>px</sub> tall gets
`outerStd = 0.035·H_px`, `rimStd = 0.009·H_px`, and `dilate = 0.004·H_px`. If you put the filter **inside** the scaled group, user-space units already scale with it, so just keep stdDeviation 21/5 in canonical units. For the final tiny shadow, multiply flood opacities by `intensity` (0.25).

**Cheaper alternative (no feMorphology, renders faster in Remotion/Chrome):** draw the same silhouette three times.
1. A copy with `fill/stroke="#E8381F"`, `filter: blur(21u)`, and `opacity 0.85·intensity`.
2. A copy with `fill/stroke="#FF4A2E"`, `blur(5u)`, and `opacity intensity`.
3. The crisp `#050505` copy on top.

Build the silhouette once as a `<symbol>`/`<g id>` and `<use>` it three times. I recommend this approach for production.

**Mirror backlight variant (frame 8):** put the glow copies inside the mirror clipPath and offset them `+0` x and `+8u` y, with outer blur ×1.3. Because the mirror's inner dark gradient covers the top, the glow appears mostly on the sides and between the legs. Turn the face off entirely.

### 1.4 Face library (all strokes `#FF7E66`, width 10 eyes / 8 mouth, round caps)

| `eyes` | Left-eye path (mirror x for right) | Used when |
|---|---|---|
| `smug` (default) | `M -61 -510 Q -38 -527 -15 -514` | whispering, gloating (frames 6, 7, 17) |
| `lidded` | `M -60 -512 L -16 -508` (flat dash, outer end 4u lower) | first appearance, bored-comfort (frame 5) |
| `slit` | `M -60 -506 L -16 -520` (inner end high: a narrow mean V) | lunge / "you can't." peak |
| `wide` | `circle r=11` at (-38,-516), fill `#FF7E66` | being hit, panic just before shattering |
| `sad` | `M -60 -520 Q -38 -512 -16 -508` (inner high, outer low) | shrunken, defeated (frame 19) |
| `none` | — | mirror reflection, silhouette in far background |

| `mouth` | Path | Used when |
|---|---|---|
| `smile` (default) | `M -26 -470 Q 0 -452 26 -470` | comfort lines |
| `grin` (frame 17 "V") | `M -30 -474 L 0 -458 L 30 -474` | gloat / block |
| `smirk` | `M -24 -466 Q 4 -458 28 -476` | "told you." |
| `open` | `ellipse cx=0 cy=-466 rx=14 ry=10` fill | desperation / shout (rare) |
| `flat` | `M -18 -464 L 18 -464` | defeated |
| `none` | — | mirror, frame 5 |

Blink: every 90–150 frames (seeded random), scaleY of the eye group goes 1 → 0.1 → 1 over 6 frames. A smug arc that "blinks" thins to a hairline and comes back.

### 1.5 Pose vocabulary (joint angles)

Angles are in degrees. Arm angle 0 = hanging straight down and +90 = pointing forward/horizontal toward the hero. Elbow is the relative bend. `lean` rotates the torso and head around the hip pivot (0,-215), and `headTilt` rotates around the neck (0,-430). "near" = the arm on the hero's side.

| Pose | Ref | lean | headTilt | near arm (sh / el) | far arm (sh / el) | legs | Notes |
|---|---|---|---|---|---|---|---|
| `lurk` | 5/6 | +4 | +6 | **150 / −80** (hand raised beside head, a "psst" wave) | 10 / 0 (hidden behind body) | straight, feet together | standing behind furniture; lower body hidden by couch arm |
| `lean` | 7 | **+14** | +8 | 55 / 10 (hand resting on chair back) | 20 / 5 | slight knee bend 8° | the "caring friend" lean |
| `shoulder` | script DAY 1 | +18 | +10 | 75 / 5 (hand **on hero's shoulder anchor**) | 15 / 0 | near leg stepped forward 10° | hand target = hero.shoulderWorld via IK |
| `whisper` | P | +20 | +18 (toward hero ear) | 120 / −110 (cupped hand by mouth) | 10 / 0 | — | text font 0.7×, opacity 0.45 |
| `mirror` | 8 | 0 | 0 | 5 / 0 | 5 / 0 | parallel | faceless, uses `build="reflection"` |
| `block` | 17 | 0 | 0 | **88 / 8** | **88 / 8** (arms wide, slight upward curl) | apart 6° each | giant, centered on path; smug grin |
| `loom` | P | +25 | +15 down | 60 / 30 (reaching down) | 60 / 30 | wide stance | giant leaning over a small hero |
| `lunge` | P | +22 | −5 | 95 / 0 (pointing) | 30 / 0 | front knee 20° | used on "you can't." emphasis |
| `defeated` | 19 | +8 | **+14 (head down)** | 4 / 6 | 4 / 6 | knees 6° | tiny, eyes `sad`, glow 0.25 |
| `idle` | P | 0 | 0 | 8 / 6 | 8 / 6 | straight | default |

Blend poses with `interpolate` on each joint, using 12–20 frames and `Easing.inOut(Easing.sin)`.

---

## 2. Behaviour and animation (30 fps)

Note: the shadow **never walks with a real walk cycle**. It glides, rises or simply *is there*. That is the creepiness. Its legs move at most ±4° while gliding.

### 2.1 Entrances

| Entrance | Frames | Recipe | Easing |
|---|---|---|---|
| **Fade + glow bloom** (default, frame 5) | 0–24 | body opacity 0→1 over f0–18. Glow intensity 0→**1.5** over f0–14, then back to 1.0 over f14–24 (bloom overshoot). Outer blur ×1.6→×1.0. Eyes off until f16, then scaleY 0→1 over f16–22 ("eyes ignite"). | opacity: `Easing.out(Easing.quad)`; bloom: `Easing.out(Easing.cubic)`, then `Easing.inOut(Easing.sin)` |
| **Rise from floor** | 0–30 | clipPath = everything above the floor line. translateY from +H to 0. Glow starts at full intensity so you see a red sun rising before the head emerges. Ends with a 2% scaleY settle (spring damping 14, stiffness 120). | `Easing.out(Easing.cubic)` + spring |
| **Step out of darkness** | 0–28 | starts at x −80u, opacity 0, glow 0. Slides to x 0 while opacity →1 (f0–16) and glow 0→1 (f8–28). Body is visible *before* the glow, a black on black reveal. | `Easing.inOut(Easing.sin)` |
| **Mirror replacement** | see 2.6 | — | — |
| **Already there (cut-in)** | 0 | cut to a shot where it is already present, with glow at 1.2 for 6 frames → 1.0. Use it in montages. | linear |

### 2.2 Idle loop (always on while visible)

```ts
const t = frame / 30;
glowPulse   = 1 + 0.12 * Math.sin(2 * Math.PI * t / 2.0);          // 2 s period
sway        = 1.5 * Math.sin(2 * Math.PI * t / 3.2);               // deg, pivot = feet (0,0)
breathScaleY= 1 + 0.012 * Math.sin(2 * Math.PI * t / 2.6 + 0.7);  // pivot = feet
headBobIdle = 1.0 * Math.sin(2 * Math.PI * t / 3.2 + 1.2);        // deg, pivot = neck
eyeFlicker  = 1 + 0.08 * noise1D(seed, frame / 6);                 // eye opacity only
```
Phase-offset everything with a per-instance `seed` so two shadows never pulse in sync.

### 2.3 Speaking (text + body)

- **Text color** `#F2473A` (M), with a soft glow (`text-shadow` equivalent via SVG blur 3u, opacity 0.5). Use the channel's rounded handwritten font (Comic Neue Bold / "Comic Sans MS"-like).
- **Placement:** anchor to head center `(0,-505)` in world space. Text sits **above and slightly toward the open side**, with its baseline about 0.15 H above the head top. In frame 6 it overlaps the head top. In frame 17 it sits beside the head, on the side away from the stairs. Never put it between the shadow and the hero's face.
- **Size by escalation level:** whisper 36–44 px, normal 56–64 px, identity 80–96 px, command 120–140 px (at 1080p).
- **Appear:** opacity 0→target over 8 f, y +8 px→0, `Easing.out(Easing.quad)`. Words appear **one at a time** (stagger 5–7 f per word) for lines of three words or more, and all at once for one- or two-word lines.
- **Whisper opacity:** comfort lines go up to 0.35–0.6 only. Frame 7's "you're tired." measures at about 20% brightness, which shows the voice can be barely legible. Identity/command lines are 1.0.
- **Head bob per word:** headTilt +3° and translateY −4u, using a 0→1→0 sine envelope over 6 f per word. Eyes squint (scaleY 0.8) during the bob. Glow +0.15 per word.
- **Hold:** 1.2 s, plus 0.25 s per word. Exit opacity →0 over 10 f, or **don't exit**: let identity lines linger and dim to 0.15 (they become the "words floating in the room" later reused in the punching-bag scene).

### 2.4 Approaching the hero

- **Glide:** x speed 1.5–2.5 px/f (1080p). Torso lean ramps 0→+14° as distance decreases (`interpolate(dist,[400,80],[0,14])`).
- **Stop distance:** shoulder-touch distance (the near hand reaches the hero's shoulder anchor). The hand lands with a tiny 4-frame overshoot (spring damping 18).
- **Hero reaction:** none at first (DISCIPLINE DAY 1: "Karakter itiraz etmez", he does not object). Later scenes add an eye-shift toward the shadow. Ignoring is the point: the voice works because it feels like your own thought.

### 2.5 Lunge / block ("you can't.")

| f | Event |
|---|---|
| 0–6 | anticipation: scale 1→0.97, glow 1→0.8 (inhale) |
| 6–12 | burst: scale 0.97→1.12 (`Easing.out(Easing.back(1.6))`), arms 40°→88°, eyes `smug`→`slit`, glow →1.6 |
| 8–14 | text slams in: scale 1.4→1.0, opacity 0→1 over 4 f; camera shake 6 px decaying over 10 f (seeded) |
| 14–40 | settle: scale 1.12→1.06, glow 1.6→1.2, eyes back to `smug` + `grin` |

### 2.6 Mirror replacement trick (frame 8, ≈ 2.0 s)

1. **f0–30:** a normal reflection. The hero's flipped silhouette sits inside the mirror clipPath, dimmed 0.6, with the hero's sad face.
2. **f30–42:** the reflection's cream fill interpolates to `#050505`, face features fade out, and limbs slightly lengthen (body path morphs `reflection`→`voice` at only 30%; it must still feel like *him*).
3. **f36–56:** backlight glow fades in inside the mirror (intensity 0→0.85).
4. **f50:** the reflection **stops copying the hero**. The hero shifts weight and the reflection does not. This is a 1-frame desync and the real scare beat.
5. **f60–68:** crack paths draw on (stroke-dashoffset, white `#bbb`, width 2) from the point nearest the reflection's head, with the glass-crack SFX.
6. **f70+:** text "you're lazy." (identity size), then 30 f later "you'll never change.", next to the mirror and away from the hero.

### 2.7 Being destroyed (hero passes through and splits it)

| f | Event |
|---|---|
| 0 | contact frame. Use a white flash 2 f (opacity 0.25 full-screen) and hit-stop: hold 3 f |
| 3–6 | eyes → `wide`, glow spikes to 2.0 (a last flare) |
| 6 | split. Render the shadow twice, clipped by complementary polygons along the hero's path line (diagonal ~70° for stairs). |
| 6–30 | halves translate ±90u perpendicular to the cut, rotate ∓10°, opacity 1→0 (`Easing.in(Easing.quad)`) |
| 6–20 | **glow collapse**: glow intensity 2.0→0, outer blur ×1→×0.3 (the light gets sucked inward, `Easing.in(Easing.cubic)`) |
| 6–50 | particles: 28 embers emitted along the cut line. r 2–5 u, color `#FF5A3C`→`#7A1A10`. Velocity 2–6 px/f outward plus upward drift −0.6 px/f (ash rises), drag 0.95/f, life 30–45 f. Seed every value with `random('iv-split-'+i)`. |
| 10–40 | the shadow's last text line ("you can't.") cracks into glyph shards (see 3.4) |

Lighter variant (punch): no split. Body squash 0.9×1.1 on impact over 4 f, then recoil 30u back, glow flicker.

### 2.8 Shrinking (the epilogue state)

The shrink happens **between scenes**: the final frame cuts straight to a small shadow. If you animate it on screen, over 45 f:
- scale current→0.45 (`Easing.inOut(Easing.cubic)`), pivot at the feet
- glow intensity 1→0.25, outer blur ratio ×1→×0.6
- eyes `smug`→`sad` at f20 (crossfade 6 f), mouth→`flat` or `none`
- pose→`defeated`
- the idle sway amplitude halves, so it looks deflated rather than calm.

In its tiny state it may mutter a line at 30 px, opacity 0.4 ("...maybe tomorrow?"). **The hero does not look at it** and walks out. Being ignored is the victory.

---

## 3. Psychology and writing

### 3.1 Core character

The voice is **not a monster that shouts**. It is a *friend who wants you comfortable*. It is smug and serene, and certain it will win because it always has.
Its power comes from three things:
1. it sounds like **your own thought** (second person, lowercase, never named, appears behind you);
2. it **offers relief now** in exchange for cost later;
3. it **turns repeated behaviour into identity**. The film's thesis inverts this: "lazy isn't who you are. It's what you repeat."

Its expression stays the same smug arc until it loses. The only time it looks truly menacing (big, arms wide) is when it is **desperate**, because the hero is already winning. Size grows with desperation, not with real power. Its real power peaked in the mirror, where it was the hero's own size.

### 3.2 The escalation ladder

| Lvl | Name | Function | Typography | Figure state | DISCIPLINE examples |
|---|---|---|---|---|---|
| 0 | **Narration bleed** | the voice is present but has no body | red, normal size, no figure | absent | "just 5 more minutes..." · "again." |
| 1 | **Permission / comfort** | makes quitting feel kind | whisper 40 px, opacity 0.5, ellipsis | 1.1×, `lurk`, `lidded`/`smile` | "skip the gym." · "tomorrow." |
| 2 | **Fake care** | frames the habit as self-care | 48 px, opacity 0.35–0.6 | 1.2×, `lean`/`shoulder` | "you're tired." |
| 3 | **Futility** | makes trying look pointless | 56 px, 0.8 | same, closer | "why even try?" |
| 4 | **Identity** | turns the behaviour into who you are | 80–96 px, 1.0 | mirror, the hero's own size, faceless | "you're lazy." · "you'll never change." |
| 5 | **Gloat** | attacks the first struggle of recovery | 64 px, figure absent (voice only) | absent, or a voice from offscreen | "told you." |
| 6 | **Echo ammunition** | old words become targets | huge 110 px, floating | absent | "you're lazy" · "quit." · "nobody cares." |
| 7 | **Desperation / command** | last stand, blocks the path | 130 px | 2.4–3×, `block`/`lunge` | "you can't." |
| 8 | **Silence / powerless** | lost | none or tiny 30 px, 0.4 | 0.45×, `defeated` | (silent in the film) |

The structural rule is that **levels 1–4 happen before rock bottom and levels 5–7 after the turn**. After the turn the hero converts each line into fuel ("told you." → he finishes the push-up out of spite).

### 3.3 Line-writing guide

1. **2–4 words.** Six is the hard maximum. Shorter is scarier.
2. **lowercase, ending in a period.** Ellipsis "..." for comfort and procrastination lines. A question mark is allowed only on futility lines. **Never "!"**: calm certainty is more frightening than shouting.
3. **Second person ("you")** or an imperative ("skip", "quit", "stay"). It never uses "I", except in the final pathetic line.
4. **The language of care in the first half:** *just, only, tomorrow, rest, deserve, one more, it's fine*.
5. **The language of identity in the middle:** *you're [trait]. you'll never [change]. this is who you are.*
6. **Absolute words at the end:** *can't, never, nobody, always*.
7. **Plant and pay off:** every late line must call back an earlier one. "told you." only works because of the earlier "you're tired.". The narrator's thesis line **inverts** the voice's identity line ("you're lazy." → "lazy isn't who you are.").
8. **Concrete and present:** "skip the gym." beats "you are unmotivated." Name the specific temptation of the scene.
9. **One line per scene beat**, two at most. The image carries the rest.
10. **Write the narrator in white and the voice in red.** The two never speak in the same frame except at the climax.

### 3.4 Words become physical objects

| Moment | What the text does | Implementation |
|---|---|---|
| Whisper | barely there, like a thought | opacity 0.2–0.5, slight blur 0.6u |
| Identity (mirror) | stays and dims; it "sticks to you" | it doesn't exit and fades to 0.15 over 3 s |
| Ammunition (bag scene, frame 14) | huge text **hangs in the air like an object** above the bag | 110 px, static, slight bob ±3 px |
| **Shatter on punch** (frame 15) | each glyph becomes a shard | split into per-character `<text>` (or per-glyph path). On impact frame `fi`, glyph i gets velocity `v = normalize(glyphPos − impactPos) * rand(6,14) px/f`, spin `rand(−12,12)°/f`, drag 0.9/f. After 12 f, settle into slow drift (0.3 px/f) and rotation (0.5°/f). Opacity 1→**0.2** (M: shards ≈`#301010`) and they **stay floating** in the background for the rest of the scene. Add 6–10 small dots (r 2) in the same dark red for dust. |
| Collapse (stairs) | "you can't." cracks in half along the hero's path | same clip-split as the body (2.7) |
| Final | no text; the voice has no words left | — |

---

## 4. Topic variants

### 4.1 Recommendation: one design, every topic

**Keep the exact same silhouette, glow, colors and face library for every film.** The reasons:
- The channel already reuses it. The DOPAMINE breakdown mentions "a black silhouette character appears behind the hero and touches him ('just one more')", and later it "offers the phone again". A recurring villain is a **brand asset**, like a mascot: viewers recognize the channel from a thumbnail glow alone.
- Red is the channel's only accent and it is reserved for the voice. Changing the hue breaks the color code (white = truth, red = the lie).
- What changes per topic: **(a) the lines, (b) the prop it offers** (phone, pillow, a photo, a closed door), **(c) the pose emphasis, (d) the defeat method, (e) the final tiny state.**
- The only allowed variation is **prop-held glow**. For example, a phone in the shadow's hand casts the blue phone glow on its face side. The body itself never changes.

### 4.2 Ladders per topic

Each list is in order (1 = first whisper, last = final stand / defeated murmur).

**LONELINESS: the voice personifies isolation-as-safety ("they don't really want you").**
Prop: closes doors and curtains, turns the phone face-down. Defeat: the hero knocks on a door or sends a message, and the shadow shrinks as a second character's warm light enters.
1. "stay in tonight."
2. "they're busy anyway."
3. "don't text first."
4. "you'd just be a bother."
5. "nobody noticed you left."
6. "they forgot you."
7. "you're better off alone."
8. "you're hard to love."
9. "they'll leave. they always do."
10. (tiny) "...maybe next time?"

**LOVE / HEARTBREAK: the voice personifies attachment and replaying the past ("go back").**
Prop: holds an old photo or the phone with their chat open. Defeat: the hero lets go of the photo and the red letters blow away like petals.
1. "just check their story."
2. "one message won't hurt."
3. "maybe they miss you."
4. "read it again."
5. "it was your fault."
6. "you weren't enough."
7. "no one will love you like that."
8. "you'll never get over it."
9. "go back."
10. (tiny) "...remember?"

**OVERTHINKING: the voice personifies "what if" loops.**
Prop: the red words multiply into a tangled scribble around the hero's head. Defeat: the hero does the action, and the scribble snaps into straight lines and falls.
1. "think it through first."
2. "what if it goes wrong?"
3. "they're judging you."
4. "replay what you said."
5. "what did they mean by that?"
6. "you always mess it up."
7. "don't move until you're sure."
8. "you can't control this."
9. "stop. wait. think."
10. (tiny) "...what if?"

**ANXIETY: the voice personifies threat-detection ("stay safe").**
Prop: none. It grows bigger the more the hero avoids. Defeat: the hero breathes and steps forward, and the shadow deflates (Exposure in reverse; the shrink is the climax).
1. "stay home. it's safer."
2. "you'll embarrass yourself."
3. "everyone will see."
4. "your heart's racing. leave."
5. "something bad is coming."
6. "you can't handle this."
7. "you're not normal."
8. "run."
9. "you'll fall apart."
10. (tiny) "...be careful."

**COMPARISON: the voice personifies the scoreboard ("they're ahead").**
Prop: holds up glowing phone screens of other people, as if they were mirrors. Defeat: the hero turns the phone around and looks at his own day counter.
1. "just look at them."
2. "they're your age."
3. "they started after you."
4. "why not you?"
5. "you're behind."
6. "you're wasting your life."
7. "you'll never catch up."
8. "you're nothing special."
9. "give up. they won."
10. (tiny) "...but look at them."

**GRIEF: the voice personifies guilt and frozen time ("moving on is betrayal").**
Handle carefully: the shadow is **less smug and more mournful** here. Use `lidded` eyes, never `grin`. Prop: keeps a clock stopped, sits in their chair. Defeat: not destroyed. **It is held, then it fades** (the hero hugs it and it shrinks into a small warm ember: the only time the glow turns orange). This is the one topic where the "defeat" is acceptance.
1. "stay in bed."
2. "don't open the curtains."
3. "you should have called."
4. "you could have saved them."
5. "smiling is betrayal."
6. "it should have been you."
7. "you'll never feel okay again."
8. "forgetting them is wrong."
9. "don't let go."
10. (tiny) "...i miss them too."

**DOPAMINE / PHONE: the voice personifies cheap pleasure ("one more").**
Prop: hands over the phone, a slot-machine lever, a donut (as in the DOPAMINE breakdown). Defeat: the hero turns his back on it and paints, and color floods back into the frame and pushes the shadow out.
1. "just one more."
2. "one more video."
3. "you earned this."
4. "you'll start after this."
5. "it's only 5 minutes."
6. "real life is boring."
7. "you can't focus anyway."
8. "you need me."
9. "you're nothing without me."
10. (tiny) "...one more?"

**COMFORT ZONE: the voice personifies safety and sameness ("why risk it").**
Prop: a blanket and a couch. It literally holds the couch cushions. Defeat: the hero walks out a door into light, and the shadow can't follow past the threshold (light clips it).
1. "why change now?"
2. "this is fine."
3. "you're comfortable here."
4. "too risky."
5. "people like you don't."
6. "you'll fail out there."
7. "you'll look stupid."
8. "stay where you belong."
9. "you can't."
10. (tiny) "...it was nice here."

### 4.3 Placement of the ladder in the film structure

| Act (from DISCIPLINE timing) | Ladder levels | Shadow scale |
|---|---|---|
| Hook / routine (0:00–0:13) | L0 narration bleed | none |
| Introduction (0:13–0:21) | L1 | 1.1× |
| Spiral montage (0:21–0:40) | L2–L3 | 1.1–1.2× |
| Mirror (0:40–0:50) | L4 identity | 0.9× (the hero's own size) |
| Rock bottom (0:50–1:00) | silence (narrator in white) | none |
| Turn / grind (1:00–1:49) | L5 gloat, L6 ammunition | none, voice only |
| Final fight (1:49–2:04) | L7 command | 2.4–3× |
| Epilogue (2:17–2:37) | L8 silence | 0.45× |

---

## 5. Remotion component API

### 5.1 Props

```ts
type IVState = 'hidden' | 'appear' | 'idle' | 'speak' | 'approach' | 'lunge' | 'hit' | 'shatter' | 'shrink' | 'defeated';
type IVPose  = 'idle' | 'lurk' | 'lean' | 'shoulder' | 'whisper' | 'mirror' | 'block' | 'loom' | 'lunge' | 'defeated';
type IVEyes  = 'smug' | 'lidded' | 'slit' | 'wide' | 'sad' | 'none';
type IVMouth = 'smile' | 'grin' | 'smirk' | 'open' | 'flat' | 'none';
type IVEntrance = 'bloom' | 'rise' | 'stepOut' | 'cut';

interface InnerVoiceProps {
  /** world position of the FEET (px, composition space) */
  x: number; y: number;
  /** height relative to the hero's standing height (1 = same height). Typical: 1.1 couch, 1.2 desk, 2.6 giant, 0.45 tiny */
  scale: number;
  /** hero standing height in px for this shot (from the hero rig); default 540 */
  heroHeight?: number;
  facing?: 1 | -1;                 // +1 = faces right
  build?: 'voice' | 'reflection';  // reflection = hero's own silhouette (mirror)

  pose: IVPose | Partial<JointAngles>;  // named pose or raw joint overrides
  poseBlendFrames?: number;             // default 16

  /** 0..2. Multiplier for glow opacity AND spread. 1 = frame 5 strength. Default by scale: >=2 →1.0, <=0.6 →0.25 */
  intensity?: number;
  glow?: { color?: string; rimColor?: string; spread?: number; backlit?: boolean }; // defaults #E8381F / #FF4A2E / 1
  eyes?: IVEyes;   // default 'smug'
  mouth?: IVMouth; // default 'smile'

  /** timeline-driven behaviour; `stateFrom` = composition frame when the state began */
  state: IVState;
  stateFrom: number;
  entrance?: IVEntrance;          // used when state === 'appear'

  /** speech: rendered as red text anchored to the head */
  line?: string;
  lineLevel?: 0|1|2|3|4|5|6|7|8;  // drives size + opacity (section 3.2)
  lineSide?: 'auto' | 'left' | 'right' | 'above';
  lineFrom?: number;              // frame the line starts; words staggered automatically
  lineLinger?: boolean;           // don't exit; dim to 0.15

  /** interaction targets */
  handTarget?: { x: number; y: number };  // e.g. hero.shoulderWorld → 2-bone IK on near arm
  approachTo?: { x: number; speed?: number };

  /** destruction */
  splitLine?: { angleDeg: number; offset?: number };   // for 'shatter'
  impactPoint?: { x: number; y: number };               // for 'hit' / text shatter

  clipToMirror?: string;   // id of a clipPath (mirror glass) when used as reflection
  seed?: string;           // deterministic noise / particles / blink timing
}
```

### 5.2 State semantics

| state | Duration (f) | What happens (section) | Auto-next |
|---|---|---|---|
| `hidden` | — | renders nothing (or only the floating text shards) | — |
| `appear` | 24–30 | entrance recipe 2.1 per `entrance` | `idle` |
| `idle` | ∞ | pulse, sway, breath, blink (2.2) | — |
| `speak` | 8 + 6·words + hold | text in + head bob per word (2.3); idle continues underneath | `idle` |
| `approach` | distance/speed | glide + lean ramp + IK hand to `handTarget` (2.4) | `idle` |
| `lunge` | 40 | anticipation → burst → text slam → settle (2.5) | `idle` (pose `block`) |
| `hit` | 20 | squash, recoil, glow flicker, text shatter at `impactPoint` | `idle` |
| `shatter` | 50 | hit-stop, flare, clip-split along `splitLine`, glow collapse, embers (2.7) | `hidden` |
| `shrink` | 45 | scale → 0.45, glow → 0.25, eyes `sad`, pose `defeated` (2.8) | `defeated` |
| `defeated` | ∞ | tiny idle at half amplitude, optional 30 px murmur | — |

Everything derives from `frame - stateFrom`, using only `interpolate`, `spring` and `random(seed)`. There is no React state and no CSS animation, so renders are deterministic.

### 5.3 Usage examples

```tsx
// DAY 1 couch
<InnerVoice x={1340} y={820} scale={1.1} heroHeight={420} facing={-1}
  pose="lurk" eyes="lidded" mouth="none" state="appear" entrance="bloom" stateFrom={0} seed="couch" />
<InnerVoice ... state="speak" stateFrom={45} eyes="smug" mouth="smile"
  line="skip the gym." lineLevel={1} lineSide="above" />

// Mirror
<InnerVoice build="reflection" pose="mirror" eyes="none" mouth="none"
  glow={{ backlit: true }} intensity={0.85} clipToMirror="mirrorGlass" ... />

// Stairs climax
<InnerVoice x={1200} y={760} scale={2.6} pose="block" eyes="smug" mouth="grin"
  state="lunge" stateFrom={30} line="you can't." lineLevel={7} lineSide="left" />
<InnerVoice ... state="shatter" stateFrom={120} splitLine={{ angleDeg: 70 }} />

// Epilogue
<InnerVoice x={240} y={880} scale={0.45} pose="defeated" eyes="sad" mouth="flat"
  intensity={0.25} state="defeated" stateFrom={0} />
```

### 5.4 Implementation notes

- **Layering:** for each of the 3 glow layers, render the body group via `<use href="#iv-body-{id}">`, with the face as a separate group on top. Use `useId()`-based ids so multiple shadows don't collide.
- **Filter cost:** Gaussian blur on a 1000 px-tall giant is expensive in headless Chrome. Clamp `stdDeviation` to ≤40 px and set filter region bounds tightly (`x/y/width/height` in user space).
- **Pivots:** root transform = `translate(x,y) scale(facing*s, s) rotate(sway)`. Torso lean: `rotate(lean, 0, -215)`. Head: `rotate(tilt, 0, -430)`. Arms: nested `<g>` with `rotate(sh, ±78, -388)` and then `rotate(el, elbowX, elbowY)`. Draw limbs as nested segment groups (never independent paths) so they can't detach.
- **IK for the hand on the shoulder:** use two-bone analytic IK (law of cosines) with upper = 95u and fore = 90u, and clamp reach. If the target is beyond reach, increase `lean` first.
- **Text component:** `<VoiceLine text level side anchor from seed />`. Use a shared module for the shatter physics so the punching-bag scene can shatter **free-floating** voice text with no figure present.
- **Text shards persist:** keep shard positions as a pure function of `(frame - impactFrame, glyphIndex, seed)` so they can live through later shots.
- **Sound hooks (for the audio agent):** use a low breathy pad swell on appear, a soft "whisper" layer under speak (level ≤3), a sub-boom on lunge, glass crack on mirror, and a reverse-cymbal → sudden cut on shatter.
