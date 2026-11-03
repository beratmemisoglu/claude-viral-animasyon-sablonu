# 04 — On-Screen Typography & Text System

Research agent 04/10 · "Day One Films" reverse-engineering · Source: 20 reference frames of *DISCIPLINE* (measured), both scripts, BRIEF.md.

> There is **no voice-over**. Text is the narration, so the text system *is* the script delivery engine.
> All numbers below are normalized to a **1920×1080 @ 30 fps** frame. The screenshots had different crop sizes, so I measured
> against the frame width (H = W·9/16) and converted. Treat the values as ±10% estimates, close enough to rebuild the look.

---

## 0. TL;DR rules (for the skill)

1. **One font family for everything**: a Comic-Sans-style rounded handwritten sans. Use **Comic Relief** (Google Fonts, metric clone of Comic Sans, includes `latin-ext` for Turkish). Fall back to **Mali**, then **Pangolin**.
2. **Color carries the meaning.** White (`#F2EFE6`) is the storyteller or the lesson. Red (`#FF4A3D`) is the inner voice or a failure state. Gray (`#BDBDBD`) is the time stamp (DAY N).
3. **At most one message on screen** besides the DAY counter. White and red never share a frame.
4. **Short lines**: narrator ≤ 7 words, voice ≤ 4 words (usually 2–3), info ≤ 4 words. Always one line, never wrapped. Couplets are two separate cards.
5. **Every text fades and blurs in.** Nothing types or slides in except the special cases listed in §3.
6. **Hold time** = `max(1.2 s, 0.8 s + 0.3 s × words)`, plus 0.5 s if the line ends a scene or carries the lesson.

---

## 1. Text role taxonomy (measured)

Coordinates: `x%` / `y%` = center of the text block as a % of frame width/height (from top-left). Font size = CSS `font-size` in px at 1080p (≈ % of height in brackets).

### (a) Narrator / lesson text: white
| Property | Value |
|---|---|
| Frames | 1 "Every day started the same." · 9 "He believed it." · 16 "Motivation gets you started." · 18 "Nobody is coming to save you." · 20 subtitle |
| Color | `#F2EFE6` (warm off-white, same family as the hero body `#E8E4D8`; not pure white) |
| Glow | Very soft: `text-shadow: 0 0 10px rgba(255,250,235,.18)`. It reads as a slight bloom, not a neon glow. |
| Size | **68–72 px (≈6.5% H)**. Cap height ≈ 4.6% H, measured the same in 1, 9, 16 and 18, so it is a fixed size. |
| Weight | Regular (400). Bold is for the title only. |
| Position: on black / alone | x 50%, **y 50%** (frame 1: y≈49.5%) |
| Position: over a scene | x 50%, **y 13–21%** (frame 18: 13%, 16: 18%, 9: 20.6%). It sits above the character's head zone and never overlaps the hero. |
| Width | 30–50% of frame width. Never wraps. |
| Case | Sentence case + **period** always. |
| Max words | 7 (longest seen: "Nobody is coming to save you." = 6) |
| Line breaks | None. A two-part thought ("Motivation gets you started." / "Discipline keeps you going.") is shown as **two consecutive cards** at the same position. |

### (b) Info / state text: red, plain
| Property | Value |
|---|---|
| Frames | 3 "just 5 more minutes..." · 4 "again." |
| Color | `#FF4A3D` (slightly warm red, a touch lighter than the shadow glow `#FF3B30`) |
| Glow | Subtle: `0 0 8px rgba(255,60,48,.35)` |
| Size | **72–90 px (≈7–8% H)**. "again." is a little larger, about 86 px, because a one-word punch line gets more size. |
| Position | Above the character, in the free upper area: frame 3 x 49.5% / y 25%; frame 4 x 56% / y 23.6%. It is centered over the **scene composition** (bed + character), not pinned to the head. |
| Case | **all lowercase**, ends with `...` (ongoing excuse) or `.` (verdict). |
| Max words | 4 |
| Semantics | Narrates the character's *state or excuse* in his own lazy voice. No shadow is present, so this is the voice before it gets a body. |

### (c) Inner-voice speech: red with glow, attached to the shadow
| Property | Normal ("talking") | Faint ("whisper", frame 7) | Shout (frames 14, 17) |
|---|---|---|---|
| Examples | 6 "skip the gym." · 12 "told you." | 7 "you're tired." | 14 "you're lazy" · 17 "you can't." |
| Color | `#FF4A3D` | `#FF4A3D` at **opacity 0.18–0.25** (reads as `#5A1A1A` on black) + 1.5 px blur | `#FF4A3D`, full |
| Glow | `0 0 6px rgba(255,59,48,.6), 0 0 18px rgba(255,59,48,.35)` | none (blur stands in for it) | `0 0 10px rgba(255,59,48,.55), 0 0 30px rgba(255,59,48,.3)` |
| Size | **55–65 px (≈5.5% H)**, "told you." ≈ 75 px | ≈65 px | **145–175 px (≈14–16% H)** |
| Position | Next to or above the **shadow's head**. Frame 6: x 74% / y 35.6%, with the text baseline overlapping the top of the head. Frame 12 has no shadow, so the text floats at the **upper-right of the hero's head** (x 76% / y 39.5%). | Above the shadow head, frame 7: x 31% / y 23% | Frame 14: top center x 53.5% / y 16.7%, drawn **over** the punching bag. Frame 17: left of the giant shadow's head, x 26% / y 30%. |
| Case | lowercase, ends with `.` | lowercase, `.` | lowercase. The period is optional: drop it when the word is about to be destroyed ("you're lazy"), keep it for a verdict ("you can't."). |
| Max words | 4 | 4 | 3 |

Rule: **voice size scales with the shadow's power.** Small shadow → 55 px. Giant shadow → 170 px. In the ending the shadow is tiny and says nothing.

### (d) DAY counter: gray, top-left
| Property | Value |
|---|---|
| Frames | 5, 6 "DAY 1" · 7 "DAY 47" · 10 "DAY 3" · 11/12 "DAY 12" · 14/15 "DAY 64" · 16/17 "DAY 270" |
| Color | Fill `#C4C4C4`, with a thin darker inner edge giving a chalky look: `-webkit-text-stroke: 1.5px #6E6E6E` + `paint-order: stroke fill` |
| Glow | none |
| Size | **≈48 px** (cap height ≈3.4% H), **Bold 700**, ALL CAPS, `letter-spacing: .04em` |
| Position | Left edge at **x ≈ 4.5% (86 px)**, vertical center at **y ≈ 10.5% (113 px)**. Top-left, inside the safe area, below the letterbox bar. |
| Format | `DAY {n}`, no leading zeros, one space |
| Behavior | Appears with the scene cut (or 6 frames after) and stays for the **whole scene**. It is never animated loudly. |

### (e) Counters / numbers (push-up "3")
| Property | Value |
|---|---|
| Frame | 13 "3" |
| Color | `#EEECE6` |
| Glow | Strong white bloom: `0 0 12px rgba(255,255,255,.45), 0 0 28px rgba(255,255,255,.2)` |
| Size | Digit height ≈10.4% H → **font-size ≈150 px**, Bold 700 |
| Position | Above the hero, horizontally on his center: x ≈ 51% / y ≈ 23% |
| Behavior | Pop-in per increment (see §3). The count is non-linear (1 … 3 … 5) and timed to each rep's push-up. |

### (f) Title card / end card
| Element | Value |
|---|---|
| Title "DISCIPLINE" | `#F2EFE6`, **Bold 700, ALL CAPS**, font-size **≈250 px (23% H)**, width ≈69% W, center x 50% / **y 40.5%**. Glow `0 0 14px rgba(255,250,235,.35)` plus a dark soft drop shadow `0 6px 18px rgba(0,0,0,.6)`. Heavy rounded strokes: if the Bold weight is too thin, add `-webkit-text-stroke: 6px #F2EFE6` with `paint-order: stroke fill`. |
| Underline | Hand-drawn **wavy** red line, `#E8463A`, stroke **8–9 px**, round caps, spans **105% of the title width** (starts slightly left of the D and ends past the E). 4–5 gentle waves, amplitude ≈ 6 px. Sits at **y ≈ 53.6%**, about 0.12 em under the baseline. |
| Subtitle | "Day one, or one day." `#F2EFE6`, Regular, **≈66 px**, center x 50% / **y ≈ 66.5%** |
| Particles | Sparse warm embers: 15–25 dots, r = 1.5–3 px, `#C9773A` at 40–70% opacity, drifting slowly upward |
| Background | Near-black `#0B0B0B` with a radial vignette |

### (g) Shattered-word particles (frame 15)
| Property | Value |
|---|---|
| Look | Individual glyphs (u, t, w, s, n, g, k…) **scattered across the whole frame**, each randomly rotated (±180°, some upside-down or mirrored-looking), dark muted red, plus tiny red ember dots |
| Color | `#FF4A3D` at **opacity 0.28–0.4** (reads as `#6E2222`), no glow. Embers are `#B8322A`, r 2–3 px. |
| Size | ≈ 60–70% of the source word's size (≈ 80–100 px from a 146 px word), with some scale variance (0.8–1.2) |
| Persistence | The letters **linger in the background** while the fight continues. They come from several destroyed phrases ("you're lazy", "quit", "nobody cares"), which is why letters like *w, g, k* show up. |
| Layer | Behind the hero and the bag, in front of the background |

---

## 2. Font

### The look
Rounded, monoline, informal **Comic Sans MS**. The "a", the "y" with a straight tail, "g" and "t" shapes in frames 3, 4 and 16 match Comic Sans closely. The title (frame 20) is Comic Sans **Bold** with extra-thick rounded strokes. The DAY counter is the same family in bold caps.

### Verified in `@remotion/google-fonts@4.0.535`
I checked each module directly on unpkg (`dist/esm/<Name>.mjs` → HTTP 200) and read its subsets and weights:

| Font | Module | Weights | Subsets | Turkish (ç ğ ı İ ö ş ü) | Match to reference |
|---|---|---|---|---|---|
| **Comic Relief** | `@remotion/google-fonts/ComicRelief` | 400, 700 | latin, **latin-ext**, cyrillic, greek | ✅ | ★★★★★ A metric-compatible Comic Sans clone, so it is nearly identical |
| **Mali** | `.../Mali` | 200–700 | latin, **latin-ext**, thai, vietnamese | ✅ | ★★★★ Rounded handwritten with many weights, good for the title |
| **Pangolin** | `.../Pangolin` | 400 | latin, **latin-ext**, cyrillic | ✅ | ★★★★ Very close to the handwritten Comic feel |
| Comic Neue | `.../ComicNeue` | 300, 400, 700 | **latin only** | ❌ ğ ş İ missing | ★★★★ Good look, but unusable for Turkish |
| Patrick Hand | `.../PatrickHand` | 400 | latin, latin-ext | ✅ | ★★★ Narrower and more "marker" |
| Itim | `.../Itim` | 400 | latin, latin-ext, thai | ✅ | ★★★ |
| Short Stack | `.../ShortStack` | 400 | latin only | ❌ | ★★★ |
| Gochi Hand, Coming Soon, Sniglet, Fredoka | exist | — | — | — | Too far from the reference |

**Recommendation**
- **Primary: Comic Relief** (400 for narrator, voice and info; 700 for DAY, counters and title).
- **Fallback: Mali** (400/700). If you want a softer, chunkier title, Mali 700 also works for the title card only.
- CSS stack: `"Comic Relief", "Mali", "Comic Sans MS", "Comic Neue", cursive`

```ts
// fonts.ts
import { loadFont as loadComicRelief } from "@remotion/google-fonts/ComicRelief";
import { loadFont as loadMali } from "@remotion/google-fonts/Mali";

export const { fontFamily: COMIC } = loadComicRelief("normal", {
  weights: ["400", "700"],
  subsets: ["latin", "latin-ext"], // latin-ext = Turkish ğ ş İ
});
export const { fontFamily: MALI } = loadMali("normal", {
  weights: ["400", "700"],
  subsets: ["latin", "latin-ext"],
});
export const FONT_STACK = `${COMIC}, ${MALI}, "Comic Sans MS", cursive`;
```
Always pass `weights` and `subsets`. Loading everything can time out (Remotion troubleshooting docs).

**Turkish casing:** use `toLocaleUpperCase("tr-TR")` / `toLocaleLowerCase("tr-TR")` (i→İ, I→ı). This matters for "DAY/GÜN" counters, titles, and the lowercase inner voice.

---

## 3. Text animation vocabulary (@30 fps)

All of it is driven by `useCurrentFrame()`, `interpolate` and `spring`. No CSS animations. `f` = frames since the element's `from`.

| # | Name | Used for | Recipe |
|---|---|---|---|
| A1 | **Fade + blur-in** (default) | narrator, info, voice | 0→18 f: opacity 0→1, `blur(8px)`→0, translateY 10→0 px, `Easing.out(Easing.cubic)` |
| A2 | **Fade + blur-out** (default exit) | all | last 12 f: opacity 1→0, blur 0→6 px. No movement. |
| A3 | **Per-word reveal** | long lessons (≥5 words), dramatic lines | Each word runs A1 with a 14 f duration, staggered **5 f/word**. Whole line visible after `5·(n-1)+14` f. |
| A4 | **Typewriter whisper** | "just one more…", "tomorrow..." | 1 char per **2 f** (15 cps). The ellipsis dots arrive 6 f apart. Optional soft cursor-less tick SFX. |
| A5 | **Letter jitter** | voice lines (subtle menace) | Every 2 f, each glyph gets dx, dy ∈ ±1.2 px and rot ±1.5° from `random(seed+glyph+floor(f/2))`. Use ±3 px for shouts. Off for narrator. |
| A6 | **Pop-in scale** | counters, "again." | `spring({damping: 10, stiffness: 180, mass: .6})` scale 1.35→1 over ≈10 f. Glow radius 28→12 px. The old number cross-fades out in 4 f. |
| A7 | **Shake (red)** | voice shout, impact | 8–10 f decaying shake: `amp = 10·(1-f/10)`, `x = amp·(random(s+f)-.5)*2`. Pair it with a 6 f scale punch 1.15→1. |
| A8 | **Slam-in (giant)** | "you can't.", "you're lazy" | scale 1.6→1 + opacity 0→1 in **6 f** (`Easing.out(Easing.exp)`), then A7 shake 10 f, then A5 jitter at ±2 px for the hold. |
| A9 | **Dim to faint** (frame 7) | voice the hero isn't listening to, or the whisper of an echo | Starts at full opacity, then over 20 f goes opacity 1→0.22 and blur 0→1.5 px with no movement. Or it appears directly faint (A1 to a 0.22 target). Hold faint ≥ 1.5 s. |
| A10 | **Shatter** (frame 15) | voice words destroyed by punches or action | On impact frame: the word splits into glyphs. Each glyph flies out (v = 6–18 px/f, angle random, slightly biased away from the impact point), spins ±(4–12)°/f with a velocity decay of 0.92/f, and opacity drops 1→0.35 over 12 f while the glyph shrinks to 0.7×. Then it drifts slowly (0.3 px/f, ±0.5°/f) **for the rest of the scene**. 10–20 ember dots spawn with the burst. |
| A11 | **Underline draw** | title card | SVG path with `strokeDasharray = L`, `strokeDashoffset` L→0 over **20 f**, `Easing.inOut(Easing.quad)`. It starts 8 f after the title settles. |
| A12 | **Count roll** | DAY montage (47→88→365) | Optional: interpolate integer over 10–12 f with ease-out, rounding each frame. Default is a hard cut per scene. |
| A13 | **Hard cut** | DAY counter, info on scene cut | Appears on the cut frame or 4–6 f after, no fade. Disappears with the scene. |

### Hold durations (reading speed)
```
holdFrames(words) = round(30 * max(1.2, 0.8 + 0.3 * words))
    + (isLesson || isSceneEnd ? 15 : 0)
```
| Words | Hold |
|---|---|
| 1 ("again.") | 1.2 s = 36 f |
| 2 ("told you.") | 1.4 s = 42 f |
| 3 ("skip the gym.") | 1.7 s = 51 f |
| 5 ("Every day started the same.") | 2.3 s + 0.5 = 84 f |
| 6 ("Nobody is coming to save you.") | 2.6 s + 0.5 = 93 f |

Total on-screen time = in (18 f) + hold + out (12 f).
- **Couplet gap**: line 1 out (12 f) → **6–10 f of empty** → line 2 in. The answer line ("So save yourself.", "Discipline keeps you going.") gets **+0.5 s** extra hold. That is the punch.
- **Title card sequence**: title in (A1, 24 f, scale 0.96→1) → hold 8 f → underline draw (20 f) → hold 10 f → subtitle in (A1) → hold until 2.5 s past the subtitle → global fade to black (20 f).

### When text overlaps action vs. gets the screen alone
| Text alone (black or near-empty frame, camera still) | Text over action |
|---|---|
| Hook line (frame 1). Black, centered, y 50%, followed by a 1–1.5 s hold before the first scene. | Info text over the bedroom loop (frames 3–4) |
| Rock-bottom lesson (frame 9). The character is motionless under the spotlight, and the text sits in the spotlight's upper cone. | Voice lines while the hero acts (sofa, desk, push-ups, bag) |
| Final lesson at the summit (frame 18). The hero walks slowly and the camera is calm. | Counters during reps |
| Title card (frame 20) | DAY counter, always |

Rule: **white lesson text only appears when the motion calms down** (slow walk, idle, or a hold). **Red text appears during conflict.** No text during fast montage cuts except the DAY counter. If a line needs reading, the shot has to last at least `holdFrames`.

---

## 4. Writing style rules

1. **Narrator (white)**: sentence case, ends with a period, past tense in the story part ("He believed it.") and second person or present tense in the lesson part ("Nobody is coming to save you."). ≤ 7 words, one clause.
2. **Inner voice (red)**: **all lowercase**, second person, imperative or judgement: "skip the gym." "you're tired." "you're lazy" "you can't." "told you." ≤ 4 words. A period marks a verdict. Drop it on words that will be destroyed.
3. **Info (red)**: lowercase first-person excuse or flat state: "just 5 more minutes..." "again." Use digits ("5"), not words.
4. **Ellipsis `...`** only for trailing excuses or temptation (snooze, "just one more..."). Never on narrator lesson lines.
5. **Couplet structure** (the signature move): setup line → answer line, each ≤ 6 words, with the answer *flipping* the setup.
   - "Motivation gets you started." / "Discipline keeps you going."
   - "Nobody is coming to save you." / "So save yourself."
   - "He believed it." / "Day after day."
   - "But lazy isn't who you are." / "It's what you repeat."
   The second line is usually shorter, and often starts with *So / But / It's*.
6. **Chiasmus or word-flip for the tagline**: "Day one, or one day." "Cheap pleasure steals your color. Earn it back." The tagline sits under the title, sentence case, ≤ 6 words + an optional 2–3 word call ("You decide.").
7. **Title**: one word, ALL CAPS, the abstract topic noun (DISCIPLINE, DOPAMINE, ROOTS, READY, LONELINESS).
8. **Hook** (first frame): ≤ 6 words, past tense, universal routine: "Every day started the same." For new topics: "Every night ended the same." / "He was never really alone." / "The phone was always there."
9. **Rhythm**: about 12–16 text cards total in 2:30–2:45. Roughly: hook (1) → info ×2 → voice ×3–4 → rock-bottom couplet (2–4) → voice in the fight ×2–3 → lesson couplet (2) → shout (1) → summit couplet (2) → title + tagline. Red count ≈ white count.
10. **Turkish adaptation**: keep the same rules. The voice is lowercase (`sporu atla.`, `yapamazsın.`), narrator is sentence case. Turkish runs ~25% longer, so give it a 6-word max and use the same formula with 0.33 s/word.

---

## 5. Remotion component proposals

Shared tokens:
```ts
// typography.ts
export const C = {
  white: "#F2EFE6", red: "#FF4A3D", redGlow: "255,59,48",
  gray: "#C4C4C4", grayStroke: "#6E6E6E", underline: "#E8463A", ember: "#C9773A",
};
export const SIZE = { narrator: 70, info: 80, voice: 60, voiceShout: 165, day: 48, counter: 150, title: 250, subtitle: 66 };
export const holdFrames = (text: string, fps = 30, lesson = false) => {
  const w = text.trim().split(/\s+/).length;
  return Math.round(fps * Math.max(1.2, 0.8 + 0.3 * w)) + (lesson ? Math.round(fps * 0.5) : 0);
};
// common in/out envelope
export const envelope = (f: number, dur: number, inF = 18, outF = 12) => ({
  opacity: interpolate(f, [0, inF, dur - outF, dur], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
  blur: interpolate(f, [0, inF, dur - outF, dur], [8, 0, 0, 6], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) }),
  y: interpolate(f, [0, inF], [10, 0], { extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) }),
});
```
Every component is placed inside a `<Sequence from durationInFrames>` and reads `useCurrentFrame()` locally. `durationInFrames` defaults to `18 + holdFrames(text) + 12`.

### `<NarratorText>`
```ts
type NarratorTextProps = {
  text: string;                       // ≤7 words, sentence case + "."
  position?: "center" | "top";        // center = y 50% (alone), top = y 17%
  y?: number;                         // override, % of height
  reveal?: "fade" | "perWord";        // A1 | A3
  lesson?: boolean;                   // +0.5s hold
  durationInFrames?: number;
};
```
Renders an `AbsoluteFill` with a centered `div`: `fontSize 70`, `color C.white`, `textShadow 0 0 10px rgba(255,250,235,.18)`, `whiteSpace: nowrap`, `filter: blur(${blur}px)`. For `perWord`, map the words to `<span>` elements, each running its own envelope offset by `i*5` frames.

### `<InfoText>`
```ts
type InfoTextProps = {
  text: string;                 // lowercase, "..." or "."
  x?: number; y?: number;       // default 50 / 24 (%)
  size?: number;                // default 80; 1-word punch → 90
  entrance?: "fade" | "pop" | "typewriter"; // A1 | A6 | A4
};
```

### `<VoiceText>`
```ts
type VoiceTextProps = {
  text: string;                         // lowercase
  anchor: { x: number; y: number };     // shadow head position in px (from rig); text sits above-left/right
  side?: "above" | "left" | "right";    // frame 6 = above, 17 = left
  intensity?: "whisper" | "talk" | "shout";  // whisper=A9 faint, talk=A1+A5, shout=A8+A7
  size?: number;                        // auto: talk 60, shout 165 (or scale with shadowScale)
  shadowScale?: number;                 // size = 60 * clamp(shadowScale,1,2.8)
  jitter?: number;                      // px, default talk 1.2 / shout 3
  seed: string;
  shatterAt?: number;                   // frame (local) → hands off to <ShatterText>
};
```
Glyphs are rendered as `<span>`s so jitter (A5) and shatter can address each letter. Glow comes from `textShadow: 0 0 6px rgba(C.redGlow,.6), 0 0 18px rgba(C.redGlow,.35)`, doubled for shout. Whisper uses `opacity 0.22`, `blur 1.5px`, and no glow.

### `<DayCounter>`
```ts
type DayCounterProps = {
  day: number; label?: string;      // label "DAY" | "GÜN"
  rollFrom?: number;                // optional A12 count roll
  delay?: number;                   // default 0–6 f, hard cut (A13)
};
```
Style: `position:absolute; left: 86px; top: 113px; transform: translateY(-50%)`, `fontWeight 700`, `fontSize 48`, `letterSpacing .04em`, `color C.gray`, `WebkitTextStroke 1.5px C.grayStroke`, `paintOrder "stroke fill"`, text `${label.toLocaleUpperCase('tr-TR')} ${n}`.

### `<CountUp>`
```ts
type CountUpProps = {
  values: number[];        // e.g. [1, 3, 5]
  hitFrames: number[];     // local frames where each value lands (sync to rep animation)
  x?: number; y?: number;  // default 51% / 23%
  size?: number;           // 150
};
// current = last index with hitFrames[i] <= f; local = f - hitFrames[i]
// scale = 1 + 0.35 * (1 - spring({frame: local, fps, config:{damping:10, stiffness:180, mass:.6}}))
// glow  = interpolate(local, [0,10], [28,12], clamp)
```

### `<ShatterText>` (deterministic)
```tsx
import { random, useCurrentFrame, interpolate } from "remotion";

type ShatterTextProps = {
  text: string;                 // "you're lazy"
  origin: { x: number; y: number }; // px, center of the word as it was rendered
  impact: { x: number; y: number }; // px, punch contact point (bias direction)
  fontSize: number;             // source size (e.g. 146)
  seed: string;                 // e.g. "day64-lazy"
  settleOpacity?: number;       // 0.35
  embers?: number;              // 14
};

export const ShatterText: React.FC<ShatterTextProps> = ({ text, origin, impact, fontSize, seed, settleOpacity = .35, embers = 14 }) => {
  const f = useCurrentFrame();              // 0 = impact frame (wrap in <Sequence from={impactFrame}>)
  const glyphs = [...text].filter(c => c !== " ");
  const advance = fontSize * 0.52;          // approx glyph advance for layout of start positions
  const startX = origin.x - (glyphs.length * advance) / 2;

  return (<>
    {glyphs.map((ch, i) => {
      const r = (k: string) => random(`${seed}-${i}-${k}`);      // deterministic 0..1
      const x0 = startX + i * advance, y0 = origin.y;
      // direction: away from impact + random spread
      const base = Math.atan2(y0 - impact.y, x0 - impact.x);
      const ang = base + (r("a") - .5) * Math.PI * 1.2;
      const v0 = 6 + r("v") * 12;                     // px/frame
      const k = 0.92;                                 // velocity decay per frame
      const travel = v0 * (1 - Math.pow(k, f)) / (1 - k);   // closed-form, no state
      const drift = Math.max(0, f - 25) * 0.3;        // slow float after burst
      const x = x0 + Math.cos(ang) * travel + Math.sin(f / 40 + r("p") * 6) * 6;
      const y = y0 + Math.sin(ang) * travel - drift * (r("d") > .5 ? 1 : -.4);
      const spin = (r("s") - .5) * 24;                // deg/frame initial
      const rot = (r("r0") - .5) * 30 + spin * (1 - Math.pow(k, f)) / (1 - k) + f * (r("w") - .5) * .5;
      const op = interpolate(f, [0, 12], [1, settleOpacity], { extrapolateRight: "clamp" });
      const sc = interpolate(f, [0, 12], [1.1, 0.65 + r("z") * .25], { extrapolateRight: "clamp" });
      const glow = interpolate(f, [0, 10], [1, 0], { extrapolateRight: "clamp" });
      return (
        <span key={i} style={{
          position: "absolute", left: x, top: y, fontSize, color: C.red, opacity: op,
          transform: `translate(-50%,-50%) rotate(${rot}deg) scale(${sc})`,
          textShadow: `0 0 ${12 * glow}px rgba(${C.redGlow},${.6 * glow})`,
          fontFamily: FONT_STACK, whiteSpace: "pre",
        }}>{ch}</span>
      );
    })}
    {Array.from({ length: embers }).map((_, j) => {
      const r = (k: string) => random(`${seed}-e${j}-${k}`);
      const a = r("a") * Math.PI * 2, v = 4 + r("v") * 10;
      const t = v * (1 - Math.pow(.9, f)) / (1 - .9);
      const op = interpolate(f, [0, 6, 45 + r("l") * 60], [0, .9, .35], { extrapolateRight: "clamp" });
      return <div key={`e${j}`} style={{ position: "absolute",
        left: origin.x + Math.cos(a) * t, top: origin.y + Math.sin(a) * t - f * .2,
        width: 3 + r("s") * 3, height: 3 + r("s") * 3, borderRadius: 99,
        background: "#B8322A", opacity: op }} />;
    })}
  </>);
};
```
Notes:
- All motion is a **closed-form function of `f`**, so it renders the same on any frame or in parallel (Lambda-safe).
- Hand-off: `<VoiceText shatterAt>` stops rendering at the impact frame, and `<ShatterText>` starts in a `<Sequence from={impact}>` with the same `origin` and font size. That way glyph positions match on the transition frame.
- Several shattered phrases stack in the same scene (frame 15 shows letters from 3+ words). Keep each shatter mounted until the scene ends.

### `<TitleCard>`
```ts
type TitleCardProps = {
  title: string;              // "DISCIPLINE" (rendered toLocaleUpperCase('tr-TR'))
  subtitle: string;           // "Day one, or one day."
  titleSize?: number;         // 250 (auto-fit: min(250, 0.69*1920 / (len*0.62)))
  underlineWaves?: number;    // 4.5
  embers?: number;            // 20
  seed: string;
};
```
Timeline (local frames): title A1 0–24 (scale 0.96→1) → underline A11 32–52 → subtitle A1 62–80 → hold → fade 20 f.

Wavy underline path. Measure the title width with `measureText()` from `@remotion/layout-utils`:
```ts
const wavyPath = (w: number, waves = 4.5, amp = 6, seed = "u") => {
  const steps = 48; let d = "";
  for (let i = 0; i <= steps; i++) {
    const t = i / steps, x = -0.025 * w + t * w * 1.05;
    const y = Math.sin(t * Math.PI * 2 * waves) * amp + (random(`${seed}${i}`) - .5) * 1.2; // hand wobble
    d += (i ? " L " : "M ") + x.toFixed(1) + " " + y.toFixed(1);
  }
  return d;
};
// <path d={...} stroke={C.underline} strokeWidth={9} strokeLinecap="round" fill="none"
//   strokeDasharray={len} strokeDashoffset={interpolate(f,[32,52],[len,0],{clamp, easing: Easing.inOut(Easing.quad)})}/>
// len from getLength(d) (@remotion/paths)
```

---

## 6. Rebuild checklist
- [ ] Load Comic Relief 400/700 with `latin-ext`. Fall back to Mali.
- [ ] One message at a time (plus DAY). White = story/lesson, red = voice/failure, gray = DAY.
- [ ] Narrator 70 px at y 50% (alone) or y ≈ 17% (over a scene). Voice 60 px next to the shadow head, 165 px when the shadow is giant. DAY 48 px bold at (86, 113).
- [ ] Every element uses the fade+blur in (18 f) and out (12 f). Hold uses `max(1.2, 0.8+0.3·words)` s.
- [ ] Inner voice is lowercase. Narrator is sentence case with a period. Ellipsis only on excuses.
- [ ] Shatter and jitter use `random(seed)` only, never `Math.random()`.

Sources: [Remotion – loadFont()](https://www.remotion.dev/docs/google-fonts/load-font) · [Remotion – font loading errors](https://www.remotion.dev/docs/troubleshooting/font-loading-errors) · [Remotion fonts](https://remotion.dev/docs/fonts) · package contents verified at `https://unpkg.com/@remotion/google-fonts@4.0.535/dist/esm/<Font>.mjs`.
