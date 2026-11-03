# 01 — Sistemin mantığı: neden tıklandı, neden izlendi, ne değişince tuttu

Kaynak: 5 paralel analist (A paketleme, B senaryo, C görsel, D izleyici/TR pazarı, E üretim hattı), 10 kanal, 100 video (27 hit ≥100K), 11 videonun kare kare kanıt paketi, 20 transkript, 1.308 yorum, 2026-10-28. Ham raporlar `deep-research/`.

## Tek cümlelik DNA

> İzleyiciye kendi gündelik hayatında 5 saniyede hayal edebileceği, **bir sayı + bir yasakla** tanımlı, hediye gibi görünen bir **lanet** ver; kuralı ilk 15 saniyede bir sahnede kır, 30 saniyede tek cümleyle söyle; bedeli önce kahramana, sonra en yakın kişiye döndür; sayıyı kişinin kafasının üstünde göster ve her dakika bir kez değiştir; iki seçenekli bir soruyla bitir.

## Kazanma zinciri (her halka ayrı ölçüldü)

Bir videonun izlenmesi çarpımdır: **dağıtım × tıklama × izleme × tartışma**. Bir halka sıfırsa sonuç sıfır.

| Halka | Ne belirliyor | Kanıt | Referans |
|---|---|---|---|
| **1. Dağıtım** | Lansman ve momentum | Kanalın 1. videosu %60 hit; 4–8. video %19. Aynı başlık farklı kanalda 16× fark (başlık dışı pay ~%70–80). Günde >1 video hit oranını düşürüyor. | `02` §7, `06` §4 |
| **2. Tıklama — başlık** | Somutluk × çift sonuç × sosyal risk | Sosyal + somut + tabu %71 hit; DUAL %75; klasik süper güç %6 | `02` |
| **3. Tıklama — thumbnail** | İkinci soru + görsel çelişki | Çelişkili %56 hit, çelişkisiz %25; başlığı tekrar eden %22 | `03` |
| **4. İzleme — hook** | Kural ihlali ≤15 sn, kural ≤30 sn | Hit medyanı 6,5 sn / 30 sn; flop 12 / 60 | `04` §2 |
| **5. İzleme — gövde** | Tırmanma + bedel zamanlaması + süre | İlk karanlık dönüş %37,5 vs %46; flop'lar daha uzun | `04` §3–4 |
| **6. İzleme — görsel** | Güç kişiye bağlı ve görünür; ritim profil içinde | Görsel aynı kanal içinde ayırt etmiyor; ama nesne-güç, boş fon, aşırı hız flop | `05` |
| **7. Tartışma** | Kural somutluğu, ahlaki ikilem, ikili soru | Hit'te kural tartışması %30,6, flop'ta %0; Snail 2,11 yorum/1K | `06` §1 |

## "Ne değişince tuttu" — aynı kanal, aynı hafta

| Kanal | Flop | Hit | Tek değişen |
|---|---|---|---|
| ConChaser | Days People Have Left 12K | Future Wealth 482K | Valans: keder sayacı → hırs sayacı |
| ConChaser | Partners Everyone Has Had 23K | Crush on You 179K (aynı gün) | Bilgi yönü: "herkesin" → "sana" |
| Jeremy Bearimy | Psychic 24K | Level Up 104K (aynı gün) | Soyut güç → oyun dili |
| Jeremy Bearimy | Control Water 10K | Heart Beat 10x 584K | Düz güç → DUAL beden |
| Jeremy Bearimy | Every GUY 9,5K | Every Girl 191K | Kitlenin arzusu |
| Alternate You | 1 Trillion Years 43K | Googol 128K → Googolplex + Best Friend 252K | Adlandırılmış ölçek + sosyal öğe + seri |
| Hour Seven | Sank 7,8K | Immortal Snail 568K | Meme + karar + kişisel bedel (sessiz, saf senaryo kıyası) |
| Ifsphere | Breathe in Space 39K | Breathe Underwater 226K | Uzak → yakın |
| The Readout | Charged Up 17K | Brighter 158K | Soyut → hissedilir birim (flop'un sesi ayrıca Danca) |
| Miko | Tesla Fly 23K | Lie Count 460K | Güç nesnede → kişide; mucize 60 sn → 1 sn |

13 mutasyon kuralının tamamı `02` §3'te.

## Neden bu niş şimdi patladı (ve ne kadar sürer)

- 10 kanalın hepsi son 2 haftada açıldı; 40 "what if" kanalının 23'ü 2026'da. Bir şablon dolaşıma girdi.
- Doygunluk başladı: büyük bir kanal şablonu kopyalayınca 39 izlenme aldı; hit videolarda kopyala-yapıştır "AI slop" yorumları var.
- **Sonuç:** İngilizce tek başına geç kalınmış bir yarış. Türkçe'de bu aile **boş** (tam eşleşme aramalarında 0 sonuç) ama format kanıtlı (Tarih SEN 2 haftada 523K'lık video). Pencere dar; ilk 3 video en güçlü 3 premise olmalı.

## Çelişkiler ve kararlar (orkestra şefi)

| Konu | Ajanlar | Karar |
|---|---|---|
| Rubrik eşiği | A kural metni "≥7", A ölçümü ≥5 → %72 hit; hiçbir başlık 7'yi geçmiyor | **≥5 üret, 4 koşullu, ≤3 reddet**; oyun mekaniği ve yenilmezliğe K5=2 |
| Süre | A: 10–13 dk %56 hit. B: incelenen hit'lerin hiçbiri ≥11 dk; aynı kanalda flop hep daha uzun | Hedef 8–10 dk, **tavan 11 dk** (doğrulayıcı reddeder) |
| Konuşma hızı | E: 135 kelime/dk. B: hit'ler 167 (EN), TR 135–155 | 145 varsayılan; ilk TTS'te gerçek hız ölçülür, `WHATIF_WPM` ile güncellenir |
| Kurgu ritmi | E: 11–20 kesme/dk (başka nişin normu). C: hit'ler iki profil | **Profil A 18–26, profil B 8–13**; sert sınır >30/dk |
| Altyazı | E: varsayılan karaoke. C: hiçbir hit'te yok | **Varsayılan kapalı**; yalnız Shorts |
| Palet | E: açık kağıt. C: hit'ler orta-koyu | Ölçülmüş palet (smoke: luma 89, doygunluk 99) |
| Lanet dönüşü | B: ilk karanlık %30–45. D: en yakın kişiye %60–70 | İki adım: kahramana %38–48, yakına %48–70 |
| Askerlik | D: kitle konuları arasında; D korkuluk: askerlik şakası yok | Bağlam olabilir, **alay olamaz** |
| Dil | D: TR ana + EN ses parçası; B: Readout flop'u ses dili ≠ başlık dili | TR ana kanal; EN dublaj ayrı ses parçası ya da kanal, başlık/ses dili hep eşleşir |

## Bilinen sınırlar

- **CTR ve gösterim verisi yok.** "Tıklandı" çıkarımı izlenme üzerinden; aynı gün aynı kanal çiftleri dağıtımı kısmen sabitliyor.
- **Heatmap yok** (11 videonun hepsinde null). Tekrar-izleme anları yorum zaman damgalarından (düşük güven).
- **n küçük:** 100 video, 27 hit; kanal içi çiftler yönlü ama istatistik testi yok. 16 video <2 günlüktü; 48 saat sonra yeniden çekilmeli.
- **Lansman etkisi** başlık etkisinden ayrışmıyor (Jeremy'nin ilk günü 3 hit DUAL istatistiğini şişiriyor).
- **Türkçe hız, RPM ve kitle tepkisi** dolaylı (tek TR rakip + 6 kanallık kohort).
- Thumbnail etiketleri tek gözlemci.
