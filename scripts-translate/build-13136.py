#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les fragments 13136 et corrige les coquilles signalées."""
import io, re

frags = [f"/home/z/my-project/tr-tmp/13136.frag{i}.html" for i in range(1, 6)]
parts = []
for p in frags:
    with io.open(p, "r", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
html = "\n".join(parts) + "\n"

# coquilles
html = html.replace("qu’Mālik", "que Mālik")
html = html.replace("de la affliction", "de l’affliction")
html = html.replace("ce qu’Mālik rapporte", "ce que Mālik rapporte")

with io.open("/home/z/my-project/tr-tmp/13136.html", "w", encoding="utf-8") as fh:
    fh.write(html)

n = len(html)
arabic = re.findall(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", html)
print(f"13136.html : {n} caractères, {len(arabic)} caractères arabes")
