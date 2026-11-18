#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-37 — profil d'encre de la zone الاستثمار p.23 (y 100-220 pt) :
# lignes de texte exactes (gaps d'encre) pour cadrer les recadrages VLM ligne-à-ligne.
from PIL import Image
import numpy as np

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03'
im = Image.open(f'{DIR}/r600/p23.png').convert('L')
S = 600 / 72.0
a = np.array(im)

# zone x 40-610 pt, y 100-225 pt
x0, x1 = int(40*S), int(610*S)
y0, y1 = int(100*S), int(225*S)
z = a[y0:y1, x0:x1]

# binarisation: encre = sombre
ink = (z < 128).sum(axis=1)  # par ligne horizontale
thr = max(4, int(0.004 * (x1-x0)))
rows = ink > thr

# regrouper en bandes
bands = []
st = None
for i, v in enumerate(rows):
    if v and st is None: st = i
    if not v and st is not None:
        if i - st >= 3: bands.append((st, i))
        st = None
if st is not None: bands.append((st, len(rows)))

print('bandes d encre (pt, base 72dpi):')
for st, en in bands:
    dens = ink[st:en].mean() / (x1-x0)
    print(f'  y {y0/S + st/S:6.1f} - {y0/S + en/S:6.1f}  (h {(en-st)/S:4.1f} pt, densite {dens:.3f})')
