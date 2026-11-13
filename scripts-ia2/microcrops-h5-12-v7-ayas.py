#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — dernier microcrop : ayas 1 et 3 du istithmar (x1.5)
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
OUT = f'{BASE}/zooms/comp-R-ayas.png'

CROPS = [
    (73, 0.545, 0.620, 0.02, 0.98, 'AYA 1 + ref (x1.5)'),
    (73, 0.635, 0.695, 0.02, 0.98, 'AYA 3 + ref (x1.5)'),
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
