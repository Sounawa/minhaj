#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — zooms composites pour 617 (p146-150) + 618 (p151-156).
Bands empilées en 7 images (économie de lecture, méthode R104/R105)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"
os.makedirs(OUT, exist_ok=True)

COMPOSITES = {
    "comp-A-617-1.png": [
        (146, 450, 2, 50),    # objectifs ×3 + تمهيد + question
        (147, 450, 0, 52),    # glosses ×4 + استخلاص ×2
        (147, 450, 45, 100),  # تفسير أولا (قوا أنفسكم)
    ],
    "comp-A-617-2.png": [
        (148, 450, 0, 50),    # hadith ʿUmar + renvoi Baḥr 10/212 + وقودها + زبانية
        (148, 450, 42, 100),  # يفعلون/يؤمرون + لا عذر للكفار + Rāzī 30/572
        (149, 450, 0, 55),    # استفاد ×4 + التقويم ×3
    ],
    "comp-A-617-3.png": [
        (149, 450, 45, 100),  # istithmār fiṭra (Muwaṭṭaʾ) + renvoi
        (150, 450, 0, 60),    # أتأمل ×3 + الإعداد (آية 8)
    ],
    "comp-B-618-1.png": [
        (151, 450, 2, 48),    # objectifs ×3 + تمهيد + question
        (151, 450, 42, 100),  # bloc verset 8 (calligraphie)
        (152, 450, 0, 55),    # glosses ×2 + استخلاص ×2 + تفسير أولا + ʿUmar
        (152, 450, 48, 100),  # عسل ناصح + الثلاثة + الزمخشري
    ],
    "comp-B-618-2.png": [
        (153, 450, 0, 52),    # وجوب + النور 32 + Muslim 100x + فرائض
        (153, 450, 45, 100),  # آداب ×3 + مراتب ×7 + بواعث ×7
        (154, 450, 0, 30),    # يوم لا يخزي + نورهم معطوف/مبتدأ
    ],
    "comp-B-618-3.png": [
        (154, 450, 22, 72),   # استعارة/حقيقة + نور على قدر الإيمان
        (154, 450, 62, 100),  # ربنا أتمم لنا نورنا + Taḥrīr 28/371
        (155, 450, 0, 55),    # استفاد ×4 + التقويم ×4
    ],
    "comp-B-618-4.png": [
        (155, 450, 48, 100),  # istithmār hadith serviteur (début)
        (156, 450, 0, 62),    # fin hadith + renvoi Bukhārī التوحيد [الفتح 15] + أتأمل + الإعداد
    ],
}

pdf = fitz.open(PDF)
for name, jobs in COMPOSITES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/z106-{page_no}-{top}.png"
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
