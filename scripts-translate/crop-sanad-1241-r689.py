# -*- coding: utf-8 -*-
"""Crop serré du paragraphe sanad 1241 (haut de p145) pour adjudication VLM."""
from PIL import Image

SRC = "/home/z/my-project/tr-tmp/qa-crops-r688/m410-p145.png"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r688/z410-8-p145-sanad.png"
img = Image.open(SRC)
w, h = img.size
# paragraphe 1 ≈ 4%-30% de la hauteur
crop = img.crop((0, int(h * 0.03), w, int(h * 0.30)))
crop = crop.resize((crop.width * 2, crop.height * 2), Image.LANCZOS)
crop.save(OUT)
print("OK", OUT, crop.size)
