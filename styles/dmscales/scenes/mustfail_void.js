// MUSTFAIL: VOID
// A deliberate mistake: the layout check must report it. If it ever passes here, the check is broken (never fix this file).
import { shot } from '../engine.js';
import { say, pops } from '../models.js';

// ---- mustfail: the cut lands, then the page stays empty for a whole second before the first word ----
shot({ t0: 0, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true;
  return { line: pops(S, say(null, 'this came a second {late}'), 1) };
} });
