#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse sunnah.com search results page."""
import re
import sys
import html as H

raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
print("PAGE SIZE:", len(raw))
links = re.findall(r'href="(/[^"]+)"', raw)
seen = []
for l in links:
    if re.match(r'^/(bukhari|muslim|tirmidhi|abudawud|nasai|ibnmajah|malik|nasai|dawud)[^"]*:[0-9]', l):
        if l not in seen:
            seen.append(l)
print("HADITH LINKS:", seen[:20])
# also grab snippet text around each
for m in re.finditer(r'<a[^>]+href="(/[^"]+:[0-9]+[a-z]?)"[^>]*>(.*?)</a>', raw, re.S):
    t = H.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))
    t = re.sub(r"\s+", " ", t).strip()
    if t:
        print(m.group(1), "=>", t[:100])
