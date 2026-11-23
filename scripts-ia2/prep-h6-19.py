#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-h6-19 : rendus 600 dpi (gris) des pp.106-109 du tirage hadith-6ep
# + OCR tesseract (ara, tessdata_best) psm 4 et psm 6, page par page
# + couche de lecture _text pp.106-109 (txt-105 déjà là).
# Bornage : L19 «فضل الله في الجزاء عن الأعمال» (pdf-mut23h3b-699, cartouche ١٨)
# démarre p.105 (t105 rendu en Z2-54 : أهداف ×3 + تمهيد + matn Ibn Abbās
# «فمن همّ بحسنة فلم يعملها كتبها الله عنده حسنة كاملة...» [رواه البخاري ومسلم
# في صحيحيهما بهذه الحروف]). L20 «العبادة وسيلة القرب والمحبة» (pdf-mut23h3b-700)
# → frontière cherchée dans pp.107-110 : p.109 = تقويم + استثمار أبو كبشة + إعداد
# قبلي (ولاية الله) → L19 = pp.105-109.
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
TXT = "/home/z/my-project/pdf-work/hadith-6-ibtidai_text.pdf"
OUT = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"

os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

# 1) rendus 600 dpi + OCR du tirage pp.106-109
for p in range(106, 110):
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

# 2) couche de lecture _text pp.106-109 (≤105 déjà extraites)
for p in range(106, 110):
    txt = f"{OUT}/txt-{p}.txt"
    if not os.path.exists(txt):
        with open(txt, "w") as fh:
            subprocess.run(["pdftotext", "-f", str(p), "-l", str(p),
                            "-layout", TXT, "-"], stdout=fh,
                           stderr=subprocess.DEVNULL)
    print(f"_text p.{p} : {os.path.getsize(txt)} o")
print("OK prep-h6-19")
