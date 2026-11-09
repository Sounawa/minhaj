# -*- coding: utf-8 -*-
"""Minhāj — Crops de SONDAGE leçon 12 hadith-3es (R663, slot pdf-mut23h2x-401,
أحكام السعي بين الصفا والمروة). Bornes p.84-89 confirmées par sondage d'en-têtes
(objectifs leçon 13 p.90 = borne exclusive ; clôture leçon 11 p.83). Mécanique
hadith3-crops-402-r657.py : pages pleines 300 dpi + bandes hautes 600 dpi.
Sortie : tr-tmp/qa-crops-r663/ (crops légers, purgeables, ne jamais détruire)."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r663"
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
crop("p83-top", 83, 0.00, 0.25, dpi=600)
crop("p84-full", 84)
crop("p84-top", 84, 0.00, 0.35, dpi=600)
crop("p85-full", 85)
crop("p86-full", 86)
crop("p87-full", 87)
crop("p88-full", 88)
crop("p89-full", 89)
crop("p89-top", 89, 0.00, 0.35, dpi=600)
crop("p90-top", 90, 0.00, 0.25, dpi=600)
