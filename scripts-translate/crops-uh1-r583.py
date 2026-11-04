#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R583 — adjudications crops 600 dpi leçon 6 ulum-hadith-tanawi-1 (p.38-42).
Chaîne R578→R582 : jamais deviné — bannière/vers/quotes tranchés par image.
Zones :
  A p38 bannière stricte (0.00-0.16)   — الدرس 6 + titre (ornée)
  B p38 vers المتن (0.55-1.00)         — bayt nāẓim المسند + المتصل
  C p39 haut (0.00-0.30)               — définitions + استخلاص المضامين
  D p39 def-verse (0.28-0.68)          — أولا المسند + verse quote + 3 usages
  E p40 haut (0.00-0.42)               — ثانيها/ثالثها + ابن الصلاح [42]
  F p40 exemple (0.40-0.72)            — البخاري « لا يصلي أحدكم... »
  G p40 متصل (0.72-1.00)               — ثانيا المتصل + verse + def + مثال
  H p41 exemple-2 (0.00-0.42)          — عمر طلاق + التابعين + العراقي
  I p41 استثمار (0.42-0.97)            — التقييم + ابن حجر « النكت 1/506 »
  J p42 إعداد قبلي (0.00-0.60)         — 2 questions المسلسل (borne sup)
Sortie : tr-tmp/r583-uh1/crops/*.png + OCR psm 6.
Usage : python3 scripts-translate/crops-uh1-r583.py
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r583-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("A-p38-banniere", 38, 0.00, 0.16),
    ("B-p38-vers", 38, 0.55, 1.00),
    ("C-p39-haut", 39, 0.00, 0.30),
    ("D-p39-def-verse", 39, 0.28, 0.68),
    ("E-p40-haut", 40, 0.00, 0.42),
    ("F-p40-exemple", 40, 0.40, 0.72),
    ("G-p40-mutasil", 40, 0.72, 1.00),
    ("H-p41-exemple2", 41, 0.00, 0.42),
    ("I-p41-istithmar", 41, 0.42, 0.97),
    ("J-p42-i3dadi", 42, 0.00, 0.60),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, y0, y1 in ZONES:
        pg = doc[page - 1]
        rect = pg.rect
        clip = fitz.Rect(rect.x0, rect.y0 + rect.height * y0,
                         rect.x1, rect.y0 + rect.height * y1)
        png = f"{WORK}/{tag}.png"
        pg.get_pixmap(dpi=600, clip=clip).save(png)
        base = png[:-4]
        for psm in ("6", "4"):
            out = f"{base}-psm{psm}.txt"
            subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", psm],
                           env=env, capture_output=True, text=True)
            if os.path.exists(base + ".txt"):
                os.replace(base + ".txt", out)
        print(f"===== {tag} =====")
        fp = f"{base}-psm6.txt"
        print(open(fp, encoding="utf-8").read().strip() if os.path.exists(fp) else "(vide)")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
