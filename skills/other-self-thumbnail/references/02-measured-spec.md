# 02 — Measured Template Spec (1280×720)

Pixel-measured from the 3 viral thumbnails (`deep-research/01-visual-forensics.md` §1–7). Generator defaults follow it.

| Parameter | Target | Tolerance |
|---|---|---|
| Canvas | 1280×720 sRGB, PNG or JPEG q ≥ 90 (YouTube needs ≥1280×720 for Test & Compare) | – |
| Layout | two bands: text band top 18–22 % H (y≈25–205), picture band below; text never over the face | ±15 px |
| Background | near-black, luma 2–13, tinted toward the emitter; props dark navy/grey, separated by lighter outlines | ≤ 15 luma |
| Text | 1–3 words, ALL CAPS, ends with ".", one line, ≤ 13 glyphs | – |
| Text alignment | top-left (margin 30–52 px) only for a short label ≤ 6 chars ("DAY 1."); otherwise centred, 80–93 % W | auto in generator |
| Cap height | 140–155 px (19.5–21.5 % H); never < 120 px | ±8 px |
| Font weight | heavy rounded (stroke ≈ 22–24 % of cap height): Fredoka 700 / Baloo 2 800 / Nunito 900 | – |
| Text colour / outline | #FFFFFF, 8–10 px dark stroke + soft dark outer glow; contrast ≥ 15 : 1 (measured 19–20) | – |
| Head | width 21–27 % W (270–345 px), height 34–49 % H; centre x 35–55 % W, y 42–52 % H; may touch the text outline | ±40 px |
| Eyes | centre within 42–61 % W, 44–57 % H; brows thick and angled ≥ 25° so emotion reads at 168 px | – |
| Gaze | at the light object | 3/3 |
| Light object | centre x 66–80 % W, y 62–77 % H (lower-right thirds point), 3–10 % of frame | ±5 % |
| Accent | exactly one hue, 1.5–6 % of pixels, S ≥ 70 %, V ≥ 90 % at peak, topic-specific | – |
| Light behaviour | emissive bloom half-max 12–15 px, falloff to bg by 50–100 px, spill tints the face, 5–7 px rim on edges facing it | – |
| Face vs bg contrast | ≥ 7 : 1 | – |
| Brightest non-text pixel | on the face / within 100 px of the eyes | – |
| Negative space | one flank ≥ 14 % of frame left dark | – |
| Badge zone | nothing important in x ≥ 1090, y ≥ 650 (timestamp) and the bottom 8 px (progress bar) | – |
| Feed test | at 168×94 and 320×180: word readable, brow angle readable, one glowing shape readable | pass/fail |

What survives at phone size (measured): the word, the brow angle, one glowing coloured shape. Blankets, handles,
small props, particles and bags on the back disappear — don't spend effort there.
