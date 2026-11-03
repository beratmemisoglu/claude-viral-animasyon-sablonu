# DISCIPLINE — frame analysis, video-A frames 100–199

Source: `research/frames/video-A/videoplayback_100.jpg … _199.jpg` (640x360). Every frame was read in order. Measurements come from the frames themselves plus pixel scans (Pillow: luminance, edge positions, color samples, glow intensity). Coordinates are in 640x360 frame pixels. "%" values are of the full 640x360 frame unless marked "active", which means the 640x296 picture inside the letterbox.

**Sampling rate: 10 fps.** Frame N is at about N/10 s. Evidence: the couch/DAY 1 scene starts at frame 140 (14.0 s), and the script puts that scene at 0:13. The caption "skip the gym." is fully visible for about 1.7 s, which is a natural reading time. The clock fast-forward takes 1.3 s. All of this fits 10 fps. **At 30 fps, frame = N × 3** (90 frames ≈ 3 s per 30 frames here). My range covers about 10.0 s to 20.0 s.

---

## 0. Global facts measured in this range (apply to the whole film)
- **Letterbox bars exist and are pure black.** Rows 0–31 and 328–359 are luminance 0. The picture area is 640x296, about **2.16:1 (≈ 2.2:1 "scope")**. At 1920x1080 the bars are **96 px top and 96 px bottom**, leaving an 888 px tall picture. The picture background is **#0B0B0B** (11,11,11), and some corners are #080808, which comes from a very soft vignette.
- **The font is Comic Sans MS**, or something that looks identical: "j", "g", "y" and "a" match it exactly. It is not a custom hand-lettered font.
- **Red caption color is ≈ #FF5040** (255,81,61). The shadow's speech is ≈ #F94E46. The text has a faint glow, about 2–3 px at 640 wide.
- **DAY counter color is light gray ≈ #BBBBBB** (187), not white.
- Hero face fill is ≈ #DBD7CB. Blanket is ≈ #272D3D (dark navy). The moon disk is ≈ #A3A7B2. Clock digits are ≈ #D04D43, which is dimmer than the caption red.

---

## 1. Shot list

| # | Frames (10 fps) | 30 fps | Content | Camera |
|---|---|---|---|---|
| A1 | ≤100–116 | ≤300–348 | Bedroom wide shot. Sleeping, 5:00, Z's, caption "just 5 more minutes..." | slow push-in (continues from before 100) |
| A2 | 117–129 | 351–387 | Same shot. Clock fast-forwards 5:00 → 8:18. Face does not change. | push-in continues |
| A3 | 130–138 | 390–414 | Same shot. 8:47, hard face swap to shock, sweat drop, "again." | push-in continues (ends at ~133) |
| T1 | 138–147 | 414–441 | **Dip to black.** Fast out, slow in. | — |
| B1 | 140–199+ (continues) | 420–597+ | DAY 1 couch. Phone glow. The shadow rises behind the couch arm and says "skip the gym." then "tomorrow." | slow push-in, faster than A |

**There is no cut inside A1–A3.** The clock fast-forward and the panic all happen in one continuous shot. The beats are separated only by captions and the clock.

**T1 transition, measured mean luminance:** 137 = 14.28 → 138 = 11.87 → 139 = 4.31 → **140 = 1.00 (minimum)** → 141 = 2.40 → 142 = 3.96 → 143 = 5.53 → 144 = 7.48 → 145 = 9.46 → 146 = 11.78 → 147 = 13.15 (plateau).
- **Fade-out is about 2.5 frames** (137→140, ≈0.25 s, ≈8 frames at 30 fps).
- **Fade-in is about 7 frames** (140→147, ≈0.7 s, ≈21 frames at 30 fps). It is close to linear.
- At frame 140 the couch scene is already faintly visible. The transition is a dip through black where the new shot starts rising as soon as the old one reaches black, with no black hold.

---

## 2. Text events

| Text | In (start) | Fully visible | Out start → gone | Entry | Exit | Position (center) | Size |
|---|---|---|---|---|---|---|---|
| `just 5 more minutes` → `..` → `...` | before 100 (?) | 102 (with "...") | 113 → 116 | **Ellipsis is typed one dot at a time**: 100 = no dots, 101 = "..", 102 = "...". That is about 2 dots per frame (≈1 dot per 1.5 frames at 30 fps). The word part was typed or faded before frame 100 (?) | Opacity fade, about 3 frames: 113 ≈ 65%, 114 ≈ 25%, 115 ≈ 12% (looks slightly blurred or ghosted), 116 = 0 | x ≈ 313/640 = **49%**, y ≈ 101/360 = **28%** (active ≈ 23%) | Line height ≈ 20 px = **5.6% of frame height** (6.8% of active). Width 220→420 = 31% of width |
| `again.` | 132 | 133 | (dies with the scene fade, 138–140) | **Pop: fade plus scale-down.** At 132 it is about 40% opacity and **≈1.18× size**; at 133 it is 100% at 1.0×. So it settles in about 1 frame (≈3 frames at 30 fps), with no overshoot visible | Fades out with the whole picture during the dip, 138 → 140 | x ≈ 332/640 = **52%**, y ≈ 101 = **28%**, same baseline as "just 5 more minutes" | same size as above |
| `DAY 1` | 145 | 147 | not out in this range | **Plain opacity fade, about 2–3 frames** (145 ≈ 30%, 146 ≈ 70%, 147 = 100%). It starts **5 frames after the shot fades in** (the scene starts rising at 140). No pop, no typing, no movement | — | Left edge x ≈ 50 (**7.8%**), center y ≈ 49 (**13.6%**). It sits just under the top bar (≈ 17 px below it, ≈ 5% of active height) | Cap height ≈ 10 px = **2.8% of frame height**. Smaller than the captions. Gray #BBB, bold |
| `skip the gym.` (shadow) | 165 | 167 | 183 → 187 | Opacity fade, about 2 frames (165 ≈ 25% ghost, 166 ≈ 85%, 167 = 100%). No scale | Fade, about 3–4 frames (183 ≈ 85%, 184 ≈ 55%, 185 ≈ 45%, 186 ≈ 15%, 187 = 0) | x ≈ 420 = **66%**, y ≈ 126 = **35%**. **Drawn over the top of the shadow's head**, crossing its forehead or eyes (see section 4) | ≈ 14 px tall = **3.9% of frame height**. Smaller than narration captions. Width ≈ 96 px = 15% of width |
| `tomorrow.` (shadow) | 191 | 192 | still on at 199 (and at 203) | Fade, about 1–2 frames | — | x ≈ 422 = **66%**, y ≈ 143 = **40%**. **Lower than "skip the gym." by about 17 px (4.7% of height)**. It sits right across the shadow's eyes | same as above |

Notes:
- "just 5 more minutes..." and "again." are **two separate captions** at the same screen spot. Between them there is a gap of 16 frames (1.6 s) with no text, during which the clock fast-forwards. The script's single line "just 5 more minutes... again." is wrong.
- The shadow's line is also **two separate captions**: "skip the gym." (1.7 s fully visible) then a gap of 4 frames (187–190), then "tomorrow.". The text is all lowercase with a period. The script's "Skip the gym... Tomorrow." is wrong on case and punctuation.
- The bedroom captions are in **screen space**: during the push-in the caption's left x stays at 220 while the scene grows. The shadow's speech stays tied to the head: its x drifts 374 → 372 during the push-in (≈ world space, or it is simply placed there (?)).
- No caption has per-word animation, blur-in or a typewriter effect, except the ellipsis dots.

---

## 3. Character motion breakdown

### 3a. Bedroom (100–138)
- **Sleeping pose, 100–129.** The body is fully covered by the navy blanket. Only a round head (≈ 38 px tall = 10.5% of frame height) shows on a gray pillow. **Nothing moves for 30 frames (3 s): no breathing rise in the blanket, no head bob.** The only motion is the camera push and the Z's.
  - Sleeping face: **flat straight brows**, **closed eyes drawn as downward arcs** (‿ ‿, content-sleep look), **small smile**. It looks smug and comfortable, not tired.
- **Z particles, 100–126.** Small gray Z's (≈ #8A8A8A). They spawn at about (262, 168), just above and right of the head. Each one **rises about 2–3 px per frame and drifts about +1 px per frame to the right**, and gets smaller and fainter as it rises. Two or three are on screen at once, spaced about 13 px apart vertically (lowest about 7 px tall, highest about 4 px).
  - **Spawning stops when the fast-forward starts (~117).** The last Z keeps rising (y 150 → 133) and fades out by **126**. So the Z's are a looping emitter that stops, with the last particle finishing its life.
- **Wake / shock: hard swap at frame 130**, on the same frame the clock shows 8:47. There are **0 in-between frames, no anticipation, no squash, and the body does not move.** The face swaps from sleeping to:
  - **Raised, angled worried brows** (outer ends lower, arched)
  - **Round dot eyes with a white catch-light**
  - **Small round "o" mouth**
  - **Tiny light-blue sweat drop** at the upper right of the head (≈ 3x5 px at 640 wide, ≈ #9CC3E6). It appears on the same frame 130 and holds still until 138. It does not drip or slide.
- **Frames 130–138: the shock face holds still for 9 frames (0.9 s).** He does not sit up or flail. **Within frames 100–138, the "panic" is only the face swap plus the sweat drop.** The brief's "character panics" is a static reaction pose here.

### 3b. Couch, DAY 1 (140–199)
- **Pose, held the whole time.** He sits slumped on the left-center of a 3-seat couch. Head center x ≈ 270 (42%).
  - The **body is a bean shape** with the head merged into the torso and tilted forward and left.
  - **Near leg** is a long straight cream tube, crossed diagonally down-right to the floor (foot at ≈ 320, 240).
  - **Far leg** is shorter and darker gray, hanging straight down.
  - **Near arm** is bent into a sharp V: the upper arm drops down the chest, the forearm comes back up to the phone. The phone is held **right in front of the chin and mouth**, tilted about 20°.
  - The arm has an **outline** (dark stroke). The body's own outline is barely visible because of the phone light.
- **Face (bored, phone-zombie):**
  - **Flat brows set close to the eyes.**
  - **Heavy half-closed eyelids** drawn as horizontal lines with small pupils showing below.
  - **Blue tint under the eyes**, which is the phone light reflecting.
  - **No mouth visible**, because the phone covers it.
- **Blink:** one blink at **frame 177**, where the eyes are fully closed for one 10 fps frame (≈ 2–3 frames at 30 fps). It is the only blink in 60 frames. Rule of thumb: 1 blink per 4–6 s (?).
- **Phone and thumb:** across the sampled frames (145 / 155 / 165 / 172 / 175) the phone angle changes by only about 2–4°. **The thumb scroll is not visible at this resolution.** Treat it as a tiny phone wobble plus screen-light flicker (section 5) rather than a visible thumb swipe (?).
- **He does not react to the shadow at all.** There is no head turn, no eye shift and no change of expression. This matches the script's "does not object".

---

## 4. Inner-voice shadow (148–199)

### Before the rise
The shadow is **already there from the first frame of the shot (141)**. All you see is a **small red glow blob on the floor behind the couch's right leg** (≈ x 430, y 230). It is hidden or crouching behind the couch. Glow intensity at x 445–470 is about 0 through frame 148.

### Rise
The shadow comes up from behind the couch's **right arm**, not from behind the seat back.
- Head top y by frame:

  | Frame | 150 | 153 | 156 | 159 | 162 | 165 |
  |---|---|---|---|---|---|---|
  | Head top y | ≈ 207 (glow only) | ≈ 152 | ≈ 133 | ≈ 125 | ≈ 122 | ≈ 117 (settled) |

- So it rises about **90 px (25% of frame height) in about 15 frames (1.5 s) with a strong ease-out.** Most of the travel happens in 150–156.
- The glow intensity follows the same curve: 149 = 1.4 → 151 = 9.5 → 153 = 19 → 156 = 27 → 160 = 31 → 164 = 33. After that it stays flat at **33–35.5 through 199**.
- **There is no separate "bloom" flash.** The glow is a fixed property of the silhouette that rises with it.

### Silhouette
- **Pure black (#000–#050505) humanoid**: big round head about **1.1× the hero's head size**, sloped shoulders, standing.
- It **leans over the couch's right arm**. Its near arm is **raised, with a fist or hand above the couch back**, a "leaning-in, hand-up" gesture. From 156 to 199 this arm **stays up and holds still** (no wave cycle).
- The far side of the body and the legs show below the couch arm on the right.
- **Glow**: a soft blurred red outer glow, not a stroke. About **8–10 px at 640 wide (≈ 25–30 px at 1080p)**. Its color goes from ≈ **#B6391D** (182,57,29) at the edge to transparent, so it is more orange-red than the text red. The glow also spills onto the couch arm's outline.
- **No measurable pulsing in 150–199.** Frame-to-frame change is ±1 on a scale of 35, which is JPEG noise. A flicker or pulse, if there is one, would be under 3%.

### Face, which changes while it "talks"
| Frames | Face |
|---|---|
| 153–156 | **Smile appears first**: a thin red upward arc while the head is still half hidden. No eyes yet. |
| 159 | Eyes start to show as dim red dashes, about 30–40%. The smile dims. |
| **162–165** | **Eyes fully lit**: two short glowing red **slanted dashes, tilted down toward the center** (angry, smug "‾\ /‾" look). Mouth gone. This is the "ignite" moment, about 3 frames (159→162). |
| 168 | Faint smile returns, about 30%, **one frame after "skip the gym." becomes fully visible**. |
| 171–186 | **Full smile**, a thin red arc (≈ 18 px wide at 640) under the eyes. The eyes stay slanted. |
| 189 | The smile fades out, about 50%. |
| 192–199 | The eyes change to **arched "⌒ ⌒" shapes** (a sly or sinister squint) while "tomorrow." covers them. The mouth is not visible, either hidden behind the text or gone (?). |

Summary: the eyes stay on the whole time; the **smile switches on while a line is spoken and off between lines**; the eye shape changes between lines.

### Where the red text sits relative to the head
- **"skip the gym." covers the head between the top of the skull and the eyes.** The text center is about 8 px left of the head center, and the line crosses the forehead.
- **"tomorrow." is lower, crossing the eyes.**
- The text is not a speech bubble and is not above the head. It is **overlaid on the head**, as if the words come out of the face.
- The text is drawn **on top** of the shadow's glow.

---

## 5. Props and environment animation
- **Clock fast-forward: discrete digit cuts, one new reading per frame (accelerating), not rolling digits.**

  | Frame | 117 | 118 | 119 | 120 | 121 | 122 | 123 | 124 | 125 | 126 | 127 | 128 | 129 | **130** |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Clock | 5:00 | 5:02 | 5:05 | 5:10 | 5:17 | 5:26 | 5:38 | 5:54 | 6:14 | 6:37 | 7:06 | 7:39 | 8:18 | **8:47 (holds)** |

  - Steps in minutes: **+2, +3, +5, +7, +9, +12, +16, +20, +23, +29, +33, +39, then +29.** That is roughly quadratic acceleration with a slight slow-down on the last step into 8:47.
  - It takes **13 frames (1.3 s)**, then 8:47 holds until the end of the shot.
  - Digits are a seven-segment-style red font (the "1" is drawn as segments: "5:10", "8:18"). The colon stays on, no blinking.
  - The clock is in a dark rounded housing with a gray outline on top of the nightstand. It has **no glow halo**: the digits are flat red.
- **The window does not change.** At 8:47 the window still shows **the moon and night sky** (moon at ≈ 577, 68), the same as at 5:00. There is also a **faint diagonal light beam** from the window going down-left across the wall, and it stays constant.
  - **There is no daylight change.** This is a continuity shortcut. The rebuild can either copy it or add a dawn tint; copying is cheaper and matches.
- **Phone light:**
  - A **blue radial halo around the hero's head** (center ≈ 285, 160, radius ≈ 40 px = 11% of frame height). Blue-minus-red index is about 10.
  - It **flickers irregularly frame to frame by about ±10%** (9.4 ↔ 12.3) with no rhythm, which reads as screen content changing.
  - It also rises slowly (≈10 → 13.4 over 145 → 199), partly because of the push-in (?).
  - **Blue light hits the face**: lower eyelids, the cheek near the phone, and the top edge of the head.
  - The phone screen is a flat light-blue rounded rectangle (≈ #6FA0E0) with a darker outline.
- **Couch:** a dark slate 3-seat sofa (≈ #2E2C36 fill) with a light-gray wobbly outline, a seat cushion line, thin metal legs and a single floor line across the full width. There is no other furniture: **the couch scene has no window, lamp or wall detail at all.**
- **Vignette:** soft and constant (center #0B0B0B, corners #080808). It does not move or pulse.

---

## 6. Camera
- **Bedroom (100–138): slow constant push-in.**
  - Distance from nightstand left edge to bed right edge: 370 px at frame 100 → 384 px at frame 130. That is **+3.8% over 30 frames (≈ 1.25% per second)**, linear.
  - It flattens out after about 130 (positions 130–138 are nearly fixed: 107 / 490 → 107 / 491).
  - The zoom center is about x 300 (47%), so the push is centered on the bed and headboard, slightly left of frame center.
  - The push already started before frame 100 (?).
- **Couch (147–199): faster push-in.**
  - Couch left edge 192 → 182. Floor line y 242 → 248.
  - That is about **+8% over 52 frames (≈ 1.5% per second)**, linear with no ease.
  - The zoom center is about (330, 170), between the hero and the shadow, slightly right of center.
- **No shake, no pan, no rack focus.** Both shots are static wide shots with a slow "breathing" zoom.

---

## 7. Pacing stats (frames 100–199 = 10 s)
- **Shots:** 2 (one transition). Average shot length in this window: bedroom about ≥ 4 s (with earlier footage), couch ≥ 6 s.
- **Captions:**
  - 4 caption events: "just 5 more minutes...", "again.", "skip the gym.", "tomorrow." Plus 1 title-card counter: DAY 1.
  - Fully visible durations: "just 5 more minutes..." ≥ 1.2 s (100–112). "again." ≈ 0.5 s before the fade. "skip the gym." 1.7 s. "tomorrow." ≥ 0.8 s.
  - **Gaps with no caption:** 1.6 s (clock run), 0.4 s (between the shadow's lines).
- **Beat timing:**
  - Clock run: 1.3 s.
  - Shock hold: 0.9 s, then fade.
  - New scene: DAY 1 at +0.5 s.
  - Shadow starts rising at +0.8 s, fully up at +2.5 s.
  - First line at +2.5 s (165).
  - Second line at +5.1 s (191).
- **Hold-heavy timing:** characters hold still most of the time. All of the "life" comes from particles (Z's), the clock, the glow, captions, blinks and the camera drift.

---

## 8. NEW / MISSED DETAILS (vs. BRIEF.md and script)
1. **Letterbox:** 32/360 px black bars top and bottom, giving a 2.16:1 picture. The brief only says "letterbox-ish top bar". **Both bars are present and pure #000**, and the picture background is #0B0B0B.
2. **The caption font is literally Comic Sans MS.** The brief only says "Comic-Sans-like".
3. **"just 5 more minutes..." and "again." are two separate captions**, 1.6 s apart, at the same spot. The script merges them. **"again." pops in with a scale-down from about 1.18× to 1.0×**, while the first caption only has typed ellipsis dots.
4. **The ellipsis is typed** (". . ." one dot at a time), which is a small but distinctive effect.
5. **The shadow's lines are "skip the gym." and "tomorrow."**: lowercase, each with a period, as **two captions** with a 0.4 s gap. The second caption sits about 17 px lower. The script writes "Skip the gym... Tomorrow." as one line.
6. **The shadow's text is overlaid on its head** (forehead, then eyes), not floating above it. The brief does not say where the text goes.
7. **The shadow does not "approach the shoulder"** as the script says. It **rises straight up from behind the couch's right arm** (ease-out, about 1.5 s) and then **stays planted**, leaning over the arm with one hand raised. It is at the opposite end of the couch from the hero, about 150 px (23% of width) away.
8. **The shadow is in the shot from frame 1 as a glow blob on the floor** behind the couch, before it rises. This foreshadows it.
9. **The glow is a soft blurred outer glow, orange-red (#B6391D-ish), not an outline stroke.** The brief says "red-outlined". There is **no pulsing.**
10. **The shadow's face is animated in a set order:** smile first (while it peeks), then the eyes ignite (3 frames), the smile turns on while it speaks, and the eye shape changes to sly arcs for the second line.
11. **Shock wake is a 0-in-between pose swap with no body motion**, plus a sweat drop that appears on the same frame. There is no sitting up or flailing in this range, and the "panic" is face-only. The sleeping face is **content and smiling**, not "sleepy".
12. **The clock fast-forward is 13 discrete accelerating readings** (+2…+39 minutes per frame), not a spinning or rolling effect, ending on a 29-minute step into 8:47.
13. **The window still shows the moon at 8:47.** There is no daylight change.
14. **Z's stop spawning the moment the fast-forward starts**, and the last one floats away. Z's are gray, not white.
15. **DAY 1 fades in 0.5 s after the shot**, as a separate layer. It is light gray (#BBB) and small (2.8% of height). The brief says gray, which is correct; the script says white, which is wrong.
16. **Dip-to-black is asymmetric:** about 0.25 s out and about 0.7 s in, with no black hold.
17. **Both shots have a slow linear push-in**: about 1.25% per second in the bedroom and about 1.5% per second on the couch.
18. **The couch set is minimal**: no window, wall or lamp. Only the couch, the floor line, the blue halo and the shadow.
19. **The phone covers the hero's mouth.** The eyes are half-lidded with **blue under-eye light**. There is one blink in 6 s. **The hero never reacts to the shadow.**
20. Captions use **two text sizes**: narration/info captions ≈ 5.6% of height, the shadow's speech ≈ 3.9%, DAY counter ≈ 2.8% cap height.

---

## 9. Rebuild notes (Remotion, 30 fps; f30 = f10 × 3)

### Composition and framing
- Composition 1920x1080. Draw letterbox `<rect>`s 0–96 and 984–1080 in #000 on top of everything.
- Scene background #0B0B0B, plus a radial vignette to #080808.

### Bedroom shot (local f30 = 0 at global 300)
- **Camera:** `scale = interpolate(f, [0, 90], [1, 1.038], {extrapolateRight:'clamp'})`, with transform-origin at about (47% x, 55% y).
- **Captions:** a `<Caption>` in screen space (outside the camera group). Font `"Comic Sans MS", "Comic Neue", cursive`, red `#FF5040`, size ≈ 60 px (5.6% of 1080), center (49%, 28%).
  - `text-shadow`/SVG glow: `feGaussianBlur stdDeviation≈3`, opacity 0.5.
- **Ellipsis typing:** reveal one dot every 1–2 frames (f30 300→306).
- **Caption fade-out:** f30 339→348, opacity 1→0 with `Easing.in(Easing.quad)`. Optional 1–2 px blur on exit.
- **Z emitter:** spawn every ~12 f30 at (785, 504) in 1080p space. Per particle over its life (~45 f30):
  - y −8 px/f30, x +3 px/f30
  - scale 1 → 0.55, opacity 0.8 → 0
  - Stop spawning at f30 351; the last particle dies by about f30 378.
- **Clock:** `const readings = ['5:00','5:02','5:05','5:10','5:17','5:26','5:38','5:54','6:14','6:37','7:06','7:39','8:18','8:47']`. Index = `Math.min(13, Math.floor((f30-351)/3))` starting at global f30 351, so 8:47 lands at **f30 390**. Use a seven-segment SVG font, fill #D04D43, no glow.
- **Face swap at f30 390:** `<HeroFace expression={f30>=390?'shock':'sleepContent'} />`, with no tween.
  - Sweat drop mounts on the same frame, light blue #9CC3E6, at the head's upper right, about 10x15 px at 1080p.
  - *Optional upgrade (not in the source): a 2-frame squash, scaleY 0.94 → 1.0.*
- **"again." pop:** starts at f30 396. Opacity 0→1 over 3 f30; scale 1.18→1.0 over 3–4 f30 with `Easing.out(Easing.cubic)`. Same position style, center (52%, 28%).

### Transition
- Global fade-out f30 414→421 (opacity to 0, ease-in). Shot B fades in f30 420→441, linear 0→1. Do not hold on black.

### Couch shot (local f30 = 0 at global 420)
- **Camera:** scale 1 → 1.08 linear over 0→180 f30 (keep extrapolating; the shot continues past my range). Transform-origin about (52%, 47%).
- **DAY 1:** opacity 0→1 over local f30 15→21. Gray #BBBBBB, bold Comic Sans, cap height ≈ 30 px. Left x = 150 px (7.8%), center y = 147 px (13.6%). Screen space, no motion.
- **Hero:** static rig pose.
  - Blink: eyelid closes on local f30 ≈ 111–113 (global 531).
  - Phone wobble: rotate ±2° with a slow noise curve.
  - Phone halo: `<radialGradient>` with blue #4A7BFF at 0.35 → 0, radius ≈ 120 px, centered on the face.
  - Halo flicker: `opacity *= 1 + 0.1*random(seed+floor(f/3))` (deterministic `random()` from remotion), changed every 3 f30 to match the measured per-frame jitter.
  - Under-eye blue tint: a small blue stroke under each lid.
- **Shadow:**
  - Silhouette group positioned behind the couch arm layer. Z-order: wall < shadow < couch < hero, with the couch's right arm drawn in front of the shadow.
  - Rise: `translateY = interpolate(f, [24, 75], [270, 0], {easing: Easing.out(Easing.cubic)})`, i.e. global 444→495, about 270 px at 1080p. Before f30 24 only the glow blob shows above the floor behind the couch leg.
  - Glow: `filter` with `feMorphology dilate r≈4` + `feGaussianBlur stdDeviation≈10` + flood #C2401F, composited under the black fill. Constant intensity, no pulse.
  - Raised arm: rotation keyframed to the "up" pose by local f30 ≈ 48 (global 468), then held.
  - Eyes: opacity 0→1 over local f30 57→66 (global 477→486). Slanted dashes, #FF4A3A, with their own small glow.
  - Smile: on during speech. Opacity 0→1 at local 81→93 (global 501→513); 1→0 at local 147→156 (global 567→576). It also flashes at 0.5 during the peek, at local 39–57.
  - Eye shape morph to sly arcs at local f30 ≈ 156 (global 576), a hard swap.
- **Shadow speech:** a `<Caption>` parented to the shadow head (world space). Center = head center + (−24 px, +27 px) for line 1, and +(−24, +78) for line 2 at 1080p. Size ≈ 42 px (3.9%). Color #F94E46.
  - "skip the gym.": in at local f30 75→81 (global 495→501), out at 147→159 (global 567→579).
  - "tomorrow.": in at local f30 153→156 (global 573→576).

### General
- Spread `<HoldNoise>`/blinks over long holds, because the source relies on holds and the push-in to feel alive.
- Never animate hero limbs during dialogue beats here. The source keeps the victim completely passive.
