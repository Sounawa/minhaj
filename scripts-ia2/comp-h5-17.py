#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-19 — composites 600 dpi pour adjudication leçon 17 hadith-5ep (pp.94-97)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'
R600 = f'{OUT}/r600'
os.makedirs(R600, exist_ok=True)

BANDS = {
    93: [(0.00, 0.32, 'G1'), (0.28, 0.68, 'G2'), (0.64, 1.00, 'G3')],
    94: [(0.00, 0.38, 'H1'), (0.34, 0.74, 'H2'), (0.70, 1.00, 'H3')],
    95: [(0.00, 0.38, 'I1'), (0.34, 0.72, 'I2'), (0.68, 1.00, 'I3')],
    96: [(0.00, 0.40, 'J1'), (0.36, 0.76, 'J2'), (0.72, 1.00, 'J3')],
    97: [(0.00, 0.40, 'K1'), (0.36, 0.76, 'K2'), (0.72, 1.00, 'K3')],
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
        out = f'{OUT}/c17-{tag}-p{page}.jpg'
        crop.convert('RGB').save(out, 'JPEG', quality=88)
        print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
