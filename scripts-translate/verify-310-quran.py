#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Vérification verbatim des versets choisis pour la leçon pdf-mut23h2v-310 (faraid-tanawi-3 lessons[0])
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

pairs = [
    (4, 11, 'يوصيكم الله في اولادكم للذكر مثل حظ الانثيين'),
    (4, 12, 'ولكم نصف ما ترك ازواجكم ان لم يكن لهن ولد ولهن الربع مما تركتم ان لم يكن لكم ولد فان كان لكم ولد فلهن الثمن مما تركتم'),
    (4, 176, 'يستفتونك قل الله يفتيكم في الكلالة'),
]

for sura, ayah, cand in pairs:
    ref = get(sura, ayah)
    r1, r2 = strip(ref or ''), strip(cand)
    match = r1 == r2 or (len(r1) > len(r2) and r1.startswith(r2))
    print(f'--- {sura}:{ayah} --- MATCH: {match}')
    print('CACHE :', (ref or '')[:400])
    print()
