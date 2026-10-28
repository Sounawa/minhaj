#!/usr/bin/env python3
# Recherche des versets d'ancrage pour 19776 (chapitre du rāʾ — alif élidée)
import json, re

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def strip_diac(t):
    # retire harakat, sukun, shadda, marcadores quraniques
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u06DF\u06E0-\u06E8\u06EA-\u06EC]', '', t)

# mots cherchés (orthographe normale, sans diacritiques)
words = {
    'ترضيتم': [], 'ميراث': [], 'ورعينا': [], 'رعينا': [], 'فرشا': [],
    'الصرط': [], 'الصراط': [], 'إكراههن': [], 'أرأيت': [], 'أريت': [],
    'الرحيمين': [], 'رزقين': [], 'الرزاقين': [], 'رعون': [], 'الراعون': [],
    'الخرصون': [], 'الخراصون': [], 'وركعون': [], 'الركعون': [],
    'مبشرت': [], 'مبشرات': [], 'عورت': [], 'عورات': [],
    'مدبرت': [], 'مدبرات': [], 'حسرت': [], 'حسرات': [],
    'غمرت': [], 'غمرات': [], 'النشرت': [], 'نشرت': [],
    'الثمرت': [], 'الثمرات': [], 'الصبرت': [], 'الصابرات': [],
    'مقصورت': [], 'مقصورات': [], 'سحرني': [], 'سحري': [], 'سحران': [],
    'آخرني': [], 'آخران': [], 'اخران': [], 'عالمين': [], 'العلمين': [],
}

for sura, data in c.items():
    for ayah, text in data['ar']:
        t = strip_diac(text)
        # mots-boundaries approximatifs: découpage sur espaces
        toks = t.split()
        for w in list(words.keys()):
            if any(tok == w or tok.rstrip('،؛؛.,') == w for tok in toks):
                words[w].append(f"{sura}:{ayah}")

for w, hits in words.items():
    print(f"{w}: {hits if hits else 'AUCUN'}")
