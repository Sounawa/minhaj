# -*- coding: utf-8 -*-
"""R343 — Passe 3 : tokens exacts (points de code) pour trancher فردى/فرادى، بُصْرى، مفترى، تترا، هذين."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def tokens(sn, an):
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            b = bare(tx)
            return b.split()
    return []

def charcode(w):
    return ' '.join(f'{c}(U+{ord(c):04X})' for c in w)

def hunt(skel):
    """retourne (sn, an, token) pour chaque token contenant skel"""
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        for w in b.split():
            if skel in w:
                out.append((sn, an, w))
    return out

print('=== A. Tokens f-r-d (فرد) — distinguer فردى élidée vs فرادى/فردا ===')
seen = {}
for (sn, an, w) in hunt('فرد'):
    seen.setdefault(w, []).append((sn, an))
for w, poss in sorted(seen.items()):
    print(f'  TOKEN «{w}» ×{len(poss)} → {poss[:6]}')
    print(f'    {charcode(w)}')

print()
print('=== B. Tokens بصر/بشر — chercher بُصْرَى / بُشْرَى ===')
seen = {}
for (sn, an, w) in hunt('بصر') + hunt('بشر'):
    seen.setdefault(w, []).append((sn, an))
for w, poss in sorted(seen.items()):
    if len(poss) <= 3 or ('بصري' in w or 'بشري' in w or w in ('بصري','بشري','بصري','بصرة','بشرة')):
        print(f'  TOKEN «{w}» ×{len(poss)} → {poss[:5]}')

print()
print('=== C. Tokens فتر (muftran hunt) ===')
seen = {}
for (sn, an, w) in hunt('فتر'):
    seen.setdefault(w, []).append((sn, an))
for w, poss in sorted(seen.items()):
    print(f'  TOKEN «{w}» ×{len(poss)} → {poss[:6]}')

print()
print('=== D. تترا 23:44 — point de code ===')
for w in tokens(23, 44):
    if 'تتر' in w:
        print(f'  TOKEN «{w}» : {charcode(w)}')

print()
print('=== E. هذYن — pourquoi 0 ? tokens contenant ذين/ذين ===')
seen = {}
for (sn, an, tx) in corpus:
    for w in bare(tx).split():
        if 'ذين' in w or 'ذين' in w:
            seen.setdefault(w, []).append((sn, an))
for w, poss in sorted(seen.items())[:12]:
    print(f'  TOKEN «{w}» ×{len(poss)} → {poss[:4]}')

print()
print('=== F. قرى exact (34:18, 59:14) ===')
for (sn, an) in [(34,18),(59,14)]:
    for w in tokens(sn, an):
        if w in ('قرى','قرى','القرى','القرى'):
            print(f'  {sn}:{an} TOKEN «{w}» : {charcode(w)}')

print()
print('=== G. Textes complets pour la rédaction ===')
for (sn, an) in [(100,3),(2,46),(2,156),(21,93),(23,60),(13,5),(27,67),(78,40),(16,81),(14,50),(26,61),(8,48),(23,44),(90,8),(16,76),(18,32),(5,23),(22,19),(6,94),(19,80),(19,95),(21,89),(34,46),(34,18),(59,14),(2,282),(28,15)]:
    print(f'--- {sn}:{an} : ' + ' '.join(bare(' '.join(tokens(sn, an))).split())[:330])
