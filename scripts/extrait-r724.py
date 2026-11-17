#!/usr/bin/env python3
"""R724 — extraction de lecture (non lossy) des leçons pdf-mut23h2x-404 et
pdf-mut23h2x-403 du livre hadith-3es, pour rédaction des commentaires vague 8.
Même protocole que les tours précédents : blocs complets h/p/li/td (les spans
RTL internes ne coupent pas les paragraphes), re-wrap 180 caractères, l'arabe
et la translittération gardés tels quels."""
import json, re, textwrap, sys

LIVRE = 'content/books/hadith-3es.json'
DOCIDS = ['pdf-mut23h2x-404', 'pdf-mut23h2x-403']

livre = json.load(open(LIVRE))
docs = ([livre['intro']] if livre.get('intro') else []) + livre['lessons']
idx = {d['docId']: d for d in docs}

def blocs(html):
    """Extrait les blocs complets (h1-h6, p, li, td, dt, dd, figcaption)."""
    pat = re.compile(r'<(h[1-6]|p|li|td|dt|dd|figcaption|blockquote)[^>]*>(.*?)</\1>', re.S)
    hors = []
    for m in pat.finditer(html):
        t = re.sub(r'<[^>]+>', '', m.group(2))
        t = t.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&laquo;', '«').replace('&raquo;', '»')
        t = re.sub(r'\s+', ' ', t).strip()
        if t:
            hors.append(m.group(1) + ' | ' + t)
    return hors

for did in DOCIDS:
    d = idx[did]
    print('=' * 100)
    print('DOCID:', did, '| titleFr:', d.get('titleFr'), '| titleAr:', d.get('titleAr'))
    print('clés:', sorted(d.keys()))
    html = d.get('htmlFr') or d.get('html') or ''
    print('longueur htmlFr:', len(html))
    for b in blocs(html):
        print(textwrap.fill(b, 180))
        print('-')
