#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — microcrops d'adjudication leçon 413 (R691, canal principal).

Bandes lues depuis pages-413/*.png (1500×1929, 300 dpi) puis upscale ×2
(largeur finale ~3000 px) — doctrine : calibrations PUIS microcrops.

Zones (y en px source) :
  p159-a  : 0-640     médaillon 24 + objectifs (titre أحكام/أمصار ? 3 ou 4 objectifs ?)
  p159-b  : 640-1180  tamhīd (شعيرة من الشعائر + āya calligraphique ﴿فصل لربك وانحر﴾ + renvoi الكوثر 2)
  p159-c  : 1180-1929 question d'ouverture + texte n° 1367 (matn : قوي على تمنها) + texte n° 1364 (isnad/matn)
  p160-a  : 0-620     texte n° 1354 (isnad بشر بن يسار + matn أنبأه/فذبحه + renvoi)
  p160-b  : 620-1050  notice أبو بردة (هانئ بن نيار ? + année 51) + الشرح (جدع : الدال والجيم ?)
  p160-c  : 1050-1500 استخلاص المضامين (2 items ?) + أولا مفهوم الأضحية
  p161-a  : 0-400    glose عياض (سُمّيت/تُفعل في الضحى)
  p161-b  : 400-1060  حكم الأضحية (Mālik 1367 + Muslim فليصق/فليمسك + الطبراني الأضحى عليّ فريضة)
  p161-c  : 1060-1929 ثانيا وقت الأضحية + أيام ثلاثة + quote ابن القصار + āya الحج (renvoi 28 ?)
  p162-a  : 0-560    fin analyse أيام + āya البقرة calligraphie + attribution المسالك (ابن عرفة ? 5/196 ?)
  p162-b  : 560-1260  حكم ذبح قبل الصلاة + رواية خطبنا رسول الله يوم النحر (letter à letter)
  p162-c  : 1260-1929 حكم بعد الصلاة + hadith جابر (بشاة/بغير) + الحسن + āya الحجرات calligraphie
  p163-a  : 0-480    3 items (résumé/évaluation ?) + rubrique
  p163-b  : 480-1260  texte n° 1356 (isnad + matn complet letter à letter)
  p163-c  : 1260-1929 استثمار (أقرأ الأثر) + إعداد القبلي (exercise شروط الأضحية)
"""
from PIL import Image
import os

SRC = "/home/z/my-project/tr-tmp/pages-413"
OUT = "/home/z/my-project/tr-tmp/m413-r691"
os.makedirs(OUT, exist_ok=True)

CROPS = [
    ("p159-a", "p159.png", 0, 640),
    ("p159-b", "p159.png", 640, 1180),
    ("p159-c", "p159.png", 1180, 1929),
    ("p160-a", "p160.png", 0, 620),
    ("p160-b", "p160.png", 620, 1050),
    ("p160-c", "p160.png", 1050, 1500),
    ("p160-d", "p160.png", 1400, 1929),
    ("p161-a", "p161.png", 0, 400),
    ("p161-b", "p161.png", 400, 1060),
    ("p161-c", "p161.png", 1060, 1929),
    ("p162-a", "p162.png", 0, 560),
    ("p162-b", "p162.png", 560, 1260),
    ("p162-c", "p162.png", 1260, 1929),
    ("p163-a", "p163.png", 0, 480),
    ("p163-b", "p163.png", 480, 1260),
    ("p163-c", "p163.png", 1260, 1929),
]

for name, src, y0, y1 in CROPS:
    im = Image.open(f"{SRC}/{src}")
    band = im.crop((0, y0, im.width, y1))
    band = band.resize((band.width * 2, band.height * 2), Image.LANCZOS)
    path = f"{OUT}/{name}.png"
    band.save(path)
    print(f"{name}: {band.size[0]}x{band.size[1]} -> {path}")
