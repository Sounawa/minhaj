#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R691 — couche texte PDF leçon 413 hadith-3es (la uḍḥiya, p.158-165)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)
print("pages PDF:", doc.page_count)
for pno in range(158, 166):  # 1-based
    page = doc[pno - 1]
    txt = page.get_text("text")
    print(f"\n════════ p.{pno} ({len(txt)} car) ════════")
    print(txt)
