# -*- coding: utf-8 -*-
"""Extraction non lossy du htmlFr + html (arabe) de la leçon pdf-17 (hadith-5ep, leçon 17 — ترك ما لا يعني)."""
import json, re, html

b = json.load(open('content/books/hadith-5ep.json'))

def extract(doc_id, champ, out):
    les = [l for l in b['lessons'] if l['docId'] == doc_id]
    h = les[0][champ]
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
    print(doc_id, champ, '→', out, ':', len(h), 'car html,', len(h2), 'car texte,', h2.count('\n'), 'lignes')

extract('pdf-17', 'htmlFr', '/tmp/r754-lecon17-fr.txt')
extract('pdf-17', 'html', '/tmp/r754-lecon17-ar.txt')
# en plus : leçon 16 (préparation qui annonce les exigences de la leçon 17)
extract('pdf-16', 'htmlFr', '/tmp/r754-lecon16-fr.txt')
