"""D — audio measurement per video.  python -I d_audio.py <video_dir> ...  -> JSON line per video
- ebur128 (integrated LUFS, LRA, true peak) via ffmpeg
- silencedetect at -35 dB / 0.25 s and -45 dB / 0.25 s
- speaking rate + pause map from json3 word onsets
- mid/side ratio (VO is mono-centred, music/SFX usually stereo) overall and in VO gaps
- energy floor (p10 of 100 ms RMS, relative to median) -> bed under the voice?
- pitch (autocorrelation F0 on mid channel, 16 kHz): median Hz + spread in semitones
- transient index: 23 ms frames where broadband energy jumps >=9 dB over the previous 150 ms mean
  and the frame is >= -30 dBFS ("hits" per 10 s) + high-band (>5 kHz) swells at visual cuts (whoosh proxy)
"""
import sys, os, json, re, glob, subprocess
import numpy as np
from scipy import signal
sys.stdout.reconfigure(encoding="utf-8")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace").stderr


def ebur(path):
    e = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"])
    s = e[e.rfind("Summary:"):]
    g = lambda k: float(re.search(k + r":\s+(-?[\d.]+|-inf)", s).group(1).replace("-inf", "-99"))
    return dict(I=g("I"), LRA=g("LRA"), TP=g("Peak"))


def silences(path, db, d=0.25):
    e = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", f"silencedetect=noise={db}dB:d={d}", "-f", "null", "-"])
    durs = [float(x) for x in re.findall(r"silence_duration: ([\d.]+)", e)]
    return dict(n=len(durs), longest=round(max(durs), 2) if durs else 0, total=round(sum(durs), 2))


def cuts(path):
    e = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-an", "-vf",
             "scale=96:170,select='gt(scene,0.05)',showinfo", "-f", "null", "-"])
    out = []
    for t in (float(x) for x in re.findall(r"pts_time:([\d.]+)", e)):
        if not out or t - out[-1] >= 0.4:   # soft transitions span several frames -> one cut
            out.append(t)
    return out


def pcm(path, sr=16000):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "2", "-ar", str(sr), "-f", "f32le", "-"],
                       capture_output=True)
    x = np.frombuffer(p.stdout, np.float32).reshape(-1, 2)
    return x


def words(d):
    f = [x for x in glob.glob(os.path.join(d, "*.json3")) if "en-orig" in x] or glob.glob(os.path.join(d, "*.json3"))
    j = json.load(open(f[0], encoding="utf-8"))
    out = []
    for ev in j.get("events", []):
        t0 = ev.get("tStartMs", 0)
        for s in ev.get("segs", []) or []:
            w = s.get("utf8", "").strip()
            if w and not w.startswith("["):
                out.append(((t0 + s.get("tOffsetMs", 0)) / 1000.0, w))
    out.sort()
    return out


def db(x):
    return 10 * np.log10(np.maximum(x, 1e-12))


def f0_track(m, sr):
    fl, hop = int(0.04 * sr), int(0.02 * sr)
    lo, hi = int(sr / 400), int(sr / 70)
    f0 = []
    for i in range(0, len(m) - fl, hop):
        fr = m[i:i + fl] - m[i:i + fl].mean()
        e = (fr ** 2).sum()
        if e < 1e-4 * fl * 0.01:
            continue
        ac = np.correlate(fr, fr, "full")[fl - 1:]
        ac = ac / (ac[0] + 1e-9)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.55:
            f0.append(sr / k)
    return np.array(f0)


def analyse(d):
    path = os.path.join(d, "video.mp4")
    r = dict(id=os.path.basename(d))
    r.update({"lufs_" + k: v for k, v in ebur(path).items()})
    r["sil35"] = silences(path, -35)
    r["sil45"] = silences(path, -45)
    sr = 16000
    x = pcm(path, sr)
    dur = len(x) / sr
    L, R = x[:, 0].astype(np.float64), x[:, 1].astype(np.float64)
    mid, side = (L + R) / 2, (L - R) / 2
    W = int(0.1 * sr)
    n = len(mid) // W
    em = (mid[:n * W].reshape(n, W) ** 2).mean(1)
    es = (side[:n * W].reshape(n, W) ** 2).mean(1)
    emdb = db(em)
    act = emdb > np.percentile(emdb, 95) - 40
    r["side_minus_mid_db"] = round(float(db(es[act].mean()) - db(em[act].mean())), 1)
    r["floor_p10_rel_median_db"] = round(float(np.percentile(emdb, 10) - np.median(emdb)), 1)
    r["floor_p10_dbfs"] = round(float(np.percentile(emdb, 10)), 1)
    # words / pacing
    ws = words(d)
    t = np.array([w[0] for w in ws])
    r["n_words"] = len(ws)
    if len(t) > 3:
        span = t[-1] - t[0] + 0.3
        r["wpm_span"] = round(60 * len(t) / span)
        gaps = np.diff(t)
        r["pauses_gt_0.6s"] = int((gaps > 0.6).sum())
        r["pause_longest_s"] = round(float(gaps.max()), 2)
        speech_time = span - float(np.clip(gaps - 0.45, 0, None).sum())
        r["wpm_articulation"] = round(60 * len(t) / speech_time)
        r["vo_start_s"] = round(float(t[0]), 2)
        r["vo_end_gap_s"] = round(dur - float(t[-1]), 2)
        # energy in VO gaps (> 0.6 s) vs during speech -> music bed under voice?
        gap_db, gap_side = [], []
        for a, b in zip(t[:-1], t[1:]):
            if b - a > 0.7:
                i0, i1 = int((a + 0.45) * 10), int((b - 0.05) * 10)
                if i1 > i0:
                    gap_db.append(emdb[i0:i1].mean()); gap_side.append(db(es[i0:i1].mean()))
        if gap_db:
            r["vo_gap_level_rel_median_db"] = round(float(np.mean(gap_db) - np.median(emdb)), 1)
            r["vo_gap_side_dbfs"] = round(float(np.mean(gap_side)), 1)
    # pitch
    f0 = f0_track(mid[: sr * 70], sr)
    if len(f0) > 50:
        st = 12 * np.log2(f0 / np.median(f0))
        r["f0_med_hz"] = round(float(np.median(f0)))
        r["f0_spread_st_p10_p90"] = round(float(np.percentile(st, 90) - np.percentile(st, 10)), 1)
    # transients
    Wt = int(0.023 * sr)
    nt = len(mid) // Wt
    et = db((mid[:nt * Wt].reshape(nt, Wt) ** 2).mean(1))
    hits = 0
    last = -99
    for i in range(7, nt):
        ref = db(np.mean(10 ** (et[i - 7:i] / 10)))
        if et[i] - ref >= 9 and et[i] > -30 and i - last > 8:
            hits += 1; last = i
    r["transients_per_10s"] = round(10 * hits / dur, 1)
    # high band swells at cuts
    b, a = signal.butter(4, 5000 / (sr / 2), "high")
    hb = signal.lfilter(b, a, mid)
    Wh = int(0.05 * sr)
    nh = len(hb) // Wh
    eh = db((hb[:nh * Wh].reshape(nh, Wh) ** 2).mean(1))
    base = np.median(eh)
    c = cuts(path)
    r["n_cuts"] = len(c)
    r["cuts_per_10s"] = round(10 * len(c) / dur, 1)
    swell = 0
    for tc in c:
        i0, i1 = max(0, int((tc - 0.3) / 0.05)), min(nh, int((tc + 0.2) / 0.05))
        if i1 > i0 and eh[i0:i1].max() - base > 10:
            swell += 1
    r["cuts_with_hf_swell_pct"] = round(100 * swell / max(1, len(c)))
    r["dur"] = round(dur, 1)
    return r


if __name__ == "__main__":
    for d in sys.argv[1:]:
        try:
            res = analyse(d)
        except Exception as e:
            res = dict(id=os.path.basename(d), error=repr(e))
        print(json.dumps(res), flush=True)
