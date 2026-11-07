# -*- coding: utf-8 -*-
"""Minhāj — Inspections image leçon 8 hadith-3es (slot pdf-mut23h2x-397).
Méthode R638 : bandes d'image localisées 320-600 dpi, ≤ 2800 px, sur les zones
incertaines de p.58-64 (bannière graphique absente de la couche texte, numéros
de référence [الموطأ رقم: NNN], versets coraniques en thuluth, chaînes et matns
corrompus, zones OCR éclatées). Sortie : tr-tmp/qa-crops-r641/*.png — lecture
sélective ensuite (budget ≤ 15 lectures)."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r641"

doc = fitz.open(PDF)

# (page 1-based, y0, y1 en fractions de hauteur, dpi, suffixe, x0, x1 en points ou None)
CROPS = [
    # p.58 — bannière + médaillon (graphique) + objectifs
    (58, 0.00, 0.26, 600, "p58-a-titre", 140, 455),
    # p.58 — tamhīd (ouverture)
    (58, 0.34, 0.64, 380, "p58-b-tamhid", None, None),
    # p.58 — début de la citation de Mālik (tamhīd)
    (58, 0.73, 0.87, 380, "p58-c-quote", None, None),
    # p.59 — fin de la citation + رقم 1024
    (59, 0.05, 0.20, 380, "p59-a-1024", None, None),
    # p.59 — chaîne مالك/يحيى + verset en thuluth + 1025
    (59, 0.17, 0.34, 400, "p59-b-yahya-verse", 50, 545),
    # p.59 — « خمسٌ فواسق » + رقم 1028
    (59, 0.40, 0.60, 380, "p59-d-1028", None, None),
    # p.59 — notice du transmetteur يحيى بن يحيى الليثي
    (59, 0.64, 0.84, 380, "p59-e-bio", None, None),
    # p.61 — ثانيا جزاء الصيد (zone OCR éclatée) + 1027 + fin de page
    (61, 0.28, 0.96, 380, "p61-a-thania-1027", None, None),
    # p.62 — verset thuluth + poème didactique
    (62, 0.27, 0.42, 400, "p62-a-verse-poem", 50, 545),
    # p.62 — « أحسنُ ما سمعتُ » + رقم 1026
    (62, 0.40, 0.61, 380, "p62-b-1026", None, None),
    # p.63 — 1033 + الباجي
    (63, 0.28, 0.46, 380, "p63-a-1033", None, None),
    # p.63 — zone éclatée + « السباع لا يعد... » + رقم garantis
    (63, 0.44, 0.62, 380, "p63-b-siba-num", None, None),
    # p.64 — textes 1036 / 1038 / 1040 + numéros
    (64, 0.13, 0.41, 380, "p64-a-texts", None, None),
    # p.64 — vue générale (bannières d'exercices graphiques)
    (64, 0.00, 1.00, 150, "p64-b-vue", None, None),
    # p.65 — bannière الدرس 9 (borne supérieure)
    (65, 0.00, 0.28, 300, "p65-a-banniere-l9", None, None),
    # — recadrages ciblés R641 (budget lectures 12 : fusion de zones) —
    # p.59 — verset thuluth ÉTENDU (fin de la citation coranique + marqueur + prose qui suit)
    (59, 0.17, 0.40, 400, "p59-b-ext", 50, 545),
    # p.62 — fusion : estimation du gibier (أ/ب/ج) + verset + poème + 1026 + ثالثا + 1030/1031
    (62, 0.28, 0.88, 320, "p62-mid", None, None),
    # p.63 — fusion : 1033 + الباجي + السباع (zone éclatée) + numéro
    (63, 0.26, 0.64, 320, "p63-mid", None, None),
    # p.64 — fusion : textes 1036/1038/1040 + exploitation (أستعين بشرح الزرقاني…) + figures
    (64, 0.10, 0.66, 320, "p64-mid", None, None),
]

os.makedirs(OUT, exist_ok=True)
for pg, f0, f1, dpi, name, x0, x1 in CROPS:
    page = doc[pg - 1]
    r = page.rect
    xa = x0 if x0 is not None else 0
    xb = x1 if x1 is not None else r.width
    clip = fitz.Rect(xa, r.height * f0, xb, r.height * f1)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    p = f"{OUT}/{name}.png"
    pix.save(p)
    print(f"OK {p} {pix.width}x{pix.height}")
print(f"{len(CROPS)} bandes écrites dans {OUT}")
