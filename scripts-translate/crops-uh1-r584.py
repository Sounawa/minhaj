#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R584 — crops 1200 dpi (lecture image directe, chaîne R580-R583).
Leçon 7 ulum-hadith-tanawi-1 (pdf-mut23h2q-118, الحديث المسلسل, p.43-46).
  Z0 p43 bannière (0.02-0.20)      — الدرس 7 + titre المسلسل
  Z1 p43 baytān + fin (0.55-0.98)  — المسلسل قل ما على وصف أتى… + الشرح + questions
  Z2 p44 baytān + définition (0.28-0.58)
  Z3 p44 حال قولي + Muʿāḏ (0.60-1.00)
  Z4 p45 Nasaʾī + qawl (0.00-0.28)
  Z5 p45 Abū Hurayra فعلي (0.28-0.56)
  Z6 p45 Anas اجتماع (0.52-0.80)
  Z7 p45 صفات الرواية (0.76-1.00)
  Z8 p46 زمن الرواية ابن عباس (0.00-0.36)
Sortie : tr-tmp/r584-uh1/crops/Z*.png
Usage : python3 scripts-translate/crops-uh1-r584.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r584-uh1/crops"

ZONES = [
    ("Z0-p43-banniere", 43, 0.02, 0.20),
    ("Z1-p43-baytan-fin", 43, 0.55, 0.98),
    ("Z2-p44-baytan-def", 44, 0.28, 0.58),
    ("Z3-p44-qawli-muadh", 44, 0.60, 1.00),
    ("Z4-p45-nasai-qawl", 45, 0.00, 0.28),
    ("Z5-p45-hurayra-fili", 45, 0.28, 0.56),
    ("Z6-p45-anas-ijtima", 45, 0.52, 0.80),
    ("Z7-p45-sifat-riwaya", 45, 0.76, 1.00),
    ("Z8-p46-zaman-makan", 46, 0.00, 0.36),
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
