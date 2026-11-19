#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — détection automatique des bandes colorées (bandeaux cmap-aveugles) pp.46-49,
# leçon 7 «دَعْمٌ وَتَطْبِيقٌ» (docId pdf-mut23h3b-687).
import numpy as np
from PIL import Image
from collections import Counter

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
S150 = 150 / 72.0  # bbox coords are in pt (72dpi)

for pg in range(46, 50):
    im = Image.open(f'{DIR}/r150/p{pg}.png').convert('RGB')
    a = np.array(im).astype(int)
    sat = a.max(axis=2) - a.min(axis=2)
    m = sat > 40
    rowfrac = m.mean(axis=1)
    bands = []
    inb = False
    for y, f in enumerate(rowfrac):
        if f > 0.04 and not inb:
            inb, y0 = True, y
        elif f <= 0.04 and inb:
            inb = False
            if y - y0 > 8:
                bands.append((y0, y))
    if inb:
        bands.append((y0, len(rowfrac)))
    print(f'===== PAGE {pg} =====')
    for y0, y1 in bands:
        seg = a[y0:y1]
        mm = m[y0:y1]
        cols = np.where(mm.any(axis=0))[0]
        x0, x1 = cols.min(), cols.max()
        pix = seg[mm]
        q = (pix // 32) * 32
        top = Counter(map(tuple, q)).most_common(3)
        ypt0, ypt1 = y0 / S150, y1 / S150
        xpt0, xpt1 = x0 / S150, x1 / S150
        print(f'  y=[{ypt0:6.0f}-{ypt1:6.0f}]pt x=[{xpt0:6.0f}-{xpt1:6.0f}]pt '
              f'h={y1-y0}px  ' + '  '.join(f'RGB{c}×{n}' for c, n in top))
