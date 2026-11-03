# 03 — Senaryo motoru

Hedef: **45–65 sn**, 160–230 kelime, 205–220 wpm. Ölçüm kaynağı `deep-research/B`.

## 1. Beat-sheet (11 vuruş; yüzdeler hit'lerden ölçüldü)
| # | Vuruş | % | 55 sn'de | Görev |
|---|---|---|---|---|
| 1 | **HOOK (iddia)** | 0–7 | 0–3,8 | Tek cümle, 12–19 kelime: fail + tuhaf eylem/nesne + stake. **Soru değil.** |
| 2 | Tepki / ilk bahis | 7–14 | 3,8–7,7 | Biri güler, inkâr eder ya da vaat büyür ("Everyone laughed." / "Yet…"). |
| 3 | Dünya kuralı ("You see,") | 10–25 | 5,5–14 | Gereken TEK kural. Mekanizmayı **sakla**. |
| 4 | İtiraz / "wait what" ("But…") | 20–30 | 11–16,5 | Mantıklı karşı-argüman ya da audience proxy. Merakı ikiye katlar. **İkinci hook 10–13 sn'de.** |
| 5 | Sahte alarm / ilk test | 25–40 | 14–22 | Bir şey olur ama yanlış yorumlanır ya da "nothing happened". |
| 6 | Tırmanma merdiveni (3 basamak) | 35–62 | 19–34 | "Then… Then… Then all of them…". Cümleler kısalır (2–6 kelime). 1 komik diyalog ya da alay. |
| 7 | Karşı-ipucu + audience proxy | 50–62 | 27–34 | Biri farklı davranır → "Wait, X?" |
| 8 | **TWIST** | 60–72 | 33–39,5 | Durum tersine döner. Medyan %65, **%75'i geçme.** |
| 9 | Mekanizma (ikinci "You see,") | 67–88 | 37–48 | Tek nefeste neden-sonuç zinciri A → B → C (25–33 kelimelik tek zincir cümle). Gündelik analoji. |
| 10 | Payoff / punchline | 88–97 | 48–53 | Yeniden çerçeveleme ya da ironi; açılış nesnesine geri dön. |
| 11 | **Kapanış hükmü + teaser** | son 2–3 sn | 53–56 | Clause'un damgası: "Legal? **Approved.**" + yorum sorusu ya da sonraki dava teaser'ı. CTA payoff'tan **sonra**. |

**Ritim kuralları:**
- 8–10 sn'de bir pivot (hedef ≥6/dk); çeşitli olsun: but, yet, except, instead, wait, you see, so.
- "You see," tam 2 kez geçer: dünya kuralı ve mekanizma.
- 1–2 diyalog satırı (alay ve otoritenin reddi), %35–60 aralığında.
- Cümle ortalaması 11–18 kelime. Uzun-kısa-kısa dalga: 20+ kelimelik cümleden sonra 2–5 kelimelik yumruk ("Big mistake.").

## 1b. "Sen simülasyonu" kalıbı (Japan Job 14,7M, kanalın en yüksek yorum oranı). Gerçek bir sistem ya da meslek için TERCİH ET
Kullanıcı 2026-10-31'de "hedefin anlattığı gibi anlatalım" dedi. Haber/liste tarzı (isim + yıl + rakamlar başta, örnekler alt alta) izleniyor ama yorum getirmiyor.
1. **0–4 sn paradoks:** Kural + "Ama" + daha tuhafı. İsim ve tarih yok.
2. **"Hayal et:"** ile izleyiciyi kahraman yap. Videonun geri kalanı 2. şahıs ve şimdiki zaman ("ediyorsun, istiyor").
3. **Kısa diyalog** (patron, müşteri) → izleyicinin itirazı tırnak içinde: "Bekle, …?"
4. **Sahte rahatlama** ("İlk başta…") → 3 küçük, somut basamak.
5. **Karşı ipucu / kuralın sınırı** → **twist** (%60–72).
6. **Tek cümlelik mekanizma** ("İşin sırrı şu:").
7. **Gerçeklik ifşası** (bizim eklememiz, doğruluk kuralı için): "Ve bu hayal değil. [İsim] bunu [yıl]'den beri yapıyor…"
8. **Ahlak cümlesi, açılışa dönüş:** VO'da damga, çağrı ya da "gönder" cümlesi YOK. Yorum sorusu ve gönderim çağrısı açıklamaya taşınır. `script.json` → `"closing": {"mode": "punchline"}`; validate.py bu modda verdict beat'ini aramaz, son satırın hook ile ortak kelimesini kontrol eder.
Örnek: `C:\dev\viral-reels-tr\tr-003-hicbir-sey-yapmayan-adam\script.json`.

**Saha kanıtı (2026-11-02, TR hesap):** tr-004 kovma odası IG'de 702K görüntüleme, 1.169 yorum (1,66/1K), 1.821 kaydetme aldı; kullanıcı kalıbı "tamamen başarılı" ilan etti. Yayınlanan sürüm script.json'dan **sadeleştirilmişti** ve bu sürüm esas alınır:
- 120–145 kelime, ~45–55 sn. "İşin sırrı şu" yok; mekanizma "Çünkü …" ile tek cümle.
- VO'da isim, yıl, gazete ya da kaynak yok (madde 7'deki gerçeklik ifşası VO'dan çıkar, sabit yoruma gider).
- Sahte rahatlama soru biçiminde: "İlk başta harika, değil mi? İş yok, maaş var."
- Üçlü tekrar: "aynı oda, aynı duvar, aynı sessizlik."
- Kapanış: tek ve cevaplaması çok kolay kişisel soru ("Peki sen bu odada kaç gün dayanırdın?"). Çoklu seçenek ekleme.
- Zayıf nokta: takip dönüşümü %0,025 → açıklamaya "önceki dosya" / seri bağlantısı koy.
Bu kalıpla yazılan ikinci örnek: `tr-016-kaybolan-insanlar`.

## 1c. Tarih kalıbı (Jar 28,8M, Spear vs Shield 7,7M). TARİHİ bir olay için ZORUNLU
Kullanıcı 2026-10-31'de "sen" ile yazılmış Zanzibar metnini "çok karışık, rakipler böyle anlatmıyor" diye reddetti.
- **"Hayal et / sen" kullanma.** Tek kahraman, 3. şahıs, di'li geçmiş: "Bir adam… koydu ve imparatora dedi ki…"
- Olaylar **tek iplikte, sırayla** akar. Araya meta cümle ("asıl tuhaf olan…"), kaynak cümlesi, kayıp sayısı ya da yan bilgi girmez; bunlar açıklamaya ve sabit yoruma gider.
- **Tarih ve yıl yok, rakam minimum.** 28,8M'lik videoda tek bir yıl bile geçmiyor.
- Kısa yumruk cümleler: "Sonra bir top düştü. Sonra bir tane daha. Sonra sekizi birden."
- Sonda "İşin sırrı şu:" ile tek nefeste mekanizma, ardından başa dönen tek bir cümle. İstenirse en sonda tek satırlık kısa soru.
- Hedef 120–150 kelime (~50–55 sn). Örnek: `C:\dev\viral-reels-tr\tr-006-38-dakika-savas\script.json`.
- **"Sen simülasyonu" (1b) yalnızca bugün de geçerli bir sistem ya da meslek için:** kovma odası, kiralık adam vb.

## 2. Anlatıcı sesi
- **Şahıs:** 3. tekil kahraman (He/She/A clerk) + izleyiciyi içeri çeken "you" köprüleri ("Think about the last time your…"). 1. tekil (I) yok, anlatıcı görünmez. Clause yalnızca kapanışta konuşur.
- **Zaman:** Açılış geçmiş zaman, sahne ortası şimdiki zaman (aciliyet), mekanizma geniş zaman.
- **Seviye:** 5.–7. sınıf kelimeleri. En fazla 1 teknik terim, hemen çevrilir ("which is a fancy word for…"). Sayılar yuvarlak ve somut (12,000 puddings, 2 a.m.).
- **Mizah:** Abartılı benzetme, otoritenin alayı, "So he does what any sane person would do.", Fortunately/Unfortunately çifti.
- **Audience proxy:** Her videoda 1 kez, tırnaksız, %28–60 aralığında: "Wait, *pudding*?"

## 3. Cümle şablonları (yapısal; doldururken rakip cümlesi kopyalanmaz)
1. Tehdit hook'u: "[Kişi] put [nesne] in [tuhaf yer] and told [otorite], 'If this [olur], [ekstrem eylem].'"
2. Paradoks hook'u: "[X] is illegal in [yer]. Yet [X] is on every corner."
3. Koşullu vaat: "If you [absürt ritüel], you could wake up with [kazanç]."
4. Kural: "You see, back then [dünya kuralı], so [somut gelenek]."
5. İtiraz: "But [antagonist] had [güç kaynağı], and he wasn't scared of a [küçük nesne]."
6. Sahte alarm: "[Zaman] later, [işaret] came. And nothing happened. Not even [abartılı küçültme]."
7. Merdiven: "Then [1]. Then [2]. Then [hepsi] at once."
8. Proxy: "Wait, [son tuhaf kelime]?"
9. Analoji köprüsü: "Think about the last time you [gündelik refleks]. You didn't decide that. [Sistem] did."
10. Mekanizma zinciri: "The tiniest [tetik] and [A] hits [B], [B] opens [C], and [sonuç]."
11. Kâğıt üstü punchline: "[Fiziksel alışveriş], and on paper, nobody ever [suç]."
12. Ters çevirme: "And the only person who [kazandı] was the one everyone laughed at."
13. Damga kapanışı (Clause): "[Hüküm sorusu]? *Approved.*" / "Legal? Technically. Smart? Stamp it."

## 4. Yorum ve paylaşım cihazları (her senaryoda **≥2 yorum + 1 send**)
**Yorum:**
1. Kişisel pazarlık: "They'd pay you $40 an hour to stand in line, no phone. How long do you last?"
2. Meydan okunabilir hüküm: "Nobody beats this rule twice."
3. Meme kelimesi: tuhaf, somut bir isim, 2 kez tekrarlanır ("12,000 puddings").
4. Kontrollü açık: "Why didn't he just cash out?" Cevap **sabitlenmiş yorumda**.
5. Tartışmalı iddiada "Most historians say…" ve "some call it a myth".
6. İçeriden kişi çağrısı: "Flight attendants — is this true?"

**Send (VO içinde, payoff'tan önce):**
- Kimlik etiketli alıcı: "…your friend who never reads the terms."
- Pratik değer: "Next time you fly, ask the gate desk first."

Yasak: kasıtlı bilgi hatası, kumarı teşvik eden ton, tek kelimelik "Overkill or genius?" sorusu.

## 5. Format: `script.json` (validate.py bunu denetler)
```json
{
  "slug": "airline-seat-twice", "case_no": 14, "series": "Small Print",
  "title": "Why Airlines Sell Your Seat Twice",
  "archetype": "GK", "hook_type": "H2", "fact_flag": "G",
  "sources": [{"claim": "Airlines overbook based on no-show rates", "url": "https://...", "url2": "https://..."}],
  "lines": [
    {"n": 1, "beat": "hook", "text": "An airline sold the same seat to two strangers, and it planned to do it.",
     "pause_after": 0.4,
     "shot": {"noun": "boarding pass", "setting": "1990s airport gate, neon night", "camera": "push_in",
              "transition": "dissolve", "clause": false}}
  ],
  "devices": {"comment": ["personal_bargain", "pinned_answer"], "send": "identity_tag", "meme_word": "the 9 a.m. flight"},
  "closing": {"verdict": "APPROVED", "teaser": "Case #15: the lifetime ticket airlines regretted"}
}
```
`beat` değerleri: hook, reaction, rule, objection, false_alarm, ladder, counter_clue, twist, mechanism, payoff, verdict.

## 6. Doğruluk kuralı: "Gerçek mekanizma, dürüst çerçeve"
1. Mekanizma, sayı ve tarih **%100 doğru** olur. Her olgusal iddia için **2 bağımsız kaynak** `sources[]`'e yazılır. Kaynaksız cümle senaryodan çıkar.
2. Karakter, diyalog ve ara sahne dramatize edilebilir. Ama tarihsel **sonuç** (ölüm, yıkım, tutuklama, rakam) **asla uydurulmaz**.
3. Fabl ya da efsane ilk 5 sn'de işaretlenir: "Legend says…", "The story goes…". `fact_flag` = "K" olur ve açıklamaya "Dramatized" notu eklenir.
4. Bilimin desteklemediği "always / never / impossible" mutlakları kullanılmaz.
5. Ülkeye bağlı yasal iddialarda kapsam söylenir ("in the US").
6. Zamana bağlı iddialar yıl verilerek yazılır.
7. Yayın öncesi test: "Bir izleyici bu cümleye 'yalan' derse kaynak gösterebilir miyiz?" Hayırsa cümleyi çıkar.

Kaynak ararken WebSearch kullan, birincil kaynağı tercih et (resmi belge, akademik yayın, büyük gazete). Wikipedia tek başına yetmez, ancak 2. kaynak olabilir.
