# 08 — Üretim hattı: videonun öğrettiği yol + bizim otomasyon planımız

Kaynak: `deep-research/08-taught-pipeline.md` (adım adım tablo, prompt yapı özetleri, ekonomi, riskler).
Not: referansın prompt metinleri kopyalanmadı; aşağıda sadece **yapıları** ve bizim yazdığımız özgün şablonlar var.

## 1. Videonun öğrettiği hat (Mart 2026 itibarıyla)

| # | Adım | Araç | Ne yapılıyor | Uyarılar |
|---|---|---|---|---|
| 0 | Rakip çalışması | YouTube kanal sayfası + vidIQ | "Popular" sırala; abone ÷ video sayısı; evergreen outlier bul; başlık mekaniğini sesli çöz | uzun videolar (44–52 dk) = daha çok reklam |
| 1 | Kanal adı | ChatGPT (yedek: Grok) | 30 isim / 3 kategori × 10 → YouTube'da ara, vidIQ skoru | aynı isimli kanal var mı kontrol |
| 2 | Logo | ChatGPT → Google Whisk 1:1 | 5 logo prompt'u, her biri 2–3 kez; kötüyse ihtiyacı düz dille söyle → 5 yeni prompt | kamerada 2 kez reddedildi (hata→düzeltme) |
| 3 | Konular | ChatGPT + YouTube/vidIQ | 50 fikir / 5 kategori × 10 → tek kategoriye 30 daha → az uzun videosu olan konuyu seç | seri halinde tek kategori |
| 4 | Senaryo | Claude (ücretsiz plan) | 1.800–2.200 kelime, 6 bölüm (Hook → Problem → Çekirdek açıklama → İçgörü → Pratik çıkarım → Kapanış); Doc'a kopyala, başlıkları sil | hook soruyla açılır, "merhaba" yok |
| 5 | Ses | Google AI Studio · Gemini TTS · Single-speaker · ses "Charon" | ChatGPT tek satırlık stil talimatı yazar; senaryo 2–3 parçada | uzun metin sessiz boşluk üretiyor; ücretsiz kota ~1 dk/üretim |
| 6 | Görsel prompt'ları | ChatGPT | 2 cümlede 1 prompt (sonra "1 kavram = 1 sahne") → ~30 sahne | uzun senaryo "message too long" hatası |
| 7 | Görseller | Whisk 16:9 | ilk iyi görseli **Subject** yuvasına sürükle → tüm sahneler + thumbnail aynı karakter | Whisk 30 Nisan 2026'da kapanıyor (Flow'a taşındı) |
| 8 | Temizlik/upscale | cleanup.pictures, Pixelcut | sadece açıklamada; ekranda kullanılmadı | — |
| 9 | Görsel→video | Grok Imagine "Animate Image" | **sadece ilk dakikanın** görselleri, aynı prompt'la | Grok artık ücretli + filigran |
| 10 | Edit | CapCut masaüstü | ses → elle sessizlik kesme → Grok klipleri (sessiz) → kavram başına görsel → In/Combo animasyon → otomatik altyazı → "Renoir" filtre + vinyet ayar katmanı → 1080p30 export | 2 Pro özellik kullanılmış; "çocuk da yaşlı da takip edebilsin" yavaş tempo |
| 11 | Thumbnail | ChatGPT → Whisk (subject = maskot) | fikir + 3–5 kelime + görsel prompt; yazıyı prompt'a koy | 1–2 öğe, büyük yazı için boşluk |
| 12 | SEO | ChatGPT | A/B için 5 başlık, açıklama, ~24 etiket, 15 anahtar kelime, 7 hashtag | — |

Gerçek emek: **10–15 saat / 10 dk video** (en çok beğenilen yorum), çoğu 100–120 görsel üretip yerleştirmek.

## 2. Bizim otomasyon hattımız (Claude = beyin · ElevenLabs = ses · Higgsfield/nano-banana/Flux = görsel · Remotion = montaj)

| Aşama | Otomatik? | Araç | Girdi → Çıktı |
|---|---|---|---|
| A. Kanal kitabı | bir kez, insan onaylı | Claude + insan | `bible.json` (persona, kitle, palet hex, STYLE_BLOCK, MASCOT_BLOCK, altyazı stili, yasaklı ifadeler, disclaimer) + `canon/*.png` |
| B. Rakip radarı | evet | YouTube Data API v3 (`competitor-radar` skill'i) | `radar/YYYY-MM-DD.json` (views/day, outlier = views ÷ kanal medyanı) |
| C. Konu | evet + **insan seçer** | Claude: outlier başlıklarını değişkenli şablona çevir → 30 konu → aramada son 12 ayda ≤ 5 uzun video olanları puanla | `topics.json` → `topic.json` |
| D. Senaryo | evet + **insan okur** | Claude (aşağıdaki şablon) + 2. geçiş: doğrulama/sadeleştirme/tutma denetimi | `script.md` (`||` vuruş işaretli) + `claims.json` |
| E. Ses | evet | ElevenLabs TTS *timestamps ile*, ≤ 2.500 karakter parçalar | `voice.wav` (−16 LUFS, > 0,6 sn boşluklar 0,35 sn'ye) + `words.json` |
| F. Sahne planı | evet | Claude: `script.md` + `words.json` → sahne listesi (hedef 5–7 sn, min 2,5, maks 10) | `scenes.json` |
| G. Görseller | evet + **insan 1-tık QA** | Higgsfield `generate_image_batch` (nano_banana_pro / flux) + 2–3 canon referans | `img/scene_###.png` + `qa.json` |
| H. Upscale/temizlik | gerekirse | Higgsfield `upscale_image`, arka plan silme | — |
| I. Görsel→video | evet | Higgsfield `generate_video`, 4–6 sn, sadece ilk 30–60 sn + dakikada ≤ 1 vurgu | `clip/scene_###.mp4` |
| J. Montaj | evet | **Remotion** (`scenes.json` + `words.json`) | `render/final.mp4` 1920×1080, 30 fps, H.264 CRF 18–20, AAC 320k |
| K. Altyazı dosyası | evet | `words.json` → SRT | `captions.srt` (CC olarak da yükle) |
| L. Thumbnail | evet + **insan 3'ten seçer** | Claude konsept → görsel model (maskot ref, **yazısız**) → yazı programatik (Sharp/Satori) | `thumb_A/B/C.png` |
| M. SEO | evet | Claude | `seo.json` (5 başlık, bölümlü açıklama, ≤ 500 karakter etiket, 3–5 hashtag, sabit yorum) |
| N. QA | evet | `scripts/edit_rhythm_qa.py` | PASS/FAIL |
| O. Yükleme | evet (önce private) | YouTube Data API `videos.insert`, `thumbnails.set`, `captions.insert` | video id |

İnsan kontrol noktaları: konu (2 dk) · senaryo (10–15 dk) · görsel QA ızgarası (10–15 dk) · 1,5× final izleme (10 dk) · thumbnail (2 dk).

## 3. Senaryo prompt şablonu (Mod F ürün videosu; özgün)
```text
ROLE
You write narration for <CHANNEL>, a faceless 2D-animated <NICHE> channel.
Narrator persona: <PERSONA>. Mascot on screen: <MASCOT NAME> (the viewer's stand-in).

GOAL
A <TARGET_MINUTES>-minute script (= TARGET_MINUTES × 155 words, ±5%) on: <TOPIC>
Core promise in one line: <PROMISE>. Audience: 18–40 beginners, many ESL. Grade-7 reading level.

HOOK (first 45–60 words, ≤ 20 s)
- Open with a second-person question or a micro-scene the viewer has lived. No greeting, no channel name.
- State the stake with ONE concrete number in the first 15 seconds.
- End the hook with an open loop that closes only in the final third.

BODY
- 4–6 concept blocks, 150–300 words each: one idea, one everyday example, one number, one "so what".
- Every 60–90 s a re-hook line (question, reversal, or "the part nobody mentions").
- Mark every statistic [SRC?]. Sentences ≤ 18 words; numbers written as spoken.

ENDING (last 120–180 words)
- Close the opening loop, give 3 practical steps, end on a reflective one-liner. One soft CTA max.

FORMAT
- Plain narration only. Put "||" wherever the visual concept changes (one every 12–18 words).
- After the script: word count, minutes at 155 wpm, the open loop + where it closes, list of [SRC?] claims.

DON'TS
- Never imitate any existing channel's wording, catchphrases, segments or characters. Never name another channel.
- No personalised financial advice, no tickers to buy, no guarantees.
```
Referans prompt'unun eksikleri (bu şablon düzeltir): süre matematiği yok (1.850 kelime ≈ 11–12 dk, "8–10 dk" değil), açık döngü yok,
doğrulama yok, TTS için cümle sınırı yok, editöre vuruş işareti yok, rakip adı geçiyor (taklide çeker).

## 4. Ekonomi (yaklaşık, bütçelemeden önce fiyatları yeniden kontrol et)

| Kalem | Tutorial yolu | Bizim otomasyon |
|---|---|---|
| Senaryo + doğrulama | $0, 15–30 dk | Claude API ~$0,2–1 · 10–15 dk insan |
| Ses | $0 (kota + sessiz boşluk riski) | ElevenLabs ~$2–3 |
| Görseller (85–120 görsel / 10 dk; reddetmeyle 110–160 üretim) | $0, 2–6 saat | ~$3–8 · 15 dk insan seçimi |
| Görsel→video (6–10 klip) | $0 (artık ücretli) | ~$2–5 |
| Montaj | 2–4 saat CapCut | Remotion 10–25 dk makine · 15–30 dk inceleme |
| Thumbnail + SEO | 30–60 dk | ~$0,5 · 10 dk |
| **Toplam** | **$0 nakit, 10–15 saat** | **~$8–18 nakit, ~1–1,5 saat insan** |

Bütçe kapısı: 10 dk video başına ≤ $20 nakit ve ≤ 90 dk insan zamanı; bir aşama bütçesinin 2 katını aşarsa dur ve logla.
Poz kütüphanesiyle kompozit + %10–20 planlı tekrar kullanım → 60–90 benzersiz üretim.

## 5. Riskler ve farklılaşma (zorunlu)
1. **YouTube "inauthentic content" (eski adıyla repetitious content, Temmuz 2025):** şablon-aynı seri üretim tüm kanalı demonetize edebilir.
   → formatı değiştir (hikâye / mit yıkma / liste / vaka), aynı açılış cümlesini asla tekrarlama, her senaryoda insan düzenlemesi.
2. **Reused content:** rakip görüntüsü kullanma, rakip senaryosunu yeniden seslendirme.
3. **Karakter IP:** referans kanalın maskotu tanınmış bir TV çizgi film karakterine benziyor → bizde her zaman **özgün maskot**; prompt'a asla "similar to {kanal/karakter}" yazma.
4. **Benzerlik / taklit:** gerçek kişi yüzü/sesi formatları (milyarder fotoğrafı, ses benzeri) yok.
5. **Finans uyumu:** "not financial advice"; hisse önerisi ve garanti yok; her istatistik doğrulanır (BLS, Fed SCF, Census gibi birincil kaynaklar).
6. **Araç kırılganlığı:** Whisk kapandı, Grok ücretli oldu, ücretsiz TTS kotası, CapCut Pro altyazı kilidi → her aşamada yedek araç tanımlı olsun.
7. **Farklılaşma asgarisi:** özgün maskot + tekrar eden yan karakter/gag · gerçek veriyle programatik grafik (kaynak etiketli) · kendi tasarladığımız ses ·
   format imzası (ör. "maliyet sayacı" overlay'i, kapanışta "3 adımlı çözüm" kartı) · 12–25 dk arası değişken süre.
