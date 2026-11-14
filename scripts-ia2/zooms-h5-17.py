#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-19 — zooms adjudication leçon 17 (pp.93-97), ×3-×5
from PIL import Image
import os

R600 = '/home/z/my-project/scripts-ia2/tmp/h5-16/r600'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'

# (page, y0, y1, x0, x1, tag, upscale)
Z = [
    (95, 0.110, 0.190, 0.00, 1.00, 'm-muhsin', 3.5),    # فهو المحسن الكف؛ لأنه... (2-3 lignes)
    (94, 0.842, 0.915, 0.00, 1.00, 'm-yuaddu', 4.0),   # الذي يعد/يعتبر/يعبر مرتبة عالية
    (93, 0.630, 0.914, 0.10, 1.00, 'm-hadref', 3.0),   # encadré hadith + référence
    (96, 0.318, 0.352, 0.30, 1.00, 'm-fiqh', 5.0),     # يريدون الفقه/الفضل + صدق الحديث
    (96, 0.488, 0.520, 0.30, 1.00, 'm-yanfauhu', 5.0), # اشغاله بما ينفعه/يعنيه من الأمور
    (96, 0.565, 0.760, 0.00, 1.00, 'm-zarqani', 3.0),  # citation الزرقاني complète
    (97, 0.300, 0.530, 0.00, 1.00, 'm-ghazali', 3.0),  # citation الغزالي complète
    (96, 0.118, 0.152, 0.00, 1.00, 'm-nuqila', 4.5),   # ونقل/روي عنهم آثار كثيرة
    (95, 0.780, 0.845, 0.20, 0.90, 'm-yughnika', 4.5), # تكلمت بما لا يغنيك/يعنيك (مالك بن دينار)
]

for (page, y0, y1, x0, x1, tag, up) in Z:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    crop = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    if crop.width * up > 3600:
        up = 3600 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=90)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
