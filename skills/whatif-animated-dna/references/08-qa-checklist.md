# 08 — Yayın öncesi QA (her video)

Otomatik kontrollerin çoğu `pipeline.py` doğrulayıcılarında. Bu liste insan/Claude gözüyle yapılanları da toplar. Bir FAIL bile varsa yayınlama.

## K1 — Fikir ve başlık (`02`)
- [ ] Başlık rubriği ≥5 (ilk 3 video için en yüksek puanlı üç premise). `package.json → title_scores`
- [ ] ≤8 kelime, ≤55 karakter, "?" ile bitiyor *(otomatik)*
- [ ] Sosyal ailede bilgi yönü izleyiciye; "herkes seni görüyor" yok
- [ ] Ölüm sayacı, cinsel sayı, marka, ünlü yok
- [ ] Aynı aileden son 30 günde ≤2 video
- [ ] Premise'te 1 sayı + 1 yasak var

## K2 — Thumbnail (`03`)
- [ ] Metin 1–4 kelime, başlığı tekrar etmiyor *(otomatik, Türkçe uyumlu)*
- [ ] `contradiction` var ve karede görünüyor *(alan otomatik, görünürlük göz)*
- [ ] Luma 60–160, siyah ≤%35, öğe ≤4
- [ ] 320×180 önizlemede okunuyor (`thumbs/*_320.png`)
- [ ] Karakter ve atkı rengi kanal standardı
- [ ] İ/ı doğru

## K3 — Senaryo (`04` §9 rubriği, ≥8/10, 1 ve 2 zorunlu)
- [ ] Kural ihlali ≤15 sn · kural tek cümle ≤30 sn, yeniden tanımlanmıyor
- [ ] Soru 20–45 sn · karanlık vaat 25–50 sn · ilk karanlık dönüş %28–48
- [ ] ≥6 damga, ×3+ büyüme, sosyal → fiziksel → varoluşsal
- [ ] ≥2 planted-payoff · bilim blokları kullanılıyor ve kaynaklı
- [ ] İkili soru + CTA ≤10 sn; sabitlenmiş yorumla aynı soru
- [ ] Kırmızı bayrak yok (edilgen kahraman, organik olmayan kriz, kural yeniden tanımı, dil uyuşmazlığı)
- [ ] Süre ≤11 dk *(otomatik)*

## K4 — Ses
- [ ] Tüm rakamlar `spoken` alanında yazıyla
- [ ] Gerçek hız ölçüldü, `WHATIF_WPM` güncel *(tts logu)*
- [ ] VO boşlukları sürenin <%3'ü; ilk 60 sn'de ≥0,35 sn sessizlik ≤1
- [ ] −14 LUFS ±1 (`qa_render.ps1` → `rhythm_qa.py`)
- [ ] Türkçe aksan/telaffuz kulakla kontrol edildi (ilk 2 dk + rastgele 3 nokta)

## K5 — Görsel ve kurgu (`05`)
- [ ] Profil seçili; kesme/dk ve medyan plan profil aralığında *(otomatik uyarı)*; sert sınırlar *(otomatik)*
- [ ] Kahraman 0. sn'de, güç ≤10 sn içinde kişiye bağlı görünür
- [ ] Başlık kartı 25–35 sn ve ≤4 sn ya da yok
- [ ] 6–15 infografik kart, bilim kartlarında kaynak satırı *(sayı otomatik uyarı)*
- [ ] Her 60–90 sn'de bir sayı değişim anı
- [ ] Draft kareleri açıldı: etiket yüzün üstünde değil, güvenli alan, boş kare yok, Türkçe karakter doğru
- [ ] Yürüme yönü, çarpışma, sahne sürekliliği (D: animasyon hataları hit'te bile en çok beğenilen yorum)
- [ ] 1 fps karelerde luma 70–105, doygunluk 95–135
- [ ] Karaoke altyazı kapalı

## K6 — Risk ve politika (`06` §3)
- [ ] "Çocuklar için değil" elle işaretlenecek; anahtar kelimelerde "çocuk/kids" yok
- [ ] Gore, cinsel ima, intihar çağrışımı yok; din/siyaset/etnik/askerlik alayı yok; kumar yok
- [ ] Özgün karakter; başka kanalın karakteri/rengi/logosu yok
- [ ] Açıklamada "kurgudur" notu, ≥3 kaynak (bilim varsa), bölüm listesi, "Ekim 2026 fiyatlarıyla" (TL rakamı varsa)
- [ ] Ses ve görsel lisans listesi proje klasöründe
- [ ] Yapay zekâ ile üretilmiş ses notu açıklamada

## K7 — Yayın
- [ ] Günde en fazla 1 video
- [ ] Sabitlenmiş yorum sorusu hazır
- [ ] 48 saat sonra izlenme kontrolü: 2. günde <20K ise seriyi devam ettirme, aileyi değiştir; hit ise 24–72 saat içinde aynı aileden eskalasyonlu devam
