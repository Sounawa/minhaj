# -*- coding: utf-8 -*-
# R619 — extraction leçon 6 ulum-hadith-tanawi-2 (pdf-mut23h2u-260, p.35-40)
# Bornes tranchées par DOUBLE sondage (jamais devinées) :
#   p.35 = bannière leçon 6 « الحديث الصحيح ومراتبه » + objectifs + tamhīd (couche incorporée)
#   p.40 = taqyīm + istiṯmār de la leçon 6 (fin) ; p.41 = objectifs leçon 7 « الحسن » (non touchée)
# Trois couches par page (méthode R613-R618) :
#   pNNN-embed.txt = couche texte incorporée (pdftotext)
#   pNNN-pymu.txt  = couche logique PyMuPDF
#   pNNN-300.txt   = OCR tesseract ara 300 dpi (tessdata du dépôt)
import os, subprocess, glob

BOOK = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r619"
PAGES = list(range(35, 42))  # 35..41 (41 = sondage borne sup, non touchée)
os.makedirs(OUT, exist_ok=True)

# 1) couches incorporée + PyMuPDF
subprocess.run(["pdftotext", "-f", "35", "-l", "41", BOOK, f"{OUT}/p035-041-embed.txt"], check=True)
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
