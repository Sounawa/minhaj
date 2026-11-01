#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R95 — zooms 600 dpi des 6 micro-zones encore douteuses après les crops 220 dpi.
(y exprimés en px de la base 220 dpi, convertis ×2.7273 en 600 dpi)"""
import fitz
from PIL import Image

PDF = "/tmp/tafsir2es-manual.pdf"
doc = fitz.open(PDF)
K = 72 / 220.0  # px (base 220 dpi) → points PDF
ZONES = [
    (90, 760, 900, "alus-ornate"),      # citation ornée dans Âlūsī
    (91, 400, 480, "l91-expressions"),  # يُمْسِكُ - تَزُولَا - يُمِيسَدُ
    (94, 950, 1030, "l94-top-ornate"),  # ornate + bracket [؟: 80]
    (94, 1280, 1390, "l94-nufur"),      # جواب للقسم المقدر
    (96, 1450, 1530, "l96-hud"),        # ornate + [التحريم? : 10]
    (97, 460, 620, "l97-expressions"),  # expressions v45-46
]
for p, y0, y1, tag in ZONES:
    page = doc[p - 1]
    clip = fitz.Rect(0, y0 * K, page.rect.width, y1 * K)
    pix = page.get_pixmap(dpi=600, clip=clip)
    out = f"/tmp/r95-z600-{p}-{tag}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
doc.close()
