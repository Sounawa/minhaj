# -*- coding: utf-8 -*-
"""verify-20054-refs.py — appareil lacunaire du fihrist (20054).
Pas de fentes « de sa parole » ici (règle ax adaptée) : les ancres sont
des renvois croisés — chaque œuvre du fihrist est cherchée dans le corpus
FR LIVRÉ (registry hand + llm, hors TODO 20048/20052/20054 dont htmlFr = GT).
Sortie : comptes par œuvre + première leçon d'apparition."""
import json, re

BASE = '/home/z/my-project'
reg = json.load(open(f'{BASE}/scripts-translate/savant-registry.json'))
hand = set(reg['hand'] if isinstance(reg['hand'], list) else reg['hand'])
llm = set(reg['llm'] if isinstance(reg['llm'], list) else reg['llm'])
d = json.load(open(f'{BASE}/content/books/rasm-wa-dabt-4ep.json'))
docs = []
for kind, doc in [('intro', d.get('intro') or {})] + [('lesson', l) for l in d.get('lessons', [])]:
    did = str(doc.get('docId'))
    if did in ('20048', '20052', '20054'):
        continue  # TODO — htmlFr = GT, pas corpus
    if did not in hand and did not in llm:
        continue
    html = doc.get('htmlFr') or ''
    if html:
        docs.append((did, html))
print(f'corpus livré : {len(docs)} documents (hand {len([x for x in docs if x[0] in hand])} + llm {len([x for x in docs if x[0] in llm])})')

OEUVRES = [
    ('1 matn al-Waḏġīrī', r'Wa[dḏ]ġīrī'),
    ('1 šarḥ al-Massārī', r'Mas+sārī'),
    ('1 titre Bahǧat an-naẓar', r'Bahǧat'),
    ('2 muṣḥaf Muḥammadī', r'Muṣḥaf al-Muḥammadī'),
    ('2 ṭarīq al-Azraq', r'al-Azraq'),
    ('2 riwāyat Warš', r'Warš'),
    ('3 Tuḥfat al-qurrāʾ', r'Tuḥfat'),
    ('3 as-Sarġīnī', r'Sarg?īnī'),
    ('4 al-Farmī', r'al-Farmī'),
    ('4 al-Ḫabbāz', r'Ḫabbāz'),
    ('5 Durra al-ǧaliyya', r'Durra al-ǧaliyya'),
    ('5 al-Maṣmūdī', r'Maṣmūdī'),
    ('6 Durra aṣ-ṣaqīla', r'Durra aṣ-ṣaqīla'),
    ('6 al-Labīb', r'al-Labīb'),
    ('6 ʿAqīla', r'[ʿʻ][Aa]qīla'),
    ('7 al-Māriġnī', r'Mār[iī]ġnī'),
    ('7 Dalīl al-ḥayrān', r'Dalīl al-ḥayrān'),
    ('7 Mawrid aẓ-ẓamʾān', r'Mawrid'),
    ('8 Ibn Mā Yābī', r'Mā Yābī'),
    ('8 muṣḥaf ḏī n-nūrayn', r'nūrayn'),
    ('9 al-Munabbihī', r'Munabbihī'),
    ('9 Kašf al-ġamām', r'Kašf al-ġamām'),
    ('10-11 ad-Dānī', r'ad-Dānī'),
    ('10 al-Muḥkam', r'al-Muḥkam'),
    ('11 al-Muqnīʿ', r'al-Muqnīʿ'),
    ('12 al-Ḫarrāz', r'Ḫarrāz'),
    ('12 ḏayl fī ḍ-ḍabṭ', r'ḏayl'),
    ('13 Ibn aṭ-Ṭayyib', r'Ibn aṭ-Ṭayyib'),
    ('13 Nuṣrat al-kuttāb', r'Nuṣrat'),
    ('14 az-Zarwālī', r'[Zz]arwālī'),
    ('14 ʿAwāriḍ al-ḥurūf', r'ʿAwāriḍ'),
]
muettes = []
for label, pat in OEUVRES:
    hits = []
    for did, html in docs:
        n = len(re.findall(pat, html))
        if n:
            hits.append((did, n))
    if hits:
        first = hits[0][0]
        tot = sum(n for _, n in hits)
        print(f"{label:26s}: {tot:3d} mentions, {len(hits):2d} leçons — 1re : {first} — {', '.join(f'{a}×{b}' for a, b in hits[:12])}")
    else:
        muettes.append(label)
        print(f"{label:26s}: — MUETTE dans le corpus livré —")
print()
print('œuvres muettes (révélées par le fihrist) :', len(muettes), '→', ' ; '.join(muettes))
