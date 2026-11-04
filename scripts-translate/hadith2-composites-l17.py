# -*- coding: utf-8 -*-
"""Minhāj — Composites 900 dpi pour leçon 17 (pdf-18, R562).
Zones incertaines à trancher mot à mot (jamais devinées) — méthode R559/R560 :
recadrages 900 dpi resserrés sur les lignes douteuses, assemblés en composites
1 900 px de large (lisibilité préservée après downscale du lecteur)."""
from PIL import Image, ImageDraw
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r562"
DPI = 900
TARGET_W = 1900

# (label, page, y0_frac, y1_frac) — bornes verticales en fraction de page
ZONES = [
    ("118-tamhid-l1", 118, 0.445, 0.505),
    ("118-box-685", 118, 0.685, 0.975),
    ("119-text4-a", 119, 0.375, 0.525),
    ("119-text4-b", 119, 0.515, 0.675),
    ("120-685-fin", 120, 0.60, 0.955),
    ("121-madin-690", 121, 0.465, 0.645),
    ("121-risala", 121, 0.640, 0.785),
    ("122-691-fin", 122, 0.095, 0.455),
    ("122-maghsoub-689", 122, 0.445, 0.725),
    ("122-zurayq", 122, 0.775, 0.965),
    ("123-quote-695", 123, 0.115, 0.345),
    ("123-anwa-a-696", 123, 0.415, 0.705),
    ("123-anwa-b-694", 123, 0.695, 0.915),
    ("124-istintaj", 124, 0.285, 0.600),
]

COMPOSITES = [
    ("comp1-118", ["118-tamhid-l1", "118-box-685"]),
    ("comp2-119-text4", ["119-text4-a", "119-text4-b"]),
    ("comp3-120-121", ["120-685-fin", "121-madin-690", "121-risala"]),
    ("comp4-122", ["122-691-fin", "122-maghsoub-689", "122-zurayq"]),
    ("comp5-123", ["123-quote-695", "123-anwa-a-696", "123-anwa-b-694"]),
    ("comp6-124", ["124-istintaj"]),
]

doc = fitz.open(PDF)
cache = {}

def render(page_no):
    if page_no not in cache:
        pix = doc[page_no - 1].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
        img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
        cache[page_no] = img
    return cache[page_no]

for cname, members in COMPOSITES:
    tiles = []
    for label in members:
        zone = next(z for z in ZONES if z[0] == label)
        _, page, y0, y1 = zone
        img = render(page)
        h = img.height
        tile = img.crop((int(0.06 * img.width), int(y0 * h),
                         int(0.94 * img.width), int(y1 * h)))
        scale = TARGET_W / tile.width
        tile = tile.resize((TARGET_W, int(tile.height * scale)), Image.LANCZOS)
        tiles.append((label, tile))
    total_h = sum(t.height + 46 for _, t in tiles) + 10
    comp = Image.new("L", (TARGET_W, total_h), 255)
    d = ImageDraw.Draw(comp)
    y = 5
    for label, tile in tiles:
        d.rectangle([0, y, TARGET_W, y + 34], fill=210)
        d.text((12, y + 8), label, fill=0)
        y += 46
        comp.paste(tile, (0, y))
        y += tile.height + 10
    path = os.path.join(OUT, f"{cname}.png")
    comp.save(path)
    print(f"OK {path} — {TARGET_W}x{total_h}")
