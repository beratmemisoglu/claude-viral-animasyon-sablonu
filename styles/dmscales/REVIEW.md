# Dmscales - review log

The working ledger of the review loop (docs/METHOD.md stage 6) and the sign-off record (stage 7). It stays in the kit:
it is never packaged. Newest round at the top of each section.

## Open findings
_(none: `cz check dmscales` and `cz check dmscales --look look-hit` report no high and no medium finding in any view or aspect)_

## Fixed
- r7-4 | round 7 (battle test: ilk-30-saniye, the first Turkish video, built in the app's project) | the thought cloud's circles pointed away from a thinker placed below it -> composition rule (head level with the cloud's top) | PITFALLS: thought cloud
- r7-3 | round 7 -> reverted in round 8 | heading()'s header was made bold in the Hit era; the side by side with N-q 20.5 s and fS8 17.6 s shows both hits set the header regular (only the current item is bold), so `bold = false` is back | PITFALLS: check a weight against the reference
- r7-2 | round 7 | 'armsup' arms ended inside the head (read as hands on the cheeks) -> elbows out, hands up beside the head (models.js figure) | PITFALLS: a pose's arms
- r7-1 | round 7 | Turkish caps lines missed their spoken words ("NASIL" cued as "nasil") -> words() lowercases in the narration's language (__CZ_LANG) | PITFALLS: caps lines in Turkish
- r6-3 | round 6 | the list card counted as empty (low) -> `heading()` sets `S.sparse = true` (models.js headingShrink / heading) | PITFALLS: sparse marks only a card whose white is the point
- r6-2 | round 6 | shrunk list items 23 px in 9:16 (small) -> the shrink scale floors at 26.5 px (models.js headingShrink SM / NS) | -
- r6-1 | round 6 | the Era control looked the same at its ends (controls: "Body type" weight alone changed 0.14 % of the frame) -> the control is the channel's era: later (regular italic, #ffffff) / hits (bold italic, #fcfcfc), measured on the reference | -
- r5-4 | round 5 | VOID at 14.61 s (the audience came 0.5 s after the cut) -> the crowd enters with the cut (sample.js S10) | PITFALLS: cut on the word the first thing shows
- r5-3 | round 5 | VOID false positive at 9.85 s -> the probe replays the engine anims we register (`dm: true`) | PITFALLS: replay every visibility source
- r5-2 | round 5 | the definition card held 0.5 s (its note never showed) -> it holds through "If those viewers watch it," and the curve cuts on "it gets" (sample.js S4/S5) | -
- r5-1 | round 5 | a 0.7 s blank page at 5.52 s the BLANK check did not report -> chart axes come with the cut (`live({ show })`), new VOID check + mustfail_void | PITFALLS: cut on the word the first thing shows
- r4-2 | round 4 | every line drawn 0.72 em above its y (hero 16:9: "SWIPE RATE:" 66 px high) -> sign fixed in say() | PITFALLS: canvas type baseline
- r4-1 | round 4 | 9:16 used the top 40 % of the frame -> `P()` spreads positions 1.15x vertically (UV) | -
- r3-4 | round 3 | the chart's L axis smoothed into a curve -> two straight strokes | PITFALLS: hand-drawn boxes / corners
- r3-3 | round 3 | a stray dot under the crowd (a hook cap under a neighbour's body) -> heads drawn by hook bottom, bodies cover their caps | -
- r3-2 | round 3 | repeat at 11.34 s (a half-typed title after playing) -> the cascade's finished state keyed apart | PITFALLS: cached painted state
- r3-1 | round 3 | BLANK at 4.88 s (definition shot cut 0.8 s before its header) -> cut on "test"; the cascade is in within ~10 frames | PITFALLS: title cascade speed
- r2-1 | round 2 | models.js SyntaxError hid every finding ("reports nothing") -> fixed; node --check after every edit | PITFALLS: a view whose findings all vanish
- r1-x | rounds 1-2 | text boxes padded (overlaps), tagBox contrast, neon-green type, squashed clip, boxes rounded into "D", kit dark board BLANK, test-media credits, base vocabulary ("stick figure"), direction.md missing -> fixed | PITFALLS lines 1-7

## Intended (medium findings left on purpose)
_(none)_

## Critics
### Critic 1 (round 6, builder's evidence pass, no score)
Not a fresh subagent: the member had not asked for agents in this session, so the builder prepared the critic's sheets
(review/critic1: targets t1-t4 from the reference, renders r1-r4, side by side, edges overlay) and judged them itself.
A fresh critic (docs/CRITIC.md) is still to run; its score decides the stop rule.
- c1-1 | accepted -> fixed in round 6 | t4: the crowd was a neat grid of same-size heads (side4: reference heads 60-140 px, loose rows, two heads apart bottom right) -> diameters 58-146 px, broken rows, turned wobbly ovals, varied hooks, two detached heads
- c1-2 | accepted -> fixed in round 6 | t4: tracked caps set every word upright (side4: reference "VIEWERS" / "PLATFORM" red italic, black words upright) -> coloured words italic in upright lines
- c1-3 | accepted -> fixed in round 6 | t3: the hit's list shrinks the earlier items (side3: N-q 20.5 s items at ~25 px above the current one at 62 px) -> `heading(..., { shrink: true })`
- c1-4 | accepted in part | t1: figure proportions. Row profile (critic1, measured): reference head .47 H wide, hip .76 H, arms span .27 H, shoulders .08 H under the head; ours .50 / .73 / .33 / .04 -> head .46, shoulders .08, arms 24 deg. The legs (.23 H) already matched: rejected "legs too short" with that profile
- c1-5 | accepted -> fixed in round 6 | t1: the hits use bold italic lines on #fcfcfc (hit_sides: page pixel 252) -> the Era control and the Hit look

## Sign-off
- 2026-11-01, kit 1 (app 0.20.0), base starter engine 1 -> dmscales engine 2 (encoder fallback, theme, sketch(), era key)
- `cz check dmscales` (hero, kit, motion, templates, sample, 8 must-fails; 16:9 + 9:16): READY, 0 high, 0 medium, 1 low (the base's own banned calls)
- `cz check dmscales --look look-hit`: READY, 0 high, 0 medium
- `cz check dmscales --controls`: the Era control changes the frame (later vs hits)
- Must-fails seen red before their checks, then firing: RED, PAGE, HOLD, VOID (+ the base's overlap, cut, small, DARK)
- Frames looked at: sample 16:9 at 0.3 1.1 1.6 2.5 3.2 4.2 5.2 5.6 6.4 7.9 8.4 9.7 10.3 11.6 12.8 13.4 14.0 14.5 15.6 17.1;
  9:16 at the same times; the full 16:9 export at 2 fps (out/review16.png) and 9:16 at 1 fps; hero 1/3/5 both aspects;
  kit dark board 1.5 9.5 19.5 23.5 29.5 32.5 35.5 39.5; templates 2.3-22.0; motion 0.5-13.5
- Consecutive frames: the title cascade 10.60 / 10.62 / 10.65 / 10.68 / 10.72 / 10.76 / 10.85 / 11.00 (motion); the clip's
  shrink 3.0 / 3.05 / 3.12 / 3.3 (motion); the curve's draw-on 5.6 / 6.2 / 6.7 / 7.2 (sample)
- NO_SLOP section 7: checks first (done), each check seen failing (done), frames at full size (done, list above), readability
  (no one hidden, every picture shows its words, the sample reads without sound), findings written finding -> meaning -> fix (above)
- Banned overlay grep (stamp, verdict words, AI-voice notices) in scenes, models.js, skill, style.json: 0 hits (one false
  match: "till the end" in a footnote)
- Member's approval of the sample: _(pending: the member watches out/sample_16x9.mp4 and the Hit look)_
- Battle test 1 (2026-11-01): projects/ilk-30-saniye, a 30 s Turkish sample in the Hit look, silent (no voice credit left),
  timed at a syllable-based reading pace, no member files. The app's Build could not start (the Claude account's weekly
  limit), so the scenes were built in-session from DIRECTION.md (edit-plan.md first); check_preview clean, check_layout
  clean at 39 frames, 4 style faults found and fixed (r7-1..r7-4)
- Still open before calling it premium: a fresh critic's score (>= 8), and the battle test with the member's own voice and
  screenshots through the app's Build
