#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-23 — recadrages d'adjudication NARROWS (n-série) leçon 20 hadith-5ep — après 2e recyclage bac.
# Cibles : les 9 conflits résiduels (étoits en x, ×2.5-3.5) — méthode leçon 19 (anti-sous-échantillonnage VLM).
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-20'
R600 = f'{OUT}/r600'

# (page, y0, y1, x0, x1, upscale, tag)
CROPS = [
    # N1 — p.111 : الدَّالَّةِ / اللَّهُ après عَلَامَاتِ الْإِيمَانِ (ligne 2e §, y≈0.718-0.755)
    #    2 tuiles étroites qui couvrent x 0.36-0.72
    (111, 0.713, 0.758, 0.36, 0.56, 3.0, 'n01'),  # tuile droite : عَلَامَاتِ الْإِيمَانِ + début [X]
    (111, 0.713, 0.758, 0.50, 0.72, 3.0, 'n02'),  # tuile gauche : [X] + عَلَى كَمَالِهِ
    # N2 — p.112 : verbe après أَنْ (تُخَفِّفَ/تَخْفَ) — ligne « أَرَادَتْ أَنْ [V1] عَنِ النَّبِيِّ »
    (112, 0.082, 0.142, 0.38, 0.98, 2.5, 'n03'),  # ligne complète du verbe, tuile droite-centre
    # N3 — p.112 : وَتُكْسِبُ/وَتَكْسِبُ الْمَعْدُومَ dans la citation خديجة
    (112, 0.278, 0.322, 0.34, 0.66, 3.0, 'n04'),
    # N4 — p.111 : إِخْوَةً/إِخْوَانًا après اعْتَبَرَ جَمِيعَ النَّاسِ (fin gauche de la ligne بل ذهب)
    (111, 0.570, 0.618, 0.08, 0.42, 3.0, 'n05'),
    # N5 — p.113 : حَثَّ/حَدَّثَ premier mot du التطبيق Q1 (droite)
    (113, 0.242, 0.288, 0.62, 0.98, 3.5, 'n06'),
    # N6 — p.112 : أَذْكُرْ ثَلَاثًا/ثَلَاثَةً مِنْ (fin gauche ligne التحليل Q1)
    (112, 0.660, 0.705, 0.04, 0.38, 3.0, 'n07'),
    # N7 — p.113 : كَيْفَ أُقْنِعُ الْمُحْسِنَ إِلَى مِثْلِ هَؤُلَاءِ
    (113, 0.288, 0.338, 0.30, 0.72, 3.0, 'n08'),
    # N8 — p.113 : بَلْ وَلَا يَقْطَعَ إِحْسَانَهُ إِلَيْهِمْ؟ (ligne suivante)
    (113, 0.325, 0.378, 0.20, 0.80, 2.5, 'n09'),
    # N9 — p.112 : قَبْلَ النُّبُوَّةِ (w12 a lu «فِيلَ» — à confirmer)
    (112, 0.192, 0.268, 0.28, 0.78, 2.5, 'n10'),
]

for page, y0, y1, x0, x1, up, tag in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    c = im.crop(box)
    # upscale LANCZOS
    c2 = c.resize((int(c.width * up), int(c.height * up)), Image.LANCZOS)
    out = f'{OUT}/z20-{tag}.png'
    c2.save(out)
    print(f'z20-{tag} p{page} y[{y0:.3f}-{y1:.3f}] x[{x0:.2f}-{x1:.2f}] base={c.width}x{c.height} -> {c2.width}x{c2.height}px (x{up})')
print('N-CROPS TERMINÉS')
