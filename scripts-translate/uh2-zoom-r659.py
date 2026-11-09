# -*- coding: utf-8 -*-
# R659 — zooms 900 dpi des zones conflictuelles de la leçon 23 uh2 (p.120-124)
# Adjudications attendues : refs miroir (628/826, 782/287, 18761/16781, 218/812,
# 384/483, 385/583, 389/983, 387/783, 2/43-2/34, 1/70), noms (السِّياق/الساق,
# خاصا/خاضا, واضل الأحذب/واصل الأحدب, العوام/الحوام, الليث/ابن لهيعة), matn
# (... أو بتغيير مع بقاء السياق: فالمصحف والمحرف), التقويم item 2-3, rubrique
# الاستثمار/الاستتمار, citation Ibn aṣ-Ṣalāḥ p.124 (بطون الكتب).
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r659"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    (120, 55, 265, "z900-p120-objectifs"),
    (120, 255, 435, "z900-p120-tamhid"),
    (120, 405, 525, "z900-p120-matn"),
    (120, 515, 765, "z900-p120-sharh-istikhlas"),
    (121, 30, 135, "z900-p121-def-refs"),
    (121, 245, 445, "z900-p121-isnad"),
    (121, 435, 660, "z900-p121-matan-muslim"),
    (122, 235, 345, "z900-p122-sam-names"),
    (122, 495, 645, "z900-p122-musnad"),
    (122, 635, 765, "z900-p122-luga-ref"),
    (123, 28, 120, "z900-p123-top"),
    (123, 85, 265, "z900-p123-jabir"),
    (123, 325, 505, "z900-p123-hukm-end"),
    (123, 550, 765, "z900-p123-ahtadi-taqwim"),
    (124, 55, 305, "z900-p124-quote"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, min(y1, page.rect.height))
    pix = page.get_pixmap(dpi=900, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
