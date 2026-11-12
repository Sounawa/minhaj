#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — adjudication finale p47 : ligne 1 du cadre + réf Tawba, 1200 dpi
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-07/plates'

png = f'{OUT}/p47-1200.png'
if not os.path.exists(png):
    subprocess.run(['pdftoppm', '-png', '-r', '1200', '-f', '47', '-l', '47', SRC, f'{OUT}/p47-1200t'], check=True)
    os.replace(f'{OUT}/p47-1200t-047.png', png)

im = Image.open(png)
w, h = im.size

zones = [
    ('L1-cadre',  0.04, 0.395, 0.62, 0.455),  # première ligne du cadre
    ('REF-tawba', 0.02, 0.875, 0.40, 0.925),  # réf dernière āya
]
crops = [im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h))) for _, x0, y0, x1, y1 in zones]
crops = [c if c.width <= 1900 else c.resize((1900, int(c.height*1900/c.width)), Image.LANCZOS) for c in crops]
W = max(c.width for c in crops)
H = sum(c.height for c in crops) + 30
canvas = Image.new('RGB', (W, H), 'white')
y = 0
for c in crops:
    canvas.paste(c, (0, y)); y += c.height + 30
canvas.save(f'{OUT}/p47-zooms3.png')
print('OK', canvas.size)
