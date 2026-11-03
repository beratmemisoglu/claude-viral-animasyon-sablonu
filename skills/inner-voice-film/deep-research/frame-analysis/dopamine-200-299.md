# DOPAMINE — frame analysis, frames 200–299 (≈ 0:20.0 – 0:29.9)

Source: `research/frames/video-B/videoplayback (1)_200.jpg … _299.jpg`, 640×360 JPG.
Analyst read all 100 frames in order, plus anchor frames 060 / 130 / 160 / 190 to check timing, plus 3× HUD crops and pixel samples (System.Drawing).

## 0. Sampling rate: the conclusion
- The folder has 300 frames (000–299). The anchor frames match the script timestamps at 10 fps: f060 (6.0 s) = painting at the easel, f130 (13.0 s) = park, kite, friend in yellow hat (script: 00:13 friend meeting), f190 (19.0 s) = first phone check with "+1", and f200–299 = Scene 3 "digital consumption" (script 00:15–00:40).
- **Conclusion: 1 frame = 0.1 s (10 fps). Frame N ≈ N/10 s.** This is confirmed by anchors only. No source video is in the repo, so ffprobe was not possible. Error is probably ±0.5 s (?).
- **Remotion @30 fps: frame = N × 3** (e.g. f258 → 774). Events that last 1 sample may really last 1–3 frames at 30 fps.

---

## 1. Shot list

| # | Frames (10 fps) | @30fps | Dur | Content | In / Out transition |
|---|---|---|---|---|---|
| A | (≤190)–279 | ≤570–837 | ≥9 s (8.0 s in range) | **Studio (one continuous shot).** Dark room, colorful props. Sequence: phone check #1 (tail) → puts phone down → paints → notification #2 → phone check, reward burst "+3" → magenta "notification creature" rises → "just one more." | In: started before f190. Out: **fade to black f276–279** (with the HUD left out of the fade) |
| — | 276–279 | 828–839 | 0.4 s | Fade to black. Mean scene luminance (HUD excluded): 44 (f275) → 41 → 29 → 18 → 7 (f279). About linear, slight ease-in. | — |
| B | 280–292 | 840–878 | 1.3 s | **Phone POV close-up (doomscroll)**: hand swipes a vertical feed of gradient cards. Clock **"2:14 PM"** top-right. | In: **hard cut from black** (no fade-in; f280 lum = 45 right away). Out: hard cut |
| C | 293–299+ | 879–899+ | ≥0.7 s (continues past f299) | **Gaming**: character sits on the floor with a gamepad in front of a TV on a stand. Screen shows colorful bokeh and "LEVEL UP!". Clock **"4:02 PM"**. | In: hard cut (straight from bright feed to dark teal scene) |

**How daylight turns into dark (key answer):** there is **no color drain and no crossfade between scenes**.
1. The studio's own background is already near-black (#0B0B0B). The "colorful daylight" feel comes only from props: the painting, the window, the rainbow shelf, the plant.
2. The darkness is introduced by a character: the black **notification creature** with a magenta rim glow rises from the floor (f250–257).
3. A short **fade to black over 4 samples (~12 frames @30fps)** follows, f276→279.
4. Then a **hard cut** opens on the dark consumption scenes (B, C). Their backgrounds are tinted (plum / teal) and their only light comes from screens.
5. The HUD graph stays at full brightness through the fade (it is a top layer), so it bridges the two worlds without a break (see §3).

---

## 2. Text events

| Text | First visible (partial) | Full | Out | Animation | Color | Position (640×360) → 1920×1080 | Size |
|---|---|---|---|---|---|---|---|
| **"+3"** (with pink heart) | f239 (at heart, y≈125) | f239–f249 | f250 fade (dim) → gone f252 | Rises with the heart (y 125→103→85→73 over f239–249, ease-out, fast then slow) and fades out over ~2 samples | white #FFF; heart #FF5275 | heart center x≈288, ends y≈73 → (864, 219); "+3" sits right of the heart | heart ≈12 px wide @360p (≈36 px @1080); "+3" cap ≈8 px (≈24 px) |
| **"just one more."** | f258 (≈40 % opacity, dark magenta #46052F→#9F2966) | f259–f276 | f277–279 fades with the global fade-to-black | Opacity fade-in in ~1–2 samples (≈4–6 f @30fps). **No scale or position animation.** Holds 1.8 s fully opaque. | hot pink core **#F860A9** (#D560A6 at strokes), soft magenta outer glow | centered x≈367 (57 % of width), baseline y≈92; spans x 297–437. **It sits above the creature's head, not at frame center** | x-height ≈10 px, line ≈18 px @360p → ~48–54 px font @1080; width ≈22 % of the frame |
| **"LEVEL UP!"** (diegetic, on TV) | f293 | f296–297 | flickers: f294 hidden, f295 partial, f298 partial, f299 hidden | **Flashing/flicker** with a ~2–3 sample period, blended behind and over the bokeh | orange-yellow (#DF9475 → #DFCB4E gradient across letters) | inside TV screen, x≈400–510, y≈127 | cap ≈14 px @360p (≈42 px) |
| **"2:14 PM"** (clock HUD) | f280 (pop-in on the cut) | f280–292 | f292 (cut) | none (static) | off-white | right-aligned, ends x≈593 (right margin ≈47 px = 7.3 % → ≈140 px @1920), y center≈48 (≈144 @1080) | cap ≈10–11 px (≈32 px @1080) |
| **"4:02 PM"** | f293 | f293–299+ | — | none | same | same | same |
| **"DOPAMINE"** (HUD label) | present every frame | — | — | static | mid gray (~#9a9a9a) (?) | x≈23–65, y≈34, sitting right on the top letterbox edge | caps ≈6 px (≈18 px @1080), wide letter-spacing |

Typography: the same rounded, handwritten, Comic-Sans-like face as DISCIPLINE. The inner-voice line follows DISCIPLINE's rule exactly: **lowercase + final period** ("again.", "told you."). **But in DOPAMINE the inner-voice color is PINK/MAGENTA, not red.**

---

## 3. HUD analysis

### 3.1 Dopamine line graph (top-left)
- **Layout:** label "DOPAMINE" above; the trace runs from x≈22 to x≈133 (≈111 px ≈ 17 % of the frame width). Vertical band y≈40–70. A **dark translucent rounded panel** behind it (x≈18–138, y≈30–80) is visible only over bright backgrounds (f130 park sky). It is invisible on dark scenes.
- **It is a scrolling strip chart.** The newest value is drawn at a fixed **"write head" on the right: a glowing white dot** (core ≈3 px, bloom ≈6–8 px). History scrolls left.
  - Measured scroll speed: spike #1 moves x 117 (f200) → 99 (f216) → 81 (f232) → 66 (f246) → 53 (f258) → 33 (f276). That is **≈1.1 px per sample @640**, i.e. **≈33 px/s at 1920 = 1.1 px per 30fps frame**.
  - The visible window is ≈10 s of history.
- **The scroll continues across the fade AND the cut** (f279: spikes at x≈28 and ≈88; f280: identical). It is one global HUD timeline and is not reset per shot.
- **Healthy section (left, older):** gentle low-amplitude sine waves (~3 px amplitude) slightly above the baseline. This is the "natural" dopamine from painting, guitar and park. It scrolls out of view by ~f276.
- **Dashed baseline:** a gray dashed horizontal line (y≈54–56 @360p) appears to the right of the first spike. It is the reference level, and the trace now stays **below** it most of the time.
- **Spike (cheap hit):**
  - Rise is near-vertical (1–2 px wide). Height ≈ **+10–11 px above baseline** (@360p).
  - Sharp peak. The **tip segment is tinted pink/red** (white → pink gradient toward the peak).
  - At trigger moments the write-head dot itself turns **magenta with a bigger bloom**: f238 and f240 (phone burst), f283 (during the swipe).
- **Crash:** right after the peak the line drops fast **past** the baseline to a trough ≈ **−12 px** (crash depth ≈ spike height). It then recovers along a long concave-up ease-out curve. The crash segment is tinted lavender/pale blue-gray. **Recovery takes ~55 samples (~5.5 s) and is never complete:** each new spike fires while the line is still below the baseline.
- **Spike timeline in range:**

| Spike | Trigger (write head turns pink) | Story event | Note |
|---|---|---|---|
| #1 | ≈f188–190 (before range) | first phone check "+1" | crash fully drawn by f224 |
| #2 | **f238–240** | notification #2 → reward burst "+3" | tallest, pink tip visible f246–258 |
| #3 | **f283–285** | doomscroll swipe | small peak first seen f285–289; slightly lower than #2 (?) |
| #4 | **f299** (new small bump at the head) | "LEVEL UP!" on TV | small; height trend suggests **diminishing returns** (?) |

  Peaks after #2 look slightly smaller while the troughs stay as deep. This fits the tolerance idea, but it is not certain at 360p (?).

### 3.2 Clock (top-right)
- **It is absent in the studio scene** (f200–279). It appears **only in the dark consumption scenes**. It acts as a "time-loss" device.
- **Format:** `H:MM PM` with no leading zero, a space before PM, uppercase PM.
- **Progression:** **2:14 PM** (f280–292, 1.3 s screen time) → **4:02 PM** (f293+).
  - That is **+1 h 48 min across one hard cut** after only 1.3 s of screen time.
  - The minutes are **not ticking** inside a shot; the time jumps only at cuts.
  - The odd, non-round values (2:14, 4:02) make it feel "real".

### 3.3 HUD in the dark scenes
- **The HUD is exempt from the fade-to-black:** in f277–279 the scene drops to lum 7 while the graph and white dot stay full brightness. Render the HUD in a layer above the transition.
- In B/C the panel box disappears (the background is dark). The graph keeps scrolling and the clock is added. No other HUD changes. There is no color shift of the label.

---

## 4. Character motion breakdown

| Frames | n | Action / pose | Expression | Glow / secondary |
|---|---|---|---|---|
| 200–209 | 10 | Standing left of the easel, phone (pink-blue screen) held up at his face with his right hand, body ¾ toward camera. **Pose held, no breathing visible.** | contented smile, dot eyes with blue irises | **Blue screen glow halo** around head and phone, radius ≈45 px (#314D62 → #253847, lavender #AD98E3 next to phone) |
| 210–211 | 2 | **Pose pop:** phone already on the stool (screen lit, small). Character faces left, hand to chest. | neutral/blank, small "o" mouth, brows flat | glow gone from face; phone emits a faint glow on the stool |
| 212–215 | 4 | Leans/reaches toward the stool, arm extended, putting the phone down (or swiping it away) | flat brows, "o" mouth | — |
| 216–231 | 16 (1.6 s) | **Pose pop to the easel** (≈+25 px right): painting with the brush in his right hand and the palette in his left. The brush tip makes small dabs (tip x 400→412, y 155→185 drifting). Body static. | **determined/focused** (brows angled down), slight smile | no glow; warm normal lighting |
| 232 | 1 | **Pose pop back toward the stool:** phone lights up — blue glow, **pink vibration ticks** ("/ \") either side, **red badge**. He turns his head toward it, hand to chin. | neutral, attentive | phone glow blue radius ≈30 px |
| 233–236 | 4 | Leans and reaches, hand on the phone (lean held 4 samples) | neutral/glazed "o" | — |
| 237 | 1 | Phone up to his face again (same pose as f200) | smile | blue halo back on |
| 238 | 1 | **Reward burst:** a rainbow-ringed flash around the phone (pink/teal/orange) | — | big bloom |
| 239–249 | 11 | Holds the phone pose. **Reward particles:** "+" sparkles (teal, pink, orange, green) explode outward, then drift out and fade. Heart + "+3" floats up. | wide happy smile | blue halo; particles fade by f249 |
| 250–257 | 8 | Same pose. **The notification creature rises from the floor** to his right (by the easel): f250 red badge "3" + a small black mound with a magenta rim on the floor line; f251 hemisphere; f252 head with a grin; f253 shoulders + arm; f254–257 full height, its arm reaches and touches his back. | f255+: **uneasy/glazed**: brows tilt up in the middle, small frown, eyes still on phone | creature's magenta glow spills onto the floor |
| 258–276 | 19 | Static two-shot. The creature leans in over his shoulder, hand on his back; its head drifts slightly (≈3 px). He keeps staring at the phone. | glazed, slightly worried; creature: closed "^^" smiling eyes (f259–264), then **glowing cyan slit eyes** + magenta grin (≈f265+) | his blue halo and the creature's magenta rim side by side (cool vs hot) |
| 280–292 | 13 | POV: his arm/hand (cream, outlined, mitten fingers) enters from the bottom-right and repeatedly swipes up. The hand alternates between a low position (y≈250, f280–284) and a high one (y≈160, f285–292). **The feed advances ~1 card per sample (~5–10 cards/s)**. | — (no face) | plum radial glow around the phone (#22121D) |
| 293–299 | 7 | **Sitting on the floor**, knees up, a dark gamepad in his hands at knee height. **Totally static** across 7 samples: the hypnotised freeze. | **angry/intense V-brows + wide round eyes (teal irises) + small "o" mouth** (the "angry/glazed" gamer face) | **Teal halo behind him** (#123642), not tinted by the screen colors |

**Notes:**
- All big pose changes are **pops between key poses**: 209→210, 215→216, 231→232, 236→237. There are no in-betweens at 10 fps sampling. At 30 fps they may have 1–2 in-betweens or be pure swaps (?).
- **Holds are long** (10–19 samples). Motion lives in particles, glow, text and the HUD, not in the body.
- No limb wobble or breathing was detected.

---

## 5. Environment & color

| Scene | BG | Key colors | Light |
|---|---|---|---|
| A Studio | flat #0B0B0B, letterbox #000 | painting (sky blue, green hills, orange ground, yellow sun, rainbow dots), rainbow shelf (red→orange→yellow→green→blue→purple→pink pills + white ball), window (blue sky, green hills, sun, cloud), poster (orange sun + blue waves on navy), guitar (tan), plant (green, terracotta pot), stool/easel brown | faint **diagonal light shaft** from the window down-left (?) |
| Creature | pure black body | **magenta/hot-pink rim glow** (#F860A9 → #612042 falloff), **cyan slit eyes** (#83B4EC-ish), magenta grin, **red notification badge "3"** with a white number | glow also lights the floor |
| B Phone | radial **plum/purple vignette** #22121D around the phone → black edges | cards: saturated 2-color gradients (pink→green, orange→lime, yellow→teal, teal→pink, orange→yellow, magenta→blue); white placeholders (rect "image", circle "avatar", big heart); red mini-hearts + white "likes" lines | the screen is the only light source |
| C Gaming | **dark teal** #0E1F26–#0F181D, darker toward the edges (#090E11) | TV bokeh: pink/magenta, orange, blue, olive-yellow translucent overlapping circles with white cores; row of yellow dots (coins/pellets) bobbing | teal halo behind the character (#123642), cool rim around the TV |

- **Contrast logic:**
  - Healthy = colorful **matte objects** in a neutral black room.
  - Addiction = **emissive** neon (glows, bokeh, gradients) in **tinted** darkness (plum, teal).
  - The palette shifts from "earthy primaries" to "neon pink/teal/purple".
  - **Red is replaced by hot pink/magenta** as the "villain" accent. Red survives only in the notification badge and the mini-hearts.
- **Letterbox measured:** black bars at rows 0–31 and 328–359 (@360p). The content area is 296 px → aspect **≈2.16:1**. @1080p: ~96 px bars top and bottom. Content bg #0B0B0B; the bars are pure #000.

---

## 6. Camera

- **A (Studio): very slow centered push-in.** The poster's left edge moves x 44→30 and the window's right edge 590→603 between f200 and f276. That is **≈+5 % scale over 7.6 s**, linear (≈0.066 % per sample → ≈0.022 % per 30fps frame). It was already running at f190.
- **B (Phone POV):** static (the phone outline stays fixed at x≈262–378, y≈63–292).
- **C (Gaming):** static (the TV frame stays fixed at x≈362–548).
- No pans, shakes or rack-focus in this range.

---

## 7. Pacing stats

| Segment | Shots | Avg shot length |
|---|---|---|
| f(≈160?)–279 studio | 1 (with 4 internal pose pops) | ≥9 s |
| f280–299 | 2 cuts in 2 s | **1.3 s**, then ≥0.7 s |

- The **rhythm collapses** from one ~9 s long take (choice and struggle) into a rapid montage (≈1–1.5 s per shot) the moment he "falls in". The montage presumably continues after f299 with bed, donut and slot machine per the script (?).
- Inside the long take, a beat happens every ~1.5–2 s: put down (f210), paint (f216), ping (f232), pick up (f237), reward (f238), creature (f250), text (f258), fade (f276).
- Earlier, f130 (park) through f190 (studio) suggests cuts every ~3–6 s (?).

---

## 8. NEW / MISSED DETAILS vs BRIEF and script (most important)

1. **The antagonist is not red.** In DOPAMINE the shadow creature is black with a **magenta/hot-pink rim glow, cyan slit eyes, a magenta grin, and a red iOS-style notification badge "3" on its head**. BRIEF lists the antagonist as red (#ff3b30); that applies to DISCIPLINE only. **Each film re-skins the villain in its topic's color.**
2. **The inner-voice text is pink (#F860A9)**, not red: "just one more." in lowercase with a period. It is placed **above the villain's head** (speaker attribution by position) rather than centered.
3. **The creature emerges from the floor** (a rising mound with the badge appearing first), over ~8 samples (~0.8 s). The script says only "appears behind him". It actually rises to his right, between him and his painting, which literally blocks his art.
4. **Reward feedback has a counter:** "+1" at f190 and **"+3"** at f239, plus the badge "3" on the creature. The like count escalates. The heart and the number float up and fade, with "+" sparkle confetti in teal, pink, orange and green.
5. **There are two notifications** in the studio before the fall:
   - #1 at ≈f188, then he puts the phone away and returns to painting (16 samples of "healthy" focus).
   - #2 at f232, with pink vibration ticks and a red badge. He gives in.
   This "resist once, then relapse" beat is missing from the script.
6. **HUD graph mechanics are precise:**
   - It is a scrolling strip chart with a glowing write-head dot that turns magenta at each hit.
   - Healthy activity = gentle sine waves; a cheap hit = vertical spike with a pink tip, then a crash below a dashed baseline and slow, incomplete recovery.
   - It scrolls continuously across fades and cuts.
   - It is **exempt from the fade-to-black**.
7. **The clock only exists in the dark scenes.** It jumps 2:14 PM → 4:02 PM across one cut and does not tick. It means "time disappearing". BRIEF/script mention it only generically.
8. **The transition to dark is a ~0.4 s fade to black followed by a hard cut**, not a color drain. "Losing colors" (grey character) is reserved for later (script Scene 4).
9. **The studio is always on near-black.** "Colorful" = colored props only. The darkness of the addiction scenes is **tinted** (plum for the phone, teal for gaming), not neutral black.
10. **Letterbox ≈2.16:1** (bars ≈96 px @1080 top and bottom). The HUD label hugs the top bar.
11. **Slow push-in (~5 % over 7–8 s)** during the long studio take. This is a subtle tension builder that was not noted anywhere.
12. **The phone feed** is built from simple gradient cards with white placeholders (rectangle, circle, big heart) and like bars. It scrolls ~5–10 cards/s with a mitten hand swiping. It is fully abstract: no real UI or text.
13. **Gaming scene:**
    - The character sits on the floor (knees up), not on a couch.
    - Face = angry V-brows + wide eyes + "o" mouth.
    - The TV is on a stand with bokeh circles and a flickering "LEVEL UP!" plus bobbing yellow dots.
    - The halo behind the character is **teal**, a constant mood color rather than a screen reflection.
14. **The script says he is "at the desk"** when the notification arrives. It is actually a **stool next to the easel**, and the phone lies on the stool.
15. The poster on the studio wall (orange sun over blue waves) and the guitar on the left edge persist as "healthy life" props. The guitar is partially cut off by the push-in.

---

## 9. Rebuild notes (Remotion, 1920×1080 @30fps; scene frame = index × 3)

**Timeline (absolute 30fps frames):**

| Frames | Event |
|---|---|
| 600 | phone pose hold |
| 630 | pop to "put down" |
| 648 | pop to painting (48 f) |
| 696 | notification ping (vibration ticks + badge) |
| 711 | phone up |
| 714 | burst + HUD spike |
| 717–750 | heart "+3" rise and fade |
| 750–774 | creature rise |
| 774–777 | "just one more." fade in |
| 828–839 | fade to black (HUD excluded) |
| 840 | CUT phone POV + clock "2:14 PM" |
| 879 | CUT gaming + "4:02 PM", LEVEL UP flicker |

**`<DopamineHUD>` component (topic-agnostic: `label`, `events[]`):**
- **State:** `samples(t)` is generated deterministically from the frame. `value(t) = baseline + healthyWave(t)·healthyWeight(t) + Σ hits`.
- **Hit at t0:** `amp·spikeShape(t−t0)`. Rise over 2–3 frames (near vertical), drop past the baseline within ~6 frames to −1.1·amp, then recover with an exponential ease (τ≈60 f) back toward the baseline over ~165 f (5.5 s).
- Add `tolerance` so each later amp is ×0.85 (optional).
- **Rendering:** an SVG `<path>` over the last 330 frames of history (≈10 s), with x = 330 px wide (≈17 % of 1920). The scroll is implicit: x = headX − (t_now − t)·1.0 px.
  - Stroke 2 px, off-white #E8E4D8.
  - Spike tips: a gradient stroke segment white → #FF4F9A. Crash segment tint #B4B8DC.
  - Dashed baseline `stroke-dasharray="4 4"`, #6B6B6B, drawn from the first hit onward.
- **Write head:** circle r=4 with a white core and a blur bloom (`feGaussianBlur` stdDev 4). For 0–6 frames after a hit, color and bloom tween to magenta #FF3FA0 and r=6.
- **Panel:** rounded rect, rgba(0,0,0,0.35).
- **Label:** gray caps, 18 px, letter-spacing 0.12em, top-left at (66, 100).
- **Layering:** render the HUD **outside/above** the `<TransitionSeries>` or fade wrapper so fades don't dim it. Keep one global frame clock so the graph never resets at cuts.

**`<ClockHUD time="2:14 PM">`:**
- Right-aligned at (1780, 144), off-white, ~40 px rounded handwritten font.
- Shown only in "consumption" scenes. It changes only on cuts (pass `time` per scene).
- Tip: auto-generate non-round times with increasing gaps to show time loss.

**Glow:**
- Use an SVG filter stack: `feGaussianBlur` (stdDev 8–20) of the shape, color-matrix tinted, `feMerge` under the sharp shape.
- **Screen glow on the face:** a radial-gradient circle (#3A6A8A @45 % opacity → 0) centered on the phone, r≈135 px, blended with `mix-blend-mode: screen`. Toggle it with the phone-up pose.
- **Creature:** a black path plus a 2-layer magenta outer glow (inner stdDev 4 @ #FF4FA0, outer stdDev 14 @ #8A1F5A). Eyes are cyan slits with a small blur.
- Villain color, inner-voice text color and HUD hit color should **all derive from one `topicAccent` token** (DISCIPLINE = red, DOPAMINE = magenta). Loneliness or anxiety would get their own accent.

**Creature rise:**
- Mask the body with a clipPath at the floor line. Animate `translateY` from +body height to 0 over 24 f (spring, damping ~15).
- The badge appears first (frame 0 of the rise).
- The arm reach starts at +9 f. Tween the arm rotation so the hand lands on the hero's back at +21 f.

**Reward burst:**
- Ring flash: 1 frame at scale 1.4, opacity 1 → 0 over 6 f.
- 14–20 "+" particles, deterministic via `random(seed)`. Velocity is radial at 3–6 px/f with drag 0.9 per frame. Colors from [#3FE0D0, #FF5A9E, #FF9A3C, #7CE07C]. Fade over 30 f.
- Heart (#FF5275) + "+N" label: translateY −150 px over 33 f, ease-out cubic. Opacity holds, then goes 1 → 0 over the last 6 f.

**Notification ping:**
- Phone screen brightens and a radial blue glow appears.
- Two pairs of pink tick marks flick at ±10° for 2–3 f alternating.
- A red badge circle pops with a spring (overshoot 1.2).

**Doomscroll feed:**
- Cards are an array of gradient rounded rects (h≈300 px, gap 24 px) inside a phone clipPath.
- Advance with `translateY = −frame·k` plus a stepped "flick" ease, ~1 card per 3–6 frames.
- The hand is rigged at the shoulder, offscreen bottom-right. It alternates between 2 key poses every ~12 f with an ease-in-out arc.
- Background: radial gradient #2A1424 → #000.

**Gaming:**
- The character is static (a hold is fine).
- Bokeh: 5–7 circles with `mix-blend-mode: screen`, opacity 0.5. Their radius and position drift with sin(frame·0.05+i) and each pulses.
- "LEVEL UP!" opacity uses a deterministic flicker pattern [1,0,0.5,1,1,0.5,0] stepping every 3 f.
- Yellow dots bob with sin.
- BG: radial teal #123642 behind the character → #0B1418 at the edges.

**Camera:**
- A long take uses a linear scale of 1.00 → 1.05 over ~230 f around the frame center (wrap the scene in a `<g transform>`). The HUD sits outside the wrap.
- Montage shots are static.

**Transitions:**
- "Fall into the dark" = a full-frame black overlay with opacity 0 → 1 over 12 f (slight ease-in), then a hard cut, no fade-in.
- Between montage shots use hard cuts only.

**Letterbox:**
- 96 px black bars top and bottom (or render at 1920×888 content inside 1080). Content bg #0B0B0B.
