#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — ultra-zoom ×5 des āyas du استثمار (p.59) + ligne المعجم
from PIL import Image

TMP = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-09'
src = Image.open(f'{TMP}/plates/hi-59.png')

for (x1, y1, x2, y2, name, fac) in [
    (100, 1800, 2655, 1975, 'istith-aya1', 5.0),
    (100, 1965, 2655, 2140, 'istith-aya2', 5.0),
    (300, 2170, 2450, 2330, 'istith-muajjam', 4.0),
]:
    im = src.crop((x1, y1, x2, y2))
    im = im.resize((int(im.width * fac), int(im.height * fac)), Image.LANCZOS)
    im.save(f'{TMP}/crops/{name}.png')
    print(name, im.size)
print('OK')
