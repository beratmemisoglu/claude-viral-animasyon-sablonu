# DISCIPLINE: frame analysis, frames 000–099 (≈ 0.0 s – 10.0 s)

Source: `research/frames/video-A/videoplayback_000.jpg … _099.jpg` (640x360). I read every frame in order. I also took pixel measurements with System.Drawing: colors, edges, text bounds and mean luminance.
Notation: `F42` = sampled frame 42. `@30 = 126` = the matching frame at 30 fps (F × 3).

## 0. Sampling rate check
- 300 frames for about 30 s gives roughly 10 fps. The content agrees with that:
  - The alarm "vibration tick" marks repeat on an exact **5-frame cycle** (on, on, off, on, off) from F40 to F73. That is a 0.5 s "beep-beep" rhythm, which fits a regular alarm sound.
  - The hook text stays fully visible for about 1.5 s and is on screen for about 2.4 s in total. That is a normal pace for reading one line.
  - The typewriter shows about 1.6 characters per sampled frame, or about 16 characters/s. That is a typical pace.
- **Conclusion:** the sampling is constant at about 10 fps, so frame N ≈ N/10 s. Absolute timing could be off by ±1 sample (±0.1 s) (?). The frames never show the clock digits change (they read 5:00 from F31 to F99), so they can't be used to check timing in this range.

## 1. Shot list

| # | Frames | Time | Content | In | Out |
|---|---|---|---|---|---|
| S1 | F00–F29 | 0.0–3.0 s | Title card on a near-black background (#0B0B0B with a radial vignette) and letterbox bars | Starts already on the background (no fade from pure black) | Text fades out over F25–F28, then a **hard cut to pure #000** at F30 |
| S2 | F30–F99+ (continues past my range) | 3.0 s → | Wide shot of the bedroom at night | **Fade in from black, F30→F38 (8 frames = 0.8 s)**, linear. Face luminance by frame: #090909 (F30), #242321, #3E3D3B, #555450, #72716C, #948F89, #AEA9A3, #C6C2B7, #DDD9CE (F38), full by F39 | — |

- The transition S1→S2 works as a dip to black: the text fades out (0.4 s), there is a 1-frame cut to pure black (F30, mean luminance ≈ 0), and then the scene fades up for 0.8 s. There is no crossfade between the two shots.
- At F30 the dark gray of the title card (#0B0B0B) jumps to #000. The bedroom then fades in from **true black**, background included.

## 2. Text events

### T1: "Every day started the same."
- **Color:** pure white #FFFFFF at peak. No glow (the pixels right next to the glyphs are background #0B0B0B).
- **Font:** a Comic Sans MS look-alike (the y, t and d glyph shapes match Comic Sans almost exactly). Regular weight, sentence case, period at the end.
- **Position:** centered horizontally. The text spans x = 193–446 px (30.2%–69.7%), so it is about 40% of the frame width. Vertically it sits at y = 170–190 px, so the center is about 50% of the frame height.
- **Size:** about 20 px from ascender to descender, which is 5.5% of frame height. Cap height is about 14 px (3.9%). At 1080p that means a font size of about 58–62 px.
- **Timeline** (peak pixel value per frame):
  - **Fade in:** F04 #1D, F05 #4A, F06 #76, F07 #99, F08 #C9, F09 #F2, F10 #FF. That is linear opacity over **6 frames (0.6 s)**.
  - **Hold:** fully visible F10–F24 (1.5 s).
  - **Fade out:** F25 #DE, F26 #B3, F27 #80, F28 #40, F29 gone. That is **4 frames (0.4 s)**, so the fade out is faster than the fade in.
- **Motion:**
  - No scale change (the text is 252–253 px wide in every frame).
  - It **drifts up very slightly**: the top edge goes from y = 170 (F07) to 167 (F26), about 3 px at 640p over 2 s. That is about 0.8% of frame height (about 9 px at 1080p). (?) This could be a deliberate slow float or encoder jitter; it looks steady and in one direction.
- **Entry/exit:** opacity only, applied to the whole line at once. No blur, no per-word reveal, no typewriter.

### T2: "just 5 more minute…" (still typing at F99, continues past my range)
- **Color:** red, peak about #FF4F58 (warm coral-red). No visible glow or halo.
- **Font:** the same Comic Sans look-alike, all lowercase.
- **Position:** **left-anchored**. The first glyph stays at x = 219 px (34.2%) while the text grows to the right; at F99 it reaches x = 394 (61.6%). The baseline is at y ≈ 108 and the text center at y ≈ 102 px (28% of frame height). It sits above and to the right of the character's head (the head center is at x ≈ 37%) and is not centered in the frame.
- **Size:** about 20 px with descenders (j), cap height about 14 px, which is about 4% of frame height. That matches T1.
- **Animation:** a **typewriter reveal, one character at a time**, with no fade on each glyph and no cursor. Characters visible per frame:
  - F89 "ju" (2)
  - F90 "jus" (3)
  - F91 "just" (4)
  - F92 "just 5" (6)
  - F93 "just 5 m" (8)
  - F94 "just 5 mor" (10)
  - F95 "just 5 more" (11)
  - F96 "just 5 more m" (13)
  - F97 "…mi" (14)
  - F98 "…minu" (16)
  - F99 "…minute" (18)
  - Rate: about **1.6 characters per frame at 10 fps, or 16 characters/s** (0.53 characters per frame at 30 fps), roughly constant. Spaces get their own step.
- The reveal starts at F89, which is **0.3 s after** the content-smile expression appears (F86).

No DAY counter appears in F00–F99.

## 3. Character motion

The character in this range is **only a head and one arm**. The body is entirely under the blanket.
- **Head:** a cream circle (#E2DED3, slightly warm off-white), about 38 px in diameter, which is about 10.5% of frame height. It sits on a gray pillow, upright and facing the camera even though the character is lying down. It is drawn front-facing like a sticker on a horizontal body.
- **Outline:** a very faint darker edge (?). There is no heavy outline.

| Beat | Frames (10 fps) | Notes |
|---|---|---|
| **Asleep, neutral** | F31–F54 | Eyes: two short, slightly downward-curved closed-lid lines. Brows: flat, thick, dark, sitting high. Mouth: a short flat line. **No breathing motion** (the head and blanket stay still). The face does not react when the alarm starts at F40; he sleeps through 1.5 s of alarm. |
| **Eyes open (tired)** | Swaps at F54→F55 (**hard swap, no blink in-between, no half-open frame**) | New face: heavy flat upper-lid lines with small dark pupils hanging just below them (half-lidded, "dead-tired" eyes). Faint **under-eye bags** (light gray curves under each eye, most visible F83–F85). Brows are flat and slightly lower than before. Mouth is a short flat line. The pupils look straight ahead; there is **no head turn toward the clock**. This face holds until F85. |
| **Arm comes out** | Starts F62, extended F64, hold F64–F82 | F62: a fat cream tube-arm pokes diagonally out of the blanket edge (hand near x = 268, y = 205). F63: the arm swings up to horizontal. F64: the arm is fully out, horizontal, from under the chin pointing **to the right, away from the clock**, with a rounded mitten hand at x ≈ 272. That is 2–3 frames (0.2–0.3 s) of movement, then a still hold of about 1.9 s. No overshoot or settle is visible at 10 fps. |
| **"Slap"** | Impact at F74 | **The hand never touches the clock in any sampled frame.** The arm stays still in its right-pointing pose from F64 to F82. The slap is shown **only by its effect on the clock**: at F74 the clock body squashes (about 70% of its height, digits smeared) and a white-gray starburst of short dashes appears around it (see section 4). If a swing to the clock exists, it lasts under 0.1 s and falls between samples (?). In effect it reads as an off-screen or "magic" slap. **The face does not change during the impact.** |
| **Arm retracts** | F83–F85, gone at F86 | F83: the elbow bends into a V (elbow dips down, forearm points up). F84: the arm is diagonal again and sinking into the blanket. F85: a flat mitten hand pats down on the blanket edge. F86: the arm is gone. About 3 frames (0.3 s), slightly slower than coming out. |
| **Contented re-sleep** | Swaps at F85→F86, holds to F99+ | **Hard swap** to a new face: closed eyes drawn as **upward-curved arcs (happy closed eyes)** and a **small U-shaped smile**. Brows stay flat. This is the "lazy relief" expression. No head settling motion is visible. |
| **zZ** | First z at F91 | A small gray "z" (#B1B1B1, about 6 px tall, faint at first) appears at the upper right of the head (x ≈ 250, y ≈ 170). It rises slowly: y 170 at F91, about 160 at F95, about 155 at F98. A second, **larger and dimmer "Z" spawns below it** at F98 (x ≈ 256, y ≈ 170). The letters spawn about 0.7 s apart, rise about 2–3 px per frame at 10 fps, and fade in. They do not sway noticeably side to side. |

- **Panic, sweat drop, head turn:** none in this range. They presumably come after F99.
- **Squash/stretch on the character:** none visible. The only squash is on the clock.

## 4. Props and environment

- **Room layout** (positions at F39, before the push-in grows):
  - **Floor:** a single thin gray line across the full width at y ≈ 246 (68%).
  - **Nightstand:** x 129–186, y 197–246. Dark warm-brown fill (#231D1D) with a gray outline, rounded corners, one drawer line and a knob dot.
  - **Alarm clock** on top of it: a dark rounded box with **red seven-segment-style "5:00"** (peak #CF5351, slight red bloom).
  - **Headboard:** a tall rounded post at x ≈ 197, rising to y ≈ 167.
  - **Bed:** a thin frame on legs, with a gray pillow.
  - **Blanket:** navy-slate (#404656) with one hand-drawn wrinkle line, covering x ≈ 250–472.
  - **Window:** upper right, x ≈ 497–587, y ≈ 52–136. Rounded square, four panes, cross mullions, panes in dark navy with a soft gradient.
  - **Moon:** an off-white circle (#AAACB8 at center after JPEG compression) with a soft glow, in the upper-right pane.
- **Moonbeam:** a very faint diagonal light shaft runs from the window down and to the left toward the bed (about #141318 against the #0B0B0B wall). It does not move.
- **Line style:** light gray (#8a–#a0) strokes about 1.5 px wide at 640p (about 4–5 px at 1080p), slightly wobbly and hand-drawn. Corners are rounded and line ends are round.
- **Alarm vibration marks:** two short **red** diagonal double-strokes ("〃" style), one at each top corner of the clock. They are visible F40–F73 in the 5-frame pattern on, on, off, on, off. On frames: 40, 41, 43, 45, 46, 48, 50, 51, 53, 55, 56, 58, 60, 61, 63, 65, 66, 68, 70, 71, 73. The clock body does **not** shake or move (?). The digits never blink; they stay steady at 5:00.
- **Impact burst (the slap):**
  - **F74:** the clock squashes vertically (about 0.7×) and a ring of about 10 short white-gray dashes sits close around it.
  - **F75:** the ring is larger and the clock is back to normal size.
  - **F76:** the ring is at its largest (about 2.5× the clock's width) and thinner/fainter.
  - **F77:** everything is gone.
  - The vibration marks stop at F74 and never return.
  - So the impact lasts 3 frames (0.3 s): the squash lasts 1 frame, and the burst expands with ease-out and fades.
- **Clock after the slap:** it still reads **5:00** through F99. There is **no jump to 5:05 and no fast-forward** in this range.
- **Lighting:** constant after the fade-in. There is no flicker and no light from the alarm onto the room.
- **Vignette:** a soft radial vignette is present in both shots. At the vertical center, the edges are #050505 and the center is #0B0B0B.
- **Letterbox:** **pure #000 bars at the top (y 0–31) and bottom (y 328–359)**, 32 px each, which is 8.9% of frame height. They are present in **both** shots, title card included. The active picture is 640x296, about 2.16:1.
- **Particles:** none.

## 5. Camera

- **S1:** static.
- **S2:** a **slow, constant push-in** from the start of the shot through at least F99, with no easing visible.
  - The nightstand's left edge moves from x 129 (F38) to 114 (F99).
  - The window's left edge moves from 496 to about 510, and the window top from y 94 to 88.
  - The floor line moves from y 246 to about 252.
  - The scale goes **from 1.00 to about 1.08 over 6.1 s** (about 1.3% per second). The zoom center is about (50%, 47%) of the frame, essentially the frame center.
  - There is no pan, rotation or shake, and the camera does not shake on the slap.

## 6. Pacing

| Segment | Duration | Type |
|---|---|---|
| Title card S1 | 3.0 s (F00–F29) | Text only. The text is visible for 2.4 s, fully visible for 1.5 s, and there are 0.4 s of empty background before it appears. |
| Bedroom fade-in → alarm | 1.0 s (F30–F39) | Calm establishing shot |
| Alarm ringing, before eyes open | 1.5 s (F40–F54) | Action (the delay is a comedic beat) |
| Tired eyes, before arm | 0.7 s (F55–F61) | Action |
| Arm out, hold, impact | 2.0 s (F62–F82) | Action. The impact is 1.9 s after the eyes open. |
| Retract → smile | 0.4 s (F83–F86) | Action |
| Smile hold, then typewriter starts | 0.3 s (F86–F89) | Action |
| Typewriter "just 5 more minute" | ≥1.1 s (F89–F99+) | Text plus idle (zZ) |

- **Text-only screen:** 3.0 s of 10 s (30%). The remaining 7.0 s is the character in the scene; red text overlays it for the last 1.1 s.
- **Beat spacing in S2:** the alarm starts 1.0 s into the shot, and each later beat follows the previous one by 1.5, 0.7, 1.2, 0.9, 0.3 and 0.3 s. **Each beat is separated by a hold**, so only one thing moves at a time.

## 7. New or missed details (not in the BRIEF or the script, or contradicting them)

1. **There is no visible slap contact.** The arm comes out pointing **away from** the clock (to the right), holds still, and the alarm is killed by a clock squash plus a starburst (F74). The script says he slowly reaches out his right arm and presses snooze, which these frames don't show. The user's description says he slaps the alarm, but that is only implied.
2. **No 5:00 → 5:05 jump.** The clock still reads 5:00 after the impact through F99, which contradicts the script.
3. **Red text is typed, not handwritten or faded.** It uses a character-by-character typewriter at about 16 characters/s, all lowercase, in the same Comic Sans–style font as the white text. It is left-anchored at about (34%, 28%), above the head, not centered. At F99 it is still "just 5 more minute" (the rest of the line and any "again." come later).
4. **The hook line fades in (0.6 s) and fades out (0.4 s)** with an asymmetric timing, holds for 1.5 s, and drifts up about 3 px. It is **pure white with no glow**, centered at 50%/50%, about 5.5% of frame height.
5. **Letterbox bars are top and bottom** (8.9% each, pure black), not "top bar-ish". They are present from frame 0, including over the title card. The title-card background is **#0B0B0B with a vignette, not pure black**.
6. **Transition = dip to black:** a hard cut to true #000 (F30), then an 0.8 s linear fade-in of the whole scene. There is no crossfade.
7. **Slow continuous push-in, about 8% over 6 s,** throughout the bedroom shot. The brief does not mention it, and it is essential for keeping a static wide shot feeling alive.
8. **The character sleeps through 1.5 s of alarm** before his eyes open. The comedic delay is part of the beat.
9. **Expressions change by hard swaps** (sprite-like face swaps) with no in-between frames: neutral closed → half-lidded tired with **eye bags** → **happy closed-arc eyes and a smile**. There is no blink, no head turn and no breathing.
10. **Only the head and one arm are visible.** The head is front-facing and upright on the pillow. The arm is a fat cream tube with a mitten hand that pops out of the blanket and back in (0.2–0.3 s each way) and bends at a V-elbow on the way back.
11. **Alarm vibration marks are red, not white,** and blink in a fixed on, on, off, on, off pattern every 0.5 s. The digits don't blink and the clock body doesn't shake.
12. **zZ letters are gray (#B1B1B1),** spawn about 0.7 s apart at the upper right of the head, start small or faint, and rise slowly. The second "Z" is bigger.
13. **Environment details** not in the brief:
    - a faint **diagonal moonbeam** from the window;
    - a moon with a soft glow;
    - a four-pane window with a navy gradient;
    - a navy-slate blanket with a wrinkle line;
    - a headboard post;
    - a dark brown nightstand with a drawer line and knob.
    The wall and floor are the same near-black, separated only by a thin gray line at 68% of the height.
14. **No camera shake or flash on the impact.** It is kept very understated.

## 8. Rebuild notes (Remotion, 1920x1080 @ 30 fps; all frame numbers are @30)

```
// Global
LETTERBOX: two <rect fill="#000"> of height 96px (8.9%) top & bottom, always on top layer.
BG: #0B0B0B + radial vignette (edges ≈ #050505).  FONT: "Comic Sans MS", "Comic Neue", cursive.

// S1 title (0–89)
text "Every day started the same."  fill #FFF, fontSize ≈ 60px, x=50% center, y=50%
opacity = interpolate(f, [12,30,75,87], [0,1,1,0], clamp)      // linear
translateY = interpolate(f, [12,87], [0,-9])                     // subtle float (?)
f=90: hard cut — S2 starts with full-frame black overlay.

// S2 bedroom (90 → beyond 300)
sceneOpacity = interpolate(f, [90,114], [0,1])                   // dip-from-black, linear
cameraScale  = interpolate(f, [90,300], [1.00,1.08])             // linear push-in, origin (50%,47%); likely continues after 300
alarmOn = f in [120,222);  ticks visible when ((f-120) % 15) in {0..5, 9..11}   // on,on,off,on,off @10fps → 3 frames each @30
face: 'sleepNeutral' f<165 ; 'tiredHalfLid'(+eye bags) 165–255 ; 'contentSmile' f>=258   // hard swaps
arm:  out f 186→192 (ease-out, from blanket edge to horizontal right), hold 192–246,
      retract 249→258 (via V-elbow pose at 249, diag at 252, flat paw at 255), hidden ≥258
impact at 222: clock scaleY 0.7 (1–3 frames, back by 225), burst ring of ~10 dashes:
      radius = interpolate(f,[222,230],[1.0,2.5]×clockW, easeOut), opacity 1→0 by 231; ticks stop at 222
typewriter "just 5 more minutes..." start 267, chars = floor((f-267)*0.53), left-anchored at x=34%, y=28%,
      fill #FF4F58 (≈#ff4d4d), fontSize ≈ 58px, no glow, no cursor
zZ: spawn 'z' at 273 (small, opacity 0→1 over ~6f), second larger 'Z' at 294; each rises ≈ -0.8px/f @1080
      (≈ -2.5px@640 per 10fps frame), color #B1B1B1, start at head upper-right (≈ +0.35·headR, -0.6·headR)
Palette: face/arm #E2DED3 · blanket #404656 · nightstand #231D1D · clock digits #E0504E w/ slight bloom ·
         line art #9A9A9A ~4.5px round caps · moonbeam polygon #FFFFFF @ ~3–4% opacity, blur
```

- Keep **only one thing moving at a time**, with 0.3–1.5 s holds between beats. This is the core of the pacing.
- Face swaps can be discrete variants of a `<Face expression=…>` component. Easing between them isn't needed and would look off-style.
- Treat the "slap" as an effect on the prop (squash plus burst) instead of animating the limb all the way to the clock. That is cheaper and matches the source. Optionally add a 1–2 frame arm smear around frame 220 (?) if a visible contact is wanted.
