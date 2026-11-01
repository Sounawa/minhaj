#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R105 — re-crops haute résolution pour trancher les formes imprimées en suspens."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r105"
os.makedirs(OUT, exist_ok=True)

RECROPS = {
    "recrop-A-615.png": [
        (135, 400, 64, 96),   # bloc calligraphique versets 66:3-4
        (136, 900, 3, 14),    # glosses 1-2 (بعض أزواجه / أخبرت)
        (137, 800, 43, 58),   # الخازن renvoi + فقوله حذف الفاعل
        (137, 800, 68, 80),   # فلما تباها + ما أخبر
        (139, 800, 38, 52),   # استفاد 1 (المسلمون عند شروطهم)
        (140, 500, 8, 46),    # hadith Ibn ʿAbbās (وعجبا لك + renvoi Bukhārī)
    ],
    "recrop-B-616.png": [
        (142, 500, 72, 100),  # citation ʿUmar + renvoi Bukhārī tafsīr
        (143, 500, 42, 78),   # citation الحجرات/الذاريات + التسهيل 2/152 + الغيب 30/571
        (144, 800, 0, 14),    # عابدات القاسمي renvoi
        (145, 500, 0, 36),    # boîte hadiths (تربت/ترتب يداك + renvois Muslim/Tirmidhī)
    ],
}

pdf = fitz.open(PDF)
for name, jobs in RECROPS.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/rc105-{page_no}-{top}.png"
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
