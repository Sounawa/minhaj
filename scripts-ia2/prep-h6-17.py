#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-h6-17 : rendus 600 dpi (gris) des pp.97-100 du tirage hadith-6ep
# + OCR tesseract (ara, tessdata_best) psm 4 et psm 6, page par page.
# Bornage : L17 «الأخوة الإسلامية» (تتمة, partie 2) démarre p.95 (أهداف ×3 déjà
# repérés sur t095 Z2-52 : أن أتعرف أنواعا أخرى من حقوق الأخوة / أن أميز معاني
# هذه الحقوق وأدرك أهميتها / أن أحرص على الالتزام بقيم الأخوة في سلوكي).
# L18 = «من الأعمال الفاضلة وثوابها» (pdf-mut23h3b-698) → chercher la frontière
# dans pp.98-100 (cartouche bleu du médaillon leçon).
# PDF source = content/textbooks-src/hadith-6ep.pdf (dépôt, SANS couche texte).
# Couche de lecture : content/textbooks-src/hadith-6-ibtidai_text.pdf (miroir
# archive.org, alignement prouvé pp.76-80, re-vérifié pp.89-90 et 95-96).
# pp.95-96 déjà rendues (t095/t096) et OCR-ées en Z2-52 — pas de reprise.
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
TXT = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6-ibtidai_text.pdf"
OUT = "/home/z/my-project/pdf-work/h6-15"   # même atelier, suite de la série h6
TESSDATA = "/home/z/my-project/pdf-work/tessdata"

os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

# 1) rendus 600 dpi + OCR du tirage pp.97-100 (95-96 déjà faites)
for p in range(97, 101):
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

# 2) couche de lecture _text pp.97-100 (95-96 déjà extraites)
for p in range(97, 101):
    txt = f"{OUT}/txt-{p}.txt"
    if not os.path.exists(txt):
        with open(txt, "w") as fh:
            subprocess.run(["pdftotext", "-f", str(p), "-l", str(p),
                            "-layout", TXT, "-"], stdout=fh,
                           stderr=subprocess.DEVNULL)
    print(f"_text p.{p} : {os.path.getsize(txt)} o")
print("OK prep-h6-17")
