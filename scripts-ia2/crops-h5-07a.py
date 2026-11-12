#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — micro-crops adjudication p47 (zones contestées) composés en une image.
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-07/plates'

# rendu 600 dpi page 47 pour zoom maximal
png600 = f'{OUT}/p47-600.png'
if not os.path.exists(png600):
    subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', '47', '-l', '47', SRC, f'{OUT}/p47-600t'], check=True)
    os.replace(f'{OUT}/p47-600t-047.png', png600)

im = Image.open(png600)
w, h = im.size  # ~5310 x 6726

# zones (fractions de la page complète) : (x0,y0,x1,y1)
zones = [
    ('Z1-premiere-ligne', 0.03, 0.435, 0.97, 0.50),   # تمثل النية ... الأساس
    ('Z2-ref-baqara',     0.30, 0.545, 0.97, 0.615),  # fin verset Baqara + réf
    ('Z3-fin-cadre',      0.03, 0.855, 0.97, 0.965),  # قال تعالى طه 14 + réf + fermeture cadre
]
crops = []
for name, x0, y0, x1, y1 in zones:
    c = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    crops.append(c)

W = max(c.width for c in crops)
H = sum(c.height for c in crops) + 40 * (len(crops) - 1)
canvas = Image.new('RGB', (W, H), 'white')
y = 0
for c in crops:
    canvas.paste(c, (0, y))
    y += c.height + 40
canvas.save(f'{OUT}/p47-zooms.png')
print('OK', canvas.size)
