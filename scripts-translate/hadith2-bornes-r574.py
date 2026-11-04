# -*- coding: utf-8 -*-
"""Minhāj R574 — Preuves de bornes pdf-30 (annexe 29) : bandeaux supérieurs p.201-203.
Composite horizontal : haut de chaque page (0-22 %) pour trancher où commence
لائحة المصادر والمراجع (annexe 30) et où finit فهرس الأعلام (annexe 29)."""
import fitz
from PIL import Image
import io, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r574-crops/bornes-p201-p202-p203.png"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

doc = fitz.open(PDF)
strips = []
for pno in (201, 202, 203):
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=300)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    h = img.height
    strip = img.crop((0, 0, img.width, int(h * 0.22)))
    strips.append((pno, strip))

w = max(s.width for _, s in strips)
gap = 30
label_h = 40
total_h = sum(s.height for _, s in strips) + gap * (len(strips) - 1) + label_h * len(strips)
comp = Image.new("RGB", (w, total_h), "white")
from PIL import ImageDraw
d = ImageDraw.Draw(comp)
y = 0
for pno, s in strips:
    d.text((10, y + 8), f"=== PAGE {pno} (haut 22%) ===", fill="blue")
    y += label_h
    comp.paste(s, (0, y))
    y += s.height + gap
comp.save(OUT)
print("OK", OUT, comp.size)
