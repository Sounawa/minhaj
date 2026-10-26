#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan de complétion des livres : repère les livres EN COURS et les docs LIBRES."""
import json, os

HOME = '/home/z/my-project'
REG = f'{HOME}/scripts-translate/savant-registry.json'
BOOKS = f'{HOME}/content/books'

reg = json.load(open(REG))
hand = set(e.split(':')[0].strip() for e in reg['hand'])
llm = set(reg['llm'].keys())

rows = []
for fn in sorted(os.listdir(BOOKS)):
    if not fn.endswith('.json'):
        continue
    b = json.load(open(os.path.join(BOOKS, fn)))
    lessons = b.get('lessons', [])
    intro = b.get('intro') or {}
    docs = list(lessons) + ([intro] if intro else [])
    n = len(docs)
    n_hand = sum(1 for d in docs if (d.get('htmlFr') or '') and str(d.get('docId')) in hand)
    n_llm = sum(1 for d in docs if (d.get('htmlFr') or '') and str(d.get('docId')) in llm)
    n_gt = sum(1 for d in docs if (d.get('htmlFr') or '') and str(d.get('docId')) not in hand and str(d.get('docId')) not in llm)
    n_vide = sum(1 for d in docs if not (d.get('htmlFr') or ''))
    # docs hand d'un livre donné (ids)
    rows.append((fn[:-5], n, n_hand, n_llm, n_gt, n_vide))

print(f"{'livre':28} {'docs':>4} {'hand':>4} {'llm':>4} {'gt':>4} {'vide':>4}  état")
en_cours = []
for name, n, nh, nl, ngt, nv in rows:
    couvert = nh + nl
    if couvert == 0:
        etat = 'VIERGE'
    elif couvert == n:
        etat = 'COMPLET'
    else:
        etat = 'EN COURS'
        en_cours.append((name, n, nh, nl, ngt, nv))
    print(f"{name:28} {n:4} {nh:4} {nl:4} {ngt:4} {nv:4}  {etat}")

print()
print('=== LIVRES EN COURS ===')
for name, n, nh, nl, ngt, nv in en_cours:
    print(f"{name:28} {nh+nl}/{n} couverts (hand {nh}, llm {nl}, gt {ngt}, vide {nv})")
