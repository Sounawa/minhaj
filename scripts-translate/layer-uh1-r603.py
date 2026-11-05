#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R603 — extraction de la couche texte du PDF (spans : bbox + COULEUR) p.125-128.
Objectif : cartographier les titres ROUGES (morts pour tesseract) objectivement
par l'attribut couleur du rendu PDF, et obtenir un second texte local à croiser
avec tesseract multi-dpi. La couche est en ordre VISUEL (mots inversés) et
formes de présentation — normalisation : NFKC + inversion de l'ordre des mots.
Usage : python3 scripts-translate/layer-uh1-r603.py [first last]
"""
import sys
import unicodedata
import fitz

HOME = "/tmp/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"


def norm_line(s: str) -> str:
    """NFKC (formes de présentation -> lettres) + inversion ordre des mots."""
    t = unicodedata.normalize("NFKC", s)
    # l'extracteur archive produit l'ordre visuel G->D ; on remet D->G par mots
    return " ".join(reversed(t.split()))


def main() -> int:
    doc = fitz.open(PDF)
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 125
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 128
    for n in range(first, last + 1):
        page = doc[n - 1]
        d = page.get_text("dict")
        print(f"######## p{n} ########")
        for b in d["blocks"]:
            if b.get("type") != 0:
                continue
            for ln in b["lines"]:
                parts = []
                col = None
                for sp in ln["spans"]:
                    parts.append(sp["text"])
                    col = sp["color"]
                if not "".join(parts).strip():
                    continue
                txt = norm_line(" ".join(parts))
                # color int -> #rrggbb
                c = f"#{col:06x}" if isinstance(col, int) else "?"
                y = int(ln["bbox"][1])
                sz = round(ln["spans"][0]["size"], 1)
                print(f"y={y:4d} col={c} sz={sz:5} | {txt}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
