# -*- coding: utf-8 -*-
"""verify-19216-quran.py — sondes coraniques pour 19216 (l'introduction au tawqīt — 5 fentes d'āya)."""
import json, re, unicodedata

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare2(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c == '\u0622': c = '\u0627'
        if c == '\u0623': c = '\u0627'
        if c == '\u0625': c = '\u0627'
        if c == '\u0671': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out)

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())

def contient(seq, label, maxn=8):
    print(f'\n## {label} — séquence {seq}')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            bs = [bare2(w) for w in W(p[1])]
            for j in range(len(bs)-len(seq)+1):
                if bs[j:j+len(seq)] == list(seq):
                    n += 1
                    if n <= maxn:
                        print(f'   {s}:{i+1} :: {p[1][:115]}')
    if n == 0:
        print('   ✗ AUCUNE position')
    elif n > maxn:
        print(f'   ... {n} positions')

# === Fente 1 — la qibla (la bienf. 3 : سمت القبلة) ===
contient(['فول', 'وجهك', 'شطر', 'المسجد'], 'F1. 2:144 fawalli waǧhaka šaṭra l-mašǧidi l-ḥarām (la qibla)')

# === Fente 2 — le nombre des années et le calcul (la bienf. 6) ===
contient(['منازل', 'لتعلموا', 'عدد', 'السنين'], 'F2. 10:5 manāzila li-taʿlamū ʿadada s-sinīna (déjà calibrée R354)')
contient(['عدد', 'السنين', 'والحساب'], 'F2b. 10:5 + 17:12 (double candidat pour la fente des années)')

# === Fente 3 — les étoiles de l'orientation (la bienf. 8 : نجوم الاهتداء) ===
contient(['النجوم', 'لتهتدوا', 'بها', 'في', 'ظلمت', 'البر'], 'F3. 6:97 an-nuǧūm li-tahtadū bi-hā fī ẓulumāt al-barri wa-l-baḥr')

# === Fente 4 — le tadbīr/tafakkur dans la création (la bienf. 9) ===
contient(['ان', 'في', 'خلق', 'السموت', 'والارض'], 'F4. 3:190 inna fī ḫalqi s-samāwāti wa-l-arḍ (la création des cieux et de la terre)')
contient(['ويتفكرون', 'في', 'خلق', 'السموت', 'والارض'], 'F4b. 3:191 wa-yatafakkarūna fī ḫalqi s-samāwāti wa-l-arḍ (wāw fusionnée)')

# === Fente 5 — le zawāl (l'istitmār du Qarāfī : دليل مشروعية الزوال) ===
contient(['اقم', 'الصلوة', 'لدلوك', 'الشمس'], 'F5. 17:78 aqimi ṣ-ṣalāta li-dulūki š-šams (rasm : الصلوة)')

# === Contrôles d'appui ===
contient(['وقدره', 'منازل'], 'C1. 10:5 wa-qaddarahū manāzila (mémoire R354 : U+06E5 dans وقدرهۥ)')
contient(['جعل', 'لكم', 'النجوم', 'لتهتدوا'], 'C2. 6:97 ǧaʿala la-kumu n-nuǧūma li-tahtadū (contexte étendu)')
contient(['ولي', 'العباس', 'اختصار'], 'C3. le naẓm et l\'abrégement — pas de fente attendue ici')
