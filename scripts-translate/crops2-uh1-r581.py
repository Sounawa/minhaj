#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R581 — ultra-crops 1200 dpi (lecture image directe, doctrine R580).
  X1 p28 bannière stricte (0.00-0.14)  — numéro « الدرس 4 » + titre (ornée)
  X2 p31 ligne 2 du poème استثمار (0.78-0.87) — يُجبَر / يُخْبَر (ح/خ)
Sortie : tr-tmp/r581-uh1/crops/X*.png
Usage : python3 scripts-translate/crops2-uh1-r581.py
"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r581-uh1/crops"

ZONES = [
    ("X1-p28-banniere-strict", 28, 0.00, 0.14),
    ("X2-p31-poeme-l2", 31, 0.76, 0.88),
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
