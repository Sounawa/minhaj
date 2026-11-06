#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R621 — leçon 8 ulum-hadith-tanawi-2 (pdf-mut23h2u-262, الدرس 8 : زيادة الثقة
والمحفوظ والشاذ = L'ajout du transmetteur fiable, le retenu (maḥfūẓ) et l'anomal
(šāḏḏ)). Borne basse : p.47 (bannière leçon 8 + objectifs, sondée R619) ; borne
haute : bannière calligraphique leçon 9 الحديث المعروف والمنكر (à sonder p.48-p.58).
Extraction TRIPLE (méthode R613-R620) : couche incorporée pdftotext (pNNN-embed.txt)
+ OCR tesseract ara 300 dpi psm 4 avec TESSDATA_PREFIX du dépôt (pNNN-300.txt)
+ couche logique FIDÈLE PyMuPDF (pNNN-pymu.txt) = arbitre.
NOMBRES DE LA COUCHE pdftotext INVERSÉS EN MIROIR PAR PAIRES (« 94-25 » = 49-52) :
tout chiffre ambigu → recadrage 600 dpi + lecture image, jamais deviné.
Usage : python3 scripts-translate/r621-extract.py [first last]"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
WORK = f"{HOME}/tr-tmp/r621"
TESSDATA = f"{HOME}/scripts-translate/tessdata"


def layer(p: int) -> str:
    out = f"{WORK}/p{p:03d}-embed.txt"
    if not (os.path.exists(out) and os.path.getsize(out) > 0):
        subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF, out], check=True)
    return open(out, encoding="utf-8").read()


def ocr_page(doc, n: int, dpi: int = 300) -> str:
    tp = f"{WORK}/p{n:03d}-300.txt"
    if not (os.path.exists(tp) and os.path.getsize(tp) > 0):
        png = f"{WORK}/p{n:03d}-300.png"
        if not os.path.exists(png):
            doc[n - 1].get_pixmap(dpi=dpi).save(png)
        env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
        r = subprocess.run(["tesseract", png, tp[:-4], "-l", "ara", "--psm", "4"],
                           env=env, capture_output=True, text=True)
        if os.path.exists(png):
            os.remove(png)
        if r.returncode != 0:
            return ""
    return open(tp, encoding="utf-8").read()


def pymu(doc, p: int) -> str:
    out = f"{WORK}/p{p:03d}-pymu.txt"
    if not (os.path.exists(out) and os.path.getsize(out) > 0):
        txt = doc[p - 1].get_text()
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(txt)
    return open(out, encoding="utf-8").read()


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 47
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 58
    doc = fitz.open(PDF)
    for p in range(first, last + 1):
        lay = layer(p)
        ocr = ocr_page(doc, p)
        pm = pymu(doc, p)
        with open(f"{WORK}/p{p:03d}-dual.txt", "w", encoding="utf-8") as fh:
            fh.write(f"===== p{p} COUCHE pdftotext =====\n{lay}")
            fh.write(f"\n===== p{p} OCR 300 dpi =====\n{ocr}\n")
        print(f"p{p}: embed {len(lay)} car, OCR {len(ocr)} car, pymu {len(pm)} car")
    doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
