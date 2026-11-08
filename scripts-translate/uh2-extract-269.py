# -*- coding: utf-8 -*-
# R645 — extraction leçon 15 ulum-hadith-tanawi-2 (pdf-mut23h2u-269, الحديث المرسل)
# Bornes par SONDAGE (jamais devinées) — caches recoupés :
#   p.78 = bannière leçon 15 + objectifs + tamhīd + matn « والثاني: المُرْسَلَ »
#   p.79 = taḥlīl (تعريف المرسل لغة/اصطلاحا ; الفقهاء والأصوليين ; ابن عبدالبر) + صور المرسل (Ibn aṣ-Ṣalāḥ)
#   p.80-81 = suite صور المرسل (الحاكم, أصاغر التابعين, ابن عباس) + حكم المرسل (مالك, الباجي) + توجيه
#   p.82 = taqwīm (2 questions, fin de leçon 15) ; p.83 = bannière leçon 16 (hors bornes)
# Recoupées avec tr-tmp/r639/ (embed pdftotext, 300 dpi, pymu p.74-79)
# et tr-tmp/uh2-l268-raw.txt (R642, p.73-79).
# Patron : scripts-translate/uh2-extract-268.py (fitz page par page)
#          + couche fix « mots réinversés » (PyMuPDF livre le RTL mot à mot inversé)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l269-raw.txt"
FIRST, LAST = 78, 82  # bornes larges : l15 (78-82) + sondage borne sup


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
chunks = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    fixed = "\n".join(fix_line(l) for l in txt.splitlines())
    chunks.append(
        f"===== PAGE {p} — COUCHE BRUTE =====\n{txt}\n"
        f"----- PAGE {p} — COUCHE FIX (mots réinversés) -----\n{fixed}\n"
    )
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — pages {FIRST}-{LAST}, {sum(len(c) for c in chunks)} car")
