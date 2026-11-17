#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-26 — re-cadrages de rattrapage (T3b/T4b/T5b/T7b) après échecs de la vague T
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'

ZONES = [
    (122, 880, 1060, 0, 1700, 'T3b', 6),    # ref [صحيح(ا) البخاري ومسلم] — ligne 2 du bloc عبادات
    (123, 900, 1080, 1000, 3700, 'T4b', 5), # بأن يُتْقِنَ الذابح — ligne entière centre
    (123, 2700, 2990, 800, 4600, 'T5b', 4), # والعقارب والفأران أو التي نزل
    (123, 5300, 5600, 3000, 3950, 'T7b', 8) # chiffres [الرحمن: ...]
]

for page, y0, y1, x0, x1, tag, scale in ZONES:
    im = Image.open(f'{R600}/p{page}.png')
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    c.save(f'{OUT}/z22-{tag}.png')
    print(f'{tag}: p{page} px y[{y0}-{y1}] x[{x0}-{x1}] → {c.size} ×{scale}')
