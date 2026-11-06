#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R619 — leçon 6 ulum-hadith-tanawi-2 (pdf-mut23h2u-260, الدرس 6 : الحديث الصحيح ومراتبه).
Bornes : p.35 = bannière leçon 6 + objectifs + tamhīd (sondée R617, couches r617) ;
borne supérieure = bannière calligraphique leçon 7 الحسن (à sonder p.36-p.48 par
image). Extraction DOUBLE : couche incorporée (pdftotext) + OCR tesseract ara
300 dpi psm 4 (méthode R613-R617) + couche logique FIDÈLE PyMuPDF (pNNN-pymu.txt).
NOMBRES DE LA COUCHE pdftotext INVERSÉS EN MIROIR (piège R613-R617) : chaque
nombre équivoque tranché par recadrage 600-1800 dpi + lecture image ; couche
PyMuPDF fidèle = arbitre.
Usage : python3 scripts-translate/r619-extract.py [first last]"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
WORK = f"{HOME}/tr-tmp/r619"
LEGACY = f"{HOME}/tr-tmp/r617"
TESSDATA = f"{HOME}/scripts-translate/tessdata"


def layer(p: int) -> str:
    out = f"{WORK}/p{p:03d}-layer.txt"
    if not (os.path.exists(out) and os.path.getsize(out) > 0):
        subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF, out], check=True)
    return open(out, encoding="utf-8").read()


def ocr_page(doc, n: int, dpi: int = 300) -> str:
    tp = f"{WORK}/p{n:03d}-300.txt"
    if not (os.path.exists(tp) and os.path.getsize(tp) > 0):
        # réutilise l'OCR R617 si déjà fait (p035, p036 partagés)
        legacy_tp = f"{LEGACY}/p{n:03d}-300.txt"
        if os.path.exists(legacy_tp) and os.path.getsize(legacy_tp) > 0:
            shutil.copy(legacy_tp, tp)
            return open(tp, encoding="utf-8").read()
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
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 35
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 48
    doc = fitz.open(PDF)
    for p in range(first, last + 1):
        lay = layer(p)
        ocr = ocr_page(doc, p)
        pm = pymu(doc, p)
        with open(f"{WORK}/p{p:03d}-dual.txt", "w", encoding="utf-8") as fh:
            fh.write(f"===== p{p} COUCHE pdftotext =====\n{lay}")
            fh.write(f"\n===== p{p} OCR 300 dpi =====\n{ocr}\n")
        print(f"p{p}: couche {len(lay)} car, OCR {len(ocr)} car, pymu {len(pm)} car")
    doc.close()
    return 0


if __name__ == "__main__":
    import shutil  # placé ici pour éviter l'écrasement de nom
    sys.exit(main())
