#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R586 — crops 1200 dpi (lecture image directe, chaîne R578-R585).
Leçon 9 ulum-hadith-tanawi-1 (pdf-mut23h2q-120, الحديث المشهور, p.51-54).
  W0  p51 bannière+objectifs (0.02-0.38) — الدرس 9 + المشهور + objectif 1 absent OCR
  W1  p51 intro+bayt ناظم (0.36-0.72) — vocalisation exacte du bayt
  W2  p51 gloss الشرح (0.70-1.00) — شهرتُ الأمر
  W3  p52 zone top (0.02-0.32) — lignes 1-/2- mystère + يشتمل الدرس
  W4  p53 hadith Bukhari (0.16-0.52) — كنت شهيرا يدعو على رجل وذكوان
  W5  p54 استثمار (0.26-0.60) — الزرقاني بحث المشهور/المتواتر
  W6  p54 إعداد قبلي (0.55-1.00) — preuve borne → المعنعن
Sortie : tr-tmp/r586-uh1/crops/W*.png
Usage : python3 scripts-translate/crops-uh1-r586.py [tags...]
"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r586-uh1/crops"

ZONES = [
    ("W0-p51-banniere-objectifs", 51, 0.02, 0.38),
    ("W1-p51-intro-bayt", 51, 0.36, 0.72),
    ("W2-p51-gloss-sharh", 51, 0.70, 1.00),
    ("W3-p52-top-lignes", 52, 0.02, 0.32),
    ("W4-p53-hadith-bukhari", 53, 0.16, 0.52),
    ("W5-p54-istithmar", 54, 0.26, 0.60),
    ("W6-p54-idad-qibli", 54, 0.55, 1.00),
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
        p.get_pixmap(dpi=1200, clip=clip).save(out)
        print(f"[ok] {tag}.png ({os.path.getsize(out)//1024} Ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
