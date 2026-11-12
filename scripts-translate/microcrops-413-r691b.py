#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — microcrops fins d'adjudication leçon 413 (R691-b, canal principal).
Bandes ~300-380 px à zoom ×3 (4500 px de large ≈ 900 dpi) pour lecture
lettre à lettre. Mêmes sources pages-413/*.png."""
from PIL import Image
import os

SRC = "/home/z/my-project/tr-tmp/pages-413"
OUT = "/home/z/my-project/tr-tmp/m413-r691b"
os.makedirs(OUT, exist_ok=True)

CROPS = [
    ("m159-obj",      "p159.png", 130, 640),
    ("m159-tamh",     "p159.png", 640, 1180),
    ("m159-t1367",    "p159.png", 1180, 1520),
    ("m159-t1364",    "p159.png", 1520, 1929),
    ("m160-t1354",    "p160.png", 0, 380),
    ("m160-notice",   "p160.png", 380, 700),
    ("m160-gloss",    "p160.png", 700, 1000),
    ("m161-hukm",     "p161.png", 0, 380),
    ("m161-muslim",   "p161.png", 380, 720),
    ("m161-tabarani", "p161.png", 720, 1060),
    ("m161-ayam",     "p161.png", 1060, 1400),
    ("m161-ibnumar",  "p161.png", 1400, 1700),
    ("m161-qassar",   "p161.png", 1700, 1929),
    ("m162-analyse",  "p162.png", 0, 300),
    ("m162-msalik",   "p162.png", 300, 560),
    ("m162-barra",    "p162.png", 560, 1260),
    ("m162-jabir",    "p162.png", 1260, 1929),
    ("m163-taqwim",   "p163.png", 0, 480),
    ("m163-t1356",    "p163.png", 480, 1260),
    ("m163-idad",     "p163.png", 1260, 1929),
]

for name, src, y0, y1 in CROPS:
    im = Image.open(f"{SRC}/{src}")
    band = im.crop((0, y0, im.width, y1))
    band = band.resize((band.width * 3, band.height * 3), Image.LANCZOS)
    path = f"{OUT}/{name}.png"
    band.save(path)
    print(f"{name}: {band.size[0]}x{band.size[1]}")
