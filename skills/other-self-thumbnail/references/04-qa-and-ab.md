# 04 — QA checklist + A/B testing (YouTube Test & Compare)

## QA (every thumbnail, look at the `_320.png` and `contact_320.png`, not only full size)

**Mobile**
- [ ] Text readable at 320×180 in < 1 s; 1–3 words, ends with "."; cap height ≥ 120 px at 720p.
- [ ] Expression reads at 320 px (squint test): brow angle and eye shape unambiguous.
- [ ] Head 34–49 % of frame height; face not covered by text/props/particles.
- [ ] Brightness order: text > face > emitter. One flank stays dark.

**Safe zones**
- [ ] Nothing important at bottom-right (timestamp) or the bottom 8 px; text inside 52 px margins.
- [ ] Still reads when centre-cropped.

**Colour / brand**
- [ ] Exactly one emitter hue, matching the topic metaphor; blue only as a hint; no competitor red.
- [ ] Background dark but not pure black; grain present (no banding).
- [ ] Character on-model (sprout, oval eyes + highlight, sand body, thin outline) — especially after a Higgsfield pass.
- [ ] No competitor elements (bean body, red glow, their compositions or text).

**Promise**
- [ ] Text does not repeat the title word.
- [ ] The scene/expression actually appears in the film (first 15 s or the turn) — Test & Compare is judged on
      watch-time share, so over-promising loses.
- [ ] In the contact sheet next to previous uploads: distinct, yet clearly the same series.

## A/B (up to 3 variants, watch-time share decides, 1280×720 minimum, desktop Studio)

| Slot | Variant | Tests |
|---|---|---|
| A (upload first; wins ties) | house concept: verdict/time text + blue hint | baseline |
| B | same image, different **text job** (step vs time vs lie vs no text) | which text adds most |
| C | different scene/trigger, or no blue hint, or flat vs Higgsfield-painterly | which trigger fits the topic |

Change ONE big axis per variant. Rotate the tested axis across uploads: text job → twin hint → emotion →
emitter hue → flat vs painterly. Never test tiny differences.

Log per video (48 h and day 7): topic · title format · variant ids + triggers used (taxonomy #) · text job ·
twin hint · emotion · emitter hue · render (flat / painterly) · T&C result + watch-time share · CTR vs channel
median · AVD % · retention at 0:30 · traffic mix · top "suggested from" videos.
Decision rules: higher CTR but lower watch-time share = over-promise → fix image or hook. Three consistent wins
for a setting in a topic family (fight / loss / fear) → make it that family's default.
