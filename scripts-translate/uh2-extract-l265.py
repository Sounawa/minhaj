# -*- coding: utf-8 -*-
# R627 — extraction leçon 11 ulum-hadith-tanawi-2 (pdf-mut23h2u-265, p.63-67)
# Bornes tranchées par DOUBLE sondage (jamais devinées) :
#   p.62 = fin leçon 10 (istithmar + i3dad-qibli, r623-crops ADJ15/ADJ16) — non touchée
#   p.63 = bannière leçon 11 « الحديث المحكم والمختلف » + objectifs + tamhīd
#   p.66 = taqwīm leçon 11 (3 items) ; p.67 = istiṯmār + أتأمل + iʿdād leçon 12
#   p.68 = contenu leçon 12 (nāsiḫ/mansūḫ : ترجيح/توقف) — non touchée
# Trois couches par page (méthode R613-R622) :
#   pNNN-embed.txt = couche texte incorporée (pdftotext)
#   pNNN-pymu.txt  = couche logique PyMuPDF
#   pNNN-300.txt   = OCR tesseract ara 300 dpi (tessdata du dépôt)
import os, subprocess, glob

BOOK = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r627"
PAGES = list(range(62, 69))  # 62..68 (62 et 68 = sondage bornes, non touchées)
os.makedirs(OUT, exist_ok=True)

# 1) couches incorporée + PyMuPDF
subprocess.run(["pdftotext", "-f", "62", "-l", "68", BOOK, f"{OUT}/p062-068-embed.txt"], check=True)
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
