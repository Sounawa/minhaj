#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-32 — 4 derniers scrutins ultra-ciblés (1200 dpi, upscale)
from PIL import Image
import os

DIR = '/home/z/my-project/scripts-ia2/tmp/h5-27'
OUT = f'{DIR}/crops'
os.makedirs(OUT, exist_ok=True)

# (id, page, x0, y0, x1, y1, upscale)
W = [
    ('w1', 154, 3200, 3180, 6600, 3820, 3),  # تَنْمِيمٌ/تَتْمِيمٌ لِلْفَرَائِضِ (item 2)
    ('w2', 153, 2400, 6440, 6200, 7120, 3),  # وَتَنْمِيمِ/وَتَتْمِيمِ الْفَرَائِضِ بِهَا
    ('w3', 155, 1400, 3640, 7200, 4360, 2),  # لَكِنْ لَا بُدَّ... (fin de l'encadré)
    ('w4', 150, 4300, 8420, 6400, 9080, 2),  # en-tête de l'encadré : الْحَدِيثُ/أَحَادِيثُ
]

for cid, p, x0, y0, x1, y1, up in W:
    dst = f'{OUT}/{cid}-p{p}.png'
    if os.path.exists(dst):
        continue
    im = Image.open(f'{DIR}/r1200/p{p}.png').crop((x0, y0, x1, y1))
    im = im.resize((im.width*up, im.height*up), Image.LANCZOS)
    im.save(dst)
    print(cid, im.size, 'OK')
print('done')
