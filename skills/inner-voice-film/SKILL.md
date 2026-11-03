---
name: inner-voice-film
description: Animated short film studio for the YouTube channel "The Other Self" — turns a TITLE + TOPIC into a retention-engineered screenplay and a production-ready Remotion (React + SVG) film starring the channel's own main character "Moon head" (big round sand-coloured head, small body, sprout on top) and his electric-blue-glowing black shadow twin (the inner voice / "the other self"), using the proven structure reverse-engineered from "DISCIPLINE | An Animated Short Film" (3.1M views) and "DOPAMINE" — DAY counters, black letterboxed stage, limited animation, silent white narrator text, and the blue inner voice (shadow twin) SPOKEN with the user's ElevenLabs voice "Second Self - Solitude". Built from 10 expert reports + frame-by-frame measurement of the real films. Use this skill WHENEVER the user wants an animated short film / 2D animasyon / motivasyon animasyonu / Remotion videosu / SVG karakter animasyonu about a psychological struggle (disiplin, erteleme, yalnızlık, aşk, kalp kırıklığı, overthinking, kaygı, karşılaştırma, telefon bağımlılığı, dopamin, yas, konfor alanı, öz değer…), mentions The Other Self, "ay kafa", "ana karakterimiz", "gölge ikiz", says "DISCIPLINE gibi", "Day One Films tarzı", "iç ses / gölge", "bu konuda animasyon yap", "senaryo yaz ve videoyu yap", gives a title + topic for a short film, or asks for hooks, beat sheets, thumbnails, titles, descriptions or Shorts for such a film — even if Remotion is not named.
---

# Inner-Voice Film Studio — The Other Self

> **ANA KARAKTERİMİZ: "Ay kafa".** Kanalın tüm filmlerinde başrol budur, başka karakter tasarlanmaz.
> Kaynak: `assets/brand-the-other-self/` → `CHARACTER.md` (spesifikasyon), `hero-rig.js` (`STYLES.moon`,
> çizim + rig + 15 ifade + 10 poz + gölge ikiz), `character-sheet.png` (görsel referans — üretime başlamadan
> bak). İç ses = onun birebir siyah ikizi, elektrik mavisi parlıyor. Referans dosyalardaki "krem fasulye
> karakter" ve "kırmızı" değerleri rakibin ölçümüdür; **kanalda yerlerine bu karakter ve marka renkleri
> (`references/06-sets-and-light.md` §6 `brand`) kullanılır.** Yapı, zamanlama ve animasyon dili aynen geçerlidir.

Bu skill tek bir şeyi kusursuz yapar: **bir başlık + konu** alır, kanıtlanmış "iç ses" yapısıyla
**senaryoyu** yazar, **Remotion + SVG** ile animasyonu kodlar, kareleri **gözle denetler** ve videoyu render eder.
Referans: DISCIPLINE (2:39, 3.1M izlenme / ~2 hafta) ve DOPAMINE (2:41, 283K). Yapı ve stil kopyalanır;
**rakibin cümleleri, sloganları ve hikâyesi birebir kopyalanmaz** — her film özgün satırlarla yazılır
("Day one, or one day.", "Nobody is coming to save you." gibi imza satırlar yalnızca örnektir).

## Önce beyin, sonra yüzey

Kopyalanan şey **yapı ve mantıktır**: hook → çatışma → ilerleme sayacı → dip noktası → dönüm sembolü →
montaj → halka kapanışı. Her bölümün **tek bir işi** vardır. Neden-sonuç tablosu ve doz kuralları:
`references/01-story-engine.md` §1b. Karakter, metin, müzik ve sahneler her filmde özgün üretilir.

**Kanal: THE OTHER SELF.** Resmi ana karakter `assets/brand-the-other-self/` (CHARACTER.md + hero-rig.js +
character-sheet.html, `STYLES.moon`). Her filmde BU karakter kullanılır: **"Ay kafa"** — büyük yuvarlak kafa +
küçük gövde + çöp uzuvlar + tepede filiz + dikey oval gözler + ince mürekkep kontur, kum rengi `#E9C9A2`; iç ses
onun birebir siyah ikizi (aynı silüet, aynı filiz) ve **elektrik mavisi** `#2F6BFF` parlıyor — kanalın varsayılan
`topicAccent`'i kırmızı DEĞİL mavidir (kırmızı rakibin imzası). Filiz büyüme motifi olarak kullanılabilir (dipte
sarkar, dönüşte dikleşir). Bu dosya
`references/05` ve `deep-research/05`'teki karakter tasarımının önüne geçer (rig matematiği aynı). Stüdyoda
`src/lib/character/` bu dosyadan birebir TSX'e taşınır. Açıklama şablonundaki kanal adı: "The Other Self".

**Özgünlük / telif:** Görsel kanon rakibin ölçülmüş stilidir — "dil"i (siyah sahne, sınırlı animasyon,
renk kodlu yazı, iç ses figürü) referans alır ama kanalın **kendi imzası** vardır ve **kararlaştırılmıştır**:
Ay kafa karakteri + siyah gölge ikizi + elektrik mavisi marka rengi + kanal adı The Other Self. Bunları
`lib/theme.ts` (`accent.brand`) ve `lib/character/` olarak uygula; kullanıcı açıkça istemedikçe değiştirme.
Rakibin karakterini, kırmızı parıltısını veya cümlelerini kullanma. Müzik/SFX ya prosedürel üretilir ya da lisanslıdır; lisans `public/sfx/LICENSES.md`'ye yazılır.

## Modlar

| Mod | Tetik | Çıktı |
|---|---|---|
| **FILM** (varsayılan) | "X başlığı / Y konusu için animasyon yap" | paket → senaryo → (onay) → kod → still QA → taslak → final mp4 + YouTube paketi |
| **SCRIPT** | "sadece senaryo", "beat sheet", "hook yaz" | senaryo dosyası (template) + paket |
| **PACKAGE** | "başlık / thumbnail / açıklama / Shorts" | 10-packaging.md kuralları ile paket |
| **FIX** | "şu sahne bozuk", "kol kopuyor", "yazı geç geliyor" | kanona göre teşhis + düzeltme + still ile doğrulama |
| **ANALYZE** | yeni rakip video/kare verildiğinde | kare analizi → kanonu güncelleme önerisi |

## Değişmez stil DNA'sı (bunları bozan film bu kanal gibi görünmez)

1. **Siyah sahne + letterbox**: `#0B0B0B` + yumuşak vinyet, üst ve alt **96 px** saf siyah bant, tek ince gri zemin çizgisi. Renk yalnızca nesnelerde/ışıklarda.
2. **Kahraman**: kanalın kendi karakteri "Ay kafa" (aşağıdaki The Other Self bölümü); arka uzuvlar aynı boya %55 opaklık. İsimsiz, sessiz, hiç konuşmaz. (Rakibin ölçülmüş krem fasulye karakteri yalnızca referanstır, kullanılmaz.)
3. **İç ses**: kahramanın birebir siyah ikizi, saf siyah, yumuşak sabit (nabızsız) parıltı (`topicAccent`, varsayılan elektrik mavisi `#2F6BFF`), parlayan yarık gözler + gülümseme. Yürümez: mobilyanın arkasından ya da yerden **yükselir**. Boyu gücünü değil çaresizliğini gösterir: 1.1× → 1.2× → ayna 1.0× → dev 2.5–3× → minik 0.5×.
4. **Sınırlı animasyon**: aynı anda tek şey hareket eder; vuruşlar arası 0.3–1.5 s bekleme; yüz ifadeleri tek karede değişir; oyunculuk pozları "pop" eder; nefes/sallanma yok. Canlılığı yavaş kamera push-in (+%1.25–1.5/s), parçacıklar, ışık, prop'lar ve yazı verir. Tam mekanik animasyon (koşu, şınav, yumruk, tırmanış) sadece fiziksel aksiyonlarda.
5. **KULLANICI KARARI (2026-10-15): gölge ikizin mavi replikleri SESLENDİRİLİR** — kullanıcının kendi ElevenLabs sesi **"Second Self - Solitude"** (voice_id `PL7EYPTnZppHWj5yLiVI`, `eleven_v3`, stiller whisper/taunt/boss; anahtar env `ELEVENLABS_API_KEY`). Stüdyoda `voice.json` + `python scripts/eleven_say.py src/films/<slug>/voice-lines.json`. Ses kullanıcı onayı olmadan değiştirilmez. Müzik replik altında ~−8 dB kısılır. Beyaz anlatıcı sessiz kalır. Müzik sakin olmalı: yumuşak piyano + pad; detone müzik kutusu, sürekli saat tıkırtısı, hışırtılı fısıltı ve davul YOK (kullanıcı "çok gıcık" dedi). Örnek boru hattı: stüdyoda `scripts/fetch-insomnia-voice.ps1` + `scripts/insomnia-cues.mjs`.
   **Beyaz anlatıcı için: seslendirme yok — yazı anlatıcıdır**: beyaz = anlatıcı/ders (cümle düzeni + nokta), accent (marka: mavi `#6E9BFF`) = iç ses/bahane (küçük harf + nokta, asla "!"), gri `DAY N` sol üst. Aynı anda tek mesaj; beyaz ve accent yazı aynı karede olmaz. Font: Comic Sans görünümü (Comic Relief).
6. **Hook**: siyah ekranda tek beyaz cümle (4–8 kelime, geçmiş zaman, soru değil) → herkesin bildiği ritüel → ritüel başarısız + tek kelimelik accent renkli hüküm ("again.") — hepsi ilk 15 saniyede.
7. **Yapı**: 13 beat; dip noktası %31–40'ta spot ışığı altında, kimlik dönüşümü cümlesi ("X isn't who you are. It's what you repeat.") + "He" → "you" geçişi; aynı ritüel sahnesi 3 kez (başarısızlık / seçim / sahiplenme); her iç ses cümlesi Act 3'te fiziksel olarak yenilir; dev boss en kısa cümleyi söyler; sadece zirvede sıcak palet; minik gölgeli bookend; TEK KELİME başlık + ≤6 kelimelik chiasmus slogan.
8. **Geçişler**: siyaha "dip" (çıkış 8–12 f, giriş 15–24 f, siyahta bekleme yok); zaman atlaması = sert kesme.
9. **Deterministik kod**: her şey `useCurrentFrame()` + `interpolate` (clamp) / `spring` / `random(seed)`; `Math.random`, CSS animasyonu, zamanlayıcı yasak. Uzuvlar FK ile hesaplanıp tek path olarak çizilir → kopma imkânsız.
10. **Süre** 2:30–2:45 (kullanıcı aksini istemedikçe). Başlık formatı `WORD | An Animated Short Film`.

Ayrıntı ve ölçülmüş değerler: `references/03-visual-canon.md` — **diğer tüm kaynaklarla çelişirse bu dosya kazanır.**

## FILM iş akışı (adım atlama)

**0. Girdiler.** Başlık, konu, (opsiyonel) süre, ekrandaki yazı dili (varsayılan İngilizce — kanal İngilizce;
Türkçe istenirse 07-text-system Türkçe kuralları), hedef kanal adı (açıklama için). Eksikse makul varsayılanla
ilerle, varsayımı belirt.

**1. Konu çözümü.** `references/11-topic-bank.md`'de konu varsa başlangıç olarak al; yoksa
`references/01-story-engine.md` §5 Topic Adaptation Engine'in 12 adımını uygula. Arketip seç (varsayılan A).
Başlık konunun "acı kelimesi" değilse (`references/10-packaging.md` §2) kullanıcıya alternatif öner.

**2. Hook + paket önce.** `references/02-hook-and-retention.md` §3'ten 3 hook varyantı yaz, kısıtlara göre
birini seç (diğer ikisini Shorts hook testi için sakla — `10-packaging.md` §7). Başlık + 2 alternatif +
thumbnail şablonu + gölge satırı. Konunun sayaç birimini seç (gün, mesaj, sayfa, km, para…).

**3. Senaryo.** `templates/screenplay-template.md` formatında, her çekim için kare aralıklarıyla yaz.
Beat yüzdeleri, voice ledger, couplet'ler, slogan. Sonra `01-story-engine.md` §7 ve
`02-hook-and-retention.md` §7 (retention killers) ile denetle; düzelt. Senaryoyu
`films/<slug>/SCREENPLAY.md` olarak kaydet ve **kullanıcıya özetleyip onay iste** — kod üretimi pahalıdır,
hikâye onaysız inşa edilmez (kullanıcı "direkt yap" dediyse atla).

**4. Stüdyo.** `references/09-remotion-build-and-qa.md` §1. Stüdyo (varsayılan `C:\dev\dayone-studio`, OneDrive
dışı) yoksa kullanıcıya bir kez sorup kur; varsa yeniden kullan. `lib/` içindeki bileşenleri yeniden kullan,
eksikleri ekle — **karakter ve gölge ikizi her zaman `assets/brand-the-other-self/hero-rig.js`'ten** birebir
TSX'e (karakter sayfasıyla still karşılaştırarak doğrula); diğerleri `deep-research/` kodundan (hareket tabloları → 06,
iç ses davranışı → 03/04, metin → 04, setler → 07,
hareket → 06, zaman çizelgesi → 08). Uyarlarken `references/` içindeki düzeltmeleri uygula.

**5. Senaryo → veri.** `src/films/<slug>/script.ts` (FilmScript). Her çekim bir SceneSpec. Kare numaraları
`makeGrid()` müzik ızgarasından gelir; aynı numaralar animasyon ve ses için kullanılır.

**6. Sahneler.** Sahne sahne kodla; her sahne için önce `<slug>-<scene>` kompozisyonundan 2–3 still al ve bak.
Sırayla: hook kartı → ritüel → … → başlık kartı. Global katmanlar: DipOverlay, TopicHUD, Letterbox (09 §4).

**7. Ses.** (a) **İç ses = ElevenLabs (zorunlu).** Gölgenin her mavi repliğini (bahane, hüküm, VOICE, boss)
`src/films/<slug>/voice-lines.json`'a yaz (`{n, text, style: whisper|taunt|boss, spoken?}`; rakamları `spoken` ile
yazıyla ver: "4" → "four") ve `python scripts/eleven_say.py src/films/<slug>/voice-lines.json` çalıştır → kullanıcının
sesi **"Second Self - Solitude"** (`voice.json`, voice_id `PL7EYPTnZppHWj5yLiVI`, `eleven_v3`, anahtar `ELEVENLABS_API_KEY`)
ile `public/audio/voice/<slug>/v<n>.wav`. Higgsfield TTS veya başka bir ses KULLANILMAZ; ses kullanıcı onayı olmadan
değiştirilmez. Replik, ekrandaki mavi yazının ilk karesinde başlar. (b) Müzik + SFX: `scripts/<slug>-cues.mjs`
(önceki filmin cues dosyasını kopyala: sakin piyano + pad, replik altında −8 dB duck) → Windows: `python
scripts/build-film-audio.py <slug>` + `node scripts/<slug>-audio.mjs …` + ffmpeg loudnorm; Linux/VPS: tek komut
`./scripts/audio.sh <slug>`. Ayrıntı `references/08-audio.md` §0. Stüdyoda yoksa skill'in `scripts/` klasöründen
kopyala: `eleven_say.py`, `voice.json`, `build-film-audio.py`, `audio.sh`, `cues-template.mjs`.

**8. QA (zorunlu).** `scripts/qa.ps1` → tsc + kompozisyonlar + kritik kare still'leri. **Her still'i Read ile
aç** ve 09 §6 kontrol listesine + kanona göre denetle. Hata → düzelt → tekrar still. Sonra `--scale=0.5` taslak;
milestone zamanlarından ffmpeg ile kare çekip zamanlamayı doğrula (02 §4). Sonra final
(`--crf=18`). Raporda neyin doğrulandığını ve neyin doğrulanmadığını dürüstçe söyle.

**9. Teslim.** mp4 yolu + SCREENPLAY.md + YouTube paketi (başlık, 2 alternatif, 3 thumbnail varyantı —
**`other-self-thumbnail` skill'i ile** üretilip QA'dan geçmiş, açıklama gerçek bölüm zaman damgalarıyla, sabit yorum, 3 Shorts önerisi).

## Kalite çıtası (her filmde kendine sor)

- İlk 3 saniyede izleyici "bu benim" diyor mu? 0:15'ten önce başarısızlık damgası var mı?
- Karakter karakter sayfasıyla birebir mi (filiz, oval gözler, kum rengi, mavi gölge ikiz)?
- Her iç ses satırının bir fiziksel karşılığı var mı? Boss satırı en kısa satır mı?
- Bir still'de iki mesaj, kopuk uzuv, kırpılmış parıltı, gövdede dış çizgi, nefes alan kahraman var mı? (olmamalı)
- Sessiz izlendiğinde hikâye anlaşılıyor mu? Slogan tişörte basılabilir mi?
- Rakibin bir cümlesini birebir mi kullandım? (kullanma)

## Dosya haritası

| Dosya | Ne zaman oku |
|---|---|
| `references/03-visual-canon.md` | HER film/sahne öncesi — ölçülmüş görsel kanon (en yüksek otorite) |
| `references/01-story-engine.md` | senaryo: 13 beat, 12 kural, uyarlama motoru, senaryo formatı |
| `references/02-hook-and-retention.md` | hook şablonları, kare kare açılış ölçümleri, milestone'lar, retention killers |
| `references/04-inner-voice.md` | gölge: yapı, yüz, pozlar, durumlar, satır yazımı, konuya göre renk |
| `references/05-character-and-motion.md` | rig, ifadeler, dönüşüm sembolü, aksiyon kataloğu |
| `references/06-sets-and-light.md` | setler, ışık, renk senaryosu, palet token'ları |
| `references/07-text-system.md` | font, metin rolleri, animasyonlar, süreler |
| `references/08-audio.md` | müzik haritası, SFX, frame-grid, Remotion ses API'si |
| `references/09-remotion-build-and-qa.md` | stüdyo kurulumu, yapı, dip overlay, QA döngüsü, Windows notları |
| `references/10-packaging.md` | başlık, thumbnail, açıklama, Shorts, yayın |
| `references/11-topic-bank.md` | 12 konu için hazır başlangıç satırları |
| `templates/screenplay-template.md` | senaryo çıktısı şablonu |
| `scripts/sfxgen.mjs` · `scripts/qa.ps1` | ses üretimi (test edildi) · QA otomasyonu |
| `deep-research/` | uzun kod listeleri ve ham uzman raporları (bkz. `deep-research/README.md` öncelik sırası) |

## Linux VPS (ubuntu@51.222.36.151, ~/the-other-self)

Aynı sistem VPS'te de kurulu: stüdyo `~/the-other-self/studio` (Windows'taki `C:\dev\the-other-self`), proje dosyaları `~/the-other-self/project`. Windows'a özel `npx.cmd`/`.ps1` yerine `npx` ve `studio/scripts/*.sh` (`render-youtube.sh <slug>`, `stills.sh`, `audio.sh <slug>`) kullanılır. Ayrıntılar: `~/the-other-self/CLAUDE.md`.

