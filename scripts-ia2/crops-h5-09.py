#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — micro-crops d'adjudication (points calligraphiques contestés)
import os
from PIL import Image

TMP = '/home/z/my-project/scripts-ia2/tmp/h5-09'
OUT = f'{TMP}/crops'
os.makedirs(OUT, exist_ok=True)

# (page, x1, y1, x2, y2, nom, facteur)  — coordonnées sur le rendu 300 dpi pleine page (2655×3363)
CROPS = [
    (58,  500, 1780, 2100, 1930, 'titre-thalitha', 2.2),   # titre rouge ثالثاً
    (58,    0, 2260, 2655, 2500, 'aya-p58', 2.0),          # āya calligraphique + réf
    (58,    0,  250, 2655,  420, 'sawaa-ibtudia', 2.0),    # سواء ابتُدِعَهُ فاعلٌ أو سُبِقَ إليه
    (58,    0, 1020, 2655, 1140, 'biraddi-furu', 2.0),     # وكالاجتهاد بِرَدِّ فروعِ الفقه
    (58,  800, 1890, 2300, 2070, 'la-yuqbal-sahibih', 2.6),# لا يُقبَل/يَنقَبُ صاحبُه
    (59,    0, 1630, 2655, 2010, 'ayat-istithmar', 2.0),   # 2 āyas du cadre استثمار
    (59,  300, 1890, 2400, 2000, 'muajjam-gloss', 2.4),    # ligne المعجم
    (57,  850, 1640, 2250, 1790, 'istikhras-title', 2.6),  # استخلاص المضامين/المفاهيم
]

for pg, x1, y1, x2, y2, name, fac in CROPS:
    src = Image.open(f'{TMP}/plates/hi-{pg}.png')
    im = src.crop((x1, y1, x2, y2))
    im = im.resize((int(im.width * fac), int(im.height * fac)), Image.LANCZOS)
    im.save(f'{OUT}/{name}.png')
    print(name, im.size)
print('OK crops')
