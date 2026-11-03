# 06 — Instagram yayın, büyüme ve YouTube geçişi

Kaynak `deep-research/F` (kaynak URL'leri orada). Etiketler: [RESMİ] Meta/Mosseri, [3P] üçüncü taraf, [TAHMİN] çıkarım.

## 1. Algoritma: neyi optimize ediyoruz
- **3 ana sinyal [RESMİ]:** izlenme süresi, erişim başına beğeni, **erişim başına DM gönderimi (sends/reach)**. Takipçi olmayanlara dağıtımda sends ağırlıkta. Bu yüzden her senaryoda bir send cihazı var.
- **Skip rate [RESMİ metrik]:** 3 sn içinde kaydırma oranı. 100K–1M hesap ortalaması %60,5 [3P]. Hedef <%50, viral adaylarda <%40.
- **Orijinallik [RESMİ]:** Yeniden yüklenen ya da filigranlı içerik öneriden düşer. Tek master yüklenir, her platforma temiz dosya gider.
- **Uzunluk:** 3 dk'ya kadar öneriliyor. Pratik bant 45–60 sn, en fazla 75 sn.

## 2. Hesap kurulumu (Gün 0; kullanıcı yapar, ajan hesap açmaz)
- Creator hesap, kategori "Education". İsim alanı: `Backdoor Bureau | Loopholes & Hidden Rules`.
- Avatar Clause'un yüzü. Bio `00-brand.md`'den. 2FA açık.
- Highlights: Start Here · Small Print · Beat the House · Built Like That · Court.
- Lansmanda ilk 48 saatte **3–6 Reel**, profil boş görünmesin diye.

## 3. Her Reel'in paketi (`package.json`, `validate.py` denetler)
| Alan | Kural |
|---|---|
| `cover_text` | 2–4 kelime, BÜYÜK HARF, orta 1080×1440 (3:4) bantta. Arka plan **"imkânsız an" karesi** (0,5–2,5 sn arası), kare 0 değil. Köşede seri rozeti + `CASE #NNN`. |
| `cover_frame_sec` | İmkânsız anın saniyesi |
| `caption_first_line` | ≤80 karakter, premise'in yeniden yazımı + gap. Videodaki cümlenin kopyası değil. |
| `caption_body` | 2–3 cümle bağlam + aranabilir anahtar kelimeler. Kaynak notu: "Sources in pinned comment". |
| `comment_question` | Taraf tutturan, bedelli soru |
| `hashtags` | **3–5** adet (Aralık 2025'ten beri üst sınır 5) [RESMİ] |
| `pinned_comment` | Kaynak linkleri + "why didn't he just…" cevabı + sonraki dava teaser'ı |
| `series_link` | Aynı seriden önceki Reel (IG "series" bağlantısı) [RESMİ özellik] |
| `trial_variants` | Aynı videonun 1–2 alternatif ilk cümlesi ya da hook bandı varyantı (Trial Reels için) |
| `yt_title` / `yt_description` | YouTube Shorts sürümü (aynı master) |
| `post_time_utc` | Önerilen: ABD Doğu 11:00–14:00 veya 18:00–21:00 (TR 18:00–21:00) |

**Caption şablonu:**
```
{caption_first_line}

{caption_body}

{comment_question}

Case #{case_no} · {series} · Sources in the pinned comment.
{hashtags}
```

## 4. Yayın ritmi ve 90 günlük plan
| Faz | Hacim | KPI (Reel başına, 72 sa) | Kümülatif hedef |
|---|---|---|---|
| **1 · Hafta 1–2 · Kalibrasyon** | 7 Reel/hafta. 5 serinin her birinden ≥2. | skip <%55, ort. izlenme ≥%45, sends/reach ≥%0,5, likes/reach ≥%3, follows/1K ≥2 | 1–5K takipçi, ≥1 Reel 50K+ |
| **2 · Hafta 3–6 · Kazananı katla** | 7 Reel + 3–5 Trial/hafta. En iyi 2 seriye %60, 3.'ye %25, deneye %15. Numaralı seriler + IG seri linki. | skip <%45, izlenme ≥%55, sends ≥%1, follows/1K ≥4, profil ziyareti→takip ≥%15 | 10–30K, ≥1 Reel 500K+ |
| **3 · Hafta 7–12 · Ölçek** | 7–10 Reel + 5 Trial/hafta. Collab (5K+ sonrası), yorum-kelime DM (10K+ sonrası). | skip <%40, izlenme ≥%60, sends ≥%1,5, follows/1K ≥5 | **100K** (min. kabul 50K), ayda ≥2 adet 1M+ |

**Gerçeklik kontrolü [TAHMİN]:** 100K takipçi ≈ 15–40M toplam erişim ≈ 3–6 adet 1M+ "pop". 90 gün iddialı bir hedef; kötü senaryoda 5–15K, bu durumda fikir ve hook stratejisini değiştir.

**Trial Reels:** Takipçi olmayanlara gösterilir, gride düşmez. Erişim ve hook testi içindir, takipçi getirmez (1,4M izlenme → 130 takipçi [3P]). Kullanım: aynı hikâyenin 2–3 ilk cümle varyantını test et, kazananı normal Reel olarak yayınla. Birebir aynı videoyu iki kez yayınlama.

## 5. Bir Reel patladığında (24–72 saat protokolü)
1. **0–6 sa:** 2 saatte normal ortalamanın 3 katı izlenme ya da sends/reach >%2 → pop adayı.
2. **≤24 sa:** Yorumlara yanıt ver, sabitlenmiş yoruma teaser koy, Reel'i profilde sabitle, Story paylaş.
3. **24–48 sa:** Part 2 (aynı mekanizmanın bir sonraki katmanı) yayınla ve seri olarak bağla. 2 kardeş konuyu Trial'da test et.
4. **48–72 sa:** Kazanan kardeşi normal Reel yap, 5–10 bölümlük mini seri planla. Kazanan Reel'in özelliklerini (hook, ilk 3 sn, uzunluk, konu) `playbook.md`'ye yaz.
5. **Yapma:** Aynı videoyu tekrar yükleme; pop'un hemen ardından alakasız bir deney paylaşma.

## 5b. "İzleniyor ama takip edilmiyor" (kullanıcı sorunu, 2026-10-31)
- Her videonun son satırı bir **bitiş kartı**: `"Yarın: [somut sonraki konu]. Kaçırmamak için Ayrıntı'yı takip et."` Ekranda da sonraki dosyanın klasörü ve takip butonu görünür. `script.json` içinde `"end_card": true` olarak işaretlenir; validate.py bu satırı twist konumu hesabına katmaz.
- Vaat edilen video ertesi gün aynı saatte yayınlanır ve Instagram "Seri" ile bağlanır.
- Profil: bio'da saat vaadi ("Her gün 19:00"), 3 sabit Reel (en çok izlenen, en çok takip getiren, serinin ilki), tek tip kapak rozeti.
- Yorumlar: ilk 1–2 saatte hepsi cevaplanır, en iyi soruya "video ile yanıtla" Reel'i çekilir, sabit yorumun son satırı sonraki dosyadır.
- 2–3 sabit seri tutulur; her gün farklı bir dünyaya atlanmaz.
- Örnek paket: `C:\dev\viral-reels-tr\paket-008-009-010.txt`

## 6. Ölçüm kaydı
Her Reel için 72. saatte `metrics.csv`'ye şunları gir: tarih, case_no, seri, hook tipi, süre, izlenme, erişim, skip rate, ort. izlenme %, beğeni, yorum, send, kaydetme, takip. `scripts/kpi_report.py` faz hedeflerine göre rapor ve öneri üretir.

## 7. YouTube geçişi
- **Önerilen:** Kanalı şimdi aç ve aynı master'ları IG'den 0–24 sa sonra Shorts'a yükle (ek üretim yok). Kendi orijinal videonu iki platforma koymak "reused content" ihlali değildir [RESMİ].
- **Kullanıcının planına göre bekleniyorsa** tetikleyici şunlardan hangisi önce gelirse: IG 100K, ya da IG ≥50K + son 30 günde ≥3 adet 1M+ Reel, ya da 90. gün.
- **Repurpose:** Arşivi günde 2–3 Short olarak yükle, aramaya dönük başlık kullan. En iyi seriyi 6–10 dk'lık uzun videoya birleştir ("Every Airline Loophole Explained"); her derlemede yeni bağlayıcı VO olsun.
- YouTube yükleme ve IG yayını **kullanıcı onayıyla** yapılır. Ajan başlığı, kapağı ve zamanı gösterip onay ister.

## 8. Riskler
- **Kumar:** Eğitici "kasa neden kazanır" açısı. Bahis sponsoru alınmaz.
- **AI etiketi:** Fotogerçekçi AI insan yok; çizgi film karakteri profil etiketini gerektirmez [TAHMİN]. Gönderiye "AI info" etiketi düşerse sorun değil.
- **Müzik:** Kendi üretimimiz ya da telifsiz lisanslı. Hesap türü Creator.
- **Hesap ısıtma bir mit** [RESMİ]. Bot, takip-takip ve engagement pod'u kısıtlama tetikler.
- **Yanlış bilgi etiketi:** `03` §6 kuralı ve sabitlenmiş yorumda kaynaklar.

## 9. Türkçe hesap
EN hesap 10–20K'ya ulaşınca (hafta 4–6) ayrı hesapta aynı animasyon, Türkçe VO ve Türkçe altyazıyla. Aynı hesapta dil karıştırılmaz.
