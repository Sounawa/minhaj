#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-h6-15 : rendus 600 dpi (gris) des pp.80-86 du tirage hadith-6ep
# + OCR tesseract (ara, tessdata_best) psm 4 et psm 6, page par page.
# Bornage : L14 «دعم وتطبيق» = pp.81-84 attendu (80 = fin L13, 85-86 = début L15).
# PDF source = content/textbooks-src/hadith-6ep.pdf (dépôt, SANS couche texte).
# Couche de lecture complémentaire : content/textbooks-src/hadith-6-ibtidai_text.pdf
# (miroir archive.org, même édition — alignement vérifié p.76-80 contre Z2-49).
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
PAGES = range(80, 87)  # 80-86 : marge de bornage autour de L14 (81-84 attendu)

os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

for p in PAGES:
    png = f"{OUT}/t{p:03d}"
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
print("OK prep-h6-15")
