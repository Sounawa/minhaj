#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — anatomie finale : (1) nature des glyphes dans les 4 bandeaux pp.46-49
# (2) micro-zone du mot disputé du header questions p.47 (أغلاه?)
# (3) structure exacte du remplissage «كل سلامى» l.1-2 p.46
# (4) points diacritiques de «فانثروا» p.47 (ن).
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
S = 1200 / 72.0

def load(pg):
    return np.array(Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB'))

# ── (1) nature des glyphes dans les bandeaux ──
print('═══ (1) BANDEAUX : nature des glyphes ═══')
bands = [
    (46, 214, 305, 547, 345, 'p46-b2 (أنجز في دفترi?)'),
    (47, 211, 77, 426, 109, 'p47-b1 (النصوص الشرعية?)'),
    (48, 211, 77, 426, 109, 'p48-b1 (أنشطة?)'),
    (49, 211, 77, 427, 109, 'p49-b1 (مشروع?)'),
    (49, 216, 360, 427, 392, 'p49-b2 (الإعداد القبلي)'),
]
for pg, x0, y0, x1, y1, lbl in bands:
    im = load(pg)
    c = im[int(y0*S):int(y1*S), int(x0*S):int(x1*S), :].astype(int)
    g = c.mean(axis=2)
    sat = c.max(axis=2) - c.min(axis=2)
    colored = sat > 40
    n = colored.sum()
    if n < 100:
        print(f'{lbl}: pas de zone colorée'); continue
    lum_colored = g[colored]
    # au sein de la zone colorée : pixels clairs (blancs = lettres) vs foncés
    bright = (lum_colored > 180).sum()
    dark = (lum_colored < 90).sum()
    med = np.median(lum_colored)
    print(f'{lbl}: fond médian={med:.0f} | px clairs(>180)={bright} ({100*bright/n:.1f}%) | px foncés(<90)={dark} ({100*dark/n:.1f}%)')

# ── (2) micro-zone mot disputé du header questions p.47 ═══
print()
print('═══ (2) HEADER QUESTIONS p.47 : colonne du mot disputé ═══')
im47 = load(47)
# ligne y≈495-515 (bbox yMin 501) ; mot après النصوص : chercher via profil d'encre
line = im47[int(495*S):int(518*S), int(200*S):int(545*S), :].astype(int)
g = line.mean(axis=2)
ink = (g < 120)
colprof = ink.sum(axis=0)
# segmenter en mots (colonnes d'encre)
runs = []
inr = False
for x, v in enumerate(colprof):
    if v > 2 and not inr:
        inr, xa = True, x
    elif v <= 2 and inr:
        inr = False
        if x - xa > 8:
            runs.append((xa, x))
if inr: runs.append((xa, len(colprof)))
print(f'{len(runs)} segments d\\u2019encre (droite→gauche):')
for xa, xb in reversed(runs):
    w = (xb - xa) / S
    seg = g[:, xa:xb]
    dens = (seg < 120).mean()
    print(f'  x=[{200 + xa/S:5.1f}-{200 + xb/S:5.1f}]pt largeur={w:5.1f}pt densité={dens:.3f}')
