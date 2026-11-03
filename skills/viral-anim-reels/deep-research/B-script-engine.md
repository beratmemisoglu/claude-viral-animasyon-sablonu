# B — Senaryo / Anlatı Motoru (Analist B, 2026-10-29)

**Veri:** Ricks Clips'in 26 videosu (22'si yeni "hikâyeli açıklayıcı" dönemden, 4'ü eski komedi klibi) ve 15 rakip video. Her videoda kelime düzeyinde zamanlama (`subs.en-orig.json3` / `video.en-orig.json3`), `meta.json` ve `transcript.txt` kullanıldı.
**Script'ler** (`python -I` ile çalışır):
- `analysis/scripts/b_dump.py`: json3 dosyasından kelime+zaman listesi ve cümle bazlı döküm üretir → `analysis/scripts/out/sent_<id>.txt`, `words_<id>.json`
- `analysis/scripts/b_stats.py`: video başına istatistik + hit/orta/düşük grup medyanları → `out/stats.json`. Twist/cevap zamanı, son satır tipi ve döngü etiketi elle işaretlendi, `ANN` sözlüğünde duruyor.
- `analysis/scripts/b_table.py`: aşağıdaki tabloyu üretir.

**Tanımlar**
- K/dk: konuşma süresine göre dakikadaki kelime.
- Pivot: but, yet, except, instead, wait, so, turns out, you see sözcüklerinin sözcüksel sayımı ("then" ayrı tutuldu).
- Twist %: ilk büyük dönüşün videonun yüzde kaçında geldiği.
- Açıklama/cevap %: izleyicinin sorusunun cevaplandığı ya da mekanizmanın açıldığı an.
- Döngü: "EVET" = son cümle yarıda kesilip ilk cümleye akıyor; "kısmi" = kapanış açılıştaki nesneye ya da kelimeye geri dönüyor.

> **Yaş uyarısı:** 5WMQ 0 günlük (2,48M), ZDy3 1 günlük, LC8h 2 günlük, t3OX 3 günlük, DEe0 4 günlük. Bu videolar henüz olgunlaşmadı. 5WMQ ve LC8h büyük olasılıkla hit olacak. t3OX ise 3 günde 324K'da kaldı. Bu kanalda hit videolar ilk 3 günde milyonları geçiyor, o yüzden t3OX'u flop saymak güvenli.

---

## 1. Video başına istatistikler

### 1a. Ricks Clips, yeni dönem (22 video, izlenmeye göre sıralı)

| # | Video | İzlenme | Süre | Kelime | K/dk | Ort. cümle | Soru | Pivot (adet @ sn) | Twist % | Açıklama/cevap % | Döngü | Son satır tipi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | The Ancient Jar That Warned an Empire (`VS1Z_Q-Klt8`) | 28.8M | 65 sn | 235 | 217 | 11.2 | 1 | but 2@13,19; so 1@29; you see 1@7 (Σ4) | 70 | 75 | hayır | punchline (mekanizma) |
| 2 | The Job Nobody Wants in Japan (`0m6G8pDtzNs`) | 14.7M | 61 sn | 224 | 223 | 13.2 | 1 | but 2@2,53; wait 2@18,58; so 2@38,55; you see 1@49 (Σ7) | 69 | 80 | hayır | ahlak/sonuç |
| 3 | The Window That Breaks Japan's Gambling Law (`eQR3pgMiUF0`) | 11.9M | 45 sn | 160 | 214 | 12.3 | 0 | but 2@12,16; yet 1@2; instead 1@19; so 2@14,37; you see 1@30 (Σ7) | 60 | 67 | kısmi (geri çağrı) | punchline |
| 4 | Your Brain's Secret Idea Zone (`PL-Yro2meY4`) | 11.6M | 39 sn | 145 | 225 | 16.1 | 0 | but 2@21,34; instead 1@38; so 1@36; you see 1@4 (Σ5) | 34 | 59 | kısmi (geri çağrı) | punchline |
| 5 | What the Grave Bell Really Meant (`GM9UKnZ6JFw`) | 9.4M | 60 sn | 219 | 222 | 13.8 | 1 | but 1@27; except 1@10; instead 1@46; wait 1@36; so 2@4,40; you see 2@3,54 (Σ8) | 62 | 62 | hayır | punchline (ikinci twist) |
| 6 | Levels of Pirate Cannonballs (`lnYLIWP2l-I`) | 8.1M | 64 sn | 218 | 206 | 24.2 | 0 | but 1@18; so 4@14,28,44,53 (Σ5) | 58 | 58 | hayır | bilgi (seviye) |
| 7 | An Unstoppable Spear vs an Unbreakable Shield (`PLe2Gu3FDuA`) | 7.7M | 45 sn | 164 | 219 | 16.4 | 1 | so 2@12,38; you see 1@33 (Σ3) | 65 | 73 | hayır | punchline (sonuç) |
| 8 | Why Humans Can't Pick Random Numbers (`TgyHSIttwdM`) | 7.6M | 47 sn | 163 | 208 | 11.6 | 1 | but 3@10,18,40; so 2@26,43 (Σ5) | 75 | 52 | EVET (kesik cümle) | seamless kesik |
| 9 | The Burglar Who Only Moved Furniture (`nzbkkEZFM8g`) | 7.0M | 58 sn | 238 | 245 | 17 | 2 | but 2@9,25; so 4@14,18,35,54; you see 1@51 (Σ7) | 82 | 88 | kısmi (geri çağrı) | punchline |
| 10 | What If Humans Invented Teleportation? (`WbRdDyaPuAU`) | 6.3M | 54 sn | 198 | 220 | 16.5 | 2 | but 2@18,25; so 1@52 (Σ3) | 39 | 69 | kısmi (geri çağrı) | soru (seçim) |
| 11 | Why Cashiers Keep Winning The Lottery (`VKsamN3Fk4U`) | 5.9M | 58 sn | 199 | 208 | 18.1 | 0 | except 1@39; wait 1@32; so 3@23,32,51; you see 1@44 (Σ6) | 65 | 75 | hayır | açıklama |
| 12 | The Scientist's Insane Time Test (`hdhggSABEws`) | 5.8M | 40 sn | 143 | 218 | 15.9 | 0 | but 1@28; so 3@8,14,36; you see 1@32 (Σ5) | 71 | 80 | hayır | açıklama |
| 13 | He Could Spot Winning Tickets Just by Looking (`DEe0iKH4KIw`) | 4.6M | 63 sn | 231 | 220 | 14.4 | 2 | but 2@14,37; yet 1@4; instead 1@14; so 3@22,48,52 (Σ7) | 62 | 50 | hayır | sonuç |
| 14 | Why the Second Draw Always Wins (`LC8hYwUZ-kU`) | 4.5M | 56 sn | 219 | 234 | 13.7 | 1 | but 2@25,45; yet 1@17; so 1@14; you see 1@36 (Σ5) | 55 | 65 | hayır | açıklama |
| 15 | Would You Upload Your Brain? (`eSRnuL-fVSE`) | 3.3M | 57 sn | 214 | 226 | 9.7 | 2 | but 3@3,7,54; so 2@14,55 (Σ5) | 77 | 83 | hayır | soru (seçim) |
| 16 | How a Mirror Rigged a Horse Race (`5WMQhPObNqQ`) | 2.5M | 64 sn | 244 | 230 | 16.3 | 1 | wait 1@11; so 3@28,32,58; you see 1@45 (Σ5) | 54 | 71 | hayır | punchline |
| 17 | The Town Built Around a Button (`ZDy3xXA2iHk`) | 1.9M | 66 sn | 245 | 225 | 15.3 | 0 | but 3@20,41,44; so 2@13,31 (Σ5) | 87 | 87 | kısmi (geri çağrı) | cliffhanger/döngü |
| 18 | This Knight Found the Ultimate Loophole (`jpFJ8Z_F-qU`) | 1.5M | 41 sn | 158 | 233 | 15.8 | 0 | yet 1@3; so 2@16,27; you see 1@3 (Σ4) | 72 | 90 | kısmi (geri çağrı) | punchline |
| 19 | This Tree Hates You (`uRkLhDrKQeU`) | 959K | 68 sn | 235 | 209 | 10.2 | 0 | but 1@11; so 2@28,64; you see 1@20 (Σ4) | 80 | 29 | kısmi (geri çağrı) | espri/ders |
| 20 | Every Memory Has a Price (`t3OXkhlI6NQ`) | 324K | 78 sn | 294 | 227 | 14.2 | 0 | but 2@33,42; so 2@18,44; you see 1@3 (Σ5) | 91 | 91 | kısmi (geri çağrı) | dram (trajik) |
| 21 | How Painkillers Actually Work (`_sUAXTvJquk`) | 286K | 35 sn | 137 | 239 | 13.7 | 4 | so 2@11,31 (Σ2) | 73 | 73 | hayır | açıklama |
| 22 | The Science Behind Slot Machines (`CJwgTrfrHL0`) | 91K | 31 sn | 112 | 219 | 12.4 | 0 | but 1@13; so 4@5,12,16,26 (Σ5) | 75 | 58 | hayır | açıklama |

### 1b. Rakipler (15 video)

| # | Video | İzlenme | Süre | Kelime | K/dk | Ort. cümle | Soru | Pivot (adet @ sn) | Twist % | Açıklama/cevap % | Döngü | Son satır tipi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | She got Her Ring Back Using a GENIUS trick 💍 (`mSJCcf5Robg`) | 42.3M | 26 sn | 68 | 158 | 8.5 | 1 | so 1@3 (Σ1) | 84 | 84 | hayır | soru |
| 2 | How the Eye In The Sky works (`B5fQLSLsXCw`) | 37.2M | 79 sn | 264 | 205 | 16.5 | 0 | but 5@11,18,19,55,64; so 1@53 (Σ6) | 90 | 81 | hayır | punchline |
| 3 | Man who broke the bank at Monte Carlo (`aVeX3-5K33Q`) | 22.9M | 67 sn | 210 | 191 | 15 | 1 | but 1@46; so 4@26,39,57,63 (Σ5) | 66 | 33 | hayır | sonuç |
| 4 | Odds of winning a lottery visualized (`NCl7daUhvsM`) | 22.4M | 59 sn | 215 | 225 | 16.5 | 0 | but 3@6,25,35; so 1@3 (Σ4) | 67 | 12 | hayır | punchline |
| 5 | Why You Get Sleep Paralysis/Sleepwalk (`Rzu4ZNnaTb8`) | 17.0M | 38 sn | 128 | 203 | 21.3 | 0 | but 2@6,19; so 2@4,26 (Σ4) | 49 | 61 | hayır | açıklama |
| 6 | Why You Should Get A Cast (`JsmBio-bQkg`) | 16.3M | 42 sn | 166 | 241 | 20.8 | 1 | but 3@2,14,27; so 1@10 (Σ4) | 65 | 32 | hayır | açıklama |
| 7 | He ESCAPED Prison With This Simple Trick 🥚 (`fHhJ8jJ2pU0`) | 16.1M | 29 sn | 84 | 173 | 12 | 1 | but 2@10,22; so 2@3,15 (Σ4) | 77 | 77 | hayır | soru |
| 8 | How an Accident Made Boats Faster #animation (`rv6qAgdPsXw`) | 14.7M | 48 sn | 151 | 192 | 11.9 | 0 | but 2@7,27; so 2@13,25 (Σ4) | 43 | 49 | kısmi (geri çağrı) | punchline (genelleme) |
| 9 | He Got His iPhone Back Using THIS Trick 📱 (`JpC3f1cYYnM`) | 13.3M | 26 sn | 78 | 185 | 15.6 | 0 | but 2@18,21; so 2@3,22 (Σ4) | 71 | 71 | hayır | punchline |
| 10 | Why Stopping Time Is A Bad Idea (`lWz9YjJ7H4E`) | 13.3M | 47 sn | 154 | 199 | 14 | 0 | but 2@31,38; so 4@12,22,26,46; you see 1@7 (Σ7) | 80 | 14 | EVET (kesik cümle) | seamless kesik |
| 11 | He Put His Head in a Particle Accelerator (`fM-_0tJG8Eo`) | 11.6M | 73 sn | 249 | 210 | 10.5 | 1 | but 1@57; so 2@23,66 (Σ3) | 59 | 61 | hayır | punchline (görsel) |
| 12 | Was Bar Shot Useless? #shorts #history (`S0sf_K08twQ`) | 10.0M | 23 sn | 94 | 246 | 11.8 | 1 | but 2@6,13; instead 1@2; so 1@8 (Σ4) | 70 | 70 | hayır | açıklama |
| 13 | The Truck You Don't Want Behind You (`vxnnsMcoCMs`) | 9.9M | 39 sn | 127 | 201 | 12.7 | 0 | but 1@5; so 2@7,27 (Σ3) | 53 | 59 | kısmi (geri çağrı) | punchline (paradoks) |
| 14 | Why Muskets Were Useless? #shorts #history (`WMF3reQPqfk`) | 6.0M | 25 sn | 93 | 221 | 13.3 | 1 | but 1@18; instead 1@3; so 1@15 (Σ3) | 71 | 71 | hayır | açıklama |
| 15 | Was Kanabo Useless? #shorts #history (`pY_bADpW_aw`) | 5.0M | 29 sn | 116 | 241 | 12.9 | 1 | but 3@7,19,22; instead 1@2; so 1@11 (Σ5) | 73 | 73 | hayır | açıklama |

### 1c. Grup medyanları (`b_stats.py` çıktısı)

| Grup | n | Medyan izlenme | Süre | Kelime | K/dk | Ort. cümle | Hook (1. cümle) kelime | Pivot/dk | Twist % | Cevap % | "You see" kullanan | Döngü/geri çağrı |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ricks HIT ≥5M | 12 | 7,9M | 56 sn | 199 | 219 | 16,0 | **16** | **6,6** | **65** | 71 | **9/12** | 5/12 |
| Ricks ORTA 1–5M | 6 | 2,9M | 60 sn | 225 | 228 | 14,9 | 12,5 | 5,3 | 67 | 77 | 3/6 | 2/6 |
| Ricks DÜŞÜK ≤1M | 4 | 0,3M | 52 sn | 186 | 223 | 13,1 | 11 | **3,7** | **78** | 66 | 2/4 | 2/4 |
| Rakipler | 15 | 14,7M | 39 sn | 128 | 203 | 13,3 | 13 | 5,7 | 70 | 61 | 1/15 | 3/15 |

### 1d. Tablodan çıkan sonuçlar
1. **Hız sabit:** Ricks dakikada 207–246 kelime okuyor (medyan 221) ve bu hit ile flop arasında fark yaratmıyor. Rakipler biraz daha yavaş (203). Hızı değil yapıyı optimize et.
2. **Süre hitlerde 39–65 sn.** En kısa iki video flop: CJwg 31 sn, _sUA 35 sn. En uzun video da flop: t3OX 78 sn. Hikâyeli formatta pratik pencere 45–65 sn. Rakiplerin 23–29 sn'lik videoları "tek hileli mini hikâye", farklı bir lig.
3. **Pivot yoğunluğu ayırıcı:** Hitlerde dakikada 6,6 pivot var, düşüklerde 3,7. Ortalama her 9 sn'de bir "but / so / you see / wait" geliyor ve her biri yeni bir mini soru açıyor.
4. **Twist erken geliyor:** Hitlerde %65'te (≈36. sn), düşüklerde %78'de. t3OX'ta %91 (70. sn). Twist'e kadar geçen 70 sn izleyiciyi kaçırıyor.
5. **Hook daha uzun ve daha somut:** Hitlerde medyan 16 kelime, düşüklerde 11. Hit hook'ları tek cümlede **özne + tuhaf eylem + sonuç tehdidi** taşıyor. Örnek yapı: "He put X in Y and told Z: if this ever falls, run."
6. **Soru sayısı fark yaratmıyor** (hit medyanı 1). Soruyla açılan tek video olan _sUA ("How do painkillers…?", 4 soru) 285K'da kaldı. **Ricks soruyla açılmaz, iddiayla açılır.** Soru sadece "audience proxy" kesmesi olarak ortada kullanılıyor ("Wait, practiced?", "But how?", "How is that possible?").
7. **"You see," ana menteşe:** 22 videonun 14'ünde, hitlerin 9/12'sinde geçiyor. İki görevi var: (a) 3–7. sn'de dünya kuralını vermek, (b) %65–85 aralığında mekanizmayı açmak.
8. **Gerçek seamless loop sadece 1/22 videoda var** (TgyH, "…there's almost always a way to" diye kesilip açılışa akıyor). Rakiplerde de 1/15 (Low Poly, lWz9, "So, you instantly" → "…you would instantly go blind"). Ricks'in kapanış stratejisi döngü değil. Ricks **son cümleyi bir punchline / yeniden çerçeveleme** olarak yazıyor. Hitlerin 5/12'si açılıştaki nesneye geri dönüyor (top → fikir, jeton → para). Bu "yumuşak geri çağrı" tekrar izlemeyi tetikliyor.
9. **Yorum motoru:** Seçim sorusuyla biten videolar yorum oranında patlıyor. eSRn 6,4/10K, WbRd 3,5/10K yorum aldı; kanal medyanı ≈0,7. 0m6G (6,8/10K) "Japonya gerçekten böyle mi?" tartışması çıkarıyor. Kapanış sorusu izlenmeyi değil yorumu artırıyor.

---

## 2. Beat-by-beat kırılımlar

Gösterim: `[sn | %] VURUŞ: içerik (kısa alıntı)`

### HIT 1 — The Ancient Jar That Warned an Empire (VS1Z, 28,8M, 65 sn)
- `[0,0 | 0%] HOOK`: Mucit ejderin ağzına top koyuyor ve imparatora "düşerse kaç" diyor. Somut nesne, açık bir tehdit ve otorite karşıtlığı tek cümlede.
- `[5,2 | 8%] TEPKİ`: Saray gülüyor. Alay, kahramanı haklı çıkarma beklentisi kuruyor.
- `[7,2 | 11%] DÜNYA KURALI ("You see,")`: 8 ejder, 8 kurbağa, toplar. Görsel envanter veriliyor, mekanizma saklanıyor.
- `[13,4 | 21%] İTİRAZ ("But")`: İmparatorun dünyanın en büyük ordusu var.
- `[17,6 | 27%] SAHTE ALARM`: Top düşüyor ama bir şey olmuyor (alıntı: "but nothing happened"). Merak ikiye katlanıyor.
- `[22,2–32,8 | 34–50%] TIRMANMA 1`: Gülüşler artıyor, mucit kovuluyor, tepede yalnız yaşıyor. Underdog dibi görüyor.
- `[32,8–37,0 | 50–57%] TIRMANMA 2 (üçlü merdiven)`: "Then… Then another. Then all eight at once." Kısalan cümlelerle ritim hızlanıyor (6 → 2 → 5 kelime).
- `[37,0–45,4 | 57–70%] İKİNCİ RED`: Muhafızlar alay ediyor ("Did your frogs get hungry again?"). Komik diyalog gerilimi tepeye taşıyor.
- `[45,8 | 70%] PAYOFF`: Sabah saray moloz yığını.
- `[48,5–58,2 | 75–89%] MEKANİZMA`: Sarkaç → çubuk → çene → top. Tek nefeslik neden-sonuç zinciri.
- `[58,2–65 | 89–100%] ANLAM PUNCHLINE'I`: Tek top uzak bir sarsıntı demek, sekizi birden "deprem tam altınızda" demek.
- **Neden çalıştı:** Bilinen bir "haklı çıkan alay edilen dahi" kalıbı + 2.000 yıllık gerçek bir alet + 2 sahte alarm + çok geç açılan, ama 10 sn'de anlaşılan bir mekanizma. Pivotlar 7, 13, 19, 29, 33. sn'lerde, yani her 5–8 sn'de bir yeni soru açılıyor.

### HIT 2 — The Job Nobody Wants in Japan (0m6G, 14,7M, 61 sn)
- `[0 | 0%] HOOK (paradoks + tehdit)`: "Kovulmak imkânsız ama… daha kötüsü var." Önce yasal bir gerçek, sonra "but" ile tehdit geliyor.
- `[4,4 | 7%] "Imagine" + 2. TEKİL`: Patron seni boş bir odaya götürüyor. İzleyici kahramanın yerine geçiyor.
- `[13,6 | 22%] DİYALOG`: "Yeni işin: hiçbir şey."
- `[17,3 | 28%] AUDIENCE PROXY`: "Wait, I'm getting paid for this?" İzleyicinin aklındaki itiraz anlatıcının ağzından söyleniyor.
- `[19,9 | 33%] SAHTE CENNET`: "Önce cennet gibi."
- `[21,6–33 | 35–54%] TIRMANMA (izolasyon merdiveni)`: Bakışlar, kesilen e-postalar, masanda başkasının aile fotoğrafı, cuma ziyaretlerinde patronun sinsi gülümsemesi. Her basamak küçük ve somut bir ayrıntı.
- `[33,1 | 54%] KARŞI-İPUCU`: Köşedeki adam 3 yıldır burada ve herkesten mutlu.
- `[38–42 | 62–69%] KABULLENME`: Sen de ayaklarını uzatıyorsun.
- `[42,2 | 69%] TWIST`: Bir pazartesi adam gitmiş, kimse nereye gittiğini söylemiyor.
- `[49,1 | 80%] MEKANİZMA ("You see,")`: Yasa kovmayı yasaklıyor, mutsuz etmeyi yasaklamıyor.
- `[55 | 90%] AHLAK PUNCHLINE'I`: "Kimse sonsuza kadar hiçbir şey yapamaz."
- **Neden çalıştı:** Gerçek bir kurum (oidashi-beya, "kovma odaları") + izleyicinin kendisi kahraman (20 kez "you/your") + "harika görünen ceza" ironisi + köşedeki adamla gelen gizem. Yorum oranı 6,8/10K, kanaldaki en yüksek oran.

### HIT 3 — The Window That Breaks Japan's Gambling Law (eQR3, 11,9M, 45 sn)
- `[0 | 0%] HOOK (iki cümlelik paradoks)`: "Kumar yasak. Yet her sokakta kumarhane var." 5 + 9 kelime, 4,4 sn.
- `[4,4 | 10%] DUYUSAL KANIT`: Binlerce makine, kova kova çelik bilye.
- `[10,3 | 23%] İTİRAZ`: Polis kapının önünden geçiyor, kimse tutuklanmıyor. Paradoks derinleşiyor.
- `[13,6 | 30%] SEN DENE`: Kovayı kazanıyorsun ama "the counter won't give you a single yen".
- `[18,6 | 41%] TUHAF SEÇENEK`: Kurabiye, şampuan ya da küçük plastik jetonlar.
- `[23,9–30 | 53–67%] TAKİP`: Öndeki adamı köşedeki tabelasız pencereye kadar izliyorsun. Merak fiziksel bir yolculuğa dönüşüyor.
- `[30,3 | 67%] CEVAP ("You see,")`: O pencere salonun parçası değil.
- `[32,9–40 | 73–89%] MEKANİZMA`: Ayrı dükkân, ödül ve satın alma.
- `[40,6 | 90%] PUNCHLINE`: Jetonlar girer, para çıkar ve "on paper, nobody gambled".
- **Neden çalıştı:** Başlıktaki nesne (pencere) 26. sn'de ekranda görünüyor ve vaat birebir karşılanıyor. İzleyici küçük bir dedektif gibi takip ediyor. Hikâye 45 sn ve tek mekânda geçiyor. Pivot sıklığı en yüksek gruptan: 7 pivot / 45 sn.

### HIT 4 — Your Brain's Secret Idea Zone (PL-Y, 11,6M, 39 sn)
- `[0 | 0%] HOOK (koşullu vaat)`: "İki çelik topla uyursan dahi uyanabilirsin." Absürt bir ritüel + kişisel kazanç.
- `[3,8–11,7 | 10–30%] TARİF (2. tekil, emir kipi)`: Plakalar, toplar, "drift off". İzleyici yapabileceği bir şeyi öğreniyor.
- `[11,7 | 30%] MENTEŞE`: "Now, here's the weird part."
- `[13,2 | 34%] OLAY`: Eller gevşiyor, toplar düşüyor, uyanıyorsun.
- `[19,0 | 49%] İTİRAZ + OTORİTE`: Kulağa en kötü şekerleme gibi geliyor, "but" Edison bilerek yaptığı rivayet ediliyor. Ünlü isim tam ortada geliyor.
- `[23,0 | 59%] BİLİM`: Hipnagoji, "yarı yol" hali.
- `[31,0 | 79%] SORUN + ÇÖZÜM`: Normalde bu hali geçersin ama gürültü seni tam ortasında yakalıyor.
- `[36,1 | 93%] GERİ ÇAĞRI PUNCHLINE'I`: Topları değil fikri tutarak uyanıyorsun. Açılıştaki "holding two steel balls" kapanışta kelime oyununa dönüşüyor.
- **Neden çalıştı:** Kısa (39 sn), kişisel fayda vaat ediyor ("dahi ol"), uygulanabilir ve sonunda kelime oyunu var. Kanaldaki en iyi "geri çağrı" kapanışı.

### HIT 5 — What the Grave Bell Really Meant (GM9U, 9,4M, 60 sn)
- `[0 | 0%] HOOK (şok)`: "Parmağına zil bağlanmış bir adamı diri diri gömdüler." 12 kelime, 3 sn.
- `[3,1 | 5%] DÜNYA KURALI ("You see,")`: İnsanlar tabutta uyanmaktan korkuyordu, mezarların üstünde zil vardı.
- `[10,0 | 17%] OLAY + RET ("Except")`: Saat 2'de zil çalıyor, komşu "rüzgârdır" diyor.
- `[15,2–21,6 | 25–36%] KOMİK TIRMANMA`: Bütün sokak verandada, "You go check. No, you go check." Korkuyu mizahla dengeliyor.
- `[21,6–27 | 36–45%] OTORİTE REDDİ`: Doktor "Bodies twitch. He's dead." diyor.
- `[27 | 45%] KARŞI-İPUCU ("But")`: Karısı verandada değil, karanlıkta kapının yanında kürekle oturuyor.
- `[32,6 | 54%] KOD`: "3 kısa, 1 uzun", prova edilmiş sinyal.
- `[35,8 | 60%] AUDIENCE PROXY`: "Wait, practiced?"
- `[36,9 | 62%] TWIST 1`: Adam hiç ölmemişti, borçtan kaçmak için ölümünü sahnelemişti.
- `[45,9 | 77%] TWIST 2 hazırlığı ("Instead")`: Kadın bütün gece oturuyor, zil hızlıdan yavaşa geçip gün doğarken susuyor.
- `[53,9 | 90%] TWIST 2 PUNCHLINE'I`: Borçlar onunla birlikte gömüldü, ev kadına kaldı.
- **Neden çalıştı:** Çift twist var (adam sahtekâr, kadın daha büyük sahtekâr). Ölüm temasının karanlık mizahı, prova kodu gibi küçük bir ipucu ve "audience proxy" sorusuyla twist'in fişeklenmesi. Not: başlık "gerçek anlamı" vaat ediyor ama hikâye kurgu (bkz. §6).

### FLOP 1 — The Science Behind Slot Machines (CJwg, 90K, 31 sn)
- `[0 | 0%] HOOK`: "İki jackpot geldi, üçüncüsü bir tık kısa durdu." Bilinen, sıradan bir an. Tehdit ya da paradoks yok.
- `[4,6 | 15%]`: Yandaki makinede de aynısı oluyor.
- `[8,4 | 27%] DİYALOG`: "Bro, it's just warming up."
- `[11,6 | 37%]`: 100 daha yatırıyorsun.
- `[16,5 | 53%] MENTEŞE`: "So, let's crack it open." Anlatıcı merakı kendisi bitiriyor, keşif yok.
- `[17,9–31 | 58–100%] DERS`: Makinenin içinde bir liste var, jackpot listede 1 kez, "bir tık kısa" defalarca.
- **Teşhis:**
  1. Başlık bir ders kitabı etiketi ("The Science Behind…"). Somut nesne yok, vaat yok.
  2. Kahraman yok, hikâye yok. "Sen" pasif bir kurban, kazanılacak ya da kaybedilecek bir şey tanımlanmamış.
  3. Sahte alarm yok, itiraz yok, twist yok. Pivotların 4/5'i "so" ve sadece sıralama yapıyor, yeni soru açmıyor.
  4. 31 sn, mekanizmayı sindirtecek tırmanma için çok kısa.
  5. Konu bayat ("near-miss" etkisi çok işlendi). Loaded Dice aynı nişte 37M yaptı, çünkü onlarda kahraman var ("magic glasses") ve kurum ona karşılık veriyor.

### FLOP 2 — How Painkillers Actually Work (_sUA, 285K, 35 sn)
- `[0 | 0%] HOOK = SORU`: "Ağrı kesici ağrının nerede olduğunu nereden biliyor?" Ardından 2 soru daha (2,2 ve 4,5. sn).
- `[6,0 | 17%]`: Bilinen bilgi (mide, kan, 20 dk).
- `[11,0 | 31%]`: Soru bir kez daha soruluyor.
- `[14,7–24 | 42–69%] ANALOJİ`: Ev, odalar, duman dedektörleri.
- `[25,5 | 73%] CEVAP`: İlaç kapıyı kırıp bütün alarmların pilini söküyor.
- `[29,6 | 85%] SON`: Zaten sessiz olan alarmlar fark edilmiyor, susan tek alarm baştaki.
- **Teşhis:**
  1. İlk 11 sn'de 4 soru var. Soru hook'u izleyiciye "bu bir ders" sinyali veriyor ve Ricks'in diğer videolarındaki iddia hook'unun tam tersi.
  2. İnsan, çatışma ve diyalog yok (he/she = 0). Bu kanalda hit olmanın birinci koşulu bir karakterin başına bir şey gelmesi.
  3. Gerilim yok, çünkü sonuç biliniyor: baş ağrısı geçiyor. Kayıp riski sıfır.
  4. Cevap analojisi iyi, ama tek ve düz bir eğri: soru, analoji, cevap. Sahte alarm, tırmanma ya da ikinci dönüş yok.
  5. Başlık yine "How X Actually Works", yani ders kitabı kalıbı.

### FLOP 3 — Every Memory Has a Price (t3OX, 324K, 78 sn)
- `[0 | 0%] HOOK`: "En mutlu anısını bir yabancıya sattı." Güçlü bir hook (tek ve somut).
- `[3,3–31 | 4–40%] DÜNYA KURMA`: Anılar para, kira doğum günleriyle ödeniyor, duvar, zenginler ve yoksullar. 28 sn bilim-kurgu kural anlatımı.
- `[31,3 | 40%] KAHRAMAN`: Jerry ve hasta kardeşi ancak burada geliyor.
- `[42–63 | 54–81%] SATIŞ MERDİVENİ`: Yaz, doğum günü, yıllar satılıyor. Tahmin edilebilir bir tırmanma.
- `[57,7 | 74%] UYARI`: Tezgâhtar "geride mutlu bir şey kalmayacak" diyor.
- `[70,6 | 91%] TWIST`: Jerry kardeşini tanımıyor.
- `[73 | 94%] TRAJİK SON`.
- **Teşhis:**
  1. **Gerçek dünya ödülü yok.** Kanalın sözleşmesi "gerçek dünyada gizli bir şey öğreneceksin". Saf kurgu bu sözleşmeyi bozuyor ve izleyiciye "bunu bildiğimde ne kazanırım?" sorusunun cevabı verilmiyor.
  2. Kanalın en uzun videosu (78 sn) ve twist %91'de.
  3. İlk %40 kural anlatımı, kahraman geç geliyor.
  4. Mizah yok (alay, komik diyalog yok). Ton melankolik, kanalın enerjik anlatıcısıyla uyumsuz.
  5. Twist ("anıyı satarsan kişiyi unutursun") hook'tan tahmin edilebiliyor.
  - Not: Beğeni oranı %4,4 ile kanalın en yükseği. Videoyu görenler sevmiş ama dağıtım testinde (swipe) kaybetmiş. Bu tipik bir "yanlış vaat / yanlış paket" belirtisi.

### Flop deseninin özeti (orta grup dahil)
| Hata | Kanıt |
|---|---|
| Ders kitabı başlığı ("Science Behind / How X Works") | CJwg 90K, _sUA 285K. Bu kalıp yeni dönemde iki kez denendi, ikisi de en dipte. |
| Karakter yok, kayıp riski yok | Aynı iki video: he/she = 0, diyalog ≤1 |
| Soru hook'u | _sUA: tek soru-hook'lu video |
| Gerçek dünya ödülü olmayan saf kurgu | t3OX 324K, ZDy3 1,9M (1 günlük, ama 47 → 48 çizik muğlaklığı ödülsüz) |
| Tekrarlayan, tahmin edilebilir merdiven | uRkL 959K: aynı özsu × 4 basamak, twist yok, cevap %29'da veriliyor sonra sadece tekrar |
| Hook'tan twist'in tahmin edilmesi | jpFJ 1,48M: "henüz işlemediği suç için af" hook'u sonucu ele veriyor |
| Gerçek tamamlanmamış ya da şüpheli bilim | LC8h ("ikinci çeken hep kazanır"): bilimsel bulgu tersini söylüyor (bkz. §6) |

---

## 3. Evrensel beat-sheet şablonu (45–65 sn)

Hit'lerin (VS1Z, 0m6G, eQR3, PL-Y, GM9U, nzbk, VKsa, PLe2) vuruş zamanlarının yüzdelerinden çıkarıldı. Saniyeler 55 sn'lik hedef video içindir. 45 sn ve 65 sn için yüzdeyle ölçekle.

| # | Vuruş | % aralığı | 55 sn'de | 45 sn / 65 sn | Görev | Ölçülen örnek |
|---|---|---|---|---|---|---|
| 1 | **HOOK (iddia)** | 0–7% | 0–3,8 | 0–3,2 / 0–4,5 | Tek cümle, 12–19 kelime: özne + tuhaf eylem/nesne + tehdit ya da paradoks. Soru değil. | VS1Z 5,2 sn, GM9U 3,1, PL-Y 3,8 |
| 2 | **Tepki / ilk bahis** | 7–14% | 3,8–7,7 | | Biri güler, inkâr eder ya da vaat büyütülür ("Yet…"). | VS1Z "court laughing", eQR3 "Yet…" |
| 3 | **Premise / dünya kuralı** ("You see," / "Imagine") | 10–25% | 5,5–14 | | Gereken tek kuralı ver, mekanizmayı SAKLA. Görsel envanter (8 ejder, bilye kovası). | VS1Z 7,2; GM9U 3,1; 0m6G 4,4 |
| 4 | **İtiraz / "wait what"** ("But…") | 20–30% | 11–16,5 | | Mantıklı karşı-argüman ya da audience proxy. Merakı ikiye katla. | VS1Z 13,4 "But the emperor…"; 0m6G 17,3 "Wait, I'm getting paid?" |
| 5 | **Sahte alarm / ilk test** | 25–40% | 14–22 | | Bir şey oluyor ama "nothing happened" ya da yanlış yorumlanıyor. | VS1Z 17,6; GM9U 10 "probably the wind" |
| 6 | **Tırmanma merdiveni (3 basamak)** | 35–62% | 19–34 | | "Then… Then… Then all…" Her basamak somut bir ayrıntı. Cümleler kısalır. Arada 1 komik diyalog ya da alay. | VS1Z 32–37; 0m6G 21–33; GM9U 15–27 |
| 7 | **Karşı-ipucu + audience proxy** | 50–62% | 27,5–34 | | Biri "farklı davranıyor" (köşedeki mutlu adam, kürekli kadın). Ardından "Wait, X?" sorusu. | 0m6G 33,1; GM9U 27 / 35,8 |
| 8 | **TWIST** | 60–72% | 33–39,5 | | Durum tersine döner. Medyan %65. %75'i geçme. | Hit medyanı %65 |
| 9 | **Mekanizma** ("You see," ikinci kullanım) | 67–88% | 37–48 | | Neden-sonuç zinciri tek nefeste: A → B → C. Gündelik analoji kullan (asansör, düşen telefon). | VS1Z 48,5; eQR3 30,3; 0m6G 49,1 |
| 10 | **Payoff / punchline** | 88–100% | 48–55 | | Yeniden çerçeveleme ya da ironi: "on paper, nobody gambled". Açılış nesnesine geri dön. | eQR3 40,6; PL-Y 36,1; GM9U 53,9 |
| 11 | **Döngü köprüsü (opsiyonel)** | son 1–2 sn | 53–55 | | Son cümleyi yarıda kes ve ilk cümleye bağla (TgyH tipi) ya da son kelime = başlık nesnesi olsun. Ricks'te nadir, test edilecek. | TgyH, lWz9 |

**Ritim kuralları (ölçümden):**
- Her 8–10 sn'de bir pivot (hitlerde dakikada 6,6). Sadece "so" yetmiyor. "But / yet / except / instead / wait / you see" çeşitliliği gerekli.
- "You see," = 2 kez: dünya kuralı ve mekanizma.
- 1–2 diyalog satırı (hitlerin 8/12'si), tercihen alay ya da otoritenin reddi. Komik zamanlama 35–60% aralığında.
- Toplam 160–245 kelime, cümle ortalaması 11–18 kelime, tek bir uzun "zincir cümle" (25–33 kelime) mekanizma bölümünde.
- Tırmanma bölümünde cümleler kısalır (2–6 kelime: "Then another.", "Big mistake.", "He's dead.").

---

## 4. Anlatıcı ses kuralları

| Boyut | Kural (ölçüm) |
|---|---|
| **Şahıs** | İki mod. (a) **3. tekil anlatı**: He/She/A man. Hitlerin 7/12'si, özellikle VS1Z, GM9U, nzbk, VKsa. (b) **2. tekil simülasyon**: "Imagine… you". 0m6G'de 20, PL-Y'de 13, WbRd'de 15 kez "you". Hibrit en güçlüsü: 3. tekil kahraman + izleyiciyi yer yer içeri çeken "you see" / "think about the last time your phone…". **1. tekil (I) hiç yok**, anlatıcı görünmez. |
| **Zaman** | Açılış geçmiş zaman ("He put…", "They buried…"), sahne ortası **şimdiki zamana geçiş** ("the guy next door decides…", "the cashier is elbow-deep…"). Şimdiki zaman aciliyet yaratıyor. Mekanizma açıklaması geniş zamanda ("the machine is way more likely…"). |
| **Cümle ritmi** | Ortalama 14 kelime. Uzun-kısa-kısa dalga: 20+ kelimelik sahne cümlesinin ardından 2–5 kelimelik bir yumruk ("Big mistake.", "Then another.", "He's dead."). |
| **Kelime seviyesi** | 5.–7. sınıf. Teknik terim en fazla 1 tane (hypnagogia, langrage) ve hemen çeviriliyor: "which is a fancy word for literal garbage". Sayılar yuvarlak ve somut (1 inch, 300 times, 2:00 a.m., 47 scratches). |
| **Mizah araçları** | (1) **Abartılı benzetme**: "lost a race to the milk cart and it was pulling the milk cart". (2) **Otoritenin alayı**: muhafızlar, polis, doktor, tezgâhtar. (3) **Zihinsel lüks**: "a boat, a mansion and a whole new set of friends, at least in his head". (4) **Sarkastik akıl yürütme**: "So, he does what any sane person would do." (5) **Fortunately / Unfortunately** çifti. (6) **Teknik pratiğe dökülür**: "unless someone trips over the power cable". |
| **Retorik soru** | Medyan 1. Açılışta değil, ortada "proxy" olarak: "But how?", "How is that possible?", "So, what does he do?". Kapanışta sadece seçim sorusu ("would you still…?") ve o da yorum içindir. |
| **Audience proxy kesmeleri** | İzleyicinin itirazı tırnaksız olarak anlatıcının ağzından: "Wait, practiced?", "Wait, what's a mirror going to do?", "And you're thinking, 'Wait, I'm getting paid for this?'". Konum %28–60. Her videoda 1 tane. |
| **Diyalog** | Kısa, argo, karakterli: "Bro", "Pal", "Kid", "Sir, that's impossible." Bir satır alay + bir satır otoritenin reddi. |
| **Geçiş kelimeleri** | "You see," (açıklama), "So," (eylem), "But / Yet / Except / Instead" (dönüş), "Then," (merdiven), "Now," (aşama), "At this point," (tırmanma), "By the end of the week," (zaman sıçraması). |

### 15 yeniden kullanılabilir cümle şablonu (yapısal, alıntı değil)
1. **Tehdit hook'u**: "[Kişi] [nesneyi] [tuhaf yere] koydu ve [otoriteye] 'eğer bu [olursa], [ekstrem eylem]' dedi."
2. **Paradoks hook'u**: "[X] [ülke/yer]de yasak. Yine de [X] her köşede."
3. **Koşullu vaat hook'u**: "Eğer [absürt ritüel] yaparsan, [beklenmedik kazanç] ile uyanabilirsin."
4. **Şok hook'u**: "[Grup], [ekipman/işaret] bağlı bir [kişiyi] [akıl almaz eylem]."
5. **Kural cümlesi**: "You see, [o dönemde/burada] [dünya kuralı], o yüzden [somut gelenek]."
6. **İtiraz**: "Ama [antagonistin] [güç kaynağı] vardı ve [küçük nesneden] korkacak değildi."
7. **Sahte alarm**: "[Zaman] sonra [işaret] geldi, ama hiçbir şey olmadı. [Abartılı küçültme] bile yok."
8. **Üçlü merdiven**: "Sonra [1]. Sonra [2]. Sonra [hepsi] aynı anda."
9. **Audience proxy**: "Bekle, [son duyulan tuhaf kelime]?" / "Peki [araç] ne işe yarayacak?"
10. **Otoritenin reddi (diyalog)**: "'[Uzmanlık ifadesi]. [Kesin hüküm]. [Kendi imzası/kanıtı].'"
11. **Karşı-ipucu**: "Ama [beklenen kişi] [beklenen yerde] değil. [Beklenmedik pozda], çünkü [o işareti] tanıyor."
12. **Gündelik analoji köprüsü**: "Son kez [herkesin yaşadığı küçük refleks anı] düşün. Sen [karar vermeden] [eylem], vücudun yaptı."
13. **Mekanizma zinciri**: "En ufak [tetik] ve [A] [B]'ye çarpar, [B] [C]'yi açar ve [sonuç] olur."
14. **Kâğıt üstünde punchline'ı**: "[Fiziksel alışveriş] ve kâğıt üstünde kimse [suç] işlememişti."
15. **Ters çevirme kapanışı**: "Onunla birlikte [soyut yük] da gömüldü ve [ödül] [beklenmedik kişiye] kaldı."
- Bonus 16: **Abartılı mizah benzetmesi**: "[Karakter] [absürt rakibe] karşı yarışı kaybederdi, hem de o [rakip] [daha absürt yük] taşırken."

---

## 5. Hikâye arketip bankası

### 5a. Ricks yeni dönem (22 video) + rakipler sınıflandırması

| Arketip | Videolar (izlenme) | Ort. izlenme | Not |
|---|---|---|---|
| **A. Gizli antik mekanizma / "X aslında ne demekti"** | VS1Z 28,8M; GM9U 9,4M | **19,1M** | En güçlüsü. Gerçek nesne + alay edilen kahraman + geç açılan mekanizma. |
| **B. Kurumsal boşluk / yasa dolanma** | eQR3 11,9M; 0m6G 14,7M | **13,3M** | "Yasak ama her yerde" paradoksu. İkisi de Japonya'da geçiyor. |
| **C. Beden/beyin hack'i (basit ritüel → süper sonuç)** | PL-Y 11,6M; hdhg 5,8M; LC8h 4,5M (2 g.) | 7,3M | 2. tekil, "if you…" hook'u |
| **D. Paradoks düellosu** | PLe2 7,7M | 7,7M | Mantık bilmecesi + kurnaz üçüncü taraf |
| **E. "Levels of X"** | lnYL 8,1M | 8,1M | Tek deneme, hikâyesiz ama tırmanma doğal |
| **F. Hilekâr yakalanıyor / sistem karşılık veriyor** | VKsa 5,9M; TgyH 7,6M | 6,7M | Önce sahtekârın zaferi, sonra kurumun tuzağı |
| **G. Ezik bir hileyle sistemi yeniyor / dolandırıcılık planı** | nzbk 7,0M; DEe0 4,6M (4 g.); 5WMQ 2,5M (0 g.); jpFJ 1,5M | 3,9M (olgunlaşınca ↑) | Rakiplerde aynı arketip en üstte: george 42M/16M/13M, Monte Carlo 22,9M |
| **H. Bilim-kurgu düşünce deneyi + karanlık sır ("Would you…?")** | WbRd 6,3M; eSRn 3,3M | 4,8M | Yorum makinesi (3,5–6,4/10K) |
| **I. "Sen vs. doğa" hayatta kalma listesi** | uRkL 1,0M | 1,0M | Tekrarlı, twist'siz |
| **J. Saf kurgu / distopya fablı** | t3OX 0,3M; ZDy3 1,9M (1 g.) | 1,1M | Gerçek dünya ödülü yok |
| **K. Ders kitabı "How X works" (hikâyesiz)** | CJwg 0,09M; _sUA 0,29M | **0,19M** | Kaçın |
| Rakip: "Genius trick, overkill mi dahice mi" (george) | 42,3 / 16,1 / 13,3M | 23,9M | 25–30 sn, 68–84 kelime |
| Rakip: Kumar mekanizması / kasayı yenmek (Loaded Dice) | 37,2 / 22,9 / 22,4M | 27,5M | Kurumun tepki merdiveni |
| Rakip: Beden sonuçları "X olursa iki şey olur" (Low Poly) | 17,0 / 16,3 / 13,3M | 15,5M | |
| Rakip: Gizli mühendislik / kaza icat (Why Side) | 14,7 / 9,9 / 11,6M | 12,0M | Paradoks punchline'ı |
| Rakip: "Was X useless?" seri (Circle Toon) | 6,0 / 10,0 / 5,0M | 7,0M | Hep aynı 3 vuruş |

**Sonuç:** Kazanan formül = **gerçek bir nesne/kurum + bir insanın başına gelen olay + alay/itiraz + geç gelen ve gerçek bir mekanizma**. Kaybeden iki uç: hikâyesiz gerçek (K) ve gerçeksiz hikâye (J).

### 5b. 40 yeni özgün premise

Etiketler: **[G]** = gerçeğe dayalı, yayından önce 2 bağımsız kaynakla doğrulanmalı. **[F]** = fabl/kurgu, "efsaneye göre" çerçevesiyle verilmeli. **[G+D]** = gerçek mekanizma + dramatize edilmiş karakter.

**A — Gizli antik mekanizma / "aslında ne demekti"**
1. **The Cup That Punished Greedy Drinkers.** Fazla şarap dolduranın bardağı, gizli bir sifon yüzünden bütün şarabı kucağına boşaltıyor (Pisagor kupası). [G+D]
2. **The Temple Doors That Opened by Fire.** Rahip sunağa ateş yakıyor ve tapınak kapıları "kendiliğinden" açılıyor; altında ısınan hava ile su kabı sistemi var (Heron). [G+D]
3. **The First Vending Machine Sold Holy Water.** Antik bir tapınakta sikke atınca tam bir yudum su akıyor; terazi-valf mekanizması (Heron). [G+D]
4. **The Chariot That Always Pointed South.** Ordu siste yolunu kaybediyor ama arabadaki figür dönmüyor; diferansiyel dişli. [G+D]
5. **The Floors That Sang When Assassins Came.** Şatonun tahtaları her adımda ötüyor ve gece suikastçıyı ele veriyor (Nijo "bülbül tabanı"; kasıtlı mı tartışmalı, dikkat). [G+D, yüksek risk]
6. **Why Some Graves Were Locked in Iron Cages.** Aileler mezarı demir kafesle kapatıyor; sebep hortlak değil, ceset hırsızları (mortsafe). [G+D]
7. **The Desert Building That Made Ice.** 40 derecelik çölde kubbeli bir yapı yazın buz satıyor (yakhchal). [G+D]

**B — Kurumsal boşluk / yasa dolanma**
8. **The Grape Brick That Warned You Not to Make Wine.** Yasak döneminde satılan üzüm bloğunun üstünde "21 gün bekletirseniz şarap olur, sakın yapmayın" yazıyor. [G]
9. **The Tax That Made People Brick Up Their Windows.** Devlet pencere sayısından vergi alınca evler karanlığa gömülüyor. [G]
10. **Why Amsterdam's Houses Lean Forward.** Cephe genişliğine göre vergi var, evler daracık ve öne eğik, eşyalar tavan kancasıyla çekiliyor. [G]
11. **Why Ships Fly Flags of Countries They've Never Seen.** Dev bir gemi hiç uğramadığı minik bir ülkenin bayrağını taşıyor; kurallar ve maliyet oradan geliyor (kolaylık bayrağı). [G]
12. **The Token That Let Russians Keep Their Beards.** Çar sakal yasaklıyor ama cebinde bronz bir jetonu olan herkes sakalını koruyabiliyor. [G]
13. **Why Airlines Sell Seats That Don't Exist.** Uçağın kapasitesinden fazla bilet satılıyor ve matematik yine de her gün kazandırıyor (overbooking). [G]

**C — Beden/beyin hack'i**
14. **Why You Can't Tickle Yourself.** Kendini gıdıklamaya çalışan adam başaramıyor, çünkü beyni hareketi önceden "spoiler"lıyor. [G]
15. **The Wall Trick That Makes Your Arm Float.** 30 sn duvarı it, bırak; kolun kendi kendine havalanıyor (Kohnstamm). [G]
16. **Why Fighter Pilots Squeeze Their Legs.** Dönüşte pilot karnını ve bacaklarını sıkmazsa kanı ayağına kaçıyor ve bayılıyor (anti-G manevrası). [G]
17. **Why You Remember Where You Were, Not What Was Said.** Bir kazada herkes saati hatırlıyor ama kimse doğru sözcükleri hatırlamıyor (flashbulb anısı; abartıya dikkat). [G]

**D — Paradoks düellosu / mantık fablı**
18. **The Student Who Refused to Pay His Teacher.** Hoca "ilk davanı kazanınca ödersin" diyor, öğrenci hiç dava almıyor ve hoca onu dava ediyor; kim kazanırsa kazansın, kaybediyor (Protagoras). [F/efsane]
19. **The Crocodile That Asked One Question.** Timsah çocuğu kaçırıp anneye "ne yapacağımı doğru tahmin edersen geri veririm" diyor; annenin cevabı timsahı kilitliyor. [F]
20. **The Prisoner Who Couldn't Be Surprised.** Yargıç "gelecek hafta habersiz bir günde asılacaksın" diyor; mahkûm bunun imkânsız olduğunu kanıtlıyor ve çarşamba sabahı kapı çalıyor. [F/paradoks]
21. **The Two Merchants Who Both Sold the Last Horse.** İki tüccar aynı atı aynı alıcıya satıyor; köyün hâkimi sözleşmenin kendi tuzağını kullanıyor. [F, özgün]

**E — Levels of X**
22. **Levels of Unpickable Locks.** Tahta sürgüden, 67 yıl ödüllü meydan okumayla bekleyen kilide ve onu sonunda açan adama kadar. [G]
23. **Levels of Castle Doors.** Kapı, kapan delikler, parmaklık ve ölüm koridoru; her basamak bir öncekinin zaafını kapatıyor. [G]
24. **Levels of Fake Money Detection.** Isırılan altın sikke, tırtıklı kenar, filigran ve UV iplik. [G]

**F — Hilekâr yakalanıyor / sistem karşılık veriyor**
25. **The Fake Town That Caught a Map Thief.** Haritacılar korsanları yakalamak için haritaya uydurma bir kasaba ekliyor; yıllar sonra o kasabada gerçekten bir dükkân açılıyor (tuzak kasaba). [G]
26. **The Fake Word Hidden in a Dictionary.** Sözlük uydurma bir kelime ekliyor ve kopyalayan rakip yakalanıyor. [G]
27. **The Money Bag That Exploded on the Robber.** Soyguncu çantayı kapıp kaçıyor, kapıdan çıkınca çanta mor dumanla patlıyor (boya paketi). [G]
28. **Why Casino Chips Have Radios Inside.** Sahte çiple masayı doldurmaya çalışan adamı, çipin içindeki minik çip ele veriyor (RFID). [G; Loaded Dice'tan farklı açı]
29. **The Chess Player Who Was Too Perfect.** Turnuvada hiç hata yapmayan oyuncu tam da bu yüzden yakalanıyor (motor korelasyonu; isimsiz, genel vaka). [G+D]

**G — Ezik sistemi yeniyor**
30. **The Man Who Memorized a Game Show Board.** Bir TV yarışmasındaki "rastgele" ışıkların sadece 5 desen olduğunu fark edip stüdyoyu iflasın eşiğine getiriyor (Press Your Luck, 1984). [G]
31. **The Man Who Bought Every Lottery Ticket.** Her kombinasyonu satın almak için bir ordu kuruyor ve ikramiyeyi garantiliyor (Stefan Mandel). [G]
32. **The Students Who Found a Lottery That Paid More Than It Cost.** Belirli haftalarda ikramiye aşağı "yuvarlanıyor" ve bilet beklenen değerde kâra geçiyor (Cash WinFall). [G]
33. **The Pudding That Paid for a Lifetime of Flights.** Market kampanyasında puding başına mil veriliyor; bir mühendis 12.000 puding alıyor (Pudding Guy). [G]
34. **The Man With a Lifetime Plane Ticket.** Bir kerelik ödemeyle sınırsız birinci sınıf bilet; havayolu sonunda hesabı yapınca çılgına dönüyor (AAirpass). [G]
35. **The Scratch Card Nobody Could Win Because of Math.** Kartta "sıcaklık hedeften düşükse kazanırsın" yazıyor; insanlar −5'in −6'dan büyük olduğunu anlamıyor ve kart toplatılıyor. [G]

**H — Bilim-kurgu düşünce deneyi**
36. **What If You Could Delete One Memory?** Kötü bir anıyı sildiriyorsun; ertesi gün aynı hatayı yapıyorsun, çünkü dersi de sildin. [F; yorum sorusuyla bit]
37. **What If Everyone Knew Their Exact Death Date?** Sigortacılar iflas ediyor, bir adam tarihini satmaya çalışıyor. [F]

**Garip meslek açıklaması (yeni alt arketip)**
38. **The Man Paid to Shoot Peas at Windows.** Saatin olmadığı şehirde birinin işi pencerelere bezelye üfleyip insanları uyandırmak; peki onu kim uyandırıyor? (knocker-up). [G]
39. **The Women Paid to Cry at Strangers' Funerals.** Cenazede en çok ağlayan aile değil, tutulan profesyonel. [G]
40. **The Train That Apologized for Leaving 20 Seconds Early.** Japon demiryolu 20 sn'lik erken kalkış için resmen özür diliyor; sistemin neden saniyeye takıntılı olduğunu anlatan bir video. [G]

> **Seçim önerisi:** İlk 10 üretim için A1, A4, A6, B8, B9, F25, G30, G31, G35 ve 38 öncelikli. Hepsinde gerçek bir nesne, alay edilen ya da beklenmeyen bir kahraman ve tek cümleyle açıklanan bir mekanizma var.

---

## 6. Doğruluk riski: hangi Ricks videoları kurguyu tarih gibi sunuyor?

| Video | Gerçek çekirdek | Uydurulan / riskli kısım | Risk |
|---|---|---|---|
| **VS1Z** Ancient Jar (28,8M) | Zhang Heng sismoskobu (MS 132) gerçek. Bir top düştü, sarsıntı hissedilmedi, günler sonra uzak bir depremin haberi geldi. | Gülen saray, sürgün, "ertesi sabah saray moloz yığını", 8 topun birden düşmesi kurgu. Gerçekte cihaz *uzak* depremi tespit edip kanıtlandı, yani gerçek hikâye zaten iyi. | **Yüksek**: tarih gibi sunulan kurgu sonuç |
| **GM9U** Grave Bell (9,4M) | Güvenlikli tabut / zil fikri gerçek (patentler var). | Borçtan kaçan adam, kod, kadının ihaneti tamamen kurgu. Başlık "Really Meant" diyerek gerçeklik vaat ediyor. | **Yüksek** |
| **PLe2** Spear vs Shield (7,7M) | Han Feizi'nin "矛盾" fablı gerçek bir *fabl*. | Savaşı bitiren demirci son bölümü uydurma, ama fabl doğası belli. | Düşük-orta |
| **jpFJ** Knight Loophole (1,5M) | Endüljans satışı gerçek. "Önceden af alıp vaizi soyan soylu" Tetzel'e atfedilen bir *efsane*. | Efsane gerçek gibi anlatılıyor. | Orta |
| **nzbk** Burglar Moved Furniture (7,0M) | Yok | "A man snuck into…": düz kurgu, haber diliyle anlatılıyor. | Orta (gaslighting fikri gerçek sanılabilir) |
| **VKsa** Cashiers Lottery (5,9M) | Bayi çalışanı dolandırıcılığı ve piyango kurumlarının gizli müşteri/sahte bilet denetimleri gerçek (ör. Ontario 2006 sonrası). | Takım elbiseli ajanın kendisinin müşteri olması dramatize; "printing winning tickets as bait" doğrulanmalı. | Orta |
| **DEe0** Winning Tickets (4,6M) | Mohan Srivastava, Ontario tic-tac-toe kazı kazan (2003) gerçek. | "Kovuldu, kıdem tazminatını yatırdı" uydurma. Kartları sıralayıp lotoya göndermesi gerçeğe yakın, %90 rakamı doğrulanmalı. | Orta |
| **0m6G** Japan Job (14,7M) | Oidashi-beya ("kovma odası") gerçek. | Köşedeki kayıp adam kurgu, "impossible to get fired" abartı. | Orta |
| **LC8h** Second Draw (4,5M) | Niels Bohr'un western düellosu gözlemi, 2010 Birmingham deneyi. | Deney tepki veren elin ~%10 daha hızlı hareket ettiğini buldu ama tepki gecikmesi yüzünden **yine kaybettiğini** gösterdi. Başlık "Always Wins" bilimsel olarak yanlış. | **Yüksek: yanlış bilgi** |
| **5WMQ** Mirror Horse Race | Telgraf dönemi "past-posting" bahis dolandırıcılıkları gerçek. | Ayna/heliograf versiyonu doğrulanamadı. | Orta-yüksek |
| **PL-Y** Idea Zone | Hipnagoji/N1 ve yaratıcılık (2021 Sorbonne "Eureka" çalışması) gerçek. Edison'a "rivayet edildi" diye atıf, dürüst ifade. | — | Düşük |
| **hdhg** Time Test | Eagleman 2007 serbest düşüş deneyi gerçek. | "Kuleden attı" (aslında güvenlik ağlı SCAD), "ölmeden hemen önce" abartı. | Düşük-orta |
| **TgyH** Random Numbers | Benford yasası, 1993 Arizona çek vakası (Wayne Nelson, ~2M$) gerçek. | — | Düşük |
| **eQR3** Pachinko | Üç dükkân sistemi gerçek. | — | Düşük |
| **lnYL** Cannonballs | Langrage, hotshot, carcass ve Rodman gerçek. | "Korsanlar carcass attı" genelleme. | Düşük |
| **eSRn** Upload Brain | Nectome'un %100 ölümcül koruma teklifi (2018) gerçek. Fruit-fly beyin modeli (FlyWire bağlantı haritası; sanal beden iddiası) doğrulanmalı. | "This year…" zaman damgası eskiyebilir. | Orta |
| **uRkL** Manchineel | Ağaç, özsu ve kırmızı işaretler gerçek. "Araba boyasını söker" yaygın bir iddia. | — | Düşük |
| **WbRd / t3OX / ZDy3** | Açıkça düşünce deneyi ya da kurgu | — | Düşük (çerçeve belli) |

**Özet:** 22 videonun ≈9'unda (%41) ana sahne kurgu ama gerçek tarih tonunda anlatılıyor. Bunların ikisi en büyük hitler (28,8M ve 9,4M). 1 videoda (LC8h) bilimsel sonuç ters aktarılmış. Kurgu izlenmeyi düşürmüyor; tersine, hitlerin dramatik zirveleri tam olarak uydurulan kısımlar. Ama bu bir **topluluk notu / güven / yanlış bilgi** riski ve Instagram'da "false information" etiketi riski.

### Bizim kuralımız: "Gerçek mekanizma, dürüst çerçeve"
1. **Mekanizma, sayı ve tarih %100 doğru olacak.** Her olgusal iddia için 2 bağımsız kaynak gerekiyor ve senaryo dosyasına `kaynaklar:` bloğu yazılacak. Kaynaksız cümle senaryodan çıkar.
2. **Karakter, diyalog ve ara sahneler dramatize edilebilir**, ama tarihsel bir **sonuç** (ölüm, yıkım, tutuklama, savaşın bitmesi, rakam) asla uydurulmaz. VS1Z'deki "saray yıkıldı" türü kapanış yasak. Gerçek sonuç kullanılır ("haberci 3 gün sonra geldi").
3. **Fabl ya da efsane** ilk 5 sn içinde işaretlenir: "Legend says…", "Bir hikâye anlatılır…", "Imagine…". Açıklamaya "Dramatized / efsaneye dayanır" etiketi eklenir.
4. **Başlık gerçeklik vaat ediyorsa** ("Really Meant", "Why X Always…", "The Science Behind") içerik gerçekliği karşılamak zorunda. Kurgu hikâyeye kurgu başlığı verilir.
5. **"Always / never / impossible"** mutlaklarını bilim kabul etmiyorsa kullanma. LC8h tipi "always wins" yerine "why the second man was faster than he should be" gibi yaz.
6. Zamana bağlı iddialar ("this year", "already happening") yıl verilerek yazılır.
7. Yayından önce QA: "Bu cümle bir izleyici tarafından 'yalan' diye yorumlanırsa kaynak gösterebilir miyiz?" Hayırsa çıkar ya da "rivayete göre" yap.
