#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-17 — microcrops adjudication leçon 15 (zones précises, zoom ×2-3)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-15'
R600 = f'{OUT}/r600'

# (page, y0, y1, x0, x1, tag, upscale)
CROPS = [
    (83, 0.030, 0.115, 0.00, 1.00, 'T-title', 2.6),   # bandeau titre
    (83, 0.105, 0.270, 0.00, 1.00, 'T-ahdaf', 2.0),   # objectifs
    (83, 0.230, 0.470, 0.00, 1.00, 'T-tamhid', 2.0),  # exorde + āya Ghafir
    (83, 0.430, 0.780, 0.00, 1.00, 'T-hadith', 2.0),  # hadith + refs
    (84, 0.000, 0.170, 0.00, 1.00, 'U-rawi', 2.4),    # trad. du hadith / rāwī
    (84, 0.120, 0.480, 0.00, 1.00, 'U-sharh1', 1.9),  # glossaire haut
    (84, 0.380, 0.660, 0.00, 1.00, 'U-sharh2', 1.9),  # glossaire bas + maḍāmīn
    (84, 0.620, 1.000, 0.00, 1.00, 'U-tahlil', 1.9),  # intro analyse + awwalan
    (85, 0.030, 0.360, 0.00, 1.00, 'V-aya1', 1.9),    # citations Baqara 267 x2
    (85, 0.300, 0.620, 0.00, 1.00, 'V-maana', 1.9),   # maʿnā amara + mustahabb
    (86, 0.060, 0.400, 0.00, 1.00, 'W-ihala', 1.9),   # mawāniʿ + laysa ihāla
    (86, 0.330, 0.720, 0.00, 1.00, 'W-yustafad', 1.9),# yustafād + taqwīm
    (87, 0.000, 0.450, 0.00, 1.00, 'X-isnad', 1.9),   # isnād + matn Tabarānī
    (87, 0.640, 1.000, 0.00, 1.00, 'X-i dad', 2.0),   # istakhradj + i dād qablī
]

for (page, y0, y1, x0, x1, tag, up) in CROPS:
    png = f'{R600}/p{page}.png'
    im = Image.open(png)
    W, H = im.size
    crop = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    if crop.width * up > 3400:
        up = 3400 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/mc-{tag.replace(" ", "")}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=88)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
