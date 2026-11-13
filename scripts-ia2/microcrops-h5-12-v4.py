#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — microcrops round 4 (final) : encadré الاستثمار en 4 bandes L/R + 4 mots restants
from PIL import Image
import os

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-12/zooms'
big = {}
for p in [70, 71, 72, 73]:
    big[p] = Image.open(f'{OUT}/big-{p}-0{p}.png')

SX, SY = 4.282, 3.835

def crop(pg, x0, y0, x1, y1, label):
    im = big[pg]
    c = im.crop((int(x0*SX), int(y0*SY), int(x1*SX), int(y1*SY)))
    if c.width > 1560:
        c = c.resize((1560, int(c.height*1560/c.width)), Image.LANCZOS)
    print(f'{label}: {c.size}')
    return c

def stack(crops, out):
    w = max(c.width for c in crops)
    h = sum(c.height for c in crops) + 14*(len(crops)-1)
    comp = Image.new('RGB', (w, h), 'white')
    y = 0
    for c in crops:
        comp.paste(c, ((w-c.width)//2, y))
        y += c.height + 14
    comp.save(out)
    print('COMPOSITE', out, comp.size, os.path.getsize(out)//1024, 'Ko')

# COMP-M : 4 mots restants
stack([
    crop(70, 120, 368, 470, 442, 'السُّرْج-في-المسجد-v4'),
    crop(71, 320, 540, 620, 620, 'لمعْمُورِها-v4'),
    crop(73, 125, 415, 900, 520, 'استفاد-items-v4'),
    crop(72, 280, 1510, 1020, 1585, 'ويكره-لهم-v4'),
], f'{OUT}/comp-M.png')

# COMP-N : encadré الاستثمار — bandes 1-2 (intro āya1 + āya1 + intro āya2), coupées L/R
stack([
    crop(73, 610, 895, 1145, 1060, 'box-b1-R'),
    crop(73, 115, 895, 640, 1060, 'box-b1-L'),
    crop(73, 610, 1050, 1145, 1190, 'box-b2-R'),
    crop(73, 115, 1050, 640, 1190, 'box-b2-L'),
], f'{OUT}/comp-N.png')

# COMP-O : encadré الاستثمار — bandes 3-4 (fin āya2 + āya3 + أفهم), L/R
stack([
    crop(73, 610, 1180, 1145, 1310, 'box-b3-R'),
    crop(73, 115, 1180, 640, 1310, 'box-b3-L'),
], f'{OUT}/comp-O.png')
