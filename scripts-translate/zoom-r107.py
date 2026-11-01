#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R107 — zooms composites pour 619 (p157-162) + 620 (p163-166).
Bands empilées en 6 images (économie de lecture, méthode R104/R105/R106)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r107"
os.makedirs(OUT, exist_ok=True)

COMPOSITES = {
    "comp-A-619-1.png": [
        (157, 450, 0, 48),    # bandeau + objectifs ×3 + تمهيد
        (157, 450, 44, 100),  # bloc calligraphique 66:9-10 + renvoi
        (158, 450, 0, 52),    # glosses ×5 + استخلاص ×2
        (158, 450, 44, 100),  # تفسير أولا : توجيهات قرآنية + قتادة/مجاهد
    ],
    "comp-A-619-2.png": [
        (159, 450, 0, 50),    # غلظ عليهم + Ibn ʿĀshūr 28/372 + تعايش
        (159, 450, 44, 100),  # bloc الممتحنة + وأويهم + ثانيا قصة المرأتين
        (160, 450, 0, 52),    # نoms والهة/والعة + خانتاهما ابن عباس
        (160, 450, 46, 100),  # مثال لأزواج النبي باطل + البيضاوي 5/226 + استفاد ×3
    ],
    "comp-A-619-3.png": [
        (161, 450, 0, 55),    # استفاد ×1 + التقويم ×3 + istithmār début
        (161, 450, 48, 100),  # fatwa fin + renvoi [2 صفر 1437 / 14 نونبر 2015]
        (162, 450, 0, 60),    # أتأمل ×2 + الإعداد القبلي expressions
    ],
    "comp-B-620-1.png": [
        (163, 450, 0, 46),    # bandeau + objectifs ×3 + تمهيد
        (163, 450, 42, 100),  # bloc calligraphique 66:11-12 + renvoi
        (164, 450, 0, 50),    # glosses ×3 + استخلاص ×2 + تفسير أولا + البيضاوي
        (164, 450, 44, 100),  # آسية + دعاء + فقبض الله روحها
    ],
    "comp-B-620-2.png": [
        (165, 450, 0, 50),    # ثانيا مريم + أحصنت فرجها + نفخنا فيه + إضافة الروح
        (165, 450, 44, 100),  # الآلوسي Rūḥ + صدقت بكلمات + قراءات + القانتين + استفاد ×1
        (166, 450, 0, 60),    # استفاد ×4 + التقويم ×3 + استثمار
    ],
}

pdf = fitz.open(PDF)
for name, jobs in COMPOSITES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/z107-{page_no}-{top}.png"
        pg.get_pixmap(dpi=dpi, clip=clip).save(png)
        im = Image.open(png)
        if im.width > 1500:
            nh = int(im.height * 1500 / im.width)
            im = im.resize((1500, nh), Image.LANCZOS)
        imgs.append(im)
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
