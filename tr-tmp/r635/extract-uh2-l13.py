#!/usr/bin/env python3
"""R635 — extraction multicouche uh2 leçon 13 (pages 72-74), modèle r632."""
import os, subprocess

PDF = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r635"
PAGES = range(72, 75)  # 72..74 inclus (p.74 = sondage borne sup)
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX="scripts-translate/tessdata")

for p in PAGES:
    subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF,
                    f"{OUT}/p{p:03d}-embed.txt"], check=False)

import fitz
doc = fitz.open(PDF)
for p in PAGES:
    txt = doc[p - 1].get_text("text")
    with open(f"{OUT}/p{p:03d}-pymu.txt", "w", encoding="utf-8") as fh:
        fh.write(txt)

for p in PAGES:
    png = f"{OUT}/p{p:03d}-300"
    if not os.path.exists(png + ".png"):
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "300",
                        "-png", "-singlefile", PDF, png], check=False)
    subprocess.run(["tesseract", png + ".png", f"{OUT}/p{p:03d}-300",
                    "-l", "ara", "--psm", "6"], env=env, check=False,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("couches écrites pour pages", list(PAGES))
