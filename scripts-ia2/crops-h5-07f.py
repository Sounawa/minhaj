#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — adjudication finale p48 : أشرح item1, ضد item2, emprise التحليل 1, réf item 4
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-07/plates'
im = Image.open(f'{OUT}/p48-900.png')
w, h = im.size
zones = [
    ('ASHRIH1', 0.04, 0.095, 0.97, 0.150),  # أشرح item 1 ligne 1
    ('ASHRIH2', 0.04, 0.145, 0.97, 0.185),  # أشرح item 1 ligne 2
    ('DIDD',    0.04, 0.180, 0.97, 0.225),  # ضد item 2
    ('TAHL1A',  0.04, 0.245, 0.97, 0.295),  # تحليل 1 āya
    ('TAHL1B',  0.04, 0.290, 0.97, 0.335),  # تحليل 1 réf
    ('TAHL4',   0.04, 0.360, 0.97, 0.435),  # تحليل 4 āya + réf
]
crops = [im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h))) for _, x0, y0, x1, y1 in zones]
crops = [c if c.width <= 1900 else c.resize((1900, int(c.height*1900/c.width)), Image.LANCZOS) for c in crops]
W = max(c.width for c in crops)
H = sum(c.height for c in crops) + 30*(len(crops)-1)
canvas = Image.new('RGB', (W, H), 'white')
y = 0
for c in crops:
    canvas.paste(c, (0, y)); y += c.height + 30
canvas.save(f'{OUT}/p48-zooms2.png')
print('OK', canvas.size)
