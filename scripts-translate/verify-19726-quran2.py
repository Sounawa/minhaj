#!/usr/bin/env python3
# R330 — vérification 19726 complémentaire : patrons corrigés + contrôles bruts Warš
import json, re, unicodedata

cache = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))
KEEP = '\u0670'

def normk(x):
    out = []
    for c in x:
        if c == KEEP:
            out.append('ٰ')
            continue
        if unicodedata.category(c).startswith('M'):
            continue
        if c == '\u0671':
            out.append('ا'); continue
        if c == '\u0640':
            continue
        out.append(c)
    return ''.join(out).replace('\u0640', '')

corpus = {}
for num, s in cache.items():
    for ay, txt in s['ar']:
        corpus[(num, ay)] = (s.get('name', num), txt)

def search(pat, label, limit=20):
    p = normk(pat)
    hits = []
    for (sn, ay), (nm, txt) in corpus.items():
        if p in normk(txt):
            hits.append((sn, ay, nm, normk(txt)))
    print(f"--- {label} [{pat}] : {len(hits)}")
    for sn, ay, nm, t in hits[:limit]:
        i = t.find(p)
        print(f"   {sn}:{ay} …{t[max(0,i-14):i+len(p)+14]}…")
    return hits

def raw(label, sn, ay):
    nm, txt = corpus.get((sn, ay), ('?', ''))
    print(f"RAW {sn}:{ay} ({nm}) : {txt}")

print("=== patrons corrigés ===")
search('بٰئر', 'كَبَائِر élidé (بٰئر) — aš-Šūrā 42:37 + an-Nağm 53:32 attendus')
search('كبِير', 'كَبِير ifrād (كبِير الاثم)')
search('أنبٰء', 'أَنبِيَاء élidé (أنبٰء/نبٰء)')
search('نبٰء', 'أَنبِيَاء élidé variante (نبٰء)')
search('الأنۢباء', 'الْأَنۢبِيَاء avec lām (hazr)')
search('حسبان', 'حُسْبَان (toutes graphies, strip)')
search('باسطوا', 'بَاسِطُوا avec alif (istiṯmār)')
search('رُهبٰن', 'رُهْبَٰن élidé')
search('رهبان', 'رُهْبَان TOUTES graphies (thubūt éventuel)')
search('رَبّٰنِي', 'rabāniyy')
print("=== RAW contrôles ciblés ===")
raw('ġaḍbān a-Aʿrāf', 7, 150)
raw('ġaḍbān Ṭāhā', 20, 86)
raw('ruhbān al-Māʾida', 5, 82)
raw('ruhbān at-Tawba', 9, 34)
raw('ruhbāniyya al-Ḥadīd', 57, 27)
raw('kabāʾir aš-Šūrā', 42, 37)
raw('kabāʾir an-Nağm', 53, 32)
raw('aš-Šuʿarāʾ 26:3', 26, 3)
raw('aš-Šuʿarāʾ 26:5 (marqueur source)', 26, 5)
raw('an-Nağm 53:32', 53, 32)
print("=== بشر / تُبَشِّر ===")
search('بشّر', 'baššira formes II')
search('تُبشّر', 'tubašširū')
search('نَٰء', 'nāʾ-hamza élidé (نٰء)')
