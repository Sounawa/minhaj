#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R616 — leçon 4 ulum-hadith-tanawi-2 (pdf-mut23h2u-258, الدرس 4 : الحديث المشهور).
Bornes : p.26 = bannière leçon 4 + objectifs (sondée R615 couche) ; borne supérieure
= p.29 (الإعداد القبلي العزيز والغريب) ; p.30 = bannière leçon 5 العزيز والغريب
(à confirmer OCR). Extraction DOUBLE : couche incorporée (pdftotext) + OCR
tesseract ara 300 dpi psm 4 (méthode R603-R615). Caches crash-safe
tr-tmp/r616/pNNN-300.txt (skip si présent).
NOMBRES DE LA COUCHE INVERSÉS (piège R613-R615) : chaque nombre tranché OCR + crop
(couche PyMuPDF fidèle — mécanisme élucidé R615).
Usage : python3 scripts-translate/r616-extract.py [first last]"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
WORK = f"{HOME}/tr-tmp/r616"
TESSDATA = f"{HOME}/scripts-translate/tessdata"


def layer(p: int) -> str:
    out = f"{WORK}/p{p:03d}-layer.txt"
    if not (os.path.exists(out) and os.path.getsize(out) > 0):
        subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), PDF, out], check=True)
    return open(out, encoding="utf-8").read()


def ocr_page(doc, n: int, dpi: int = 300) -> str:
    tp = f"{WORK}/p{n:03d}-300.txt"
    if os.path.exists(tp) and os.path.getsize(tp) > 0:
        return open(tp, encoding="utf-8").read()
    png = f"{WORK}/p{n:03d}-300.png"
    if not os.path.exists(png):
        doc[n - 1].get_pixmap(dpi=dpi).save(png)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    r = subprocess.run(["tesseract", png, tp[:-4], "-l", "ara", "--psm", "4"],
                       env=env, capture_output=True, text=True)
    os.remove(png)
    if r.returncode != 0:
        return ""
    return open(tp, encoding="utf-8").read()


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    doc = fitz.open(PDF)
    lay_all, ocr_all = [], []
    for n in range(first, last + 1):
        lt = layer(n)
        ot = ocr_page(doc, n)
        lay_all.append(f"===== p{n} COUCHE =====\n{lt}")
        ocr_all.append(f"===== p{n} OCR 300 =====\n{ot}")
        print(f"p{n}: couche {len(lt)} car / OCR {len(ot)} car")
    with open(f"{HOME}/tr-tmp/r616-l4-layer.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lay_all))
    with open(f"{HOME}/tr-tmp/r616-l4-ocr.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(ocr_all))
    print("écrit : tr-tmp/r616-l4-layer.txt + tr-tmp/r616-l4-ocr.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
