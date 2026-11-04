# -*- coding: utf-8 -*-
"""Minhāj — OCR local leçon 24 hadith-2es (slot pdf-25, R570).
Bornes (hadith2-map.py) : l24 أحكام الصيام 2 أهداف الدرس p.165 ;
l25 أحكام الصيام 3 أهداف p.171 → leçon = p.165-170.
Matière déjà pré-extraite : tr-tmp/hadith2-l24-readable.txt (13:09Z).
OCR arabe local tesseract 300 dpi + TSV (tessdata du dépôt, zéro API vision).
"""
import csv
import os
import subprocess

import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r570"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
FIRST, LAST = 165, 170

os.makedirs(CROPS, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

doc = fitz.open(PDF)
for n in range(FIRST, LAST + 1):
    page = doc[n - 1]
    png300 = f"{CROPS}/page-{n}-300.png"
    if not os.path.exists(png300):
        pix = page.get_pixmap(dpi=300)
        pix.save(png300)
        print(f"RENDU {png300}")
    r = subprocess.run(
        ["tesseract", png300, f"{CROPS}/tess-page-{n}", "-l", "ara", "--psm", "4"],
        env=env, capture_output=True, text=True)
    ok = "OK" if r.returncode == 0 else f"ERR {r.stderr[:120]}"
    tp = f"{CROPS}/tess-page-{n}.txt"
    size = len(open(tp, encoding="utf-8").read()) if os.path.exists(tp) else 0
    print(f"OCR p.{n}: {ok} — {size} car")

# TSV : positions (y à 300 dpi) des lignes contenant des chiffres → ciblage crops
print("--- TSV lignes avec chiffres (page, y1, texte) ---")
for n in range(FIRST, LAST + 1):
    tsv = f"{CROPS}/tess-page-{n}.tsv"
    if not os.path.exists(tsv):
        subprocess.run(
            ["tesseract", f"{CROPS}/page-{n}-300.png", f"{CROPS}/tess-page-{n}",
             "-l", "ara", "--psm", "4", "tsv"],
            env=env, capture_output=True, text=True)
    rows = list(csv.reader(open(tsv, encoding="utf-8"), delimiter="\t"))
    lines = {}
    for row in rows[1:]:
        if len(row) < 12:
            continue
        try:
            conf = float(row[10])
        except ValueError:
            continue
        if conf < 0:
            continue
        key = (row[2], row[3], row[4])
        lines.setdefault(key, []).append((int(row[7]), row[11]))
    for key, words in lines.items():
        text = " ".join(w for _, w in words)
        if any(c.isdigit() for c in text):
            top = min(int(k.split("\t")[1]) if False else 0 for k in [key[0]])  # placeholder
    # version simple : relire tsv par blocs
    blocs = {}
    for row in rows[1:]:
        if len(row) < 12 or row[0] != "5":
            continue
        try:
            conf = float(row[10])
        except ValueError:
            continue
        if conf < 0 or not row[11].strip():
            continue
        k = (row[2], row[3], row[4])
        blocs.setdefault(k, []).append((int(row[7]), row[11]))
    for k, words in blocs.items():
        words.sort()
        text = " ".join(w for _, w in words)
        if any(c.isdigit() for c in text):
            print(f"p.{n} y={words[0][0]:>4} | {text[:110]}")
print("DONE")
