#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-14 — planche d'adjudication finale V : zones restées contestées après P/Q/T/R/N/O
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-V-final.png'

def zone(pg, y0, y1, x0, x1, label, src='big'):
    """crop fraction of the 600dpi render (big-*) or 150dpi page (p-*)"""
    if src == 'big':
        im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    else:
        im = Image.open(f'{BASE}/p-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = 1560
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(69, 0.155, 0.44, 0.03, 0.98, 'V1. p69 AHDAF (3 objectifs, mot a trancher: wa-manzilataha? + atamaththala sunnatahu?)'),
    zone(69, 0.70, 0.99, 0.03, 0.98, 'V2. p69 HADITH box complet + question'),
    zone(70, 0.155, 0.27, 0.03, 0.98, 'V3. p70 BIO l.1-3 (nuaym? sanata tis-a? banu d-dari?)'),
    zone(70, 0.26, 0.36, 0.03, 0.98, 'V4. p70 l.4-5 (qassa... bad-ahu/baynahu? sana-a minbaran?)'),
    zone(70, 0.36, 0.52, 0.03, 0.98, 'V5. p70 SHARH glossa + istikhlas items'),
    zone(71, 0.28, 0.47, 0.03, 0.98, 'V6. p71 kalima jamiaa... hiyazat al-hazzi... (l.3-6 du bloc thaniya)'),
    zone(72, 0.885, 1.00, 0.03, 0.98, 'V7. p72 fin bloc 5 (yuhibbuhum/yahutthuhum ala at-takhalluqi?)'),
    zone(73, 0.00, 0.09, 0.03, 0.98, 'V8. p73 debut (bi-kulli ma sabaqa...)'),
    zone(73, 0.41, 0.53, 0.03, 0.98, 'V9. p73 YUSTAFAD items (bayana? / wa-taqtadi?)'),
    zone(73, 0.50, 0.75, 0.03, 0.98, 'V10. p73 ENCADRE ISTITHMAR complet (3 ayas + refs + ligne afhem)'),
    zone(73, 0.75, 0.99, 0.03, 0.98, 'V11. p73 TAQWIM items 1-2 + I-DAD QABLI items 1-2'),
]

imgs = CROPS
total_h = sum(c.height + 46 for _, c in imgs)
comp = Image.new('RGB', (1580, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1579, y+40], fill=(230, 240, 230))
    d.text((14, y+10), label, fill=(20, 20, 20))
    y += 44
    comp.paste(c, ((1580-c.width)//2, y))
    y += c.height + 2

comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
