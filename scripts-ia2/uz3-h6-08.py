#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — bloc item-2 p.46 : rendre y=405-490 à 2400 dpi (depuis le PDF),
# segmenter en lignes (profil de lignes, fond local soustrait), puis pour
# chaque ligne : runs d'encre classés (mots/points) pour cartographier
# l'emplacement exact des blancs «........».
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
S24 = 2400 / 72.0
os.makedirs(f'{DIR}/hi', exist_ok=True)

fp = f'{DIR}/hi/item2block'
if not os.path.exists(fp + '-046.png'):
    subprocess.run(['pdftoppm', '-png', '-r', '2400', '-f', '46', '-l', '46',
                    '-x', str(int(60*S24)), '-y', str(int(405*S24)),
                    '-W', str(int(510*S24)), '-H', str(int(85*S24)), SRC, fp],
                   check=True)
im = np.array(Image.open(fp + '-046.png').convert('L')).astype(int)
H, W = im.shape
Y0 = 405.0
X0 = 60.0

bg = np.median(im, axis=0).astype(int)[None, :]
ink = (im - bg) < -35

# ── lignes : profil par ligne de pixels, fenêtres glissantes ──
rows = ink.sum(axis=1)
bands, inb = [], False
for y, v in enumerate(rows):
    if v > 40 and not inb:
        inb, ya = True, y
    elif v <= 40 and inb:
        inb = False
        if y - ya > 60:
            bands.append((ya, y))
if inb: bands.append((ya, H))
print(f'{len(bands)} bandes de lignes :')
for ya, yb in bands:
    print(f'  y=[{Y0+ya/S24:6.1f}-{Y0+yb/S24:6.1f}]pt h={(yb-ya)/S24:5.1f}pt')

# ── pour chaque bande : runs ──
for bi, (ya, yb) in enumerate(bands):
    seg = ink[ya:yb, :]
    colprof = seg.sum(axis=0)
    runs, inr = [], False
    for x, v in enumerate(colprof):
        if v >= 1 and not inr:
            inr, xa = True, x
        elif v < 1 and inr:
            inr = False
            runs.append((xa, x))
    if inr: runs.append((xa, W))
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < 4:
            merged[-1] = (merged[-1][0], r[1])
        else:
            merged.append(r)
    # classer : suite de ≥4 runs compacts réguliers = série de POINTS
    print(f'— bande {bi+1} (y={Y0+ya/S24:.0f}-{Y0+yb/S24:.0f}) : {len(merged)} groupes')
    prev_kind = None
    for xa, xb in merged:
        w = (xb - xa) / S24
        d = seg[:, xa:xb].mean()
        kind = 'PT' if (w < 3.2 and d > 0.15) else ('mot' if w > 6.5 else 'ltr')
        print(f'    x=[{X0+xa/S24:6.1f}-{X0+xb/S24:6.1f}] l={w:5.1f} d={d:.2f} {kind}')
