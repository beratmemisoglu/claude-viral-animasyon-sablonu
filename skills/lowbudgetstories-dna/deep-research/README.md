# deep-research — 5 analistin ham raporları (gerektiğinde oku)

Referans: @LowBudgetStories (Low Budget Stories), en çok izlenen 10 video (2,46M–6,39M).
2026-10-23'te 5 paralel analist ajan tarafından tek bir kanıt paketinden üretildi: 10 videonun 1080p dosyası, 1 fps kareler (her saniye damgalı 3×3 kontak sayfaları, toplam 386 sayfa), ilk 60 sn 4 fps (4×4, video başına 15 sayfa, toplam 150), tüm karelerin scdet skoru, ses analizi (LUFS/mid-side/geçici ses), faster-whisper transkript (kelime zamanlı), heatmap, 4.000 üst yorum, kanalın 148 videosunun meta verisi (+14 ekstra thumbnail).
Raporlar İngilizcedir; `../references/` bunların Türkçe, birleştirilmiş ve çelişkileri çözülmüş halidir.

Her ajan: **kendi 2 videosunu saniye saniye** (v** dosyaları) + **10 videoluk bir mercek raporu** (L**).

| Dosya | Ajan | İçerik |
|---|---|---|
| v01-origin-of-a-doomer.md | 1 | #1 (6,39M), sözsüz saga: kayıp merdiveni, beat-kilitli piyano, ihanet ifşası %84 |
| v03-life-of-a-fast-food-employee.md | 1 | iş serisi modeli: sözsüz soğuk açılış, başlık kartı 21 sn, dört müşteri, ayağa kalkış %82, viral tweet bitişi |
| L1-packaging-ctr-series.md | 1 | 148 video dağılımı, yıl etkisi, 22 başlık şablonu, thumbnail piksel ölçümü + spec, açıklama/SEO, seri zincirleri, dağıtım nedenleri |
| v02-from-doomer-to-bloomer.md | 2 | iç ses mentoru, istasyon yapısı, %84 ayna dönüşümü, %90 kimlik ifşası |
| v06-life-of-a-retail-employee.md | 2 | 8 engelli arzu merdiveni, 6 kurulum→ödeme çifti, Karen 52 sn sarkması |
| L2-script-story-engine.md | 2 | **senaryo motoru:** 10 senaryo kıyası, 12 değişmez, aile şablonları, merdiven/karşıtlık/callback/gizleme, gag süreleri, pantomim, diyalog, **sözsüz senaryo yöntemi**, 70'lik vuruş bankası, konu testi, anti-kalıplar, yazar analizi |
| v04-doomers-path-to-happiness.md | 3 | sözsüz montaj saga, 57 kesmenin 52'si 97,6 BPM beat'inde |
| v05-gyms-in-2050.md | 3 | distopya, TTS makine sesleri, 37 reframe swish, donuk 18 sn tutuş zayıflığı |
| L3-visual-production-recipe.md | 3 | **görsel makine:** kare farkı ölçümleri, karakter anatomisi (hex), kompozit kuralları, hareket, arka plan türleri, pipeline/maliyet, **yeniden kurma spec'i** (özgün cast brief, katman yığını, grade, preset'ler, Remotion) |
| v07-living-in-a-social-credit-system.md | 4 | sayaç merdiveni, gizli kayıt dönüşü %86, 97,7 sn araba diyaloğu çukuru |
| v08-life-of-a-food-delivery-driver.md | 4 | kompakt iş modeli, 50 fps, kukla ustası merdiveni, 5 sn siyah perde arası |
| L4-audio-edit-rhythm.md | 4 | **nicel ritim + ses:** kalibre sınır modeli (+%17), plan dağılımı, ducking testi, SFX envanteri, TTS kanıtı, bitiş kartı sesi, **ritim spec'i + ses spec'i**, QA script'i test sonuçları |
| v09-living-in-a-metaverse.md | 5 | iki-dünya fabl, sürekli caz yatağı, iki "illüzyon kırılması" |
| v10-gaming-addiction-cycle.md | 5 | 5 sessiz faz kartı + döngü kartı, sahte tepe %62–66, sessiz bildirim gut-punch %77 |
| L5-audience-retention-psychology.md | 5 | **izleyici psikolojisi:** yorum madenciliği, tekrar-izleme türleri, duygu yayları, evren stratejisi, **risk/etik/IP**, tutma rehberi, duygusal QA |

**Çelişkide öncelik:**
1. `L4` (nicel ölçüm, kalibre sınırlar) ve orkestra şefinin doğrulamaları (`../references/10-reverse-engineering-method.md` §4)
2. kare-kanıtlı per-video teardown'lar (`v**`) ve `L3`
3. yorum/çıkarım ağırlıklı `L1`, `L2` (yazar analizi), `L5`

**Orkestra şefinin ham veriyle doğruladıkları:** kanal medyanı 518.729 / ortalama 871.133 / top-10 payı %30,0 (148 video) · yıl medyanları (2023 = 1.596.313; 2026 = 282.525) · ısı haritası zirveleri (v01 186 sn ≈%84; v10 324 sn ≈%77) · `rhythm_qa.py` v08 çıktısı (66 sınır, 19,3/dk) analist raporlarıyla birebir.

**Bilinen sınırlar:** CTR/gösterim/trafik kaynağı verisi yok (paketleme neden-analizi çıkarım) · heatmap = tekrar-izleme yoğunluğu, tutma eğrisi değil · yorumlarda yanıt zincirleri yakalanmadı · ses kayıtları dinlenmedi (müzik/SFX spektral karakter+yerleşimden) · n=10 korelasyonlar (bitiş tonu, kesme hızı) yıl/aile/konuyla karışık · arka plan yüzdeleri 8 atanmamış videoda 72'şer örnek saniyeye dayanıyor.

Telif notu: raporlar transkripti kopyalamaz; kısa alıntılar (<15 kelime) yalnız kalıbın kendisi kelime olduğunda kullanıldı. Tanınmış meme karakterleri yalnız tarif edildi; tüm kurallar özgün karakter ister.
