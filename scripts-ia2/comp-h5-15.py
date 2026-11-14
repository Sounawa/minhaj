#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-17 — composites 600 dpi pour adjudication leçon 15 hadith-5ep (pp.83-87)
# Bandes horizontales chevauchantes, JPEG q85 (gestion budget VLM)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-15'
R600 = f'{OUT}/r600'
os.makedirs(R600, exist_ok=True)

# bandes (fractions de hauteur) par page — chevauchement 3%
BANDS = {
    83: [(0.00, 0.24, 'A1'), (0.20, 0.50, 'A2'), (0.46, 0.80, 'A3'), (0.76, 1.00, 'A4')],
    84: [(0.00, 0.30, 'B1'), (0.26, 0.62, 'B2'), (0.58, 1.00, 'B3')],
    85: [(0.00, 0.34, 'C1'), (0.30, 0.70, 'C2'), (0.66, 1.00, 'C3')],
    86: [(0.00, 0.38, 'D1'), (0.34, 0.74, 'D2'), (0.70, 1.00, 'D3')],
    87: [(0.00, 0.40, 'E1'), (0.36, 0.75, 'E2'), (0.71, 1.00, 'E3')],
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
