#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatène les fragments 13124 et corrige les coquilles signalées."""
import io, re

frags = [f"/home/z/my-project/tr-tmp/13124.frag{i}.html" for i in range(1, 6)]
parts = []
for p in frags:
    with io.open(p, "r", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
html = "\n".join(parts) + "\n"

# coquilles
html = html.replace("a institutée", "a instituée")
html = html.replace("qu’Mālik", "que Mālik")

with io.open("/home/z/my-project/tr-tmp/13124.html", "w", encoding="utf-8") as fh:
    fh.write(html)

n = len(html)
arabic = re.findall(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", html)
print(f"13124.html : {n} caractères, {len(arabic)} caractères arabes")
