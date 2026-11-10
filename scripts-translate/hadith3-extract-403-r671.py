# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 14 hadith-3es (R671, slot pdf-mut23h2x-403,
أحكام مزدلفة). Mécanique hadith3-extract-404-r670.py (R670).
Fenêtre 97-103 : ouverture p.97 (bannière du cours 14 + أحفظ أحاديث الدرس),
contenu p.98+ ; clôture = avant la bannière du cours 15 (p.103 ouverture 404,
déjà tranchée par R670 : bornes 403 = p.97-102, p.103 bannière 15).
Sortie : tr-tmp/h3-403-raw.txt puis tr-tmp/h3-403-readable.txt — TROIS couches par
page : FIX (mots réinversés), BRUTE, VUE LISIBLE (montage lignes triées)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT_RAW = "/home/z/my-project/tr-tmp/h3-403-raw.txt"
OUT_READ = "/home/z/my-project/tr-tmp/h3-403-readable.txt"
FIRST, LAST = 97, 103

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def decode_page(p):
    """Couche lisible : lignes triées par (bande y, x1 descendant) — droite→gauche."""
    page = doc[p]
    d = page.get_text("dict")
    out = []
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if txt:
                out.append((round(b["bbox"][0], 1), round(l["bbox"][1], 1), round(l["bbox"][2], 1), txt))
    return out


chunks, reads = [], []
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    fixed = "\n".join(fix_line(l) for l in txt.split("\n"))
    chunks.append(f"===== PAGE {p + 1} — COUCHE FIX (mots réinversés) =====\n{fixed}")
    chunks.append(f"===== PAGE {p + 1} — COUCHE BRUTE =====\n{txt}")
    lines = decode_page(p)
    lines.sort(key=lambda t: (round(t[1] / 8), -t[2]))
    reads.append(f"===== PAGE {p + 1} — VUE LISIBLE (tri colonnes droite→gauche) =====")
    for x0, y0, x1, t in lines:
        reads.append(fix_line(t))

open(OUT_RAW, "w", encoding="utf-8").write("\n\n".join(chunks))
open(OUT_READ, "w", encoding="utf-8").write("\n".join(reads))
print(f"OK {OUT_RAW} — {sum(len(c) for c in chunks)} car, pages {FIRST}-{LAST}")
print(f"OK {OUT_READ} — {sum(len(r) for r in reads)} car")
