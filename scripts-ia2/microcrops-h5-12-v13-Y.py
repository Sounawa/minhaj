#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-14 — planche Y (lecture finale) : 3 dernières micro-zones, ×2.2-2.4
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-Y-final.png'

def zone(pg, y0, y1, x0, x1, label, scale=2.2):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1750:
        tw = 1750
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(71, 0.150, 0.275, 0.04, 0.99, 'Y1. p71 l.2-4 du bloc THANIA (fa-kalimatu n-nasihati kalimatun ... hiyazatu l-hazzi ...)', 2.2),
    zone(73, 0.620, 0.725, 0.04, 0.99, 'Y2. p73 encadre : dernieres lignes (fin aya 2 + ref 78 + aya 3 + ref 19)', 2.4),
    zone(73, 0.345, 0.430, 0.04, 0.99, 'Y3. p73 TAQWIM item 1', 2.4),
]

imgs = CROPS
total_h = sum(c.height + 46 for _, c in imgs)
comp = Image.new('RGB', (1770, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1769, y+40], fill=(230, 240, 230))
    d.text((14, y+10), label, fill=(20, 20, 20))
    y += 44
    comp.paste(c, ((1770-c.width)//2, y))
    y += c.height + 2

comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
