# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 10 hadith-3es (R649, slot pdf-mut23h2x-399).
Mécanique hadith3-extract-398.py (R647/ouvrier 398). Bornes tranchées par sondage
hadith3-map-399.py + preuve image VLM (hadith3-vlm-read-399.py) : ouverture p.71
(bannière الدرس العاشر, médaillon 10, titre أحكام الطواف (1), أهداف الدرس) ;
clôture p.77 (تقويم + الإعداد القبلي) — p.78 = bannière الدرس الحادي عشر
(médaillon 11, أحكام الطواف (2)) = borne supérieure exclusive.
Fenêtre élargie 70-78 pour preuves de jonction. Sortie :
tr-tmp/hadith3-l399-readable.txt — DEUX couches par page (fix + brute)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith3-l399-readable.txt"
FIRST, LAST = 70, 78

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in txt.split("\n"))
    chunks.append(f"===== PAGE {p + 1} — COUCHE FIX (mots réinversés) =====\n{fixed}")
    chunks.append(f"===== PAGE {p + 1} — COUCHE BRUTE =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n\n".join(chunks))
print(f"OK {OUT} — {sum(len(c) for c in chunks)} car, pages {FIRST}-{LAST}")
