#!/usr/bin/env python3
# R329 — vérification au cache coranique des mots du rasm cités dans 19725
# (f aṣl al-hamza d'ʿUmdat al-Bayān) : formes canoniques des rasm imprimés.
import json, re, unicodedata

cache = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def strip_h(x):
    return ''.join(c for c in x if not unicodedata.category(c).startswith('M'))

def norm(x):
    # neutraliser alif-wasla U+0671, tatwīl, tatweel ; hamzas normalisées
    x = x.replace('\u0671', 'ا').replace('\u0640', '')
    x = x.replace('أ', 'ء').replace('إ', 'ء').replace('آ', 'ءا').replace('ٱ', 'ا')
    return strip_h(x)

corpus = {}
for num, s in cache.items():
    for ay, txt in s['ar']:
        corpus[(num, ay)] = (s.get('name', num), txt)

def search(pat, label, limit=12):
    p = norm(pat)
    hits = []
    for (sn, ay), (nm, txt) in corpus.items():
        if p in norm(txt):
            hits.append((sn, ay, nm))
    print(f"--- {label} [{pat}] : {len(hits)} occurrence(s)")
    for sn, ay, nm in hits[:limit]:
        t = corpus[(sn, ay)][1]
        print(f"   {sn}:{ay} ({nm})")
    return hits

print("=== Vérifications 19725 ===")
# 1. قرآنًا عربيًّا — début de Yūsuf et az-Zuḫruf
search('قرانا عربيا', 'قرآنا عربيا (début Yūsuf 12:2 / Zuḫruf 43:3 attendus)')
# 2. هذا القرآن — dans la sourate (Yūsuf 12:3 attendu)
search('هذا القرآن', 'هذا القرآن')
# 3. لولا نزل هذا القرآن (Zuḫruf 43:31 attendu)
search('لولا نزل هذا القرآن', 'لولا نزل هذا القرآن')
# 4. آم/آل à double hamza-alif (rasm ءاامنت هم ءاالهدنا)
search('امنت هم', 'ءاامنت هم (rasm ءاامنتُم)')
search('الهتنا', 'ءاالهدنا/ءاالهمتنا (rasm ءاالِهتنا)')
search('همتنا', 'آلهمتنا (آلِهَتُنا)')
# 5. يوسف occurrences of آمنت-ish forms — full scan of Yūsuf for hamza+alif words
print("--- Yūsuf : ayahs avec آم/آل (formes canoniques):")
for sn in ['12']:
    for ay, txt in cache[sn]['ar']:
        n = strip_h(txt)
        if re.search('[ءأإآ]', n) and ('امن' in n or 'اله' in n or 'الله' in n):
            pass
# 6. ساءت / سوءت (rasm سَوْءَتُ)
search('ساءت', 'ساءت (rasm سَوْءَتُ)')
# 7. نشأت (ar-Raḥmān — rasm مُنْشَأَتْ)
search('نشات', 'منشات (rasm مُنْشَأَتْ)')
# 8. خطيئة / خطايا (rasm خَطِيئَتُ)
search('خطيئت', 'خطيئت (rasm خَطِيئَتُ)')
search('خطايا', 'خطايا (pluriel)')
# 9. برءاء (rasm وَبُرَءَؤُاْ)
search('برءا', 'برءا (rasm وَبُرَءَؤُاْ)')
search('ءاء', 'séquence hamza+alif final برءاء')
# 10. جاءنا (rasm جَاءَنَا)
search('جاءنا', 'جاءنا (rasm جَاءَنَا)')
# 11. an-Najm — رأى (les deux exceptions au thubūt de رءا)
print("--- an-Najm 53 : toutes les ayahs avec رأى :")
for ay, txt in cache['53']['ar']:
    if 'رأى' in strip_h(txt) or 'رَأَى' in txt:
        print(f"   53:{ay} : {txt[:100]}")
# 12. ناء / نئا (rasm نَئَا)
search('ناء', 'ناء (rasm نَئَا ?)')
# 13. السوأى / سوءا (rasm السُّوأَى)
search('سوأ', 'سوأ (rasm السُّوأَى ?)')
# 14. الآن (rasm ءَالَنَ)
search('الآن', 'الآن (rasm ءَالَـنَ)')
# 15. باسط (iʿdād qibliyya — rasm بَـسِطٌ)
search('بسط', 'بسط (iʿdād : « بَـسِطٌ » avec ḥaḏf)')
