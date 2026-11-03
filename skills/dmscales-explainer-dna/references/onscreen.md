# Ekran metni, edit-plan ve ses

Kaynak: `ToonStudio-Projects\research\dmscales\reports\script_audio.md` §3–5, `visual.md`, `motion.md`, stil kiti `Style Kit\dist\custom-dmscales\skill\DIRECTION.md` + `STYLE_GUIDE.md` + `SOUND.md`.

Kural sırası: **ses metni asla değişmez**; ekran yoğunlaştırabilir, dipnot ve alıntı ekleyebilir.

## 1. Senaryodaki `(EKRAN: …)` satırları
Senaryo yazılırken şu anlarda EKRAN satırı zorunludur:
- Deiktik söz ("şunlardan biri", "bu grafik", "buraya kadar", "böyle", "bunlar") → gösterilecek şey.
- Bantlı teşhis → 3 maddelik liste (seslendirilmez).
- Rakam/eşik → stat kartı ("VVSA: <%80").
- Kanıt gerektiren iddia → kullanıcının ekran görüntüsü (yoksa `kullanıcıdan: …` notu) ya da temsilî kart.
- Her ~30 sn'de en az 1 "yalnız ekranda" bilgi (dipnot ipucu, kaynak notu, şaka).

## 2. Anlatım → ekran dönüşüm kuralları (ölçülmüş oranlar: %55 birebir parça, %15 başlık/etiket, %20 yıldızlı dipnot, %10 alıntı)

1. **Parçalama:** cümleyi virgül, bağlaç (ve, ama, çünkü, yani, sonra) ve ~6 kelimeden sonra böl. Kart başına 3–8 kelime (medyan 6), ~1,2–1,8 sn. Uzun bir yan cümlede yalnız **son** içerik parçası gösterilir.
2. **Biçim:** tamamı küçük harf (başlıklar ve vurgulu kelimeler hariç); dolgu atılır; "ama, ve, yani" kalır. Dipnotlarda gündelik yazım serbest ("~", "yt", "ör:").
3. **Tanımlar:** "Buna X deniyor" / "X denen gizli bir ölçü" → BAŞLIK kartı "X:" büyük harf, ayırt edici kelime kırmızı ("DENEME **ODASI**:", "**GÜVEN** PUANI:"); altında 1–3 "- " madde kendi kelimesinde belirir.
4. **Listeler:** iki noktayla biten uydurma başlık ("NASIL DÜZELİR:", "SİSTEMİN BAKTIĞI 3 ŞEY:"); her söylenen madde kendi kelimesinde "- madde" olarak eklenir; maddeye küçük (parantez) açıklama eklenebilir.
5. **Tırmanma:** "ama en önemlisi" kendi temiz kartını alır (renksiz); sonra son madde büyük gelir, öncekiler %45'e küçülür.
6. **Renk:** kart başına 1–2 kırmızı kelime (en fazla 3): kavram adı (~%45), değerlendirici sıfat (~%25: gizli, aynı, kötü, ücretsiz), ana fiil (~%20: iter, harcar, düşürür), rakam (~%10). Zamir/edat/bağlaç asla kırmızı değil. **Yeşil** yalnız iyi/istenen taraf, ~30 kartta bir. **BÜYÜK HARF + kırmızı** vurgulu pekiştirici (ASLA, GERÇEKTEN, TAM OLARAK). **Altçizgi** "sen/senin" ya da anlamı değiştiren karşıtlık kelimesi.
7. **Deiktikler:** "bu / şunlar / burası / böyle" → kare referansı göstermek ZORUNDA (ekran görüntüsü, liste, rakam) + elle çizilmiş kırmızı ok/daire.
8. **Rakamlar** rakamla, "yaklaşık" → "~", aralık "100 - 10.000"; her kısaltmaya sözlük dipnotu.
9. **Dipnotlar** "*" ile, ana öğenin altında ortalı, ~%40 boyut: uyarı ("*bu puanı görmek imkânsız"), daha sıkı ipucu, kaynak ("*kaynak: Meta Şeffaflık Merkezi"), feragat ("*temsilî görsel", "*benim ekran görüntüm değil"), emojili şaka. 6–10 sn'de bir.
10. **Alıntılar:** izleyici düşüncesi → çöp adam yanında küçük harf "çift tırnak"; algoritmanın düşüncesi → beyin görseli yanında ("hmm, bunu kim sonuna kadar izler…"); karşı görüş → meme görseli. VO birinin ne istediğini/düşündüğünü anlatıyorsa alıntı yaz.
11. **Sorular:** VO'daki problem cümlesi ekranda soruya çevrilebilir ("*neden boşuna izleyici harcasın?").
12. **Yalnız ekranda:** teşekkür, araç adı, "Kısa not:" ipuçları — her 30 sn'de ≥1.

## 3. Cümle tipi → görsel şablonu (stil kiti id'leri)

| VO cümle tipi | Görsel | Şablon |
|---|---|---|
| "…yaptığında" (izleyici eylemi) | çöp adam (yüz sonuca göre), sağda metin | T07 |
| Rakamlı platform iddiası | gerçek analytics/arayüz görüntüsü + kırmızı ok/daire + dipnot | T10 / T12 |
| "Buna X deniyor" | başlık kartı "X:" + maddeler | T04 |
| Çözüm/nasıl yapılır listesi | büyüyen liste "NASIL DÜZELİR:" | T03 |
| Geçiş ("ama en önemlisi", "ve bu sırada:") | düz metin kartı, renksiz | T01 |
| Algoritma ne ister/düşünür | beyin görseli + alıntı | T09 |
| İzleyici ne ister/düşünür | çöp adam + telefon/düşünce bulutu + alıntı | T08 / CLD |
| Kitle, rekabet, arz-talep | kalabalık / "Videomu izle!" büstleri | T14 / T15 / T19 |
| İki seçenek | yan yana kutular | CMP |
| "Grafik şöyle görünür" | elle çizilmiş eğri (şekil, veri değil) + etiket | CRV |
| Büyüme / viral | yeşil zikzak çizgi | GRW |
| Bölüm başı | "BÖLÜM 2: NASIL {ÇIKILIR}" kartı | PRT |
| En iyi sonucun ifşası | siyah vizör + kart | VF |
| CTA | kendi kanal/oynatma listesi görüntüsü, topluluk logosu | T10 |

Ekran süresi hedefi: kanıt medyası %40–55, metin kartları ~%35, figür/kalabalık ~%15. Aynı şablon 3 kez üst üste olmaz; her dakikada kanıt + tip + çizim ailelerinin üçü de bulunur.

## 4. edit-plan.md formatı (stil kiti girişi)

`scripts/edit_plan_scaffold.py` iskeleti üretir; sen her bloğu doldurursun:
```
## S07  1:12.4  T10 screenshot + footnote
say:    "aim to get your retention up to here."      <- VO parçası, birebir (değiştirme)
screen: to get your {retention} up to _here_          <- markup: {kırmızı} {g:yeşil} _altçizgi_ **kalın**
media:  analytics_week3 (w 870) + mark circle on the 70% bar
foot:   *anything above 60% on a 10 min video is great
quote:  (varsa) "…"
enter:  pop on "aim" ; mark wipe on "here" ; foot pop +0.4 s
note:   (varsa) kullanıcıdan istenecek dosya / EKRAN satırı
```
Hız: ilk 15 sn'de 0,7–1,2 sn'de bir yeni çekim; sonrasında dakikada 15–23 çekim (medyan 2–4 sn), hiçbir çekim 6 sn'yi pop'suz geçmez. İlk çekim 0,0 sn'de ekranda. Zamanlar tahminidir; gerçek ses kaydı (`audio/script_timed.txt`) gelince stil kiti kelime zamanlarına göre yeniden hizalar.
Medya: kullanıcının gerçek dosyası yoksa `media: -` ve `note: kullanıcıdan: <ne lazım>`; **sahte ekran görüntüsü çizme**.

## 5. Ses spec (pakete ekle)

- **Ses:** ElevenLabs, genç erkek (veya kanalın kayıtlı sesi), rahat ve kendinden emin, hafif monoton, gerçekçi (hype değil). Türkçe hız ~165–180 kel/dk → speed ~1,1–1,2; stability ~0,45, similarity ~0,8, style ~0,15.
- **Nefes kesimi:** cümle arası sessizlik 0,10–0,20 sn, yan cümle arası 0,05–0,12 sn; hiçbir duraklama 0,35 sn'yi geçmez (vuruş cümlesinden sonra bilinçli 0,5 sn hariç).
- **İşleme:** kompresör 4:1 → limiter; ses ~−18/−19 LUFS, true peak −1 dBTP, LRA 3–5 LU.
- **Müzik:** tek sürekli lo-fi/chill-trap enstrümantal, 75–95 BPM (varsayılan 85), vokal/drop yok; 0,0 sn'de tam seviyede başlar (fade-in yok), son kareye kadar sürer; sesin 8–10 LU altında (~−27/−29 LUFS), **ducking yok**. 5 dk üstünde bölüm sınırında parça değişebilir.
- **SFX:** yok (hitlerin "klasik" profili). Metin kartlarında pop/ding asla.
- **Master:** −16/−18 LUFS entegre, −1 dBTP.
- Stil kiti için `audio/beds.json`: `{ "beds": [ { "from": 0, "to": <N>, "type": "music", "mood": "curious", "bpm": 85, "gain": -30 } ] }`
