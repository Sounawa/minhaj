# -*- coding: utf-8 -*-
"""R628 — décodeur vrai-ordre de la couche miroir hadith-3es.
La couche PyMuPDF stocke chaque mot lettres inversées ET l'ordre des mots
inversé (rendu visuel LTR d'une ligne RTL). Décodage vrai : reverse(lettres)
de chaque mot, puis inversion de l'ordre des mots de la ligne.
Les chiffres arabes-européens de la couche sont déjà à l'ordre imprimé
(constaté R624 : raw «901» = imprimé 901 ; le fix simple les retourne en
«109» — artefact, PAS l'imprimé). On garde donc les runs de chiffres tels
quels dans le décodage (regex protected), conformément au constat R624/R628.
Sortie : tr-tmp/hadith3-l393-readable.txt (lecture vraie, p.30-39)."""
import re

SRC = "/home/z/my-project/tr-tmp/hadith3-l393-raw.txt"
OUT = "/home/z/my-project/tr-tmp/hadith3-l393-readable.txt"

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
