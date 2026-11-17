#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-23 — 3e vague de recadrages n-série (n16-n19)
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-20'
R600 = f'{OUT}/r600'

CROPS = [
    # n16 — p.112 : وَتُقْرِي الضَّيْفَ dans la citation (ligne sous وَتُكْسِبُ الْمَعْدُومَ)
    (112, 0.280, 0.335, 0.52, 0.90, 3.5, 'n16'),
    # n17 — p.112 : قَبْلَ النُّبُوَّةِ (mot entre بِهَا et النُّبُوَّةِ, ligne y≈0.19-0.235)
    (112, 0.183, 0.240, 0.48, 0.76, 4.5, 'n17'),
    # n18 — p.112 : أَذْكُرْ ثَلَاثًا (début DROITE de la 2e ligne التحليل Q1)
    (112, 0.652, 0.712, 0.68, 0.98, 3.5, 'n18'),
    # n19 — p.112 : verbe V1 après أَنْ (début DROITE de la 2e ligne du cadre خديجة)
    (112, 0.070, 0.145, 0.70, 1.00, 3.5, 'n19'),
]

for page, y0, y1, x0, x1, up, tag in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    c = im.crop(box)
    c2 = c.resize((int(c.width * up), int(c.height * up)), Image.LANCZOS)
    out = f'{OUT}/z20-{tag}.png'
    c2.save(out)
    print(f'z20-{tag} p{page} y[{y0:.3f}-{y1:.3f}] x[{x0:.2f}-{x1:.2f}] base={c.width}x{c.height} -> {c2.width}x{c2.height}px (x{up})')
print('3e VAGUE N TERMINÉE')
