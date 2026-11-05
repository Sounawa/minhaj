#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R587 — crops2 1400 dpi (adjudications fines, chaîne R578-R586).
  X1  p57 (0.36-0.58) — quote ابن الصلاح « وفما/وفيما قاله مسلم نظر » + عاصروه
      + اشتراط ابن السمعاني/أبي عمرو الداني/القابسي
  X2  p57 (0.58-0.95) — شعبة « لا يجزئ » / سفيان « يجزئ » / رجع عن قوله
      + النووي « مردود بإجماع السلف »
  X3  p56 (0.22-0.42) — sentence التحليل « وإذا صح المشهور الاصطلاحي… »
      + « يشتمل هذا الدرس على ما يأتي »
Sortie : tr-tmp/r587-uh1/crops/X*.png
Usage : python3 scripts-translate/crops2-uh1-r587.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r587-uh1/crops"

ZONES = [
    ("X1-p57-ibn-salah-quote", 57, 0.36, 0.58),
    ("X2-p57-shuba-sufyan", 57, 0.58, 0.95),
    ("X3-p56-tahlil-sentence", 56, 0.22, 0.42),
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
