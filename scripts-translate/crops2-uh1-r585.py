#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R585 — micro-crops 1400 dpi (mots difficiles, chaîne R582-R584).
  W1 p49 y 0.42-0.49 — « وإليه يومئ/يومي كلام الحاكم »
  W2 p49 y 0.78-0.87 — « لا يعترد/يعتد بها » dans تعقب
  W3 p49 y 0.345-0.40 — « ولم تتوفر فيهما/فيهم شروط الصحة »
Sortie : tr-tmp/r585-uh1/crops/W*.png
"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r585-uh1/crops"

ZONES = [
    ("W5-p50-qaraid-straddle", 50, 0.525, 0.585),
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
        pg.get_pixmap(dpi=1400, clip=clip).save(png)
        print(tag, os.path.getsize(png))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
