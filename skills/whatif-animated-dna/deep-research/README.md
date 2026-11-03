# deep-research — 5 analist ajanın ham raporları

Tarih: 2026-10-28. Yöntem: 1 orkestra şefi + 5 paralel analist; ortak brief `BRIEF.md`; ortak veri `dataset.csv` (10 kanal, 100 video, hit = ≥100K izlenme) + 11 videonun kanıt paketi (video, 1 fps ve ilk 60 sn 4 fps kontak sayfaları, scdet kesmeleri, sessizlik, loudness, 400 yorum) + 100 thumbnail + 20 transkript. Kanıt paketleri ve ara dosyalar oturum scratchpad'indeydi (`whatif/ev`, `thumbs`, `transcripts`, `A`, `C_work`, `d_agent`, `remotion-smoke`) ve kalıcı değil.

`../references/` bu raporların Türkçe, birleştirilmiş ve çelişkileri çözülmüş halidir. Üretimde önce `references/`'ı kullan; ham rapora yalnız ayrıntı gerekirse in.

| Dosya | Ajan | İçerik |
|---|---|---|
| `A-packaging-ctr.md` | A — Paketleme/CTR | Başlık grameri (aile, somutluk, polarite, sosyal yön, tabu), 26 aynı-gün kanal içi A/B, 100 thumbnail PIL + gözle etiket, 13 mutasyon kuralı, 0–10 rubrik (geriye dönük doğrulandı), 20 şablon EN+TR, 3 layout + 10 QA kapısı, lansman/kadans gözlemleri |
| `A-title-stats.csv`, `A-thumb-stats.csv` | A | 100 video × 46 sütun etiket + PIL metrikleri |
| `B-hook-script-engine.md` | B — Hook + senaryo | 20 video (10 hit / 10 flop) ölçüm tablosu, hit vs flop medyanları, kanal çiftlerinde senaryo mu paketleme mi, hook saniye bütçesi, 10 vuruşluk şablon, merdiven, 50 vuruş bankası, dil + TTS kuralları, bitiş tipleri, QA rubriği, tam Türkçe örnek senaryo |
| `B-transcript-notes/<id>.md` | B | 20 video notu (ilk 30 sn dökümü + yapı tablosu) |
| `C-visual-animation-rhythm.md` | C — Görsel/ritim | 11 video nicel tablo (kesme/dk, plan, LUFS, duraklama, luma/doygunluk), 7 kanal görsel kimliği, 12 güç tekniği, iki ritim profili, Remotion/SVG yeniden kurma spec'i, E iskeleti eksik listesi, maliyet |
| `C-video-notes/<id>.md` | C | 11 video notu |
| `D-audience-tr-market.md` | D — İzleyici + TR pazarı | 1.308 yorum kategorisi, etkileşim oranları, mekanizma → kural, risk/korkuluk, NexLev RPM, TR rakip taraması, go/no-go, 40 Türkçe premise puanlı |
| `E-pipeline.md` | E — Üretim hattı | Mevcut altyapı keşfi, aşama tablosu, 10 tasarım kararı, smoke test, hata modları, ilk video adım listesi |
| `dataset.csv` | Şef | 100 video ham veri |
| `BRIEF.md` | Şef | Ajanlara verilen ortak brief |

**Çelişkide öncelik:** nicel ölçüm (C kesme/luma, B zaman damgaları, A aynı-gün çiftleri) > kare kanıtı > yorum/çıkarım. Şefin kararları `../references/01-why-it-won.md` "Çelişkiler ve kararlar" tablosunda.

**Şefin doğruladıkları:** aile hit oranları (A ile bağımsız sınıflandırma, uyumlu); shot doğrulayıcısı Tesla tipi aşırı hızlı kurguyu reddediyor; paket doğrulayıcısı Türkçe büyük harfli tekrar metni yakalıyor (ilk sürümdeki `lower()` hatası düzeltildi); `SceneInfoCard` + yeni palet tsc temiz ve render edildi (sokak karesi luma 89 / doygunluk 99, hedef aralıkta).

**Bilinen sınırlar:** CTR/gösterim yok; heatmap 11 videonun hepsinde null; n küçük; 16 video <2 günlük; lansman etkisi ayrışmıyor; TR verisi dolaylı; thumbnail etiketleri tek gözlemci; gerçek ElevenLabs çağrısı, stüdyoya entegrasyon, 10 dk final render ve upload test edilmedi.

Telif: raporlar transkript kopyalamaz (alıntı <15 kelime); rakip karakterleri yalnız tarif edildi; tüm kurallar özgün karakter ister.
