# -*- coding: utf-8 -*-
"""Vérification coranique 19785 — tamma du chapitre du ra (rasm-wa-dabt-4ep).
Méthode fill-19776-search : squelette (rasm sans voyelles) + frontières de mots."""
import json, re, sys

QC = '/home/z/my-project/scripts-translate/quran-cache.json'
cache = json.load(open(QC, encoding='utf-8'))

def bare(s):
    # supprime diacritiques, petites lettres, tatweel, sujets d'ornement
    s = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', s)
    s = s.replace('\u0671', '\u0627')  # alif wasla -> alif
    return s

def words(b):
    return re.findall(r'[\u0621-\u064A]+', b)

CORPUS = []
for sura, v in cache.items():
    arr = v['ar']
    for idx, pair in enumerate(arr):
        ayah, text = pair[0], pair[1]
        b = bare(text)
        for w in words(b):
            CORPUS.append((int(sura), ayah, idx, w))

def count(sk, exact=False):
    """Occurrences avec frontières de mots. sk = squelette sans voyelles."""
    res = []
    for sura, ayah, idx, w in CORPUS:
        if (w == sk) if exact else (sk in w):
            res.append((sura, ayah, w))
    return res

def show(name, sk, exact=False, limit=12):
    r = count(sk, exact)
    uniq = []
    seen = set()
    for sura, ayah, w in r:
        k = (sura, ayah)
        if k not in seen:
            seen.add(k)
            uniq.append((sura, ayah, w))
    print(f'== {name} [{sk}] exact={exact} : {len(r)} occurrences / {len(uniq)} versets')
    for sura, ayah, w in uniq[:limit]:
        print(f'   {sura}:{ayah} {w}')
    return uniq

if __name__ == '__main__':
    print('--- SECTION I-A : jam al-muannath salim (12 vedettes) ---')
    show('adh-dhakirati', 'ذاكرت', True)
    show('al-muasirati', 'معصرت', True)
    show('magharatin', 'مغارت', True)
    show('maghrat (bayt maghartin?)', 'مغرت', True)
    show('fa-z-zajirati', 'زاجرت', True)
    show('muhajiratin', 'مهاجرت', True)
    show('al-khayrati', 'خيرت', True)
    show('marratin', 'مررت', True)
    show('musakhkharatin', 'مسخرت', True)
    show('hujurati', 'حجرت', True)
    show('qasiratu', 'قصرت', True)
    show('baqaratin', 'بقرت', True)
    show('mutajawirat', 'متجورت', True)
    show('mutajawirat2', 'متجاورت', True)

    print('--- SECTION I-B : jam al-mudhakkar salim (2) ---')
    show('ar-rashiduna', 'رشدون', True)
    show('ar-rasikhuna', 'رسخون', True)

    print('--- SECTION I-T : al-muthanna (2) ---')
    show('tantasirna', 'تنتصرن', True)
    show('al-bahran', 'بحرن', True)
    show('al-bahrayn (plein, contre)', 'بحرين', True)

    print('--- SECTION I-TH : ism aajami (2) ---')
    show('Imran (element)', 'عمرن')
    show('Ibrahim (rasm avec ha)', 'ابرهيم', True)
    show('Ibrahim (rasm avec alif, contre)', 'ابراهيم', True)

    print('--- SECTION II : hadf ishara (2) ---')
    show('wa-haram (21:95)', 'وحرام', True)
    show('haram (element)', 'حرام')
    show('sirajan (25:61)', 'سرج')
    show('siraj (element)', 'سراج')

    print('--- SECTION III : mahdufa mutlaqan ---')
    show('murgham (demonstration?)', 'مرغم')
    show('taradaw', 'ترضوا', True)
    show('taradu', 'ترضو', True)
    show('araytum (corpus hamze)', 'ارايتتم', True)
    show('araytum (element Warsh)', 'ارايتيم', True)
    show('darahima', 'دراهيم', True)
    show('darahim (element)', 'درهيم', True)
    show('murawada (demonstration?)', 'مرود')
    show('rawada (racine)', 'راود')
    show('marad (madi demonst?)', 'مرت', True)

    print('--- ISTIMAR : exemples ad-Dani (4) ---')
    show('ulaika', 'اولئك', True)
    show('ulaihahum/alaik', 'اوليكم', True)
    show('al-malaika', 'ملائك')
    show('ya ayyuha', 'يأيها', True)
    show('haaulai', 'هولاء', True)
    show('haulai ha', 'هؤلاء', True)

    print('--- IDAD : turaban (2) + alif thabita ---')
    show('turab (toutes formes)', 'تراب')
    show('turba (element?)', 'ترب')
    show('rab (squelette r-b)', 'راب', True)
