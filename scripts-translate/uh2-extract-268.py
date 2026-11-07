# -*- coding: utf-8 -*-
# R642 — extraction leçon 14 ulum-hadith-tanawi-2 (pdf-mut23h2u-268, المردود وأقسامه)
# Bornes par SONDAGE (jamais devinées) — cache R639 (tr-tmp/r639/) recoupé :
#   p.73 = fin leçon 13 (anšaṭa taṭbīqiyya, R635) — non touchée
#   p.74 = bannière « الدرس 14 : المردود » + objectifs + tamhīd + matn
#   p.75-76 = taḥlīl + الحديث المعلق (تعريفه، الفرق مع المعضل، حكمه) + الزهري
#   p.77 = taqwīm + istiṯmār + iʿdād (fin de leçon 14)
#   p.78-79 = sondage borne sup (bannière leçon 15 ?) — non touchées
# Patron : scripts-translate/hadith2-extract-l11.py (fitz page par page)
#          + couche fix « mots réinversés » (PyMuPDF livre le RTL mot à mot inversé)
# Couches complémentaires déjà au dépôt : tr-tmp/r639/ (embed pdftotext,
#   pymu, OCR tesseract 300 dpi, adjudications VLM ocr-p07X-*.txt de R639).
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l268-raw.txt"
FIRST, LAST = 73, 79  # bornes larges : fin l13 (73) + l14 (74-77) + sondage (78-79)


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
