#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-26 — zooms ultimes pour départage final (leçon 22) : T1-T9
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'

# (page, y0px, y1px, x0px, x1px, tag, scale)
ZONES = [
    (120, 3330, 3900, 200, 2000, 'T1', 5),   # الإيمان/الإتقان + الجنان/الجنان (fins de lignes 3-4)
    (122, 2060, 2340, 3850, 5300, 'T2', 6),  # الحوار/الجوار (début de ligne)
    (122, 830, 990, 50, 1150, 'T3', 6),      # ref [صحيح(ا) البخاري ومسلم]
    (123, 850, 1080, 1650, 3150, 'T4', 6),   # يُتْقِنَ (le tāʾ ?)
    (123, 2670, 2980, 1750, 4250, 'T5', 5),  # العقارب والفأران + أَوِ الَّتِي
    (123, 3120, 3700, 0, 5310, 'T6', 2),     # item 1 de ومما يستفاد + numérotation
    (123, 5270, 5480, 40, 760, 'T7', 8),     # chiffres de [الرحمن: ٦٠/٥٩]
    (124, 4460, 4700, 0, 5310, 'T8', 2),     # ligne d'instruction الإعداد (الآتيَ ?)
]

for page, y0, y1, x0, x1, tag, scale in ZONES:
    im = Image.open(f'{R600}/p{page}.png')
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    c.save(f'{OUT}/z22-{tag}.png')
    print(f'{tag}: p{page} px y[{y0}-{y1}] x[{x0}-{x1}] → {c.size} ×{scale}')
