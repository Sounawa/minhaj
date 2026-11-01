#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — re-crops haute résolution pour trancher les formes imprimées en suspens."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"
os.makedirs(OUT, exist_ok=True)

RECROPS = {
    "recrop-A-r106.png": [
        (147, 900, 3, 16),    # glosses وقودها/حفظة/غلاظ/شداد
        (149, 500, 3, 12),    # استفاد 1 (بملازمة/بملاءمة)
        (152, 800, 2, 14),    # glosses نصوحا/يخزي/يكفر
        (153, 500, 28, 62),   # آداب ×3 + مراتب (العادين/العدول)
        (153, 800, 52, 66),   # بواعث (الجبيب/الحبيب, القائم/القادر)
    ],
    "recrop-B-r106.png": [
        (154, 500, 0, 16),    # glosse للذين تابوا / يوم (العامل في يوم)
        (154, 800, 10, 26),   # نور كالنخلة/كالخلة/كالنشأة
        (154, 800, 24, 38),   # يقولون عائدًا على طوائف/إرادة التوزيع
        (154, 900, 44, 52),   # renvoi التحرير والتنوير 371/28 ou 28/371
        (156, 500, 40, 62),   # renvoi Bukhārī التوحيد [الفتح : 15]
    ],
}

pdf = fitz.open(PDF)
for name, jobs in RECROPS.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/rc106-{page_no}-{top}.png"
        pg.get_pixmap(dpi=dpi, clip=clip).save(png)
        imgs.append(Image.open(png))
    W = max(i.width for i in imgs)
    H = sum(i.height for i in imgs) + 24 * (len(imgs) - 1)
    canvas = Image.new("RGB", (W, H), (255, 250, 250))
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + 24
    canvas.save(os.path.join(OUT, name))
    print(name, canvas.size)
pdf.close()
