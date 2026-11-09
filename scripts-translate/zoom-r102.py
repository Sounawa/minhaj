#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R102 — zooms de précision pour les leçons 609 (p99-105) + 610 (p106-112).
Cible : tamhīd al-Mustadrak, glosses des termes, citations d'al-Qurṭubī,
Ibn Kathīr, al-Ṭirmiḏī, Muwaṭṭaʾ (Fāṭima bint Qays), parole dʿUmar,
musnad al-Ṭayālasī, Ibn ʿĀšūr 28/327, Ibn al-ʿArabī 4/287, tableau d'évaluation."""
import os

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r102"
os.makedirs(OUT, exist_ok=True)

# (page, dpi, top%, bottom%)
JOBS = [
    (99, 400, 8, 78),     # 609 objectifs 2-3 + tamhīd Ubayy ibn Kaʿb + questions + orné
    (100, 500, 5, 52),    # 609 termes + citation البقرة (226 ?) + début tafsīr
    (101, 500, 5, 55),    # 609 من لا قرء لها + glosses + début Qurṭubī
    (101, 500, 50, 88),   # 609 citation Qurṭubī + [165/18 ?] + ارتبتم
    (102, 400, 5, 72),    # 609 علي/ابن عباس + سبيعة الأسلمية + ابن مسعود + [البقرة 232]
    (103, 500, 5, 78),    # 609 ابن كثير [152/8] + تلكم أمر الله + الترمذي + مسند أحمد
    (104, 400, 5, 72),    # 609 التقويم 4 + الاستثمار [البقرة 226/234 ?] + الإعداد
    (105, 500, 5, 45),    # 609 الإعداد القبلي : العبارتان garbled
    (108, 400, 5, 78),    # 610 Fāṭima bint Qays Muwaṭṭa + parole ʿUmar + al-Ṭayālasī
    (109, 500, 18, 66),   # 610 citation Ibn ʿĀšūr + réf البقرة + ثانيا
    (110, 500, 5, 78),    # 610 فإن أرضعن + ائتمروا + «ومنه» [القصص 19 ?] + تعاسرتم
    (111, 400, 5, 82),    # 610 التقويم tableau + ابن العربي + [287/4]
]

pdf = fitz.open(PDF)
for page_no, dpi, top, bottom in JOBS:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    name = f"p{page_no}-{dpi}-{top}-{bottom}.png"
    pix.save(os.path.join(OUT, name))
    print(f"{name}: {pix.width}x{pix.height}")
pdf.close()
