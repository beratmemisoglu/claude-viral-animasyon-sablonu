// MUSTFAIL: RED
// A deliberate mistake: the layout check must report it. If it ever passes here, the check is broken (never fix this file).
import { shot } from '../engine.js';
import { say } from '../models.js';

// ---- mustfail: four red words in one line (the style allows 3 at most) ----
shot({ t0: 0, trans: 'cut', captions: false, build(S) {
  S.bg(); S.noCamera = true;
  return { line: say(null, 'the {first} {video} {always} {flops}') };
} });
