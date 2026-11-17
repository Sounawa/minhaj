#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-22 — composites 600 dpi pour adjudication leçon 20 hadith-5ep (pp.111-113)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-20'
R600 = f'{OUT}/r600'
os.makedirs(R600, exist_ok=True)

BANDS = {
    111: [(0.00, 0.28, 'A1'), (0.22, 0.52, 'A2'), (0.46, 0.74, 'A3'), (0.68, 1.00, 'A4')],
    112: [(0.00, 0.34, 'B1'), (0.28, 0.60, 'B2'), (0.54, 0.86, 'B3'), (0.80, 1.00, 'B4')],
    113: [(0.00, 0.30, 'C1'), (0.24, 0.58, 'C2'), (0.52, 0.84, 'C3'), (0.78, 1.00, 'C4')],
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
        out = f'{OUT}/z-c20-{tag}.png'
        if os.path.exists(out):
            continue
        im.crop((0, int(a * H), W, int(b * H))).save(out)
        print(f'z-c20-{tag} (p{page} {a:.2f}-{b:.2f}) OK')
print('COMPOSITES TERMINÉS')
