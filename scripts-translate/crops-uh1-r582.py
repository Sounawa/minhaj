#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R582 — adjudications crops 600 dpi leçon 5 ulum-hadith-tanawi-1 (p.33-37).
Chaîne R578→R581 : jamais deviné — bannière/vers/quotes tranchés par image.
Zones :
  A p33 bannière stricte (0.00-0.15)   — الدرس 5 + titre (ornée)
  B p33 vers+gloses (0.50-0.95)        — بيت الناظم + الشرح
  C p34 haut (0.00-0.16)               — question(s) « ماذا يطلق... »
  D p34 exemples (0.40-0.90)           — القولي/الفعلي/التقريري/الوصفي
  E p35 haut (0.00-0.30)               — fin الوصفي + المرفوع يصدق + الخطيب
  F p35 milieu (0.30-0.62)             — ابن الصلاح + أنواع صريح/حكما
  G p35 bas (0.72-1.00)                — vers « وما للتابعي هو المقطوع » + def
  H p36 haut (0.05-0.45)               — التابعي + الحسن البصري + مسروق
  I p36 milieu (0.42-0.70)             — المنقطع vs المقطوع (ابن الصلاح…)
  J p36-37 استثمار (p36 0.68-1.00)     — نصوص المسيّب/مسلم
  K p37 استثمار fin + إعداد (0.00-0.95) — مالك + questions ×2 + إعداد
Sortie : tr-tmp/r582-uh1/crops/*.png + OCR psm 6.
Usage : python3 scripts-translate/crops-uh1-r582.py
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r582-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("A-p33-banniere", 33, 0.00, 0.15),
    ("B-p33-vers-gloses", 33, 0.50, 0.95),
    ("C-p34-haut", 34, 0.00, 0.16),
    ("D-p34-exemples", 34, 0.40, 0.90),
    ("E-p35-haut", 35, 0.00, 0.30),
    ("F-p35-milieu", 35, 0.30, 0.62),
    ("G-p35-vers-maqtu", 35, 0.72, 1.00),
    ("H-p36-haut", 36, 0.05, 0.45),
    ("I-p36-milieu", 36, 0.42, 0.70),
    ("J-p36-istithmar", 36, 0.68, 1.00),
    ("K-p37-istithmar-i3dadi", 37, 0.00, 0.95),
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
