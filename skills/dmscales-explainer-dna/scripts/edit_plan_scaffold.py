#!/usr/bin/env python3
"""paket.md senaryosunu yan cümlelere böler ve stil kitinin edit-plan.md iskeletini (zamanlı) üretir.

Kullanım:
  python edit_plan_scaffold.py paket.md -o edit-plan.md [--wpm 170]
Çıkan blokların screen/media/foot/enter alanlarını references/onscreen.md kurallarıyla doldur.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qc import parse, words_of, fmt  # noqa: E402

SPLIT_WORDS = {"ve", "ama", "çünkü", "yani", "sonra", "fakat", "ancak", "ki"}
TEMPLATE_HINT = {
    "KAPI": "T07 figure left, text right",
    "MEKANİZMA": "T10 screenshot + footnote",
    "İSİM": "T04 definition card",
    "TEŞHİS": "T03 header + growing list",
    "TAKTİK": "T03 header + growing list",
    "UYARI": "T01 single line",
    "ÇERÇEVE": "CLD thought cloud + X",
    "AKSİYOM": "T09 quote + brain",
    "SAYAÇ": "T04 definition card",
    "KURAL": "T10 screenshot + footnote",
    "KÖPRÜ": "T15 creators field",
    "CTA": "T10 screenshot + footnote",
}


def clauses(text):
    out, cur = [], []
    for w in text.split():
        bare = re.sub(r"[^\wçğıöşüÇĞİÖŞÜ]", "", w).lower()
        if cur and bare in SPLIT_WORDS and len(cur) >= 6:
            out.append(" ".join(cur))
            cur = []
        cur.append(w)
        if re.search(r"[.,;:?!]$", w) and len(cur) >= 3:
            out.append(" ".join(cur))
            cur = []
    if cur:
        if out and len(cur) < 3:
            out[-1] += " " + " ".join(cur)
        else:
            out.append(" ".join(cur))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paket")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--wpm", type=float, default=170)
    ap.add_argument("--pause", type=float, default=0.12)
    a = ap.parse_args()
    meta, items, _, _, _ = parse(a.paket)
    spw = 60.0 / a.wpm
    t, n, blocks = 0.0, 0, []
    for it in items:
        cl = clauses(it["text"])
        for k, c in enumerate(cl):
            n += 1
            note = []
            if k == len(cl) - 1 and it["screens"]:
                note = [s.strip("()") for s in it["screens"]]
            blocks.append(
                f"## S{n:02d}  {fmt(t)}  {TEMPLATE_HINT.get(it['tag'], 'T01 single line')}   <!-- [{it['tag']}] -->\n"
                f'say:    "{c}"\n'
                f"screen: \n"
                f"media:  -\n"
                f"foot:   \n"
                f"enter:  \n"
                + (f"note:   {' | '.join(note)}\n" if note else "")
            )
            t += len(words_of(c)) * spw
        t += a.pause
    head = (f"# edit-plan.md — {meta.get('title', os.path.basename(a.paket))}\n"
            f"> İskelet: {n} çekim · ~{fmt(t)} @ {a.wpm:.0f} kel/dk. Zamanlar tahminîdir; gerçek ses kaydından yeniden hizalanır.\n"
            f"> Şablon ipuçları etikete göre varsayılandır; aynı şablonu 3 kez üst üste kullanma (onscreen.md §3).\n\n")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(head + "\n".join(blocks))
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"{n} çekim yazıldı → {a.out} (~{fmt(t)})")


if __name__ == "__main__":
    main()
