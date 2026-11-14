#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — zooms finaux (passe 4) : 3 mots contestés
from PIL import Image
import os

R600 = '/home/z/my-project/scripts-ia2/tmp/h5-16/r600'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'

Z = [
    # référence sous encadré hadith p.88 (f 0.855-0.905)
    (88, 0.852, 0.908, 0.10, 0.95, 'f-ref', 5.0),
    # mot «و...ه» ligne «...إلى ما لا تشك فيه منها» p.90 (f 0.528-0.558, droite)
    (90, 0.526, 0.560, 0.40, 1.00, 'f-watajjah', 6.0),
    # citation «تركتكم على ...» p.88 (f 0.450-0.482, droite)
    (88, 0.449, 0.484, 0.42, 1.00, 'f-quote', 5.0),
]

for (page, y0, y1, x0, x1, tag, up) in Z:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    crop = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    if crop.width * up > 3600:
        up = 3600 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=92)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
