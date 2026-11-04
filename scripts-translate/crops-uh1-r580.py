#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R580 — adjudications crops 600 dpi leçon 3 ulum-hadith-tanawi-1 (p.23-27).
Chaîne R578/R579 : jamais deviné — tout chiffre/terme incertain tranché par image.
Zones :
  A p23 bannière (0.72-1.00)          — vers Bayqūnī imprimé
  B p25 refs (0.00-0.14 + 0.14-0.30)  — [شرح العلل الصغير: …] [الموضوعات: …]
  C p26 haut (0.00-0.40)              — suite الزرقاني + commentaire الترمذي
  D p27 استثمار (0.24-0.66)           — نص ابن الصلاح + [مقدمة ابن الصلاح: …]
Sortie : tr-tmp/r580-uh1/crops/*.png + OCR psm 6 (tessdata dépôt).
Usage : python3 scripts-translate/crops-uh1-r580.py
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r580-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("A-p23-banniere", 23, 0.72, 1.00),
    ("B1-p25-ref-alaq", 25, 0.00, 0.14),
    ("B2-p25-ref-mawduat", 25, 0.14, 0.30),
    ("C-p26-haut", 26, 0.00, 0.40),
    ("D-p27-istithmar", 27, 0.24, 0.66),
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
            r = subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", psm],
                               env=env, capture_output=True, text=True)
            if os.path.exists(base + ".txt"):
                os.replace(base + ".txt", out)
        print(f"===== {tag} =====")
        for psm in ("6", "4"):
            fp = f"{base}-psm{psm}.txt"
            print(f"-- psm{psm} --")
            print(open(fp, encoding="utf-8").read().strip() if os.path.exists(fp) else "(vide)")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
