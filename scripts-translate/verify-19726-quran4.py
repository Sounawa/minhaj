#!/usr/bin/env python3
# R330 — compléments de vérification 19726 (bāʾ) : بشر elidé, أنبياء/أنباء, 66:5 RAW, comptes finaux
import json, re, unicodedata

cache = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))
KEEP = '\u0670'

def normk(x):
    out = []
    for c in x:
        if c == KEEP:
            out.append('ٰ'); continue
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

def search(pat, label, limit=25):
    p = normk(pat)
    hits = []
    for (sn, ay), (nm, txt) in corpus.items():
        if p in normk(txt):
            hits.append((sn, ay, nm, normk(txt)))
    print(f"--- {label} [{pat}] : {len(hits)}")
    for sn, ay, nm, t in hits[:limit]:
        i = t.find(p)
        print(f"   {sn}:{ay} ({nm}) …{t[max(0,i-14):i+len(p)+14]}…")
    return hits

def raw(sn, ay):
    nm, txt = corpus.get((str(sn), str(ay)), ('?', 'ABSENT'))
    print(f"RAW {sn}:{ay} ({nm}) : {txt}")

print("=== بشر au rasm élidé (le chapitre du bāʾ) ===")
search('بَٰش', 'toute forme ب+سuscrit+ش', 30)
search('بَٰشِر', 'بَشِر/بَشير élidé', 30)
search('بَٰشّ', 'بَشّ élidé (form II)', 30)
search('تُبَٰش', 'تُبَشّ élidé', 30)
search('يُبَٰش', 'يُبَشّ élidé', 30)
search('أُبَٰش', 'أُبَشّ élidé', 30)
search('بَٰشِّرْ', 'بَشِّرْ élidé', 30)
search('بَٰشِّرُو', 'بَشِّرُوا élidé', 30)

print("=== أَنْبِيَاء / أَنْبَاء toutes formes ===")
search('أَنۢبَاء', 'أَنۢباء (ikfāʾ)', 30)
search('أَنْبِيَاء', 'أَنْبِيَاء pleine', 30)
search('نَبِيّ', 'نَبِيّ (contrôle)', 5)

print("=== RAW 66:5 et versements 42/53/13/18 ===")
raw(66, 5)
raw(13, 14)
raw(18, 18)
raw(42, 37)
raw(53, 32)
raw(3, 79)
raw(5, 44)
raw(5, 18)
raw(38, 29)
raw(13, 11)

print("=== comptes finaux élidé ===")
search('بَٰلِغ', 'بَالِغ élidé', 30)
search('رُبَٰع', 'رُبَاع élidé', 30)
search('بَٰطِل', 'بَاطِل élidé', 30)
search('عِبَٰد', 'عِبَاد élidé (compte plein)', 30)
search('أَدْبَٰر', 'أَدْبَار élidé (compte plein)', 30)
search('مُبَٰرَك', 'مُبَارَك élidé (compte plein)', 30)
print("=== بَعِدْ (maʿdūd?) ===")
search('بَٰعِد', 'بَعِيد élidé', 30)
search('بَعِيد', 'بَعِيد pleine (contrôle)', 8)
