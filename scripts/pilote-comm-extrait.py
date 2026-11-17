#!/usr/bin/env python3
"""Extrait le contenu des leçons pilotes pour rédiger les commentaires."""
import json, os, re, sys
from html.parser import HTMLParser

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blobs = []          # (type, texte)
        self._buf = []
        self._type = None

    def handle_starttag(self, tag, attrs):
        if tag in ('h1', 'h2', 'h3', 'p', 'li', 'tr'):
            self._type = tag
            self._buf = []
        if tag == 'span':
            d = dict(attrs)
            if d.get('dir') == 'rtl':
                self._type = 'ar'

    def handle_endtag(self, tag):
        if tag in ('h1', 'h2', 'h3', 'p', 'li', 'tr', 'span') and self._type:
            t = ''.join(self._buf).strip()
            if t:
                self.blobs.append((self._type, t))
            self._type = None
            self._buf = []

    def handle_data(self, data):
        if self._type:
            self._buf.append(data)

def dump(slug, docid):
    chemin = os.path.join(REPO, 'content', 'books', slug + '.json')
    data = json.load(open(chemin, encoding='utf-8'))
    docs = list(data.get('lessons') or [])
    if data.get('intro'):
        docs.insert(0, {'docId': 'introduction', **data['intro']})
    cible = None
    for d in docs:
        if str(d.get('docId')) == docid:
            cible = d
            break
    if not cible:
        print(f'!! {slug}:{docid} introuvable — FR disponibles :')
        for d in docs:
            if (d.get('htmlFr') or '').strip():
                n = len(d['htmlFr'])
                print(f'   {d["docId"]:28s} {n:7d} car  {d.get("titleFr", "")[:60]}')
        return False
    p = P()
    p.feed(cible['htmlFr'])
    print(f'===== {slug} / {docid} — {cible.get("titleFr", "")} | {cible.get("titleAr", "")} — {len(cible["htmlFr"])} car =====')
    for typ, t in p.blobs[int(os.environ.get('COMM_DEBUT', '0')):int(os.environ.get('COMM_DEBUT', '0')) + 60]:
        print(f'[{typ}] {t[:220]}')
    return True

ok = True
for slug, docid in [('hadith-3es', sys.argv[1] if len(sys.argv) > 1 else 'pdf-mut23h2x-413'),
                    ('hadith-3es', sys.argv[2] if len(sys.argv) > 2 else 'pdf-mut23h2x-414')]:
    ok = dump(slug, docid) and ok
    print()
sys.exit(0 if ok else 1)
