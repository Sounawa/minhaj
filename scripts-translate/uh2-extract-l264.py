# -*- coding: utf-8 -*-
# R630 — extraction leçon 10 ulum-hadith-tanawi-2 (pdf-mut23h2u-264, p.57-62)
# Bornes tranchées (jamais devinées) :
#   p.57 = bannière « الدرس 10 » + objectifs (vlm-ADJ1/1b/1c, r623-crops)
#   p.62 = istiṯmār + iʿdād qiblī (fin de leçon 10)
#   p.63 = bannière leçon 11 « محكم الحديث ومختلف » (vlm-p63-header, sondage borne sup, non touchée)
# Trois couches par page (méthode R613-R619) :
#   pNNN-embed.txt = couche texte incorporée (pdftotext)
#   pNNN-pymu.txt  = couche logique PyMuPDF
#   pNNN-300.txt   = OCR tesseract ara 300 dpi (tessdata du dépôt)
import os, subprocess, glob

BOOK = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r630"
PAGES = list(range(57, 64))  # 57..63 (63 = sondage borne sup, non touchée)
os.makedirs(OUT, exist_ok=True)

# 1) couches incorporée + PyMuPDF
subprocess.run(["pdftotext", "-f", "57", "-l", "63", BOOK, f"{OUT}/p057-063-embed.txt"], check=True)
import fitz
doc = fitz.open(BOOK)
for p in PAGES:
    txt = doc[p - 1].get_text()
    open(f"{OUT}/p%03d-pymu.txt" % p, "w", encoding="utf-8").write(txt)

# 2) OCR tesseract 300 dpi
env = dict(os.environ, TESSDATA_PREFIX="scripts-translate/tessdata")
for p in PAGES:
    png = f"{OUT}/p%03d" % p
    subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "300",
                    "-singlefile", "-png", BOOK, png], check=True)
    subprocess.run(["tesseract", png + ".png", png + "-300", "-l", "ara", "--psm", "6"],
                   check=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(png + ".png")

files = sorted(glob.glob(OUT + "/*"))
print("OK — %d fichiers couches :" % len(files))
for f in files:
    print("  ", f, os.path.getsize(f), "octets")
