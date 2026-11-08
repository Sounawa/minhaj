# -*- coding: utf-8 -*-
"""Minhāj — Inspections image leçon 16 ulum-hadith-tanawi-2 (slot pdf-mut23h2u-270).
Méthode R641-R645 : bandes d'image localisées 300-600 dpi sur les zones incertaines
de p.83-87 (matn Ibn Ḥaǧar dégradé, ligne tasmīa, isnad/matn de l'exemple du
Ḥākim, ḥukm du manqaṭiʿ, consigne istiṯmār). Sortie : tr-tmp/qa-crops-r646/*.png
— lecture sélective ensuite (budget ≤ 6 lectures)."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r646"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# (page 1-based, y0, y1 en fractions de hauteur, dpi, suffixe, x0, x1 en points ou None)
CROPS = [
    # p.83 — المتن Ibn Ḥaǧar (zone dégradée dans les deux couches) + début الفهم
    (83, 0.42, 0.72, 500, "p83-a-matn", None, None),
    # p.83 — استخلاص المضامين (rubriques الثالث + items)
    (83, 0.72, 0.97, 400, "p83-b-istihlas", None, None),
    # p.84 — ligne tasmīa dégradée + السخاوي فتح المغيث
    (84, 0.14, 0.34, 500, "p84-a-tasmia", None, None),
    # p.86 — isnad + matn حذيفة + commentaire du Ḥākim (zone éclatée)
    (86, 0.10, 0.52, 450, "p86-a-isnad-matn", None, None),
    # p.86 — حكم الحديث المنقطع (garble) + ابن عبد البر
    (86, 0.52, 0.82, 450, "p86-b-hukm", None, None),
    # p.87 — consigne الاستثمار dégradée + إعداد قبلي (vue)
    (87, 0.00, 0.55, 400, "p87-a-istithmar", None, None),
]

for pg, y0, y1, dpi, suf, x0, x1 in CROPS:
    page = doc[pg - 1]
    rect = page.rect
    clip = fitz.Rect(
        x0 if x0 is not None else rect.x0,
        rect.y0 + (rect.height * y0),
        x1 if x1 is not None else rect.x1,
        rect.y0 + (rect.height * y1),
    )
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    path = f"{OUT}/{suf}.png"
    pix.save(path)
    print(f"{path} — {pix.width}x{pix.height}")
