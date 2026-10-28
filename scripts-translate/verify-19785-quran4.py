# -*- coding: utf-8 -*-
"""Passe 4 : code-points exacts des dessins critiques."""
import json, re

QC = '/home/z/my-project/scripts-translate/quran-cache.json'
cache = json.load(open(QC, encoding='utf-8'))

def context(sura, ayah, needle_bare):
    """Retourne le raw du mot contenant needle_bare (recherche dans bare, mapping sur raw)."""
    t = cache[str(sura)]['ar'][ayah-1][1]
    b = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A\u0653\u0654\u0655]', '', t)
    b = b.replace('\u0671', '\u0627')
    for h in '\u0623\u0625\u0622':
        b = b.replace(h, '\u0627')
    i = b.find(needle_bare)
    if i < 0:
        return f'{sura}:{ayah} NON TROUVE ({needle_bare})'
    # approximativement : les diacritiques precèdent les lettres -> chercher dans le raw
    # methode robuste : scan lettre par lettre
    letters_raw = []
    for ch in t:
        if '\u0621' <= ch <= '\u064A':
            letters_raw.append(ch)
    # reconstruire : trouver l'index dans la sequence de lettres
    seq = ''.join(letters_raw)
    # normaliser seq aussi (hamza) pour matcher needle
    seq_n = seq.replace('\u0623', '\u0627').replace('\u0625', '\u0627').replace('\u0622', '\u0627')
    j = seq_n.find(needle_bare)
    return f'{sura}:{ayah} seq={seq[max(0,j-6):j+len(needle_bare)+6] if j>=0 else "?"}'

def raw_between(sura, ayah, start_letter, n=30):
    t = cache[str(sura)]['ar'][ayah-1][1]
    i = t.find(start_letter)
    print(f'{sura}:{ayah} raw[...{t[max(0,i-2):i+n]}...]')

# 55:35 tantasiran : alif pleine (U+0627) ou dagger (U+064E) ?
t = cache['55']['ar'][34][1]
i = t.find('\u062a\u0646\u062a\u0635\u0631')  # تنتصر sans diacritiques? le raw a des diacritiques
# chercher les chars
for m in re.finditer('ن', t):
    pass
# methode : extraire la sequence de lettres et leurs diacritiques associes
def dump_word(t, needle_seq, label):
    """needle_seq = sequence de lettres (sans diacritiques). Retourne le raw du mot."""
    letters = []
    for ch in t:
        if '\u0621' <= ch <= '\u064A':
            letters.append(ch)
    seq = ''.join(letters)
    # essayer direct puis normalise
    k = seq.find(needle_seq)
    if k < 0:
        ns = seq.replace('\u0623', '\u0627').replace('\u0625', '\u0627').replace('\u0622', '\u0627')
        k = ns.find(needle_seq)
    if k < 0:
        print(f'{label}: non trouve'); return
    # compter les lettres precedentes et retrouver position raw
    count = 0
    for ci, ch in enumerate(t):
        if '\u0621' <= ch <= '\u064A':
            if count == k:
                start = ci; break
            count += 1
    # fin du mot : jusqu'au prochain caractere non-lettre/non-diacritique
    end = start
    for ci in range(start, len(t)):
        ch = t[ci]
        if '\u0621' <= ch <= '\u064A' or ch in '\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653\u0654\u0655\u0640\u0670\u06DF\u06E1\u06EA\u06EB\u06EC\u06ED\u06D6\u06D7\u06D8\u06D9\u06DA\u06DB\u06DC':
            end = ci
        else:
            break
    print(f'{label}: {repr(t[start:end+1])}')

# tantasiran 55:35
dump_word(t, 'تنتصر', '55:35 tantasiran')
# 9:96 taradaw x2
t9 = cache['9']['ar'][95][1]
dump_word(t9, 'ترضو', '9:96 taradaw #1')
t2 = cache['2']['ar'][231][1]
dump_word(t2, 'ترضو', '2:232 taradaw')
# 49:7 rashidun + ulaika
t7 = cache['49']['ar'][6][1]
dump_word(t7, 'رشدون', '49:7 rashidun')
dump_word(t7, 'اولئك', '49:7 ulaika')
# 3:7 rasikhun x2
t3 = cache['3']['ar'][6][1]
dump_word(t3, 'رسخون', '3:7 rasikhun')
# 4:162
t4 = cache['4']['ar'][161][1]
dump_word(t4, 'رسخون', '4:162 rasikhun')
# 12:26 rawadat
t12 = cache['12']['ar'][25][1]
dump_word(t12, 'رودت', '12:26 rawadat')
t51 = cache['12']['ar'][50][1]
dump_word(t51, 'رودت', '12:51 rawadat #1')
# 24:58 marrat
t24 = cache['24']['ar'][57][1]
dump_word(t24, 'مرت', '24:58 marrat')
# 6:40 arayta
t6 = cache['6']['ar'][39][1]
dump_word(t6, 'ارءيت', '6:40 arayta')
# 20:63 sahiran elide + 28:48 plein
t20 = cache['20']['ar'][62][1]
dump_word(t20, 'سحرن', '20:63 sahiran')
t28 = cache['28']['ar'][47][1]
dump_word(t28, 'سحران', '28:48 sahiran')
# 18:60 bahrayn
t18 = cache['18']['ar'][59][1]
dump_word(t18, 'بحرين', '18:60 bahrayn')
# 25:61 sirajan elide / 33:46 sirajan plein
dump_word(cache['25']['ar'][60][1], 'سرج', '25:61 sirajan')
dump_word(cache['33']['ar'][45][1], 'سراج', '33:46 sirajan')
# 21:95 haram
dump_word(cache['21']['ar'][94][1], 'حرام', '21:95 haram')
# 2:27 ulaika
dump_word(cache['2']['ar'][26][1], 'اولئك', '2:27 ulaika')
# 2:34 malaika
dump_word(cache['2']['ar'][33][1], 'ملئك', '2:34 malaika')
# 2:21 ya ayyuha
dump_word(cache['2']['ar'][20][1], 'يأيها', '2:21 ya-ayyuha')
# 2:31 haulai
dump_word(cache['2']['ar'][30][1], 'هؤلاء', '2:31 haulai')
# 12:20 darahima
dump_word(cache['12']['ar'][19][1], 'درهم', '12:20 darahima')
# 4:100 muraghama
dump_word(cache['4']['ar'][99][1], 'مرغم', '4:100 muraghama')
# 78:14 muasirat
dump_word(cache['78']['ar'][13][1], 'معصرت', '78:14 muasirat')
# 9:57 magharat
dump_word(cache['9']['ar'][56][1], 'مغرت', '9:57 magharat')
# 37:2 zajirat
dump_word(cache['37']['ar'][1][1], 'زجرت', '37:2 zajirat')
# 55:70 khayrat
dump_word(cache['55']['ar'][69][1], 'خيرت', '55:70 khayrat')
# 12:43 baqarat
dump_word(cache['12']['ar'][42][1], 'بقرت', '12:43 baqarat')
# 13:4 mutajawirat
dump_word(cache['13']['ar'][3][1], 'متجورت', '13:4 mutajawirat')
# 49:4 hujurat
dump_word(cache['49']['ar'][3][1], 'حجرت', '49:4 hujurat')
# 37:48 qasirat
dump_word(cache['37']['ar'][47][1], 'قصرت', '37:48 qasirat')
# 3:33 imran
dump_word(cache['3']['ar'][32][1], 'عمرن', '3:33 imran')
# 22:5 turab
dump_word(cache['22']['ar'][4][1], 'تراب', '22:5 turab')
# 9:101 marratayn
dump_word(cache['9']['ar'][100][1], 'مرتين', '9:101 marratayn')
