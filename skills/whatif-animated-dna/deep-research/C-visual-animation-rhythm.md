# C — Görsel / animasyon / kurgu ritmi analizi ("What If" nişi, 11 video)

Kanıt: `scratchpad/whatif/ev/<id>/` (kontak sayfaları, `cuts.csv` scdet≥8, `silences.csv`, `loudness.txt`, `metrics.json`). Ara hesaplar: `scratchpad/whatif/C_work/quant.json`, `palette.json`. Video başına notlar: `C-video-notes/<id>.md` (11 dosya). İnceleme kapsamı: 5 hit'te (M_t2ZUz7_pc, jJCQG4Actqk, rvyd0ylInfY, rLCVK9llntQ, MGZdDZyQUGg 0–278 s) 4 fps intro sayfalarının tamamı ve 1 fps sayfaların tamamı/çoğu; DK4EOHCrVvM'de 0–332 s tam, sonrası örneklem; nOheMXyWXGg ve ggRf0ZYzrr8'de intro'nun ~%25'i ve 1 fps'in ~%8'i; 3 flop'ta intro'nun ~%20'si ve 2–3 sayfa (ayrıntı §10'da).

> **Heatmap uyarısı:** 11 videonun hiçbirinde YouTube "most replayed" verisi yok (`heatmap.json` = null; `yt-dlp -j` ile 28 Ekim'de yeniden denendi, yine null: videolar çok yeni ya da eşik altında). §7'deki "tekrar izlenen an" bulguları **yorumlardaki zaman damgaları + chapter'lar + görsel olay yoğunluğu** ile vekil olarak çıkarıldı. Güven düşük.

## 1. Özet (10 madde)
1. **Hit'lerde kesme hızı tek bir sihirli sayı değil:** 6.8–28.1 kesme/dk (medyan 15.8). Bu iki kanal ailesine ayrılıyor: (A) "hikâye-hızlı" 18–28/dk, medyan plan ≤3 s (ConChaser, Miko, Jeremy Bearimy, Iflord-Never Missed); (B) "anlatı-yavaş" 7–13/dk, plan 4.6–8.6 s, 30–55 s'lik uzun tutuşlar (Hour Seven, Iflord-Immortal, Ifsphere, Ifquirky). İkisi de çalışıyor; **aynı videoda tutarlılık** önemli.
2. **Karakter 0. saniyede.** 11/11 videoda kahraman ya da olayın kişisi ilk karede görünüyor (rLCVK9llntQ'da "sen" = kamera, first-person). Logo, intro animasyonu ya da kanal kartı yok.
3. **Güç görseli ilk 10 sn'de:** hit'lerde ilk güç görselinin medyanı ~3.5 s (Lie Count 1.0 s sayı flip'i, Hates 3.5 s aura, Never Missed 6–8 s kağıt top yayı, Future Wealth 8.25 s kafa-üstü $). Flop Tesla'da uçan araba 19.5 s'de, Days Left'te küçük kırmızı "1" 8.5 s'de geliyor ama okunmuyor.
4. **Başlık kartı en erken 16 s'de, çoğunlukla 29–35 s'de ya da hiç yok.** Cold open → başlık sırası: Lie Count 29 s, Immortal 32.75 s, Never Missed 34.5 s, Heart 47 s; Future Wealth ve Breathe'de başlık kartı yok; Hates'te başlık **finalde** (493 s).
5. **En güçlü güç tekniği: "kafa-üstü sayı + değişim anı".** Future Wealth'te koyu kutulu $ etiketi, Lie Count'ta kırmızı damga çerçeveli sayının son hanesinin flip'i (her yalanda +1). Sayının *değiştiği* an videonun punchline'ı oluyor (DK4E 309 s $64.8B→$4.2M; MGZd 224–238 s 22,780→22,784).
6. **Kafa-üstü etiket ancak güç "insanlar hakkında gizli bilgi" olunca işliyor.** Flop Tesla'da güç bir nesnenin yeteneği (uçan araba) olduğu için etiket sistemi yok; video ürün explainer'ına dönüyor (hız göstergesi, "49 HOURS" çubuğu).
7. **Aynı kanalın flop'u görsel olarak hit'iyle birebir aynı (aynı rig, sokak modülleri, palet).** Ölçülebilir farklar başka yerde: ConChaser flop'ta VO boşlukları sürenin %19'u (343 duraklama, ilk dakikada 24; hit'te 1) ve süre +%38. Miko flop'ta medyan plan 1.2 s ve ilk dakikada 39 kesme/dk (aşırı hızlı). Iflord flop'ta hook olaysız (bir yüz) ve arka planlar boş. **Görsel kalite gerekli ama yeterli değil.**
8. **Ekrana gömülü karaoke altyazı hiçbir hit'te yok.** Metin overlay'i *etiket* olarak kullanılıyor: sayaçlar, köşe zaman rozetleri ("DAY ONE — 6 P.M.", "YEAR 10"), karakter yanında pill, sarı vurgu kelimesi ("CLASSIC MARCUS.", "SWISH!"), konuşma balonu. Overlay yoğunluğu 4.8–13.5 olay/dk.
9. **Üç görsel rejimin dönüşümü standart:** (a) sahne (karakter + düz renkli set + DOF), (b) reaction yakın planı (bulanık fon, ifade 1 karede değişir), (c) lacivert infografik kart (grafik, sayaç, şema, kaynak satırı). 8 hit'in 8'inde (c) var; renk her kanalda lacivert-gece (#0d1623–#232b4b).
10. **Remotion + SVG ile yeniden kurulabilir seviye:** Hour Seven'ın low-poly 3D first-person stili hariç tüm stiller düz 2D vektör + blur/glow. Şablonlanabilir: rig, etiket, kalabalık, 6–8 set, infografik kart, kamera, geçişler. Tahmini üretim: 8–9 dk'lık video için 14–22 saat ilk sürüm, şablonlar oturunca 6–10 saat (§6.9). E ajanının `templates/remotion/` iskeleti bunun %55–60'ını karşılıyor; eksikler §6.10'da.

## 2. Nicel tablo (11 video)
Kesme = ffmpeg scdet skor≥8. Duraklama = ≥0.35 s sessizlik. Overlay sayısı = elle sayılan metin olayı (dk başına; yaklaşık). "Güç sn" = güç ilk kez görselleştirildiği an. Sahne = benzersiz set/arka plan (yaklaşık).

| Video (kanal) | Durum | Süre | Kesme/dk (ilk60/orta/son60) | Ort./medyan plan | En uzun tutuş | İlk 15 sn kesme | LUFS | Duraklama (toplam) | İlk karakter | İlk metin | İlk güç | Başlık kartı | Sahne | Overlay/dk | Stil |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M_t2ZUz7_pc Immortal (Iflord) | HIT 656K | 8:45 | 8.4 (16/7.7/5.0) | 7.1/5.5 s | 32.8 s @432 | 6 | -13.9 | 17 (14.6 s) | 0 s | 8.75 s CRASH! | 14.5 s (kalkış) / 44.5 s sayaç | 32.75 s (8.5 s) | ~40 | ~6.9 | 3D low-poly + 2D çubuk + infografik |
| rvyd0ylInfY Heart 10× (Jeremy Bearimy) | HIT 584K | 6:16 | 19.5 (20/19.7/18) | 3.1/2.5 s | 15 s @191 | 6 | -14.1 | 5 (2.2 s) | 0 s | ~9 s (50 m) | 24.75 s BPM saat | 47 s | ~24 | ~4.8 | kalın konturlu 2D, rim light, DOF |
| rLCVK9llntQ Immortal Snail (Hour Seven) | HIT 568K | 7:46 | 6.8 (6/7.6/3) | 8.6/5.0 s | 55 s @370 | 2 | -19.9 | 3 (12.8 s) | 0 s (POV) | 0 s HUD | 0 s HUD mesafe | yok (zarf kartı 4 s) | ~45 | ~11 (HUD+altyazı) | low-poly 3D first-person |
| DK4EOHCrVvM Future Wealth (ConChaser) | HIT 482K | 10:47 | **28.1** (26/28.7/25) | 2.1/1.7 s | 18 s @460 | 8 | -23.2 | 1 (1.3 s) | 0 s | 2.25 s $5 | 8.25 s kafa-üstü $ | yok | ~14 | **~13.5** | 2D çubuk-adam+, rim light |
| MGZdDZyQUGg Lie Count (Miko) | HIT 460K | 10:10 | 24.8 (24/25.5/20) | 2.4/2.2 s | **9.7 s** @422 | 5 | -14.2 | 6 (2.5 s) | 0 s | 0 s sayı | **1.0 s flip** | 29 s (kelime kelime) | ~22 | ~9.7 | sinematik 2D, volümetrik ışık |
| jJCQG4Actqk Never Missed (Iflord) | HIT 345K | 8:10 | 18.5 (18/19.4/13) | 3.2/3.0 s | 16.3 s @474 | 5 | -14.0 | 13 (13 s) | 0 s | 8.5 s SWISH! | 6–8 s yay / 26 s 50/50 | 34.5 s (2.75 s) | ~20 | ~8.6 | 2D çubuk + reaction + infografik |
| nOheMXyWXGg Secretly Hates (Ifquirky) | HIT 223K | 8:22 | 13.0 (12/13.2/13) | 4.6/3.9 s | 18.5 s @183 | 5 | -14.2 | 5 (2.2 s) | 0 s | 1.75 s "30 FACES" | 3.5 s aura | finalde (493 s) | ~15 | ~5–6 (örneklem) | kapsül-hoodie 2D, bloom |
| ggRf0ZYzrr8 Breathe Underwater (Ifsphere) | HIT 226K | 9:09 | 9.5 (12/9.1/10) | 6.2/4.8 s | 31.9 s @437 | 3 | -15.5 | 0 | 0 s | 2.25 s | ~3.5 s / 25.75 s kronometre | yok | ~15 | ~7 (örneklem) | kontursuz flat infografik |
| uVUDl0qUpXo Tesla Fly (Miko) | FLOP 23K | 4:56 | **32.0** (39/27.9/37) | 1.9/**1.2 s** | 12.2 s | **11** | -14.1 | 0 | 0 s | 16 s başlık | **19.5 s** (nesne) | 16 s | — | — | Miko ile aynı |
| 7jLDdD-uIEQ Control Electricity (Iflord) | FLOP 3.5K | 8:35 | 9.2 (10/9.6/6) | 6.4/3.8 s | 23.2 s | 4 | -14.1 | 11 (11.1 s) | 0 s | 32 s başlık | 32.5 s pil % | 32 s | az (düz fonlar) | — | 2D düz + infografik |
| L3PPO4MdLyY Days Left (ConChaser) | FLOP 12K | **14:55** | 23.6 (25/23.7/21) | 2.5/2.1 s | 16.8 s | 7 | -21.9 | **343 (173 s)** | 0 s | 8.5 s "1" | 8.5 s (küçük "1") | — | — | — | ConChaser ile aynı |

Ek ölçümler (1 fps karelerden, python; luma ve doygunluk 0–255; diff = ardışık kareler arası ortalama mutlak fark):

| Video | Luma ort. (sd) | Doygunluk | Koyu piksel oranı | Kare farkı ort. / %>40 | Baskın 5 renk |
|---|---|---|---|---|---|
| M_t2ZUz7_pc | 70 (57) | 145 | 0.50 | 12.2 / 9 % | #040409 #1a2544 #d8d4c4 #9b9c98 #9d6b44 |
| rvyd0ylInfY | 62 (20) | 106 | 0.31 | 18.4 / 12 % | #231e32 #4f3f53 #050408 #896e78 #bcb7c5 |
| rLCVK9llntQ | 81 (60) | 121 | 0.38 | 13.3 / 12 % | #010302 #aab3b2 #837d76 #4e4943 #1f1e22 |
| DK4EOHCrVvM | 100 (30) | **65** | 0.17 | 26.4 / **31 %** | #635d57 #898476 #c2bba7 #333538 #070707 |
| MGZdDZyQUGg | 60 (16) | 109 | 0.30 | 21.6 / 18 % | #261c32 #4c3b50 #040307 #7f6972 #c7b5b2 |
| jJCQG4Actqk | 91 (46) | 118 | 0.32 | 28.3 / 26 % | #070910 #b8c7c8 #343847 #6f898f #b0773f |
| nOheMXyWXGg | **119** (49) | 116 | 0.06 | 23.2 / 21 % | #232b4b #cdcec4 #797f7d #3e80ad #c97a57 |
| ggRf0ZYzrr8 | 94 (56) | 128 | 0.29 | 16.1 / 12 % | #0d1623 #3a85a9 #b5cad2 #334752 #9e9982 |
| uVUDl0qUpXo (F) | 69 (14) | 105 | 0.19 | 26.6 / 21 % | #554052 #302138 #87616e #030204 #c6b5b7 |
| 7jLDdD-uIEQ (F) | 67 (48) | 138 | 0.43 | 14.9 / 14 % | #020406 #0d152c #232e4a #6d706d #bdbaa7 |
| L3PPO4MdLyY (F) | 93 (33) | 68 | 0.20 | 22.8 / 20 % | #898175 #373436 #0a090b #615a57 #bdb8a9 |

Hit aralıkları: luma 60–119 (medyan ~85), doygunluk 65–145 (medyan ~117), kesme/dk 6.8–28.1 (medyan 15.8), ort. plan 2.1–8.6 s (medyan 3.9), LUFS -13.9…-23.2 (medyan -14.2; 5/8 hit -14±0.3, Ifsphere -15.5, Hour Seven -19.9, ConChaser -23.2), duraklama 0–17 (medyan 5).

## 3. Kanal başına görsel kimlik kartı (7 kanal)
Bunlar **tanımdır**; kopyalanmayacak. §6'daki rig onlardan farklı.

**Iflord** (M_t2ZUz7_pc, jJCQG4Actqk; flop 7jLDdD-uIEQ)
- Karakter: siyah daire kafa, ince siyah boyun, renkli hoodie (Immortal turuncu, Never Missed sarı) ve ipleri, çubuk uzuvlar, ellerde siyah top. Yüz: beyaz oval gözler + beyaz ağız. Kontur yok.
- Dönüşümlü 3 rejim: 3D low-poly sinematik açılış (vinyet, DOF, whip-pan) + 2D "sunucu" (bulanık fon önünde karakter konuşur) + lacivert radyal infografik (sarı vurgu, koyu kutulu beyaz caps).
- İmzalar: kademeli onomatope (CRASH!, SWISH!, BAM), sağ üst köşe rozeti ("YEAR 1", "DAY 1", "MONTH 3"), beyaz flaş + blur-in geçişi (~20 kez), sahte yorum kutusu CTA (Immortal 251 s), sonda "WOULD YOU…? / TELL US IN THE COMMENTS / SUBSCRIBE" (15 s).
- Palet: lacivert #1a2544 + siyah + bej #d8d4c4 + turuncu-kahve; doygunluk 118–145.

**Jeremy Bearimy** (rvyd0ylInfY)
- AE/Illustrator kalitesinde 2D: kalın koyu kontur (~4 px), yumuşak gradyan, rim light, partikül, DOF. Büyük leylak küre kafa, kapüşon, göğüste parlayan pembe kalp (güç sürekli görünür).
- Tek gece-moru palet (luma sd 20, en tutarlısı), vurgu pembe-kırmızı ve yeşil.
- Güç cihaz UI'ları üzerinden gösteriliyor: akıllı saat BPM, hastane monitörü, termometre, split-screen "NORMAL vs YOU".
- Overlay seyrek (~4.8/dk), geniş geometrik font; gazete manşeti gag'i; CTA iki seçenekli kart + sahte SUBSCRIBE imleci.

**Hour Seven** (rLCVK9llntQ)
- Low-poly 3D, first-person, karakter görünmüyor; tek doygun renk neon turkuaz (salyangoz).
- Kalıcı HUD: serif "Year 0, Day 1" + "SNAIL / 180.0 mi" (yakınken kırmızıya döner). Anlatım italik serif altyazı.
- Yavaş ritim (6.8/dk), uzun tutuşlar (55 s), 9 s tam siyah ekran, LUFS -19.9 (atmosferik). Ritmi kesme değil sayaç ve metin değişimi taşıyor.
- CTA: zarf + YES/NO düğmeleri, "Comment YES or NO."

**ConChaser** (DK4EOHCrVvM; flop L3PPO4MdLyY)
- 2D "çubuk adam+": siyah daire kafa, siyah ince gövde + renkli ceket/hoodie, kalın siyah kontur + krem rim light (tüm karakterlerde). Yüz beyaz ince çizgiler; varsayılan "meh" iki yatay çizgi göz.
- Düşük doygunluklu gri-bej dünya (sat 65), 4K, DOF, diyagonal ışık bandı; tekrar kullanılan vitrin modülleri (CRUMB & CO / VOLT / FIRST CITY BANK).
- En hızlı kurgu (28/dk): geniş → reaction → nesne insert → kart döngüsü.
- Kafa-üstü koyu kutulu $ etiketi; tonlar yeşil/pembe/gri/üstü çizili. Sol üst "SAAT · MEKÂN" etiketi. Cross-dissolve ile mekân geçişi.

**Miko** (MGZdDZyQUGg; flop uVUDl0qUpXo)
- En sinematik 2D: büyük beyaz-leylak daire kafa (gövdenin ~%45'i), kıvrık tek tel saç (kahraman), kalın mor kontur, amber rim light, volümetrik ışık, toz partikülü, yoğun DOF, OTS ön plan siluet.
- Mor-lacivert gece + amber lamba paleti (luma 60, sd 16).
- Kırmızı rubber-stamp çerçeveli sayı, son hane flip + glow; sayıya snap-zoom. Köşe rozeti "NINE DAYS AGO".
- Cold open → kelime kelime yazılan başlık (29 s) → flashback; kaynak/atıf satırı alt kenarda.

**Ifquirky** (nOheMXyWXGg)
- Kapsül gövde: siyah parlak küre kafa + specular highlight, iki beyaz göz (şekliyle duygu), kafaya geçirilmiş hoodie; kontur yok, bloom.
- En aydınlık palet (luma 119): krem + lacivert + mavi aura.
- Güç = renkli aura (mavi sever / gri umursamaz / kırmızı nefret), pulsing radyal glow + aynı renkte rim. Sayım pili ("30 FACES → 26 BLUE"). Başlık finalde.

**Ifsphere** (ggRf0ZYzrr8)
- Kontursuz, gölgesiz flat infografik (Kurzgesagt-lite): siyah daire kafa + diken saç tutamı, iki beyaz göz, renkli kapüşon gövde.
- Su teması (cyan+mavi %86).
- En sistematik metin katmanı: sol üst bağlam pill'i, üstte sarı caps konum, altta veri pill'i, diyalog balonu, sarı vurgu kelimesi. Final found-footage HUD ("HELMET CAM 02" + saat).

## 4. "Güç görselleştirme" kataloğu (12 teknik)

| # | Teknik | Nasıl yapılıyor (ölçü) | Uyduğu premise türü | Örnek (videoId @ sn) |
|---|---|---|---|---|
| 1 | **Kafa-üstü sayı etiketi** | Kafanın ~40 px üstünde koyu yuvarlak kutu (%90 opak), beyaz kalın rakam ~26 px @1080; 0.25 s scale-pop; karakterle hareket eder | "Herkesin X'ini görebilseydin" (servet, gün, yaş, puan) | DK4EOHCrVvM @8.25, 55.75, 110, 298 |
| 2 | **Damga sayaç + flip** | Kırmızı çift çerçeveli sayı (rubber-stamp); olay anında son hane flip + kırmızı glow 0.25 s; sayıya snap-zoom 1.5–3 s | Birikimli sayılar (yalan, günah, adım) | MGZdDZyQUGg @1.0, 139, 224–238, 154 |
| 3 | **Renk aurası** | Silüet arkasında radyal glow (blur ~40 px) + 2–3 px renkli rim; 3 kategori rengi; pulsing 0.5 s | Duygu/niyet okuma (sevgi/nefret, güven) | nOheMXyWXGg @3.5, 9–11, 22.5 |
| 4 | **Kalıcı HUD sayacı** | Sol üst serif metin + değer, her saniye güncellenir; tehlike yaklaşınca kırmızı | Kovalamaca, geri sayım, mesafe | rLCVK9llntQ @0–430, 41.75, 401–424 |
| 5 | **Köşe zaman rozeti** | Sağ/sol üst küçük çerçeveli caps ("YEAR 10", "DAY ONE — 6 P.M.") | Zaman atlayan anlatı (ölümsüzlük, X gün) | M_t2ZUz7_pc @154, 194; MGZdDZyQUGg @22.5, 37.5 |
| 6 | **Sayaç/kart dolumu** | Büyük glow rakam 0→N, 0.75–3 s ease-out; altında küçük letter-spaced açıklama | Ölçek şoku (servet, süre, olasılık) | DK4EOHCrVvM @35.5; M_t2ZUz7_pc @173–190 ($100→$3.9T), 302–309 |
| 7 | **"Normal vs SEN" karşılaştırma** | Split-screen ya da çubuk grafik; SEN çubuğu kadrajdan taşar / yeşil %100 | Fiziksel süper yetenek (kalp, isabet, ömür) | rvyd0ylInfY @41.75; jJCQG4Actqk @59–68; M_t2ZUz7_pc @130–139 |
| 8 | **Cihaz UI'ı** | Akıllı saat, monitör, telefon; değer sıçrar, eşikte ERROR + glitch | Biyolojik/teknolojik yetenek | rvyd0ylInfY @24.75, 154–165; jJCQG4Actqk @184–187 |
| 9 | **Hareket izi / yay** | Beyaz kesikli yay + iniş noktasında sarı halka + onomatope | Fiziksel kusursuzluk (isabet, hız) | jJCQG4Actqk @6–8, 13, 17 |
| 10 | **İlerleme ızgarası / tik dolumu** | 50 gri daire, 0.25 s'de 10 yeşil tik | Başarı sayısı, "her seferinde" | jJCQG4Actqk @26–34 |
| 11 | **Kronometre / gösterge** | Dolan pembe dilim, ibre; altta sarı caps sonuç | Süre limiti (nefes, pil) | ggRf0ZYzrr8 @25.75; 7jLDdD-uIEQ @32.5 (pil %, flop) |
| 12 | **Sayı değişimi = plot twist** | Etiket değeri ve tonu değişir (yeşil→pembe, büyük→küçük) | Gelecek / kader değişebilir | DK4EOHCrVvM @309, 619, 644; MGZdDZyQUGg @152 (kendi sayısı aynada) |

Kural: 1–3. teknikler (kişiye bağlı, sürekli görünür) en yüksek görüntülenen dört videonun üçünde var. Flop'larda güç ya nesnede (Tesla) ya soyut (pil %, şema) ya da küçük/kontrastsız (Days Left'te kutusuz kırmızı "1").

## 5. Kurgu ritmi spec'i
İki profil; video başında birini seç ve video boyunca koru.

| Parametre | Profil A "Hızlı hikâye" (ConChaser/Miko/Heart) | Profil B "Anlatı" (Iflord-Immortal/Hour Seven/Ifsphere) |
|---|---|---|
| Kesme/dk (genel) | 18–26 (hedef 22) | 8–13 (hedef 10) |
| Hook 0–15 s | 5–8 kesme | 3–6 kesme |
| Hook 0–60 s | 20–26/dk | 12–16/dk (Immortal 16) |
| Orta | 18–26/dk | 8–13/dk |
| Son 60 s | %15–30 yavaşla (Never Missed 19.4→13) | %30–60 yavaşla (Immortal 7.7→5) |
| Medyan plan | 1.7–3.0 s | 3.9–5.5 s |
| Maks. tutuş | ≤10–18 s (Lie Count hiç 10 s aşmıyor) | uzun tutuş serbest ama yalnızca "duygusal zirve"de (32–55 s), plan içinde sayaç ya da metin değişmeli |
| p90 plan | ≤5 s | ≤13 s |
| Üst sınır | **>30/dk ya da medyan <1.5 s yapma** (Tesla flop: 32/dk, medyan 1.2 s) | **10 s'den uzun planda en az bir olay olsun** (Electricity flop: 17 plan >10 s ve boş fon) |

- **Reaction döngüsü (A):** geniş 2 s → yakın reaction 1–2 s (ifade 1 karede pop) → insert 1–2 s → geniş/kart. Her 2–4 kesmede bir reaction.
- **Push-in:** varsayılan %1–2/sn (ölçülen yavaş push'lar Immortal 3D açılışında ~%8/sn, 6 s'de 1.6×; 2D sahnelerde %1–2/sn). Dramatik vurgu için snap-zoom: 0.25–0.5 s'de 1.0→1.6–2.5× (Lie Count sayıya zoom, Never Missed blur-in).
- **Ses:** LUFS -14 (±1) entegre; VO boşlukları toplam sürenin <%3'ü; ilk 60 s'de ≥0.35 s sessizlik ≤1 (ConChaser flop 24 adet). Kasıtlı sessizlik yalnızca zirvede (Immortal 6.2 s, Snail 7 s).
- **Süre:** hit'ler 6:16–10:47; flop'larda uçlar (4:56 ve 14:55). Hedef 7–10.5 dk.

## 6. Yeniden kurma spec'i (Remotion + SVG)
E ajanının iskeleti: `~/.claude/skills/whatif-animated-dna/templates/remotion/` (StickFigure.tsx, HeadLabel.tsx, Crowd.tsx, Caption.tsx, Scene*.tsx, WhatIfFilm.tsx, theme.ts). Aşağıdaki spec bileşen adlarıyla eşleştirildi; eksikler §6.10'da.

### 6.1 Özgün karakter rigi brief'i → `StickFigure.tsx`
Ayırt edicilik kuralı: kanallarda görülen dört kafa tipini kullanma (siyah daire kafa + beyaz göz; beyaz-leylak daire kafa + kıvrık saç; siyah parlak küre + hoodie başlık; leylak küre + kalp). Önerilen: **sıcak krem "yumurta" kafa** (dikey elips, rx 26 / ry 30) + **tek renkli bere ya da atkı** (kahraman = sinyal turuncu atkı; E iskeletinde `hero` atkısı var, uyumlu) + kısa dolgu gövde (yelek/ceket şekli, düz dolgu).
- Ölçüler (rig birimi, 1.25 ölçekte 1080p'de ~220 px boy): toplam boy 176; kafa 52×60 (boyun ~%32'si; hit'ler %30–45 arasında); gövde dolgusu boyundan kalçaya 42 px yükseklik × 34 genişlik, yuvarlatılmış yamuk; uzuv çizgisi 7 px (E: `stroke 7`, uygun); el = 9 px daire; kontur 3 px koyu mor-gri #2A2433 (hit'lerde 0–4 px).
- Işık: ışık kaynağı tarafında 2 px **sıcak rim** (#FFC98A, %70). Karakter görünen 7 hit'in 4–5'inde rim light var (ConChaser, Miko, Jeremy Bearimy, Ifquirky; Iflord kısmen), en ucuz "premium" etkisi bu.
- Renkler: kafa #F2E6D8, ink #2A2433, kahraman atkısı #FF6B35 (E theme `hero`), yan karakter gövdeleri pastel 8 renk havuzu.
- **8 poz** (E'de var: stand, walk, run, sit, point, phone, armsUp, slump). Ekle: `handOnHead` (şaşkınlık/facepalm, MGZd @135), `wave`, `reachOut` (uzatma/verme, MGZd @88–90), `lieDown` (düşme/uyku, ggRf @142). En az 8'i üretimde kullanılır: stand, walk, point, phone, armsUp, slump, handOnHead, reachOut.
- **6 ifade** (E'de: neutral, happy, sad, shocked, angry, worried). Ekle: `meh` (yarım kapalı göz; ConChaser'ın varsayılanı, en sık kullanılan reaction) ve `smug` (tek kaş, yan gülüş; Miko @26–27, Iflord @15). Göz kırpma: her 3–5 s'de 3 kare.
- Konuşma: ağız 2 kare (açık/kapalı) VO genliğiyle; reaction yakın planında ifade değişimi 1 karede (geçişsiz pop).

### 6.2 Kalabalık üreteci → `Crowd.tsx`
- Var: N figür, derinlik ölçeği, seed'li poz/etiket, yürüme. Hit'lerle uyumlu.
- Ekle: (a) `silhouette` katmanı: uzak sıra düz koyu (#1E1A26), yüzsüz, %70 opak, 6–10 px gauss blur (DK4E, MGZd sinema @63); (b) `grid` dizilimi (sınıf/salon: 5×6, Hates @1.75 "30 FACES"); (c) etiket gösterim sırası: soldan sağa 0.08 s arayla pop; (d) kategori sayım pill'i (üst-orta "30 YÜZ → 26 MAVİ").
- Sınır: kadrajda en fazla 30 figür, en fazla 8'i etiketli (okunurluk).

### 6.3 Kafa-üstü etiket → `HeadLabel.tsx`
- Var: number/text/icon, tonlar, sayma animasyonu, TR binlik ayırıcı, pop (back easing), bob.
- Spec: yükseklik 44 px @1080 (scale 1), font 30 px / 800 ağırlık, yatay padding 14 px, köşe yarıçapı 10 px (hit'lerdeki kutular hap değil hafif köşeli; E'deki tam yuvarlak hap da olur). Kafa üstünden boşluk 14–40 px.
- Ekle: (1) `variant: 'pill' | 'stamp' | 'aura'`. Stamp: çift çerçeve 3 px + iç 1.5 px, eğim -2°, kırmızı. Aura: etiket yok, silüet arkasına radyal glow r=1.6×boy, opaklık 0.35↔0.55, 0.5 s pulse; (2) `flipAt: number[]` ile değer değişiminde son hane dikey flip (6 kare) + 8 kare glow; (3) `strike: true` (üstü çizili, 2 px çizgi, DK4E @116); (4) `delta` rozeti (+1 / -7 YIL, sağ üstte küçük); (5) minimum okunurluk: geniş planda scale <0.55 olursa etiketi gizleme, 0.55'te sabitle (E'de var). Days Left flop'undaki kutusuz küçük rakam hatası böylece önlenir.

### 6.4 Altı sahne şablonu → `Scene*.tsx`
E'de: Street, Office, Home, School, Transit, Wedding. Hit'lerin kullandığı ağırlıklara göre öneri (her biri düz renk zemin + 3–5 prop + gece varyantı + DOF katmanı):
1. **Sokak** (`SceneStreet`, var): 3 vitrin modülü (tabelalar TR: FIRIN / ELEKTRONİK / BANKA) + bank + çöp kutusu + lamba. Hit'lerde en sık set.
2. **Ev / salon-mutfak** (`SceneHome`, var): kanepe, lamba, pencere (gece mor), mutfak tezgâhı alternatifi.
3. **Okul / sınıf** (`SceneSchool`, var): sıra ızgarası (kalabalık grid ile), tahta, renkli dolap bölmeleri.
4. **Kafe / restoran** (eksik, ekle `SceneCafe`): yuvarlak masa + mum + pencere bokeh + duvar aplik. DK4E @205–350 ve MGZd @213–247 bu sette uzun sahneler çekiyor.
5. **İş yeri / resmi mekân** (`SceneOffice`, var): masa, dosya, lamba (yeşil banker lambası MGZd'de kimlik ögesi).
6. **Lacivert infografik kart** (eksik ve en kritik, ekle `SceneInfoCard`): #141B33→#0B1022 radyal gradyan + hafif grid (opaklık 0.06) + bokeh daireler; slotlar: başlık (sarı caps), grafik (çubuk / çizgi / ızgara / kronometre / şema), kaynak satırı (alt sol, 14 px, %50 opak). 8/8 hit'te var.
- Transit ve Wedding'i ikinci öncelikte tut. Her sahne için `night` + `dusk` palet varyantı; arka plan blur seviyeleri 0 / 6 / 14 px (geniş / orta / yakın).

### 6.5 Kamera preset'leri → `WhatIfFilm.tsx` Camera
Var: static, push (rate %1.6/s), pull, pan. Ölçülen değerlerle:
| Preset | Değer | Kullanım |
|---|---|---|
| `pushSlow` | %1.0–1.5/s, ease yok | konuşma, geniş plan |
| `pushDrama` | %3–5/s, 2–4 s | kararlar, kötü haber (Immortal 3D açılış ~%8/s) |
| `snapZoom` (ekle) | 0.25–0.4 s'de 1.0→1.8× (etiket/sayıya origin), sonra %1/s | sayı flip'i, şok yüz (MGZd @1.75, 154) |
| `blurIn` (ekle) | 6 kare: blur 18→0 px + scale 1.06→1.0 | reaction'a geçiş (Iflord imzası, ~20 kez) |
| `whip` (ekle) | 6 kare yatay 400 px + motion blur | mekân/zaman atlama (Immortal @14, 165) |
| `shake` (ekle) | 4–6 px, 8 kare, sönümlü | darbe, CRASH (Immortal @10–14) |
| `ots` | ön planda karakter silüeti %40 kadraj, 14 px blur | diyalog (MGZd @0–9) |

### 6.6 Metin kartı spec'i → `Overlay` (WhatIfFilm.tsx)
Hit ölçümleri @1080p; font: geometrik bold sans, **Türkçe glif zorunlu** (E: Fredoka latin-ext; öneri: başlık/caps için Montserrat ExtraBold ya da Poppins Bold, ikisi de latin-ext).
| Tip | Boyut | Ağırlık | Konum | Süre | Renk |
|---|---|---|---|---|---|
| Başlık kartı | üst satır 34–40 px letter-spacing 0.15em + alt satır 96–120 px | 600 / 900 | orta-üst (sahne üstüne, karartmasız) | 2.5–4 s (Immortal'ın 8.5 s'si hit'ler arasında aykırı) | krem + vurgu kelime sinyal rengi |
| Vurgu kelimesi | 64–80 px caps + 4 px koyu gölge | 800 | alt-orta ya da karakter yanı | 1.0–1.5 s | sarı #F6C445 |
| Köşe zaman rozeti | 20–24 px caps, 1.5 px çerçeve | 700 | sol üst, SAFE.top 90 / side 96 | sahne boyunca | beyaz |
| Bağlam pill'i | 22–28 px | 700 | karakter yanı ya da alt-orta | 2–4 s | koyu %85 + beyaz |
| Sayı kartı | açıklama 22 px letter-spaced + rakam 120–160 px glow | 900 | tam ekran infografik | 1.5–3 s (sayma 0.75 s) | beyaz/yeşil/kırmızı glow |
| Konuşma balonu | 30–34 px sentence-case | 600 | konuşanın üstü | cümle süresi | beyaz kutu, koyu metin |
| Kaynak satırı | 13–15 px | 400 | alt sol | kartla birlikte | %50 beyaz |
- **Kelime-kelime karaoke altyazı (`Caption.tsx`) hit'lerde yok.** Varsayılanı `captions: 'off'` yap ya da yalnızca Shorts kesimlerinde aç. Uzun formda ekranı etiketlere bırak.
- Yoğunluk hedefi: 6–12 metin olayı/dk; her metin ekranda ≥1.0 s.

### 6.7 Palet önerisi → `theme.ts`
E'nin placeholder'ı açık kağıt (#F4EFE6). Hit'ler ise orta-karanlık (luma medyan ~85/255). Önerilen özgün palet (hiçbir kanalın paletiyle aynı değil): **"alacakaranlık zeytin-mürdüm"**:
- Zemin gündüz #CDBFA8 (kum) / alacakaranlık #4A3B4F (mürdüm) / gece #1F2233 (mürekkep laciverti).
- Işık #FFC98A (amber, rim ve lamba), gölge #2A2433.
- Sinyal (güç) rengi tek: **#2EE6C5 (nane-turkuaz)** iyi/artış, **#FF4D5E** tehlike/azalış; nötr etiket #2B2730.
- Infografik zemin #141B33→#0B1022.
- Hedef ölçüm (1 fps karelerde QA): ortalama luma 70–105, doygunluk 95–135, luma sd 15–50; kadrajda tek seferde en fazla 1 sinyal rengi.

### 6.8 Geçiş kuralları
1. Varsayılan sert kesme (her hit'te ≥%85).
2. Mekân değişimi: cross-dissolve 0.5 s (ConChaser) ya da sert kesme + köşe rozeti.
3. Güç tetiklenmesi / büyük şok: 1–2 kare beyaz flaş (Immortal @8.5, 24.5; Never Missed @34.25; Hates @3.25).
4. Reaction'a giriş: blurIn 6 kare.
5. Bölüm sonu / zaman atlama: dip-to-black 8+14 kare (E'de `dip` var).
6. Yasak: wipe, star wipe, 3D küp, glitch (yalnızca cihaz arızasında: Heart @157).

### 6.9 Prodüksiyon maliyet tahmini (8–9 dk video, Remotion + SVG)
| İş | İlk video | Şablon oturduktan sonra |
|---|---|---|
| Rig + 10 poz + 8 ifade + rim | 6–8 sa (tek sefer) | 0 |
| 6 sahne + gece varyantı | 8–12 sa (tek sefer) | 0–1 sa (1 yeni prop seti) |
| Shot list → shots.json (~150–250 shot, profil A) | 3–4 sa | 1.5–2 sa (LLM taslak + elle düzeltme) |
| Infografik kartlar (8–15 adet) | 3–5 sa | 1–2 sa (5 kart tipi şablon) |
| Kafa-üstü etiket / sayaç zamanlaması | 1–2 sa | 0.5 sa (VO zaman damgasından otomatik) |
| Render + QA (draft 0.5×, final) | 1–2 sa | 1 sa |
| **Toplam (video başına)** | **~14–22 sa** (+ tek seferlik 14–20 sa) | **~6–10 sa** |
- Şablonlanabilir öğeler: rig + poz/ifade, kalabalık, etiket (4 varyant), 6 sahne, 5 infografik kart (çubuk, çizgi, sayaç, ızgara, kronometre), köşe rozeti, başlık kartı, CTA kartı, 6 kamera preset'i, 5 geçiş.
- Elle kalanlar: konuya özel 3–6 prop (araba, kalp, hayvan), 1–2 gag animasyonu (kedi bardağı devirir: Hates @36–38; kağıt top yayı: Never Missed @6–8).
- Replike edilemeyen: Hour Seven low-poly 3D first-person (2D'ye çevir: POV + HUD + altyazı versiyonu yapılabilir).

### 6.10 E iskeletinde eksikler (birleştirme listesi)
| Bileşen | Var | Eksik / değiştir |
|---|---|---|
| StickFigure.tsx | 8 poz, 6 ifade, FK, hero atkısı, label bağlantısı | gövde dolgusu (hoodie/yelek; karakter görünen 7/7 hit dolgu gövde kullanıyor), rim light, `meh` ve `smug` ifadesi, göz kırpma, ağız flap, `handOnHead`/`reachOut`/`wave`/`lieDown` pozları, yakın plan modu (scale 3–5, kafa ayrıntısı), kafa şekli (elips) + bere/atkı aksesuar slotu |
| HeadLabel.tsx | pill, sayma, TR format, tonlar, ikon | `stamp`, `aura` varyantları, `flipAt` hane flip, `strike`, `delta` rozeti, köşeli (r=10) seçenek |
| Crowd.tsx | seed'li N figür, derinlik, etiket havuzu | silüet uzak sıra + blur, grid dizilimi, sıralı pop, kategori sayım pill'i, max etiket sınırı |
| Scene*.tsx | Street, Office, Home, School, Transit, Wedding | **SceneInfoCard** (kritik), SceneCafe, DOF blur katmanı (0/6/14 px), dusk varyantı, TR tabela metinleri |
| WhatIfFilm Camera | static/push/pull/pan | snapZoom, blurIn, whip, shake, ots |
| Overlay | card/title/lower/counter | köşe rozeti, vurgu kelimesi (sarı + gölge), konuşma balonu, sayı kartı (sayaçlı), kaynak satırı, damga ("YASAK", "YANLIŞ"), CTA kartı (soru + iki seçenek) |
| Caption.tsx | karaoke | uzun formda varsayılan `off` (hit'lerde yok) |
| theme.ts | açık kağıt palet | §6.7 paleti; `card` #111318 yerine infografik gradyanı |
| Geçişler | cut/dip/fade | flash (1–2 kare beyaz), crossDissolve 0.5 s, blurIn |
| QA | — | 1 fps luma/sat ölçümü + kesme/dk + maks. tutuş kontrolü (bu rapordaki `palette.py` / `quant.py` mantığı) |

## 7. Heatmap bulguları (vekil veri)
Gerçek "most replayed" eğrisi yok. Vekil: yorum zaman damgaları (11 videoda toplam ~40 adet; en çok 2'şer tekrar) + görsel olay yoğunluğu. Bu verilerle en çok anılan üç an türü:
1. **Güç kuralını kıran ya da ters çeviren gag**: Hates 0:37 ×2 (kırmızı aura kedi bardağı deviriyor), Heart 0:07 ×2 (bebek arabası, nabız saatinin ilk sıçraması).
2. **Ölçek/sayı şoku**: Immortal 6:47 ×2 (sahte yorum kutusu "milyar yılda tek anı?") ve 7:38 (evrenin sonu sayacı); Future Wealth 5:00 (etiketin $64.8B'den düşmesi ~309 s); Lie Count 4:19–4:20 (restoranda sayaç 22,78x tırmanıyor).
3. **Duygusal kırılma / twist**: Breathe 6:24 (nehir), Lie Count 2:35 (kendi sayısı aynada 14,003), Snail 3:53–4:55 (yıllar akıyor, aile).
Görsel karşılık: bu anların hepsinde **sayı/etiket ya da güç görseli ekranın merkezinde, 2–4 s tutulmuş ve snap-zoom ya da flash ile vurgulanmış.** Spec kuralı: her 60–90 s'de bir böyle "tekrar izlenebilir kare" planla (§8 kural 9).

## 8. Kopyalanacak kurallar (numaralı, ölçülebilir)
1. Kahramanı 0. saniyede, kadrajın ≥%15'inde göster; logo, kanal kartı ya da intro koyma.
2. Gücü ilk 10 s içinde görselleştir (hedef ≤5 s); ilk güç görseli kişiye bağlı olsun (etiket, aura, sayaç).
3. İlk 15 s'de profil A için 5–8, profil B için 3–6 kesme yap; 10'u geçme (Tesla flop 11).
4. Başlık kartını cold open'dan sonra 25–35 s arasında, en fazla 4 s göster ya da hiç gösterme.
5. Profil seç: A 18–26 kesme/dk (medyan plan 1.7–3 s) ya da B 8–13 kesme/dk (medyan 4–5.5 s). Videonun her dakikası seçilen aralıkta kalsın (dakika başına QA).
6. Hiçbir zaman >30 kesme/dk ya da medyan plan <1.5 s yapma.
7. 10 s'den uzun her planda en az bir değişim olsun (sayaç, metin, ifade, kamera hareketi).
8. Kafa-üstü etiketi ≥44 px yükseklikte, kontrastı ≥4.5:1 olan kutuda göster; tek haneli çıplak rakam kullanma.
9. Her 60–90 s'de bir "sayı/etiket değişim anı" planla: snap-zoom + flip/flash + 2–4 s tutuş.
10. Her 2–4 kesmede bir reaction yakın planı koy (bulanık fon, ifade 1 karede değişir).
11. Her 60–120 s'de bir lacivert infografik kart koy (grafik / sayaç / şema + kaynak satırı); toplamda 6–15 kart.
12. Uzun formda ekrana gömülü kelime-kelime altyazı kullanma; 6–12 metin etiketi/dk kullan.
13. Zamanı köşe rozetiyle göster ("GÜN 1", "3 YIL SONRA"); her zaman atlamasında güncelle.
14. Entegre ses -14 LUFS ±1; VO boşlukları sürenin <%3'ü; ilk 60 s'de ≥0.35 s sessizlik ≤1.
15. Kare ortalaması: luma 70–105, doygunluk 95–135; kadrajda tek sinyal rengi (güç rengi).
16. Sahne sayısı ≥14; tek sette ≥2 dk kalırsan açı değiştir (geniş / OTS / insert / yakın, en az 4 açı).
17. Son 10–16 s: soru kartı + iki seçenek ya da "yorumla" çağrısı + abone ol; yazıyı karakterin üstüne koy.
18. Geçişlerin ≥%85'i sert kesme; flaş yalnızca güç tetiklenince ya da büyük şokta, video başına ≤6.

## 9. Türkçe uyarlama notları
- **Kelime uzunluğu:** Türkçe caps metin İngilizceden ortalama %25–40 daha uzun ("NEVER MISSED" → "HİÇ ISKALAMASAYDIN"). Başlık alt satırında 96–120 px'te 1080p genişliğe ~16–18 karakter sığar (96 px kenar boşluklarıyla). Daha uzunsa iki satıra böl ya da 80 px'e in; vurgu kelimesini tek kelime seç ("ISKALAMAZ", "YALAN").
- **Glif:** İ, ı, ğ, ş, ç, ö, ü için latin-ext alt kümesi zorunlu (E `fonts.ts` doğru). Caps'te "i" → "İ" dönüşümünü `toLocaleUpperCase('tr-TR')` ile yap; JS'in varsayılan `toUpperCase()` "I" üretir (hata).
- **Sayı biçimi:** binlik nokta, ondalık virgül (E HeadLabel'da var: 22.784). Para: "₺" ya da "TL" sonda ("8,7 milyar TL"); etiket genişliği için kısaltma "8,7 Mr ₺" kullan, tam sayıyı sayı kartında ver.
- **Köşe rozetleri:** "GÜN 1", "1. YIL", "3 YIL SONRA", "GECE 23.00" (saat noktayla).
- **Onomatope:** "SWISH!" → "VIIN!", "CRASH!" → "GÜM!", "BAM" → "PAT!". Kısa, büyük harf.
- **Tabelalar:** sokak modüllerinde TR esnaf adları (FIRIN, ECZANE, BAKKAL, BANKA); marka ve gerçek isim kullanma.
- **Diyalog balonu:** sentence-case Türkçe, ≤7 kelime; Türkçe fiil sonda olduğundan vurgu kelimesini ayrı sarı kartla ver.
- **Rozet ve pill'ler** Türkçede daha geniş; pill genişliğini metinden ölç (E HeadLabel `label.length*fontSize*0.6` yaklaşımı; Türkçe büyük harfler için katsayıyı 0.66 al).

## 10. Açık sorular / düşük güven
- **Heatmap yok:** "Tekrar izlenen an" bölümü yorum damgalarıyla çıkarıldı (n küçük, 1–2 tekrar). 2–3 hafta sonra `yt-dlp -j` ile yeniden çekilmeli.
- **Örneklem derinliği:** Hates, Breathe ve 3 flop'ta 1 fps sayfaların yalnızca bir kısmı görüldü (Hates 4/56, Breathe 3/61, Days Left 3/100, Tesla 2/33, Electricity 2/58 sayfa; 4 fps intro'nun ~%20–25'i). Bu videolarda sahne ve overlay sayıları tahmindir.
- **Overlay sayımları elle yapıldı;** OCR ile doğrulanmadı (±%20).
- **Kesme eşiği:** scdet≥8; blur-in ve cross-dissolve geçişlerinin bir kısmı kaçmış olabilir (profil B'de gerçek kesme sayısı biraz daha yüksek olabilir).
- **Nedensellik:** Flop farkları (VO boşluğu, aşırı hız, nesne-güç, boş fonlar) korelasyondur; başlık/konu etkisi (A/B ajanlarının alanı) baskın olabilir.
- **Miko/Iflord flop'ları** farklı premise türleri (nesne / doğa gücü); aynı premise ile görsel A/B testi yok.
- **Önerilen palet ve rig** henüz render edilmedi; ilk 3 shot render'ında luma/doygunluk QA'sı yapılmalı.

## Diğer ajanlar için notlar
- **Başlık/paketleme ajanı:** Hates ve Breathe'de başlık metni videonun içinde başlık kartı olarak geçmiyor ya da finalde geçiyor (Hates @493). Lie Count başlığı kelime kelime yazıyor (29–31.5 s), "LIES" kırmızı damga kutusunda: thumbnail ile aynı görsel dil olabilir, A ajanı kontrol etsin.
- **Senaryo ajanı:** Hit'lerin 4'ü cold open + flashback ("NINE DAYS AGO", "YEARS AGO", Snail'in başa dönen sonu) kullanıyor. Hit'lerde güç "başkaları hakkında gizli sayı" ise ikinci perde twist'i sayının değişmesi (DK4E @309). Flop Electricity'de "NEVER TRY IT" ders tonu var.
- **Ses ajanı:** ConChaser flop'ta 343 VO duraklaması (173 s); hit'te 1. TTS segment birleştirmesinde boşluk kırpma kritik. Hour Seven -19.9 LUFS, ConChaser -23.2 LUFS ile de tuttu; normalizasyon hedefi -14 önerildi ama zorunlu değil.
