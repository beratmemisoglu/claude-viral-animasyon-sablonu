# Tersine Mühendislik Raporu — "Why Traffic Stops for No Reason, and How One Driver Can Fix It"

Kaynak: `videoplayback (5).mp4` (7:27,6 · 640×360 · 30 fps · H.264 · AAC 44,1 kHz) + transkript + mind map.
Yöntem: 1 fps kontak sayfaları (447 kare), 17 sahne sınırında 10 fps geçiş şeritleri, 26 tam çözünürlüklü anahtar kare, piksel renk örneklemesi, ses RMS/stereo/spektrum ölçümü.

**İşaretleme:** **[G]** = gözlem (karede görülen) · **[Ç]** = çıkarım (kanıta dayalı tahmin) · **[B]** = belirsiz.
Zaman damgaları ±0,5 sn (1 fps örnekleme); geçişler ±0,1 sn (10 fps örnekleme).

---

## A. Yönetici Özeti

- **Format:** Uzun-form (7,5 dk) yüzsüz bilim açıklayıcı. Tek anlatıcı VO + sürekli, sakin ambient müzik yatağı. Kamerada yüz yok, stok görüntü yok, fotoğraf yok.
- **Görsel motor:** Tamamen **kodla üretilmiş 2D, kuşbakışı (top-down) trafik simülasyonu + veri-görselleştirme (infografik) katmanı**. Arabalar el ile anime edilmiş gibi değil; aralarındaki mesafe, fren dalgası ve yığılma davranışı bir trafik modelinin çıktısı gibi tutarlı **[Ç, yüksek güven]**.
- **Tek ana "aktör":** kırmızı fren-ışığı parıltısı (glow). Tüm hikâye "kırmızının nerede olduğu ve hangi yöne aktığı" ile anlatılıyor. İkinci aktör: kehribar (amber) renkli **"sen" arabası**.
- **Kurgu:** 18 sahne, **hiç sert kesme yok**. Her bölüm geçişi aynı reçete: ~0,1–0,2 sn **koyu laciverte söndürme → 1–2 kare lacivert → ~0,2–0,3 sn yeni sahne belirmesi**, ardından ~0,3–0,5 sn sonra bölüm başlığı. Ortalama sahne süresi ~25 sn, ama sahne içinde **her 2–4 sn'de bir yeni bilgi katmanı** (etiket, sayaç, panel, vurgu halkası) ekleniyor.
- **Kamera:** Neredeyse tamamen **statik**. Hareket hissi kameradan değil, simülasyondan geliyor. Birkaç yerde kompozisyon kayması/zoom-out var (1:14, 2:24).
- **Tipografi:** Tamamı BÜYÜK HARF, DIN-benzeri dar/endüstriyel grotesk; 4 seviyeli hiyerarşi (bölüm başlığı + kehribar alt çizgi / dev sayı / küçük etiket / kaynak atfı).
- **Başarı formülü:** "Soru → laboratuvar deneyi (halka) → mekanizma (zincirleme fren) → doğası (geriye akan dalga) → kanıt (hava fotoğrafı diyagramı) → koşul (devrilme noktası) → tetikleyiciler → model (4 kural) → kalıcılık → çözümler (3) → izleyiciye görev (boşluk bırak) → checklist özet → bookend kapanış".

---

## B. Global Görsel Stil Analizi

### B1. Tür ve format
| Öğe | Değer |
|---|---|
| Tür | Popüler bilim / "explainer", veri-gazeteciliği estetiği |
| Format | Yüzsüz, VO + motion graphics, 16:9 uzun-form YouTube |
| Anlatı tonu | Sakin, kanıta dayalı, "dürüst olayım" tipi kanıt sınırı belirten (5:20 civarı) |

### B2. En-boy oranı, çözünürlük, kalite
- 16:9, dosya 640×360 **[G]**. Orijinalin 1080p/4K olduğu, bu kopyanın düşük çözünürlüklü indirme olduğu muhtemel **[Ç]**. Küçük etiketlerin (≈5–6 px) bu çözünürlükte okunamaması bunu destekliyor.
- 30 fps; ince çizgiler ve glow'da sıkıştırma artefaktı var.

### B3. Sanat yönetimi
- "Gece haritası / kontrol odası HUD'u" estetiği: koyu, desatüre zemin + tek parlak sinyal rengi (kırmızı) + tek vurgu rengi (kehribar).
- Gerçekçilik seviyesi: araçlar **stilize top-down vektör ikonlar** (yuvarlatılmış dikdörtgen gövde, koyu cam, 4–5 renk varyantı: beyaz, açık gri, gri, mavi, petrol yeşili). Yol: koyu gri asfalt şerit + beyaz kenar çizgileri + kesik şerit çizgileri.

### B4. Animasyon stili
- **2D, kuşbakışı, prosedürel/simülasyon tabanlı** + **infografik/UI animasyonu** (paneller, bar'lar, sayaçlar, çizgi grafikler, checklist).
- Karakter animasyonu, 3D, kolaj, stok görüntü **yok** [G].

### B5. Arka plan işleme
| Katman | Gözlem |
|---|---|
| Ana zemin | Koyu yeşilimsi-gri, düşük kontrastlı **bulut/duman dokusu** (Perlin-noise benzeri), ~#121C19 – #1F2923 aralığında [G] |
| Doku hareketi | Doku sahneler arasında aynı; çok yavaş kayma olup olmadığı 1 fps'de belirsiz [B] |
| Veri paneli zemini | Düz koyu lacivert **#0B121E**, ince ~1 px açık kenarlık (#2A3340 civarı), hafif yuvarlatılmış köşe (~6–8 px @1080p) [G] |
| Geçiş rengi | Aynı lacivert ton (#0B121E) — geçiş "dip"i siyaha değil laciverte [G] |
| Derinlik | Gerçek ışıklandırma yok. Derinlik = parıltı (bloom) + panel kenarlıkları + doku üstünde düz şekiller |
| Gölge | Araçların altında belirgin gölge yok; yolun hafif koyu dış kenarı var [G] |

### B6. Renk paleti (piksel örnekleri, sıkıştırma nedeniyle ±)
| Rol | Yaklaşık HEX | Kullanım |
|---|---|---|
| Zemin dokusu | #18221D (aralık #0F1816–#222B27) | Tüm "dünya" sahneleri |
| Panel/geçiş laciverti | #0B121E | Grafik panelleri, geçiş dip'i, checklist |
| Asfalt | #2C3033 – #323A3F | Yollar |
| Yol çizgisi | #C8CDD2 (yarı saydam) | Kenar/şerit çizgileri |
| Birincil metin | #FFFFFF | Başlıklar, etiketler |
| İkincil metin | #A3ACAC | Dev sayılar ("22 CARS"), alt satırlar, kaynak atfı (daha soluk) |
| **Sinyal kırmızısı** | çekirdek ≈ #E8453C, kenar/glow ≈ #A04040→saydam | Fren, durma, "jam", uyarı metni |
| **Vurgu kehribarı** | ≈ #F0A848 (#E0A040–#F0B058) | "Sen" arabası, başlık alt çizgisi, kendi kendine giden araç, "doğru davranış" |
| Mavi araç / ikincil | ≈ #3C5A80 | Araç varyantı, 1:28'de "içindekiler" halkaları |

**Renk kuralı [Ç, yüksek güven]:** Kırmızı = problem/dalga; kehribar = izleyici/çözüm; beyaz = nötr bilgi; lacivert = "analiz moduna geçtik". Yeşil yalnızca trafik ışığında (5:00–5:10) görünür.

### B7. Tipografi
| Seviye | Örnek | Boyut (1080p eşdeğeri, ~) | Renk | Hizalama |
|---|---|---|---|---|
| H1 Bölüm başlığı | THE JAM WITH NO CAUSE | ~40–44 px, Bold | Beyaz + altında **kehribar alt çizgi** (~4 px kalın, metinden ~%75 kısa, sola hizalı) | Sol üst, kenar boşluğu ~%2 x / %4 y |
| H0 Dev sayı | 22 CARS / 23 | ~60–90 px, Bold | İkincil gri #A3ACAC | Halka merkezi |
| H2 Durum metni | NO WAVES / 8 STOPPED | ~22–30 px, Semibold | Beyaz / kırmızı / kehribar | Merkez veya öğenin yanında |
| H3 Etiket | HOW HARD EACH DRIVER BRAKED, THE GAP | ~14–18 px, Semibold, geniş harf aralığı | Beyaz / kehribar / kırmızı | Nesnenin üstünde/altında |
| H4 Kaynak atfı | REDELMEIER AND TIBSHIRANI, 1999 | ~12–14 px | Soluk gri | Sağ üst köşe |

- Font kategorisi: **DIN-benzeri endüstriyel/teknik grotesk**, düz terminaller, dar oranlar ("2" ve "C" şekilleri DIN'e çok yakın) **[Ç, orta güven]**. Tam font adı tespit edilemez.
- Tüm metin **BÜYÜK HARF**, cümle sonu noktalama yok (tek istisna: "BUILD ANOTHER LANE?", "SUBSCRIBE!").
- Metin asla 6 kelimeyi aşmıyor (en uzun: "EVERY ONE BRAKED HARDER THAN THE CAR AHEAD").

### B8. Kompozisyon
- **Tek odak, bol negatif alan.** Ekranın %40–60'ı çoğu zaman boş doku.
- Üç tekrar eden yerleşim şablonu (bkz. I bölümü): **Yatay şerit** (yol ekranı yatay keser, y≈%45–60), **Merkez halka** (halka ekranın ortasında, çap ≈ yüksekliğin %78'i), **Bölünmüş ekran** (sol: simülasyon / sağ: lacivert grafik paneli).
- Metin hiçbir zaman ana nesnenin üstüne binmiyor; nesnenin yanına, üstüne veya altına "etiket" olarak konuyor.

### B9. Kamera dili
- %90+ **statik kare** [G]. Hareket = simülasyon.
- Gözlenen istisnalar: 1:14 yolun incelmesi (zoom-out ~0,6×, 1 sn içinde) [G]; 2:24 halkanın merkezden sola kayıp sağa panel açılması (reframe) [G]; 1:41'de yolun dikey şeride dönüşmesi aslında geçişle yapılmış yeni kompozisyon (kamera dönüşü değil) [G, 10 fps şeridiyle doğrulandı].
- Pan, whip, rotasyon, sahte derinlik/parallax **yok**.

### B10. Kurgu ritmi
| Metrik | Değer |
|---|---|
| Sahne sayısı | 18 |
| Bölüm geçişi (dip) sayısı | 17 |
| Sert kesme | 0 |
| Ortalama sahne süresi | ~24,9 sn (aralık 16–37 sn) |
| Sahne içi "yeni görsel olay" sıklığı | ~2–4 sn'de bir (etiket, sayaç adımı, panel, halka, ok) |
| Görsel yoğunluk | Düşük-orta: aynı anda en fazla ~5 metin öğesi |

### B11. Anlatı yapısı ve dikkat yönetimi
Dikkat, **sahne değişiminden değil "katman eklemeden"** geliyor. Her cümle ekrana bir etiket/ölçüm/vurgu ekliyor; böylece görüntü sabit olsa bile göz her 2–4 sn'de yeni bir şey okuyor. Sayaçlar (7→8→9→10→11 STOPPED; 12→15→18→21→23; 8→15 KM/H) sürekli bir "ilerleme" duygusu yaratıyor.

### B12. Ses (ölçümler)
| Ölçüm | Sonuç |
|---|---|
| Kanal | **Mono** (L–R fark sinyali ≈ −180 dB; iki kanal özdeş) [G] |
| Ortalama seviye | ≈ −26 dBFS RMS; konuşma %75–95 dilimi −24 / −22 dBFS |
| Sessizlik | −40 dB altında 0,35 sn'den uzun sessizlik **yok** (son 1,3 sn hariç) → altta sürekli bir yatak var [G] |
| Yatak seviyesi | Konuşma duraklarında ≈ −43 / −46 dBFS (konuşmanın ~18–20 dB altı) |
| Yatak tonalitesi | Duraklarda spektral tepeler 98, 147, 196, 220, 247, 294, 392, 494, 587 Hz → **G majör (G–A–B–D) pentatonik, sakin ambient/piyano-pad** [Ç, yüksek güven] |
| Yatak ritmi | Kapanışta (7:08–7:25) zarf her ~2,5 sn'de bir yükselip sönüyor → seyrek, çınlayan tek notalar (piyano/pluck) [Ç, orta güven] |
| SFX | Spektrumda belirgin transient (whoosh/klik) izi tespit edilmedi; ses kulakla dinlenmediği için SFX varlığı **[B]** |

---

## C. Zaman Damgalı Sahne Dökümü

> Konumlar: x = soldan %, y = üstten %. Boyutlar ekran yüksekliğine (H) veya genişliğine (W) göre.
> Tüm sahneler aynı geçişle girer/çıkar (G bölümü): **"lacivert dip"**. Aşağıda tekrar edilmez, sadece istisnalar yazılır.

### S1 · 0:00,0 – 0:23,8 (23,8 sn) · Soğuk açılış: "Hiçbir şey yokken durdun"
- **Anlatım:** "You're on the motorway and everything stops… It was travelling down the road towards you, backwards…"
- **Mesaj:** Sıkışmanın bir sebebi görünmüyor; sıkışma sana doğru geriye hareket eden bir şey.
- **İlk kare:** Sol alttan sağ üste S-eğrili, ikiye bölünmüş 4×2 şeritli otoyol; üst taşıt yolunda x %65–100 aralığında kırmızı parlayan yoğun araç kümesi. Video siyahtan değil doğrudan dolu kareyle açılıyor [G].
- **Son kare:** Küme sola (yolun gerisine) kaymış, kırmızı dikdörtgen çerçeve içinde; altında sola bakan kırmızı ok.
- **Öğeler:** Otoyol (ekranı çapraz kesen, ~W×%45H bant) · ~100 araç · kırmızı glow kümesi · kehribar "YOU" arabası (x≈%60, y≈%32, kümenin içinde, üstünde küçük kehribar "YOU" etiketi) · 3 yuvarlak çizgi ikon (kaza, yol çalışması, arızalı kamyon; üzeri çizili) · kırmızı yuvarlatılmış dikdörtgen kontur · kehribar vurgu halkası · kırmızı ok.
- **Animasyon:**
  - 0:00–0:23 kırmızı küme sürekli sola (yolun ters yönüne) kayıyor; araçlar sağa ilerliyor → "dalga geriye, araçlar ileriye" fikri ilk saniyeden görselde [G].
  - 0:07 / 0:08 / 0:09 — ikonlar **x≈%52 → %56 → %60, y≈%57'de birer saniye arayla** beliriyor ("No crash, no roadworks, no broken down lorry" ile senkron) [G]; 0:12'de sönüyor.
  - ~0:15 kırmızı kontur kümeyi çevreliyor (ekran genişliğinin ~%30'u).
  - ~0:17 kehribar halka YOU arabasının etrafında; 0:21'de büyük (çap ~%15H) ince halka olarak genişleyip sönüyor (pulse).
  - 0:18–0:23 kümenin altında (x %5–20, y %45) sola bakan kırmızı ok.
  - Alt taşıt yolunda sol tarafta ara ara tekil kırmızı araçlar (küçük fren tapları) [G].
- **Amaç:** Merak (hook) + videonun ana görsel tezinin ilk 20 sn'de "gösterilmesi".
- **Güven:** Yüksek (konumlar ±%5).

### S2 · 0:23,8 – 0:52,7 (28,9 sn) · Halka deneyi "THE JAM WITH NO CAUSE"
- **Anlatım:** "In 2008, physicists in Japan… twenty two cars on a circular track… a jam appeared… began to move backwards round the circle."
- **Mesaj:** Sebepsiz sıkışma laboratuvarda yeniden üretildi.
- **Öğeler / zamanlama:**
  - 0:24,3 halka (merkez x%50 y%50, dış çap ≈ %78H, yol kalınlığı ≈ %4H) belirir; 22 araç saat yönünde dönüyor.
  - 0:24,4–0:24,7 H1 başlık + kehribar alt çizgi sol üstte belirir.
  - 0:29 "22 CARS" (H0, gri) halka merkezinde.
  - 0:31 alt satır "230 M ROUND" · 0:35 "ASKED TO HOLD 30 KM/H" (H3, gri-beyaz, merkezde alt alta).
  - 0:38 halka içinde üstte saat yönünde beyaz yay ok + "ALL GOING ROUND".
  - 0:41 "NO JAM YET" (beyaz) dördüncü satır.
  - 0:45 halkanın **dışında**, sol üstte kırmızı yay belirir; 0:45–0:52 saat yönünün **tersine** uzar (~45°'den ~200° yaya) ve ucunda ok başı.
  - 0:47–0:52 durum satırı kırmızı sayaç: "7 STOPPED → 8 → 9 → 10 → 11" (~1 sn'de bir adım).
  - Başlık ~0:30'da söner (sol üst boşalır).
- **Amaç:** Kanıt + "sebepsiz" iddiasını kontrollü ortamda kanıtlamak.

### S3 · 0:52,7 – 1:20,4 (27,7 sn) · Mekanizma: zincirleme fren
- **Anlatım:** "One driver drifts a little close and touches the brake… Each driver passes the problem back, slightly bigger…"
- **Öğeler:** Tek şeritli yatay yol (y≈%59, tam genişlik) · 8–10 araç · beyaz **reaksiyon zamanlayıcısı** (dolan pasta/saat ikonu, çap ~%4H) bir aracın üstünde · araçların üstünde kırmızı dikey **fren şiddeti çubukları** · çubuk tepelerini birleştiren kesik beyaz zarf çizgisi · "STOPPED" kırmızı etiket · araç altlarında beyaz noktalar.
- **Zamanlama:** 0:56 ilk kırmızı fren + küçük çubuk; 0:57–0:58 pasta saat yönünde dolar (≈1 sn = "takes about a second to react"); 1:02 sol üstte "HOW HARD EACH DRIVER BRAKED" (H3 gri); 1:05–1:13 her yeni araçta bir öncekinden **daha uzun** çubuk; 1:08'den itibaren kesik zarf çizgisi; 1:12 "STOPPED"; **1:14 zoom-out** (yol incelir, daha çok araç görünür, çubuklar sıkışır); 1:17 araçların altında beyaz noktalar (her araca bir işaret).
- **Amaç:** Fiziksel mekanizmanın adım adım görselleştirilmesi; çubuklar "büyüyen problem"in ölçüsü.

### S4 · 1:20,4 – 1:40,9 (20,5 sn) · "IT MOVES BACKWARDS"
- **Anlatım:** "Now look at what the jam is. It isn't a set of cars… It's a wave… around twenty kilometres an hour…"
- **Öğeler:** 3 şeritli yatay yol (y≈%55) · sola doğru yoğunlaşan kırmızı küme · "JOINING →" (x≈%30, y≈%45) ve "LEAVING →" (x≈%78) etiketleri + küçük beyaz oklar (1:24–1:25) · 1:28 kümedeki araçlar mavi kontur halkalarla işaretlenir + altta "THE ONES THAT WERE IN IT" · 1:29–1:30 kırmızı dikdörtgen · 1:31 üstte "THE CARS" + sağa beyaz ok; altta "THE JAM" + sola kırmızı ok · 1:32 "AROUND 20 KM/H" · 1:33 sağ üstte lacivert küçük **inset** (halka + kırmızı yay, S2'nin minyatürü) · 1:36 "WHERE IT WAS" kesik çizgili hayalet dikdörtgen (kümenin eski yeri).
- **Not:** Mavi halkalı araçlar sağa çıkarken kırmızı dikdörtgen sola gidiyor → "dalga farklı araçlardan oluşur" görsel kanıtı.
- **Amaç:** Kavramsal sıçrama: nesne değil dalga.

### S5 · 1:40,9 – 2:08,7 (27,8 sn) · Havadan bakış: zaman-uzay diyagramı
- **Anlatım:** "In the 1970s, researchers in Ohio flew along a motorway… Each car becomes a line on a chart…"
- **Öğeler:** Sağda dikey yol şeridi (x≈%93, tam yükseklik) · "SEEN FROM ABOVE" (sağ üst, 1:42) · "ONE PICTURE A SECOND" + yol üzerinde fotoğraf karesi çerçevesi (1:46) · 1:49 solda büyük lacivert panel (x %3–80, y %8–96) · panelde nokta matrisi → 1:52 noktalar **çizgilere dönüşür** (beyaz çapraz = hareket, kırmızı yatay = durma) · bir aracın çizgisi kehribar · eksen etiketleri "DISTANCE ALONG THE ROAD" (dikey) ve "TIME →" · 1:57 lejant "/ MOVING", 2:00 "— STOPPED" · 2:02 kırmızı bölge genişler · 2:05 panelin sol üstünden sağ alta uzanan **kırmızı düz çizgi** (dalga cephesi) çizilir · 2:08 "THROUGH CAR AFTER CAR".
- **Bağlantı:** Yol şeridi ile panel arasında ince kesik yatay kılavuz çizgiler (yoldaki konum ↔ grafikteki y) [G, 1:58 tam karesi].
- **Amaç:** Görselden kanıta: bilimsel grafiğin "okunmasını" öğretmek.

### S6 · 2:08,7 – 2:35,2 (26,5 sn) · "THE TIPPING POINT"
- **Anlatım:** "It only happens when the road is busy enough… Add cars and the road carries more, up to a peak…"
- **Öğeler / zamanlama:** Halka (merkez, çap ≈ %70H) + "12 CARS" · 2:10 başlık · 2:13 alt tarafta tek kırmızı tap → "THE TAP FADES" (2:14) · 2:17–2:21 sayaç **12 → 15 → 18 → 21 → 23** (yeni araçlar kırmızı parıltıyla eklenir) · 2:22 "THE SAME TAP GROWS" (kırmızı) + halkanın dışında kırmızı yay · **2:24 halka sola kayar (merkez x %50 → %28) ve küçülür; sağda lacivert grafik paneli açılır** · kehribar nokta "HOW FULL THE ROAD IS" eksenine göre eğri çizer: 2:26–2:29 yükselir, 2:29 tepe, 2:30–2:31 titreşerek düşer · 2:32 "THE MOST IT CAN CARRY" (kehribar) + tepeden dikey kesik çizgi.
- **Amaç:** Koşulu tanımlamak; temel diyagramı (akış–yoğunluk eğrisi) canlı çizmek.

### S7 · 2:35,2 – 2:54,8 (19,6 sn) · Tetikleyiciler
- **Anlatım:** "A car joining from a slip road. A hill… Somebody changing lane…"
- **Öğeler:** S1'deki S-eğrili otoyol (sakin, kırmızısız) — **açılış kompozisyonuna geri dönüş** · 2:37–2:39 yol üzerinde 1→3 beyaz kontur halka (aday tetik noktaları) · 2:40 / 2:42 / 2:44 üç dikey panel **soldan sağa sırayla** belirir (her biri ~%14W × %60H, x≈%3/%20/%37... ölçekte yan yana): "A CAR JOINS" (rampa birleşmesi), "A HILL" (kamyon), "A LANE CHANGE" · 2:49 üst orta "A QUIET ROAD: NOTHING HAPPENS" (beyaz) · 2:52 "NEAR THE TIPPING POINT: A JAM" (kırmızı) · 2:53 üç panelin etrafında kırmızı kontur yanıp sönmesi + panellerde kırmızı glow.
- **Amaç:** Soyut koşulu gerçek yollara bağlamak; 3'lü karşılaştırma.

### S8 · 2:54,8 – 3:28,7 (33,9 sn) · "Yan şerit hep daha hızlı" illüzyonu
- **Öğeler:** İki şeritli yatay yol (y≈%30) · kehribar "sen" arabası alt şeritte, ince kehribar halka + arkasında hız çizgileri · 2:58 "THE NEXT LANE" (sol üst, yolun üstü) · 3:01 sağ üstte "REDELMEIER AND TIBSHIRANI, 1999" · 3:04 "IT ONLY LOOKS FASTER" (kehribar, sağ) · 3:05 "MOVING: SPREAD OUT" · 3:07 "SLOW: BUNCHED UP" · **3:08 alt-orta lacivert panel** (x %35–77, y %62–90): pasta zamanlayıcı + "YOU PASS FOUR CARS" + beyaz ilerleme çubuğu → **2,8 S** (3:08–3:12) · 3:14–3:24 ikinci satır "FOUR CARS PASS YOU" kehribar çubuk → **8,7 S** · 3:19 "BOTH LANES: THE SAME AVERAGE SPEED" · 3:25–3:28 şerit değiştirme sonrası arkada kırmızı fren taplari + dalga halkaları.
- **Amaç:** İzleyicinin kendi davranışını sorgulatmak (kişisel bağ).

### S9 · 3:28,7 – 4:05,6 (36,9 sn) · "FOUR RULES" (Nagel–Schreckenberg)
- **Öğeler:** Hücrelere bölünmüş ızgara yol (y≈%38, x %2–98, düşük kontrast) · küçük araçlar · sağ üst "NAGEL AND SCHRECKENBERG, 1992" · kural kartları (lacivert, ince kenarlıklı, ~%12W×%7H) soldan sağa: **1 »»»** (3:37), **2 ■|—|■** (3:40), **3 göz** (3:45), **4 →** (3:49) · konuşulan kural kartı **kehribar kenarlık + kehribar rakam** ile vurgulanır (2 @3:43, 3 @3:51) · 3:55 kart 3 altında "THE HUMAN ONE" · **3:56 yolun altında aşağı doğru büyüyen zaman-uzay ızgarası** (her satır bir zaman adımı; kırmızı kümeler sola-aşağı çapraz = geriye akan sıkışmalar) · 3:59 "← THE JAMS" kırmızı · **4:02 kart 3'ün üzerine kırmızı çapraz çizgi çizilir** (kural kaldırıldı) · 4:05 "NO JAMS".
- **Amaç:** Basit kurallar → karmaşık davranış; "insan faktörü"nü izole etmek.

### S10 · 4:05,6 – 4:31,7 (26,1 sn) · "WHY IT LASTS"
- **Öğeler:** 3 şeritli sıkışık yol (y≈%47) · 4:10 "JOINING: AT ONCE →" (sol) · 4:14 kırmızı dikdörtgen · 4:17 "LEAVING: ONE BY ONE →" (sağ) · ön taraftaki araçların üstünde dolan pasta zamanlayıcılar (tereddüt) · 4:21 alt panel 3 bar: "WHAT GETS OUT OF THE JAM" (kırmızı, ~%60), "WHAT A CLEAR ROAD CAN CARRY" (beyaz, ~%100), "WHAT IS ARRIVING NOW" (kehribar, 4:23'ten itibaren azalarak ~%60'a).
- **Amaç:** Asimetri (durmak hızlı, kalkmak yavaş).

### S11 · 4:31,7 – 4:54,8 (23,1 sn) · "BUILD ANOTHER LANE?"
- **Öğeler:** Sıkışık yol (y≈%20) · 4:36 yolun altına yeni şerit (kehribar kesik çizgi + "THE NEW LANE") · 4:37 alt-orta panel: "LANE MILES" beyaz bar büyür · 4:41 "MILES DRIVEN" kehribar bar büyür · 4:46 "+10%" · 4:48 ikinci "+10%" · 4:51 "EASIER, SO MORE PEOPLE DRIVE" (yolun üstü) · 4:53 "JUST AS FULL AS BEFORE" (kırmızı).
- **Amaç:** Sezgisel çözümü çürütmek (indüklenmiş talep).

### S12 · 4:54,8 – 5:10,9 (16,1 sn) · "HOLD THEM BACK" (rampa ışığı)
- **Öğeler:** Üstte yatay ana yol (y≈%17) · sol alttan sağa kıvrılarak birleşen rampa · rampada kırmızı glow'lu kuyruk · rampa ağzında trafik ışığı (yeşil/kırmızı nokta, ~1,5 sn'de bir değişir) · 5:00 "ONE CAR AT A TIME" · 5:02 kesik dikdörtgen "A QUEUE ON THE SLIP ROAD" · 5:04 sağ üst/alt mini gösterge "HOW FULL THE MAIN ROAD IS" (beyaz bar + kehribar eşik çizgisi "TIPS HERE") · 5:08 "EVERYONE KEEPS MOVING".

### S13 · 5:10,9 – 5:31,8 (20,9 sn) · "SLOW DOWN EARLY" (değişken hız limiti)
- **Öğeler:** 3 şeritli yol (y≈%52) · 5:13'ten itibaren üç köprü gantry (dikey koyu çubuklar) + her şeritte dairesel hız tabelası **60 / 50** · ileride kırmızı küme · 5:20 kırmızı dikdörtgen · 5:23 "ARRIVING SLOWLY" · 5:25 alt panel: "SAFER" / "MORE CARS THROUGH"; 5:28 "SAFER" yanına kehribar ✓; 5:30 "MORE CARS THROUGH" yanına "?".
- **Amaç:** Kanıt dürüstlüğü (✓ ve ? ile görsel olarak).

### S14 · 5:31,8 – 5:57,8 (26,0 sn) · "ONE CAR" (Arizona 2018)
- **Öğeler:** Halka sola yerleşik (merkez x≈%30) · kırmızı dalgalar + halka dışında kırmızı yaylar · 5:38 "22 CARS, HUMAN DRIVERS" · 5:43 bir araç **kehribara döner** + "THIS ONE DRIVES ITSELF" (kehribar) + sağ üstte "▶▶" hızlandırma ikonu · 5:46–5:51 "8 → 10 → 12 → 13 → 14 → 15 KM/H, HELD STEADY" · 5:47 kehribar aracın önünde kesik kehribar yay (boşluk) · 5:50 "EASING OFF, NOT BRAKING" · 5:52 "NO WAVES" (büyük beyaz) — kırmızı yaylar kaybolur · 5:54 sağda lacivert panel "FUEL BURNED BY THE RING": yarım daire gösterge LESS–MORE, kehribar yay + ibre "MORE"dan ortaya/"LESS"e doğru döner (5:54–5:57).

### S15 · 5:57,8 – 6:23,9 (26,1 sn) · Adaptif hız sabitleyici
- **Öğeler:** Tek şeritli yol (y≈%62) · araçlar arasında sensör üçgenleri (araçtan öndekine uzanan ince açık üçgen) · 6:02 "NEW CARS, ON CRUISE CONTROL" (sol üst) · 6:08 araçların altında numaralar 7…1 (1 = en öndeki, sağda) · 6:09 "EVERY ONE BRAKED HARDER THAN THE CAR AHEAD" (kırmızı, sağ üst) · 6:12 "EACH CAR'S SPEED" + her aracın üstünde mini hız eğrisi (sparkline); çukur derinliği sola doğru artar · 6:14 "NOSE TO TAIL" · 6:16–6:18 çukurlar kehribar/kırmızıya döner · 6:19 sıfırlama · 6:21 "SET UP TO LEAVE A GAP" (beyaz) · 6:23 "TODAY: SET UP TO CLOSE IT" (kırmızı).

### S16 · 6:23,9 – 6:46,6 (22,7 sn) · "LEAVE A GAP" (izleyiciye görev)
- **Öğeler:** Yatay yol (y≈%55) · kehribar "sen" arabası + halka · 6:27 "THE GAP" (kehribar) + öndeki boşlukta kehribar kesik çizgi · 6:29 sağda "BRAKE LIGHTS AHEAD" (kırmızı) · 6:30 "OFF THE ACCELERATOR, EARLY" · 6:32 "17 KM/H, STILL ROLLING" (hız azalan sayaç, 6:39'da 14, 6:41'de 12…11) · 6:33–6:36 alt şeritte karşılaştırma aracı (kırmızı) "DRIVING UP TO IT, AND STOPPING" · 6:37 "THE QUEUE HAS GONE" · 6:43 sol üstte "A CLEAR ROAD BEHIND" + sola beyaz ok.

### S17 · 6:46,6 – 7:03,4 (16,8 sn) · Özet checklist
- **Öğeler:** Tam ekran lacivert zemin · ortada panel (x %5–90, y %10–90): 5 satır = boş kutu + etiket + sağda **o bölümün canlı mini simülasyonu** (şerit küçük resmi) · Kutular kehribar ✓ ile işaretlenir: IT'S A WAVE (6:49) · A BUSY ROAD, ONE TAP (6:50) · LATE AND TOO HARD (6:52–6:53) · QUICK TO STOP, SLOW TO START (6:56) · LEAVE A GAP (6:59) · 7:03 panel söner.
- **Amaç:** Hatırlanabilirlik; her satır anlatımdaki "So, a jam with no cause is a wave…" cümleleriyle birebir.

### S18 · 7:03,4 – 7:27,6 (24,2 sn) · Kapanış / bookend + abone CTA
- **Öğeler:** S1 ile **aynı S-eğrili otoyol, bu kez sakin, kırmızısız** · 7:06 sol üstte "SUBSCRIBE!" (H1 + kehribar alt çizgi) + altında "SCIENCE, EXPLAINED BY A SCIENTIST" · 7:09–7:12 kehribar araç görünür, etrafında genişleyen kehribar halka · 7:25–7:27 müzik söner (son 1,3 sn sessiz).
- **Amaç:** Görsel çözümleme: açılıştaki kırmızı kaos → kapanışta akan yol ("birisi 20 araba arkanda eve daha erken varacak").

---

## D. Varlık (Asset) Envanteri

| ID | Nesne | Stil / şekil | Renk | Tür [Ç] | Tekrar | Yeniden üretim |
|---|---|---|---|---|---|---|
| A01 | Araç (sedan) | Top-down yuvarlatılmış dikdörtgen, koyu ön/arka cam, ~2:1 oran | 5 renk varyantı | Vektör/SVG veya kod şekli | Tüm video | 1 SVG + renk parametresi |
| A02 | Fren glow'u | Aracın arkasında kırmızı çekirdek + geniş Gauss bulanıklık (radius ≈ 3–4 araç boyu) | #E8453C → saydam | Prosedürel (additive blur) | Her sahne | Kopya katmanı + blur + "add/screen" |
| A03 | "Sen" arabası | A01 kehribar + ince kehribar halka | #F0A848 | Vektör | S1, S8, S16, S18 | A01 varyantı |
| A04 | Kamyon | Uzun dikdörtgen, açık gri | Gri | Vektör | S7 | Basit şekil |
| A05 | Düz yol | Asfalt bant + 2 kenar + kesik şerit çizgileri | #2C3033 / #C8CDD2 | Vektör/kod | S3,S4,S8–S16 | Parametrik şerit sayısı |
| A06 | S-eğrili otoyol | Bezier yol, 2 taşıt yolu, orta ayırıcı | Aynı | Vektör (path) | S1, S7, S18 | 1 path + offset |
| A07 | Halka pist | Dairesel yol, dış çap ≈ %70–78H | Aynı | Vektör | S2, S6, S14, inset S4 | Daire + stroke |
| A08 | Rampa | Ana yola teğet birleşen eğri | Aynı | Vektör | S7, S12 | Bezier |
| A09 | Izgara (hücresel) yol | Hücre çizgili dar şerit | Soluk gri | Kod | S9 | Grid |
| A10 | Lacivert panel | Yuvarlatılmış dikdörtgen, ince kenarlık | #0B121E | UI | S5,S6,S8,S10,S11,S13,S14,S17 | 1 bileşen |
| A11 | İlerleme çubuğu | Koyu ray + yuvarlak uçlu dolgu | Beyaz/kehribar/kırmızı | UI | S8,S10,S11,S12 | 1 bileşen |
| A12 | Pasta zamanlayıcı | Beyaz daire, saat yönünde dolan dilim | Beyaz/kehribar | UI | S3, S8, S10 | Conic fill |
| A13 | Fren şiddeti çubuğu | İnce dikey kırmızı dikdörtgen + kesik zarf | Kırmızı/beyaz | Grafik | S3 | Bar + polyline |
| A14 | Çizgi grafik (eksenli) | İnce beyaz eksen + dikey/yatay etiket | Beyaz/kehribar | Grafik | S5, S6 | 1 bileşen |
| A15 | Gösterge (gauge) | Yarım daire, kehribar yay, ibre | Kehribar | UI | S14 | 1 bileşen |
| A16 | Vurgu halkası | İnce (~1,5 px) daire, genişleyip sönen | Kehribar/beyaz | Şekil | S1,S7,S8,S16,S18 | Stroke circle |
| A17 | Vurgu dikdörtgeni | Yuvarlatılmış kontur | Kırmızı / kesik beyaz ("WHERE IT WAS") | Şekil | S1,S4,S10,S12,S13 | 1 bileşen |
| A18 | Yön oku | İnce çizgi + küçük ok başı, etiketli | Beyaz/kırmızı | Şekil | S1,S4,S10,S16 | 1 bileşen |
| A19 | Yay ok | Halka dışında/içinde dairesel yay + ok başı | Kırmızı/beyaz | Şekil | S2,S6,S14 | Arc stroke + trim |
| A20 | Durum ikonları | Daire içinde çizgi ikon, üstü çizili | Beyaz | Vektör | S1 | Icon set |
| A21 | Kural kartları | Rakam + çizgi ikon (»», ■|■, göz, →) | Lacivert/kehribar vurgu | UI | S9 | Kart bileşeni |
| A22 | Gantry + hız tabelası | Dikey çubuk + kırmızı halkalı yuvarlak tabela | Kırmızı/beyaz | Vektör | S13 | Basit |
| A23 | Trafik ışığı | Tek parlak nokta (yeşil/kırmızı) | #3CD070 / kırmızı | Şekil | S12 | Daire + glow |
| A24 | Sensör üçgeni | Araçtan öne uzanan saydam üçgen | Beyaz %15 | Şekil | S15 | Polygon |
| A25 | Sparkline | Mini hız eğrisi | Beyaz→kehribar/kırmızı | Grafik | S15 | Path |
| A26 | Checklist satırı | Kutu + ✓ + etiket + canlı mini sim | Kehribar ✓ | UI | S17 | 1 bileşen |
| A27 | Arka plan dokusu | Düşük kontrast bulut gürültüsü | #121C19–#222B27 | Raster/prosedürel | Tüm "dünya" sahneleri | Fractal noise |

**Tekrar eden motifler:** halka (3 kez + inset), S-eğrili otoyol (açılış/orta/kapanış = 3 kez), lacivert panel (8 sahne), kehribar halka (5 sahne), "eski yer" kesik kontur.

---

## E. Animasyon Dökümü (Seçilmiş Ana Animasyonlar)

> Easing değerleri 10 fps ölçümle ancak kaba tahmin edilebilir; aşağıda "pratik yaklaşık" verilmiştir.

**E1 · Fren glow dalgası (tüm video)**
- Başlangıç: araç normal, glow yok.
- 1: Araç yavaşlar (simülasyon) → aynı karede kırmızı çekirdek + glow opaklığı 0→1 (~0,2–0,3 sn).
- 2: Arkadaki araç ~1 sn gecikmeyle aynı şeyi yapar; glow arkaya doğru "akar".
- 3: Araç hızlanınca glow ~0,5 sn'de söner.
- Son: Kümenin "kütlesi" yolun gerisine kaymış.
- Karakter: Glow opaklığı muhtemelen **frenleme/yavaşlık miktarına bağlı sürekli değişken** [Ç]; hareket fiziksel (eased değil, simülasyon).
- Teknik: Araç başına "brake" değeri → glow sprite opaklığı; additive blend.
- Güven: Yüksek (davranış), orta (eşleme fonksiyonu).

**E2 · Bölüm başlığı + alt çizgi**
- Başlangıç: görünmez. 1: Geçiş bittikten ~0,3–0,5 sn sonra metin + alt çizgi opaklık 0→1 (~0,3 sn). 2: Sahnenin ilk ~5–10 sn'si sabit kalır. 3: Söner (~0,3 sn) veya geçişle birlikte gider.
- Konum/ölçek değişimi 10 fps'de görülmedi [G] → saf opaklık; alt çizginin soldan sağa wipe olması mümkün **[B, düşük güven]**.

**E3 · Halka üzerindeki kırmızı yay (S2, S6, S14)**
- Başlangıç: yok. 1: Halka dış yarıçapının ~%8 dışında, kırmızı ince yay (stroke ~%0,8H) kısa parça olarak belirir. 2: Saat yönünün **tersine** uzar (S2'de 7 sn'de ~200°). 3: Ucunda ok başı. Yay, durmuş araçların açısal aralığını takip ediyor [Ç] → veri güdümlü.
- Teknik: `arc(startAngle(t), endAngle(t))` sim çıktısından; alternatif: trim path.

**E4 · Sayaç adımları (STOPPED, CARS, KM/H)**
- Başlangıç: sayı. 1: Değer **anında** değişir (aradaki sayılar akmıyor; 12→15→18 atlıyor) [G]. Adım ~1 sn.
- Teknik: Sim verisinden tamsayıya yuvarlanmış metin; tween yok.

**E5 · Fren şiddeti çubukları (S3)**
- Başlangıç: yükseklik 0. 1: Araç frenlediğinde çubuk yukarı büyür (~0,3–0,5 sn, ease-out görünümlü). 2: Bir sonraki çubuk daha uzun. 3: Kesik zarf çizgisi tepeleri birleştirir. 4: 1:14 zoom-out ile çubuklar yatayda sıkışır, yükseklikleri korunur.
- Güven: Orta.

**E6 · Pasta zamanlayıcı**
- Başlangıç: boş beyaz daire. 1: Saat yönünde dilim dolar (~1 sn, doğrusal). 2: Dolunca kaybolur/sıfırlanır. Narration'daki "about a second" ile birebir.

**E7 · Zaman–uzay diyagramı çizimi (S5)**
- 1: Panel opaklıkla belirir (~0,3 sn). 2: Noktalar sütun sütun soldan sağa eklenir (her sütun = bir fotoğraf). 3: 1:52'de noktalar birleşerek çizgilere dönüşür. 4: Durma bölgeleri kırmızıya döner. 5: 2:05 kırmızı dalga cephesi çizgisi sol üstten sağ alta "line draw" (~1 sn) ile çizilir.
- Teknik: Simülasyon kayıtlarından polyline; stroke trim/dash offset.

**E8 · Akış–yoğunluk eğrisi (S6)**
- Kehribar nokta veri noktası olarak ilerler; arkasında beyaz iz çizgisi kalır (2:26–2:31, ~5 sn). Düşüş kısmında gürültülü (titreşimli) iz [G] → gerçek ölçüm/sim gürültüsü. Tepe noktasından dikey kesik çizgi + kehribar etiket sonradan.

**E9 · Reframe: halka sola + panel sağa (2:24)**
- Halka merkezden sola ~%22W kayar ve hafif küçülür; panel sağda opaklıkla belirir. Süre ~0,5–1 sn, ease-in-out görünümlü [Ç, orta].

**E10 · Üç dikey panel (S7)**
- Her panel 2 sn arayla, soldan sağa belirir (opaklık; kayma görülmedi). Son aşamada üçüne aynı anda kırmızı kontur (~1 sn) → "hepsi aynı sonucu doğurur".

**E11 · Kural kartı vurgusu (S9)**
- Konuşulan kart: kenarlık gri→kehribar, rakam beyaz→kehribar (anında veya <0,2 sn). Kaldırma: kırmızı çapraz çizgi sol alttan sağ üste çizilir (~0,3 sn).

**E12 · Checklist (S17)**
- Satırlar baştan görünür (soluk), ✓ sırayla gelir; ✓ gelen satırın metni beyaza parlar. Her satırın mini simülasyonu sürekli canlı döngü.

**E13 · Vurgu halkası pulse (S1, S18)**
- İnce kehribar halka, aracın merkezinden ~%4H → ~%15H'e genişler, opaklık 1→0 (~0,8–1 sn, ease-out).

---

## F. Tipografi ve Metin Analizi

| # | Metin | Giriş–Çıkış (~) | Konum | Hiyerarşi / renk |
|---|---|---|---|---|
| 1 | YOU | 0:03–0:23 | Kehribar aracın üstü | H3 küçük, kehribar |
| 2 | THE JAM WITH NO CAUSE | 0:24,5–~0:30 | Sol üst | H1 + kehribar alt çizgi |
| 3 | 22 CARS | 0:29–0:52 | Halka merkezi | H0 gri |
| 4 | 230 M ROUND / ASKED TO HOLD 30 KM/H | 0:31 / 0:35 | Merkez alt satırlar | H3 gri-beyaz |
| 5 | ALL GOING ROUND | 0:38–0:44 | Halka içi üst, yay okun altında | H3 beyaz |
| 6 | NO JAM YET → 7…11 STOPPED | 0:41 → 0:47–0:52 | Merkez 4. satır | H2 beyaz → kırmızı |
| 7 | HOW HARD EACH DRIVER BRAKED | 1:02–1:20 | Sol üst (y≈%17) | H3 gri |
| 8 | STOPPED | 1:12–1:20 | Durmuş aracın altı | H3 kırmızı |
| 9 | IT MOVES BACKWARDS | 1:21–1:27 | Sol üst | H1 |
| 10 | JOINING → / LEAVING → | 1:24 / 1:25 | Yolun üstü | H3 beyaz + ok |
| 11 | THE ONES THAT WERE IN IT | 1:28–1:29 | Alt orta | H3 gri |
| 12 | THE CARS → / ← THE JAM / AROUND 20 KM/H | 1:31 / 1:31 / 1:32 | Yolun üstü / altı | H3 beyaz / kırmızı |
| 13 | WHERE IT WAS | 1:36–1:40 | Kesik konturun üstü | H3 kırmızı-soluk |
| 14 | SEEN FROM ABOVE → ONE PICTURE A SECOND | 1:42 / 1:46 | Sağ üst | H3 |
| 15 | DISTANCE ALONG THE ROAD / TIME → | 1:49– | Panel eksenleri | H4 |
| 16 | / MOVING, — STOPPED | 1:57 / 2:00 | Panel sol üst lejant | H3 beyaz / kırmızı |
| 17 | THROUGH CAR AFTER CAR | 2:08 | Kırmızı çizginin üstü | H3 kırmızı |
| 18 | THE TIPPING POINT | 2:10–2:15 | Sol üst | H1 |
| 19 | 12…23 CARS / THE TAP FADES / THE SAME TAP GROWS | 2:09–2:35 | Halka merkezi | H0 / H3 beyaz / H3 kırmızı |
| 20 | CARS GETTING THROUGH / HOW FULL THE ROAD IS / THE MOST IT CAN CARRY | 2:24– / 2:32 | Panel | H4 / H3 kehribar |
| 21 | A CAR JOINS / A HILL / A LANE CHANGE | 2:40 / 2:42 / 2:44 | Panellerin altı | H3 |
| 22 | A QUIET ROAD: NOTHING HAPPENS → NEAR THE TIPPING POINT: A JAM | 2:49 → 2:52 | Üst orta | H3 beyaz → kırmızı |
| 23 | THE NEXT LANE / IT ONLY LOOKS FASTER | 2:58 / 3:04 | Sol / sağ üst | H3 beyaz / kehribar |
| 24 | REDELMEIER AND TIBSHIRANI, 1999 | 3:01–3:28 | Sağ üst | H4 soluk |
| 25 | MOVING: SPREAD OUT / SLOW: BUNCHED UP | 3:05 / 3:07 | Yolun üstü/altı | H3 |
| 26 | YOU PASS FOUR CARS 2,8 S / FOUR CARS PASS YOU 8,7 S | 3:08 / 3:14 | Alt panel | H3 + sayısal değer sağda |
| 27 | BOTH LANES: THE SAME AVERAGE SPEED | 3:19 | Panelin üstü | H3 |
| 28 | FOUR RULES / NAGEL AND SCHRECKENBERG, 1992 | 3:29 / 3:32 | Sol üst / sağ üst | H1 / H4 |
| 29 | THE HUMAN ONE / ← THE JAMS / NO JAMS | 3:55 / 3:59 / 4:05 | Kart altı / ızgara altı / ızgara sağı | H3 kehribar / kırmızı / beyaz |
| 30 | WHY IT LASTS / JOINING: AT ONCE / LEAVING: ONE BY ONE | 4:07 / 4:10 / 4:17 | — | H1 / H3 |
| 31 | WHAT GETS OUT OF THE JAM / WHAT A CLEAR ROAD CAN CARRY / WHAT IS ARRIVING NOW | 4:21–4:23 | Alt panel | H4 kırmızı/beyaz/kehribar |
| 32 | BUILD ANOTHER LANE? / THE NEW LANE / LANE MILES / MILES DRIVEN / +10% | 4:32 / 4:36 / 4:37 / 4:41 / 4:46 | — | H1 / H3 kehribar / H4 |
| 33 | EASIER, SO MORE PEOPLE DRIVE / JUST AS FULL AS BEFORE | 4:51 / 4:53 | Yol üstü / altı | H3 beyaz / kırmızı |
| 34 | HOLD THEM BACK / ONE CAR AT A TIME / A QUEUE ON THE SLIP ROAD / HOW FULL THE MAIN ROAD IS – TIPS HERE / EVERYONE KEEPS MOVING | 4:55–5:10 | — | H1 / H3 / H4 |
| 35 | SLOW DOWN EARLY / ARRIVING SLOWLY / SAFER ✓ / MORE CARS THROUGH ? | 5:11 / 5:23 / 5:28 / 5:30 | — | H1 / H3 / panel |
| 36 | ONE CAR / 22 CARS, HUMAN DRIVERS / THIS ONE DRIVES ITSELF / 8…15 KM/H, HELD STEADY / EASING OFF, NOT BRAKING / NO WAVES / FUEL BURNED BY THE RING | 5:32–5:57 | — | H1 / H3 / kehribar / H2 |
| 37 | NEW CARS, ON CRUISE CONTROL / EVERY ONE BRAKED HARDER THAN THE CAR AHEAD / EACH CAR'S SPEED / NOSE TO TAIL / SET UP TO LEAVE A GAP / TODAY: SET UP TO CLOSE IT | 6:02–6:23 | — | H3 beyaz / kırmızı |
| 38 | LEAVE A GAP / THE GAP / BRAKE LIGHTS AHEAD / OFF THE ACCELERATOR, EARLY / 17…11 KM/H, STILL ROLLING / DRIVING UP TO IT, AND STOPPING / THE QUEUE HAS GONE / A CLEAR ROAD BEHIND | 6:25–6:46 | — | H1 / kehribar / kırmızı |
| 39 | Checklist 5 satır | 6:47–7:03 | Merkez panel | H2 beyaz |
| 40 | SUBSCRIBE! / SCIENCE, EXPLAINED BY A SCIENTIST | 7:06–7:27 | Sol üst | H1 / H3 |

**Metin animasyonu:** Kelime/harf bazlı animasyon, daktilo, kayma, ölçek **gözlenmedi**; tüm metinler **blok halinde opaklık fade** (~0,3 sn) [G, orta-yüksek güven]. Metin genellikle **anlatımla eşzamanlı veya ~0,2–0,5 sn sonra** geliyor; asla önce değil (istisna: sayaçlar anlık veri).
**Yeniden kullanılabilir kurallar:** (1) Başlık sadece bölüm başında, ~5–10 sn; (2) Etiket = isim cümlesi, ≤6 kelime; (3) Renk = anlam (kırmızı kötü, kehribar sen/çözüm); (4) Kaynak atfı her zaman sağ üst, en soluk; (5) Sayılar birimle birlikte ("17 KM/H", "2,8 S", "+10%").

---

## G. Geçiş Analizi

| # | Zaman | Çıkan → giren | Davranış (10 fps ile ölçüldü) |
|---|---|---|---|
| T1 | 0:23,6–0:24,3 | Otoyol → Halka | Çıkan sahne ~0,1 sn'de lacivert (#0B121E) tona söner; 1 kare lacivert; halka ~0,2 sn'de belirir; başlık +0,3–0,5 sn |
| T2 | 0:52,6–0:53,0 | Halka → tek şerit | Aynı; yol önce soluk/ince, ~0,2 sn'de tam |
| T3 | 1:20,0–1:20,7 | Çubuklar → 3 şerit | Aynı (0,4 sn tam lacivert kare görüldü) |
| T4 | 1:40,7–1:41,2 | Yatay yol → dikey yol | Aynı; **kamera dönüşü değil** |
| T5 | 2:08,6–2:09,4 | Diyagram → halka | Aynı |
| T6–T17 | 2:35,2 · 2:54,8 · 3:28,7 · 4:05,6 · 4:31,7 · 4:54,8 · 5:10,9 · 5:31,8 · 5:57,8 · 6:23,9 · 6:46,6 · 7:03,4 | — | Hepsi aynı reçete (şeritlerle doğrulandı) |

- **Tür:** "Dip to color" (renge söndürüp açma) — siyah değil, **panel laciverti**. Toplam ~0,4–0,7 sn [G].
- **Match cut / wipe / whip / morph:** Yok [G].
- **Sahne-içi "mikro geçişler":** opaklık fade'leri (etiket, panel), reframe (E9), zoom-out (1:14).
- **Anlatımla ilişki:** Dip'ler anlatımdaki paragraf/konu değişimine denk geliyor; ses tarafında 0,5–1,25 sn'lik konuşma araları (2:54, 4:54, 3:43 vb.) dip'lerle örtüşüyor [G: 174,0 s ve 294,0 s'de 1,0 sn'lik duraklar].

---

## H. Ses Tasarımı Analizi

- **VO:** Tek erkek(?) anlatıcı — cinsiyet ve aksan dinlenmeden doğrulanamaz **[B]**; transkriptteki "motorway, lorry, slip road" İngiliz İngilizcesi. Kelime hızı: 1.106 kelime / ~440 sn ≈ **151 kelime/dk** (sakin-orta tempo). Ortalama paragraf sonrası 0,5–1,25 sn duraklama (40 adet ≥0,5 sn).
- **Müzik:** G majör pentatonik, düşük seviyeli (konuşmanın ~18–20 dB altında), sürekli ambient yatak; kapanışta ~2,5 sn aralıklı seyrek notalar. Video boyunca bas/perküsyon izi yok [Ç].
- **SFX:** Ölçümde belirgin transient yok → SFX ya hiç yok ya da çok düşük **[B]**. Tüm "vurgu" görsel (glow, renk) ile yapılıyor.
- **Sessizlik vurgusu:** Gerçek sessizlik yok; vurgu VO duraklarıyla (müzik yatağı devam ederken) yapılıyor.
- **Kapanış:** 7:25,9'dan itibaren ses ~1,5 sn'de söner.

---

## I. Yeniden Kullanılabilir Görsel Sistem

### I1. Temel ilkeler (kopyalanabilir, jenerik)
1. **Tek sinyal rengi = tek kavram.** Videodaki her şey tek bir "kötü şey"in (kırmızı) uzay-zamandaki hareketiyle anlatılır.
2. **İzleyici avatarı = vurgu rengi.** "Sen" her zaman aynı renkte; çözüm de o renkte.
3. **Görüntü değil, katman ekle.** Sahne sabit kalır; her cümle bir etiket/ölçüm/vurgu ekler (2–4 sn ritmi).
4. **Veri güdümlü animasyon.** Yaylar, sayaçlar, çubuklar simülasyon verisinden; bu "gerçeklik" hissi verir.
5. **Analiz moduna geçiş = lacivert panel.** Dünya (dokulu yeşil) ↔ veri (düz lacivert) iki ayrı görsel dil.
6. **Tek tip geçiş.** Tüm bölüm geçişleri aynı → izleyici "yeni bölüm" kalıbını öğrenir.
7. **Kanıt atfı ekranda.** Her çalışma "SOYAD AND SOYAD, YIL" ile sağ üstte.
8. **Bookend.** Açılış kompozisyonu kapanışta "çözülmüş" hali ile döner.
9. **Kanıt dürüstlüğü görselleştirilir.** ✓ ve ? ikonlarıyla.

### I2. Kompozisyon şablonları
| Şablon | Tanım | Kullanıldığı sahneler |
|---|---|---|
| T-STRIP | Tam genişlikte yatay yol, y %45–62; üstü etiket, altı panel | S3, S4, S8, S10, S11, S13, S15, S16 |
| T-RING | Merkezde halka, merkezde dev sayı + 3–4 satır | S2, S6 |
| T-SPLIT | Solda sim (halka/yol), sağda lacivert grafik paneli | S5 (ayna), S6, S14 |
| T-TRIPTYCH | 3 dikey panel yan yana | S7 |
| T-CARDS | Üstte kural/öğe kartları, altta sim | S9 |
| T-HERO | Tam ekran manzara (S-eğri) | S1, S7 (giriş), S18 |
| T-CHECKLIST | Lacivert tam ekran özet | S17 |

### I3. Zamanlama kuralları
- Bölüm: 16–37 sn (ort. 25). Bölüm başı: dip (0,5 sn) → sahne → +0,4 sn başlık → başlık 5–10 sn sonra söner.
- Sahne içi olay: 2–4 sn'de bir. Sayaç adımı ≈ 1 sn.
- Etiketler anlatımdaki anahtar kelimeyle aynı anda veya ≤0,5 sn sonra.

### I4. Vurgulama kuralları
Önem sırası: kırmızı glow > kehribar renk değişimi > kontur/halka > beyaz etiket > gri etiket. Bir anda tek "sıcak" vurgu.

### I5. Tek seferlik yaratıcı kararlar (taklit edilmemeli)
Japon halka deneyinin halka görselleştirmesi, "22 CARS" merkez sayaç düzeni, S-eğrili otoyol bookend'i, "SCIENCE, EXPLAINED BY A SCIENTIST" sloganı, yeşilimsi bulut dokusu + lacivert + kırmızı/kehribar kombinasyonu, DIN-benzeri tüm büyük harf tipografi + kehribar alt çizgi imzası.

---

## J. Üretim Planı (Bu stilde bir video için)

> Özgün bir kanal için tam sistem ve örnek storyboard **03_ozgun_uretim_sistemi.md** dosyasında. Burada referans videonun üretim mantığının teknik planı var.

1. **Stil rehberi:** I bölümü + B6/B7 tablolarını bir "token" dosyasına çevir (renk, font boyutları, kenar boşlukları, geçiş süresi 0,5 sn).
2. **Storyboard / shot list:** C bölümü birebir shot list olarak kullanılabilir (18 sahne, olay zaman damgalarıyla).
3. **Varlık listesi:** D tablosu (27 varlık; çoğu parametrik bileşen).
4. **Animasyon listesi:** E1–E13.
5. **Tipografi:** F tablosu + kurallar.
6. **Geçişler:** Tek reçete (G).
7. **Ses:** VO ~150 kel/dk, −16 LUFS hedef; müzik yatağı konuşmanın 18–20 dB altında; SFX opsiyonel.
8. **Üretim yöntemi önerisi [Ç]:** Bu görsel, After Effects'te elle keyframe ile değil, **kod tabanlı** (ör. Remotion/React + SVG/Canvas, Motion Canvas, p5.js veya Python→render) bir trafik simülasyonu (IDM / Nagel-Schreckenberg) ile üretilmeye çok uygun. Simülasyon her kare için araç konum/hız/fren değeri üretir; UI katmanları bu veriye bağlanır.
9. **Şablonlar:** T-STRIP, T-RING, T-SPLIT, Panel, ProgressBar, PieTimer, Label, SectionTitle, DipTransition, HighlightRing, Checklist.
10. **Basitleştirilebilecekler:** Glow (tek blur katmanı), doku (tek statik görsel + yavaş kayma), araç çeşitliliği (3 renk yeter).
11. **Özgünleştirme için değiştirilmesi gerekenler:** I5'teki her şey + renk/tipografi/geçiş dili (bkz. 03).

---

## K. Belirsizlikler ve Sınırlar

| Konu | Durum |
|---|---|
| Orijinal çözünürlük | 640×360 kopya; küçük etiketlerin bir kısmı (≈5 px) bağlamdan okundu |
| Zaman damgaları | 1 fps → ±0,5 sn; geçişler 10 fps → ±0,1 sn |
| Easing eğrileri | 10 fps ile eğri şekli güvenilir ölçülemez; "fade ~0,3 sn" düzeyinde |
| Font adı | Tespit edilemez; DIN-benzeri grotesk tahmini |
| Yazılım | Bilinmiyor; kod tabanlı simülasyon olduğu güçlü çıkarım |
| SFX | Kulakla dinlenmedi; spektral ölçümde iz yok → [B] |
| Anlatıcı cinsiyeti/aksanı | Dinlenmedi → [B] (metin İngiliz İngilizcesi) |
| Arka plan dokusunun hareketi | 1 fps'de belirsiz |
| Transkript zamanları | NoteGPT parçaları ~25 sn'lik bloklar; cümle-kare eşleşmesi görsel olaylardan geriye doğru kuruldu |
