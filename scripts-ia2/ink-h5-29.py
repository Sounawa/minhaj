#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — profil d'encre verticale (numpy) des zones disputées leçon 29 :
#  A: p159 x40-600  y200-295  — entrée القرآن : ligne cachée après «المصحف» ?
#  B: p159 x30-115  y640-678  — entrée 4 : quelque chose après «الأزدي» ?
#  D: p162 x40-600  y502-596  — gap 94.6pt entre entrées 19/20 : bandeau/rubrique ?
#  E: p163 x480-570 y688-716  — date de mort العيني (cmap ne voit qu'un «5» large)
#  G: p165 x40-600  y596-650  — header entrée 37 (ligne invisible au cmap)
# Pour chaque bande d'encre détectée : strip + tesseract psm 7.
from PIL import Image
import numpy as np, subprocess, os

D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S = 1200 / 72.0
TESS = '/home/z/my-project/scripts-translate/tessdata'

zones = [
    ('A', 159, 40, 600, 200, 295),
    ('B', 159, 30, 115, 640, 678),
    ('D', 162, 40, 600, 502, 596),
    ('E', 163, 480, 570, 688, 716),
    ('G', 165, 40, 600, 596, 650),
]

os.makedirs(f'{D}/crops', exist_ok=True)
for nom, pg, xa, xb, ya, yb in zones:
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    a = np.asarray(im, dtype=np.uint8)
    x0, x1 = int(xa*S), int(xb*S)
    y0, y1 = int(ya*S), int(yb*S)
    z = a[y0:y1, x0:x1]
    ink = (z < 128).astype(np.float32)
    prof = ink.mean(axis=1)
    runs, cur, start = [], False, 0
    for i, v in enumerate(prof):
        if v > 0.003 and not cur:
            cur, start = True, i
        elif v <= 0.003 and cur:
            cur = False
            if i - start > 10:
                runs.append((start, i))
    if cur: runs.append((start, len(prof)))
    print(f'===== ZONE {nom} (p{pg}, x{xa}-{xb}, y{ya}-{yb}) =====')
    if not runs:
        print('  AUCUNE ENCRE DÉTECTÉE (zone vide)')
    for k, (s, e) in enumerate(runs):
        y_pt = ya + s / S
        h_pt = (e - s) / S
        dens = ink[s:e].mean()
        pad = 6
        ys, ye = max(0, y0 + s - pad), y0 + e + pad
        strip = Image.open(f'{D}/r1200/p{pg}.png').crop((x0, ys, x1, ye))
        fp = f'{D}/crops/ink-{nom}{k}.png'
        strip.save(fp)
        r = subprocess.run(['tesseract', fp, 'stdout', '-l', 'ara',
                            '--tessdata-dir', TESS, '--psm', '7'],
                           capture_output=True, text=True)
        print(f'  bande{k} y={y_pt:6.1f}pt h={h_pt:4.1f}pt dens={dens:.3f} => {r.stdout.strip()[:130]}')
    print()
