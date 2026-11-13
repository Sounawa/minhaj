#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — ultra-zoom āya p.58 (2 lignes séparées) + réf
from PIL import Image

TMP = '/home/z/my-project/scripts-ia2/tmp/h5-09'
src = Image.open(f'{TMP}/plates/hi-58.png')

for (x1, y1, x2, y2, name, fac) in [
    (0, 2820, 2655, 2990, 'aya-p58-L1', 4.0),
    (0, 2960, 2655, 3130, 'aya-p58-L2', 4.0),
]:
    im = src.crop((x1, y1, x2, y2))
    im = im.resize((int(im.width * fac), int(im.height * fac)), Image.LANCZOS)
    im.save(f'{TMP}/crops/{name}.png')
    print(name, im.size)
print('OK')
