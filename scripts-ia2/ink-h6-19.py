#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — ink-h6-19 : profil d'encre pleine page pp.105-109 (L19 «فضل الله في
# الجزاء عن الأعمال») sur les rendus 600 dpi : bandes de texte exactes pour
# cadrer les recadrages ciblés.
from PIL import Image
import numpy as np

DIR = '/home/z/my-project/pdf-work/h6-15'
for pg in (105, 106, 107, 108, 109):
    im = Image.open(f'{DIR}/t{pg:03d}.png').convert('L')
    a = np.array(im)
    H, W = a.shape
    x0, x1 = int(0.06 * W), int(0.94 * W)
    z = a[:, x0:x1]
    ink = (z < 120).sum(axis=1)
    thr = max(4, int(0.006 * (x1 - x0)))
    rows = ink > thr
    bands = []
    st = None
    for i, v in enumerate(rows):
        if v and st is None:
            st = i
        if not v and st is not None:
            if i - st >= 6:  # ≥6 px à 600 dpi
                bands.append((st, i))
            st = None
    if st is not None:
        bands.append((st, len(rows)))
    print(f'═══ p{pg} ({len(bands)} bandes) ═══')
    for st, en in bands:
        dens = ink[st:en].mean() / (x1 - x0)
        print(f'  y {st:5d} - {en:5d}  (h {en-st:4d}, dens {dens:.3f})')
