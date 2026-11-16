#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-20 — microcrops v2 (lignes individuelles, zooms x2.2-x2.5)
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-18'
R600 = f'{OUT}/r600'
S = 600 / 72.0

ZONES = [
    (98,  55, 424, 640, 452, 'm15-tamhid-l1', 2.5),
    (98,  55, 441, 640, 478, 'm16-tamhid-l2', 2.5),
    (98, 130, 395, 420, 420, 'm17-ayat-dalla', 2.5),
    (98,  55, 498, 640, 548, 'm18-questions', 2.0),
    (99, 140, 203, 570, 240, 'm19-duaa-fin', 2.5),
    (102, 55, 263, 640, 308, 'm20-yustafad3-fin', 2.5),
    (102, 150, 343, 640, 400, 'm21-taqwim1', 2.2),
    (100, 150, 453, 580, 502, 'm22-fudayl-fin', 2.5),
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
