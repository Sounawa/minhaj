#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — structure de la ligne 1 du hadith item-2 p.46 (salami1, 2400 dpi) :
# localiser la série de points (blanc à remplir) et mesurer ce qui la précède
# (=> «عليه» imprimé ou non). + détection de lam haut.
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
im = np.array(Image.open(f'{DIR}/hi/salami1-046.png').convert('L')).astype(int)
H, W = im.shape
print(f'image {W}x{H} px (2400 dpi : {W*72/2400:.0f}x{H*72/2400:.0f} pt)')
g = im
# seuil adaptatif : l'encre est ici grise/claire
thr = np.percentile(g, 8) + 0.5 * (np.percentile(g, 60) - np.percentile(g, 8))
ink = g < thr
print(f'seuil={thr:.0f} | densité encre={ink.mean():.3f}')
colprof = ink.sum(axis=0)
# runs
runs, inr = [], False
for x, v in enumerate(colprof):
    if v >= 1 and not inr:
        inr, xa = True, x
    elif v < 1 and inr:
        inr = False
        runs.append((xa, x))
if inr: runs.append((xa, W))
# fusion serrée (< 3 px)
merged = []
for r in runs:
    if merged and r[0] - merged[-1][1] < 3:
        merged[-1] = (merged[-1][0], r[1])
    else:
        merged.append(r)
S24 = 2400 / 72.0
print(f'{len(merged)} runs (gauche→droite), unités pt :')
for xa, xb in merged:
    w = (xb - xa) / S24
    seg = ink[:, xa:xb]
    dens = seg.mean()
    hh = np.where(seg.any(axis=1))[0]
    top, bot = hh.min(), hh.max()
    # classification : point = étroit + position basse + compact
    kind = '??'
    if w < 2.6 and dens > 0.25:
        kind = 'POINT'
    elif w > 6:
        kind = 'mot'
    else:
        kind = 'lettre'
    print(f'  x=[{xa/S24:6.1f}-{xb/S24:6.1f}]pt l={w:5.1f}pt d={dens:.2f} '
          f'y=[{top/S24:4.1f}-{bot/S24:4.1f}] {kind}')
