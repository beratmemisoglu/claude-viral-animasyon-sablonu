#!/usr/bin/env python3
"""dmscales-explainer-dna QC: paket.md içindeki senaryoyu (## 4. bölümü) hit motorunun ölçütlerine göre denetler.

Kullanım:
  python qc.py paket.md [--wpm 170] [--vo script.txt] [--timed script_timed.txt] [--json]
"""
import argparse
import json
import re
import sys

TAGS = ["KAPI", "MEKANİZMA", "İSİM", "TEŞHİS", "TAKTİK", "UYARI", "ÇERÇEVE",
        "AKSİYOM", "SAYAÇ", "KURAL", "KÖPRÜ", "CTA"]
LINE_RE = re.compile(r"^\s*(?:`?\d+:\d\d(?:\.\d)?`?\s*)?\[(" + "|".join(TAGS) + r")\]\s*(.*)$")
SCREEN_INLINE_RE = re.compile(r"\(EKRAN:[^)]*\)")
SOURCE_RE = re.compile(r"\[KAYNAK GEREKL[İI][^\]]*\]")
PLACEHOLDER_RE = re.compile(r"\[[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ \-]{2,}:[^\]]*\]")

PRONOUNS = {"sen", "senin", "sana", "seni", "sende", "senden", "seninle", "kendin", "kendini", "kendine"}
VERB_2SG = ("sın", "sin", "sun", "sün", "san", "sen", "sınız")
POSS_2SG = ("ın", "in", "un", "ün", "ını", "ini", "unu", "ünü", "ına", "ine", "una", "üne",
            "ında", "inde", "unda", "ünde", "ından", "inden", "undan", "ünden")
POSS_STOP = {"için", "bin", "değin", "din", "kin", "çin", "ilin", "bilgin", "zengin", "ancak", "sin", "son"}
FILLERS = ["yani", "işte", "falan", "filan", "hani", "açıkçası", "arkadaşlar", "bu videoda", "aslında"]
TURN_WORDS = {"ama", "fakat", "ancak", "eğer"}
TURN_TAGS = {"TEŞHİS", "UYARI", "ÇERÇEVE", "İSİM"}
RESPONSE_TAGS = {"TAKTİK", "ÇERÇEVE", "UYARI", "KURAL", "AKSİYOM"}
DEICTIC_RE = re.compile(r"şunlardan biri|bu grafi|bu tablo|buraya kadar|burada|böyle bir|şuna benz|\bbunlar\b|\bşunlar\b|şöyle görün")
FORBIDDEN_CTA = ["abone ol", "beğenmeyi unutma", "beğen butonu", "beğeni bırak", "videoyu beğen", "like at",
                 "bildirimleri aç", "zile bas", "yorumlara yaz", "kanala abone"]
FIRST_PERSON = re.compile(r"\b(ben|benim|bence|bana|beni|hazırladım|kullanıyorum|güncelliyorum|tutuyorum)\b")
GREETING_RE = re.compile(r"merhaba|selam|hoş geldin|bu videoda|arkadaşlar|hadi başla")
NAMING_RE = re.compile(r"\b\w*(deniyor|diyor|denir|denen|diyelim|adı verilen|diyorum)\b")
MOTIVE_RE = re.compile(r"başkasını|başkasının|tercih eder|yerine .{0,40}(öne|iter|gösterir)")


def trlower(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def words_of(text):
    return [w for w in re.findall(r"\S+", text) if re.search(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü]", w)]


def clean_word(w):
    return re.sub(r"^[^\wçğıöşü%]+|[^\wçğıöşü%]+$", "", trlower(w))


def concept_regex(name):
    parts = []
    for w in trlower(name).split():
        w = re.sub(r"[^\wçğıöşü]", "", w)
        if not w:
            continue
        stem = w[: max(3, len(w) - 2)] if len(w) > 4 else w
        parts.append(re.escape(stem) + r"\w*")
    if not parts:
        return None
    return re.compile(r"\b" + r"\s+".join(parts), re.UNICODE)


def fmt(t):
    m, s = divmod(t, 60)
    return f"{int(m)}:{s:04.1f}"


def parse(path):
    text = open(path, encoding="utf-8").read()
    meta = {}
    for key, rx in [("target", r"^Hedef süre:\s*(\d+)"), ("counter", r"^Gizli sayaç:\s*(.+)$"),
                    ("concepts", r"^Kavramlar:\s*(.+)$"), ("title", r"^Başlık:\s*(.+)$")]:
        m = re.search(rx, text, re.M)
        if m:
            meta[key] = m.group(1).strip()
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if re.match(r"^##\s*4\b", l)), None)
    if start is None:
        start = -1
    end = next((i for i in range(start + 1, len(lines)) if re.match(r"^##\s*\d", lines[i])), len(lines))
    items, untagged, placeholders = [], [], 0
    sources = 0
    for raw in lines[start + 1:end]:
        line = raw.strip()
        if not line or line.startswith(("#", ">", "|")):
            continue
        if line.startswith("(EKRAN"):
            if items:
                items[-1]["screens"].append(line)
            continue
        m = LINE_RE.match(line)
        if m:
            tag, body = m.group(1), m.group(2)
        else:
            tag, body = None, line
            untagged.append(line)
        screens = SCREEN_INLINE_RE.findall(body)
        body = SCREEN_INLINE_RE.sub(" ", body)
        sources += len(SOURCE_RE.findall(body))
        body = SOURCE_RE.sub(" ", body)
        placeholders += len(PLACEHOLDER_RE.findall(body))
        body = PLACEHOLDER_RE.sub(" ", body)
        body = re.sub(r"\s+", " ", body).strip()
        if not body:
            if items and screens:
                items[-1]["screens"].extend(screens)
            continue
        items.append({"tag": tag, "text": body, "screens": screens})
    return meta, items, untagged, sources, placeholders


def run(path, wpm, pause):
    meta, items, untagged, sources, placeholders = parse(path)
    if not items:
        sys.exit("Senaryo bulunamadı: '## 4.' bölümünde [ETİKET] ile başlayan satır yok.")
    spw = 60.0 / wpm
    t = 0.0
    timeline = []  # (time, cleaned word, item index)
    for i, it in enumerate(items):
        ws = words_of(it["text"])
        it["start"] = t
        for w in ws:
            timeline.append((t, clean_word(w), i))
            t += spw
        it["end"] = t
        it["words"] = len(ws)
        t += pause
    total = t
    nwords = len(timeline)
    minutes = total / 60
    vo_low = trlower(" ".join(it["text"] for it in items))
    target = int(meta.get("target", 0)) or None
    title_n = None
    if "title" in meta:
        m = re.search(r"(\d+)\s*(Saniye|Seconds)", meta["title"], re.I)
        if m:
            title_n = int(m.group(1))
    if not target:
        target = title_n

    res = []

    def add(cid, name, ok, value, note="", level=None):
        res.append({"id": cid, "name": name, "status": level or ("ok" if ok else "fail"), "value": value, "note": note})

    first = items[0]
    fl = trlower(first["text"])
    ok = first["tag"] == "KAPI" and re.search(r"ilk (şey|yaptığı|olan)", fl) and not GREETING_RE.search(fl) and "?" not in fl
    add(1, "Açılış = sistemin 1. adımı", bool(ok), f'[{first["tag"]}] {len(words_of(first["text"]))} kelime',
        "İlk satır [KAPI] olmalı ve 'olan ilk şey şu' kalıbını içermeli; selam/soru yok; 18–30 kelime")

    tnum = next((tm for tm, w, _ in timeline if re.search(r"\d", w)), None)
    add(2, "İlk rakam ≤7 sn", tnum is not None and tnum <= 7, fmt(tnum) if tnum is not None else "yok")

    tname = None
    for it in items:
        if it["tag"] == "İSİM":
            tname = it["start"]
            break
    for tm, w, _ in timeline:
        if NAMING_RE.fullmatch(w or "") and (tname is None or tm < tname):
            tname = tm
            break
    add(3, "İlk vaftiz ≤15 sn", tname is not None and tname <= 15, fmt(tname) if tname is not None else "yok")

    concepts = [c.strip() for c in meta.get("concepts", "").split(";") if c.strip()]
    found = []
    for c in concepts:
        rx = concept_regex(c)
        if rx and rx.search(vo_low):
            found.append(c)
    missing = [c for c in concepts if c not in found]
    dens = len(found) / minutes if minutes else 0
    need = max(8, round(4 * minutes))
    add(4, "Kavram yoğunluğu ≥4/dk", dens >= 4 and len(found) >= need,
        f"{len(found)}/{len(concepts)} kavram VO'da · {dens:.1f}/dk (gereken ≥{need})",
        ("VO'da geçmeyen: " + ", ".join(missing)) if missing else ("'Kavramlar:' satırı yok" if not concepts else ""))

    gates = sum(1 for it in items if it["tag"] == "KAPI")
    gmin, gmax = max(3, round(total / 45)), round(total / 30) + 1
    add(5, "Aşama sayısı (KAPI)", gmin <= gates <= gmax, f"{gates} (beklenen {gmin}–{gmax})")

    bad = []
    for i, it in enumerate(items):
        if it["tag"] != "TEŞHİS":
            continue
        j = next((k for k in range(i + 1, len(items)) if items[k]["tag"] in RESPONSE_TAGS), None)
        gap = (items[j]["start"] - it["end"]) if j is not None else None
        if gap is None or gap > 8:
            bad.append(f'{fmt(it["start"])} ({"cevapsız" if gap is None else f"{gap:.0f} sn"})')
    add(6, "Ceza → taktik ≤8 sn", not bad, "tüm teşhisler eşleşti" if not bad else "; ".join(bad))

    cname = meta.get("counter")
    ccount = 0
    if cname:
        rx = concept_regex(cname)
        ccount = len(rx.findall(vo_low)) if rx else 0
    add(7, "Gizli sayaç ≥4 geçiş", ccount >= 4, f'"{cname or "?"}" × {ccount}', "" if cname else "'Gizli sayaç:' satırı yok")

    ax = sum(1 for it in items if it["tag"] == "AKSİYOM")
    mot = len(MOTIVE_RE.findall(vo_low))
    add(8, "Aksiyom + 'başkasını tercih eder'", ax >= 1 and mot >= 1, f"AKSİYOM×{ax}, hatırlatma×{mot}")

    nums = []
    for _, w, _ in timeline:
        if re.search(r"\d", w) and w not in nums:
            nums.append(w)
    add(9, "Rakam cetveli ≥6", len(nums) >= 6, f"{len(nums)}: " + ", ".join(nums[:12]))

    diag = [it for it in items if "şunlardan biri" in trlower(it["text"])]
    diag_ok = diag and all(it["screens"] for it in diag)
    add(10, "Teşhis listesi + EKRAN", bool(diag_ok), f"{len(diag)} bant", "" if diag_ok else "'şunlardan biri' + altında (EKRAN: 3 madde) gerekli")

    fr = [it for it in items if it["tag"] == "ÇERÇEVE"]
    if fr:
        pos = fr[0]["start"] / total * 100
        add(11, "Yeniden çerçeve %30–50", 30 <= pos <= 50 and len(fr) <= 2, f"{len(fr)} adet, ilki %{pos:.0f} ({fmt(fr[0]['start'])})")
    else:
        add(11, "Yeniden çerçeve %30–50", False, "yok")

    marks = [0.0]
    for it in items:
        if it["tag"] in TURN_TAGS:
            marks.append(it["start"])
    marks += [tm for tm, w, _ in timeline if w in TURN_WORDS]
    # köprü + CTA kapanışı salınım değil ◆ bitiştir (#18 ayrıca ölçer); orta-CTA kapanış sayılmaz
    tail_i = len(items)
    while tail_i > 0 and items[tail_i - 1]["tag"] in ("KÖPRÜ", "CTA"):
        tail_i -= 1
    tail = items[tail_i]["start"] if tail_i < len(items) else total
    marks = sorted(m for m in marks if m <= tail) + [tail]
    gaps = [(marks[k + 1] - marks[k], marks[k]) for k in range(len(marks) - 1)]
    mg, mat = max(gaps)
    add(12, "Düz bölüm ≤15 sn (sezgisel)", mg <= 15, f"en uzun {mg:.0f} sn ({fmt(mat)}'den itibaren)")

    buts = sum(1 for _, w, _ in timeline if w in {"ama", "fakat", "ancak"})
    add(13, "'Ama' ≥2,5/dk", buts / minutes >= 2.5, f"{buts} kez · {buts / minutes:.1f}/dk")

    you = 0
    for _, w, _ in timeline:
        if not w or "'" in w or "’" in w:
            continue
        if w in PRONOUNS or w.endswith(VERB_2SG) or (w.endswith(POSS_2SG) and w not in POSS_STOP and len(w) > 4):
            you += 1
    q = sum(it["text"].count("?") for it in items)
    yph = you / nwords * 100
    add(14, "Hitap ≥5/100 (sezgisel) · soru ≤2", yph >= 5 and q <= 2, f"2. tekil {yph:.1f}/100 · soru {q}")

    fill = 0
    fill_hits = []
    for it in items:
        low = trlower(it["text"])
        for f in FILLERS:
            if f == "aslında" and it["tag"] == "ÇERÇEVE":
                continue
            if f == "yani" and it["tag"] == "TAKTİK" and low.startswith("yani"):
                continue  # "Yani olabildiğince hızlı X için…" aşama sonu kalıbıdır, dolgu değil
            n = len(re.findall(r"\b" + f + r"\b", low))
            if n:
                fill += n
                fill_hits.append(f)
    add(15, "Dolgu ≤1/100", fill / nwords * 100 <= 1, f"{fill} ({', '.join(sorted(set(fill_hits))) or '-'})")

    fp = [fmt(it["start"]) for it in items
          if it["tag"] not in ("KÖPRÜ", "CTA") and FIRST_PERSON.search(trlower(it["text"]))]
    add(16, "1. şahıs yalnız CTA'da", not fp, "temiz" if not fp else "CTA öncesi: " + ", ".join(fp), level=None if not fp else "warn")

    late_warn = [it for it in items if it["tag"] == "UYARI" and it["start"] / total >= 0.70]
    add(17, "Doruk sonrası uyarı (≥%70)", bool(late_warn), f"{len(late_warn)} uyarı")

    forb = [f for f in FORBIDDEN_CTA if f in vo_low]
    cta_secs = sum(it["end"] - it["start"] for it in items if it["tag"] in ("KÖPRÜ", "CTA"))
    share = cta_secs / total * 100
    add(18, "CTA temiz ve ≤%12", not forb and share <= 12, f"pay %{share:.0f}" + (f" · yasak: {', '.join(forb)}" if forb else ""))

    if target:
        dev = (total - target) / target * 100
        add(19, "Süre ≈ hedef (±%8 tahmini)", abs(dev) <= 8, f"{fmt(total)} tahmini / hedef {target} sn ({dev:+.0f}%) · {nwords} kelime @ {wpm} kel/dk",
            f"başlıktaki N={title_n}" if title_n and title_n != target else "")
    else:
        add(19, "Süre ≈ hedef", False, f"{fmt(total)} · 'Hedef süre:' satırı yok", level="warn")

    dmiss = [fmt(it["start"]) for it in items if DEICTIC_RE.search(trlower(it["text"])) and not it["screens"]]
    add(20, "Deiktik → EKRAN", not dmiss, "temiz" if not dmiss else "EKRAN eksik: " + ", ".join(dmiss))

    add(21, "Kaynak etiketi", sources == 0 and placeholders == 0,
        f"KAYNAK GEREKLİ×{sources} · yer tutucu×{placeholders}",
        "YAYINA HAZIR DEĞİL" if sources or placeholders else "", level=None if not (sources or placeholders) else "warn")

    if untagged:
        add(22, "Etiketsiz VO satırı", False, f"{len(untagged)} satır", "İlk: " + untagged[0][:60])

    return {"file": path, "words": nwords, "seconds": round(total, 1), "wpm": wpm, "checks": res,
            "items": [{k: it[k] for k in ("tag", "text", "start", "end", "screens")} for it in items]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paket")
    ap.add_argument("--wpm", type=float, default=170)
    ap.add_argument("--pause", type=float, default=0.12, help="satır arası duraklama (sn)")
    ap.add_argument("--vo", help="ElevenLabs için düz VO metni yaz")
    ap.add_argument("--timed", help="zaman damgalı satırlar yaz")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    r = run(a.paket, a.wpm, a.pause)
    if a.vo:
        with open(a.vo, "w", encoding="utf-8") as f:
            f.write("\n".join(it["text"] for it in r["items"]) + "\n")
    if a.timed:
        with open(a.timed, "w", encoding="utf-8") as f:
            for it in r["items"]:
                f.write(f'{fmt(it["start"])}\t{it["tag"]}\t{it["text"]}\n')
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return
    sym = {"ok": "✔", "fail": "✖", "warn": "⚠"}
    ok = sum(1 for c in r["checks"] if c["status"] == "ok")
    print(f"QC · {r['words']} kelime · ~{fmt(r['seconds'])} @ {a.wpm:.0f} kel/dk · {ok}/{len(r['checks'])} geçti")
    for c in r["checks"]:
        line = f"{sym[c['status']]} {c['id']:>2} {c['name']}: {c['value']}"
        if c["note"] and c["status"] != "ok":
            line += f"  → {c['note']}"
        print(line)


if __name__ == "__main__":
    main()
