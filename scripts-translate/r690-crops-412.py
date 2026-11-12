#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R690 — microcrops d'adjudication leçon 412 hadith-3es (la 'umra, p.152-158).
Crops par bandes y (pleine largeur du texte) autour d'ancres cherchées en
forme VISUELLE (chaque mot inversé caractère par caractère). Zoom 4x ≈ 3000px."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/m412"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

import re as _re

MARKS = _re.compile(r'[\u064B-\u0652\u0670\u0653-\u0655\u0640\u0656\u0657\u0658]')

def norm(s):  # retire diacritiques + ponctuation
    return MARKS.sub('', s).strip('«»:.،؛؟()\u0640 ')

def rev(s):  # inverse caractère par caractère (forme visuelle du calque)
    return s[::-1]

def find_band(pno, anchor, dx=(38, 560), dy=(-14, 30)):
    """Trouve l'ancre (mot inversé, sans diacritiques) sur la page, bande y pleine largeur."""
    page = doc[pno - 1]
    words = page.get_text("words")
    target = rev(norm(anchor))
    hits = [w for w in words if target and target in norm(w[4])]
    if not hits:
        return None
    y0 = min(w[1] for w in hits) + dy[0]
    y1 = max(w[3] for w in hits) + dy[1]
    return (dx[0], max(0, y0), dx[1], min(page.rect.height, y1))

CROPS = [
    # (tag, page, ancre, marge_haut, marge_bas, extension_y)
    ("p152-idad",       152, "أعرّف",        -60, 55, 0),   # items i'dād leçon 23
    ("p153-aya",        153, "تعالى:",       -16, 150, 0),  # médaillon āya + renvoi
    ("p153-umar",       153, "أشهر",         -50, 30, 0),   # hadith 'Umar + renvoi
    ("p153-objectifs",  153, "أدرك",         -40, 30, 0),   # 3e objectif + médaillon au-dessus
    ("p154-icha-quote", 154, "رمضان",        -60, 45, 0),   # hadith 'Ā'icha + renvoi
    ("p154-malik-miq",  154, "المواقيت",     -70, 60, 0),   # question + réponse Mālik + renvoi
    ("p154-hicham",     154, "شوال",         -55, 30, 0),   # hadith Hicham + renvoi
    ("p154-charh",      154, "تجوزت",        -70, 60, 0),   # gloses du charh
    ("p155-istikhlas",  155, "استخلاص",      -30, 90, 0),   # items استخلاص المضامين
    ("p155-malik-sunna",155, "تركها",        -60, 30, 0),   # citation Mālik sunna + renvoi
    ("p155-kaffara",    155, "بينهما",       -60, 30, 0),   # hadith kaffāra + renvoi
    ("p155-notice",     155, "مات",          -60, 30, 0),   # notice Abū Bakr b. 'Abd ar-Raḥmān
    ("p156-repetition", 156, "مرارا",        -55, 30, 0),   # citation Mālik répétition + renvoi
    ("p156-miqat",      156, "التنعيم",      -45, 55, 0),   # citation Mālik miqāt + renvoi
    ("p156-ramadan",    156, "بركة",         -50, 40, 0),   # paragraphe 'umra Ramadan
    ("p157-3umras",     157, "الجعرانة",     -60, 45, 0),   # hadith 3 'umras + renvoi
    ("p157-hicham2",    157, "شوال",         -55, 45, 0),   # Hisham re-cité + renvoi
    ("p157-said",       157, "سعيد:",        -50, 45, 0),   # citation Sa'īd + renvoi
    ("p158-umar-salama",158, "قفل",          -60, 30, 0),   # 'Umar b. Abī Salama + renvoi
    ("p158-idad",       158, "أعرف",         -50, 60, 0),   # i'dād leçon 24
]

ZOOM = 4.0
for tag, pno, anc, up, dn, _ in CROPS:
    band = find_band(pno, anc, dy=(up, dn))
    if band is None:
        print(f"ANCRE ABSENTE p{pno}: {anc} ({tag})")
        continue
    page = doc[pno - 1]
    mat = fitz.Matrix(ZOOM, ZOOM)
    pix = page.get_pixmap(matrix=mat, clip=fitz.Rect(*band))
    f = f"{OUT}/{tag}.png"
    pix.save(f)
    print(f"{tag}: p{pno} band y={band[1]:.0f}-{band[3]:.0f} -> {pix.width}x{pix.height}")
