# 04 — The Inner-Voice Antagonist

Contents: 1 Identity · 2 Body & glow construction · 3 Face library · 4 Poses · 5 States & timings ·
6 Size/glow curve across the film · 7 Writing the lines · 8 Words as objects · 9 Topic re-skin ·
10 Component API

Copy-paste SVG, filter variants and per-topic 10-line ladders: `deep-research/03-inner-voice.md`.
Measured behaviour (wins on conflict): `03-visual-canon.md` §7.

---

## 1. Identity

It is not a monster that shouts. It is a *friend who wants you comfortable* — smug, serene, certain it will
win. Its power: it sounds like your own thought (2nd person, lowercase, appears **behind** you); it offers
relief now for cost later; it turns repeated behaviour into identity. Its face stays smug until it loses.
It only gets big when it is **desperate** (the hero is already winning). It is the channel's recurring
brand villain: **same body in every film**; lines, props, accent colour and defeat method change.

## 2. Body & glow construction

**Our channel**: the inner voice is Moon head's exact black twin — `hero({ shadow: { mood } })` in
`assets/brand-the-other-self/hero-rig.js` (same silhouette and sprout, fill `#04050B`, glow `#2F6BFF`, rim
`#7FA6FF`, eyes `#D6E4FF`). The numbers below describe the reference films' shadow and are kept for behaviour/
glow technique only; the stacked-glow method is what `hero-rig.js` already does.

- The hero's silhouette, slightly narrower torso and longer, thinner legs (a stretched "adult" version).
  In the mirror it uses **the hero's exact silhouette** (it *is* his reflection) and has **no face**.
- Canonical rig (H = 600 units, origin between the feet, y up negative): head circle r 95 at y −505 (no neck,
  overlaps a bean torso 180 wide from −445 to −198); hips ±32 at −215; legs stroke 36 to ankles ±36 at −20;
  feet ellipses 32×18; shoulders ±78 at −388; arms 95 + 90, stroke 30; mitt hands r 26.
- Fill `#000–#050505`. **Glow = 3 stacked copies (cheap, recommended)**: copy 1 accent `#E8381F`-ish blurred
  ≈ 0.035·H_px at 0.85 opacity · copy 2 rim colour blurred ≈ 0.009·H_px at 1.0 · copy 3 crisp black on top.
  Build the silhouette once (`<symbol>`/`<g id>`) and `<use>` it three times. Even cheaper: stacked strokes of
  widths 60/34/14 px at 0.12/0.25/0.55 opacity. **Never animate stdDeviation**; animate opacity.
- Measured look: soft orange-red outer glow ≈25–30 px falloff at 1080, a thin brighter rim, **constant**.
- Face on top with its own small glow: strokes in a light accent tint (`#FF7E66` for red), width ≈10 eyes / 8 mouth.

## 3. Face library

| eyes | look | when |
|---|---|---|
| `smug` ∩ arcs | closed, outer ends drooping | default whisper / gloat |
| `lidded` | flat dashes | first peek, bored comfort |
| `slit` | glowing dashes tilted down to centre (‾\ /‾) | "ignited", after a line lands, lunge |
| `sly` ⌒⌒ | arched squint | second line of a scene |
| `wide` | filled circles | being hit, last flare |
| `sad` | inner ends high | tiny/defeated |
| `none` | — | mirror, far background |

mouth: `smile` (on only while speaking) · `grin` (wide V, gloat/block) · `smirk` ("told you.") · `flat` (defeated) · `none`.
Swaps are **hard cuts**, not morphs.

## 4. Poses (hold them; no gesture loops)

`lurk` behind furniture, near hand raised to the mouth (whisper) · `lean` hand resting on the hero's chair back
(possessive) · `shoulder` hand on his shoulder (DOPAMINE creature: hand on his back) · `mirror` arms down,
faceless · `block` arms wide on a path (giant) · `loom` leaning down over a small hero · `lunge` pointing ·
`defeated` head down, slouched, tiny.

## 5. States & timings (30 fps)

| State | Recipe |
|---|---|
| **pre-planted** | glow blob visible on the floor/behind furniture from the scene's first frame |
| **rise** (default entrance) | mask at the furniture edge or the floor line; translateY from +body height → 0, ease-out cubic, 33–45 f; floor version reads arc → dome → head (grin already on) → shoulders → body; settles 6–9 f |
| appear-in-place (montage) | cut to a shot where it's already there |
| **face ignite** | smile first while peeking → eyes 0→1 over ~9 f → smile on during each spoken line, off between lines → eye swap for line 2 → slits after the line lands |
| **speak** | text drawn over its head (§8 of canon); harsher line: glow ×1.5 wider/brighter, eyes hotter |
| idle | **nothing** (no pulse, no sway) — keep it planted. Optional ≤ 1–2 px drift only in Act 3 boss shots. |
| **lunge** (boss "you can't.") | 0–6 f anticipation scale 0.97, glow 0.8 · 6–12 f burst scale 1.12 (back-out), arms to block, eyes→slit, glow 1.6 · 8–14 f text slams in (scale 1.4→1, 4 f) + camera shake · 14–40 f settle |
| **hit** (punch) | body squash 0.9×1.1 over 4 f, recoil, glow flicker |
| **shatter / split** (boss defeat) | contact: 2 f white flash 0.25 + 3 f hit-stop · eyes wide, glow flare 2.0 · split along the hero's path with two complementary clip polygons; halves drift ±90 u, rotate ∓10°, fade 24 f · glow collapses 2→0 over 14 f · ~28 seeded embers rising (ash) |
| **shrink** | usually happens *between* scenes (cut straight to tiny). On screen: 45 f to 0.45×, glow →0.25, eyes→sad, pose→defeated |
| **defeated** | tiny, dim, ignored. May mutter one 30 px line at 0.4 opacity ("...maybe tomorrow?"). The hero never looks at it. |

## 6. Size / glow curve across the film

| Beat | Form | Size × hero | Glow | Line level |
|---|---|---|---|---|
| B02 | text only (no body) | — | — | excuse |
| B03 | behind furniture | 1.1 | 1.0 | permission / comfort |
| B04 | at his chair | 1.2 | 0.65 → 1.0 (+50 % on harsh line) | fake care · futility |
| B05 | his reflection, faceless, backlit | 1.0 | backlight 0.85 | identity · prophecy |
| B06 | absent — **he** believes it | — | — | (white narrator) |
| B08 | disembodied floating words | — | — | gloat, word targets |
| B10 | giant on the path | 2.4–3 | 1.6 | absolute negation |
| B12 | tiny by the ritual prop | 0.45–0.5 | 0.25 | silent |

## 7. Writing the lines

2–4 words (6 max), lowercase, period; "..." only on comfort/procrastination; "?" only on futility; never "!".
2nd person or imperative, concrete and present ("skip the gym." beats "you are unmotivated.").
First half uses care words (just, only, tomorrow, rest, deserve, one more, it's fine); middle uses identity
(you're [trait]. you'll never [change].); end uses absolutes (can't, never, nobody, always).
Plant and pay off: every late line calls back an early one; the narrator's thesis inverts the identity line.
One line per beat, two at most. White and red never share a frame (except the climax).

## 8. Words as physical objects

- Comfort lines appear and leave. Identity lines may **linger** dimming to 0.15.
- Grind ammunition: huge red words hang in the air above the target (≈110–175 px) with a tiny bob.
- **Shatter on punch**: the word splits into glyphs at the impact frame; each flies out (6–18 px/f, away from
  the impact, closed-form drag 0.92/f, spin), shrinks to ~0.65, dims to ~0.25–0.35, then **keeps drifting
  slowly in the background for the rest of the scene** (shards from several phrases accumulate). 10–20 dark-red
  ember dots. Purely a function of `(frame − impact, glyphIndex, seed)`. Code: `deep-research/04-typography.md` §5 `ShatterText`.
- Boss line cracks in half along the split line with the body.
- Grief variant: words **dissolve into warm light** instead of shattering.

## 9. Topic re-skin (`topicAccent` + one prop + defeat method)

| Topic | Accent (glow / voice text) | Eyes | Prop / badge | Defeat |
|---|---|---|---|---|
| **Default (The Other Self brand)** | electric blue `#2F6BFF` / text `#6E9BFF` | `#D6E4FF` | — | split in two / per topic |
| Discipline / procrastination (reference film) | red `#E8381F` / `#F94E46` | salmon `#FF836C` | — | split in two |
| Dopamine / phone | magenta `#F860A9` | cyan | red notification badge with a number | turned away from; colour floods back |
| Loneliness | cold blue-violet `#6F7BFF` (or keep red for brand) | pale | closes doors, turns phone face-down | warm light of another person enters, it shrinks |
| Heartbreak | rose `#FF5A7A` | pale pink | holds old photo / phone with their chat | he lets go, letters blow away like petals |
| Overthinking | amber-red `#FF7A3A` | white | red scribble yarn around his head | he acts; scribble snaps straight and falls |
| Anxiety | red | white | none — grows when avoided | he breathes and steps forward; it deflates |
| Comparison | acid green `#B8FF3A` | white | glowing phone screens of others | he turns the phone around, looks at his own counter |
| Grief | **no hostile accent**; dim warm ember | lidded only, never grin | stopped clock, sits in their chair | held, then fades into a small warm ember |
| Comfort zone | red | white | blanket / couch cushions | he exits through a lit door; it can't cross the threshold |

Keep the brand blue as the default if unsure — brand recognition beats novelty (red belongs to the competitor). Change accent only when colour is part of the topic's metaphor; the topic rows above give metaphor-driven alternatives.

## 10. Component API (sketch)

```ts
type IVState = 'hidden'|'preplant'|'rise'|'speak'|'idle'|'lunge'|'hit'|'split'|'shrink'|'defeated';
interface InnerVoiceProps {
  x: number; y: number;            // feet, px
  scale: number;                   // × hero standing height
  heroHeight: number;              // px
  facing?: 1 | -1;
  build?: 'voice' | 'reflection';
  pose: 'lurk'|'lean'|'shoulder'|'mirror'|'block'|'loom'|'lunge'|'defeated';
  eyes: 'smug'|'lidded'|'slit'|'sly'|'wide'|'sad'|'none';
  mouth: 'smile'|'grin'|'smirk'|'flat'|'none';
  accent: string;                  // topicAccent
  intensity: number;               // glow 0..2
  state: IVState; stateFrom: number;
  maskY?: number;                  // furniture edge / floor line for 'rise'
  splitAngleDeg?: number; seed: string;
  badge?: {text: string; color: string};
}
```
Everything derives from `frame − stateFrom`, `interpolate`, `spring`, `random(seed)` — no React state.
