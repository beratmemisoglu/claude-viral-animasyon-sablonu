// dmscales motion view: the reference's moving templates on fixed times (no narration), to check every entrance, move
// and media device frame by frame against motion.md. Media are the kit's own test files (assets/media, made with ffmpeg).
import { shot, VERT } from '../engine.js';
import { P, T, say, figure, mark, media, clip, stack, enter, leave, move, pops, heading } from '../models.js';

const xy = ([x, y]) => ({ x, y });

// ---- 1: phone clip left + line right + red arrow; then the clip shrinks to the top centre with a footnote (N-q 85-89 s) ----
shot({ t0: 0, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true; const st = {};
  // measured (N-q 85 s): phone clip ~430 x 790 left of centre, two bold lines on the right at y 430 / 475, arrow under them
  st.clip = clip(S, 'test_clip', { n: 45, fps: 15, h: VERT ? 1000 : 790, r: 28, at: 0, ...xy(VERT ? P(720, 300) : P(400, 540)) });
  st.l1 = pops(S, say(null, 'anyone can {enjoy} watching', { size: T.sub, bold: true, ...xy(VERT ? P(720, 900) : P(1030, 430)) }), .3);
  st.l2 = pops(S, say(null, 'these {type} of videos', { size: T.sub, bold: true, ...xy(VERT ? P(720, 960) : P(1030, 480)) }), 1.3);
  st.arrow = enter(S, VERT ? mark(null, 'arrow', { w: 150, h: 130, mirror: 1, ...xy(P(1060, 1080)) })
    : mark(null, 'arrow', { w: 120, h: 60, mirror: 1, flip: 1, bend: .3, ...xy(P(760, 600)) }), .6, 'wipe');
  for (const k of ['l1', 'l2', 'arrow']) leave(S, st[k], 3, 'cut');
  const [cx, cy] = P(720, VERT ? 300 : 430);
  move(S, st.clip, 3, { x: cx, y: cy, s: VERT ? .85 : .8, frames: 6 });
  st.foot = enter(S, say(null, '*this channel is an example', { size: 40, bold: true, ...xy(P(720, VERT ? 930 : 900)) }), 3.15);
  return st;
} });

// ---- 2: screenshot stack, then the marker arrow and the footnote (N-q 45 s, 12-14 s) ----
shot({ t0: 4.5, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true; const st = {};
  st.shots = stack(S, ['test_shot', 'test_shot', 'test_shot'], [4.7, 5.3, 5.9], { w: 700, ...xy(P(VERT ? 720 : 680, 470)) });
  st.arrow = enter(S, mark(null, 'arrow', { w: 200, h: 120, flip: 1, mirror: 1, ...xy(VERT ? P(1150, 760) : P(1250, 330)) }), 6.6, 'wipe');
  st.arrow.userData.over = st.shots;                       // the arrow points at the pile and may touch its edge
  st.line = pops(S, say(null, 'this is the {proof}', { size: T.body, ...xy(VERT ? P(720, 1010) : P(1180, 200)) }), 6.6);
  st.foot = enter(S, say(null, '*not my screenshots', { size: T.foot, ...xy(P(720, VERT ? 1100 : 900)) }), 7);
  return st;
} });

// ---- 3: the figure arrives with its elastic bounce, the line builds word by word (AGk 37 s, VQ 0.3 s) ----
shot({ t0: 8.5, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true; const st = {};
  st.guy = enter(S, figure(null, { h: VERT ? 600 : 430, face: 'grin', pose: 'armsup', ...xy(VERT ? P(720, 300) : P(330, 540)) }), 8.55, 'elastic');
  st.line = pops(S, say(null, 'when you {finally} get views', { size: T.body, ...xy(VERT ? P(720, 760) : P(930, 540)) }), [8.9, 9.1, 9.3, 9.6, 9.8], { lead: true });
  return st;
} });

// ---- 4: the header + list build: header alone at the centre, slides up, items pop on their words (N-q 15-21 s) ----
shot({ t0: 10.5, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true;
  const { head, items } = heading(S, 'HOW TO {PASS}:', [
    { src: '- a hook in the {first} second', at: 11.4 },
    { src: '- one clear {idea}', at: 12.0, note: '(if you cant say it in a sentence, its two videos)' },
    { src: '- but most importantly, {retention}', at: 12.7 },
  ], { at: 10.6 });
  return { head, items: items.flat() };
} });
