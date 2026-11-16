#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-21 — composites 600 dpi pour adjudication leçon 19 hadith-5ep (pp.104-110)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-19'
R600 = f'{OUT}/r600'
os.makedirs(R600, exist_ok=True)

BANDS = {
    104: [(0.00, 0.30, 'A1'), (0.24, 0.62, 'A2'), (0.56, 1.00, 'A3')],
    105: [(0.00, 0.30, 'B1'), (0.24, 0.58, 'B2'), (0.52, 0.84, 'B3'), (0.78, 1.00, 'B4')],
    106: [(0.00, 0.30, 'C1'), (0.24, 0.58, 'C2'), (0.52, 0.84, 'C3'), (0.78, 1.00, 'C4')],
    107: [(0.00, 0.30, 'D1'), (0.24, 0.58, 'D2'), (0.52, 0.84, 'D3'), (0.78, 1.00, 'D4')],
    108: [(0.00, 0.30, 'E1'), (0.24, 0.58, 'E2'), (0.52, 0.84, 'E3'), (0.78, 1.00, 'E4')],
    109: [(0.00, 0.30, 'F1'), (0.24, 0.58, 'F2'), (0.52, 0.84, 'F3'), (0.78, 1.00, 'F4')],
    110: [(0.00, 0.40, 'G1'), (0.30, 0.70, 'G2'), (0.60, 1.00, 'G3')],
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
        out = f'{OUT}/z-c19-{tag}.png'
        if os.path.exists(out):
            continue
        im.crop((0, int(a * H), W, int(b * H))).save(out)
        print(f'z-c19-{tag} (p{page} {a:.2f}-{b:.2f}) OK')
print('COMPOSITES TERMINÉS')
