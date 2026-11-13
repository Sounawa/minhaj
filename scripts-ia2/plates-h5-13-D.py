#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-15 — planche D (ultime) : fenêtres corrigées ×2.6, sans recouvrement
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-13'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-D13.png'

def zone(pg, y0, y1, x0, x1, label, scale=2.6):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1780:
        tw = 1780
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(77, 0.135, 0.30, 0.03, 0.99, 'D1. p77 refs [at-Taghabun: ?] et [al-Hajj: ?] — chiffres arabes EXACTS'),
    zone(77, 0.55, 0.78, 0.03, 0.99, 'D2. p77 note grammaticale complete (bi-dammi ? / ma-tufun ?ala kathrati / ablugh / nasha-a)'),
    zone(78, 0.085, 0.21, 0.03, 0.99, 'D3. p78 ala wajhi (l-amali? at-taallumi?) mimma yuhtaju ilayhi'),
    zone(78, 0.305, 0.475, 0.03, 0.99, 'D4. p78 li-anna kathrata s-su-ali rubbama ... — phrase complete'),
    zone(79, 0.145, 0.325, 0.03, 0.99, 'D5. p79 taqwim items 2-3 (haddara? nahaw? rasulu ?llahi?)'),
    zone(78, 0.865, 0.99, 0.03, 0.99, 'D6. p78 yustafad item 2 (hadyi ?al-fatwa/ ?al-islami at-taysira)'),
    zone(75, 0.285, 0.385, 0.03, 0.99, 'D7. p75 annee deces Abū Hurayra (sanata ? aw ? wa-khamshina)'),
    zone(75, 0.565, 0.80, 0.03, 0.99, 'D8. p75 istikhlas al-madamin items 1-2 (verbes exacts)'),
]

imgs = CROPS
total_h = sum(c.height + 50 for _, c in imgs)
comp = Image.new('RGB', (1800, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1799, y+44], fill=(225, 235, 225))
    d.text((14, y+12), label, fill=(20, 20, 20))
    y += 48
    comp.paste(c, ((1800-c.width)//2, y))
    y += c.height + 4

comp.save(OUT)
print('OK', OUT, comp.size, os.path.getsize(OUT)//1024, 'Ko')
