#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Extracteur PDF→slot, version lisible d'une leçon du manuel miroir
al-Kahf (tafsir-3-thanawi_text.pdf) — miroir de isra-readable.py pour la
carte kahf-map.py (même mécanique R458/R487 : décodage mot-à-mot puis
ré-inversion de la SÉQUENCE DES MOTS de chaque ligne).

Usage : python3 scripts-translate/kahf-readable.py <N>   # leçon N → tr-tmp/kahf-lN-readable.txt
"""
import importlib.util
import sys

_spec = importlib.util.spec_from_file_location(
    "kahf_map", "/home/z/my-project/scripts-translate/kahf-map.py")
kahf_map = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kahf_map)
extract = kahf_map.extract


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
    lines = [f"KAHF LEÇON {n} — slot {d['slot']} — {d['verses']} — pages {lo}-{hi}",
             "=" * 70, ""]
    for p in range(lo, hi + 1):
        fx = d["content"][p]["fixed"]
        lines.append(f"===== PAGE {p} (brut mot-décodé) =====")
        lines.append(fx)
        lines.append("")
        lines.append(f"===== PAGE {p} (LISIBLE — mots ré-inversés) =====")
        lines.append(readable(fx))
        lines.append("")
    out_path = f"/home/z/my-project/tr-tmp/kahf-l{n}-readable.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"OK {out_path} ({len(chr(10).join(lines))} car)")


if __name__ == "__main__":
    main()
