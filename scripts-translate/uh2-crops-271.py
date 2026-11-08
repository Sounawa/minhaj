# -*- coding: utf-8 -*-
"""Minhāj — Inspections image leçon 17 ulum-hadith-tanawi-2 (slot pdf-mut23h2u-271).
Méthode R646 (patron uh2-crops-270.py) : bandes 400-500 dpi sur zones incertaines
de p.88-92 (matn Ibn Ḥaǧar, استخلاص deux colonnes, citations شعبة, حكم التدليس,
الفرق/مثال المرسل الخفي, أهتدي + بيان أرقام ابن المنكدر). Sortie : tr-tmp/qa-crops-r648/
— lecture sélective ensuite (budget ≤ 6 lectures par sous-passe)."""
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r648"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# (page 1-based, y0, y1 en fractions de hauteur, dpi, suffixe)
CROPS = [
    # p.88 — المتن matn Ibn Ḥaǧar (garble partiel : الحتيج/التاريخ، صيغ اللقي)
    (88, 0.38, 0.68, 500, "p88-a-matn"),
    # p.88 — استخلاص المضامين (deux colonnes à apparier)
    (88, 0.62, 0.97, 400, "p88-b-istihlas"),
    # p.90 — citations شعبة garblées «لأن أزني...» + العقب ابن الصلاح
    (90, 0.26, 0.62, 500, "p90-a-shuba"),
    # p.91 — حكم الحديث المدلس (ligne très garblée) + تعريف المرسل الخفي
    (91, 0.20, 0.55, 450, "p91-a-hukm"),
    # p.91 — الفرق بين المدلس والمرسل الخفي (النووي والعراقي) + مثال أبو هريرة
    (91, 0.55, 0.97, 400, "p91-b-farq-mithal"),
    # p.92 — بيان ابن المنكدر (أرقام) + أهتدي وأقتدي (référence bracket ص 842)
    (92, 0.00, 0.55, 450, "p92-a-bayan-ihtadi"),
]

for pg, y0, y1, dpi, suf in CROPS:
    page = doc[pg - 1]
    rect = page.rect
    clip = fitz.Rect(rect.x0, rect.y0 + rect.height * y0, rect.x1, rect.y0 + rect.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    path = f"{OUT}/{suf}.png"
    pix.save(path)
    print(f"{path} — {pix.width}x{pix.height}")
