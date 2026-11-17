#!/usr/bin/env python3
"""Vérification indépendante R716 : registres savants ↔ corpus content/books.
Répond à la question utilisateur : combien de traductions savantes réellement ?"""
import json, glob, os, sys
from collections import OrderedDict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def charge(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)

# 1) Les trois registres
regs = OrderedDict()
for nom, chemin in [
    ('racine (périmé ?)', os.path.join(REPO, 'savant-registry.json')),
    ('scripts-translate (fait foi)', os.path.join(REPO, 'scripts-translate', 'savant-registry.json')),
    ('scripts-ia2 (sous-registre)', os.path.join(REPO, 'scripts-ia2', 'savant-registry-ia2.json')),
]:
    if os.path.exists(chemin):
        d = charge(chemin)
        regs[nom] = d
        print(f'REGISTRE {nom} : clés={list(d.keys())}')
        ids = set()
        for k, v in d.items():
            if isinstance(v, list):
                print(f'  {k}: {len(v)} ids (list)')
                ids |= set(v)
            elif isinstance(v, dict):
                print(f'  {k}: {len(v)} entrées (dict)')
                ids |= set(v.keys())
            else:
                print(f'  {k}: {type(v).__name__}')
        regs[nom] = ids
        print(f'  → total ids uniques : {len(ids)}')

union = set()
for ids in regs.values():
    union |= ids
print(f'UNION des 3 registres : {len(union)} docIds')

# 2) Corpus : intros + leçons
total_docs = 0; avec_fr = 0; sans_fr = 0; pdf_only = 0
docs_fr = set()
livres = []
for chemin in sorted(glob.glob(os.path.join(REPO, 'content', 'books', '*.json'))):
    livre = os.path.basename(chemin)[:-5]
    d = charge(chemin)
    n_livre = 0; fr_livre = 0
    for k, v in d.items():
        if not isinstance(v, list):
            continue
        for doc in v:
            if not isinstance(doc, dict):
                continue
            docid = doc.get('docId') or doc.get('id') or ''
            if not docid:
                continue
            n_livre += 1
            fr = (doc.get('htmlFr') or '').strip()
            if fr:
                fr_livre += 1
                avec_fr += 1
                docs_fr.add(docid)
            else:
                sans_fr += 1
                if doc.get('pdfOnly'):
                    pdf_only += 1
    if n_livre:
        total_docs += n_livre
        livres.append((livre, n_livre, fr_livre))
print(f'\nCORPUS : {total_docs} documents (leçons + intros) sur {len(livres)} livres')
print(f'  avec htmlFr : {avec_fr}')
print(f'  sans htmlFr : {sans_fr} (dont {pdf_only} slots pdfOnly)')
print(f'  docIds uniques avec FR : {len(docs_fr)}')

# 3) Couverture registre ↔ corpus
couverts = docs_fr & union
orphelins = docs_fr - union
fantomes = union - docs_fr
print(f'\nCOUVERTURE : {len(couverts)}/{len(docs_fr)} documents FR inscrits au registre')
print(f'  FR non inscrits : {len(orphelins)}')
print(f'  ids registre sans doc FR (fantômes) : {len(fantomes)}')

# 4) Répartition par zone (primaire *-ep vs secondaire)
prim = [(l, n, f) for l, n, f in livres if l.endswith('ep')]
sec = [(l, n, f) for l, n, f in livres if not l.endswith('ep')]
for nom, zone in (('PRIMAIRE (zone IA-2)', prim), ('SECONDAIRE (zone IA-1)', sec)):
    n_docs = sum(x[1] for x in zone); n_fr = sum(x[2] for x in zone)
    restants = sorted(((l, n - f) for l, n, f in zone if f < n), key=lambda x: -x[1])
    print(f'\n{nom} : {len(zone)} livres, {n_docs} docs, {n_fr} avec FR, {n_docs - n_fr} sans FR')
    for l, r in restants[:12]:
        print(f'    {l}: {r} à transcrire')
