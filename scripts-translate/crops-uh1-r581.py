#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R581 — adjudications crops 600 dpi leçon 4 ulum-hadith-tanawi-1 (p.28-32).
Chaîne R578/R579/R580 : jamais deviné — tout chiffre/terme/bannière tranché par image.
Zones :
  A p28 top (0.00-0.28)          — bannière « الدرس 4 » titre + numéro (ornée)
  B p28 bas (0.28-0.85)          — vers du nāẓim « وكل ما عن رتبة الحسن قصر... » + gloses
  C p29 (0.30-0.62)              — vers repris en « أولا : تعريف » + définition
  D p30 (0.08-0.34)              — أقسام : chiffres ابن حبان (خمسين / مائة وستة وعشرين)
  E p30 bas (0.80-1.00)          — ابن حجر « قليل الفائدة » + transition
  F p31 haut (0.00-0.30)         — citation العراقي [شرح التبصرة والتذكرة: 105/1]
  G p31 bas (0.55-1.00)          — استثمار : ألفية العراقي (poème جبر) + question
  H p32 (0.00-0.60)              — الإعداد القبلي (items L116)
Sortie : tr-tmp/r581-uh1/crops/*.png + OCR psm 6 (tessdata dépôt).
Usage : python3 scripts-translate/crops-uh1-r581.py
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r581-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("A-p28-banniere", 28, 0.00, 0.28),
    ("B-p28-vers-gloses", 28, 0.28, 0.85),
    ("C-p29-vers-def", 29, 0.30, 0.62),
    ("D-p30-ibnhibban", 30, 0.08, 0.34),
    ("E-p30-ibnhajar", 30, 0.80, 1.00),
    ("F-p31-iraqi", 31, 0.00, 0.30),
    ("G-p31-istithmar", 31, 0.55, 1.00),
    ("H-p32-i3dadi", 32, 0.00, 0.60),
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
