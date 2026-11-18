#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-33 — profil d'encre verticale (numpy) de la zone hadith p156 (y 640-720 pt)
# pour compter les lignes réelles + strips fines tesseract.
from PIL import Image
import numpy as np, subprocess, os

D = '/home/z/my-project/scripts-ia2/tmp/h5-28'
S = 1200 / 72.0
im = Image.open(f'{D}/r1200/p156.png').convert('L')
a = np.asarray(im, dtype=np.uint8)

# zone x 60-580 pt, y 640-725 pt
x0, x1 = int(60*S), int(580*S)
y0, y1 = int(640*S), int(725*S)
z = a[y0:y1, x0:x1]
ink = (z < 128).astype(np.float32)   # encre = sombre

# profil par ligne de pixels : densité
prof = ink.mean(axis=1)
runs, cur, start = [], False, 0
for i, v in enumerate(prof):
    if v > 0.004 and not cur:
        cur, start = True, i
    elif v <= 0.004 and cur:
        cur = False
        if i - start > 8:
            runs.append((start, i))
if cur: runs.append((start, len(prof)))
print('bandes d encre (y pt rel 640):')
for s, e in runs:
    y_pt = 640 + s / S
    h_pt = (e - s) / S
    dens = ink[s:e].mean()
    print(f'  y={y_pt:6.1f}pt h={h_pt:4.1f}pt dens={dens:.3f}')

# strips fines par bande détectée
os.makedirs(f'{D}/crops', exist_ok=True)
for k, (s, e) in enumerate(runs):
    pad = 6
    ys, ye = max(0, y0 + s - pad), y0 + e + pad
    strip = Image.open(f'{D}/r1200/p156.png').crop((x0, ys, x1, ye))
    fp = f'{D}/crops/L-strip{k}.png'
    strip.save(fp)
    r = subprocess.run(['tesseract', fp, 'stdout', '-l', 'ara',
                        '--tessdata-dir', '/home/z/my-project/scripts-translate/tessdata',
                        '--psm', '7'], capture_output=True, text=True)
    print(f'strip{k} y={640+s/S:.1f}-{640+e/S:.1f}pt =>', r.stdout.strip()[:120])
