#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R690 — extraction des renvois [الموطأ رقم: N] du calque brut p152-158.
Les chiffres sont latins dans le calque ('994]'). Sort page, y, nombre."""
import fitz, re

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)

pat_dig = re.compile(r'^[\[\(]?(\d{2,4})[\]\)]')
pat = re.compile(r'\]|\[')

for pno in range(152, 159):
    page = doc[pno - 1]
    words = page.get_text("words")
    hits = []
    for w in words:
        t = w[4]
        m = pat_dig.match(t)
        if m and (']' in t or '[' in t or ']' in words[max(0,words.index(w)-1)][4] if False else True):
            pass
    # plus simple : mots chiffre+crochet
    for w in words:
        t = w[4]
        m = re.search(r'(\d{2,4})\]', t)
        if m:
            hits.append((w[1], w[0], m.group(1), 'X]'))
        elif re.match(r'^\[\d{2,4}$', t):
            hits.append((w[1], w[0], m.group(1) if (m:=re.search(r'\[(\d{2,4})', t)) else '', '[N'))
        elif re.fullmatch(r'\d{2,4}', t) and (':' in ' '.join(x[4] for x in words[max(0,words.index(w)-3):words.index(w)]) or True):
            # chiffre isolé : contexte proche
            idx = words.index(w)
            ctx = ' '.join(x[4] for x in words[max(0, idx-4):idx+2])
            if 'اطوملا' in ctx or 'مقر' in ctx or 'ةروس' in ctx or 'ةيآلا' in ctx:
                hits.append((w[1], w[0], t, 'iso'))
    hits.sort()
    print(f"===== PAGE {pno} =====")
    for y, x, n, kind in hits:
        print(f"  y={y:.0f} x={x:.0f} NUM={n} ({kind})")
