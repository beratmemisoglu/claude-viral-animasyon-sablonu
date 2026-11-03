# 06 — İzleyici psikolojisi, risk ve Türkiye pazarı

Kaynak: `deep-research/D-audience-tr-market.md` (1.308 kök yorum, NexLev RPM ve rakip taraması, 40 premise). Ara veri: scratchpad `whatif/d_agent/`.

## 1. Neden izleniyor (yorum kanıtı)

| Ölçüm | Hit | Flop |
|---|---|---|
| "Ben olsam…" (self-insert) | %16,9 | %5,0 |
| Kural/boşluk tartışması (beğeni ağırlıklı) | **%30,6** | %0 |
| "Devam et / yeni video" nezaket yorumu | düşük | %19,5 |

- Hit video bir **tartışma motoru**dur. İzleyici kuralı bükmeye çalışır (salyangozu izle, karşı kıtaya kaç, sıkılınca dokun).
- En çok tartışma, kuralı somut ve zaman ufku açık premise'te: Immortal Snail 2,11 yorum/1K, Immortal 0,92, niş medyanı 0,30.
- "Gör" ailesi (yalan, nefret, servet) en yüksek beğeni oranını alıyor (7,3–7,6/1K) ve ahlaki ikilem yorumları üretiyor.
- Flop'ların beğeni oranı bazen daha yüksek (Days Left 14,1/1K): izleyen memnun, ama az kişi tıklamış. Sorun **paketleme**.
- Animasyon hataları hit'te bile en çok beğenilen yorum oluyor ("geri geri yürüyor" 390 beğeni). QA'da yürüme yönü, çarpışma ve süreklilik kontrol edilmeli.
- Kanal sahibinin sabitlenmiş sorusu yorumu ~8 kat artırıyor (Iflord: 51 beğeni, 40 cevap).

## 2. Mekanizma → kural

| Mekanizma | Kanıt | Kural |
|---|---|---|
| Kural somutluğu | Snail 2,11 yorum/1K | Premise'te 1 sayı + 1 yasak |
| Sosyal asimetri | Gör ailesi 7,3–7,6 beğeni/1K | Güç başkası hakkında bilgi versin |
| Lanet dönüşü | Hit'lerin son üçte biri | Sürenin %60–70'inde güç en yakın kişiye döner |
| Hamle | Days Left flop | Sayaç izleyiciye strateji bıraksın |
| Self-insert | Immortal %24 | 2. tekil anlatım + açık uçlu bitiş sorusu + sabitlenmiş yorum |

## 3. Risk ve korkuluklar (yayından önce zorunlu)

1. **Özgün karakter seti** ve isim; başka kanalın karakteri, rengi, logosu yok.
2. **Reused / "AI slop" riski:** 7+ kanal aynı şablonu kullanıyor ve hit videolarda kopyala-yapıştır "AI SLOP" yorumları başladı. Her videoda ≥2 özgün sahne, aynı premise 30 gün içinde tekrar yok, ses insan düzeltmeli.
3. **Made-for-kids yanlış sınıflandırma:** stick figure + "science for kids" etiketi riskli. "Çocuklar için değil" elle işaretle; anahtar kelimede "çocuk/kids" yok; yetişkin bağlam.
4. Gore, kan, cinsel ima, intihar çağrışımı yok. Yas premise'lerinde uyarı ve yumuşak ton.
5. Gerçek marka, dizi, ünlü yok. Meme kavramları yerelleştirilmiş isimle.
6. **TR'ye özel:** din, siyaset, etnik köken ve askerlik **alay konusu olmaz**; kumar yok. Askerlik ya da deprem gibi konular yalnız saygılı bağlam olarak kullanılabilir.
7. Açıklamada ≥3 kaynak (bilim içeriyorsa) + "kurgudur" notu + bölüm listesi.
8. Ses/görsel lisans listesi proje klasöründe.
9. Sabitlenmiş yorum sorusu her videoda.
10. Ayrıca A ajanı: cinsel sayı (partner sayısı) reklam/öneri riskli, kullanılmaz.

## 4. Türkiye pazarı

### RPM
| Veri | RPM $ |
|---|---|
| 5 hedef EN kanal (medyan) | 3,59 (2,10–4,51) |
| Future Wealth (finans premise) | 6,30 |
| Immortal Snail | 1,93 |
| Tarih SEN (TR, 2. tekil hipotetik animasyon) | 1,40 |
| TR animasyon kohortu medyanı (6 kanal) | 1,58 |

TR'de fiyat EN'nin yaklaşık %44'ü, ama ortalama izlenme yaklaşık 4 kat (TR animasyon kohortu 300K–1,4M).

### Rakip boşluğu
- "ya olsaydı", "ya herkes", "görebilseydin", "olsa ne olur" tam eşleşme aramaları, son 180 gün, ≥20K: **sıfır sonuç**. Süper güç ve sosyal asimetri ailesi Türkçe'de boş.
- Format TR'de kanıtlı: **Tarih SEN** 13 Ekim 2026'da açıldı, 19 video, "Eğer 1965'te Görücü Usulü Evlenseydin?" **523K**. "Kızlar Askerde Olsaydı? | Türkçe Animasyon" 251K.

### Karar (D ajanı Go/No-Go)
| Seçenek | Karar |
|---|---|
| Türkçe ana kanal (sosyal sayı + DUAL + oyun) | **GO, şartlı**: 30 günde ≥3 video >100K ve yorum/1K ≥0,4 |
| Yalnız İngilizce kanal | **Tek başına NO-GO**: niş Ekim 2026'da doyuyor |
| Türkçe ana + İngilizce ses parçası (multi-audio) | **GO, önerilen**: aynı animasyon, EN tarafında 2,5–3,5× RPM |
| Nostalji kolu ("Eğer 19XX'te…") | Ayda 1 bölüm, ayrı kanal değil |

İlk 10 video karışımı: 6 "gör" ailesi, 2 lanet, 2 nostalji-sosyal. 30 gün eşiği tutmazsa **premise ailesini** değiştir, formatı değil.

### Kitle ve dil
- Ana kanal 18–30 yaş: kira, maaş, YKS, apartman, iş görüşmesi.
- Ses: Türkçe TTS aksanı hemen fark edilir. Yüksek kalite ses + insan redaksiyonu şart; EN dublajda AI ses kabul görüyor.
- TR yorum motoru **itiraz** üzerinden çalışıyor: senaryoya kaynaklı ama tartışılabilir bir detay koy.
- TL rakamları 6 ayda eskir: açıklamaya "Ekim 2026 fiyatlarıyla" yaz.
- 100K izlenme ≈ 120–180 $ (TR). İlk 3 ay kitle inşası olarak planla.
