# C — Görsel stil, animasyon ve kurgu ritmi (Analist C, 2026-10-29)

**Veri:** Ricks Clips'ten 26 klasör var. Bunların 22'si yeni dönem ("core", 7–29 Ekim 2026), 4'ü eski komik klip. Ayrıca 15 rakip video incelendi.
**Ölçüm:** Kendi script'lerimi yazdım: `analysis/scripts/c_measure.py`, `c_transition_types.py`, `c_accent_palette.py`, `c_literal_sample.py`, `c_summarize.py`. Ham çıktılar `analysis/scripts/out/c_measure.json`, `c_transitions.json`, `c_summary.txt` ve `c_literal_*.png` dosyalarında.

- Videolar 10 fps'te 90×160'a indirildi. Altyazı bandı (yüksekliğin %52–80'i) maskelendi, çünkü kelime altyazısı her 0,3 sn'de değişip ölçümü bozuyor.
- **Geçiş** = büyük kare farkı + renk histogramı değişimi. 0,4 sn içindeki çoklu kareler tek geçiş sayıldı.
- **Görsel değişim** = 16×28'lik küçük resim, son "çapa" kareden ortalama 28 gri seviyeden fazla uzaklaştığında (kaba eşik: 40). Kamera hareketiyle oluşan yeni kompozisyonları da sayar.
- **Kamera sınıfı** 0,5 sn adımlarla belirlendi: faz korelasyonu ile pan, ölçek araması ile zoom.
- **Geçiş tipi** 30 fps'te ±0,4 sn pencereyle belirlendi: tek karede sert kesme, karışım kalıntısı düşükse dissolve, ikisi de değilse whip/morph.

Kontak sayfaları: VS1Z_Q-Klt8, 0m6G8pDtzNs, eQR3pgMiUF0, PL-Yro2meY4 ve GM9UKnZ6JFw'nin bütün sayfalarına baktım. Ek olarak CJwgTrfrHL0, _sUAXTvJquk, t3OXkhlI6NQ, lnYLIWP2l-I ve nzbkkEZFM8g'den birer sayfa (toplam 10 Ricks videosu). Her rakip kanaldan 1 sayfa baktım: Circle Toon S0sf, Low Poly Rzu4, Why Side rv6q, george mSJC, Loaded Dice B5fQ. Tam çözünürlükte kafa kırpmaları da inceledim.

> **cuts.txt uyarısı doğrulandı.** VS1Z için cuts.txt 4 kesme diyor. Benim dedektörüm 17 gerçek geçiş buldu; elle kontrol edildi (`out/c_cutcheck.png`). Ricks'te neredeyse hiç sert kesme yok. Geçişlerin hepsi 0,1–0,3 sn'lik dissolve ya da hızlı kamera/morph. Bu yüzden scene>0.15 eşiği onları kaçırıyor.

---

## 1. Karakter tasarımı

### 1a. Ricks Clips karakter spesifikasyonu (gözlem)

| Öğe | Ölçüm / gözlem |
|---|---|
| Kafa | Yatay oval, genişlik:yükseklik ≈ 1,1–1,2:1. Kafa toplam boyun ≈ %30–35'i, figür ≈ 3 kafa boyunda. Close-up'ta kafa kadrajın %40–60'ını kaplıyor. |
| Kafa rengi | Kırık beyaz / krem (#F1E9D9, #EADABF). Bazı figürlerde ten tonu ya da sarımsı ten var (0m6'daki "guy", eQR3'teki işçi). Saç, kafa üstüne oturan tek parça "kask" şeklinde (kahve, siyah, kızıl). |
| Kontur | Kalın, sabit kalınlıkta, koyu kahve-siyah (#1E1612 civarı). 720 px genişlikte ≈ 5–7 px. Arka plan ile karakter arasındaki bütün okunabilirlik bu konturdan geliyor. |
| Gözler | İki küçük siyah oval/badem göz ve üstte kalın kaş çizgisi. İfade %80 kaş açısıyla veriliyor. Şok anında gözler büyük beyaz daire + nokta göbek oluyor (VS1Z 4 sn, PL-Y hook 2,75 sn). Mutlulukta "^ ^" kapalı göz. |
| Ağız | Küçük çizgi ya da küçük siyah oval. Gülerken dişli "ızgara" (0m6 patron). Bıyık rol göstergesi (imparator, şerif). |
| Gövde | Kapsül/fasulye gövde, tek düz renk + yumuşak gradyan gölge. Kol yok gibi; giysi gövdenin kendisi. |
| Uzuvlar | İnce koyu çizgi kollar ve bacaklar. Uçta küçük koyu top el, parmak yok. Bacaklar çoğu sahnede tek çizgi ya da gövdenin altında gizli. |
| Rol = şapka + gövde rengi | İmparator: siyah-altın taç-şapka, lacivert-kırmızı cübbe. Muhafız: zincir zırh + miğfer. Polis: lacivert kep + yıldız. Hırsız: kar maskesi. Korsan: üç köşeli şapka. Patron: gri saç + kırmızı kravat. Uyuyan: çizgili gece şapkası. Rol 0,5 sn'de, siluetten okunuyor. |
| Video başına karakter | 1 protagonist (ekranda ≈ %50–70) + 2–5 yan karakter. VS1Z: mucit, imparator, 2 muhafız, saray. 0m6: kahraman, patron, 3 iş arkadaşı. PL-Y: "sen" + Edison. GM9U: gömülen adam, kasaba halkı, doktor, eş. |
| İfade değişimi | Kelime düzeyinde. Yüz animasyonu yerine ardışık ifade "pozları" kullanılıyor: nötr → kaş kalkık → şok gözler → sırıtma. Değişim hemen hep kamera itmesi (push-in) ile birlikte geliyor. Ağız neredeyse hiç lip-sync yapmıyor. |
| Animasyon | Sınırlı: hafif nefes/salınım, kol jesti, göz kırpma. Asıl "hareket" kamerada (bölüm 3). Bunlar AI image-to-video'nun karaktere verdiği tipik mikro hareketler. |
| Nesnelere yüz | Hap karakteri (_sUA), barut çuvalı (lnYL). Soyut kavramları karaktere çeviriyor. |

**Hukuki not:** Bu figür; beyaz yuvarlak kafa, kapsül gövde, çizgi uzuv ve top el ile Cyanide & Happiness çizgisine çok yakın. Ricks'in eski dönem açıklamasında "I only do the voice. Artist: bradtjonas" yazıyor, yani eski klipler başkasının çizimi. Bu figürü birebir kopyalamak hem marka/telif riski hem de "kopya kanal" algısı yaratır. Bize gereken, figürün **okunabilirlik mekanizması**: tek renk büyük boş kafa, kalın kontur, rol = şapka + gövde rengi, ifade = kaş.

### 1b. Özgün karakterimiz: **"MOX"** (çalışma adı)

| Öğe | Spesifikasyon (Ricks / C&H'den farkı) |
|---|---|
| Siluet | **Yuvarlatılmış kare "çakıl taşı" kafa** (köşe yarıçapı ≈ %35, oran 1:1). Kafa toplam boyun %45'i, figür 2,2 kafa boyunda. Daha chibi ve tıknaz; çöp adam değil. |
| Kafa rengi | **Kayısı #F4C59A**, beyaz değil. Ricks'in krem kafası ve sıcak arka planlarıyla karışmaz; hem gece mavisi hem altın ışıkta ayrışır. |
| Kontur | **Koyu lacivert #1E2340**, ≈ 6 px @1080w. Siyah-kahve yerine lacivert, imza farkı olur. |
| Gözler | İki **dikey beyaz hap göz** ve lacivert yuvarlak gözbebeği. Kaş yok; ifade göz kapağı kesimiyle ve gözbebeği yönüyle veriliyor. C&H'nin nokta göz + kaş dilinden ayrışır. |
| Ağız | Küçük, renkli iç ağız (#D9534F). Şaşkınlıkta "o", zaferde geniş "D". |
| Gövde | Kısa **trapez panço/palto**, teal #1F8A8A, **hardal sarısı atkı #F2B134**. Kapsül değil. |
| Uzuvlar | Çizgi değil, **kalın "erişte" kollar**, beyaz eldiven eller (4 parmak). Kısa silindir bacaklar, lacivert botlar. |
| İmza obje | **Pirinç büyüteç**, atkıya iple bağlı. "Gizli mekanizma ifşası" anlatımında her videoda bir kez büyütecin camından "iris insert" yapılır; Ricks'in daire inset'inin bizdeki marka versiyonu. İkincil imza: kafanın üstünde soru işareti şeklinde tek tutam saç. Merakta dikleşir, ifşa anında ünlem olur. |
| Rol sistemi | Ana karakter her zaman Mox. Yan karakterler aynı "çakıl kafa" iskeletini kullanır, ama kafa rengi ten paletinden (#E8B48A, #C68C5E, #8D5A3B, #F6DCC0) seçilir. Rol şapka + gövde rengiyle verilir. Antagonist için tek kural: gövde koyu bordo #6B1E2E. |
| Kadro limiti | Video başına en fazla 4 isimli karakter. 1 karede en fazla 3 yüz; fazlası kalabalık siluet olur. |
| Tutarlılık | Higgsfield `manage_reference_elements` ile "Mox" referans elementi: önden, ¾, profil, arkadan + 6 ifade (bölüm 6a). |

---

## 2. Arka plan / dünya stili

- **Render:** Hibrit "2D cel karakter + boyalı 2.5D/3D ortam". Ortamlar ışıklandırılmış 3D sahne gibi duruyor (perspektif, hacimli gölge, gerçek derinlik), ama dokular fırça-boyama ve hafif "Pixar konsept art" gibi. Bazı objeler neredeyse foto-gerçekçi 3D: VS1Z'deki ejder başları ve kurbağalar, CJwg'deki slot makinesi. Bu stil karışıklığı ve tutarsız çizgi kalınlığı AI görüntü üretiminin tipik izi. Hepsinde **kalın konturlu karakter** ile **konturu çok ince ya da hiç olmayan ortam** ayrımı var.
- **Bir alt tür daha:** 0m6 (Japonya ofisi) ve nzbk (hırsız) daha düz, vektör/cel-shaded, kalın çizgili iç mekân. Yani kanal tek bir "model stili"ne kilitli değil; karakter tasarımı sabit, ortam render'ı videoya göre değişiyor.
- **Işık:** Sıcak pratik ışık (lamba, mum, gün batımı, neon) ile soğuk mavi ortam ışığı (gece, gölge) karşıtlığı. Doygun piksellerin hue dağılımı: kırmızı-turuncu-amber (0–60°) **%41**, mavi (210–240°) **%31**, yeşil **%10**. Klasik turuncu-mavi tamamlayıcı ışık. Hemen her videoda gece/gündüz geçişi var (VS1Z: gün → gün batımı → gece → sabah; GM9U: gece → gün doğumu aynı plan içinde).
- **Parlaklık/doygunluk (HSV ortalama, core 22):** V **%61,7** (medyan), S **%45,2**. Rakipler daha karanlık: Loaded Dice V %28,6, Why Side %35,8, Circle Toon %41,1. Ricks, örnekteki en aydınlık animasyon kanalı.
- **Alan derinliği:** Belirgin. Ön planda bulanık obje + net karakter (eQR3 31–35 sn rack focus, VS1Z 13 sn). Close-up'larda arka plan bokeh. Bu, image-to-video modellerinin varsayılan "sinematik" çıktısıyla örtüşüyor.
- **Dönem/mekân:** Antik Çin sarayı, ortaçağ şato, 1800'ler Amerikan kasabası, Japon pachinko salonu ve ofis, korsan gemisi, 1920'ler at yarışı, kumarhane, beyin/vücut içi metaforları. **Dünya içi tabelalar** neredeyse her sahnede: "PRIZE COUNTER", "CAREER DEVELOPMENT ROOM", "FIRE EMPLOYEE", "CERTIFICATE OF DEATH", "ACID SPA", "HYPNAGOGIA". Bilgi altyazı yerine sahnenin içine yazılıyor. Metinler temiz okunuyor; bu, metin üretebilen yeni nesil modelleri (nano banana pro / gpt-image sınıfı) gösteriyor.

**Palet (Ricks core, k-means; altyazı bandı hariç).** Ham k-means renkleri orta tonlara çekiyor. Uygulamada kullanmak için vurgu, gölge ve parlak tonları ayrı kümeledim:

| Grup | Hex (ağırlık sırasıyla) |
|---|---|
| Genel (10 küme) | #221C27 (16%), #676659, #E3DEDA, #6B3A29, #273A73, #DAB48E, #948C89, #C07840, #4475CA, #8FB3DB |
| Vurgu (S>%55, V>%45; piksellerin %22'si) | #8D3D2A tuğla-kırmızı, #BF613A turuncu, #24388D lacivert, #DCA444 altın, #4153C7 kobalt, #65A538 çimen, #489EE5 gök mavisi, #228794 teal |
| Gölgeler (V<%30; %14) | #0F0C14, #101635, #231922, #3E2624, #2D213A, #1D2C42 (gölgeler siyah değil; mor-lacivert) |
| Işıklar (V>%80; %11) | #F1E9D9, #D7D3CF, #EADABF, #F7F6F3, #E1E5ED, #C6D9EA |

**Bizim için palet önerisi:** gece #101635 / #2D213A, sıcak ışık #DCA444 / #BF613A, Mox kafa #F4C59A + atkı #F2B134 + gövde #1F8A8A, kontur #1E2340.

---

## 3. Kamera ve geçiş grameri

**Ölçülen (core 22, medyan):**
- 0,5 sn'lik adımların **%0'ı statik**. 22 videonun 20'sinde 1 sn'yi aşan tek bir donma yok; kalan ikisinde en uzun duruş 1,0 sn. **Kamera hiç durmuyor.**
- Ölçülebilir kamera hareketi (pan/tilt + zoom) zamanın **%44'ü**: pan/tilt %35, push-in %8, pull-out %1,7. Kalan %42 "diğer hareket": karakter animasyonu, paralaks, morph, dolly kombinasyonları. Global kayma/ölçek olarak yakalanamayan orbit ve paralaks da büyük ihtimalle bu grupta.
- **Geçiş tipi (22 videoda toplam):** sert kesme **3** (video başına 0), dissolve **142** (medyan 7/video), whip/morph/hızlı kamera **150** (medyan 6,5/video). Ricks yeni dönemde **sert kesme kullanmıyor**. Karşılaştırma: eski komik klip LUGcyIwlcto'da 38 sert kesme var; Low Poly 29/3 video, Loaded Dice 13, Why Side 12.

**Hareket sözlüğü** (sıklık 10 videonun kontak sayfasından elle sayıldı):

| Hareket | Video başına | Ne zaman kullanılıyor (anlatıma göre) |
|---|---|---|
| Yavaş push-in (dolly in) | 4–8 | Karakterin replik/ifade anında ve anahtar ismin söylendiği kelimede. Kamera konuya doğru yaklaşıyor (VS1Z 10–12 sn: "jar… ball… frog's" boyunca kavanoza itme). |
| Yatay pan / kayma ve paralaks | 5–10 | Uzun cümlelerde mekânı "gezdirme". Kalabalık, koridor, sokak (eQR3 pachinko koridoru, GM9U kasaba). |
| Kısa dissolve (0,1–0,3 sn) | ≈7 | Cümle ya da yan cümle sınırında yeni mekâna geçiş. Klip birleşim yerlerini gizliyor. |
| Whip pan / hızlı kamera savrulması | ≈3–5 | "But…", "Then…", "So…" gibi dönüş kelimelerinde, yeni bilgi bloğunun başında. |
| Morph / eşleşen şekil geçişi | 1–3 | Bir objeden ilgili objeye (çömlek → imparatorun yüzünün yansıdığı kâse, VS1Z 20 sn; ofis masası → saat). |
| Crash zoom / hızlı pull-out | 0–1, genelde hook'ta | PL-Y: yüz close-up'tan 0,75 sn'de geniş plana. Hook'ta kompozisyonu açıp "sahneyi" gösteriyor. |
| Kuşbakışı / tepeden plan, harita | 1–3 | Mekanizma ve yerleşim anlatımı: masa üstü (0m6), sarkaç mekanizması (VS1Z 49–52), şehir havadan (eQR3 4 sn), yol haritası (DEe0). |
| Kesit / cutaway (diorama) | 10 videonun ≈5'inde | "İçeride ne var" ifşası: mezar kesiti (GM9U), yer katmanları (VS1Z final), deri katmanları (uRk), uyku derinliği okyanusu (PL-Y), hap vücut içinde (_sUA). |
| Daire / büyüteç "iris" inset | 10 videonun ≈3'ünde | Mikro detay (lnYL "soaking" barut lifleri, TgyH büyüteç). |
| Rack focus / sığ alan derinliği | 1–2 | Duygusal vurgu, "sır" anı (eQR3 tokens penceresi). |
| X-ray / şeffaf beden | 10 videonun 1'inde | Beyin/uyku anlatımı (PL-Y 13–18 sn). |
| Plan içinde zaman/ışık geçişi | 1 | Bekleme ve zaman atlaması ("all night" → "sunrise", GM9U 46–52). |
| Diegetik metin kartı (tabela, belge) | 3–6 | Rakamı ya da ismi okutmak için. Altyazı dışında metin bindirmesi yok. |

**Anlatıma göre zamanlama:** Görsel değişimleri kelime başlangıçlarıyla otomatik eşleştirmeyi denedim. Kelimeler 0,3 sn'de bir geldiği için şans düzeyi zaten %87; sonuç (%87) anlamlı fark vermiyor. Bu yüzden zamanlamayı kontak sayfalarından elle okudum. Kural şu: **yeni mekân cümle başında geliyor; aynı mekân içindeki yeni kompozisyon, cümledeki somut ismin söylendiği karede geliyor.** Örnekler: "dragon's" ejder close-up'ı, "the whole court" geniş saray, "a hill" tepe, "Edison" Edison.

---

## 4. Kurgu ritmi sayıları

| Metrik (medyan) | Ricks core 22 | Hit ≥5M (12) | Orta 1–5M (6) | Flop ≤1M (4) |
|---|---|---|---|---|
| Süre | 57,3 sn | 55,9 | 60,1 | 51,3 |
| Plan geçişi (dissolve + whip) | 14 | 12,5 | 13 | 14,5 |
| **Ortalama plan süresi** | **3,8 sn** | 3,8 | 4,0 | 4,4 |
| Görsel değişim / 10 sn (eşik 28) | **10,5** | 8,5 | 10,9 | 11,0 |
| Görsel değişim / 10 sn (kaba eşik 40) | 5,6 | 5,1 | 6,5 | 6,0 |
| İki görsel değişim arası (medyan) | **0,6 sn** | 0,68 | 0,6 | 0,6 |
| Statik / ≥1 sn duruş | %0 / 0 sn | 0 | 0 | 0 |
| Kamera hareketi (pan + zoom) | %44 | %44 | %42 | %46 |
| Parlaklık V / Doygunluk S | 61,7 / 45,2 | 63,0 / 44,4 | 61,3 / 45,0 | 59,5 / **52,7** |

Özet: **Her ≈3,8 sn'de bir yeni plan, her ≈1 sn'de bir yeni kompozisyon.** Kaba eşikle her ≈1,8 sn'de belirgin yeni görüntü.

**10 sn'lik pencere eğrisi** (görsel değişim/10 sn, core medyanı):

```
0–10 sn  : 11     ███████████   (hook: en yoğun)
10–20 sn : 10     ██████████
20–30 sn : 9      █████████
30–40 sn : 8      ████████      (orta çukur)
40–50 sn : 10,5   ██████████
50–60 sn : 12     ████████████  (final ifşa / kesit planı yeniden hızlanıyor)
```

Hitlerde eğri U şeklinde: 11 → 9,5 → 9 → 8 → (6) → 12.

**Hit ve flop karşılaştırması:** Kurgu ritmi başarıyı açıklamıyor. log(izlenme) ile korelasyonlar: değişim/10 sn **−0,23**, plan sayısı +0,17, plan süresi −0,09. Flop'lar biraz *daha hızlı* kesilmiş (11,0'a karşı 8,5). Görsel açıdan ölçülebilen tek sinyal **doygunluk**: r = **−0,51**, flop'lar 52,7'ye karşı hitler 44,4. CJwg (slot makinesi, S 60) ve uRk (S 53) aşırı doygun. Kontak sayfalarında görülen nitel fark: flop'lar **soyut metafor dünyasında** geçiyor (vücut içi hap, "hafıza dükkânı", slot makinesi iç devresi). Hitler **gerçek, somut bir tarihsel mekân + tek bir fiziksel obje** üzerine kurulu (kavanoz, mezar zili, ofis odası, pachinko penceresi). Yani görsel olarak fark yaratan şey ritim değil, *konunun somutluğu*. Bu konu analist A/B'nin alanı.

**Rakip ritimleri** (görsel değişim/10 sn | plan süresi | sert kesme payı):

| Kanal | Değişim/10 sn | Plan süresi | Sert kesme |
|---|---|---|---|
| Circle Toon | 21,2 | 1,2 sn | %2 (whip ağırlıklı) |
| george | 14,4 | 1,95 sn | %17 |
| Ricks | 10,5 | 3,8 sn | %1 |
| Low Poly | 8,2 | 2,2 sn | %57 |
| Loaded Dice | 7,8 | 6,1 sn | %34 |
| Why Side | 5,7 | 6,4 sn | %44 |

Kısa (25–30 sn) formatlar çok daha hızlı; 60 sn formatlar ≈ 6–10 değişim/10 sn bandında.

---

## 5. Kelimesi kelimesine görselleştirme kuralı

Yöntem: 20 core videonun her birinden altyazı JSON'undan rastgele 2 içerik kelimesi seçildi (stopword ve -ly/-ing/-ed hariç, ≥4 harf). Kelimenin başlangıcından 0,3 sn sonraki kare kodlandı (`out/c_literal_1..4.png`, `c_literal_sample.json`).

| Kod | Sonuç |
|---|---|
| Söylenen kelimenin kendisi karede görünüyor | **21/40 (%53)** |
| Karede o cümlenin öznesi ya da nesnesi var (kelime fonksiyonel olsa bile) | **38/40 (%95)** |
| Örnekteki somut isimler (20 adet: trunk, spear, counter, house, tickets, bell, glass, dimmer, racetrack, door, customers…) | **19/20 (%95)** isim söylendiği anda ekranda. Tek istisna "dragon": kamera o anda ejderin *içindeki* sarkaçta. |
| İlgisiz ya da genel görüntü | 2/40 ("rent", "first") |

**Kural:** Her cümlenin somut ismi, söylendiği ±0,3 sn içinde ekranda olmalı. İsim yoksa (fiil, sıfat, bağlaç) kamera o cümlenin öznesine yaklaşır. Soyut kavram (hypnagogia, "random") dünya içi tabela ya da etiket olarak yazılır: "HYPNAGOGIA" yazısı, duvarda rakamlar.

---

## 6. Üretim çıkarımı ve yeniden üretim tarifi

### 6.1 Ricks muhtemelen nasıl üretiyor?

- **AI görsel + AI image-to-video + CapCut tarzı birleştirme. After Effects ya da Blender değil.** Kanıtlar:
  1. Plan süresi 3,8 sn civarında kümeleniyor: 4–5 sn'lik üretim klipleri kırpılmış.
  2. 22 videoda yalnız 3 sert kesme var, ≈14 geçişin hepsi dissolve ya da whip. Klip birleşimini gizlemenin en ucuz yolu bu, ve her klip kamera hareketiyle başlayıp bitiyor.
  3. %0 statik kare. I2V modelleri her zaman bir kamera hareketi üretir.
  4. Aynı karede stil karışıklığı (cel karakter + foto-gerçekçi 3D kurbağa/ejder), plandan plana değişen çizgi kalınlığı, temiz dünya içi tabela metinleri. Yeni nesil görsel modellere işaret ediyor.
  5. Ağız senkronu yok, karakter animasyonu sınırlı mikro hareket.
  6. Karakterin plandan plana hafifçe değişmesi (saç ve gövde oranı). Bu, referans görselle tutarlılık sağlandığını gösteriyor; rig değil.
- **Video başına tahmini iş:** ≈15 plan (14 geçiş + 1), yani ≈15–18 anahtar kare ve ≈15–20 I2V üretimi (ıskalar dahil ≈25). Altyazı: tek kelime/kısa öbek, beyaz kalın sans, siyah kontur + gölge, ekran yüksekliğinin ≈%70'inde (CapCut auto caption benzeri).

### 6.2 Bizim reçetemiz (Higgsfield MCP + ffmpeg + Remotion `C:\dev\the-other-self`)

**Adım 0: Referans.** Mox referans sayfası (6a) → `manage_reference_elements` ile "MOX" elementi. Her yan karakter için de bir element.

**Adım 1: Senaryodan plan listesi.** VO metnini cümlelere böl. Her cümle 1 plan (hedef 3–4,5 sn). Her plana şunları yaz:
- (i) ana somut isim (literal kuralı),
- (ii) mekân,
- (iii) kamera hareketi (aşağıdaki tablo),
- (iv) geçiş tipi.

60 sn VO ≈ 15 plan. 15'ten fazla planda aynı mekânı 2–3 açıyla tekrar kullan; mekân başına 1 "master" kare üretip açıları ondan çıkar.

**Adım 2: Anahtar kare.** `generate_image` ile nano_banana_pro ya da flux_3_image, 9:16, MOX referansıyla. Prompt şablonu 6b.

**Adım 3: Image-to-video.** `generate_video` ile:
- Ana model: **seedance_2_0** (start_image + image_references, kimlik tutarlılığı; 4–5 sn, 720p, `generate_audio:false`).
- Ucuz taslak: **seedance_2_0_mini** ya da **grok_video_v15_lite**.
- Morph geçişleri için seedance'ın `start_image` + `end_image` modu: plan A'nın son karesi ile plan B'nin ilk karesi.

Toplu üretim için `generate_video_batch` + `jobs_wait` kullan. Prompt şablonu 6c.

**Adım 4: ffmpeg ön işleme.**
- Her klibi 3,0–4,5 sn'ye kırp. İlk ve son 0,3 sn'yi bırak; I2V başlangıcındaki donukluğu atar.
- 30 fps'e normalize et: `ffmpeg -i in.mp4 -vf "fps=30,scale=1080:1920:flags=lanczos" -an -c:v libx264 -crf 17 out.mp4`.

**Adım 5: Remotion montaj.**
- `<Series>` ile klipler, aralarda 6–9 karelik (0,2–0,3 sn) crossfade.
- Her 3. geçiş whip olsun: 4 karelik yatay translate + motion blur (`filter: blur`) ve 1 karelik beyaz flash.
- Kelime altyazısı: VO'nun kelime zamanlaması (ElevenLabs alignment ya da Whisper) ile 1–3 kelimelik öbekler. Font Montserrat/Poppins ExtraBold 64–72 px @1080w, beyaz, 8 px #000 stroke + gölge, y = %68–72. Altyazıya renk vurgusu yok; Ricks sade.
- Gerekirse klip üstüne ek Ken-Burns (scale 1,00 → 1,06) uygula ki hiçbir an statik kalmasın.
- Final: `npx remotion render` → 1080×1920, 30 fps.

**Plan uzunluğu kuralları (ölçümlerden):**
1. Plan 2,5–5 sn, hedef medyan 3,8 sn. 60 sn'lik videoda 14–16 plan.
2. Her plan içinde kompozisyon ≈1 sn'de bir değişmeli (kamera hareketi, ifade değişimi, obje girişi). Hiçbir an ≥1 sn statik olmamalı.
3. Sert kesme yasak. Varsayılan geçiş: %50 dissolve (0,2 sn), %40 whip/hızlı kamera, %10 morph (start/end frame).
4. Yoğunluk eğrisi: 0–10 sn 11 değişim, 30–40 sn 8'e düşebilir, son 10 sn tekrar ≥11 (final ifşa planı: kesit/kuşbakışı).
5. Hook ilk 0,75 sn'de bir crash zoom/pull-out ya da obje close-up'ı ile açılmalı.
6. Her cümlenin somut ismi ±0,3 sn içinde ekranda olmalı. Soyut kavram dünya içi tabela ile yazılır.
7. Video başına en az 1 kesit/cutaway ve 1 kuşbakışı, isteğe bağlı 1 büyüteç-iris inset (Mox imzası).
8. Doygunluğu S ≈ %40–48'de tut. Neon ya da kırmızı ağırlıklı aşırı doygun sahneden kaçın; flop'larda S 52,7.

### 6a. Karakter referans sayfası prompt'u (nano_banana_pro / flux)
```
Character turnaround reference sheet, original cartoon mascot "MOX": a short chubby
character 2.2 heads tall, big rounded-square pebble-shaped head (soft corners), apricot
skin color #F4C59A, thick uniform dark navy outline #1E2340, two tall white pill-shaped
eyes with round navy pupils, no eyebrows, small mouth with red inner color, single
question-mark-shaped hair tuft on top of head, short teal #1F8A8A trapezoid poncho coat,
mustard yellow scarf #F2B134, chunky noodle arms with white 4-finger cartoon gloves, short
cylindrical legs with navy boots, a small brass magnifying glass hanging from the scarf on a
cord. Views: front, three-quarter, side profile, back. Below: 6 expression heads (neutral,
curious, shocked with wide eyes, smug grin, scared, triumphant). Flat cel shading with one
soft shadow tone, clean vector-like lines, plain light grey background, no text, consistent
proportions across all views.
```

### 6b. Sahne anahtar karesi prompt şablonu
```
Vertical 9:16 frame. [MOX reference] {action, e.g. "peers through his brass magnifying glass
at"} {CONCRETE NOUN of the sentence} in {SETTING + ERA, e.g. "a 1890s snowy New England
graveyard"}, {TIME OF DAY: golden hour / moonlit night / neon-lit night}. Style: 2D cel-shaded
cartoon character with thick navy outlines placed inside a richly painted 2.5D storybook
environment, painterly textures, volumetric warm practical lights against cool blue ambient
shadows (orange-teal contrast), soft depth of field with blurred foreground prop, cinematic
wide-angle {SHOT: close-up / medium / wide establishing / top-down overhead / cutaway
cross-section diorama}, readable in-world sign that says "{LABEL}" (only if needed),
moderate saturation, no extra text, no watermark, subject in upper 60% of frame (leave
lower-middle band clear for captions).
```
Sahne kategorilerine göre ek ifadeler:
- Kesit: `cutaway cross-section diorama showing layers underground, labeled`
- Kuşbakışı: `top-down overhead view, map-like`
- İris: `circular magnifying-glass vignette inset revealing a macro detail of {X}`

### 6c. Image-to-video hareket prompt'u (seedance_2_0, 4–5 sn, ses kapalı)
```
Keep the exact art style, outlines and character design of the start image. Camera: {ONE
move — slow dolly push-in toward {noun} / smooth lateral truck right revealing {noun} /
fast whip pan right at the end / quick pull-back from close-up to wide / slow overhead
crane down}. Subtle character motion only: {MOX blinks and raises magnifying glass / turns
head toward camera with shocked eyes}. Gentle parallax between foreground and background,
light particles/dust in the air, no scene cut, no new characters, no text changes, no
morphing of the character's face, continuous motion from first to last frame.
```
Morph için `start_image` = önceki planın son karesi, `end_image` = yeni anahtar kare. Prompt sonuna `smooth transformation of {A} into {B}` ekle.

---

## 7. Rakip stil karşılaştırması

| Kanal | Render | Karakter | Kamera/kurgu | Altyazı | Görsel kalite | Solo maliyet/zaman |
|---|---|---|---|---|---|---|
| **Ricks Clips** | AI boyalı 2.5D ortam + cel karakter | Beyaz oval kafa, kapsül gövde (C&H benzeri) | Sürekli kamera, dissolve/whip, 3,8 sn plan, %0 statik | Beyaz, siyah kontur, 1–3 kelime, ortada | Yüksek, "film" hissi | Orta: ≈15 görsel + ≈20 I2V/video |
| **Low Poly Shorts** | PS1 low-poly 3D, hazır asset | Gerçekçi ama düşük poligonlu insan | %57 sert kesme, 2,2 sn plan, az kamera | Küçük sarı, alt-orta | Bilerek "çirkin", ironik | Düşük (Blender/oyun motoru + asset); bilgi ve öğrenme gerekiyor; düşüşte |
| **Loaded Dice** | Low-poly 3D kumarhane, karanlık (V 28,6) | Low-poly figürler | 6,1 sn plan, push-in ağırlıklı, sert kesme + dissolve | Küçük beyaz, alt | Orta | Düşük–orta (tek set tekrar kullanılıyor) |
| **Circle Toon History** | Gerçekçi 3D ortam (Unreal benzeri) + beyaz 3D figür, 2D çizilmiş yüz | Beyaz yuvarlak kafa, rol şapkası | Çok hızlı: 21 değişim/10 sn, 1,2 sn plan, whip ağırlıklı | BÜYÜK HARF beyaz, kalın kontur | Yüksek ama koyu | Yüksek (3D sahne/animasyon); 25 sn format telafi ediyor |
| **The Why Side** | AI semi-gerçekçi stilize 3D | Gerçekçi insanlar | 6,4 sn plan, sert kesme + grafik bindirme (sayı, ok, tarih etiketi) | Renkli anahtar kelime (kırmızı/sarı/yeşil) | Yüksek (S 65,6 sahnede çok canlı) | Orta: Ricks'e benzer AI zinciri + motion grafik |
| **i think it's george** | Hazır Sketchfab 3D modeller + render | Gerçekçi 3D insan, anlatıcı avatarı | 14 değişim/10 sn, 2 sn plan, whip | BÜYÜK HARF condensed beyaz | Orta (asset kolajı) | Orta–yüksek (sahne kurulumu) |

**Solo içerik üreticisi için en iyi kalite/maliyet:** Ricks tipi zincir, yani **AI anahtar kare + I2V + Remotion montaj**, ama *kendi* karakterimizle (Mox).

- 3D/Blender kurulumu (Circle Toon, george, Low Poly) gerektirmiyor.
- Somut tarihsel mekânları her video için sıfırdan, ucuza çizebiliyor.
- Görsel olarak en aydınlık ve en okunur stil (V %62, tek kalın konturlu karakter), dolayısıyla mobilde ve Reels'te avantajlı.
- 60 sn formatta 15 plan, insan işçiliğiyle günler sürecek bir işi saatlere indiriyor.

Low-poly ise en ucuz ama en jenerik ve düşüşte olan stil; ancak ikinci bir "B kanalı" için düşünülebilir. Why Side'ın renkli anahtar kelime altyazısı ve tarih/yer etiketi, Ricks reçetesine eklenebilecek ucuz bir iyileştirme. Instagram'da bu sinyal ayrıca test edilmeli.
