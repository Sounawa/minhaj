#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — microcrops d'adjudication leçon 412 (R690, canal principal).

Bande lues depuis pages-412/*.png (1500×1929, 300 dpi) puis upscale ×2
(largeur finale ~3000 px) — doctrine : calibrations PUIS microcrops.

Zones (y en px source) :
  p153-a  : 40-560   médaillon 23 + les trois objectifs (أركان vs أحكام)
  p153-b  : 560-1160 tamhīd (fin) + texte n° 991 (premier mot افصلوا/أفضعوا)
  p153-c  : 1160-1929 texte n° 990 (matn de la femme : نذرت أن أطوف vs تجهزت للحج)
  p154-a  : 560-1240 fin texte 979 + notice d'abū bakr b. 'abd ar-raḥmān
  p155-a  : 560-1180 fin hadith Jābir + Mālik 993 (أراه/ضياعا) + début فضل
  p156-a  : 1200-1929 miqāt (fin) + citation Mālik 997 (فمن شاء vs فإنه)
  p157-a  : 200-1000 trois 'umra (renvoi 973) + temps (renvoi Hishām : 973 ou 974 ?)
  p158-a  : 0-950    disposition p.158 : texte n° 976 + mot تقل/قفل/تولى + rubriques
"""
from PIL import Image
import os

SRC = "/home/z/my-project/tr-tmp/pages-412"
OUT = "/home/z/my-project/tr-tmp/m412-r690"
os.makedirs(OUT, exist_ok=True)

CROPS = [
    ("p153-a", "p153.png", 40, 560),
    ("p153-b", "p153.png", 560, 1160),
    ("p153-c", "p153.png", 1160, 1929),
    ("p154-a", "p154.png", 560, 1240),
    ("p155-a", "p155.png", 560, 1180),
    ("p156-a", "p156.png", 1200, 1929),
    ("p157-a", "p157.png", 200, 1000),
    ("p158-a", "p158.png", 0, 950),
]

for name, src, y0, y1 in CROPS:
    im = Image.open(f"{SRC}/{src}")
    band = im.crop((0, y0, im.width, y1))
    band = band.resize((band.width * 2, band.height * 2), Image.LANCZOS)
    path = f"{OUT}/{name}.png"
    band.save(path)
    print(f"{name}: {band.size[0]}x{band.size[1]} -> {path}")
