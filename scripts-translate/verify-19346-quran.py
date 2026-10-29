#!/usr/bin/env python3
# Vérification verbatim des versets choisis pour la leçon 19346
# az-Zumar 39:21 (les sources/yanābīʿ) + al-Baqara 2:28 (le retour/turjaʿūn)
import json, re, unicodedata

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def get(sura, ayah):
    s = c[str(sura)]
    for n, t in s['ar']:
        if n == ayah:
            return t
    return None

def strip(t):
    # retire diacritiques + lettres non basiques pour comparaison squelette
    t = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\uFBB2-\uFBC1]', '', t)
    t = t.replace('ٱ', 'ا').replace('آ', 'ا').replace('أ', 'ا').replace('إ', 'ا').replace('ى', 'ي').replace('ة', 'ه')
    t = re.sub(r'[^\u0600-\u06FF ]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

pairs = [
    (39, 21, 'أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًا مُّخْتَلِفًا أَلْوَٰنُهُۥ'),
    (2, 28, 'كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًا فَأَحْيَٰكُمْ ۖ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ'),
]

for sura, ayah, cand in pairs:
    ref = get(sura, ayah)
    print(f'--- {sura}:{ayah} ---')
    print('CACHE :', ref)
    r1, r2 = strip(ref or ''), strip(cand)
    match = r1 == r2 or (len(r1) > len(r2) and r1.startswith(r2))
    print('MATCH squelette (égal ou préfixe exact) :', match)
    print('CACHE strip :', r1)
    print('CAND  strip :', r2)
    print()
