# -*- coding: utf-8 -*-
# R639 — extraction leçon 14 ulum-hadith-tanawi-2 (pdf-mut23h2u-268, p.74-77)
# Bornes par DOUBLE sondage (jamais devinées) :
#   p.73 = fin leçon 13 (anšaṭa taṭbīqiyya, R635) — non touchée
#   p.74 = bannière leçon 14 « المردود » (mardūd) + objectifs + tamhīd + matn
#   p.75 = taḥlīl (أسباب رد الحديث) + الحديث المعلق (تعريفه، الفرق مع المعضل)
#   p.76-77 = suite leçon 14 (أمثلته؟ taqwīm, istiṯmār, iʿdād) — à confirmer
#   borne sup = page de la bannière leçon 15 « الحديث المرسل » (sondage p.76-79)
# Trois couches par page (méthode R613-R635) :
#   pNNN-embed.txt = couche texte incorporée (pdftotext)
#   pNNN-pymu.txt  = couche logique PyMuPDF
#   pNNN-300.txt   = OCR tesseract ara 300 dpi (tessdata du dépôt)
import os, subprocess, glob

BOOK = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r639"
PAGES = list(range(74, 80))  # 74..79 (78-79 = sondage bornes, non touchées)
os.makedirs(OUT, exist_ok=True)

# 1) couches incorporée + PyMuPDF
subprocess.run(["pdftotext", "-f", "74", "-l", "79", BOOK, f"{OUT}/p074-079-embed.txt"], check=True)
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
