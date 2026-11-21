#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — rogne chaque encadré p.74 (bordures détectées) + tess psm4/6 sur chacun.
from PIL import Image
import subprocess, os

D = '/home/z/my-project/scripts-ia2/tmp/h6-13'
im = Image.open(f'{D}/r1200/p74.png').convert('RGB')
S = 1200 / 72.0
OUT = f'{D}/encadres'
os.makedirs(OUT, exist_ok=True)
TESS = '/home/z/my-project/tessdata'

ENCS = [  # (numéro, x0, x1) pt — ordre de lecture droite→gauche
    (1, 493, 572), (2, 403, 483), (3, 325, 404),
    (4, 235, 314), (5, 155, 234), (6, 65, 144),
]
y0, y1 = 268, 473

for n, x0, x1 in ENCS:
    crop = im.crop((int(x0 * S), int(y0 * S), int(x1 * S), int(y1 * S)))
    png = f'{OUT}/enc{n}.png'
    crop.save(png)
    for psm in (4, 6):
        r = subprocess.run(['tesseract', png, 'stdout', '--psm', str(psm), '-l', 'ara',
                            '--tessdata-dir', TESS],
                           capture_output=True, text=True, timeout=300)
        txt = r.stdout.strip()
        if txt:
            open(f'{OUT}/enc{n}-psm{psm}.txt', 'w', encoding='utf-8').write(txt)
    print(f'enc{n}: {crop.size}')
print('OK')
