#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R105 — zooms composites pour 615 (p135-140) + 616 (p141-145).
Bands empilées en 7 images (économie de lecture, méthode R104)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r105"
os.makedirs(OUT, exist_ok=True)

COMPOSITES = {
    "comp-A-615-1.png": [
        (135, 400, 30, 68),   # bloc versets 66:3-4 (calligraphie)
        (136, 450, 2, 52),    # الهم glosses ×6 + استخلاص ×2
        (136, 450, 45, 95),   # التفسير أولا + قول الأول
    ],
    "comp-A-615-2.png": [
        (137, 450, 0, 50),    # القول الثاني + عاقبة حفصة + الخازن quote + renvoi
        (137, 450, 45, 100),  # كلما تكتم + وأظهر الله + عرض عن بعض + الكسائي + تظاهرا
    ],
    "comp-A-615-3.png": [
        (138, 450, 0, 45),    # ثانيا وعظ + صغت + ابن مسعود + عاصم نبيه
        (138, 450, 38, 100),  # المولى وجهان
        (139, 450, 0, 42),    # fin ʿUmar + الصالحين مفرد/جمع
        (139, 450, 35, 88),   # استفاد ×4
    ],
    "comp-A-615-4.png": [
        (140, 450, 0, 55),    # الاستثمار hadith Ibn ʿAbbās + renvoi Bukhārī
        (140, 450, 48, 95),   # أتأمل ×3 + الإعداد (آية 5)
    ],
    "comp-B-616-1.png": [
        (141, 400, 52, 100),  # bloc verset 5 (calligraphie)
        (142, 450, 0, 50),    # الهم glosses ×5 + استخلاص + تفسير début
        (142, 450, 42, 100),  # عسى ربه + نصرة وتسلية + citation ʿUmar + renvoi
    ],
    "comp-B-616-2.png": [
        (143, 450, 0, 48),    # عسى للرجاء/التحقيق + Ālūsī 28/155 + ثمان صفات
        (143, 450, 40, 100),  # citation faces islām/īmān (Hujurāt 14, Qaṣaṣ/Dhāriyāt, التسهيل) + Rāzī 30/571
        (144, 450, 0, 52),    # عابدات القاسمي 9/275 + سائحات + ثيبات/أبكار
    ],
    "comp-B-616-3.png": [
        (144, 450, 45, 100),  # الخازن 4/316 + استفاد ×2
        (145, 450, 0, 50),    # الاستثمار hadiths ×2 + renvoi Tirmidhī
        (145, 450, 42, 100),  # أتأمل + الإعداد (6-7)
    ],
}

pdf = fitz.open(PDF)
for name, jobs in COMPOSITES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/z105-{page_no}-{top}.png"
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
