#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — microcrops 600 dpi des zones contestées de la leçon 12 hadith-5ep → composites empilés
from PIL import Image
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-12/zooms'
os.makedirs(OUT, exist_ok=True)

# rendu 600 dpi des pages contestées
for p in [69, 70, 71, 72, 73]:
    subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(p), '-l', str(p), SRC, f'{OUT}/big-{p}'], check=True)

# résolution des rendus 600 dpi
big = {}
for f in sorted(os.listdir(OUT)):
    if f.startswith('big-') and f.endswith('.png'):
        pg = int(f.split('-')[1].split('.')[0])
        big[pg] = Image.open(f'{OUT}/{f}')
        print(f, big[pg].size)

S = 4  # facteur 150dpi -> 600dpi

def crop(pg, x0, y0, x1, y1, label):
    im = big[pg]
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
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

# COMP-A : objectif 1 (p69) + أسْرَج (p70 L3 fin) + السُّرْج في المسجد (p70 L4) + قصّ وعطّف (p70)
stack([
    crop(69, 280, 400, 700, 475, 'obj1-ومدلّيها'),
    crop(70, 160, 328, 560, 398, 'أسْرَج-finL3'),
    crop(70, 830, 368, 1180, 432, 'السُّرْج-في-المسجد'),
    crop(70, 430, 368, 1000, 438, 'قصّ-وعطّف'),
], f'{OUT}/comp-A.png')

# COMP-B : بائنه وصنع منبر (p70 L5) + عمر رضي الله (p70 L5 droite) + لمعروّها وسّموها (p71) + وتبييهم/غفلوا (p72) + وتبليغهم (p72)
stack([
    crop(70, 380, 418, 830, 485, 'بائنه-وصنع-منبر'),
    crop(70, 810, 418, 1180, 485, 'عمر-رضي-الله-عنه'),
    crop(71, 320, 493, 780, 558, 'لمعروّها-وسّموها'),
    crop(72, 480, 788, 800, 852, 'وتبييهم'),
    crop(72, 240, 788, 580, 852, 'بما-غفلوا'),
    crop(72, 790, 836, 1140, 900, 'وتَبْلِغَهم'),
], f'{OUT}/comp-B.png')

# COMP-C : ويكره لهم (p72 L7) + تفقضي (p73) + āya 1 début (p73) + āya 1 fin
stack([
    crop(72, 400, 1248, 920, 1312, 'ويكره-لهم'),
    crop(73, 140, 452, 720, 512, 'تَفْقِضِي'),
    crop(73, 690, 848, 1140, 918, 'aya1-debut'),
    crop(73, 130, 848, 600, 918, 'aya1-fin'),
], f'{OUT}/comp-C.png')

# COMP-D : āya 2 (A'rāf) en 3 bandes
stack([
    crop(73, 740, 940, 1140, 1018, 'aya2-debut'),
    crop(73, 430, 940, 830, 1018, 'aya2-milieu'),
    crop(73, 120, 940, 520, 1018, 'aya2-fin'),
], f'{OUT}/comp-D.png')

# COMP-E : āya 3 (al-Qaṣaṣ) en 3 bandes
stack([
    crop(73, 740, 1018, 1140, 1096, 'aya3-debut'),
    crop(73, 430, 1018, 830, 1096, 'aya3-milieu'),
    crop(73, 120, 1018, 520, 1096, 'aya3-fin'),
], f'{OUT}/comp-E.png')
