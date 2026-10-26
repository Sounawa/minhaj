#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les fragments 13624 et corrige les coquilles signalées."""
import io, re

frags = [f"/home/z/my-project/tr-tmp/13624.frag{i}.html" for i in range(1, 5)]
parts = []
for p in frags:
    with io.open(p, "r", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
html = "\n".join(parts) + "\n"

# coquilles relevées à la relecture
html = html.replace("l’uncle-ité", "l’oncle-ité")
html = html.replace("La milket", "La grille")
html = html.replace("donner permission", "donner la permission")
html = html.replace("est, en prohibition, au rang", "est, en prohibé, au rang")
html = html.replace("le milket de Khalīl", "la grille de Khalīl")

with io.open("/home/z/my-project/tr-tmp/13624.html", "w", encoding="utf-8") as fh:
    fh.write(html)

n = len(html)
arabic = re.findall(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", html)
print(f"13624.html : {n} caractères, {len(arabic)} caractères arabes")
