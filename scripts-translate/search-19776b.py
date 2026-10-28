#!/usr/bin/env python3
# Recherche sous-chaîne + impression des versets pour 19776 (chapitre du rāʾ)
import json, re

c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

def norm(t):
    t = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u06DF\u06E0-\u06E8\u06EA-\u06EC\u0670]', '', t)
    t = t.replace('\u0671', 'ا')  # alef wasla
    t = t.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
    t = t.replace('ء', '')  # hamza nue (أريت vs أرأيت)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

# patrons en orthographe RASM (alif élidée) et normale
pats = {
    'ترضيتم': 0, 'ميرث': 0, 'ميراث': 0, 'ورعنا': 0, 'رعينا': 0,
    'فرشا': 0, 'فراشا': 0, 'صرط': 0, 'صراط': 0, 'إكرههن': 0, 'اكراههن': 0,
    'اريت': 0, 'ارايت': 0,
    'الرحيمين': 0, 'رزقين': 0, 'رعون': 0, 'الخرصون': 0, 'وركعون': 0, 'ركعون': 0,
    'مبشرت': 0, 'عورت': 0, 'مدبرت': 0, 'حسرت': 0, 'غمرت': 0,
    'النشرت': 0, 'نشرت': 0, 'الثمرت': 0, 'الصبرت': 0, 'مقصورت': 0,
    'سحرن': 0, 'اخرن': 0,
}

hits = {k: [] for k in pats}
for sura, data in c.items():
    for ayah, text in data['ar']:
        t = norm(text)
        for p in pats:
            if p in t:
                hits[p].append((f"{sura}:{ayah}", text))

for p, hs in hits.items():
    print(f"### {p} — {len(hs)} verset(s)")
    for ref, full in hs:
        print(f"  [{ref}] {full}")
    print()
