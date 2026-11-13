#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — microcrop ultime : p70 lignes 4-5 (minbar + abadat + arba'in)
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
OUT = f'{BASE}/zooms/comp-S-minbar.png'

im = Image.open(f'{BASE}/p-070.png')
W, H = im.size
c = im.crop((int(0.02*W), int(0.250*H), int(0.98*W), int(0.325*H)))
tw = 1500
c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)

comp = Image.new('RGB', (1520, c.height + 46), 'white')
d = ImageDraw.Draw(comp)
d.rectangle([0, 0, 1519, 40], fill=(230, 240, 230))
d.text((14, 10), 'p70 l.4-5 : wa-sanaa minbaran ... an-nabiyyi ... ba-adatih ... arba-in (x1.4)', fill=(20, 20, 20))
comp.paste(c, ((1520-c.width)//2, 44))
comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
