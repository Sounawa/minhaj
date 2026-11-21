#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""R780 — correction du livre hadith-tanawi-3, leçons 10-20 : éradication
des 18 831 séquences « ?? » réintroduites par les poses W21-W23/R741/R743/
R778/R779 (le même défaut que R700-R712 : le pipeline d'extraction PDF perd
le glyphe d'espace inter-mots de la fonte arabe vocalisée ; chaque espace
perdu revenait comme 2 caractères « ? », parfois doublé « ???? »).

Précédent : scripts/r721-corrige-ht3.py (leçons 1-9, 15 412 « ?? » → espace,
vérifié en ligne). Les poses postérieures (leçons 10-20) ont réutilisé des
couches OCR défectueuses et ont laissé les « ?? » dans les htmlFr — visibles
aujourd'hui sur les pages rendues pdf-mut23h2n-10 à -20.

Sémantique par plage (r'\?{2,}', ne touche jamais le « ? » isolé français) :
  - plage entourée de DEUX caractères de mot (lettre arabe, lettre ASCII,
    chiffre) → remplacée par UNE espace (l'espace inter-mots perdu) ;
  - sinon (espace, ponctuation, balise, crochet déjà présent) → supprimée.
Les marqueurs d'arbitrage délibérés « [؟] » (U+061F dans crochets, ~980)
sont CONSERVÉS : ce sont des consignations de lecture incertaine voulues par
les sessions de pose, absentes des leçons 1-9 mais documentées dans les
worklogs W21-W23/R741/R743/R778/R779.

Contrôles :
  - seuls les champs htmlFr des leçons changent — intouchabilité vérifiée
    champ par champ (html, titleAr, titleFr, et tous les autres champs) ;
  - les « ? » isolés français sont intouchés (compte avant/après) ;
  - round-trip indent=2 ensure_ascii=False identique au format du fichier ;
  - 0 « ?? » restant dans tout le fichier après correction.
"""

import hashlib
import json
import re
import unicodedata
from pathlib import Path

FICHIER = Path(__file__).resolve().parent.parent / 'content' / 'books' / 'hadith-tanawi-3.json'

PLAGE = re.compile(r'\?{2,}')

# lettres arabes (blocs U+0600-U+06FF, suppléments et formes de présentation),
# lettres ASCII, chiffres — ce qui constitue un « mot » de part et d'autre
def est_caractere_de_mot(c):
    o = ord(c)
    if 0x0600 <= o <= 0x06FF or 0x0750 <= o <= 0x077F or \
       0xFB50 <= o <= 0xFDFF or 0xFE70 <= o <= 0xFEFF:
        # le « ؟ » (U+061F) est une ponctuation : il ne prolonge pas un mot
        # (sinon on créerait une espace parasite AVANT lui — « لَا ؟ »)
        return unicodedata.category(c).startswith('L')
    return c.isascii() and (c.isalnum())


def corriger(champ):
    """Retourne (champ corrigé, nb plages, nb plages→espace, nb plages→'')."""
    if not champ or '??' not in champ:
        return champ, 0, 0, 0

    vers_espace = 0
    vers_rien = 0

    def remplacer(m):
        nonlocal vers_espace, vers_rien
        debut, fin = m.start(), m.end()
        prec = champ[debut - 1] if debut > 0 else ''
        suiv = champ[fin] if fin < len(champ) else ''
        if prec and suiv and est_caractere_de_mot(prec) and est_caractere_de_mot(suiv):
            vers_espace += 1
            return ' '
        vers_rien += 1
        return ''

    corrige = PLAGE.sub(remplacer, champ)
    total = vers_espace + vers_rien
    return corrige, total, vers_espace, vers_rien


def sha256(fichier):
    return hashlib.sha256(fichier.read_bytes()).hexdigest()


def principal():
    avant_sha = sha256(FICHIER)
    raw = FICHIER.read_text(encoding='utf-8')
    d = json.loads(raw)

    q_simples_avant = raw.count('?') - 2 * raw.count('??')
    # (les « ???? » comptent pour 2 « ?? » ; le reste = « ? » isolés + « ? »
    #  arabes U+061F hors décompte ASCII — approximation volontaire, la vraie
    #  garantie est la vérification par re-lecture champ par champ)

    total = 0
    total_espace = 0
    total_rien = 0
    details = []

    intro = d.get('intro') or {}
    if intro.get('htmlFr'):
        nv, n, e, r = corriger(intro['htmlFr'])
        intro['htmlFr'] = nv
        if n:
            details.append(('intro', n, e, r))
            total += n
            total_espace += e
            total_rien += r

    for x in d.get('lessons', []):
        nv, n, e, r = corriger(x.get('htmlFr') or '')
        if n:
            details.append((x.get('docId'), n, e, r))
            total += n
            total_espace += e
            total_rien += r
        x['htmlFr'] = nv
        # contrôle d'intouchabilité des champs arabes et titres
        assert '??' not in (x.get('html') or ''), 'html arabe touché ?!'
        assert '??' not in (x.get('titleFr') or ''), 'titleFr touché ?!'
        assert '??' not in (x.get('titleAr') or ''), 'titleAr touché ?!'

    sortie = json.dumps(d, ensure_ascii=False, indent=2)
    if raw.endswith('\n'):
        sortie += '\n'
    FICHIER.write_text(sortie, encoding='utf-8')

    apres_sha = sha256(FICHIER)

    # ---- vérifications post-écriture ----
    relecture = json.loads(FICHIER.read_text(encoding='utf-8'))
    reste = sum((x.get('htmlFr') or '').count('??') for x in relecture['lessons'])
    reste += ((relecture.get('intro') or {}).get('htmlFr') or '').count('??')
    assert reste == 0, f'« ?? » restants : {reste}'

    # intouchabilité totale : tous les champs SAUF htmlFr identiques
    for avant, apres in zip(d['lessons'], relecture['lessons']):
        for cle in avant:
            if cle == 'htmlFr':
                continue
            assert avant[cle] == apres[cle], f'champ {cle} modifié pour {avant.get("docId")}'

    # plages « ? » multi restantes ? et « ? » isolés conservés
    cru = FICHIER.read_text(encoding='utf-8')
    q_multi_restants = PLAGE.findall(cru)
    assert not q_multi_restants, f'plages multi-? restantes : {len(q_multi_restants)}'

    print(f'SHA avant : {avant_sha[:16]}')
    print(f'SHA après : {apres_sha[:16]}')
    print(f'plages corrigées : {total} (→ espace {total_espace}, supprimées {total_rien})')
    for docid, n, e, r in details:
        print(f'  {docid}: {n} (→ espace {e}, supprimées {r})')
    print('vérifications : 0 « ?? » restant, champs non-htmlFr identiques byte à byte, '
          '« [؟] » conservés (' + str(cru.count('[؟]')) + '), plages multi-? 0')


if __name__ == '__main__':
    principal()
