# DOPAMINE: frame analysis, frames 000–099 (≈ 0.0 s – 10.0 s)

Source: `research/frames/video-B/videoplayback (1)_000.jpg … _099.jpg` (640x360). I read every frame in order. I also checked a few frames past the range for anchoring (F100, F103, F299), and took pixel measurements with System.Drawing: colors, bounding boxes, mean luminance, frame differencing, and HUD trace tracking.
Notation: `F42` = sampled frame 42. `@30 = 126` = the matching frame at 30 fps (F × 3). Percentages are of the full 640x360 frame, letterbox included, unless stated otherwise.

## 0. Sampling rate check

- The folder has 300 frames.
- The hard cut from studio/guitar to the outdoor park lands exactly between F99 and F100. The script puts the park scene at 00:10, so F100 = 10.0 s.
- The text fade-in takes 7 samples (0.7 s) and the fade-out 4 samples (0.4 s). Those are the same values as DISCIPLINE's title card in `discipline-000-099.md`, so both extractions use the same rate.
- The HUD trace scrolls at a constant ≈1.2 px per sample (see §4). That is consistent with uniform sampling.
- F299 already shows the "4:02 PM" gaming scene, which the script places in its 00:15–00:40 block. That is plausible at ≈29.9 s.
- **Conclusion:** the sampling is uniform at **≈10 fps, so frame N ≈ N/10 s** (±0.1 s). The script's "00:06 sits down" is off: the guitar shot starts at **7.0 s (F70)**.

## 1. Shot list

| # | Frames | Time | Dur (samples / @30) | Content | In | Out |
|---|---|---|---|---|---|---|
| S1 | F00–F39 | 0.0–4.0 s | 40 / 120 | **Hook title card** "The world used to be full of color." on #0B0B0B with a vignette and letterbox bars | Starts on the background (no fade from #000) | Text fades out F33–F36, then the card is empty for F37–F39 |
| S2 | F40–F69 | 4.0–7.0 s | 30 / 90 | **Studio, wide shot: painting at the easel** | **Fade up from true black**, F40→F44, about linear. Mean luminance: 3.6, 13.8, 23.8, 34.4, 40.8. F40 is darker than the card (9.9), so the transition is a dip to #000 and not a crossfade. | Hard cut |
| S3 | F70–F99 | 7.0–10.0 s | 30 / 90 | **Same studio, slightly closer framing: sitting on the stool playing guitar.** The easel and canvas are **gone** from the set. | **Hard cut** plus a small camera "settle" over F70→F73 (§7) | Hard cut to the sunny park at F100 (outside range) |

- There are 3 shots in 10 s and the average shot length is 3.3 s. The two scene shots are **exactly equal length (3.0 s each)**, which suggests a beat-grid edit.
- The cut from S2 to S3 is a **time-skip cut**: no sit-down animation and no walk to the stool. Between the two shots the character teleports from standing at the easel to seated on the stool.

## 2. Opening hook

- **First thing on screen:** an empty dark card (#0B0B0B with a radial vignette, edges #060606) between letterbox bars, for **0.5 s (F00–F04)**.
- **Text (exact):** `The world used to be full of color.` The words are pure white. The word **"color."** is drawn **letter by letter in rainbow order**:
  - c = red #EA6A4F / #FF675B
  - o = orange #F49A3A
  - l = yellow #FFDF4F
  - o = green #66B47C
  - r = blue #4A8FE0
  - . = purple #9786BA
  
  So the final word plus the period is a 6-step ROYGBV spectrum.
- **Character appears:** dimly at F40 (in the fade-up) and clearly by F42–F43. That is **≈4.0–4.2 s** after the start.
- **Difference from DISCIPLINE ("Every day started the same."):**
  1. **Tense and premise.** DISCIPLINE is a present-feeling routine statement ("this keeps happening"). DOPAMINE uses past tense, "used to be", which **promises a loss**: the viewer immediately asks "what took the color away?". It is a before/after hook, not a routine hook.
  2. **Color carries meaning in the typography.** The only colored glyphs are in the word "color". The hook shows the film's central visual metaphor (color = healthy dopamine, gray = depleted). DISCIPLINE's hook is plain white. This is the first time the channel uses **color as a keyword highlight inside a white line**.
  3. **Longer card.** DOPAMINE's card is 4.0 s, with the text held at full opacity for 2.1 s. DISCIPLINE's card is 3.0 s, held for 1.5 s. The line is longer (35 vs 27 characters), so the hold scales with text length.
  4. **Gap before the scene.** There are 0.3 s of empty card plus a dip to #000. DISCIPLINE had a 1-frame #000 cut. The approach is the same; the gap here is slightly longer.
  5. **The first scene is the "full of color" state.** The character is happy and productive in a saturated studio. In DISCIPLINE the first scene is already the problem (the alarm and snooze). DOPAMINE **opens on the ideal state** and destroys it later.

## 3. Text events

### T1: "The world used to be full of color."

- **Font:** a Comic Sans MS look-alike, regular weight, sentence case, period at the end. It is identical to the DISCIPLINE hook.
- **Color:** white #FFFFFF (peak value 255) for "The world used to be full of"; the per-letter rainbow for "color." (§2).
- **Glow:** none. Within 1–2 px of the glyphs the pixels drop to #000–#060606, darker than the #0B0B0B background. This is probably JPEG ringing, or possibly a very thin dark shadow (?). There is no light halo.
- **Position:**
  - Horizontally centered: x = 167–472 px (26.1%–73.8%), center 49.9%, about 47.7% of the frame width.
  - Vertically: y = 167–188, center ≈177, which is **49.3% of frame height** (optical center).
- **Size:** about 18–21 px from ascender to baseline (the line has no descenders), which is **≈5.3% of frame height**. That is about 57 px at 1080p, or a font-size of ≈72 px in Comic Sans at 1080p.
- **Timeline** (peak luminance in the text box per frame):
  - **Fade in:** F05 25, F06 64, F07 104, F08 137, F09 173, F10 206, F11 242, F12 255. That is **linear over 7 samples (0.7 s)**.
  - **Hold:** fully visible F12–F32 (**2.1 s**).
  - **Fade out:** F33 219, F34 174, F35 118, F36 61, F37 gone. That is **4 samples (0.4 s)**, so the fade out is faster than the fade in. This is the same asymmetry as DISCIPLINE.
- **Motion:**
  - It **drifts up slowly**. The bbox top goes from 170 (F08) to 166 (F32) and the bottom from 188 to 184, so it rises ≈3–4 px at 640p (≈1% of height, ≈10 px at 1080p) over ≈3 s. It is linear and in one direction. This matches DISCIPLINE's float.
  - There is no scale change: the width is 305 px throughout.
- **Entry/exit:** opacity only, on the whole line at once. There is no typewriter, no per-word reveal and no per-letter color animation. The rainbow letters are colored from the first visible frame.

### T2: HUD label "DOPAMINE" (persistent from F45/F46)

- Small, wide-tracked, all-caps sans-serif. It looks like a rounded or monospace UI font, not Comic Sans (?).
- Mid gray: brightest pixel #7C7C7C, apparent color ≈#8a8a8a.
- Position: x ≈ 22–64 (3.4%–10%), y ≈ 32–37 (top edge **touching the letterbox bar**).
- Cap height ≈5 px (≈1.4% of height, ≈15–18 px at 1080p).
- It fades in with the graph over F46–F50 and is static after that.

No DAY counter, no red text and no clock appear in F00–F99.

## 4. HUD analysis

### 4.1 Dopamine graph (top-left)

- **Appearance timing:**
  - It is not present on the title card or during the scene fade-up (F40–F44).
  - The trace first appears faintly at **F45**, starting with its right part. The label appears at F46.
  - Tip-dot brightness by frame: #20 (F45), #69, #A4, #CE, #D2, #E4 (F50), #F0 (F51).
  - So the **HUD fades in over ≈F45→F51 (0.6 s), starting 0.5 s after the scene is fully up**. It is a separate layer with its own entrance.
- **Panel:**
  - A dark translucent rounded rectangle at x ≈ 18–138 (2.8%–21.6%), y ≈ 31(clipped)–80 (8.6%–22%).
  - Measured darkening:
    - #0B0B0B wall → #040404 inside the panel (F60)
    - Navy poster #222649 → #151424 (F85)
    - Sky #6399E3 → #354F74 (F100)
  - That works out to roughly **black at 45–60% opacity**. On the dark studio wall it is barely visible. Over the poster in S3 it **visibly dims the top of the poster** (F70–F99), and the poster appears behind the HUD.
  - The rounded corners are clearly visible over the sky at F100.
- **Trace:**
  - A single thin line (≈1.5 px at 640p, ≈4–5 px at 1080p) in light gray/white (#C8C8C8–#E0E0E0) with a slight glow.
  - It spans x ≈ 22–133 (3.4%–20.8%, about 17% of the width). The baseline is at y ≈ 54 (15% of the frame, or 7.4% down into the active picture).
- **Shape and motion in this range: a calm sine-like wave (the "healthy" state).**
  - Crest-to-trough is y 51–57, so the amplitude is **±3 px (±0.8% of height, ±9 px at 1080p)**.
  - The **wavelength is ≈35 px** (crests at x ≈ 83 and 118, for example), so about 3 waves are visible.
  - The wave is not a perfect sine. Crest heights vary slightly, so it reads as hand-made noise, not a math sine.
  - It **scrolls left continuously**. One crest moves x 119 (F49) → 106 (F60), ≈1.2 px per sample, so **≈12 px/s at 640 ≈ 36 px/s at 1920 ≈ 1.2 px per frame at 30 fps**. The same speed holds in S3 (crest 50→45 over F80→F84).
  - The scroll is continuous across the S2→S3 cut. The HUD is a global layer and does not reset at the cut.
  - There are **no spikes in this range**. Painting and guitar both read as healthy, sustained, gentle dopamine.
- **Tip dot:**
  - A glowing dot (core ≈3 px, soft glow radius ≈6–8 px) at the right end of the trace, x ≈ 132–133, y bobbing between 52 and 57 with the wave.
  - Its color is **white (#F0F0F0–#F6F6F6) F50–F66**.
  - It turns **pink/magenta (#FFC6F1 – #FFDDF9)** on **F67–F72** and briefly on **F92** (#FFD0F7). Between those it is white with a faint pink cast (#FFF0F8 – #F7E9EC, F74–F99).
  - F67 is when the arm reaches full extension to dot the last flowers. F92 has no obvious action. The pink may be a small "reward pulse" or a cosmetic color cycle (?).
  - Frames F200–F299 (see `dopamine-200-299.md`) show that cheap hits produce **tall spikes with pink tips**. In this range the trace never leaves the ±3 px band.
- **Storytelling role:**
  - The HUD is a **"vital-sign monitor" for the protagonist's mind**. Earned pleasures (painting, music) produce a calm, steady, rolling wave. It sets the baseline the audience will later see spiked and crashed.
  - It enters 0.5 s after the scene, so the viewer first reads the world and then learns that it is being measured.
  - Its top-left placement echoes DISCIPLINE's top-left DAY counter (same HUD slot, a different data type).

### 4.2 Clock (top-right)

- It is **not present anywhere in F00–F99**. In S2 and S3 the top-right corner contains only the window, wall and letterbox.
- First seen out of range: "2:14 PM" at F280 and "4:02 PM" at F299 (see `dopamine-200-299.md`).
- From F299: white or off-white, right-aligned, ending at x ≈ 593 (92.7%), y ≈ 48 (13%), cap height ≈10 px.
- **Implication:** the clock is a **"time-loss" device reserved for the cheap-dopamine scenes**. The healthy opening has no clock because time isn't being wasted. That contrast is itself the storytelling.

## 5. Character motion breakdown

### Common design in this range

- The body is a warm cream bean (#DCD3C9; slightly darker shading #CAC5BB on the face side), with the head merged into the body.
- The **near arm** is cream with a **thin dark outline** (≈#222) and is drawn over the body.
- The **far limbs** are gray: far leg #A4A398, shadow side #626158; the far arm in S3 is gray.
- The face is thick dark brows, dot eyes and a small curved mouth, with no nose.
- Standing height in S2: head top y = 137 to feet at y ≈ 271, so **134 px ≈ 37% of frame height** (45% of the active picture). Center x ≈ 300 (47%).

### S2, painting (F40–F69)

Props:
- **Brush** in the near (right) hand: a thin brown stick with a colored tip dot.
- **Palette** held by the far hand at belly height: orange #F29B39 kidney shape with rainbow paint dots.

| Phase | Frames (10 fps) | @30 | Pose / action |
|---|---|---|---|
| A: reach low | F40–F48 | 120–146 | The arm is extended **diagonally down-right**, and the brush touches the canvas's lower-left area (tip ≈ x 360–368, y 195–205). Small 1–3 px tip drift per frame (dabbing). |
| A→B: raise | F49–F52 | 147–158 | The forearm lifts. The tip rises from y≈200 to ≈180, and the brush angle steepens. |
| B: bent, hand near chin | F53–F61 | 159–185 | The **elbow is bent sharply** with the hand up by the cheek or mouth. The brush points up-right at ≈45°, with the tip at ≈(345–350, 150–158). This is a "careful dabbing" pose that also reads as a thinking pose. Peak bend is F56–F59 (the hand partly covers the mouth). |
| B→C: extend | F62–F66 | 186–200 | The arm swings out. The tip moves from (352,152) to (372,168). |
| C: straight reach | F67–F69 | 201–209 | The arm is **fully horizontal**, straight to the canvas's right side (tip ≈ x 375, y 168–172). This is held until the cut. |

- **No body movement.** The legs, torso and head are locked (frame-diff centroid stays on the arm/brush area, about 220–620 px changed per sample, all around x ≈ 311–323).
- **No line boil** in S2: static regions such as the window and poster show 0–10 changed pixels per frame.
- **The brush-tip color cycles through the rainbow** in the same order as the hook's "color.":
  - **red** (F42–F44)
  - **orange** (F45–F48)
  - **yellow** (F49–F53)
  - **green** (F55–F58)
  - **blue** (F60–F64)
  - **purple** (F65–F69)
- **The painting is NOT stroke-driven.** It builds by **hard-edged rectangular wipe reveals, left to right**, independent of the brush position:

  | Layer | Frames | @30 | Notes |
  |---|---|---|---|
  | (pre-painted) sky #70B9FD + sun #FEC435 | visible from F40 | — | The lower 45% of the canvas is blank off-white |
  | Light-green hills #369752 | F43 → F48 | 129–146 | The wipe edge is a vertical hard line moving right, ≈15 px per sample |
  | Darker green lower hill band | F49 → F52 | 147–158 | Second wipe, left to right |
  | Brown/orange ground #D07B38 | F53 → F59 | 159–179 | Wipe from left; the top edge follows the hill contour |
  | Flower dots (red, yellow, orange, pink, purple, blue, ≈2 px) | F60 → F69 | 180–209 | **≈1 new dot per sample** (≈10 dots in total), scattered on the brown ground |

- **Expression (S2):** dot eyes, **brows angled down toward the center (focused/confident)**, a small closed smile. It is constant, with no swaps and no blink.

### S3, guitar (F70–F99)

- **Pose:** seated on the stool (one brown stool leg visible at x≈276), facing right, body upright.
  - The orange acoustic guitar (body #E28037–#EE9655, two overlapping circles, light soundhole #EFD9BA, brown neck #83664F) lies across the lap, angled up-right with the neck end at ≈(390,180).
  - The **far arm (gray tube)** reaches horizontally to the neck. A light-gray round knob at (376,187) is probably the fretting hand (?).
  - The **near arm** curls down, with the hand at the soundhole.
- **Strumming:**
  - It is **barely visible**: the near hand at the soundhole changes every sample, alternating between "notch visible" and "notch covered".
  - Frame-difference counts in the hand box alternate ≈360 / ≈150 / ≈360 …, a **2-sample cycle**. At 10 fps sampling this is an aliased fast strum (true rate ≥5 Hz (?)), or the hand is simply toggling between 2 drawings.
  - The head changes only 44–86 px per sample, so it is essentially still. There is **no body bob and no head nod**.
- **Music notes (secondary motion), two staggered emitters, a loop:**
  - **Emitter 1: a single green ♪** (#3FAF5A-ish).
    - It spawns faint at ≈(355,130), just above the head and right of it.
    - It rises up-right to ≈(390,70) over ≈14 samples, fading in for the first 2 samples and out for the last 2–3.
    - Cycle ≈16 samples (1.6 s). Spawns seen at F78, F94–F95, and one already rising at F70.
  - **Emitter 2: a cluster of 3 beamed notes**, overlapping, colored **yellow / orange / red**.
    - It follows the same path, offset by **≈8 samples (half a cycle)**. A cluster is seen rising F70–F83, then a new one spawns F85–F86 and rises to F99.
  - The motion is roughly linear, about 35 px up and 25 px right per 10 samples, with no sway.
- **Expression (S3):** **half-lidded eyes** (flat upper lids over the dots), flat brows, a small contented smile. It reads as blissful or "in the flow", which is different from S2's focused face. The face is static and the change happens by swap at the cut.
- **Ambient animation:** the **poster's three blue wave lines undulate** in S3. Their phase shifts every sample (diff 27–95 px), whereas in S2 the poster was static (0–10 px). It may be on only in S3, or too slow to register in S2 (?). The bottle shelf shows 7–38 px of noise, which is probably just compression.

## 6. Environment and color

### Studio set (S2 positions)

| Element | Position (px @640) | Colors |
|---|---|---|
| Floor line | full width, y = 269 (74.7%) | light gray #A09D97, ≈1.5 px |
| Wall / floor | — | both #0B0B0B (same tone); vignette edges #060606 |
| Framed poster (left) | x 2–74, y 56–150 | navy #0A0D1C–#0F1126, orange sun #B5671F (warmer in S3), 3 blue wave lines #4A8FE0-ish, light-gray rounded frame |
| Shelf of 9 rainbow paint bottles/crayons + white ball | bottles x 128–215, y 75–110; shelf y 112 | red #F8523C, ochre #B76926, yellow #FED33A, green #43B054, blue #3495FC, purple #9866D0, pink #F976AA, red-orange #FA5535, orange #FE981E; ball #E6E6F0; shelf #8C6550 |
| Stool | x 193–237, seat y 213 | warm brown #9D6631, legs #886044 |
| Easel + canvas | canvas x 346–437 (54–68%), y 127–241; easel legs to the floor | easel #664A3D–#845E37; canvas colors in §5 |
| Window (upper right) | x 450–557 (70–87%), y 46–142 | sky #63A0ED, sun #F4DA8A, cloud #D8CFC8, green hills #4D9F53, brown frame with cross mullions |
| Potted plant | x 545–630, pot y 237–270 | pot terracotta #A1502A, leaves #2E7A3D with round dot tips #42824F |
| **Light shaft** | diagonal band from the window toward lower-left, passing over the canvas and character | warm faint #1B1A18–#241F1B on #0B0B0B (≈+8% lum) |

### Saturation and lighting

- The props, canvas and window are **fully saturated flat colors** (HSV S ≈ 55–80%, V ≈ 95%+).
- The background stays near-black, which is the same dark-stage convention as DISCIPLINE. Color appears **only on objects**, so the rainbow pops against black.
- The character remains cream/neutral and is not colorized.
- Lighting is flat fills with no cast shadows on the floor. A soft vignette and the window light shaft are the only lighting effects. There is no flicker.
- Overall impression: "a black stage with candy-colored props". This is a big difference from DISCIPLINE's mostly gray/red world, and it is the **"full of color" baseline** that the film will later desaturate.

### Letterbox and other details

- **Letterbox:** pure #000 rows 0–31 and 328–359 (32 px = 8.9% each), with a 1–3 px #010101 transition row at the bottom. The active picture is 640x296 (≈2.16:1). It is present from F00, including over the title card, and is identical to DISCIPLINE.
- **Outdoor peek (F100, for context):** blue sky gradient, white clouds, a sun with a glow, green hills, round trees, grass with **multicolor flower specks**, and birds as "v" marks. It is fully daylit and is the brightest scene so far.

## 7. Camera

| Shot | Behaviour |
|---|---|
| S1 | Static |
| S2 F40–F42 | A tiny settle during the fade-up (window left edge 454→452, top 48→46, about 2 px) (?) |
| S2 F43–F69 | **Locked static.** Window x 452–553, poster edge 73–74, floor 269 and head top 137 all stay constant to ±1 px for 27 samples. **No push-in**, unlike DISCIPLINE's 8%-over-6-s push-in. |
| S3 framing | A **closer, re-composed framing of the same set**: props are ≈1.07–1.10× larger (window 107→115 px wide, poster 72→77 px, shelf 87→94–98 px) and shifted right ≈+25 px. The easel has been removed from the set. |
| S3 F70→F73 | A **cut-in settle**: poster right edge 96→101→103→104, floor 262→261→260→260, head top 134→136. That is a ≈3–4% scale ease-out from slightly bigger to final over ≈0.3 s, consistent with an eased "zoom out to rest". |
| S3 F73–F99 | Locked static (all landmarks ±1 px) |

## 8. Pacing stats (F00–F99, 10 s)

| Segment | Duration | Share |
|---|---|---|
| Empty card before the text | 0.5 s | 5% |
| Hook text visible (in 0.7 / hold 2.1 / out 0.4) | 3.2 s | 32% |
| Empty card after the text | 0.3 s | 3% |
| Scene fade-up from black | 0.5 s | 5% |
| Painting (character visible) | 2.6 s (after the fade) | 26% |
| Guitar | 3.0 s | 30% |

- **The first 4.0 s (40%) is text only.** That is a larger share than DISCIPLINE's 3.0 s.
- Shots: 3 in total; the two scene shots are 3.0 s each.
- **Actions per shot: 1.** Painting has 3 arm poses in 3 s; guitar has 1 pose with looping secondaries.
- The **HUD enters at 4.5 s**, the second "new information" beat after the scene itself.
- There is **no narration text** over the scenes in this range. The opening is a 6-second "show the good life" montage with zero copy. Meaning is carried by color, HUD and particles.
- Motion budget:
  - S2: one limb plus the canvas reveal plus the HUD.
  - S3: notes plus a micro-strum plus the HUD plus the poster waves.
  - The body never moves, so one or two things move at a time. This is the same rule as DISCIPLINE.

## 9. New or missed details (vs BRIEF and script-DOPAMINE.txt)

1. **The hook card is missing from the script.**
   - The film opens with 4.0 s of "The world used to be full of color.", with **"color." in per-letter rainbow** (red, orange, yellow, green, blue, purple).
   - The script starts directly at the studio, and the BRIEF only describes DISCIPLINE's hook.
   - This is the first time the style uses colored keyword letters in a narrator line.
2. **There is a rainbow motif in three places.** The same ROYGBV order appears in the hook word "color.", in the **brush-tip color sequence** (F42→F69: red, orange, yellow, green, blue, purple), and in the **shelf of 9 rainbow bottles**. It is a designed system, not decoration.
3. **The canvas paints by left-to-right hard-edged wipe reveals** (hills, then darker hills, then ground, then flower dots), not by brush strokes. The brush position doesn't match the reveal edge. The script's "brush strokes" are only implied.
4. **The HUD is not present from the start.**
   - It fades in at F45–F51 (4.5–5.1 s), after the scene.
   - It has a **translucent dark rounded panel** (black at ≈50% opacity), measured over the sky at F100 and over the poster in S3.
   - The label **"DOPAMINE"** is small, gray (#7C7C7C–#8a8a8a), all caps, wide-tracked, and sits right under the letterbox.
5. **The healthy dopamine trace is a scrolling, gentle, irregular wave**: ±3 px at 640 (±9 px at 1080), wavelength ≈35 px (≈105 px at 1080), scrolling left at ≈1.2 px per frame at 30 fps.
   - It has a **glowing tip dot** at the right end that is white with **brief pink tints (F67–F72, F92)**.
   - There are no spikes during the healthy activities. The script mentions only "falling curves" later.
6. **There is no clock in the healthy opening.** The clock only exists in the cheap-dopamine scenes (2:14 PM, 4:02 PM from F280). It is a deliberate device: "time is now being counted/lost".
7. **There is no sit-down animation.** At 7.0 s a hard cut skips time to the seated guitar pose. The script says "sits on the stool at 00:06". In the new framing the **easel and canvas have disappeared**, a continuity cheat that keeps the frame clean.
8. **S3 is a re-framed, ≈8% closer view of the same set,** with a short ease-out "settle" on the cut (≈3–4% scale over 0.3 s). There is no push-in on S2, which differs from DISCIPLINE's slow push-in.
9. **Expressions differ per activity** and swap at the cut. Painting has focused down-angled brows and a smile; guitar has half-lidded blissful eyes and a smile. In the "careful dab" pose (F53–F61) the hand comes up to the chin.
10. **Music notes are two staggered loop emitters**: a single green ♪ and a yellow/orange/red beamed cluster, half a cycle apart, ≈1.6 s per cycle, rising diagonally up-right from above the head. They don't swirl around the character as the script says.
11. **The strum is a 2-drawing micro-toggle of the hand at the soundhole.** There is no visible arm swing and no body bob.
12. **The poster's water waves animate in S3** (ambient life).
13. **There is a warm diagonal light shaft from the studio window** (≈+8% luminance), which is the counterpart of DISCIPLINE's moonbeam.
14. **The set has a nine-color bottle shelf, a sun/sea poster, a potted plant with dot-tipped leaves and a 4-pane daylight window.** All of it sits on a black stage with a single gray floor line at 74.7%.
15. **The far limbs are gray and the near arm has a dark outline** (#222-ish) where it overlaps the body. The body has no heavy outline. Body color here is #DCD3C9, slightly warmer and darker than the BRIEF's #e8e4d8.
16. **The title-card mechanics are identical to DISCIPLINE**: Comic Sans look-alike, white, no glow, centered at ≈50/49%, about 5.3% of height, linear fade in 0.7 s and fade out 0.4 s, ≈1% upward drift, dip to true black before the scene. This is a reusable template.
17. **The empty card lead-in is 0.5 s** before the text starts fading in, and the scene comes in **0.3 s after the text is gone**.

## 10. Rebuild notes (Remotion, 1920x1080 @ 30 fps; all frame numbers are @30 = F×3)

```tsx
// ---------- GLOBAL ----------
LETTERBOX: <rect y=0 h=96 fill="#000"/> + <rect y=984 h=96 fill="#000"/>   // topmost layer, from f0
BG: #0B0B0B + radial vignette (edges #060606)
FONT_NARRATOR: "Comic Sans MS","Comic Neue",cursive
HUD_FONT: small caps sans (e.g. "Nunito"/"Varela Round" 600, letterSpacing 0.15em) (?)

// ---------- S1 HOOK CARD (0–119) ----------
<Text x="50%" y="49.3%" anchor="middle" fontSize≈72 fill="#FFF">
  The world used to be full of <tspan fill="#EA6A4F">c</tspan><tspan fill="#F49A3A">o</tspan>
  <tspan fill="#FFDF4F">l</tspan><tspan fill="#66B47C">o</tspan><tspan fill="#4A8FE0">r</tspan>
  <tspan fill="#9786BA">.</tspan>
</Text>
opacity    = interpolate(f, [15, 36, 96, 108], [0, 1, 1, 0], clamp)   // linear; 0.7s in, 2.1s hold, 0.4s out
translateY = interpolate(f, [15, 108], [0, -10])                      // slow float ≈1% of height
// f108–119 empty card

// ---------- S2 PAINTING (120–209) ----------
sceneFade  = interpolate(f, [119, 133], [0, 1])   // from TRUE #000 (black overlay), linear
camera: static (optional 1.01→1.00 settle over 120–129)
character standing: feetY = 74.7% (807px), centerX ≈ 47% (900px), height ≈ 37% (400px)
armPose keyframes (near arm, pivot at shoulder; elbow joint):
  120–146 'reachLow'   (shoulder ≈ -35°, elbow ≈ 10°), small dabs ±3px every ~6f
  147–158  → 'bentUp'  (ease-in-out)
  159–185 'bentUp'     (elbow ≈ 140°, hand at chin, brush ↗ 45°)
  186–200  → 'straight'
  201–209 'straight'   (arm horizontal to the canvas)
brushTipColor: steps at 120:#E8524A 135:#F39A2E 147:#FFD43A 165:#43B054 180:#3495FC 195:#9866D0
canvas layers (clipPath rect width animated left→right, linear):
  hillsLight  interpolate(f,[129,146],[0,W])
  hillsDark   interpolate(f,[147,158],[0,W])
  ground      interpolate(f,[159,179],[0,W])
  flowerDots  dot i visible when f >= 180 + i*3   (≈10 dots, palette rainbow, r≈6px)
face: 'focused' (brows angled in, dot eyes, small smile)

// ---------- S3 GUITAR (210–299) ----------
hard cut at 210; set re-framed: scale 1.08, offsetX +75px (@1080) vs S2; remove easel
cut-settle: camScale = interpolate(f,[210,219],[1.04,1.00], easeOut)
pose 'seatedGuitar' static; face 'blissHalfLid'
strumHand: toggle between 2 drawings every 3 frames ((f/3|0)%2) (?) — tiny ±4px offset
notes: 2 emitters, period 48f, emitter B offset 24f
   path: from head + (+0.25·W_head, -0.15·H) → (+105px, -180px) linear over 42f
   opacity: interpolate(t,[0,6,36,42],[0,1,1,0]); A = single green ♪ #3FAF5A; B = beamed triple (yellow/orange/red)
poster waves: phase += 0.15 rad/frame (?) (ambient)

// ---------- <DopamineHUD> (global layer, ABOVE fades/cuts, starts 135) ----------
opacity  = interpolate(f, [135, 153], [0, 1])
panel: rounded rect x=54 y=93 w=360 h=147 (rx≈18) fill rgba(0,0,0,0.5)   // top edge tucked under letterbox
label "DOPAMINE": x=66 y=~104 (just under bar), fontSize≈16, fill #8A8A8A, letterSpacing wide
trace: x 66→399, baselineY=162, stroke #D8D8D8 w≈4.5, round caps, soft glow (blur 2)
   y(x,f) = base + 9*noiseSine((x + 1.2*f)/105 * 2π)   // scroll left 1.2 px/frame, λ≈105px, amp ±9px
   healthy state = no spikes (whole S1–S3 range)
tipDot at x=399: r≈5 + glow r≈20, fill #F4F4F4; optional pink pulse #FFC6F1 at 201–216 and 276
// No clock component in this range (enter it only in cheap-dopamine scenes).

// Palette tokens
cream #DCD3C9 · farLimb #A4A398 · outline #222 · floorLine #A09D97 · wall #0B0B0B
skyCanvas #70B9FD · sun #FEC435 · hill #369752 · ground #D07B38 · guitar #E28037/#EE9655
stool #9D6631 · easel #845E37 · pot #A1502A · leaf #2E7A3D · lightShaft rgba(255,230,200,0.06)
rainbow [#F8523C,#FE981E,#FED33A,#43B054,#3495FC,#9866D0,#F976AA]
```

- Template reuse: the hook card for a new topic is `white line + keyword tinted with the topic's "healthy" palette`. For a loneliness film, for example, "people" could be tinted warm.
- Keep the HUD and the letterbox outside the per-shot fade wrappers, and drive the HUD scroll from the global frame so it never resets on cuts.
- Build the "healthy" scenes as a **saturated-prop-on-black-stage** set, so a later desaturation (filter `saturate(0)` interpolated per layer) has maximum effect.
