#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-20 — microcrops calibrés par bbox pdftotext, leçon 18 hadith-5ep (pp.98-103)
# zones en points PDF (637.2 x 807.12) → pixels 600 dpi (x8.3333), upscale x2 LANCZOS
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-18'
R600 = f'{OUT}/r600'
S = 600 / 72.0

# (page, x0, y0, x1, y1, tag, upscale)
ZONES = [
    (98, 380, 238, 640, 312, 'm1-obj23', 2.0),
    (98,  55, 393, 640, 480, 'm2-tamhid', 1.6),
    (98,  55, 478, 640, 575, 'm3-questions', 1.6),
    (99, 140, 203, 575, 300, 'm4-duaa-bustan-death', 1.6),
    (99, 100, 466, 575, 508, 'm5-sharh2', 2.2),
    (99, 180, 565, 560, 645, 'm6-istikhlas', 2.0),
    (100, 95, 448, 585, 515, 'm7-fudayl', 2.0),
    (101, 95, 78, 585, 140, 'm8-ibnhibban', 2.0),
    (101, 55, 333, 625, 448, 'm9-mystery-bullet1', 1.6),
    (101, 55, 593, 625, 632, 'm10-yuamilu', 2.0),
    (102, 55, 93, 625, 170, 'm11-yustafad1', 1.8),
    (102, 55, 173, 625, 235, 'm12-yustafad2', 1.8),
    (102, 55, 238, 625, 310, 'm13-yustafad3', 1.8),
    (102, 55, 350, 625, 400, 'm14-taqwim1', 2.0),
]

for (page, x0, y0, x1, y1, tag, up) in ZONES:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    box = (int(x0*S), int(y0*S), min(int(x1*S), W), min(int(y1*S), H))
    crop = im.crop(box)
    if up != 1.0:
        crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    if crop.width > 3400:
        r = 3400 / crop.width
        crop = crop.resize((3400, int(crop.height*r)), Image.LANCZOS)
    out = f'{OUT}/mc-{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=90)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
