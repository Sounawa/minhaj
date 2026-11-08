# -*- coding: utf-8 -*-
# R648 — extraction leçon 17 ulum-hadith-tanawi-2 (pdf-mut23h2u-271, السقط الظاهر والخفي)
# Bornes par SONDAGE (jamais devinées) :
#   p.88 = bannière leçon 17 (vue par sondage R646 : 3 objectifs + tamhīd + matn Ibn Ḥaǧar
#          « ثم قد يكون واحدا واضحا أو خفيا… فالأول يردك بعدم التالي… » PARTIELLEMENT lisible)
#   borne sup = bannière leçon 18 (الدرس الثامن عشر أسباب الطعن في الراوي) À TRANCHER
# Patron : scripts-translate/uh2-extract-270.py (fitz page par page + couche FIX)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l271-raw.txt"
FIRST, LAST = 88, 97  # bornes larges : l17 (88-…) + sondage borne sup


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
# sondage bannière leçon 18
for p in range(FIRST + 1, min(LAST, doc.page_count) + 1):
    t = doc[p - 1].get_text("text")
    for token in (" ةنيمئاملا ", " عونلا ", " ثيدحلا فحص"):
        pass
    # recherche inversée : « الدرس الثامن عشر » s'écrit en brut LTR inversé
    rev = " رشع نماثملا سرتدلا"[::-1]
    rev2 = " رشع نماثملا نيدلا".strip()
    if "نماثم" in t or "نماثم"[::-1] in t:
        print(f"p.{p} : motif « الثامن » détecté (candidat bannière leçon 18) — à confirmer par image")
