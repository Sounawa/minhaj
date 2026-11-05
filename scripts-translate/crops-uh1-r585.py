#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R585 — crops 1200 dpi (lecture image directe, chaîne R578-R584).
Leçon 8 ulum-hadith-tanawi-1 (pdf-mut23h2q-119, الحديث العزيز, p.47-50).
  Y0  p47 bannière+objectifs (0.02-0.40) — الدرس 8 + العزيز + 3 objectifs
  Y1  p48 bayt ناظم + المتواتر (0.38-0.72)
  Y2  p48 سُمّي + حبان + نزهة حجر (0.70-1.00)
  Y3  p49 مثاله + hadith محبة + chaîne (0.00-0.40)
  Y4  p49 علاقة جمهور + جبائي/حاكم (0.40-0.66)
  Y5  p49 ابن عربي + شرح بخاري (0.62-0.90)
  Y6  p49 تعقب رد + ابن رشيد (0.86-1.00)
  Y7  p50 تقييم 3 questions (0.00-0.22)
  Y8a p50 استثمار جدة 1/2 (0.22-0.55)
  Y8b p50 استثمار جدة 2/2 (0.55-0.72)
  Y9  p50 questions + إعداد قبلي (0.70-1.00)
  Y10 p51 bannière الدرس 9 + objectifs (0.02-0.34) — preuve borne L120
Sortie : tr-tmp/r585-uh1/crops/Y*.png
Usage : python3 scripts-translate/crops-uh1-r585.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r585-uh1/crops"

ZONES = [
    ("Y0-p47-banniere-objectifs", 47, 0.02, 0.40),
    ("Y1-p48-bayt-mutawatir", 48, 0.38, 0.72),
    ("Y2-p48-summi-hibban-nuzha", 48, 0.70, 1.00),
    ("Y3-p49-mithal-hadith-chaine", 49, 0.00, 0.40),
    ("Y4-p49-alaqa-jamhur-jubbai", 49, 0.40, 0.66),
    ("Y5-p49-ibn-arabi-bukhari", 49, 0.62, 0.90),
    ("Y6-p49-taqqub-rushd", 49, 0.86, 1.00),
    ("Y7-p50-taqwim-questions", 50, 0.00, 0.22),
    ("Y8a-p50-istithmar-jadda-1", 50, 0.22, 0.55),
    ("Y8b-p50-istithmar-jadda-2", 50, 0.55, 0.72),
    ("Y9-p50-questions-idad", 50, 0.70, 1.00),
    ("Y10-p51-banniere-l120", 51, 0.02, 0.34),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    want = set(sys.argv[1:])
    doc = fitz.open(PDF)
    for tag, page, y0, y1 in ZONES:
        if want and tag.split("-")[0] not in want:
            continue
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
