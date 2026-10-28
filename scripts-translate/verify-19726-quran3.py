#!/usr/bin/env python3
# R330 — vérification 19726 v3 : RAW à clés chaînes + anbāʾ + tubašširū
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
        corpus[(str(num), ay)] = (s.get('name', num), txt)

def raw(label, sn, ay):
    nm, txt = corpus.get((str(sn), ay), ('?', '?'))
    print(f"RAW {sn}:{ay} ({nm}) : {txt}")

def search(pat, label, limit=25):
    p = normk(pat)
    hits = []
    for (sn, ay), (nm, txt) in corpus.items():
        if p in normk(txt):
            hits.append((sn, ay, nm, normk(txt)))
    print(f"--- {label} [{pat}] : {len(hits)}")
    for sn, ay, nm, t in hits[:limit]:
        i = t.find(p)
        print(f"   {sn}:{ay} …{t[max(0,i-16):i+len(p)+16]}…")
    return hits

print("=== RAW ciblés ===")
raw('ġaḍbān Aʿrāf', 7, 150); raw('ġaḍbān Ṭāhā', 20, 86)
raw('ḥusbān al-Anʿām', 6, 96); raw('ḥusbān al-Kahf', 18, 40); raw('ḥusbān ar-Raḥmān', 55, 5)
raw('ruhbān Māʾida', 5, 82); raw('ruhbān Tawba 31', 9, 31); raw('ruhbān Tawba 34', 9, 34); raw('ruhbāniyya Ḥadīd', 57, 27)
raw('bāḫiʿ Kahf', 18, 6); raw('bāḫiʿ Šuʿarāʾ 3', 26, 3); raw('Šuʿarāʾ 5 (marqueur)', 26, 5)
raw('anbāʾ+lām al-Qaṣaṣ', 28, 66); raw('anbāʾ+lām al-Qamar', 54, 4)
raw('bāsiṭū al-Anʿām', 6, 93)
raw('kabāʾir Šūrā', 42, 37)
print("=== anbāʾ (nouvelles) sans lām — al-Anʿām attendu ===")
search('أَنۢباء', 'أَنۢبَاء stripped')
search('أَنۢبٰء', 'أَنۢبَاء élidé (أنۢبٰء)')
print("=== tubašširū / bašširū ===")
search('بشرو', 'bašširū/ʾalif pleine')
search('بشروا', 'bašširū alif pleine explicite')
search('تبشروا', 'tubašširū alif pleine')
search('تبشرو ', 'tubašširū sans alif')
