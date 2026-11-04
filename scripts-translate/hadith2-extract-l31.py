# -*- coding: utf-8 -*-
"""Minhāj — Extraction + rendu annexe 30 hadith-2es (slot pdf-31, R575).
1) tr-tmp/hadith2-l31-readable.txt (pages 200-209, marqueurs de page)
2) tr-tmp/r575-pages/pXXX-300dpi.png (pages 201-208)"""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"

doc = fitz.open(PDF)

# --- extraction couche texte ---
OUT = "/home/z/my-project/tr-tmp/hadith2-l31-readable.txt"
FIRST, LAST = 200, 209
chunks, total = [], 0
for p in range(FIRST - 1, min(LAST, doc.page_count)):
    txt = doc[p].get_text("text")
    total += len(txt)
    chunks.append(f"===== PAGE {p + 1} =====\n{txt}")
open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print(f"OK {OUT} — {total} car, pages {FIRST}-{LAST}")

# --- rendu 300 dpi ---
OUTDIR = "/home/z/my-project/tr-tmp/r575-pages"
os.makedirs(OUTDIR, exist_ok=True)
for p in range(200, 209):  # pages 201-208 + 209 témoin de clôture
    pix = doc[p].get_pixmap(dpi=300)
    fp = f"{OUTDIR}/p{p + 1:03d}-300dpi.png"
    pix.save(fp)
    print(fp, pix.width, "x", pix.height)
print("OK")
