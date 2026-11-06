#!/usr/bin/env python3
"""R638 — crops de preuve frais 1200 dpi p.17-24 (leçon 391).
Localise [الموطأ رقم] et les zones-clés via la couche texte du PDF."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r638"
doc = fitz.open(PDF)

def dump(pno):
    pg = doc[pno - 1]
    words = pg.get_text("words")
    print(f"--- PAGE {pno} ({pg.rect.width:.0f}x{pg.rect.height:.0f}) ---")
    hits = []
    for w in words:
        if "الموطأ" in w[4] or "رقم" in w[4]:
            hits.append(w)
    for h in hits:
        print(f"  MOTAR {h[4][:20]!r} x={h[0]:.0f} y={h[1]:.0f}")

for p in (17, 18, 20, 21, 22, 23):
    dump(p)
