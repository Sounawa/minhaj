#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-h6-20 : rendus 600 dpi (gris) des pp.110-116 du tirage hadith-6ep
# + OCR tesseract (ara, tessdata_best) psm 4 et psm 6, page par page
# + couche de lecture _text pp.110-116.
# Bornage : L20 «العبادة وسيلة القرب والمحبة» (pdf-mut23h3b-700, cartouche ١٩ attendu
# par triangulation p90=15/p95=16/p100=17/p105=18) démarre p.110 (annoncé par
# l'إعداد قبلي de L19 : أحفظ حديث الدرس الموالي وأبين من هم أولياء الله تعالى
# وما مكانتهم عند الله — matn = hadith الولاية «من عادى لي ولياً...» Bukhārī 6502).
# L21 = pdf-mut23h3b-701 «دعم وتطبيق» (leçon d'activités NON numérotée) → chercher
# la frontière dans pp.113-116.
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
TXT = "/home/z/my-project/pdf-work/hadith-6-ibtidai_text.pdf"
OUT = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"

os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

# 1) rendus 600 dpi + OCR du tirage pp.110-116
for p in range(110, 117):
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

# 2) couche de lecture _text pp.110-116
for p in range(110, 117):
    txt = f"{OUT}/txt-{p}.txt"
    if not os.path.exists(txt):
        with open(txt, "w") as fh:
            subprocess.run(["pdftotext", "-f", str(p), "-l", str(p),
                            "-layout", TXT, "-"], stdout=fh,
                           stderr=subprocess.DEVNULL)
    print(f"_text p.{p} : {os.path.getsize(txt)} o")
print("OK prep-h6-20")
