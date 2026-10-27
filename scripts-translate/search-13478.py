# -*- coding: utf-8 -*-
"""Recherche normalisée (sans diacritiques) dans le cache — résolution E18/E19."""
import json, re

Q = json.load(open('scripts-translate/quran-cache.json'))

TASH = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u06DF\u06E0-\u06E8\u08D3-\u08FF]')

def norm(t):
    return TASH.sub('', t).replace('ٱ', 'ا').replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ى', 'ي').replace('﴾', '').replace('﴿', '')

def search(pat, label):
    print(f'--- {label} ({pat}) ---')
    rx = re.compile(pat)
    hits = 0
    for s in Q:
        sura = Q[s]
        for e in sura['ar']:
            n = norm(e[1])
            if rx.search(n):
                print(f'[{sura["englishName"]} {e[0]}]', e[1][:140])
                hits += 1
    if not hits:
        print('(aucun résultat)')

search('شركائ', 'Mes associés (شُرَكَائِي)')
search('تشاق', 'dispute (تشاق)')
search('ادخلوا ابواب جهنم|قل ادخلوا', 'portes de la Géhenne')
search('اين ما كنتم تشركون|اين شركائي', 'adresse ironique')
print('[az-Zumar 72]', Q['39']['ar'][71][1])
print('[Ghāfir 73]', Q['40']['ar'][72][1])
print('[Yūnus 28]', Q['10']['ar'][27][1])
search('جاءنا نذير', 'le warners venu')
search('فبئس مثوى|لبئس مثوى', 'فبئس مثوى / فلبئس مثوى')
search('بئس', 'بئس (toutes occurrences)')
