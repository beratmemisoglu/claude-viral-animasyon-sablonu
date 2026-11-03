# Kalite kontrol (yayından önce)

`scripts/qc.py` senaryoyu (`## 4.` bölümü) okur, kelime sayısından zaman tahmin eder (varsayılan 170 kel/dk) ve aşağıdaki ölçütleri basar. ✔ geçti, ✖ kaldı, ⚠ uyarı (yayın engeli değil ama bak). Sezgisel ölçümler (hitap, salınım) işaretlidir; ✖ çıkarsa metni oku, sayıya körü körüne uyma.

| # | Kontrol | Geçme ölçütü | Nasıl ölçülür |
|---|---|---|---|
| 1 | Açılış | İlk VO satırı `[KAPI]`, "ilk şey/ilk yaptığı" içerir; selam/"bu videoda"/soru yok | regex |
| 2 | İlk rakam | ≤7 sn | ilk rakamlı kelimenin zamanı |
| 3 | İlk vaftiz | ≤15 sn | ilk `[İSİM]` satırı ya da "deniyor/diyor/denen/diyelim" |
| 4 | Kavram yoğunluğu | ≥4/dk (180 sn'de ≥12) | `Kavramlar:` listesinden VO'da geçenler (ekli halleri dahil) |
| 5 | Aşama sayısı | 180 sn'de 4–7 `[KAPI]` | etiket sayımı (süreye ölçekli) |
| 6 | Ceza → taktik | her `[TEŞHİS]`/`[İSİM]` sonrası ≤8 sn içinde `[TAKTİK]`/`[ÇERÇEVE]`/`[UYARI]` | zaman farkı |
| 7 | Gizli sayaç | `Gizli sayaç:` adı VO'da ≥4 kez (1 tanım + ≥3 geri çağırma) | sayım |
| 8 | Aksiyom | ≥1 `[AKSİYOM]` + ≥1 "başkasını / tercih eder / yerine" hatırlatması | regex |
| 9 | Rakam cetveli | ≥6 farklı rakam | rakam sayımı |
| 10 | Teşhis listesi | ≥1 "şunlardan biri" + altında EKRAN | regex |
| 11 | Yeniden çerçeve | 1 `[ÇERÇEVE]`, %30–50 arasında başlar | zaman |
| 12 | Düz bölüm (salınım vekili) | dönüş işaretleri ("ama/fakat/ancak/eğer/-sa" ya da TEŞHİS/UYARI/ÇERÇEVE etiketi) arası en uzun boşluk ≤15 sn — sezgisel | zaman |
| 13 | "Ama" dönüşleri | ≥2,5/dk | sayım |
| 14 | Hitap ve soru | 2. tekil biçim ≥4/100 kelime (sezgisel); soru işareti ≤2 | regex |
| 15 | Dolgu | "yani, işte, falan, şey, hani, açıkçası, bu videoda, arkadaşlar" + çerçeve dışı "aslında" ≤1/100 | sayım |
| 16 | 1. şahıs | KÖPRÜ/CTA öncesi "ben/benim/bence/hazırladım" yok (⚠) | regex |
| 17 | Doruk sonrası uyarı | %70'ten sonra ≥1 `[UYARI]` | zaman |
| 18 | CTA | yasak ifade yok (abone ol, beğen, like, bildirim, zile bas); KÖPRÜ+CTA payı ≤%12 | regex + zaman |
| 19 | Süre | tahmini süre `Hedef süre:` ±%8 (gerçek ses sonrası ±%3) | kelime/hız |
| 20 | Deiktik → EKRAN | "şunlardan biri / bu grafik / buraya / böyle / bunlar" geçen her satırın altında EKRAN | satır kontrolü |
| 21 | Kaynak | `[KAYNAK GEREKLİ]` sayısı; >0 → "YAYINA HAZIR DEĞİL" (⚠) | sayım |

Kullanım:
```
python qc.py paket.md                     # rapor
python qc.py paket.md --wpm 182           # gerçek ses hızıyla
python qc.py paket.md --vo script.txt --timed script_timed.txt   # ElevenLabs metni + zamanlı satırlar
python qc.py paket.md --json              # makine okunur
```

Elle bakılacaklar (script ölçemez):
- Aşamalar gerçekten kronolojik mi, sistemin **uyguladığı** sırada mı?
- Her etiket mekanizmadan sonra mı geliyor; "İnsanlar buna … diyor" doğru mu?
- Rakam cetveli küçükten büyüğe mi; her rakamın kaynağı listede mi?
- Taktikler birbirini yalanlıyor mu?
- Başlık/bölüm/etiketlerdeki her kavram senaryoda var mı?
- Türkçe doğal mı (çeviri kokusu, uzun tamlama)? Sesli oku.
