#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-14 — planche W (dernière) : micro-zones restées contestées, crops 600 dpi précis
from PIL import Image, ImageDraw
import os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-12'
Z = f'{BASE}/zooms'
OUT = f'{Z}/comp-W-final.png'

def zone(pg, y0, y1, x0, x1, label, scale=1.6):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1700:
        tw = 1700
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(69, 0.275, 0.435, 0.05, 0.98, 'W1. p69 obj1+obj3 (wa-manzilataha? / umaththila as-sunnata am amtathila sunnatahu?)'),
    zone(69, 0.485, 0.575, 0.05, 0.98, 'W2. p69 tamhid l.2 (ma-anna ma-naha? akbar min dhalik idh ... hatta t-tanzima/t-tadamina d-dina kullahu)'),
    zone(70, 0.145, 0.245, 0.05, 0.98, 'W3. p70 bio l.1-2 (ad-Dari al-lakhmi? al-himyari? asraja s-suruja? as-siraja?)'),
    zone(70, 0.520, 0.680, 0.05, 0.98, 'W4. p70 SHARH glossa complete (a-immatu l-muslimina...)'),
    zone(71, 0.225, 0.345, 0.05, 0.98, 'W5. p71 fa-kalimatun n-nasihatu kalimatun ... hiyazatu l-hazzi l-l-mansukhi wa-iradatu ... l-khayri'),
    zone(72, 0.145, 0.290, 0.05, 0.98, 'W6. p72 bloc3 (ihya-i sunnatihi? at-tafaqquhi fi ma-aniha? wa-d-dabbi anha? + tahbib/tahdhir?)'),
    zone(72, 0.575, 0.660, 0.05, 0.98, 'W7. p72 bloc4 l.1 (wa-tanbihihim? mu-awanatihim?)'),
    zone(72, 0.690, 0.800, 0.05, 0.98, 'W8. p72 bloc5 (takunu nasihatuna? wa-daf-i l-adha? al-madarri?)'),
    zone(73, 0.085, 0.300, 0.05, 0.98, 'W9. p73 YUSTAFAD 3 items complets'),
    zone(73, 0.330, 0.480, 0.05, 0.98, 'W10. p73 TAQWIM item 1 + item 2'),
    zone(73, 0.615, 0.720, 0.05, 0.98, 'W11. p73 encadre AYA 3 seule ligne par ligne (debut exact?)'),
    zone(73, 0.880, 0.985, 0.05, 0.98, 'W12. p72-73 I-DAD item 2 (ala/ani yasri l-islami)'),
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
# version scindee en 2 pour le VLM
h = comp.height
comp.crop((0, 0, 1720, h//2)).save(f'{Z}/comp-Wa.png')
comp.crop((0, h//2, 1720, h)).save(f'{Z}/comp-Wb.png')
print('Wa/Wb OK')
