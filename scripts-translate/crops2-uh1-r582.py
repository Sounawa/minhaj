#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R582 — ultra-crops 1200 dpi (lecture image directe, doctrine R580/R581).
  X0 p33 bannière (0.04-0.32)  — الدرس 5 + titre الحديث المرفوع والحديث المقطوع
  X1 p33 vers (0.50-0.62)      — بيت الناظم « وما أضيف... والتابع وللمقطوع »
  X2 p34 fin (0.82-1.00)       — الفعلي « كانت صلاة النبي بالليل مثتى... » + الوصفي
  X3 p36 قولي (0.09-0.23)      — الحسن البصري « صلِّ وعليه بدعته »
  X4 p36 فعلي (0.15-0.32)      — مسروق « يرخي الستر... يخليهم لدنياهم »
  X5 p36 استثمار (0.70-0.82)   — سعيد بن المسيّب « إذا جئت أرضا يوفون... »
  X6 p37 مسلم (0.00-0.22)      — fin « قدّر الله وما شاء فعل... عمل الشيطان »
  X7 p37 مالك (0.18-0.42)      — « يغطي السلعة... فهذا غرر »
Sortie : tr-tmp/r582-uh1/crops/X*.png
Usage : python3 scripts-translate/crops2-uh1-r582.py
"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r582-uh1/crops"

ZONES = [
    ("X0-p33-banniere", 33, 0.04, 0.32),
    ("X1-p33-vers", 33, 0.50, 0.62),
    ("X2-p34-fin", 34, 0.82, 1.00),
    ("X3-p36-hasan", 36, 0.09, 0.23),
    ("X4-p36-masruq", 36, 0.15, 0.32),
    ("X5-p36-musayyab", 36, 0.70, 0.82),
    ("X6-p37-muslim", 37, 0.00, 0.22),
    ("X7-p37-malik", 37, 0.18, 0.42),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    doc = fitz.open(PDF)
    for tag, page, y0, y1 in ZONES:
        pg = doc[page - 1]
        rect = pg.rect
        clip = fitz.Rect(rect.x0, rect.y0 + rect.height * y0,
                         rect.x1, rect.y0 + rect.height * y1)
        png = f"{WORK}/{tag}.png"
        pg.get_pixmap(dpi=1200, clip=clip).save(png)
        print(tag, os.path.getsize(png))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
