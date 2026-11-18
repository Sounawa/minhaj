# -*- coding: utf-8 -*-
"""Extraction non lossy du htmlFr des leçons 12959-12966 (hadith-tanawi-1, leçons 5-6)."""
import json, re, html

b = json.load(open('content/books/hadith-tanawi-1.json'))
les = [l for l in b['lessons'] if l['docId'] in ('12959', '12966')]
for l in les:
    h = l['htmlFr']
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
    fn = '/tmp/r734-lecon' + l['docId'] + '.txt'
    open(fn, 'w').write(h2)
    print('ecrit', fn, '| car htmlFr:', len(h), '| car extrait:', len(h2), '| lignes:', h2.count('\n'))
