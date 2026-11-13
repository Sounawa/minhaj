#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — micro-crops v2 (coordonnées recalibrées sur rendu 300 dpi 2655×3363)
import os
from PIL import Image

TMP = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-09'
OUT = f'{TMP}/crops'
os.makedirs(OUT, exist_ok=True)

CROPS = [
    (58,  400, 2020, 2300, 2190, 'titre-thalitha2', 2.4),
    (58,    0, 2830, 2655, 3120, 'aya-p58-v2', 2.0),
    (58,    0,  420, 2655,  620, 'sawaa-ibtudia2', 2.0),
    (58,    0, 1740, 2655, 1900, 'biraddi-furu2', 2.0),
    (58,  500, 2280, 2400, 2470, 'la-yuqbal-sahibih2', 2.6),
    (59,    0, 1790, 2655, 2150, 'ayat-istithmar2', 2.0),
    (59,  200, 2160, 2450, 2330, 'muajjam-gloss2', 2.4),
    (57,  700, 1810, 2400, 1970, 'istikhras-title2', 2.6),
]

for pg, x1, y1, x2, y2, name, fac in CROPS:
    src = Image.open(f'{TMP}/plates/hi-{pg}.png')
    im = src.crop((x1, y1, x2, y2))
    im = im.resize((int(im.width * fac), int(im.height * fac)), Image.LANCZOS)
    im.save(f'{OUT}/{name}.png')
    print(name, im.size)
print('OK crops v2')
