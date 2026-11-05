#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R603 — OCR 300 dpi pages 124-132 de ulum-hadith-1-thanawi.pdf (chaîne R578→R602).
Leçon 26 ulum-hadith-tanawi-1 (pdf-mut23h2r-137, الحديث المنكر) :
  ouverture imprimée p.125 (bannière الدرس 26 + objectifs) ; borne supérieure par
  sondage (الإعداد القبلي annonçant le matrūk / bannière الدرس 27).
Post-recyclage sandbox : HOME = /tmp/my-project (arbre vivant — PDF source et
cache tr-tmp/r592-uh1 y subsistent). Cache crash-safe p<N>-300.txt (skip si
présent) — le cache partagé r592-uh1 est PROLONGÉ (p124+ utiles à R602 aussi).
fitz 300 dpi + tesseract ara psm 4 — zéro vision API.
Usage : python3 scripts-translate/ocr-uh1-r603.py [first last]
"""
import os
import subprocess
import sys

import fitz

HOME = "/tmp/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r592-uh1"
TESSDATA = f"{HOME}/scripts-translate/tessdata"


def ocr_page(doc, n: int, dpi: int = 300) -> str:
    tp = f"{WORK}/p{n}-300.txt"
    if os.path.exists(tp) and os.path.getsize(tp) > 0:
        return open(tp, encoding="utf-8").read()
    png = f"{WORK}/p{n}-300.png"
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
    doc = fitz.open(PDF)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 124
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 132
    for n in range(first, last + 1):
        txt = ocr_page(doc, n)
        print(f"--- p{n} ({len(txt)} car) ---")
        print(txt)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
