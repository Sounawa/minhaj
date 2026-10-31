#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Extracteur PDF→slot, étape 2 : version lisible d'une leçon du miroir.

Établi R458-R462 : la couche texte OCR du manuel miroir (tafsir-2-thanawi_text.pdf)
porte chaque mot en caractères inversés (ordre visuel). isra-map.py rétablit
l'ordre des LETTRES dans chaque mot ; le décodage complet exige EN OUTRE la
ré-inversion de la SÉQUENCE DES MOTS de chaque ligne (l'ordre visuel place le
dernier mot de la phrase arabe en premier).

Usage : python3 scripts-translate/isra-readable.py <N>   # leçon N → tr-tmp/isra-lN-readable.txt
Sortie : tr-tmp/isra-lN-readable.txt (brut «fixed» + section «lisible»).
"""
import importlib.util
import sys

import fitz

_spec = importlib.util.spec_from_file_location(
    "isra_map", "/home/z/my-project/scripts-translate/isra-map.py")
isra_map = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(isra_map)
PDF, STARTS, FIHRIS, extract = (isra_map.PDF, isra_map.STARTS,
                                isra_map.FIHRIS, isra_map.extract)


def readable(fixed: str) -> str:
    """Ré-inverse la séquence des mots de chaque ligne déjà décodée mot à mot."""
    out = []
    for line in fixed.split("\n"):
        words = line.split()
        out.append(" ".join(reversed(words)) if len(words) > 1 else line)
    return "\n".join(out)


def main() -> None:
    n = int(sys.argv[1])
    d = extract(n)
    lo, hi = d["pages"]
    lines = [f"LEÇON {n} — slot {d['slot']} — {d['verses']} — pages {lo}-{hi}",
             "=" * 70, ""]
    for p in range(lo, hi + 1):
        fx = d["content"][p]["fixed"]
        lines.append(f"===== PAGE {p} (brut mot-décodé) =====")
        lines.append(fx)
        lines.append("")
        lines.append(f"===== PAGE {p} (LISIBLE — mots ré-inversés) =====")
        lines.append(readable(fx))
        lines.append("")
    out_path = f"/home/z/my-project/tr-tmp/isra-l{n}-readable.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"OK {out_path} ({len(chr(10).join(lines))} car)")


if __name__ == "__main__":
    main()
