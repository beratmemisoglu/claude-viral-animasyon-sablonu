// sfxgen.mjs — zero-dependency procedural SFX/music-stem generator (Node >= 18)
// usage: node sfxgen.mjs <outDir>
import fs from 'node:fs';
import path from 'node:path';

const SR = 48000;
const OUT = process.argv[2] ?? 'public/sfx';
fs.mkdirSync(OUT, {recursive: true});

// ---------- utilities ----------
let seed = 1337; // deterministic noise => identical renders every time
const rnd = () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296) * 2 - 1;
const buf = (sec) => new Float32Array(Math.ceil(sec * SR));
const TAU = Math.PI * 2;
const mtof = (m) => 440 * 2 ** ((m - 69) / 12);
const env = (t, a, d) => (t < a ? t / a : Math.exp(-(t - a) / d)); // attack-lin, exp decay
function lp(x, cutoff) { // one-pole low-pass, cutoff may be fn(i)
  let y = 0; const o = new Float32Array(x.length);
  for (let i = 0; i < x.length; i++) {
    const fc = Math.max(20, typeof cutoff === 'function' ? cutoff(i) : cutoff); // clamp: negative fc = unstable
    const a = 1 - Math.exp((-TAU * fc) / SR); y += a * (x[i] - y); o[i] = y;
  }
  return o;
}
const hp = (x, fc) => { const l = lp(x, fc); return x.map((v, i) => v - l[i]); };
function normalize(x, peakDb = -1) {
  let m = 0; for (const v of x) m = Math.max(m, Math.abs(v));
  const g = m ? 10 ** (peakDb / 20) / m : 1; return x.map((v) => v * g);
}
function fadeEdges(x, ms = 4) { const n = Math.floor((ms / 1000) * SR);
  for (let i = 0; i < n && i < x.length; i++) { x[i] *= i / n; x[x.length - 1 - i] *= i / n; } return x; }
function writeWav(name, x, peakDb = -1) {
  x = fadeEdges(normalize(x, peakDb));
  const b = Buffer.alloc(44 + x.length * 2);
  b.write('RIFF', 0); b.writeUInt32LE(36 + x.length * 2, 4); b.write('WAVE', 8);
  b.write('fmt ', 12); b.writeUInt32LE(16, 16); b.writeUInt16LE(1, 20); b.writeUInt16LE(1, 22);
  b.writeUInt32LE(SR, 24); b.writeUInt32LE(SR * 2, 28); b.writeUInt16LE(2, 32); b.writeUInt16LE(16, 34);
  b.write('data', 36); b.writeUInt32LE(x.length * 2, 40);
  x.forEach((v, i) => b.writeInt16LE(Math.max(-32768, Math.min(32767, Math.round(v * 32767))), 44 + i * 2));
  fs.writeFileSync(path.join(OUT, name), b); console.log('wrote', name, (x.length / SR).toFixed(2) + 's');
}

// ---------- generators ----------
function alarmBeep({beeps = 4, freq = 2000, on = 0.09, gap = 0.07, rest = 0.5} = {}) {
  const x = buf(beeps * (on + gap) + rest);
  for (let b = 0; b < beeps; b++) {
    const s = Math.floor(b * (on + gap) * SR);
    for (let i = 0; i < on * SR; i++) { const t = i / SR;
      const sq = Math.sign(Math.sin(TAU * freq * t)) * 0.5 + Math.sin(TAU * freq * t) * 0.5; // softened square
      x[s + i] += sq * Math.min(1, t / 0.003, (on - t) / 0.003); }
  }
  return lp(x, 6000);
}
function heartbeat({bpm = 60, beats = 4} = {}) {
  const per = 60 / bpm, x = buf(beats * per + 0.5);
  const thump = (start, amp) => { for (let i = 0; i < 0.25 * SR; i++) { const t = i / SR;
      const f = 45 + 50 * Math.exp(-t / 0.03); // pitch drop = "chest" thump
      x[start + i] += amp * Math.sin(TAU * f * t) * env(t, 0.004, 0.07); } };
  for (let b = 0; b < beats; b++) { const s = Math.floor(b * per * SR);
    thump(s, 1); thump(s + Math.floor(0.22 * SR), 0.7); } // lub ... dub
  return lp(x, 400);
}
function drone({midi = 33, sec = 8} = {}) { // A1
  const x = buf(sec), f = mtof(midi);
  for (let i = 0; i < x.length; i++) { const t = i / SR;
    const lfo = 1 + 0.003 * Math.sin(TAU * 0.13 * t);
    x[i] = Math.sin(TAU * f * lfo * t) + 0.5 * Math.sin(TAU * f * 1.5 * t + 0.3) + 0.25 * Math.sin(TAU * f * 2.003 * t)
      + 0.08 * rnd();
    x[i] *= Math.min(1, t / 2, (sec - t) / 2); } // 2 s fade in/out so it loops/crossfades
  return lp(x, 300);
}
function whoosh({sec = 0.7, peak = 0.55} = {}) { // filtered noise sweep, peak = position of loudest point (0..1)
  const x = buf(sec), n = x.length;
  for (let i = 0; i < n; i++) x[i] = rnd();
  const y = lp(x, (i) => 300 + 5000 * Math.sin(Math.PI * Math.min(1, i / n / peak / 2 + 0.0001)) ** 2);
  return hp(y.map((v, i) => { const p = i / n; return v * (p < peak ? (p / peak) ** 2 : ((1 - p) / (1 - peak)) ** 1.5); }), 150);
}
function impact({sec = 0.6, body = 70, click = 1} = {}) { // punch / slap / clack depending on params
  const x = buf(sec);
  for (let i = 0; i < x.length; i++) { const t = i / SR;
    const f = body + body * 2 * Math.exp(-t / 0.02);
    x[i] = Math.sin(TAU * f * t) * env(t, 0.001, 0.09) + click * rnd() * env(t, 0.0005, 0.012); }
  return x;
}
function rumble({sec = 4} = {}) { const x = buf(sec);
  for (let i = 0; i < x.length; i++) x[i] = rnd() * Math.min(1, (i / SR) / 1.5, (sec - i / SR) / 1.5);
  return lp(lp(x, 80), 120); }
function glassCrack({sec = 1.2} = {}) { const x = buf(sec);
  for (let k = 0; k < 40; k++) { // random tiny ticks clustered at the front + ringing partials
    const s = Math.floor(Math.abs(rnd()) ** 2 * 0.5 * SR), f = 2500 + Math.abs(rnd()) * 6000, a = Math.abs(rnd());
    for (let i = 0; i < 0.15 * SR && s + i < x.length; i++) { const t = i / SR;
      x[s + i] += a * (Math.sin(TAU * f * t) * env(t, 0.0005, 0.03) + rnd() * env(t, 0.0002, 0.004)); } }
  return hp(x, 1500);
}
function pianoNote(midi, sec = 3, vel = 1) { // additive "felt piano": decaying partials, slight inharmonicity
  const x = buf(sec), f = mtof(midi);
  for (let h = 1; h <= 8; h++) { const fh = f * h * Math.sqrt(1 + 0.0004 * h * h), amp = vel / h ** 1.3, dec = 1.6 / h ** 0.6;
    if (fh > SR / 2.2) break;
    for (let i = 0; i < x.length; i++) { const t = i / SR; x[i] += amp * Math.sin(TAU * fh * t) * env(t, 0.006, dec); } }
  for (let i = 0; i < 0.01 * SR; i++) x[i] += 0.05 * vel * rnd(); // hammer/felt noise
  return lp(x, 3500);
}
function mixInto(dst, src, atSec, gain = 1) { const s = Math.floor(atSec * SR);
  for (let i = 0; i < src.length && s + i < dst.length; i++) dst[s + i] += src[i] * gain; return dst; }
function pianoPhrase(notes, bpm, tailSec = 3) { // notes: [beat, midi, lenBeats, vel]
  const spb = 60 / bpm, end = Math.max(...notes.map((n) => (n[0] + n[2]) * spb)) + tailSec, x = buf(end);
  for (const [beat, m, len, vel = 0.8] of notes) mixInto(x, pianoNote(m, len * spb + tailSec, vel), beat * spb);
  return x;
}
function reverb(x, mix = 0.3) { // cheap Schroeder-ish comb reverb
  const y = Float32Array.from(x);
  for (const [d, g] of [[1557, 0.8], [1617, 0.79], [1491, 0.78], [1422, 0.77]]) { const c = new Float32Array(x.length);
    for (let i = 0; i < x.length; i++) c[i] = x[i] + (i >= d * 2 ? g * c[i - d * 2] : 0);
    for (let i = 0; i < x.length; i++) y[i] += (mix / 4) * c[i]; }
  return y;
}
function wind({sec = 10} = {}) { const x = buf(sec); for (let i = 0; i < x.length; i++) x[i] = rnd();
  return lp(x, (i) => 700 + 350 * Math.sin(TAU * 0.11 * (i / SR)) + 200 * Math.sin(TAU * 0.37 * (i / SR)))
    .map((v, i) => v * Math.min(1, (i / SR) / 2, (sec - i / SR) / 2)); }
function shimmer({sec = 4} = {}) { const notes = [81, 84, 88, 91, 93]; const x = buf(sec); // A5 C6 E6 G6 A6 sparkles
  notes.forEach((m, k) => { for (let i = 0; i < x.length; i++) { const t = i / SR;
    x[i] += 0.3 * Math.sin(TAU * mtof(m) * t) * Math.sin(TAU * (0.5 + 0.17 * k) * t) ** 2 * Math.min(1, t / 1.5, (sec - t) / 1.5); } });
  return reverb(x, 0.4); }

// ---------- render the library ----------
writeWav('alarm_beep.wav', alarmBeep());                 // tip: freq: 1760 (A6) to sit in-key
writeWav('heartbeat_60.wav', heartbeat({bpm: 60, beats: 4}));
writeWav('heartbeat_120.wav', heartbeat({bpm: 120, beats: 8}));
writeWav('drone_A1.wav', drone({midi: 33, sec: 12}), -6);
writeWav('whoosh_text.wav', whoosh({sec: 0.5, peak: 0.4}), -6);   // offsetToPeak = 0.2 s = 6 f @30fps
writeWav('whoosh_cut.wav', whoosh({sec: 0.9, peak: 0.7}), -3);
writeWav('punch.wav', impact({body: 70, click: 0.8}));
writeWav('slap_clack.wav', impact({sec: 0.25, body: 300, click: 1.5}));
writeWav('title_thud.wav', reverb(impact({sec: 2.5, body: 42, click: 0.2}), 0.25));
writeWav('rumble_low.wav', rumble({sec: 6}), -4);
writeWav('glass_crack.wav', glassCrack());
writeWav('wind_loop.wav', wind({sec: 12}), -8);
writeWav('sunrise_shimmer.wav', shimmer(), -6);
// Act-1 motif: A minor, 72 BPM (25 frames/beat @30fps). [beat, midi, lenBeats, vel]
writeWav('piano_motif_Am_72.wav', reverb(pianoPhrase([
  [0, 45, 4, 0.6], [0, 69, 1, 0.7], [1, 72, 1, 0.6], [2, 76, 2, 0.7],        // Am
  [4, 41, 4, 0.6], [4, 69, 1, 0.6], [5, 72, 1, 0.5], [6, 77, 2, 0.6],        // F
  [8, 48, 4, 0.6], [8, 67, 1, 0.6], [9, 72, 1, 0.5], [10, 76, 2, 0.6],       // C
  [12, 43, 4, 0.6], [12, 67, 1, 0.6], [13, 71, 1, 0.5], [14, 74, 2, 0.6],    // G
], 72), 0.35), -3);
// Finale reprise (major): same rhythm, swap C->C# (A major) in the first bar, end on A major chord.
