#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — zooms serrés ×4 pour arbitrages finaux leçon 16
from PIL import Image
import os

R600 = '/home/z/my-project/scripts-ia2/tmp/h5-16/r600'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'

# (page, y0, y1, tag) — fractions de hauteur, pleine largeur, upscale ×4 borné 3400px
ZOOMS = [
    (88, 0.322, 0.355, 'z-obj3'),        # verbe objectif 3 + عن + sing/pluriel
    (88, 0.448, 0.490, 'z-quote'),       # «قد تركتكم على البيضاء...» exact
    (88, 0.488, 0.550, 'z-tamhid2'),     # يلتبس/يختلط الحكم + ولا أن الشيء أم لا
    (88, 0.730, 0.850, 'z-hadithref'),   # référence sous l'encadré hadith
    (89, 0.782, 0.830, 'z-halalbayyin'), # الحلال اليقين/البين ما علمت ملكه
    (89, 0.858, 0.900, 'z-shubha-def'),  # الشبهة: ما لا يدري أهو لك أو لغيرك
    (90, 0.078, 0.122, 'z-ijtinab'),     # فالورع اجتنابها/اجتنابه + ref عمدة القاري
    (90, 0.203, 0.252, 'z-khafaiaha'),   # للتباسها وخفائها/حفاظها + ذلك أن
    (90, 0.475, 0.522, 'z-ay-natak'),    # أي: نترك ما نشك في حرمته + ونجت/ننتقي
    (90, 0.592, 0.640, 'z-tirmidhi2'),   # حتى يتروك + مخافة لما به بأس + ref
    (91, 0.383, 0.422, 'z-mayufa2'),     # لكنها لم تتحقق + لم تغير حكمها
    (91, 0.498, 0.545, 'z-bukhari2'),    # شكا إلى النبي الرجل الذي يجد
    (92, 0.588, 0.628, 'z-tafar3-2'),    # أستخرج/متفرع الأنواع الواردة
    (92, 0.745, 0.928, 'z-idad2'),       # الإعداد القبلي complet
]

for (page, y0, y1, tag) in ZOOMS:
    png = f'{R600}/p{page}.png'
    im = Image.open(png)
    W, H = im.size
    crop = im.crop((0, int(y0*H), W, int(y1*H)))
    up = 4.0
    if crop.width * up > 3400:
        up = 3400 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=90)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
