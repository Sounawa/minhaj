# -*- coding: utf-8 -*-
"""Minhāj — Crops de preuve leçon 407 hadith-3es (R674, slot pdf-mut23h2x-407).
Mécanique hadith3-crops-397.py / hadith2-crops*.py : chaque zone = bandes de
lignes consécutives de la VUE LISIBLE (tri (bande y, x1 desc)), bbox union
élargie, rendu fitz zoom élevé. Sortie : tr-tmp/qa-crops-r674/<tag>.png"""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r674"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page 1-indexée, idx_début, idx_fin_inclus, zoom, tag) — idx = ordre VUE LISIBLE
ZONES = [
    (124, 0, 3, 5, "p124-qs-def"),
    (124, 4, 4, 7, "p124-aya"),
    (124, 5, 7, 5, "p124-nuqsan"),
    (124, 8, 11, 7, "p124-h1121"),
    (125, 0, 8, 6, "p125-h1135"),
    (125, 9, 10, 6, "p125-notice"),
    (125, 13, 17, 4, "p125-istihlas"),
    (126, 2, 6, 6, "p126-atb1"),
    (126, 7, 11, 6, "p126-atb2"),
    (126, 12, 16, 6, "p126-daya"),
    (126, 17, 20, 4, "p126-thania"),
    (127, 0, 6, 6, "p127-h1134"),
    (127, 7, 9, 7, "p127-h1136"),
    (127, 10, 12, 4, "p127-fouat2"),
    (127, 13, 21, 6, "p127-said"),
    (127, 22, 25, 6, "p127-after"),
    (128, 0, 3, 6, "p128-h1129"),
    (128, 4, 5, 7, "p128-h1138"),
    (128, 6, 7, 7, "p128-h1139"),
    (128, 9, 12, 6, "p128-khatima"),
    (128, 13, 16, 4, "p128-exos"),
    (128, 17, 26, 6, "p128-athar"),
]


def decode_sorted(p):
    page = doc[p]
    d = page.get_text("dict")
    out = []
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if txt:
                out.append((round(b["bbox"][0], 1), round(l["bbox"][1], 1), round(l["bbox"][2], 1), round(l["bbox"][3], 1), txt))
    out.sort(key=lambda t: (round(t[1] / 8), -t[2]))
    return out, page


for pg, i0, i1, zoom, tag in ZONES:
    lines, page = decode_sorted(pg - 1)
    if i1 >= len(lines):
        i1 = len(lines) - 1
        print(f"WARN {tag}: idx_max={i1}")
    sel = lines[i0:i1 + 1]
    x0 = max(min(l[0] for l in sel) - 18, 0)
    x1 = min(max(l[2] for l in sel) + 18, page.rect.width)
    y0 = max(min(l[1] for l in sel) - 14, 0)
    y1 = min(max(l[3] for l in sel) + 14, page.rect.height)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=fitz.Rect(x0, y0, x1, y1))
    path = f"{OUT}/{tag}.png"
    pix.save(path)
    print(f"OK {tag} — page {pg} lignes {i0}-{i1} zoom {zoom} → {pix.width}×{pix.height}px")
