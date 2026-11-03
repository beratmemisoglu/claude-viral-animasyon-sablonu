# 07 — SCRIPT FORMAT, SELF-CRITIQUE → REWRITE → FINAL AUDIT

## 1. Beat sheet formatı (`02-beatsheet.md`)
```markdown
# BEAT SHEET — <başlık>
Mimari: A3 · Hedef süre: 17 dk (~2.500 kelime @150 wpm) · Hook: H1 · Kapanış: sentez + anti-hype
Merkezi soru: …
İzleyicinin ilk varsayımı: … → kırılması: …

## Vaat sözleşmesi
| Vaat | Ödeme yeri |

## Ünite seçimi (Decision Engine)
| # | Ünite | Seçildi çünkü | Dışarıda bırakılan | Somut çapa (Fact ID / [VERIFY]) | Analoji | Transfer | Eylem | Stinger taslağı |

## Retention haritası
| # | Zaman | % | Bölüm | İşlev | Teknik (R#) | İzleyici ne biliyor | YENİ SORU | Açık döngüler |

## Döngü kayıt defteri
| L# | Açılış | Soru | Ödeme | Tip | Durum |

## Duygu eğrisi
0% … → 35% (dip) … → 100% …
```

## 2. Script formatı (`03-script-final.md`)
```markdown
# <BAŞLIK>
Süre hedefi: ~X dk · Kelime: ~Y

[HOOK]
[VISUAL: chalkboard; white doodle of … ]
Seslendirme metni…

[UNIT 1 — (alt başlık)]
[VISUAL: …]
…
[ON-SCREEN TEXT: "People respond to rewards, not intentions."]   ← (örnek işlev; özgün yaz)
…

[CLOSE]
…

---
## [VERIFY] listesi
| # | Satır | İddia | Durum (Dossier F-ID / doğrulanmadı) |
## Kişisel anekdotlar (kanona eklenecek)
| # | Tip (P1–P8) | Özet | Eklenen kanon gerçeği |
```
Görsel notları kısa: whiteboard/doodle sahnesi, ekranda vurgulanacak kelime/rakam, harita/grafik, karakter çizimi. "Merak edilen nesneyi hemen gösterme" kuralı: tahmin oyununda cevap görseli cevaptan sonra.

## 3. SELF-CRITIQUE → REWRITE → FINAL AUDIT döngüsü

### AUDIT 1 — OPENING
- İlk cümle devam etmek için anlamlı bir neden yaratıyor mu?
- Merkezi merak net mi?
- Gereksiz kurulum var mı (kanal adı, "today", selam)?
- Vaat spesifik mi? Aşırı vaat var mı (başlıkla karşılaştır)?
- Anlatı en çarpıcı noktadan mı başlıyor?
- İlk somut kanıt ≤ 40 sn mi?
- 5 katman: hangileri var? Uzun menzilli döngü var mı?

### AUDIT 2 — RETENTION (bölüm bölüm oku)
Tespit et ve her biri için *problem + somut düzeltme* yaz:
- İlginin düşebileceği bölümler (YENİ SORU sütunu boş/zayıf)
- Tekrarlanan bilgi
- Çok uzun açıklamalar (>45 sn yeni çapa olmadan)
- Zayıf geçişler
- Unutulan açık döngüler
- Çok geç / çok erken gelen ödemeler (hook vaatlerinin hepsi %55'ten önce bitiyor mu? → biri ertelensin)
- Yapay gerilim ("you won't believe…" tipi, karşılıksız)
- Eksik bağlam (isim/kavram hatırlatması)
- İkinci yarı hikâye bütçesi (%40) sağlandı mı?

### AUDIT 3 — NATURALNESS
Robotik · jenerik · fazla cilalı · tekrarlı · yapay dramatik · standart AI şablonu gibi duyulan pasajları bul ve doğal konuşma diline çevir. Kontrol listesi: `05-voice-and-style.md` §10 ASLA listesi; ifade rotasyonu; fragman oranı; cümle ortalaması; "Imagine" sayısı; mutlak kelimeler.

### AUDIT 4 — DNA ALIGNMENT
Core DNA (C1–C12) ve seçilen mimari şablonuna karşı puanla:
| Kural | Uygulandı mı | Kanıt (satır) | Eksikse düzeltme |
Kaynak kanalın birebir ifadeleri kullanılmış mı? → varsa yeniden yaz.

### AUDIT 5 — FACT & SAFETY (bu sürümün eklemesi)
- Her rakam/vaka/deney/alıntı: Dossier F-ID veya [VERIFY].
- Tartışmalı iddialarda ihtiyat dili.
- Finans/sağlık: genel bilgi tonu; kişiye özel yatırım tavsiyesi yok.
- Cinsiyet/yaş varsayımlı transfer sahneleri nötrleştirildi mi?
- Kişisel anekdotlar kanonla tutarlı mı; gerçek kişi/şirket adı, ünlü, büyük servet ya da mucize sonuç içermiyor mu; kaynak kanalın anekdotlarını kopyalamıyor mu?
- Anekdot sayısı ve sırası `09` §4 ve §7'ye uygun mu (ilk anekdot kusur, son anekdot küçük zafer)?

### FINAL TASK
Audit bulgularıyla **tam scripti yeniden yaz**. Olgusal doğruluğu, mantık sürekliliğini ve kaynağın gerçek anlamını koru. Çıktı: iyileştirilmiş script + kısa audit raporu (`04-audit.md`).

## 4. FINAL QC CHECKLIST (hepsi ✓ olmadan teslim yok)
**Açılış**
- [ ] İlk 5 sn'de selam/kanal adı/abone isteği yok
- [ ] Otorite/emek kredisi veya ayna sahnesi ilk ~25 sn'de
- [ ] İlk somut içerik ≤ 40 sn
- [ ] En az 1 uzun menzilli açık döngü, %55'ten sonra ödeniyor
**Yapı**
- [ ] Seçilen mimarinin (A1–A9) adımları mevcut
- [ ] Her ünite somut çapa ile açılıyor
- [ ] Her ünitede tek kırılma işareti (varyantlı)
- [ ] Her ünite eylem / söylenecek cümle / teşhis sorusuyla bitiyor
- [ ] Her ünitenin stinger'ı var (4–10 kelime antitez)
- [ ] Hook'taki her örnek/karakter geri çağrılıyor (callback)
- [ ] Retention haritasında her satırın YENİ SORU'su dolu
- [ ] Döngü kayıt defterinde açık kalan döngü yok
- [ ] İkinci yarı ≥ %40 hikâye/vaka içeriyor; son üniteler kısalmıyor
**Dil**
- [ ] Ort. cümle 8–10 kelime, %15–25 fragman
- [ ] "you" yoğun; izleyici sahnede
- [ ] Jargon ≤ 2 ve anında somutlaştırılmış
- [ ] Analojiler çizilebilir ve mekanizma testi geçti
- [ ] Aynı kalıp ifade ≤ 2 kez; yasaklı AI klişeleri yok
- [ ] Kaynak kanalın imza cümleleri birebir yok
**Kapanış**
- [ ] Başlık vaadinin her parçası ödendi (vaat sözleşmesi ✓)
- [ ] Sentez/recap/bookend/kişisel matematikten biri
- [ ] ≤ 1 CTA, outro ≤ 40 sn
**Doğruluk**
- [ ] [VERIFY] listesi çıkarıldı; doğrulanmamış rakam hook'ta yok
- [ ] Apokrif anekdotlar ihtiyat diliyle
- [ ] Kişisel anekdotlar kanonla tutarlı ve `persona/ANLATICI-CANON.md` anekdot kaydı güncellendi

## 5. Değişken tablosu (final audit'in sonuna, kaynak videolarla karşılaştırma için)
| Değişken | Bu script | En yakın kaynak video değeri |
|---|---|---|
| Hook type | | |
| Hook duration | | |
| Central question | | |
| Open loops (sayı, uzun menzilli) | | |
| Payoff timing | | |
| Narrative escalation | | |
| Information density (wpm, ünite süresi) | | |
| Sentence rhythm (ort., fragman %) | | |
| Emotional shifts | | |
| Transition type | | |
| Ending structure | | |
Kaynak değerler: `08-evidence-index.md`.

## 6. AUDIT modu (kullanıcının hazır scripti)
Aynı 5 audit + DNA uyum skoru (Core DNA maddeleri / 12) + QC checklist + yeniden yazılmış script. Değişiklikleri gerekçeleriyle listele.
