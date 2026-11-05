#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R599 — Phase 1 : recadrages structurels 600 dpi de ulum-hadith-1-thanawi.pdf
Leçon 22 ulum-hadith-tanawi-1 (pdf-mut23h2q-133, الحديث المدرج, p.108-112).
Bornes p.108-112 par DOUBLE sondage (bannière ad-dars 23 + objectifs المُدَبَّج
lus à l'OCR p.113). Zones OCR manquantes/divergentes à trancher PAR L'IMAGE :
  c01 p.110 bas    : fin الصورة الرابعة (phrase + exemple ?) + sentence القطان
  c02 p.111 haut   : continuation éventuelle avant « 2- الإدراج في المتن » (GAP)
  c03 p.111 bas    : fin phrase النووي (à cheval p.111→p.112)
  c04 p.112 haut   : continuation زكريا الأنصاري + bandeau التقويم + Q1-Q2
  c05 p.112 milieu : bandeau الاستثمار + texte Ibn Ḥaǧar نزهة النظر ص116
  c06 p.112 bas    : bandeau الإعداد القبلي + questions (Q1 manquante OCR)
Chaîne R578+ (zéro vision API) — lecture image directe des crops."""
import os
import fitz
from PIL import Image, ImageDraw

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r599"
os.makedirs(OUT, exist_ok=True)
DPI = 600

# (nom, page, y0_frac, y1_frac) — bandes pleine largeur
BANDS = [
    ("c01-p110-bas",       110, 0.74, 1.00),
    ("c02-p111-haut",      111, 0.00, 0.20),
    ("c03-p111-bas",       111, 0.80, 1.00),
    ("c04-p112-haut",      112, 0.00, 0.24),
    ("c05-p112-milieu",    112, 0.24, 0.60),
    ("c06-p112-bas",       112, 0.60, 1.00),
]

doc = fitz.open(PDF)
cache = {}
def page_img(pno):
    if pno not in cache:
        pix = doc[pno - 1].get_pixmap(dpi=DPI)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        cache[pno] = img
    return cache[pno]

for name, pno, f0, f1 in BANDS:
    img = page_img(pno)
    W, H = img.size
    band = img.crop((0, int(H * f0), W, int(H * f1)))
    # marge blanche + label
    lab = Image.new("RGB", (band.width, band.height + 56), "white")
    lab.paste(band, (0, 56))
    d = ImageDraw.Draw(lab)
    d.text((12, 14), f"{name}  p.{pno}  [{f0:.2f}-{f1:.2f}]  {band.width}x{band.height}", fill="red")
    lab.save(f"{OUT}/{name}.png")
    print(f"{name}: {lab.width}x{lab.height}")
print("R599 phase 1 crops terminés ->", OUT)
