#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-15 — planche C (ultime) : 9 micro-zones restantes de la leçon 13, 600 dpi ×2.2
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-13'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-C13.png'

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
    zone(75, 0.285, 0.40, 0.03, 0.99, 'C1. p75 ligne deces (sanata ? wa-khamshina li-l-hijrati an ? wa-sabinata)'),
    zone(75, 0.40, 0.60, 0.03, 0.99, 'C2. p75 SHARH glose fajtanibuhu + items ISTIKHLAS'),
    zone(76, 0.40, 0.56, 0.03, 0.99, 'C3. p76 wa-huwa (maqdurun? wasi-un?) li-kulli ahadin'),
    zone(76, 0.565, 0.71, 0.03, 0.99, 'C4. p76 fa-yusalli / fa-yatammamu bi-ma yastatiu minha'),
    zone(77, 0.05, 0.175, 0.03, 0.99, 'C5. p77 les 3 REFERENCES imprimees (al-Baqara: ? / at-Taghabun: ? / al-Hajj: ?)'),
    zone(77, 0.40, 0.75, 0.03, 0.99, 'C6. p77 ayat Al Imran + note grammaticale (bi-dammi ?al-hai/al-fa / ma-tufun ala kathratu)'),
    zone(78, 0.075, 0.19, 0.03, 0.99, 'C7. p78 (ala wajhi l-amali? at-taallumi?) mimma yuhtaju ilayhi'),
    zone(78, 0.29, 0.44, 0.03, 0.99, 'C8. p78 li-anna kathrata s-su-ali rubbama ... (phrase complete)'),
    zone(79, 0.04, 0.175, 0.03, 0.99, 'C9. p79 TAQWIM item 1 (u-dakkiru? adhkuru?) + item 3 (haddara?)'),
    zone(78, 0.855, 0.985, 0.03, 0.99, 'C10. p78 YUSTAFAD item 2 (hadyi ?al-?islami? al-fatwa? at-taysiru)'),
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
# split en 2 pour le VLM
h = comp.height
comp.crop((0, 0, 1770, h//2)).save(f'{Z}/comp-C13-a.png')
comp.crop((0, h//2, 1770, h)).save(f'{Z}/comp-C13-b.png')
print('split OK')
