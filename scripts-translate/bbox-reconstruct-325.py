#!/usr/bin/env python3
# Reconstruction RTL par lignes (bbox) du dars 27 — الحمل والمفقود, p.193-201
import re, unicodedata, subprocess, sys

DIAC = ''.join(unicodedata.normalize('NFKC', c) for c in '\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652\u0670\u06d6\u06d7\u06d8\u06d9\u06da\u06db')

def clean(s):
    # strip Arabic diacritics for the working file (kept in matn via VLM/careful read)
    return ''.join(c for c in s if c not in DIAC)

out = []
for p in range(193, 202):
    subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-bbox',
                    'content/textbooks/faraid-2-thanawi-text.pdf','/tmp/bb.xml'], check=True)
    xml = open('/tmp/bb.xml').read()
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', xml)
    lines = {}
    for xmin,ymin,xmax,ymax,w in words:
        key = round(float(ymin)/5)*5
        lines.setdefault(key, []).append((float(xmin), unicodedata.normalize('NFKC', w)))
    out.append(f"===== PAGE {p} =====")
    for key in sorted(lines):
        chars = sorted(lines[key])
        r2l = ''.join(c for _,c in sorted(chars, reverse=True))
        r2l = clean(r2l)
        if len(r2l.strip()) > 2:
            out.append(f"[y{key}] {r2l}")

open('content/textbooks/faraid-2-haml-mafqud-bbox.txt','w').write('\n'.join(out))
print('written', len(out), 'lines')
