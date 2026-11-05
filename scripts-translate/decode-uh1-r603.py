#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R603 — décodeur ordre visuel -> logique pour la couche texte du PDF.
La couche archive stocke les glyphes en ordre VISUEL (LTR = gauche->droite de
la page) avec marques de vocalisation stockées AVANT leur base. Décodage :
inverser la séquence de clusters (base + marques suivantes), puis NFKC.
Usage : python3 scripts-translate/decode-uh1-r603.py "texte visuel brut"
        python3 scripts-translate/decode-uh1-r603.py --page 125   (y=552 bayt)
"""
import sys
import unicodedata
import fitz

PDF = "/tmp/my-project/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
MARKS = set(range(0x064B, 0x0653)) | {0x0640, 0x0670, 0x0656, 0x0657, 0x0658}


def clusters(s: str):
    """Découpe en clusters [base + marques qui la suivent dans le flux visuel]."""
    out, cur = [], None
    for ch in s:
        o = ord(ch)
        if o in MARKS or o in (0x200D, 0x200C):
            if cur is None:
                cur = ch
            else:
                cur += ch
        else:
            if cur is not None:
                out.append(cur)
            cur = ch
    if cur is not None:
        out.append(cur)
    return out


def decode_visual(s: str) -> str:
    """Ordre visuel -> logique : inverse les clusters de chaque mot."""
    words = []
    for w in s.split(" "):
        cs = clusters(w)
        words.append("".join(reversed(cs)))
    return " ".join(reversed(words))


def logical(s: str) -> str:
    return unicodedata.normalize("NFKC", decode_visual(s))


def main() -> int:
    if len(sys.argv) > 2 and sys.argv[1] == "--page":
        doc = fitz.open(PDF)
        page = doc[int(sys.argv[2]) - 1]
        d = page.get_text("dict")
        for b in d["blocks"]:
            if b.get("type") != 0:
                continue
            for ln in b["lines"]:
                for sp in ln["spans"]:
                    t = sp["text"]
                    if "\uFB50" <= t[0:1] <= "\uFEFF" or any(0x0600 <= ord(c) <= 0x06FF for c in t):
                        print(f'y={int(ln["bbox"][1]):4d} | RAW: {t}')
                        print(f'          | LOG: {logical(t)}')
        return 0
    print(logical(sys.argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
