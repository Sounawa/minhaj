#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — adjudication DERNIÈRE : (1) segmentation en lignes du bloc item-2 p.46
# puis profil mot-à-mot de la ligne «كل سلامى» ; (2) super-crop du mot disputé
# p.47 (x=394-432) + comptage des points au-dessus du corps par composante.
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/micro', exist_ok=True)

def load(pg):
    return np.array(Image.open(f'{DIR}/r1200/p{pg}.png').convert('L'))

# ── (1) lignes du bloc item-2 p.46 (y=405-485) ──
print('═══ (1) SEGMENTATION EN LIGNES p.46 y=405-485 ═══')
im46 = load(46)
blk = im46[int(405*S):int(485*S), int(60*S):int(570*S)].astype(int)
ink = blk < 130
rows = ink.sum(axis=1)
bands, inb = [], False
for y, v in enumerate(rows):
    if v > 8 and not inb:
        inb, ya = True, y
    elif v <= 8 and inb:
        inb = False
        if y - ya > 8:
            bands.append((ya, y))
if inb: bands.append((ya, len(rows)))
lines = [(405 + ya/S, 405 + yb/S) for ya, yb in bands]
print(f'{len(lines)} lignes détectées :')
for ya, yb in lines:
    print(f'  y=[{ya:6.1f}-{yb:6.1f}]pt h={yb-ya:4.1f}pt')

# profil de chaque ligne : runs d'encre avec classification point/lettre
for li, (ya, yb) in enumerate(lines):
    y0, y1 = int(ya*S), int(yb*S)
    seg = (im46[y0:y1, int(60*S):int(570*S)] < 130)
    colprof = seg.sum(axis=0)
    runs, inr = [], False
    for x, v in enumerate(colprof):
        if v >= 1 and not inr:
            inr, xa = True, x
        elif v < 1 and inr:
            inr = False
            runs.append((xa, x))
    if inr: runs.append((xa, len(colprof)))
    # fusion des runs < 2.2pt de séparation
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < 2.2*S/1:
            merged[-1] = (merged[-1][0], r[1])
        else:
            merged.append(r)
    print(f'  — ligne {li+1} (y={ya:.0f}-{yb:.0f}) : {len(merged)} groupes')
    for xa, xb in merged:
        w = (xb - xa) / S
        dens = seg[:, xa:xb].mean()
        kind = 'POINT' if w < 2.8 and dens > 0.2 else 'txt'
        print(f'      x=[{60+xa/S:5.1f}-{60+xb/S:5.1f}] l={w:5.1f}pt d={dens:.2f} {kind}')

# ── (2) mot disputé p.47 : super-crop + points ──
print()
print('═══ (2) MOT DISPUTÉ p.47 (x=392-434, y=493-523) ═══')
im47 = load(47)
word = im47[int(493*S):int(523*S), int(392*S):int(434*S)].astype(int)
# seuil local
g = word
thr = (np.percentile(g, 15) + np.percentile(g, 85)) / 2
b = (g < thr)
# composantes (flood approx par lignes/colonnes sur le binaire)
from scipy import ndimage
lab, n = ndimage.label(b)
sizes = ndimage.sum(b, lab, range(1, n+1))
objs = ndimage.find_objects(lab)
print(f'{n} composantes ; seuil={thr:.0f}')
comps = []
for i, sl in enumerate(objs):
    if sizes[i] < 3:
        continue
    y0, y1 = sl[0].start, sl[0].stop
    x0, x1 = sl[1].start, sl[1].stop
    h, w = y1-y0, x1-x0
    area = sizes[i]
    # un point = petit et compact
    isdot = (h <= 9 and w <= 9 and area <= 45)
    comps.append((x0/S, y0/S, w/S, h/S, area, 'DOT' if isdot else 'GLYPH'))
for x0, y0, w, h, area, k in sorted(comps):
    print(f'  x={392+x0:5.1f} y={493+y0:5.1f} w={w:4.1f} h={h:4.1f} a={area:5.0f} {k}')
# super-crop pour tesseract
img = Image.fromarray(np.where(b, 0, 255).astype(np.uint8))
img = img.resize((img.width*3, img.height*3), Image.LANCZOS)
fp = f'{DIR}/micro/qword-super.png'
img.save(fp)
for psm in (8, 7, 6, 13):
    base = f'{DIR}/micro/qword-super'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    txt = open(base + '.txt', encoding='utf-8').read().strip()
    if txt:
        print(f'  [super/psm{psm}] {txt[:80]}')
