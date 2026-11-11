# -*- coding: utf-8 -*-
"""Minhāj — micro-crops leçon 410 hadith-3es (à RÉGLER après lecture des calibrations).

Doctrine (R685/R687) : 1) lire d'abord les calibrations pleine page 300 dpi
tr-tmp/qa-crops-r687/cal410-p141-142.png … cal410-p147-148.png et les sondes de
borne borne410-p147-haut.png / borne410-p148-haut.png (médaillon 22 à localiser) ;
2) AJUSTER les bandes ci-dessous au layout réel de chaque page (fractions y) ;
3) exécuter : python3 scripts-translate/microcrops-410-r688.py
4) lire les crops, trancher les numéros chiffre par chiffre (couches OCR
inversées : «0421»=1240, «2421»=1242, «3421»=1243, «4421»=1244, «5421»=1245,
«8421»=1248, «0621»=1260), adjudiquer à 900-1200 dpi les mots litigieux.
"""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r688"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0, r.x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, bands, width=1500):
    imgs = []
    for p, a, b in bands:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append(im.resize((width, int(im.height * r)), Image.LANCZOS))
    sep = 14
    H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
    sheet = Image.new("RGB", (width, H), (255, 210, 210))
    y = 0
    for im in imgs:
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print(f"OK {path} — {sheet.width}x{sheet.height}")


# ⚠︎ BANDES PROVISOIRES (trois tiers par page) — À AJUSTER après calibrations
SHEETS = [
    ("m-A-p141-medaillon-tamhid", [(141, 0.0, 0.35), (141, 0.33, 0.68)]),
    ("m-B-p141-textes", [(141, 0.60, 1.0), (142, 0.0, 0.20)]),
    ("m-C-p142-textes-notice", [(142, 0.18, 0.60), (142, 0.55, 1.0)]),
    ("m-D-p142-gloses-p143", [(143, 0.0, 0.35)]),
    ("m-E-p143-fiqh", [(143, 0.30, 0.70), (143, 0.65, 1.0)]),
    ("m-F-p144-fiqh", [(144, 0.0, 0.40), (144, 0.35, 0.75)]),
    ("m-G-p145-fiqh", [(145, 0.0, 0.40), (145, 0.35, 0.80)]),
    ("m-H-p146-tail", [(146, 0.0, 0.45), (146, 0.40, 0.90)]),
]

import os
os.makedirs(OUT, exist_ok=True)
for name, bands in SHEETS:
    composite(name, bands)
