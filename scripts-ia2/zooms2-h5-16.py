#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — zooms r3 (recadrage des zones mal couvertes)
from PIL import Image
import os

R600 = '/home/z/my-project/scripts-ia2/tmp/h5-16/r600'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'

# (page, y0, y1, x0, x1, tag, upscale)
Z = [
    (88, 0.446, 0.484, 0.40, 1.00, 'r3-quote-open', 4.0),  # قد تركتكم على المحجة البيضاء (début, droite)
    (88, 0.518, 0.592, 0.00, 1.00, 'r3-tamhid2b',   3.2),  # ولا أن الشيء من الواجبات أم لا... المسمى بالشبهات
    (88, 0.815, 0.955, 0.15, 1.00, 'r3-hadithref',  3.2),  # référence sous encadré hadith
    (89, 0.820, 0.872, 0.00, 1.00, 'r3-halalbayyin',3.5),  # ففي الممتلكات مثلا: الحلال اليقين/البين
    (89, 0.860, 0.902, 0.00, 0.55, 'r3-shubha-end', 4.5),  # الشبهة: ما لا يدري أهو له أم لغيرك (fin de ligne, gauche)
    (90, 0.080, 0.136, 0.00, 1.00, 'r3-ijtinab2',   3.5),  # فالورع اجتنابها/ه + [عمدة القاري]
    (90, 0.482, 0.525, 0.42, 1.00, 'r3-ay1',        4.0),  # أي: نترك/اترك ما نشك/تشك في حرمته (droite)
    (90, 0.518, 0.562, 0.42, 1.00, 'r3-ay2',        4.0),  # ونجت/ننتقل إلى ما لا تشك فيه منها (droite)
    (91, 0.376, 0.442, 0.00, 1.00, 'r3-mayufa3',    3.5),  # لكنها لم تتحقق فيها لذلك لم تغير حكمها
    (91, 0.616, 0.748, 0.00, 1.00, 'r3-bukhari3',   3.0),  # hadith Bukhari complet + ref
    (92, 0.744, 0.798, 0.00, 1.00, 'r3-idad-open',  3.5),  # أحفظ حديث الدرس المقبل و...
]

for (page, y0, y1, x0, x1, tag, up) in Z:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    crop = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    if crop.width * up > 3400:
        up = 3400 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=90)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
