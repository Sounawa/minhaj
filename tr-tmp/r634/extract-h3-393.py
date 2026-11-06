#!/usr/bin/env python3
"""R634 — extraction multicouche hadith-3es leçon 4 pdf-mut23h2x-393 (pages 31-38), méthode r632."""
import os, subprocess

PDF = "content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "tr-tmp/r634"
PAGES = range(31, 39)  # 31..38 inclus
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX="scripts-translate/tessdata")

# 1) couche embed pdftotext
for p in PAGES:
    subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF,
                    f"{OUT}/p{p:03d}-embed.txt"], check=False)

# 2) couche logique PyMuPDF
import fitz
doc = fitz.open(PDF)
for p in PAGES:
    pg = doc[p - 1]
    txt = pg.get_text("text")
    with open(f"{OUT}/p{p:03d}-pymu.txt", "w", encoding="utf-8") as fh:
        fh.write(txt)

# 3) couche tesseract ara 300 dpi (tessdata du dépôt)
for p in PAGES:
    png = f"{OUT}/p{p:03d}-300"
    if not os.path.exists(png + ".png"):
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "300",
                        "-png", "-singlefile", PDF, png], check=False)
    subprocess.run(["tesseract", png + ".png", f"{OUT}/p{p:03d}-300", "-l", "ara",
                    "--tessdata-dir", "scripts-translate/tessdata"], check=False,
                   env=env, capture_output=True)

print("extraction r634 terminée:", len(os.listdir(OUT)), "fichiers")
