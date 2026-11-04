#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R580 — passe 3 : micro-zones 900 dpi + mesure non-blanc p.23-27.
Z1 p26 0.105-0.180 : phrase الزرقاني (mot de jonction entre عدل / خف)
Z2 p26 0.395-0.480 : liste companions الترمذي « وفي الباب عن … »
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r580-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("Z1-p26-zaraqani-tight", 26, 0.105, 0.180),
    ("Z2-p26-asami-tight", 26, 0.395, 0.480),
]


def nonwhite(page: int) -> float:
    """Ratio pixels non-blancs de la page à 150 dpi (mesure d'activité)."""
    pm = doc[page - 1].get_pixmap(dpi=150)
    n = pm.width * pm.height
    samples = pm.samples
    cnt = 0
    for i in range(0, len(samples), 3):
        r, g, b = samples[i], samples[i + 1], samples[i + 2]
        if not (r > 235 and g > 235 and b > 235):
            cnt += 1
    return cnt / n * 100.0


def main() -> int:
    global doc
    os.makedirs(WORK, exist_ok=True)
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, y0, y1 in ZONES:
        pg = doc[page - 1]
        rect = pg.rect
        clip = fitz.Rect(rect.x0, rect.y0 + rect.height * y0,
                         rect.x1, rect.y0 + rect.height * y1)
        png = f"{WORK}/{tag}.png"
        pg.get_pixmap(dpi=900, clip=clip).save(png)
        base = png[:-4]
        for psm in ("6", "7", "4"):
            out = f"{base}-psm{psm}.txt"
            subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", psm],
                           env=env, capture_output=True, text=True)
            if os.path.exists(base + ".txt"):
                os.replace(base + ".txt", out)
        print(f"===== {tag} =====")
        for psm in ("6", "7", "4"):
            fp = f"{base}-psm{psm}.txt"
            print(f"-- psm{psm} --")
            print(open(fp, encoding="utf-8").read().strip() if os.path.exists(fp) else "(vide)")
        print()
    for p in range(23, 28):
        print(f"p{p} non-blanc = {nonwhite(p):.1f} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
