# -*- coding: utf-8 -*-
"""R571 — micro-recadrages de preuve pour la leçon 25 (pdf-26, p.171-176).
Chaque renvoi Muwaṭṭaʾ, chaque zone ambiguë → crop haute résolution à LIRE à l'œil.
Repérage des zones par search_for sur la couche texte (mêmes chaînes brouillées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
doc = fitz.open(PDF)

# (page 1-based, ancre de recherche, étiquette, marge en points)
TARGETS = [
    (172, "الموطأ", "num-818", 90),      # fin hadith 1 (كفارة)
    (172, "الموطأ", "num-821", 90),      # fin hadith 2 (حجامة ابن عمر)
    (172, "الموطأ", "num-826", 90),      # fin hadith 3 (عاشوراء معاوية)
    (173, "الموطأ", "num-819-desm", 90), # وصم يوماً
    (174, "الموطأ", "num-819-ata", 90),  # عطاء / سعيد بن المسيب
    (174, "الموطأ", "num-822", 90),      # حجامة سعد وابن عمر
    (175, "الموطأ", "num-825", 90),      # عائشة عاشوراء
    (176, "الموطأ", "num-824", 90),      # استهلال مالك (الحجامة)
    (171, "مسكين", "p171-fin-hadith1", 120),  # zone fin p.171 (suite du hadith 1)
    (171, "أهداف", "p171-objectifs", 200),    # bandeau + objectifs
    (172, "الشرح", "p172-glos-irq", 150),     # glossaire العَرَّق
    (172, "ترجمة", "p172-bio-muawiya", 200),  # ترجمة الراوي معاوية
    (173, "مشهور", "p173-derniere-ligne", 120),  # fin p.173 (مشهور قول الإمام مالك...)
    (175, "العاشر", "p175-fin-contenu", 140),    # fin contenu p.175 (avant تقويم)
    (176, "الحجّام", "p176-istihlal", 150),      # استهلال p.176
]

counts = {}
for pno, needle, tag, margin in TARGETS:
    page = doc[pno - 1]
    rects = page.search_for(needle)
    key = (pno, needle)
    counts[key] = len(rects)
    for i, r in enumerate(rects):
        clip = fitz.Rect(max(0, r.x0 - margin), max(0, r.y0 - margin * 0.9),
                         min(page.rect.x1, r.x1 + margin), min(page.rect.y1, r.y1 + margin * 0.9))
        for zoom, suffix in ((4, "600"), (8, "1200")):
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
            name = f"{OUT}/mc-r571-{tag}{'-' + str(i) if len(rects) > 1 else ''}-{suffix}.png"
            pix.save(name)

# bandeau « الدرس 25 » en tête de p.171 (haut de page, pleine largeur)
p171 = doc[170]
band = fitz.Rect(0, 0, p171.rect.x1, p171.rect.y1 * 0.30)
for zoom in (4, 8):
    pix = p171.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=band)
    pix.save(f"{OUT}/mc-r571-bandeau-171-{zoom * 100 // 4}.png")

# bas de p.175 (fin du contenu / tête تقويم) pour la zone « إفراد العاشر + crochet illisible »
p175 = doc[174]
band175 = fitz.Rect(0, p175.rect.y1 * 0.72, p175.rect.x1, p175.rect.y1)
for zoom in (4, 8):
    pix = p175.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=band175)
    pix.save(f"{OUT}/mc-r571-bas-175-{zoom * 100 // 4}.png")

# ligne finale de p.173 (مشهور قول الإمام مالك ...) pleine largeur
p173 = doc[172]
band173 = fitz.Rect(0, p173.rect.y1 * 0.86, p173.rect.x1, p173.rect.y1)
for zoom in (4, 8):
    pix = p173.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=band173)
    pix.save(f"{OUT}/mc-r571-bas-173-{zoom * 100 // 4}.png")

for k, v in sorted(counts.items()):
    print(f"page {k[0]} ancre {k[1]!r} : {v} occurrence(s)")
print("crops écrits dans", OUT)
