#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R590 — fine crops haute résolution p.69-71 (adjudication image, zéro vision API).
Leçon 13 ulum-hadith-tanawi-1 (pdf-mut23h2q-124, الحديث الموقوف, p.69-71).
  F1 p69 (0.56-0.78) 1800 — متن bayt (vocalisation)
  F2 p69 (0.72-1.00) 1800 — الشرح glose (« زكن: سكن/غلم »)
  F3 p70 (0.00-0.22) 1500 — en-tête + 2 questions top
  F4 p70 (0.24-0.46) 1600 — يشتمل + أولا + bayt (double occurrence)
  F5 p70 (0.56-0.72) 1600 — ثانيا header (« ومميزاته/ومظاته »)
  F6 p71 (0.00-0.24) 1500 — التقويم en-tête + Q1-Q3
  F7 p71 (0.30-0.62) 1800 — الاستثمار 2 bayts al-ʿIrāqī
  F8 p71 (0.58-0.80) 1500 — instruction + Q1 + Q2 fin
  F9 p69 (0.00-0.17) 1500 — bannière (badge الدرس 13)
Sortie : tr-tmp/r590-uh1/crops/<tag>.png (+ OCR psm6)
Usage : python3 scripts-translate/crops-fine-uh1-r590.py [tags F1..F9]
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
    ("F1-p69-matn-bayt-1800", 69, 0.56, 0.78, 1800),
    ("F2-p69-sharh-glose-1800", 69, 0.72, 1.00, 1800),
    ("F3-p70-top-questions-1500", 70, 0.00, 0.22, 1500),
    ("F4-p70-awwalan-bayt-1600", 70, 0.24, 0.46, 1600),
    ("F5-p70-thanawi-header-1600", 70, 0.56, 0.72, 1600),
    ("F6-p71-taqwim-1500", 71, 0.00, 0.24, 1500),
    ("F7-p71-istithmar-bayts-1800", 71, 0.30, 0.62, 1800),
    ("F8-p71-istithmar-q-1500", 71, 0.58, 0.80, 1500),
    ("F9-p69-banniere-1500", 69, 0.00, 0.17, 1500),
    ("F10-p70-thanawi-header2-1800", 70, 0.70, 0.84, 1800),
    ("F11-p69-bayt-2400", 69, 0.62, 0.72, 2400),
    ("F12-p69-glose-zukn-2400", 69, 0.85, 0.93, 2400),
    ("F13-p69-avant-matn-1800", 69, 0.50, 0.61, 1800),
    ("F14-p70-q2-mot-2400", 70, 0.13, 0.22, 2400),
    ("F15-p71-bayt1-2400", 71, 0.36, 0.51, 2400),
    ("F16-p71-q2-fin-2400", 71, 0.54, 0.68, 2400),
    ("F17-p70-q2-mot-3000", 70, 0.145, 0.195, 3000),
    ("F18-p69-bayt-line-3000", 69, 0.655, 0.705, 3000),
    ("F19-p71-bayts-3000", 71, 0.365, 0.465, 3000),
    ("F20-p71-q2-3000", 71, 0.545, 0.655, 3000),
    ("F21-p69-glose-3000", 69, 0.855, 0.925, 3000),
    ("F22-p70-thanawi-3000", 70, 0.615, 0.665, 3000),
]

# (tag, page, x0, x1, y0, y1, dpi) — recadrages horizontaux fins
XZONES = [
    ("F23-p70-q2-mot-x-3000", 70, 0.20, 0.52, 0.148, 0.196, 3000),
    ("F24-p70-thanawi-mot-x-3000", 70, 0.33, 0.68, 0.612, 0.662, 3000),
    ("F25-p71-bayt2-parenth-x-3000", 71, 0.34, 0.60, 0.405, 0.448, 3000),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = set(sys.argv[1:]) or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, f0, f1, dpi in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + (r.y1 - r.y0) * f0, r.x1, r.y0 + (r.y1 - r.y0) * f1)
        out = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=dpi, clip=clip).save(out)
        ocrtxt = out[:-4] + "-ocr.txt"
        subprocess.run(["tesseract", out, ocrtxt[:-4], "-l", "ara", "--psm", "6"],
                       env=env, capture_output=True, text=True)
        txt = open(ocrtxt, encoding="utf-8").read()
        print(f"===== {tag}.png ({os.path.getsize(out)//1024} Ko, {dpi} dpi) — OCR psm6 =====")
        print(txt)
        print()

    for tag, page, x0, x1, f0, f1, dpi in XZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0 + (r.x1 - r.x0) * x0, r.y0 + (r.y1 - r.y0) * f0,
                         r.x0 + (r.x1 - r.x0) * x1, r.y0 + (r.y1 - r.y0) * f1)
        out = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=dpi, clip=clip).save(out)
        ocrtxt = out[:-4] + "-ocr.txt"
        subprocess.run(["tesseract", out, ocrtxt[:-4], "-l", "ara", "--psm", "6"],
                       env=env, capture_output=True, text=True)
        print(f"===== {tag}.png ({os.path.getsize(out)//1024} Ko, {dpi} dpi) =====")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
