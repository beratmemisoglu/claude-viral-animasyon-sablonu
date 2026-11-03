# dmscales: motion, animation and editing spec (measured)

Scope: motion, timing, cut grammar and sync to the narration. Visual design and script/audio are covered in other reports.
Every number here was measured from the local files. Paths are relative to `research/dmscales/`.

- Per-frame features at native fps (ink share, red share, changed-pixel share, ink bbox and centroid) for every frame of all 5 videos:
  `work/motion/feat_<id>.npy` (made by `work/motion/feat.py`). Change events: `work/motion/events.json`. Scene changes:
  `work/motion/scenes.json`.
- Scripts: `events.py` (event detection and word sync), `cutgram2.py` (transition types and shot lengths), `sentsync.py`
  (cuts vs clause starts), `popsync.py`, `drift.py` (camera and continuous motion), `trace.py <id> <t0> <t1> [step]`
  (per-frame numbers), `redtrack.py` (full-res tracking of red pixels and ink), `tile.sh` (full-fps contact tiles).
- Full-fps tiles made for this report: `work/motion/*.jpg` (named below).
- Word times come from the YouTube auto-captions (`videos/<id>.en.vtt`, `<00:00:01.234><c>` tags). They are typically
  accurate to about ±100 ms, so read any lead or lag under 100 ms as "on the word".

## 0. Source facts that change the build

| video | date | views | size | fps | runtime |
|---|---|---|---|---|---|
| N-q-XLQymnU "Shorts algorithm in 180 s" | 2026-04-01 | 705K | 1440x1080 | 60 | 179 s |
| -fS8na576Jc "Longform algorithm in 300 s" | 2026-04-14 | 368K | 1440x1080 | 60 | 300 s |
| AGkRkNuhO_o "TikTok algorithm in 120 s" | 2026-05-04 | 30K | 1440x1080 | 60 | 120 s |
| EQUn6IVAgCg "10,000 hours in 16 min" | 2026-05-16 | 99K | 1440x1080 | 30 | 977 s |
| VQvIV__toUk "blow up a channel" | 2026-06-13 | 43K | 1440x1080 | 60 | 337 s |

- **All five videos are 4:3, 1440x1080, including the "Shorts" explainer.** None is vertical. The Shorts video is a
  landscape explainer *about* Shorts, so there is no separate vertical grammar to copy. (A vertical version would be our own
  adaptation; see section 10.)
- **Render at 60 fps.** Pops land on single 60 fps frames. EQUn6 is the only 30 fps file.
- There are three motion "dialects". The two most-viewed videos use the plainest one:
  - **A. "Pop" (N-q, fS8; the core style).** Static canvas, elements hard-pop on the word, about 1 short fade per scene
    change, almost no continuous motion. Continuous motion makes up 7% of N-q's runtime and 16% of fS8's
    (`drift.py`).
  - **B. "Kinetic type" (AGkRk).** Every word fades and rises into place, and figures enter with a bounce. Continuous
    motion: 56% of runtime.
  - **C. "AE heavy" (VQvIV).** Slams with zoom blur, shape bursts, whip and pinch transitions, red flashes, a camera that
    flies through and follows a line as it draws. Continuous motion: 42% of runtime.
  - **EQUn6** is dialect A plus Minecraft gameplay b-roll as filler. Moving footage fills 62% of its runtime.

  **Recommendation:** default to A, with B's word entrance as an option (`textMode: "pop" | "kinetic"`) and a small set of
  C accents for the hook and section openers.

## 1. Text entrance

### 1a. Pop (dialect A default): one frame, no animation
- Bullets, sub-lines and keywords added to an existing scene appear in **1 frame (16.7 ms)**: 0% to 100% opacity, no
  scale and no move.
  - N-q 16.20 "- aged channel (...)": ink share 0.9% to 2.9% in one frame. N-q 16.87 "- older email": one frame.
    N-q 19.57 "- enable third level feature eligibility": one frame.
  - fS8 13.83 / 14.90 / 15.97 / 17.57: the "Warm up / Brand / Use A Trusted Email / Enable 3rd Level" list items are each a
    one-frame pop (`trace.py -fS8na576Jc 11.5 19.5`).
- Share of events: in N-q, 67% of all visible-change events are a single frame and 77% are 3 frames or fewer. In fS8 the
  figures are 61% and 66% (`events.py`).
- Pop rate inside a scene (1-2 frame events under 12% of the frame): N-q 23/min, fS8 43/min, VQvIV 30/min.

### 1b. Section title or first line (dialect A/C): character cascade, 6 to 10 frames
- A heading that opens a scene types itself in **per character**. Each glyph fades from 0 to 1 with about 2 frames of
  stagger, starts slightly rotated and offset, and settles.
- The order varies:
  - right-to-left: N-q 15.07 "HOW TO FIX:", where "X:" appears first and "HOW TO FIX:" is complete at 15.20;
  - left-to-right: VQvIV 94.30 "YOU'RE TARGETING";
  - centre-out: fS8 11.80 "HOW TO GET YOUR VID IN THE ALGO:".
- Visible within **8 frames (0.13 s)**. The line then keeps drifting up about 40 px (N-q: bbox top 540 to 498) and
  levels out from about 2-3 degrees of tilt, over 15 more frames, with ease-out. Total about 26 frames (0.43 s).
  - Tile: `work/motion/nq_howtofix.jpg`, rows 3-5. Numbers: `trace.py N-q-XLQymnU 14.8 16.6 2`.
- VQvIV opening word "all" (0.05 to 0.15 s): characters cascade right-to-left with a fade and about 8 degrees of rotation
  over **6 frames**. The next words "it" (0.300) and "takes" (0.467) then **pop in 1 frame**. Tile:
  `work/motion/vq_open.jpg`.
- **Rule:** the first word or line of a scene gets the cascade. Every later word in that line pops.

### 1c. Kinetic word (dialect B, AGkRk): fade plus rise, 30 frames
- Each word enters on its own cue word. Measured on the red word "people", AGkRk 37.60 to 38.10, at full resolution
  (`redtrack.py AGkRkNuhO_o 37.5 0.9`):
  - **rise:** 67 px (6.2% of frame height) from below. Centroid y per 2 frames: 597, 584, 572, 564, 556, 550, 545, 541,
    537, 534, 532, 531, 530. That is ease-out quad: 50% of the travel after 8 of 30 frames. **Duration 30 frames
    (0.5 s).**
  - **opacity:** 0 to 1 over the same 30 frames, ease-out. Red saturation 84 to 168.
  - **x:** no horizontal travel. The line re-centres by 4 px as later words land.
- Words on the second line start further down and to the right, and the line re-centres as it fills ("for as long as
  possible" ends centred under line 1). Tile: `work/motion/ag_words.jpg`.
- Consecutive words overlap: a new word starts every 4 to 12 frames, so 2 to 4 words are in flight at once.

### 1d. Centre-out mask reveal (dialect C)
- VQvIV 2.38 to 2.67, "and everyone who says:": a soft-edged opacity mask opens symmetrically from the line's centre.
  The feather is about one word wide. **17 frames (0.28 s)**. Tile: `work/motion/vq_reveal.jpg`.
- It begins while the previous shot is still sliding out (overlap of about 2 frames).

### 1e. Re-layout when lines are added
- **Single line:** the line is centred and **re-centred instantly** on every popped word ("all it" then "all it takes",
  VQvIV 0.30 / 0.47).
- **Heading plus list ("HOW TO FIX:", "HOW TO GET YOUR VID IN THE ALGO:", "ZERO VIEW JAIL:")**: a fixed 3-step pattern.
  1. The heading arrives alone at the vertical centre (y about 528 in a 1080 frame).
  2. When the first sub-item is due, the heading **slides up linearly** (constant speed, no easing):
     - fS8 12.217 to 12.367: 10 frames, 258 px (about 25 px per frame), and scales from 1.00 to about 0.90 at the same
       time (`trace.py -fS8na576Jc 12.2 12.75 1`);
     - N-q 15.700 to 15.833: 8 frames, 150 px (about 19 px per frame), no scale.

     The slide finishes 0.15 to 0.37 s **before** the first sub-item appears.
  3. After that the **top edge is fixed**: items append below with 1-frame pops and nothing above moves (fS8 header top
     stays at y=246 from 12.4 to 19.1 s).
- **Staircase variant (VQvIV 10-12 s, "-no gatekeeping / -no courses / -no BS mentorship"; 23-24 s "generate / ideas /
  people / will / actually"):** each new line pops below the previous one, indented right by about 40-60 px. Nothing above
  moves.
- **Side-by-side re-layout:** when an image joins a centred text, the text slides sideways to make room.
  - VQvIV 18.80 to 18.95: text slides left about 340 px in about 9 frames, then the brain image enters on the right.
  - VQvIV 0.82: "all it takes" slides left while the phone screenshot drops in.
- **No grey-out.** Earlier lines never dim while new content arrives. Every "grey" or "pink" line in the contact sheets is
  a frame caught mid-fade on entry or exit (for example AGkRk 41 s, fS8 1 s, fS8 23 s).

## 2. Element entrances and exits (screenshots, images, figures, arrows, crowds)

| device | measured example | duration | curve |
|---|---|---|---|
| Hard pop (screenshots, logos, $ sign, icons) | N-q 21.20 dashboard screenshot; 45.40 / 45.97 / 46.63 screenshot stack | **1 frame** | none |
| Opacity fade-in of a screenshot | N-q 1.050-1.333 (onto the "how you'll appear" panel), fS8 1.49-1.77 | **17 frames (0.28 s)** | linear (changed-pixel share flat at about 17.5% per frame) |
| Slide-in from the frame edge (phone screenshot) | VQvIV 0.817-0.967: drops from the top edge, centroid y 157 to 538 | **10 frames (0.17 s)** | ease-out. Steps per frame: 58, 63, 61, 52, 41, 34, 40, 23, 9 px |
| Fly-in from the right plus push-left of the existing item | VQvIV 1.350-1.567: chart enters from the right with a fade, the phone shrinks to 0.83 and moves left | **14 frames (0.23 s)** | ease-out |
| Slide-out downward (whole group) | VQvIV 2.150-2.400: bbox top 162 to 522, accelerating (6, 6, 18, 18, 24, 30, 30 px) | **15 frames (0.25 s)** | ease-in, then cut |
| Scale-in "zoom pop" of a crowd drawing | VQvIV 22.17-22.42: width 474 to 774 px (0.61 to 1.0) | **15 frames (0.25 s)**, on 2s | ease-out, no overshoot |
| Elastic scale-in of a stick figure | AGkRk 37.08-37.48: height 0 to 308 (8 fr), back to 268 (6 fr), up to 316 (5 fr), settles at 318 | **24 frames (0.4 s)** | elastic: overshoot then damped bounce |
| Slam-in (huge to final) with zoom blur | VQvIV 20.333-20.467 "EXECUTION IS THE EASY PART": ink 37% of frame to 8% | **8 frames (0.13 s)**, on 2s | ease-out (exponential) plus radial blur |
| Camera fly-out reveal | VQvIV 94.13-94.43: starts inside a blurred point, pulls back with rotation to reveal 2 figures, which settle upright by 94.6 | **18 frames (0.3 s)** plus about 10 frames of settle | ease-out |
| Shape burst (circle, x, square, triangle confetti) | VQvIV 20.40-21.40: shapes start at the text edge, drift outward (bbox width 750 to 1150) while shrinking and fading (ink 8% to 1%) | **60 frames (1.0 s)** | exponential decay |
| Arrow | fS8 23.93-24.03: red area 12 to 13,187 px with the centroid sweeping from left to right (a wipe along the stroke), while opacity keeps rising to 24.17 | **wipe 6 frames (0.1 s)**, fade about 15 frames | ease-out |
| Live handwriting (EQUn6) | EQUn6 73.7-74.8: red loops accumulate in real time; then handwritten notes "I'm baseline", "space for another channel ???" (sheet `frames/EQUn6IVAgCg/sheets/sheet_0060s.jpg`, 74-80 s) | 1-3 s per annotation, real pen speed | none (a recorded drawing) |
| Line chart draw-on with camera follow | VQvIV 95.9-97.4: the green line's tip crosses 1440 px; green px added per 0.1 s: 6900, 5500, 4400, 3700, 3100, 2500, 2100, 1800, 1500, 1300 | **about 1.5 s** | ease-out, then the camera pulls back about 25% over 97.5-98.1 |
| Exit: whole-scene fade to white | N-q 14.85-15.02 ("ZERO VIEW JAIL" scene) | **11 frames (0.18 s)**, then 4 white frames | linear |
| Exit: crossfade under the incoming title | fS8 11.82-12.10: old scene fades while the new heading reveals over it | **17 frames** | linear |
| Exit: text fade plus figure shrink | N-q 0.917-1.10: text fades, the stick figure scales to about 0.9 and stays | **11 frames** | linear |
| Exit: chromatic split dissolve | VQvIV 22.98-23.25: crowd plus red X fade with an RGB (cyan/red) offset ghost | about 15 frames | linear |

- **Images idle-float.** The brain PNG floats continuously while on screen (VQvIV 19.0-20.3: about 3% of pixels change
  every frame, centroid drifts about 30 px). Screenshots never idle-move in N-q or fS8: their holds are pixel-identical.
- **Screenshot stack.** Screenshots pile up one per beat, each one popping in offset diagonally on top of the last.
  N-q 45.5 / 46.1 / 46.7: three 1-frame pops about 0.6 s apart. Tile: `work/motion/nq_crowd.jpg`.
- **Embedded footage plays.** Example Shorts play inside their card (N-q 85.3-89.3, `work/motion/nq_85.jpg`). The card
  later slides from the left to the top centre in about 6 frames as the text crossfades (87.4).

## 3. Camera

- **No Ken Burns or idle camera in dialect A.** N-q has only 5 continuous-motion runs of 1 s or more (12 s in total), all
  of them playing footage or brief settles. fS8 has 19 runs (49 s). Holds are fully static: N-q has 49 runs of 1 s or more
  with zero changed pixels.
- **No camera shake** anywhere.
- **Dialect C camera moves (VQvIV only), all short:**
  - **Punch/slam to text:** 8 frames, from roughly 3x to 1x scale, radial zoom blur (20.33).
  - **Fly-out reveal:** 18 frames with rotation (94.13).
  - **Push-in on a crowd with motion blur:** sheet `frames/VQvIV__toUk/sheets/sheet_0000s.jpg` at 28 s; the crowd fills the
    frame, blurred, in under 0.2 s.
  - **Follow-cam on a drawing line, then pull-back:** 95.9-98.1. The pull-back takes the scale down about 25% in 0.6 s,
    ease-in-out.
  - **Whip/pinch transitions:** 21.42-22.17, `frames/VQvIV__toUk/motion/motion_0019.83s.jpg`. The text squashes with
    horizontal blur, the next screenshot grows out of a barrel/pinch distortion (0.4 s), then pinches out to the crowd.
  - **Viewfinder overlay:** a black frame with white corner brackets around a thumbnail
    (`frames/VQvIV__toUk/sheets/sheet_0120s.jpg`, 148-149 s).

## 4. Cut grammar

Here a "scene change" is a frame-to-frame change of 12% of the frame or more, and its "core" is the run of frames at 30%
of the peak change or more (`cutgram2.py`). "Visible events" means every change of 0.4% of the frame or more, which
includes pops (`events.py`).

| video | scene changes/min | hard (1-frame core) | gradual (>6 fr) | interval p10 / median / p90 (s) | visible events/min | first 15 s events/min | in continuous motion |
|---|---|---|---|---|---|---|---|
| N-q (Shorts algo) | **23.1** | **86%** | 12% | 0.70 / **1.97** / 4.99 | 56 | **108** | 7% |
| fS8 (Longform algo) | 15.6 | 58% | 36% | 1.26 / **2.97** / 5.97 | 75 | 40 | 16% |
| VQvIV | 20.3 | 80% | 15% | 0.88 / 2.05 / 5.98 | 69 | 96 | 42% |
| AGkRk | 6.5 | 8% | 69% | 2.75 / 7.95 / 14.32 | 55 | 24 | 56% |
| EQUn6 (30 fps) | 9.5 | 47% | 35% | 0.22 / 2.93 / 16.45 | 25 | 48 | 72% (footage) |

- Transitions are hard cuts or short linear fades/crossfades (11-17 frames). Wipes, pushes and whips appear only in
  VQvIV.
  - Dips through white: N-q 1, fS8 5, VQvIV 9.
  - Full-frame red flash: 1 frame of solid red, then about 10 frames of red-to-white decay under a scaled-down red
    circle-X (VQvIV 22.55).
- ffmpeg's scene detector (`frames/<id>/cuts.txt`) undercounts the fades and overcounts VQvIV's flicker clusters (many
  0.03-0.04 s gaps). Use the table above.
- **Hook density:** N-q runs 108 visible events/min in the first 15 s against 51/min for the rest. VQvIV runs 96 against
  68. fS8 and AGkRk do not front-load.
- **Targets for the dmscales style (dialect A):**
  - scene change every **2.0 s median** (p10 0.7 s, p90 5 s), about **20-23 per minute**;
  - **55-75 visible changes per minute** (one new element about every 0.8-1.1 s);
  - first 15 s at about **100 per minute**;
  - **85% of scene changes hard**; the rest 11-17 frame linear fades;
  - no hold longer than 6 s without a pop.

## 5. Sync to narration

- **Scene changes land on clause starts.** A "clause start" is the first word after a word ending in `. , ? ! :`
  (`sentsync.py`).
  - Median distance from a hard scene change to the nearest clause start: N-q 88 ms, fS8 123 ms, VQvIV 117 ms,
    EQUn6 100 ms. For a random time it is about 500-576 ms.
  - Within 250 ms: 60-74% of scene changes, against 25-27% at random.
  - **The signed offset for all 204 matched cuts is +67 ms (IQR 0 to +107 ms).** The cut lands on the first word of the new
    clause or 1 to 6 frames after it.
  - Examples (N-q): "To"@14.84 → 14.85 (fade starts); "but"@18.40 → 18.47; "This"@21.12 → 21.20; "All"@24.84 → 24.90;
    "YouTube"@36.56 → 36.63; "People"@39.20 → 39.30; "Every"@45.28 → 45.40.
- **Keyword pops land on their word, 0 to +100 ms.** For N-q's in-scene pops, 59% fall 0-100 ms after the nearest word
  onset, against 41% at random (`popsync.py`). The bias is the same in the other videos but weaker.
  - Examples: "aged"@16.16 → 16.20 (+40); "enable"@19.44 → 19.57 (+130); "older"@16.96 → 16.87 (-90); "trust"@26.56 →
    "TRUST SCORE:" 26.43 (-130); "it"@0.28 → 0.30 (+20); "takes"@0.36 → 0.47 (+107); fS8 "Warm"@13.96 → 13.83 (-130);
    "use"@15.84 → 15.97 (+130).
  - **Rule:** pop on the cue word's onset, ±2 frames. The on-screen words copy the spoken words verbatim.
- **Animated words start early.**
  - Kinetic words (AGkRk) become visible **0 to 330 ms before** the word: "keeping" +80, "people" +40, "on" -107,
    "the" -90, "app" -73, "long" -190, "possible" -240 ms.
  - Cascaded titles in VQvIV lead by 180-330 ms: "two" -180, "different" -180, "audiences" -330.
  - **Rule:** for a 30-frame entrance, start it about 150 ms before the word so that it is legible at the onset.
- **Pre-roll for heading lists:** the heading slide-up (1e) runs 0.15-0.37 s before the first bullet's word, and the
  bullet pops on its word.
- **Figures and images arrive in the pause before their clause.** The AGkRk figure appears at 37.08: after "thing:"@36.96,
  before "keeping"@37.32.
- **Holds:** everything on screen holds until the next clause cut. Median gap between visible events: N-q 0.75 s (p90
  1.97 s), fS8 0.25 s, VQvIV 0.18 s.

## 6. Character, crowd and arrow animation

- **Stick figures are static raster cut-outs.** There is no line boil and no frame-to-frame redraw wobble.
  - Holds are pixel-identical: N-q 0-0.9 s, and the AGkRk figure after 37.5 s.
  - The N-q and fS8 figures sit on a white rectangle (an image with a background).
  - No limb animation was found in any video. Expression changes are separate drawings swapped by cut.
- Figure motion is transform-only: elastic scale-in (AGkRk, 24 frames), shrink to 0.9 when the scene changes (N-q 0.92),
  or settling from a tilt after a camera fly-out (VQvIV 94.4-94.9, about 10 degrees to 0 over about 30 frames).
- **Crowds are a single scribbled drawing** (an overlapping cluster of about 15 heads). They do not multiply, scroll or
  scatter.
  - Entrance: scale-in 0.61 to 1.0 in 15 frames (VQvIV 22.17), or a hard cut.
  - Negation: a red X slams on with a full-frame red flash (22.55).
  - Exit: RGB-split dissolve (22.98).
  - Also used as a full-frame blurred push-in (VQvIV 28 s).
- **Arrows:** hand-drawn red curved arrows. They enter with a fast wipe along the stroke (6 frames) plus a fade of about
  15 frames (fS8 23.93), or they pop. Once placed they are static.
- **Icons and emoji** (light bulb, $ sign, TikTok and IG logos, a group icon) hard-pop. The VQvIV hook's light bulb comes
  with a small burst.

## 7. Frame rate of the animation

- **Delivered at 60 fps, animated on 1s** for transforms and fades in N-q, fS8 and AGkRk. Inside animation events lasting
  12 frames or more, static frames make up 1% in AGkRk, 15% in fS8 and 30% in N-q (most of it the playing 30 fps
  footage).
- **VQvIV** is mixed. 74 animation events (102 s) run **on 2s** (alternating changed/unchanged frames, pattern
  `101010101010`): the slams, bursts, crowd zoom and line draw were rendered as 30 fps comps. 58 events (50 s) run on 1s:
  slides and fades.
- **Our build:** render everything at 60 fps on 1s. Pops must land on an exact frame. Optionally step the dialect-C
  "effect" layers on 2s (`stepFrames: 2`) to match VQvIV.

## 8. Recurring devices (build each as a preset)

1. **Heading plus list build:** the heading cascades in at the centre, slides up linearly in 8-10 frames, then bullets
   pop one per cue word, top-anchored, each with a smaller grey parenthetical under it.
   Seen at N-q 15-21, fS8 12-19 and `frames/-fS8na576Jc/sheets/sheet_0000s.jpg`.
2. **Staircase lines:** each next phrase pops one line lower, indented about 50 px further right (VQvIV 10-12, 23-24).
3. **Figure plus caption:** a stick figure on the left third, text on the right. The scene changes by crossfading the text
   while the figure shrinks to 0.9, and the screenshot fades in over 17 frames (N-q and fS8 openings; identical template).
4. **Screenshot proof, then annotation:**
   - the screenshot pops or fades in;
   - a red arrow wipes in pointing at it, with a 1-line red/black caption ("*killer video", "stupid easy");
   - an italic footnote pops under it ("*not my screenshots", N-q 12-14).
5. **Screenshot stack:** 2-3 analytics cards pop in diagonally overlapped, about 0.6 s apart (N-q 45.4-46.7).
6. **Side-by-side compare:** two items (two figures, viewer vs creator labels, phone and chart) placed left and right;
   the second arrival pushes the first sideways (VQvIV 1.35, N-q 45.3).
7. **Keyword reveal:** the red word is part of the line and pops (A) or rises (B) with it. There is no separate highlight
   sweep, underline or strike-through animation in any of the 5 videos.
8. **Slam card plus shape burst** (dialect C hook or section opener): huge-to-fit slam in 8 frames with radial blur, then
   circle/x/square/triangle shapes drifting out and fading over 60 frames (VQvIV 20.33, 15.3).
9. **Red flash negation:** 1 frame of full red, a red circle-X slam, about 10 frames of decay to white (VQvIV 22.55).
10. **Line-chart draw-on with follow-cam:** a green line draws on in about 1.5 s with ease-out, the camera tracks the tip,
    then pulls back (VQvIV 15-16, 96-98).
11. **Gameplay b-roll filler (EQUn6):** an inset Minecraft clip with a white border, no text, during talky stretches;
    hard cuts between clips every 1-4 s.
12. **Live pen annotation (EQUn6):** red loops and handwriting drawn at real speed over a screenshot grid.
13. **Part card:** a talking-head or screenshot image with "PART 6: CONTENT CREATION SKILLS" under it, the keyword in red
    (EQUn6 462 s).

No cursor animation, counters or tickers, typewriter-with-caret, strike-through, highlight sweep or screen shake were
found.

## 9. Engine requirements

Time base: 60 fps, `t` in seconds, and every element a pure function of `t`. Cue times come from the narration's word
timings.

- `cue(word|clauseStart, offsetMs=0)`: resolves to a frame. Defaults:
  - scene cuts: clause start +67 ms (round to the frame on or after the word onset, max +6 frames);
  - pops: word onset +0..+33 ms;
  - animated entrances: onset −150 ms.
- `pop(el, t0)`: opacity 0 to 1 in 1 frame. No transform.
- `fade(el, t0, frames=17, curve=linear, dir=in|out)`. Scene fade-to-white: 11 frames, then 4 frames of white.
- `crossfade(sceneA, sceneB, t0, frames=17)`: B's heading may start its cascade at `t0`.
- `cascadeText(line, t0, order=ltr|rtl|center, perCharFrames=2, charFadeFrames=6, rot0=±3..8deg, dy0=+40px,
  settleFrames=15, ease=outCubic)`.
- `kineticWord(word, t0, frames=30, dy0=+67px (6.2% H), ease=outQuad, opacity ease=outQuad)` plus live re-centring of the
  line (lerp to the new centre over 12 frames).
- `lineBuild(words[], cues[])`: the first word uses `cascadeText`, the rest use `pop`, with instant re-centring.
- `listBuild(heading, items[], cues[])`:
  - heading at the vertical centre;
  - before item 1, `moveLinear(heading, dy=-150..-260px, frames=8..10, scale→0.9 optional)` ending 9-22 frames before
    item 1's cue;
  - items pop top-anchored with a fixed line pitch; optional staircase indent of 50 px.
- `slideIn(el, from=top|right|bottom|left, frames=10..14, ease=outCubic)`, `slideOut(el, to, frames=15, ease=inQuad)`,
  and `pushAside(existing, dx, scale→0.83, frames=14)` when a second item joins.
- `scaleIn(el, from=0.6, frames=15, ease=outCubic)`; `elasticIn(el, frames=24, keys=[0, 0.97@8, 0.84@14, 1.0@19,
  1.0@24])`.
- `slam(el, fromScale=3, frames=8, ease=outExpo, radialBlur=true)` plus `burst(shapes=[circle, x, square, triangle],
  n=8..10, frames=60, outward=+50%, shrink+fade=expo)`.
- `wipeStroke(path, t0, frames=6)` for arrows (reveal along path length) plus `fade(frames=15)`.
- `drawOn(polyline, t0, seconds=1.5, ease=outQuad)` plus `camera.follow(tip)` then `camera.zoom(0.75, 36 frames,
  inOutQuad)`.
- `camera`: a 2D transform (scale, translate, rotate) over the whole stage, plus optional motion blur. Idle is identity:
  no drift and no shake.
- `flash(color=red, holdFrames=1, decayFrames=10)`; `rgbSplitOut(el, frames=15)`; `pinch/barrel(el, frames=24)`, optional
  for dialect C.
- `idleFloat(el, amp=15px, rot=2deg, period=2.5s)` for cut-out images (brain, logos) only. Never for screenshots or text.
- `stack(cards[], cues[], offset=(+70px, +90px))` for screenshot piles.
- `crowd(drawing, mode=pop|scaleIn|pushIn)`: one static drawing, scaled, never simulated.
- `stepFrames(layer, 2)`: optional on-2s stepping for dialect-C effect layers.
- `video(clip, rect)`: inset footage that plays (examples, b-roll).
- **QA checks:**
  - 85% or more of scene changes hard;
  - median scene length 1.8-3.0 s;
  - 55-75 visible changes per minute;
  - every scene change within 0..+100 ms of a clause start;
  - every pop within ±50 ms of its cue word;
  - no element moving during a hold in dialect A.

## 10. Shorts vs landscape

- The "Shorts" video (N-q) is landscape 4:3 like the others. It is simply the purest dialect A:
  - highest scene rate (23.1/min) and hardest cuts (86%);
  - least continuous motion (7%);
  - most front-loaded hook (108 events/min in the first 15 s);
  - only 1 fade-to-white.
- Its sibling fS8 (longform algorithm) reuses the identical opening template: figure plus text, then a crossfade to the
  "how you'll appear" screenshot, measured at 17 frames in both. It cuts slightly slower (15.6/min, median 2.97 s).
- A vertical (9:16) adaptation is our own extrapolation. To build one, keep dialect A's timings unchanged and change only
  the layout: stack where the landscape layout uses side-by-side, and keep the top-anchored list.
