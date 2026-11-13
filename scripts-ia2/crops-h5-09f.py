#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — zoom ×7 segments āyas استثمار (p.59)
from PIL import Image

TMP = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-09'
src = Image.open(f'{TMP}/plates/hi-59.png')

for (x1, y1, x2, y2, name, fac) in [
    (1200, 1800, 2655, 1975, 'istith-aya1-debut', 7.0),   # début āya 1 (droite)
    (100, 1800, 1450, 1975, 'istith-aya1-fin', 7.0),      # fin āya 1 (gauche)
    (1500, 1965, 2655, 2140, 'istith-aya2-debut', 7.0),   # début āya 2 (droite)
    (100, 1965, 1650, 2140, 'istith-aya2-fin', 7.0),      # fin āya 2 (gauche)
]:
    im = src.crop((x1, y1, x2, y2))
    im = im.resize((int(im.width * fac), int(im.height * fac)), Image.LANCZOS)
    im.save(f'{TMP}/crops/{name}.png')
    print(name, im.size)
print('OK')
