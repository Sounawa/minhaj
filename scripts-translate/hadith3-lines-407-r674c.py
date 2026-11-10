# -*- coding: utf-8 -*-
"""Minhāj — Structure de lignes triées p.124-130 (R674-C, ouvrier B trace 1a19c7c0ffb4f845).
But : localiser les bandes de lignes pour les crops d'adjudication."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)


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


for pg in [124, 125, 126, 127, 128, 129, 130]:
    lines, page = decode_sorted(pg - 1)
    print(f"===== PAGE {pg} ({len(lines)} lignes) =====")
    for i, (x0, y0, x1, y1, t) in enumerate(lines):
        short = " ".join(w[::-1] for w in t.split())[:90]
        print(f"{i:3d} y={y0:6.1f}-{y1:6.1f} | {short}")
