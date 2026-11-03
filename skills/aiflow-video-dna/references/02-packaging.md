# 02 — Paketleme: başlık, thumbnail, açıklama, etiket, sabit yorum

Kaynak: `deep-research/01-packaging-ctr.md` (ölçümler, piksel koordinatları, kanal benchmark tabloları).

## 1. Başlık

### 1.1 Kazanan iskelet
```
How To Make Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER} {NICHE} Niche)
```
| Parça | Görev |
|---|---|
| `How To Make Videos Like` | aday yaratıcıların baskın arama kalıbı |
| `{SUCCESS_CHANNEL}` | ödünç otorite + arama yakalama + o kanalın izleyicisine "önerilen" komşuluğu |
| `With AI` | kolaylık / düşük maliyet vaadi |
| `({MONEY_QUALIFIER} {NICHE} Niche)` | para + kategori; mobilde kesilse bile thumbnail tekrarlıyor |

Ölçüler: 69 karakter / 13 kelime · Title Case · sayı, emoji, "|" ve yıl yok · varlık adı 35. karakterde bitiyor ·
"viral / insane / secret" gibi abartı kelimesi yok — para vaadi parantezde.
Başlık ve thumbnail işi bölüşür: başlık = **varlık + yöntem**, thumbnail = **kategori + bütünlük + kanıt + çıktı önizlemesi**.
Thumbnail kanal adını yazmaz; o kanalın *türünü* gösterir.

### 1.2 Kurallar
1. Kanal adı "@" olmadan; tam **bir** parantez; "| keyword" kuyruğu **yok**; ≤ 75 karakter; varlık 40. karakterden önce bitsin.
2. "Full Course" başlığa yazılmaz (başlıkta medyan 8,7K) → thumbnail hapına konur.
3. `{SUCCESS_CHANNEL}` seçimi: **≤ 200 video, ≥ 50K abone, son 6 ayda ≥ 500K izlenmiş en az 1 video.** Kendi yorumlarında ≥ 2 kez istenen kanal öncelikli.
   (Bizde: `competitor-radar` skill'i outlier'ları bu filtreyle verir.)
4. Para nişi (finans, high-RPM, USA audience) amiral videolara.

### 1.3 Kanalın kazanan başlık aileleri (kanıtlı)
1. Named model channel — "How To Make Videos Like {X} ({niş/para})" → 196K, 144,5K, 117K, 73K, 60K
2. İçeriden fedakârlık — "I Bought {X}'s Paid Course So You Don't Have To" → 168K
3. Birinci şahıs inşa — "How I Create Viral AI {Format} Videos from Scratch (Free Tools)" → 264K, 146K
4. Yeni niş aciliyeti — "How to Make AI {Format} Videos in {Year} – New Viral Niche Exploding Right Now (Full Tutorial)" → 278K
5. Büyük sonuçlu seri — "…That Get Millions of Views (Step-by-Step) | Part 2" → 230K
6. Clone-any — "Clone Any YouTube Channel with Claude AI (No Coding, 100% Free)" → 159K
Zayıf aileler: niş listeleri (3,2K), araç haberleri (6,1K), "bu kanal N izlenme aldı" vakaları (5,2K).

### 1.4 25 şablon
1. How To Make Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER} {NICHE} Niche)
2. How To Make Videos Like {SUCCESS_CHANNEL} ({GEO} {NICHE} Faceless Channel Reveal)
3. How To Make {NICHE} Videos Like {SUCCESS_CHANNEL} With AI (Full Course)
4. How I Make Videos Like {SUCCESS_CHANNEL} Using Only AI ({MONEY_QUALIFIER} Niche)
5. How To Make {FORMAT} Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER})
6. I Bought {SUCCESS_CHANNEL}'s Paid Course So You Don't Have To
7. How I Create {MONEY_QUALIFIER} {NICHE} Videos Using ONLY AI
8. How To Make Videos Like {SUCCESS_CHANNEL} With FREE AI Tools ({NICHE} Niche)
9. Zero Experience? How To Make Videos Like {SUCCESS_CHANNEL} With AI
10. How To Make Videos Like {SUCCESS_CHANNEL} With AI (Evergreen {NICHE} Niche)
11. How To Make Videos Like {SUCCESS_CHANNEL} With AI (Part 2: {STEP})
12. How To Make Videos Like {SUCCESS_CHANNEL} With {TOOL} ({MONEY_QUALIFIER} {NICHE} Niche)
13. How To Start a {NICHE} Channel Like {SUCCESS_CHANNEL} With AI (Full Course)
14. How I Built a {NICHE} Channel Like {SUCCESS_CHANNEL} Using Only AI
15. How To Make {NICHE} Videos Like {SUCCESS_CHANNEL} in {YEAR} ({MONEY_QUALIFIER})
16. {NICHE} Videos Like {SUCCESS_CHANNEL} Are Blowing Up – Here's How To Make Them With AI
17. How To Make Videos Like {SUCCESS_CHANNEL} With AI (New {MONEY_QUALIFIER} Niche)
18. How To Make Long {NICHE} Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER})
19. How To Make Videos Like {SUCCESS_CHANNEL} and {SUCCESS_CHANNEL_2} With AI ({NICHE} Niche)
20. How To Make Videos Like {SUCCESS_CHANNEL} With AI ({GEO} Audience, {MONEY_QUALIFIER})
21. How To Make Videos Like {SUCCESS_CHANNEL} With AI (No Editing Skills Needed)
22. How I Recreate the {SUCCESS_CHANNEL} Style With AI ({NICHE} Niche Full Course)
23. How To Make {FORMAT} {NICHE} Videos Like {SUCCESS_CHANNEL} (100% FREE AI)
24. How To Make Videos Like {SUCCESS_CHANNEL} With AI ({N} Videos, {MONEY_QUALIFIER} Niche)
25. How To Make Faceless {NICHE} Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER})

Türkçe kanal için aynı iskelet: `{SUCCESS_CHANNEL} Gibi Video Nasıl Yapılır? Yapay Zekâyla ({PARA} {NİŞ} Nişi)` — varlık başta, tek parantez.

> Finans-anlatım ürün videolarının (Mod F) başlıkları farklıdır: ≤ 60 karakter, tek merak kalıbı
> ("Why everything changes after $X", "The X trap that keeps people poor", "The hidden cost of X", "Why most people stay broke").
> Bkz. `07-finance-explainer-style.md`.

## 2. Thumbnail — "house template" (1280×720)

Kanalın sabit şablonu; her videoda sadece **konu kelimesi, konu rengi, 4 örnek kart ve kanıt sayısı** değişir.

### 2.1 Izgara (% W × % H)
```
y 0–46   [KART TL 3–41% x 3–46%]   (teal oluk 41–59%)   [KART TR 59–97% x 4–46%]
y 35–49  ███ {KONU} (sarı gradyan) ███  NICHE (gümüş) ███   başlık bandı, merkez (49%, 41%)
y 53–64          [■ FULL COURSE ■ hap 35–65%]
y 52–89  [KART BL]                                          [KART BR]
y 75–96          ┌ [logo] [logo] │ VIEWS / {GERÇEK SAYI} VIEWS (yeşil ↑) ┐  kanıt paneli 24–75%
y 83–100 $$$$$$$$$ yeşil banknot yığını, tam genişlik $$$$$$$$$
```
Okuma yolu: başlık → hap → kanıt paneli → kart başlıkları. Mobilde (168×94) kalan üç mesaj: **{KONU} NICHE · karikatür para örnekleri · para**.

### 2.2 Katman spesifikasyonu (alttan üste)
| Katman | Spec |
|---|---|
| L0 Arka plan | Radyal gradyan merkez (50%,45%) r=75%: `#086F77` → 45% `#08445E` → 100% `#091841`. Dikey ışık şeridi x 43–57%, `#0FA3A8` %25 opaklık, blur 60 px |
| L1 4 örnek kart | 38% W × 41% H; TL(3,3) TR(59,4) BL(3,52) BR(59,53); dolgu `#E4E4E6` + %3 kâğıt gürültüsü; dönüş TL −2° TR +2° BL +1° BR −1°; gölge 0 10 28 rgba(0,0,0,.45). İçerik: **kendi özgün maskotumuz** kartın sol %40'ında; sağda 2–3 satır Anton/Oswald 700 `#050505`, en büyük kelime %9–13 H; siyah el çizimi kavisli ok (8 px); tek niş objesi |
| L2 Para bandı | y 83–100%, yeşil banknot `#0A760A` + vurgu `#2FBF3A`; kartların altına %3–5 H taşar |
| L3 Başlık halesi | başlık kopyası `#0B1F1A`, blur 22 px, %85, ofset (0,+6) — **taşıyıcı katman** (sarı/soluk kart kontrastı 1,2:1 → hale ile 8,4:1) |
| L4 Başlık | tek satır, merkez x 50%, cap yüksekliği **%13–14 H**, genişlik **%82–88 W**. Kelime 1 `{KONU}` Montserrat Black 900, dikey gradyan (finans `#F7C41E → #F7B409`); kelime 2 `NICHE` (veya COURSE/METHOD/CHANNEL) gümüş `#C6C8CA → #F6F7F8 → #CBCDD1`; **sert kontur yok** |
| L5 Hap | yuvarlatılmış dikdörtgen, merkez x 50%, y 53–64%, ~%30 W, r 12 px, `#F7090A`, 0…−2°; "FULL COURSE" (veya STEP BY STEP / FREE TOOLS) Montserrat Black beyaz, cap %5–6 H |
| L6 Kanıt paneli | x 24–75%, y 75–96%, dolgu `#FEFEFE`, kontur 7 px `#282B2D`, r 14 px; solda 2 araç logosu (siyah çizgi, %14–16 H, gösterme hakkın olan logolar ya da jenerik glifler); sağda "VIEWS" Oswald 700 %5 H + "{GERÇEK_SAYI} VIEWS" + yeşil daire Ø %9 H `#13C813` beyaz ↑ ve glow |
| L7 (ops.) | başlık arkasında (50%,30%) %15 beyaz radyal parıltı |

Konu kelimesi renkleri: Finans `#F7C41E→#F7B409` · Sağlık/fitness `#B6F23A→#7ED321` · Tarih `#F5A623→#D9822B` ·
Psikoloji `#FF7AD9→#E040A0` · Korku/hayatta kalma `#FF4D4D→#D41C1C` (hap `#FFC400` siyah yazı) · Teknoloji `#4FD1FF→#1FA2FF`.

### 2.3 Thumbnail QA (export öncesi)
1. 168×94'e küçült: başlık okunmalı, en az 1 kart başlığı okunmalı, para bandı "para" olarak okunmalı.
2. Gri tonlamada başlık en parlak öğe.
3. Hale kontrastı her geçtiği zeminde ≥ 7:1.
4. Toplam metin bloğu ≤ 7 (başlık + hap + panel + 4 kart).
5. Kanıt sayısı **doğru ve doğrulanabilir** (geri dönüştürülmüş sayı yok).
6. Maskot özgün; benzerlik kontrolü yapıldı; başka kanalın gerçek thumbnail'i kullanılmadı.

## 3. Açıklama şablonu
```
{TITLE}

In this video, you will learn how to create {NICHE} videos like {SUCCESS_CHANNEL} using AI tools. The {NICHE} niche is one of the {MONEY_QUALIFIER} niches on YouTube, and many faceless channels {DOĞRULANABİLİR_SONUÇ}.

I will show you the complete process step by step: how to find viral {NICHE} video topics, how to write a high-quality script with AI, how to generate an AI voiceover, and how to create visuals and images for your videos. Even if you have no experience, you can start a {NICHE} channel with this method.

This tutorial also explains how channels like {SUCCESS_CHANNEL} grow so fast with evergreen {NICHE} content: curiosity-driven titles, simple thumbnails, and simple editing that keeps viewers watching.

If you want to start a faceless YouTube channel in the {MONEY_QUALIFIER} {NICHE} niche, this video takes you from channel creation to publishing.

📄 Free Prompt Pack (all prompts in this video): {DİREKT_LİNK}
__________________
🛠️ Tools used
{ARAÇ}: {URL}
{AFFILIATE (açıkça belirtilmiş)}: {URL}
__________________
🌍 Community
{TELEGRAM/DISCORD/WHATSAPP}: {URL}
__________________
⏰ Chapters
00:00 Important
mm:ss Channel Setup · Video Topics · Script · Voice · Visuals · Videos · Editing · Thumbnail · SEO · Final Video
__________________
🎬 Watch next
▶ {seri videosu kısa etiket} {URL}   (6–10 adet, aynı niş/aynı "like X" serisi önce)
__________________
📌 Questions people ask
{12–20 doğal varyant: "how to make videos like {SUCCESS_CHANNEL}", "{NICHE} faceless channel", "{MONEY_QUALIFIER} youtube niche", "{BENZER_KANAL_2} style videos with ai", "how to start a {NICHE} youtube channel {YEAR}"}

#{HASHTAG1} #{HASHTAG2} #{HASHTAG3} #{HASHTAG4} #{HASHTAG5}
```
Ölçüler: ~550 kelime · satır 1 = başlık · düzyazıda niş kelimesi ≥ 6×, kanal adı ≥ 3× · ilk 3 hashtag başlığın üstünde görünür.

**Etiketler (12–16, ≤ 480 karakter):** jenerik (make money online, ai tools, {MARKA}) · 4–5 varyant "how to make videos like {SUCCESS_CHANNEL}" (s'li/s'siz, create/make, "channel like", yaygın yazım hatası) · 3 niş how-to · 1–2 komşu kanal · 1 tarihli sorgu.

**Bölümler:** 9–12 tek kelime adım; ilk bölümün adı **"Important"** ("Intro" değil — atlamayı caydırır).

**Sabit yorum:** satır 1 = kaynak paketi linki; 2–4 = aynı serinin en yeni videoları; **her ay yeniden düzenle** (eski evergreen trafiği yeni videolara akıtır).

## 4. Kaynak paketi / beğeni hedefi — etik versiyon
- Referans mekaniği: paket her adımda anılır (≥ 6×), erişim son 60–90 sn'de açıklanır, "{N} Likes" neon kartı. Sonuç %3,1 beğeni + yüksek yorum, ama teslim edilmeyince şikâyet.
- **Bizim kural:** link **yüklemede** açıklama + sabit yorumda canlı. Videoda paket her adımda anılır; finalden önce "link sabit yorumda" denir.
  Beğeni hedefi istenirse topluluk hedefi olarak söylenir, teslimat ona **bağlanmaz**. Asla "söz ver, tutma".

## 5. Dağıtım
- Amiral tutorial'ları mümkünse **YouTube Collaboration** ile 2–4 aynı-kitle kanalla yayınla.
- Orijinal ses + **otomatik dublaj** açık (veya gözden geçirilmiş İngilizce dublaj).
- Süre 18–28 dk; asla 12 dk altı "kanal kurma" tutorial'ı.
- Yorumlardan sonraki `{SUCCESS_CHANNEL}`'ı çıkar: ≥ 2 yorumda istenen veya toplam ≥ 10 beğenili kanal kısa listeye.
