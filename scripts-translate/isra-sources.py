#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Extracteur PDF→slot, annexe sources et références (p.214-220)
→ tr-tmp/isra-sources-readable.txt

Même mécanique que isra-readable.py (R458-R462) : décodage mot-à-mot (fix_line
d'isra-map.py) puis ré-inversion de la séquence des mots de chaque ligne.
R485 : la page imprimée 214 ouvre déjà la rubrique المصادر والمراجع (tranchage
par le contenu) — périmètre du slot pdf-mut23h3c-738 = pages 214 à 220.
"""
import importlib.util

import fitz

_spec = importlib.util.spec_from_file_location(
    "isra_map", "/home/z/my-project/scripts-translate/isra-map.py")
isra_map = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(isra_map)
PDF, fix_line = isra_map.PDF, isra_map.fix_line

RANGE = (214, 220)   # p.214 = début de la rubrique (matière du slot 738)


def readable(fixed: str) -> str:
    out = []
    for line in fixed.split("\n"):
        words = line.split()
        out.append(" ".join(reversed(words)) if len(words) > 1 else line)
    return "\n".join(out)


def main() -> None:
    doc = fitz.open(PDF)
    lo, hi = RANGE
    lines = [f"SOURCES — les sources et références — slot pdf-mut23h3c-738 — pages {lo}-{hi}",
             "=" * 70, ""]
    for p in range(lo, hi + 1):
        raw = doc[p - 1].get_text()
        fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
        lines.append(f"===== PAGE {p} (brut mot-décodé) =====")
        lines.append(fixed)
        lines.append("")
        lines.append(f"===== PAGE {p} (LISIBLE — mots ré-inversés) =====")
        lines.append(readable(fixed))
        lines.append("")
    out_path = "/home/z/my-project/tr-tmp/isra-sources-readable.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"OK {out_path} ({sum(len(x) for x in lines)} car)")


if __name__ == "__main__":
    main()
