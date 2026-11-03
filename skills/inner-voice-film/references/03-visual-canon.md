# 03 — Visual Canon (MEASURED · highest authority)

> **Brand override (The Other Self).** This file records the *reference films* as measured. Structure, timing,
> transitions, camera, text roles/sizes/animations, DAY counter, shadow behaviour and the limited-animation law
> apply unchanged. Two things are replaced in our films: (1) the hero look → our main character "Moon head"
> (`assets/brand-the-other-self/CHARACTER.md`), the shadow = his black twin; (2) the accent red → brand
> electric blue (`06-sets-and-light.md` §6 `brand`): shadow glow, eyes, voice/info text, title underline.
> Wherever §5, §7, §8 say "red"/"cream", read "brand accent"/"Moon head".

Everything here was **measured frame-by-frame** from the first 30 s of DISCIPLINE and DOPAMINE
(600 frames @10 fps, pixel-sampled). When any other reference or `deep-research/` file disagrees
with this file, **this file wins**. Values are at **1920×1080, 30 fps**.

Contents: 1 Frame & stage · 2 The "limited animation" law · 3 Transitions · 4 Camera · 5 Text specs ·
6 DAY counter · 7 Inner-voice shadow behaviour · 8 Hero look · 9 Prop micro-animations · 10 Topic HUD ·
11 Corrections to earlier assumptions

---

## 1. Frame & stage

| Item | Value |
|---|---|
| Letterbox | Pure `#000` bars **96 px top and 96 px bottom**, present from frame 0 on every shot incl. title cards. Active picture = 1920×888 (≈2.16:1). Top-most layer. |
| Background | `#0B0B0B` centre → `#050505–#080808` edges, very soft wide radial vignette. Title cards use the same (not pure black). |
| Floor | One thin gray line full-bleed. Measured y = 68–75 % of full frame height (≈735–810 px). Colour `#8E8E8E–#A09D97`, ≈3 px, round caps. Wall and floor are the same near-black (floor zone may be +1–2 % lighter). |
| Line art | Light gray `#8A8A8A–#A0A0A0`, ≈4–5 px at 1080p, round caps/joins, rounded corners, very slightly wobbly. **No line boil** (static regions change 0 px frame-to-frame). |
| Fills | Flat dark fills (`#231D1D` nightstand, `#2E2C36` couch, `#272D3D–#404656` blanket). No cast shadows. |
| Colour logic | Black stage + **colour lives only on objects/lights** (red digits, blue phone glow, warm lamp pool, candy-coloured hobby props in DOPAMINE). The hero stays neutral cream. |
| Sets are minimal | Couch scene = couch + floor line + phone halo + shadow. Nothing else. Max 3–5 props per set. |
| Light | Soft radial pools/beams only: moonbeam (≈3–4 % white diagonal), lamp = **soft warm radial pool** (amber ≈ `#C89A5A` @ 25–35 % → 0, r ≈ 250 px), never a hard cone. Lights may ramp up 3–6 f after a scene fades in. No flicker. |

## 2. The "limited animation" law (the most important finding)

The films feel alive but **almost nothing moves**. Copy this, don't "improve" it with constant motion.

1. **One thing moves at a time.** Beats are separated by **holds of 0.3–1.5 s** (9–45 f).
2. **Expressions hard-swap** on a single frame. No in-betweens, no blink-to-transition, no tween.
3. **Acting poses pop** between key poses (0–2 in-betweens). Paint → surprised → reach are snaps. Use full tweened mechanics only for *physical actions* (run, push-up, punch, climb, walk).
4. **No breathing loop, no idle sway** on the hero during acting holds. One blink per 4–6 s at most (eyes closed for 2–3 f).
5. **Time-skips are cuts**, not animations (DOPAMINE: standing at easel → hard cut → already seated with guitar; the easel even disappears from the re-framed shot).
6. **The hero never reacts to the inner voice** in Act 1. Passivity is the point.
7. Life comes from the *environment*, not the body: slow camera push-in, particles (zZ, music notes, dust), glow, props (clock digits, spinning wall clock, vibration ticks), text, the topic HUD.
8. **Comic delay**: the sleeper ignores 1.5 s of alarm before the eyes open. Let gags breathe.

## 3. Transitions

| Type | Spec | Used for |
|---|---|---|
| **Dip through black** (default between scenes) | Out 8–12 f (ease-in) → in 15–24 f (linear). **No hold on black** — the new shot starts rising the frame the old one hits black. Applied to the whole composite incl. DAY counter. | Scene / location changes |
| Title card → first scene | Text fades out (12 f) → 3–9 f empty card → **hard cut to true `#000`** → scene fades up linearly 15–24 f | After every hook card |
| Hard cut | 0 f, optional 9 f "settle" zoom 1.04 → 1.00 ease-out on the new shot | Time-skip inside the same location; montage; dark consumption shots |
| Fade-to-black then **hard cut** (no fade-in) | 12 f out, cut in | "Falling into the dark" (DOPAMINE) |
| Smash cut | 0 f + optional 1-f flash | Rock bottom → turning-point clock |

Global HUD layers (topic meter, letterbox) are **exempt** from fades. The DAY counter is **not** exempt.

## 4. Camera

- **Default = slow linear push-in on every acting shot**: +1.25–1.5 % scale per second (≈ +4–8 % over a 3–6 s shot), no easing, origin near the subject (≈47–52 % x, 47–55 % y). DOPAMINE long take: +5 % over 7.6 s.
- Some "happy/healthy" shots are **locked** (DOPAMINE painting). Locked = calm; push-in = pressure.
- A slow **pan** (≈6 % width over ≈2 s, ease-in-out) is allowed to follow attention (DOPAMINE turning to the phone, revealing the guitar).
- **No handheld drift. No shake in Act 1** (the alarm slap has none). Shake/hit-stop belong to Act 3 impacts only.
- Screen-space layers (letterbox, DAY counter, text, HUD) sit **outside** the camera group.

## 5. Text specs (font: Comic Sans look — use Comic Relief, see 07-text-system.md)

| Role | Colour | Size @1080 | Position | Animation (30 fps) |
|---|---|---|---|---|
| **Hook / narrator on black** | `#FFFFFF`, **no glow** | glyph box ≈5.3–5.5 % H → font-size ≈66 px | centre (50 %, 49.5 %) | 12–15 f empty → **linear fade-in 18–21 f** → hold 45–63 f (scale with length: ~1.5 s for 27 chars, ~2.1 s for 35 chars) → **fade-out 12 f** (faster than in). Whole line rises ≈9–10 px over its life. No blur, no scale, no typing. |
| Hook keyword tint (optional) | each letter of ONE keyword in the topic's "healthy" palette (DOPAMINE: c-o-l-o-r-. = red, orange, yellow, green, blue, purple) | same | same | coloured from first visible frame |
| **Info / excuse (red, before the shadow has a body)** | `#FF4F58–#FF5040`, glow ≈ 6–8 px faint | ≈60 px | above the hero's head, **left-anchored** ≈(34 %, 28 %) | **Typewriter ≈16 chars/s** (one char per ~2 f, spaces count), no cursor, **ellipsis dots typed one at a time**. Exit: fade 9 f. |
| **Verdict word** ("again.") | same red | ≈60–64 px | same baseline as the excuse | **Pop**: opacity 0→1 and scale 1.18→1.0 over 3 f (ease-out). Holds until the scene dip. |
| **Inner-voice speech** | `#F94E46–#FF4A3A`, soft red glow | ≈42–46 px (3.9 % H); 2nd/harsher line ×1.2 and brighter; boss lines huge (see 04) | **On the shadow's head** (across forehead, then across the eyes for the next line) or just above it — never a speech bubble | Fade-in 3–6 f, **continuous upward drift** (~0.3 px/f) for the whole hold, fade-out 9–12 f while still rising. Lines are separate events with a **0.4 s gap**. |
| DAY counter | see §6 | | | |
| Reward "+N" | white bold + pink heart `#FD4C76` | ≈24 px + 36 px heart | spawns at the phone | rises 135 px with ease-out over 27–33 f, holds, fades 15 f; sparkle burst of 4-point stars |
| Topic HUD label | gray `#8A8A8A`, all caps, wide tracking, small (≈16–18 px) | | tucked right under the top letterbox bar | static |

Rules: one message at a time (+ DAY counter/HUD). White and red never share a frame. Inner-voice text is lowercase with a period. "Faint red text" in a still is just a mid-fade sample, **not** a permanent whisper style.

## 6. DAY counter

- Text `DAY N`, bold, gray **`#BBBBBB`** (not white), cap height ≈2.8 % H (≈30 px → font-size ≈42 px).
- Left edge x = **150 px** (7.8 %), vertical centre y ≈ **147 px** (13.6 %) — just below the letterbox.
- Screen space (ignores camera push). Fades in over 6 f, **starting ≈15 f after the scene begins** to fade up.
- **Roll device**: a new scene can open still showing the old day (it dims through the dip with the frame), then **count up inside the new shot** with ease-out (quartic-ish), integer hard-swaps every 3 f, sticking on the penultimate value 2–3 steps before landing. Measured: 1,4,14,22,29,35,39,42,44,45,46,46,46,47 over 39 f. The intermediate days (e.g. 25) are never shown as their own scenes.
- The roll is synchronised with something "growing" (the shadow rising out of the floor).

## 7. Inner-voice shadow behaviour (measured)

- **Pre-planted**: its glow is already visible on the floor / behind furniture in the scene's first frame before it rises. Dread before sight.
- **Entrance = rise**, ease-out cubic, ≈ 33–45 f: from behind a furniture edge (couch arm) or **out of the floor line** (floor-masked: red arc → dome → head with grin → shoulders → full body; reaches full height then settles 6–9 f).
- **Glow** = soft blurred outer glow, orange-red `#B6391D–#D1422D`, ≈25–30 px falloff at 1080, a thin brighter rim. **Constant — no pulsing.** It spills onto nearby outlines.
- **Fill** pure black `#000–#050505` (darker than the wall: it reads as a hole).
- **Face sequence**: smile appears first (while peeking) → eyes "ignite" over ≈9 f (slanted glowing dashes, tilted down toward the centre) → smile turns **on while a line is spoken and off between lines** → eye shape hard-swaps to sly arcs `⌒ ⌒` for the next line → after a line has landed the closed-smile eyes become **glowing slits**.
- **Escalation inside a scene is by face + glow, not size**: on the harsher second line the glow widens/brightens ≈1.5× and the slit eyes go white-hot.
- **Poses**: hand raised to the mouth (whisper), hand resting on the hero's chair back (possessive), leaning over a furniture arm. Holds them; no gesture cycles.
- **Never walks**. Rises, appears, glides. Stays at its own end of the frame (~23 % width away from the hero).
- **Topic re-skin**: the accent colour of glow + eyes + voice text is a per-film token (`topicAccent`). DISCIPLINE = red; DOPAMINE = black body, **magenta/hot-pink glow `#F860A9`, cyan slit eyes, magenta grin, red notification badge "3" on its head**, voice text pink. Body/proportions stay the same — that's the brand.

## 8. Hero look (measured)

- Cream bean body + merged head: `#DCD8CB` (samples #DBD7CB, #DDDACB, #DCD3C9, #E2DED3).
- **No outline on body/head.** Only the **near-side limbs** get a dark outline (`#141210–#222`, ≈4–5 px).
- **Far limbs = the same cream at ≈55–60 % opacity** (reads `#A5A295` on black, green-tinted on grass). Implement with opacity, not a separate gray.
- In bed: only the round head shows (≈ 114 px diameter in a wide shot), upright and front-facing like a sticker on the pillow; one arm can pop out of the blanket.
- Standing ≈ 33–37 % of full frame height in wide shots.
- Faces: thick dark bar brows, dot eyes (white catch-light when shocked), small single-stroke mouth. Extras: tiny blue sweat drop `#9CC3E6` that appears on the same frame as the shock face and doesn't move; under-eye bags on tired faces; blue phone light on lower lids.
- Secondary characters = **same rig + a different skin tint + ONE saturated accessory** (DOPAMINE friend: tan `#D7C1A9` + yellow hard hat `#F4BC29` with a knob).

## 9. Prop micro-animations (copy exactly)

- **Alarm ringing**: red `〃` vibration ticks at the clock's top corners blinking in a 5-sample pattern (on,on,off,on,off → at 30 f: 3-frame steps); clock body doesn't shake; digits don't blink.
- **Snooze "slap" (Act 1)**: the arm pops out of the blanket (6–9 f) pointing **away** from the clock and holds; the hit is shown **only on the prop**: clock `scaleY 0.7` for 1–3 f + a ring of ~10 white-gray dashes that expands to 2.5× the clock width over 9 f (ease-out) and fades. No camera shake, no face change. Arm retracts in 9 f via a V-elbow pose.
- **zZ**: gray `#B1B1B1`, spawn every ~21 f at the head's upper-right, rise ~0.8 px/f, drift right ~0.3 px/f, shrink and fade as they rise; spawning **stops** the moment time jumps, the last Z finishes its life.
- **Clock fast-forward**: **discrete hard digit jumps, one per 3 f, accelerating** — 5:00, 5:02, 5:05, 5:10, 5:17, 5:26, 5:38, 5:54, 6:14, 6:37, 7:06, 7:39, 8:18, **8:47** (13 steps, 39 f). The shock face swap + sweat drop land on the frame the final value appears. The window keeps the moon (no daylight change).
- **Wall clock time-lapse**: hands spin fast and continuously the whole scene (≥1 rev / 0.6 s), even after the DAY roll stops.
- **Phone glow**: blue radial halo r ≈ 120 px around face/phone, flickers ±10 % every 3 f (seeded), blue light on the lower eyelids. The halo moves with the phone.
- **Notification**: red badge pre-planted on the phone before it buzzes; buzz = pink/magenta tick marks either side + glow (the phone doesn't shake).
- **Reward hit**: 1-frame rainbow ring flash → 4-point sparkle burst (cyan, pink, yellow, orange) → heart + "+N" floats up → hero's eyes become glowing teal rings. Counter escalates (+1 → +3).
- **Music notes**: two looping emitters half a cycle apart (≈48 f period), rising diagonally up-right over ≈42 f, fade in/out 6 f.
- **Canvas painting**: layers revealed by **hard-edged left→right wipes** (hills, darker hills, ground), then one flower dot per 3 f; brush tip colour steps through the rainbow. Brush position needn't match.
- **Guitar strum**: the hand toggles between 2 drawings every 3 f. No body bob.

## 10. Topic HUD (optional per film — DOPAMINE's signature device)

A small screen-space "vital sign" for the topic. DOPAMINE: a scrolling strip chart.
- Panel: rounded rect at (54, 93) 360×147, `rgba(0,0,0,0.5)`, top edge tucked under the letterbox. Label in gray caps.
- Fades in 15–18 f **0.5 s after** the first scene is up. Never fades with scene dips; scrolls on the **global** frame clock (never resets at cuts).
- Trace: off-white `#D8D8D8` ≈4.5 px, scroll left ≈1.1–1.2 px/f, ≈10–11 s of history visible, glowing write-head dot at the right.
- States: **healthy** = gentle irregular wave ±9 px, λ ≈105 px; **craving** = dead flat line from the moment of temptation; **cheap hit** = near-vertical spike ≈3× healthy amplitude with a pink tip, write-head turns magenta for 0–6 f; **crash** = drops below baseline by ≈ the spike height, slow incomplete recovery (~5.5 s); later spikes slightly smaller (tolerance). A dashed gray baseline appears after the first hit.
- Companion **clock HUD** top-right (`2:14 PM` style, right-aligned at x≈1780, y≈144) appears **only in the bad scenes** and jumps only at cuts with odd non-round times. Its absence in the good scenes is the message.
- Adapt per topic: loneliness → "messages: 0" counter / heartbeat monitor; anxiety → BPM; overthinking → "thoughts: 1, 4, 19, 87…"; procrastination → "tasks done: 0". One HUD at most.

## 10b. Not measured yet

Only 0:00–0:30 of each film was measured. Mirror, rock bottom, grind, boss, summit, end card and DOPAMINE's
colour-burst / ink-splash transition (~2:11, colour returning) are reconstructed from stills and scripts.
For the colour-return moment of Archetype B use an expanding radial colour wipe (clipPath circle growing from
the hero, saturate 0→1 per layer, a few paint-splash blobs) — mark it as unverified until frames are analysed.

## 11. Corrections to earlier assumptions (do not repeat these mistakes)

| Assumed (brief/scripts) | Measured truth |
|---|---|
| Alarm jumps 5:00 → 5:05 after snooze | stays 5:00; later fast-forwards in 13 discrete jumps to 8:47 |
| "just 5 more minutes... again." is one line | two separate captions 1.6 s apart; first is typed, second pops |
| Shadow "approaches his shoulder" | rises straight up behind the couch arm and stays planted |
| Glow is a red outline that pulses | soft blurred orange-red outer glow, constant |
| Separate DAY 25 shot | one desk shot rolling the counter 1 → 47 |
| Hero asleep at desk | eyes open, heavy-lidded, holding one slumped pose |
| "you're tired." is a faint whisper | normal red; faint frame was mid-fade. Followed by "why even try?" (bigger) |
| Far limbs darker gray | cream at ~58 % opacity |
| Body/head outlined | no outline; only near limbs |
| Lamp = cone | soft radial pool |
| One letterbox bar | bars top AND bottom, 96 px each |
| DOPAMINE starts on the studio | starts with a hook card "The world used to be full of color." |
| Villain is always red | accent is per topic (DOPAMINE: magenta + cyan eyes + badge) |
| Continuous character motion everywhere | limited animation: holds, pops, one mover at a time |
