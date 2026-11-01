#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R108 — Sondes + OCR p167-174 (bornage 621 = فهرس الأعلام, 622 = فهرس المصادر).

Rend chaque page du manuel tafsir-3es en 400 dpi, recadre le bandeau supérieur
(haut ~22 % de la page) et empile 3 bandeaux par composite PNG pour lecture
visuelle (Read) : les bandeaux portent le titre de section et permettent de
borner فهرس الأعلام (621) et فهرس المصادر والمراجع (622).

Par ailleurs, OCR tesseract (ara, tessdata_best, psm 6) à 300 dpi de chaque
page, texte cru écrit dans tr-tmp/probe-r108/ocr-pNNN.txt (première passe de
lecture ; le cache officiel content/ocr-cache/pdf-mut23h36-621.json sera écrit
après bornage visuel de la section).
"""
import os
import subprocess
import sys

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/probe-r108"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
PAGES = list(range(167, 175))  # p167-174 (fin du livre, 174 pages)
PER = 3  # bandeaux par composite

os.makedirs(OUT, exist_ok=True)
pdf = fitz.open(PDF)
print(f"PDF ouvert : {pdf.page_count} pages", file=sys.stderr)

bands = []
for p in PAGES:
    pix = pdf[p - 1].get_pixmap(dpi=400)
    png = f"{OUT}/full-p{p}.png"
    pix.save(png)
    img = Image.open(png)
    w, h = img.size
    crop = img.crop((0, 0, w, int(h * 0.22)))
    bands.append((p, crop))

    # OCR cru 300 dpi
    pix300 = pdf[p - 1].get_pixmap(dpi=300)
    png300 = f"{OUT}/ocr300-p{p}.png"
    pix300.save(png300)
    env = dict(os.environ)
    env["TESSDATA_PREFIX"] = TESSDATA
    proc = subprocess.run(
        ["tesseract", png300, "stdout", "-l", "ara", "--psm", "6"],
        capture_output=True, text=True, timeout=180, env=env,
    )
    os.remove(png300)
    txt = proc.stdout if proc.returncode == 0 else f"[OCR erreur rc={proc.returncode}]"
    with open(f"{OUT}/ocr-p{p}.txt", "w", encoding="utf-8") as fh:
        fh.write(txt)
    nl = len([ln for ln in txt.splitlines() if ln.strip()])
    print(f"p{p} : bande {crop.size}, OCR {nl} lignes", file=sys.stderr)

pdf.close()

# empilement 3 par 3, largeur max unifiée
W = max(c.size[0] for _, c in bands)
for gi in range(0, len(bands), PER):
    grp = bands[gi:gi + PER]
    H = sum(c.size[1] for _, c in grp) + 30 * (len(grp) - 1)
    comp = Image.new("L", (W, H), 255)
    y = 0
    for p, c in grp:
        comp.paste(c, (0, y))
        y += c.size[1] + 30
    out = f"{OUT}/bands-{grp[0][0]}-{grp[-1][0]}.png"
    comp.save(out, optimize=True)
    print(f"composite : {out} ({comp.size})")

# nettoyage des full-p (bandes déjà extraites)
for p in PAGES:
    fp = f"{OUT}/full-p{p}.png"
    if os.path.isfile(fp):
        os.remove(fp)
print("probe-r108 terminé")
