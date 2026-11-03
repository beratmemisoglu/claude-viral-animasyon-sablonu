#!/usr/bin/env node
// add_media.mjs: bring the member's own screenshots and video clips into a dmscales project.
//   node add_media.mjs <project dir> <file> [<file> ...] [--fps 12] [--width 960] [--height 800] [--name <name>]
// A picture (png jpg jpeg webp) is copied to assets/media/<name>.<ext> and becomes project.json images[name].
// A video (mp4 mov webm mkv m4v) becomes frames assets/media/<name>/0000.jpg ... at --fps (default 12), fitted inside --width x --height (960 x 800: the largest the style shows a clip; memory)
// registered as images[name_0 .. name_(n-1)]: scenes play it with clip(S, name, { n, fps }).
// Every file is listed in assets/media/media.json: { name: { kind, file, w, h, n, fps, seconds, source } }.
// The video's own sound is not used (the style runs on the voice and one music bed).
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const args = process.argv.slice(2), opt = (k, d) => { const i = args.indexOf('--' + k); return i >= 0 ? args.splice(i, 2)[1] : d; };
const fps = +opt('fps', 12), maxW = +opt('width', 960), maxH = +opt('height', 800), forced = opt('name', null);
const [dir, ...files] = args;
if (!dir || !files.length) { console.error('usage: node add_media.mjs <project dir> <file> [...] [--fps 12] [--width 960] [--height 800] [--name n]'); process.exit(2); }
const pjFile = path.join(dir, 'project.json');
if (!fs.existsSync(pjFile)) { console.error(`no project.json in ${dir}`); process.exit(2); }
const ff = process.env.FFMPEG || 'ffmpeg', fp = process.env.FFPROBE || 'ffprobe';
const pj = JSON.parse(fs.readFileSync(pjFile, 'utf8').replace(/^﻿/, '')); pj.images ??= {};
const out = path.join(dir, 'assets', 'media'); fs.mkdirSync(out, { recursive: true });
const manFile = path.join(out, 'media.json'), man = fs.existsSync(manFile) ? JSON.parse(fs.readFileSync(manFile, 'utf8')) : {};
const slug = s => s.toLowerCase().normalize('NFKD').replace(/[^\w]+/g, '_').replace(/^_+|_+$/g, '').replace(/^(\d)/, 'm$1').slice(0, 40) || 'media';
const probe = f => JSON.parse(execFileSync(fp, ['-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:format=duration', '-of', 'json', f], { encoding: 'utf8' }));

for (const src of files) {
  if (!fs.existsSync(src)) { console.error(`missing: ${src}`); continue; }
  const ext = path.extname(src).slice(1).toLowerCase(), name = forced && files.length === 1 ? slug(forced) : slug(path.basename(src, path.extname(src)));
  for (const k of Object.keys(pj.images)) if (k === name || new RegExp(`^${name}_\\d+$`).test(k)) delete pj.images[k];
  if (['png', 'jpg', 'jpeg', 'webp'].includes(ext)) {
    const rel = `assets/media/${name}.${ext}`; fs.copyFileSync(src, path.join(dir, rel));
    const s = probe(src).streams?.[0] ?? {};
    pj.images[name] = rel; man[name] = { kind: 'image', file: rel, w: s.width, h: s.height, source: path.basename(src) };
    console.log(`image ${name}: ${rel} (${s.width}x${s.height})`);
  } else if (['mp4', 'mov', 'webm', 'mkv', 'm4v'].includes(ext)) {
    const fd = path.join(out, name); fs.rmSync(fd, { recursive: true, force: true }); fs.mkdirSync(fd, { recursive: true });
    execFileSync(ff, ['-v', 'error', '-y', '-i', src, '-vf', `fps=${fps},scale=w='min(${maxW},iw)':h='min(${maxH},ih)':force_original_aspect_ratio=decrease,scale=trunc(iw/2)*2:trunc(ih/2)*2`, '-q:v', '3', '-start_number', '0', path.join(fd, '%04d.jpg')]);
    const frames = fs.readdirSync(fd).filter(f => f.endsWith('.jpg')).sort();
    frames.forEach((f, i) => { pj.images[`${name}_${i}`] = `assets/media/${name}/${f}`; });
    const p = probe(path.join(fd, frames[0])).streams?.[0] ?? {};
    man[name] = { kind: 'clip', dir: `assets/media/${name}`, n: frames.length, fps, w: p.width, h: p.height, seconds: +(frames.length / fps).toFixed(2), source: path.basename(src) };
    console.log(`clip ${name}: ${frames.length} frames at ${fps} fps (${man[name].seconds} s, ${p.width}x${p.height}) -> clip(S, '${name}', { n: ${frames.length}, fps: ${fps} })`);
  } else console.error(`skipped (not a picture or a video): ${src}`);
}
fs.writeFileSync(pjFile, JSON.stringify(pj, null, 1));
fs.writeFileSync(manFile, JSON.stringify(man, null, 1));
console.log(`media.json: ${Object.keys(man).length} item(s)`);
