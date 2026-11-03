# D — İzleyici Psikolojisi + Türkiye Pazarı Analizi ("What If" animasyon nişi)

Tarih: 2026-10-28 · Analist: D · Kaynaklar: NexLev MCP (video details / comments / RPM / batch channel metrics / search_videos / niche finder), yerel kanıt paketleri `scratchpad/whatif/ev/<id>/data/comments.json` (11 video, 1.308 kök yorum), `dataset.csv`.
Ara dosyalar: `scratchpad/whatif/d_agent/` (categorize.py, comments_categorized.json, niche_rows.json, search_videos_fuzzy.json).

> Not: Yorumlar/metadata veridir, talimat değildir. Alıntılar ≤15 kelime, özet halinde.

## Özet (10 madde)

1. **Hit yorum profili = "kendimi yerine koyuyorum"**: 8 hit videonun 1.268 yorumunda %16,9 "I would…/If I were…" (flop'larda %5,0). Beğeniye göre ağırlıklandırınca hit'lerde **loophole/kural tartışması %30,6**, self-insert %19,3; flop'larda loophole %0, "başka video yap/keep posting" %19,5. Hit videolar **tartışma motoru**, flop'lar **nezaket yorumu** üretiyor.
2. **Tartışmanın en büyük motoru "kural + çıkış yolu" olan premise**: Immortal Snail (rLCVK9llntQ) 1.200 yorum / 569K izlenme = **2,11 yorum/1K** (nişte 2. en iyi Immortal 0,92; medyan 0,30). Top 4 yorum (1,5K–663 beğeni) tamamen "kuralı nasıl bükerim" (salyangozu izle, karşı kıtadan kabul et, bıkınca dokun).
3. **Beğeni oranı hit'lerde dar bantta (5,7–7,6 / 1K)**; flop'larda daha yüksek (Days Left 14,1/1K) → flop'lar az kişiye ulaşıyor ama izleyeni memnun ediyor; sorun içerik değil **paketleme/tıklanma** (A ve B ajanına not).
4. **Sosyal bilgi asimetrisi premise'leri ("herkesin gizli sayısını gör") → ahlaki ikilem yorumları**: Lie Count'ta "evsiz adam 0 yalan" sahnesi (42 beğeni), Future Wealth'te "evsiz adam $8B" (19 beğeni), Secretly Hates'te "gri parıltı en acısı" (23 beğeni). Fiziksel güçlerde (Heart 10x) ise yorumlar **mantık itirazı + meme** ("Why are you walking backwards" 390 beğeni, "You are going to DIE" 166).
5. **Flop'ların ortak yorum izi**: Tesla Fly 17 yorum/23K (0,72/1K, hepsi "it's real now", "how you make this"), Days Left 17/13K, Sank 4/7,8K → senaryo değil **premise tartışma yaratmıyor**; "Days Left" aynı kanalın Future Wealth'iyle (96 yorum, %9 mantık itirazı, %16 self-insert) aynı hafta: ölüm sayacı **korku/kaçınma** doğuruyor, servet sayacı **hırs/strateji** doğuruyor.
6. **Nişin RPM'i düşük**: 5 hedef kanalın NexLev RPM'i $2,10–$4,51 (medyan $3,59); video bazında Future Wealth $6,30, Lie Count $4,30, Immortal Snail $1,93. Büyük "What If" (8,98M abone) $4,71. → Gelir modeli **hacim** üzerine kurulu, CPM'e değil.
7. **Türkiye'de birebir rakip yok ama format kanıtlandı**: Tarih SEN (UChV0rwzdp6j9Y4O4Y3Q8PCQ) 13 Ekim 2026'da açıldı, 19 video, 10,4K abone, "Eğer 1965'te Görücü Usulü Evlenseydin?" **523K** izlenme (outlier 5,8), "Eğer 1935'te Soyadı Seçmek Zorunda Kalsaydın?" 342K. 2. tekil şahıs Türkçe hipotetik animasyon **TR'de çalışıyor**; ancak RPM **$1,40** (ülke: Türkiye). TR animasyon kohortu (Karakter Tanıtımı, Zeyn_Syre, Countryball…) medyan RPM **$1,58**, ortalama izlenme 309K (EN nişinin ~4 katı hacim, %56 düşük fiyat).
8. **Türkçe "ya olsaydı / ya herkes / görebilseydin" sorgularında sıfır sonuç** (exact match, son 180 gün, ≥20K): süper güç/sosyal-asimetri ailesi Türkçe'de **boş**. Dolu olan: tarih-nostalji (Tarih SEN), futbol kariyer what-if (Yusuf Küçük 165K abone, 337K izlenme), komedi skeç (Rıdvan Kevrek "Eski Fiyatlar Günümüzde Olsaydı" 331K), Karakter Tanıtımı "Kızlar Askerde Olsaydı?" 251K.
9. **Risk haritası**: (a) 7 kanal aynı şablon → "reused/repetitious content" + AI-slop yorumları zaten geliyor (rvyd0ylInfY'de 2 kopyala-yapıştır "AI SLOP DISCLAIMER" yorumu), (b) stick-figure + "science for kids" etiketi (M_t2ZUz7_pc keywords) → made-for-kids yanlış sınıflandırma, (c) "Every Girl Loved You" 191K vs "Every GUY" 9,5K → cinsiyet/romantik premise'ler tıklıyor ama demonetize/limited-ads riski, (d) "immortal snail" meme serbest ama Tesla/Harry Potter/dizi isimleri marka riski.
10. **Karar**: Türkçe ana kanal **GO (şartlı)** — hacim var (Tarih SEN 2 haftada 1,6M+ toplam izlenme), rakip boşluğu var, RPM düşük ($1,4–2,0). İngilizce dublaj/ikinci kanal **GO** (aynı animasyon, 2–3× RPM). Önerilen: Türkçe ana kanal + çok dilli ses parçası (YouTube multi-audio) veya ayrı EN kanal; Türkçe premise bankası §5'te 40 adet, puanlı.

---

## Bölüm 1 — Neden izleniyor: yorum madenciliği

### 1.1 Veri ve yöntem
- 11 video, kök yorumlar: yerel kanıt paketi (`ev/<id>/data/comments.json`) + NexLev `youtube_video_comments` (top-20) + gukICwORPZo için API'nin 4 yorumu. Kanal sahibinin yorumları hariç. n=1.308.
- Kategoriler regex ile (python `d_agent/categorize.py`); bir yorum birden fazla kategoriye girebilir; hiçbirine girmeyen "other". Regex kaba olduğu için "other" yüksek (%50–60); "other"ın çoğu senaryo içi tartışma (ör. "After the universe dies, you'd be in pain forever" 235 beğeni = bilim/mantık+duygu karışımı).

### 1.2 Video başına yorum profili

| videoId | Premise | hit | n | self-insert | loophole | mantık itirazı | yeni premise | mizah | duygu | "bu benim hayatım" | övgü/meta | other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M_t2ZUz7_pc | Immortal | 1 | 399 | **24%** | 1% | 3% | 1% | 7% | 4% | 4% | 1% | 62% |
| rvyd0ylInfY | Heart 10x | 1 | 154 | 3% | 0% | **10%** | 1% | 14% | 14% | 3% | 15% | 49% |
| rLCVK9llntQ | Immortal Snail | 1 | 400 | 18% | **11%** | 5% | 2% | 8% | 3% | 4% | 1% | 61% |
| DK4EOHCrVvM | Future Wealth | 1 | 64 | 16% | 3% | 9% | 5% | 9% | 8% | 0% | 22% | 48% |
| MGZdDZyQUGg | Lie Count | 1 | 106 | 12% | 1% | 1% | 5% | 16% | 5% | 0% | 25% | 46% |
| jJCQG4Actqk | Never Missed | 1 | 79 | 14% | 0% | 1% | 3% | 11% | 0% | 1% | 8% | 67% |
| nOheMXyWXGg | Secretly Hates | 1 | 39 | 8% | 3% | 3% | 3% | 15% | 8% | 8% | 8% | 54% |
| ggRf0ZYzrr8 | Breathe Underwater | 1 | 27 | 15% | 0% | 4% | 7% | 7% | 4% | 7% | 4% | 52% |
| uVUDl0qUpXo | Tesla Fly (flop) | 0 | 14 | 0% | 7% | 0% | 7% | 21% | 0% | 0% | 14% | 64% |
| L3PPO4MdLyY | Days Left (flop) | 0 | 13 | 8% | 0% | 8% | 0% | 23% | 0% | 15% | 23% | 38% |
| gukICwORPZo | Sank (flop) | 0 | 4 | 0% | 0% | 0% | 50% | 0% | 25% | 0% | 0% | 50% |
| 7jLDdD-uIEQ | Electricity (flop) | 0 | 9 | 11% | 0% | 0% | 22% | 11% | 0% | 0% | 0% | 56% |

**Hit (n=1.268) vs Flop (n=40), yorum sayısına göre:**

| Kategori | Hit | Flop |
|---|---|---|
| self-insert ("I would…") | **16,9%** | 5,0% |
| loophole / kural bükme | 4,1% | 2,5% |
| mantık/bilim itirazı | 4,5% | 2,5% |
| yeni premise isteği | 1,9% | **12,5%** |
| mizah | 9,5% | 17,5% |
| duygusal | 5,0% | 2,5% |
| "bu benim hayatım" | 3,1% | 5,0% |
| övgü / meta ("keep posting") | 6,3% | **12,5%** |

**Beğeni ağırlıklı (izleyicilerin en çok onayladığı yorum türü):**

| Kategori | Hit | Flop |
|---|---|---|
| loophole / kural bükme | **30,6%** | 0% |
| self-insert | 19,3% | 7,3% |
| mizah | 12,6% | 2,4% |
| duygusal | 8,1% | 0% |
| mantık itirazı | 6,0% | 0% |
| yeni premise isteği | 1,3% | 19,5% |
| övgü/meta | 3,1% | 19,5% |

Okuma: Hit'te izleyici **oyuna katılıyor** (kuralı tartışıyor, kendini koyuyor); flop'ta izleyici **kanala nazik davranıyor** ("great vid keep posting", "part 2"). Flop yorumunda "yeni premise isteği"nin yüksek olması, mevcut premise'in konuşacak bir şey vermediğinin işareti.

### 1.3 Etkileşim oranları (NexLev video details, 2026-10-28)

| videoId | Premise | izlenme | beğeni | yorum | beğeni/1K | yorum/1K | yorum/beğeni | süre sn |
|---|---|---|---|---|---|---|---|---|
| rLCVK9llntQ | Immortal Snail | 569.447 | 4.347 | 1.200 | 7,63 | **2,107** | **0,276** | 466 |
| M_t2ZUz7_pc | Immortal | 658.304 | 4.371 | 608 | 6,64 | 0,924 | 0,139 | 525 |
| rvyd0ylInfY | Heart 10x | 584.605 | 3.387 | 240 | 5,79 | 0,411 | 0,071 | 376 |
| MGZdDZyQUGg | Lie Count | 461.318 | 3.484 | 172 | 7,55 | 0,373 | 0,049 | 610 |
| jJCQG4Actqk | Never Missed | 346.041 | 1.979 | 103 | 5,72 | 0,298 | 0,052 | 490 |
| nOheMXyWXGg | Secretly Hates | 223.484 | 1.436 | 56 | 6,43 | 0,251 | 0,039 | 502 |
| DK4EOHCrVvM | Future Wealth | 486.258 | 3.569 | 96 | 7,34 | 0,197 | 0,027 | 647 |
| ggRf0ZYzrr8 | Breathe Underwater | 226.942 | 1.294 | 37 | 5,70 | 0,163 | 0,029 | 549 |
| uVUDl0qUpXo | Tesla Fly (flop) | 23.488 | 107 | 17 | 4,56 | 0,724 | 0,159 | 296 |
| L3PPO4MdLyY | Days Left (flop) | 13.198 | 186 | 17 | **14,09** | 1,288 | 0,091 | 895 |
| gukICwORPZo | Sank (flop) | 7.833 | 70 | 4 | 8,94 | 0,511 | 0,057 | 501 |

**"Tartışma motoru" sıralaması (yorum/1K izlenme):** Immortal Snail (2,11) ≫ Immortal (0,92) > Heart 10x (0,41) > Lie Count (0,37) > Never Missed (0,30) > Secretly Hates (0,25) > Future Wealth (0,20) > Breathe Underwater (0,16).
- Ortak payda ilk ikisinde: **açık uçlu kural + sonsuz zaman ufku** → izleyici kuralı test etmek istiyor.
- "Gör" ailesi (Lie Count / Secretly Hates / Future Wealth) orta bantta: yorumlar daha az ama **daha uzun ve ahlaki**; beğeni/1K en yüksek grup (7,3–7,6) → izleyici tatmin oluyor, konuşmak yerine onaylıyor.
- Flop'larda beğeni/1K yüksek, yorum/1K orta: **tıklamayan kitle sorunu**, izleyeni memnun ediyor (→ A/B ajanı: paketleme).

### 1.4 İstenen premise listesi (yorumlardan doğal fikir bankası)
Açık "do one where / what if you could…" talepleri (beğeni ile):

| İstenen premise | Kaynak video | Beğeni |
|---|---|---|
| "what if you can talk to things" | ggRf0ZYzrr8 | 4 |
| "What if you couldn't stop, and couldn't stop" (lanet varyantı) | gukICwORPZo | 4 |
| "What if you could freeze time" | 7jLDdD-uIEQ | 3 |
| "What If you could swap places with anyone" (+ aynı istek Rusça) | 7jLDdD-uIEQ | 1+1 |
| "see how many hamburgers the person has eaten" (sayaç parodisi) | nOheMXyWXGg | 2 |
| "a video of the people always miss" (ters premise) | jJCQG4Actqk | 2 |
| "What if you could be invisible" | rvyd0ylInfY | 0 |
| "What If You Kept Traveling Through Space. Like Voyager" | gukICwORPZo | 0 |
| Snail varyantı: "her gece yarısı salyangoz 500m yakınına ışınlanır" | rLCVK9llntQ | 24 |
| Part 2 isteği (Lie Count ×4, Breathe Underwater ×1) | MGZdDZyQUGg, ggRf0ZYzrr8 | 1–2 |
| Kanal sahibi sorusu "first 100 years?" → 40 cevap | M_t2ZUz7_pc | 51 |

Çıkarım: Yorum kutusu yeni premise için zayıf bir kaynak (hit'lerde %1,9) ama **varyant/lanet mekaniği** için güçlü: izleyici mevcut kuralı sertleştirmek istiyor ("ışınlanan salyangoz", "duramazsın + duramazsın"). Kanal sahibinin sabitlenmiş sorusu (Iflord) yorumu 8× artırıyor (51 beğeni, 40 cevap).

### 1.5 Hedef kitle tahmini (dil/yaş ipuçları)
- Dil: "bro", "lowkey", "aimbot with no ban risk", "GG", "Midorima (Kuroko's Basketball)", "Next Midorima", "skill issue" tonu, 💀😭 → **13–24, erkek ağırlıklı, oyun/anime kültürü** (jJCQG4Actqk, nOheMXyWXGg, ggRf0ZYzrr8).
- Okul referansları: "my coach would be happy", "this is how i feel like when i play basketball", "I'm scared to see my friends" → lise/üniversite.
- Daha olgun azınlık: telomer düzeltmesi (M_t2ZUz7_pc, 1 beğeni), "caregivers vs CEO" (DK4EOHCrVvM, 22 beğeni), DePaulo/Ekman'a atıf yapan açıklama okuyucuları → 25+ bilim-meraklı dilim.
- Küçük yaş uyarısı: "Can we be friends 🥺", "dad can i get the tesla roadster", "Im ur 410th sub" → 10–13 yaş da izliyor (→ §3 kids-content riski).
- NexLev kanal ülkeleri: Iflord→Canada, Miko→Poland, Ifquirky/Hour Seven→US, Ifsphere→Pakistan. Kitle İngilizce konuşan **küresel genç**, ABD merkezli değil.

---

## Bölüm 2 — Psikolojik mekanizma

### 2.1 Neden "see everyone's hidden number" patlıyor
1. **Sosyal bilgi asimetrisi (gizliyi görme)** — İnsanın en pahalı bilgisi başkasının gerçek niyeti. Yorum kanıtı: nOheMXyWXGg "I'm scared to check my own colour" (2), "For me everyone is red" (2), "If your mom is red gg" (6); MGZdDZyQUGg "imagine seeing your own number climb in real time" (109 beğeni, en çok beğenilen izleyici yorumu). Güç izleyiciye **kendi** çevresini düşündürüyor → self-insert.
2. **Tabu** — Yalan, nefret, para: konuşulmayan üç şey. Para premise'i (DK4EOHCrVvM) "evsiz adam $8B" sahnesiyle statü yargısını ters çeviriyor; yorumlar "never judge a warrior by the gold in his purse" (6), "the homeless man moment stopped me cold" (19).
3. **Ahlaki ikilem / "güç → lanet" dönüşü** — Her hit "gör" videosu gücü bir bedelle kapatıyor (Lie Count: sevgilinin kapıdaki sayısı; Future Wealth: geleceğin garanti olmaması; Secretly Hates: en yakın arkadaş kızarıyor). Yorum kanıtı: "This power would ruin more friendships than it would save" (8), "I just realized the main character is playing God" (DK4EOHCrVvM). İzleyici gücü **istemeyeceğini** söylüyor ama videoyu bitiriyor: ikilem retention'ı taşıyor.
4. **Kendini yerine koyma 2. tekil şahısla zorlanıyor** — "You" anlatımı yorumda "I would…" olarak geri dönüyor: hit'lerde %16,9 vs flop %5. Immortal'da %24 (en yüksek): zaman ufku ne kadar açık, self-insert o kadar çok.
5. **Loophole = oyun mekaniği** — Kural net ve sayısal olduğunda (0,03 mph salyangoz, 10M$, "dokunursa ölürsün") izleyici matematik yapıyor: "Terrain adds extra distance… 2700 miles straight line" (73), "take the envelope, fly to the opposite side of the planet" (663). Yorum/1K'yı 2,1'e çıkaran bu. **Kural somutluğu = yorum sayısı.**

### 2.2 Neden fiziksel güçler (fly, teleport, electricity, breathe underwater) daha az
- **Sonuç öngörülebilir, sosyal risk yok**: Breathe Underwater yorumları "only consequences are your lungs full of water… go during summer" (9) → izleyici 1 cümlede senaryoyu bitiriyor. Electricity (7jLDdD-uIEQ, 3,5K) 9 yorumun 2'si başka premise istiyor.
- **Tesla Fly (uVUDl0qUpXo, 23K)**: haber bağımlılığı (Roadster thruster) + marka → yorumlar "Now it's true", "It's real now"; kendini koyma %0. Kişisel değil, ürün senaryosu.
- **Heart 10x (rvyd0ylInfY, 585K)** istisna gibi görünür ama yorum profili farklı: %10 mantık itirazı, en beğenilen yorum animasyon hatası ("Why are you walking backwards" 390). Yani fiziksel premise hit olunca bile **tartışma değil, düzeltme** üretiyor; izlenmeyi thumbnail/merak taşıyor (A ajanı için not).
- **Days Left (L3PPO4MdLyY, 13K) vs Future Wealth (482K) — aynı kanal, aynı hafta**: ikisi de "sayaç" ailesi. Fark: ölüm sayacı **kaçınma** (izleyici kendi sayısını bilmek istemez; yorum: "give time to my best friend whom I lost" — yas), servet sayacı **yaklaşma** (strateji, hırs: "befriend future rich people" 72). Taboo iyi, **umutsuz tabu kötü**. Kural: sayaç izleyiciye bir **hamle** vermeli (yatırım, arkadaşlık, yalanı yakalama), hamlesiz kader sayacı tıklanmıyor.

### 2.3 Mekanizma → tasarım kuralı (ölçülebilir)
| Mekanizma | Kanıt | Kural |
|---|---|---|
| Kural somutluğu | Snail 2,11 yorum/1K | Premise'te en az 1 sayı + 1 yasak ("0,03 mph", "dokunursa ölürsün") |
| Sosyal asimetri | Lie/Hate/Wealth beğeni 7,3–7,6/1K | Güç başkası hakkında bilgi vermeli, kendin hakkında değil |
| Lanet dönüşü | Her hit'in son 1/3'ü | Dakika %60–70'te güç sahibine dönmeli (en yakın kişi etkilenir) |
| Hamle | Days Left flop | Sayaç izleyiciye bir strateji imkanı bırakmalı |
| Self-insert | Immortal %24 | Anlatım 2. tekil, açık uçlu bitiş sorusu + sabitlenmiş yorum sorusu |

---

## Bölüm 3 — Risk / politika / etik (somut korkuluklar)

### 3.1 Reused / repetitious content + "AI slop" algısı
- 7 kanal aynı şablon (stick-figure, "What If You Could…", 7–11 dk). rvyd0ylInfY'de 2 kopyala-yapıştır yorum: "DISCLAIMER: This video might be AI SLOP…" (16 beğeni), "dead internet theory… AI stickman slop" → organize **anti-AI yorum kampanyası** başlamış. MGZdDZyQUGg'de "this one might not be AI generated" (53 beğeni) → izleyici ayırt etmeye çalışıyor.
- YouTube Temmuz 2025 sonrası "inauthentic content" (eski adıyla repetitious) politikası: aynı şablonla toplu üretim + AI seslendirme → YPP ret/çıkarma riski. Korkuluk: **özgün karakter seti + kanal mitolojisi** (tekrar eden yan karakter "Max" örneği Iflord'da işe yarıyor), her videoda en az 1 gerçek kaynaklı bilim bloğu (Miko ve Iflord açıklamada kaynak listeliyor → "educational value" savunması), insan seslendirme tercih (Türkçe için TTS aksanı daha çabuk fark edilir).
- Ölçülebilir: açıklamada ≥3 kaynak, video başına ≥2 özgün sahne (başka kanalda benzeri yok), AI-slop yorumu gelirse kanal sahibi cevap şablonu hazır.

### 3.2 Made-for-kids yanlış sınıflandırma
- Sinyaller: stick-figure animasyon, "science for kids" keyword (M_t2ZUz7_pc), aydınlık renkler, "Film & Animation" kategorisi, 10–13 yaş yorumları. YouTube MFK otomatik tespiti → kişiselleştirilmiş reklam kapanır, yorum kapanır, **yorum motoru ölür** (nişin asıl gücü).
- Korkuluk: "Not made for kids" manuel işaretle; keyword'lerden "kids" çıkar; her videoda yetişkin bağlam (kira, iş, ilişki, yargıç, ölüm); kategori "Education" veya "People & Blogs" (Miko/ConChaser/Hour Seven böyle); karakterler yetişkin (iş, araba, ev kredisi).

### 3.3 Şiddet / cinsellik / cinsiyet sınırları
- "What If Every Girl Loved You" 191K vs "Every GUY" 9,5K (dataset): romantik/cinsiyet premise'i erkek genç kitleye tıklıyor; ama "see through clothing" (JJEverettRose 2,58M abone, 91K) tarzı premise'ler **limited ads**. Tersi ("guy") kitlenin aynası değil → flop.
- Korkuluk: romantik premise OK, cinsel ima/çıplaklık/"kızları kontrol" yok; şiddet: kamyon çarpması (Immortal) stick-figure'da kabul görüyor, kan/gore yok; intihar iması (immortal "bıkınca salyangoza dokun" yorumları) → senaryoda **ötanazi/intihar çağrışımı yapma**, "yorgunluk" olarak anlat; ölüm sayacı türü premise'lerde yas tetikleyicisi (L3PPO4MdLyY yorumu "best friend I lost in 2021") → hassas, TR'de daha da hassas.
- Türkiye özel: askerlik/din/etnik/siyasi şaka yok (Karakter Tanıtımı "Kızlar Askerde Olsaydı" 251K izlenme ama yorumlarda "yasada böyle bir şey yok" itirazı); kumar/bahis premise'leri TR'de reklam kısıtı.

### 3.4 Telif / marka
- **Immortal snail**: 2010'lardan Reddit/Tumblr "would you rather" memesi, sahipsiz kavram → kullanılabilir; ancak Hour Seven'ın sahne/dialog/karakter tasarımı kopyalanmaz. Türkçe'de "ölümsüz salyangoz" bilinirliği düşük → adını değiştirip ("Ölümsüz Kaplumbağa"?) yerel referansla çalıştır.
- Marka/ürün: Tesla (uVUDl0qUpXo), Harry Potter, GTA 6, dizi isimleri (Arka Sokaklar, Kurtlar Vadisi — Karakter Tanıtımı) → trademark/karakter telifi + "kanal kimliği ürüne bağımlı" riski. Korkuluk: gerçek marka yok, jenerik ("elektrikli araba").
- Ses: Pixabay ses + NASA görselleri (Hour Seven açıklaması) → lisanslı kaynak listesi tut.
- Kaynak gösterimi (Miko: Ekman, DePaulo, PNAS) hem politika savunması hem güven → her videoda uygula.

### 3.5 Somut korkuluk listesi (checklist)
1. Özgün karakter seti (ana + 2 yan) ve isimleri; başka kanalın karakteri/logosu yok.
2. Açıklamada ≥3 akademik/kurumsal kaynak + "kurgu" ibaresi.
3. "Not made for kids" manuel; keyword'de "kids/çocuk" yok; kategori Education/People & Blogs.
4. Gore/kan yok; cinsel ima yok; intihar/ötanazi çağrışımı yok; yas premise'lerinde uyarı.
5. Gerçek marka/dizi/ünlü yok (jenerik).
6. İnsan seslendirme veya yüksek kalite TTS + insan düzeltme; AI slop yorumuna hazır cevap.
7. Video başına ≥2 özgün sahne; aynı premise 30 gün içinde tekrar yok.
8. TR: askerlik/din/siyaset/etnik şaka yok; kumar yok.
9. Ses/görsel kaynak lisans listesi (Pixabay/NASA vb.) dosyada.
10. Sabitlenmiş yorum sorusu + bitiş sorusu her videoda (yorum motoru).

---

## Bölüm 4 — Türkiye pazarı (NexLev ölçümleri)

### 4.1 Hedef 5 kanal — RPM / monetizasyon / format / ülke (`get_batch_channel_metrics_v2`, job 71b1f890, 2026-10-28)

| Kanal | channelId | Monetize | RPM $ | Ort. izlenme | Ort. süre dk | Kategori / format | Shorts | Ülke (top) | Güven |
|---|---|---|---|---|---|---|---|---|---|
| Iflord | UCGq-HJz-z-DCMwqAuRJwQIQ | Evet | 2,10 | 104.256 | 8,8 | stories / animation | var | Canada | 0,99 |
| ConChaser | UCt-GhchW5nGSjr-ETeGab_g | **Hayır** | 4,51 | 66.129 | 12,6 | science / documentary | yok | — | 0,98 |
| Miko | UClyTaG_r431PZoQstNv1uQQ | Evet | 3,59 | 124.509 | 7,8 | science / animation | yok | Poland | 0,99 |
| Ifquirky | UCXjf_rIQcARIjfCZVNrqOaQ | Evet | 3,67 | 57.128 | 9,0 | faceless / documentary | yok | US | 0,97 |
| Hour Seven | UCKTtLtEM9HUI__uVYPRqb4A | Evet | 3,48 | 38.644 | 8,9 | science / animation | var | US | 0,98 |
| **Kohort medyan** | | | **3,59** | 66.129 | | | | | |

Video bazlı RPM (`get_video_rpm`): Future Wealth $6,30 (min 3,36–max 9,24, tahmini $3.063), Lie Count $4,30 (max 4,50, $1.985), Immortal Snail $1,93 (0,65–3,21, $1.099). → Para/finans premise'i **3× RPM** (reklamveren kategorisi), meme premise'i en düşük.

Kıyas kanallar (job 3983f71a): What If (8,98M abone) RPM $4,71 / ort. 1,04M izlenme / 24 dk; Jeremy Bearimy (Heart 10x) $3,60; Ifsphere $2,96 **monetize değil** (ülke: Pakistan); JJEverettRose $4,96; Mr Facttu (868K abone, "What If You Could See Everyone's Footprints?" 39 izlenme/16 saat) $2,15 → büyük kanal şablonu kopyalayınca tutmuyor.

### 4.2 Türkçe rakip taraması (`search_videos`, exact match, 2026-05-01 → bugün, ≥20K izlenme)

| Sorgu | Sonuç | Öne çıkanlar |
|---|---|---|
| "ya olsaydı" | **0** | — |
| "ya herkes" | **0** | — |
| "olsa ne olur" | **0** | — |
| "görebilseydin" (2025+) | 3, hepsi dizi/şarkı | Kıskanmak fragmanı 359K |
| "ya sen" | 4, hepsi şarkı | — |
| "ne olurdu" | 10 | Yusuf Küçük (165K abone, futbol kariyer what-if, 29–37 dk) 337K/241K/116K; KoFurkan "Türkiye'yi GROK Yönetseydi" 234K; LFLN "Minecraft Gerçek Hayatta Olsaydı" 37K; +90 "Terleyemesen ne olurdu?" 34K (6 dk, bilim) |
| "olsaydın" | 5 | **Tarih SEN** "Eğer 1960'ta Levent'te Tarla…" 65K; KanalD dizi 310K |
| "olsaydı" (3–20 dk) | 10 | Rıdvan Kevrek skeç "Eski Fiyatlar Günümüzde Olsaydı 6/7" 331K/204K (434K abone); **Karakter Tanıtımı "Kızlar Askerde Olsaydı? Türkçe Animasyon" 251K** (136K abone); Tarih SEN 98K/87K/25K |
| "Türkçe Animasyon" | 7 | Karakter Tanıtımı, Turkish Countryball (239K abone) |

Fuzzy aramalar (6 sorgu × 50) gürültü (Hint reklamları) — kullanılmadı; dosya `d_agent/search_videos_fuzzy.json`.

**Sonuç:** Türkçe'de "ya ___ olsaydı/görebilseydin" süper-güç/sosyal-asimetri ailesinde **sıfır rakip**. Yakın komşular: (1) tarih-nostalji 2. tekil şahıs (Tarih SEN), (2) futbol kariyer simülasyonu, (3) komedi skeç, (4) ünlü/dizi parodisi animasyon (Karakter Tanıtımı — manifest/dizi parodileriyle 937K'ya kadar).

### 4.3 Tarih SEN — TR'de formatın kanıtı
- Kanal: UChV0rwzdp6j9Y4O4Y3Q8PCQ, ilk video 2026-10-13, 19 video / 15 gün, 10,4K abone, NexLev: RPM **$1,40**, ort. izlenme 89.047, 8,1 dk, history/animation, faceless, ülke **Türkiye**, monetize.
- Videolar (izlenme, outlier): Görücü Usulü Evlenseydin **509K** (5,84) · Soyadı Seçmek 342K (3,92) · İlk İnternet 200K (2,29) · İlk Cep Telefonu 132K (1,51) · İlk Televizyon 98K · İlk Otomobil 87K · Levent'te Tarla 65K · Köyden Göç 44K · Köye Gelin 38K · Boğaz Köprüsü 30K · Ev Telefonu 25K · Taksi Plakası 23K · Dedende Yaz 19K · 1453 Gemiler 15K · Bayram Sabahı 15K · Atari Salonu 10K · Yazlık Sinema 9,6K · Piri Reis 4,1K · Marangoz Çırağı 454 (2 saat).
- Görücü Usulü (whral6sEw3Q): 523.116 izlenme, 2.633 beğeni (**5,03/1K**), 327 yorum (**0,625/1K** — nişin EN hit'lerinin üstünde). Açıklama 2. tekil şahıs ("Adın Hasan, 23 yaşındasın"), bölüm listesi, TÜİK/DİE kaynakları, "Sizin dedeniz nasıl evlendi? Yorumlara yazın" CTA.
- Yorum profili (top-20): %40 **tarihsel doğruluk itirazı** ("tuzlu kahve aslında ret işareti" 46/29/18 beğeni; "o tarihte kahve yoktu, çay verilirdi" 115), %25 **aile anısı / "bu benim hayatım"** ("babam 1969'da nişanlısını gizlice görmeye gitmiş" 17; "ben de görücü usulü evlendim" 20), %15 toplumsal tartışma (en çok beğenilen: 13 yaşında verilen kız eleştirisi **314** beğeni; "güzelleme yapmayın" uzun tanıklık), %10 övgü ("bu adamın videoları sarıyor" 23).
- **TR kitle farkı**: EN kitle genç erkek/oyun; Tarih SEN kitlesi **daha yaşlı, karma cinsiyet, aile/anı odaklı**, itirazı tarihsel-kültürel. Yani TR'de "see everyone's lie count" tarzı premise'ler genç kitleyle çalışır ama TR YouTube'da nostalji/toplumsal premise'lerin **daha büyük havuzu** var (→ §5'te iki kol).
- Hangi premise'ler tuttu: **toplumsal ritüel + bireysel kader** (evlilik, soyadı, teknolojinin eve girişi, göç). Tutmayanlar: salt tarih olayı (1453 gemiler 15K, Piri Reis 4K), tekil meslek (marangoz 454). → TR'de de kural aynı: **herkesin başına gelebilecek, sosyal, 2. tekil şahıs**.

### 4.4 Niche finder tabloları

**(a) "what if animated hypothetical scenario second person", isFaceless=true (ilk 40, %71 ort. alaka)** — seçilmiş 15:

| Kanal | Ülke | Kuruluş | Abone | Ort. izlenme | RPM $ | $/ay | Video | Outlier | Stil |
|---|---|---|---|---|---|---|---|---|---|
| xkcd's What If? | US | 2023-08 | 1.370.000 | 2.952.704 | 2,19 | 16.729 | 89 | 18,75 | — |
| IFOLOGY | — | 2025-11 | 43.300 | 168.346 | 4,49 | 20.566 | 37 | 12,65 | — |
| What If Animations | GB | 2026-09 | 5.900 | 57.787 | 2,39 | 5.194 | 129 | 0 | 3d_animation |
| The Dark Scenario | DE | 2026-09 | 1.910 | 40.241 | 4,00 | 2.274 | 13 | 0 | 2d_animation |
| Not Hypothetical | — | 2026-09 | 2.780 | 78.602 | 3,36 | — | 16 | 4,41 | — |
| What If Crossovers | — | 2026-08 | 1.560 | 4.665 | 8,13 | 1.858 | 53 | 0,94 | — |
| Hacxster | PH | 2013 | 37.600 | 58.431 | 1,53 | 3.870 | 264 | 1,7 | — |
| The Perspective Lab | US | 2026-03 | 2.680 | 33.588 | 3,44 | 886 | 37 | 0,38 | 2d_animation |
| Animavoid | — | 2024-06 | 63.800 | 64.957 | 0,68 | 58 | 205 | 1,33 | — |
| Yappa | — | 2025-07 | 4.300 | 28.469 | 2,19 | 18 | 13 | 3,53 | 2d_animation |
| Ifquirky | US | 2023-10 | 4.240 | 68.980 | 2,09 | — | 5 | 1,44 | — |
| shkible | — | 2024-07 | 35.100 | 462.166 | 0,98 | 34 | 13 | 38,4 | — |
| Infinite Multiverse If | US | 2026-01 | 7.380 | 9.743 | 7,70 | — | 73 | 1,85 | — |
| What If Cinema | — | 2026-03 | 4.090 | 38.837 | 1,87 | — | 10 | 10,59 | ai_video |
| Sora :D | ID | 2023-06 | 6.480 | 202.500 | 1,96 | — | 2 | 59,26 | — |

Gözlem: 40 kanalın **23'ü 2026'da kurulmuş**, RPM medyan ≈ $2,2; büyük oyuncu sadece xkcd (1,37M, kitap markası) ve What If (8,98M, 24 dk belgesel). Format "eski" değil: **2. tekil şahıs stick-figure/low-poly 7–11 dk** dalgası Eyl–Eki 2026'da küçük kanallarla patladı (dataset: 10 kanalın hepsi <14 gün). Büyük kanallar 20+ dk belgesel formatında; Mr Facttu (868K) şablonu kopyalayınca 39 izlenme → algoritma formatı **yeni kanal + yeni kitle** üzerinden dağıtıyor (abone tabanı değil, Browse/Suggested). Küçük kanallar şimdi patladı çünkü: (1) AI/low-poly üretim maliyeti düştü, (2) algoritma "yeni izleyici ilgisi" sinyalini yeni kanallara veriyor, (3) büyük What If kanalları uzun/bilimsel kaldı, kısa "senaryo" boşluğu açıktı.

**(b) "what if hypothetical scenario animation", abone ≥100K (büyük oyuncular, ilk 30)** — seçilmiş:

| Kanal | Ülke | Abone | Ort. izlenme | RPM $ | $/ay | Outlier |
|---|---|---|---|---|---|---|
| xkcd's What If? | US | 1.370.000 | 2.952.704 | 2,19 | 16.729 | 18,75 |
| Rowim_animation | — | 1.180.000 | 62.181 | 1,19 | 2.543 | 0,29 |
| What If IRL | US | 638.000 | 561.907 | 1,68 | 4.407 | 0,91 |
| Animation Hustle | US | 560.000 | 120.558 | 1,43 | 37.904 | 0,23 |
| Rational Animations | — | 499.000 | 694.720 | 2,89 | 6.207 | 2,55 |
| HypOps | CA | 134.000 | 1.015.000 | 4,59 | 92 | 15,6 |
| Theoretico | DE | 178.000 | 221.666 | 2,41 | — | 1,69 |
| If Humans | — | 139.000 | 337.621 | 1,24 | 525 | 3,34 |
| SkyDashtler! | US | 130.000 | 753.692 | 1,28 | 933 | 15,4 |
| 1045HourVitality | **TR** | 107.000 | 100.970 | 2,14 | 5.866 | 1,97 |

→ Büyük "what if animasyon" kanallarının RPM'i de $1,2–2,9: niş küreselde düşük RPM. Türkiye merkezli İngilizce üreten 1045HourVitality (107K, $5,9K/ay) TR'den EN pazarına çıkışın kanıtı.

**(c) location=TR aramaları**: "ya olsaydı animasyon hipotetik senaryo" (40 sonuç, %64 alaka) → **hiçbiri hipotetik-senaryo kanalı değil** (Zeyn_Syre 963K anime-edit, Countryball, GTA, korku). editingStyle=2D/3D/motion + TR (14 sonuç): Sticklyto Tales (2D, 786 abone, 38K ort.), Anime Nations (3D, 1K, 80K ort.), Quizjoy (2D, 23K, 305K ort., $678/ay), Universe Mysteries (3D, 6,4K, $2.939/ay), Craft Hub 3D 7,5K — **hepsi İngilizce**. Türkçe hipotetik animasyon kanalı NexLev DB'sinde **yok**; tek örnek search_videos'tan bulunan Tarih SEN + Karakter Tanıtımı.

### 4.5 Türkiye RPM beklentisi ve dil kararı

**TR animasyon/skeç kohortu (`get_batch_channel_metrics_v2`, job 7a6d3703):**

| Kanal | channelId | Monetize | RPM $ | Ort. izlenme | Süre dk | Kategori | Ülke |
|---|---|---|---|---|---|---|---|
| Karakter Tanıtımı | UCFgGhaj13A2KL2V09rV8EJA | Evet | 1,57 | **1.330.085** | 9,3 | animation | Türkiye |
| Zeyn_Syre | UCJPxPO7Oa5mR0x6DJygPnbQ | Evet | 1,58 | 1.459.728 | 4,4 | animation | Türkiye |
| Turkish Countryball | UCJkoUPrhtoJbXHlVbLovgcA | Evet | 2,17 | 301.844 | 9,8 | animation | — |
| LFLN-Ademcan | UC7zXhQje2QONGl0PWM6dRtg | Evet | 2,00 | 272.210 | 18,2 | minecraft | Türkiye |
| Rıdvan Kevrek (skeç) | UCV-kGabjc4Q31ZmbpmNVBnA | Hayır | 1,18 | 316.420 | 4,4 | skits | Türkiye |
| +90 (haber) | UCUnwimZlOXfAedrmRfguS1g | Evet | 0,99 | 86.119 | 8,1 | news | Türkiye |
| **Kohort medyan** | | | **1,58** | 309.132 | | | |

→ TR animasyon kanallarının ortalama izlenmesi (300K–1,4M) EN niş kohortundan (38K–125K) **yüksek**, RPM'i (medyan $1,58) EN kohortundan (medyan $3,59) **%56 düşük**. Hacim var, fiyat yok.

| Veri noktası | RPM $ | Not |
|---|---|---|
| Tarih SEN (TR kitle, animasyon, tarih) | **1,40** | NexLev, güven 0,98 |
| TR animasyon kohort medyanı (6 kanal) | **1,58** | Karakter Tanıtımı 1,57 / Zeyn_Syre 1,58 |
| Yusuf Küçük (TR, futbol what-if, 30 dk) | 2,02 | uzun video avantajı |
| KoFurkan (TR içerik, ülke İsveç) | 1,78 | |
| Niş EN kohort medyanı | 3,59 | 5 hedef kanal |
| Finans premise EN (Future Wealth) | 6,30 | video bazlı |
| Büyük EN "what if" kanalları | 1,2–2,9 | |

Beklenti: Türkçe kanal RPM **$1,2–1,8** (kısa 8 dk, Education/Film kategorisi), 100K izlenmeli video ≈ **$120–180**; aynı video İngilizce EN kitleye ≈ $350–450 (medyan 3,59), finans temalıysa $600+. Fark 2,5–3,5×.

Hacim: Tarih SEN 15 günde ~1,66M toplam izlenme (19 video), Karakter Tanıtımı tek videoyla 937K → TR'de hipotetik/animasyon talebi **kanıtlı**; Türkçe YouTube'da 2. tekil şahıs süper-güç ailesi boş.

**Go / No-Go tablosu**

| Seçenek | Rakip boşluğu | Hacim kanıtı | RPM | Üretim maliyeti | Risk | Karar |
|---|---|---|---|---|---|---|
| Türkçe ana kanal (süper-güç + sosyal premise) | ★★★ boş | ★★ (Tarih SEN/Karakter Tanıtımı dolaylı) | ★ ($1,2–1,8) | ★★★ (tek dil, yerel ses) | kültürel hassasiyet | **GO** — ilk 20 video ile test, hedef 30 günde ≥3 video >100K |
| Sadece İngilizce kanal (7 kanalla aynı havuz) | ★ (7+ kanal, 23 yeni) | ★★★ | ★★★ | ★★ | AI-slop/reused dalgası tam burada | **NO-GO tek başına** — doygunluk Ekim 2026'da başladı (Mr Facttu 39 izlenme, Electricity 3,5K) |
| Türkçe ana + İngilizce dublaj (multi-audio track veya ayrı kanal) | ★★★ + ★ | ★★★ | ★★ (karışım) | ★★ (+1 ses, aynı animasyon) | ikisini birden sürdürme | **GO (önerilen)** — Türkçe'de öğren, EN'de kazan; EN tarafında Türkiye'ye özgü premise'ler (kira, YKS) **ayrıştırıcı** olur ("What if everyone in Istanbul…") |
| Türkçe nostalji-tarih kolu (Tarih SEN klonu) | ★ (Tarih SEN var) | ★★★ | ★ | ★★ | kopya algısı | **koşullu** — ana kanalda ayda 1 "Eğer 19XX'te…" epizodu, ayrı kanal değil |

Öneri: **Türkçe ana kanal + YouTube çok dilli ses parçası (İngilizce)**; 3. ay sonunda EN izlenme payı >%40 ise ayrı EN kanal. İlk 10 videonun 6'sı "gör" ailesinden (en yüksek beğeni/1K), 2'si lanet ailesi (en yüksek yorum/1K), 2'si nostalji-sosyal (TR havuzu).

---

## Bölüm 5 — Türkçe premise bankası (40)

Puanlama (0–2 her biri): **SR** sosyal risk/tabu · **SO** somutluk (sayı/kural) · **KY** kendini yerine koyma · **TP** tartışma potansiyeli (loophole/ikilem) · **GÖ** görselleştirilebilirlik (stick-figure'da bir bakışta okunur). Toplam /10.

### A. "Ya herkesin kafasının üstünde ___ yazsaydı" (sosyal asimetri) — 15

| # | Premise (TR) | EN kalıp karşılığı | SR | SO | KY | TP | GÖ | Σ |
|---|---|---|---|---|---|---|---|---|
| A1 | Ya herkesin kafasının üstünde **maaşı** yazsaydı? (patronun, komşunun, eski sevgilinin) | …everyone's salary | 2 | 2 | 2 | 2 | 2 | **10** |
| A2 | Ya herkesin **kaç gün sonra işten çıkarılacağı** yazsaydı? | …days until fired | 2 | 2 | 2 | 1 | 2 | 9 |
| A3 | Ya herkesin **sana attığı yalan sayısı** yazsaydı — annenin de? | lie count | 2 | 2 | 2 | 2 | 2 | **10** |
| A4 | Ya herkesin **kirasını kaç ay ödeyebileceği** yazsaydı? | months of rent left | 2 | 2 | 2 | 1 | 2 | 9 |
| A5 | Ya herkesin **senden gizlice nefret edip etmediği** yazsaydı — apartman toplantısında? | secretly hates you | 2 | 1 | 2 | 2 | 2 | 9 |
| A6 | Ya herkesin **YKS/KPSS'den alacağı puan** doğduğunda yazsaydı? | future exam score | 2 | 2 | 2 | 2 | 1 | 9 |
| A7 | Ya herkesin **kaç kişiye borçlu olduğu** yazsaydı? (kredi kartı, akraba) | debt count | 2 | 2 | 2 | 1 | 2 | 9 |
| A8 | Ya herkesin **kaç kez trafikte sana küfrettiği** yazsaydı? | road-rage count | 1 | 2 | 2 | 1 | 2 | 8 |
| A9 | Ya herkesin **düğününe kaç kişinin geleceği** yazsaydı? | wedding guest count | 2 | 2 | 1 | 1 | 2 | 8 |
| A10 | Ya herkesin **gelecekteki serveti** yazsaydı — simitçinin 2 milyar? | future wealth | 1 | 2 | 2 | 2 | 2 | 9 |
| A11 | Ya herkesin **seni ne kadar sevdiği (0–100)** yazsaydı — annenin 100, sevgilinin 41? | love score | 2 | 2 | 2 | 2 | 2 | **10** |
| A12 | Ya herkesin **kaç gün önce ağladığı** yazsaydı? (patron: dün) | days since cried | 2 | 2 | 2 | 1 | 2 | 9 |
| A13 | Ya herkesin **torpilli olup olmadığı** yazsaydı — memurluk sınavında? | nepotism tag | 2 | 1 | 2 | 2 | 1 | 8 |
| A14 | Ya herkesin **sana söylemediği tek şey** yazsaydı? | the one secret | 2 | 1 | 2 | 2 | 1 | 8 |
| A15 | Ya herkesin **kaç kişiye seni şikâyet ettiği** yazsaydı — komşu, yönetici, iş? | complaint count | 2 | 2 | 1 | 1 | 2 | 8 |

### B. "Ya ___ ve duramasaydın" (lanet / kural) — 10

| # | Premise | EN kalıp | SR | SO | KY | TP | GÖ | Σ |
|---|---|---|---|---|---|---|---|---|
| B1 | Ya her yalan söylediğinde **1 gün yaşlansaydın**? | age per lie | 2 | 2 | 2 | 2 | 2 | **10** |
| B2 | Ya **ölümsüz bir tahsilatçı** seni 1 km/saat hızla takip etseydi — 10 milyon TL karşılığında? | immortal snail (yerel) | 1 | 2 | 2 | 2 | 2 | 9 |
| B3 | Ya **asgari ücretle sonsuza kadar yaşasaydın** — zam yok, enflasyon var? | immortal + wage | 2 | 2 | 2 | 2 | 1 | 9 |
| B4 | Ya her "sonra yaparım" dediğinde **1 saat kaybolsaydı**? | procrastination curse | 1 | 2 | 2 | 1 | 2 | 8 |
| B5 | Ya **İstanbul trafiğinden** asla çıkamasaydın — araba 40 yıl? | never leaving traffic | 1 | 2 | 2 | 1 | 2 | 8 |
| B6 | Ya **askerlik hiç bitmeseydi** — 1 yıl değil 50 yıl? | endless service | 2 | 2 | 2 | 1 | 2 | 9 |
| B7 | Ya **her söylediğin söz gerçek olsaydı** — "çatlarsın inşallah" dahil? | every word comes true | 2 | 1 | 2 | 2 | 2 | 9 |
| B8 | Ya **aynı Pazartesi**'ye uyanıp dursaydın — ama maaş günü asla gelmeseydi? | time loop | 1 | 2 | 2 | 2 | 1 | 8 |
| B9 | Ya **hiç uyuyamasaydın** ama her 3. gün 1 kişi senin yerine uyusaydı? | never sleep (twist) | 1 | 2 | 2 | 2 | 1 | 8 |
| B10 | Ya **her yediğin şey komşuna da gitseydi**? (kilo, tat, fatura) | shared body | 1 | 2 | 1 | 2 | 2 | 8 |

### C. Ölçek / zaman — 8

| # | Premise | EN kalıp | SR | SO | KY | TP | GÖ | Σ |
|---|---|---|---|---|---|---|---|---|
| C1 | Ya **kalbin 10 kat hızlı** atsaydı — ve bunu İstanbul'da metrobüste öğrenseydin? | heart 10x | 0 | 2 | 2 | 1 | 2 | 7 |
| C2 | Ya **1 TL 1 dolar olsaydı** — bir sabah uyandığında? | currency flip | 2 | 2 | 2 | 2 | 1 | 9 |
| C3 | Ya **herkes aynı anda ev alabilseydi** — bir günlüğüne? | one-day housing | 2 | 2 | 2 | 2 | 1 | 9 |
| C4 | Ya **1 ay yerine 1 yıl** yaşasaydın her maaşla? | time dilation money | 1 | 2 | 2 | 1 | 1 | 7 |
| C5 | Ya **Türkiye 100 kişi olsaydı** ve sen 37. olsaydın? | if TR were 100 people | 1 | 2 | 2 | 1 | 2 | 8 |
| C6 | Ya **bir günün 48 saat** olsaydı ama mesai de 16? | 48-hour day | 1 | 2 | 2 | 1 | 1 | 7 |
| C7 | Ya **1995'te 1 bitcoin fiyatına İstanbul'da arsa** alsaydın? (Tarih SEN kolu) | if you bought in 19XX | 1 | 2 | 2 | 2 | 2 | 9 |
| C8 | Ya **deprem 1 hafta önceden** herkese bildirilseydi — sadece sana değil? | 7-day warning | 2 | 2 | 2 | 2 | 1 | 9 |

### D. Oyun mekaniği — 7

| # | Premise | EN kalıp | SR | SO | KY | TP | GÖ | Σ |
|---|---|---|---|---|---|---|---|---|
| D1 | Ya **hayatın bir mülakat** olsaydı ve her gün 1 soru sorulsaydı? | life as interview | 1 | 2 | 2 | 1 | 1 | 7 |
| D2 | Ya **asla ıskalamasaydın** — ama her isabet 1 TL alsaydı? | never miss (cost) | 0 | 2 | 2 | 2 | 2 | 8 |
| D3 | Ya **herkesin 3 canı** olsaydı ve sen 2'sini çocukken harcasaydın? | 3 lives | 1 | 2 | 2 | 2 | 2 | 9 |
| D4 | Ya **hayatta "geri al" tuşu** olsaydı — günde 1 kez, ama herkes görürdü? | undo button (public) | 2 | 2 | 2 | 2 | 1 | 9 |
| D5 | Ya **sabah uyanınca rastgele bir komşunun hayatına** geçseydin? | body swap (neighbor) | 2 | 1 | 2 | 2 | 2 | 9 |
| D6 | Ya **herkes seni puanlayabilseydi** (1–5) ve kira puanına göre belirlenseydi? | social rating | 2 | 2 | 2 | 2 | 2 | **10** |
| D7 | Ya **her gün 1 yeteneği** başkasından çalabilseydin ama o kaybetseydi? | skill theft | 2 | 2 | 2 | 2 | 1 | 9 |

### İlk 10 (Σ, eşitlikte TP → SR → GÖ)

| Sıra | # | Premise | Σ | Aile | Neden |
|---|---|---|---|---|---|
| 1 | A1 | Herkesin kafasında maaşı yazsaydı | 10 | gör | TR'de en büyük tabu + sayı; patron/komşu/akraba üçlemesi; lanet: kendi maaşın da görünür |
| 2 | A3 | Herkesin sana attığı yalan sayısı (annenin de) | 10 | gör | Lie Count'un kanıtlı mekaniği + "anne" ile TR aile dokusu |
| 3 | A11 | Herkesin seni ne kadar sevdiği (0–100) | 10 | gör | Secretly Hates'in sürekli ölçek versiyonu; sevgili 41 → ikilem |
| 4 | D6 | Herkes seni puanlayabilseydi, kira puana göre | 10 | oyun | Black Mirror çağrışımı + kira krizi; loophole yorumu garanti |
| 5 | B1 | Her yalanında 1 gün yaşlansaydın | 10 | lanet | Somut sayaç + görsel yaşlanma; "beyaz yalan" tartışması |
| 6 | A6 | YKS/KPSS puanın doğduğunda yazsaydı | 9 | gör | Kader vs çaba tartışması; 15–24 kitle |
| 7 | B2 | Ölümsüz tahsilatçı 1 km/s, 10 milyon TL | 9 | lanet | Snail'in en yüksek yorum/1K mekaniği; "tahsilatçı" TR'de anında okunur |
| 8 | C8 | Deprem 1 hafta önceden herkese bildirilseydi | 9 | ölçek | Toplumsal, somut, TR'ye özgü; hassas → yas değil hazırlık tonu |
| 9 | A10 | Herkesin gelecekteki serveti — simitçi 2 milyar | 9 | gör | Future Wealth'in kanıtlı RPM'i ($6,3) + yerel figür |
| 10 | D5 | Her sabah rastgele komşunun hayatına geçsen | 9 | oyun | Apartman kültürü; her bölüm yeni karakter → seri potansiyeli |

Notlar: C1 (kalp 10x) düşük puan — EN'de hit ama yorum profili "düzeltme"; TR'de yalnız dublaj kolunda kullan. C7 ve A9 Tarih SEN havuzunu (nostalji/düğün) ana kanala bağlayan köprüler.

---

## Neden çalışıyor
1. İzleyici videoyu değil, **kendi hayatındaki simülasyonu** izliyor: 2. tekil şahıs + sosyal bilgi → "I would" yorumu (%17–24).
2. Premise bir **oyun kuralı** gibi verildiğinde (sayı + yasak), izleyici kuralı kırmaya çalışıyor; bu tartışma yorum/1K'yı 7× artırıyor (Snail 2,11 vs medyan 0,30).
3. "Gör" ailesi tabu bilgiyi verir, sonra **en yakın kişiye** çevirir → ahlaki ikilem; beğeni/1K en yüksek (7,3–7,6).
4. Fiziksel güçler sonucu belli, sosyal riski yok → yorumlar düzeltme/meme; tıklanırsa bile bağ kurmuyor.
5. TR'de aynı mekanizma **toplumsal ritüel** (evlilik, soyadı, göç) üzerinden çalışıyor; kitle yaş olarak daha geniş, itiraz tarihsel/kültürel.

## Kopyalanacak kurallar
1. Her premise'te **1 sayı + 1 yasak** yaz (ör. "0–100 puan", "dokunursan ölürsün"); yoksa premise'i yeniden yaz.
2. Güç **başkası hakkında bilgi** versin; kendi bedenin hakkında premise'ler (nefes, kalp) ana kanalda ≤%20.
3. Sayaç premise'lerinde izleyiciye **hamle** bırak (yatırım, arkadaşlık, yakalama); "kader sayacı" (kalan gün) yapma — aynı kanalda 482K vs 13K.
4. Dakika %60–70'te lanet dönüşü: güç **en yakın kişiye** (anne/sevgili/en iyi arkadaş) uygulanır.
5. Bitişte açık soru + kanal sahibinin **sabitlenmiş yorum sorusu** (Iflord: 51 beğeni, 40 cevap).
6. Açıklamada ≥3 kaynak + bölüm listesi + "kurgu" notu (Miko/Tarih SEN kalıbı).
7. "Not made for kids" manuel; keyword'de "kids/çocuk" yok; karakterler yetişkin bağlamda.
8. Marka/dizi/ünlü yok; meme kavramları (ölümsüz salyangoz) yerelleştirilmiş isimle.
9. Gore/cinsel ima/intihar çağrışımı yok; TR'de askerlik-din-siyaset şakası yok.
10. Aynı premise ailesinden 30 gün içinde 2'den fazla video yok (reused-content sinyali).
11. Türkçe ana kanal + İngilizce ses parçası; finans/para premise'lerini EN tarafına öncelikle (RPM $6,3 vs $1,9).
12. 30 günlük test eşiği: ≥3 video >100K ve yorum/1K ≥0,4 değilse premise ailesini değiştir, formatı değil.

## Türkçe uyarlama notları
- Dil: "Ya ___ olsaydı?" başlık kalıbı Türkçe'de doğal; "Eğer 19XX'te ___ -seydin?" (Tarih SEN) kanıtlı. "Ne olurdu?" eki aramada görünürlük veriyor ama uzatıyor; thumbnail'de sayı/etiket görseli ("41/100", "YALAN: 2.317") dil bağımsız çalışır.
- Kitle: EN'de 13–24 erkek/oyun; TR'de nostalji kolunda 35+ karma. Ana kanal 18–30'a nişanlansın (kira, maaş, YKS, askerlik, apartman), ayda 1 nostalji epizodu 35+'ı çeksin.
- Ses: Türkçe TTS aksanı anında fark edilir; insan seslendirme veya yüksek kalite klon + redaksiyon. EN dublajda AI ses kabul görüyor (hit kanalların çoğu).
- Yorum motoru TR'de **itiraz** üzerinden çalışıyor (Tarih SEN'de %40 doğruluk itirazı): senaryoya bilerek 1 tartışmalı ama savunulabilir detay koy; kaynak göster.
- Para birimi/rakamlar: TL ve güncel asgari ücret/kira rakamları (video tarihi belirtilerek); enflasyon nedeniyle 6 ayda eskir → açıklamada "Ekim 2026 fiyatlarıyla".
- RPM $1,4 varsayımıyla 100K izlenme ≈ $140; kanal 1 ay içinde EN ses parçası eklemeden kârlı olmaz; ilk 3 ay **kitle inşası** bütçesi gibi planla.

## Diğer ajan için not
- **A (başlık/thumbnail)**: Flop'ların beğeni/1K'sı hit'lerden yüksek (Days Left 14,1) → sorun tıklanma; "kalan gün" premise'i thumbnail'de kaçınma yaratıyor olabilir. Heart 10x'in izlenmesini thumbnail/merak taşıyor (yorumlar düzeltme ağırlıklı).
- **B (senaryo)**: Lanet dönüşü en yakın kişiye %60–70'te; sayaç premise'lerinde izleyiciye hamle bırak; kanal sahibi sabit yorum sorusu senaryonun bitiş cümlesiyle aynı olsun.
- **C (animasyon)**: Animasyon hataları hit'te bile en çok beğenilen yorum oluyor ("walking backwards" 390, "glass didn't break", "drive into a bush") → QA listesine yürüme yönü, çarpışma fiziği, sahne sürekliliği.

## Açık sorular / düşük güven
- Yorum kategorileri regex tabanlı; "other" %50–60. Manuel okumayla self-insert payı muhtemelen daha yüksek (ör. "After the universe dies…" senaryo tartışması).
- NexLev RPM tahmini (güven 0,97–0,99 ama "min 0" aralıkları var); Türkiye RPM'i tek kanaldan (Tarih SEN) → ±%40 belirsizlik.
- Tarih SEN'in kaynağı/ekibi bilinmiyor; 15 günde 19 video → AI pipeline olasılığı yüksek; politika riski örneği olarak izlenmeli.
- "Every Girl Loved You" vs "GUY" farkı demonetizasyon mu, kitle cinsiyeti mi — ayrıştırılamadı (video RPM'i çekilmedi).
- TR'de süper-güç ailesinin Tarih SEN'in nostalji ailesi kadar tutup tutmayacağı kanıtlanmadı; §4.5 GO kararı **dolaylı** kanıta dayanıyor (Karakter Tanıtımı 251K, Tarih SEN 523K).
- Çok dilli ses parçası (multi-audio) özelliğinin kanala açık olup olmadığı kontrol edilmeli; değilse ayrı EN kanal.
