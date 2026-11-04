#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R577 PASS 2 — adjudication 300 dpi de la zone-bannière (haut de page,
~22 %) des 28 en-têtes de leçon tafsir-1-iadadi. Objectif : lire numéros
« الدرس N » et noms de sourates LUS, jamais devinés. Cache par page.
"""
import json
import os
import re
import subprocess

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/tafsir-1-iadadi.pdf"
WORK = f"{HOME}/tr-tmp/r577-t1"
TESSDATA = f"{HOME}/scripts-translate/tessdata"
PAGES = [11, 15, 20, 25, 30, 34, 38, 43, 47, 52, 57, 62, 67, 72, 77, 82,
         87, 92, 97, 102, 106, 111, 115, 119, 125, 129, 134, 139]

doc = fitz.open(PDF)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
out = []
os.makedirs(f"{WORK}/banners-300", exist_ok=True)
for n in PAGES:
    tp = f"{WORK}/banners-300/p{n}"
    txtf = tp + ".txt"
    if not os.path.exists(txtf):
        page = doc[n - 1]
        rect = page.rect
        clip = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + rect.height * 0.22)
        pix = page.get_pixmap(dpi=300, clip=clip)
        png = f"{WORK}/banners-300/p{n}.png"
        pix.save(png)
        r = subprocess.run(["tesseract", png, tp, "-l", "ara", "--psm", "6"],
                           env=env, capture_output=True, text=True)
        os.remove(png)
    txt = open(txtf, encoding="utf-8").read() if os.path.exists(txtf) else ""
    flat = re.sub(r"\s+", " ", txt).strip()
    out.append({"page": n, "banner": flat[:220]})
    print(f"p.{n:>3}: {flat[:160]}")

json.dump(out, open(f"{WORK}/banners-300.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("→", f"{WORK}/banners-300.json")
