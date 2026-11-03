# Ses Tasarımı (ElevenLabs Voice Design)

Referans videonun anlatıcısı ölçümle: mono, ~151 kel/dk, sakin, kanıta dayalı, İngiliz İngilizcesi metin; vurgu sesle değil duraklarla yapılıyor. Kanal sesi bu ilkeleri alır ama **belirli bir gerçek kişiyi taklit etmez** (isim, ünlü, "sounds like X" yazma).

## Ana ses: "Small Cause Narrator"
**Voice description** (ElevenLabs → Voices → Voice Design → "Describe your voice"; İngilizce yapıştır):
```
A calm, warm male narrator in his late thirties with a clear, neutral British accent. Friendly science explainer tone: curious, gently amused, never dramatic or salesy. Medium-low pitch, smooth and slightly breathy, close-mic studio recording with no reverb and no background noise. Speaks at an unhurried, even pace with natural pauses between sentences, like explaining something fascinating to a smart friend across a table. Clear consonants, relaxed delivery, short sentences land softly with a hint of dry humour.
```

**Preview text** (100–1000 karakter; senaryonun hook'u — tonlamanın en zor olduğu yer):
```
A hot afternoon. The lights go out. Not just yours. The street. Then the city. Then eight states and part of Canada. No storm. No attack. No explosion. So what switched off fifty million people? A few overgrown trees. And the blackout was never in one place. It travelled across the map, line by line, faster than anyone could stop it.
```

## Alternatifler (A/B için)
- **B — Kadın, sıcak:** `A warm, calm female narrator in her early thirties with a soft, neutral British accent. Clear and friendly science explainer, quietly curious with a light dry wit, never dramatic. Medium pitch, smooth, close-mic studio quality, no reverb. Unhurried, even pace with natural pauses, like telling a fascinating story to a friend.`
- **C — Erkek, Amerikan (ABD kitlesi):** `A relaxed, warm male narrator in his thirties with a neutral General American accent. Thoughtful science explainer, calm and curious, a little playful, never hype. Medium-low pitch, smooth and clear, close-mic studio recording, no reverb or room sound. Steady, unhurried pacing with natural pauses between ideas.`

Seçim kuralı: 3–4 varyasyon üret, hook'u dinle; "So what switched off fifty million people?" sorusunda yükselen ama abartısız, "A few overgrown trees." cevabında düşen-kısa tonlama vereni seç. Dramatik/fragman sesi veren varyasyonu ele.

## Üretim ayarları (TTS)
| Ayar | Değer | Neden |
|---|---|---|
| Model | Eleven Multilingual v2 (tutarlılık) · v3 (duygu etiketleri gerekiyorsa) | Uzun anlatımda v2 daha stabil |
| Stability | 0,55–0,65 | Sakin, bölümler arası tutarlı |
| Similarity | 0,75 | Ses kimliği korunur |
| Style exaggeration | 0–0,15 | Abartı formatın güvenini bozar |
| Speaker boost | Açık | Netlik |
| Speed | 0,95–1,0 | Hedef 145–155 kel/dk |

## Metin hazırlama kuralları
- VO'yu **bölüm bölüm** üret (V1, V2…), tek seferde değil; her bölüm ayrı dosya → kurguda blackout blink / dip geçişi araya rahat girer, düzeltme ucuz olur.
- Duraklar: cümle sonu nokta yeter; bölüm içi daha uzun durak için yeni paragraf. v2'de `<break time="0.6s" />` kullanılabilir; aşırı kullanma.
- Sayılar kelimeyle yazılı kalsın ("two thousand and three", "forty percent") — model rakamları yanlış okuyabilir.
- Kısaltmaları açık yaz: "N minus one", "megawatts", "hertz".
- v3 kullanılırsa yalnız hafif etiketler: `[curious]` hook sorusunda, `[softly]` kapanış cümlesinde. Her bölümde en fazla bir etiket.

## Kontrol
- Ölçülen hızı `pace_check.py`'deki tahminle karşılaştır; farklıysa `time_beats.py --wpm <gerçek>` ile yeniden zamanla.
- Tüm bölümlerde loudness −16 LUFS (son mix); bölümler arası ton farkı duyuluyorsa o bölümü aynı seed/ayarla yeniden üret.
