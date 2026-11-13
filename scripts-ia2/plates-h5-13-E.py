#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-15 — planche E (micro-zooms ×3.2, dernière)
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-13'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-E13.png'

def zone(pg, y0, y1, x0, x1, label, scale=3.2):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1900:
        tw = 1900
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(78, 0.875, 0.985, 0.03, 0.99, 'E1. p78 yustafad item 2 (an min hadyi ?al-? at-taysira fi umuri d-dini wa-d-dunya)'),
    zone(75, 0.290, 0.380, 0.03, 0.99, 'E2. p75 annee deces (tuwaffiya biha sanata ? ... li-l-hijrati an ? ... sana)'),
    zone(75, 0.570, 0.790, 0.03, 0.99, 'E3. p75 istikhlas al-madamin items 1-2 complets'),
    zone(78, 0.090, 0.170, 0.03, 0.99, 'E4. p78 (ala wajhi l-amali? at-taallumi?) mimma yuhtaju ilayhi min umuri d-dini'),
    zone(77, 0.590, 0.780, 0.03, 0.99, 'E5. p77 fin de la note (ay: ahlakahum kathratu ... wa-ahlakahumu ?htilafuhum wa-huwa ablugh ...)'),
]

imgs = CROPS
total_h = sum(c.height + 50 for _, c in imgs)
comp = Image.new('RGB', (1920, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1919, y+44], fill=(225, 235, 225))
    d.text((14, y+12), label, fill=(20, 20, 20))
    y += 48
    comp.paste(c, ((1920-c.width)//2, y))
    y += c.height + 4

comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
