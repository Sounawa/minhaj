#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Extracteur PDF→annexe tafsir-5ep, version lisible (R529).
Usage : python3 scripts-translate/kahf-annex-readable.py <765|766|767>
       → tr-tmp/kahf-annex-<N>-readable.txt"""
import importlib.util
import sys

_spec = importlib.util.spec_from_file_location(
    "kahf_map", "/home/z/my-project/scripts-translate/kahf-map.py")
kahf_map = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kahf_map)


def readable(fixed: str) -> str:
    out = []
    for line in fixed.split("\n"):
        words = line.split()
        out.append(" ".join(reversed(words)) if len(words) > 1 else line)
    return "\n".join(out)


def main() -> None:
    docid = int(sys.argv[1])
    d = kahf_map.extract_annex(docid)
    lo, hi = d["pages"]
    lines = [f"KAHF ANNEXE slot {d['slot']} — pages {lo}-{hi}",
             "=" * 70, ""]
    for p in range(lo, hi + 1):
        fx = d["content"][p]["fixed"]
        lines.append(f"===== PAGE {p} (LISIBLE — mots ré-inversés) =====")
        lines.append(readable(fx))
        lines.append("")
    out_path = f"/home/z/my-project/tr-tmp/kahf-annex-{docid}-readable.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"OK {out_path} ({sum(len(x) for x in lines)} car)")


if __name__ == "__main__":
    main()
