#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-h6-16 : rendus 600 dpi (gris) des pp.90-96 du tirage hadith-6ep
# + OCR tesseract (ara, tessdata_best) psm 4 et psm 6, page par page.
# Bornage : L16 «الأخوة الإسلامية» (partie 1) démarre p.90 (أهداف en tête,
# t90.png déjà rendu en Z2-51 sans OCR complet) ; L17 = partie 2 → chercher
# la frontière dans pp.91-96 (cartouche bleu du medaillon leçon).
# PDF source = content/textbooks-src/hadith-6ep.pdf (dépôt, SANS couche texte).
# Couche de lecture : content/textbooks-src/hadith-6-ibtidai_text.pdf (miroir
# archive.org, alignement prouvé pp.76-80 et re-vérifié pp.89-90 ce tour :
# même contenu en tête/fin de page).
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
TXT = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6-ibtidai_text.pdf"
OUT = "/home/z/my-project/pdf-work/h6-15"   # même atelier, suite de la série h6
TESSDATA = "/home/z/my-project/pdf-work/tessdata"

os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

# 1) rendus 600 dpi + OCR du tirage (p.90 déjà rendue en t90.png → OCR seulement)
for p in range(90, 97):
    png = f"{OUT}/t{p:03d}" if p >= 91 else f"{OUT}/t90"
    if not os.path.exists(png + ".png"):
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "600",
                        "-gray", "-png", "-singlefile", PDF, png], check=True)
    for psm in (4, 6):
        txt = f"{png}-psm{psm}.txt"
        if not os.path.exists(txt):
            with open(txt, "w") as fh:
                subprocess.run(["tesseract", png + ".png", "stdout",
                                "-l", "ara", "--psm", str(psm)],
                               env=env, stdout=fh, stderr=subprocess.DEVNULL)
    print(f"p.{p} : {os.path.getsize(png + '.png') // 1024} Ko PNG, "
          f"psm4={os.path.getsize(png + '-psm4.txt')} o, psm6={os.path.getsize(png + '-psm6.txt')} o")

# 2) couche de lecture _text pp.93-96 (90-92 déjà extraites)
for p in range(93, 97):
    txt = f"{OUT}/txt-{p}.txt"
    if not os.path.exists(txt):
        with open(txt, "w") as fh:
            subprocess.run(["pdftotext", "-f", str(p), "-l", str(p),
                            "-layout", TXT, "-"], stdout=fh,
                           stderr=subprocess.DEVNULL)
    print(f"_text p.{p} : {os.path.getsize(txt)} o")
print("OK prep-h6-16")
