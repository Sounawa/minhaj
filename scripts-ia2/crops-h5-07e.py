#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — adjudication p48 : liste أشرح (item 1) + ضِدّ (item 2) + emprise/ réf التحليل 1
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import subprocess

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-07/plates'

png = f'{OUT}/p48-900.png'
if not os.path.exists(png):
    subprocess.run(['pdftoppm', '-png', '-r', '900', '-f', '48', '-l', '48', SRC, f'{OUT}/p48-900t'], check=True)
    os.replace(f'{OUT}/p48-900t-048.png', png)

im = Image.open(png)
w, h = im.size
zones = [
    ('ASHRIH', 0.04, 0.255, 0.97, 0.385),   # item 1 أشرح sur 2 lignes
    ('DIDD',    0.04, 0.385, 0.97, 0.435),  # item 2 ضد
    ('TAHLIL1', 0.04, 0.615, 0.97, 0.72),   # التحليل 1 + réf
]
crops = [im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h))) for _, x0, y0, x1, y1 in zones]
crops = [c if c.width <= 1900 else c.resize((1900, int(c.height*1900/c.width)), Image.LANCZOS) for c in crops]
W = max(c.width for c in crops)
H = sum(c.height for c in crops) + 40*(len(crops)-1)
canvas = Image.new('RGB', (W, H), 'white')
y = 0
for c in crops:
    canvas.paste(c, (0, y)); y += c.height + 40
canvas.save(f'{OUT}/p48-zooms.png')
print('OK', canvas.size)
