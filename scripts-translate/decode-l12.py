# -*- coding: utf-8 -*-
"""Minhāj — Décodage OCR leçon 12 (slot pdf-13, R551).
Applique fix_line (inversion caractères par mot) + readable (ré-inversion
séquence mots) de hadith2-map.py au fichier brut d'extraction.
Entrée : tr-tmp/hadith2-l12-readable.txt (p.85-91)
Sortie : tr-tmp/hadith2-l12-decoded.txt"""
import re

RAW = "/home/z/my-project/tr-tmp/hadith2-l12-readable.txt"
OUT = "/home/z/my-project/tr-tmp/hadith2-l12-decoded.txt"


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def readable(fixed: str) -> str:
    out = []
    for line in fixed.split("\n"):
        words = line.split()
        out.append(" ".join(reversed(words)) if len(words) > 1 else line)
    return "\n".join(out)


raw = open(RAW, encoding="utf-8").read()
out_lines = []
for line in raw.split("\n"):
    if re.match(r"^===== PAGE \d+ =====$", line.strip()) or not line.strip():
        out_lines.append(line)
    else:
        out_lines.append(readable(fix_line(line)))
open(OUT, "w", encoding="utf-8").write("\n".join(out_lines))
print(f"OK {OUT} — {sum(len(l) for l in out_lines)} car")
