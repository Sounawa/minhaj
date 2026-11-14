#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — microcrops adjudication leçon 16 (zones précises, zoom ×2.2)
from PIL import Image
import os

R600 = '/home/z/my-project/scripts-ia2/tmp/h5-16/r600'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'

# (page, y0, y1, x0, x1, tag, upscale) — fractions de hauteur/largeur
CROPS = [
    (88, 0.318, 0.358, 0.00, 1.00, 'obj3',      2.2),  # أن تعد ڪن الشبهات في عبادتي ومعامتي
    (88, 0.408, 0.500, 0.00, 1.00, 'tamhid1',   2.0),  # محجة بيضاء + «قد تركتكم على البيضاء...» + ref
    (88, 0.482, 0.600, 0.00, 1.00, 'tamhid2',   2.0),  # لكنه قد تعرض أمور ملتبسة...ولا أن الشيء من الواجبات أم لا؟
    (88, 0.600, 0.830, 0.00, 1.00, 'hadithbox', 1.9),  # encadré hadith + référence
    (89, 0.240, 0.320, 0.00, 1.00, 'rawi2',     2.2),  # ومات سنة أربع وأربعينه وقيل غير ذلك
    (89, 0.410, 0.525, 0.00, 1.00, 'sharh',     2.0),  # gloses سبط/دع/يريبك
    (89, 0.775, 0.915, 0.00, 1.00, 'awwalan',   2.0),  # الحلال اليقين/البين + الحرام البين + الشبهة ما لا...
    (90, 0.060, 0.130, 0.00, 1.00, 'warajtinib',2.2),  # فالورع اجتنابها + [عمدة القاري للعيني بتصرف]
    (90, 0.180, 0.260, 0.00, 1.00, 'thaniya',   2.0),  # حث النبي...للتباسها وخفائها/حفاظها
    (90, 0.470, 0.550, 0.00, 1.00, 'ay',        2.0),  # أي: نترك ما نشك في حرمته + و...؟ إلى ما لا تشك فيه
    (90, 0.550, 0.650, 0.00, 1.00, 'tirmidhi',  2.0),  # لا يبلغ العبد... محافظة/مخافة + ref
    (91, 0.375, 0.470, 0.00, 1.00, 'mayufa',    2.0),  # هناك أمور فيها معنى الشبهة لكنها...لم تغير حكمها
    (91, 0.550, 0.635, 0.00, 1.00, 'wswas',     2.0),  # من كثر شكه... يبني على اليقين ولا يلتفت
    (91, 0.620, 0.750, 0.00, 1.00, 'bukhari',   1.9),  # hadith Bukhari complet + يعتريه الشك كثيرا + ref
    (91, 0.760, 0.875, 0.00, 1.00, 'yustafad',  2.0),  # أن الحلال المحض... تسكن إليه النفس ويطمئن به القلب
    (92, 0.180, 0.270, 0.00, 1.00, 'taqwim',    2.2),  # 1. أعرف الشبهات... + ligne mystère + 2. أذكر
    (92, 0.390, 0.435, 0.00, 1.00, 'wara3-1',   2.4),  # ورع الصديقين: ترك ما لا يتناول بغير نية القوة
    (92, 0.585, 0.640, 0.00, 1.00, 'tafar3',    2.2),  # - متفرع؟ الأوجه؟ الواردة في النص مع بيان ما يعد
    (92, 0.740, 0.930, 0.00, 1.00, 'idad',      2.0),  # الإعداد القبلي complet
]

for (page, y0, y1, x0, x1, tag, up) in CROPS:
    png = f'{R600}/p{page}.png'
    im = Image.open(png)
    W, H = im.size
    crop = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    if crop.width * up > 3400:
        up = 3400 / crop.width
    crop = crop.resize((int(crop.width*up), int(crop.height*up)), Image.LANCZOS)
    out = f'{OUT}/mc-{tag}-p{page}.jpg'
    crop.convert('RGB').save(out, 'JPEG', quality=88)
    print(out, crop.size, os.path.getsize(out)//1024, 'Ko')
print('OK')
