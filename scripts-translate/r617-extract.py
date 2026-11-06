#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R617 — leçon 5 ulum-hadith-tanawi-2 (pdf-mut23h2u-259, الدرس 5 : العزيز والغريب).
Bornes : p.30 = bannière leçon 5 العزيز والغريب (sondée R615/R616, à confirmer
image) ; borne supérieure = bannière leçon 6 الحديث الصحيح ومراتبه (à sonder
p.31-p.40). Extraction DOUBLE : couche incorporée (pdftotext) + OCR tesseract
ara 300 dpi psm 4 (méthode R603-R616). Caches crash-safe tr-tmp/r617/pNNN-*.txt
(skip si présent — OCR p030 déjà dans tr-tmp/r616/, réutilisé par lien).
NOMBRES DE LA COUCHE pdftotext INVERSÉS EN MIROIR (piège R613-R616) : chaque
nombre équivoque tranché par recadrage 600-1200 dpi + lecture image (couche
PyMuPDF fidèle — mécanisme élucidé R615).
Usage : python3 scripts-translate/r617-extract.py [first last]"""
import os
import shutil
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
WORK = f"{HOME}/tr-tmp/r617"
LEGACY = f"{HOME}/tr-tmp/r616"
TESSDATA = f"{HOME}/scripts-translate/tessdata"


def layer(p: int) -> str:
    out = f"{WORK}/p{p:03d}-layer.txt"
    if not (os.path.exists(out) and os.path.getsize(out) > 0):
        subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF, out], check=True)
    return open(out, encoding="utf-8").read()


def ocr_page(doc, n: int, dpi: int = 300) -> str:
    tp = f"{WORK}/p{n:03d}-300.txt"
    if not (os.path.exists(tp) and os.path.getsize(tp) > 0):
        # réutilise l'OCR R616 si déjà fait (p030 partagé)
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


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 36
    doc = fitz.open(PDF)
    for p in range(first, last + 1):
        lay = layer(p)
        ocr = ocr_page(doc, p)
        with open(f"{WORK}/p{p:03d}-dual.txt", "w", encoding="utf-8") as fh:
            fh.write(f"===== p{p} COUCHE pdftotext =====\n{lay}")
            fh.write(f"\n===== p{p} OCR 300 dpi =====\n{ocr}\n")
        print(f"p{p}: couche {len(lay)} car, OCR {len(ocr)} car")
    doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
