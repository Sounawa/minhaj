#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R583 — ultra-crops 1200 dpi (lecture image directe, doctrine R580-R582).
  Y0 p38 bannière (0.02-0.18)  — الدرس 6 + titre الحديث المسند والمتصل
  Y1 p38 baytān (0.58-0.84)    — المسند + المتصل (صدر وعجز)
  Y2 p40 verse mutaṣil (0.70-0.86) — وسمع كل راوٍ يتصل…
  Y3 p40 baḫarī matn (0.26-0.46)   — لا يُصلي أحدكم في الثوب الواحد…
  Y4 p40 muwaṭṭa matn1 (0.84-1.00) — صلاة الجماعة تفضل صلاة الفرد…
  Y5 p41 muwaṭṭa matn2 (0.00-0.32) — عمر: أيما امرأة طلقت…
  Y6 p41 ibn ḥaǧar (0.44-0.80)     — وأما الحاكم وغيره… النكت 1/506
  Y7 p39 verse-quote (0.32-0.46)   — reprise du bayt au šarḥ (backup Y1)
Sortie : tr-tmp/r583-uh1/crops/Y*.png
Usage : python3 scripts-translate/crops2-uh1-r583.py
"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r583-uh1/crops"

ZONES = [
    ("Y0-p38-banniere", 38, 0.02, 0.18),
    ("Y1-p38-baytan", 38, 0.58, 0.84),
    ("Y2-p40-verse-mutasil", 40, 0.70, 0.86),
    ("Y3-p40-bahari-matn", 40, 0.26, 0.46),
    ("Y4-p40-muwatta-matn1", 40, 0.84, 1.00),
    ("Y5-p41-muwatta-matn2", 41, 0.00, 0.32),
    ("Y6-p41-ibnhajar", 41, 0.44, 0.80),
    ("Y7-p39-verse-quote", 39, 0.32, 0.46),
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
