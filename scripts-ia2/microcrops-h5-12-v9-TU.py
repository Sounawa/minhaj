#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — planches d'adjudication finales T et U (7 micro-zones)
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-12'

def build(crops, out):
    imgs = []
    for pg, y0, y1, x0, x1, label in crops:
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
    comp.save(out)
    print('OK', out, comp.size, os.path.getsize(out)//1024, 'Ko')

build([
    (70, 0.550, 0.905, 0.05, 0.98, 'T1. p70 0.55-0.90 : sharh a-imma + madamin + tahlil awwalan (luga/istilah/nasih)'),
    (71, 0.220, 0.325, 0.05, 0.98, 'T2. p71 0.22-0.32 : thaniya : tatajalla + (hiyazat al-hazz?) + wa-hiya min wajiz'),
    (71, 0.575, 0.645, 0.05, 0.98, 'T3. p71 0.575-0.645 : (an jami an-naqais?) wa-taatihi wa-jtinab'),
], f'{BASE}/zooms/comp-T.png')

build([
    (72, 0.130, 0.425, 0.05, 0.98, 'U1. p72 0.13-0.42 : fin bloc 2 (tahdhir/tahbib?) + bloc 3 (tasdiq... nusrat... taadub/tadabbur?)'),
    (72, 0.585, 0.700, 0.05, 0.98, 'U2. p72 0.585-0.70 : bloc 4 (tanbihuhum/tandiyuhum?)'),
    (73, 0.693, 0.758, 0.05, 0.98, 'U3. p73 0.693-0.758 : ligne apres aya 3 (fi-l-ayat as-sabiga...)'),
    (73, 0.790, 0.870, 0.05, 0.98, 'U4. p73 0.79-0.87 : al-i dad al-qabli items 1-2'),
], f'{BASE}/zooms/comp-U.png')
