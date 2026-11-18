# -*- coding: utf-8 -*-
"""R747 — vérification des citations : chaque fragment « ... » des entrées
pdf-7/pdf-8 doit apparaître (après normalisation espaces/fines/apostrophes)
dans les textes des leçons (pdf-5..pdf-8 concaténés)."""
import json, re, html, unicodedata

def plain(h):
    h2 = re.sub(r'<(p|li|div|tr|h[1-6]|br)[^>]*>', ' ', h)
    h2 = re.sub(r'<[^>]+>', '', h2)
    h2 = html.unescape(h2)
    h2 = unicodedata.normalize('NFC', h2)
    h2 = h2.replace('\u202f', ' ').replace('\u00a0', ' ')
    h2 = h2.replace('’', "'")
    h2 = re.sub(r'\s+', ' ', h2)
    return h2

def norme_frag(s):
    s = unicodedata.normalize('NFC', s)
    s = s.replace('\u202f', ' ').replace('\u00a0', ' ')
    s = re.sub(r'["""«»“”]', '', s)
    s = s.replace('\u2019', '\u02BE').replace("'", '\u02BE')
    s = s.replace('\u02BF', '\u02BE')
    s = s.lower()
    s = re.sub(r'\s+', ' ', s)
    return s

b = json.load(open('content/books/hadith-5ep.json'))
corpus = ''
for did in ('pdf-5', 'pdf-6', 'pdf-7', 'pdf-8'):
    l = [x for x in b['lessons'] if x['docId'] == did][0]
    corpus += ' ' + norme_frag(plain(l['htmlFr']))

d = json.load(open('content/commentaires/hadith-5ep.json'))
manques_total = 0
for did in ('pdf-7', 'pdf-8'):
    e = d['commentaires'][did]
    textes = [e['resume']] + e['explication'] + e['points']
    frags = []
    for t in textes:
        for m in re.findall(r'«([^»]+)»', t):
            frags.append(m.strip())
    print(f'=== {did} : {len(frags)} fragments « » ===')
    for f in frags:
        c = norme_frag(f)
        if len(c) < 12:
            continue
        if c not in corpus:
            manques_total += 1
            print('  MANQUE :', c[:110])
print('fragments non retrouvés :', manques_total)
