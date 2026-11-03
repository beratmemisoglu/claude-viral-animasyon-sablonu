# Görsel Sistem, Kurgu ve Ses

## İçindekiler
1. Değişmez ilkeler (iki modda da)
2. Stil modu `night-map`
3. Stil modu `transit-ink`
4. Kompozisyon şablonları
5. Ekran olayı türleri ve ritim
6. Tipografi kuralları
7. Geçişler
8. Kamera
9. Ses planı
10. Vuruş → şablon eşleme tablosu

---

## 1. Değişmez ilkeler
1. **Tek sinyal rengi = problem.** Kırmızı/turuncu gibi tek sıcak renk yalnızca problemi (dalga, gecikme, yığılma) gösterir. Bir karede tek sıcak vurgu.
2. **Tek vurgu rengi = izleyici + çözüm.** "Sen" avatarı ve doğru davranış hep aynı renk.
3. **Hareketi veri üretir.** Nesneler bir kural/simülasyonla hareket eder; yaylar, çubuklar, sayaçlar bu veriden okunur. Elle "güzel" hareket değil, tutarlı davranış.
4. **İki dünya:** "Dünya" (dokulu zemin + kuşbakışı sim) ve "Analiz" (düz panel + grafik). Panele geçmek = "şimdi ölçüyoruz".
5. **Sahneyi değiştirme, katman ekle.** Bölüm 16–37 sn; içinde her 2–4 sn yeni olay.
6. **Metin nesnenin yanında,** üstüne binmez; ≤6 kelime; birimli sayılar.
7. **Kanıt ekranda atıflı.**
8. **Bookend:** açılış kompozisyonu kapanışta "çözülmüş" haliyle döner.
9. **Dürüstlük görselleşir:** ✓ (kanıtlandı) ve ? (belirsiz).

## 2. `night-map` (varsayılan)
Referansın ilkeleri, kanala ait tokenlar. Referans değerleri bilgi için verildi; kanal paleti onlardan en az bir ton/doygunluk adımı farklı seçilmeli.

| Token | Referans (bilgi) | Önerilen kanal değeri | Rol |
|---|---|---|---|
| `bg` | #18221D yeşilimsi gri + bulut dokusu | #141A24 koyu arduvaz + ince gren | Dünya zemini |
| `panel` | #0B121E lacivert | #0E1622, 1 px #2B3646 kenar, 10 px radius | Analiz paneli |
| `asphalt/surface` | #2C3033 | #2A2F38 | Yol/hat/zemin nesnesi |
| `line` | #C8CDD2 | #C9D1DB %70 | Kenar çizgileri |
| `text` | #FFFFFF | #F4F6F8 | Birincil |
| `text-2` | #A3ACAC | #9AA6B5 | İkincil |
| `signal` | ≈#E8453C kırmızı glow | #FF4D3D veya konuya göre (ör. gecikme için #FF7A2F) | Problem |
| `accent` | ≈#F0A848 kehribar | #FFC247 sarı veya #36C5F0 camgöbeği | Sen/çözüm |
| `ok` | — | #4ADE80 (yalnız ✓/ışık) | Onay |

Tipografi: teknik grotesk, BÜYÜK HARF etiketler. Açık lisanslı seçenekler: **Barlow Semi Condensed / Barlow** (DIN hissine yakın), **Rajdhani**, **Saira Semi Condensed**. Başlık imzası: referanstaki "sol üst + kehribar alt çizgi" yerine kanal imzası seç — ör. başlığın solunda 6 px dikey vurgu çubuğu, ya da başlık önünde bölüm numarası "03 /".

Glow: sinyal nesnelerinde çekirdek + Gauss blur (yarıçap ≈ 3–4 nesne boyu), blend add/screen.

## 3. `transit-ink`
Krem kâğıt (#F2ECE0) + nokta ızgara, metro haritası soyutlaması, petrol (#138A7E) akış, hurma turuncusu (#E2552D) sinyal, kobalt (#2F55E0) sen/çözüm, fosforlu sarı (#F6D35B) başlık şeridi; Space Grotesk (başlık, cümle düzeni) + IBM Plex Mono (etiket, küçük harf + birim); pill etiketler + leader line; glow yerine stroke "nabzı" ve sert ofset gölge. Geçiş: tek büyük tuval üzerinde "map glide", perde arasında "sayfa çevir", detayda "mercek".

## 4. Kompozisyon şablonları
| Kod | Yerleşim | Ne için | Referans örneği |
|---|---|---|---|
| T-HERO | Tam ekran kuşbakışı manzara, sistem çapraz/eğri | Hook, bookend, "gerçek dünya" | S-eğrili otoyol (0:00, 2:35, 7:04) |
| T-STRIP | Tam genişlik yatay şerit y %45–62; üst etiket, alt panel | Mekanizma, karşılaştırma, davranış | Tek şerit fren zinciri, "leave a gap" |
| T-LOOP | Merkezde kapalı döngü (halka/çevrim), merkezde dev sayı + 3–4 satır | Kontrollü deney, devrilme noktası | Halka pist — **birebir kopyalama**: farklı geometri seç (oval, kare döngü, spiral, çizgi üstünde döngü sayacı) |
| T-SPLIT | Sol sim / sağ panel (veya tersi) | "Gör + ölç" | Halka + akış eğrisi |
| T-DIAGRAM | Büyük panel + yanında ince kaynak şeridi, kılavuz çizgilerle bağlı | Zaman-uzay, gerçek veri | Havadan fotoğraf → çizgi grafiği |
| T-TRIPTYCH | 3 dikey panel | Tetikleyiciler, 3'lü karşılaştırma | Rampa / tepe / şerit değişimi |
| T-CARDS | Üstte numaralı kural kartları, altta sim + aşağı büyüyen zaman ızgarası | Model kuralları | 4 kural |
| T-GAUGE | Sim + küçük gösterge paneli | Sonuç metriği (yakıt, süre, maliyet) | Yakıt göstergesi |
| T-CHECKLIST | Tam ekran panel, satır = kutu + etiket + canlı mini sim | Özet | 5 satırlık özet |

## 5. Ekran olayı türleri ve ritim
Her `> EKRAN:` satırı bunlardan biri olmalı (kategori adını satırda yaz):
`ETİKET` (metin belirir) · `SAYAÇ` (sayı adımlar) · `VURGU` (halka/kontur/renk değişimi) · `OK` (yön oku/yay) · `PANEL` (analiz paneli açılır) · `GRAFİK` (çizgi/çubuk çizilir) · `İKON` (ikon belirir/üstü çizilir) · `SİM` (simülasyonda olay: fren, ekleme, kural kaldırma) · `KAMERA` (reframe/zoom) · `GEÇİŞ`.

Ritim kuralları:
- Ortalama ≥1 olay / 4 sn; hook'ta ≥1 olay / 3 sn.
- Bölüm başlığı (ETİKET-H1) geçişten 0,3–0,5 sn sonra, 5–10 sn kalır.
- Etiket VO'daki anahtar kelimeyle aynı anda veya ≤0,5 sn sonra; asla önce (istisna: veri sayaçları).
- Aynı anda ≤5 metin öğesi.
- Sayaç adımı ~1 sn (night-map: anlık; transit-ink: tween).

## 6. Tipografi kuralları
| Seviye | Kullanım | Boyut @1080p |
|---|---|---|
| H1 | Bölüm başlığı (2–4 kelime, soru olabilir: "BUILD ANOTHER LANE?") | 40–56 px |
| H0 | Döngü/panel merkezinde dev sayı | 90–160 px |
| H2 | Durum ("NO WAVES", "8 STOPPED") | 24–36 px |
| H3 | Nesne etiketi (≤6 kelime) | 16–22 px |
| H4 | Kaynak atfı, eksen | 12–18 px |
Renk anlamı: beyaz nötr · sinyal rengi kötü/uyarı · vurgu rengi sen/çözüm · ikincil gri bağlam.

## 7. Geçişler
- `night-map`: Bölüm arası **renge dip** (kanal panel rengine): 0,12 sn söndür → 0,08 sn tam → 0,3 sn aç. Toplam ≈0,5 sn (30 fps'te 15 kare). VO'daki 0,5–1 sn paragraf durağına hizala.
- Bölüm içi: yalnız opaklık fade'leri, reframe (0,5 sn ease-in-out), zoom-out (1 sn).
- Sert kesme, whip, glitch, zoom-punch kullanma — formatın sakin "laboratuvar" tonunu bozar.
- `transit-ink`: map glide 0,9 sn / sayfa çevir 0,5+1,2+0,45 sn / mercek 0,6 sn.

## 8. Kamera
%90 statik. İzinli hareketler: reframe (nesneyi kenara al, panele yer aç), tek zoom-out (detaydan sisteme), bookend'de çok yavaş drift. Hareket hissi simülasyondan gelmeli.

## 9. Ses planı
| Katman | Referans (ölçüm) | Öneri |
|---|---|---|
| VO | Mono, ~151 kel/dk, sakin, İngiliz İngilizcesi metin | ElevenLabs/kendi ses, sakin uzman tonu, −16 LUFS |
| Müzik | Sürekli sakin ambient yatak, G majör pentatonik, VO'nun ~18–20 dB altında, perküsyonsuz, kapanışta seyrek ~2,5 sn'lik notalar | Majör, perküsyonsuz/çok hafif ambient piyano-pad; VO altında −20 dB; bölüm duraklarında +3 dB nefes; son 1,5 sn fade |
| SFX | Ölçümde belirgin iz yok (vurgular görsel) | Opsiyonel: çok düşük (−30 dB) yumuşak "tık" yalnız ✓ ve sayaç zirvelerinde |
| Sessizlik | Gerçek sessizlik yok | Aynı: müzik hiç kesilmez |

## 10. Vuruş → şablon eşleme (varsayılan)
| V | Şablon | Tipik olaylar |
|---|---|---|
| 1 Hook | T-HERO | SİM (sinyal geriye akar), İKON ×3 (üçlü red), VURGU (sen), OK |
| 2 Lab kanıtı | T-LOOP | ETİKET-H1, SAYAÇ, ETİKET ×3 (düzenek), OK (akış yönü), SİM (sinyal doğar), SAYAÇ (kaç durdu) |
| 3 Mekanizma | T-STRIP | SİM (ilk tap), İKON (tepki zamanlayıcısı), GRAFİK (artan çubuklar), ETİKET, KAMERA (zoom-out) |
| 4 Doğası | T-STRIP | ETİKET-H1, OK (giren/çıkan), VURGU (içindekiler), OK (sistem → / dalga ←), SAYAÇ (hız), inset (lab'ı hatırlat) |
| 5 Gerçek kanıt | T-DIAGRAM | ETİKET (yöntem), PANEL, GRAFİK (noktalar → çizgiler), ETİKET (lejant), GRAFİK (dalga cephesi) |
| 6 Koşul | T-LOOP → T-SPLIT | SAYAÇ (yoğunluk artar), ETİKET (söner/büyür), KAMERA (reframe), GRAFİK (eğri), ETİKET (tepe) |
| 7 Tetikleyiciler | T-HERO → T-TRIPTYCH | VURGU (aday noktalar), PANEL ×3 (stagger 2 sn), ETİKET (sakin: yok / dolu: var) |
| 8 Kişisel sapma | T-STRIP + alt panel | ETİKET, atıf, ilerleme çubukları (sen vs onlar), SİM (yeni dalga) |
| 9 Model | T-CARDS | Kart ×N (stagger), VURGU (insani kural), GRAFİK (zaman ızgarası), SİM (kural kaldırılır → çizik) |
| 10 Kalıcılık | T-STRIP + alt panel | ETİKET (giriş/çıkış), İKON (tereddüt zamanlayıcıları), GRAFİK (3 bar) |
| 11 Yanlış çözüm | T-STRIP + alt panel | SİM (yeni kapasite), GRAFİK (iki bar birlikte büyür), ETİKET (+%) |
| 12–14 Çözümler | T-STRIP / T-LOOP + T-GAUGE | Her çözüm: SİM + ETİKET + sonuç metriği; 13'te ✓/? |
| 15 Pürüz | T-STRIP | ETİKET (kırmızı bulgu), GRAFİK (mini eğriler büyür), ETİKET (olması gereken / bugün) |
| 16 Senin rolün | T-STRIP | VURGU (sen), ETİKET (boşluk), SAYAÇ (hız düşer ama durmaz), karşılaştırma ajanı, ETİKET (sonuç) |
| 17 Özet | T-CHECKLIST | ✓ ×5 (VO cümleleriyle) |
| 18 Kapanış | T-HERO (çözülmüş) | ETİKET (CTA), VURGU (sen) |
