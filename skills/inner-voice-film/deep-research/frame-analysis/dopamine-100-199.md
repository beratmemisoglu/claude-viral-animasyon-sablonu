# DOPAMINE — frame analysis, samples 100–199 (≈ 0:10.0 – 0:19.9)

Source: `research/frames/video-B/videoplayback (1)_100.jpg … _199.jpg` (640x360). I read every frame in order. I also checked key regions with 3–4x crops and pixel sampling (System.Drawing).

## 0. Sampling rate: conclusion
- The folder has **300 frames**. Scene timing matches the script: the run ends at about 0:13, the kite two-shot runs 0:13–0:15, and the phone appears around 0:15–0:16. The HUD graph also scrolls at a steady ≈1 px per sample.
- **Conclusion: 10 fps sampling, so sample N = N/10 s (±0.1 s). At 30 fps, frame = N×3.** All "@30" numbers below use this.
- Pixel conventions: coordinates are at 640x360. Multiply by 3 for 1920x1080. Percentages are of the full 640x360 frame.

## Global frame format (applies to every shot here)
- **Letterbox.** Pure #000 bars, top y=0–30 and bottom y=328–359. The active picture is y=31–327 (297 px tall), giving an active aspect of **≈2.15:1**. At 1080p each bar is ≈93 px. The bars stay through every shot, including the dark studio.
- **Vignette.** Soft darkening at the corners and edges in the daylight scenes. Sky at the centre is #79B4F6; near the right edge at the same height it is #718FB5.
- **Light shafts.** A soft diagonal light beam/glare runs from the top-right toward the lower-left in the daylight scenes. A fainter one appears at the left near the HUD. In the studio there is a clear grey light wedge from the window (top-right) down to the floor at the easel.
- **Line boil (?).** In the kite two-shot the character silhouettes have slightly rough, painterly edges. This looks like a texture or "chalk" edge rather than a crisp vector. It is not a frame-to-frame boil, because the held frames are identical.

---

## 1. Shot list

| # | Samples | Time (s) | @30fps frames | Dur | Shot | In / Out transition |
|---|---|---|---|---|---|---|
| S1 | 100–129 (shot began before 100) | 10.0–12.9 | 300–389 | ≥3.0 s | Park run. Side view, hero runs right, background parallax-scrolls left. | Out: **hard cut** at 129→130 |
| S2 | 130–157 (+158–159 fading) | 13.0–15.9 | 390–479 | 2.8 s held + 0.2 s fade | Kite two-shot. Hero (kite string in raised hand) and friend in yellow hard-hat, static, kite flutters. | In: hard cut, possibly with a 1-sample scale "settle" (130 is ≈3% larger than 131) (?). Out: **dip to black** |
| — | 158–160 | 15.8–16.0 | 474–482 | ≈0.3 s | Dip-to-black. Mean luma: 157=143, 158=119, 159=47, 160=5. | Fade-out is ease-in (slow then fast). Full black at 160. |
| S3a | 160/161–171 | 16.1–17.1 | 483–515 | ≈1.1 s | Dark studio, wide. Hero paints at the easel. Phone sits on a stool with a red badge. | In: fade from black over ≈0.2 s (160→161/162) |
| S3b | 172–199 (continues) | 17.2–19.9+ | 516–599+ | ≥2.8 s | Same shot, continuous. Phone buzzes, hero turns, grabs the phone, gets the "+1" hit. **The camera starts a slow pan left at 172 and eases to a stop ≈190.** | No cut. S3a and S3b are one shot. |

Shot count in 10 s: 3 shots, 2 transitions (1 hard cut and 1 dip-to-black). Every shot is wide or full-figure. There are no close-ups in this range.

---

## 2. Text events

**No narrator, lesson or info text appears in this 10-second range.** The script's "just one more" comes later. Only two kinds of text are on screen:

| Text | In | Full | Out | Animation | Color | Position (x%, y%) | Size | Glow |
|---|---|---|---|---|---|---|---|---|
| `DOPAMINE` (HUD label) | already on at 100 | whole range | stays | none (static). It stays at full brightness through the dip-to-black (HUD sits above the scene fade). | light grey ≈#9A9A9A–#B0B0B0, ≈80% opacity | top-left of the HUD panel, ≈x 3.6–11%, y ≈9–10% | cap height ≈5–6 px (≈1.6% H, ≈16–18 px @1080). Uppercase rounded/hand font, slightly letter-spaced | none |
| `+1` (with heart icon) | 184 (heart appears in the sparkle burst) | 185–193 | fades 194–199, invisible by ≈200 (?) | Pops in during the sparkle burst. **Floats up with ease-out:** y = 128→117→107→102→97→92→87→83 px (samples 185–193), drifting x 285→290. Then holds and fades (opacity ≈100→30% over 195–199, heart darkens toward #8a2a3a). | heart #FD4C76 (sampled), `+1` white #FFFFFF bold | heart ≈45% x; travels from y 35% to 23%. `+1` sits just right of the heart at ≈49% x | heart ≈16x14 px (2.5% W); `+1` cap height ≈8 px (≈2.2% H) | soft white/pink glow at the start (185–188), none later |

Other non-text icons:
- **Phone notification badge.** A red #E8403A circle with tiny white text, possibly "999" (?). It sits at the phone's lower-right corner from 161 onward.
- **Vibration ticks.** Two pairs of short magenta/pink slashes (`\\ //`) on both sides of the phone, 172–180. They are static per frame, so the effect is a "buzz" glyph rather than a shaking phone.

---

## 3. HUD analysis (the most important device)

### Geometry (measured at sample 100)
- **Panel.** Rounded rectangle, x ≈ 19→128 px (**3.0%–20.0% W**), y ≈ 31→81 px (**8.6%–22.5% H**). **Its top edge sits flush against the top letterbox bar.** Corner radius ≈4 px (≈12 px @1080).
- **Fill.** Semi-transparent black, ≈50–55% opacity. Sky #6193D0 under the panel reads #2B4264. Clouds show through the panel, so it is not blurred.
  - In the dark studio the panel is invisible (black on black). Only the label and line remain.
  - During the dip-to-black (159) the panel fades with the scene, but **the line and label do not**. The panel looks like part of a scene-tinted layer, or simply an alpha box over whatever is underneath.
- **Plot area.** Line from x ≈ 22→133 px (≈3.5%–20.8% W), centred vertically at y ≈ 50–52 px (≈14% H).
- **Write head.** The line's newest point is always at the right end, x ≈ 132 px. It is drawn as a **glowing dot**: white core r≈1.5–2 px plus a soft glow r≈5–6 px (≈x3 @1080).

### Line behaviour
- **Mechanism: an ECG/oscilloscope-style scroll.** History scrolls left at **≈1.0–1.1 px per sample**. I measured this by tracking the phone spike peak: x ≈ 127.7 (190) → 122.7 (194) → 117.7 (199).
  - That is ≈10 px/s @640, which is **≈1 px per frame at 30 fps @1920** (30 px/s).
  - With ≈110 px of plot width, the visible window is **≈11 s of history**.
- **Line style.** White/very light grey #E8E8E8, ≈1.5 px (≈4–5 px @1080). Slightly irregular, hand-drawn quality. Rounded joins.

| Samples | Story action | Line behaviour | Head color |
|---|---|---|---|
| 100–120 | running in the park | **Healthy baseline.** Gentle sine-like waves, amplitude ≈±3–4 px (≈±10 px @1080), wavelength ≈25–30 px (≈2.5–3 s period). Uneven, organic. | white |
| 121–129 | still running (no visible new action) | Small **upward tick** of the newest segment, about +3–4 px above the wave mean. | **pink/magenta ≈#FF4FA8 with pink glow** (121–128), white again by 129 |
| 130–152 | kite with friend | Same gentle waves, scrolling | white |
| 153–159 | kite, then fading out | Another small rise | **pink** again (153–159) |
| 160–171 | painting (dark studio) | Gentle waves continue. The amplitude looks slightly lower (?) | white |
| **172–183** | **phone buzzes; hero turns, reaches, picks up** | **The line goes FLAT.** A dead-straight horizontal segment starts ≈172 and grows to ≈12 px by 183. The calm "natural" wave stops the instant the phone buzzes. | white |
| **184–186** | phone at face, sparkle burst, heart +1 | **Sharp spike.** The line jumps up ≈10–12 px (≈3x the healthy amplitude) within 1–2 samples. | **pink/magenta glow** (184–186) |
| 187–199 | holding phone, heart floating, then fading | The spike peak scrolls left, **and the peak segment stays tinted pink**. After the peak the line **drops sharply to below the old baseline** (≈4–6 px under it) and continues low. That is the crash dip. | head white from ≈188 |

Interpretation, for reuse:
- Natural joys (running, friend, kite) produce **small rounded pink-tipped bumps** on a lively wave.
- The phone produces a **dead flatline (craving), then a tall sharp spike, then a dip below baseline**.
- Colour coding: **pink = a dopamine release happening now**. Rises tint the head pink, and the spike segment keeps its pink tint as it scrolls away.
- A frame range outside mine (≈278–299, seen in a shared scratch crop) shows that **later a dashed horizontal baseline appears in the HUD** and spikes keep pink peaks. **No dashed baseline exists in 100–199.** It is introduced later as a "normal level" reference.

### Clock
- **There is no clock in samples 100–199** (top-right is empty in all three shots).

---

## 4. Character motion breakdown

### 4a. Run cycle (S1, 100–129)
- **Screen position.** The hero is pinned at **x ≈ 46% (≈295 px)**. Feet are on the ground line at y ≈ 265 px (≈73.6% H). The world scrolls; the character does not travel.
- **Size.** Head-top y ≈148 to feet y ≈265, so ≈117 px ≈ **32.5% of frame height** (≈39% of the active picture).
- **Cycle period: 6 samples = 0.6 s = 18 frames @30fps** (two steps of 9 frames). The pattern was consistent for 5 cycles. "Passing" poses fall at 100, 103, 106, 109, 112, 115(?), 118/119, 122, 125, 128.
  - Near (cream) leg trails back at 101–102, 107–108, 113–114, 120–121, 126–127.
  - Far (grey) leg trails back at 104–105, 110–111, 116–117, 123–124, 129.
  - Aliasing check: the poses progress monotonically (back, then passing, then opposite back), so this is not a reverse-aliased faster cycle (?, low risk).
- **Pose key list (per half-cycle):**
  1. **Contact/stride.** Rear leg extended diagonally back about 45°, foot toe-down. Front leg nearly vertical, slightly bent.
  2. **Stride hold.** Same shape on the next sample.
  3. **Passing.** Rear leg swings forward with the knee raised and the lower leg folded back. The support leg is vertical.
- **Lean.** Torso tilted forward ≈5–8°. The head stays upright-ish because head and body are one bean.
- **Bounce.** Very small: head-top y varies about 148–150 px (≈2 px, ≈6 px @1080). Highest at passing. **The bounce is almost nil**, which reads light and floaty.
- **Arm swing.**
  - The near arm is a bent L (elbow ≈90°). It pumps from fist-forward at chest height (101–102) to elbow-back with the fist near the hip (104–105, 110–111).
  - The far arm is mostly hidden behind the torso, with a grey sliver visible.
  - Arms are counter-phase to the legs.
- **Far limbs = the SAME cream color at ≈55–60% opacity, not a separate grey.**
  - On the green ground the far leg samples #A2B599, which is a greenish mix, so it is translucent.
  - In the dark studio it reads ≈#8A8A86, which is cream at ≈60% over black.
  - This differs from the BRIEF's "darker grey shade".
- **Outlines: only the near limbs are outlined.** They get a dark #1a1a1a stroke, ≈1.5 px (≈4–5 px @1080). The torso/head bean has **no outline**, and neither do the far limbs.
- **Face during the run.** Flat confident brows tilted slightly inward, dot eyes, and a **open D-shaped smile with a pink tongue** (#E07070-ish). The face does not change during the run.
- **Foot sliding.** Ground flowers move ≈16–17 px/sample, i.e. ≈100 px per 0.6 s cycle, so ≈50 px per step. The leg span at max stride is ≈55–60 px, so foot slip is small but probably not perfectly locked (?).

### 4b. Parallax pan (S1). Measured on a 2x stacked crop of samples 110–113.

| Layer | Speed (px/sample @640) | @1920 per 30fps frame | Notes |
|---|---|---|---|
| Sun | 0 | 0 | fixed at ≈(503, 85) = 78.6% x, 23.6% y |
| Clouds | ≈0–0.5 | ≈0–0.5 | nearly static, slow left drift (≈7 px over 13 samples) |
| Birds (3 "v" marks) | ≈+1 (drift **right**/up) | ≈+1 | flap slightly, drift opposite to the scroll, so they read as flying |
| Hills (2 layered green bands) | ≈3–5 (?) | ≈3–5 | low-contrast. Hard to measure: cross-correlation was noisy |
| Trees (tiled, trunks spaced exactly 140 px ≈ 21.9% W) | **≈13–14.5** (e.g. trunk 248→222→193→165 at 2x) | **≈14** | uniform spacing, so a looped tile |
| Ground flowers / ground plane | **≈16–17.5** | **≈17** | foreground, fastest |
| Ground line (y≈268) | n/a | n/a | a straight, infinitely long horizontal stroke, so scrolling is invisible |

- The tree tile repeats every 140 px. At 14 px/sample that is a 1.0 s loop; at 1920 the tile is 420 px.
- Trees vary slightly in canopy shape, but placement is a strict grid.

### 4c. Greeting / waving (S2)
- **The script's "they raise their hands and greet joyfully" is NOT animated in these frames.** Instead there is a hard cut to an already-composed **static two-shot hold** (130–157, 2.8 s). Character poses are identical across all 28 samples. Only the kite, its tail and the clouds move.
- **Hero (left, x ≈ 42%):**
  - Near arm raised overhead, bent at the elbow, hand up, holding the kite string. This doubles as a wave gesture.
  - Far arm hidden.
  - Legs straight, feet planted. The far leg is the translucent cream.
  - **Face: relaxed, content, heavy-lidded.** Dot eyes under a straight upper-lid line, flat brows, small open smile with a pink tongue.
- **Friend (right, x ≈ 55%).** Angled toward the hero. Near arm reaches across horizontally toward the hero's chest/raised arm (a touch or high-five gesture (?)). Same content face, half-lidded.

### 4d. Second character design: friend with the yellow cap
- **Body.** Identical bean rig and proportions to the hero, but **darker tan/beige skin: ≈#D7C1A9–#D7C5AF** (hero ≈#DEDBCC–#E1DDD1). Recolouring is the only body differentiation, with the same height.
- **Hat.** A **yellow hard-hat / bowl cap** with a small knob on top, ≈#F4BC29, with a lighter highlight and a darker orange underside rim. It sits low on the forehead, covering the head-top. It reads more like a construction helmet than a baseball cap.
- **Face.** Same face kit, half-lidded relaxed eyes with lid line, small open smile.
- **Rig.** Same rules: outlined near limbs, translucent far limbs, no torso outline.
- **Takeaway: secondary characters = hero rig + skin tint + ONE accessory in a saturated colour.**

### 4e. Kite animation (S2)
- **Kite.**
  - Diamond (rhombus) ≈ 30x45 px, center ≈ (440, 85), i.e. 69% x, 24% y.
  - Fill **orange-red ≈#FF5A3C–#F04A2A**, with yellow-orange cross spars and a thin dark outline.
  - Motion: it bobs ±2–3 px and rotates a few degrees. Centre wanders slightly: (440, 85) at 130, (443, 82) at 139, (445, 83) at 145. Slow and continuous.
- **Tail.** A thin **blue wavy line** hanging down ≈70 px, with 4–5 small coloured bows/dots (orange, green, purple, blue). It **sways left-right like a pendulum or sine wave** (bottom tip x swings ≈435–448 px), so the tail is animated as a wave.
- **String.** A thin white line, ≈1 px (≈3 px @1080). It runs from the hero's raised hand (≈300, 160) to the kite's bottom vertex with a slight downward sag. The kite end follows the bob.

### 4f. Studio sequence (S3, 161–199)

| Samples | Action | Expression |
|---|---|---|
| 161–171 | Hero faces right toward the easel. Holds the **palette** (tan oval with red/orange/yellow/green/blue dots) at the hip and a **brush** (thin brown stick, blue tip) in the near hand. Small strokes: the brush tip moves ≈5–10 px between samples. | calm, focused (flat brows, small smile) |
| 172–173 | Phone buzzes: blue radial glow (radius ≈45 px), magenta vibration ticks. The hero keeps painting for 2 samples. | unchanged |
| 174–177 | **Snap pose change** (no in-between at 10 fps): the hero now faces front-left, arms folded in front (one hand at the chest). Looks toward the phone. | **surprised/alert**: raised brows, round dot eyes, small "o" mouth |
| 178–180 | Leans forward and reaches with the near arm to the phone on the stool (hand on the phone at 179–180). | same "o" face |
| 181 | Phone lifted to chest height in the hand (phone now vertical, screen gradient pink→blue). Starts to smile. | slight smile |
| 182–183 | Phone held up to the face. **The phone glow halo moves with the phone** and lights the face blue-white. | smile, eyes on the phone |
| 184–186 | **Dopamine hit.** Burst of 4-point sparkles (cyan, pink, yellow, orange, ≈6–10 px), heart and +1. **Eyes become glowing teal/cyan rings** (screen-hypnotised). HUD spike. | wide hooked grin, cyan ring eyes |
| 187–199 | Holding the pose (static hold ≈1.3 s). Sparkles fade out by ≈193. The heart floats up and fades. The camera pan settles. | same grin with cyan eyes. Rendered as eyes only, without a mouth change |

---

## 5. Environment & colour

### Daylight park (S1, S2). Sampled hex values.
- **Sky.** A vertical gradient, darker blue at the top (#62A4F0 at y=40) to lighter (#79B4F6 at y=120). Edges are darkened by the vignette (#6D98C5, #718FB5). There is a light haze/glare near the horizon on the right side.
- **Sun.** A flat pale-yellow disc, **#FFECA7**, r≈22 px (≈3.4% W). Soft edge, faint glow, static.
- **Clouds.** Flat white/very light grey (#F4F7FB) elongated ellipses with feathered edges, 2–4 per shot.
- **Birds.** 3 dark-grey "v" strokes.
- **Hills.** Two rolling bands. Back band ≈#4E9A62, front band ≈#429359 / #3F8F57, with a lighter rim between them. Low contrast against the trees.
- **Trees.** Canopy of 2–3 overlapping circles in **#2B702F** (dark) and ≈#3A8A3E (light), with brushy/feathered edges. Thin straight trunk **#784526**. Height ≈75 px (top ≈148, base on the ground line at 268).
- **Ground.**
  - Flat green **#408F56 → #3E984E** below a **thin dark ground line** (#1E1E1E, ≈1 px).
  - The ground has **sparse confetti-like flower dots** (2–3 px) in yellow, orange, red, pink, purple and blue. They are randomly scattered, densest at y ≈ 275–325.
  - Some dots glint, so they may twinkle (?).
- **Overall feel.** A saturated "kids-book" palette with full colour everywhere.

### Dark studio (S3)
- **Wall/floor.** Near-black **#0B0B0B**, the same value above and below a thin grey floor line at y≈265. Edges vignette to #050505.
- **Light wedge.** A diagonal light beam from the window to the floor around the easel (≈+8–12 luma).
- **Props:**
  - **Framed poster** (left wall): a light-grey outlined rounded rectangle, dark navy inside, **orange sun #C56F22** over three blue wave lines (a sea sunset).
  - **Shelf** with a rainbow row of pill/oval shapes (books or paint tubes?): red, orange, yellow, green, blue, purple, pink, orange. A white ball at the end. Brown shelf board.
  - **Window** (top-right): brown frame with cross mullions, blue sky **#8FC0F8**, yellow sun, white cloud, green hills.
  - **Easel and canvas.** Wooden easel. The **canvas painting replicates the park**: blue sky, yellow sun #FDC83E, green hills, orange field #D07E2C with confetti flower dots. It is a visual callback.
  - **Plant**: terracotta pot #A7562B with spiky green stems ending in round bulbs.
  - **Stool**: thin brown, holding the phone.
  - **Guitar**: acoustic, at the far-left wall, revealed by the pan from ≈180.
  - **Orange object** cut off at the left edge (≈x 0, y 240): the guitar body.
- **Phone.** A dark bezel with a **pink→blue (#FF5FA0→#5A7BFF) gradient screen**. When active it carries a **blue radial halo** (≈#2A4A70 at the edge, transparent at the falloff). The halo lights nearby surfaces.

**Contrast logic.**
- Even the "dark" studio is in a positive, creative state: colour lives only in the hobby props (paintings, books, plant, guitar), on a black void.
- The daylight scenes are fully saturated.
- The phone introduces a **new, artificial colour family (neon pink/cyan/blue glow)** that is not in the warm hobby palette. This sets up the later "colour loss".

---

## 6. Camera
- **S1:** locked camera. The run is pure layer scrolling (parallax) with the character pinned.
- **S2:** locked. Possibly a 1-sample scale settle at the cut: at 130 the trees sit ≈3% further out than at 131, i.e. a tiny zoom-out ease (?).
- **S3:**
  - 161–171 locked.
  - **172–190: slow truck/pan left.** All background elements shift right by ≈2–3 px per sample. Totals 171→193: window 445→485 (+40 px), easel +37, poster +31.
  - That is ≈6% of width over ≈1.9 s, ease-in-out, stopping ≈190–193.
  - There may be a very slight zoom-in, since the poster width grew 68→72 px while the height stayed the same (?).
  - The pan follows the hero's attention toward the phone and reveals the guitar at the left.
- **HUD is screen-space.** It is unaffected by camera moves and by the dip-to-black (line and label stay bright at 159–160).

---

## 7. Pacing stats (samples 100–199 = 10.0 s)
- Shots: 3 (S1 ≥3.0 s, S2 ≈2.8 s + fade, S3 ≥3.9 s). Mean ≈3.2 s per shot.
- Transitions: 1 hard cut (action → social), 1 dip-to-black ≈0.5 s total (social → indoors). There is no on-screen text, so story beats are carried by picture and HUD only.
- Long holds: S2 is a 2.8 s near-static hold, and 187–199 is a 1.3 s hold after the phone hit. Holds let the HUD and particles "speak".
- Beat density:
  - ≈1 story beat per 2.5 s: run, friend/kite, painting, buzz, grab, hit.
  - HUD events: 3 in 10 s (small bump 121, small bump 153, flatline 172→spike 184).
- **Sound-design implication (?)**: the pink HUD bumps at 121 and 153 do not coincide with visible actions. They may be synced to music accents.

---

## 8. NEW / MISSED DETAILS vs BRIEF and script
1. **Letterbox ≈2.15:1** (top and bottom bars ≈8.6% each). The **HUD panel's top edge touches the letterbox bar**. Rebuild this exactly: the "letterbox-ish top bar" in the BRIEF is a real bar on both top and bottom.
2. **Far limbs are translucent cream (≈55–60% opacity), not a separate grey**, and **only near limbs are outlined**. The torso/head has no outline.
3. **Run cycle = 0.6 s (18 f @30)** with **almost no vertical bounce** (≈2 px @640) and a slight lean. The character is pinned at 46% x.
4. **Parallax speeds** (px/frame @1920/30fps): trees ≈14, ground flowers ≈17, hills ≈3–5 (?), clouds ≈0–0.5, sun 0. Birds drift the opposite way (+1). The tree layer is a **140-px (@640) uniform tile**.
5. **The greeting is not animated.** The script implies hands raised in greeting, but the film cuts to a static 2.8 s hold. Only the kite (bob plus sine-swaying tail), clouds and HUD move. This is a big production shortcut worth copying.
6. **Friend design = hero rig + darker tan skin (#D7C1A9) + yellow hard-hat with a knob (#F4BC29)**, not a baseball cap.
7. **HUD mechanics:**
   - The scroll speed is ≈1 px/frame @1920/30fps, giving an ≈11 s visible window.
   - The write head is a glowing dot.
   - **The head turns pink while dopamine rises, and spike segments stay pink as they scroll.**
   - **The line flatlines from the moment the phone buzzes until the hit.** Then comes a tall spike (≈3x the natural amplitude), then a **dip below baseline**. The crash is already visible here, within seconds of the first hit.
   - Small natural pink bumps happen during the run and kite (121, 153).
8. **The HUD survives transitions.** It is not faded by the dip-to-black, so it is a persistent overlay from the start.
9. **No clock** in this range. **No dashed baseline yet.** One appears later (≈278+, seen in another range's crop).
10. **Dip-to-black** between the park and the studio: ≈0.3 s out (ease-in), ≈0.2 s in.
11. **The studio is not "dark = sad".** It is a black void with colourful hobby props: rainbow shelf, sea-sunset poster, window, painting, plant, guitar. **The canvas painting replicates the park scene**, which is a motif link (the painting can later lose colour).
12. **The phone is pre-planted.** It is visible on the stool with a **red badge** from 161, before it buzzes at 172. The buzz glyph is magenta tick marks plus a blue radial glow, not a shaking phone.
13. **Snap-pose acting.** Painting → turned/surprised at 174 with no visible in-between at 10 fps. The pose likely changes within ≤3 frames @30. The "o"-mouth surprise face is a reusable expression.
14. **The phone glow is a moving light.** The halo follows the phone and tints the face.
15. **The dopamine reward has a full grammar:**
    - sparkle burst of 4-point stars in cyan, pink, yellow and orange
    - heart #FD4C76 and white "+1" floating up with ease-out over ≈0.9 s, holding, then fading over ≈0.5 s
    - **eyes switch to glowing teal/cyan rings** (hypnotised)
    - synchronized HUD spike
16. **The camera moves in the studio.** There is a slow ease-in-out pan left (≈6% width over ≈1.9 s) during the phone pickup. The script says "fixed".
17. **Timing correction vs script.** The kite meeting starts exactly at 13.0 s. The phone notification is at **17.2 s** and the first hit at **18.4 s**, which the script lumps into 0:15–0:40.

---

## 9. Rebuild notes (Remotion, 1920x1080 @30fps)

**Timeline (@30fps):**

| Frames | Event |
|---|---|
| ≤300–389 | Run |
| 390 | Cut to kite hold (to 479) |
| 474–482 | Fade to black |
| 482–488 | Fade in studio |
| 516 | Phone buzz |
| 522 | Turn (snap) |
| 534–540 | Reach |
| 543 | Phone in hand |
| 546–549 | Phone to face |
| 552 | Sparkles, heart and HUD spike |
| 555–579 | Heart floats up |
| 585–597 | Heart fades |
| 516–570 | Camera pan (ease in-out) |

**Letterbox.** Two black `<rect>`s, height 93 px, top and bottom. Draw all scene content inside y = 93–987.

**Parallax.** Each layer is a `<g>` with `transform={`translate(${-(frame*speed) % tileW}, 0)`}`. Render two or three tile copies side by side so the loop is seamless.
- Speeds in px per frame: sky/sun 0, clouds 0.3, hills 4, trees 14 (tileW = 420, one tree per tile with small per-index canopy variation from a seeded random), flowers/ground 17 (tileW ≈ 1920, seeded dot scatter).
- Ground line: a static full-width stroke at y≈804.
- Birds: x = base + 1·frame, with a flap from `Math.sin(frame*0.8)` on the wing angle.

**Run cycle** (character pinned at x≈880, feet at y≈795, height ≈350 px):
- `phase = (frame % 18) / 18`
- Hip angles: near leg `thigh = 35*sin(2π·phase)`, far leg the same with +π.
- Knee: `knee = max(0, 60*sin(2π·phase + π/2))`, which folds the lower leg back during the passing pose.
- Arms counter-phase: shoulder `±40°`, elbow fixed at ≈90°.
- Torso lean: `rotate(6°)` about the hip.
- Bob: `translateY(-3*|sin(2π·phase)|)` px @1080 (keep it tiny).

**Rig rules:**
- Near limbs: cream fill plus dark stroke 4–5 px with round caps.
- Far limbs: the same path with `opacity 0.58` and no stroke, drawn behind the body.
- Body bean: no stroke.
- Expressions: `content` (lid line plus dots), `confident` (inward brows plus D-smile with pink tongue), `surprised` (raised brows plus "o"), `hooked` (cyan glowing ring eyes plus grin).

**Secondary character.** Use the same component with props `skin="#D7C1A9"` and `accessory="hardhat"` (#F4BC29).

**Kite:**
- Position `y = base + 6*sin(frame*0.12)`, rotation `3*sin(frame*0.09)`.
- Tail: a polyline where point i has `x = 6*sin(frame*0.15 - i*0.6)`, with bows at fixed indices.
- String: a quadratic curve from the hero's hand to the kite vertex, with a sag control point.

**HUD (screen-space, top-level, outside any fade):**
- Panel at x 58, y 93, w 326, h 150, rx 12, fill `rgba(0,0,0,0.55)`.
- Label "DOPAMINE" at (68, 112), 18 px, #A8A8A8, letter-spacing 1 px.
- Generate the line from a **data function `level(t)`**: natural noise wave (amplitude 10, period ≈85 frames) plus scripted events. Events: a bump at 363 and 459 (+10, pink); flat from 516; a spike at 552 (+33 within 3–6 frames, pink); then decay to −15 over ≈30 frames.
- Draw the last ≈330 frames of history mapped onto 330 px of width (1 px per frame), newest at the right.
- Colour each segment pink (#FF4FA8) when its local slope is above a threshold or it belongs to an event; otherwise #E8E8E8.
- Head: a circle r 5 plus a blur glow r 16. Pink while rising.

**Dip-to-black.** A full-screen black rect *below* the HUD layer. Opacity 0→1 over 474–480 with ease-in, then 1→0 over 482–488.

**Phone:**
- `<rect>` with a linear-gradient screen (pink→blue).
- Red badge circle.
- When `buzz`: a radial-gradient halo (r 135, #3A6AA0 at 0.45 → 0) plus two pairs of magenta ticks.
- The halo is a child of the phone transform, so it follows the hand.

**Reward particles:**
- 8–12 four-point stars, seeded, spawned at the phone, drifting outward 1–2 px/frame, twinkle (scale `sin`), fade over 25 frames.
- Heart plus "+1": `y = interpolate(f,[552,579],[384,249],{easing: Easing.out(Easing.cubic)})`, then opacity `interpolate(f,[585,600],[1,0])`.

**Camera pan.** Wrap the scene (not the HUD) in a `<g transform=translate(camX)>` with `camX = interpolate(f,[516,570],[0,120],{easing: Easing.inOut(Easing.cubic)})` px @1920. Optionally add a scale of 1→1.03.

**Snap poses.** Swap pose presets on a single frame (or with a 2–3 frame interpolation) rather than full tweening. This matches the observed blocky, "limited animation" acting.
