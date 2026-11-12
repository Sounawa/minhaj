#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — micro-crops 900 dpi p47 : mot contesté (Z1), réf Baqara (Z2), dernière āya (Z3)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-07/plates'

png900 = f'{OUT}/p47-900.png'
if not os.path.exists(png900):
    subprocess.run(['pdftoppm', '-png', '-r', '900', '-f', '47', '-l', '47', SRC, f'{OUT}/p47-900t'], check=True)
    os.replace(f'{OUT}/p47-900t-047.png', png900)

im = Image.open(png900)
w, h = im.size

zones = [
    ('Z1mot',      0.02, 0.442, 0.55, 0.478),  # تمثل النية العضر الأساس — zoom mot
    ('Z2ref',      0.55, 0.555, 0.99, 0.60),   # [البقرة: 91] + fin du verset
    ('Z3aya',      0.02, 0.815, 0.99, 0.90),   # dernière āya complète + début
    ('Z3ref',      0.02, 0.885, 0.45, 0.93),   # la réf de la dernière āya
]
crops = [im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h))) for _, x0, y0, x1, y1 in zones]
W = max(c.width for c in crops)
H = sum(c.height for c in crops) + 30 * (len(crops) - 1)
canvas = Image.new('RGB', (W, H), 'white')
y = 0
for c in crops:
    canvas.paste(c, (0, y)); y += c.height + 30
# redimensionner pour rester sous ~2000 px de large
if W > 2000:
    r = 2000 / W
    canvas = canvas.resize((2000, int(H * r)), Image.LANCZOS)
canvas.save(f'{OUT}/p47-zooms2.png')
print('OK', canvas.size)
