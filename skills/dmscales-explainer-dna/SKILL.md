---
name: dmscales-explainer-dna
description: "@dmscales kanalının \"The Entire [SİSTEM] Explained in [N] Seconds…\" hit motorunun (706K izlenme, kanal medyanının ×7,1'i; 5 video, 7 analist ajan + kare-kare görsel/ses ölçümü ile tersine mühendislik) ÜRETİM SİSTEMİ. Kullanıcı yalnızca bir KONU verir; skill otomatik olarak uygunluk testi → kaynaklı araştırma → Yaşam Döngüsü Merdiveni (A0–A4) → K-M-İ-T-T-U üniteleri → gizli sayaç + aksiyom + icat edilmiş kavram adları + rakam cetveli → beat etiketli tam Türkçe senaryo (ekran satırlarıyla) → QC script'i (15 ölçüt) → başlık/thumbnail/açıklama/bölümler/etiketler → ElevenLabs düz metni + render motoru için edit-plan.md üretir. Kullanıcı \"dmscales tarzı\", \"dmscales sistemiyle\", \"Tamamı N saniyede\", \"X algoritmasının tamamı\", \"Entire X explained in N seconds\", \"X nasıl çalışır videosu\", \"view jail / trust score / güven puanı tarzı\", \"yaşam döngüsü merdiveni\", \"konuyu vereyim içeriği/senaryoyu sen yaz\", \"bu konuda algoritma açıklayıcı video\", \"kara kutu sistem videosu\" dediğinde ya da bir sistem/algoritma/kurum süreci konusu verip senaryo, hook, başlık, thumbnail veya edit plan istediğinde MUTLAKA bu skill'i kullan — skill adı geçmese bile."
---

# dmscales Explainer DNA

Bir **konuyu**, dmscales'in kanıtlanmış hit motoruyla yayına hazır bir **içerik paketine** çevirir. Kullanıcı sadece konuyu verir; geri kalan her karar bu dosyadaki kurallara göre otomatik verilir.

Motorun özü (her parça buna hizmet eder):
1. **Hikâye değil, durum makinesi.** Bir kara kutu sistemin izleyiciye uyguladığı süreç kronolojik aşamalarla (A0→A4) anlatılır. İzleyici "ben hangi aşamadayım?" diye kendini teşhis eder.
2. **Her aşamada aynı ünite: K-M-İ-T-T-U** — Kapı → Mekanizma (+rakam) → İsim → Teşhis → Taktik → Uyarı/Çerçeve. Ceza ≤8 sn içinde taktiğiyle eşleşir; ayrı "ders" bloğu yoktur.
3. **Gizli sayaç + platform güdüsü aksiyomu** tüm kuralları tek mantığa bağlar ("…umursadığı tek şey…", "…seni değil başkasını öne çıkarır").
4. **Kavram icadı ve sıkıştırma:** ~5 isimli kavram/dk, ~16 sn'de bir ceza↔umut salınımı, dolgusuz, soru cümlesiz, 2. tekil şahıs.
5. **Başlık bir çarpandır, motor değil.** Konu kitlenin kendi acısı değilse formül ×0,3 getirir (TikTok dersi).

## Girdi

Zorunlu: **konu** (ör. "Instagram Reels algoritması", "kredi notu", "LinkedIn", "ATS CV filtresi").
İsteğe bağlı (verilmezse varsayılanı kullan, sorma; paketin başında `Varsayımlar:` satırına yaz):

| Parametre | Varsayılan | Not |
|---|---|---|
| Süre (N) | **180 sn** | 120 / 180 / 300. Başlıktaki sayı = gerçek süre. 120 sn yatay video "ölü bölge"dir (`topic_fit.md` S4); 120 istenirse dikey öner. |
| Dil | Türkçe VO + Türkçe ekran | İngilizce istenirse `phrasebook_tr.md` içindeki EN kalıpları ve 265–280 WPM kullan. |
| Format | YouTube 4:3 yatay (1440×1080) | Referansın kendisi 4:3. Dikey (Reels/Shorts 9:16) istenirse aynı kompozisyon ölçeklenir. |
| Hedef kitle | Konunun kendi kullanıcıları (o sistemde "takılı" olanlar) | Kanal kitlesi bilinen bir şeyse (yaratıcılar, öğrenciler…) onunla eşleştir. |
| CTA varlığı | "açıklamadaki ücretsiz liste/tablo" + "topluluk (Discord/Telegram)" | Kullanıcının gerçek varlığı varsa onu kullan; yoksa `[CTA VARLIĞI: ...]` yer tutucusu bırak. |

Konu gerçekten anlaşılmıyorsa (hangi sistem olduğu belirsizse) tek bir soru sor; aksi halde hiç soru sormadan üret.

## İş akışı

1. **Uygunluk testi** — `references/topic_fit.md`. 5 soruyu puanla (0–5). 5/5 değilse en yakın *sistem açısına* yeniden çerçevele (ör. "motivasyon" → "Beynin ödül sisteminin tamamı…" değil; uygun değilse `topic_fit.md` §3'teki dönüşümleri uygula) ve devam et. ≤2 ise kullanıcıya 3 alternatif açı öner ve en yükseğiyle üret. Puanı ve gerekçeyi pakete yaz.

2. **Araştırma (zorunlu, kaynaklı)** — WebSearch/WebFetch ile: sistemin gerçek kronolojisi, resmî açıklamalar (platform yardım sayfaları, kurum mevzuatı, mühendislik blogları, resmî röportajlar), sayılar (grup büyüklükleri, eşikler, yüzdeler, süreler), topluluğun kullandığı acı terimleri ("X'te takıldım" aramaları, forumlar). Çıktı: **rakam cetveli** (küçükten büyüğe ≥6 rakam) ve **kaynak listesi** (her rakam → URL + tarih).
   - Doğrulanamayan her iddia senaryoda `[KAYNAK GEREKLİ: ne gerekiyor]` ile işaretlenir ya da cümle çıkarılır. **Rakam asla uydurulmaz.**
   - "İnsanlar buna X diyor" kalıbı yalnızca topluluk o terimi gerçekten kullanıyorsa. Etiketi sen icat ettiysen "Buna X diyelim" / "Ben buna X diyorum" de.
   - Tartışmalı/yaygın-ama-resmî-olmayan iddialar yumuşatılır ("büyük ihtimalle", "çoğu üreticinin gözlemine göre") ve sabit yoruma düzeltme notu hazırlanır (dmscales'in güven sigortası).

3. **Motor tasarımı** — `references/engine.md`:
   - Aşama haritası A0 (giriş kapısı) → A1 (test) → A2 (birikim) → A3 (kırılma) → A4 (yüksek durum), her birine bir zaman kapısı fiili.
   - **Aksiyom** (sistemin tek güdüsü; para/risk/güven) ve **gizli sayaç** (tek isim; ≥3 kez geri çağrılacak).
   - **Kavram sözlüğü:** ≥2 mekân metaforu (ceza durumları; biri rakamlı: "30 bin hapsi" tipi), 1 gizli sayaç, 1 evre metaforu (balayı/ısınma), toplam ≥12 isimli kavram (180 sn). İsim üretme kuralları: `engine.md` §5.
   - Teşhis bantları (1–2), yeniden çerçeve (1, %35–45), doruk (%76–82) + doruk sonrası uyarı, CTA köprüsü (son sorun → varlık).

4. **Senaryo** — `references/budgets.md` iskeletini (süreye göre) doldur, `references/phrasebook_tr.md` kalıplarını kullan. **Format sabittir** (QC script'i bunu okur):
   ```
   ### A0 · Giriş kapısı
   [KAPI] Yeni bir … açtığında olan ilk şey şu: …
   [MEKANİZMA] …
   (EKRAN: grafik — yavaş başlangıç, sıçrama, düz çizgi)
   [İSİM] Buna … deniyor.
   ```
   - Her VO satırı tek etiketle başlar: `KAPI MEKANİZMA İSİM TEŞHİS TAKTİK UYARI ÇERÇEVE AKSİYOM SAYAÇ KURAL KÖPRÜ CTA`.
   - `(EKRAN: …)` satırları VO değildir; ekranda olacak liste/grafik/kanıtı yazar. Sesli metin "şunlardan biri / bu grafik / burada" diyorsa hemen altına EKRAN satırı zorunlu. Teşhis listeleri **sadece ekranda** olur (seslendirilmez).
   - `> NOT:` satırları yorumdur, sayılmaz. `[KAYNAK GEREKLİ: …]` seslendirilmez, kelime sayısına girmez.
   - Rakamlar VO'da rakamla yazılır (30.000, %40, 24–48 saat).
   - Hedef kelime: 120 sn ≈ 330–360, 180 sn ≈ 480–540, 300 sn ≈ 800–880 (TR, ~170 kel/dk).

5. **QC (zorunlu)** — paketi yazdıktan sonra:
   `python <bu skill klasörü>/scripts/qc.py <paket.md>`
   15+ ölçütü (`references/qc.md`) ölçer: açılış kapısı, ilk rakam ≤7 sn, ilk vaftiz ≤15 sn, kavram/dk, aşama sayısı, ceza→taktik, sayaç geri çağırma, aksiyom, rakam cetveli, teşhis listesi, çerçeve konumu, düz bölüm, "ama"/dk, hitap, soru, dolgu, CTA ve süre, deiktik→EKRAN, kaynak etiketi. **Her ✖'yi düzelt ve yeniden çalıştır** (en fazla 3 tur); kalan sapmayı gerekçesiyle yaz. Son çıktıyı paketin §7'sine yapıştır. `[KAYNAK GEREKLİ]` sayısı >0 ise paket "YAYINA HAZIR DEĞİL" olarak işaretlenir.

6. **Paketleme** — `references/packaging.md`:
   - 5 başlık (ana: **"[SİSTEM] Algoritmasının/Sisteminin Tamamı [N] Saniyede…"**), 0–10 puanla; birini seç.
   - 3 thumbnail konsepti (beyaz zemin + solda kanıt kartı kırmızı elips + sağda 2 kelimelik **zorluk tavrı** iddiası + kıvrık kırmızı ok) + görsel üretim prompt'u.
   - Açıklama (sabit 8 parçalı iskelet), bölümler (`qc.py --timed` zamanlarından), 3–6 hashtag, 10–25 etiket (uzun kuyruklu acı sorguları), sabit yorum (kaynaklar + abartı düzeltmesi), seri devamı fikri.

7. **Üretim dosyaları** — `references/onscreen.md`:
   - `python <skill>/scripts/qc.py <paket.md> --vo <klasör>/script.txt --timed <klasör>/script_timed.txt`
   - `python <skill>/scripts/edit_plan_scaffold.py <paket.md> -o <klasör>/edit-plan.md` → iskeleti `onscreen.md` kurallarıyla doldur (screen markup `{kırmızı}` `{g:yeşil}` `_altçizgi_`, footnote `*`, şablon id'leri T01–T22). Bu dosya dmscales stil kitinin (`~\ToonStudio-Projects\Style Kit\dist\custom-dmscales\`) beklediği formattadır; ses kaydı gelince zamanlar gerçek ses dosyasından yeniden alınır.
   - Ses ayarları (ElevenLabs + müzik yatağı) `onscreen.md` §5'ten pakete eklenir.

8. **Sohbete** yalnız kısa özet yaz: seçilen başlık, ilk 2 cümle (hook), kavram adları, QC skoru, kaç `[KAYNAK GEREKLİ]` kaldığı ve dosya bağlantıları.

## Çıktı

Klasör: kullanıcının çalışma klasöründe `uretim/<slug>/` (yoksa oluştur). Dosyalar: `paket.md`, `script.txt`, `script_timed.txt`, `edit-plan.md`.
`paket.md` şablonu `templates/paket_template.md`'dedir; bölüm başlıklarını değiştirme (QC `## 4.` bölümünü okur, `Hedef süre:`, `Gizli sayaç:`, `Kavramlar:` satırlarını arar).

## Kesin kurallar (ihlal = yeniden yaz)

- İlk cümle sistemin **1. adımıdır** (2. tekil, in-medias-res, 18–30 kelime). Selam, "bu videoda", kendini tanıtma, soru ile açılış YOK.
- Ayrı "hook", "çatışma" ya da "ders" bloğu kurma; her ceza kendi aşamasında taktiğiyle eşleşir.
- Doruk videonun %76–82'sinde; doruktan sonra rahatlatma değil **uyarı** gelir; video tedirgin biter ve çözümü CTA varlığı sunar.
- CTA tek seferdir, içerikteki son sorunun çözümüdür, sürenin ≤%12'si. "Abone ol / beğen / bildirimleri aç" YOK. "Ben/benim" yalnızca CTA'da (ve varsa tek kişisel kanıt cümlesinde).
- Paketlemede vaat edilen her kavram (başlık, bölüm adı, etiket) senaryoda isimlendirilir ve geri çağrılır.
- Doymuş "nasıl viral olunur / nasıl yapılır" açısı değil, boş "**nasıl çalışır**" açısı.
- Sponsor/araç tanıtımı yok; gerekiyorsa ≤10 sn ve içerikten çıkan bir soru kılığında.
- Gerçek bir kurumun arayüzünü birebir taklit eden sahte ekran görüntüsü üretme; kanıt kartları ya kullanıcının gerçek ekran görüntüsü ya da açıkça "temsilî" işaretli çizimdir.
- dmscales'in kendi etiketlerini ("zero view jail", "trust score") başka konulara kopyalama; her konu kendi kavramlarını alır. (Konu YouTube Shorts ise topluluk terimi olarak anılabilir.)

## Referans dosyaları

| Dosya | Ne zaman |
|---|---|
| `references/topic_fit.md` | Adım 1: 5 soru, puanlama, açı dönüştürme, 20 TR konu bankası |
| `references/engine.md` | Adım 3–4: merdiven, ünite, gerilim salınımı, isim üretme, aşama şablonları, yapma listesi |
| `references/phrasebook_tr.md` | Adım 4: 25 kalıp (TR+EN), ritim, sözcük seçimi, yasak dolgu |
| `references/budgets.md` | Adım 4: 120/180/300 sn bütçe tabloları ve doldurulabilir iskeletler |
| `references/qc.md` | Adım 5: 15 ölçüt + otomatik kontrollerin açıklaması |
| `references/packaging.md` | Adım 6: başlık, thumbnail, açıklama, etiket, sabit yorum, seri |
| `references/onscreen.md` | Adım 7: ekran metni kuralları, edit-plan formatı, şablon eşlemesi, ses spec |
| `references/examples.md` | Format örneği (QC'den geçen tam 180 sn Türkçe senaryo) |
| `references/sources.md` | Ham analiz dosyalarının yerleri (derin ayrıntı gerektiğinde) |
