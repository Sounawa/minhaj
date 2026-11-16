#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-21 — ultra-zooms s-série leçon 19 (lignes exactes en litige, bbox-calibrés)
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-19'
R600 = f'{OUT}/r600'

ZOOM = [
    ('s01', 106, 0.125, 0.195, 3.0),  # رجا ثوابه... ضبط جواره التي هي رعايته وهو مسئول
    ('s02', 106, 0.235, 0.365, 2.5),  # ومن أسباب الحث + أ استقامة اللسان
    ('s03', 105, 0.815, 0.965, 2.2),  # قوله... يعني... المنجي الموصل إلى رضوان الله
    ('s04', 106, 0.675, 0.805, 2.5),  # 2. مخاطر اللسان + خص النبي... لخطورته X
    ('s05', 107, 0.055, 0.210, 3.0),  # ب: ارتكابا للزلات... يكب الناس... حصائد
    ('s06', 107, 0.650, 0.735, 3.0),  # عناية خاصة X تماسك المجتمع وترسخ
    ('s07', 108, 0.080, 0.205, 2.5),  # وصية الله لنبيه + ما زال جبريل + سيورثه
    ('s08', 108, 0.740, 0.815, 3.0),  # liste إكرام الضيف items du milieu
    ('s09', 109, 0.085, 0.235, 2.5),  # Ibn Hubayra : يضيف غنيا... يعيرها... اليسير... كلفة
    ('s10', 109, 0.550, 0.625, 3.0),  # item2 fin (والابتعاد) + item3 حث الإسلام
    ('s11', 109, 0.285, 0.375, 2.5),  # ضيّف إبراهيم + آية الذاريات + réf 24
    ('s12', 109, 0.780, 0.910, 2.5),  # تقويم Q2 + Q3
]

for tag, page, a, b, sc in ZOOM:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    crop = im.crop((0, int(a * H), W, int(b * H)))
    out = f'{OUT}/z-{tag}.png'
    if os.path.exists(out):
        continue
    crop = crop.resize((int(crop.width * sc), int(crop.height * sc)), Image.LANCZOS)
    crop.save(out)
    print(f'z-{tag} (p{page} {a:.3f}-{b:.3f} x{sc}) OK {crop.size}')
print('S-SÉRIE TERMINÉE')
