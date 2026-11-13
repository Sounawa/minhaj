#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — zoom ×6 sur l'ouverture de l'āya p.58 (moitié droite de L1) + réf zoomée
from PIL import Image

TMP = '/home/z/my-project/scripts-ia2/tmp/h5-09'
src = Image.open(f'{TMP}/plates/hi-58.png')

for (x1, y1, x2, y2, name, fac) in [
    (1150, 2810, 2655, 3000, 'aya-p58-L1-droite', 5.0),
    (100, 2950, 1500, 3140, 'aya-p58-ref', 5.0),
]:
    im = src.crop((x1, y1, x2, y2))
    im = im.resize((int(im.width * fac), int(im.height * fac)), Image.LANCZOS)
    im.save(f'{TMP}/crops/{name}.png')
    print(name, im.size)
print('OK')
