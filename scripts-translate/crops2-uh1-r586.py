#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R586 — crops2 1400 dpi (re-lecture fine, chaîne R578-R585).
Leçon 9 ulum-hadith-tanawi-1 (الحديث المشهور, p.51-54).
  X1 p52 (0.28-0.48)  quote bayt + définition + ويرد
  X2 p52 (0.48-0.76)  اشترط + bloc citation Ibn Mandah
  X3 p52 (0.76-1.00)  Ibn Hajar + المشهور/المستفيض
  X4 p53 (0.28-0.44)  ligne hadith Bukhari + référence
  X5 p53 (0.50-0.88)  paragraphe chaîne des transmetteurs
  X6 p51 (0.66-0.82)  ligne bayt (vocalisation finale)
Sortie : tr-tmp/r586-uh1/crops/X*.png
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r586-uh1/crops"

ZONES = [
    ("X1-p52-quote-bayt-def", 52, 0.28, 0.48),
    ("X2-p52-ibn-mandah", 52, 0.48, 0.76),
    ("X3-p52-hajar-mustafid", 52, 0.76, 1.00),
    ("X4-p53-hadith-ligne", 53, 0.28, 0.44),
    ("X5-p53-chaine", 53, 0.50, 0.88),
    ("X6-p51-bayt-fin", 51, 0.66, 0.82),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = set(sys.argv[1:]) or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    for tag, page, f0, f1 in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + (r.y1 - r.y0) * f0, r.x1, r.y0 + (r.y1 - r.y0) * f1)
        out = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=1400, clip=clip).save(out)
        print(f"[ok] {tag}.png ({os.path.getsize(out)//1024} Ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
