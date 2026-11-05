#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R588 — fines 1600 dpi (adjudications critiques, chaîne R578-R587).
Leçon 11 ulum-hadith-tanawi-1 (pdf-mut23h2q-122, الحديث المبهم, p.59-62).
  W1  p61 (0.28-0.36) — وهو ضعيف (شرحبيل بن سعد الخطمي)
  W2  p61 (0.70-0.82) — citation مسلم « دَخَلَتْ أُمُّهَاتٌ بَنَاتُ شَكَّلٌ »
  W3  p62 (0.26-0.40) — isnād « أُمَّهَاتَ بَنَاتِ شَكَّلٍ … أُمَّ هَانِئٍ »
  W4  p62 (0.42-0.60) — « فُلَانُ ابْنُ هُبَيْرَةَ » + « مَرْحَبًا بِأَهْلِ هَانِئٍ »
  W5  p60 (0.14-0.28) — fin liste صيغ « حدثني ابن أم فلان » « حدثني ناسٌ »
Sortie : tr-tmp/r588-uh1/crops/W*.png
Usage : python3 scripts-translate/fines-uh1-r588.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r588-uh1/crops"

ZONES = [
    ("W1-p61-shurhabil-daiif", 61, 0.28, 0.36),
    ("W2-p61-muslim-quote", 61, 0.70, 0.82),
    ("W3-p62-isnad-ummahat", 62, 0.26, 0.40),
    ("W4-p62-fulan-ibn-hubayra", 62, 0.42, 0.60),
    ("W5-p60-fin-liste-nas", 60, 0.14, 0.28),
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
        p.get_pixmap(dpi=1600, clip=clip).save(out)
        print(f"[ok] {tag}.png ({os.path.getsize(out)//1024} Ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
