# -*- coding: utf-8 -*-
"""Extraction non lossy du htmlFr + html (arabe) de la leçon pdf-19 (hadith-5ep, leçon 19 — من خصال الإيمان).
En plus : leçon 18 (préparation précédente) pour le iʿdād."""
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

extract('pdf-19', 'htmlFr', '/tmp/r756-lecon19-fr.txt')
extract('pdf-19', 'html', '/tmp/r756-lecon19-ar.txt')
extract('pdf-18', 'htmlFr', '/tmp/r756-lecon18-fr.txt')
