# -*- coding: utf-8 -*-
"""Minhāj — Crops ciblés R655 (slot pdf-mut23h2x-400, leçon 11 hadith-3es).
Mécanique hadith3-zoom-400-r654.py (R654) : bandes 600-900 dpi rendues depuis
content/textbooks-src/hadith-3-iadadi_text.pdf avec PyMuPDF, stockées HORS
sondage de bornes dans tr-tmp/qa-crops-r655/ (cache lectures VLM _r655-read-*).
Zones choisies d'après les coordonnées de la couche texte (hadith3-map-400.py
et lecture blocs fitz) — chaque bande porte son étiquette bleue [سورة/الموطأ]
pour lier citation et référence sans écart."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r655"

# (nom, page 1-based, y0, y1, dpi)
BANDS = [
    ("p78-tamhid",      78, 360, 505, 600),   # tamhīd + citation Mālik + ref 1088
    ("p78-hadith",      78, 495, 690, 600),   # double question + hadith ʿUmar + ref 1080
    ("p79-cit1",        79,  92, 165, 900),   # citation calligraphique 1 + label 30
    ("p79-cit2",        79, 150, 225, 900),   # citation calligraphique 2 + label 31 + ref 1081
    ("p79-saad",        79, 215, 330, 600),   # hadith Saʿd + ref 1087
    ("p79-acha",        79, 300, 440, 600),   # hadith ʿĀʾiša + ref 1230 + début tarǧama
    ("p80-fahm",        80,  38, 200, 600),   # rubrique الفهم + 3 gloses
    ("p80-istihlas",    80, 190, 320, 600),   # استخلاص المضامين (3 items)
    ("p80-cit1",        80, 560, 630, 900),   # citation 1 fiqh + label 30
    ("p80-cit2",        80, 618, 700, 900),   # citation 2 fiqh + label 31 + قال مالك + المراد
    ("p81-radd",        81,  38, 160, 600),   # الرجوع لطواف الوداع + Safiyya + ref 1232
    ("p81-urwa",        81, 150, 300, 600),   # passage ʿUrwa + ref 1083 + ثانيا
    ("p81-haid",        81, 545, 720, 600),   # ثالثا + حكم طواف الحائض + مذهب الجمهور
    ("p82-mudtahar",    82,  38, 270, 600),   # عدم الطهارة + قال مالك 1089 + hadith 1086
    ("p82-rijal",       82, 255, 360, 600),   # رواة الموطأ بلغة أن عجوزا + الاستحاضة + الاغتسال
    ("p82-items",       82, 470, 700, 600),   # rubriques 2-3 + refs 1231/1231
    ("p83-ihlal",       83,  38, 150, 600),   # paragraphe يستفاد من الدرس
    ("p83-taqwim",      83, 150, 320, 600),   # التقويم (items)
    ("p83-hadith",      83, 300, 500, 600),   # الاستثمار + hadith زينب + ref 1085
    ("p83-idad",        83, 500, 730, 600),   # الزرقاني + الإعداد القبلي (2 items)
    ("p84-banner",      84,   0, 240, 600),   # borne sup : bannière leçon 12 + objectifs
]

doc = fitz.open(PDF)
for name, pno, y0, y1, dpi in BANDS:
    pg = doc[pno - 1]
    rect = pg.rect
    clip = fitz.Rect(0, y0, rect.width, min(y1, rect.height))
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    path = f"{OUT}/{name}.png"
    pix.save(path)
    print(f"{name}: {pix.width}x{pix.height} -> {path}")
