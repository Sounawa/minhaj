#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-20 — microcrops v3 : Q1 تقويم (2 lignes) + fin item 3 يُستفاد, zoom x3
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-18'
R600 = f'{OUT}/r600'
S = 600 / 72.0

ZONES = [
    (102, 100, 346, 640, 372, 'm23-q1-l1', 3.0),
    (102, 100, 370, 640, 398, 'm24-q1-l2', 3.0),
    (102, 100, 266, 640, 292, 'm25-y3-l1', 3.0),
    (102, 100, 288, 640, 312, 'm26-y3-l2', 3.0),
]

for (page, x0, y0, x1, y1, tag, up) in ZONES:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    box = (int(x0*S), int(y0*S), min(int(x1*S), W), min(int(y1*S), H))
    crop = im.crop(box)
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    if crop.width > 3400:
        r = 3400 / crop.width
        crop = crop.resize((3400, int(crop.height*r)), Image.LANCZOS)
    out = f'{OUT}/mc-{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=90)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
