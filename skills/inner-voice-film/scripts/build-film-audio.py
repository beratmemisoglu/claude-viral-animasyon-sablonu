"""Builds scripts/<slug>-audio.mjs = shared generators (from patience-audio.mjs, up to the motifs) + scripts/<slug>-cues.mjs.
usage: python scripts/build-film-audio.py <slug>   then   node scripts/<slug>-audio.mjs public/audio/<slug>-mix-raw.wav"""
import io, os, sys
slug = sys.argv[1]
D = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(D, 'patience-audio.mjs'), encoding='utf-8').read()
head = src[:src.index('// ---------- motifs ----------')]
head = head.replace('../src/films/patience/timeline.json', f'../src/films/{slug}/timeline.json').replace('patience-mix-raw.wav', f'{slug}-mix-raw.wav')
cues = io.open(os.path.join(D, f'{slug}-cues.mjs'), encoding='utf-8').read()
io.open(os.path.join(D, f'{slug}-audio.mjs'), 'w', encoding='utf-8', newline='\n').write(head + '\n' + cues)
print('ok', slug)
