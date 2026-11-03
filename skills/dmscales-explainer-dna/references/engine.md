# Motor: Yaşam Döngüsü Merdiveni

Kaynak: `SISTEM.md` §2–5, `11_script_engine` §1–6, `01_shorts_algo_180s` §4–7. Ölçümler ana hit (SH, 706K, 180 sn) üzerinden.

## 1. İskelet

```
[BAŞLIK: "[SİSTEM]'in Tamamı [N] Saniyede…"]
 A0  GİRİŞ KAPISI   "Yeni bir X açtığında olan ilk şey şu: …"   (doğrulama / güven kontrolü)
 ★   AKSİYOM        "[Sistem]in umursadığı tek şey…" + "…denen gizli bir ölçü: [SAYAÇ]"
 A1  TEST           (deneme grubu, dalgalar, ilk ceza, teşhis bantları, yeniden çerçeve, ana kural)
 A2  BİRİKİM        ("…dıkça", kümülatif sinyal, ritim taktiği)
 A3  KIRILMA        ("İlk …'ten sonra … balayı/ısınma")
 A4  YÜKSEK DURUM   ("[SAYAÇ] yeterince yükseldiğinde…" = DORUK → hemen "Ama bu noktaya geldiğinde…")
 ⟶  KÖPRÜ + CTA     "Ama en önemli şey [X]…" → "Bu konuda yardım için … hazırladım" → topluluk
```

- **Dikey eksen = kronoloji.** Aşamalar sistemin izleyiciye *uyguladığı* sırayla dizilir, anlatıcının fikir sırasıyla değil.
- Her aşama bir **zaman kapısı** ile açılır: *Yeni bir … açtığında / … yaptığın anda / İlk …'ten sonra / …dıkça / … eşiğini geçtiğinde / Ama bu noktaya geldiğinde*.
- Aşama sayısı: 120 sn → 3–4, 180 sn → 5 (±1), 300 sn → 6–7 (+ ~%55'te bir orta-CTA).
- Shorts, Longform ve TikTok videoları **neredeyse aynı kelimelerle** açılır ve "To avoid this" üçünde de aynı konumdadır (A0'ın 3. cümle grubu). Şablon bilinçlidir; sen de kullan.

## 2. Aşama ünitesi: K-M-İ-T-T-U

| # | Parça | Görevi | Kalıp | Süre |
|---|---|---|---|---|
| 1 | **Kapı** | Zamanı ilerletir: "sen şu an buradasın" | "…yaptığın anda" | 1–3 sn |
| 2 | **Mekanizma** | Perde arkası + **bir rakam** | "…yaklaşık 30.000 kişiye gösterir" | 3–8 sn |
| 3 | **İsim** | Duruma etiket (önce olay, sonra ad) | "Buna X deniyor" | 1–2 sn |
| 4 | **Teşhis/Eşik** | "Hangi durumdasın?" | "Eğer …'de takılıyorsan sebep şunlardan biri" | 3–6 sn |
| 5 | **Taktik** | Emir kipi çözüm | "Bundan kaçınmak için … yapman gerekiyor" | 3–10 sn |
| 6 | **Uyarı/Çerçeve** | Cezayı umuda çevirir ya da ödüle risk koyar | "Herkes X'e söylenir ama aslında…" / "Şimdi tembelleşirsen…" | 3–10 sn |

1-2-3 sabit sırada gelir; 4-5-6 yer değiştirebilir, biri atlanabilir. Bir ünite 15–60 sn.

Etiket eşlemesi (senaryo formatı): `[KAPI] [MEKANİZMA] [İSİM] [TEŞHİS] [TAKTİK] [UYARI]/[ÇERÇEVE]`. Ünite dışı: `[AKSİYOM] [SAYAÇ] [KURAL] [KÖPRÜ] [CTA]`.

### Ana hitin gerçek akışı (saniye bazlı, 180 sn)
| Sn | İçerik | Ünite parçası |
|---|---|---|
| 0–9 | Yeni kanal → bot kontrolü → "seed audience of around 30,000" | A0 KAPI + MEKANİZMA |
| 9–14 | Güvenilmezsen hiç itilmez → "This is called zero view jail" | A0 TEŞHİS + İSİM |
| 14–24 | "To avoid this… aged channel… but most importantly…" | A0 TAKTİK (ceza→taktik 1 sn) |
| 24–34 | "hidden metric called trust score… would rather push someone else's" | AKSİYOM + SAYAÇ |
| 34–50 | "Once you start posting… People call this the 30k view jail" | A1 KAPI + MEKANİZMA + İSİM |
| 50–64 | Grafik kalıbı + iki bantlı teşhis ("one of these", liste sadece ekranda) | A1 TEŞHİS |
| 64–77 | "A lot of people hate on… but it's actually a really good spot" | A1 ÇERÇEVE (%36–43) |
| 78–110 | Geniş kitle taktiği + "retention more than any other stat" + CTA-spam uyarısı | A1 TAKTİK + KURAL + UYARI |
| 110–127 | "monthly audience slowly grows… uploading every single day" | A2 |
| 127–136 | "honeymoon phase… might get view jailed again temporarily, but" | A3 |
| 136–147 | "Once your trust score is high enough… stop view jailing you… 10 million" | A4 DORUK (%76–82) |
| 148–158 | "If you get lazy now… restart" | A4 UYARI |
| 158–168 | "But the most important thing… niche… over-saturated" | KÖPRÜ |
| 169–178 | "I have a playlist… join the Discord" | CTA |

## 3. Gerilim mimarisi: ceza ↔ umut salınımı

Notasyon: ▼ ceza/tehdit, ▲ umut/ödül, ◆ taktik (kontrol hissi), ↻ yeniden çerçeve.

- Ana hit 3 dakikada **~11 tam ▼→▲ döngüsü** yapar, ortalama **16 sn'de bir**. Hiçbir düz bölüm 15 sn'yi geçmez.
- Salınımı "but" dönüşleri taşır: **3,0/dk** (Longform ve TikTok 0,5–0,6/dk → düz anlatım, daha düşük performans). TR karşılığı: "ama / fakat / ancak", hedef ≥2,5/dk.
- **Soru cümlesi yok** (SH 0, TT 0). Gerilimi koşullu teşhis ("Eğer…") taşır: SH'de 3,7 "if"/dk. Düşük performanslı "blow up" videosunda 17 retorik soru var ve ton sohbete kayıyor.
- Doruk (▲▲▲) %76–82'de. Doruktan hemen sonra iki ▼ gelir (tembellik riski, doygunluk). **Kapanış rahatlatmaz**, çözüm olarak CTA'yı sunar.

```
 ▲      ▲    ▲   ↻▲▲ ▲     ▲   ▲▲  ▲▲▲(DORUK %76-82)
 │ /\  /\   /\  /  \/\  /\ /\ /\/\ / \
 │/  \/  \/\/  \/      \/  \/  \/  \/   \__ ◆CTA (tedirgin kapanış)
 0:00   0:30    1:00     1:30    2:00   2:30  3:00
```

Yazarken kontrol: her ~15 sn'lik pencerede en az bir ▼ ve bir ▲ (ya da ◆) olmalı.

## 4. Gizli sayaç ve aksiyom

- **Aksiyom:** "[Sistem]in umursadığı tek bir şey var: [insanları uygulamada tutmak / paranın geri gelmesi / riski azaltmak]. Daha çok A, daha çok B; daha çok B, daha çok para." Bütün kurallar bu güdüden türetilir. Videoda en az 2 kez **"… riske girmek yerine başkasını öne çıkarır"** kalıbıyla hatırlat. Düşman platformun çıkarıdır; bu, kuralları keyfi değil mantıklı gösterir.
- **Gizli sayaç:** tek bir isim ("güven puanı", "ödeme alışkanlığı", "eşleşme puanı"). 0:25 civarında tanımlanır ("Bunların hepsi X denen gizli bir ölçüye gidiyor. Kısacası, …"), sonra her aşamada geri çağrılır (≥3 kez). Her taktik puanı artırır ya da düşürür; oyun puanı gibi çalışır. Görülemezliği ekranda dipnotla söylenir ("*bu puanı görmek imkânsız").
- Sayaç resmî bir şey değilse bunu dürüstçe çerçevele: "resmî adı yok ama…", "sistem buna doğrudan puan demiyor ama davranışı tam olarak böyle".

## 5. Jargon motoru: kavram icat etme

Ana hit 3 dakikada **15 isimli kavram** (≈5/dk); ilk kavram 0:06'da, ilk icat edilmiş etiket 0:12'de. Kavram yoğunluğu izlenmeyle aynı sırada (SH 5,0 > TT 3,5 > LF 2,0 > KI 1,1).

**5 isim üretme kuralı:**
1. **Cezayı mekâna çevir:** hapis, oda, kafes, bekleme salonu, tavan, karantina. Mekân metaforu "çıkış yolu ne?" sorusunu kendiliğinden doğurur.
2. **Rakamı isme göm:** "30 bin hapsi", "300 izlenme duvarı". Ölçülebilir ve yorumda paylaşılabilir olur ("ben 2-3 bin hapsindeyim" yorumu 387 beğeni aldı).
3. **Görünmez bir sayaç adlandır:** "… denen gizli bir ölçü".
4. **Ödül durumuna bir evre metaforu ver:** balayı, ısınma dönemi, vitrin dönemi. Ödülün geçici ve kaybedilebilir olduğunu hissettirir.
5. **Sahipliği topluluğa ver (yalnızca doğruysa):** "İnsanlar buna X diyor". Topluluk terimi değilse "Buna X diyelim".

Kurallar:
- Etiket **mekanizmadan sonra** gelir (önce olay, sonra ad).
- Her etiket en az 1 kez geri çağrılır (ana hitte "jail" kökü 7 kez). Türkçede ekli halleri kullan ("deneme odasından çıkmak", "hapse düşmek").
- Resmî terimler de kavram sayılır ve otorite verir ("third level feature eligibility", "Findeks", "hard inquiry") — tek cümlelik tanımla gel.
- Kısaltmalar ekranda dipnotla açılır.
- **TikTok dersi:** paketlemede (bölüm adı, etiket) vaat edilen kavram senaryoda hiç geçmezse vaat boşa düşer. Bölüm adları ve etiketler senaryodaki kavramlardan türetilir.

Kavram türleri karışımı (180 sn, ≥12): 2–3 mekân metaforu, 1 gizli sayaç, 1 evre metaforu, 3–4 resmî/sektör terimi, 2–3 metrik/sinyal adı, 1–2 izleyici/kullanıcı sınıfı, 1 grafik kalıbı ("yavaş başlangıç, sıçrama, düz çizgi").

## 6. Teşhis bantları ve yeniden çerçeve

- **Bantlı teşhis:** "Eğer [X] [bant A]'da takılıyorsa sebep şunlardan biri. (EKRAN: 3 madde) Ama [bant B]'deysen sebep şunlardan biri. (EKRAN: 3 madde)". Maddeler **seslendirilmez**, sadece ekranda — izleyiciyi ekrana bakmaya zorlar ve hızı artırmadan bilgi yükler.
- **Grafik kalıbı:** "Yeni [hesap]ların grafiği hep aynıdır: yavaş bir başlangıç, bir sıçrama, sonra düz bir çizgi." (üçleme)
- **Yeniden çerçeve (1 adet, %35–45):** "Herkes [ceza durumu]na söylenir ama aslında bu iyi bir yer, çünkü [sistem] sadece [eksik veri] istiyor." Cezayı umuda çevirir, en büyük ↻▲▲ anıdır.

## 7. Kapanış ve CTA (5 videonun 5'inde aynı)

1. **Son aşama uyarısı:** "Ama bu noktaya geldiğinde her zamankinden çok çalış. Şimdi tembelleşirsen baştan başlarsın."
2. **Köprü:** "Ama en önemli şey [CTA varlığının çözdüğü sorun]." + doygunluk/rekabet tehdidi ("aynı şeyi yapan on kişi varken…").
3. **Varlık teklifi:** "Bu konuda yardım için [liste/tablo/kontrol listesi] hazırladım, sürekli güncelliyorum. Kendim de kullanıyorum."
4. **Topluluk:** "Ücretsiz [kişisel inceleme/yol haritası] istersen [topluluk]a katıl." Son kelime topluluk adı; veda yok.

Süre ≈ %10 (180 sn'de 15–20 sn). Abone/beğeni isteği yok (videonun kendi kuralıyla tutarlı: "CTA'yı spamlama"). 300 sn'de ek olarak ~%55'te 10 sn'lik orta-CTA (aynı varlık, içerikten çıkan köprüyle).

## 8. Neden çalışıyor (yazarken aklında tut)
1. **Kendini konumlandırma:** her izleyici bir aşamada; izleme kişisel teşhise dönüşür, yorumlar "itiraf duvarı" olur.
2. **Açık döngü zinciri:** her kapı bir sonraki durumu vaat eder; "benim aşamam gelecek" diye kalınır.
3. **Gizli sayaç:** oyun puanı gibi; her taktik onu oynatır.
4. **Düşman = platformun çıkarı:** kurallar mantıklı ve inandırıcı görünür.
5. **Sıkıştırma:** 282 WPM, dolgu yok; "25% hızda yeniden izleyeceğim" yorumu = yoğunluk değer olarak algılanıyor.

## 9. Yapma listesi (başarısız videolardan)

| Hata | Video | Ders |
|---|---|---|
| Kitlenin platformu dışında bir sistem anlatmak | TikTok ×0,30 | Konu kitlenin günlük acısı olmalı |
| Paketlemede vaat edilen jargonu senaryoda kurmamak | TikTok | Başlık/bölüm/etiketteki her kavram isimlendirilip geri çağrılır |
| İlk 45 sn'de isimli kavram yok, 2. cümlede genel liste | TikTok | 7 sn'de rakam, 15 sn'de vaftiz |
| Doymuş "how to" açısı | blow up ×0,43 | "Nasıl çalışır" açısı |
| Başlık vaadini teslim etmemek ("tek öldürücü fikir" hiç verilmiyor) | blow up | Vaat = içerik |
| Ana cevabı erken vermek (1:15) | blow up | Doruk %75–85'te |
| 17 retorik soru, "Well," menteşesi | blow up | Soru yerine koşullu teşhis |
| Doğaçlama + "sıradaki konu" geçişleri, dolgu ("like" 123 kez) | 10K ×1,00 | Her ünite bir kapıyla ve neden-önemli köprüsüyle açılır |
| Emek rakamını şişirmek (başlık 10.000, açıklama 1.000 saat), kendi videosunu küçümsemek | 10K | Anti-guru güveni kanalın sermayesidir |
| Sponsor ritmi kırar (%10 süre) | Longform, blow up | Gerekirse ≤10 sn, soru kılığında |
| Abartılı iddialar (etiketler, arama) yorumda düzeltildi | Longform | Tartışmalıyı yumuşat, sabit yorumda düzelt |
| Kendi içinde çelişki ("çok sık paylaşma" → "her gün paylaş") | TikTok | Taktikler birbirini yalanlamasın |
| Monetizasyon/ek bilgiyle sönen son (dorukla bitmiyor) | TikTok | A4 doruk + uyarı + köprü sırası korunur |
