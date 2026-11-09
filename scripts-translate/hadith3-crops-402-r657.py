# -*- coding: utf-8 -*-
"""Minhāj — Crops de SONDAGE leçon 13 hadith-3es (R657, slot pdf-mut23h2x-402,
أعمال يوم عرفة). Bornes à trancher : ouverture = bannière الدرس الثالث عشر
attendue p.90 ; clôture = exploitation + préparation préalable p.96 ; p.97 =
bannière du cours 14 (borne supérieure exclusive). Mécanique
hadith3-bannières-399.py : crops 300 dpi pleines + bandes hautes à 600 dpi.
Sortie : tr-tmp/qa-crops-r657/ (crops légers, purgeables, ne jamais détruire)."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r657"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(tag, page_no, y0=0.0, y1=1.0, x0=0.0, x1=1.0, dpi=300):
    pix = doc[page_no - 1].get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    W, H = img.size
    c = img.crop((int(W * x0), int(H * y0), int(W * x1), int(H * y1)))
    path = f"{OUT}/{tag}.png"
    c.save(path)
    print(f"OK {path} — {c.width}x{c.height}")


# Sondage bornes : pages entières 300 dpi + bandes hautes 600 dpi
crop("p89-full", 89)
crop("p90-full", 90)
crop("p90-top", 90, 0.00, 0.30, dpi=600)
crop("p91-full", 91)
crop("p92-full", 92)
crop("p93-full", 93)
crop("p94-full", 94)
crop("p95-full", 95)
crop("p96-full", 96)
crop("p96-top", 96, 0.00, 0.30, dpi=600)
crop("p97-full", 97)
crop("p97-top", 97, 0.00, 0.30, dpi=600)
