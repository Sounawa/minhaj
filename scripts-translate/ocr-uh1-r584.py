#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R584 — OCR 300 dpi p.43-49 de ulum-hadith-1-thanawi.pdf (chaîne R578→R583).
Leçon 7 ulum-hadith-tanawi-1 (pdf-mut23h2q-118, الحديث المسلسل) :
bornes p.43-? (sondage : objectifs L119 p.>43 — carte R578, starts p.43,47,52…).
p.43 pré-seedée du cache R583 (déjà OCR pour sondage borne).
fitz 300 dpi + tesseract ara (tessdata dépôt) psm 4 — zéro vision API.
Cache crash-safe : tr-tmp/r584-uh1/p<N>-300.txt (txt nominal, png supprimé après).
Usage : python3 scripts-translate/ocr-uh1-r584.py [first last]
"""
import os
import shutil
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r584-uh1"
SEED = f"{HOME}/tr-tmp/r583-uh1"
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
    # pré-seed p.43 depuis le cache R583 (déjà OCR pour le sondage de borne)
    for n in range(43, 45):
        src = f"{SEED}/p{n}-300.txt"
        dst = f"{WORK}/p{n}-300.txt"
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copyfile(src, dst)
            print(f"[seed p{n} <- R583]")
    doc = fitz.open(PDF)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 43
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 49
    for n in range(first, last + 1):
        txt = ocr_page(doc, n)
        print(f"--- p{n} ({len(txt)} car) ---")
        print(txt)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
