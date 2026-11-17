#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-24 — recadrages LIGNE-ÉTROITS (série m) pour adjudication directe.
# Bandes d'une ou deux lignes, demi-largeur max, pour lisibilité diacritique.
import os
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-21'
R600 = f'{OUT}/r600'

# (page, y0, y1, x0, x1, tag)
CROPS = [
    # p114 — cadre du hadith (texte blanc sur vert, invisible en couche bbox)
    (114, 0.660, 0.800, 0.45, 1.00, 'm01'),  # cadre haut droite (en-tête + sanad)
    (114, 0.660, 0.800, 0.00, 0.58, 'm02'),  # cadre haut gauche
    (114, 0.780, 0.950, 0.45, 1.00, 'm03'),  # cadre bas droite (matn)
    (114, 0.780, 0.950, 0.00, 0.58, 'm04'),  # cadre bas gauche (matn + ref)
    # p114 — تمهيد ligne 3 (la phrase dure)
    (114, 0.520, 0.565, 0.42, 1.00, 'm05'),  # droite : والشر بمثله. ودفاعا لذلك...
    (114, 0.520, 0.565, 0.00, 0.46, 'm06'),  # gauche : ...الغضب يدفع به [X] الوجيعة
    # p114 — ligne des questions (تملك النفس)
    (114, 0.598, 0.672, 0.00, 0.55, 'm07'),
    # p115 — الشرح item1 (أوصني) + item2 (فردد) + item3 (لا تغضب)
    (115, 0.258, 0.312, 0.30, 1.00, 'm08'),  # item1
    (115, 0.312, 0.352, 0.00, 0.60, 'm09'),  # item2 (فردد مرارا)
    (115, 0.352, 0.405, 0.00, 1.00, 'm10'),  # item3 (لا تغضب: ...)
    # p115 — استخلاص Q1 + Q2
    (115, 0.440, 0.535, 0.28, 1.00, 'm11'),
    # p116 — ففيها (ligne dense) 2 moitiés
    (116, 0.080, 0.125, 0.42, 1.00, 'm12'),
    (116, 0.080, 0.125, 0.00, 0.46, 'm13'),
    (116, 0.125, 0.165, 0.00, 0.46, 'm14'),  # suite gauche (الذين ملكوا...)
    # p116 — معنى قوله ... أى لا تستحب داعي الغضب
    (116, 0.262, 0.305, 0.28, 1.00, 'm15'),
    # p116 — عطية hadith : fin (وإنما تطفأ النار بالماء فإذا غضب أحدكم فلي...)
    (116, 0.598, 0.665, 0.00, 1.00, 'm16'),
    # p116 — لهذا يخرج... وينتهك الحدود و[البعضاء؟]
    (116, 0.660, 0.745, 0.00, 1.00, 'm17'),
    # p116 — فالشيطان هو الذي زين له... من أقوى الحيل لدفع كيده
    (116, 0.752, 0.855, 0.00, 1.00, 'm18'),
    # p117 — ثانيا intro (لا يخفى أن في عزم الإناة والتجـ... جماع الخير والفضل و... الثمرات)
    (117, 0.125, 0.200, 0.00, 1.00, 'm19'),
    # p117 — ثمرة 4 [للطبراني] (très garblée en couche)
    (117, 0.680, 0.795, 0.00, 1.00, 'm20'),
    # p118 — مما يستفاد header + item1 (اللجوع... ناصحه...؟)
    (118, 0.315, 0.400, 0.00, 1.00, 'm21'),
    # p118 — تقويم Q1 + Q2/Q3 (openers)
    (118, 0.580, 0.660, 0.00, 1.00, 'm22'),
    (118, 0.715, 0.790, 0.00, 1.00, 'm23'),  # Q3
    # p119 — استثمار hadith 1 milieu (ورجلان يستبان... احمر؟)
    (119, 0.170, 0.315, 0.00, 1.00, 'm24'),
    # p119 — question استخرج + إعداد قبلي
    (119, 0.480, 0.560, 0.00, 1.00, 'm25'),
    (119, 0.590, 0.745, 0.00, 1.00, 'm26'),
]

for page, y0, y1, x0, x1, tag in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    c = im.crop(box)
    # léger agrandissement x1.6 pour compenser le resize de l'outil de lecture
    c2 = c.resize((int(c.width * 1.6), int(c.height * 1.6)), Image.LANCZOS)
    out = f'{OUT}/z21-{tag}.png'
    c2.save(out, optimize=True)
    print(f'{tag}: p{page} y[{y0:.3f}-{y1:.3f}] x[{x0:.2f}-{x1:.2f}] -> {c2.width}x{c2.height} ({os.path.getsize(out)//1024} Ko)')
print('M-CROPS TERMINÉS')
