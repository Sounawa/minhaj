# -*- coding: utf-8 -*-
"""R631 — décodeur vrai-ordre de la couche miroir hadith-3es, leçon 2 (p.16-25).
Mécanique hadith3-decode-393.py (R628) : la couche PyMuPDF stocke chaque mot
lettres inversées ET l'ordre des mots inversé (rendu visuel LTR d'une ligne
RTL). Décodage vrai : reverse(lettres) de chaque mot, puis inversion de
l'ordre des mots de la ligne. Les runs de chiffres sont PROTÉGÉS (constat
R624/R628 : raw «901» = imprimé 901 ; le fix naïf les retourne — artefact),
conformément à la doctrine « jamais de chiffre cité sans preuve image » :
les numéros portés dans la leçon seront en outre TRANCHÉS CHIFFRE À CHIFFRE
sur recadrages (tr-tmp/qa-crops-r631/).
Entrée : tr-tmp/hadith3-l391-raw2.txt (p.16-25) — sortie :
tr-tmp/hadith3-l391-readable.txt (lecture vraie)."""
import re

SRC = "/home/z/my-project/tr-tmp/hadith3-l391-raw2.txt"
OUT = "/home/z/my-project/tr-tmp/hadith3-l391-readable.txt"

NUM = re.compile(r"^[0-9][0-9\s.,:%°\-–—]*$")


def true_line(s: str) -> str:
    words = s.split()
    out = []
    for w in words:
        core = w.strip(".,:;[]()«»?!-–—*·|<>{}=+_/\\'\"")
        if core and NUM.match(core):
            out.append(w)  # run de chiffres : ordre déjà imprimé
        else:
            out.append(w[::-1])
    out.reverse()  # ordre des mots : RTL -> vrai ordre de lecture
    return " ".join(out)


chunks = []
cur = None
buf = []
for line in open(SRC, encoding="utf-8").read().split("\n"):
    if line.startswith("===== PAGE"):
        if cur is not None:
            chunks.append((cur, "\n".join(buf)))
        cur, buf = line, []
    else:
        buf.append(true_line(line))
if cur is not None:
    chunks.append((cur, "\n".join(buf)))

with open(OUT, "w", encoding="utf-8") as f:
    for hdr, body in chunks:
        f.write(hdr + "\n" + body + "\n")
print(f"OK {OUT} — {sum(len(b) for _, b in chunks)} car décodés")
