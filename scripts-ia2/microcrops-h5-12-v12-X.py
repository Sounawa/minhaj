#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-14 — planche X (ultime) : 6 micro-zones restantes, crops 600 dpi ×2
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-X-final.png'

def zone(pg, y0, y1, x0, x1, label, scale=2.0):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1700:
        tw = 1700
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(70, 0.415, 0.535, 0.04, 0.99, 'X1. p70 SHARH glose complete'),
    zone(71, 0.250, 0.370, 0.04, 0.99, 'X2. p71 fa-kalimatu n-nasihatu kalimatun ... hiyazatu ... wa-iradatu ... l-khayri lahu'),
    zone(72, 0.520, 0.600, 0.04, 0.99, 'X3. p72 bloc4 ligne 1 (mu-awanatihim ala l-haqqi wa-tanbihihim)'),
    zone(72, 0.640, 0.730, 0.04, 0.99, 'X4. p72 bloc5 debut (aammatu l-muslimina... takunu nasihatUNA/nasihatUHUM bikhafdi l-janahi)'),
    zone(73, 0.335, 0.425, 0.04, 0.99, 'X5. p73 TAQWIM item 1 exact'),
    zone(73, 0.600, 0.715, 0.04, 0.99, 'X6. p73 AYA 3 lignes exactes'),
]

imgs = CROPS
total_h = sum(c.height + 46 for _, c in imgs)
comp = Image.new('RGB', (1720, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1719, y+40], fill=(230, 240, 230))
    d.text((14, y+10), label, fill=(20, 20, 20))
    y += 44
    comp.paste(c, ((1720-c.width)//2, y))
    y += c.height + 2

comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
