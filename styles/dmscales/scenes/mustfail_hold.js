// MUSTFAIL: HOLD
// A deliberate mistake: the layout check must report it. If it ever passes here, the check is broken (never fix this file).
import { shot } from '../engine.js';
import { say, pops } from '../models.js';

// ---- mustfail: one line popped at 0.2 s, then nothing new for 7.8 s (the style allows 6 s) ----
shot({ t0: 0, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true;
  return { line: pops(S, say(null, 'nothing else happens {here}'), .2) };
} });
