#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — cartographie TSV des lignes réelles (pixels) pour recalibrage des recadrages N
import os, subprocess, sys

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'
env = dict(os.environ, TESSDATA_PREFIX=TESS)

page = sys.argv[1] if len(sys.argv) > 1 else '120'
r = subprocess.run(['tesseract', f'{R600}/p{page}.png', '-', '-l', 'ara', '--psm', '4', 'tsv'],
                   capture_output=True, text=True, env=env)
lines = {}
for row in r.stdout.splitlines()[1:]:
    f = row.split('\t')
    if len(f) < 12 or f[11].strip() == '':
        continue
    key = (f[1], f[2], f[3], f[4])  # page, block, par, line
    x, y, w, h = int(f[6]), int(f[7]), int(f[8]), int(f[9])
    lines.setdefault(key, {'x': x, 'y': y, 'w': w, 'h': h, 'words': []})
    lines[key]['words'].append(f[11])
    L = lines[key]
    L['x'] = min(L['x'], x); L['y'] = min(L['y'], y)
    L['w'] = max(L['w'], x + w - L['x']); L['h'] = max(L['h'], y + h - L['y'])

from PIL import Image
W, H = Image.open(f'{R600}/p{page}.png').size
print(f'PAGE {page} — {W}x{H}')
for key in sorted(lines, key=lambda k: lines[k]['y']):
    L = lines[key]
    txt = ' '.join(L['words'])
    if len(txt.strip()) < 3:
        continue
    print(f"y[{L['y']:5d}-{L['y']+L['h']:5d}] ({L['y']/H:.3f}-{(L['y']+L['h'])/H:.3f}) x[{L['x']:5d}-{L['x']+L['w']:5d}] | {txt[:95]}")
