# -*- coding: utf-8 -*-
"""Minhāj — Extraction + OCR local leçon 23 hadith-2es (slot pdf-24, R569).
Bornes (hadith2-map.py) : l23 أحكام الصيام 1 أهداف الدرس p.158 ;
l24 أحكام الصيام 2 أهداف p.165 → leçon = p.158-164.
Extraction large p.157-165 pour preuve des bornes (jamais devinées).
OCR arabe local tesseract 300 dpi (tessdata du dépôt, zéro API vision).
"""
import os
import subprocess

import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l23-readable.txt"
FIRST, LAST = 157, 165
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r569"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"

os.makedirs(CROPS, exist_ok=True)

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
data = "\n".join(chunks)
open(OUT, "w", encoding="utf-8").write(data)
print(f"EXTRACTION OK {OUT} — {len(data)} car, pages {FIRST}-{LAST}")

# OCR tesseract 300 dpi des pages de la leçon (158-164)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
for n in range(158, 165):
    page = doc[n - 1]
    pix = page.get_pixmap(dpi=300)
    png = f"{CROPS}/page-{n}-300.png"
    pix.save(png)
    r = subprocess.run(
        ["tesseract", png, f"{CROPS}/tess-page-{n}", "-l", "ara", "--psm", "4"],
        env=env, capture_output=True, text=True)
    ok = "OK" if r.returncode == 0 else f"ERR {r.stderr[:120]}"
    size = 0
    tp = f"{CROPS}/tess-page-{n}.txt"
    if os.path.exists(tp):
        size = len(open(tp, encoding="utf-8").read())
    print(f"OCR p.{n}: {ok} — {size} car")
print("DONE")
