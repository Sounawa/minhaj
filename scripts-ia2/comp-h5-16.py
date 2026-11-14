#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — composites 600 dpi pour adjudication leçon 16 hadith-5ep (pp.88-92)
# Bandes horizontales chevauchantes, JPEG q88 (gestion budget VLM)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'
R600 = f'{OUT}/r600'
os.makedirs(R600, exist_ok=True)

# bandes (fractions de hauteur) par page — chevauchement ~4%
BANDS = {
    88: [(0.00, 0.26, 'A1'), (0.22, 0.52, 'A2'), (0.48, 0.78, 'A3'), (0.74, 1.00, 'A4')],
    89: [(0.00, 0.30, 'B1'), (0.26, 0.60, 'B2'), (0.56, 1.00, 'B3')],
    90: [(0.00, 0.32, 'C1'), (0.28, 0.64, 'C2'), (0.60, 1.00, 'C3')],
    91: [(0.00, 0.34, 'D1'), (0.30, 0.68, 'D2'), (0.64, 1.00, 'D3')],
    92: [(0.00, 0.40, 'E1'), (0.36, 0.76, 'E2'), (0.72, 1.00, 'E3')],
}

for page in sorted(BANDS):
    png = f'{R600}/p{page}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(page), '-l', str(page),
                        SRC, f'{R600}/q{page}'], check=True)
        got = [f for f in os.listdir(R600) if f.startswith(f'q{page}-')]
        os.rename(f'{R600}/{got[0]}', png)
    im = Image.open(png)
    W, H = im.size
    for (a, b, tag) in BANDS[page]:
        crop = im.crop((0, int(a*H), W, int(b*H)))
        # redimensionne si largeur > 3200 (le VLM sous-échantillonne au-delà)
        if crop.width > 3200:
            r = 3200 / crop.width
            crop = crop.resize((3200, int(crop.height*r)), Image.LANCZOS)
        out = f'{OUT}/comp-{tag}-p{page}.jpg'
        crop.convert('RGB').save(out, 'JPEG', quality=88)
        print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
