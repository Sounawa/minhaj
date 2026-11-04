#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R580 — passe 2 de crops 600 dpi (zones fines restantes).
E p25 0.28-0.46  : ابن الجوزي + [الموضوعات: …] + اعتراض ابن دقيق العيد
F p26 0.10-0.24  : phrase الزرقاني serrée (mot entre عدل/خف ?)
G p26 0.38-0.64  : commentaire الترمذي + [سنن الترمذي…]
H p27 0.58-0.92  : الإعداد القبلي items
I p24 0.50-0.84  : [معالم السنن: …] + اعتراض/جواب
"""
import os
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r580-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("E-p25-ibnjawzi", 25, 0.28, 0.46),
    ("F-p26-zaraqani", 26, 0.10, 0.24),
    ("G-p26-tirmidhi", 26, 0.38, 0.64),
    ("H-p27-idad", 27, 0.58, 0.92),
    ("I-p24-maalim", 24, 0.50, 0.84),
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
        for psm in ("6", "4"):
            fp = f"{base}-psm{psm}.txt"
            print(f"-- psm{psm} --")
            print(open(fp, encoding="utf-8").read().strip() if os.path.exists(fp) else "(vide)")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
