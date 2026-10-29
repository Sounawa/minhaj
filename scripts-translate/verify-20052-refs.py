# -*- coding: utf-8 -*-
"""verify-20052-refs.py — appareil lacunaire des biographies (20052).
Pas de fentes « de sa parole » (règle ax adaptée) : ancres = renvois croisés —
chaque savant des 21 notices est cherché dans le corpus FR LIVRÉ
(hand + llm, hors TODO 20048/20052 ; 20054 est désormais livré et inclus)."""
import json, re

BASE = '/home/z/my-project'
reg = json.load(open(f'{BASE}/scripts-translate/savant-registry.json'))
hand = set(reg['hand'] if isinstance(reg['hand'], list) else reg['hand'])
llm = set(reg['llm'] if isinstance(reg['llm'], list) else reg['llm'])
d = json.load(open(f'{BASE}/content/books/rasm-wa-dabt-4ep.json'))
docs = []
for kind, doc in [('intro', d.get('intro') or {})] + [('lesson', l) for l in d.get('lessons', [])]:
    did = str(doc.get('docId'))
    if did in ('20048', '20052'):
        continue
    if did not in hand and did not in llm:
        continue
    html = doc.get('htmlFr') or ''
    if html:
        docs.append((did, html))
print(f'corpus livré : {len(docs)} documents')

NOMS = [
    ('01 Ibn Aǧaṭṭā', r'Aǧaṭṭā'),
    ('02 Ibn aṭ-Ṭayyib', r'Ibn aṭ-Ṭayyib'),
    ('03 Ibn al-Qāḍī', r'Ibn al-Qāḍī'),
    ('04 Ibn Mā Yābī', r'Mā Yābī'),
    ('05 Ibn Naǧǧāḥ', r'Naǧǧāḥ'),
    ('06 al-Balansī', r'Balansī'),
    ('07 at-Tanasī', r'Tanasī'),
    ('08 al-Ḫabbāz', r'Ḫabbāz'),
    ('09 al-Ḫarrāz', r'Ḫarrāz'),
    ('10 ad-Dānī', r'ad-Dānī'),
    ('11 az-Zarwālī', r'[Zz]arwālī'),
    ('12 al-Labīb', r'al-Labīb'),
    ('13 al-Māriġnī', r'Mār[iī]ġnī'),
    ('14 Nāfiʿ', r'Nāfiʿ'),
    ('15 ʿUṯmān b. ʿAffān', r'ʿAffān'),
    ('15 (ʿUṯmān tous)', r'ʿUṯmān'),
    ('16 al-Ġāzī', r'al-Ġāzī'),
    ('17 al-Faḫḫār', r'Faḫḫār'),
    ('18 al-Qaysī', r'al-Qaysī'),
    ('19 aš-Šāṭibī', r'Šāṭibī'),
    ('20 aš-Šabānī (al-Munabbihī)', r'Munabbihī'),
    ('21 Warš', r'Warš'),
]
muetts = []
for label, pat in NOMS:
    hits = []
    for did, html in docs:
        n = len(re.findall(pat, html))
        if n:
            hits.append((did, n))
    if hits:
        tot = sum(n for _, n in hits)
        print(f"{label:28s}: {tot:3d} mentions, {len(hits):2d} leçons — 1re : {hits[0][0]} — {', '.join(f'{a}×{b}' for a, b in hits[:14])}")
    else:
        muetts.append(label)
        print(f"{label:28s}: — MUETT—")
print()
print('noms muets :', len(muetts), '→', ' ; '.join(muetts))
