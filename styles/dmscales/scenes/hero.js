// dmscales hero frames: three still frames that show the look at a glance. Static on purpose (no pops, no camera).
// Layouts are the reference's templates (visual.md section 8), given in reference px (1440 x 1080) through P().
import { shot, VERT } from '../engine.js';
import { P, T, GREY, say, figure, crowd, mark } from '../models.js';

// ---- hero 1: figure left, line right (T07) ----
shot({ t0: 0, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true; const st = {};
  st.guy = figure(null, { h: VERT ? 560 : 440, face: 'frown', ...xy(VERT ? P(720, 300) : P(330, 540)) });
  st.line = say(null, VERT ? 'when you post\nyour {first} video' : 'when you post your {first} video', { size: T.body, ...xy(VERT ? P(720, 760) : P(930, 540)) });
  st.foot = say(null, '*most channels never get past this part', { size: T.foot, ...xy(VERT ? P(720, 900) : P(930, 640)) });
  return st;
} });

// ---- hero 2: definition card (T04) ----
shot({ t0: 2, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true; const st = {};
  st.head = say(null, '{SWIPE} RATE:', { size: 92, bold: true, ...xy(P(720, 395)) });
  st.def = say(null, '- how many people {skip} your video\nbefore it even _starts_', { size: 54, bold: true, ...xy(P(720, 535)) });
  st.note = say(null, '(the lower it is, the further it {travels})', { size: 31, bold: true, color: GREY, ...xy(P(720, 640)) });
  return st;
} });

// ---- hero 3: tracked-caps statement over the audience, with a marker arrow (T06 + T14) ----
shot({ t0: 4, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true; const st = {};
  st.caps = say(null, VERT ? 'EVERY VIEWER\nWANTS ONE THING:\n{g:A REASON}' : 'EVERY VIEWER WANTS\nONE THING: {g:A REASON}', { size: T.caps, italic: false, track: .11, ...xy(P(720, VERT ? 120 : 220)) });
  st.crowd = crowd(null, { w: VERT ? 880 : 700, h: VERT ? 590 : 470, ...xy(P(VERT ? 720 : 660, VERT ? 640 : 630)) });
  st.arrow = VERT ? mark(null, 'arrow', { w: 150, h: 130, mirror: 1, ...xy(P(1000, 1030)) })
    : mark(null, 'arrow', { w: 170, h: 130, flip: 1, mirror: 1, ...xy(P(1190, 520)) });
  st.note = say(null, '*to click', { size: 33, ...xy(VERT ? P(1060, 1220) : P(1250, 365)) });
  return st;
} });

function xy([x, y]) { return { x, y }; }
