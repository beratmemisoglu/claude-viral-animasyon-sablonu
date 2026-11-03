# 03 · Production System: how we generate our own thumbnails

Agent 3 of 3. Scope: the pipeline, the generator spec, a working prototype, the rig upgrades needed for thumbnails, the Remotion port and QA.
The click logic (what to show and why) is covered by agents 01/02. This document covers how we make the image.

**TL;DR**
- **Default path:** SVG thumbnail generator built from `hero-rig.js` plus a dedicated "thumbnail head", rendered by headless Edge now and by a Remotion `<Still>` later. It is free and deterministic, renders in about 3 s, stays 100% on-model, and we own the art outright. A working prototype is in `proto/`.
- **Premium path:** the hybrid. Render the SVG composition, run AI img2img at low denoise for a painterly finish, then put the SVG text back on top. Use it for a channel's first five or so uploads and for videos that are already outperforming.
- **Not recommended as default:** pure AI generation from the character sheet. The character drifts (sprout, eye shape, outline weight, body proportions), the output is not reproducible, and it brings legal and originality risk.

Prototype output (1280×720, plus a `_320` mobile preview of each):

| preset | full | mobile |
|---|---|---|
| `bedClock`: "DAY 1." glaring at a blue 5:00 alarm | `proto/out/bedClock.png` | `proto/out/bedClock_320.png` |
| `doorLight`: "JUST START." hand on the handle, light leaking through the door gap | `proto/out/doorLight.png` | `proto/out/doorLight_320.png` |
| `phoneBed`: "3 AM." face lit blue by the phone, notifications floating up | `proto/out/phoneBed.png` | `proto/out/phoneBed_320.png` |
| param variants (custom text, accent swap, zoom, shadow twin, expression) | `proto/out/var-*.png` | `proto/out/contact_variants_320.png` |
| safe-zone overlays | `proto/out/*_debug.png` | `proto/out/contact_320.png` (all 3 side by side) |

---

## 1. Pipeline options compared

What the references actually are (from T1–T3): bespoke compositions, not video frames. They use flat cel shapes plus a light painterly layer: soft form shading, one coloured light source with a rim on the lit side, bloom around the source and a dark vignette. There is no texture-heavy painting. Thumbnails T2 and T3 show tell-tale AI-finish traits (soft glow halos, slightly melted outline weights, fur-like brain texture), which suggests the competitor itself uses an AI pass. All of the rendering they need can be reproduced with SVG gradients, masks and filters.

| | (a) Pure SVG/HTML from hero-rig.js | (b) AI generation from the character sheet | (c) Hybrid: SVG comp → AI img2img → SVG text |
|---|---|---|---|
| **Quality** | Clean, crisp, "premium flat". It gets about 80% of the painterly look through gradient shading, rim-light filters, bloom, vignette and grain. Lacks organic texture. | Can look richest (soft light, texture). Text rendering is unreliable, so text has to be overlaid anyway. | Highest. It keeps the exact composition and pose and gains organic light and texture. |
| **Consistency with our character** | 100%. It uses the same rig math, palette, sprout, eyes and outline as the films. | Weak to medium. Typical drift: the sprout disappears or becomes hair, eyes get pupils or whites, the body grows, the outline thickens, skin turns grey or white. Needs a reference image and/or a trained LoRA, and cherry-picking. | High at low denoise (0.25–0.40), because the SVG fixes silhouette and face. Above about 0.45 drift returns. |
| **Speed** | Around 3 s per render. Batch variants for A/B tests are trivial (JSON in, PNG out). | 20–60 s per image, plus 4–12 attempts to find an on-model one, plus text overlay. | SVG (3 s) + img2img (20–60 s × 2–4 tries) + overlay. Roughly 5–10 min of human time each. |
| **Cost** | €0 marginal. | Credits per image × retries. | Credits for a few img2img runs. Cheap per thumbnail, but it adds up across A/B variants. |
| **Determinism / A/B** | Fully reproducible. Change one parameter and only that changes, which makes clean A/B tests possible. | Not reproducible, and every variant differs in many ways at once, so A/B results are noisy. | Composition stays reproducible; finish varies slightly. |
| **Originality / legal** | Our own code and art; no third-party style ingestion; full ownership. Lowest risk. | Risk of competitor style bleed if prompts or references mention or resemble Day One Films. Model terms vary, and copyright in pure AI output is uncertain in some jurisdictions. Never feed competitor thumbnails as references. | Lower risk than (b), because the human-authored SVG dominates the image. Same rule: only our own renders and character sheet go in as references. |
| **Brand control (one accent, our blue)** | Exact hex colours. | The model tends to over-saturate or add extra colours. | Re-tint or colour-grade after the AI pass if needed. Text is always SVG. |

**Recommendation**
- **Default = (a).** Every film gets an SVG thumbnail from the generator below, with 2–3 variants for YouTube's "Test & Compare".
- **Premium = (c).** Use it for launch videos and winners: take the (a) render with the text hidden (`text: ""`) and run img2img in the main session through the Higgsfield MCP (`generate_image` with the SVG PNG as the image reference). Prompt along the lines of "same composition, soft painterly 2D cartoon lighting, gentle rim light, subtle paper grain, keep flat sand-coloured round head with thin dark outline and the small leaf sprout, keep solid black oval eyes". Use low strength, generate 2–4 candidates, reject any that drift (sprout, eyes, outline, colour), then composite the original SVG text layer on top. Never put text in the prompt.
- (b) is useful only for **exploration**: brainstorming new scene ideas or props. The chosen scene is then rebuilt as an SVG preset.

---

## 2. Thumbnail generator spec

### 2.1 Layer stack (bottom → top). Implemented in `proto/thumb.js → render()`

| # | Layer | Rules / implementation |
|---|---|---|
| 1 | **Background** | Near-black base `#07–0B` tinted toward the accent (blue-black for blue, brown-black for amber). No pure #000, which looks dead after YouTube compression. |
| 2 | **Environment, back** | 2–4 simple props max (bed, pillow, nightstand, door, headboard). Dark values on dark ground, separated by a **lighter outline** (`#30–47` grey-blue, 4–6 px) instead of the hero's ink outline. Props are low-contrast so the face wins. |
| 3 | **Accent light** | Exactly **one coloured light source** in the frame (clock digits, door gap, phone screen). Three stacked passes: core (accent mixed 55–75% to white) → 4 px blur → 14–40 px blur bloom → a full-frame radial `screen` spill (radius 520–620 px, 0.4–0.55 alpha). |
| 4 | **Hero body** | The `hero-rig.js` body (`noHead: true`), followed by two light passes: (i) form shade, a radial gradient centred on the light that darkens away from it, masked by the body silhouette; (ii) accent tint near the light (`screen`). Then a **rim light** using a filter of the form `SourceAlpha − offset(SourceAlpha, away from light)`, flooded with accent mixed 45% to white. Extra hands are drawn after props so they can grip them. |
| 5 | **Thumbnail head** | A dedicated painterly head (see §4), larger than in films, placed by the crop rules below. |
| 6 | **Environment, front** | Blanket and foreground occluders, plus the cast shadow of the head on the pillow. |
| 7 | **FX** | Topic metaphor particles in the accent colour (notification bubbles, sparks). At most about 7 elements, decreasing in size along one arc. |
| 8 | **Grade** | Radial vignette (0 → 0.7 black at the corners), then fractal-noise grain at 0.07 opacity in `overlay` mode. Grain hides gradient banding after YouTube's JPEG/WebP recompression. |
| 9 | **Text** | Heavy rounded sans (**Fredoka 700**; fallbacks Baloo 2 800, Nunito 900), white `#FFF`, dark stroke `#06070B` at 7.5% of the font size using `paint-order: stroke`, plus a drop shadow (dy 7, blur 7, 75%). ALL CAPS, **always ending with a period**. 1–3 words. Auto-fit: start at 168–170 px, shrink to the max width. |
| 10 | **Safe-zone check** | `debug:true` overlay: 52 px side margins, timestamp box at bottom right (174×48), progress-bar strip at the bottom (8 px), text bbox and head-ratio readout. |

### 2.2 Crop and composition rules
- **Head diameter = 40–48% of frame height** (radius 145–170 px at 720p). The references measure about 38–45%. The prototype gives bedClock 46%, doorLight 41% and phoneBed 42%.
- Head centre in the **middle third horizontally** (x 450–770), vertically at y 370–425, so the sprout clears the text band (text block ends around y 170–200).
- **Gaze vector points at the accent object.** The object sits in the opposite half of the frame from the head's back, at 0.35–0.6× the head size, and is the brightest thing in the image.
- Body is cropped by the frame bottom or a blanket. No feet: the thumbnail is a close-up.
- Text: `top-left` when the object is on the right and the head centre-left (T1 layout); `top-center` across the full width when the head is central (T2/T3 layout). Text never overlaps the face. It may overlap the sprout tip or background.
- Nothing important in the bottom-right 190×70 box (timestamp).

### 2.3 Parameters
`text`, `textLayout`, `textSize`, `font`, `preset` (scene), `accent` (hex), `light {x,y}`, `expression` (thumbnail set), `look [x,y]`, `extras` (sweat / bags), `head {x,y,r,tilt}` (crop override), `zoom` + `focus` (camera push toward the face), `props` (per-preset: `clock`, `bubbles`), `twin` (optional glowing shadow twin for A/B), `grain`, `debug`.

### 2.4 JSON schema: thumbnail request

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "theotherself/thumbnail-request.json",
  "title": "ThumbnailRequest",
  "type": "object",
  "required": ["preset", "text"],
  "properties": {
    "id":        { "type": "string", "description": "output file stem, e.g. discipline-v1" },
    "film":      { "type": "string", "description": "film slug this belongs to" },
    "preset":    { "enum": ["bedClock", "doorLight", "phoneBed"], "description": "scene preset (extend per film)" },
    "text":      { "type": "string", "maxLength": 18, "pattern": "^[A-Z0-9 '’!?:-]+\\.$", "description": "1–3 words, ALL CAPS, ends with a period" },
    "textLayout":{ "enum": ["top-left", "top-center"] },
    "textSize":  { "type": "number", "minimum": 110, "maximum": 190, "description": "max px; auto-shrinks to fit" },
    "font":      { "enum": ["Fredoka", "Baloo 2", "Nunito"], "default": "Fredoka" },
    "accent":    { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$", "default": "#2F6BFF", "description": "the ONE light colour" },
    "light":     { "type": "object", "properties": { "x": {"type": "number"}, "y": {"type": "number"} } },
    "expression":{ "enum": ["glare", "resolve", "tired", "shocked", "sad", "hopeful", "anxious", "content"] },
    "look":      { "type": "array", "items": { "type": "number", "minimum": -1, "maximum": 1 }, "minItems": 2, "maxItems": 2 },
    "extras":    { "type": "array", "items": { "enum": ["sweat", "bags"] } },
    "noExtras":  { "type": "array", "items": { "enum": ["sweat", "bags"] } },
    "head":      { "type": "object", "properties": { "x": {"type": "number"}, "y": {"type": "number"}, "r": {"type": "number", "minimum": 130, "maximum": 180}, "tilt": {"type": "number"} } },
    "zoom":      { "type": "number", "minimum": 0.8, "maximum": 1.5, "default": 1 },
    "focus":     { "type": "object", "properties": { "x": {"type": "number"}, "y": {"type": "number"} } },
    "props":     { "type": "object", "properties": { "clock": {"type": "string", "pattern": "^[0-9:]{3,5}$"}, "bubbles": {"type": "boolean"} } },
    "twin":      { "type": "object", "properties": { "x": {"type": "number"}, "y": {"type": "number"}, "scale": {"type": "number"}, "opacity": {"type": "number"}, "mood": {"enum": ["smug", "slit", "sad"]}, "facing": {"enum": [1, -1]} } },
    "grain":     { "type": "number", "minimum": 0, "maximum": 0.15, "default": 0.07 },
    "debug":     { "type": "boolean" }
  }
}
```

---

## 3. Prototype: `proto/`

| file | role |
|---|---|
| `thumb.html` | 1280×720 stage. Loads Google Fonts (Fredoka/Baloo 2/Nunito), `hero-rig.js` and `thumb.js`. Renders from URL params or an inline `window.THUMB_CONFIG`, then re-renders on `document.fonts.ready` so the auto-fit measures the real font. |
| `thumb.js` | The generator: thumbnail head, body light passes, the 3 presets, 7-segment clock, compositor, text fit, debug overlay, URL parser. |
| `hero-rig.js` | **Copy** of `brand/character/hero-rig.js` with two additive thumb upgrades (`opts.noHead`, `TOS.headAnchor()`). The brand file is untouched. |
| `render.py` | Headless Edge → `out/<id>.png`, PIL Lanczos → `out/<id>_320.png`, `out/contact_320.png`, plus `--debug` safe-zone renders. |
| `examples.json` | Request examples (text, clock, zoom, accent swap, shadow twin, expression). |

**Usage**
```powershell
cd "thumbnail-research\03-production-system\proto"
python render.py                 # 3 presets → out\bedClock.png, doorLight.png, phoneBed.png (+ _320 + contact sheet)
python render.py --debug         # + *_debug.png safe-zone overlays
python render.py examples.json   # any list of ThumbnailRequest objects
```
Open in a browser for live tweaking (file:// works; network is needed for the font):
`thumb.html?preset=bedClock&text=DAY%2047.&clock=4:59&expr=resolve&zoom=1.1&debug=1`
URL params: `preset text accent expr zoom size layout clock look=x,y head=x,y,r[,tilt] extras=sweat,bags twin=1 grain debug=1 scale=0.25` (scale 0.25 = a live 320×180 view), or `config=<JSON or base64 JSON>`.

Edge flags that matter: `--virtual-time-budget=8000` (wait for the web font and re-render), `--force-device-scale-factor=1`, `--allow-file-access-from-files`.

**What was verified visually:** all 3 presets plus 3 variants at 1280×720 and 320×180. At mobile size the text, the face expression (brow angle) and the light source read instantly. The head is 41–46% of the frame height. The safe zones are clean: nothing important sits under the timestamp. Iterations fixed the following:
- arc brows that read as "worried": made them straight and steeper;
- a secondary blue catchlight that read as a tear: removed;
- a door arm that read as "zombie": the handle was lowered and moved closer;
- phone hands that did not hold the phone: added a gripping hand on the phone edge;
- a stray second mouth line: removed;
- a second background shape that competed with the accent: removed.

**Known limits:** limbs stay rig-thin, so they look flatter than the head (acceptable, and on-brand). Presets use hand-placed geometry, so a new scene means a new preset function (about 40–80 lines). The rim on the body is a uniform-width band, not true normal-based lighting.

---

## 4. Thumbnail-specific face and rig upgrades (needed in hero-rig.js)

Implemented in the proto (`thumb.js → thumbHead/thumbFace`, `proto/hero-rig.js`). These should be merged into the brand rig as a **`thumb` LOD** (level of detail) so films keep the light film face.

1. **`noHead` option** on `hero()`. It renders the body only, so a high-detail head can be composited (done in the proto copy).
2. **`headAnchor(opts)`** returns the head centre, radius and tilt in screen space for a given placement, including the `headTilt` pivot. It is needed for compositing and crop rules (done).
3. **`placeHero(pose, hx, hy, r)`**: inverse placement ("put the head here at this size") plus **`toRig()`** for IK targets in screen space (in `thumb.js`).
4. **Bigger eyes:** ×1.26–1.5 (`rx 5→6.6`, `ry 7.6→10`), spread +1.5. Highlight radius 0.36·rx (it was 1.5 u) so it survives 4× downscaling. A faint accent tint is mixed into the highlight.
5. **Angled upper-lid cut** per eye (clip by a rotated half-plane, plus an ink lid line). This is the single biggest legibility gain for anger and fatigue, and the film rig can only switch between whole eye shapes.
6. **Thick, near-straight brows:** stroke 5.5 → 7.2 u, length +20%, curvature parameter `browCurve`, stronger angle ranges (glare outer −29 / inner −11).
7. **Eye bags:** a blurred mauve ellipse (`#6E4C5C`, 38%) plus an ink arc under each eye. This is the "tired / dopamine / 3 AM" signal.
8. **Sweat drop ×1.55** with an ink outline and a white highlight (the film version has no outline and disappears on dark backgrounds).
9. **Thumbnail mouths:** `grit` (asymmetric angry frown), `pout`, small `o`, `wobble`.
10. **Painterly head shading:** a radial gradient biased toward the light (hi = body mixed 45% to `#FFF4E2`, lo = body mixed 38% to `#5A3A26`); accent `screen` tint on the lit side; a two-layer rim (crisp crescent mask plus a soft wide crescent) computed from the light direction in head space.
11. **Thicker outline** on the head (3.4 u vs 2.6 u) and the sprout (stem 4.6, leaf 3.6). Sprout leaf filled with a gradient.
12. **Light-aware body pass:** silhouette mask → form-shade gradient, accent tint, and a rim-light filter from the light direction.
13. **Thumbnail expression set** `TX`: glare, resolve, tired, shocked, sad, hopeful, anxious, content. These map to the film `EXPR` names where they overlap, so a film's key emotion carries straight into its thumbnail.
14. *(Future)* an optional **front-facing 3/4 "q" up to 1.0** for the face, and a `blanket`/`hand` primitive in the rig, so presets do not hand-draw them.

---

## 5. Remotion port plan

```
src/
  lib/character/hero-rig.ts      # 1:1 port of hero-rig.js (+ noHead, headAnchor) — returns JSX instead of strings
  lib/thumb/ThumbHead.tsx        # thumbHead/thumbFace → JSX; ids via useId() (avoid collisions when several Stills render)
  lib/thumb/lightPasses.tsx      # <LitBody>, <GlowSpot>, <Grade> (vignette+grain), <SevenSeg>
  lib/thumb/presets/*.tsx        # bedClock, doorLight, phoneBed … one file per scene, same build(c, L) contract
  lib/thumb/schema.ts            # zod schema mirroring §2.4 → Remotion `schema` prop → editable in Studio UI
  thumbnails/Thumbnail.tsx       # <Thumbnail {...ThumbnailRequest}/> compositor (layer stack §2.1)
  Root.tsx                       # one <Still> per film + variants
```
```tsx
// Root.tsx
<Still id="discipline-thumb-a" component={Thumbnail} width={1280} height={720}
       schema={thumbnailSchema} defaultProps={films.discipline.thumbnails[0]} />
```
- **Fonts:** `@remotion/google-fonts/Fredoka` with `loadFont()` (the font is bundled, so there is no network race). Text fitting uses `measureText()` from `@remotion/layout-utils` instead of `getComputedTextLength`.
- **Filters:** SVG filters (feGaussianBlur, feTurbulence, feComposite rim) render identically in Remotion's headless Chrome. Keep `mix-blend-mode` on SVG elements, which Chrome supports.
- **Render:** `npx remotion still src/index.ts discipline-thumb-a out/discipline-a.png --image-format=png`. Add a script that loops over `films/*.json` thumbnails and emits the `_320` previews and the contact sheet (sharp, or keep the Python step).
- **Single source of truth:** each film's `film.json` carries `thumbnails: ThumbnailRequest[]` (2–3 A/B variants). The skill `inner-voice-film` writes these during packaging.
- **Premium hook:** `npm run thumb:premium <id>` renders with `text: ""`, hands the PNG to the img2img step (Higgsfield in the main session) and recomposites the text layer, which it renders alone as a transparent PNG with `--image-format=png` and the background hidden.

---

## 6. QA checklist (run on every thumbnail before upload)

**Mobile legibility (check `_320.png` and the contact sheet, never only the full size)**
- [ ] Text readable at 320×180 in under 1 s. It is 1–3 words, cap height ≥ 15% of the frame height (about 110 px at 720p; the presets use about 120 px), and ends with a **period**.
- [ ] The expression reads at 320 px: brow angle and eye shape are unambiguous (squint at the image to test).
- [ ] Head diameter 38–48% of the frame height. The face is not occluded by text, props or particles.
- [ ] Squint/blur test: the three brightest things are text, face and light source, in that order.

**Safe zones**
- [ ] Nothing important in the bottom-right 190×70 px (timestamp) or the bottom 8 px (progress bar).
- [ ] Text inside 52 px side margins. The sprout may touch the text band but must not collide with letters in an ugly way.
- [ ] Still works when cropped to the centre (YouTube sometimes shows thumbnails cropped or with overlays).

**Contrast and colour**
- [ ] **One accent colour** only. Default brand blue `#2F6BFF`; one topic-metaphor colour is allowed (e.g. warm amber for "a door / a start"). No competitor red.
- [ ] Background is dark but not pure black, and props are separated by lighter outlines.
- [ ] White text has a dark stroke and a shadow. Contrast against the area behind it ≥ 7:1.
- [ ] Grain present (no visible banding in the glow after export).

**Clutter and brand**
- [ ] At most 4 props plus 1 accent object. FX particles ≤ 7.
- [ ] The character is on-model: sprout present, solid black oval eyes with highlight, sand body, thin ink outline, no pupils or whites added. This matters most after any AI pass.
- [ ] No competitor elements (bean body, red accent, their exact compositions or text). The thinking is copied, not the art.
- [ ] The thumbnail promises something the film actually shows (the same expression or prop appears in the film).
- [ ] Shown next to the other uploads in the contact sheet, it is distinct but recognisably part of the channel's series (same font, dark field, one light, the Moon head).
- [ ] 2–3 variants are exported for YouTube Test & Compare, and each differs in **one** variable only (text, expression, accent object or zoom).
