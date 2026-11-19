#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — FINAL : sur le crop 2400 salami1 (x=60-570pt, y=436-454pt),
# trouver la SÉRIE DE POINTS (blanc) : runs compacts réguliers, puis ce qui
# la précède immédiatement à droite (RTL) => «عليه» imprimé ou non.
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
im = np.array(Image.open(f'{DIR}/hi/salami1-046.png').convert('L')).astype(int)
H, W = im.shape
S24 = 2400 / 72.0
X0 = 60.0  # origine pt du crop

# encre = pixels nettement plus sombres que le fond LOCAL (colonne par colonne)
bg = np.median(im, axis=0).astype(int)[None, :]
rel = im - bg
ink = rel < -35
print(f'densité encre={ink.mean():.3f}')

colprof = ink.sum(axis=0)
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
print(f'{len(merged)} runs (gauche→droite) :')
for xa, xb in merged:
    w = (xb - xa) / S24
    seg = ink[:, xa:xb]
    dens = seg.mean()
    hh = np.where(seg.any(axis=1))[0]
    top, bot = (hh.min()/S24, hh.max()/S24) if len(hh) else (0, 0)
    kind = 'PT' if (w < 3.0 and dens > 0.2) else ('mot' if w > 6 else 'ltr')
    print(f'  x=[{X0+xa/S24:6.1f}-{X0+xb/S24:6.1f}]pt l={w:5.1f} d={dens:.2f} y=[{top:4.1f}-{bot:4.1f}] {kind}')
