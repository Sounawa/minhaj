#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-23 — 2e vague de recadrages n-série (n11-n15) : correction des zones manquées
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-20'
R600 = f'{OUT}/r600'

CROPS = [
    # n11 — p.112 : أَذْكُرْ ثَلَاثًا/ثَلَاثَةً (début DROITE de la ligne 2 du التحليل Q1)
    (112, 0.655, 0.708, 0.58, 0.95, 3.5, 'n11'),
    # n12 — p.112 : verbe après أَنْ (début DROITE de la ligne 2 du cadre خديجة)
    (112, 0.072, 0.148, 0.60, 1.00, 3.0, 'n12'),
    # n13 — p.112 : وَتُكْسِبُ/وَتَكْسِبُ الْمَعْدُومَ (ligne des verbes de la citation)
    (112, 0.255, 0.318, 0.30, 0.68, 3.5, 'n13'),
    # n14 — p.112 : قَبْلَ النُّبُوَّةِ (mot entre بِهَا et النُّبُوَّةِ)
    (112, 0.242, 0.300, 0.48, 0.72, 4.0, 'n14'),
    # n15 — p.112 : items du glossaire الفهم Q2 (لتصل الرحم – تحمل الكل – تكسب المعدوم – تقرى الضيف)
    (112, 0.468, 0.525, 0.25, 0.68, 3.5, 'n15'),
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
print('2e VAGUE N TERMINÉE')
