#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — microcrops round 3 : 6 points restants, coordonnées recalibrées v3
from PIL import Image
import os

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-12/zooms'
big = {}
for p in [70, 71, 72]:
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

# COMP-L : 6 adjudications finales
stack([
    crop(70, 920, 368, 1180, 440, 'أسْرَج-السُّرْج-v3'),
    crop(70, 128, 428, 350, 494, 'بَيْنَهُ-v3'),
    crop(71, 420, 543, 710, 617, 'لمعْمُورِها-وسّموها-v3'),
    crop(72, 690, 923, 1180, 992, 'وتبييهم-وما-غفلوا-v3'),
    crop(72, 690, 978, 1180, 1047, 'وتَبْلِغَهم-v3'),
    crop(72, 290, 1468, 1010, 1537, 'ويكره-لهم-v3'),
], f'{OUT}/comp-L.png')
