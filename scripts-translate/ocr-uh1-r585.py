#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R585 — OCR 300 dpi p.47-52 de ulum-hadith-1-thanawi.pdf (chaîne R578→R584).
Leçon 8 ulum-hadith-tanawi-1 (pdf-mut23h2q-119, الحديث العزيز) :
bornes p.47-? (sondage : objectifs L120 p.>47 — directive tail R584).
p.47-50 pré-seedées du cache R584 (déjà OCR pour sondage borne).
fitz 300 dpi + tesseract ara (tessdata dépôt) psm 4 — zéro vision API.
Cache crash-safe : tr-tmp/r585-uh1/p<N>-300.txt (txt nominal, png supprimé après).
Usage : python3 scripts-translate/ocr-uh1-r585.py [first last]
"""
import os
import shutil
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r585-uh1"
SEED = f"{HOME}/tr-tmp/r584-uh1"
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
    # pré-seed p.47-50 depuis le cache R584 (déjà OCR pour sondage de borne)
    for n in range(47, 51):
        src = f"{SEED}/p{n}-300.txt"
        dst = f"{WORK}/p{n}-300.txt"
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copyfile(src, dst)
            print(f"[seed p{n} <- R584]")
    doc = fitz.open(PDF)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 51
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 52
    for n in range(first, last + 1):
        txt = ocr_page(doc, n)
        print(f"--- p{n} ({len(txt)} car) ---")
        print(txt)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
