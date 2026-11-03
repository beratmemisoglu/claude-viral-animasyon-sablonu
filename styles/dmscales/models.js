// dmscales models: the style's own elements (registerElement) and the timing helpers its scenes use.
// The look (research reports visual.md / motion.md): flat white page, Arial italic type centred on one axis, pure red
// keywords, round-capped marker drawings in #1e1e1e, marker-red #e5161c arrows and marks. Everything pops on its word
// (one frame, no transform); nothing idles. Numbers in this file are px at the reference's 1440 x 1080 frame: P() / U map
// them into the engine's frame (16:9: the 1440-wide frame centred in 1920; 9:16: scaled 0.75, centred a little high).
import { THREE, LAYOUT_CHECKS, SHOTS, SETTINGS, css, registerElement, in2d, in3d, group, rect, text, circle, box, sketch, image, IMG, C, DIM, textOn, VERT, cue, rng, E, seg, clamp } from './engine.js';

// ---------- layout: reference px -> engine px ----------
export const U = VERT ? .75 : 1;                                  // scale of the reference composition
export const UV = VERT ? 1.15 : 1;                                // 9:16 spreads positions vertically (sizes keep U)
export const CY = VERT ? 100 : 0;                                 // where the reference frame's centre sits (engine y)
/** P(x, y): a point given in reference px (1440 x 1080, origin top-left, y down) -> engine px (centre origin, y up). */
export const P = (x, y) => [(x - 720) * U, (540 - y) * UV + CY];
export const FONT = 'Arial';                                      // the reference's font (true italic); a system font
export const RED = '#ff0000', MARK = '#e5161c', INK = '#1e1e1e', BLACK = '#000000', GREEN = '#00fc16', GREY = '#525252', YELLOW = '#fcd400';
// GTEXT: the reference's neon green #00fc16 reads at 1.4:1 on white; green TYPE uses #00960d (3.9:1), strokes keep GREEN
export const GTEXT = '#00960d';
// type tiers (visual.md 2.2): hero 97, tracked caps 62, body 62, secondary 48, list 38, note 33, footnote 27
export const T = { hero: 97, caps: 62, body: 62, sub: 48, list: 38, note: 33, foot: 27 };
// type scale: 9:16 is read on a phone, so type keeps 0.9 of its size while the composition scales 0.75
export const TU = VERT ? .9 : 1;
const px = s => Math.max(26, Math.round(s * TU));                 // nothing under 26 px (the footnote tier)

// the look's era (visual.md 1, 2.2): 'hits' = the two most-viewed videos (April): every italic line of 40 px and up in bold
// italic, on a #fcfcfc page; 'later' = regular italic on #ffffff
export const HITS = SETTINGS.era === 'hits', BODY_BOLD = HITS;
if (HITS) { C.bg = '#fcfcfc'; C.bg2 = '#fcfcfc'; }

// ---------- markup: {red words} {g:green words} _underlined_ **bold**, \n = new line ----------
/** parseMarkup(src) -> lines of words; a word is a list of styled segments, so '{travels})' stays one word. */
export function parseMarkup(src) {
  const lines = [[]]; let color = null, under = false, bold = false, word = null;
  const flush = () => { if (word && word.t) lines[lines.length - 1].push(word); word = null; };
  const add = c => {
    word ??= { t: '', segs: [] }; const last = word.segs[word.segs.length - 1];
    if (last && last.color === color && last.under === under && last.bold === bold) last.t += c; else word.segs.push({ t: c, color, under, bold });
    word.t += c;
  };
  for (let i = 0; i < src.length; i++) {
    const c = src[i];
    if (c === '\n') { flush(); lines.push([]); continue; }
    if (c === ' ') { flush(); continue; }
    if (c === '{') { if (src.startsWith('g:', i + 1)) { color = GTEXT; i += 2; } else color = RED; continue; }
    if (c === '}') { color = null; continue; }
    if (c === '_') { under = !under; continue; }
    if (c === '*' && src[i + 1] === '*') { bold = !bold; i++; continue; }
    add(c);
  }
  flush();
  return lines.filter(l => l.length);
}
const fontOf = (sg, size, italic) => `${italic ? 'italic ' : ''}${sg.bold ? 700 : 400} ${size}px ${FONT}, Arimo, "Liberation Sans", sans-serif`;
const _m = new OffscreenCanvas(8, 8).getContext('2d');
function segW(sg, size, italic, track) { _m.font = fontOf(sg, size, italic); _m.letterSpacing = `${track * size}px`; return _m.measureText(sg.t).width; }
// an upright line (tracked caps) still sets its coloured words in italic, as the reference does (visual.md 2.2, H1)
const measure = (w, size, italic, track) => (w.segs ?? [w]).reduce((a, sg) => a + segW(sg, size, italic || !!sg.color, track), 0);

/** say(p, '{trust} is everything', { x, y, size, bold, italic, track, lineH, color, align, indent }): a block of type, one
 *  element per word so words can pop in one at a time (pops()). x, y: the block's centre in engine px (P() for reference
 *  px). align 'center' (every line centred) | 'left' (lines start at x, each next line `indent` px further right). */
export const say = registerElement('say', (p, src, { x = 0, y = 0, size = T.body, bold, italic = true, track = 0, lineH = .97, color = BLACK, align = 'center', indent = 0 } = {}) => {
  bold ??= BODY_BOLD && italic && size >= 40;                       // the look decides when the scene doesn't
  const g = group(in2d(p, 'say'), x, y), sz = px(size), words = [];
  const lines = parseMarkup(String(src)).map(l => l.map(w => ({ ...w, segs: w.segs.map(sg => ({ ...sg, bold: sg.bold || bold })) })));
  const pitch = sz * lineH, top = (lines.length - 1) * pitch / 2;
  const space = measure({ t: ' ' }, sz, italic, track);
  lines.forEach((line, li) => {
    line.forEach(w => {
      const lw = measure(w, sz, italic, track), pad = sz * .3, cw = lw + pad * 2, chh = sz * 1.5, base = sz * 1.08;
      const col = w.segs.map(sg => sg.color).find(Boolean) ?? color;                 // the word's colour, for the checks
      // paint(ctx, ch): the word; ch(i) -> { a, r } per character (alpha, tilt in radians) for the title cascade
      const paint = (ctx, ch) => {
        let cx = pad, ci = 0;
        for (const sg of w.segs) {
          const it = italic || !!sg.color, sw = segW(sg, sz, it, track);
          ctx.font = fontOf(sg, sz, it); ctx.letterSpacing = `${track * sz}px`; ctx.fillStyle = sg.color ?? color; ctx.textBaseline = 'alphabetic';
          if (!ch) ctx.fillText(sg.t, cx, base);
          else { let x = cx; for (const c of sg.t) { const cw2 = segW({ ...sg, t: c }, sz, it, track), { a, r } = ch(ci++);
            if (a > 0) { ctx.save(); ctx.globalAlpha = a; ctx.translate(x + cw2 / 2, base); ctx.rotate(r); ctx.fillText(c, -cw2 / 2, 0); ctx.restore(); } x += cw2; } }
          if (sg.under && (!ch || ch(ci - 1).a >= 1)) ctx.fillRect(cx, base + sz * .21, sw, Math.max(2, sz * .055));   // 0.055 em bar, 0.21 em under the baseline
          cx += sw;
        }
      };
      const m = sketch(g, cw, chh, ctx => paint(ctx, null), { kind: 'text', role: 'text', size: sz, color: col, text: w.t });
      m.userData.redraw = ch => { const tex = m.material.map, cv = tex.image, c2 = cv.getContext('2d');
        c2.setTransform(1, 0, 0, 1, 0, 0); c2.clearRect(0, 0, cv.width, cv.height); c2.scale(cv.width / cw, cv.height / chh); paint(c2, ch); tex.needsUpdate = true; };
      m.userData.chars = [...w.t].length;
      // the checks measure the ink, not the padded canvas: ascender .72 em above the baseline, descender .27 em below
      const yb = chh / 2 - base; m.geometry.boundingBox = new THREE.Box3(new THREE.Vector3(-lw / 2, yb - sz * .27, 0), new THREE.Vector3(lw / 2, yb + sz * .72, 0));
      // the cap-height middle (0.36 em above the baseline) sits on the line's y
      m.position.y = top - li * pitch - (chh / 2 - base) - sz * .36;
      Object.assign(m.userData, { lw, line: li });
      words.push(m);
    });
  });
  const widthOf = (li, n) => { const lw = words.filter((m, k) => m.userData.line === li && k < n); return [lw, lw.reduce((a, m, k) => a + m.userData.lw + (k ? space : 0), 0)]; };
  // centre each line on the words shown so far (the reference re-centres instantly as words pop)
  g.userData.layout = (n = words.length) => {
    lines.forEach((_, li) => {
      const [lw, width] = widthOf(li, n);
      let cx = align === 'left' ? li * indent * U : -width / 2;
      for (const m of lw) { m.position.x = cx + m.userData.lw / 2; cx += m.userData.lw + space; }
    });
  };
  g.userData.layout();
  Object.assign(g.userData, { words, text: String(src), w: Math.max(...lines.map((_, li) => widthOf(li, words.length)[1])), h: lines.length * pitch });
  return g;
});

// ---------- marker drawing helpers (seeded wobble, round caps) ----------
function stroke(ctx, pts, w, color, rnd, amp = .012) {
  if (pts.length < 2) return;
  const L = pts.slice(1).reduce((a, q, i) => a + Math.hypot(q[0] - pts[i][0], q[1] - pts[i][1]), 0) || 1;
  const ph = rnd() * 6.28, f = 2 + rnd() * 1.5, A = L * amp;
  let acc = 0; const q = pts.map((pt, i) => {
    if (i) acc += Math.hypot(pt[0] - pts[i - 1][0], pt[1] - pts[i - 1][1]);
    const s = Math.sin(ph + f * 6.28 * acc / L) * A; return [pt[0] + s * .7, pt[1] + s];
  });
  ctx.strokeStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  ctx.beginPath(); ctx.moveTo(q[0][0], q[0][1]);
  for (let i = 1; i < q.length - 1; i++) ctx.quadraticCurveTo(q[i][0], q[i][1], (q[i][0] + q[i + 1][0]) / 2, (q[i][1] + q[i + 1][1]) / 2);
  ctx.lineTo(q[q.length - 1][0], q[q.length - 1][1]); ctx.stroke();
}
/** an open loop (head, circle-out): ellipse points from a0 over `turn` turns, narrower at the top by `egg`, flatter below */
function loop(cx, cy, rx, ry, { a0 = -1.9, turn = 1.12, egg = 0, flat = 0, n = 48, rot = 0 } = {}) {
  const pts = [], cr = Math.cos(rot), sr = Math.sin(rot);
  for (let i = 0; i <= n; i++) {
    const a = a0 + turn * 6.2832 * i / n, s = Math.sin(a), c = Math.cos(a);
    const dx = rx * c * (1 - egg * Math.max(0, -s)), dy = ry * s * (s > 0 ? 1 - flat * s * s : 1);
    pts.push([cx + dx * cr - dy * sr, cy + dx * sr + dy * cr]);
  }
  return pts;
}
const dot = (ctx, x, y, r, color) => { ctx.fillStyle = color; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.2832); ctx.fill(); };

// ---------- the marker guy (visual.md 5.1): proportions of the full height H ----------
export const FACES = ['neutral', 'smile', 'frown', 'grin', 'worried', 'shock'];
export const POSES = ['stand', 'phone', 'armsup', 'point', 'shrug'];
/** figure(p, { h = 481, face, pose, dir = 1 | -1, x, y, seed }): a marker figure centred on (x, y); h in reference px.
 *  Faces: neutral smile frown grin worried shock. Poses: stand phone armsup point shrug. dir -1 faces left. */
export const figure = registerElement('figure', (p, { h = 481, face = 'neutral', pose = 'stand', dir = 1, x = 0, y = 0, seed = 7 } = {}) => {
  if (!FACES.includes(face)) throw new Error(`figure: face "${face}" is not one of ${FACES.join(' ')}`);
  if (!POSES.includes(pose)) throw new Error(`figure: pose "${pose}" is not one of ${POSES.join(' ')}`);
  const H = h * U, w = H * 1.0, ch = H * 1.06;
  return sketch(in2d(p, 'figure'), w, ch, (ctx) => {
    const r = rng(seed), lw = H * .05, cx = w / 2, top = H * .04;
    const hw = H * .46, hh = H * .43, hcy = top + hh / 2;
    stroke(ctx, loop(cx, hcy, hw / 2, hh / 2, { egg: .16, flat: .12, a0: -1.75, turn: 1.1 }), lw, INK, r, .006);
    const ey = top + hh * .36, ex = cx + dir * hw * .05, er = H * .021, sp = H * .06, my = top + hh * .66, mw = H * .12;
    if (face === 'shock') {
      dot(ctx, ex - sp, ey, er * 1.25, INK); dot(ctx, ex + sp, ey, er * 1.25, INK);
      stroke(ctx, loop(ex, my + H * .01, mw * .3, mw * .38, { turn: 1.05 }), lw * .55, INK, r, .004);
    } else {
      dot(ctx, ex - sp, ey, er, INK); dot(ctx, ex + sp, ey, er, INK);
      if (face === 'grin') {
        ctx.fillStyle = '#ffffff'; ctx.beginPath(); ctx.moveTo(ex - mw * .7, my - H * .02); ctx.quadraticCurveTo(ex, my + H * .11, ex + mw * .7, my - H * .02); ctx.closePath(); ctx.fill();
        stroke(ctx, [[ex - mw * .7, my - H * .02], [ex + mw * .7, my - H * .02]], lw * .5, INK, r, .002);
        stroke(ctx, [[ex - mw * .7, my - H * .02], [ex - mw * .35, my + H * .05], [ex, my + H * .07], [ex + mw * .35, my + H * .05], [ex + mw * .7, my - H * .02]], lw * .5, INK, r, .002);
      } else if (face === 'worried') stroke(ctx, [[ex - mw / 2, my], [ex - mw / 6, my - H * .012], [ex + mw / 6, my + H * .012], [ex + mw / 2, my]], lw * .5, INK, r, .002);
      else { const k = { neutral: 0, smile: -1, frown: 1 }[face]; stroke(ctx, [[ex - mw / 2, my + k * H * .015], [ex, my - k * H * .02], [ex + mw / 2, my + k * H * .015]], lw * .55, INK, r, .002); }
    }
    // torso from the bottom of the head, arms from a shoulder 0.04 H below it, legs an inverted V
    const nx = cx, ny = top + hh * .97, hipY = ny + H * .37, sy = ny + H * .08, aL = H * .28, lg = H * .23;
    stroke(ctx, [[nx, ny], [nx + dir * H * .01, (ny + hipY) / 2], [nx + dir * H * .015, hipY]], lw, INK, r, .004);
    const arm = (deg, len = aL) => [nx + Math.sin(deg * Math.PI / 180) * len, sy + Math.cos(deg * Math.PI / 180) * len];
    if (pose === 'armsup') for (const s of [-1, 1]) stroke(ctx, [[nx, sy], [nx + s * H * .19, sy - H * .02], [nx + s * H * .3, sy - H * .27]], lw, INK, r, .004);   // elbows out, hands up beside the head (never through it)
    else if (pose === 'shrug') { stroke(ctx, [[nx, sy], arm(-80, aL * .55), arm(-130, aL)], lw, INK, r, .004); stroke(ctx, [[nx, sy], arm(80, aL * .55), arm(130, aL)], lw, INK, r, .004); }
    else if (pose === 'point') { stroke(ctx, [[nx, sy], arm(-dir * 30)], lw, INK, r, .004); stroke(ctx, [[nx, sy], [nx + dir * aL * 1.1, sy - H * .03]], lw, INK, r, .004); }
    else if (pose === 'phone') {
      stroke(ctx, [[nx, sy], arm(-dir * 25)], lw, INK, r, .004);
      const px0 = nx + dir * H * .2, py0 = sy + H * .02, pw = H * .2, ph = H * .34;
      stroke(ctx, [[nx, sy], [nx + dir * H * .09, sy + H * .2], [px0 - dir * pw * .2, py0 + ph * .6]], lw, INK, r, .004);
      ctx.save(); ctx.translate(px0, py0 + ph / 2); ctx.rotate(dir * .22);
      ctx.fillStyle = '#ffffff'; ctx.lineWidth = lw * .45; ctx.strokeStyle = INK; ctx.beginPath(); ctx.roundRect(-pw / 2, -ph / 2, pw, ph, pw * .18); ctx.fill(); ctx.stroke(); ctx.restore();
    } else { stroke(ctx, [[nx, sy], arm(-24)], lw, INK, r, .004); stroke(ctx, [[nx, sy], arm(24)], lw, INK, r, .004); }
    const hx = nx + dir * H * .015;
    stroke(ctx, [[hx, hipY], [hx - H * .1, hipY + lg * .93]], lw, INK, r, .004);
    stroke(ctx, [[hx, hipY], [hx + H * .1, hipY + lg * .93]], lw, INK, r, .004);
  }, { x, y, kind: 'figure', role: 'form', face, pose });
});

// ---------- crowd = audience (visual.md 5.3): ~20 overlapping heads with shoulder hooks ----------
/** crowd(p, { w = 780, h = 515, n = 20, x, y, seed }): an audience cluster (reference px). */
export const crowd = registerElement('crowd', (p, { w = 780, h = 515, n = 20, x = 0, y = 0, seed = 3 } = {}) => {
  const W2 = w * U, H2 = h * U;
  return sketch(in2d(p, 'crowd'), W2, H2, (ctx) => {
    const r = rng(seed), heads = [], rows = 4, per = Math.ceil(n / rows), lw = 15 * U, Hc = H2 * (n >= 12 ? .84 : 1);
    for (let i = 0; i < n; i++) {
      const row = Math.floor(i / per), k = (i % per + .5) / per, d = (58 + r() * 78 + row * 8) * U;
      const hk = 1.6 + r() * .4;                                     // hook length (x R): 0.8-1.0 of the diameter
      const xx = W2 * (.08 + .84 * k + (r() - .5) * .07 + (row % 2 ? .03 : -.02)), yy = Hc * (.13 + row * .19) + (r() - .5) * .07 * Hc;
      heads.push({ x: clamp(xx, d / 2 + lw, W2 - d / 2 - lw), y: Math.max(d / 2 + lw, Math.min(yy, Hc - d / 2 * (hk + .3) - lw)), d, hk });
    }
    if (n >= 12) for (const [fx0, s0] of [[.7, 0], [.85, 1]]) {      // two smaller heads apart, bottom right
      const d = (52 + r() * 12) * U; heads.push({ x: W2 * fx0, y: H2 - d / 2 * 2.3 - lw - s0 * 6 * U, d, hk: 1.9 });
    }
    heads.sort((a, b) => (a.y + a.d / 2 * a.hk) - (b.y + b.d / 2 * b.hk));   // lower hooks last: no cap peeks out under a body
    for (const hd of heads) {
      const R = hd.d / 2, rx = R * (.92 + r() * .16), ry = R * (.84 + r() * .16), rot = (r() - .5) * .5, hk = hd.hk;
      ctx.fillStyle = '#ffffff';
      ctx.save(); ctx.translate(hd.x, hd.y); ctx.rotate(rot); ctx.beginPath(); ctx.ellipse(0, 0, rx + lw / 2, ry + lw / 2, 0, 0, 6.2832); ctx.fill(); ctx.restore();
      // the body hides what is behind it only down to the shoulder hooks' ends, so no straight white edge shows
      const fb = hd.y + R * hk + lw * .6, fx = R * 1.15 + lw * .5;   // down to (and around) the round caps of its own hooks
      ctx.beginPath(); ctx.moveTo(hd.x - fx, fb); ctx.quadraticCurveTo(hd.x - R * 1.05, hd.y + R * 1.1, hd.x - R * .5, hd.y + R * .8);
      ctx.lineTo(hd.x + R * .5, hd.y + R * .8); ctx.quadraticCurveTo(hd.x + R * 1.05, hd.y + R * 1.1, hd.x + fx, fb); ctx.closePath(); ctx.fill();
      stroke(ctx, loop(hd.x, hd.y, rx, ry, { a0: -2 + r(), turn: 1.08, rot }), lw, INK, r, .014);
      const hl = R * hk, curl = R * .15;                             // each hook curls out a little at its end
      stroke(ctx, [[hd.x - R * .55, hd.y + R * .85], [hd.x - R * 1.0, hd.y + R * 1.3], [hd.x - R * 1.12, hd.y + hl - curl], [hd.x - R * 1.22, hd.y + hl]], lw, INK, r, .006);
      stroke(ctx, [[hd.x + R * .55, hd.y + R * .85], [hd.x + R * 1.0, hd.y + R * 1.3], [hd.x + R * 1.12, hd.y + hl - curl], [hd.x + R * 1.22, hd.y + hl]], lw, INK, r, .006);
    }
  }, { x, y, kind: 'crowd', role: 'form' });
});

// ---------- bust = a creator (visual.md 5.2): squashed-oval head, arch body, red play wedge ----------
/** bust(p, { s = 1, x, y, seed }): one creator, ~170 x 190 reference px at s = 1. */
export const bust = registerElement('bust', (p, { s = 1, x = 0, y = 0, seed = 5 } = {}) => {
  const k = s * U, w = 170 * k, h = 190 * k;
  return sketch(in2d(p, 'bust'), w, h, (ctx) => {
    const r = rng(seed), lw = 23 * k, cx = w / 2;
    stroke(ctx, loop(cx, 50 * k, 42 * k, 30 * k, { turn: 1.08 }), lw, INK, r, .006);
    stroke(ctx, [[cx - 68 * k, 176 * k], [cx - 52 * k, 120 * k], [cx, 100 * k], [cx + 52 * k, 120 * k], [cx + 68 * k, 176 * k]], lw, INK, r, .004);
    ctx.fillStyle = MARK; ctx.strokeStyle = MARK; ctx.lineJoin = 'round'; ctx.lineWidth = 10 * k;
    ctx.beginPath(); ctx.moveTo(cx - 20 * k, 124 * k); ctx.lineTo(cx + 26 * k, 143 * k); ctx.lineTo(cx - 20 * k, 161 * k); ctx.closePath(); ctx.fill(); ctx.stroke();
  }, { x, y, kind: 'bust', role: 'form' });
});

// ---------- marks (visual.md 5.4): marker arrow, circle-out, X-out, connector ----------
/** mark(p, 'arrow' | 'circle' | 'x' | 'down', { w, h, x, y, bend, flip, mirror, color, lw, seed }): a hand-drawn mark in a
 *  w x h box (reference px). arrow: bottom-left to top-right (flip: top-left to bottom-right; mirror: right to left);
 *  circle: a loose ellipse around the box; x: two crossing strokes; down: a small straight connector. */
export const mark = registerElement('mark', (p, kind = 'arrow', { w = 230, h = 120, x = 0, y = 0, bend = .18, flip = 0, mirror = 0, color = MARK, lw, seed = 9 } = {}) => {
  const W2 = w * U, H2 = h * U, o = 40 * U, sw = (lw ?? { arrow: 22, circle: 9, x: 13, down: 7 }[kind]) * U;
  return sketch(in2d(p, 'mark'), W2 + o * 2, H2 + o * 2, (ctx) => {
    const r = rng(seed);
    if (kind === 'circle') { stroke(ctx, loop(o + W2 / 2, o + H2 / 2, W2 / 2, H2 / 2, { a0: -2.6, turn: 1.12 }), sw, color, r, .004); return; }
    if (kind === 'x') { stroke(ctx, [[o, o], [o + W2, o + H2]], sw, color, r, .006); stroke(ctx, [[o + W2, o], [o, o + H2]], sw, color, r, .006); return; }
    let a = flip ? [o, o] : [o, o + H2], b = flip ? [o + W2, o + H2] : [o + W2, o];
    if (kind === 'down') { a = [o + W2 / 2, o]; b = [o + W2 / 2, o + H2]; }
    if (mirror) { a = [2 * o + W2 - a[0], a[1]]; b = [2 * o + W2 - b[0], b[1]]; }
    const L = Math.hypot(b[0] - a[0], b[1] - a[1]), bb = kind === 'down' ? 0 : bend * (mirror ? -1 : 1);
    const c = [(a[0] + b[0]) / 2 - (b[1] - a[1]) / L * L * bb, (a[1] + b[1]) / 2 + (b[0] - a[0]) / L * L * bb];
    const pts = []; for (let i = 0; i <= 24; i++) { const t = i / 24; pts.push([(1 - t) ** 2 * a[0] + 2 * (1 - t) * t * c[0] + t * t * b[0], (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * c[1] + t * t * b[1]]); }
    stroke(ctx, pts, sw, color, r, .004);
    const tx = b[0] - pts[21][0], ty = b[1] - pts[21][1], tl = Math.hypot(tx, ty) || 1, ux = tx / tl, uy = ty / tl;
    const bl = Math.min(L * .34, (kind === 'down' ? 16 : 80) * U);
    const barb = ang => [b[0] - bl * (ux * Math.cos(ang) - uy * Math.sin(ang)), b[1] - bl * (ux * Math.sin(ang) + uy * Math.cos(ang))];
    stroke(ctx, [barb(.7), b, barb(-.7)], sw, color, r, .002);
  }, { x, y, kind: 'mark', role: 'detail', mark: kind });
});

/** shotImage(p, key, { w = 870, x, y }): a real picture (project.json "images") dropped flat: no border, no shadow, square
 *  corners, w in reference px. Real evidence only: never a drawn stand-in for a screenshot. */
export const shotImage = registerElement('shotImage', (p, key, { w = 870, x = 0, y = 0 } = {}) => image(in2d(p, 'shotImage'), key, { w: w * U, x, y }));

// ---------- timing helpers: hard pops on the spoken word (motion.md 1a, 5) ----------
/** note(S, t, el): something new appears at t (the HOLD check measures the gaps between these). With el, the entrance is
 *  also registered with the engine (S.anims, kind 'none': it only hides el before t; our ticks run after it and own the
 *  motion), so the layout check waits for a shot to build up and samples a frame after every entrance. */
export const note = (S, t, el) => {
  if (!Number.isFinite(t)) return; (S._dmEv ??= []).push(t);
  if (el?.isObject3D && S.anims && t > S.t0 + 1e-3) S.anims.push({ obj: el, at: t, in: 'none', dur: 0, outDur: 0, pos: el.position.clone(), scl: el.scale.clone(), dist: 0, u: 1, dm: true });
};
/** at(S, el, t0, { out, fade }): el appears in one frame at t0 (fade: seconds of linear fade-in instead) and leaves at out. */
export function at(S, el, t0, { out = Infinity, fade = 0 } = {}) {
  note(S, t0, el);
  const mats = []; el.traverse(o => { if (o.material) { o.material.transparent = true; mats.push([o.material, o.material.opacity]); } });
  S.tick(t => { el.visible = t >= t0 - 1e-4 && t < out; if (fade) { const k = clamp((t - t0) / fade, 0, 1); for (const [m, o] of mats) m.opacity = o * k; } });
  return el;
}
/** pops(S, sayEl, times, { lead }): word i of a say() block appears at times[i] (one number: all at once; fewer times than
 *  words: the rest come with the last). lead: the first word comes in with the heading settle (0.13 s fade, 40 px rise and a
 *  3 deg tilt settling over 0.43 s, motion.md 1b). Lines re-centre as words arrive. */
export function pops(S, el, times, { lead = false, order = 'ltr' } = {}) {
  const ws = el.userData.words, ts = Array.isArray(times) ? times : [times];
  const tw = ws.map((_, i) => ts[Math.min(i, ts.length - 1)]), base = ws.map(m => m.position.y);
  tw.forEach((t, i) => note(S, t, i ? null : el));
  ws.forEach(m => { m.material.transparent = true; });
  // the title cascade (motion.md 1b): the words that arrive with the first one type in per character: the starts spread
  // over at most 6 frames (2 frames apart for a short word), each character fading in over 4 frames from a 6 deg tilt
  // (order ltr | rtl | center), so the title is in within ~10 frames; the line rises 40 px and levels over 0.43 s
  const lw = lead ? ws.filter((_, i) => tw[i] === tw[0]) : [], n = lw.reduce((a, m) => a + m.userData.chars, 0);
  const spread = Math.min(2 * Math.max(0, n - 1), 6) / 60, fade = 4 / 60, end = tw[0] + spread + fade, last = Math.max(1, n - 1);
  const slot = i => (order === 'rtl' ? n - 1 - i : order === 'center' ? Math.abs(i - (n - 1) / 2) * 2 : i) / last;
  let painted = -1;
  S.tick(t => {
    el.userData.layout(tw.filter(x => t >= x - 1e-4).length);
    ws.forEach((m, i) => { m.visible = t >= tw[i] - 1e-4; });
    if (!lw.length) return;
    const k = E.outCubic(seg(t, tw[0], tw[0] + .43));
    lw.forEach(m => { const i = ws.indexOf(m); m.position.y = base[i] - 40 * U * (1 - k); m.rotation.z = .03 * (1 - k); });
    const f = t >= end ? -2 : Math.round(clamp(t, tw[0], end) * 60); if (f === painted) return; painted = f;
    let off = 0;
    for (const m of lw) { const o = off; m.userData.redraw(t >= end ? null : ci => { const u = clamp((t - tw[0] - slot(o + ci) * spread) / fade, 0, 1); return { a: u, r: .1 * (1 - u) }; }); off += m.userData.chars; }
  });
  return el;
}
/** A word lowercased the narration language's way (the host sets __CZ_LANG): Turkish 'NASIL' -> 'nasıl', 'İLK' -> 'ilk',
 *  so a caps line still finds its spoken word (cue() lowercases the English way, I -> i). */
const lower = s => { try { return s.toLocaleLowerCase(globalThis.__CZ_LANG || 'en'); } catch { return s.toLowerCase(); } };
/** words(src, near): the narration time of every word of a markup line, searched from `near` seconds on (punctuation and
 *  markup ignored). Use with pops() for word-by-word builds. */
export function words(src, near) {
  const out = []; let t = near;
  for (const l of parseMarkup(src)) for (const w of l) { const clean = lower(w.t.replace(/[^\p{L}\p{N}']/gu, '')); if (clean) t = cue(clean, t); out.push(t); }
  return out;
}
/** heading(S, '{TRUST} SCORE:', items, { at, size, itemSize, noteSize }): the list build (motion.md 1e). The header arrives
 *  alone at the centre at `at`, slides up linearly in 9 frames just before the first item, then each item pops on its
 *  time below it, top-anchored. items: [{ src, at, note }] (note: a smaller parenthetical under the item). */
export function heading(S, src, items = [], { at: t0, size = 90, itemSize = 58, noteSize = 32, gap = 60, bold = false, shrink = false } = {}) {   // the header is regular in both eras (N-q 20.5 s, fS8 17.6 s)
  if (shrink) return headingShrink(S, src, items, { t0, size, itemSize, noteSize, gap, bold });
  S.sparse = true;                                                // a list card: the white is the point
  const [hx, hy] = P(720, 540), head = say(null, src, { x: hx, y: hy, size, bold });
  const block = it => itemSize * 1.05 + (it.note ? noteSize * 1.25 + 8 : 0);
  const total = size + gap + items.reduce((a, it) => a + block(it) + 26, 0) - (items.length ? 26 : 0);
  const topY = 540 - total / 2, rise = (540 - (topY + size / 2)) * UV;
  pops(S, head, t0, { lead: true, order: 'rtl' });
  const hy0 = head.position.y, first = items[0]?.at ?? Infinity, tUp = first - .2 - .15;
  if (items.length) S.tick(t => { head.position.y = hy0 + rise * clamp((t - tUp) / .15, 0, 1); });
  let yy = topY + size + gap;
  const out = items.map(it => {
    const [ix, iy] = P(720, yy + itemSize * .55), el = say(null, it.src, { x: ix, y: iy, size: itemSize, bold: true });
    pops(S, el, it.at); let n = null;
    if (it.note) { const [nx, ny] = P(720, yy + itemSize * 1.05 + 8 + noteSize * .6); n = say(null, it.note, { x: nx, y: ny, size: noteSize }); pops(S, n, it.at); }
    yy += block(it) + 26; return n ? [el, n] : el;
  });
  return { head, items: out };
}

// ---------- media: real screenshots and real video clips (the member's files) ----------
// Files come in with skill/scripts/add_media.py: a picture becomes project.json images[name]; a video becomes its frames
// images[name_0 .. name_(n-1)] at a fixed fps plus an entry in assets/media/media.json (n, fps, w, h, seconds).
// give w or h (the other follows the picture's own shape); both = that exact box; neither = 870 wide
const fitBox = (im, w, h) => { const ar = (im?.naturalWidth || 16) / (im?.naturalHeight || 9); if (!w && !h) w = 870 * U; return w && h ? [w, h] : w ? [w, w / ar] : [h * ar, h]; };
function drawPic(ctx, im, w, h, r) {
  ctx.save(); if (r) { ctx.beginPath(); ctx.roundRect(0, 0, w, h, r); ctx.clip(); }
  if (im) ctx.drawImage(im, 0, 0, w, h); else { ctx.fillStyle = '#d9d9d9'; ctx.fillRect(0, 0, w, h); }
  ctx.restore();
}
/** media(p, key, { w = 870, h, x, y, r = 0 }): a real picture dropped flat (visual.md 6): no border, no shadow; r = corner
 *  radius (0 for screenshots, 12 for a YouTube card, 28 for a phone recording). w / h in reference px. Never a drawn
 *  stand-in for a screenshot: a missing key shows grey and the check warns. */
export const media = registerElement('media', (p, key, { w, h, x = 0, y = 0, r = 0 } = {}) => {
  const im = IMG[key]; if (!im) console.warn(`media missing: "${key}" (run skill/scripts/add_media.py)`);
  const [bw, bh] = fitBox(im, w && w * U, h && h * U);
  return sketch(in2d(p, 'media'), bw, bh, ctx => drawPic(ctx, im, bw, bh, r * U), { x, y, kind: 'media', role: 'form', key, missing: im ? undefined : key });
});
/** clip(S, name, { n, fps = 12, w, h, x, y, r, at, from = 0, loop = true }): a real video clip (its frames name_0..) that
 *  plays from `at` (frame `from` first), in sync with the timeline so the export matches the preview. Holds the first
 *  frame before `at`. n / fps: from assets/media/media.json. */
export function clip(S, name, { n, fps = 12, w, h, x = 0, y = 0, r = 0, at: t0 = S.t0, from = 0, loop = true } = {}) {
  const first = IMG[`${name}_0`]; if (!first) console.warn(`clip missing: "${name}" (run skill/scripts/add_media.py)`);
  n ??= Object.keys(IMG).filter(k => k.startsWith(name + '_') && /^\d+$/.test(k.slice(name.length + 1))).length;
  const [bw, bh] = fitBox(first, w && w * U, h && h * U), rr = r * U;
  const m = sketch(in2d(null, 'clip'), bw, bh, ctx => drawPic(ctx, first, bw, bh, rr), { x, y, kind: 'clip', role: 'form', key: name, frames: n });
  const tex = m.material.map, cv = tex.image, ctx = cv.getContext('2d'); let shown = 0;
  note(S, t0); note(S, t0 + (n || 0) / fps);   // a playing clip is movement for its whole length
  S.tick(t => {
    let f = Math.floor(Math.max(0, t - t0) * fps) + from; f = loop ? f % Math.max(1, n) : Math.min(f, n - 1);
    if (f === shown) return; shown = f; const im = IMG[`${name}_${f}`]; if (!im) return;
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height); ctx.scale(cv.width / bw, cv.height / bh);
    drawPic(ctx, im, bw, bh, rr); tex.needsUpdate = true;
  });
  return m;
}

// ---------- motion (motion.md 2): one controller per element, every move a pure function of t ----------
const FR = 1 / 60;                                                // the reference is 60 fps; durations below are its frames
function fxOf(S, el) {
  if (el.userData.fx) return el.userData.fx;
  const base = { x: el.position.x, y: el.position.y, s: el.scale.x, r: el.rotation.z }, mats = [];
  el.traverse(o => { if (o.material) { o.material.transparent = true; mats.push([o.material, o.material.opacity ?? 1]); } });
  const fx = el.userData.fx = { base, ops: [] };
  S.tick(t => {
    let x = base.x, y = base.y, s = base.s, r = base.r, o = 1, vis = true;
    for (const op of fx.ops) { const d = op(t); if (!d) continue; x += d.dx ?? 0; y += d.dy ?? 0; s *= d.s ?? 1; r += d.r ?? 0; o *= d.o ?? 1; if (d.vis === false) vis = false; }
    el.position.x = x; el.position.y = y; el.scale.set(s, s, 1); el.rotation.z = r; el.visible = vis && o > .001;
    for (const [m, o0] of mats) m.opacity = o0 * o;
  });
  return fx;
}
const EASE = { linear: k => k, out: E.outCubic, in: k => k * k, inOut: E.inOutCubic };
/** enter(S, el, t0, kind = 'pop', { frames, from }): how a thing arrives (measured on the reference, 60 fps frames):
 *  pop 1 (the default: text, screenshots, icons) | fade 17 linear | drop 10 from the top edge, ease-out | rise 10 from below |
 *  left / right 14 from that side with a fade | scale 15 from 0.61, ease-out (crowds) | elastic 24 with one overshoot
 *  (figures) | wipe 15 (marker arrows: a quick fade-in; the stroke itself is drawn whole). Before t0 the element is hidden. */
export function enter(S, el, t0, kind = 'pop', { frames, from } = {}) {
  note(S, t0, el);
  const fx = fxOf(S, el), F = (frames ?? { pop: 1, fade: 17, drop: 10, rise: 10, left: 14, right: 14, scale: 15, elastic: 24, wipe: 15 }[kind] ?? 1) * FR;
  const k = t => clamp((t - t0) / F, 0, 1), dist = (VERT ? 1100 : 700);
  fx.ops.push(t => {
    if (t < t0 - 1e-4) return { vis: false };
    const e = E.outCubic(k(t));
    if (kind === 'fade' || kind === 'wipe') return { o: kind === 'wipe' ? E.outCubic(k(t)) : k(t) };
    if (kind === 'drop') return { dy: (1 - e) * dist };
    if (kind === 'rise') return { dy: -(1 - e) * 67 * U, o: e };
    if (kind === 'left' || kind === 'right') return { dx: (kind === 'left' ? -1 : 1) * (1 - e) * dist, o: Math.min(1, k(t) * 2) };
    if (kind === 'scale') return { s: (from ?? .61) + (1 - (from ?? .61)) * e };
    if (kind === 'elastic') { const u = k(t), keys = [[0, 0], [8 / 24, .97], [14 / 24, .84], [19 / 24, 1.0], [1, 1]];
      let i = 0; while (i < keys.length - 2 && u > keys[i + 1][0]) i++; const [a, b] = [keys[i], keys[i + 1]];
      return { s: Math.max(1e-3, a[1] + (b[1] - a[1]) * E.outCubic(clamp((u - a[0]) / (b[0] - a[0]), 0, 1))) }; }
    return null;
  });
  return el;
}
/** leave(S, el, t0, kind = 'cut', { frames }): cut (gone in one frame) | fade 11 linear | down 15, ease-in (slides off). */
export function leave(S, el, t0, kind = 'cut', { frames } = {}) {
  const fx = fxOf(S, el), F = (frames ?? { cut: 1, fade: 11, down: 15 }[kind] ?? 1) * FR, k = t => clamp((t - t0) / F, 0, 1);
  fx.ops.push(t => t < t0 ? null : kind === 'fade' ? { o: 1 - k(t) } : kind === 'down' ? { dy: -k(t) * k(t) * (VERT ? 1100 : 700), vis: k(t) < 1 } : { vis: false });
  return el;
}
/** move(S, el, t0, { x, y, s, frames = 14, ease = 'out' }): a later move to engine px (x, y) and scale s: the push-aside
 *  when a second thing joins (14 frames, scale .83), the clip that shrinks to the top centre (6 frames), the header that
 *  slides up before its list (9 frames, ease 'linear'). */
export function move(S, el, t0, { x, y, s, frames = 14, ease = 'out' } = {}) {
  note(S, t0);
  const fx = fxOf(S, el), F = frames * FR, f = EASE[ease] ?? EASE.out;
  fx.ops.push(t => { if (t < t0) return null; const e = f(clamp((t - t0) / F, 0, 1));
    return { dx: x == null ? 0 : (x - fx.base.x) * e, dy: y == null ? 0 : (y - fx.base.y) * e, s: s == null ? 1 : 1 + (s - 1) * e }; });
  return el;
}
/** stack(S, keys, times, { w = 760, x, y, step = [70, -90] }): screenshots piled one per beat (motion.md 2, N-q 45 s): each
 *  pops in on its time, offset diagonally on top of the last. x, y: the first one's centre (engine px). Returns the pictures. */
export function stack(S, keys, times, { w = 760, x = 0, y = 0, step = [70, -90] } = {}) {
  const n = keys.length, ox = -step[0] * U * (n - 1) / 2, oy = -step[1] * U * (n - 1) / 2;
  const pics = keys.map((k, i) => enter(S, media(null, k, { w, x: x + ox + step[0] * U * i, y: y + oy + step[1] * U * i }), times[i] ?? times[times.length - 1]));
  pics.forEach(m => { m.userData.over = pics.filter(o => o !== m); });   // the pile overlaps on purpose
  return pics;
}

// ---------- more of the reference's scenes (visual.md 8, research/dmscales/work/ref2) ----------
/** live(S, p, w, h, draw, { t0, dur, ease, ...opts }): a sketch drawn progressively: draw(ctx, w, h, k) with k 0..1 from t0
 *  over dur seconds (curves, the growth line). Before t0 it is hidden. */
export function live(S, p, w, h, draw, { t0 = S.t0, dur = 1.5, ease = 'out', show = t0, ...opts } = {}) {
  note(S, t0); note(S, t0 + dur);
  const m = sketch(p, w, h, (ctx, ww, hh) => draw(ctx, ww, hh, 1), opts), tex = m.material.map, cv = tex.image, ctx = cv.getContext('2d');
  let last = -1; const f = EASE[ease] ?? EASE.out;
  S.tick(t => {
    m.visible = t >= show - 1e-4; const k = Math.round(f(clamp((t - t0) / Math.max(1e-3, dur), 0, 1)) * 200) / 200;
    if (k === last || !m.visible) return; last = k;
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height); ctx.scale(cv.width / w, cv.height / h); draw(ctx, w, h, k); tex.needsUpdate = true;
  });
  return m;
}
const partial = (pts, k) => {                                      // the first k (0..1) of a polyline, by length
  if (k >= 1) return pts; const L = []; let tot = 0; for (let i = 1; i < pts.length; i++) { tot += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); L.push(tot); }
  const want = tot * k, out = [pts[0]];
  for (let i = 1; i < pts.length; i++) { if (L[i - 1] <= want) { out.push(pts[i]); continue; } const a = i > 1 ? L[i - 2] : 0, u = (want - a) / (L[i - 1] - a); out.push([pts[i - 1][0] + (pts[i][0] - pts[i - 1][0]) * u, pts[i - 1][1] + (pts[i][1] - pts[i - 1][1]) * u]); break; }
  return out;
};
const xy2 = ([x, y]) => ({ x, y });

/** columns(S, header, left, right, { at, times, foot }): T13, the two-column inventory: an underlined header (74 px,
 *  markup), an optional footnote, then two left-aligned bold 38 px columns of "-items" (times: one per item, left then
 *  right; or everything at `at`). 9:16 stacks the columns. */
export function columns(S, header, left, right, { at: t0, times, foot, size = 38 } = {}) {
  const st = {}, n = left.length + right.length, ts = times ?? Array(n).fill(t0);
  st.head = enter(S, say(null, header, { size: 74, ...xy2(P(720, VERT ? 60 : 285)) }), t0);
  if (foot) st.foot = enter(S, say(null, foot, { size: T.foot, ...xy2(P(720, VERT ? 130 : 342)) }), t0);
  const pitch = VERT ? 44 : 40, top = VERT ? 210 : 400;
  st.items = [];
  [left, right].forEach((col, ci) => col.forEach((src, i) => {
    const [x, y] = VERT ? P(300, top + (ci * (left.length + .6) + i) * pitch) : P(ci ? 770 : 248, top + i * pitch);
    st.items.push(enter(S, say(null, src, { size, bold: true, align: 'left', x, y }), ts[ci ? left.length + i : i]));
  }));
  return st;
}

/** tagBox(p, 'Viewer', { x, y, size = 46 }): the dark label plate of the compare cards (white upright type). */
export const tagBox = registerElement('tagBox', (p, str, { x = 0, y = 0, size = 46 } = {}) => {
  const sz = px(size), f = `400 ${sz}px ${FONT}, Arimo, sans-serif`; _m.font = f; _m.letterSpacing = '0px';
  const w = _m.measureText(str).width + sz * .9, h = sz * 1.6, g = group(in2d(p, 'tagBox'), x, y);
  rect(g, w, h, '#232323');
  sketch(g, w, h, ctx => { ctx.font = f; ctx.fillStyle = '#ffffff'; ctx.textBaseline = 'middle'; ctx.textAlign = 'center'; ctx.fillText(str, w / 2, h / 2 + sz * .04); },
    { kind: 'text', role: 'text', size: sz, color: '#ffffff', text: str });
  Object.assign(g.userData, { bg: '#232323', w, h, text: str }); return g;
});
/** compare(S, [{ label: 'Viewer', items: ['- loves {animals}', ...] }, { label: 'Creator', items }], { at, times }):
 *  side-by-side cards (N-q 42 s): a dark label, bullets under it popping on their times. 9:16 stacks them. */
export function compare(S, cards, { at: t0, times } = {}) {
  const st = { labels: [], items: [] }, all = cards.reduce((a, c) => a + c.items.length, 0), ts = times ?? Array(all).fill(t0); let k = 0;
  cards.forEach((c, ci) => {
    const cx = VERT ? 720 : (cards.length === 1 ? 720 : 400 + ci * 640), cy0 = VERT ? 120 + ci * 560 : 300;
    st.labels.push(enter(S, tagBox(null, c.label, xy2(P(cx, cy0))), c.at ?? t0));
    c.items.forEach((src, i) => { st.items.push(enter(S, say(null, src, { size: 44, bold: true, ...xy2(P(cx, cy0 + 110 + i * 56)) }), ts[k++])); });
  });
  return st;
}

/** cloud(p, 'a niche is the content you make', { w = 420, h = 300, x, y, tail = 'left' }): a thought cloud with three
 *  trailing circles toward the thinker and a small quoted line inside (EQUn6 16 s). X it out with mark(null, 'x', ...). */
export const cloud = registerElement('cloud', (p, str, { w = 420, h = 300, x = 0, y = 0, tail = 'left', seed = 4, size = 30 } = {}) => {
  const W2 = w * U, H2 = h * U, pad = 70 * U;
  return sketch(in2d(p, 'cloud'), W2 + pad * 2, H2 + pad * 1.2, ctx => {
    const r = rng(seed), lw = 9 * U, cx = pad + W2 / 2, cy = pad * .9 + H2 / 2, bumps = 11, pts = [];
    for (let i = 0; i <= bumps * 8; i++) { const a = i / (bumps * 8) * 6.2832, b = Math.abs(Math.sin(a * bumps / 2)) * .09 + .91; pts.push([cx + Math.cos(a) * W2 / 2 * b, cy + Math.sin(a) * H2 / 2 * b]); }
    ctx.fillStyle = '#ffffff'; ctx.beginPath(); pts.forEach(([a, b], i) => i ? ctx.lineTo(a, b) : ctx.moveTo(a, b)); ctx.fill();
    stroke(ctx, pts, lw, INK, r, .002);
    const sx = tail === 'left' ? -1 : 1;
    [[.55, .05, 22], [.75, -.15, 17], [.93, -.32, 12]].forEach(([d, dy, rad]) => stroke(ctx, loop(cx + sx * W2 / 2 * d, pad * .9 + dy * pad * 1.4, rad * U, rad * U, { turn: 1.05 }), lw * .8, INK, r, .004));
    const sz = Math.max(26, size * TU); ctx.font = `400 ${sz}px ${FONT}, Arimo, sans-serif`; ctx.fillStyle = BLACK; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    const words = `“${str}”`.split(' '), lines = []; let cur = '';
    for (const wd of words) { const nx = cur ? cur + ' ' + wd : wd; if (cur && ctx.measureText(nx).width > W2 * .7) { lines.push(cur); cur = wd; } else cur = nx; } lines.push(cur);
    lines.forEach((l, i) => ctx.fillText(l, cx, cy + (i - (lines.length - 1) / 2) * sz * 1.15));
  }, { x, y, kind: 'cloud', role: 'form', text: String(str), size: Math.max(26, size * TU) });
});

const CURVES = {                                                  // explanatory shapes, x 0..1 -> y 0..1 (1 = top)
  bad: x => .04 + .92 * Math.exp(-x * 7) + .06 * (1 - x),         // falls off a cliff at the start
  good: x => .95 - .25 * x - .04 * Math.sin(x * 9) * (1 - x),     // stays high
  drop: x => x < .55 ? .85 - .1 * x : .25 - .05 * x,              // a sudden drop in the middle
  rise: x => .08 + .82 * Math.pow(x, 1.6),                        // grows
  flat: x => .5 + .02 * Math.sin(x * 11),
};
/** curve(S, { shape = 'bad' | 'good' | 'drop' | 'rise' | 'flat', w = 560, h = 320, x, y, at, dur = 1.2, top, bottom,
 *  color }): a hand-drawn explanatory chart (an L of axes, 100% / 0% marks) whose line draws on (-fS8 3:24). A SHAPE to
 *  explain an idea, never data: the member's real numbers come from their screenshot. */
export function curve(S, { shape = 'bad', w = 560, h = 320, x = 0, y = 0, at: t0 = S.t0, dur = 1.2, top = '100%', bottom = '0%', color = '#2f9de8' } = {}) {
  const W2 = w * U, H2 = h * U, ox = 100 * U, oy = 25 * U, f = CURVES[shape] ?? CURVES.bad;
  const pts = Array.from({ length: 60 }, (_, i) => [ox + 16 * U + (W2 - 24 * U) * i / 59, oy + 8 * U + (H2 - 16 * U) * (1 - f(i / 59))]);
  return live(S, null, W2 + ox + 20 * U, H2 + oy + 30 * U, (ctx, ww, hh, k) => {
    stroke(ctx, [[ox, oy], [ox, oy + H2]], 9 * U, INK, rng(11), .002);                 // a sharp L: two strokes, never one
    stroke(ctx, [[ox, oy + H2], [ox + W2, oy + H2 + 4 * U]], 9 * U, INK, rng(13), .002);
    ctx.font = `400 ${Math.max(26, 32 * TU)}px "Segoe Print", "Comic Sans MS", ${FONT}`; ctx.fillStyle = INK; ctx.textBaseline = 'middle'; ctx.textAlign = 'right';
    ctx.fillText(top, ox - 14 * U, oy + 10 * U); ctx.fillText(bottom, ox - 14 * U, oy + H2 - 8 * U);
    if (k > 0) stroke(ctx, partial(pts, k), 7 * U, color, rng(12), .001);
  }, { t0, dur, show: S.t0, x, y, kind: 'curve', role: 'form', shape });    // the axes come with the cut, the line on `at`
}
/** growth(S, { at, dur = 1.5, w = 1440, h = 700, x, y }): the neon-green zig-zag growth line from the bottom left, drawn
 *  on (VQ 134 s). Build it first so cards built after it sit on top. */
export function growth(S, { at: t0 = S.t0, dur = 1.5, w = 1440, h = 700, x = 0, y = 0, seed = 2 } = {}) {
  const W2 = w * U, H2 = h * U, r = rng(seed), pts = [[0, H2]];
  for (let i = 1; i <= 7; i++) pts.push([W2 * i / 7, H2 * (1 - i / 7) + (i % 2 ? -1 : 1) * H2 * (.06 + r() * .05)]);
  const m = live(S, null, W2, H2, (ctx, ww, hh, k) => {
    const q = partial(pts, k); ctx.strokeStyle = GREEN; ctx.lineWidth = 30 * U; ctx.lineJoin = 'miter'; ctx.lineCap = 'butt';
    ctx.beginPath(); q.forEach(([a, b], i) => i ? ctx.lineTo(a, b) : ctx.moveTo(a, b)); ctx.stroke();
  }, { t0, dur, x, y, kind: 'growth', role: 'detail' });
  m.userData.bleed = true; m.userData.over = true; return m;
}
/** burst(p, { r = 150, n = 14, arc = 200, dir = 0, x, y }): yellow excitement ticks fanned around a thing (AGk 20 s);
 *  dir: the degrees the fan opens toward (0 = right, 90 = up). */
export const burst = registerElement('burst', (p, { r = 150, n = 14, arc = 200, dir = 0, x = 0, y = 0, seed = 6 } = {}) => {
  const R = r * U, s = R * 2.9;
  const m = sketch(in2d(p, 'burst'), s, s, ctx => {
    const rr = rng(seed), c = s / 2, len = R * .36;
    for (let i = 0; i < n; i++) { const a = (dir - arc / 2 + arc * (i + .5) / n) * Math.PI / 180, j = .88 + rr() * .24;
      stroke(ctx, [[c + Math.cos(a) * R * j, c - Math.sin(a) * R * j], [c + Math.cos(a) * (R * j + len), c - Math.sin(a) * (R * j + len)]], 8 * U, YELLOW, rr, .002); }
  }, { x, y, kind: 'burst', role: 'detail' });
  m.userData.over = true; return m;
});
/** boxes(p, { n = 7, marked = [], size = 70, x, y }): a row of hand-drawn boxes; the marked ones hold a red "0" (days
 *  without posting, AGk 24 s). */
export const boxes = registerElement('boxes', (p, { n = 7, marked = [], size = 70, gap = 22, x = 0, y = 0, seed = 8 } = {}) => {
  const S2 = size * U, G = gap * U, w = n * S2 + (n - 1) * G + 20 * U, h = S2 + 20 * U;
  return sketch(in2d(p, 'boxes'), w, h, ctx => {
    const r = rng(seed);
    for (let i = 0; i < n; i++) { const x0 = 10 * U + i * (S2 + G), y0 = 10 * U;
      const j = () => (r() - .5) * 4 * U, q = [[x0 + j(), y0 + j()], [x0 + S2 + j(), y0 + j()], [x0 + S2 + j(), y0 + S2 + j()], [x0 + j(), y0 + S2 + j()]];
      ctx.strokeStyle = INK; ctx.lineWidth = 6 * U; ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      ctx.beginPath(); q.forEach(([a, b], k) => k ? ctx.lineTo(a, b) : ctx.moveTo(a, b)); ctx.closePath(); ctx.stroke();
      if (marked.includes(i)) { ctx.font = `700 ${S2 * .7}px ${FONT}`; ctx.fillStyle = RED; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText('0', x0 + S2 / 2, y0 + S2 / 2 + 2); } }
  }, { x, y, kind: 'boxes', role: 'form' });
});
/** part(S, 3, 'HOW TO {IMPROVE} + GO {VIRAL}', { at, media, clip, n, fps }): the chapter card (EQUn6 610 s): the member's
 *  picture or clip (optional) above "PART 3: TITLE" in 62 px, key words red. */
export function part(S, num, title, { at: t0 = S.t0, media: key, clip: name, n, fps } = {}) {
  const st = {}, has = key || name, [mx, my] = P(720, VERT ? 420 : 470);
  if (key) st.media = enter(S, media(null, key, { w: 920, x: mx, y: my }), t0);
  if (name) st.media = enter(S, clip(S, name, { n, fps, w: 920, x: mx, y: my, at: t0 }), t0);
  st.title = enter(S, say(null, VERT ? `PART ${num}:
${title}` : `PART ${num}: ${title}`, { size: VERT ? 56 : 62, ...xy2(P(720, has ? (VERT ? 840 : 857) : 540)) }), t0);
  return st;
}
/** viewfinder(S, { at }): the reveal frame (VQ 148 s): black page, white corner brackets at ~15 % insets. Build the card
 *  on top after it; type on it is white: say(..., { color: '#ffffff' }). */
export function viewfinder(S, { at: t0 = S.t0 } = {}) {
  S.bg('#000000'); S.visibility = false;
  const w = 1100 * U, h = 760 * U, [cx, cy] = P(720, 540);
  const m = sketch(null, w, h, ctx => {
    ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 4 * U; const L = 120 * U, i = 4 * U;
    for (const [x0, y0, dx, dy] of [[i, i, 1, 1], [w - i, i, -1, 1], [i, h - i, 1, -1], [w - i, h - i, -1, -1]]) { ctx.beginPath(); ctx.moveTo(x0 + dx * L, y0); ctx.lineTo(x0, y0); ctx.lineTo(x0, y0 + dy * L); ctx.stroke(); }
  }, { x: cx, y: cy, kind: 'viewfinder', role: 'detail' });
  m.userData.over = true; return enter(S, m, t0);
}

/** the shrinking-history list (heading(..., { shrink: true })): item k arrives big at the bottom; items before it drop to
 *  .45 (their notes to 26 px) and close up under the header. Top-anchored on the final state (all but the last small). */
function headingShrink(S, src, items, { t0, size, itemSize, noteSize, gap, bold }) {
  S.sparse = true;                                                 // a list card: the white is the point
  const [hx, hy] = P(720, 540), head = say(null, src, { x: hx, y: hy, size, bold }), SM = Math.max(.45, 26.5 / px(itemSize)), NS = Math.max(SM, 26.5 / px(noteSize));
  const big = it => itemSize * 1.05 + (it.note ? noteSize * 1.25 + 8 : 0), small = it => itemSize * 1.05 * SM + (it.note ? noteSize * 1.25 * NS + 4 : 0) + 8;
  const n = items.length, total = size + gap + items.slice(0, -1).reduce((a, it) => a + small(it), 0) + (n ? big(items[n - 1]) : 0);
  const topY = 540 - total / 2, rise = (540 - (topY + size / 2)) * UV, first = items[0]?.at ?? Infinity, tUp = first - .2 - .15;
  pops(S, head, t0, { lead: true, order: 'rtl' });
  const hy0 = head.position.y;
  if (n) S.tick(t => { head.position.y = hy0 + rise * clamp((t - tUp) / .15, 0, 1); });
  const els = items.map(it => {
    const el = pops(S, say(null, it.src, { size: itemSize, bold: true }), it.at);
    const nt = it.note ? pops(S, say(null, it.note, { size: noteSize }), it.at) : null;
    return [el, nt];
  });
  S.tick(t => {
    const c = items.filter(it => t >= it.at - 1e-4).length; let yy = topY + size + gap;
    items.forEach((it, j) => {
      const [el, nt] = els[j], sm = j < c - 1, s = sm ? SM : 1, ns = sm ? NS : 1, ih = itemSize * 1.05 * s;
      const [ix, iy] = P(720, yy + ih / 2); el.position.set(ix, iy, 0); el.scale.set(s, s, 1);
      if (nt) { const [nx, ny] = P(720, yy + ih + (sm ? 2 : 8) + noteSize * ns * .6); nt.position.set(nx, ny, 0); nt.scale.set(ns, ns, 1); }
      yy += sm ? small(it) : big(it) + 26;
    });
  });
  return { head, items: els.map(([e, nt]) => nt ? [e, nt] : e) };
}

// ---------- this style's own checks (QUALITY.md; proven by mustfail_red, mustfail_page, mustfail_hold) ----------
const sayBlocks = st => { const out = []; const walk = v => { if (!v) return; if (Array.isArray(v)) return v.forEach(walk);
  if (v.isObject3D) v.traverse(o => { if (o.userData?.words && !out.includes(o)) out.push(o); }); }; Object.values(st || {}).forEach(walk); return out; };
const vis = o => { for (; o; o = o.parent) if (!o.visible) return false; return true; };
// RED: more than 3 red words in one line of type
LAYOUT_CHECKS.push((S, t, def) => {
  const out = [];
  for (const g of sayBlocks(def._st)) {
    const lines = {}; for (const m of g.userData.words) if (vis(m) && String(m.userData.color).toLowerCase() === RED) lines[m.userData.line] = (lines[m.userData.line] ?? 0) + 1;
    for (const [li, n] of Object.entries(lines)) if (n > 3) out.push({ type: 'RED', detail: `${n} red words in one line (max 3): "${g.userData.text.split(String.fromCharCode(10))[li]}". Keep the 1-2 words the line is about red, the rest black.` });
  }
  return out;
});
// PAGE: the page is not the style's flat page (#ffffff; #fcfcfc in the 'hits' era; black only through viewfinder())
LAYOUT_CHECKS.push((S, t, def) => {
  if (S.kit || S.visibility === false) return [];
  const bg = String(S._bg ?? '').toLowerCase(), page = String(C.bg).toLowerCase();   // #ffffff, or #fcfcfc in the 'hits' era
  return bg && bg !== page ? [{ type: 'PAGE', detail: `the page is ${bg}, not ${page}: use S.bg() (the style's page); a black page only through viewfinder()` }] : [];
});
// HOLD: nothing new for more than 6 s
LAYOUT_CHECKS.push((S, t, def) => {
  if (S.kit) return [];
  const ev = [def.t0, ...(S._dmEv ?? [])].filter(x => x <= t + 1e-3).sort((a, b) => a - b);
  let gap = t - ev[ev.length - 1]; for (let i = 1; i < ev.length; i++) gap = Math.max(gap, ev[i] - ev[i - 1]);
  return gap > 6 ? [{ type: 'HOLD', detail: `nothing new for ${gap.toFixed(1)} s (max 6): pop the next chunk, bullet or footnote on its word, or cut` }] : [];
});

// VOID: nothing on screen 0.25 s after the cut (the first thing arrives with the cut; motion.md 5). The check plays the
// shot's ticks at the probe time and back (ticks are pure functions of t), once per shot.
LAYOUT_CHECKS.push((S, t, def) => {
  if (S.kit) return [];
  if (def._dmVoid) return def._dmVoid;
  const i = SHOTS.indexOf(def), end = SHOTS[i + 1]?.t0 ?? Infinity, tt = def.t0 + .25;
  if (end - def.t0 < .4) return (def._dmVoid = []);
  const shown = () => { let any = false; const walk = v => { if (any || !v) return; if (Array.isArray(v)) return v.forEach(walk);
    if (v.isObject3D) v.traverse(o => { if (!any && o.isMesh && vis(o) && (o.material?.opacity ?? 1) > .05) any = true; }); };
    Object.values(def._st || {}).forEach(walk); return any; };
  const marks = (S.anims || []).filter(a => a.dm), play = x => { for (const a of marks) a.obj.visible = x >= a.at - 1e-4; for (const f of S.ticks) f(x); };
  play(tt);
  const ok = shown();
  play(t);
  return (def._dmVoid = ok ? [] : [{ type: 'VOID', detail: `nothing on screen 0.25 s after the cut at ${def.t0.toFixed(2)} s: the first thing arrives with the cut (cut on the word it shows, or show the drawing's base before it moves)` }]);
});

// ---------- the base's examples (kept exported: the kit's contract) ----------
// badge(p, 'A', { r, fill, x, y }): a round marker with a letter or number (2D; on a 3D shot it goes on the HUD)
export const badge = registerElement('badge', (p, { r = 60, fill = C.accent, x = 0, y = 0, label = '' } = {}) => {
  const g = group(in2d(p, 'badge'), x, y);
  circle(g, r, fill);
  if (label) text(g, String(label), { size: Math.round(r * .9), color: textOn(fill) });
  g.userData.bg = fill;                                            // the plate its text reads against (contrast check)
  return g;
});

// table(p, { w, d, h, color, x, z }): a top on four legs, standing on y (3D only). The legs carry the top, so nothing floats.
export const table = DIM === '3d' ? registerElement('table', (p, { w = 1.4, d = .8, h = .75, top = .05, color = C.surface, legs = C.muted, x = 0, y = 0, z = 0 } = {}) => {
  const g = group(in3d(p, 'table'), x, y, z), lx = w / 2 - .08, lz = d / 2 - .08;
  for (const [sx, sz] of [[-1, -1], [1, -1], [-1, 1], [1, 1]]) box(g, .06, h - top, .06, legs, { x: sx * lx, z: sz * lz });
  box(g, w, top, d, color, { y: h - top });
  return g;
}) : null;
