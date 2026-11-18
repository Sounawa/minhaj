#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-37 — QA de la livraison hadith-6ep leçon 2 «تحريم الظلم»
# (docId pdf-mut23h3b-682 = leçon 2 du tirage, pp.17-23, hadith qudsi d'Abū Ḏarr, Nawawī 24).
import re, sys, json

LIV = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-682.html'
h = open(LIV, encoding='utf-8').read()
ok, ko = 0, 0

def chk(cond, label):
    global ok, ko
    if cond:
        ok += 1
    else:
        ko += 1
        print(f'ÉCHEC: {label}')

# — structure (leçon 2 : rubriques lues au tirage ; NOTA: bandeau des gloses = الشرح, PAS الفهم) —
chk(h.startswith('<h1>Interdiction de l’injustice</h1>'), 'h1 titre')
for s in ['<h2>Objectifs', '<h2>Introduction', '<h2>Le hadith</h2>',
          '<h2>Notice du transmetteur</h2>', '<h2>L’explication',
          '<h3>Extraction des idées du texte</h3>',
          '<h2>L’analyse', '<h3>Premièrement', '<h4>1 — Dieu S’interdit',
          '<h4>2 — L’interdiction de se léser', '<h3>Deuxièmement', '<h3>Troisièmement',
          '<h3>Quatrièmement', '<h2>Ce que le hadith enseigne', '<h2>L’évaluation',
          '<h2>L’enrichissement', '<h2>La préparation préalable']:
    chk(s in h, f'section {s[:38]}')

# — contenu arabe clé (tirage pp.17-23) —
for frag in ['يَا عِبَادِي', 'حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي', 'فَلَا تَظَالَمُوا',
             'لَنْ تَبْلُغُوا ضُرِّي فَتَضُرُّونِي', 'أَتْقَى قَلْب', 'أَفْجَرَ قَلْب',
             'إِنْسَكُمْ وَجِنَّكُمْ', 'الْمِخْيَط', 'أُحْصِيهَا لَكُمْ ثُمَّ أُوَفِّيكُمْ إِيَّاهَا',
             'فَلَا يَلُومَنَّ إِلَّا نَفْسَهُ', 'ضَالّ', 'فَاسْتَهْدُونِي', 'فَاسْتَطْعِمُونِي',
             'فَاسْتَكْسُونِي', 'الْإِحْصَاء', 'الْعَدُّ الْمُنْضَبَطُ',
             'مِنْ تَمَامِ عَقِيدَةِ الْمُسْلِمِ', 'الصِّرَاطِ الْمُسْتَقِيمِ',
             'لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ',
             'بِهَا تَتَرَقَّى نُفُوسُهُمْ وَتَطْمَئِنُّ قُلُوبُهُمْ وَتَسْعَى حَيَاتُهُمْ',
             'خَزَائِنُهُ لَا تَنْفَدُ', 'يَدُ اللهِ مَلْأَى', 'وَكَانَ عَرْشُهُ عَلَى الْمَاءِ',
             'الْحَدِيثِ الْقُدْسِيِّ', 'وَلَا يَظْلِمُ رَبُّكَ أَحَدًا', 'مِثْقَالَ ذَرَّةٍ',
             'وَمَا مِنْ دَابَّةٍ فِي الْأَرْضِ إِلَّا عَلَى اللهِ رِزْقُهَا',
             'لَا نَسْأَلُكَ رِزْقًا نَحْنُ نَرْزُقُكَ وَالْعَاقِبَةُ لِلتَّقْوَى',
             'أَسْمَاءُ اللهِ تَعَالَى وَصِفَاتُهُ', 'مَظَاهِرُهَا فِي الْحَدِيثِ الْقُدْسِيِّ',
             'ثَمَرَاتُهَا فِي حَيَاتِي', 'الرَّبَذَة', 'فِي أُمُورِي كُلِّهَا',
             'الْقِيْمَةُ', 'سُلُوكَاتٍ عَمَلِيَّةٍ', 'أَهْدَافُ الدَّرْسِ',
             'التَّحْلِيلُ', 'التَّقْوِيمُ', 'الِاسْتِثْمَارُ', 'الِإِعْدَادُ الْقَبْلِيُّ']:
    chk(frag in h, f'frag arabe {frag[:30]}')

# — rubrique du tirage : bandeau des gloses = الشرح (PAS الفهم, contrairement à la leçon 1) —
chk('(الشَّرْحُ)' in h, 'bandeau gloses = الشرح')
chk('(الْفَهْمُ)' not in h, 'leçon 2 sans الفهم (bandeaux varient par leçon)')

# — références coraniques du tirage (chiffres TELS QU'IMPRIMÉS) —
# écarts consignés du tirage : الكهف imprimé 48 (texte = v.49) ; طه imprimé 131 (texte = v.132b)
for ref in ['(18)\u202f: 48', '(4)\u202f: 40', '(11)\u202f: 6', '(20)\u202f: 131']:
    chk(ref in h, f'réf coranique {ref}')

# — données du tirage —
chk('en l’an 32 de l’Hégire' in h, 'année de mort 32 H (pixels, non le 23 bidi du cmap)')
chk('[Rapporté par Muslim]' in h, 'isnād Muslim')
chk('Ǧundub' in h and 'Ǧunāda' in h and 'Sufyān' in h and '’Ubayd' in h,
    'nasab Ǧundub b. Ǧunāda b. Sufyān b. ’Ubayd')
chk(h.count('que Dieu prie sur lui et le salue') >= 4, 'formule ﷺ écrite en toutes lettres (×4)')
chk('\u0640\u200d' not in h and 'ﷺ' not in h, 'pas de caractère ﷺ compact')
chk('que Dieu l’agrée' in h, 'riḍiya llāhu ’anhu rendu')
chk('Rabda' in h, 'ar-Rabda toponyme')
# hadith qudsi : formule de transmission propre au tirage
chk('dans ce qu’il rapporte de son Seigneur' in h, 'formule فيما يرويه عن ربه')
# Bukhari (citation du charh, p.21 du tirage)
chk('n’a pas diminué ce qui est dans Sa main' in h, 'hadith de Bukhari (لم يغض ما في يده)')
chk('Ṣaḥīḥ al-Buḫārī' in h, 'référence Bukhari')
# tableau التقويم : 5 lignes nommées, colonnes 2-3 vides ; tableau الاستثمار : 2 lignes (la Justice y revient)
chk(h.count('<tr><td>la Justice') == 2 and h.count('<tr><td>le Riche') == 1
    and h.count('<tr><td>le Guide') == 1 and h.count('<tr><td>le Tout-Pardonneur') == 1
    and h.count('<tr><td>le Pourvoyeur') == 1 and h.count('<tr><td>la Gratitude') == 1,
    'tableaux : 5 lignes التقويم + 2 lignes الاستثمار')
chk(h.count('<td></td>') == 12, 'cellules à remplir vides (10 + 2)')
# أهداف : 3 items avec formulations du tirage
chk('أَنْ أَعْرِفَ عَدْلَ اللهِ تَعَالَى وَتَحْرِيمَهُ لِلظُّلْمِ' in h,
    'objectif 1 exact (أعرف + للظلم, bbox)')
chk('أَنْ أَدْرِكَ مَظَاهِرَ افْتِقَارِ الْخَلْقِ إِلَى اللهِ تَعَالَى' in h, 'objectif 2 exact')
# الإعداد القبلي : 2 items (leçon 3 = الذكر/الصدقة)
chk('فَوَائِدَ الذِّكْرِ' in h, 'i’dād 1 فوائد الذكر')
chk('كَيْفِيَّةَ تَحْوِيلِ الْعَادَةِ إِلَى عِبَادَةٍ' in h, 'i’dād 2 العادة إلى عبادة')

# — typographie série —
chk(h.count('\u202f') >= 90, 'U+202F ≥ 90')
chk(chr(39) not in h, '0 apostrophe droite')
chk('&nbsp;' not in h and '\u00a0' not in h, '0 nbsp/U+00A0')
for bad in ['\u02bc', '\u02be', '\u02bf', '\u02bb', '\u2018', '\u201a']:
    chk(bad not in h, f'interdit {bad!r} absent')

# — arabe uniquement en spans RTL (hors <em> translittération) —
body = re.sub(r'<span dir="rtl" lang="ar">.*?</span>', '', h, flags=re.S)
body_no_tags = re.sub(r'<[^>]+>', '', body)
arabic_outside = [c for c in body_no_tags if '\u0600' <= c <= '\u06ff']
chk(len(arabic_outside) == 0, f'arabe hors spans RTL = {len(arabic_outside)}')

# — placeholders —
for bad in ['TODO', 'XXX', '【', 'undefined', 'NaN', '… remplacer', 'à compléter']:
    chk(bad not in h, f'placeholder {bad!r} absent')

print(f'\n== verify-h6-03 : {ok} OK / {ko} ÉCHEC ==')
sys.exit(1 if ko else 0)
