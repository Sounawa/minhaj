#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R103 — zooms de précision pour les leçons 611 (p113-117) + 612 (p118-123).
Cible : bandeaus (آية 7 / آيات 8-11), glosses des termes, citations [البقرة],
hadith de Hind, أبو حيان/ابن المواز, boîte d'istithmār (تفسير الطبري),
قراءة بغت, الحساب (قولان), إعراب ذكرا/رسولا, الزمخشري, ابن عاشور 337-338/28,
[إبراهيم 1], [البقرة 256], ابن كثير 8/177 (بتصرف), الإعداد."""
import os

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r103"
os.makedirs(OUT, exist_ok=True)

# (page, dpi, top%, bottom%)
JOBS = [
    (113, 400, 0, 35),    # 611 bandeau «الآية: 7» + objectifs ×3
    (113, 450, 55, 100),  # 611 glosses ذو السعة… (bas de page)
    (114, 450, 0, 35),    # 611 glosses suite (مما آتاه الله / ما آتاها)
    (114, 450, 52, 100),  # 611 ابن عجيبة + الوعد + [الشرح: 5] + فلن يغلب
    (115, 450, 0, 45),    # 611 مالك/أبو حنيفة + citations [البقرة ×2]
    (115, 450, 40, 92),   # 611 hadith Hind + source + أبو حيان + ابن المواز + [البحر المحيط]
    (116, 450, 42, 96),   # 611 boîte الاستثمار (أبو حبيبة) + [تفسير الطبري]
    (117, 400, 0, 60),    # 611 الإعداد القبلي (الآيات 8-11 + العبارات)
    (118, 400, 0, 40),    # 612 bandeau «الآيات: 8-11» + objectifs
    (119, 450, 0, 62),    # 612 glosses + استخلاص + بغت قراءة الجمهور
    (120, 450, 0, 50),    # 612 أبو حيان [البحر المحيط 3/358] + الحساب قولان
    (121, 400, 0, 55),    # 612 فاتقوا + آمنوا + قد أنزل ذكرا + ابن عاشور 337/28
    (121, 450, 42, 100),  # 612 إعراب + ابن عطية + وقيل + الزمخشري + مبينات + ليخرج
    (122, 400, 0, 62),    # 612 [إبراهيم 1] + [البقرة 256] + ابن كثير 8/177 + وعد
    (123, 450, 0, 78),    # 612 التقويم 3-4 + الاستثمار ابن عاشور 338/28 + قواعد
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
