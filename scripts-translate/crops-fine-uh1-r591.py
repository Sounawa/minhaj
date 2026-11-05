#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R591 — crops fins 1600-2400 dpi p.72-75 (zones resserrées, passe 2).
Zones :
  F1 p72 (0.00-0.09) 2400 — bannière الدرس 14 ?
  F2 p72 (0.55-0.75) 2400 — bayt du nāẓim
  F3 p73 (0.30-0.52) 2400 — citation «...» [مريم: ?] + وكأن المرسل
  F4 p74 (0.56-0.82) 2400 — en-tête de boîte au-dessus des 2 questions
  F5 p75 (0.00-0.08) 2400 — bandeau d'en-tête de p.75
  F6 p75 (0.58-0.88) 1600 — boîte إعداد قبلي
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
    ("F1-p72-banniere-2400", 72, 0.00, 0.09, 2400),
    ("F2-p72-bayt-2400", 72, 0.55, 0.75, 2400),
    ("F3-p73-citation-2400", 73, 0.30, 0.52, 2400),
    ("F4-p74-boite-2400", 74, 0.56, 0.82, 2400),
    ("F5-p75-bandeau-2400", 75, 0.00, 0.08, 2400),
    ("F6-p75-idad-1600", 75, 0.58, 0.88, 1600),
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
        print(ocr.strip()[:700])
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
