#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les fragments 13623 et corrige les coquilles signalées."""
import io, re

frags = [f"/home/z/my-project/tr-tmp/13623.frag{i}.html" for i in range(1, 6)]
parts = []
for p in frags:
    with io.open(p, "r", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
html = "\n".join(parts) + "\n"

# coquilles relevées à la relecture
html = html.replace("diverg­ence", "divergence")
html = html.replace("la voie la plus sûr", "la voie la plus sûre")
html = html.replace("qui résiderait dans", "qui réside dans")

with io.open("/home/z/my-project/tr-tmp/13623.html", "w", encoding="utf-8") as fh:
    fh.write(html)

n = len(html)
arabic = re.findall(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", html)
print(f"13623.html : {n} caractères, {len(arabic)} caractères arabes")
