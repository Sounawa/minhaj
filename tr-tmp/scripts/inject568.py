#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 568 (pdf-only) bilingue dans tafsir-2es.json."""
import json, os, tempfile

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
AR = "/home/z/my-project/tr-tmp/568-ar.html"
FR = "/home/z/my-project/tr-tmp/568-fr.html"
DOCID = "pdf-mut23h33-568"

html = open(AR, encoding="utf-8").read().strip()
html_fr = open(FR, encoding="utf-8").read().strip()
assert html.startswith("<h1>") and html_fr.startswith("<h1>")
assert "{{U" not in html_fr and "<img" not in html_fr

data = json.load(open(BOOK, encoding="utf-8"))
hit = 0
for les in data["lessons"]:
    if les.get("docId") == DOCID:
        les["html"] = html
        les["htmlFr"] = html_fr
        les["pdfOnly"] = False
        hit += 1
assert hit == 1, f"expected 1 lesson, hit {hit}"

d = os.path.dirname(BOOK)
fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
os.replace(tmp, BOOK)
print(f"OK {DOCID} injecte ({len(html)} car AR, {len(html_fr)} car FR)")
