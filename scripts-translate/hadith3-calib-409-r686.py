# -*- coding: utf-8 -*-
"""Minhāj — calibrations 300 dpi pleine page leçon 409 hadith-3es (R686).
Méthode r685 : calibrations pleine page PUIS micro-crops 600 dpi ciblés.
Feuilles : 2 pages par image, largeur 1400."""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r686"
import os
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
W = 1400

def page_img(n, dpi=300):
    pix = doc[n - 1].get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    r = W / img.width
    return img.resize((W, int(img.height * r)), Image.LANCZOS)

pairs = [("cal-p136-137", 136, 137), ("cal-p138-139", 138, 139), ("cal-p140-141", 140, 141)]
for name, a, b in pairs:
    ia, ib = page_img(a), page_img(b)
    sep = 16
    sheet = Image.new("RGB", (W, ia.height + ib.height + sep), (255, 205, 205))
    sheet.paste(ia, (0, 0))
    sheet.paste(ib, (0, ia.height + sep))
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print("OK", path, sheet.size)
