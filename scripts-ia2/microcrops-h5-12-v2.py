#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — microcrops round 2, coordonnées recalibrées (x×4.282, y×3.835)
from PIL import Image
import os

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-12/zooms'
big = {}
for p in [69, 70, 71, 72, 73]:
    path = f'{OUT}/big-{p}-0{p}.png'
    big[p] = Image.open(path)

SX, SY = 4.282, 3.835  # disp(150dpi affiché) -> 600dpi réel

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

# COMP-F : objectif 1 (p69) + السُّرْج في المسجد (p70) + وعطّف بالصّابحين (p70)
stack([
    crop(69, 540, 395, 900, 480, 'obj1-ومدلّيها-v2'),
    crop(70, 800, 428, 1180, 494, 'السُّرْج-في-المسجد-v2'),
    crop(70, 290, 428, 810, 494, 'وعطّف-بالصّابحين-v2'),
], f'{OUT}/comp-F.png')

# COMP-G : عمر رضي الله عنه بائنه (p70 L5 droite) + بائنه وصنع منبر (p70 L5 gauche) + لمعروّها وسّموها (p71)
stack([
    crop(70, 660, 485, 1180, 550, 'عمر-رضي-الله-v2'),
    crop(70, 140, 485, 680, 550, 'بائنه-وصنع-منبر-v2'),
    crop(71, 290, 538, 910, 612, 'لمعروّها-وسّموها-v2'),
], f'{OUT}/comp-G.png')

# COMP-H : وتبييهم + غفلوا (p72 L2) + وتبليغهم (p72 L3) + ويكره (p72 L7)
stack([
    crop(72, 640, 833, 1180, 897, 'وتبييهم-v2'),
    crop(72, 230, 833, 660, 897, 'بما-غفلوا-v2'),
    crop(72, 680, 883, 1180, 947, 'وتَبْلِغَهم-v2'),
    crop(72, 370, 1293, 950, 1362, 'ويكره-لهم-v2'),
], f'{OUT}/comp-H.png')

# COMP-I : تفقضي (p73) + āya1 (3 bandes)
stack([
    crop(73, 130, 498, 740, 562, 'تَفْقِضِي-v2'),
    crop(73, 690, 893, 1145, 970, 'aya1-d'),
    crop(73, 410, 893, 730, 970, 'aya1-m'),
    crop(73, 125, 893, 450, 970, 'aya1-f'),
], f'{OUT}/comp-I.png')

# COMP-J : āya2 (3 bandes)
stack([
    crop(73, 730, 963, 1145, 1044, 'aya2-d'),
    crop(73, 420, 963, 770, 1044, 'aya2-m'),
    crop(73, 115, 963, 460, 1044, 'aya2-f'),
], f'{OUT}/comp-J.png')

# COMP-K : āya3 (3 bandes)
stack([
    crop(73, 730, 1038, 1145, 1120, 'aya3-d'),
    crop(73, 420, 1038, 770, 1120, 'aya3-m'),
    crop(73, 115, 1038, 460, 1120, 'aya3-f'),
], f'{OUT}/comp-K.png')
