#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — planche d'adjudication finale leçon 12 : 7 microcrops empilés
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-12'
OUT = f'{BASE}/zooms/comp-P-final.png'

# (page, y0, y1, x0, x1, label) — fractions de la planche 150 dpi
CROPS = [
    (69, 0.475, 0.735, 0.05, 0.98, 'p69 TAMHID complet'),
    (70, 0.185, 0.405, 0.05, 0.98, 'p70 BIO tamim (l.1-4)'),
    (71, 0.375, 0.460, 0.05, 0.98, 'p71 lomomiha wa-samwiha'),
    (71, 0.625, 0.725, 0.05, 0.98, 'p71 nasyha lillah (agtimar?)'),
    (72, 0.865, 0.935, 0.05, 0.98, 'p72 fin bloc 5 (wa-yakrah...)'),
    (73, 0.605, 0.690, 0.05, 0.98, 'p73 AYA 1 + ref'),
    (73, 0.735, 0.825, 0.05, 0.98, 'p73 AYA 3 + ref'),
]

imgs = []
for pg, y0, y1, x0, x1, label in CROPS:
    im = Image.open(f'{BASE}/p-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = 1500
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    imgs.append((label, c))

total_h = sum(c.height + 46 for _, c in imgs)
comp = Image.new('RGB', (1520, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1519, y+40], fill=(230, 240, 230))
    d.text((14, y+10), label, fill=(20, 20, 20))
    y += 44
    comp.paste(c, ((1520-c.width)//2, y))
    y += c.height + 2

comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
