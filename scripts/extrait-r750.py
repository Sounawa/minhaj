# -*- coding: utf-8 -*-
"""Extraction non lossy du htmlFr des leçons pdf-11 et pdf-12 (hadith-5ep, leçons 11-12)."""
import json, re, html

b = json.load(open('content/books/hadith-5ep.json'))

def extract(doc_id, out):
    les = [l for l in b['lessons'] if l['docId'] == doc_id]
    h = les[0]['htmlFr']
    # garde la structure : marque titres, gloses, cellules de tableaux
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
    open(out, 'w').write(h2)
    print(doc_id, '→', out, ':', len(h), 'car htmlFr,', len(h2), 'car texte,', h2.count('\n'), 'lignes')

extract('pdf-11', '/tmp/r750-lecon11.txt')
extract('pdf-12', '/tmp/r750-lecon12.txt')
