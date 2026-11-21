#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — découpe des pages 71-75 (600 dpi) en 4 bandes horizontales chevauchantes
# pour lecture VLM (même géométrie que Z2-45..47 : bandes ≈ 5309×1760, chevauchement 90 px).
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h6-13/r600'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-13/bands'
os.makedirs(OUT, exist_ok=True)

for p in range(71, 76):
    im = Image.open(f'{D}/p{p}.png')
    w, h = im.size
    n = 4
    ov = 90
    band_h = (h + ov * (n - 1)) // n
    for i in range(n):
        top = max(0, (h - band_h) * i // max(1, n - 1))
        bot = min(h, top + band_h)
        crop = im.crop((0, top, w, bot))
        crop.save(f'{OUT}/p{p}-b{i+1}.png')
        print(f'p{p}-b{i+1}: y{top}-{bot} {crop.size}')
