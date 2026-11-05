#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R590 — crops 1200 dpi p.69-71 de ulum-hadith-1-thanawi.pdf + OCR local psm 6.
Leçon 13 ulum-hadith-tanawi-1 (pdf-mut23h2q-124, الحديث الموقوف, p.69-71).
Zones sensibles (OCR 300 dpi dégradé) :
  C1  p69 (0.00-0.30) — bannière الدرس 13 + أهداف (3 objectifs)
  C2  p69 (0.28-0.62) — تمهيد + متن bayt (vocalisation)
  C3  p69 (0.58-1.00) — الشرح glose (« زكن » critique)
  C4  p70 (0.00-0.28) — 2 questions top + en-tête éventuel
  C5  p70 (0.22-0.66) — يشتمل + أولا تعريف + bayt + أثر/خبر + توسع
  C6  p70 (0.62-1.00) — ثانيا شروط + الحاكم + الجمهور + الجوامع + ابن بدر
  C7  p71 (0.00-0.30) — التقويم en-tête + questions
  C8  p71 (0.25-0.80) — الاستثمار bayt + 2 questions
  C9  p71 (0.75-1.00) — إعداد قبلي (المرسل)
Sortie : tr-tmp/r590-uh1/crops/<tag>.png + <tag>-ocr.txt
Usage : python3 scripts-translate/crops-uh1-r590.py [tags C1..C9]
"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r590-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("C1-p69-banniere-objectifs", 69, 0.00, 0.30),
    ("C2-p69-tamhid-matn", 69, 0.28, 0.62),
    ("C3-p69-sharh-glose", 69, 0.58, 1.00),
    ("C4-p70-top-questions", 70, 0.00, 0.28),
    ("C5-p70-extraction-awwalan", 70, 0.22, 0.66),
    ("C6-p70-thanawi-fin", 70, 0.62, 1.00),
    ("C7-p71-taqwim", 71, 0.00, 0.30),
    ("C8-p71-istithmar", 71, 0.25, 0.80),
    ("C9-p71-idad-qabli", 71, 0.75, 1.00),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = set(sys.argv[1:]) or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, f0, f1 in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + (r.y1 - r.y0) * f0, r.x1, r.y0 + (r.y1 - r.y0) * f1)
        out = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=1200, clip=clip).save(out)
        # OCR local de la bande (psm 6 : bloc uniforme) — adjudication zéro vision
        ocrtxt = out[:-4] + "-ocr.txt"
        subprocess.run(["tesseract", out, ocrtxt[:-4], "-l", "ara", "--psm", "6"],
                       env=env, capture_output=True, text=True)
        txt = open(ocrtxt, encoding="utf-8").read()
        print(f"===== {tag}.png ({os.path.getsize(out)//1024} Ko) — OCR psm6 =====")
        print(txt)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
