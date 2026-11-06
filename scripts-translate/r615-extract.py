#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R615 — leçon 3 ulum-hadith-tanawi-2 (pdf-mut23h2u-257, الدرس 3 : المتواتر والآحاد).
Bornes : p.20 = bannière leçon 3 + objectifs (sondée R614/R615 couche) ; borne supérieure
= p.26 bannière leçon 4 المشهور (à confirmer OCR). Extraction DOUBLE :
couche incorporée (pdftotext) + OCR tesseract ara 300 dpi psm 4 (méthode R603-R614).
Caches crash-safe tr-tmp/r615/pNNN-300.txt (skip si présent).
NOMBRES DE LA COUCHE INVERSÉS (piège R613-R614) : chaque nombre tranché OCR + crop.
Usage : python3 scripts-translate/r615-extract.py [first last]"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
WORK = f"{HOME}/tr-tmp/r615"
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
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 26
    doc = fitz.open(PDF)
    lay_all, ocr_all = [], []
    for n in range(first, last + 1):
        lt = layer(n)
        ot = ocr_page(doc, n)
        lay_all.append(f"===== p{n} COUCHE =====\n{lt}")
        ocr_all.append(f"===== p{n} OCR 300 =====\n{ot}")
        print(f"p{n}: couche {len(lt)} car / OCR {len(ot)} car")
    with open(f"{HOME}/tr-tmp/r615-l3-layer.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lay_all))
    with open(f"{HOME}/tr-tmp/r615-l3-ocr.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(ocr_all))
    print("écrit : tr-tmp/r615-l3-layer.txt + tr-tmp/r615-l3-ocr.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
