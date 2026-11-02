#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Extracteur PDF→slot, version lisible d'une leçon du manuel miroir
hadith-2-iadadi (Muwaṭṭaʾ/Zarqānī 2ᵉ collégial) — miroir de kahf-readable.py
pour la carte hadith2-map.py (même mécanique R458/R487 : décodage mot-à-mot
puis ré-inversion de la SÉQUENCE DES MOTS de chaque ligne).

Usage :
  python3 scripts-translate/hadith2-readable.py <N>      # leçon N (1..28)
  python3 scripts-translate/hadith2-readable.py <29|30>  # annexes (fihris/sources)
→ tr-tmp/hadith2-lN-readable.txt
"""
import importlib.util
import sys

_spec = importlib.util.spec_from_file_location(
    "hadith2_map", "/home/z/my-project/scripts-translate/hadith2-map.py")
hadith2_map = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hadith2_map)
extract = hadith2_map.extract
extract_annex = hadith2_map.extract_annex
readable = hadith2_map.readable


def main() -> None:
    n = int(sys.argv[1])
    if n in (29, 30):
        d = extract_annex(n)
        lo, hi = d["pages"]
        lines = [f"HADITH-2 ANNEXE {n} — slot {d['slot']} — pages {lo}-{hi}",
                 "=" * 70, ""]
        out_path = f"/home/z/my-project/tr-tmp/hadith2-annex-{n}-readable.txt"
    else:
        d = extract(n)
        lo, hi = d["pages"]
        lines = [f"HADITH-2 LEÇON {n} — slot {d['slot']} — {d['label']} — pages {lo}-{hi}",
                 "=" * 70, ""]
        for p in range(lo, hi + 1):
            fx = d["content"][p]["fixed"]
            lines.append(f"===== PAGE {p} (brut mot-décodé) =====")
            lines.append(fx)
            lines.append("")
            lines.append(f"===== PAGE {p} (LISIBLE — mots ré-inversés) =====")
            lines.append(readable(fx))
            lines.append("")
        out_path = f"/home/z/my-project/tr-tmp/hadith2-l{n}-readable.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"OK {out_path} ({len(chr(10).join(lines))} car)")


if __name__ == "__main__":
    main()
