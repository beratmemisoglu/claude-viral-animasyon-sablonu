// dmscales sample: the 17 s sample narration (audio/timeline.json, ~270 wpm) as a finished video. Plan, one shot per clause
// (template, what lands on which word):
//  S1 T07  "When you upload a new video,"            figure (frown) left, the line builds word by word, "new" red
//  S2 T01  "the first thing that happens is"         one line, first word cascades
//  S3 T14  "YouTube shows it to a tiny test group."  caption + the crowd scales in on "tiny"
//  S4 T04  "(This is called the) test pool. If those viewers watch it,"  cut on "test": "TEST POOL:" cascades in, bullet
//          on "pool", grey note; the card stays while "those viewers" are spoken about (1.6 s, readable)
//  S5 CRV  "it gets pushed out to more people."     cut on "it": the curve draws on with the cut, label on "pushed"
//  S6 T07  "If they swipe away, it dies right there." figure (shock) + line, "dies" red, footnote
//  S7 T03  "To pass the test, you need a hook in the first second, one clear idea,"  HOW TO PASS: items on their words
//  S8 T01  "but most importantly,"                   a clean card, no red
//  S9 T02  "retention."                              the hero word
//  S10 T06 "Because every viewer only wants one thing: a reason to keep watching."  tracked caps over the crowd, green payoff
import { shot, cue, VERT } from '../engine.js';
import { P, T, GREY, say, figure, crowd, curve, enter, pops, words, heading, mark } from '../models.js';

const xy = ([x, y]) => ({ x, y });
const at = (w, near) => cue(w, near);
const cut = (t0, build) => shot({ t0, trans: 'cut', captions: false, build(S) { S.bg(); S.noCamera = true; return build(S) ?? {}; } });

// ---- S1: figure left, line right ----
cut(0, S => {
  const src = 'when you upload a {new} video';
  return { guy: figure(null, { h: 440, face: 'frown', ...xy(VERT ? P(720, 330) : P(330, 540)) }),
    line: pops(S, say(null, src, { ...xy(VERT ? P(720, 780) : P(930, 540)) }), words(src, 0), { lead: true }) };
});
// ---- S2: one line ----
cut(at('the', 1.3) - .02, S => {
  S.sparse = true;                                         // a text-only card: the white is the point
  const src = 'the {first} thing that happens is';
  return { line: pops(S, say(null, src, { size: T.hero * .8, ...xy(P(720, 540)) }), words(src, 1.3), { lead: true }) };
});
// ---- S3: caption + crowd ----
cut(at('YouTube', 2.6) - .02, S => {
  const src = 'youtube shows it to a {tiny test group}';
  return { cap: pops(S, say(null, src, { size: T.body, ...xy(P(720, VERT ? 170 : 210)) }), words(src, 2.6)),
    crowd: enter(S, crowd(null, { w: 640, h: 420, n: 14, ...xy(P(720, VERT ? 600 : 600)) }), at('tiny', 3.5), 'scale') };
});
// ---- S4: definition card ----
cut(at('test', 5) - .02, S => ({
  head: pops(S, say(null, '{TEST} POOL:', { size: 92, bold: true, ...xy(P(720, 400)) }), at('test', 5), { lead: true, order: 'rtl' }),
  def: pops(S, say(null, '- the first ~{200 - 500} people\nwho ever see your video', { size: 54, bold: true, ...xy(P(720, 540)) }), at('pool', 5.2)),
  note: pops(S, say(null, '(they decide if it goes any further)', { size: 31, bold: true, color: GREY, ...xy(P(720, 645)) }), at('pool', 5.2) + .35),
}));
// ---- S5: the explanatory curve ----
cut(at('it', 6.62) - .02, S => ({
  chart: curve(S, { shape: 'rise', at: at('it', 6.62), dur: 1, ...xy(P(720, VERT ? 470 : 430)) }),
  label: pops(S, say(null, 'it gets {pushed} out', { size: 52, bold: true, ...xy(P(720, VERT ? 760 : 790)) }), at('pushed', 6.9)),
}));
// ---- S6: figure + line ----
cut(at('If', 8.1) - .02, S => {
  const src = 'if they swipe away, it {dies} right there';
  return { guy: figure(null, { h: 420, face: 'shock', pose: 'armsup', ...xy(VERT ? P(720, 330) : P(330, 540)) }),
    line: pops(S, say(null, 'if they swipe away,\nit {dies} right there', { size: T.body, ...xy(VERT ? P(720, 780) : P(930, 520)) }), words(src, 8.1)),
    foot: enter(S, say(null, '*and the algorithm moves on', { size: T.foot, ...xy(VERT ? P(720, 900) : P(930, 640)) }), at('there', 9.5) + .1) };
});
// ---- S7: header + list ----
cut(at('To', 9.8) - .02, S => {
  const { head, items } = heading(S, 'HOW TO {PASS}:', [
    { src: '- a {hook} in the first second', at: at('hook', 11.1) },
    { src: '- one clear {idea}', at: at('clear', 12.3) },
  ], { at: at('pass', 10), shrink: true });
  return { head, items: items.flat() };
});
// ---- S8: the clean transition card ----
cut(at('but', 12.8) - .02, S => (S.sparse = true, { line: pops(S, say(null, 'but most importantly', { ...xy(P(720, 540)) }), words('but most importantly', 12.8)) }));
// ---- S9: the hero word ----
cut(at('retention', 13.6) - .02, S => {
  const word = pops(S, say(null, '{RETENTION}', { size: T.hero * 1.2, bold: true, ...xy(P(720, 520)) }), at('retention', 13.6), { lead: true });
  const ring = enter(S, mark(null, 'circle', { w: 760, h: 170, ...xy(P(720, 525)) }), at('retention', 13.6) + .35);
  ring.userData.over = [word];                             // the circle is drawn around the word on purpose
  return { word, ring };
});
// ---- S10: tracked caps over the audience, the payoff in green ----
cut(at('Because', 14.1) - .02, S => {
  const src = VERT ? 'EVERY VIEWER\nONLY WANTS ONE THING:\n{g:A REASON TO WATCH}' : 'EVERY VIEWER ONLY WANTS\nONE THING: {g:A REASON TO WATCH}';
  return { caps: pops(S, say(null, src, { size: T.caps, italic: false, track: .1, ...xy(P(720, VERT ? 140 : 220)) }), [...words('EVERY VIEWER ONLY WANTS ONE THING:', 14.4), at('reason', 16)]),
    crowd: enter(S, crowd(null, { w: VERT ? 900 : 800, h: VERT ? 600 : 520, seed: 12, ...xy(P(720, VERT ? 660 : 640)) }), at('Because', 14.6), 'scale') };   // the audience comes with the cut
});
