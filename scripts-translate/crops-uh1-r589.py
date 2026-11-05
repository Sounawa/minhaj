#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R589 — crops 1200 dpi p.64-69 de ulum-hadith-1-thanawi.pdf + OCR local psm 6.
Leçon 12 ulum-hadith-tanawi-1 (pdf-mut23h2q-123, الحديث العالي والنازل, p.64-67).
Zones sensibles (OCR 300 dpi dégradé) :
  C1  p64 (0.42-0.68) — bayt « وكل ما قلت رجاله علا * وضده ذاك الذي قد نزلا » + الشرح
  C2  p66 (0.03-0.30) — bullets العلو النسبي fin (« بتقدم/بتقام ») + ثانيا النازل + bayt
  C3  p66 (0.30-0.62) — فإذا كان + أقسام النزول (المطلق + النسبي début)
  C4  p67 (0.06-0.36) — Muwaṭṭaʾ isnād + « بسبع وعشرين درجة » + référence
  C5  p67 (0.36-0.72) — Bayhaqī isnād (noms dégradés) + « بخمسة وعشرين جزءا » + réf.
  C6  p69 (0.02-0.16) — bannière الدرس 13 (preuve borne)
Sortie : tr-tmp/r589-uh1/crops/<tag>.png + <tag>-ocr.txt
Usage : python3 scripts-translate/crops-uh1-r589.py [tags C1..C6]
"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r589-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("C1-p64-bayt-sharh", 64, 0.42, 0.68),
    ("C2-p66-bullets-nazil-bayt", 66, 0.03, 0.30),
    ("C3-p66-aqsam-nuzul", 66, 0.30, 0.62),
    ("C4-p67-muwatta-27", 67, 0.06, 0.36),
    ("C5-p67-bayhaqi-25", 67, 0.36, 0.72),
    ("C6-p69-banniere-L13", 69, 0.02, 0.16),
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
