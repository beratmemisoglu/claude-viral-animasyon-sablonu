"""D — join meta + caption + audio results, print markdown tables + hit/flop group stats.
python -I d_aggregate.py <research_root>"""
import sys, os, json, glob
import numpy as np
sys.stdout.reconfigure(encoding="utf-8")
root = sys.argv[1]
S = os.path.join(root, "analysis", "scripts")


def load(fn):
    out = {}
    for ln in open(os.path.join(S, fn), encoding="utf-8"):
        ln = ln.strip()
        if ln.startswith("{"):
            d = json.loads(ln); out[d["id"]] = d
    return out


cap, aud = load("d_captions_results.jsonl"), load("d_audio_results.jsonl")
rows = []
for ch in ("ricksclips", "competitors"):
    for d in glob.glob(os.path.join(root, "videos", ch, "*")):
        m = json.load(open(os.path.join(d, "meta.json"), encoding="utf-8"))
        tr = open(os.path.join(d, "transcript.txt"), encoding="utf-8").read()
        rows.append(dict(ch=ch, channel=m["channel"], id=m["id"], title=m["title"], views=m["view_count"],
                         date=m["upload_date"], music_tags=tr.count("[music]"),
                         **{"c_" + k: v for k, v in cap.get(m["id"], {}).items() if k != "id"},
                         **{"a_" + k: v for k, v in aud.get(m["id"], {}).items() if k != "id"}))
rows.sort(key=lambda r: (r["ch"] != "ricksclips", r["channel"], -int(r["date"])))
ricks = [r for r in rows if r["ch"] == "ricksclips"]
newest = sorted(ricks, key=lambda r: r["date"], reverse=True)[:22]
core = {r["id"] for r in newest}
for r in rows:
    r["grp"] = ("CORE-HIT" if r["views"] >= 5e6 else "CORE-FLOP" if r["views"] <= 1e6 else "CORE-MID") if r["id"] in core \
        else ("OLD" if r["ch"] == "ricksclips" else "COMP")

print("| Kanal | id | Başlık | İzl. (M) | Grup | Kelime/kart | Kart sn (med) | Sync ms | y% | Yazı yük. px | LUFS | TP | LRA | Sessizlik<-35 | WPM | Duraklama>0.6 | F0 Hz | Ton aralığı st | Side−Mid dB | Boşluk seviyesi dB | Transient/10s | [music] |")
print("|" + "---|" * 23)
for r in rows:
    g = lambda k, f="{}": (f.format(r[k]) if r.get(k) is not None else "–")
    print(f"| {r['channel'][:14]} | {r['id']} | {r['title'][:38]} | {r['views']/1e6:.2f} | {r['grp']} | {g('c_words_per_card')} | {g('c_card_dur_med')} | {g('c_sync_offset_med_ms')} | {g('c_y_center_pct')} | {g('c_text_h_med_1080')} | {g('a_lufs_I')} | {g('a_lufs_TP')} | {g('a_lufs_LRA')} | {r.get('a_sil35',{}).get('n','–')} | {g('a_wpm_span')} | {g('a_pauses_gt_0.6s')} | {g('a_f0_med_hz')} | {g('a_f0_spread_st_p10_p90')} | {g('a_side_minus_mid_db')} | {g('a_vo_gap_level_rel_median_db')} | {g('a_transients_per_10s')} | {r['music_tags']} |")

keys = ["views", "c_words_per_card", "c_card_dur_med", "c_sync_offset_med_ms", "c_y_center_pct", "c_text_h_med_1080",
        "a_lufs_I", "a_lufs_TP", "a_lufs_LRA", "a_wpm_span", "a_wpm_articulation", "a_pauses_gt_0.6s", "a_pause_longest_s",
        "a_f0_med_hz", "a_f0_spread_st_p10_p90", "a_side_minus_mid_db", "a_floor_p10_rel_median_db",
        "a_vo_gap_level_rel_median_db", "a_transients_per_10s", "a_cuts_per_10s", "a_cuts_with_hf_swell_pct",
        "a_vo_start_s", "a_vo_end_gap_s", "a_dur", "music_tags"]
print("\n## Grup medyanları")
groups = {}
for r in rows:
    groups.setdefault(r["grp"], []).append(r)
    if r["grp"] == "COMP":
        groups.setdefault("COMP:" + r["channel"], []).append(r)
print("| metrik | " + " | ".join(f"{k} (n={len(v)})" for k, v in groups.items()) + " |")
print("|---|" + "---|" * len(groups))
for k in keys:
    vals = []
    for g, rs in groups.items():
        xs = [r[k] for r in rs if isinstance(r.get(k), (int, float))]
        vals.append(f"{np.median(xs):.4g}" if xs else "–")
    print(f"| {k} | " + " | ".join(vals) + " |")
# correlation in core
cr = [r for r in rows if r["id"] in core]
print("\n## Spearman (core 22) log-views vs metric")
from scipy.stats import spearmanr
for k in keys[1:]:
    xs = [(r[k], r["views"]) for r in cr if isinstance(r.get(k), (int, float))]
    if len(xs) > 5:
        rho, p = spearmanr([a for a, _ in xs], [b for _, b in xs])
        print(f"- {k}: rho={rho:+.2f} p={p:.2f}")
