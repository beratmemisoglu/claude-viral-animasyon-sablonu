# 04 — Görsel dil, plan listesi ve kurgu

Kaynak `deep-research/C`. Ricks muhtemelen AI anahtar kare + AI image-to-video (I2V) + CapCut tipi montajla üretiyor. Biz aynı zinciri **kendi karakterimizle** kuruyoruz: Higgsfield (görsel + I2V) → `assemble.py` (ffmpeg montaj).

## 1. Ölçülen kurgu grameri (hedeflerimiz)
| Metrik | Hedef |
|---|---|
| Plan süresi | 2,5–5 sn, medyan **3,8 sn**. 60 sn'de **14–16 plan**. |
| Kompozisyon değişimi | ~**1 sn'de bir** (kamera hareketi, ifade, obje girişi). Hiçbir an ≥1 sn statik değil. |
| Geçişler | **Sert kesme yok.** %50 dissolve (0,2 sn), %40 whip (hızlı kayma + blur), %10 morph (start/end frame). |
| Yoğunluk eğrisi | 0–10 sn yoğun, 30–40 sn hafif düşebilir, son 10 sn yine yoğun (final ifşa planı). |
| Hook | İlk 0,75 sn'de crash zoom / pull-out ya da obje close-up. İlk görsel olay ≤1,5 sn, ölçek reveal ≤2,5 sn. |
| Kare 0 | Karakter (ya da Clause'un damgası/dosyası) görünür, kamera zaten hareket halinde, altyazı ekranda. |
| Literal kural | Her cümlenin **somut ismi, söylendiği ±0,3 sn içinde ekranda.** Soyut kavram dünya içi tabela/etiket olarak yazılır ("OVERBOOKED", "NO-SHOW RATE 8%"). |
| Zorunlu planlar | Video başına en az 1 **kesit/cutaway** ("içeride ne var"), 1 **kuşbakışı/harita**, 1 **büyüteç iris insert** (Clause imzası) ve 1 **damga kapanış karesi**. |
| Renk | V ~%60, **S %40–48**. Aşırı doygun neon ya da kırmızı ağırlıklı sahneden kaçın (flop sinyali). |
| Yeni mekân | Cümle başında gelir. Aynı mekânda yeni kompozisyon, somut ismin söylendiği karede gelir. |

## 2. Kamera sözlüğü (`script.json` → `shot.camera`)
| Kod | Hareket | Ne zaman |
|---|---|---|
| `push_in` | Yavaş dolly-in | Replik, ifade ve anahtar isim anı (en sık, 4–8/video) |
| `truck` | Yatay kayma + paralaks | Uzun cümlede mekânı gezdirme |
| `whip` | Hızlı savrulma | "But / Then / So" dönüş kelimesi, yeni bilgi bloğu |
| `pull_out` | Close-up'tan genişe hızlı açılış | Hook ve ölçek reveal |
| `overhead` | Kuşbakışı / harita | Mekanizma ve yerleşim |
| `cutaway` | Kesit diorama | "İçeride ne var" ifşası |
| `iris` | Büyüteç daire inset | Mikro detay (Clause imzası) |
| `rack` | Rack focus | Sır ve twist anı |
| `morph` | Start/end frame dönüşümü | Nesneden ilişkili nesneye geçiş (1–2/video) |

## 3. Higgsfield üretim tarifi
Önce `models_explore(action:'recommend')` ile güncel model adlarını doğrula. Ekim 2026 itibarıyla iyi çalışan zincir:
- **Anahtar kare:** `generate_image`, `nano_banana_pro` (dünya içi tabela metni temiz) ya da `flux_3_image`, 9:16.
- **Hareket:** `generate_video`, `seedance_2_0` (start_image + referans; 4–5 sn, 720p+, sessiz). Taslak için `seedance_2_0_mini`. Morph için `start_image` + `end_image`.
- **Toplu iş:** `generate_image_batch` / `generate_video_batch` → `jobs_wait` → tek `show_generation_by_ids`.
- **Karakter tutarlılığı:** Referans sayfası bir kez üretilir ve `manage_reference_elements` ile **"CLAUSE"** elementi olarak kaydedilir. Sonraki her karede bu element kullanılır.
- **Maliyet kontrolü:** Üretimden önce `balance` kontrol et. Plan başına 1 anahtar kare ve 1 I2V; ıskalar dahil ~20 üretim/video. Kullanıcı bütçe vermediyse ilk videoda tahmini krediyi söyle ve onay al.

### 3a. Karakter referans sayfası prompt'u
```
Character turnaround reference sheet of an ORIGINAL cartoon mascot "CLAUSE": a short chubby
raccoon inspector, 2.2 heads tall, big rounded-square head with round ears, warm grey fur
#8C8A93, dark mask #3A3842, cream muzzle #F1E6D2, striped ringed tail, thick uniform dark navy
outline #1E2340, large round brass-rimmed glasses with white pill-shaped eyes and navy pupils,
green translucent visor cap, short teal #1F8A8A trench coat, mustard yellow scarf #F2B134, a
brass magnifying glass on a cord, a red rubber stamp in one hand, a manila folder labeled
"CASE" under the arm. Views: front, three-quarter, side, back. Below: 6 expression heads
(neutral, curious squint, shocked wide eyes, smug grin, alarmed, triumphant stamping).
Flat cel shading with one soft shadow tone, clean vector-like lines, plain light grey
background, consistent proportions, no extra text.
```

### 3b. Sahne anahtar karesi şablonu (`shotlist.py` her plan için doldurur)
```
Vertical 9:16 frame. {SUBJECT_ACTION} — the key object "{NOUN}" clearly visible and large —
in {SETTING}, {TIME_OF_DAY}. Style: 2D cel-shaded cartoon characters with thick dark-navy
outlines inside a richly painted 2.5D storybook environment, painterly textures, warm
practical lights against cool blue ambient shadows (orange-teal contrast), soft depth of
field with a blurred foreground prop, cinematic {SHOT_SIZE}, {SIGN_CLAUSE}moderate
saturation, no watermark, main subject in the upper 60% of the frame, keep the band between
46% and 60% of the height free of important detail (caption zone), keep the right edge
clear (UI icons).
```
- `SHOT_SIZE`: wide establishing / medium / close-up / top-down overhead map view / cutaway cross-section diorama / circular magnifying-glass vignette revealing a macro detail.
- `SIGN_CLAUSE`: yalnızca soyut kavram varsa `a readable in-world sign that says "{LABEL}", `.
- Clause'un göründüğü planlarda Clause referans elementi eklenir ve `SUBJECT_ACTION` içinde "Clause the raccoon inspector peers through his brass magnifying glass at…" gibi tarif edilir.
- **Gerçekçi insan yüzü yok**: tüm insanlar aynı çizgi film grameriyle çizilir (IG AI etiketi ve yanıltma riski).

### 3c. Image-to-video hareket prompt'u
```
Keep the exact art style, outlines and character design of the start image. Camera: {ONE
MOVE}. Subtle character motion only: {MICRO_ACTION}. Gentle parallax between foreground and
background, light dust particles in the air, no scene cut, no new characters, no text
changes, no face morphing, continuous motion from the first to the last frame.
```
Hareket karşılıkları: `push_in` → "slow dolly push-in toward the {noun}", `truck` → "smooth lateral truck right revealing the {noun}", `whip` → "fast whip pan to the right in the last half second", `pull_out` → "quick pull-back from a close-up of the {noun} to a wide shot", `overhead` → "slow overhead crane down", `cutaway` → "slow push-in on the cross-section", `iris` → "slow zoom into the magnified circle".

## 4. Dosya düzeni ve montaj (`assemble.py`)
- Planlar `shots/s01.mp4 … sNN.mp4` olarak kaydedilir (numara = `lines[].n`). Klip yoksa `shots/sNN.png` (anahtar kare) kullanılır ve Ken Burns (1,00 → 1,08 zoom) uygulanır. O da yoksa yer tutucu kart çıkar (animatik modu).
- I2V klipleri baştan 0,25 sn kırpılır (başlangıçtaki donukluk), plan süresine göre kesilir, gerekirse yavaşlatılır (en az 0,8x).
- Geçişler `shot.transition` alanından: `dissolve` = xfade fade 0,2 sn, `whip` = xfade slideleft 0,15 sn + whoosh SFX, `morph` = xfade dissolve 0,35 sn.
- Altyazı katmanı en üstte ve kamera hareketinden bağımsız (ASS burn).
- Remotion alternatifi: `C:\dev\the-other-self` stüdyosunda `<WordCaptions>` (props `05` §1) ve `<Series>` + crossfade. ffmpeg yolu varsayılan, Remotion opsiyonel.
