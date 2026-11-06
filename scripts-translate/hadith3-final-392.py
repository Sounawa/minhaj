# -*- coding: utf-8 -*-
"""Minhāj — pile 900 dpi finale, 3 zones restantes (R625 leçon 3):
a) p.26 gloss شَرَّة (ligne y≈645-675)
b) p.27 citation Muslim (y≈640-690)
c) p.28 dialogue 925 (autour de la ligne « رقم 925 »)
Sortie : tr-tmp/qa-crops-r625/pile-finale-900.png
"""
import fitz, re
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r625/pile-finale-900.png"
doc = fitz.open(PDF)

def line_y(page, needle_re):
    d = page.get_text("dict")
    ys = []
    for blk in d["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            t = "".join(s["text"] for s in ln["spans"])
            if re.search(needle_re, t):
                ys.append(fitz.Rect(ln["bbox"]).y0)
    return min(ys) if ys else None

crops = []
pw, ph = doc[25].rect.width, doc[25].rect.height
pix = doc[25].get_pixmap(dpi=900, clip=fitz.Rect(0, 636, pw, 682))   # p.26 gloss
pix.save("/home/z/my-project/tr-tmp/qa-crops-r625/f-a-p26-gloss.png")
crops.append("/home/z/my-project/tr-tmp/qa-crops-r625/f-a-p26-gloss.png")

pix = doc[26].get_pixmap(dpi=900, clip=fitz.Rect(0, 638, pw, 692))   # p.27 Muslim
pix.save("/home/z/my-project/tr-tmp/qa-crops-r625/f-b-p27-muslim.png")
crops.append("/home/z/my-project/tr-tmp/qa-crops-r625/f-b-p27-muslim.png")

p28 = doc[27]
y925 = line_y(p28, r"925")
print("y925 =", y925)
pix = p28.get_pixmap(dpi=900, clip=fitz.Rect(0, y925 - 128, pw, y925 + 26))
pix.save("/home/z/my-project/tr-tmp/qa-crops-r625/f-c-p28-925.png")
crops.append("/home/z/my-project/tr-tmp/qa-crops-r625/f-c-p28-925.png")

ims = [Image.open(f) for f in crops]
w = max(im.width for im in ims)
h = sum(im.height for im in ims) + 12 * (len(ims) - 1)
canvas = Image.new("RGB", (w, h), (255, 255, 255))
y = 0
for im in ims:
    canvas.paste(im, (0, y))
    y += im.height + 12
canvas.save(OUT)
print(f"OK {OUT} {canvas.size}")
