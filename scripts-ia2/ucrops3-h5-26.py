#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-31 — DERNIERS scrutins : 9 recadrages ultra-ciblés (1200 dpi ×2) pour les mots encore ouverts
from PIL import Image
import os

DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26'
OUT = f'{DIR}/crops3'
os.makedirs(OUT, exist_ok=True)

# (id, page, x0, y0, x1, y1) en px 1200 dpi, upscale x2
W = [
    ('w1', 144, 7000, 4550, 10100, 5080),  # أَحْرِصَ (أهداف item 3)
    ('w2', 144, 3000, 6420, 6800, 7560),   # تمهيد L1-L2 : مُلَخِّصٍ + ponctuation نافعة
    ('w3', 146, 3400, 2680, 6600, 3320),   # أَعْمَلُ عَلَيْهِ وَأَثِقُ/أَتَّقِ/أَنْقِي بِهِ
    ('w4', 146, 250, 7330, 3600, 8020),    # عمر : يَرُوغُوا/يَرُوعُوا رَوْغَانَ الثَّعْلَبِ/التَّعْلُّبِ
    ('w5', 147, 4400, 3600, 7900, 4270),   # «قُلْ/فَقُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ»
    ('w6', 147, 7100, 10230, 10100, 10920),# الواسطي : قَدُحَتِ/قَبَحَتِ الْمَحَاسِنُ
    ('w7', 147, 1400, 10640, 4900, 11320), # وَثَمَرَاتِهَا/وَثَمَرَتِهَا (en-tête ثمرات)
    ('w8', 149, 1900, 3130, 6300, 3800),   # encadré أنس : جَارُهُ/جَارَهُ بَوَائِقَهُ
    ('w9', 147, 4400, 2240, 7600, 2900),   # الَّتِي تُفِيدُ/تَقْدِمُ التَّرْتِيبَ
]

for cid, p, x0, y0, x1, y1 in W:
    dst = f'{OUT}/{cid}-p{p}.png'
    if os.path.exists(dst):
        continue
    im = Image.open(f'{DIR}/r1200/p{p}.png').crop((x0, y0, x1, y1))
    im = im.resize((im.width*2, im.height*2), Image.LANCZOS)
    im.save(dst)
    print(cid, im.size, 'OK')
print('done')
