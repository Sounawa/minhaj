#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R721 — correction du livre hadith-tanawi-3 : remplacement des séquences
« ?? » par une espace dans les htmlFr.

Contexte : le livre hadith-tanawi-3 a été transcrit par l'IA-1 elle-même
(tours R700-R712, avant le protocole trois-IA — l'historique git montre
l'auteur « Z User » avec traces r701-r710-ht3). Son pipeline d'extraction
PDF de l'époque perdait le glyphe d'espace inter-mots de la fonte arabe
vocalisée : chaque espace devenait 2 caractères « ? ». Vérifié :
  - 15 412 « ?? » dans les htmlFr (9 leçons), toujours en frontière de mot
    (précédés d'une lettre/harakat finale, suivis d'une espace, d'une
    ponctuation ou d'une balise fermante) ;
  - le champ arabe `html` est propre (0 « ?? ») ;
  - les 82 « ? » isolés restants sont des points d'interrogation français
    légitimes — intouchés ;
  - aucun claim IA-3 sur ce livre (les passes IA-3 W5-W11 portent sur
    fiqh-tanawi-3 et ulum-hadith-tanawi-1).
Correction : remplacement mécanique « ?? » → « » (espace) dans les SEULS
champs htmlFr ; re-dump indent=2 ensure_ascii=False (round-trip vérifié
identique au format du fichier). Zéro autre changement.
"""

import hashlib
import json
from pathlib import Path

FICHIER = Path(__file__).resolve().parent.parent / 'content' / 'books' / 'hadith-tanawi-3.json'


def sha256(fichier):
    return hashlib.sha256(fichier.read_bytes()).hexdigest()


def principal():
    avant = sha256(FICHIER)
    raw = FICHIER.read_text(encoding='utf-8')
    d = json.loads(raw)

    total = 0
    details = []

    def corriger(champ):
        nonlocal total
        if not champ:
            return champ, 0
        n = champ.count('??')
        if n:
            total += n
        return champ.replace('??', ' '), n

    intro = d.get('intro') or {}
    if intro.get('htmlFr'):
        nv, n = corriger(intro['htmlFr'])
        intro['htmlFr'] = nv
        if n:
            details.append(('intro', n))

    for x in d.get('lessons', []):
        nv, n = corriger(x.get('htmlFr') or '')
        if n:
            x['htmlFr'] = nv
            details.append((x.get('docId'), n))
        # champs arabe et titres : contrôle d'intouchabilité
        assert '??' not in (x.get('html') or ''), 'html arabe touché ?!'
        assert '??' not in (x.get('titleFr') or ''), 'titleFr touché ?!'
        assert '??' not in (x.get('titleAr') or ''), 'titleAr touché ?!'

    FICHIER.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n'
                       if raw.endswith('\n') else
                       json.dumps(d, ensure_ascii=False, indent=2),
                       encoding='utf-8')

    apres = sha256(FICHIER)
    relecture = json.loads(FICHIER.read_text(encoding='utf-8'))
    reste = sum((x.get('htmlFr') or '').count('??') for x in relecture.get('lessons', []))
    reste += ((relecture.get('intro') or {}).get('htmlFr') or '').count('??')
    q_fr = sum(1 for x in relecture.get('lessons', [])
               for c in (x.get('htmlFr') or '').replace('??', '')
               if c == '?')
    print(f'sha256 avant : {avant[:16]}…  après : {apres[:16]}…')
    print(f'« ?? » remplacés par une espace : {total}')
    for doc, n in details:
        print(f'  - {doc} : {n}')
    print(f'« ?? » restants après correction : {reste}')
    print(f'points d’interrogation français simples conservés : {q_fr}')
    return 0 if (total == 15412 and reste == 0) else 1


if __name__ == '__main__':
    raise SystemExit(principal())
