# 04 — Senaryo motoru: yapı, adım döngüsü, tutma cihazları, anlatım

Kaynak: `deep-research/03-script-storytelling.md` (tüm zaman damgaları, cihaz envanteri, worked example'lar).
Telif: referansın cümleleri kopyalanmaz; aşağıdaki tüm örnek satırlar özgündür, sadece **işlev** kopyalanır.

## 1. Tek cümlelik yapı
**Kanıt → vaat → tek bir koşan örnekle 9 adımlık reçete → ödül (bitmiş video).**
Rehber ("abi/kardeş" tonunda mentor) izleyiciyi saniyede ~3,5 kelimeyle, neredeyse hiç boşluk bırakmadan yürütür;
her adım aynı döngüdür ve bir **kopyalanabilir eser** (prompt) etrafında döner.

## 2. Makro iskelet (22:00 master; başka süreler için yüzdeleri koru)

| # | Bölüm | Hedef | % | İçermesi şart |
|---|---|---|---|---|
| 0 | Soğuk açılış sorusu → niş cevabı | 0:00–0:12 | 1 | izleyiciye soru ≤ 0:02; "evet, doğru bildin" zihin okuma; niş kinetik yazı olarak |
| 1 | Kanıt yığını | 0:12–2:05 | 9 | ≥ 2 outlier kanal × 5 gerçek (video sayısı, abone, ilk yükleme yaşı, en iyi video izlenmesi, viral olma tazeliği); minimum RPM × izlenme = $ ; "sahte izlenme değil" kontrolü |
| 2 | Neden para kazandırıyor (mekanizma) | 2:05–2:30 | 2 | tek mekanizma (uzunluk → daha çok reklam; evergreen); ≤ 3 sn meme |
| 3 | Vaat + güvence + teaser | 2:30–2:55 | 2 | "Bu videoda sana … öğreteceğim"; "hiç stres yapma"; ≤ 10 sn bitmiş çıktı teaser'ı |
| 4 | Abone CTA #1 (misyon) | 2:55–3:10 | 1 | sayısal hedef + tarih; abone animasyonu |
| 5 | Adım 1: Kimlik (isim + logo) | 3:10–6:30 | 15 | prompt #1, #2; YouTube araması kontrolü; 1 hata→düzeltme |
| 6 | Adım 2: Konular | 6:30–9:15 | 12 | prompt #3 (başlık kalıpları ≥ 3 sn okunur); tek kategori; aramayla doğrula; **koşan örneği kilitle** |
| 7 | Adım 3: Senaryo | 9:15–11:25 | 10 | prompt #4; en iyi ücretsiz model; kelime→dakika düğmesi; **bekleme CTA #2**; üretilen hook'u sesli oku |
| 8 | Adım 4: Ses | 11:25–12:50 | 6 | ücretsiz TTS; tam tıklama yolu; stil talimatı hilesi; ses adı; bölme uyarısı; **bekleme CTA #3**; 15–25 sn örnek |
| 9 | Adım 5: Görseller | 12:50–15:00 | 10 | rakip görsel analizi; prompt #5 (kavram başına 1 görsel); tutarlılık hilesi "bunu kaçırma" |
| 10 | Adım 6: Hareket | 15:00–15:50 | 4 | sadece ilk dakikayı canlandır; görsel prompt'unu tekrar kullan; 5–8 sn örnek — **orta-üçte "vay" anı** |
| 11 | Adım 7: Edit | 15:50–18:45 | 13 | sessizlik kesme; kavram başına medya (1 benzetme); zoom; otomatik altyazı; tempo kuralı; erken uyarıya geri çağrı |
| 12 | Export beklemesi = fırsat hatırlatması | 18:45–19:20 | 3 | "Hâlâ emin değil misin?" + 3. kanıt kanalı + en güçlü *savunulabilir* kazanç cümlesi (%80–87'de) |
| 13 | Adım 8: Thumbnail | 19:20–20:25 | 5 | prompt #6; zayıfsa yeniden üret; yazıyı görsele koy |
| 14 | Adım 9: SEO | 20:25–21:05 | 3 | prompt #7: A/B için 5 başlık, açıklama, etiket |
| 15 | Kapanış CTA bloğu | 21:05–21:45 | 3 | "Final videodan önce…"; tekrar izle + yorumla; "yeni başlayan bile yapar"; abone nedeni; kaynak paketinin yeri |
| 16 | Final video gösterimi | 21:45–22:45 | 4–5 | "İşte final video. Görüşürüz." → 45–75 sn bitmiş video; **sonrasında konuşma yok** |

İlk eyleme geçilebilir adım ≤ %14 süre (22 dk'da ≤ 3:15). İlk kopyalanabilir eser ~3:30.
Bölümler sadece açıklamadadır; ekranda başlık kartı yok — geçiş cümlesi + uygulama değişimi bölümü işaretler.

## 3. Mikro yapı: her adımın 12 vuruşlu döngüsü
```
T  GEÇİŞ          "X hazır; şimdi sıra Y'de"                         1–3 sn
N  NEDEN          bu adım neden önemli (tercihen rakip üzerinden)     3–10 sn
E  EMPATİ         "Şu an aklında fikir yok, biliyorum" / "dert etme"  2–4 sn
P  ESER KAYNAĞI   "bu yüzden prompt'u pakete koydum" / araç + "ücretsiz" 3–5 sn
C  TIKLAMA YOLU   kopyala → aracı aç → yapıştır → 1–2 ayar → çalıştır 10–25 sn
Z  SIFIR EMEK     "prompt'ta hiçbir şeyi değiştirme, sadece çalıştır"   2–3 sn
K  DÜĞME          varsayılan değer + nasıl değişir (30→300 isim; 1.800–2.200 kelime) 3–8 sn
W  BEKLEME DOLGU  (sadece araç işlerken) CTA veya motivasyon ≤ 12 sn
R  SONUÇ          "şimdi bak…" + çıktı ekranda ≥ 3 sn (+ medya örneği)
X  İPUCU/UYARI    alternatif araç, kontrol ya da hata→düzeltme       5–25 sn
V  SEÇ/DOĞRULA    birini seç, YouTube'da kontrol et, Doc'a kaydet     5–15 sn
T' SONRAKİ GEÇİŞ
```
Referans frekansları: "bundan sonra" 18× · bölüm sınırında aynı geçiş cümlesi 5/5 · "prompt'ta hiçbir şeyi değiştirme" 5× ·
"bak" ~31× (her ~42 sn) · tam "şimdi bak" sonuç ifadesi 7× · "basit" 17× · "…yapman gerekiyor" ~45×.
**R ve X asla atlanmaz.**

## 4. Tutma cihazı kotaları (22 dk için)

| Cihaz | Referans | Bizim kota |
|---|---|---|
| Toplam cihaz | 118 adet, medyan her 10 sn, en uzun boşluk ~31 sn | ≥ 1 / 15 sn, boşluk ≤ 30 sn |
| Doğrudan soru / zihin okuma | 6 | ≥ 4 (0:00 açılış + "evet, doğru düşündün" geri çağrısı) |
| Açık döngü / vaat | 11 | ≥ 8; en az 2'si sonra ekranda kapanan uyarı |
| Güvence | ~20 (her ~65 sn) | ≥ 18; biri dil ("basit İngilizce"), biri beceri ("yeni başlayan bile") |
| Uyarı / önem bayrağı | 9 | 6–10; "bunu kaçırma" en az 1 (tutarlılık hilesi) |
| "İçeriden bilgi" çerçevesi | 3 (asla "secret" denmiyor) | 2–4 |
| Ücretsiz araç vurgusu | 4 | her araçta ücretsiz/ücretli net söylenir |
| Para anma | 10 (7'si ilk 2:31'de) | ilk 3 dk'da yoğun; %80–87'de bir kez daha |
| Sosyal kanıt | girişte 9 + 3 tekrar enjeksiyon | aynı |
| Mizah / meme | 6 | ≥ 5: ≥ 2 kanıt bölümünde, ≥ 2 bekleme CTA'larında |
| Abone CTA | 4 (3'ü bekleme anında) | ≤ 4, hiçbiri 2:45'ten önce değil |
| Kaynak paketi anma | 7 | her adımda (≥ 6) |
| Videolar arası link | 3 | 2–3 |
| Sonuç örnekleri | teaser 10 sn, ses 24 sn, hareket 6 sn, final 58 sn | ses 15–25 sn, hareket 5–8 sn, final 45–75 sn |
| Hata→düzeltme | 1 (logo) + 1 (sessiz boşluk) | ≥ 1 ilk üçte birde |

**Bekleme deseni:** araç işlerken (senaryo üretimi, ses render, export) 3 kez CTA/motivasyon; ikincisi kendini geri alan şakalı ton
("yok yok, zaten abonesin biliyorum").

## 5. Anlatım (teslim) spesifikasyonu

| Ölçü | Referans | Hedef |
|---|---|---|
| Hız | 205–215 Hintçe token/dk ≈ 186 İngilizce kelime/dk | İngilizce 180–190 · Türkçe 150–170 (pilotla doğrula) |
| Kaplama | konuşma %89–94 | ≥ %90 |
| Duraklama | 21:50 öğretimde ≥ 0,35 sn sadece 11–15 adet | ≤ 1/dk ≥ 0,35 sn (ön-reveal boşluğu hariç) |
| Nefes | ~0,2/dk (kesilmiş/sentetik) | nefesleri temizle |
| Dinamik | LRA 2,8 LU (ağır kompresyon) | LRA ≤ 4 LU |
| Cümle | ortalama 11,2 kelime, medyan 10, %35'i ≤ 8 | medyan ≤ 10; ≥ %30 ≤ 8; cümle başına 1 talimat |
| Ton | samimi "abi/bhai" mentor; asla resmi; dolgu sesi yok | aynı |
| Kod karışımı | araç adı, UI etiketi, para/YouTube terimleri İngilizce (~%24); duygu + sıralama ana dilde | Türkçede: prompt'u, CapCut'ta, export'u, RPM'i… |

Bu hız 1.850 kelimelik İngilizce senaryo ≈ 10 dk değil **~11–12 dk** eder (155–160 wpm ürün sesi).
Öğretim anlatımı için: 21 dk öğretim ≈ 3.700–4.100 İngilizce kelime.

## 6. Hikâye anlatımı
- **Kahraman = izleyici; anlatıcı = rehber** (StoryBrand). Engeller tek tek adlandırılıp kaldırılır.
- **Düşmanlar:** düşük RPM nişleri, boş sayfa korkusu, rekabet (dokunulmamış konu seçerek çözülür), karmaşıklık, önceden haber verilen hata modları.
- **FOMO üç ayakla:** tazelik ("ilk video 2 ay önce, viral 2 hafta önce"), küçüklük ("24 video → 46K abone" = ulaşılabilir), evergreen ("hâlâ saatte izlenme").
- **Topluluk misyonu:** "{tarih}'ten önce {N} abone" → abone olmak = misyona katılmak.
- **Koşan örnek:** konular adımında seçilen tek konu senaryo → ses → görseller → thumbnail → final videoya kadar taşınır (5/5 adım).
- **Kapanış artefaktla:** konuşan özet yok; bitmiş video oynar ve video biter → izleyicinin son düşüncesi "bunu ben de yaparım".

## 7. Özgün satır bankası (İngilizce, işlev aynı / kelimeler yeni)

**Geçişler:** "The script is done — now let's give it a voice." · "Name and logo are sorted. Next question: what will this channel actually talk about?" ·
"With the voice ready, let's build what people will actually see." · "Images are done. Now we make the first minute move." ·
"That's every raw piece. Time to stitch it together." · "The video is ready — but nobody clicks without a reason. Thumbnail time." ·
"One last thing before upload: the words YouTube reads." · "Hold on to this topic. We'll use it in every step, right up to the final video."

**Yeniden kanca / açık döngü:** "Stay till the end — I'll play the finished video we're building right now." ·
"This next setting is the one most people skip, and it's why their voice-overs sound flat." ·
"Remember this warning. In about five minutes you'll see what happens if you ignore it." ·
"I'll fix this in a second — first, look at what went wrong." · "Before the final video, two quick things that decide whether this works for you."

**Güvence:** "Don't touch anything in the prompt. I've already done that work for you." ·
"If your first result looks bad, that's normal. Mine did too, thirty seconds ago." ·
"Weak English? No problem — the script is written in simple English on purpose." ·
"It sounds complicated when I explain it. On the timeline it takes two minutes." ·
"If you can copy and paste, you can do every step in this video." · "Missed a click? Go back ten seconds — everything is on screen."

**Uyarı / ipucu:** "Before you fall in love with a name, search it on YouTube." ·
"Long script? Generate the voice in two or three parts, or you'll get silent holes." ·
"Pick topics with almost no long videos yet — that's where new channels win." ·
"Use the same character reference for every image, thumbnail included."

**CTA:** "While the model is writing, tap subscribe — you'll finish before the script does." ·
"We're aiming for {GOAL} subscribers by {DATE}. If this saved you a day of work, you're part of that." ·
"Stuck on a step? Comment the timestamp and I'll answer right there." · "The full prompt pack is in the pinned comment." ·
"Here's the finished video. See you in the next one."

**Türkçe örnekler:**
1. "Sana bir soru sorayım: YouTube'da RPM'i neredeyse hiç düşmeyen niş hangisi?"
2. "Evet, tam düşündüğün gibi — finans nişi."
3. "Bu kanal sadece {N} video atmış ve {M} abone toplamış; ilk videosu da {X} ay önce."
4. "Hiç stres yapma, prompt'ta hiçbir şeyi değiştirmiyorsun: kopyala, yapıştır, çalıştır."
5. "Şimdi şuna bak — tek seferde otuz kanal adı, üç kategoriye ayrılmış."
6. "İngilizcen zayıfsa dert etme; script'i bilerek çok basit İngilizceyle yazdırıyoruz."
7. "Claude script'i yazarken sen de abone ol butonuna bas — tek kuruş ödemiyorsun."
8. "Bu uyarıyı aklında tut: script uzunsa sesi iki üç parçada üret, yoksa araya sessiz boşluklar girer."
9. "Ses de hazır olduğuna göre, sıra izleyicinin göreceği görsellerde."
10. "Prompt paketinin tamamı sabit yorumda. Şimdi final video geliyor — görüşürüz!"

## 8. Para iddiaları politikası
Referans "minimum RPM × izlenme" aritmetiği ve "bir ayda bir yıllık gelir" gibi doğrulanmamış iddialar kullanıyor.
Biz: **sadece kamuya açık sayılardan aritmetik**, "tahmini" kelimesiyle; garanti gelir cümlesi yok; finans ürün videolarında "not financial advice".
