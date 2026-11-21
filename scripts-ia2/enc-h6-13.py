#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — détection des colonnes d'encadrés p.74 (y265-470) par analyse des pixels bleus,
# puis découpe en tranches verticales pour tess 1200 dpi.
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h6-13'
im = Image.open(f'{D}/r1200/p74.png').convert('RGB')
S = 1200 / 72.0
y0, y1 = int(265 * S), int(470 * S)
w = im.size[0]

# 1) carte des colonnes bleues (bordures des encadrés)
zone = im.crop((0, y0, w, y1))
zw, zh = zone.size
px = zone.load()
col_blue = []
for x in range(zw):
    cnt = 0
    for y in range(0, zh, 8):
        r, g, b = px[x, y]
        if b > 120 and b > r + 30 and b > g + 20:
            cnt += 1
    col_blue.append(cnt)
# seuil : colonnes très bleues = bordures verticales
thr = max(col_blue) * 0.5
borders = [x for x, c in enumerate(col_blue) if c > thr and c > 10]
# regroupe
groups = []
for x in borders:
    if groups and x - groups[-1][-1] <= 6:
        groups[-1].append(x)
    else:
        groups.append([x])
centers = [sum(g) // len(g) for g in groups]
print('bordures verticales bleues (px):', centers)
print('bordures verticales bleues (pt):', [round(c / S, 1) for c in centers])

# 2) tranches tess : pleine largeur y265-470 en 4 tranches horizontales chevauchantes
OUT = f'{D}/enc-tranches'
os.makedirs(OUT, exist_ok=True)
full = im.crop((0, y0, w, y1))
fw, fh = full.size
n = 4
ov = 200
th = (fh + ov * (n - 1)) // n
for i in range(n):
    top = max(0, (fh - th) * i // (n - 1))
    bot = min(fh, top + th)
    t = full.crop((0, top, fw, bot))
    t.save(f'{OUT}/t{i+1}.png')
    print(f't{i+1}: y{top}-{bot} {t.size}')
print('OK')
