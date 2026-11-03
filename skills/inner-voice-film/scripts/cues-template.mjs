// PROCRASTINATION cue sheet — calm score (soft felt piano + pads), voiced twin (ElevenLabs), music ducked under the voice.
function readWav(file) { const b = fs.readFileSync(file); let p = 12, fmt = null, data = null;
  while (p < b.length) { const id = b.toString('ascii', p, p + 4), sz = b.readUInt32LE(p + 4);
    if (id === 'fmt ') fmt = {ch: b.readUInt16LE(p + 10)}; if (id === 'data') { data = b.subarray(p + 8, p + 8 + sz); break; } p += 8 + sz + (sz % 2); }
  const n = data.length / 2 / fmt.ch, x = new Float32Array(n);
  for (let i = 0; i < n; i++) { let v = 0; for (let c = 0; c < fmt.ch; c++) v += data.readInt16LE((i * fmt.ch + c) * 2); x[i] = v / fmt.ch / 32768; } return x; }
const softPiano = (m, sec = 4, vel = 0.5) => lp(pianoNote(m, sec, vel), 2200);
function tick() { const x = buf(0.05); for (let i = 0; i < x.length; i++) { const t = i / SR; x[i] = (rnd() * 0.5 + Math.sin(TAU * 2600 * t)) * env(t, 0.0003, 0.005); } return hp(x, 1200); }
function noiseBurst(sec, lo, hi, shape = 1) { const x = buf(sec); for (let i = 0; i < x.length; i++) x[i] = rnd(); const y = bp(x, lo, hi);
  for (let i = 0; i < y.length; i++) { const p = i / y.length; y[i] *= Math.sin(Math.PI * p) ** shape; } return norm(y); }
function sizzle(sec) { const x = buf(sec); for (let i = 0; i < x.length; i++) x[i] = rnd() * (Math.abs(rnd()) > 0.97 ? 3 : 1); const y = hp(x, 3000);
  for (let i = 0; i < y.length; i++) y[i] *= Math.min(1, (i / SR) / 0.3, (sec - i / SR) / 0.5); return norm(y); }
function growl() { const x = buf(1.1); for (let i = 0; i < x.length; i++) { const t = i / SR; x[i] = Math.sin(TAU * (70 + 25 * Math.sin(TAU * 7 * t)) * t) * Math.sin(Math.PI * t / 1.1) * (0.7 + 0.3 * rnd()); } return lp(x, 300); }
function bell(m) { const x = buf(1.2), f = mtof(m); for (let i = 0; i < x.length; i++) { const t = i / SR; x[i] = (Math.sin(TAU * f * t) + 0.3 * Math.sin(TAU * f * 2 * t)) * env(t, 0.002, 0.35); } return x; }

const N = Math.ceil((TOTAL / FPS) * SR) + SR;
const MU = new Float32Array(N), FX = new Float32Array(N), VO = new Float32Array(N);
const mus = (f, x, g = 1) => add(MU, x, fr(f), g), sfx = (f, x, g = 1) => add(FX, x, fr(f), g), voc = (f, x, g = 1) => add(VO, x, fr(f), g);
sfx(0, roomTone(TOTAL / FPS - 1.5), 0.01);

// ---------- music ----------
const Am = [45, 57, 60, 64], F = [41, 57, 60, 65], Cm = [48, 55, 60, 64], G = [43, 55, 59, 62], Amaj = [45, 57, 61, 64], D = [50, 57, 62, 66], E = [52, 56, 59, 64];
mus(S.hook + 30, reverb(softPiano(69, 4, 0.45), 0.5), 0.3);
{ const prog = [Am, F, Cm, G], mel = [76, 72, 74, 71, 72, 69, 71, 67]; let k = 0;
  for (let f = S.ritual; f < S.mirror + 240; f += 120, k++) { mus(f, pad(prog[k % 4], 4.6), 0.1);
    mus(f, reverb(softPiano(mel[(k * 2) % 8], 3.5, 0.35), 0.45), 0.16); mus(f + 60, reverb(softPiano(mel[(k * 2 + 1) % 8], 3.5, 0.3), 0.45), 0.13); } }
mus(S.seduction + 10, drone((S.mirror + 240 - S.seduction - 10) / FPS + 2).map((v, i) => v * Math.min(1, i / (SR * 4))), 0.06);
mus(S.mirror + 150, riser(100 / FPS), 0.08);
for (const [o, m] of [[15, 64], [49, 60], [150, 57], [192, 69]]) mus(S.bottom + o, reverb(softPiano(m, 5, 0.4), 0.5), 0.22);
mus(S.turn + 60, pad(Am, 9), 0.07);
{ const prog = [F, Cm, G, Am], arp = (ch) => [ch[1] + 12, ch[2] + 12, ch[3] + 12, ch[2] + 12]; let k = 0;
  for (let f = S.run; f < S.boss - 10; f += 90, k++) { const ch = prog[k % 4]; mus(f, pad(ch, 3.4), 0.09); mus(f, softPiano(ch[0] - 12, 3, 0.35), 0.14);
    arp(ch).forEach((m, j) => mus(f + j * 22, reverb(softPiano(m, 2.2, 0.28), 0.35), 0.1)); } }
mus(S.montage + 165, riser(60 / FPS), 0.06);
mus(S.summit, pad(Amaj, 6.4), 0.12); mus(S.summit + 180, pad(D, 6.4), 0.12);
for (const [o, m] of [[60, 76], [106, 81], [200, 78], [260, 76]]) mus(S.summit + o, reverb(softPiano(m, 4, 0.4), 0.45), 0.16);
[Amaj, D, E, Amaj].forEach((ch, k) => { mus(S.bookend + k * 66, pad(ch, 2.8), 0.08); mus(S.bookend + k * 66, reverb(softPiano([76, 78, 80, 81][k], 3, 0.32), 0.45), 0.14); });
sfx(S.title + 20, reverb(impact(2.5, 42, 0.2), 0.25), 0.45);
mus(S.title + 92, reverb(phrase([[0, 45, 6, 0.5], [0, 57, 6, 0.4], [0, 61, 6, 0.4], [0, 64, 6, 0.4], [0, 69, 6, 0.35]], 72, 4), 0.4), 0.22);

// ---------- SFX ----------
for (let k = 0; k < 13; k++) sfx(S.ritual + 170 + k * 3, tick(), 0.06);
for (const at of [S.seduction + 12, S.sport + 4, S.mirror + 40, S.cook + 4]) sfx(at, rumble(2.2), 0.16);
sfx(S.food + 6, noiseBurst(0.4, 200, 1200), 0.06); sfx(S.food + 50, growl(), 0.35);
for (let k = 0; k < 4; k++) sfx(S.food + 86 + k * 6, noiseBurst(0.08, 1500, 6000, 0.5), 0.08);
sfx(S.laundry + 2, noiseBurst(0.6, 300, 2500), 0.06); sfx(S.laundry + 84, noiseBurst(0.3, 150, 900), 0.1);
{ let f = S.mirror + 120, gap = 24; while (f < S.mirror + 250) { sfx(f, tick(), 0.04); f += gap; gap = Math.max(6, gap * 0.88); } }
sfx(S.mirror + 250, glassCrack(), 0.35); sfx(S.mirror + 250, impact(1.2, 40, 0.3), 0.25);
sfx(S.turn + 28, noiseBurst(0.25, 200, 1200), 0.1); sfx(S.turn + 44, impact(0.1, 300, 0.4), 0.08);
sfx(S.turn + 150, noiseBurst(0.4, 150, 900), 0.12); sfx(S.turn + 175, reverb(bell(88), 0.3), 0.1);
for (let f = S.turn + 70; f < S.turn + 132; f += 8) sfx(f, step(), 0.06);
for (let f = S.turn + 200; f < S.turn + 330; f += 8) sfx(f, step(), 0.06);
for (let f = S.run; f < S.run + 110; f += 15) sfx(f, step(), 0.1);
for (let f = S.run + 182; f < S.cook; f += 15) sfx(f, step(), 0.1);
sfx(S.cook, sizzle(4), 0.05); sfx(S.cook + 140, impact(0.08, 600, 0.6), 0.1); sfx(S.cook + 150, sizzle(4), 0.04);
sfx(S.cook + 190, reverb(bell(88), 0.3), 0.08);
for (const h of [110, 152, 194]) { sfx(S.box + h, impact(0.5, 65, 0.9), 0.4); sfx(S.box + h + 1, glassCrack(), 0.08); }
sfx(S.montage + 18, impact(0.4, 65, 0.8), 0.25);
sfx(S.boss, rumble(4), 0.3); sfx(S.boss + 95, impact(1.2, 38, 0.4), 0.35);
sfx(S.boss + 163, whoosh(0.45, 0.85), 0.18);
sfx(S.boss + 175, impact(1.6, 42, 0.8), 0.5); sfx(S.boss + 175, glassCrack(), 0.2); sfx(S.boss + 180, shimmer(3), 0.1);
sfx(S.boss + 200, noiseBurst(0.8, 200, 900), 0.06);
sfx(S.summit - 15, wind((S.bookend - S.summit + 30) / FPS), 0.05);
for (let f = S.summit; f < S.summit + 140; f += 15) sfx(f, step(), 0.08);
sfx(S.bookend + 196, noiseBurst(0.8, 200, 900), 0.06);

// ---------- the twin's voice (ElevenLabs "Second Self - Solitude") ----------
const V = (n) => readWav(path.join('public/audio/voice/procrastination', `v${n}.wav`));
const lines = [
  [S.ritual + 70, 1, 1.0], [S.ritual + 222, 2, 1.0], [S.seduction + 92, 3, 1.0], [S.seduction + 178, 4, 1.1],
  [S.food + 70, 5, 1.0], [S.sport + 66, 6, 1.0], [S.mirror + 80, 7, 1.05], [S.mirror + 165, 8, 1.2],
  [S.turn + 232, 1, 0.7], [S.cook + 60, 9, 1.0], [S.box + 18, 3, 0.5], [S.box + 40, 6, 0.5], [S.box + 62, 4, 0.5],
  [S.boss + 95, 10, 1.3],
];
const voiced = [];
for (const [at, n, g] of lines) { const v = V(n); voc(at, v, g); voiced.push([fr(at), fr(at) + v.length]); }
{ const duck = new Float32Array(N).fill(1); for (const [a, b] of voiced) for (let i = Math.max(0, a - 7200); i < Math.min(N, b + 24000); i++) {
    const t = i < a ? 1 - (a - i) / 7200 : i > b ? 1 - (i - b) / 24000 : 1; duck[i] = Math.min(duck[i], 1 - 0.6 * t); }
  for (let i = 0; i < N; i++) MU[i] *= duck[i]; }
const mute = (a, b, B) => { for (let i = fr(a); i < fr(b) && i < N; i++) B[i] *= Math.max(0, 1 - (i - fr(a)) / (SR * 0.15)); };
mute(S.mirror + 254, S.bottom, MU); mute(S.mirror + 254, S.bottom, FX);
for (const B of [MU, FX]) for (let i = fr(S.boss + 140); i < fr(S.boss + 163); i++) B[i] *= 0.15;

const M = new Float32Array(N); for (let i = 0; i < N; i++) M[i] = MU[i] + FX[i] + VO[i];
{ const a = fr(TOTAL - 45); for (let i = a; i < N; i++) M[i] *= Math.max(0, 1 - (i - a) / (SR * 0.6)); }
const out = fadeEdges(norm(M.slice(0, Math.ceil((TOTAL / FPS) * SR)), 0.89));
fs.mkdirSync(path.dirname(OUT), {recursive: true});
const wb = Buffer.alloc(44 + out.length * 2);
wb.write('RIFF', 0); wb.writeUInt32LE(36 + out.length * 2, 4); wb.write('WAVE', 8); wb.write('fmt ', 12); wb.writeUInt32LE(16, 16);
wb.writeUInt16LE(1, 20); wb.writeUInt16LE(1, 22); wb.writeUInt32LE(SR, 24); wb.writeUInt32LE(SR * 2, 28); wb.writeUInt16LE(2, 32); wb.writeUInt16LE(16, 34);
wb.write('data', 36); wb.writeUInt32LE(out.length * 2, 40);
out.forEach((v, i) => wb.writeInt16LE(Math.max(-32768, Math.min(32767, Math.round(v * 32767))), 44 + i * 2));
fs.writeFileSync(OUT, wb);
console.log('wrote', OUT, (out.length / SR).toFixed(2) + 's');
