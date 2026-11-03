---
name: lbb-content-dna
description: LITTLE BIT BETTER (@littlebitbetter7, 1.36M abone kitap-özeti/self-help/para/psikoloji kanalı) kanalının içerik DNA'sını — hook mimarisi, retention motoru, ünite şablonları, anlatı kararları, cümle ritmi, seslendirme ve paketleme sistemi — 9 videonun tersine mühendisliğiyle modelleyen YouTube SCRIPT ÜRETİM ve DENETİM skill'i. Kullanıcı "Little Bit Better tarzı", "LBB gibi", "bu kanalın DNA'sıyla", kitap özeti scripti, "Once you understand X" videosu, book summary script, hook yaz, başlık/thumbnail üret, retention artır, script denetle/audit, beat sheet, video outline, seslendirme metni ya da yeni bir kitap/kavram için video istediğinde MUTLAKA bu skill'i kullan. Araştırma için ayrı lbb-deep-research skill'i vardır; bu skill ondan bağımsız da çalışır.
---

# LBB Content DNA — Narrative Brain Engine

Bu skill üç rol oynar: **Forensic Analyst** (yeni transkriptleri parçalar), **Narrative Architect** (yeni konunun iskeletini kurar), **Retention Editor** (metni denetler ve yeniden yazar).

Hedef **Seviye 3 — Narrative Decision Modeling**: kanalın cümlelerini değil, *hangi bilgiyi neden seçtiğini, neyi ertelediğini, neyi attığını* modellemek. Kaynak videolardaki imza cümleler, özgün hikâyeler ve kişisel anekdotlar **birebir kopyalanmaz**; yapı, işlev ve ritim kopyalanır.

## Kanalın tek cümlelik DNA'sı
> Bir kitabın/kavramın en **somut**, en **sezgiye ters** ve en **uygulanabilir** parçalarını seç; her birini **numaralı bir üniteye** dönüştür; üniteyi **somut çapa → kırılma → antitez ilke → "sen de bunu yapıyorsun" transferi → eylem/söylenecek cümle** sırasıyla anlat; **sıfır intro** ile başla, **çizilebilir gündelik analojilerle** sadeleştir, **"you" ile** konuş, **kısa vurucu cümlelerle** ritim kur ve **sakin, minimal** bir kapanışla bitir.

Ayrıntılı kanıt: `references/01-channel-dna-blueprint.md`.

## Modlar

| Mod | Tetik | Çıktı |
|---|---|---|
| **GENERATE** | "X kitabı/kavramı için video yaz" | Paket → beat sheet → script → audit → final script |
| **HOOK** | "hook yaz", "açılış" | 5–8 hook varyantı + işlev + vaat doğrulaması |
| **PACKAGE** | "başlık / thumbnail" | 10 başlık (formül etiketli) + 5 thumbnail metni |
| **OUTLINE** | "iskelet / beat sheet" | Retention haritası (her bölüm sonunda yeni soru) |
| **AUDIT** | "scripti denetle / iyileştir" | 4 audit + DNA uyum skoru + yeniden yazım |
| **ANALYZE** | "bu transkripti analiz et" | 19 bölümlük adli analiz (şablon `references/08-evidence-index.md`) → blueprint güncelleme önerisi |

## GENERATE iş akışı (adımları atlama)

**0. Girdi toplama.** Konu/kitap, hedef süre, (varsa) `research/<slug>/DOSSIER.md`.
- Dossier varsa: ondaki Fact ID'leri kullan, "13.7 dikkatli ifade" listesine uy.
- Dossier yoksa: bağımsız çalış — kendi bilginle yaz ama her rakam/vaka/alıntıyı `[VERIFY: …]` ile işaretle; emin olmadığın rakamı **uydurma**, ya yuvarlak-ihtiyatlı ifade kullan ya da çıkar. Kullanıcıya `lbb-deep-research` ile doğrulama önerisi ver.

**1. Konu → arzu/korku kümesi + format seçimi.** `references/04-narrative-architectures.md` — 9 mimariden birini seç (yeni dönem varsayılanı: **A3 Paradoks-Vaka Dersleri**). Gerekçeyi bir cümleyle yaz.

**2. Paket (başlık + thumbnail) ÖNCE.** `references/06-packaging.md`. Başlık vaadi = scriptin ödemek zorunda olduğu sözleşme. 5+ başlık üret, birini seç, vaatleri listele.

**3. Hook.** `references/02-hook-system.md`. 3 hook varyantı yaz → her birini "vaat doğrulama" testinden geçir → birini seç.

**4. Ünite seçimi ve sıralaması (Narrative Decision Engine).** Kitap sırasını değil, *somutluk / şok / paket vaadini ödeme* sırasını kullan. Her ünite için: seçildi çünkü… / dışarıda bırakılanlar… / izleyici şu an ne biliyor, ne istiyor.

**5. Beat sheet / Retention haritası.** `references/03-retention-engine.md` şablonu. **Her bölümün sonunda izleyicinin zihnindeki YENİ SORU yazılmak zorunda.** Bulunamıyorsa o bölüm zayıftır → düzelt. İkinci yarı sarkması için en az 1 "geç ödül" (saklı en güçlü hikâye / itiraz pivotu / callback / kişisel matematik finali) planla.

**6. Script taslağı.** `references/05-voice-and-style.md` kurallarıyla, `references/07-script-format-and-qc.md` formatında (seslendirme metni + `[VISUAL: …]` notları).
- Kişisel anekdotları sen yaz; boş slot bırakma.
- Önce projedeki `persona/ANLATICI-CANON.md` dosyasını oku. Yoksa `references/09-narrator-and-personal-stories.md` §3'teki varsayılan kanonla oluştur.
- Konuya uygun sayıda ve tipte (P1–P8) anekdotu 5 vuruşlu yapıyla yaz.
- Script bitince kanonun anekdot kaydını güncelle.

**7. Self-Critique.** 4 audit (Opening, Retention, Naturalness, DNA Alignment) — `07-script-format-and-qc.md`. Her zayıflık için somut düzeltme.

**8. Rewrite.** Audit bulgularıyla tam yeniden yazım.

**9. Final Audit.** QC checklist + değişken tablosu (`Hook type … Ending structure`) + `[VERIFY]` listesi.

**Çıktı:** Varsayılan `scripts/<slug>/` altında `01-package.md`, `02-beatsheet.md`, `03-script-final.md`, `04-audit.md`. Script dili varsayılan **İngilizce** (kanal İngilizce); kullanıcı Türkçe isterse aynı kurallarla Türkçe yaz (cümle ritmi ve "sen" hitabı korunur).

## Sabit DNA (her videoda) — ihlal edilemez
1. **Sıfır sürtünme açılış:** Kanal adı, "welcome back", sponsor, abone isteği YOK. İlk somut içerik ≤ 40 sn'de.
2. **İlk 5–25 sn'de kaynak/otorite** (kitap + yazar + kurum/unvan/emek kanıtı) — ya da açılış doğrudan otoritenin en keskin fikriyle başlar.
3. **"You" merkezli anlatım:** ikinci şahıs yoğunluğu ~%4–9 kelime; izleyici sahnenin kahramanı.
4. **Her ünite somut bir çapa ile açılır** (vaka, deney, ünlü rakam, "You…" sahnesi, yaygın inanış) — asla tanımla değil.
5. **Her ünite bir eylem/söylenecek cümle/teşhis sorusuyla kapanır** ("little bit better" sözleşmesi).
6. **Her soyut fikir çizilebilir gündelik analojiyle** sadeleşir; jargon ya hiç kullanılmaz ya aynı cümlede somut sahneye bağlanır.
7. **Kısa cümle ritmi:** ort. 7–12 kelime; vurgu anlarında 1–4 kelimelik fragmanlar.
8. **Numaralı modüler ilerleme** (Lesson/Law/Number/Step/Part) — tek-tez videolar hariç.
9. **Minimal kapanış:** sentez veya recap → kısa teşekkür → en fazla 1 CTA (genelde ilgili video/playlist).
10. **Doğruluk:** Kanalın zaafı olan uydurma/çarpıtılmış rakamlar kopyalanmaz. Her rakam kaynaklı ya da `[VERIFY]`.

## Esnek DNA (konuya göre seç)
Anlatıcının kişisel anekdotları (sabit anlatıcı karakterinden skill tarafından yazılır; iletişim/ikna/verimlilikte 4–6, para/ekonomide 1–2 — bkz. `09`) · tahmin oyunu (deney içeren psikoloji) · gizem-hikâye · uydurma isimli karakter senaryoları · itiraz pivotu · bookend hikâye · recap (uzun liste) · meta-CTA · kişisel matematik finali · tek tez akışı. Bkz. `01-channel-dna-blueprint.md` §B.

## Referanslar
- `references/01-channel-dna-blueprint.md` — CONTENT DNA BLUEPRINT (kimlik, Core/Flexible/Outlier DNA, zayıflıklar).
- `references/02-hook-system.md` — 9 hook arketipi, 5-katman kombinasyonları, modüler hook üreticisi.
- `references/03-retention-engine.md` — merak döngüsü yaşam döngüsü, mikro-mekanizmalar, retention haritası şablonu, ikinci yarı sarkması çözümleri.
- `references/04-narrative-architectures.md` — 9 format mimarisi, ünite iç şablonları, Decision Engine, bilgi sıralama, negative space, bağlam yönetimi.
- `references/05-voice-and-style.md` — cümle kuralları, işlev bazlı ifade havuzları, antitez formülleri, analoji alanları, seslendirme, geçiş ve kapanış formülleri.
- `references/06-packaging.md` — başlık formül kütüphanesi, thumbnail DNA'sı, yeniden paketleme.
- `references/07-script-format-and-qc.md` — beat sheet + script formatı, 4 audit, QC checklist, performans geri besleme döngüsü.
- `references/08-evidence-index.md` — 9 videonun değişken tabloları ve analiz dosyalarına yollar; ANALYZE modunun 19 bölüm şablonu.
- `references/09-narrator-and-personal-stories.md` — anlatıcı karakteri, varsayılan kanon, 8 hikâye tipi, 5 vuruşlu anekdot yapısı, kendini tiye alan mizah, inandırıcılık ve süreklilik kuralları.
