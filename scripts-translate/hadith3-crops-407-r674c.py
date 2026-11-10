# -*- coding: utf-8 -*-
"""Minhāj — Crops d'ADJUDICATION leçon 407 hadith-3es (R674-C, ouvrier B trace
1a19c7c0ffb4f845) : zones laissées en conflit par les rondes r674 + couverture p.129
(jamais lue par r674) + contrôle borne sup p.130. Mécanique hadith3-crops-407-precision-r674.py."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r674c"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    # (page, y0, y1, zoom, tag)
    (124, 340, 435, 10, "a-p124-aya"),          # āya p.124 — 3 lectures VLM en conflit
    (125, 60, 255, 8, "a-p125-h1135"),          # hadith 1135 complet (conflits mid)
    (126, 165, 390, 7, "a-p126-rule"),          # paragraphe de règle 1 (تعالى vs عليه الصلاة والسلام + clause)
    (126, 470, 600, 9, "a-p126-q1125"),         # citation 1125 (نذر)
    (126, 600, 715, 9, "a-p126-thania"),        # titre ثانيا + 1- (بغير vs بسبب)
    (127, 80, 230, 7, "a-p127-h1134"),          # hadith 1134 complet (استيسر/استطعت)
    (127, 225, 325, 8, "a-p127-q1136"),         # citation 1136 (structure)
    (127, 415, 595, 7, "a-p127-h1128"),         # récit 1128 (milieu flou)
    (127, 595, 715, 8, "a-p127-after2"),        # passage Zarqānī (غير أنه vs غايته)
    (128, 50, 145, 8, "a-p128-malik1129"),      # passage Mālik + 1129
    (128, 140, 260, 10, "a-p128-h1138"),        # isnad 1138 + citation
    (128, 195, 260, 10, "a-p128-h1139"),        # قول ربيعة 1139 (النوم/اليوم)
    (128, 585, 675, 8, "a-p128-h1140"),         # athar 1140 (vérification)
    (129, 40, 320, 7, "a-p129-full"),           # p.129 ENTIER (أتأمل النص + annonce cours 19)
    (129, 165, 320, 9, "a-p129-announce"),      # bannière أجب عن + 3 questions
    (130, 55, 300, 3, "a-p130-top"),            # borne sup : bannière cours 19 + objectifs
]


def crop(page_no, y0, y1, zoom, tag):
    page = doc[page_no - 1]
    w = page.rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(0, y0, w, y1))
    pix.save(f"{OUT}/{tag}.png")
    print(f"OK {tag} — {pix.width}×{pix.height}px")


for pg, y0, y1, zoom, tag in ZONES:
    crop(pg, y0, y1, zoom, tag)
print("crops r674c terminés")
