#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Vérification verbatim des versets choisis pour la leçon pdf-mut23h2v-311 (faraid-tanawi-3 lessons[1])
# an-Nisāʾ 4:11 (segment enfants + segment parents) ; an-Nisāʾ 4:176 (ouverture kalāla + segment sœurs/frère)
import json, re

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def get(sura, ayah):
    s = c[str(sura)]
    for n, t in s['ar']:
        if n == ayah:
            return t
    return None

def strip(t):
    t = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\uFBB2-\uFBC1]', '', t)
    t = t.replace('ٱ', 'ا').replace('آ', 'ا').replace('أ', 'ا').replace('إ', 'ا').replace('ى', 'ي').replace('ة', 'ه')
    t = re.sub(r'[^\u0600-\u06FF ]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

# (sura, ayah, candidat, type) — type: 'prefix' (début du verset) | 'segment' (passage intérieur continu)
pairs = [
    (4, 11, 'يوصيكم الله في اولدكم للذكر مثل حظ الانثيين', 'prefix'),
    (4, 11, 'ولابويه لكل وحد منهما السدس مما ترك ان كان له ولد', 'segment'),
    (4, 176, 'يستفتونك قل الله يفتيكم في الكلله', 'prefix'),
    (4, 176, 'فان كانتا اثنتين فلهما الثلثان مما ترك وان كانوا اخوه رجالا ونساء فللذكر مثل حظ الانثيين', 'segment'),
]

ok = True
for sura, ayah, cand, kind in pairs:
    ref = get(sura, ayah)
    r1, r2 = strip(ref or ''), strip(cand)
    if kind == 'prefix':
        match = r1 == r2 or (len(r1) > len(r2) and r1.startswith(r2))
    else:
        match = r2 in r1
    ok = ok and match
    print(f'--- {sura}:{ayah} [{kind}] --- MATCH: {match}')
    print('CAND   :', r2[:120])
    if not match:
        print('CACHE  :', r1[:400])
print('VERDICT GLOBAL:', 'OK — 4/4 vérifiés verbatim au cache' if ok else 'ÉCHEC')
