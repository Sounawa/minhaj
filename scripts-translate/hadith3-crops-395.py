# -*- coding: utf-8 -*-
"""Minhāj — inspections image leçon 6 hadith-3es (slot pdf-mut23h2x-395, R638).
Piles 600 dpi des zones ambiguës / numéros de référence à trancher chiffre à
chiffre (jamais deviné — doctrine R625-R636) :
  A) p.45 haut   : bannière + objectifs + تحديد الغاية (couches corrompues)
  B) p.45 bas    : texte n° 930 (matn + numéro en crochet bleu)
  C) p.46        : textes n° 961/963 + tarǧama al-Qāsim + الشرح
  D) p.48 haut   : miqāts 1-2 (ذو الحليفة + 931, الجحفة + زاد النسائي)
  E) p.49        : textes 964/965/966 + ثالثا حكم مجاوزة (numéros + ابن عبد البر)
  F) p.50        : عياض + المواقيت الزمانية + 962/963
Sortie : tr-tmp/qa-crops-r638/pile-<tag>.png"""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r638"
os.makedirs(OUT, exist_ok=True)

ZONES = {
    "A-p45-haut":   (45, 0.00, 0.52),
    "B-p45-bas":    (45, 0.50, 1.00),
    "C-p46":        (46, 0.00, 1.00),
    "D-p48-haut":   (48, 0.00, 0.42),
    "E-p49":        (49, 0.00, 1.00),
    "F-p50":        (50, 0.30, 1.00),
}

doc = fitz.open(PDF)
for tag, (p, f0, f1) in ZONES.items():
    page = doc[p - 1]
    pix = page.get_pixmap(dpi=600)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    h = img.height
    crop = img.crop((0, int(h * f0), img.width, int(h * f1)))
    # piles larges : on découpe en tranches verticales empilées pour lisibilité
    W = crop.width
    slice_w = 1500
    n = (W + slice_w - 1) // slice_w
    parts = [crop.crop((i * slice_w, 0, min((i + 1) * slice_w, W), crop.height)) for i in range(n)]
    total_w = max(p.width for p in parts)
    total_h = sum(p.height for p in parts) + 8 * (len(parts) - 1)
    pile = Image.new("RGB", (total_w, total_h), "white")
    y = 0
    for part in parts:
        pile.paste(part, (0, y))
        y += part.height + 8
    path = f"{OUT}/pile-{tag}.png"
    pile.save(path)
    print(f"OK {path} — {pile.width}x{pile.height}")
