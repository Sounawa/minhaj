#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — planche d'adjudication v6 : zones réajustées + ultra-zooms mots fins
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
OUT = f'{BASE}/zooms/comp-Q-v6.png'

# (page, y0, y1, x0, x1, label) — fractions
CROPS = [
    (69, 0.395, 0.495, 0.05, 0.98, 'A. p69 tamhid DEBUT (yazun... tantazim)'),
    (70, 0.195, 0.255, 0.03, 0.45, 'B. p70 (ma-akhihi naim/tuaym fa-aslama sanata tis) x1.6'),
    (70, 0.230, 0.310, 0.15, 0.80, 'C. p70 (wa-az bi-qasas as-sabiqin) (wa-sanaa minbaran...) x1.6'),
    (71, 0.310, 0.390, 0.05, 0.98, 'D. p71 li-omumiha wa-samuha wa-fa-d-dinu nashun kulluh'),
    (71, 0.560, 0.640, 0.05, 0.98, 'E. p71 (al-igtimar/itiraf bi-nimatihi wa-shukr alayhi)'),
    (72, 0.855, 0.915, 0.02, 0.50, 'F. p72 (wa-yuhatthu/yahtami ala at-takhalluq?) x1.8'),
    (73, 0.540, 0.690, 0.05, 0.98, 'G. p73 bloc ayas 1-3 complet'),
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
