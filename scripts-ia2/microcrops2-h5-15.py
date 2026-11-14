#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-17 — microcrops v2 (positions calibrées par bbox pdftotext)
import os
from PIL import Image

R600 = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-15/r600'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-15'

# (page, y0, y1, tag, upscale)
CROPS = [
    (83, 0.185, 0.365, 'T2-ahdaf', 2.2),    # les 3 objectifs
    (83, 0.375, 0.575, 'T2-tamhid', 2.0),   # exorde + āya Ghafir + ref
    (83, 0.575, 0.900, 'T2-hadith', 2.0),   # hadith + 2 refs
    (84, 0.130, 0.215, 'U2-rawi', 2.6),     # أَبُو هُرَيْرَةَ... ligne
    (84, 0.255, 0.400, 'U2-sharh12', 2.2),  # entrées 1-2 du glossaire
    (84, 0.415, 0.565, 'U2-sharh36', 2.2),  # entrées 3-6
    (84, 0.555, 0.660, 'U2-madamin', 2.4),  # استخلاص المضامين
    (84, 0.680, 0.915, 'U2-tahlil', 2.0),   # intro + أولاً + phrase أبواب
    (85, 0.285, 0.570, 'V2-aya', 2.0),      # 2 citations Baqara + جاء في الحديث
    (85, 0.560, 0.900, 'V2-adab', 2.0),     # مستحبة + 2 bullets
    (86, 0.170, 0.345, 'W2-ihala', 2.2),    # تناول الحرام + استبعاد/إحالة
    (86, 0.480, 0.680, 'W2-yustafad', 2.2), # يستفاد bullets
    (86, 0.690, 0.860, 'W2-taqwim', 2.4),   # تقويم
    (87, 0.170, 0.460, 'X2-isnad', 2.0),    # isnad + matn
    (87, 0.455, 0.560, 'X2-istakhraj', 2.4),# أستخرج item
    (87, 0.550, 0.780, 'X2-idad', 2.2),     # إعداد قبلي
]

for (page, y0, y1, tag, up) in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    crop = im.crop((0, int(y0*H), W, int(y1*H)))
    if crop.width * up > 3400:
        up = 3400 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/mc2-{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=90)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
