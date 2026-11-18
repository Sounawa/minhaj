#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 — QA de la livraison hadith-6ep leçon 1 «المسارعة في الخيرات»
# (docId pdf-mut23h3b-681 = leçon 1 du tirage, pp.11-16).
import re, sys, json

LIV = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-681.html'
h = open(LIV, encoding='utf-8').read()
ok, ko = 0, 0

def chk(cond, label):
    global ok, ko
    if cond:
        ok += 1
    else:
        ko += 1
        print(f'ÉCHEC: {label}')

# — structure —
chk(h.startswith('<h1>S’empresser vers les œuvres bonnes</h1>'), 'h1 titre')
for s in ['<h2>Objectifs', '<h2>Introduction', '<h2>Le hadith</h2>',
          '<h2>Notice du transmetteur</h2>', '<h2>La compréhension',
          '<h3>Explication des termes', '<h3>Extraction des idées du texte</h3>',
          '<h2>L’analyse', '<h3>Premièrement', '<h3>Deuxièmement', '<h3>Troisièmement',
          '<h4>A — La prière est lumière</h4>', '<h4>B — L’aumône est preuve</h4>',
          '<h4>C — La patience est clarté rayonnante', '<h3>Quatrièmement',
          '<h3>Cinquièmement', '<h2>Ce que le hadith enseigne', '<h2>L’évaluation',
          '<h2>L’enrichissement', '<h2>La préparation préalable']:
    chk(s in h, f'section {s[:35]}')

# — contenu arabe clé (tirage pp.11-16) —
for frag in ['الطُّهُورُ', 'شَطْرُ الْإِيمَانِ', 'الْمِيزَانَ', 'نُور', 'بُرْهَان',
             'ضِيَاء', 'حُجَّة', 'كُلُّ النَّاسِ يَغْدُو', 'أَبُو مَالِك',
             'الْمُدَّثِّر', 'الْبَقَرَة', 'الْمُؤْمِنُون', 'التَّوْبَة', 'فُصِّلَت',
             'أَهْدَافُ الدَّرْسِ', 'تَمْهِيد', 'الْفَهْمُ', 'الشَّرْحُ', 'التَّحْلِيلُ',
             'التَّقْوِيمُ', 'الِاسْتِثْمَارُ', 'الِإِعْدَادُ الْقَبْلِيُّ',
             'مَحَبَّةُ النَّاسِ وَالصِّدْقُ عَلَيْهِمْ', 'الِاهْتِمَامُ بِجَمَالِ الظَّاهِرِ',
             'تِلَاوَةُ الْقُرْآنِ وَالتَّخَلُّقُ بِآدَابِهِ', 'الْغَفْلَةُ عَنْ ذِكْرِ اللهِ',
             'السُّلُوكَات', 'تَزْكِيَةِ النَّفْسِ', 'مُهْلِكُهَا', 'التَّطَهُّرُ']:
    chk(frag in h, f'frag arabe {frag[:28]}')

# — références coraniques du tirage (chiffres TELS QU'IMPRIMÉS) —
for ref in ['(74)\u202f: 4', '(2)\u202f: 142', '(23)\u202f: 103', '(9)\u202f: 112',
            '(41)\u202f: 46']:
    chk(ref in h, f'réf coranique {ref}')

# — données du tirage —
chk('en l’an 18 de l’Hégire' in h, 'année de mort 18 H')
chk('[Rapporté par Muslim]' in h, 'isnād Muslim')
chk('Ka’b' in h and 'Āṣim' in h, 'nasab Ka’b b. ’Āṣim')
chk(h.count('que Dieu prie sur lui et le salue') >= 8, 'formule ﷺ écrite en toutes lettres')
chk('\u0640\u200d' not in h and 'ﷺ' not in h, 'pas de caractère ﷺ compact')
chk('emplissent — ou emplit —' in h, 'variance تملآن/تملأ rendue')

# — typographie série —
chk(h.count('\u202f') >= 90, 'U+202F ≥ 90')
chk(chr(39) not in h, '0 apostrophe droite')
chk('&nbsp;' not in h and '\u00a0' not in h, '0 nbsp/U+00A0')
for bad in ['\u02bc', '\u02be', '\u02bf', '\u02bb', '\u2018', '\u201a']:
    chk(bad not in h, f'interdit {bad!r} absent')
outside = re.sub(r'<span dir="rtl" lang="ar">.*?</span>', '', h, flags=re.S)
chk(not re.findall(r'[\u0600-\u06FF]', outside), 'arabe uniquement en spans RTL')
for ph in ['TODO', 'XXX', '【', '待补充', 'non reproduit']:
    chk(ph not in h, f'placeholder {ph} absent')

# — tableau 3×4 —
chk(h.count('<th>') == 3, 'tableau 3 en-têtes')
chk(h.count('<tr><td>') == 4, 'tableau 4 lignes')
chk(h.count('<td></td>') == 8, 'cellules vides à remplir')

# — pose (htmlFr dans le JSON) —
d = json.load(open('/home/z/my-project/content/books/hadith-6ep.json', encoding='utf-8'))
les = [x for x in d['lessons'] if x['docId'] == 'pdf-mut23h3b-681']
chk(len(les) == 1, 'emplacement unique pdf-mut23h3b-681')
if les:
    posed = les[0].get('htmlFr') or ''
    chk(posed.strip() == h.strip(), f'htmlFr posé identique ({len(posed)} car)')

print(f'\n{ok} contrôles OK / {ko} échec')
sys.exit(1 if ko else 0)
