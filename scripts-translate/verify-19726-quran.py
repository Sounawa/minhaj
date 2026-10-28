#!/usr/bin/env python3
# R330 — vérification 19726 v2 : norme qui PRÉSERVE U+0670 (alif suscrit = ḥaḏf au corpus)
import json, re, unicodedata

cache = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))
KEEP = '\u0670'

def normk(x):
    # strip diacritiques SAUF U+0670 ; neutraliser wasla/tatweel
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
        # contexte
        i = t.find(p)
        print(f"   {sn}:{ay} ({nm}) …{t[max(0,i-12):i+len(p)+12]}…")
    return hits

print("=== ḤAḎF claims (motif AVEC U+0670) ===")
search('بَٰسِط', 'بَـسِطٌ élidé — ar-Raʿd (13) + al-Kahf (18) attendus')
search('كَٰئِر', 'كَبَائِر élidé — aš-Šūrā (42) + an-Nağm (53) attendus')
search('نَٰءُ', 'أَنبَاءُ élidé (نٰء) — al-Anʿām (6) + aš-Šuʿarāʾ 26:5 attendus')
search('غَٰضَب', 'غَضْبَانَ élidé — al-Aʿrāf (7) + Ṭāhā (20) attendus')
search('بَٰخِع', 'بَـخِعٌ élidé — aš-Šuʿarāʾ attendu')
search('رُهْبَٰن', 'رُهْبَان élidé (بِمِيمِ الْجَمْعِ)')
search('عِبَٰد', 'عِبَاد élidé (iʿdād qibli)', 25)
search('حُسْبَٰن', 'حُسْبَان élidé (انْصِبْ حُسْبَن)')
search('إِدْبَٰر', 'إِدْبَر élidé (ثُمَّ إِدْبَر)')
search('أَدْبَٰر', 'أَدْبَر élidé (كَيْفَ أَدْبَر)')
search('الْأَلْبَٰب', 'الْأَلْبَاب élidé (خَبَائِثَ الْأَلْبَاب)', 25)
search('الْأَسْبَٰب', 'الْأَسْبَاب élidé (رَائِبَ الْأَسْبَاب)')
search('خَبَٰئِث', 'خَبَائِث élidé (خَبَـئِثَ الْأَلْبَاب)')
search('أَحِبَّٰٓؤ', 'أَحِبَّاءُهُ élidé (بَـعِدْ أَحِبَّؤُهُ)')
search('مُبَٰرَك', 'مُبَارَك élidé (مُبَرَكٌ كَيْفَ)')
search('رَبَّٰنِي', 'رَبَّانِيُّون/يِّين élidé (رَبَّنِيِّينْ/رَبَّنِيُّونْ)', 25)
search('الْبَٰقِيَٰ', 'الْبَاقِيَات élidé (وَالْبَـقِيَتُ)')
search('تَٰئِبَٰ', 'تَائِبَات élidé (تَـئِبَتٍ)')
search('ثَيِّبَٰ', 'ثَيِّبَات élidé (ثَيِّبَتْ)')
search('طَيِّبَٰ', 'طَيِّبَات élidé (وَطَيِّبَتٌ)', 25)
search('مُعَقِّبَٰ', 'مُعَقِّبَات élidé (مُعَقِّبَتْ)')
search('بَٰرِز', 'بَرِزُوا élidé (وَبَرِزُونَ)')
search('رُبَٰع', 'رُبَعَ élidé (رُبَعَ كَيْفَ)')
search('بَٰلِغ', 'بَلَغَ élidé (كَيْفَ بَـلِغَ)', 25)
search('بَٰطِل', 'بَـطِلٌ élidé (وَطَيِّبَتٌ بَطِلٌ)')
print("=== THUBŪT / autres graphies ===")
search('بَاسِطُوا', 'بَاسِطُوا (istiṯmār — avec alif)')
search('كَبِيرِ الْإِثْم', 'كَبِيرِ الْإِثْم (ifrād — le rasm pointe vers cette lecture)')
search('أَنْبَاءِ', 'أَنْبَاءِ (avec lām — le rasm élidé pointe ailleurs)')
search('رُهْبَانِي', 'رُهْبَانِيّ (thubūt — sans élision)')
