// dmscales kit: every element of the style alone, on light and on dark, one second each (the Kit stage). An element joins
// a scene only after its two frames here look right and the layout check is clean.
import { THREE, group, rect } from '../engine.js';
import { kitGallery } from '../lib/kit.js';
import { say, figure, crowd, bust, mark, cloud, tagBox, burst, boxes, media, clip } from '../models.js';

// the style lives on white paper only: on the kit's dark board an element sits on its own white sheet
function paper(S, make) {
  const g = group(null), el = make(g), dark = parseInt(String(S._bg ?? '#ffffff').slice(1, 3), 16) < 128;
  if (!dark) return g;
  g.updateWorldMatrix(true, true); const b = new THREE.Box3().setFromObject(el), c = b.getCenter(new THREE.Vector3()), sz = b.getSize(new THREE.Vector3());
  const sheet = rect(g, sz.x + 120, sz.y + 120, '#ffffff', c.x, c.y); sheet.renderOrder = -1; g.children.unshift(g.children.pop());
  g.userData.bg = '#ffffff'; return g;
}

kitGallery([
  { name: 'say (body line)', build: S => paper(S, g => say(g, 'all it {takes} is _one_ video')) },
  { name: 'say (header)', build: S => paper(S, g => say(g, '{TRUST} SCORE:', { size: 92, bold: true })) },
  { name: 'say (tracked caps)', build: S => paper(S, g => say(g, 'EVERY VIEWER WANTS\nONE THING: {g:A REASON}', { italic: false, track: .11 })) },
  { name: 'say (footnote)', build: S => paper(S, g => say(g, '*not my screenshots', { size: 27 })) },
  { name: 'figure frown', build: S => paper(S, g => figure(g, { h: 420, face: 'frown' })) },
  { name: 'figure grin phone', build: S => paper(S, g => figure(g, { h: 420, face: 'grin', pose: 'phone' })) },
  { name: 'figure shock armsup', build: S => paper(S, g => figure(g, { h: 420, face: 'shock', pose: 'armsup' })) },
  { name: 'figure worried shrug', build: S => paper(S, g => figure(g, { h: 420, face: 'worried', pose: 'shrug' })) },
  { name: 'figure smile point', build: S => paper(S, g => figure(g, { h: 420, face: 'smile', pose: 'point' })) },
  { name: 'crowd', build: S => paper(S, g => crowd(g, { w: 700, h: 460 })) },
  { name: 'bust', build: S => paper(S, g => bust(g, { s: 1.6 })) },
  { name: 'mark arrow', build: S => paper(S, g => mark(g, 'arrow', { w: 260, h: 150 })) },
  { name: 'mark circle', build: S => paper(S, g => mark(g, 'circle', { w: 300, h: 160 })) },
  { name: 'mark x', build: S => paper(S, g => mark(g, 'x', { w: 300, h: 220 })) },
  { name: 'cloud', build: S => paper(S, g => cloud(g, 'a niche is the content you make', { w: 420, h: 280 })) },
  { name: 'tagBox', build: S => paper(S, g => tagBox(g, 'Viewer')) },
  { name: 'burst', build: S => paper(S, g => burst(g, { r: 140, arc: 300 })) },
  { name: 'boxes', build: S => paper(S, g => boxes(g, { n: 7, marked: [4, 6] })) },
  { name: 'media', build: S => paper(S, g => media(g, 'test_shot', { w: 700 })) },
  { name: 'clip', build: S => clip(S, 'test_clip', { n: 45, fps: 15, h: 600, r: 28 }) },
], { t0: 0, each: 1 });
