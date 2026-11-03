# 05 — Hero Rig, Expressions & Motion

Contents: 1 Look · 2 Rig architecture (no detached limbs) · 3 Expressions · 4 Transformation token ·
5 Two animation modes · 6 Action catalog (key numbers) · 7 Global mechanics (Act 3) · 8 QA

Full code: `deep-research/05-character-design.md` §2.5 FK/IK helpers, §3.3 `EXPRESSIONS` path data, §6 complete
`Hero.tsx`. Keyframe tables + `poseAt()` for every action: `deep-research/06-motion-library.md` §6.
Apply the overrides in this file when you reuse that code.

---

## 1. Look — OUR MAIN CHARACTER "Moon head" (The Other Self)

**Source of truth: `assets/brand-the-other-self/CHARACTER.md` + `hero-rig.js` (`STYLES.moon`) + `character-sheet.png`.**
Port `hero-rig.js` 1:1 to `src/lib/character/` (keep the numbers, swap string-building for JSX). Do not redesign.

- Big round head (r 58, separate from the body), small rounded body, stick limbs (width 13), mitten hands, small oval feet.
- **Sprout on top of the head** (ink stem + sand leaf) = brand signature; may droop at rock bottom and stand up at the turn.
- **Tall oval eyes** (`rx 5, ry 7.6`) with a white highlight, bar brows, single-stroke mouth; 15 expressions in `EXPR`.
- Colours: body warm sand `#E9C9A2`, ink `#2B1F17`, **thin ink outline on the whole figure** (2.6 u).
- Far arm/leg: same paint, group `opacity 0.55` (tints correctly over coloured backgrounds).
- Shadow twin (inner voice): identical silhouette incl. sprout, fill `#04050B`, glow `#2F6BFF` + rim `#7FA6FF`, eyes `#D6E4FF` (his own eye shape, narrowed/tilted) → `hero({shadow:{mood}})`.
- Scale: wide shot hero ≈ 330–400 px tall; bed shot = `mode:'headOnly'`.
- Draw order: far leg → far arm → body → head (sprout, face, token) → near leg → near arm.
- Secondary characters: same rig, different body tint + one saturated accessory; never give them the sprout.

Reference-film look (cream bean, no body outline, far limbs @0.58) is documented in `03-visual-canon.md` §8 for
analysis only. If you reuse `deep-research/05` code (FK/IK, expressions): `breathing` false, blink about every
150–180 f, hard-swap expressions.

## 2. Rig architecture — why limbs can't detach

Compute joint world positions per frame in TypeScript (forward kinematics, plus analytic 2-bone IK for planted
hands/feet), then draw each limb as **one path `M shoulder L elbow L wrist`**. The child start *is* the parent
end, so detachment is impossible and the round line-join hides elbow seams. Nested `<g transform>` is only for
rigid parts: torso capsule, head (tilt about the neck pivot), face, token, props held in hand.

Angle convention (shared with all tables): `dir(θ) = (sin θ, cos θ)` → **0° = down, +90° = forward**.
Arms inherit torso lean; legs are world-space (the pelvis is a ball). Elbow + = natural bend, knee bend
positive in the 06 tables (`shinAbs = hip − knee`). Facing left = `scale(-1,1)` around the character, pose data
never changes. Dev assertion: `|elbow − shoulder| == upperLen ± 0.01` every frame.

Pose = plain numbers `{x, y, lean, sx, sy, armN{a,b,s}, armF, legN, legF, headTilt, ...}` → lerpable, springable.

## 3. Expressions (hard-swapped sprites of one `Face` component)

Measured set: `asleepContent` (closed ‿ arcs + small smile — smug, not tired) · `tiredHalfLid` (flat lid line, pupils hanging below, eye bags) · `contentSmile` (closed ∩ happy arcs + U smile) · `shock` (raised arched brows, dot eyes with catch-light, small "o" mouth, blue sweat drop) · `numbPhone` (flat low brows, heavy lids, blue under-eye light, mouth hidden by phone) · `exhausted` · `sad` (inner brow ends up, lid eyes, frown) · `cryingHidden` (hand over face) · `focused` (brows angled in, dots, small smile) · `bliss` (half-lidded, smile) · `surprisedO` · `hooked` (glowing teal ring eyes + grin) · `gamerAngry` (V brows, wide eyes, "o") · `determined` (V brows, dots, flat mouth) · `straining` (steep V, gritted-teeth box with grid lines, sweat, `//` stress marks, blush, anger vein) · `confident` (mild V, tiny smile) · `happy`.
New-topic set: `lonely`, `longing`, `inLove`, `heartbroken`, `anxious`, `overthinking`, `hopeful`.
All path data (head at 0,0 r 50, brows share one command structure so they *can* morph): `deep-research/05` §3.3.

## 4. Transformation token

One single-colour object that appears **exactly at the turn (B07)**, never leaves, rides a rig slot with
secondary motion, and is echoed by the end-card underline colour.
DISCIPLINE: red headband — thick sloppy stroke overshooting the head, sitting just above the brows, with a
travelling-wave tail (droops when still, streams when running, flaps at the summit). Accessories may "boil"
(jitter ±0.6 units every 3 f); the body never boils.
Other topics: loneliness = amber scarf (neck, two tails) · love = red thread on the wrist · grief = small
pale-yellow flower · anxiety = pale-cyan lantern pulsing with breath · overthinking = yellow pencil behind the
ear · comparison = red pot with a seedling that grows across acts · dopamine = phone left face-down → a book.

## 5. Two animation modes (do not mix them up)

| | **Acting mode** (default, Acts 1–2, emotional beats) | **Action mode** (physical tasks, mostly Act 3) |
|---|---|---|
| Body | held key poses, pops between them (0–2 in-betweens) | full tweened mechanics from the 06 tables |
| Face | hard swaps | swaps; straining face held |
| Idle | none (no breathing/sway); 1 blink per 5–6 s | cycles (run, guard bounce) |
| Life | camera push, particles, props, text | + overlap (head lags 2–3 f, token tail 3–6 f), squash/stretch, smears |
| Impacts | effect on the prop (squash + dash burst), no shake | hit-stop 2–3 f + camera shake + flash + SFX same frame |

Mood presets for the same action: lazy (Act 1–2: soft easing, slumped lean +6–10, head down, arm swing 0.25,
eyes 0.5) vs determined (Act 3: crisp easing, decision hold 8–12 f before decisive moves, chin up, token on).

## 6. Action catalog — key numbers (tables in `deep-research/06` §6)

| Action | Key numbers |
|---|---|
| Snooze slap (Act 1) | **effect-based** (canon §9): arm pops out 6–9 f, holds ~57 f, prop squash + dash ring, retract 9 f. Do not animate a full IK reach. |
| Calm wake (B07) | eyes snap open (no squint) → 5 f decision hold → deliberate reach 10 f → press, button squash 0.85 + `CLACK` + tap shake → 10 f hold on the button → one firm nod → sit on bed edge, token appears |
| Shock (oversleep) | face swap + sweat drop on the clock's last digit frame; no body motion |
| Couch scroll | static slouch (lean −14, legs crossed/hanging, both hands at chin); phone glow flicker carries the life |
| Desk exhaustion | pre-posed slump, hands on the book, eyes open heavy; optional tiny nod-off (lids 60→85 %, head +2–3°) every ~3 s |
| Sad walk / confident walk | 40 f vs 26 f cycles; sad: hip amp 14°, lean 9, arms dead; confident: hip 24°, lean 3, arm swing 0.8; ground speed 3.3 vs 8.5 px/f |
| Curl (rock bottom) | knees to chest, near hand over face, far arm outlined for readability; sob shudders (4 f period, decaying) every 45–80 f |
| **Run** | **18 f cycle** (two 9 f steps), lean 5–8° (healthy) / 15° (determined, against wind), bounce ≤ 6 px, hero **pinned** ≈ 46 % x while the world scrolls; tiring version stretches the cycle 18 → 26 f, stops, hands on knees, pants (18 f), looks up, decision hold, relaunch |
| Parallax (measured DOPAMINE) | ground/flowers 17 px/f, trees 14 (tile 420 px), hills 3–5, clouds 0.3, sun 0, birds drift +1 the other way; night city: road/lamps 1.0v, buildings 0.35v, skyline 0.12v, speed lines 1.3–2.1v |
| **Push-up** | plank pivots at the toes, pitch only 5–18°, hands IK-planted; rep 26 f (12 down / 2 hold / 12 up); failing rep 64 f with noise tremble driven by strain; collapse (4 f fall, wobble) → eyes shut → snap open → 44 f grind up → counter pops |
| **Boxing** | guard bounce 16 f; jab 12 f (impact f4, hit-stop 2); cross 16 f (wind-up, impact f6, hit-stop 3, heavy shake, **word shatter**); bag = damped pendulum T 1.6 s, ζ 0.08, superposed impulses |
| **Stairs** | rise 46 / run 92 px, 32 f per two steps, feet IK-planted on treads (zero sliding), lean 14; or keep hero in place and scroll the staircase diagonally |
| Push through giant | cycle slows 32→48 f, lean 26, arms shielding, token streams back hard → split at contact (hit-stop 3, quake shake, rim flash) → recover |
| Summit | upright, determined idle, wind squint, token flapping with gusts (noise envelope) |
| Bed edge → exit | 12 f hold, anticipation (lean 32), rise with stretch overshoot, settle, confident walk out of frame |
| Reach for temptation | 14 f soft ease with an 8 f hesitation hold at 70 % reach |

## 7. Global mechanics (action mode only)

- Easing presets: `inOut` bezier(.45,0,.55,1) default · `out` (.22,1,.36,1) settle · `snap` (.7,0,.84,0) into impacts · `whip` (.9,0,.1,1) 2–3 f strikes · `backOut` (.34,1.56,.64,1) pops.
- Springs: pop {d 8, m .6, k 180} · settle {14, 1, 120} · snap {20, .5, 300} · heavy {18, 3, 90}.
- Camera shake = decaying sine, F ≤ 12 Hz at 30 fps, applied to the camera group: tap A3 τ.08 · hit A7 τ.12 · heavy A14 τ.18 · quake A18 τ.28.
- Hit-stop freezes **character time** only; shake, particles and audio keep running.
- Smear when a hand moves > 25 px/f; speed lines when the world moves > 12 px/f.
- Every action exports `events[]` (impact, hitstop, shake, sfx, spawn) so picture and sound share frame numbers.
- No `Math.random`, `Date`, CSS animation. `random(seed)` / `noise2D(seed, …)` only. Clamp every interpolate.

## 8. QA per shot

Limbs attached at every frame · feet don't slide in walks/runs (< 2 px/f), zero on stairs · loops close
(`poseAt(0) == poseAt(len)`) · impacts have anticipation ≥ 2 f, SFX on the contact frame, follow-through ≥ 6 f ·
text beats get ≥ 12 f of character hold · acting shots obey the one-mover rule.
