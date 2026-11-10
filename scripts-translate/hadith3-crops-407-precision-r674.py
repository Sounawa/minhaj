# -*- coding: utf-8 -*-
"""Minhāj — Crops de PRÉCISION leçon 407 (R674) : bandes resserrées, zoom 8-9,
pour trancher les zones que la passe VLM 1 a laissées ambiguës."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r674"
doc = fitz.open(PDF)

ZONES = [
    (124, 4, 4, 9, "z-p124-aya"),
    (124, 5, 6, 9, "z-p124-nuqsan"),
    (125, 2, 8, 9, "z-p125-h1135matn"),
    (125, 9, 10, 9, "z-p125-notice"),
    (126, 7, 8, 9, "z-p126-q1122"),
    (126, 9, 11, 9, "z-p126-q1124"),
    (126, 13, 15, 9, "z-p126-q1125"),
    (126, 18, 20, 9, "z-p126-thania"),
    (127, 0, 5, 9, "z-p127-h1134"),
    (127, 7, 9, 9, "z-p127-q1136"),
    (127, 11, 12, 9, "z-p127-afsada"),
    (127, 14, 20, 8, "z-p127-saidmid"),
    (127, 22, 25, 9, "z-p127-after"),
    (128, 0, 3, 9, "z-p128-h1129"),
    (128, 4, 5, 9, "z-p128-h1138"),
    (128, 6, 7, 9, "z-p128-h1139"),
    (128, 11, 13, 9, "z-p128-khat-aya"),
    (128, 13, 16, 9, "z-p128-exos"),
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
    sel = lines[i0:i1 + 1]
    x0 = max(min(l[0] for l in sel) - 12, 0)
    x1 = min(max(l[2] for l in sel) + 12, page.rect.width)
    y0 = max(min(l[1] for l in sel) - 8, 0)
    y1 = min(max(l[3] for l in sel) + 8, page.rect.height)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(x0, y0, x1, y1))
    pix.save(f"{OUT}/{tag}.png")
    print(f"OK {tag} — {pix.width}×{pix.height}px")
