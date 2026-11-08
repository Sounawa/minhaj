# -*- coding: utf-8 -*-
# R646 — extraction leçon 16 ulum-hadith-tanawi-2 (pdf-mut23h2u-270, المعضل والمنقطع)
# Bornes par SONDAGE (jamais devinées) :
#   p.83 = bannière leçon 16 + objectifs + tamhīd + matn Ibn Ḥaǧar (dégradé — image)
#   p.84+ = شرح, استخلاص, rubriques — borne sup À TRANCHER par sondage (بانية الدرس 17)
# Patron : scripts-translate/uh2-extract-269.py (fitz page par page)
#          + couche fix « mots réinversés » (PyMuPDF livre le RTL mot à mot inversé)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l270-raw.txt"
FIRST, LAST = 83, 91  # bornes larges : l16 (83-…) + sondage borne sup


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
chunks = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} — {len(out)} car, pages {FIRST}-{min(LAST, doc.page_count)}")
