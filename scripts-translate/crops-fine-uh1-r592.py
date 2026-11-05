#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R592 — crops fins 1600-2400 dpi p.76-79 (zones resserrées, passe 2).
Zones :
  F1 p76 (0.55-0.75) 2400 — bayt imprimé (hémistiche + points de suite)
  F2 p76 (0.74-1.00) 1600 — شرح glosse غريب
  F3 p77 (0.00-0.22) 2400 — top mystère «2- أبين» + header + يشتمل
  F4 p77 (0.60-0.85) 1600 — hadith السفر (سُهَيْل ? + يمنع) + bracket
  F5 p77 (0.86-1.00) 2000 — quote Mālik «شر العلم الغريب»
  F6 p78 (0.58-0.78) 1600 — chaîne أم زرع + المحفوظ + أبو الفتح
  F7 p78 (0.78-1.00) 1600 — hadith زكاة الفطر + bracket + «من المسلمين»
  F8 p79 (0.00-0.16) 2400 — استخلاص header + 3 questions
  F9 p79 (0.16-0.52) 1600 — استثمار header + quote Ibn Raǧab + bracket
  F10 p79 (0.52-0.80) 2000 — أتأمل النص + 2 questions (q1 à trancher)
  F11 p79 (0.80-1.00) 2000 — إعداد قبلي header + 2 items
"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r592-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("F1-p76-bayt-2400", 76, 0.55, 0.75, 2400),
    ("F2-p76-charh-1600", 76, 0.74, 1.00, 1600),
    ("F3-p77-top-2400", 77, 0.00, 0.22, 2400),
    ("F4-p77-safar-1600", 77, 0.60, 0.85, 1600),
    ("F5-p77-malik-2000", 77, 0.86, 1.00, 2000),
    ("F6-p78-umzar-1600", 78, 0.58, 0.78, 1600),
    ("F7-p78-fitr-1600", 78, 0.78, 1.00, 1600),
    ("F8-p79-istikhlas-2400", 79, 0.00, 0.16, 2400),
    ("F9-p79-rajab-1600", 79, 0.16, 0.52, 1600),
    ("F10-p79-atamal-2000", 79, 0.52, 0.80, 2000),
    ("F11-p79-idad-2000", 79, 0.80, 1.00, 2000),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = {t.split("-")[0] for t in sys.argv[1:]} or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, f0, f1, dpi in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + f0 * r.height, r.x1, r.y0 + f1 * r.height)
        png = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=dpi, clip=clip).save(png)
        base = png[:-4]
        subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", "6"],
                       env=env, capture_output=True, text=True)
        ocr = open(base + ".txt", encoding="utf-8", errors="replace").read()
        print(f"===== {tag} ({os.path.getsize(png)//1024} Ko) =====")
        print(ocr.strip()[:1600])
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
