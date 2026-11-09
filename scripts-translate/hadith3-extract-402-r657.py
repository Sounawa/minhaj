# -*- coding: utf-8 -*-
"""Minhāj — Extraction couche texte leçon 13 hadith-3es (R657, slot pdf-mut23h2x-402,
أعمال يوم عرفة). Mécanique hadith3-extract-400-r652.py (R652).
Bornes à trancher par sondage image : ouverture = bannière الدرس الثالث عشر
(médaillon 13, أهداف الدرس) attendue vers p.89-90 ; clôture = page avant la
bannière du cours 14 (المبيت بمزدلفة). Fenêtre élargie 88-98 pour preuves de
jonction. Sortie : tr-tmp/h3-402-raw.txt puis tr-tmp/h3-402-readable.txt —
TROIS couches par page : FIX (mots réinversés), BRUTE, DÉCODÉE (montage lignes)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT_RAW = "/home/z/my-project/tr-tmp/h3-402-raw.txt"
OUT_READ = "/home/z/my-project/tr-tmp/h3-402-readable.txt"
FIRST, LAST = 88, 98

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def decode_page(p):
    """Couche décodée : blocs triés par (colonne droite→gauche, y) pour ordre
    de lecture arabe plus fidèle — mécanique hadith3-decode-391.py."""
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
    # vue lisible : lignes triées x descendante (droite→gauche) puis y croissante
    lines = decode_page(p)
    lines.sort(key=lambda t: (round(t[1] / 8), -t[2]))
    reads.append(f"===== PAGE {p + 1} — VUE LISIBLE (tri colonnes droite→gauche) =====")
    for x0, y0, x1, t in lines:
        reads.append(fix_line(t))

open(OUT_RAW, "w", encoding="utf-8").write("\n\n".join(chunks))
open(OUT_READ, "w", encoding="utf-8").write("\n".join(reads))
print(f"OK {OUT_RAW} — {sum(len(c) for c in chunks)} car, pages {FIRST}-{LAST}")
print(f"OK {OUT_READ} — {sum(len(r) for r in reads)} car")
