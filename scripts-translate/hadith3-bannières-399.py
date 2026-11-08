# -*- coding: utf-8 -*-
"""Minhāj — PREUVE IMAGE bannières leçon 10 hadith-3es (R649, slot pdf-mut23h2x-399).
Bannières « الدرس العاشر » (borne inférieure) et « الدرس الحادي عشر » (borne
supérieure) : sans couche texte (déjà vérifié par sondage), preuve OBLIGÉE par
inspection d'image. Crops des bandes supérieures p.70-72 et p.77-79 à 600 dpi.
Sortie : tr-tmp/qa-crops-r647/ (crops légers, purgeables, ne jamais détruire)."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r647"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
DPI = 600


def crop(tag, page_no, y0, y1, x0=0.0, x1=1.0):
    pix = doc[page_no - 1].get_pixmap(dpi=DPI)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    W, H = img.size
    c = img.crop((int(W * x0), int(H * y0), int(W * x1), int(H * y1)))
    path = f"{OUT}/{tag}.png"
    c.save(path)
    print(f"OK {path} — {c.width}x{c.height}")


# Bande supérieure de chaque page candidate à la bannière
crop("p70-top", 70, 0.00, 0.30)
crop("p71-top", 71, 0.00, 0.30)
crop("p72-top", 72, 0.00, 0.25)
crop("p77-full", 77, 0.00, 1.00)
crop("p78-top", 78, 0.00, 0.35)
crop("p79-top", 79, 0.00, 0.35)
