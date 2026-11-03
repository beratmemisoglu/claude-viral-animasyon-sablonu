# A — Paketleme / CTR analizi: "What If" animasyon nişi (başlık + thumbnail)

Veri: `dataset.csv` (10 kanal, 100 video, hit = ≥100K), 100 thumbnail (hepsi gözle incelendi + PIL ölçümü), 9 kanıt paketi `ev/<id>/raw/v.info.json` (açıklama, etiket, kategori, bölümler), 400'er üst yorum (thumbnail/başlık geçen yorumlar tarandı).
Ekler: `A-title-stats.csv` (100 satır: başlık etiketleri + thumbnail gözlem etiketleri + PIL metrikleri birleşik), `A-thumb-stats.csv` (PIL ham metrikleri, 3×3 kenar/luma ızgaraları).
Yöntem notu: Yayın tarihi 2026-10-27/28 olan 16 video (<2 gün) izlenme olarak olgunlaşmamış; oranlar aksi belirtilmedikçe **mature = yaş ≥2 gün, n=84, 26 hit (%31)** üzerinden. Tüm 100 video için hit oranı %27.

## Özet (10 madde)

1. **Başlık kalıbı tek başına kaderi belirlemiyor; "ne kadar somut + çift sonuç + sosyal risk" belirliyor.** Somut görüntü üreten başlık hit %40 (n=50) vs soyut %18 (n=34); "hediye gibi görünen lanet" (DUAL) hit %75 (n=8, medyan 190K) vs düz güç %26 (n=50, medyan 19K). Soyut + düz güç = %10 (n=21).
2. **En kötü aile = klasik süper güç** (fly, teleport, control X, invisible, clone, psychic): n=17 mature, hit %6, medyan 19K. Tek istisna Breathe Underwater 226K (somut + thumbnail'de çelişki: sakin oturan karakter vs boğulan dalgıç).
3. **En iyi aileler:** yenilmezlik (Immortal/Never Missed/No Pain: 3/4 hit, medyan 354K), oyun mekaniği (Respawn/Level Up/Creative Mode: 3/4, medyan 118K), "see everyone's gizli sosyal sayı" (5/10, tavan 482K; **ama sadece sayı aspirasyonel/sosyal ise** — ölüm sayacı versiyonları 12K–44K), adlandırılmış devasa sayı (googol/googolplex/Graham: 3/3).
4. **Sosyal × somut × tabu üçlüsü en yüksek hit oranı: %71 (n=7, medyan 166K)** — Lie Count, Crush, Secretly Hates, Future Wealth, Time Left. Aynı aileden flop'lar ya ölüm/keder (Days Left 12K, Timer 33K) ya da "başkalarının" bilgisi olup **sana dönmeyen** (Partners 23K, Really Thinks 3.9K).
5. **Kanal-içi doğal A/B'ler (aynı gün yüklenen çiftler, 26 çift) tutarlı:** kazanan taraf 22/26'da ya daha somut ya DUAL ya sosyal-tabu. En net: Crush "on **You**" 179K vs Partners "Everyone" 23K (7.8×, aynı gün, aynı şablon) → öz-ilgi (self-relevance) tek değişken.
6. **Thumbnail'de görsel çelişki (gülen yüz + "2 HOURS", evsiz + $8.7 milyar, "I love you" + 9,317 +1)** hit %56 (n=16, medyan 134K) vs çelişkisiz %25 (medyan 19.5K). Başlığı aynen tekrar eden metin (REPEAT) hit %22; **ikinci merak** açan (SECOND_HOOK) %43; metinsiz 0/3.
7. **Renk/parlaklık ikincil:** hit medyan luma 97 vs flop 76; siyah piksel oranı hit %13 vs flop %25. Tek sert kural: luma <30 veya siyah >%50 olan 4 thumbnail'in hepsi flop (Sank 7.8K, Black Hole 22K, Breath 5K, Vibrated 1.1K). Doygunluk, kenar yoğunluğu, kırmızı oranı hit'i ayırmıyor.
8. **Lansman etkisi devasa:** kanalın 1. videosu hit %60 (6/10, medyan 124K), 2–3. video %33, 4–8. video %19. 10 kanalın 7'si ilk 3 videoda hit aldı. Jeremy'nin ilk gün 4 videosu: 584K/364K/304K/18K. → Yeni kanalın ilk 3 başlığı en güçlü kalıplara ayrılmalı.
9. **Aynı başlık farklı kanalda 16× fark edebiliyor** ("10 Seconds Into the Future": Jeremy 304K lansman günü vs ConChaser 19K; "Same Day Forever": Iflord 114K, önceki video 656K vs Alternate You 8.7K, önceki video 7.4K). Başlık dışı pay (momentum + lansman + thumbnail) bu çiftlerde tahminen %70–80.
10. **Kadans:** en sık yükleyen kanal (Ifsphere 1.62 video/gün) en düşük hit oranına (%11) ve medyana (8.1K) sahip; 1.0/gün kanallar (Iflord, Readout, Ifquirky) %30–50. Süre 10–13 dk hit %56 (n=16), 6–8 dk %23 — süre B/C ajanının alanı, sadece not.

## 1. Başlık grameri (nicel)

### 1a. Kalıp aileleri (mature n=84; sıralama hit oranı)

| Aile | Örnek | n | hit | hit% | medyan | max |
|---|---|---|---|---|---|---|
| IMMORTAL | Were Immortal | 1 | 1 | 100% | 656K | 656K |
| MEME (tanıdık internet senaryosu) | Immortal Snail Chased You | 1 | 1 | 100% | 568K | 568K |
| EVERY_GIRL_GUY (herkes seni sevdi) | Every Girl on Earth Loved You | 2 | 2 | 100% | 156K | 191K |
| GAME_MECH (respawn/level up/creative) | Could Respawn | 4 | 3 | 75% | 119K | 158K |
| LIVED_N (adlandırılmış devasa sayı) | Lived a Googol Years | 3 | 2 | 67% | 128K | 252K |
| NEVER (never missed / no pain / never wait) | Never Missed | 4 | 2 | 50% | 195K | 364K |
| SEE_OTHERS (herkesin gizli X'ini gör) | See Everyone's Lie Count | 10 | 5 | 50% | 92K | 482K |
| COULDNT_STOP (X oldun ve duramadın) | Got Brighter and Couldn't Stop | 8 | 3 | 38% | 47K | 158K |
| TIME (10 sn gelecek / aynı gün) | See 10 Seconds Into the Future | 6 | 2 | 33% | 14K | 304K |
| MONEY | Infinite Money | 4 | 1 | 25% | 7K | 154K |
| WORLD_EVENT (dünya/çevre olayı) | Rained Acid and Didn't Stop | 6 | 1 | 17% | 7K | 126K |
| TENX (10x vücut fonksiyonu) | Heart Beat 10x Faster | 7 | 1 | 14% | 17K | 584K |
| SUPERPOWER (fly/teleport/control X) | Could Fly | 17 | 1 | 6% | 19K | 226K |
| ROLE (famous/president/law) | Became Famous | 3 | 0 | 0% | 18K | 71K |
| CURSE_BODY (aged 1yr/day, shrunk) | Shrunk 1cm Every Hour | 3 | 0 | 0% | 9K | 13K |
| OTHER | Hidden Survival Base | 5 | 1 | 20% | 5K | 145K |

**Orkestra şefi çapraz kontrolüyle uyum:** (i) "fiziksel güç n=21 hit %5 medyan 10K" ↔ benim SUPERPOWER tüm-100'de n=22 (Tesla dahil), mature n=17 hit %6 — uyumlu; medyan farkı <2 gün yaşındaki 5 flop'u (Electricity 3.5K, Swapped 1.2K vb.) dışarıda bırakmamdan. (ii) "INVULN n=4 hit %75 medyan 354K" = benim IMMORTAL(1) + NEVER'dan "Never Had to Wait" (30K) çıkarılmış hali; aynen doğrulanıyor (656/345/364 hit, Felt No Pain 45K flop). (iii) "oyun mekaniği n=6 %67" ↔ benim n=4 %75; şef muhtemelen Infinite Money ve/veya Go Back 1 Day'i de saydı — her iki tanımda da ≥%67. (iv) "see hidden social n=12 %42" ↔ benim n=10 (0 günlük Darkest Secret 15 izl. ve Search History 861 hariç) %50 = 5/12 → aynı. (v) "couldn't stop n=10 %40" ↔ benim COULDNT_STOP 8 + Snail (MEME'ye koydum) + 0 günlük Vibrated = 10, 4 hit = %40 → aynı. Fark sadece sınıflandırma sınırında; sonuçlar değişmiyor.

### 1b. Tek boyutlu etiketler (mature n=84)

| Boyut | Değer | n | hit% | medyan | Yorum |
|---|---|---|---|---|---|
| (b) Sosyal/fiziksel | S (başkaları hakkında) | 17 | **47%** | 71K | |
| | P (kendi bedeni/gücü) | 60 | 28% | 22K | |
| | W (dünya olayı) | 7 | 14% | 6K | "It rained/hailed" özne "You" değil |
| (c) Sayı | yok | 57 | 32% | 31K | |
| | rakam (10x, 1cm, 60 m, 500 IQ) | 20 | **10%** | 11K | sıradan rakam zarar veriyor |
| | adlandırılmış (googol, trillion, infinite) | 3 | 100% | 154K | |
| | "how many / count" | 3 | 67% | 166K | sayı değil, sayma *vaadi* |
| (d) Kelime | ≤6 | 18 | 33% | 24K | |
| | 7–8 | 31 | 35% | 44K | tatlı nokta |
| | 9–10 | 23 | 22% | 10K | |
| | 11+ | 12 | 33% | 22K | |
| (d) Karakter | ≤30 | 13 | 23% | 23K | |
| | 31–40 | 28 | **36%** | 33K | |
| | 41–50 | 29 | 28% | 19K | |
| | 51+ | 14 | 36% | 28K | |
| (e) "You" konumu | 3. token ("What If You…") | 77 | 30% | 22K | standart |
| | daha geç ("What If The Immortal Snail Chased **You**") | 4 | 50% | 135K | nesne konumunda "you" = tehdit |
| | yok ("It Rained Acid") | 3 | 33% | 6K | |
| (f) "IF" büyük harf | evet (Jeremy) | 9 | 44% | 24K | kanal etkisi; kanal içinde IF-caps 4/9 vs normal 4/9 → **etkisiz** |
| (g) Somut görüntü | evet | 50 | **40%** | 39K | |
| | hayır | 34 | 18% | 19K | |
| (h) Tabu/sosyal risk | evet | 13 | **46%** | 71K | |
| | hayır | 71 | 28% | 19K | |
| (i) Polarite | DUAL (hediye gibi lanet) | 8 | **75%** | 190K | |
| | CURSE | 26 | 27% | 24K | |
| | POW | 50 | 26% | 19K | |
| "couldn't/never stop" ibaresi | var | 9 | 44% | 60K | |
| "see/knew" fiili | var | 13 | 46% | 44K | |

Hit vs flop ortalamaları: kelime 8.15 vs 8.29, karakter 42.1 vs 41.0 → **uzunluk ayırt etmiyor**; somutluk 0.77 vs 0.52, tabu 0.23 vs 0.12 → ayırt ediyor.

### 1c. Kombinasyonlar (asıl sinyal)

| Kombinasyon | n | hit% | medyan |
|---|---|---|---|
| Sosyal + somut + tabu | 7 | **71%** | 166K |
| Fiziksel + somut + temiz | 34 | 38% | 36K |
| Sosyal + soyut (tabu olsun olmasın) | 9 | 22% | 14–44K |
| Fiziksel + soyut | 25 | 16% | 17K |
| Dünya olayı | 7 | 14% | 6K |
| Somut + DUAL | 4 | 75% | 242K |
| Soyut + DUAL | 4 | 75% | 190K |
| Somut + POW | 29 | 38% | 39K |
| Soyut + POW | 21 | **10%** | 10K |

Okuma: DUAL soyutluğu telafi ediyor (Immortal, Same Day Forever soyut ama DUAL → hit); POW ise somutluk olmadan ölüyor (Luck, Psychic, Teleport, Erase, Copy Skill).

## 2. Kanal-içi A/B (aynı kanal, aynı hafta)

Format: hit vs flop → fark eden tek değişken → mekanizma → güven.

**ConChaser (4 günlük kanal, 5 video)**
- Future Wealth 482K (3. video, 10-26) vs Days People Have Left 12K (1. gün, 10-24): İkisi de "See everyone's [sayı]". Fark: **valans** — zenginlik aspirasyonel ve ters-çevrilebilir (evsiz adam → $8,742,619,300), ölüm günü sadece keder (thumbnail: gülen anneanne + "1 DAY LEFT", konuşma balonu "See you in a week grandma!" = 8 kelime, okunmuyor). Mekanizma: *sosyal-sayı hit'leri izleyiciye "ben kaç olurdum?" oyunu vaat etmeli; ölüm sayacı oyunu değil yası vaat ediyor*. Ölüm sayacı ailesinin tamamı: 166K (Miko, lansman videosu), 44K, 33K, 12K → kanal lansmanı dışında hiç hit yok. Güven: yüksek.
- Crush on You 179K vs Partners Everyone Has Had 23K (aynı gün 10-27, aynı şablon: kafa üstü sayılar "0" vs "999+" / "0" vs "78"): Tek fark **başlığın yönü**: "on **You**" (öz-ilgi; izleyici kendi sayısını merak ediyor) vs "Everyone Has Had" (dedikodu; ayrıca cinsel içerik → reklam-dostu değil, önerilme kısılmış olabilir; thumbnail'de rahibe + "78" şakası izleyici tabanını da ikiye bölüyor). Mekanizma: *sosyal sayı → "you" nesnesi olmalı*. Güven: yüksek (aynı gün, 7.8×).
- 10 Seconds Future 19K: Aynı başlık Jeremy'de 304K. ConChaser versiyonu lansman günü, kırmızı hoodie'li **farklı protagonist** (kanal karakteri tutarsız), thumbnail'de silahlı adam düşünce balonu (tehdit, kullanım senaryosu yok); Jeremy'de rulet masası + "FUTURE VISION" (somut kazanç senaryosu). Başlık dışı pay: ≥%70 (lansman etkisi + thumbnail). Güven: orta.

**Miko (11 gün, 5 video)**
- Lie Count 460K / Time Left 166K (lansman) vs Erase Anything 21K / Tesla 23K / Think 10x 19K: Hit'ler sosyal-sayı; flop'lar kendi gücü. Thumbnail'ler: hit'lerde **ikinci kişi + kafa üstü sayı + yüz ifadesi çelişkisi** ("I love you" diyen kız + "9,317 +1"; gülen arkadaş + "2 HOURS"); flop'larda tek karakter güç demosu, metin = başlık tekrarı ("ERASE ANYTHING", "10X FASTER", "BYE, TRAFFIC!"). Tesla ayrıca 4:57, Think 10x 3:45 (kısa; süre ajanının alanı). Mekanizma: *sosyal sahne + çelişki*. Güven: yüksek. Not: Time Left 166K **lansman videosu**; aynı aile sonraki kanallarda 44K/33K/12K → bu hit'in ~yarısı lansman etkisi.

**Ifquirky (6 gün, 7 video)**
- Secretly Hates You 223K (lansman) / Last Girl Alive 120K vs Timer Above Head 33K / Dreams 26K / Go Back 1 Day 7.5K / Every Man Feared 6.5K: Hates = sosyal tabu + "you" + thumbnail'de POV eller ve 3 etiketli kişi (LIKES YOU / DOESN'T CARE / HATES YOU) + soru "WHO HATES ME?". Timer = ölüm sayacı (bkz. valans) + thumbnail "MOM?! 2 DAYS" ağlayan karakter (keder). Dreams = "Everyone could see **your**" (ters sosyal: utanç, izleyici kaçıyor; Ifsphere'in "Search History" 861 aynı ters yön). Every Man Feared/Every Woman Loved 6.5K: 13 kelime, iki fikir birden, ayrıca 1 gün yaşında. Mekanizma: *bilgi akışı sana doğru (sen görüyorsun) → hit; senden dışarı (herkes seni görüyor) → flop*. Güven: orta-yüksek (ters yön n=3, hepsi flop).

**Alternate You (13 gün, 12 video)**
- Googolplex + Best Friend 252K / Googol 128K vs Trillion 43K / Graham 41K (0 gün — hâlâ büyüyor) / Same Day Forever 8.7K / Aged 1 Year 13K: Thumbnail şablonu 12 videoda aynı (dikey bölünmüş önce/sonra + iki büyük yazı). Fark başlıkta: **adlandırılmış devasa sayı** (googol = bilinmeyen-ama-söylenebilir ölçek; "1 trilyon" hayal edilebilir, sıkıcı). Seri etkisi: Trillion 43K → Googol 128K → Googolplex 252K → Graham 41K/<24 saat: her bölüm bir öncekinin izleyicisini taşıyor (devam serisi momentumu). "+ Best Friend" eklemesi (sosyal öğe) 2× daha fazla. Same Day Forever 8.7K: Iflord'da 114K; AY'nin önceki 3 videosu 7.4K/13K/3.3K → momentum sıfır; thumbnail "DAY 1 / DAY 1 LOOP 2,101" doğru ama kanal ölü. Mekanizma: *isimli ölçek + seri eskalasyonu*. Güven: yüksek (sayı), orta (momentum payı).

**Jeremy Bearimy (14 gün, 22 video, 1.47/gün)**
- Every Girl 191K vs Every GUY 9.5K (ertesi gün): Hedef kitle erkek-genç (yorumlar, thumbnail'ler); "girl" = fantezi, "GUY" = thumbnail'de "I'M NOT GAY!" + panik → şaka olarak çerçevelenmiş, fantezi yok; ayrıca 1 günlük (Girl 2 günde 191K; GUY 1 günde 9.5K → yaş düzeltmesiyle de ~10×). Mekanizma: *cinsiyet hedefi = kitlenin arzusu; arzu yoksa merak da yok*. Güven: yüksek.
- Heart 10x 584K / No Pain 364K / 10 Seconds 304K (hepsi lansman günü 10-14) vs Control Water 10K / Firebending 19K / Clone 8.9K / Superpowers 5.2K: Lansman etkisi ilk üçü şişiriyor ama aynı gün "Became Famous" 18K → lansman tek başına yetmiyor; Heart/Pain = **vücut + DUAL** (10x kalp = hem hız hem ölüm; ağrısızlık = "this is fine.." meme'i + kanayan gülen yüz). Flop'ların 4'ünde thumbnail **metinsiz** (Water, Clone, Superpowers, Firebending) — kanalın metinsiz 5 thumbnail'inin 5'i flop. Mekanizma: *klasik element gücü (su/ateş) = çocukluk fantezisi, sonucu belli; DUAL = sonucu belirsiz*. Güven: yüksek.
- Respawn 158K / Infinite Money 154K (aynı gün) / Level Up 104K / Creative Mode 133K vs Psychic 24K (Level Up ile aynı gün, 4.3×) / Shrunk 8.5K (Creative ile aynı gün, 15.6×): Oyun mekaniği = oyuncu kitlesinin **in-group dili** ("/gamemode creative" komutu, LEVEL 10 stat paneli, RESPAWN). Psychic soyut. Güven: yüksek.

**Hour Seven (13 gün, 8 video, low-poly 3D, karaktersiz)**
- Immortal Snail 568K vs Sank 7.8K: Snail = **tanıdık meme** (internet "immortal snail" sorusu; açıklamada $10M + 0.03 mph matematiği) + somut görüntü (sokakta salyangoz, "100 m / It never stops."). Sank: thumbnail %70 siyah (luma 23.6, en karanlık 2. thumbnail), "YOU CAN'T STOP" + "10,935 m" okunmuyor, neye battığı belirsiz. Mekanizma: *meme tanınırlığı + görünürlük*. Güven: yüksek.
- Acid Rain 126K vs Hail 6.2K (1 gün arayla, aynı şablon): İkisi de "It X'd and Didn't Stop". Fark: **tehlike somutluğu** — "pH 1.5 / AS ACIDIC AS STOMACH ACID" vücuda ne olur sorusunu açıyor; "7.0 cm hail / baseball-sized" sadece hava durumu; Hail thumbnail'i beyaz-gri düşük kontrast. Not: Acid Rain kanalın 4. videosu, Hail 7. (momentum benzer). Güven: orta.
- Diğer flop'lar (Billionaire 1.1K, President 2.2K): thumbnail'de başlık aynen tekrar (12 ve 11 kelime serif), ROLE ailesi. Billionaire parlak mavi olmasına rağmen 1.1K → parlaklık kurtarmıyor.

**The Readout (10 gün, 11 video, fotoreal 3D, karaktersiz, editoryal serif)**
- Brighter 158K / Louder 144K / Garden Bigger Than Universe 104K vs Charged 17K / Vibrated 1.1K (0 gün) / Black Hole 22K / Breath 5K: Aynı şablon (küçük etiket + dev sayı + italik sonuç cümlesi). Hit'lerde sayı **gündelik birimle hissedilir** (1.8 trilyon lümen → "Night turns to day around you"; 176 dB → "Every window shatters."); flop'larda sayı soyut fizik (113 Earths, 1 billion volts, 13.8 billion years) ya da görüntü %62–64 siyah (Black Hole, Breath). Louder vs Charged: "louder" herkesin bedeninde deneyimlediği bir şey; "charged up" ne demek belirsiz (soyut). Mekanizma: *beden-ölçekli, hissedilir sonuç*. Güven: orta-yüksek.

**Iflord (7 gün, 8 video)**
- Immortal 656K (lansman) / Never Missed 345K / Same Day 114K vs Control Electricity 3.5K (0 gün) / Invisible 20K / Copy Skill 16K: Hit'ler DUAL/yenilmezlik; flop'lar klasik süper güç. Thumbnail şablonu aynı (2 kelime beyaz+sarı sol üst, karakter sağda, 1 nesne). Fark tamamen başlıkta + thumbnail metninde: "CAN'T DIE." / "NEVER MISS." (sonuç cümlesi) vs "HALF ME." / "ONE LOOK. COPIED." (anlaşılmaz). Açıklamalar en uzun ve SEO'lu (etiket listesi 20+, bölümler 20 adet; Film & Animation kategorisi) — diğer kanallar 0–5 etiket. Güven: yüksek.

**Ifsphere (12 gün, 21 video, 1.62/gün)**
- Hidden Secrets 140K / Breathe Underwater 226K vs Breathe in Space 39K / Fly 4.5K / Heal Anyone 8.8K / Really Thinks of You 3.9K: Underwater vs Space aynı fiil: "underwater" herkesin denediği şey (havuzda nefes tutma → somut, ulaşılabilir), "space" uzak. Thumbnail: Underwater'da çelişki (dalgıç boğuluyor, sen sakin oturuyorsun) güçlü; Space'te aynı çelişki daha karanlık (luma 44.7). "Really Thinks of You" 3.9K = SEE_OTHERS ailesinin karşı örneği: thumbnail "TRUE COLORS." + düşünce balonları (sayı yok, belirli kişi yok) ve kanal 4 gündür <10K'da (momentum ölü), ayrıca aynı gün 2. video. Mekanizma: *yakınlık (proximity) + kadans yorgunluğu*. Güven: orta.

**Başlık dışı faktör payı (aynı başlık, farklı kanal):**
| Başlık | Kanal A | Kanal B | Oran | Açıklama |
|---|---|---|---|---|
| See 10 Seconds Into the Future | Jeremy 304K (lansman günü, 3. hit) | ConChaser 19K (lansman günü, aynı gün Days Left ile) | 16× | Jeremy'nin aynı gün 4 videosundan 3'ü hit → kanal lansmanı çok güçlü; ConChaser lansmanı 2 flop'la başladı (Days Left 12K / 10 Sec 19K), 3. video 482K. Thumbnail: rulet (kazanç) vs silah (tehdit). |
| Same Day Forever | Iflord 114K (2. video; önceki 656K) | Alternate You 8.7K (7. video; önceki 7.4K) | 13× | Momentum farkı; thumbnail ikisinde de sayı var. |
Tahmin: bu çiftlerde varyansın %70–80'i başlık dışı (lansman/momentum ≈ %50, thumbnail ≈ %20–30). Güven: düşük-orta (n=2).

**Aynı gün aynı kanal 26 çiftin özeti:** kazanan tarafta somut/DUAL/sosyal-tabu niteliklerinden en az biri fazla olan çift sayısı 22/26; kalan 4 (Iflord No Pain 45K ≈ Knew Die 44K; Jeremy Respawn 158K ≈ Infinite Money 154K; Jeremy GUY 9.5K ≈ Clone 8.9K; Hour Seven Hail 6.2K vs Fish 4.3K) zaten eşit sayılabilir (<1.6×).

## 3. Thumbnail analizi (100 jpg; PIL ölçümü + gözle inceleme)

### 3a. PIL metrikleri — hit vs flop (mature n=84; hepsi 1280×720)

| Metrik | hit medyan | flop medyan | Yorum |
|---|---|---|---|
| luma ortalama | **97** | 76 | hit'ler daha aydınlık; çeyrek analizi: en karanlık çeyrek (<58) hit %18, en aydınlık (>123) %40 |
| luma p5 (gölge tabanı) | 10.5 | 3.0 | flop'larda tam siyah alanlar |
| siyah piksel oranı (luma<20) | **%13** | %25 | siyah >%50 olan 4 thumbnail'in 4'ü flop |
| beyaz piksel (luma>235) | %4.3 | %5.8 | fark yok; en beyaz thumbnail (9RyF, %35 beyaz, luma 191) 5.2K flop |
| doygunluk | 0.58 | 0.62 | fark yok; en doygun çeyrek hit %25 (en düşük) |
| colorfulness (Hasler) | 80.5 | 80.2 | fark yok |
| kenar yoğunluğu (metin/karmaşıklık proxy) | 0.045 | 0.044 | fark yok; en karmaşık çeyrek (>0.062) hit %20 → **kalabalık zarar veriyor** |
| kırmızı doygun piksel | %0.8 | %1.3 | en az kırmızı çeyrek hit %45 (!) — kırmızı vurgu şart değil |
| ten rengi alanı | %1.5 | %2.2 | karakterler siyah/beyaz yuvarlak kafa; yüz alanı ölçülemiyor |

Baskın renk 1: siyah (42 thumbnail, hit %26), mavi (28, hit %36), mor (4, 2 hit). Kanal medyan luma: Jeremy 134, Miko 129, Ifquirky 102, Alternate You 94, ConChaser 81, Readout 76, Iflord 68, Hour Seven 57, Ifsphere 56. **En karanlık iki kanal (Hour Seven, Ifsphere) en düşük medyan izlenmeye sahip (7K, 8.1K)**; ama aynı kanalların hit'leri de karanlık (Underwater luma 31.9 — en karanlık hit; Immortal 53) → luma kanal-içi hit'i açıklamıyor, kanal-arası tabanı açıklıyor. Sonuç: **renk/parlaklık bir kapı (gate), itici güç değil.**

### 3b. Gözle inceleme etiketleri (100 thumbnail; `A-title-stats.csv` → thumb_* sütunları)

| Etiket | Değer | n | hit% | medyan |
|---|---|---|---|---|
| Metin–başlık ilişkisi | SECOND_HOOK (yeni merak/çelişki/mikro-hikâye) | 21 | **43%** | 44K |
| | COMPLEMENT (başlığa sayı/ölçek ekler) | 33 | 33% | 17K |
| | REPEAT (başlığı tekrar eder) | 27 | 22% | 24K |
| | NONE (metin yok) | 3 | 0% | 10K |
| Görsel çelişki (gülen yüz + ölüm sayısı; evsiz + milyar; sakin + boğulan) | var | 16 | **56%** | 134K |
| | yok | 68 | 25% | 19.5K |
| Başlık somut + thumbnail çelişkili | | 11 | **64%** | 166K |
| Başlık soyut + çelişkisiz | | 29 | 14% | 18K |
| İkinci kişi/kalabalık | var | 37 | 32% | 39K |
| | yok | 47 | 30% | 19K |
| Sosyal başlık + ikinci kişi | | 16 | **50%** | 96K |
| Fiziksel başlık + ikinci kişi | | 19 | 21% | 39K |
| POV (öndeki eller/direksiyon) | var | 6 | 50% | 80K |
| Metin kelime sayısı | 0 | 3 | 0% | 10K |
| | 1–2 | 31 | 35% | 31K |
| | 3–4 | 19 | 26% | 30K |
| | 5–8 | 14 | 36% | 33K |
| | 9+ | 17 | 29% | 22K |
| Thumbnail'de sayı | var | 47 | 30% | 22K |
| | yok | 37 | 32% | 24K |
| Karakter stili | WHITE_ROUND (beyaz yuvarlak kafa, flat vektör — Jeremy/Miko) | 22 | **45%** | 51K |
| | LOWPOLY/fotoreal, karaktersiz (Hour Seven/Readout) | 18 | 28% | 28K |
| | STICK_BLACK (siyah yuvarlak kafa — Iflord/Ifsphere/Ifquirky/ConChaser/AY) | 43 | 23% | 13K |
| | COMIC (el çizimi — Survival) | 1 | 100% | 145K |

Yorumlardan kanıt (ev/ comments.json, 400 üst yorum): Never Missed'te "unskippable thumbnail", "The thumbnail got meme potential"; Future Wealth'te "do not use ai thumbnail" (AI-render görünümü eleştirisi, yine de 482K); Lie Count'ta "that thumbnail is just sad" (duygu üretmiş). Thumbnail yorumları hit'lerde var, flop'larda yok.

**"Thumbnail = başlığın görsel cevabı değil, ikinci merak" ilkesi — kanıt:** REPEAT %22 vs SECOND_HOOK %43 (2×), çelişkili %56 vs çelişkisiz %25 (2.2×). En iyi örnekler: Lie Count (başlık: yalan sayısı görmek → thumbnail: "I love you" diyen kız ve 9,317 **+1**: başlık soruyu, thumbnail "sevgilin de mi?" sorusunu açıyor); Future Wealth (başlık: zenginlik görmek → thumbnail: evsiz adamın üstünde $8.7 milyar: "nasıl?"); Secretly Hates (başlık → "WHO HATES ME?" + 3 etiketli kişi: izleyici kendi çevresini düşünüyor); Googol (başlık: googol yıl → thumbnail: "1 TRILLION YEARS 0%": "trilyon yıl hiç mi?"). Karşı örnekler: "ERASE ANYTHING", "10X FASTER", "PSYCHIC", "GO ANYWHERE", "SHAPESHIFT." → başlık tekrarı, hepsi flop. İstisna: Iflord "CAN'T DIE." / "NEVER MISS." teknik olarak tekrar ama **sonuç cümlesi** formunda (emir/kesinlik kipi) ve lansman momentumu var.

### 3c. Kanal şablonları (gözlem; ölçüler 1280×720'ye göre)

| Kanal | Karakter | Metin | Kompozisyon | "Güç" gösterimi | Palet | Not |
|---|---|---|---|---|---|---|
| Iflord | siyah yuvarlak kafa, turuncu hoodie, sağda %40 genişlik, göz hizası izleyiciye, sırıtış | 2 kelime, 2 satır (1. beyaz, 2. sarı), sol üst, ~%45 genişlik × %40 yükseklik, kalın sans + siyah dış çizgi | karakter sağ, nesne sol-orta (kurşun, basket potası, çalar saat) | tek fiziksel nesne + küçük kırmızı rozet ("DAY 300", "PAIN: 0%") | gece şehri bokeh, mor/lacivert; luma 53–87 | şablon 8/8 aynı; açıklama SEO çok yoğun |
| Ifsphere | siyah yuvarlak kafa, mor hoodie, sağ/orta | 2 kelime (1. beyaz, 2. mor), sol üst | karakter + ikinci figür (dalgıç, kedi, astronot) | ikinci figürün hâli karakterle çelişiyor | gece moru, en karanlık (luma 56) | 21 video aynı şablon; 2 hit |
| Ifquirky | siyah parlak küre kafa, hoodie, 3D render | 2–4 kelime soru/ünlem ("WHO HATES ME?", "MOM?!"), beyaz+renk | POV eller önde (hit'te), 3 kişi etiketli | kafa üstü etiket/sayı + aura rengi (mavi/gri/kırmızı) | sıcak gri/kırmızı aura | |
| ConChaser | siyah yüz, sarı hoodie, AI-render yarı gerçekçi şehir | **büyük başlık metni yok**; sadece kafa üstü sayılar (mavi = sen, yeşil/kırmızı = öteki) | sen sol, öteki sağ, ikisi de kafa üstü sayı | **sayı kontrastı** ($150 vs $8.7 mlr; 0 vs 999+) | gün ışığı, sıcak | metin yok ama sayılar metin işlevi görüyor |
| Miko | beyaz yuvarlak kafa (bukle), sarı hoodie, flat | 2 kelime tam genişlik üst bant (beyaz+sarı, ~%90 genişlik × %22 yükseklik) + kırmızı sayı rozeti | sen sağ, öteki sol, konuşma balonu | kafa üstü kırmızı sayı + ifade çelişkisi | doygun mor/mavi, en parlak 2. (129) | hit'lerde 2. kişi, flop'larda tek |
| Jeremy Bearimy | beyaz yuvarlak kafa, mavi hoodie, flat vektör | 1–3 kelime sarı/beyaz, üst bant (büyük harf veya küçük harf meme tonu "this is fine..", "oh yeah.") | karakter sol-orta büyük (%50+), kalabalık/nesne sağ | aksiyon anı (koşma, düşme, parada yatma) + oyun UI (stat paneli, komut satırı) | en parlak (134), mor/mavi/pembe | metinsiz 5 thumbnail → 5 flop |
| Alternate You | siyah kafa (tepede halka), mavi hoodie, 3D | 2 panel × 2–4 kelime, dev sarı/beyaz | **dikey ikiye bölünmüş önce/sonra** (sol %48 / sağ %52, zikzak çizgi) | sayı eskalasyonu (0% → 100%, YEAR 1 → 1 TRILLION) | sol sıcak, sağ soğuk | 12/12 aynı; hit = sayı ölçeği |
| Hour Seven | karakter yok; low-poly 3D sahne | serif editoryal: küçük etiket + dev sayı (kırmızı/beyaz) + italik cümle "It never stops." (6–11 kelime) | metin sol %45, sahne sağ | tek nesne (salyangoz, yağmur, dolu) | mat, çoğu karanlık (57) | 2 hit: meme + asit |
| The Readout | karakter yok; fotoreal 3D | serif: "YOUR LIGHT / 1.8 trillion / LUMENS · DAYLIGHT AT 2 A.M. / Night turns to day around you." (10–14 kelime) | metin sol üst %50, italik sonuç sol alt | sayı + hissedilir birim | mat, karanlık (76) | hit = gündelik birim |
| What If Survival | el çizimi komik figür | "OUTSIDE / INSIDE" + "FULL STORY" rozeti | dikey bölünmüş | dışarıda zombiler / içeride rahat | mavi-gri vs kahve | 1 video, 145K |

Ortak: **karakter yüzü = iki nokta göz + ağız; marka = hoodie rengi**; metin her zaman üstte; sağ alt köşe (süre rozeti) boş. Hit'lerin hiçbirinde 4'ten fazla görsel öğe yok (karakter, 1 öteki, 1 nesne, 1 metin bloğu).

## 4. Teslimatlar

### 4a. Kalıp aileleri — sıralı (bkz. §1a tablosu). Skill için öncelik sırası
1. Yenilmezlik / DUAL beden (immortal, never missed, no pain, heart 10x) — 4/5 hit, medyan 354K
2. "Herkesin gizli sosyal sayısını gör" — sayı aspirasyonel/ilişkisel ve "you"ya dönük (lie count, crush on you, who hates you, future wealth) — 5/7 hit, medyan 166K; **ölüm sayacı hariç** (1/4, o da lansman)
3. Oyun mekaniği gerçek hayatta (respawn, level up, creative mode) — 3/4, medyan 119K
4. Adlandırılmış devasa sayı serisi (trillion → googol → googolplex → Graham) — 3/4, seri eskalasyonu
5. Tanıdık meme senaryosu (immortal snail) — 1/1, 568K; "this is fine" thumbnail'i de meme
6. "Herkes seni sevdi" (hedef kitlenin arzu nesnesi) — 1/2 (karşı cinsiyet 191K, aynı cinsiyet 9.5K)
7. "X oldun ve duramadın" — yalnızca hissedilir gündelik X (brighter, louder, shrink) — 3/8
8. Zaman (10 sn gelecek, aynı gün) — 2/6; momentumla çalışıyor
9. Dünya olayı / rol / klasik süper güç / 10x soyut / para — **kaçın** (%0–17)

### 4b. Başlık mutasyon kuralları — flop'u hit'e çeviren 12 değişiklik (hepsi veri çiftinden)

| # | Kural | Flop → Hit örneği (gerçek veri) | Kanıt |
|---|---|---|---|
| 1 | **Bilginin yönünü sana çevir**: "see everyone's X" → "see how many X **on you** / who X **you**" | Partners Everyone Has Had 23K → Crush on You 179K (aynı gün) | 7.8× |
| 2 | **Ölüm sayacını ilişki sayacına çevir**: days left / timer → lie count / crush / hates | Days People Have Left 12K → Future Wealth 482K; Timer Above Head 33K → Secretly Hates 223K | 40×, 7× |
| 3 | **Ters yönü yasakla**: "Everyone could see **your** X" (utanç) → "**you** could see everyone's X" | Dreams 26K, Search History 861, Playing Along 1.7K vs Hidden Secrets 140K | 3/3 flop vs hit |
| 4 | **Hediyeye bedel ekle (DUAL)**: güç → sonucu belirsiz güç | Control Water 10K → Heart Beat 10x Faster 584K; Felt No Pain / Stopped Feeling Pain 364K | DUAL %75 vs POW %26 |
| 5 | **Klasik süper gücü oyun mekaniğine çevir**: psychic/teleport → respawn/level up/creative mode | Psychic 24K → Level Up 104K (aynı gün); Firebending 19K → Creative Mode 133K | 4.3×, 7× |
| 6 | **Sıradan rakamı adlandırılmış ölçeğe çevir**: 1 trillion → googol → googolplex | Trillion 43K → Googol 128K → Googolplex 252K | rakamlı başlık hit %10, adlandırılmış %100 |
| 7 | **Sayı değil sayma vaadi**: "10x", "1cm every hour" → "how many…", "…count" | Shrunk 1cm Every Hour 8.5K vs Lie Count 460K; "how many/count" 2/3 hit | |
| 8 | **Uzak ortamı yakın ortama çevir**: space → underwater; black hole → louder | Breathe in Space 39K → Breathe Underwater 226K; Black Hole 22K → Louder 144K | 5.8×, 6.5× |
| 9 | **Soyut sonucu hissedilir sonuca çevir** (Readout tipi): "charged up" → "brighter/louder" + thumbnail'de birim | Charged 17K → Brighter 158K | 9× |
| 10 | **Meme tanınırlığı ekle**: "X chased you" → "The Immortal Snail chased you" | Sank 7.8K → Immortal Snail 568K | 73× (karanlık thumbnail de etkili) |
| 11 | **Hedef kitlenin arzusuna hizala**: Every GUY → Every Girl (kitle genç erkek) | GUY 9.5K → Girl 191K | 20× |
| 12 | **Bir fikir, ≤8 kelime, "What If You" + fiil + somut nesne**: iki fikirli/13 kelimelik başlıkları böl | "Every Man Feared You and Every Woman Loved You" 6.5K; "Relive Any Day… As Many Times As You Wanted" 2.3K vs "Could Respawn?" 158K | 9–10 kelime hit %22 |
| + | **Sosyal öğe ekle**: "You lived X" → "You and your best friend lived X" | Googol 128K → Googolplex + Best Friend 252K | 2× |

### 4c. Başlık skor rubriği (0–10; skill bunu otomatik uygular)

| Kriter | Puan | Nasıl ölçülür |
|---|---|---|
| K1 Somut görüntü | 0 / 1 / 2 | 2: başlıktaki isim/fiil tek karede çizilebilir (snail, heart, lie count, respawn); 1: kısmen (immortal, future); 0: soyut (luck, psychic, erase anything) |
| K2 Polarite | 0 / 1 / 2 | 2: DUAL (hediye + bedel aynı anda sezilir: immortal, 10x heart, no pain); 1: CURSE somut (acid rain, couldn't stop); 0: düz POW |
| K3 Sosyal yön | 0 / 1 / 2 | 2: başkalarının gizli bilgisi **sana** akıyor + sayı/etiket ("how many… on you", "who… you", "everyone's count"); 1: sosyal ama sana dönmüyor / sen görülüyorsun (−1 uygula → 0); 0: sadece kendi bedenin |
| K4 Tabu/sosyal risk | 0 / 1 | 1: hates, crush, lie, secret, wealth; ölüm/keder sayacı = 0; cinsel (partners) = 0 (reklam/öneri riski) |
| K5 Tanıdıklık | 0 / 1 | 1: meme / oyun mekaniği / adlandırılmış ölçek / herkesin denediği şey (underwater) |
| K6 Biçim | 0 / 1 | 1: 6–8 kelime, 31–45 karakter, tek fikir, "What If You…" veya "What If [tehdit] … You", sıradan rakam yok (10x, 1cm, 60 m, 500 IQ → 0) |
| K7 Valans | 0 / 1 | 1: izleyici "ben olsam ne yapardım / benim sayım kaç" oyununu oynayabilir; 0: sadece keder/utanç (days left, dreams leaked) |
| **Toplam** | **0–10** | |

**Retrospektif doğrulama** (rubrik `A-title-stats.csv` etiket sütunlarından otomatik hesaplandı, `score` sütunu; mature n=84):

| Skor | n | hit | hit% | medyan |
|---|---|---|---|---|
| 7 | 3 | 3 | 100% | 191K |
| 6 | 4 | 4 | 100% | 238K |
| 5 | 14 | 9 | 64% | 149K |
| 4 | 22 | 7 | 32% | 41K |
| 1–3 | 41 | 3 | 7% | 10K |

Toplu: **≥5 → %72 hit (13/18, medyan 156K); 4 → %32; ≤3 → %7.** Eşik kuralı: **≥5 üretime girer; 4 yalnızca lansman veya seri momentumu varsa; ≤3 ret.** Otomatik puanlamada gözlenen aralık 1–7 (K-maksimum 10'a hiçbir başlık ulaşmıyor; 8+ teorik). Düşük puanla hit olan 10 başlığın 7'si lansman/seri videosu (Immortal 4 — 1. video; 10 Seconds 2 — lansman günü; Respawn/Level Up/Creative 4 — oyun mekaniği K5'te yalnız 1 puan alıyor → skill'de oyun mekaniği + yenilmezlik ailelerine **K5=2** ver, o zaman bunlar 5–6'ya çıkıyor). Yüksek puanla flop: Every GUY 7 (kitle cinsiyeti — K3'te "arzu nesnesi kitleye uyar mı" kontrolü manuel), Graham 6 (0 gün, 41K → hit olacak), Partners/Days Left 5 (K4/K7 cezaları manuel listeyle doğru işliyor ama K1/K3 puanları yüksek). Rubrik tek başına %72; lansman/momentum bilgisiyle birlikte kullanılmalı.

### 4d. 20 başlık şablonu (EN orijinal + TR uyarlama)

Türkçe sınır: **≤55 karakter, ≤8 kelime** (Türkçe ekler uzatır; YouTube mobilde ~50 karakter sonrası kesiyor). "Ya … olsaydı?" / "Ya … görebilseydin?" doğal; "What If" yerine "YA" büyük harf başlangıç (A/B önerisi). Köşeli parantez = değişken.

| # | EN şablon | TR uyarlama | Aile / rubrik |
|---|---|---|---|
| 1 | What If You Could See Everyone's [Lie Count]? | Ya Herkesin [Yalan Sayısını] Görebilseydin? | SEE_OTHERS, 9 |
| 2 | What If You Could See How Many People Have a [Crush] on You? | Ya Sana [Âşık Olanların] Sayısını Görebilseydin? | SEE_OTHERS+you, 9 |
| 3 | What If You Could See Who Secretly [Hates] You? | Ya Senden Gizlice [Nefret Edenleri] Görebilseydin? | SEE_OTHERS+tabu, 9 |
| 4 | What If You Could See Everyone's Future [Wealth]? | Ya Herkesin Gelecekteki [Servetini] Görebilseydin? | SEE_OTHERS+aspirasyon, 8 |
| 5 | What If You Could See Everyone's Hidden [Secret]? | Ya Herkesin Gizli [Sırrını] Görebilseydin? | SEE_OTHERS, 7 |
| 6 | What If You Were [Immortal]? | Ya [Ölümsüz] Olsaydın? | INVULN/DUAL, 7 |
| 7 | What If You Never [Missed]? | Ya Hiç [Iskalamasaydın]? | NEVER, 7 |
| 8 | What If You Stopped Feeling [Pain]? | Ya [Acı] Hissetmeyi Bıraksaydın? | NEVER/DUAL, 7 |
| 9 | What If Your [Heart] Beat 10x Faster? | Ya [Kalbin] 10 Kat Hızlı Atsaydı? | TENX beden + DUAL, 7 (10x burada beden işlevi → istisna) |
| 10 | What If You Could [Respawn]? | Ya [Yeniden Doğabilseydin] (Respawn)? | GAME_MECH, 8 — TR'de oyun terimini parantezle koru |
| 11 | What If You Could Level Up in Real Life? | Ya Gerçek Hayatta Level Atlayabilseydin? | GAME_MECH, 8 |
| 12 | What If You Had [Creative Mode] in Real Life? | Ya Gerçek Hayatta [Yaratıcı Mod] Olsaydı? | GAME_MECH, 7 |
| 13 | What If You Lived a [Googol] Years? | Ya [Googol] Yıl Yaşasaydın? | LIVED_N, 7 (seri: trilyon → googol → googolplex) |
| 14 | What If You and Your Best Friend Lived [Forever]? | Ya En Yakın Arkadaşınla [Sonsuza Dek] Yaşasaydın? | LIVED_N+sosyal, 8 |
| 15 | What If The [Immortal Snail] Chased You and Never Stopped? | Ya [Ölümsüz Salyangoz] Peşini Hiç Bırakmasaydı? | MEME, 9 |
| 16 | What If Every [Girl] on Earth Loved You? | Ya Dünyadaki Her [Kız] Sana Âşık Olsaydı? | EVERY_X, 7 (kitle cinsiyetine göre) |
| 17 | What If You Got [Louder] and Couldn't Stop? | Ya Sesin [Yükselse] ve Duramasaydın? | COULDNT_STOP, 6 — X gündelik olmalı |
| 18 | What If You Got [Brighter] and Couldn't Stop? | Ya [Parlasan] ve Duramasaydın? | COULDNT_STOP, 6 |
| 19 | What If You Could Breathe [Underwater]? | Ya [Su Altında] Nefes Alabilseydin? | SUPERPOWER istisnası (yakın + çelişkili thumbnail), 6 |
| 20 | What If You Could See [10 Seconds] Into the Future? | Ya Geleceği [10 Saniye] Önceden Görebilseydin? | TIME, 5 — yalnızca momentumla |

TR dil notları: "Ya … -saydı/-seydin?" kalıbı 2. tekil şahsı koruyor; "What If" → "Ya" kısa olduğu için 8 kelime sınırı tutuyor. Sayı yazımı: "10 Kat" (rakam+kat), devasa sayılar isimle ("Googol", "Trilyon"). Tabu kelimeler TR'de daha sert algılanabilir ("nefret", "yalan" OK; cinsel içerik yok). "Herkesin" + iyelik eki ("sayısını") kalıbı = TR'nin "everyone's count" karşılığı.

### 4e. Thumbnail spec (1280×720; 3 layout + QA kapıları)

**İlke (kanıtlı, §3b):** Thumbnail başlığın resmi değil, **ikinci sorusu**. Başlık "ne olurdu?" sorar; thumbnail "peki ya o kişiye/sayıya?" sorusunu bir çelişkiyle sorar. Metin başlığı tekrar etmez; sonuç/çelişki cümlesidir.

**Layout 1 — "Kafa üstü sayı" (sosyal aile; Lie Count / Wealth / Crush / Hates)**
- Sahne: sen (solda, x 5–40%, yüksekliğin %70'i) + öteki kişi (sağda, x 50–90%). Öteki kişinin ifadesi sayısıyla **çelişir** (gülümseyen + büyük yalan sayısı; evsiz + milyar).
- Sayı rozeti: ötekinin kafasının 10–40 px üstü, yükseklik 60–90 px, **kırmızı/yeşil doygun zemin + beyaz kalın rakam**, ≤12 karakter. Senin sayın (küçük, mavi) isteğe bağlı kontrast için.
- Metin bloğu: üst bant, y 4–26%, x 3–92%, 2 kelime (1. beyaz, 2. sarı/mor), 900 ağırlık, siyah 6–8 px dış çizgi; ya da hiç başlık metni (ConChaser) — ama o zaman sayılar ≥70 px.
- İsteğe bağlı konuşma balonu ≤3 kelime ("I love you").
- Renk: arka plan mor/lacivert gece veya sıcak gün; luma 80–140.

**Layout 2 — "Sonuç cümlesi + tek nesne" (beden/yenilmezlik/oyun; Immortal, Never Miss, Respawn, 10x Faster)**
- Karakter sağda (x 55–95%), yüz izleyiciye, **sırıtış** (power) veya gülümseyen-kanayan (DUAL); boy %80.
- Tek nesne solda-ortada: kurşun izi, basket potası, düşen beden, para yığını. Başka öğe yok (≤4 öğe toplam).
- Metin: sol üst, x 3–48%, y 5–45%, **2 kelime, 2 satır**, 1. satır beyaz, 2. satır sarı, 900 ağırlık, satır yüksekliği ~130 px; kesin kip: "CAN'T DIE." / "NEVER MISS." / "RESPAWN" / "this is fine.." (meme tonu küçük harf de olur).
- Küçük rozet (kırmızı, ≤10 karakter) isteğe bağlı: "DAY 300", "PAIN: 0%".
- Luma 70–150; arka plan bokeh şehir.

**Layout 3 — "Önce / sonra bölünmüş" (ölçek/seri; Googol, Survival Base)**
- Dikey zikzak/eğik bölme x≈48%. Sol: normal/küçük ölçek (sıcak), sağ: devasa/aykırı ölçek (soğuk).
- Her panelde dev metin üstte (y 5–28%), 1–3 kelime, sarı/beyaz; alt yarıda karakter aynı pozda, yalnızca ifade/ortam değişir.
- Sayı kontrastı asıl mesaj: "1 TRILLION 0%" vs "GOOGOL 100%"; progress bar (yükseklik 30 px) isteğe bağlı.
- Dikkat: Alternate You bu şablonu 12 videoda aynen kullandı, yalnızca isimli ölçek + "best friend" videoları tuttu → layout değil içerik hit yapıyor; seride **her bölümde bir öğe değişmeli** (yeni kişi, yeni sayı adı).

**QA kapıları (hepsi geçmeli):**
1. Luma ortalaması 60–160; siyah piksel (luma<20) ≤%35; beyaz ≤%30 (Sank 23.6/%70 siyah → 7.8K; Superpowers 191/%35 beyaz → 5.2K).
2. Metin kelime sayısı 1–4 (ConChaser tipi sayı-only hariç); 9+ kelime yalnızca serif editoryal şablonda ve o zaman tek büyük sayı ≥160 px.
3. Metin başlığı tekrar etmiyor → "ikinci soru" testi: thumbnail metni + başlık yan yana okunduğunda **yeni bilgi** veriyor mu? (Hayır → yeniden yaz.)
4. Çelişki testi: karede bir yüz ifadesi bir sayı/durumla çelişiyor mu? (Sosyal ailede zorunlu; beden ailesinde DUAL ise zorunlu.)
5. Öğe sayısı ≤4 (karakter, öteki, nesne, metin). Kenar yoğunluğu (FIND_EDGES >60) ≤0.062 (en kalabalık çeyrek hit %20).
6. Mobil küçültme: 320×180'e indirildiğinde metin ve sayı okunuyor; yüz ≥%12 kare alanı.
7. Karakter tutarlılığı: aynı hoodie rengi/kafa; ConChaser'ın kırmızı hoodie'li 10 Seconds (19K) gibi karakter değişimi yok.
8. Metinsiz thumbnail yasak (0/3 hit, Jeremy'de 0/5).
9. Kırmızı rozet zorunlu değil (en az kırmızı çeyrek hit %45); kullanılırsa ≤%5 alan.
10. Başlıkla **renk/nesne** eşleşmesi: başlıktaki somut isim karede var (snail, heart, hoop).

### 4f. İlk 24 saat / momentum / kadans gözlemleri (`dataset.csv`)

| Gözlem | Veri |
|---|---|
| Lansman etkisi | Kanalın 1. videosu hit %60 (6/10; medyan 124K); 2–3. video %33; 4–8. video %19; 9+ %32. 7/10 kanal ilk 3 videoda hit aldı. Jeremy 1. gün 4 video: 584K/364K/304K/18K (Heart 10x info.json upload_date 2026-10-11, dataset 10-14 → kanal yaşı 14 gün tutarlı). |
| Lansman tek başına yetmiyor | Hour Seven 1. video 2.2K, Alternate You 1.4K, Ifsphere 4.5K → lansmanda **zayıf başlık** push'u boşa harcıyor. ConChaser 1. gün 12K/19K, 3. video 482K. |
| İlk 24 saat izlenmeleri | Yaş 0 gün (n=8): medyan 1.2K, max 41K (Graham — seri momentumuyla). Yaş 1 gün (n=8): medyan 12.8K, max 179K (Crush). Yaş 2 gün: medyan 90K. → Hit'ler 24–48 saatte belli oluyor; 2. günde <20K olan video hit olmuyor (n=84'te istisna yok). |
| Hit sonrası | Hit'ten hemen sonraki videonun medyanı: Iflord 114K (n=3), Jeremy 64K (n=8), Alternate You 252K (seri), Ifsphere 5.7K, Hour Seven 6.2K, Miko 19K, Readout 22K. → Hit, aynı aileden devam gelirse taşınıyor (Iflord, AY), aile değişirse taşınmıyor (Hour Seven Snail → yok; Miko Lie Count → Erase 21K). |
| Kadans | video/gün: Ifsphere 1.62 (hit %11, medyan 8.1K), Jeremy 1.47 (%44, 50K — lansman şişkin), ConChaser 1.25, Iflord 1.0 (%50, 80K), Readout 1.0 (%30), Ifquirky 1.0 (%40), AY 0.86 (%18), Hour Seven 0.73 (%25), Miko 0.45 (%50, 94K). → **1 video/gün üstü hit oranını düşürüyor; 0.5–1.0 bandı en verimli.** Aynı gün 2 video: 26 çiftte kazanan ortalama 7.7× — ikinci video neredeyse her zaman kaybediyor (öneri: günde 1). |
| Süre (not, B/C ajanı alanı) | 10–13 dk hit %56 (n=16, medyan 109K); 8–10 dk %33; 6–8 dk %23; <6 dk %25; 13+ dk %11. Hit'lerin medyan süresi ≈ 9–10 dk. |
| Metadata (ev/ info.json, 9 video) | Kategori: Film & Animation (Iflord), Education (Miko), Entertainment (Jeremy), People & Blogs (ConChaser/Ifsphere/Ifquirky/Hour Seven) → kategori hit'i ayırmıyor. Etiket: Iflord 20+ (ifverse, stickman animation, what if animation…), Hour Seven 5, Miko 1, ConChaser/Ifsphere/Ifquirky/Jeremy 0 → **etiketsiz 482K/460K/226K var; etiket önemsiz.** Açıklama: Iflord/Miko/Underwater bölümlü (13–20 chapter) + "Would YOU…? Tell us in the comments"; ConChaser 3 cümle. Hepsi "comments" CTA'lı. Hit'lerin beğeni/izlenme ≈ %0.6–0.8; yorum/izlenme Immortal ve Snail'de %0.06+ (400 yorum tavanı), diğerlerinde %0.01–0.03. |

## Neden çalışıyor (mekanizma özeti)

1. **Simülasyon arzusu, güç arzusu değil.** Hit başlıklar izleyiciye "ben olsam?" simülasyonu başlatıyor; sonucu belirsiz olanlar (DUAL) simülasyonu uzatıyor. Sonucu belli klasik güçler (uçmak, teleport) simülasyon üretmiyor → %6.
2. **Sosyal bilgi asimetrisi = en güçlü merak.** "Sadece sen görüyorsun" + "sayı" + "senin çevren" = hem oyun (benim sayım kaç?) hem risk (sevdiklerim?). Aynı mekanik keder (ölüm günü) ya da utanç (senin sırrın görülüyor) olunca kaçınma tetikliyor.
3. **Thumbnail'de çelişki, başlığın vaat ettiği mekanizmanın ilk sonucunu gösterip ikinci soruyu açıyor** (gülen sevgili + 9,317 +1). Tekrar eden metin bilgi eklemiyor; metinsiz kare mekanizmayı iletmiyor.
4. **Tanıdıklık maliyeti sıfırlıyor** (meme, oyun UI, googol, "this is fine"): izleyici kavramı 0.3 sn'de yerleştiriyor, kalan dikkat çelişkiye gidiyor.
5. **Lansman + seri momentumu** dağıtımı belirliyor; başlık/thumbnail dönüşümü belirliyor. İkisi çarpım: zayıf başlık × lansman = 2K (Hour Seven), güçlü başlık × ölü kanal = 8.7K (AY Same Day), güçlü × lansman = 656K.

## Kopyalanacak kurallar (ölçülebilir, emir kipi)

1. Başlığı rubrikle puanla; **≥7 değilse üretme**. Haftada en az 2 başlık sosyal-sayı ailesinden (K3=2, K4=1), 1 başlık DUAL beden ailesinden.
2. Başlık 6–8 kelime (TR ≤8 kelime, ≤55 karakter), tek fikir, "Ya … -seydin?" kalıbı, soru işaretiyle bitir.
3. Sıradan rakam kullanma (10x, 1 cm, 60 m, 500 IQ); sayı gerekiyorsa **isimli ölçek** (googol) ya da **sayma vaadi** ("kaç kişi", "sayısı").
4. Sosyal ailede bilgi yönü daima izleyiciye: "sen görüyorsun"; "herkes seni görüyor" yasak. Sayı nesnesi aspirasyonel/ilişkisel; ölüm sayacı ve cinsel partner sayısı yasak.
5. Klasik süper güç (uç, ışınlan, X'i kontrol et, görünmezlik, klon) **yasak**; mutlaka istenirse oyun mekaniği diline çevir (respawn, level, creative mode) veya DUAL yap (bedel ekle).
6. Thumbnail metni 1–4 kelime, başlığı tekrar etmez, sonuç/çelişki cümlesi; 1. satır beyaz, 2. satır sarı/mor, 900 ağırlık, siyah dış çizgi; sol üst %45×%40 veya üst bant %90×%22.
7. Sosyal ailede thumbnail'de ikinci kişi + kafa üstü sayı rozeti + ifade çelişkisi **zorunlu** (Layout 1).
8. Beden ailesinde tek nesne + karakter sırıtışı + sonuç cümlesi (Layout 2); toplam öğe ≤4.
9. QA: luma 60–160, siyah ≤%35, kenar yoğunluğu ≤0.062, 320×180'de okunur, karakter/hoodie sabit, metinsiz thumbnail yok.
10. Kanalın ilk 3 videosu en yüksek rubrik puanlı 3 başlık olsun (K≥8); ilk 48 saatte <20K ise seri devam ettirme, aile değiştir.
11. Günde en fazla 1 video; 0.5–1.0 video/gün; aynı gün iki video yükleme.
12. Hit gelince aynı aileden eskalasyonlu devam (googol → googolplex; lie count → crush) 24–72 saat içinde; bir öğe değiştir (yeni kişi, yeni sayı adı).
13. Metadata: bölümler (≥10 chapter) + "Sen olsan ne yapardın? Yorumlara yaz" CTA; etiketlere zaman harcama.

## Türkçe uyarlama notları

- "What If You…" → "Ya … -saydın/-seydin?" (2. tekil korunur, 1–2 kelime tasarruf). Büyük harf "YA" veya "Ya" A/B test edilmeli (EN'de "IF" büyük harf etkisiz çıktı, TR'de de beklenmez).
- Türkçe eklerle karakter sayısı %15–25 artar; EN 40 karakter ≈ TR 50. Mobil kesme için ana somut ismi ilk 5 kelimeye koy ("Ya Herkesin Yalan Sayısını…").
- Sosyal-sayı kalıbı TR'de doğal: "Herkesin ___ Sayısını Görebilseydin", "Sana ___ Olanları Görebilseydin", "Senden Gizlice Nefret Edenleri". "Crush" → "âşık olan / hoşlanan" (hoşlanan daha hafif, test et).
- Oyun terimleri (respawn, level, creative mode) TR oyuncu kitlesinde İngilizce yaygın; başlıkta TR fiil + parantez içinde terim ("Yeniden Doğabilseydin (Respawn)") veya doğrudan "Level Atlayabilseydin".
- Meme tanınırlığı yerel: "ölümsüz salyangoz" TR'de bilinirliği düşük olabilir → TR internetinin kendi meme senaryoları (ör. "Ya her gün aynı güne uyansaydın" tanıdık; "ya herkesin maaşını görebilseydin" TR'de sosyal-tabu olarak güçlü aday — maaş gizliliği kültürel).
- Dini/cinsel şaka (rahibe + 78) TR'de daha riskli; QA'da yasak.
- Thumbnail metni TR'de 2 kelime: "ÖLEMİYORUM." / "ASLA ISKALAMAM." / "KİM NEFRET EDİYOR?" — büyük harf İ/ı sorunlarına dikkat (font seçimi: Montserrat/Inter 900 Türkçe glifli).

## Diğer ajan için not

- (Senaryo/retention ajanı) Süre 10–13 dk bandı hit %56; hit'lerin açıklamalarında 13–20 bölüm (Immortal: Year 1 → Year 10,000 → Sun dies; Lie Count: Day one → By Friday → Midnight) → zaman atlamalı eskalasyon yapısı. Underwater 0:25'te "What if…", 0:45'te "The rule" → kural 45 sn'de konuyor.
- (Senaryo) DUAL başlıklarda açıklama "bedel" cümlesiyle bitiyor ("hardest part… watching everyone you love grow old"); hook'un bedeli erken sezdirmesi muhtemel.
- (Yorum/kitle ajanı) Yorum/izlenme Immortal ve Snail'de ≥%0.06 (400 tavan), sosyal-sayı hit'lerinde %0.01–0.02 → felsefi/varoluşsal başlıklar yorum, sosyal-sayı başlıklar izlenme getiriyor.
- (Animasyon) Hit thumbnail stilleri: WHITE_ROUND flat vektör hit %45, STICK_BLACK %23 — ama kanal karıştırıcı; stil seçimi okunabilirlik (açık kafa koyu zeminde) lehine.

## Açık sorular / düşük güven

1. Lansman etkisi ile başlık etkisi ayrıştırılamıyor (ilk video hit %60); Jeremy'nin ilk gün 3 hit'i tüm "beden/DUAL" istatistiğini şişiriyor — Heart 10x/No Pain/10 Seconds lansman dışı bir kanalda test edilmeli.
2. Ölüm sayacı ailesi n=4 (1 hit, lansman): "valans" hipotezi makul ama küçük örnek.
3. Ters-yön sosyal (herkes seni görüyor) n=3, hepsi 0–5 gün yaşında ve düşük momentumlu kanalda (Ifquirky/Ifsphere) → karıştırıcı var.
4. "IF" büyük harf, kategori, etiketler: etkisiz görünüyor ama tek kanal/az örnek.
5. CTR gerçek değeri yok (gösterim verisi yok); izlenme = CTR × dağıtım. "Tıklandı" çıkarımları izlenme üzerinden; aynı gün/aynı kanal çiftleri dağıtımı kısmen sabitliyor ama YouTube'un ilk saatlerdeki testi iki videoya farklı davranmış olabilir.
6. 0–1 günlük 16 video (Graham 41K, Electricity 3.5K, Darkest Secret 15…) sonuçları değiştirebilir; 48 saat sonra yeniden çekilmeli.
7. Thumbnail "çelişki" ve "ikinci merak" etiketleri tek gözlemci (ben) tarafından verildi; ikinci bir etiketleyici ile uyum ölçülmedi.
8. Süre/retention bulguları başka ajanın alanı; burada yalnızca korelasyon.
