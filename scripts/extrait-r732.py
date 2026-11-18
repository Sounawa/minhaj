# -*- coding: utf-8 -*-
"""Extraction non lossy des htmlFr des leçons hadith-tanawi-1 docIds 12925 et 12934."""
import json, re, html

b = json.load(open('content/books/hadith-tanawi-1.json'))
for docid, sortie in [('12925', '/tmp/r732-l1.txt'), ('12934', '/tmp/r732-l2.txt')]:
    les = [l for l in b['lessons'] if l['docId'] == docid]
    h = les[0]['htmlFr']
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
    open(sortie, 'w').write(h2)
    print(docid, '| htmlFr:', len(les[0]['htmlFr']), '| extrait:', len(h2), '| titleAr:', les[0].get('titleAr'))
