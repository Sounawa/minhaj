#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-32 — bandes 1200 dpi natives pour les points contestés (mapping cluster validé)
from PIL import Image
import os

DIR = '/home/z/my-project/scripts-ia2/tmp/h5-27'
OUT = f'{DIR}/bands'
os.makedirs(OUT, exist_ok=True)

# (id, page, y0, y1) px 1200 — pleine largeur 250-10370, jamais de ligne coupée
B = [
    ('b01', 150, 8300, 12000),  # encadré hadith (orné) : sanad + matn + [صحيح مسلم]
    ('b02', 151, 4900, 5900),   # الفهم/الشرح : glose أَرَأَيْتَ (2 derniers mots)
    ('b03', 151, 11550, 12250), # وَلِبَيَانِ مَوْضُوعِ الدَّرْسِ تُتَنَاوَلُ/نَتَنَاوَلُ
    ('b04', 152, 1800, 2750),   # glose النووي (اجْتَنَبْتُهُ/أَجْتَنِبْتُهُ + فَعَلْتُهُ)
    ('b05', 153, 2250, 2950),   # وَأَفَادَ/أَقَادَ صَاحِبُ الْمَفْهُومِ
    ('b06', 153, 5480, 6650),   # يُثَابِرُونَ... مُثَابَرَتِهِمْ + اغْتِنَامِ ثَوَابِهَا + تَنْمِيَةِ
    ('b07', 153, 9200, 10300),  # الحاصل : يُتَقَرَّبُ بِهَا ... مَحَبَّة (2 lignes)
    ('b08', 154, 3160, 3850),   # item 2 : تَنْمِيَةٌ/تَنْمِيمٌ/تَثْمِيمٌ لِلْفَرَائِضِ
    ('b09', 154, 6420, 7150),   # تقويم Q2 : الْفَوَائِدِ/الْقَوَاعِدِ
    ('b10', 154, 10600, 11850), # استثمار : بِالْعِلِّيَّةِ/بِالْعِلَّةِ (2 lignes)
    ('b11', 155, 3600, 4450),   # box tail : لَكِنْ لَا بُدَّ... + crochet
    ('b12', 155, 6800, 9200),   # الاِعْدَادُ الْقَبْلِيُّ (items ?)
]

for cid, p, y0, y1 in B:
    out = f'{OUT}/{cid}-p{p}.png'
    if os.path.exists(out):
        continue
    im = Image.open(f'{DIR}/r1200/p{p}.png').crop((250, y0, 10370, y1))
    im.save(out)
    print(cid, im.size, 'OK')
print('done')
