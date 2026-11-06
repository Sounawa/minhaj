#!/usr/bin/env python3
"""R636 — extraction multicouche hadith-3es leçon 5 pdf-mut23h2x-394 (pages 39-46), méthode r634."""
import os, subprocess

PDF = "content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "tr-tmp/r636"
PAGES = range(39, 47)  # 39..46 inclus
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX="scripts-translate/tessdata")

for p in PAGES:
    subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF,
                    f"{OUT}/p{p:03d}-embed.txt"], check=False)

import fitz
doc = fitz.open(PDF)
for p in PAGES:
    pg = doc[p - 1]
    with open(f"{OUT}/p{p:03d}-pymu.txt", "w", encoding="utf-8") as fh:
        fh.write(pg.get_text("text"))

for p in PAGES:
    png = f"{OUT}/p{p:03d}-300"
    if not os.path.exists(png + ".png"):
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "300",
                        "-png", "-singlefile", PDF, png], check=False)
    subprocess.run(["tesseract", png + ".png", f"{OUT}/p{p:03d}-300", "-l", "ara",
                    "--tessdata-dir", "scripts-translate/tessdata"], check=False,
                   env=env, capture_output=True)

# sondage borne sup : bandeau bannière des pages 44-47
def band(pno, y0, y1, name, zoom=6):
    pg = doc[pno - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * 0.04, r.height * y0, r.width * 0.97, r.height * y1)
    pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip).save(f"{OUT}/{name}.png")

for pno in (44, 45, 46, 47):
    band(pno, 0.04, 0.30, f"s-p{pno:03d}-haut")

print("extraction r636 terminée:", len(os.listdir(OUT)), "fichiers")
