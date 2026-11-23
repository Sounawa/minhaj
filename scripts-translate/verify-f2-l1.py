#!/usr/bin/env python3
# W55 : verify leçon 1 fiqh-2es — structure, citations, renvois, coquilles documentées, registre
import json, re, sys

b = json.load(open('content/books/fiqh-2es.json', encoding='utf-8'))
ids = [x['docId'] for x in b['lessons']]
assert ids == ['pdf-1', '12164', '12431'], f'ordre registre: {ids}'
e = b['lessons'][0]
t = e['htmlFr']
assert e['titleAr'] == 'زكاة العين والحرث', e['titleAr']
assert e.get('pdfOnly') is True
ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))

chk('h1 leçon 1', '<h1>Leçon 1 — La zakāt des espèces monétaires et des céréales</h1>' in t)
chk('0 arabe', not re.search(r'[\u0600-\u06FF]', t))
chk('mutun Risâla cité', 'La <em>zakāt</em> de l’espèce, des céréales et des troupeaux est une obligation' in t)
chk('5 awsuq', 'cinq <em>awsuq</em>' in t and 'six <em>aqfiza</em> et un quart de <em>qafīz</em>' in t)
chk('wasq 60 sâʿ', 'soixante <em>ṣāʿ</em>' in t)
chk('or 20 dinars', 'pas de <em>zakāt</em> sur l’or en deçà de vingt dinars' in t)
chk('argent 200 dirhams', 'en deçà de deux cents dirhams' in t)
chk('quart dîme centaine', 'de chaque centaine' in t)
chk('2 versets + renvois corrigés', 'verset 43&nbsp;; le tirage imprime' in t and 'verset 103&nbsp;; le tirage imprime' in t)
chk('hadith pilier Bukhârî', 'L’Islam est bâti sur cinq' in t and 'jeûne de Ramaḍān' in t)
chk('Mâlik sunna sans divergence', 'La <em>sunna</em> qui ne souffre aucune divergence, chez nous' in t)
chk('Muwaṭṭaʾ renvoi', 'al-Mūwaṭṭaʾ, livre de la <em>zakāt</em>' in t)
chk('653 kg', '653 kilogrammes' in t)
chk('hadith Apportez le quart', 'Apportez le quart de la dîme' in t and 'trente-neuf, rien n’est dû' in t)
chk('Abû Dâwûd renvoi', 'Sunan Abī Dāwūd, livre de la <em>zakāt</em>' in t)
chk('Musnad Ahmad renvoi', 'Musnad Aḥmad, musnad de ʿAlī b. Abī Ṭālib' in t)
chk('ʿushr/nâḍḥ', 'relève de la dîme' in t and 'irrigation (<em>nadḥ</em>) relève du demi' in t)
chk('Tawba verset khudh', 'Prends de leurs biens une aumône' in t)
chk('Muʿâdh Yémen', 'Muʿādh b. Jabal au Yémen' in t and 'prise chez leurs riches et rendue à leurs pauvres' in t)
chk('ʿAdawī 1/511', 'ḥāshiya al-ʿAdawī sur <em>Kifāyat al-ṭālib al-rabbānī</em> 1/511' in t)
chk('maqṣirī glose', 'abreuve par sa sueur' in t)
chk('shuqâʿ/ʿatharî', 'pluvial (<em>ʿatharī</em>)' in t)
chk('ouverture leçon 2', 'Définis les marchandises' in t)
chk('guillemets appariés', t.count('«') == t.count('»') and t.count('«') >= 20)
chk('0 apostrophe droite', not re.findall(r"[\w]'[\w]", t))
chk('glossaire متن', 'Glossaire du texte' in t and 'al-māniḥa' in t and 'al-salt' in t)
chk('conditions 6+4', 'la venue du collecteur' in t and 'le versement à l’endroit de son obligation' in t)

f = sum(1 for _, c in ok if not c)
for n, c in ok:
    if not c: print('  FAIL:', n)
print(f'verify-f2-l1 : {len(ok)-f}/{len(ok)} PASS')
sys.exit(1 if f else 0)
