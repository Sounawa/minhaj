#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-39 — profil d'encre pleine page pp.29-35 (leçon 4 «شكر الله على نعمة الجوارح»),
# leçon 5 début p.36 (bornage) : bandes de texte exactes pour cadrer les recadrages VLM.
from PIL import Image
import numpy as np

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-05'
for pg in (29, 30, 31, 32, 33, 34, 35, 36):
    im = Image.open(f'{DIR}/r150/p{pg}.png').convert('L')
    S = 150 / 72.0
    a = np.array(im)
    x0, x1 = int(30*S), int(610*S)
    z = a[:, x0:x1]
    ink = (z < 120).sum(axis=1)
    thr = max(4, int(0.006 * (x1-x0)))
    rows = ink > thr
    bands = []
    st = None
    for i, v in enumerate(rows):
        if v and st is None: st = i
        if not v and st is not None:
            if i - st >= 3: bands.append((st, i))
            st = None
    if st is not None: bands.append((st, len(rows)))
    print(f'═══ p{pg} ═══')
    for st, en in bands:
        dens = ink[st:en].mean() / (x1-x0)
        print(f'  y {st/S:6.1f} - {en/S:6.1f}  (h {(en-st)/S:4.1f} pt, dens {dens:.3f})')
