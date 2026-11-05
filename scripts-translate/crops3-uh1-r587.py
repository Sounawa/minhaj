#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R587 — crops3 (adjudications sensibles, 1400/1600 dpi).
  X4  p57 (0.26-0.40) 1400 dpi — quote ابن الصلاح « وفما/وفيما قاله مسلم نظر »
      + « فيشترط لقيهما لتحمَّل العنعنة على السماع »
  X5  p57 (0.43-0.66) 1600 dpi — « من قبيل المرسل » + « فلذا جاء عن شعبة »
Sortie : tr-tmp/r587-uh1/crops/X4*.png X5*.png
Usage : python3 scripts-translate/crops3-uh1-r587.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r587-uh1/crops"

ZONES = [
    ("X4-p57-ibn-salah-quote", 57, 0.26, 0.40, 1400),
    ("X5-p57-qabil-faladha", 57, 0.43, 0.66, 1600),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = set(sys.argv[1:]) or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    for tag, page, f0, f1, dpi in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + (r.y1 - r.y0) * f0, r.x1, r.y0 + (r.y1 - r.y0) * f1)
        out = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=dpi, clip=clip).save(out)
        print(f"[ok] {tag}.png ({os.path.getsize(out)//1024} Ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
