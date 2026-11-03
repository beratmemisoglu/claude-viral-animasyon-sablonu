# Paketleme: başlık, thumbnail, açıklama, etiket, sabit yorum

Kaynak: `10_packaging_hooks` §2–7, `SISTEM.md` §6, `script_audio.md` §6, `visual.md` §9.

## 1. Başlık

### Formül A (iki hitin formülü) — varsayılan
**TR:** "[SİSTEM] Algoritmasının Tamamı [N] Saniyede…" / "[SİSTEM] Sisteminin Tamamı [N] Saniyede…" / "[SİSTEM]'in Tamamı [N] Saniyede…"
**EN:** "The Entire [SYSTEM] Explained in [N] Seconds…"

| Parça | İşlev |
|---|---|
| Tamamı / The Entire | Bütünlük vaadi; "başka video izlemene gerek yok", kapanış ihtiyacı. Türkçede sonda daha doğal ("…Tamamı"). |
| [SİSTEM] (+Algoritması) | Kara kutu; izleyicinin sürekli şikâyet ettiği düşmanı adlandırır. Bilinen marka/kurum adı. |
| Explained / (TR'de örtük) | Taktik değil mekanizma; boş "nasıl çalışır" açısı. |
| [N] Saniyede | Sıkıştırma; dakika değil saniye (180 > 3). **N = gerçek süre**, saniyesi saniyesine (doğrulanabilir sözleşme → güven). |
| … | Bitmemiş cümle, merak (ikincil etki; tutarlı ol: tek karakter "…"). |
| Title Case | Otorite/ansiklopedi tonu. |

### Formül B (orta performans, sadece uzun derleme için)
"[BÜYÜK EMEK] [Konu] Bilgisi [KISA SÜRE]de" — emek rakamı **gerçek** olmalı ve açıklamayla çelişmemeli.

### Kaçın
Küçük harf "nasıl … yapılır (tek … ile)" (×0,43): doymuş açı, süre sözleşmesi yok, vaat teslim edilmedi.

### Puanlama (her aday için 0–10)
Bilinen sistem adı (2) + bütünlük kelimesi (2) + saniye = gerçek süre (2) + kitlenin günlük acısı (2) + hook'un in-medias-res ve 15 sn'de vaftize uygunluğu (2). Paket 5 aday listeler: 3'ü Formül A varyantı (sistem adı farklı söylenişlerle), 1'i Formül B, 1'i "acı sorgusu" başlığı (ör. "Reels'in Neden 300 İzlenmede Takılıyor? Tamamı 180 Saniyede…"). Seçilen = en yüksek puan, eşitlikte Formül A.

**Başlık–hook kuralı:** Başlık "Tamamı" diyorsa ilk cümle sistemin **1. adımı** olmalı ("olan ilk şey şu"). Bütünlük kronolojiyle teslim edilir.

## 2. Thumbnail (1280×720)

Ana formül (4/5 video):
- **Beyaz zemin** (#FFFFFF). Yaratıcının gerekçesi: kitle karanlık modda geziyor, beyaz öne çıkıyor.
- **Sol %55–60:** tek bir koyu arayüz kanıt kartı (istatistik/sonuç/puan ekranı). Kilit rakam **kırmızı elle çizilmiş elipsle** (#E5161C, ~8 px) daire içinde. Rakam kahramandır.
- **Sağ %40:** 2–3 kelime, kalın küçük harf (Roboto/Arial Bold ~100–110 px), iki kademeli satır: 1. satır siyah, 2. satır kırmızı (#FF0000), biraz büyük ve yarım kelime sağa-aşağı kaydırılmış.
- **Kıvrık kırmızı ok** (~10 px, açık ok ucu) kırmızı kelimenin altından rakama döner.
- Yüz, çöp adam, kanal markası yok. Gradyan/gölge yok.

**Metin kuralı:** konu etiketi DEĞİL, **zorluk hakkında tavır iddiası**. "easy as f*ck" (706K), "stupid easy" (368K) çalıştı; "tiktok explained" (konu etiketi) ×0,30 aldı.
TR örnekleri: "saçma / kolay", "çocuk / oyuncağı", "bu kadar / basit", "kimse / söylemiyor…", "aşırı / kolay", "bir video / uzaktasın". Argo istenirse sansürlü: "kolay mı? / aşırı ko-".

Varyantlar: (EQUn) üstte "**kimse** size bunu söylemeyecek…" + 6 kanıt kartı yelpazesi; (VQ) tam ekran koyu grafik + ortada beyaz "**bir video** uzaktasın" + dizdeki kırmızı aşağı ok.

**Kanıt kartı dürüstlüğü:** Kartta gerçek bir sonuç olmalı (kullanıcının kendi ekran görüntüsü) ya da açıkça temsilî/generik bir kart (gerçek bir bankanın/platformun arayüzünü birebir taklit etme, logo kullanma). Rakam senaryodaki kaynaklı bir rakam olmalı.

Paket 3 konsept verir: (1) ana formül, (2) varyant, (3) cesur tavır varyantı. Her biri için: sol kart içeriği + daire içindeki rakam, sağ 2 kelime, ok yönü, ve görsel üretim prompt'u (İngilizce, ör. "flat white background, left: dark-mode analytics card showing ..., the number ... circled with a hand-drawn red marker ellipse; right: two staggered lowercase words in heavy black sans '…' and red '…', a curly hand-drawn red arrow from the red word to the circled number; no faces, no gradients, no shadows, 1280x720").

## 3. Açıklama (5 videoda aynı iskelet)

1. **Vaat paragrafı:** "Bu videoda [SİSTEM]in tamamını anlatıyorum: [sistem] neyi umursar, her aşamada ne olur, [sayaç] nedir ve [kaçış] için ne yapman gerekir."
2. **Güvenilirlik paragrafı:** kullanıcının gerçek deneyimi/sonuçları (yoksa `[GÜVENİLİRLİK: kullanıcı doldurur]`; **uydurma rakam yok**, şişirme yok).
3. **Kaynaklar:** senaryodaki her rakamın kaynağı (Ayrıntı kuralı: VO'da değil açıklama/sabit yorumda).
4. Araç/affiliate linkleri (varsa).
5. "Kurs satmıyorum; konuşmak ya da diğer üreticilerle tanışmak istersen [topluluk]: <link>" (anti-guru konumlandırması).
6. Abone hatırlatması tek satır, açıklamada (videoda değil).
7. **Bölümler:** her 20–60 sn'de bir; adlar senaryodaki kavramlardan: "0:00 Giriş · 0:25 [Gizli sayaç] · 0:35 [Ceza metaforu-2] · 2:07 [Evre metaforu] · 2:40 Kapanış". İlk bölüm 0:00. Zamanları `qc.py --timed` çıktısından al.
8. **3–6 hashtag** (CamelCase) + **10–25 etiket**: sistem adı, "nasıl çalışır", kavram adları, uzun kuyruklu acı sorguları ("reels neden 300 izlenmede takılıyor", "kredi notum neden yükselmiyor").

## 4. Sabit yorum (güven sigortası)
- Kaynak listesi kısa hali + "Bu videoda X'i biraz basitleştirdim: …" türünden dürüst bir düzeltme (dmscales: "I kinda exaggerated how much tags + chapters affect everything").
- Yorum tetikleyicisi soru sorma; kavram doğal olarak itiraf yorumu üretir ("hangi hapistesin?" diye sorma — izleyici kendisi yazar).

## 5. Seri planı
Pakete 2 devam konusu: (a) aynı sistemin diğer formatı (Shorts → Uzun video), (b) kitlenin bitişik sistemi (Reels → Keşfet). İlk yorumlarda "şimdi de X'i yap" talebi gelirse sıra ona göre değişir.
