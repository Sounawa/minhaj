# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 12 hadith-2es (slot pdf-13, R552).
Adapté de hadith2-extract-l11.py (R547).
Bornes sondées par hadith2-map.py STARTS : l12 = p.86 (أهداف الدرس
« أحكام الصلاة في الأوقات المفضلة والمكروهة ») → p.90 (الإعداد القبلي
clôturant, l13 الجنائز 1 ouvre p.91).
Sortie : tr-tmp/hadith2-l12-readable.txt (pages 85-91, marqueurs de page)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/hadith2-l12-readable.txt"
FIRST, LAST = 85, 91  # bornes larges : fin l11 (85) + l12 (86-90) + tête l13 (91)

doc = fitz.open(PDF)
chunks = []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {len(chr(10).join(chunks))} car, pages {FIRST}-{LAST}")
