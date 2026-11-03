/* The Other Self ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â thumbnail generator prototype (framework-free; port 1:1 to a Remotion <Still>).
 * Depends on hero-rig.js (proto copy with two thumb upgrades: opts.noHead + TOS.headAnchor()).
 * Layer stack: bg ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ environment (back) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ accent light ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ hero body (flat ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ form shade ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ rim) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢
 *              thumbnail head (painterly) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ environment (front) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ FX ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ grade (vignette, grain) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ text ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ debug.
 * All coordinates are 1280ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â720 screen pixels unless noted "head space" (head centre 0,0, nominal radius 50).
 */
(function (g) {
  const W = 1280, H = 720;
  const S = TOS.STYLES.moon;
  const f = (n) => (Math.round(n * 100) / 100).toString();
  let uid = 0; const id = (p) => `${p}${++uid}`;

  // ------------------------------------------------------------ colour helpers
  const hex = (c) => { c = c.replace('#', ''); if (c.length === 3) c = c.split('').map((x) => x + x).join(''); return [0, 2, 4].map((i) => parseInt(c.substr(i, 2), 16)); };
  const toHex = (a) => '#' + a.map((v) => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, '0')).join('');
  const mix = (a, b, t) => { const A = hex(a), B = hex(b); return toHex(A.map((v, i) => v + (B[i] - v) * t)); };
  const unit = (x, y) => { const l = Math.hypot(x, y) || 1; return { x: x / l, y: y / l }; };
  const rotv = (v, d) => { const c = Math.cos(d * Math.PI / 180), s = Math.sin(d * Math.PI / 180); return { x: v.x * c - v.y * s, y: v.x * s + v.y * c }; };

  // ------------------------------------------------------------ thumbnail expressions (head space)
  // brow: y of outer / inner end (eye centre is y ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Â¹ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢1). lid: angled upper-lid cut {y offset from eye centre, angle; + = inner side lower}.
  const TX = {
    glare:    { brow: [-29, -11], browCurve: 1, lid: { y: -3.5, a: 24 }, eye: 1.32, look: [1, 0.1], mouth: 'grit', extras: [] },
    resolve:  { brow: [-27, -14], browCurve: 1.5, lid: { y: -4.5, a: 15 }, eye: 1.3, look: [1, 0], mouth: 'pout', extras: ['sweat'] },
    tired:    { brow: [-18, -26], browCurve: 0.5, lid: { y: -2, a: -10 }, eye: 1.26, look: [0.8, 0.7], mouth: 'o', extras: ['bags'] },
    shocked:  { brow: [-28, -30], lid: null, eye: 1.5, look: [0, 0], mouth: 'o', extras: ['sweat'] },
    sad:      { brow: [-17, -27], lid: { y: -3, a: -12 }, eye: 1.25, look: [0.3, 0.6], mouth: 'frown', extras: ['bags'] },
    hopeful:  { brow: [-25, -28], lid: null, eye: 1.4, look: [0.6, -0.4], mouth: 'smile', extras: [] },
    anxious:  { brow: [-19, -28], lid: null, eye: 1.15, look: [0.4, 0], mouth: 'wobble', extras: ['sweat', 'bags'] },
    content:  { brow: [-22, -23], lid: null, eye: 1.3, look: [0.5, 0], mouth: 'smile', extras: [] },
  };

  function thumbFace(ex, q, light) {
    const ink = S.ink, E = S.eye, k = ex.eye;
    const rx = E.rx * k, ry = E.ry * k, spread = E.spread + 1.5, off = 7 * q;
    const eyes = [{ x: -spread + off * 0.8, y: -1, left: true }, { x: spread + off * 1.15, y: -1, left: false }];
    const lx = (ex.look[0] || 0) * 1.8, ly = (ex.look[1] || 0) * 1.8;
    let back = '', s = '';
    eyes.forEach((e) => {
      const cx = e.x + lx, cy = e.y + ly;
      // eye bags (behind the eye)
      if (ex.extras.includes('bags')) {
        back += `<ellipse cx="${f(e.x)}" cy="${f(e.y + ry * 0.75)}" rx="${f(rx * 1.9)}" ry="${f(ry * 0.85)}" fill="#6E4C5C" opacity=".38" filter="url(#soft3)"/>`;
        s += `<path d="M ${f(e.x - rx * 1.25)} ${f(e.y + ry + 1.5)} Q ${f(e.x)} ${f(e.y + ry + 6.5)} ${f(e.x + rx * 1.25)} ${f(e.y + ry + 1.5)}" stroke="${ink}" stroke-width="2.2" opacity=".55" fill="none" stroke-linecap="round"/>`;
      }
      // eyeball with angled upper-lid cut
      let clip = '', lidLine = '';
      if (ex.lid) {
        const a = e.left ? ex.lid.a : -ex.lid.a, ly0 = e.y + ex.lid.y;
        const cid = id('lid');
        clip = ` clip-path="url(#${cid})"`;
        s += `<clipPath id="${cid}"><rect x="${f(e.x - 30)}" y="${f(ly0)}" width="60" height="40" transform="rotate(${a} ${f(e.x)} ${f(ly0)})"/></clipPath>`;
        const d = rotv({ x: rx + 2.6, y: 0 }, a);
        lidLine = `<path d="M ${f(e.x - d.x)} ${f(ly0 - d.y)} L ${f(e.x + d.x)} ${f(ly0 + d.y)}" stroke="${ink}" stroke-width="3.4" stroke-linecap="round"/>`;
      }
      const hlY = ex.lid ? cy - ry * 0.05 : cy - ry * 0.42;
      s += `<g${clip}><ellipse cx="${f(cx)}" cy="${f(cy)}" rx="${f(rx)}" ry="${f(ry)}" fill="${ink}"/>` +
           `<circle cx="${f(cx - rx * 0.36)}" cy="${f(hlY)}" r="${f(rx * 0.36)}" fill="#fff"/>` +
           `<circle cx="${f(cx - rx * 0.36)}" cy="${f(hlY)}" r="${f(rx * 0.36)}" fill="${light}" opacity=".18"/></g>` + lidLine;
      // brow: thick, nearly straight (thumbnail brows read as angles, not arcs)
      const xo = e.left ? e.x - 11.5 : e.x + 11.5, xi = e.left ? e.x + 10 : e.x - 10;
      const yo = ex.brow[0], yi = ex.brow[1], mx = (xo + xi) / 2, my = (yo + yi) / 2 - (ex.browCurve == null ? 2 : ex.browCurve);
      s += `<path d="M ${f(xo)} ${yo} Q ${f(mx)} ${f(my)} ${f(xi)} ${yi}" stroke="${ink}" stroke-width="7.2" fill="none" stroke-linecap="round"/>`;
    });
    const mx = off * 0.9 + lx * 0.6, my = 21;
    const st = `stroke="${ink}" stroke-width="3.8" fill="none" stroke-linecap="round" stroke-linejoin="round"`;
    const M = {
      grit: `<path d="M ${f(mx - 9)} ${my + 2} Q ${f(mx - 1)} ${my - 5} ${f(mx + 10)} ${my - 1}" ${st}/>`,
      pout: `<path d="M ${f(mx - 5.5)} ${my + 2} Q ${f(mx)} ${my - 3} ${f(mx + 5.5)} ${my + 2}" ${st}/>`,
      o: `<ellipse cx="${f(mx)}" cy="${my + 1}" rx="3.2" ry="3.9" fill="${ink}"/>`,
      frown: `<path d="M ${f(mx - 7)} ${my + 3} Q ${f(mx)} ${my - 3} ${f(mx + 7)} ${my + 3}" ${st}/>`,
      smile: `<path d="M ${f(mx - 7)} ${my - 2} Q ${f(mx)} ${my + 5} ${f(mx + 7)} ${my - 2}" ${st}/>`,
      wobble: `<path d="M ${f(mx - 8)} ${my} Q ${f(mx - 4)} ${my - 3} ${f(mx)} ${my} Q ${f(mx + 4)} ${my + 3} ${f(mx + 8)} ${my}" ${st}/>`,
      flat: `<path d="M ${f(mx - 6)} ${my} L ${f(mx + 6)} ${my}" ${st}/>`,
    };
    s += M[ex.mouth] || '';
    if (ex.extras.includes('sweat')) {
      s += `<g transform="translate(${f(spread + off + 20)} -27) scale(1.55)"><path d="M 0 -9 Q -6 0 -4.2 3.2 A 4.8 4.8 0 0 0 4.2 3.2 Q 6 0 0 -9 Z" fill="#A9CFF2" stroke="${ink}" stroke-width="1.3"/>` +
           `<ellipse cx="-1.6" cy="1" rx="1.1" ry="1.8" fill="#fff"/></g>`;
    }
    return { back, front: s };
  }

  /** Painterly thumbnail head. h = {x, y, r, tilt, facing, q}, light = {x, y, color}. */
  function thumbHead(h, ex, light) {
    const k = h.r / 50, fx = h.facing === -1 ? -1 : 1;
    let l = unit(light.x - h.x, light.y - h.y);
    l = rotv(l, -(h.tilt || 0)); l.x *= fx;                                         // light dir in head space
    const skinHi = mix(S.body, '#FFF4E2', 0.45), skinLo = mix(S.body, '#5A3A26', 0.38);
    const gid = id('hg'), cid = id('hc'), rim = id('rm'), rimW = id('rw'), tint = id('ht');
    const ink = S.ink, ow = 3.4;
    const topper = S.topper.split('INK').join(ink).split('BODY').join(`url(#${id('lf')})`)
      .replace('stroke-width="3.6"', 'stroke-width="4.6"').replace('stroke-width="3"', 'stroke-width="3.6"');
    const leafId = 'lf' + uid;
    const face = thumbFace(ex, h.q == null ? 0.8 : h.q, light.color);
    const rimCol = mix(light.color, '#ffffff', 0.45);
    return `<g transform="translate(${f(h.x)} ${f(h.y)}) rotate(${f(h.tilt || 0)}) scale(${f(fx * k)} ${f(k)})">
  <defs>
    <radialGradient id="${gid}" gradientUnits="userSpaceOnUse" cx="${f(l.x * 16)}" cy="${f(l.y * 16 - 6)}" r="74">
      <stop offset="0" stop-color="${skinHi}"/><stop offset=".42" stop-color="${S.body}"/><stop offset=".8" stop-color="${mix(S.body, skinLo, 0.6)}"/><stop offset="1" stop-color="${skinLo}"/></radialGradient>
    <radialGradient id="${tint}" gradientUnits="userSpaceOnUse" cx="${f(l.x * 52)}" cy="${f(l.y * 52)}" r="70">
      <stop offset="0" stop-color="${light.color}" stop-opacity=".55"/><stop offset="1" stop-color="${light.color}" stop-opacity="0"/></radialGradient>
    <linearGradient id="${leafId}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${skinHi}"/><stop offset="1" stop-color="${mix(S.body, skinLo, 0.5)}"/></linearGradient>
    <clipPath id="${cid}"><circle r="50"/></clipPath>
    <mask id="${rim}" maskUnits="userSpaceOnUse" x="-80" y="-80" width="160" height="160"><circle r="50" fill="#fff"/><circle cx="${f(-l.x * 5)}" cy="${f(-l.y * 5)}" r="50.5" fill="#000"/></mask>
    <mask id="${rimW}" maskUnits="userSpaceOnUse" x="-80" y="-80" width="160" height="160"><circle r="50" fill="#fff"/><circle cx="${f(-l.x * 17)}" cy="${f(-l.y * 17)}" r="52" fill="#000"/></mask>
  </defs>
  ${topper}
  <circle r="${50 + ow}" fill="${ink}"/>
  <circle r="50" fill="url(#${gid})"/>
  <g clip-path="url(#${cid})">
    <circle r="50" fill="url(#${tint})" style="mix-blend-mode:screen"/>
    <g filter="url(#soft4)" opacity=".55"><circle r="50" fill="${rimCol}" mask="url(#${rimW})"/></g>
    <g filter="url(#soft1)"><circle r="50" fill="${rimCol}" mask="url(#${rim})"/></g>
  </g>
  ${face.back}${face.front}
</g>`;
  }

  // ------------------------------------------------------------ body (rig) with lighting passes
  const P = (o) => Object.assign({ root: { x: 0, y: 0, rot: 0 }, lean: 0, headTilt: 0,
    armNear: { a: 6, b: 6 }, armFar: { a: -5, b: 6 }, legNear: { a: 3, b: -2 }, legFar: { a: -4, b: -2 } }, o);

  /** Place the rig so that its head centre lands on (hx, hy) with head radius r. */
  function placeHero(pose, hx, hy, r, facing = 1) {
    const scale = r / S.head.r;
    const a = TOS.headAnchor({ pose, scale, facing, x: 0, y: 0 });
    return { pose, scale, facing, x: hx - a.x, y: hy - a.y, tilt: a.tilt };
  }
  /** screen point ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ rig space for IK targets */
  const toRig = (pl, p) => ({ x: (p.x - pl.x) / (pl.scale * pl.facing), y: (p.y - pl.y) / pl.scale });

  function litBody(pl, light) {
    const base = { style: 'moon', pose: pl.pose, scale: pl.scale, facing: pl.facing, x: pl.x, y: pl.y, noHead: true };
    const flat = TOS.hero(base);
    const white = TOS.hero(Object.assign({}, base, { style: Object.assign({}, S, { body: '#fff', ink: 'none', farOpacity: 1 }) }));
    const mid = id('bm'), sh = id('bs'), tn = id('bt'), rf = id('rf');
    const l = unit(light.x - pl.x, light.y - (pl.y - 200 * pl.scale));
    const d = 7;
    return `<defs>
  <mask id="${mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}">${white}</mask>
  <radialGradient id="${sh}" gradientUnits="userSpaceOnUse" cx="${light.x}" cy="${light.y}" r="760">
    <stop offset="0" stop-color="#1a0e06" stop-opacity="0"/><stop offset=".3" stop-color="#1a0e06" stop-opacity="0"/><stop offset="1" stop-color="#1a0e06" stop-opacity=".62"/></radialGradient>
  <radialGradient id="${tn}" gradientUnits="userSpaceOnUse" cx="${light.x}" cy="${light.y}" r="420">
    <stop offset="0" stop-color="${light.color}" stop-opacity=".55"/><stop offset="1" stop-color="${light.color}" stop-opacity="0"/></radialGradient>
  <filter id="${rf}" filterUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}">
    <feOffset in="SourceAlpha" dx="${f(-l.x * d)}" dy="${f(-l.y * d)}" result="o"/>
    <feComposite in="SourceAlpha" in2="o" operator="out" result="e"/>
    <feGaussianBlur in="e" stdDeviation="1.6" result="eb"/>
    <feComposite in="eb" in2="SourceAlpha" operator="in" result="ei"/>
    <feFlood flood-color="${mix(light.color, '#ffffff', 0.45)}"/><feComposite in2="ei" operator="in"/>
  </filter>
</defs>
${flat}
<g mask="url(#${mid})"><rect width="${W}" height="${H}" fill="url(#${sh})"/><rect width="${W}" height="${H}" fill="url(#${tn})" style="mix-blend-mode:screen"/></g>
<g filter="url(#${rf})">${white}</g>`;
  }

  /** A loose hand (for holding props drawn after the body). */
  const hand = (x, y, r, light) => `<circle cx="${f(x)}" cy="${f(y)}" r="${f(r + S.outline * r / S.handR * 0.9)}" fill="${S.ink}"/>` +
    `<circle cx="${f(x)}" cy="${f(y)}" r="${f(r)}" fill="${S.body}"/>` +
    `<circle cx="${f(x)}" cy="${f(y)}" r="${f(r)}" fill="${light.color}" opacity=".12"/>`;

  // ------------------------------------------------------------ props
  const SEG = { 0: 'abcdef', 1: 'bc', 2: 'abged', 3: 'abgcd', 4: 'fgbc', 5: 'afgcd', 6: 'afgedc', 7: 'abc', 8: 'abcdefg', 9: 'abcdfg' };
  function sevenSeg(str, x, y, h, color) {
    const w = h * 0.52, t = h * 0.12; let cx = x, out = '', off = '';
    const seg = (n, X, Y) => {
      const hz = (sx, sy) => `<rect x="${f(sx + t * 0.6)}" y="${f(sy - t / 2)}" width="${f(w - t * 1.2)}" height="${f(t)}" rx="${f(t / 2)}"/>`;
      const vt = (sx, sy) => `<rect x="${f(sx - t / 2)}" y="${f(sy + t * 0.6)}" width="${f(t)}" height="${f(h / 2 - t * 1.2)}" rx="${f(t / 2)}"/>`;
      return { a: hz(X, Y), g: hz(X, Y + h / 2), d: hz(X, Y + h), f: vt(X, Y), b: vt(X + w, Y), e: vt(X, Y + h / 2), c: vt(X + w, Y + h / 2) }[n];
    };
    for (const ch of str) {
      if (ch === ':') { out += `<circle cx="${f(cx + t)}" cy="${f(y + h * 0.3)}" r="${f(t * 0.62)}"/><circle cx="${f(cx + t)}" cy="${f(y + h * 0.7)}" r="${f(t * 0.62)}"/>`; cx += t * 2 + h * 0.16; continue; }
      const on = SEG[ch] || '';
      for (const s of 'abcdefg') (on.includes(s) ? (out += seg(s, cx, y)) : (off += seg(s, cx, y)));
      cx += w + h * 0.24;
    }
    return { svg: `<g fill="${color}" opacity=".09">${off}</g>` +
      `<g fill="${color}" filter="url(#glow14)" opacity=".95">${out}</g><g fill="${color}" filter="url(#glow4)">${out}</g>` +
      `<g fill="${mix(color, '#ffffff', 0.55)}">${out}</g>`, width: cx - x };
  }

  function glowSpot(x, y, r, color, op = 0.5) {
    const gid = id('gs');
    return `<radialGradient id="${gid}" gradientUnits="userSpaceOnUse" cx="${x}" cy="${y}" r="${r}"><stop offset="0" stop-color="${color}" stop-opacity="${op}"/>` +
      `<stop offset=".45" stop-color="${color}" stop-opacity="${op * 0.3}"/><stop offset="1" stop-color="${color}" stop-opacity="0"/></radialGradient>` +
      `<rect width="${W}" height="${H}" fill="url(#${gid})" style="mix-blend-mode:screen"/>`;
  }

  // ------------------------------------------------------------ scene presets
  const PRESETS = {
    /* DAY-counter close-up: lying in bed, glaring at a glowing alarm clock. */
    bedClock: {
      text: 'DAY 1.', textLayout: 'top-left', accent: '#FFA53D', expression: 'glare', bg: '#0A0908',
      head: { x: 455, y: 420, r: 165, tilt: -9 }, light: { x: 1035, y: 470 }, props: { clock: '5:00' },
      build(c, L) {
        const hd = c.head, acc = c.accent;
        const clk = sevenSeg(c.props.clock || '5:00', 0, 0, 104, acc);
        const cw = clk.width, clX = 1035 - cw / 2;
        const back = `
  <rect x="742" y="232" width="50" height="520" rx="25" fill="#191C26" stroke="#373E52" stroke-width="5"/>
  <rect x="1" y="1" width="0" height="0"/>
  <path d="M 300 520 C 300 470 360 455 470 462 L 720 470 C 790 474 806 520 800 560 C 794 610 760 632 700 632 L 380 630 C 320 628 300 580 300 520 Z" fill="#262B39" stroke="#3E4659" stroke-width="5"/>
  <rect x="240" y="604" width="580" height="160" rx="22" fill="#1B1F2C" stroke="#363D52" stroke-width="5"/>
  <ellipse cx="${hd.x + 10}" cy="${hd.y + hd.r * 0.92}" rx="${hd.r * 0.95}" ry="${hd.r * 0.22}" fill="#000" opacity=".55" filter="url(#soft12)"/>`;
        const right = `
  <rect x="830" y="585" width="430" height="190" rx="28" fill="#12141B" stroke="#30364A" stroke-width="5"/>
  <circle cx="1045" cy="672" r="12" fill="#2E3443"/>
  <rect x="848" y="392" width="374" height="178" rx="56" fill="#0F1118" stroke="#3A4258" stroke-width="6"/>
  <rect x="876" y="416" width="318" height="130" rx="34" fill="#04060B"/>
  <g transform="translate(${f(clX)} 429)">${clk.svg}</g>`;
        const front = `
  <path d="M -40 388 C 80 336 220 340 316 432 C 372 488 404 548 452 592 C 500 630 590 644 700 652 L 836 662 L 836 760 L -40 760 Z" fill="url(#blanket)" stroke="#475378" stroke-width="5" stroke-linejoin="round"/>
  <path d="M 120 470 C 180 520 210 600 230 700 M 330 560 C 360 610 380 660 390 720" stroke="#11162A" stroke-width="7" fill="none" stroke-linecap="round" opacity=".7"/>
  <path d="M 316 432 C 372 488 404 548 452 592 C 500 630 590 644 700 652" stroke="${mix(acc, '#ffffff', .3)}" stroke-width="3" fill="none" opacity=".35"/>`;
        return { back: back + right + glowSpot(1035, 480, 520, acc, 0.55), hero: L.head(), front };
      },
    },

    /* Threshold: hand on the door handle, light leaking through the gap. */
    doorLight: {
      text: 'JUST START.', textLayout: 'top-center', accent: '#FFB547', expression: 'resolve', bg: '#0B0A0C',
      head: { x: 760, y: 402, r: 146 }, light: { x: 958, y: 420 }, props: {},
      build(c, L) {
        const acc = c.accent, hd = c.head;
        const handle = { x: 1004, y: 612 };
        const pose = P({ lean: 7, headTilt: -2, armFar: { a: -24, b: 30 }, legNear: { a: 20, b: -6 }, legFar: { a: -16, b: -4 } });
        let pl = placeHero(pose, hd.x, hd.y, hd.r, 1);
        const t = toRig(pl, handle);
        pose.armNear = { ik: { x: t.x, y: t.y, bend: -1 } };
        pl = placeHero(pose, hd.x, hd.y, hd.r, 1);
        const gap = 958;
        const back = `
  <rect width="${W}" height="${H}" fill="url(#wallDoor)"/>
  <rect x="${gap - 34}" y="-10" width="30" height="740" fill="#16120F" stroke="#2E2620" stroke-width="4"/>
  <rect x="${gap + 12}" y="-10" width="320" height="740" fill="#17130F"/>
  <rect x="${gap + 60}" y="40" width="210" height="300" rx="10" fill="none" stroke="#231D17" stroke-width="6"/>
  <rect x="${gap + 60}" y="400" width="210" height="300" rx="10" fill="none" stroke="#231D17" stroke-width="6"/>
  <rect x="${gap - 4}" y="-10" width="18" height="740" fill="${acc}" filter="url(#glow40)" opacity=".9"/>
  <rect x="${gap - 4}" y="-10" width="18" height="740" fill="${acc}" filter="url(#glow14)"/>
  <rect x="${gap}" y="-10" width="10" height="740" fill="${mix(acc, '#ffffff', 0.75)}"/>
  <path d="M ${gap + 12} -10 L ${gap + 12} 730" stroke="${mix(acc, '#ffffff', .3)}" stroke-width="3" opacity=".8"/>
  ${glowSpot(gap + 5, 420, 620, acc, 0.42)}
  <rect x="${handle.x - 14}" y="${handle.y - 70}" width="34" height="150" rx="12" fill="#221C17" stroke="#4A3D2F" stroke-width="4"/>`;
        const lever = `<rect x="${handle.x - 22}" y="${handle.y - 13}" width="74" height="24" rx="12" fill="#2C241D" stroke="${mix(acc, '#3a2a1a', .5)}" stroke-width="4"/>`;
        // the hand goes over the lever
        const J = TOS.solve(S, TOS.resolvePose(S, pose));
        const hs = { x: pl.x + pl.scale * J.armNear.end.x, y: pl.y + pl.scale * J.armNear.end.y };
        const heroSVG = litBody(pl, L.light) + lever + hand(hs.x + 4, hs.y + 2, S.handR * pl.scale * 1.15, L.light) + L.head({ tilt: pl.tilt });
        return { back, hero: heroSVG, front: '' };
      },
    },

    /* Night scroll: sitting up in bed, face lit from below by the phone. */
    phoneBed: {
      text: '3 AM.', textLayout: 'top-center', accent: '#8FD3FF', expression: 'tired', bg: '#07090C',
      head: { x: 548, y: 402, r: 152 }, light: { x: 790, y: 540 }, props: { bubbles: true },
      build(c, L) {
        const acc = c.accent, hd = c.head;
        const phone = { x: 752, y: 506, a: -12 };
        const pose = P({ root: { x: 0, y: S.shin, rot: 0 }, lean: 9, headTilt: 9, legNear: { a: 88, b: -88 }, legFar: { a: 82, b: -84 } });
        let pl = placeHero(pose, hd.x, hd.y, hd.r, 1);
        const tn = toRig(pl, { x: phone.x - 40, y: phone.y + 62 }), tf = toRig(pl, { x: phone.x + 46, y: phone.y + 36 });
        pose.armNear = { ik: { x: tn.x, y: tn.y, bend: -1 } };
        pose.armFar = { a: 40, b: 60 };   // hidden under the blanket; its hand is placed on the phone edge below
        pl = placeHero(pose, hd.x, hd.y, hd.r, 1);
        const J = TOS.solve(S, TOS.resolvePose(S, pose));
        const hn = { x: pl.x + pl.scale * J.armNear.end.x, y: pl.y + pl.scale * J.armNear.end.y };
        const back = `
  <path d="M 70 330 C 70 270 120 250 200 252 L 470 262 C 540 266 560 300 560 360 L 556 540 C 554 600 520 620 460 620 L 160 616 C 100 614 72 590 72 530 Z" fill="#191D29" stroke="#30374A" stroke-width="5"/>
`;
        const ph = `<g transform="translate(${phone.x} ${phone.y}) rotate(${phone.a})">
    <rect x="-70" y="-110" width="140" height="220" rx="40" fill="${acc}" filter="url(#glow40)" opacity=".9"/>
    <rect x="-50" y="-92" width="100" height="184" rx="20" fill="#0C0E15" stroke="#465070" stroke-width="5"/>
    <rect x="-41" y="-82" width="82" height="164" rx="13" fill="url(#screen)"/>
    <rect x="-30" y="-64" width="60" height="16" rx="8" fill="#fff" opacity=".55"/><rect x="-30" y="-38" width="44" height="12" rx="6" fill="#fff" opacity=".35"/>
    <rect x="-30" y="-14" width="60" height="44" rx="10" fill="#fff" opacity=".25"/></g>`;
        let bubbles = '';
        if (c.props.bubbles) {
          const B = [[892, 396, 30, 'heart'], [952, 304, 24, 'dot'], [925, 222, 18, 'heart'], [1000, 182, 13, 'dot'], [1050, 250, 10, ''], [880, 290, 8, ''], [1052, 128, 7, '']];
          B.forEach(([x, y, r, ic]) => {
            const icon = ic === 'heart' ? `<path d="M 0 ${f(r * 0.38)} C ${f(-r * 0.75)} ${f(-r * 0.1)} ${f(-r * 0.45)} ${f(-r * 0.62)} 0 ${f(-r * 0.25)} C ${f(r * 0.45)} ${f(-r * 0.62)} ${f(r * 0.75)} ${f(-r * 0.1)} 0 ${f(r * 0.38)} Z" fill="#fff"/>`
              : ic === 'dot' ? `<circle r="${f(r * 0.32)}" fill="#fff"/>` : '';
            bubbles += `<g transform="translate(${x} ${y})"><rect x="${-r * 1.25}" y="${-r * 1.25}" width="${r * 2.5}" height="${r * 2.5}" rx="${r * 0.8}" fill="${acc}" filter="url(#glow14)"/>` +
              `<rect x="${-r}" y="${-r}" width="${r * 2}" height="${r * 2}" rx="${r * 0.6}" fill="${mix(acc, '#ffffff', 0.25)}" stroke="${mix(acc, '#ffffff', 0.7)}" stroke-width="2"/>${icon}</g>`;
          });
          bubbles = `<path d="M 838 418 C 910 350 970 270 1000 160" stroke="${acc}" stroke-width="22" fill="none" opacity=".35" filter="url(#glow14)" stroke-linecap="round"/>` + bubbles;
        }
        const blanket = `<path d="M -40 600 C 150 560 330 600 470 622 C 600 642 700 610 860 618 C 1020 626 1140 596 1320 612 L 1320 760 L -40 760 Z" fill="url(#blanket2)" stroke="#2C3550" stroke-width="5"/>
  <path d="M 560 640 C 640 652 760 640 900 630" stroke="${mix(acc, '#ffffff', .2)}" stroke-width="4" fill="none" opacity=".45" filter="url(#soft1)"/>
  <path d="M 200 650 C 260 690 280 720 290 760 M 1000 650 C 1040 690 1050 720 1060 760" stroke="#0A0D18" stroke-width="7" fill="none" opacity=".8"/>`;
        const hfo = rotv({ x: 50, y: 34 }, phone.a), hf = { x: phone.x + hfo.x, y: phone.y + hfo.y };
        const heroSVG = litBody(pl, L.light) + L.head({ tilt: pl.tilt }) + ph + hand(hf.x, hf.y, S.handR * pl.scale * 1.05, L.light) + hand(hn.x, hn.y, S.handR * pl.scale * 1.12, L.light);
        return { back: back + glowSpot(phone.x, phone.y - 40, 560, acc, 0.5), hero: heroSVG, front: blanket + bubbles };
      },
    },
  };

  // ------------------------------------------------------------ compositor
  function render(cfg, mount) {
    uid = 0;
    const pre = PRESETS[cfg.preset] || PRESETS.bedClock;
    const c = Object.assign({}, pre, cfg);
    c.head = Object.assign({}, pre.head, cfg.head || {});
    c.light = Object.assign({}, pre.light, cfg.light || {});
    c.props = Object.assign({}, pre.props, cfg.props || {});
    // measured rule: top-left is only for short labels ("DAY 1."); longer text goes full-width centred so it stays big on mobile
    if (c.textLayout === 'top-left' && !cfg.textLayout && (c.text || '').replace(/\s/g, '').length > 6) c.textLayout = 'top-center';
    const accent = c.accent;
    const light = { x: c.light.x, y: c.light.y, color: accent };
    const ex = Object.assign({}, TX[c.expression] || TX.glare);
    if (cfg.look) ex.look = cfg.look;
    ex.extras = (ex.extras || []).slice();
    (cfg.extras || []).forEach((e) => ex.extras.includes(e) || ex.extras.push(e));
    (cfg.noExtras || []).forEach((e) => (ex.extras = ex.extras.filter((x) => x !== e)));
    const L = { light, head: (o = {}) => thumbHead(Object.assign({ facing: 1, q: 0.8 }, c.head, o, cfg.head && cfg.head.tilt != null ? { tilt: cfg.head.tilt } : {}), ex, light) };
    const scene = pre.build(c, L);
    const zoom = c.zoom || 1, fx = c.focus ? c.focus.x : c.head.x, fy = c.focus ? c.focus.y : c.head.y;
    const zt = `translate(${fx} ${fy}) scale(${zoom}) translate(${-fx} ${-fy})`;
    const twin = c.twin ? `<g opacity="${c.twin.opacity || 0.9}">${TOS.hero({ style: 'moon', shadow: { mood: c.twin.mood || 'smug' }, scale: c.twin.scale || 1.6, x: c.twin.x || 1100, y: c.twin.y || 760, facing: c.twin.facing || 1 })}</g>` : '';
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<defs>
  <filter id="soft1" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.2"/></filter>
  <filter id="soft3" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
  <filter id="soft4" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="soft12" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="12"/></filter>
  <filter id="glow4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="glow14" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="glow40" x="-300%" y="-100%" width="700%" height="300%"><feGaussianBlur stdDeviation="40"/></filter>
  <filter id="glowWide" x="-60%" y="-40%" width="220%" height="180%"><feGaussianBlur stdDeviation="16"/></filter>
  <filter id="glowRim" x="-40%" y="-30%" width="180%" height="160%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="eyeGlow" x="-100%" y="-200%" width="300%" height="500%"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  <filter id="textShadow" x="-10%" y="-30%" width="120%" height="170%"><feDropShadow dx="0" dy="7" stdDeviation="7" flood-color="#000" flood-opacity=".75"/></filter>
  <radialGradient id="vignette" cx="50%" cy="50%" r="75%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".7"/></radialGradient>
  <linearGradient id="blanket" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2E3A60"/><stop offset="1" stop-color="#161C33"/></linearGradient>
  <linearGradient id="blanket2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1D2438"/><stop offset="1" stop-color="#0D101B"/></linearGradient>
  <linearGradient id="wallDoor" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#080707"/><stop offset="1" stop-color="#141110"/></linearGradient>
  <linearGradient id="screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(accent, '#ffffff', 0.55)}"/><stop offset="1" stop-color="${accent}"/></linearGradient>
</defs>
${c.baseImage
  // text-only mode: an externally finished image (e.g. Higgsfield painterly pass) is the background; we only add the text
  ? `<image href="${esc(c.baseImage)}" x="0" y="0" width="${W}" height="${H}" preserveAspectRatio="xMidYMid slice"/>`
  : `<rect width="${W}" height="${H}" fill="${c.bg}"/>
<g transform="${zt}">${scene.back}${twin}${scene.hero}${scene.front}</g>
<rect width="${W}" height="${H}" fill="url(#vignette)"/>
<rect width="${W}" height="${H}" filter="url(#grain)" opacity="${c.grain == null ? 0.07 : c.grain}" style="mix-blend-mode:overlay"/>`}
<text id="title" font-family="'${c.font || 'Fredoka'}', 'Baloo 2', 'Nunito', sans-serif" font-weight="${c.fontWeight || 700}" fill="#FFFFFF"
  stroke="#06070B" stroke-width="12" stroke-linejoin="round" paint-order="stroke" filter="url(#textShadow)" letter-spacing="3">${esc(c.text)}</text>
<g id="debug"></g>
</svg>`;
    mount.innerHTML = svg;
    layoutText(mount.querySelector('#title'), c);
    if (c.debug) drawDebug(mount.querySelector('#debug'), c);
  }
  const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');

  /** Fit text: max size, then shrink to fit the allowed width. */
  function layoutText(t, c) {
    const margin = 52, maxW = c.textMaxWidth || (c.textLayout === 'top-left' ? 640 : W - 2 * margin);
    let size = c.textSize || (c.textLayout === 'top-left' ? 170 : 168);
    t.setAttribute('font-size', size);
    let w = t.getComputedTextLength();
    if (w > maxW) { size = Math.floor(size * maxW / w); t.setAttribute('font-size', size); w = t.getComputedTextLength(); }
    t.setAttribute('stroke-width', f(size * 0.075));
    const capTop = c.textTop || 36, base = capTop + size * 0.74;
    if (c.textLayout === 'top-left') { t.setAttribute('x', margin); t.setAttribute('text-anchor', 'start'); }
    else { t.setAttribute('x', W / 2); t.setAttribute('text-anchor', 'middle'); }
    t.setAttribute('y', f(base));
  }

  function drawDebug(gEl, c) {
    const b = gEl.ownerSVGElement.querySelector('#title').getBBox();
    const hd = c.head, pct = Math.round(hd.r * 2 / H * 100);
    gEl.innerHTML = `<rect x="52" y="30" width="${W - 104}" height="${H - 60}" fill="none" stroke="#0f0" stroke-dasharray="8 6" stroke-width="2"/>
  <rect x="${W - 190}" y="${H - 64}" width="174" height="48" fill="rgba(255,0,0,.35)" stroke="#f00"/><text x="${W - 182}" y="${H - 34}" fill="#fff" font-size="16" font-family="monospace">timestamp zone</text>
  <rect x="0" y="${H - 8}" width="${W}" height="8" fill="rgba(255,0,0,.45)"/>
  <rect x="${b.x}" y="${b.y}" width="${b.width}" height="${b.height}" fill="none" stroke="#ff0" stroke-width="2"/>
  <circle cx="${hd.x}" cy="${hd.y}" r="${hd.r}" fill="none" stroke="#0ff" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="${hd.x - 60}" y="${hd.y + hd.r + 24}" fill="#0ff" font-size="18" font-family="monospace">head ${pct}% of H</text>`;
  }

  /** Config from URL: ?preset=&text=&accent=&expr=&zoom=&clock=&look=x,y&head=x,y,r,tilt&debug=1  or ?config=<json|base64json> */
  function configFromURL() {
    const q = new URLSearchParams(location.search), c = {};
    if (q.get('config')) { const raw = q.get('config'); try { Object.assign(c, JSON.parse(raw)); } catch (e) { Object.assign(c, JSON.parse(atob(raw))); } }
    const num = (s) => s.split(',').map(Number);
    if (q.get('preset')) c.preset = q.get('preset');
    if (q.get('text')) c.text = q.get('text');
    if (q.get('accent')) c.accent = q.get('accent');
    if (q.get('expr')) c.expression = q.get('expr');
    if (q.get('zoom')) c.zoom = +q.get('zoom');
    if (q.get('size')) c.textSize = +q.get('size');
    if (q.get('layout')) c.textLayout = q.get('layout');
    if (q.get('clock')) c.props = Object.assign(c.props || {}, { clock: q.get('clock') });
    if (q.get('look')) c.look = num(q.get('look'));
    if (q.get('extras')) c.extras = q.get('extras').split(',');
    if (q.get('head')) { const [x, y, r, tilt] = num(q.get('head')); c.head = { x, y, r }; if (!isNaN(tilt)) c.head.tilt = tilt; }
    if (q.get('twin')) c.twin = {};
    if (q.get('debug')) c.debug = true;
    if (q.get('grain')) c.grain = +q.get('grain');
    if (q.get('base')) c.baseImage = q.get('base');
    if (q.has('notext')) c.text = '';
    return c;
  }

  g.THUMB = { render, PRESETS, TX, thumbHead, configFromURL };
})(window);
