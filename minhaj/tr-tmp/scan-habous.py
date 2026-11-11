#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan habous page for verse images (AhabousAR pattern)."""
import re
import sys
import urllib.parse

path = sys.argv[1]
html = open(path, encoding="utf-8", errors="replace").read()
print("SIZE:", len(html))
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
verse_imgs = [i for i in imgs if "AhabousAR" in urllib.parse.unquote(i)]
print(f"--- {len(verse_imgs)} verse images ---")
for i in verse_imgs:
    print("IMG:", urllib.parse.unquote(i))
if not verse_imgs:
    print(f"--- all {len(imgs)} images ---")
    for i in imgs[:30]:
        print("ALL:", urllib.parse.unquote(i)[:110])
