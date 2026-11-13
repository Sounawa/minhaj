#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — zooms 600 dpi pour adjudication leçon 10 hadith-5ep (pp. 60-63)
# 4 composites : points contestés lettre à lettre.
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-10/zooms'
os.makedirs(OUT, exist_ok=True)

def band600(pg, y0, y1, x0=0.0, x1=1.0):
    """Render one page at 600 dpi and crop the fractional band, return PIL image resized to 2200 wide."""
    png = f'{OUT}/p600-{pg}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(pg), '-l', str(pg),
                        SRC, f'{OUT}/tmp600-{pg}'], check=True)
        os.replace(f'{OUT}/tmp600-{pg}-{pg:03d}.png', png)
    im = Image.open(png)
    w, h = im.size
    crop = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    nw = 2200
    nh = int(crop.size[1] * nw / crop.size[0])
    return crop.resize((nw, nh), Image.LANCZOS)

def composite(name, bands):
    W = 2200
    total_h = sum(b.size[1] for b in bands) + 12 * (len(bands) - 1)
    canvas = Image.new('RGB', (W, total_h), (200, 200, 200))
    y = 0
    for b in bands:
        canvas.paste(b, (0, y))
        y += b.size[1] + 12
    canvas.save(f'{OUT}/{name}.png')
    print(name, canvas.size)

# Z1 — p60 تمهيد (les mots أَذِنَ / أَشْبَهَ) + p61 رواية (مَعَالِيَة + date)
composite('z1-tamhid-rawi', [
    band600(60, 0.435, 0.525),          # paragraphe تمهيد lignes
    band600(61, 0.205, 0.345),          # tarjamat ar-rawi lignes 3-6
])

# Z2 — p62 item 1 : āyas الحلال الطيب + refs
composite('z2-ayas-item1', [
    band600(62, 0.285, 0.40),
])

# Z3 — p62 haut : item 2 āyas + refs + prose ; item 3 : النمور + إجماع
composite('z3-item2-item3', [
    band600(62, 0.545, 0.665),
    band600(62, 0.665, 0.905),
])

# Z4 — p63 : 3e قيل + نَقُصُ/يَقُودُ + āya تركوا/تركنوا + التزينة
composite('z4-p63-points', [
    band600(63, 0.245, 0.335),          # 3e qila
    band600(63, 0.405, 0.505),          # bullet 2
    band600(63, 0.735, 0.835),          # aya + ghaliban
    band600(63, 0.875, 1.000),          # wama yustafad
])

print('OK zooms h5-10')
