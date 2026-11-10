# -*- coding: utf-8 -*-
"""R674 — micro-lot final : crops hyper-serrés (zoom 11-13) pour trancher
le nom de 1134, le cœur de 1135, l'āya de p.124, le verdict مالك de 1128,
l'isnad de 1138, la citation 1136 et la citation 1139."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r674"
doc = fitz.open(PDF)

ZONES = [
    (127, 3, 3, 13, "m-1134-name"),
    (125, 2, 5, 12, "m-1135-mid"),
    (124, 4, 4, 12, "m-p124-aya"),
    (127, 21, 21, 13, "m-1128-malik"),
    (128, 4, 4, 13, "m-1138-isnad"),
    (127, 7, 8, 11, "m-1136-frame"),
    (128, 6, 7, 12, "m-1139-quote"),
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
    sel = lines[i0:i1 + 1]
    x0 = max(min(l[0] for l in sel) - 10, 0)
    x1 = min(max(l[2] for l in sel) + 10, page.rect.width)
    y0 = max(min(l[1] for l in sel) - 6, 0)
    y1 = min(max(l[3] for l in sel) + 6, page.rect.height)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(x0, y0, x1, y1))
    pix.save(f"{OUT}/{tag}.png")
    print(f"OK {tag} — {pix.width}×{pix.height}px")
