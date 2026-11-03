# deep-research — 8 analistin ham raporları (gerektiğinde oku)

Referans: AI Flow — "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)" (SRjm9tvMHhs, 22:52, 144.518 izlenme).
Ekim 2026'da 8 paralel analist ajanı tarafından tek bir kanıt paketinden (1 fps 1.371 kare, ilk 60 sn 4 fps, 41.103 karenin
tamamında scdet skoru, 10 fps sınıflandırma, Whisper transkript + çeviri, heatmap, 133 yorum, kanalın 108 videosu) üretildi.
Raporlar İngilizcedir; `../references/` bunların Türkçe, birleştirilmiş ve çelişkileri çözülmüş halidir.

**Çelişkide öncelik:**
1. `04-edit-rhythm-metrics.md` (nicel ölçüm) ve orkestra şefinin doğrulamaları (`../references/10-reverse-engineering-method.md` §4)
2. kare raporları `02`, `05`, `06`, `07`
3. yorum/çıkarım içeren raporlar `01`, `03`, `08`

| Dosya | İçerik |
|---|---|
| 01-packaging-ctr.md | başlık anatomisi + 25 şablon, thumbnail piksel ölçümü + yeniden kurma spec'i, açıklama/etiket şablonu, yorum analizi, heatmap okuması, kanal formül benchmark'ı, collab etkisi |
| 02-hook-intro.md | 0:00–3:12 saniye saniye hook tablosu, hook anatomisi, yeniden kullanılabilir hook şablonu |
| 03-script-storytelling.md | makro/mikro yapı, 118 tutma cihazı envanteri, WPM/duraklama/nefes analizi, kod karışımı, satır bankası, Türkçe adaptasyon |
| 04-edit-rhythm-metrics.md | 582 görsel değişim olayı, bölüm/dakika tabloları, 14 zoom'un ölçümü, ek kadansı, ses ritmi (sting'ler), retention korelasyonu, hedef tempo tablosu, QA script'i |
| 05-frames-0312-0925.md | çekim günlüğü, vurgu sistemi (seçim, tıklama halkası), Doc başlığı = bölüm kartı, vinyet, tipografi/renk hex |
| 06-frames-0925-1555.md | 1:1 gövde, prompt okunurluk süreleri, AI çıktı açılış yöntemleri, abone kartı faz tablosu, heatmap zirvelerinin açıklaması |
| 07-frames-1555-2252.md | CapCut gösterimi, zaman sıkıştırma (~10:1), kapanış; bitmiş finans videosunun çekim listesi, Ken Burns ölçümü, vinyet hex'leri, altyazı spec'i, tüm CapCut ayarları |
| 08-taught-pipeline.md | öğretilen araç hattı, prompt yapı özetleri, geliştirilmiş senaryo prompt'u, özgün maskot brifi, ekonomi, riskler, otomasyon planı, scenes.json şeması |

Bilinen ve çözülmüş çelişkiler: sonuç anı sesi (sting vs bass hit vs müzik → yüksek, bas ağırlıklı müzik vuruşu; 18:07'de doğrulandı),
gövdede zoom (yok; tek parametre zoomu), tıklama halkası rengi, statik süre limiti (kademeli), PDF kapısı (link yüklemede canlı),
rakip klibi (kendi ürünümüz). Ayrıntı: `../references/10-reverse-engineering-method.md` §4.

Telif notu: raporlar transkripti kopyalamaz; kısa alıntılar (< 15 kelime) sadece kalıbın kendisi kelime olduğunda kullanıldı.
Tanınmış karakterlere benzeyen örnekler sadece tarif edildi; tüm kurallar özgün maskot ister.
