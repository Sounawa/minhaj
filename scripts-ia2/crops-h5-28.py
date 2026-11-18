#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-33 — recadrages ciblés 1200 dpi natifs (leçon 28) pour les points disputés :
#  A: p156 ouverture du النص (titre ?)  B: p156 hadith ligne 1 (المحجة ?)
#  C: p156 hadith ligne 2               D: p156 ligne «نتيجة غضب م[ذ/د]موم»
#  F: p157 الغضب الم[ذ/د]موم (فهم 2)    G: p157 تحليل 3 (fin — في المجتمع)
#  H: p158 bandeau de section            I: p156 mot غضب مذموم SERRE (encre)
#  J: p157 mot المذموم SERRE (encre)
# Convention : bbox en points PDF (page 637.2x807.12) ; r1200 => ×1200/72 = 16.6667
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h5-28'
S = 1200 / 72.0

zones = [
    # (page, nom, x0,y0,x1,y1 en points)
    (156, 'A-nass-ouverture',  60, 350, 580, 415),
    (156, 'B-hadith-l1',       60, 650, 580, 683),
    (156, 'C-hadith-l2',       60, 678, 580, 712),
    (156, 'D-ghadab-mdmoum',   60, 622, 580, 657),
    (157, 'F-fahm2-mdmoum',   130, 198, 580, 228),
    (157, 'G-tahlil3-fin',    130, 545, 580, 612),
    (158, 'H-bandeau',         60,  85, 580, 168),
]

for p, nom, x0, y0, x1, y1 in zones:
    im = Image.open(f'{D}/r1200/p{p}.png')
    box = (int(x0*S), int(y0*S), int(x1*S), int(y1*S))
    crop = im.crop(box)
    out = f'{D}/crops/{nom}.png'
    os.makedirs(f'{D}/crops', exist_ok=True)
    crop.save(out)
    print(nom, crop.size)
