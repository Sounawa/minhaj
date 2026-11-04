# -*- coding: utf-8 -*-
"""R573 — rendu 300 dpi pages 192-198 + tesseract arabe + crops ciblés.
Sortie : tr-tmp/r573-pages/ + tr-tmp/r573-crops/ + tesseract layer."""
import os
import subprocess

import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r573-pages"
CROPS = "/home/z/my-project/tr-tmp/r573-crops"
os.makedirs(OUT, exist_ok=True)
os.makedirs(CROPS, exist_ok=True)

doc = fitz.open(PDF)
pages = [192, 193, 194, 195, 196, 197, 198]
for pno in pages:
    pix = doc[pno - 1].get_pixmap(dpi=300)
    path = f"{OUT}/p{pno}.png"
    pix.save(path)
    print(path, pix.width, "x", pix.height)

# crops 900 dpi des zones ambiguës : (page, rect proportionnel x0,y0,x1,y1, nom)
# repérage approximatif sur la couche texte ; serons larges, adjudication à l'œil
CROP_DEFS = [
    # p.192 : taḥmīd + hadith ʿĀʾiša + crochet [Muwaṭṭaʾ 862] (moitié basse)
    (192, 0.30, 0.42, 1.00, 1.00, "p192-tahmid-hadith-862", 900),
    # p.193 : hadith أبي هريرة + crochet [864] + hadith الجمعة [887] (moitié haute)
    (193, 0.00, 0.00, 1.00, 0.55, "p193-hadith-864-887", 900),
    # p.193 : bas (المشكل/الشرح/الخلاف)
    (193, 0.00, 0.50, 1.00, 1.00, "p193-mushkil-sharh", 900),
    # p.195 : crochet [65] zone فتحت أبواب الجنة + [863] zone الصيام جنة
    (195, 0.00, 0.00, 1.00, 0.45, "p195-hadith-65-ramadan", 900),
    (195, 0.00, 0.45, 1.00, 1.00, "p195-hadith-863-junna", 900),
    # p.196 : مالك 887 + حديث الجمعة الصحيحين
    (196, 0.00, 0.00, 1.00, 1.00, "p196-full", 600),
    # p.197 : الاستثمار مالك + الزرقاني [866] + sources
    (197, 0.00, 0.00, 1.00, 1.00, "p197-full", 600),
    # p.198 : page entière — contenu inconnu (couche vide)
    (198, 0.00, 0.00, 1.00, 1.00, "p198-full", 600),
]
for pno, x0, y0, x1, y1, name, dpi in CROP_DEFS:
    page = doc[pno - 1]
    r = page.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    path = f"{CROPS}/{name}.png"
    pix.save(path)
    print(path, pix.width, "x", pix.height)
