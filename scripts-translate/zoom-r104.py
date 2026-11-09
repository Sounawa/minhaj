#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R104 — zooms composites pour 613 (p124-128) + 614 (p129-134).
Bands empilées en 6 images seulement (économie de lecture)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r104"
os.makedirs(OUT, exist_ok=True)

# Composites : nom → [(page, dpi, top%, bottom%), ...]
COMPOSITES = {
    "comp-A-613-1.png": [
        (124, 400, 0, 32),    # bandeau «الآية: 12» + objectifs ×3
        (124, 450, 30, 75),   # تمهيد
        (125, 450, 2, 55),    # glosses ×2 + استخلاص + الطبري quote + «وإعداما»
    ],
    "comp-A-613-2.png": [
        (125, 450, 45, 95),   # الإسراء + الأرضين + حديثا البخاري + source
        (126, 450, 25, 82),   # مثلهن قولان + الرازي 566/30 + ابن عاشور + réf Taḥrīr
        (127, 450, 0, 50),    # الرازي 2/383 + استفاد 1
    ],
    "comp-A-613-3.png": [
        (127, 400, 45, 90),   # استفاد ×3 + التقويم + الاستثمار
        (128, 450, 0, 60),    # الإعداد (المادة coupée)
    ],
    "comp-B-614-1.png": [
        (129, 400, 0, 34),    # bandeau «الآيتان: 1-2» + objectifs ×3
        (129, 450, 30, 75),   # تمهيد (سورة النبي, مناسبة)
        (130, 450, 2, 60),    # glosses ×5 + استخلاص + story (عسلا, مغافير)
    ],
    "comp-B-614-2.png": [
        (130, 500, 50, 90),   # story end (صمغ الغرفة, جرست النخلة) + p131 عتاب
        (131, 450, 5, 62),    # بخاري + ثانيا + النداء + [الأعراف 30] + أبو حيان 10/207
        (131, 450, 55, 100),  # أقوال تحريم الزوجة (إنما يلزم… مالك المشهور… ابن الماجشون… بائنة/رجعية)
    ],
    "comp-B-614-3.png": [
        (132, 450, 0, 45),    # تبتغي + عفوا + تحليلة + ornate المائدة
        (132, 450, 40, 100),  # [المائدة 91] + kaffāra opinions ×3 + مولىكم
        (133, 450, 25, 80),   # استفاد ×3 + ابن العربي الحصول 109
        (134, 450, 0, 70),    # أتأمل + الإعداد (expressions garbled)
    ],
}

# Bande de renvois de pagination @900 dpi (une ligne chacun)
REFS = [
    (125, 62, 72),   # [تفسير الطبري: 77/23]
    (126, 45, 56),   # [مفاتيح الغيب: 566/30]
    (126, 76, 88),   # [التحرير والتنوير: ??]
    (127, 38, 48),   # [مفاتيح الغيب: 383/2]
    (131, 58, 68),   # [البحر المحيط: 10/207]
    (133, 68, 80),   # [الحصول في أصول الفقه: 109]
]

pdf = fitz.open(PDF)
for name, jobs in COMPOSITES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/z104-{page_no}-{top}.png"
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

imgs = []
for page_no, top, bottom in REFS:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    png = f"/tmp/ref104-{page_no}-{top}.png"
    pg.get_pixmap(dpi=900, clip=clip).save(png)
    imgs.append(Image.open(png))
W = max(i.width for i in imgs)
H = sum(i.height for i in imgs) + 20 * (len(imgs) - 1)
canvas = Image.new("RGB", (W, H), (255, 250, 250))
y = 0
for i in imgs:
    canvas.paste(i, (0, y))
    y += i.height + 20
canvas.save(os.path.join(OUT, "refs-r104-900.png"))
print("refs-r104-900.png", canvas.size)
pdf.close()
