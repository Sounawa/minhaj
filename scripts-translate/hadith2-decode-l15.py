#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — décodage lisible de l'extraction OCR l15 (mots inversés → lisibles).
Réutilise fix_line/readable de hadith2-map.py (méthode documentée là-bas)."""
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "hadith2_map", "/home/z/my-project/scripts-translate/hadith2-map.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
fix_line, readable = _mod.fix_line, _mod.readable

SRC = "/home/z/my-project/tr-tmp/hadith2-l15-readable.txt"
OUT = "/home/z/my-project/tr-tmp/hadith2-l15-decoded.txt"

raw = open(SRC, encoding="utf-8").read()
out = []
for block in raw.split("===== PAGE "):
    if not block.strip():
        continue
    num, _, body = block.partition("=====")
    body = body.replace("=====\n", "")
    out.append(f"===== PAGE {num.strip()} =====")
    fixed = "\n".join(fix_line(l) for l in body.split("\n"))
    out.append(readable(fixed))
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(f"OK {OUT}")
