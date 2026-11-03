// dmscales templates view: every composite template alone, on fixed times, to check it against the reference frames
// (research/dmscales/work/ref2/sheet.png). Media are the kit's own ffmpeg test files.
import { shot, VERT } from '../engine.js';
import { P, T, GREY, say, figure, mark, enter, pops, columns, compare, cloud, curve, growth, burst, boxes, part, viewfinder, media } from '../models.js';

const xy = ([x, y]) => ({ x, y });
const cut = (t0, build) => shot({ t0, trans: 'cut', captions: false, build(S) { S.bg(); S.noCamera = true; return build(S) ?? {}; } });

// ---- T13 two columns ----
cut(0, S => columns(S, '_{everything} i covered_', ['-shorts algorithm', '-long-form algorithm', '-metrics', '-hooks', '-retention', '-metadata'],
  ['-adsense', '-niche selection', '-branding', '-scaling', '-tools', '-and lots of {underground} tricks'], { at: 0, foot: '*this is {thousands} of hours of testing in 1 video' }));

// ---- compare cards: Viewer vs Creator (items pop one by one) ----
cut(2.5, S => compare(S, [
  { label: 'Viewer', items: ['- loves {animals}', '- watches car shorts', '- swipes away on games'] },
  { label: 'Creator', items: ['- posts {animal} shorts', '- viewers like him love this'] },
], { at: 2.6, times: [2.8, 3.1, 3.4, 3.7, 4.0] }));

// ---- thought cloud, then X-ed out ----
cut(5, S => {
  const st = {};
  st.guy = figure(null, { h: 420, face: 'smile', ...xy(VERT ? P(520, 720) : P(470, 600)) });
  st.cloud = cloud(null, 'a niche is the content you make', { w: 420, h: 280, ...xy(VERT ? P(900, 300) : P(930, 380)) });
  st.x = enter(S, mark(null, 'x', { w: 470, h: 340, ...xy(VERT ? P(900, 300) : P(930, 380)) }), 6.4);
  st.x.userData.over = [st.cloud];
  return st;
});

// ---- explanatory curve drawing on + its label and footnote ----
cut(7.5, S => ({
  chart: curve(S, { shape: 'bad', at: 7.6, ...xy(P(720, 430)) }),
  label: enter(S, say(null, 'Bad Hook', { size: 52, bold: true, ...xy(P(720, 790)) }), 8.2),
  foot: enter(S, say(null, '*you didnt give a viewer a {reason} to stay till the end', { size: 30, bold: true, ...xy(P(720, 850)) }), 8.4),
}));

// ---- figure with a phone and the yellow burst ----
cut(10, S => ({
  guy: figure(null, { h: 460, face: 'grin', pose: 'phone', ...xy(P(640, 540)) }),
  burst: enter(S, burst(null, { r: 120, arc: 220, dir: 0, ...xy(P(790, 560)) }), 10.3, 'scale'),
  line: pops(S, say(null, 'when the {first} views come in', { size: T.sub, ...xy(VERT ? P(720, 930) : P(720, 930)) }), 10.6),
}));

// ---- tick boxes ----
cut(12.5, S => ({
  line: pops(S, say(null, 'dont post for a {couple days}', { size: T.body, ...xy(P(720, 420)) }), 12.6),
  boxes: enter(S, boxes(null, { n: 7, marked: [4, 6], size: VERT ? 100 : 92, ...xy(P(720, 560)) }), 13.0),
  foot: enter(S, say(null, '*warm up your account for ~{7 days} first', { size: T.foot, ...xy(P(720, VERT ? 720 : 680)) }), 13.4),
}));

// ---- growth line behind a card ----
cut(15, S => {
  const st = {};
  st.line = growth(S, { at: 15.1, ...xy(P(720, 700)) });
  st.card = enter(S, media(null, 'test_shot', { w: 560, ...xy(P(720, 430)) }), 15.0);
  st.q = enter(S, say(null, 'whats a viewers {reason} to\nwatch this video?', { size: 48, ...xy(P(760, 720)) }), 15.6);
  return st;
});

// ---- chapter card ----
cut(17.5, S => part(S, 3, 'HOW TO {IMPROVE} + GO {VIRAL}', { at: 17.5, media: 'test_shot' }));

// ---- viewfinder reveal ----
cut(20, S => {
  const vf = viewfinder(S, { at: 20 });
  const card = enter(S, media(null, 'test_shot', { w: 700, ...xy(P(720, 520)) }), 20);
  card.userData.over = [vf];
  return { vf, card };
});
