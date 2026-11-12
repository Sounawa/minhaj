#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R691 — planche de contact des microcrops 413 (contrôle de localisation)."""
from PIL import Image, ImageDraw
import os

SRC = "/home/z/my-project/tr-tmp/m413-r691"
OUT = "/home/z/my-project/tr-tmp/m413-r691/contact-sheet.jpg"
names = ["p159-a","p159-b","p159-c","p160-a","p160-b","p160-c","p160-d",
         "p161-a","p161-b","p161-c","p162-a","p162-b","p162-c",
         "p163-a","p163-b","p163-c"]
TW = 560  # largeur vignette
cols = 4
rows = (len(names) + cols - 1) // cols
cell_h = 400
sheet = Image.new("RGB", (cols * TW, rows * cell_h), "white")
d = ImageDraw.Draw(sheet)
for i, n in enumerate(names):
    im = Image.open(f"{SRC}/{n}.png")
    r = TW / im.width
    im = im.resize((TW, int(im.height * r)), Image.LANCZOS)
    x = (i % cols) * TW
    y = (i // cols) * cell_h
    sheet.paste(im.crop((0, 0, TW, min(cell_h - 18, im.height))), (x, y))
    d.text((x + 6, y + cell_h - 16), n, fill="red")
sheet.save(OUT, quality=72)
print(OUT, sheet.size)
