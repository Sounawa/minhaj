# -*- coding: utf-8 -*-
# R662 — crops TIGHT (cadrés sur les tokens localisés r662-locate-277.py)
# Conflits à trancher PAR IMAGE : السياق/السُّباق, المحرف/التحرف (objectifs),
# وبينوا/وميزوا + المخالفة/الخلافَة, المتون/المتن + كان/كائن, chaîne isnad,
# فرد عليه/فردّه, بإسناده/بشّاده, bracket مسلم (حجرة/حجيرة, المسافر وقصرها),
# واضل الأحذب/واصل الأحدب, ref المسند 18761, مقاييس 2/43|2/34, «53» p.123,
# hadith جابر (فكواه), note غندر, clause والقدر/فالمصحف, التقويم 2-3,
# rubrique الاستثمار/الاستتمار p.124. Sortie : tr-tmp/qa-crops-r662/
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r662"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    (120, 40, 125, 0, 0, 1200, "t-p120-title"),
    (120, 122, 205, 0, 0, 1500, "t-p120-obj"),
    (120, 295, 355, 60, 560, 1800, "t-p120-tamhid-1"),
    (120, 440, 530, 60, 560, 1200, "t-p120-matn-ctx"),
    (120, 478, 528, 130, 340, 2500, "t-p120-siyaaq-word"),
    (121, 245, 308, 60, 560, 1800, "t-p121-ahamiyya-1"),
    (121, 340, 475, 60, 560, 1500, "t-p121-isnad-chain"),
    (121, 490, 560, 60, 560, 1800, "t-p121-correction"),
    (121, 545, 765, 60, 560, 1200, "t-p121-matan-example"),
    (122, 172, 272, 60, 560, 1800, "t-p122-sam"),
    (122, 385, 508, 60, 560, 1500, "t-p122-maani"),
    (122, 685, 725, 280, 520, 2500, "t-p122-luga-tight"),
    (123, 26, 88, 370, 595, 2500, "t-p123-def53-tight"),
    (123, 26, 135, 60, 560, 1200, "t-p123-def-line"),
    (123, 100, 250, 60, 560, 1500, "t-p123-jabir"),
    (123, 195, 325, 60, 560, 1800, "t-p123-ghundar"),
    (123, 400, 502, 60, 560, 1800, "t-p123-hukm"),
    (123, 598, 765, 60, 560, 1200, "t-p123-ahtadi-taqwim"),
    (124, 50, 100, 200, 430, 2500, "t-p124-rubric-tight"),
    (124, 95, 330, 60, 560, 1200, "t-p124-quote"),
]
for p, y0, y1, x0, x1, dpi, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(x0 or 0, y0, x1 or page.rect.width, min(y1, page.rect.height))
    pix = page.get_pixmap(dpi=dpi, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
