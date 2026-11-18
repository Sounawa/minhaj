# -*- coding: utf-8 -*-
"""Extraction non lossy du htmlFr de la leçon pdf-mut23h2x-390 (hadith-3es, leçon 1)."""
import json, re, html

b = json.load(open('content/books/hadith-3es.json'))
les = [l for l in b['lessons'] if l['docId'] == 'pdf-mut23h2x-390']
h = les[0]['htmlFr']

# garde la structure : marque titres, gloses, parenthèses arabes
h2 = re.sub(r'<h2[^>]*>', '\n\n### ', h)
h2 = re.sub(r'<h3[^>]*>', '\n\n#### ', h2)
h2 = re.sub(r'<h4[^>]*>', '\n\n##### ', h2)
h2 = re.sub(r'<(p|li|div|tr)[^>]*>', '\n', h2)
h2 = re.sub(r'<(br|/tr)[^>]*>', '\n', h2)
h2 = re.sub(r'<(td|th)[^>]*>', ' | ', h2)
h2 = re.sub(r'<[^>]+>', '', h2)
h2 = html.unescape(h2)
h2 = re.sub(r'[ \t]+', ' ', h2)
h2 = re.sub(r'\n\s*\n+', '\n\n', h2)

open('/tmp/r731-lecon390.txt', 'w').write(h2)
print('car htmlFr:', len(les[0]['htmlFr']))
print('car texte extrait:', len(h2))
print('lignes:', h2.count('\n'))
