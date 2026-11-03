// MUSTFAIL: PAGE
// A deliberate mistake: the layout check must report it. If it ever passes here, the check is broken (never fix this file).
import { shot } from '../engine.js';
import { say } from '../models.js';

// ---- mustfail: a grey page (the style lives on #ffffff only) ----
shot({ t0: 0, trans: 'cut', captions: false, build(S) {
  S.bg('#d8d8d8'); S.noCamera = true;
  return { line: say(null, 'this page is {grey}') };
} });
