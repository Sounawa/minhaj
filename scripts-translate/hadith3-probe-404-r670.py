# -*- coding: utf-8 -*-
"""Minhāj — PROBE structure p.100-125 hadith-3es pour bornes leçon 15 (pdf-404, R670).
Les bannières médaillon (الدرس الخامس عشر) n'ont pas de couche OCR — repérage par :
tailles de pages (pages-bannières = quasi vides), أهداف, mots-clés des leçons 15/16,
chiffres de médaillons. JAMAIS de borne devinée : confirmation image ensuite."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


print("=== TAILLES p.95-125 ===")
for p in range(94, min(125, doc.page_count)):
    txt = doc[p].get_text("text")
    print(f"p.{p+1}: {len(txt)} car, {len(txt.splitlines())} lignes")

print("\n=== CONTENU p.103-112 (FIX, 400 premiers car) ===")
for p in range(102, min(112, doc.page_count)):
    txt = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in txt.split("\n"))
    print(f"\n--- p.{p+1} ---")
    print(fixed[:400])
