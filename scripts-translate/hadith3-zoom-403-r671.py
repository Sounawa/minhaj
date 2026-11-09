# -*- coding: utf-8 -*-
"""Minhāj — zooms ciblés leçon 403 hadith-3es (R671, p.97-102).
Zones pivot où les couches texte divergent ou restent illisibles :
chiffres Muwaṭṭa (brackets bleus), mots glosés, citation Mālik + āyāt p.102.
Crops fitz 600 dpi via recherche de rects du calque texte (tessdata local en
secours). Sortie : tr-tmp/qa-crops-r670/zoom-*.png."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r670"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
SCALE = 0.92  # PIL resize après 600 dpi


def band_rects(page_no, needles, pad_y0=0.012, pad_y1=0.012, x0=0.04, x1=0.96):
    """Retourne la bande y (fractions) englobant les rects des aiguilles."""
    pg = doc[page_no - 1]
    ys = []
    for n in needles:
        for r in pg.search_for(n):
            ys.append((r.y0, r.y1))
    if not ys:
        return None
    y0 = max(0.0, min(y for y, _ in ys) / pg.rect.height - pad_y0)
    y1 = min(1.0, max(y for _, y in ys) / pg.rect.height + pad_y1)
    return (page_no, y0, y1, x0, x1)


# Bandes fixes éprouvées (positions des composites r670-*), 600 dpi.
ZOOMS = [
    ("zoom-a-p97-tamhid-fin",  97, 0.47, 0.585),   # وتَرْلُوا + تقدّموا وتفرّقوا
    ("zoom-b-p97-num",         97, 0.855, 0.930),  # نَصّ + فوق العتق + [1165]
    ("zoom-c-p98-num",         98, 0.395, 0.465),  # [الموطأ رقم: N2]
    ("zoom-d-p98-tarjama",     98, 0.545, 0.745),  # ترجمة أسامة (سطران حَرِجَان)
    ("zoom-e-p99-athar-num",   99, 0.760, 0.845),  # قَذِر/قدر رمية + [1166]
    ("zoom-f-p100-ataa",      100, 0.055, 0.165),  # قال عَلَى/عَطَاء + وارتفعوا + [1152]
    ("zoom-g-p100-nafii",     100, 0.435, 0.575),  # نافع + ابن عمر/حمر + [1192] + [1195]
    ("zoom-h-p101-ibnmasud",  101, 0.240, 0.400),  # ابن مسعود + رأيتُ النّبيّ + أخذ مالك
    ("zoom-i-p101-numbers",   101, 0.660, 0.955),  # 3 āṯār + leurs chiffres + بالعجلة/العظة
    ("zoom-j-p102-malik",     102, 0.440, 0.690),  # قال مالك + رفث + الذبيح + āya1+āya2
    ("zoom-k-p102-aya3",      102, 0.690, 0.930),  # قرىش/عرب + āya3 + fin [الموطأ 1154]
]

for name, pg_no, y0, y1 in ZOOMS:
    pg = doc[pg_no - 1]
    clip = fitz.Rect(pg.rect.width * 0.04, pg.rect.height * y0,
                     pg.rect.width * 0.96, pg.rect.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img = img.resize((int(img.width * SCALE), int(img.height * SCALE)), Image.LANCZOS)
    path = f"{OUT}/{name}.png"
    img.save(path)
    print(f"OK {path} — {img.width}x{img.height}")
