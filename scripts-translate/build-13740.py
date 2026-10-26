#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les fragments 13740 et corrige les coquilles signalées."""
import io, re

frags = [f"/home/z/my-project/tr-tmp/13740.frag{i}.html" for i in range(1, 5)]
parts = []
for p in frags:
    with io.open(p, "r", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
html = "\n".join(parts) + "\n"

# coquilles relevées à la relecture
html = html.replace("le compte d’un seul", "le compte d’un seul")
html = html.replace("la compte", "le compte")
html = html.replace("à leur héritage", "à l’héritage")
html = html.replace("Troisièmement : les desseins", "Troisièmement : les desseins")
html = html.replace("le détachement", "le détachement")
html = html.replace("Sur la détachement", "Sur le détachement")
html = html.replace("t’est imposé ce que", "t’est imposé ce que")

with io.open("/home/z/my-project/tr-tmp/13740.html", "w", encoding="utf-8") as fh:
    fh.write(html)

n = len(html)
arabic = re.findall(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", html)
print(f"13740.html : {n} caractères, {len(arabic)} caractères arabes")
