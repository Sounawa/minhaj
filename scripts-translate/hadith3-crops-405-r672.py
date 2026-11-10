# -*- coding: utf-8 -*-
"""Minhāj — bandes 600 dpi leçon 405 hadith-3es (R672, slot pdf-mut23h2x-405,
aʿmāl ayyām Minā (2), fenêtre p.110-116, borne exclusive p.117).
Patron hadith3-zoom-403-r671.py (fitz). Feuilles de contact : 2 bandes max
par image (largeur 1600) pour rester lisibles sous le budget d'images.
Sortie : tr-tmp/qa-crops-r672/sheet-*.png (crops légers, purgeables)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r672"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
WIDTH = 1600


def band(page_no, y0, y1):
    """Bande pleine largeur (fractions de hauteur) à 600 dpi, PIL Image."""
    pix = doc[page_no - 1].get_pixmap(dpi=600)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    W, H = img.size
    c = img.crop((int(W * 0.03), int(H * y0), int(W * 0.97), int(H * y1)))
    r = WIDTH / c.width
    return c.resize((WIDTH, int(c.height * r)), Image.LANCZOS)


SHEETS = [
    # (nom, [(page, y0, y1), ...])
    ("sheet-p110", [(110, 0.50, 0.80), (110, 0.74, 0.99)]),
    ("sheet-p111-a", [(111, 0.03, 0.42), (111, 0.40, 0.72)]),
    ("sheet-p111-b", [(111, 0.70, 0.99)]),
    ("sheet-p112-a", [(112, 0.03, 0.44), (112, 0.42, 0.72)]),
    ("sheet-p112-b", [(112, 0.70, 0.99)]),
    ("sheet-p113-a", [(113, 0.02, 0.40), (113, 0.38, 0.68)]),
    ("sheet-p113-b", [(113, 0.66, 0.99)]),
    ("sheet-p114-a", [(114, 0.02, 0.42), (114, 0.40, 0.70)]),
    ("sheet-p114-b", [(114, 0.68, 0.99)]),
    ("sheet-p115", [(115, 0.02, 0.46), (115, 0.44, 0.80), (115, 0.78, 0.99)]),
    ("sheet-p117-top", [(117, 0.00, 0.46)]),
]

for name, bands in SHEETS:
    parts = [band(p, y0, y1) for p, y0, y1 in bands]
    sep = 14
    total_h = sum(p.height for p in parts) + sep * (len(parts) - 1)
    sheet = Image.new("RGB", (WIDTH, total_h), (255, 210, 210))
    y = 0
    for p in parts:
        sheet.paste(p, (0, y))
        y += p.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print(f"OK {path} — {sheet.width}x{sheet.height}")
