# 05 — Altyazı, seslendirme ve ses miksi

Kaynak `deep-research/D` (40 video ölçüldü). Bu katman **hijyen**: hit ile flop'ta aynı. Şablonu birebir uygula.

## 1. Altyazı spec'i (1080×1920, `captions.py` üretir)
| Parametre | Değer |
|---|---|
| Font | **Montserrat ExtraBold** (OFL). Bulunamazsa Arial Black (`C:/Windows/Fonts/ariblk.ttf`). Fontu `fonts/` klasörüne koy. |
| Boyut | 80 px; kart 12 karakteri geçerse 72 px. Maks. genişlik 950 px. |
| Harf durumu | Konuşulduğu gibi. UPPERCASE yalnızca A/B varyantında. |
| Renk | Beyaz #FFFFFF, siyah 3 px kontur, sert siyah gölge (+4, +6). |
| **Konum** | Merkez **y = 1060** (izinli bant 900–1150). Ricks'in y≈1352'si IG'de arayüzün altında kalıyor. Yasak alanlar: üst 270 px, alt 672 px, yanlarda 65 px. |
| Kart | En fazla 2 kelime / 14 karakter. İşlev kelimeleri (a, the, to, of, in, his…) sonraki kelimeye bağlanır. Noktalama kartı bitirir. Hedef 1,25–1,35 kelime/kart, medyan 0,30 sn. |
| Senkron | Kart, kelimeden **33 ms önce** gelir. Kartlar arası boşluk yok. Son kart 0,4 sn kalır. |
| Vurgu | Opsiyonel: sayı, para ya da twist kelimesi sarı #FFD60A. 10 kartta en fazla 1, ilk 3 sn'de en fazla 1. Emoji yok. |
| Hook bandı (IG testi) | İlk 0–2 sn, üstten ≥300 px'te 2–4 kelimelik kapak metni. Trial Reel'de bantlı/bantsız A/B testi. |

## 2. Seslendirme
**Persona:** Arkadaşına inanılmaz bir şey anlatan enerjik Amerikalı erkek hikâyeci. Hafif eğlenmiş, üst-orta register (~190–210 Hz), canlı tonlama (~14 yarım ton). Ricks'in sesini **taklit etme**; aynı enerji bandında özgün bir ElevenLabs sesi seç (ses seçimi kullanıcının kararı).

| Ayar | Değer |
|---|---|
| Model | `eleven_multilingual_v2` (tutarlı). Daha ekspresif sonuç için `eleven_v3`. |
| stability / similarity / style | 0,40 / 0,85 / 0,45 (karakter replikleri için style 0,7) |
| speed | 1,10–1,15 |
| Endpoint | `/v1/text-to-speech/{voice}/with-timestamps` (kelime zamanları buradan altyazıya gider) |
| Hedef | 205–220 wpm. VO 0,00 sn'de başlar, sonda ≤0,6 sn boşluk kalır. |
| Duraklamalar | 60 sn'de 6–10 adet, her biri 0,35–0,8 sn (`pause_after`). Konumları: hook'tan sonra, "You see/But/So" öncesi, twist öncesi (en uzun), replik etrafı, son punchline öncesi. Diğer cümle araları ≤250 ms. |

Config: `voice-narrator.json` (skill kökünde). `voice_id` alanı kullanıcı seçene kadar `CHOOSE_ME` kalır. Aday listesi için `tts.py --list-voices "energetic american male storyteller"`. **`inner-voice-film/voice.json`'a dokunma**; o başka bir kanalın kilitli sesi.

## 3. Müzik ve SFX
| Katman | Kural | Seviye |
|---|---|---|
| Müzik yatağı | Tek parça, merak/quirky tonda (pizzicato, marimba, yumuşak pad), perküsyon yok ya da çok hafif. **Kesintisiz, hiç sessizlik yok.** Kendi üretimimiz ya da telifsiz lisanslı. | VO'nun ~10 dB altı (−24…−26 LUFS), VO varken sidechain ducking |
| Whoosh | Geçişlerin ≥%60'ında | peak −10 dBFS |
| Pop/tık | Vurgu kartı ya da obje belirmesi (en fazla 1 / 3 sn) | −14 dBFS |
| Impact | Twist ve damga anı | −8 dBFS |
| **Duraklama dolgusu** | Her >0,4 sn VO duraklaması SFX ya da müzik şişmesiyle dolar. Ses tarafında hit ile flop'u ayıran tek sinyal bu. | |
| Damga | Kapanışta lastik damga "thunk" sesi (marka sesi) | −8 dBFS |
| Master | **−14 LUFS integrated, ≤ −1 dBTP**, LRA 2–4, 48 kHz, AAC 320k. Mix neredeyse mono. | |

`assemble.py` whoosh, pop ve damga seslerini ffmpeg ile prosedürel üretir. `music/` klasöründe parça varsa onu kullanır, yoksa düşük seviyeli prosedürel pad üretir (yer tutucu; final için gerçek bir yatak önerilir). Yedek SFX kaynağı: `inner-voice-film/scripts/sfxgen.mjs` (whoosh_cut, punch).

## 4. QA (`qa.py`)
- −35 dB altında ≥0,25 sn sessizlik **0** olmalı.
- I = −14 ±0,5, TP ≤ −1.
- VO başlangıcı ≤0,05 sn.
- Altyazı bandı kontak sayfasından görsel olarak kontrol edilir.
