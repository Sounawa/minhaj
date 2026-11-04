#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R580 — crop ultime : nom du 8e compagnon dans la liste الترمذي (p.26).
Ligne « وعائشة؛ وجابر؛ وأبي ... الأسلمي » — zone droite (RTL), y 0.408-0.458.
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r580-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("W-p26-nom-droite", 26, 0.408, 0.458, 0.45, 1.00),
    ("W-p26-nom-ligne", 26, 0.408, 0.458, 0.00, 1.00),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, y0, y1, x0, x1 in ZONES:
        pg = doc[page - 1]
        rect = pg.rect
        clip = fitz.Rect(rect.x0 + rect.width * x0, rect.y0 + rect.height * y0,
                         rect.x0 + rect.width * x1, rect.y0 + rect.height * y1)
        png = f"{WORK}/{tag}.png"
        pg.get_pixmap(dpi=900, clip=clip).save(png)
        base = png[:-4]
        for psm in ("7", "6"):
            out = f"{base}-psm{psm}.txt"
            subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", psm],
                           env=env, capture_output=True, text=True)
            if os.path.exists(base + ".txt"):
                os.replace(base + ".txt", out)
        print(f"===== {tag} =====")
        for psm in ("7", "6"):
            fp = f"{base}-psm{psm}.txt"
            print(f"-- psm{psm} --")
            print(open(fp, encoding="utf-8").read().strip() if os.path.exists(fp) else "(vide)")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
