# -*- coding: utf-8 -*-
"""R571 — repérage des jetons numériques + zones d'ancrage par mots inversés, puis crops."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
doc = fitz.open(PDF)

def num_tokens(page):
    d = page.get_text("dict")
    toks = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                for w in s["text"].split():
                    core = w.strip("()[]«»،؛:.،")
                    if core.isdigit():
                        toks.append((w, fitz.Rect(s["bbox"])))
    return toks

for pno in range(171, 177):
    page = doc[pno - 1]
    toks = num_tokens(page)
    print(f"--- p.{pno} : {len(toks)} jetons numériques ---")
    for w, r in toks:
        print(f"   {w!r:24} y={r.y0:7.1f} x={r.x0:6.1f}")
