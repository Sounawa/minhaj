#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-20 — composites 600 dpi pour adjudication leçon 18 hadith-5ep (pp.98-103)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-18'
R600 = f'{OUT}/r600'
os.makedirs(R600, exist_ok=True)

BANDS = {
    98:  [(0.00, 0.30, 'A1'), (0.24, 0.62, 'A2'), (0.56, 1.00, 'A3')],
    99:  [(0.00, 0.42, 'B1'), (0.36, 0.74, 'B2'), (0.68, 1.00, 'B3')],
    100: [(0.00, 0.30, 'C1'), (0.24, 0.58, 'C2'), (0.52, 0.84, 'C3'), (0.78, 1.00, 'C4')],
    101: [(0.00, 0.30, 'D1'), (0.24, 0.56, 'D2'), (0.50, 0.80, 'D3'), (0.74, 1.00, 'D4')],
    102: [(0.00, 0.34, 'E1'), (0.28, 0.56, 'E2'), (0.50, 0.80, 'E3'), (0.74, 1.00, 'E4')],
    103: [(0.00, 0.40, 'F1'), (0.30, 0.70, 'F2')],
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
        if crop.width > 3200:
            r = 3200 / crop.width
            crop = crop.resize((3200, int(crop.height*r)), Image.LANCZOS)
        out = f'{OUT}/c18-{tag}-p{page}.jpg'
        crop.convert('RGB').save(out, 'JPEG', quality=88)
        print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
