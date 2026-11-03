# DISCIPLINE — frame analysis, frames 200–299 (video-A, 640x360)

**Sampling.** The folder has 300 frames covering about 30 s, so this is about 10 fps (frame N ≈ N/10 s). The content agrees: "you're tired." is fully readable for about 2.5 s (25 samples), and the scene dips take about 0.4 s each, which fits normal editing speed. **Range 200–299 ≈ 0:20.0–0:29.9.** At 30 fps, frame N ≈ 3N (±2 frames, because each sample covers 3 video frames).
Coordinates below are in 640x360 pixels. I convert them to % of width (x) and % of height (y).

---

## 1. Shot list

| # | Frames (10fps) | ≈ time | Shot | Transition IN | Transition OUT | Duration |
|---|---|---|---|---|---|---|
| S1 (tail) | 200–216 | 20.0–21.6 s | DAY 1 couch: phone glow, shadow behind the couch's right arm | (before range) | **dip through black**, 217–219 out | 17 clean + 3 fading |
| T1 | 217–221 | 21.7–22.1 s | Dip to (near-)black. Couch fades 217→219, desk fades up 220→221+ | — | — | ≈5 samples (≈15 f @30) |
| S2 | 220–296 | 22.0–29.6 s | Desk at night: lamp, wall clock, books, shadow stands at the chair. DAY counter rolls 1→47 | dip from black, with an extra lamp-glow ramp up to ≈225 | **dip to black** starting 297 | ≈77 samples (≈7.7 s) |
| T2 | 297–299 (+) | 29.7–30 s | Fade to black, still running at 299 (299 ≈ 25–30 % brightness) | — | continues past my range | ≥3 samples |

- **No hard cuts in this range.** Both scene changes are **dips through black** (fade out about 3–4 samples, fade in about 2–5 samples). The frame never goes fully black: the darkest frames (219 and 220) still show faint shapes. It is probably a short fade-out plus fade-in that meet at about 5 % brightness, or a crossfade over a black layer (?).
- **How a DAY-counter scene change works:** the counter **stays on screen through the dip, still reading the old number.** "DAY 1" dims with the whole frame in 219–221 and is still "DAY 1" when the desk scene appears (220, 221). It then **rolls up** in the new scene. The counter does not cut to the new day. It counts up to it inside the new shot (see §2).
- The counter is dimmed by the dip as well. So the fade is applied to the whole composite, UI included, even though the camera push does **not** affect the counter (see §6).

## 2. Text events

Font: the rounded, handwritten, Comic-Sans-like font from the BRIEF. All inner-voice text is **lowercase with a final period or question mark**.

| Text | In (start → full) | Hold | Out (start → gone) | Animation | Color / glow | Position (center) | Size |
|---|---|---|---|---|---|---|---|
| `tomorrow.` (end of "skip the gym… tomorrow.") | before 200 → full at 200 | 200–211 | 212 → 215 (faint 214, ghost 215, gone 216) | **Constant upward drift**: baseline y≈142 (200) → 137 (207) → 135 (213), about 0.5 px per sample ≈ 0.15 % H per sample. Fade-out takes about 4 samples, with a slight blur/soften in the last 2 (?) | red ≈ #ff4a3a. Turns pinkish where it overlaps the shadow's red glow. Soft red glow | x≈423/640 = **66 %**, y≈39 % → 37.5 %. **Sits right on top of the shadow's face** (the eyes show through the letters) | cap height ≈ 11 px ≈ **3 % H**. Width ≈ 90 px ≈ 14 % W |
| `DAY 1` → `DAY 47` (counter) | already on screen | 200–299 | still on screen at 299, fading with the dip | **Number roll, ease-out**, and digits hard-swap (no fade between numbers): 221=1, 222=4, 223=14, 224=22, 225=29, 226=35, 227=39, 228=42, 229=44, 230=45, 231–233=46, 234=47 (locked). Deltas 3,10,8,7,6,4,3,2,1,1,0,0,1 → a fast ramp, then a slow crawl with a "stick" on 46 (3 samples) before 47 lands. About 13 samples = **1.3 s** | off-white/light gray ≈ #d8d8d8, no glow | top-left. Left edge x≈50 px = **7.8 % W**, y center ≈ 48 px = **13.3 % H**. Left-aligned (grows to the right) | cap height ≈ 9–10 px ≈ **2.7 % H** |
| `you're tired.` | 235 (≈25 % opacity, faint) → 236 (full) | 236–258 | 259 (≈70 %) → 260 (≈25 %) → gone 261 | **Fade in over 2 samples** (≈6 f @30) with a tiny upward drift: y≈110 (235) → 109 (240) → 102 (259) → 101 (260). That is about 8 px over 25 samples ≈ **0.09 % H per sample** while it holds. Fade-out also takes about 2 samples | red ≈ #ff4a3a, soft glow (smaller than the shadow's) | center x≈187 px = **29 % W**. Baseline y≈108 px = **30 % H**, **just above the shadow's head** (head top ≈ y120) | x-height ≈ 8 px, total height ≈ 14 px ≈ **3.9 % H**. Width ≈ 100 px ≈ 15.6 % W |
| (gap) | — | 261–264 | — | **4 samples (≈0.4 s) of silence** between the two lines | — | — | — |
| `why even try?` | 265 (partial: only "…en try?" visible, ≈40 % opacity) → 266 (full) | 266–292 | 293 (≈80 %) → 294 (≈50 %) → 295 (≈20 %, ghost) → gone 296 | Fade in over 1–2 samples. The left half shows up later in 265. Most likely this is because the faint red text is invisible against the red glow and black head of the shadow, not a real wipe (?). Upward drift while holding: y≈125 (266) → 117 (290) → 113 (294) → 110 (295) | red, **brighter and more saturated** than "you're tired." Stronger glow | center x≈199 px = **31 % W**. Baseline y≈125 px = **35 % H**. **Overlaps the top of the shadow's head and its eyes** (like `tomorrow.` did) | total height ≈ 17 px ≈ **4.7 % H** (**about 20 % bigger** than "you're tired."). Width ≈ 122 px ≈ 19 % W |

**Text rules found:**
- Inner-voice lines are **not** placed at a fixed screen spot. They anchor to the **shadow's head**: either on its face (`tomorrow.`, `why even try?`) or just above it (`you're tired.`).
- Each line **drifts upward slowly the whole time it is visible** (about 0.1–0.5 % H per 0.1 s) and fades out while still rising. It never pops or scales.
- **Escalation inside one scene:** the second line is bigger, brighter and lower (it sits on the face).
- Line rhythm: about **2.5 s on, 0.4 s off, about 3 s on.**

## 3. Character motion

**Couch (200–219):** seated far left on the couch. The near leg is crossed and lifted (knee at about 290,205, foot at 325,245). Both hands hold the phone at chin height (283,185). Eyes are heavy-lidded (a flat lid line over dot eyes, "bored") and the mouth is a short flat line. **I saw no movement in 20 samples**: no thumb scroll, no breathing, no blink (a blink shorter than 0.1 s could be missed (?)). The phone's blue glow (radius about 35 px around the head and phone) stays the same, then fades **slightly faster than the scene** in 218–219.

**Desk (220–299), held pose:** sitting on a chair (back post at x≈210), body leaning steeply forward at about 45°. **Both arms reach straight out along the desk** (hands at about 300,207 on an open book). The head is upright and rests on top of the arms. The near leg is bent and the foot is on the floor (280,250). He is already in this pose at the first frame (220), so the **"arms sliding forward" and "head dropping on desk" actions are NOT animated here**. The pose is the start state. Script and BRIEF say "asleep". In fact the **eyes are open but heavy**: half-closed lids, dot pupils, a flat or slightly down mouth = "exhausted, staring at the book".
- **Micro-motion:** a small head nod or heavy-lid moment at **249** (lids lower, head about 1–2 px lower, back at 250) and again at **278–279** (lids lower, head slightly down) (?). These read as "nodding off" beats about 3 s apart. There is no visible breathing loop at 10 fps (amplitude would be under 1 px if it exists).
- **Expression stays the same** through the whole desk scene (tired, half-lidded). He never reacts to the shadow, which is the point: the voice is internal.

## 4. Inner-voice shadow

**Couch (200–219):** stands behind the couch's right end (x≈420, feet at the floor line y≈250). Its silhouette is taller than the couch back. **Its near arm is raised, bent, with the hand by its head (≈385,150), like a whispering hand next to the mouth.** The face shows **closed-eye smile arcs plus a wide smile** through 200–213. At **214–216** the face changes, just as `tomorrow.` fades: **red glowing slit eyes with angled brows and a wide grin**. The "mask" appears once the words are gone. The glow is a **red outer glow about 8–10 px** plus a **thin bright red rim line**, about the same strength across 200–216. It fades with the dip in 217–219. Idle sway: the head drifts about 1–2 px (?), which is basically still.

**Desk entrance — rising from the floor, NEW (not in the BRIEF):**
| Frame | State |
|---|---|
| 221–222 | A thin **red glowing arc on the floor line** at x≈165 (a "puddle" or horizon glow). No body yet |
| 223 | the arc gets a little taller |
| 224 | a **dome** (top of the head) rises out of the floor. Red rim, black fill |
| 225 | whole head above the floor. **Smile already visible** (wide red curve) |
| 226 | head plus shoulders |
| 227 | torso. Arm reaching toward the chair |
| 228 | almost full height. Hand nearly on the chair back |
| 229 | full body. **Hand on the chair back** (≈205,195) |
| 230–232 | keeps rising/stretching: head top 140 → 133 → 127 → 120 (**settles about 2–3 samples after reaching full height**, a soft overshoot or ease-out with no bounce back) |
| 233+ | stands still. Final head top ≈ y120, feet on the floor ≈ y256 → height ≈ 136 px ≈ **38 % H**. The seated hero's head top is ≈ y172 |

- The rise (221–232, ≈1.2 s) is **synchronized with the DAY counter roll** (221–234). Shadow "grows" = days pass.
- **Hand on chair:** from 229 to the end. The arm is bent with the hand resting on top of the chair's back post. This is a **possessive "I'm with you" pose**. There is no stroking motion.
- **Face over time:** 225–232 closed-eye smile arcs plus a grin. 233–241 eyes open as **thin red slits** under angled brows (eyes and mouth glow). **From 242 on**, the eye slits are **brighter, almost white-hot red**. From about 260 on, a stronger grin and brows (more menacing) come with `why even try?`.
- **Glow intensity:** 225–259 the rim and outer glow are medium (≈8 px). **From ≈260 the glow gets brighter and wider (≈10–12 px, more saturated)**, right as the second, harsher line arrives. Escalation is shown through glow, not size.
- **Lean / drift:** 260–299 the head shifts about 5–8 px left and slightly down. Most of that is the camera push-in (§6). A small extra lean toward the hero of about 2 px is possible (?).
- **Exit:** none in this range. It is still there when the fade to black starts (297–299). Its glow fades with the scene, and the red rim is still faintly visible at 299.

## 5. Props and environment

- **Couch:** dark gray-purple fill (≈#3a3845), light gray outline about 1.5 px, rounded arms, thin legs. A single floor line runs across the whole frame at y≈252 (70 % H).
- **Desk scene layout** (at 230): wall clock center (348,92) = **54 % W / 26 % H**, radius ≈ 22 px (6 % H), white outline, dark face, **two white hands**. Desk top y≈212 from x≈255 to 475, thin plank, two legs. Chair: just a thin vertical back post at x≈210 plus a seat. **Desk lamp** at the right: gray outline, arm, and a head at (415,155) tilted down-left toward the hero. **Book stack** under the lamp, top to bottom: **olive/khaki ≈ #7a7a45, blue ≈ #3f5f9a, red ≈ #9a3a3a**, each about 8 px tall with rounded ends. **Open book/papers** on the desk in front of the hero's hands: two pale flat shapes at x 305–380.
- **Lamp light:** this is **NOT a hard cone**. It is a **soft warm radial gradient** (amber ≈ #c89a5a at about 25–35 % alpha → transparent), centered about (360,180), radius ≈ 80–90 px. It covers the desk, the hero's hands and the book, and leaks slightly onto the floor below the desk. **It builds up after the dip:** about 5 % at 220, rising to a steady level by about 224–225. That is about 4 samples, slower than the scene fade-in. **No flicker** was found in 225–296.
- **Wall clock — time-lapse spin:** the hands are at a different, seemingly **random angle in every sample from 220 to 296**, both during the day roll and **after the counter has locked on 47**. That is strong aliasing: at 10 fps the minute hand moves ≥90° per sample, so it spins ≥1 turn per 0.4 s (?). The direction cannot be judged from the samples. In practice it means "time keeps passing / nights blur together". A rebuild should use a fast continuous spin, not a frame-random angle, so it reads well at 30 fps.
- **Letterbox:** solid black bars **top y 0–≈30 (8.5 % H) and bottom y ≈328–360 (9 % H)** in both scenes. The room background in between is very dark gray (≈#121212), and the **floor area below the floor line is a bit lighter** (≈#161616).
- **Vignette:** a soft radial darkening toward the corners in both scenes. Faint **vertical lines near x≈55 and x≈590** (the edges of a darker side vignette, or wall/room corners (?)) show best in the darkened frames 219 and 299.
- **Frame 299 darkening = YES, a fade-out to black** (§1, T2). 297 ≈ 85 %, 298 ≈ 55 %, 299 ≈ 25 % brightness. It continues into the next analyst's range.

## 6. Camera

- **Couch tail (200–219):** static. Floor line, couch and counter don't move (±1 px).
- **Desk (220–299): slow continuous push-in (zoom).** Measurements:
  - shadow's left edge x 135 (230) → 129 (260) → 122 (290)
  - desk's right edge / leg x 470 (230) → 478 (260) → 482 (290)
  - floor line y 256 (230) → 260 (262) → 262 (290)
  - clock center y 92 (230) → 89 (260) → 87 (290)
  - Horizontal span 335 → 360 px ≈ **scale 1.00 → ≈1.075 over ≈60 samples (6 s)**. Linear, with no visible ease (?). Zoom center ≈ (300–310, 180–190) = **≈48 % W, 52 % H** (around the hero's hands and the lamp glow). It probably starts as the scene fades in. At 220–229 the change is too small to measure.
  - **The DAY counter does not scale or move** (it stays at x≈50, y≈48 from 221 to 299). It sits on a screen-space UI layer above the camera.
  - **Letterbox bars do not move** (UI layer).
- No pan, shake or rotation.

## 7. Pacing stats (10 fps samples → ×3 for 30 fps frames)

| Segment | Samples | Seconds |
|---|---|---|
| Couch tail with `tomorrow.` | 200–215 | 1.6 s (+ the earlier part, outside my range) |
| Couch hold without text (menace face) | 214–216 | 0.3 s |
| Dip couch→desk | 217–221 | ≈0.5 s |
| Day roll + shadow rise | 221–234 | 1.3 s |
| Settle (no text) | 232–234 | 0.3 s |
| `you're tired.` | 235–260 | 2.6 s |
| Gap | 261–264 | 0.4 s |
| `why even try?` | 265–295 | 3.1 s |
| Hold without text | 296 | 0.1 s |
| Fade out | 297–(≥299) | ≥0.3 s |

- The desk scene lasts about 7.7 s and has 2 voice lines. That is about **1 line per 3 s**, each held about 2.5–3 s. The counter roll ends 0.1 s before the first line appears.
- The visual rhythm is: **establish (with motion: counter, rise, clock) → settle → line → breath → harsher line → fade**.

## 8. NEW / MISSED DETAILS vs BRIEF and script

1. **DAY 25 is not a separate shot.** One continuous desk shot rolls the counter **1 → 47** with an ease-out curve (1,4,14,22,29,35,39,42,44,45,46,46,46,47). The script's "DAY 25 asleep / DAY 47 shadow appears" is really a single "time passes" roll, and 25 is never shown (22 → 29).
2. **The counter carries over across the dip:** the new scene opens still showing the **old day (DAY 1)**, then counts up. This is a reusable "time-lapse into scene" device.
3. **The shadow rises out of the floor** as a glowing red arc → dome → head → body, in step with the day roll. The BRIEF only says "appears behind". Here it **grows out of the ground like a puddle** as days pass.
4. **There are two voice lines at the desk: `you're tired.` then `why even try?`** (both lowercase). The BRIEF's frame 7 only mentions "you're tired." The script has "You're tired. Why even try?" but as one line. On screen they are separate events with a 0.4 s gap, and the second is **bigger and brighter** and sits **on the face**.
5. **Text anchors to the shadow's head and drifts upward** the whole time, then fades out mid-rise. There is no typewriter, no per-word reveal and no scale pop. The "faint" text in reference frame 7 is just a fade-in or fade-out sample, **not a permanent whisper style**: at full opacity, "you're tired." is solid red.
6. **The shadow's face changes from closed-eye smile arcs to glowing slit eyes** once its line lands, or once its words fade on the couch. **The glow brightens on the second, harsher line.** Escalation is done with face plus glow.
7. **Hand on the chair** (the possessive pose) from the moment it reaches full height. On the couch, the **raised hand is at its mouth** (a whisper gesture).
8. **The hero is NOT asleep and NOT animated slumping.** He holds a pre-posed "collapsed over the book, eyes open but heavy" pose, with 2 tiny nod-off beats (249, 278–279 (?)). He never reacts to the shadow.
9. **The clock spins nonstop** (time-lapse) for the whole desk scene, even after the counter stops. It means the night is slipping away.
10. **A slow 7–8 % push-in** over the desk scene. The UI counter is excluded from it.
11. **Lamp light is a soft warm radial pool, not a cone.** It ramps up after the dip (lights coming on). No flicker. The desk book stack is olive/blue/red. The red book is a subtle accent echo (?).
12. **All scene changes here are dips through black** (about 0.4 s out, 0.4 s in), including the fade-out at the end of the desk scene. The UI counter fades with the frame.
13. **Letterbox bars of about 8.5–9 % top and bottom** (≈2.16:1 visible area) in both scenes. The floor zone under the floor line is slightly lighter than the wall.
14. The couch line is `tomorrow.` (lowercase, with a period), written on top of the shadow's face. The phone's blue glow **fades slightly before the scene**.
15. The phone glow is a plain radial gradient, and the hero shows no scroll motion in the last 2 s of the couch shot.

## 9. Rebuild notes (Remotion, 30 fps; f30 = 3 × sample index, so the range starts at f600)

```
// Global timeline, absolute frames @30fps
COUCH_TEXT_tomorrow   : visible ..→636, fadeOut 636→648 (opacity 1→0), translateY -0.15%H per 3f (≈ -1.5px/10f at 1080p)
COUCH_SHADOW_FACE     : smileArcs ..→642, slitEyes 642→ (cut or 3f blend)
DIP_1                 : sceneOpacity 1→0  f648→660 (easeIn), 0→1 f660→672 (easeOut). UI included.
LAMP_GLOW             : opacity 0→1  f660→675 (lags the scene by ~3–6f)
DAY_COUNTER           : f663→702: value = round(interpolate(f,[663,702],[1,47], easeOutCubic/Quart)); hard swap digits
                        (check the sequence 1,4,14,22,29,35,39,42,44,45,46,46,46,47 — easeOutQuart-ish with late hold)
SHADOW_RISE           : translateY from +100%bodyH (below floor, masked by floor line) → 0, f663→696, easeOutCubic;
                        red floor-arc glow visible from f663 (mask: clip everything below floor y)
                        hand-on-chair IK target locked from f687
SHADOW_FACE           : arcs f675→699, slits f699→, eyeGlow boost f726→, glowRadius 8→12 (×1.5) & brighter f780→
CLOCK                 : minuteHand rotate += 12–20°/frame (≥1 rev/0.6s), hourHand /12, f660→end
CAMERA_PUSH           : scale 1.00→1.075 linear f660→900+, origin (48%W, 52%H); UI layer (counter, letterbox) outside
TEXT "you're tired."  : fadeIn f705→708 (or 0→1 over 6f), hold →777, fadeOut 777→783; y drift -8px@640 (-2.2%H) over 75f
                        anchor: center x = shadowHead.x + ~2%W, baseline = shadowHead.top − ~3%H
GAP                   : f783→795
TEXT "why even try?"  : fadeIn f795→798, hold →879, fadeOut 879→888; y drift -15px@640 (-4%H) over 90f;
                        fontSize ×1.2 vs previous, brighter red + bigger glow; baseline over the shadow's eyes
HERO_NOD              : head rotate +2–3° & lids 60%→85% closed at f747±3 and f834→840, ease back
DIP_2                 : sceneOpacity 1→0 f888→~903 (continues beyond the range)
```

Sizes at 1920x1080: DAY counter cap height ≈ 29 px, left 150 px, center y 144 px. Voice text height 42 px ("you're tired.") / 51 px ("why even try?"). Letterbox bars ≈ 92 px top and 97 px bottom. Floor line y ≈ 756 (couch) / 768 (desk, pre-push). Shadow height ≈ 410 px. Clock radius ≈ 66 px at (1044, 276). Lamp glow radius ≈ 250 px.

Reusable components implied: `<DayCounterRoll from to ease holdOnLast/>`, `<ShadowRiseFromFloor/>` (floor-masked), `<VoiceLine anchorTo="shadowHead" drift fade escalate/>`, `<TimelapseClock/>`, `<DipToBlack includeUI/>`, `<CameraPush excludeUI/>`, `<LampPool/>`.
