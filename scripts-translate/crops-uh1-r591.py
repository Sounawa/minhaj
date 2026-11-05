#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R591 — crops 1200 dpi p.72-75 de ulum-hadith-1-thanawi.pdf + OCR local psm 6.
Leçon 14 ulum-hadith-tanawi-1 (pdf-mut23h2q-125, الحديث المرسل, p.72-75).
Zones sensibles (OCR 300 dpi dégradé) :
  Z1  p72 (0.00-0.16) — bannière/أهداف header
  Z2  p72 (0.48-0.78) — bayt du nāẓim
  Z3  p73 (0.04-0.34) — استخلاص + أولا تعريف + citation
  Z4  p74 (0.72-1.00) — bas de page : 2 questions + en-tête
  Z5  p75 (0.00-0.28) — haut : bandeau + texte Mālik
  Z6  p75 (0.48-1.00) — activité + إعداد قبلي
Recréé après le recyclage bac à sable n°5 (passe R591) — contenu identique.
"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r591-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("Z1-p72-top-banniere", 72, 0.00, 0.16),
    ("Z2-p72-bayt-nazim", 72, 0.48, 0.78),
    ("Z3-p73-citation-maryam", 73, 0.04, 0.34),
    ("Z4-p74-bottom-questions", 74, 0.72, 1.00),
    ("Z5-p75-top-entete-malik", 75, 0.00, 0.28),
    ("Z6-p75-activite-idad", 75, 0.48, 1.00),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = {t.split("-")[0] for t in sys.argv[1:]} or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, f0, f1 in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + f0 * r.height, r.x1, r.y0 + f1 * r.height)
        png = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=1200, clip=clip).save(png)
        base = png[:-4]
        subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", "6"],
                       env=env, capture_output=True, text=True)
        ocr = open(base + ".txt", encoding="utf-8", errors="replace").read()
        print(f"===== {tag} ({os.path.getsize(png)//1024} Ko) =====")
        print(ocr.strip()[:900])
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
