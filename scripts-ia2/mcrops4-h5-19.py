#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-21 — recadrages MOT-NIVEAU w-série (bbox-calibrés, x fraction de largeur)
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-19'
R600 = f'{OUT}/r600'

# (tag, page, y0, y1, x0, x1, scale) — x/y en fractions de page
CROPS = [
    ('w01', 106, 0.160, 0.200, 0.50, 0.92, 3.5),  # ضبط [جواره التي هي] رعاياه وهو مسئول
    ('w02', 107, 0.685, 0.728, 0.55, 0.86, 3.5),  # عناية خاصة تمكن تمسك المجتمع وترسخ
    ('w03', 109, 0.203, 0.245, 0.40, 0.64, 4.0),  # بما فتح الله [له؟] من غير كلفة
    ('w04', 109, 0.562, 0.602, 0.74, 0.92, 4.0),  # حثّ/حثَّ الإسلام على الجود
    ('w05', 109, 0.793, 0.848, 0.28, 0.96, 2.8),  # Q2 كاملة
    ('w06', 107, 0.126, 0.168, 0.38, 0.60, 4.0),  # وهل يكب/يكبّ الناس في النار
]

for tag, page, a, b, c, d, sc in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    crop = im.crop((int(c * W), int(a * H), int(d * W), int(b * H)))
    out = f'{OUT}/z-{tag}.png'
    if os.path.exists(out):
        continue
    crop = crop.resize((int(crop.width * sc), int(crop.height * sc)), Image.LANCZOS)
    crop.save(out)
    print(f'z-{tag} (p{page} y{a:.3f}-{b:.3f} x{c:.2f}-{d:.2f} x{sc}) OK {crop.size}')
print('W-SÉRIE TERMINÉE')
