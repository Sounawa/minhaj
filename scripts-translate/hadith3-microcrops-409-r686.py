# -*- coding: utf-8 -*-
"""Minhāj — micro-crops 600 dpi leçon 409 hadith-3es (R686). Zones décisives :
tamhīd+1174 (p.136), textes 1178/1184/1177 + notice + gloses (p.137),
fiqh 1-2 (p.138), ʿaḍliyya 1179 (p.139), 1180 + 1175 (p.140)."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r686"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
W = 1600


def band(page_no, y0, y1):
    pix = doc[page_no - 1].get_pixmap(dpi=600)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    Wp, Hp = img.size
    c = img.crop((int(Wp * 0.03), int(Hp * y0), int(Wp * 0.97), int(Hp * y1)))
    r = W / c.width
    return c.resize((W, int(c.height * r)), Image.LANCZOS)


SHEETS = [
    ("m-A-p136-tamhid-1174", [(136, 0.17, 0.53)]),
    ("m-B-p137-textes", [(137, 0.02, 0.30), (137, 0.28, 0.58)]),
    ("m-C-p137-notice", [(137, 0.56, 0.76)]),
    ("m-D-p137-gloses", [(137, 0.72, 0.96)]),
    ("m-E-p138-fiqh", [(138, 0.10, 0.42), (138, 0.38, 0.72)]),
    ("m-F-p139-aḍliyya", [(139, 0.02, 0.34), (139, 0.30, 0.64)]),
    ("m-G-p140-1180-1175", [(140, 0.02, 0.16), (140, 0.26, 0.46)]),
]

for name, bands in SHEETS:
    parts = [band(p, y0, y1) for p, y0, y1 in bands]
    sep = 14
    total_h = sum(p.height for p in parts) + sep * (len(parts) - 1)
    sheet = Image.new("RGB", (W, total_h), (255, 210, 210))
    y = 0
    for p in parts:
        sheet.paste(p, (0, y))
        y += p.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print(f"OK {path} — {sheet.width}x{sheet.height}")
