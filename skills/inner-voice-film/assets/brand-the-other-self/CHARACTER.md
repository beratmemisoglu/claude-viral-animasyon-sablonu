# The Other Self — Main Character Spec (v2 · "Moon head", chosen 2026-10-14)

Single source of truth: `hero-rig.js` → `STYLES.moon` (default style). Preview: `character-sheet.html`
(+ `character-sheet.png`). Alternatives kept for reference only: `compare.html` (bean / lantern / drop).
Every film uses this character. Port 1:1 to `src/lib/character/` in the Remotion studio (same math, same paths).

## Concept
The hero and the inner voice are **the same person**. The shadow is his exact silhouette — big round head,
small body, the sprout on top — inverted: hollow black with an electric-blue glow. The channel name is the
character: *the other self*. The sprout = growth; it can be used as a quiet progress motif (droops at rock
bottom, stands up at the turn).

## Brand signatures (never change)
| Signature | Hero | Shadow twin |
|---|---|---|
| Silhouette | big round head (r 58) on a small rounded body, stick limbs | identical |
| Sprout on top of the head | ink stem + sand-coloured leaf | black stem + black leaf inside the glow |
| Eyes | tall ovals `rx 5 ry 7.6` + white highlight | his eye shapes, narrowed, tilted, glowing |
| Outline | thin ink contour on the whole figure (2.6 u) | none (glow instead) |
| Body | warm sand `#E9C9A2`, ink `#2B1F17` | `#04050B` |
| Far limbs | same paint, group opacity 0.55 | solid black |
| Glow | — | wide blur `#2F6BFF` @0.85 + rim `#7FA6FF`, eyes `#D6E4FF`; constant (no pulse) |

Default `topicAccent` = electric blue `#2F6BFF` (brand). A film may re-tint the twin's glow/eyes only when the
colour is part of the topic metaphor; the body never changes. Extras: sweat `#A9CFF2`, blush `#E9A99C`.

## Rig (units, ground y = 0, y down, faces +x)
pelvis 92 above ground · torso rounded box top −94 / bottom +14 (pelvis space) · head separate, centre (6, −146),
r 58 · shoulders near (14,−70) far (−12,−72) · hips ±10 · arm 42+38 · leg 44+44 · limb width 13 · hand r 9 ·
foot 13×7 · face/topper scaled by r/50. Angles: 0° down, +90° forward. Limbs = one FK path each (no detachment).
Front view: `pose.front = true`. Seated/curled heights resolve from leg length (`'SIT'`, `'CURL'`).

## Libraries in hero-rig.js
15 expressions (neutral, content, sleepy, asleep, shocked, numb, sad, crying, determined, straining, confident,
happy, lonely, hopeful, anxious — hard-swapped in films) · 10 poses (standing, front, sad, determined, walk, run,
sitEdge, punch, guard, curled) · shadow faces (smug, slit, sad) · modes full / headOnly (bed) · token example
headband (scales with the head).

## Scale in a film (× hero standing height)
couch 1.1 · desk 1.2 · mirror 1.0 · boss 2.5 · final 0.5.
