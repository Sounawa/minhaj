#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — anatomie pixel : détection de points diacritiques sur les mots disputés.
# Méthode : composantes connexes du crop 1200 dpi binarisé ; un « point » = petite
# composante isolée AU-DESSUS du corps du mot. Comparaison ص/ض (إصلاح), د/ذ (البذل), ن/ذ (نفرة).
import numpy as np
from PIL import Image, ImageOps
from scipy import ndimage

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
S = 1200 / 72.0

def anatomy(pg, y0, y1, x0, x1, tag, dot_zone_hint=None):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = ImageOps.autocontrast(c)
    a = np.array(c)
    H, W = a.shape
    # binarisation : encre sombre
    thr = a.mean() - 1.2 * a.std()
    ink = a < max(thr, 110)
    lab, n = ndimage.label(ink)
    comps = []
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if len(ys) < 4:
            continue
        comps.append({'i': i, 'n': len(ys), 'x0': xs.min(), 'x1': xs.max(),
                      'y0': ys.min(), 'y1': ys.max()})
    # corps du mot = composantes larges ; points = petites composantes HAUTES
    if not comps:
        print(f'{tag}: aucune composante')
        return
    maxh = max(cc['y1']-cc['y0'] for cc in comps)
    print(f'===== {tag} (crop {W}x{H}px, {n} composantes) =====')
    for cc in sorted(comps, key=lambda z: -z['x0']):  # droite→gauche
        w = cc['x1']-cc['x0']+1
        h = cc['y1']-cc['y0']+1
        kind = 'CORPS' if h > 0.45*maxh else ('POINT' if cc['n'] <= 260 else 'glyphe')
        pos = 'DESSUS' if cc['y1'] < 0.45*maxh else ('DESSOUS' if cc['y0'] > 0.72*maxh else 'milieu/baseline')
        print(f"  x[{cc['x0']:>4}-{cc['x1']:>4}] y[{cc['y0']:>3}-{cc['y1']:>3}] {cc['n']:>4}px {kind:<7} {pos}")

# 1. إصلاح القلب (p39 y446-472, bande «أهمية إصلاح القلب بأنواع البر»)
# mot إصلاح ≈ x330-470 d'après zoom ; re-crop serré
anatomy(39, 448, 472, 340, 480, 'islah-1 (أهمية إصلاح القلب)')
anatomy(39, 448, 472, 100, 260, 'islah-2 (لإصلاح حركات الجوارح)')
# 2. البذل/البدل في الإحسان (p38 y409-435)
anatomy(38, 408, 436, 340, 480, 'badl (البذل في الإحسان)')
# 3. يورث نفرة/ذفرة/زفرة (p38 y618-652, mot ≈ x296-345)
anatomy(38, 620, 650, 290, 350, 'nafra (يورث X في القلب)')
# 4. قابل كل بينهما (p38 y705-732, gap x434-465)
anatomy(38, 705, 735, 425, 470, 'qabil (mot après قابل)')
# 5. المعدود (p37 y140-165, x437-462)
anatomy(37, 140, 165, 430, 470, 'madud')
# 6. يكنى أبا شداد (p37 y228-252)
anatomy(37, 230, 252, 290, 420, 'kunya (يكنى أبا شداد)')
# 7. خزيمة (p37 y230-252)
anatomy(37, 230, 252, 400, 480, 'khuzayma (أسد بن خزيمة)')
# 8. citation head كالبر/قال البر (p38 y76-106)
anatomy(38, 76, 108, 380, 565, 'citation-head')
# 9. تغذية (p38 y76-106)
anatomy(38, 76, 108, 240, 400, 'taghdiya')
# 10. المحاولة/المحاورة (p38 y381-408)
anatomy(38, 381, 408, 200, 340, 'muhawara')
# 11. وله أحاديث (p37 y254-280)
anatomy(37, 256, 278, 370, 520, 'lahu-ahadith')
# 12. p37 tail تزكية النفس zone (y698-732)
anatomy(37, 698, 732, 60, 380, 'tahlil-tail')
