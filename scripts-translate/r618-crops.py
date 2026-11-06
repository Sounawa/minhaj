#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R618 — recadrages d'arbitrage leçon 4 ulum-hadith-tanawi-2 (p.26-29).
Chaque zone ambiguë (nombres miroir, pavés muets, lecture OCR douteuse) est
rendue en PNG 600 dpi puis recadrée par bandes relatives pour lecture image.
Usage : python3 scripts-translate/r618-crops.py"""
import os

import fitz
from PIL import Image

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r618"
os.makedirs(OUT, exist_ok=True)

# (nom, page, (y0, y1) en fractions de hauteur) — bandes 600 dpi
CROPS = [
    ("r01-p26-banniere", 26, (0.00, 0.22)),    # bannière leçon 4 + objectifs
    ("r02-p26-tamhid-matn", 26, (0.20, 0.52)), # tamhīd + matn Ibn Ḥaǧar
    ("r03-p26-def-langa", 26, (0.50, 0.99)),   # تعريف لغة + مقاييس + footer
    ("r04-p27-haut", 27, (0.00, 0.30)),        # اصطلاحاً + فاض الماء + غيّر
    ("r05-p27-conditions", 27, (0.28, 0.55)),  # شروط 1-2 + الصحابة
    ("r06-p27-qismain", 27, (0.52, 0.75)),     # قسمان اصطلاحي/غير اصطلاحي
    ("r07-p27-qunut", 27, (0.72, 1.00)),       # أنواع + قنوت أنس + footer
    ("r08-p28-fiqh-aam", 28, (0.00, 0.28)),    # الفقهاء الطلاق + العامة العجلة
    ("r09-p28-dates", 28, (0.26, 0.62)),       # 5 مصنفات + dates miroir
    ("r10-p28-ajluni-hukm", 28, (0.58, 0.80)), # العجلوني + حكم المشهور
    ("r11-p28-iyad", 28, (0.78, 1.00)),        # عياض + ص:؟
    ("r12-p29-taqwim", 29, (0.00, 0.30)),      # التقويم 3 items
    ("r13-p29-istithmar", 29, (0.28, 0.62)),   # السخاوي فتح المغيث 4/؟ + question
    ("r14-p29-iidad", 29, (0.60, 1.00)),       # الإعداد القبلي + footer
]

doc = fitz.open(PDF)
for name, page, (fy0, fy1) in CROPS:
    pix = doc[page - 1].get_pixmap(dpi=600)
    png = f"{OUT}/{name}-full.png"
    pix.save(png)
    im = Image.open(png)
    w, h = im.size
    im.crop((0, int(h * fy0), w, int(h * fy1))).save(f"{OUT}/{name}.png")
    os.remove(png)
    print(name, "OK")
print("DONE", OUT)
