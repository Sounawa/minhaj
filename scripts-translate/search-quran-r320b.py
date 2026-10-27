import json
import re

q = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

HARAKAT = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
def strip(t):
    return HARAKAT.sub('', t).replace('\u0671', 'ا').replace('\u0649', 'ي').replace('\u0626','ي')

print('=== root sh-r-k (stripped) ===')
for sura, sdata in q.items():
    ar = sdata.get('ar', [])
    for i, text in enumerate(ar, 1):
        t = strip(text)
        if any(w in t for w in ['شرك', 'اشترك', 'شريك', 'شارك', 'استشر', 'شراك']):
            print(f'[{sura}:{i}] {t[:140]}')

print()
print('=== khalT root (stripped) ===')
for sura, sdata in q.items():
    ar = sdata.get('ar', [])
    for i, text in enumerate(ar, 1):
        t = strip(text)
        if 'خلط' in t:
            print(f'[{sura}:{i}] {t[:140]}')
