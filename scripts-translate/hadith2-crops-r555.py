# -*- coding: utf-8 -*-
"""Minhāj — R555 (pdf-12, leçon 11) : preuves image pour trancher les numéros
Muwaṭṭaʾ rouges + les blocs illisibles. Sortie : tr-tmp/qa-crops-r555/
  - composite-numbers.png : bandes serrées 900 dpi autour de chaque renvoi
  - composite-p79..p85.png : zones de matn 500 dpi empilées par page
"""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r555"
import os
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# --- bandes numéros : (page, token) ---
NUMS = [(79, "151"), (79, "41"), (79, "60"), (80, "562"), (80, "572"),
        (81, "566"), (82, "564"), (82, "567"), (83, "569"), (83, "569"),
        (83, "569"), (84, "572"), (84, "572"), (84, "576"), (85, "151"),
        (85, "185")]
strips = []
for pno, tok in NUMS:
    page = doc[pno - 1]
    hits = page.search_for(tok)
    if not hits:
        continue
    r = hits[0]
    clip = fitz.Rect(max(0, r.x0 - 15), max(0, r.y0 - 7),
                     min(page.rect.width, r.x1 + 120), min(page.rect.height, r.y1 + 7))
    pm = page.get_pixmap(matrix=fitz.Matrix(900 / 72, 900 / 72), clip=clip)
    pm.save(f"{OUT}/_strip.png")
    strips.append((pno, tok, Image.open(f"{OUT}/_strip.png")))
w = max(im.width for _, _, im in strips)
h = sum(im.height + 8 for _, _, im in strips)
comp = Image.new("RGB", (w, h), "white")
y = 0
for pno, tok, im in strips:
    comp.paste(im, (0, y))
    y += im.height + 8
comp.save(f"{OUT}/composite-numbers.png")
print(f"composite-numbers.png : {w}x{h} — {len(strips)} bandes")

# --- zones matn par page (pt coords) ---
ZONES = {
    79: [(40, 25, 600, 150), (40, 360, 600, 500), (40, 515, 600, 800)],
    80: [(40, 55, 600, 165), (40, 185, 600, 335)],
    81: [(40, 475, 600, 710)],
    82: [(40, 130, 600, 230), (40, 425, 600, 680)],
    84: [(40, 300, 600, 430), (40, 535, 600, 685)],
    85: [(40, 35, 600, 195), (40, 195, 600, 290), (40, 300, 600, 435),
         (40, 440, 600, 625)],
}
DPI = 500
for pno, zones in ZONES.items():
    page = doc[pno - 1]
    imgs = []
    for z in zones:
        clip = fitz.Rect(*z)
        pm = page.get_pixmap(matrix=fitz.Matrix(DPI / 72, DPI / 72), clip=clip)
        pm.save(f"{OUT}/_z.png")
        imgs.append(Image.open(f"{OUT}/_z.png"))
    tw = 1700
    sc = tw / max(i.width for i in imgs)
    imgs = [i.resize((int(i.width * sc), int(i.height * sc)), Image.LANCZOS) for i in imgs]
    H = sum(i.height + 10 for i in imgs)
    comp = Image.new("RGB", (tw, H), "white")
    y = 0
    for i in imgs:
        comp.paste(i, (0, y))
        y += i.height + 10
    comp.save(f"{OUT}/composite-p{pno}.png")
    print(f"composite-p{pno}.png : {comp.width}x{comp.height} — {len(zones)} zones")
os.remove(f"{OUT}/_strip.png")
os.remove(f"{OUT}/_z.png")
