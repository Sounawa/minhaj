#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-vlm-h6-14 : recadrages COULEUR des zones résiduelles pour VLM
# (les zones colorées — gloses sur fond coloré, bandeaux, cartouche — sont
# illisibles en niveaux de gris pour tesseract ; le VLM les lit).
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/vlm"
os.makedirs(OUT, exist_ok=True)

# (label, page, y0, y1 @600, note) — largeur pleine, 600 dpi couleur
ZONES = [
    ("v01-cartouche-p76",    76,  620, 1030, "cartouche calligraphique du titre"),
    ("v02-objectifs-p76",    76, 1620, 2420, "encadré des objectifs"),
    ("v03-gloses-p77",       77, 3200, 3740, "zone des gloses du commentaire (fond coloré)"),
    ("v04-istikhlal-p77",    77, 3700, 4700, "extraction des idées (titre + items)"),
    ("v05-liali-p78",        78, 1880, 2200, "définition du plaignant, mot disputé"),
    ("v06-lahiqqi-p78",      78, 3700, 4030, "exemple, mot disputé avant «qui يدّعيه»"),
    ("v07-malam-p78",        78, 4760, 5050, "fin du paragraphe : ما لم … عليه بيّنة"),
    ("v08-yubayyin-p78",     78, 5360, 5690, "début du paragraphe ثانياً (2 premiers mots)"),
    ("v09-thalithan-p79",    79,  860, 1220, "éventuel sous-titre rouge ثالثاً"),
    ("v10-istithmar-p79",    79, 4370, 4870, "bandeau الاستثمار + ligne d'appel"),
    ("v11-bayyina-p78",      78, 1070, 1680, "définition de la preuve (2e ligne disputée)"),
    ("v12-yustafad-p79",     79, 1990, 2700, "bandeau + 2 items مما يستفاد"),
]

for label, page, y0, y1, _ in ZONES:
    base = f"{OUT}/{label}"
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "600",
                        "-png", "-singlefile", "-x", "150", "-y", str(y0),
                        "-W", "5000", "-H", str(y1 - y0), PDF, base], check=True)
    img = Image.open(base + ".png")
    if img.width > 3300:
        r = 3300 / img.width
        img = img.resize((3300, int(img.height * r)), Image.LANCZOS)
        img.save(base + ".png")
    print(f"{label} : {img.width}x{img.height}")
print("OK prep-vlm")
