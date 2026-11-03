/* The Other Self — hero rig v2 (framework-free; ported 1:1 to Remotion TSX later).
 * Style-driven: body silhouette, head, limbs, colours and shadow-twin colours come from a STYLE object,
 * so different character designs share one animation system.
 * Coordinates: rig units, ground at y = 0, y grows DOWN (SVG), character faces +x.
 * Angles: dir(a) = (sin a, cos a) → 0° = down, +90° = forward. Limbs = one FK path each (no detachment).
 */
(function (g) {
  const DEG = Math.PI / 180;
  const dir = (a) => ({ x: Math.sin(a * DEG), y: Math.cos(a * DEG) });
  const add = (a, b) => ({ x: a.x + b.x, y: a.y + b.y });
  const mul = (a, s) => ({ x: a.x * s, y: a.y * s });
  const rot = (v, d) => { const c = Math.cos(d * DEG), s = Math.sin(d * DEG); return { x: v.x * c - v.y * s, y: v.x * s + v.y * c }; };
  const f = (n) => (Math.round(n * 100) / 100).toString();

  // ---------------------------------------------------------------- styles
  const CURL = '<path d="M -4 -49 C -9 -66 8 -76 15 -66 C 20 -58 10 -52 6 -59" fill="none" stroke="INK" stroke-width="4.5" stroke-linecap="round"/>';
  const STYLES = {
    // v1 — bean body with merged head (closest to the reference look)
    bean: {
      name: 'v1 · Fasulye', body: '#ECE5D3', ink: '#1C1A17', outline: 3, farOpacity: 0.62,
      limbW: 24, handR: 14, footRx: 18, footRy: 10, upperArm: 60, foreArm: 56, thigh: 58, shin: 56, pelvisH: 125,
      shoulderNear: { x: 10, y: -60 }, shoulderFar: { x: -6, y: -63 }, hipNear: { x: 12, y: 0 }, hipFar: { x: -10, y: 0 },
      torsoPath: 'M -50 -107 A 50 50 0 0 1 50 -107 C 53 -70 56 -30 50 -12 C 45 6 28 14 0 14 C -28 14 -46 6 -50 -12 C -54 -40 -52 -80 -50 -107 Z',
      head: { c: { x: 0, y: -107 }, r: 50, separate: false }, neck: null, topper: CURL,
      eye: { rx: 4.6, ry: 7.2, spread: 16 },
      shadow: { fill: '#050505', glow: '#E8381F', rim: '#FF5A3A', eye: '#FF8A70' },
    },
    // A — "Lantern": separate round head on a thin neck, small pear body, thin limbs. Paper white + violet twin.
    lantern: {
      name: 'A · Fener', body: '#F2EEE6', ink: '#22232A', outline: 2.6, farOpacity: 0.55,
      limbW: 16, handR: 10, footRx: 14, footRy: 8, upperArm: 50, foreArm: 46, thigh: 52, shin: 50, pelvisH: 112,
      shoulderNear: { x: 12, y: -64 }, shoulderFar: { x: -10, y: -66 }, hipNear: { x: 10, y: 0 }, hipFar: { x: -10, y: 0 },
      torsoPath: 'M 0 -84 C 24 -84 30 -62 36 -32 C 44 0 34 16 0 16 C -34 16 -44 0 -36 -32 C -30 -62 -24 -84 0 -84 Z',
      head: { c: { x: 4, y: -140 }, r: 44, separate: true }, neck: { from: { x: 0, y: -80 }, to: { x: 3, y: -104 }, w: 13 },
      topper: CURL,
      eye: { rx: 5.6, ry: 6.6, spread: 15 },
      shadow: { fill: '#06050A', glow: '#7B5CFF', rim: '#A88FFF', eye: '#E0D6FF' },
    },
    // B — "Drop": one teardrop shape (pointed tip = the signature), short stubby limbs. Blue-grey + teal twin.
    drop: {
      name: 'B · Damla', body: '#C9D5E3', ink: '#1B2430', outline: 3, farOpacity: 0.55,
      limbW: 20, handR: 12, footRx: 15, footRy: 9, upperArm: 44, foreArm: 40, thigh: 46, shin: 44, pelvisH: 100,
      shoulderNear: { x: 18, y: -50 }, shoulderFar: { x: -14, y: -52 }, hipNear: { x: 14, y: 0 }, hipFar: { x: -12, y: 0 },
      torsoPath: 'M 0 -182 C 12 -156 62 -124 62 -62 C 62 -12 36 14 0 14 C -36 14 -62 -12 -62 -62 C -62 -124 -12 -156 0 -182 Z',
      head: { c: { x: 4, y: -78 }, r: 50, separate: false }, neck: null, topper: '',
      eye: { rx: 4, ry: 8.4, spread: 17 },
      shadow: { fill: '#04070A', glow: '#14D3C4', rim: '#6FF5EA', eye: '#C4FFF9' },
    },
    // C — "Moon head": big round head on a small body, stick limbs, a sprout on top. Warm sand + electric-blue twin.
    moon: {
      name: 'C · Ay kafa', body: '#E9C9A2', ink: '#2B1F17', outline: 2.6, farOpacity: 0.55,
      limbW: 13, handR: 9, footRx: 13, footRy: 7, upperArm: 42, foreArm: 38, thigh: 44, shin: 44, pelvisH: 92,
      shoulderNear: { x: 14, y: -70 }, shoulderFar: { x: -12, y: -72 }, hipNear: { x: 10, y: 0 }, hipFar: { x: -10, y: 0 },
      torsoPath: 'M -26 -84 Q -28 -94 -12 -94 L 12 -94 Q 28 -94 26 -84 L 30 -2 Q 30 14 0 14 Q -30 14 -30 -2 Z',
      head: { c: { x: 6, y: -146 }, r: 58, separate: true }, neck: null,
      topper: '<path d="M 0 -50 C -2 -60 -1 -66 2 -72" fill="none" stroke="INK" stroke-width="3.6" stroke-linecap="round"/>' +
              '<path d="M 2 -72 C 12 -84 26 -78 24 -70 C 16 -64 8 -66 2 -72 Z" fill="BODY" stroke="INK" stroke-width="3" stroke-linejoin="round"/>',
      eye: { rx: 5, ry: 7.6, spread: 19 },
      shadow: { fill: '#04050B', glow: '#2F6BFF', rim: '#7FA6FF', eye: '#D6E4FF' },
    },
  };

  // ---------------------------------------------------------------- expressions
  const EXPR = {
    neutral:    { brow: [-17, -17], eyes: 'oval', mouth: 'flat' },
    content:    { brow: [-17, -18], eyes: 'oval', mouth: 'smile' },
    sleepy:     { brow: [-15, -15], eyes: 'lid', mouth: 'flat' },
    asleep:     { brow: [-14, -15], eyes: 'closedDown', mouth: 'smile', extras: ['zz'] },
    shocked:    { brow: [-21, -25], eyes: 'wide', mouth: 'o', extras: ['sweat'] },
    numb:       { brow: [-14, -14], eyes: 'lid', mouth: 'none' },
    sad:        { brow: [-13, -22], eyes: 'lidSad', mouth: 'frown' },
    crying:     { brow: [-12, -23], eyes: 'closedDown', mouth: 'frown', extras: ['tear'] },
    determined: { brow: [-21, -12], eyes: 'oval', mouth: 'flat' },
    straining:  { brow: [-23, -10], eyes: 'squeeze', mouth: 'teeth', extras: ['sweat', 'stress'] },
    confident:  { brow: [-19, -15], eyes: 'oval', mouth: 'smile' },
    happy:      { brow: [-21, -22], eyes: 'closedUp', mouth: 'bigSmile', extras: ['blush'] },
    lonely:     { brow: [-15, -20], eyes: 'ovalDown', mouth: 'small' },
    hopeful:    { brow: [-20, -23], eyes: 'wide', mouth: 'smile' },
    anxious:    { brow: [-16, -24], eyes: 'wideSmall', mouth: 'wobble', extras: ['sweat'] },
  };

  function eyeSVG(type, cx, cy, ink, E) {
    const hl = (x, y, r) => `<circle cx="${f(x)}" cy="${f(y)}" r="${r}" fill="#FFFFFF"/>`;
    const rx = E.rx, ry = E.ry;
    switch (type) {
      case 'oval': return `<ellipse cx="${f(cx)}" cy="${f(cy)}" rx="${rx}" ry="${ry}" fill="${ink}"/>` + hl(cx - rx * 0.3, cy - ry * 0.45, 1.5);
      case 'ovalDown': return `<ellipse cx="${f(cx)}" cy="${f(cy + 2)}" rx="${rx * 0.9}" ry="${ry * 0.9}" fill="${ink}"/>` + hl(cx - rx * 0.3, cy - 0.6, 1.3);
      case 'wide': return `<ellipse cx="${f(cx)}" cy="${f(cy)}" rx="${rx * 1.3}" ry="${ry * 1.22}" fill="${ink}"/>` + hl(cx - rx * 0.4, cy - ry * 0.5, 2.2);
      case 'wideSmall': return `<ellipse cx="${f(cx)}" cy="${f(cy)}" rx="${rx * 0.78}" ry="${ry * 0.78}" fill="${ink}"/>` + hl(cx - 1.1, cy - 2.4, 1.2);
      case 'lid': return `<path d="M ${f(cx - rx)} ${f(cy - 1)} A ${rx} ${ry * 0.83} 0 0 0 ${f(cx + rx)} ${f(cy - 1)} Z" fill="${ink}"/>` +
        `<path d="M ${f(cx - 8)} ${f(cy - 1)} L ${f(cx + 8)} ${f(cy - 1)}" stroke="${ink}" stroke-width="4" stroke-linecap="round"/>` +
        `<path d="M ${f(cx - 6)} ${f(cy + 9)} Q ${f(cx)} ${f(cy + 11.5)} ${f(cx + 6)} ${f(cy + 9)}" stroke="rgba(80,70,55,.45)" stroke-width="2.6" fill="none" stroke-linecap="round"/>`;
      case 'lidSad': return `<path d="M ${f(cx - rx)} ${f(cy)} A ${rx} ${ry * 0.83} 0 0 0 ${f(cx + rx)} ${f(cy)} Z" fill="${ink}"/>` +
        `<path d="M ${f(cx - 7.5)} ${f(cy)} L ${f(cx + 7.5)} ${f(cy)}" stroke="${ink}" stroke-width="4" stroke-linecap="round"/>`;
      case 'closedDown': return `<path d="M ${f(cx - 7)} ${f(cy - 1)} Q ${f(cx)} ${f(cy + 5)} ${f(cx + 7)} ${f(cy - 1)}" stroke="${ink}" stroke-width="4" fill="none" stroke-linecap="round"/>`;
      case 'closedUp': return `<path d="M ${f(cx - 7)} ${f(cy + 2)} Q ${f(cx)} ${f(cy - 6)} ${f(cx + 7)} ${f(cy + 2)}" stroke="${ink}" stroke-width="4" fill="none" stroke-linecap="round"/>`;
      case 'squeeze': return `<path d="M ${f(cx - 6)} ${f(cy - 5)} L ${f(cx + 5)} ${f(cy)} L ${f(cx - 6)} ${f(cy + 5)}" stroke="${ink}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
      default: return '';
    }
  }

  function mouthSVG(type, mx, my, ink) {
    const s = `stroke="${ink}" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"`;
    switch (type) {
      case 'flat': return `<path d="M ${f(mx - 5)} ${my} L ${f(mx + 5)} ${my}" ${s}/>`;
      case 'small': return `<path d="M ${f(mx - 3)} ${my} L ${f(mx + 3)} ${my}" ${s}/>`;
      case 'smile': return `<path d="M ${f(mx - 6)} ${my - 2} Q ${f(mx)} ${my + 4} ${f(mx + 6)} ${my - 2}" ${s}/>`;
      case 'frown': return `<path d="M ${f(mx - 6)} ${my + 3} Q ${f(mx)} ${my - 3} ${f(mx + 6)} ${my + 3}" ${s}/>`;
      case 'o': return `<ellipse cx="${f(mx)}" cy="${my + 1}" rx="3.6" ry="4.6" fill="${ink}"/>`;
      case 'bigSmile': return `<path d="M ${f(mx - 8)} ${my - 3} Q ${f(mx)} ${my - 1} ${f(mx + 8)} ${my - 3} Q ${f(mx + 6)} ${my + 8} ${f(mx)} ${my + 8} Q ${f(mx - 6)} ${my + 8} ${f(mx - 8)} ${my - 3} Z" fill="${ink}"/>`;
      case 'wobble': return `<path d="M ${f(mx - 7)} ${my} Q ${f(mx - 3.5)} ${my - 3} ${f(mx)} ${my} Q ${f(mx + 3.5)} ${my + 3} ${f(mx + 7)} ${my}" ${s}/>`;
      case 'teeth': return `<rect x="${f(mx - 8)}" y="${my - 5}" width="16" height="10" rx="3" fill="#F6F1E4" stroke="${ink}" stroke-width="2.6"/>` +
        `<path d="M ${f(mx - 8)} ${my} L ${f(mx + 8)} ${my} M ${f(mx - 3)} ${my - 5} L ${f(mx - 3)} ${my + 5} M ${f(mx + 3)} ${my - 5} L ${f(mx + 3)} ${my + 5}" stroke="${ink}" stroke-width="1.8"/>`;
      default: return '';
    }
  }

  /** Face in head space (head centre 0,0, nominal r 50). q = 0 front … 1 three-quarter. */
  function face(S, name, q = 0.8) {
    const e = EXPR[name] || EXPR.neutral, ink = S.ink, E = S.eye;
    const off = 7 * q;
    const L = { x: -E.spread + off * 0.8, y: -2 }, R = { x: E.spread + off * 1.15, y: -2 };
    const brow = (c, outer, inner, isLeft) => {
      const xo = isLeft ? c.x - 9 : c.x + 9, xi = isLeft ? c.x + 8 : c.x - 8;
      const mx = (xo + xi) / 2, my = Math.min(outer, inner) - 1.5;
      return `<path d="M ${f(xo)} ${outer - (E.ry - 7.2)} Q ${f(mx)} ${f(my - (E.ry - 7.2))} ${f(xi)} ${inner - (E.ry - 7.2)}" stroke="${ink}" stroke-width="5.5" fill="none" stroke-linecap="round"/>`;
    };
    let s = '';
    const ex = e.extras || [];
    if (ex.includes('blush')) s += `<circle cx="${f(L.x - 4)}" cy="11" r="5" fill="#E9A99C" opacity=".55"/><circle cx="${f(R.x + 4)}" cy="11" r="5" fill="#E9A99C" opacity=".55"/>`;
    s += brow(L, e.brow[0], e.brow[1], true) + brow(R, e.brow[0], e.brow[1], false);
    s += eyeSVG(e.eyes, L.x, L.y, ink, E) + eyeSVG(e.eyes, R.x, R.y, ink, E);
    s += mouthSVG(e.mouth, off * 0.9, 19, ink);
    if (ex.includes('sweat')) s += `<path d="M 40 -34 Q 34 -24 37 -20 A 4.5 4.5 0 0 0 44 -20 Q 46 -24 40 -34 Z" fill="#A9CFF2"/><circle cx="39" cy="-24" r="1.2" fill="#fff"/>`;
    if (ex.includes('tear')) s += `<path d="M ${f(L.x)} 4 Q ${f(L.x - 2)} 12 ${f(L.x)} 18" stroke="#A9CFF2" stroke-width="2.6" fill="none" stroke-linecap="round"/>`;
    if (ex.includes('stress')) s += `<path d="M -40 2 L -35 -3 M -39 8 L -34 3 M 44 2 L 49 -3 M 45 8 L 50 3" stroke="${ink}" stroke-width="2.2" stroke-linecap="round"/>`;
    if (ex.includes('zz')) s += `<text x="34" y="-58" font-family="Comic Sans MS, cursive" font-weight="700" font-size="13" fill="#B1B1B1">z</text><text x="44" y="-76" font-family="Comic Sans MS, cursive" font-weight="700" font-size="17" fill="#B1B1B1">Z</text>`;
    return s;
  }

  /** Shadow-twin face: his own eye shape, narrowed, tilted and glowing. */
  function shadowFace(S, mood = 'smug', q = 0.8) {
    const c = S.shadow, E = S.eye, off = 7 * q;
    const L = { x: -E.spread + off * 0.8, y: -2 }, R = { x: E.spread + off * 1.15, y: -2 };
    const sw = `stroke="${c.eye}" stroke-linecap="round" fill="none"`;
    let eyes = '';
    if (mood === 'smug') {
      eyes = `<path d="M ${f(L.x - 8)} ${L.y} Q ${f(L.x)} ${L.y - 7} ${f(L.x + 8)} ${L.y - 1}" ${sw} stroke-width="4.5"/>` +
             `<path d="M ${f(R.x - 8)} ${R.y - 1} Q ${f(R.x)} ${R.y - 7} ${f(R.x + 8)} ${R.y}" ${sw} stroke-width="4.5"/>`;
    } else if (mood === 'slit') {
      eyes = `<ellipse cx="${f(L.x)}" cy="${L.y}" rx="${E.rx * 0.48}" ry="${E.ry}" transform="rotate(-28 ${f(L.x)} ${L.y})" fill="${c.eye}"/>` +
             `<ellipse cx="${f(R.x)}" cy="${R.y}" rx="${E.rx * 0.48}" ry="${E.ry}" transform="rotate(28 ${f(R.x)} ${R.y})" fill="${c.eye}"/>`;
    } else if (mood === 'sad') {
      eyes = `<path d="M ${f(L.x - 7)} ${L.y + 2} L ${f(L.x + 7)} ${L.y - 3}" ${sw} stroke-width="4"/>` +
             `<path d="M ${f(R.x - 7)} ${R.y - 3} L ${f(R.x + 7)} ${R.y + 2}" ${sw} stroke-width="4"/>`;
    }
    const mouth = mood === 'sad' ? '' : `<path d="M ${f(off - 9)} 16 Q ${f(off)} 25 ${f(off + 9)} 16" ${sw} stroke-width="3.6"/>`;
    return `<g filter="url(#eyeGlow)">${eyes}${mouth}</g>`;
  }

  // ---------------------------------------------------------------- kinematics
  function chain(start, baseAbs, lp, l1, l2) {
    if (lp.ik) {
      const t = lp.ik, dx = t.x - start.x, dy = t.y - start.y;
      const d = Math.min(Math.max(Math.hypot(dx, dy), Math.abs(l1 - l2) + 1e-3), l1 + l2 - 1e-3);
      const base = Math.atan2(dx, dy) / DEG;
      const A = Math.acos(Math.max(-1, Math.min(1, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d)))) / DEG;
      const joint = add(start, mul(dir(base + t.bend * A), l1));
      const end = add(start, mul(dir(base), d));
      return { start, joint, end, lower: Math.atan2(end.x - joint.x, end.y - joint.y) / DEG };
    }
    const upper = baseAbs + lp.a, joint = add(start, mul(dir(upper), l1)), lower = upper + lp.b;
    return { start, joint, end: add(joint, mul(dir(lower), l2)), lower };
  }

  function solve(S, p) {
    const pelvis = { x: p.root.x, y: p.root.y - S.pelvisH };
    const torsoRot = p.root.rot + p.lean;
    const T = (v) => add(pelvis, rot(v, torsoRot));
    const Rt = (v) => add(pelvis, rot(v, p.root.rot));
    const halfW = S.frontHalfW || 46;
    const sN = p.front ? { x: halfW, y: S.shoulderNear.y } : S.shoulderNear, sF = p.front ? { x: -halfW, y: S.shoulderNear.y } : S.shoulderFar;
    const hN = p.front ? { x: 16, y: 0 } : S.hipNear, hF = p.front ? { x: -16, y: 0 } : S.hipFar;
    return {
      pelvis, torsoRot,
      armNear: chain(T(sN), -torsoRot, p.armNear, S.upperArm, S.foreArm),
      armFar: chain(T(sF), -torsoRot, p.armFar, S.upperArm, S.foreArm),
      legNear: chain(Rt(hN), -p.root.rot, p.legNear, S.thigh, S.shin),
      legFar: chain(Rt(hF), -p.root.rot, p.legFar, S.thigh, S.shin),
    };
  }

  function limbSVG(S, c, kind, paint, ink, oW, footAngle = 0) {
    const d = `M ${f(c.start.x)} ${f(c.start.y)} L ${f(c.joint.x)} ${f(c.joint.y)} L ${f(c.end.x)} ${f(c.end.y)}`;
    const w = S.limbW;
    const endShape = (grow, fill) => {
      if (kind === 'arm') { const h = add(c.end, mul(dir(c.lower), 3)); return `<circle cx="${f(h.x)}" cy="${f(h.y)}" r="${S.handR + grow}" fill="${fill}"/>`; }
      const ft = add(c.end, rot({ x: S.footRx * 0.45, y: 1 }, footAngle));
      return `<ellipse cx="${f(ft.x)}" cy="${f(ft.y)}" rx="${S.footRx + grow}" ry="${S.footRy + grow}" transform="rotate(${footAngle} ${f(ft.x)} ${f(ft.y)})" fill="${fill}"/>`;
    };
    const st = 'fill="none" stroke-linecap="round" stroke-linejoin="round"';
    return `<path d="${d}" ${st} stroke="${ink}" stroke-width="${w + 2 * oW}"/>` + endShape(oW, ink) +
           `<path d="${d}" ${st} stroke="${paint}" stroke-width="${w}"/>` + endShape(0, paint);
  }

  // ---------------------------------------------------------------- poses
  const P = (o) => Object.assign({ root: { x: 0, y: 0, rot: 0 }, lean: 0, headTilt: 0,
    armNear: { a: 6, b: 6 }, armFar: { a: -5, b: 6 }, legNear: { a: 3, b: -2 }, legFar: { a: -4, b: -2 } }, o);
  const POSES = {
    standing:   P({}),
    front:      P({ front: true, armNear: { a: 10, b: -4 }, armFar: { a: -10, b: 4 }, legNear: { a: 2, b: 0 }, legFar: { a: -2, b: 0 } }),
    sad:        P({ lean: 5, headTilt: 9, armNear: { a: 3, b: 2 }, armFar: { a: -2, b: 3 }, legFar: { a: -7, b: 0 } }),
    determined: P({ lean: -2, headTilt: -3, armNear: { a: 4, b: 10 }, legNear: { a: 6, b: 0 }, legFar: { a: -9, b: 0 } }),
    walk:       P({ lean: 4, armNear: { a: -22, b: 18 }, armFar: { a: 24, b: 20 }, legNear: { a: 24, b: -4 }, legFar: { a: -22, b: -30 } }),
    run:        P({ root: { x: 0, y: -6, rot: 0 }, lean: 15, headTilt: -5, armNear: { a: -40, b: 90 }, armFar: { a: 45, b: 95 },
                    legNear: { a: 40, b: -70 }, legFar: { a: -48, b: -14 } }),
    sitEdge:    P({ root: { x: 0, y: 'SIT', rot: 0 }, lean: -2, armNear: { a: 30, b: 42 }, armFar: { a: 20, b: 40 },
                    legNear: { a: 88, b: -88 }, legFar: { a: 82, b: -84 } }),
    punch:      P({ lean: 12, headTilt: 5, armNear: { a: 88, b: 4 }, armFar: { a: 25, b: 125 }, legNear: { a: 20, b: -5 }, legFar: { a: -22, b: -3 } }),
    guard:      P({ lean: 8, headTilt: 4, armNear: { a: -8, b: 140 }, armFar: { a: 22, b: 125 }, legNear: { a: 18, b: -5 }, legFar: { a: -18, b: -3 } }),
    curled:     P({ root: { x: 0, y: 'CURL', rot: 0 }, lean: 24, headTilt: 14, armNear: { a: 110, b: 70 }, armFar: { a: 40, b: 150 },
                    legNear: { a: 150, b: -150 }, legFar: { a: 140, b: -140 } }),
  };
  // seated heights depend on leg length (sit on a seat = drop by shin; curl on the floor = drop to near the ground)
  const resolvePose = (S, p) => {
    if (p.root.y === 'SIT') return Object.assign({}, p, { root: { x: 0, y: S.shin, rot: 0 } });
    if (p.root.y === 'CURL') return Object.assign({}, p, { root: { x: 0, y: S.pelvisH - 20, rot: 0 } });
    return p;
  };

  // ---------------------------------------------------------------- renderer
  /**
   * opts: { style ('bean'|'lantern'|'drop'|'moon' or object), pose, expression, q, facing, scale, x, y,
   *         mode 'full'|'headOnly', headRot, shadow: false|{mood}, token: null|'headband' }
   */
  function hero(opts = {}) {
    const o = Object.assign({ style: 'moon', pose: POSES.standing, expression: 'neutral', q: 0.8, facing: 1, scale: 1, x: 0, y: 0, mode: 'full', headRot: 0, shadow: false, token: null }, opts);
    const S = typeof o.style === 'string' ? STYLES[o.style] : o.style;
    const isShadow = !!o.shadow;
    const paint = isShadow ? S.shadow.fill : S.body;
    const ink = isShadow ? S.shadow.fill : S.ink;
    const oW = isShadow ? 0 : S.outline;
    const k = S.head.r / 50; // face/topper scale
    const topper = (S.topper || '').split('INK').join(ink).split('BODY').join(paint);
    const tokenSVG = o.token === 'headband'
      ? `<path d="M -54 -28 Q 0 -42 54 -24" stroke="#E8463A" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M -52 -27 Q -70 -22 -78 -8 M -52 -27 Q -72 -30 -84 -20" stroke="#E8463A" stroke-width="6" fill="none" stroke-linecap="round"/>`
      : '';
    const faceSVG = isShadow ? shadowFace(S, o.shadow.mood || 'smug', o.q) : face(S, o.expression, o.q);
    // head contents in head space, scaled to head radius
    const headDecor = `<g transform="scale(${f(k)})">${topper}${faceSVG}${tokenSVG}</g>`;
    const headDisc = (withOutline) => (withOutline && oW ? `<circle r="${S.head.r + oW}" fill="${ink}"/>` : '') + `<circle r="${S.head.r}" fill="${paint}"/>`;

    const fx = o.facing === -1 ? -1 : 1;
    const open = `<g transform="translate(${f(o.x)} ${f(o.y)}) scale(${f(fx * o.scale)} ${f(o.scale)})">`;
    if (o.mode === 'headOnly') {
      return open + `<g transform="rotate(${o.headRot})">${`<g transform="scale(${f(k)})">${topper}</g>`}${headDisc(true)}${headDecor}</g></g>`;
    }
    const p = resolvePose(S, o.pose), J = solve(S, p);
    const far = p.front ? '' : `<g opacity="${isShadow ? 1 : S.farOpacity}">` +
      limbSVG(S, J.legFar, 'leg', paint, ink, oW) + limbSVG(S, J.armFar, 'arm', paint, ink, oW) + `</g>`;
    const neck = S.neck ? `<path d="M ${S.neck.from.x} ${S.neck.from.y} L ${S.neck.to.x} ${S.neck.to.y}" stroke="${ink}" stroke-width="${S.neck.w + 2 * oW}" stroke-linecap="round"/>` +
                          `<path d="M ${S.neck.from.x} ${S.neck.from.y} L ${S.neck.to.x} ${S.neck.to.y}" stroke="${paint}" stroke-width="${S.neck.w}" stroke-linecap="round"/>` : '';
    const hc = S.head.c;
    const headGroup = S.head.separate
      ? `<g transform="rotate(${p.headTilt} ${hc.x} ${hc.y + S.head.r * 0.8})"><g transform="translate(${hc.x} ${hc.y})">` +
        `<g transform="scale(${f(k)})">${topper}</g>${headDisc(true)}${headDecor}</g></g>`
      : `<g transform="rotate(${p.headTilt} ${hc.x} ${hc.y + 27})"><g transform="translate(${hc.x} ${hc.y})">${headDecor}</g></g>`;
    const torso = `<g transform="translate(${f(J.pelvis.x)} ${f(J.pelvis.y)}) rotate(${f(J.torsoRot)})">` + neck +
      `<path d="${S.torsoPath}" fill="${paint}" stroke="${ink}" stroke-width="${oW * 2}" stroke-linejoin="round" paint-order="stroke"/>` +
      headGroup + `</g>`;
    const frontLimbs = p.front ? limbSVG(S, J.legFar, 'leg', paint, ink, oW, 180) + limbSVG(S, J.armFar, 'arm', paint, ink, oW) : '';
    const near = frontLimbs + limbSVG(S, J.legNear, 'leg', paint, ink, oW) + limbSVG(S, J.armNear, 'arm', paint, ink, oW);
    const body = far + torso + near;
    if (!isShadow) return open + body + `</g>`;
    const silhouette = body.replace(faceSVG, '');
    const tint = (svg, c) => svg.split(S.shadow.fill).join(c);
    return open +
      `<g filter="url(#glowWide)" opacity=".85">${tint(silhouette, S.shadow.glow)}</g>` +
      `<g filter="url(#glowRim)">${tint(silhouette, S.shadow.rim)}</g>` + body + `</g>`;
  }

  g.TOS = { STYLES, EXPR, POSES, hero, face, shadowFace, solve };
})(window);
