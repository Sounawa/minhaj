#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom1-h6-15 : localisateur de lignes (TSV tesseract 600 dpi, psm 6)
# Affiche les groupes de mots par ligne avec coordonnées y (px @600dpi)
# pour cibler les bandes à recadrer en 1200 dpi. Pages L14 = 81-84.
import subprocess, os, re, sys

DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

pages = [int(a) for a in sys.argv[1:]] or [81, 82, 83, 84]

for p in pages:
    png = f"{DIR}/t{p:03d}.png"
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6", "tsv"],
                       env=env, capture_output=True, text=True)
    lines = {}
    for row in r.stdout.splitlines()[1:]:
        c = row.split("\t")
        if len(c) < 12 or not c[11].strip():
            continue
        top, h = int(c[7]), int(c[9])
        key = (c[2], c[3], c[4])  # block, par, line
        lines.setdefault(key, []).append((top, h, c[11]))
    print(f"\n════════ PAGE {p} — lignes TSV (y_min → y_max @600dpi) ════════")
    for key in sorted(lines, key=lambda k: min(w[0] for w in lines[k])):
        ws = lines[key]
        y0 = min(w[0] for w in ws)
        y1 = max(w[0] + w[1] for w in ws)
        text = " ".join(w[2] for w in ws)
        if len(text) > 95:
            text = text[:92] + "..."
        print(f"  y[{y0:4d}-{y1:4d}] {text}")
