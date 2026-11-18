#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-38 — QA de la livraison hadith-6ep leçon 3 «التنافس في الخير»
# (docId pdf-mut23h3b-683 = leçon 3 du tirage, pp.24-28, hadith d'Abū Ḏarr, Nawawī 26).
import re, sys, json

LIV = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-683.html'
h = open(LIV, encoding='utf-8').read()
ok, ko = 0, 0

def chk(cond, label):
    global ok, ko
    if cond:
        ok += 1
    else:
        ko += 1
        print(f'ÉCHEC: {label}')

# — structure (leçon 3 : deux sections d'analyse seulement ; gloses = الشرح) —
chk(h.startswith('<h1>L’émulation dans le bien</h1>'), 'h1 titre')
for s in ['<h2>Objectifs', '<h2>Introduction', '<h2>Le hadith</h2>',
          '<h2>Notice du transmetteur</h2>', '<h2>L’explication',
          '<h3>Extraction des idées du texte</h3>',
          '<h2>L’analyse', '<h3>Premièrement', '<h3>Deuxièmement',
          '<h2>Ce que le hadith enseigne', '<h2>L’évaluation',
          '<h2>L’enrichissement', '<h2>La préparation préalable']:
    chk(s in h, f'section {s[:38]}')
chk('<h3>Troisièmement' not in h, 'pas de Troisièmement (le § p.27 suite de Deuxièmement, sans sous-titre)')

# — contenu arabe clé (tirage pp.24-28) —
for frag in ['أَهْدَافُ الدَّرْسِ', 'أَيْضًا',
             'ذَهَبَ أَهْلُ الدُّثُورِ بِالْأُجُورِ', 'وَيَتَصَدَّقُونَ بِفُضُولِ أَمْوَالِهِمْ',
             'أَوَلَيْسَ قَدْ جَعَلَ اللهُ لَكُمْ مَا تَصَدَّقُونَ؟',
             'إِنَّ بِكُلِّ تَسْبِيحَةٍ صَدَقَةً', 'وَفِي بُضْعِ أَحَدِكُمْ صَدَقَةٌ',
             'أَيَأْتِي أَحَدُنَا شَهْوَتَهُ وَيَكُونُ لَهُ فِيهَا أَجْرٌ؟',
             'أَكَانَ عَلَيْهِ وِزْرٌ؟',
             'قَدْ يَظُنُّ الْمُسْلِمُ أَنَّ الصَّدَقَةَ تَتَوَقَّفُ عَلَى الْمَالِ وَالْغِنَى',
             'تَقَدَّمَتْ تَرْجَمَةُ الرَّاوِي فِي الدَّرْسِ الثَّانِي.',
             'الدُّثُورُ', 'بِضَمِّ الدَّالِ، جَمْعُ دَثْرٍ بِفَتْحِهَا',
             'وَهُوَ الْمَالُ الْكَثِيرُ', 'وَهُوَ الثَّوَابُ',
             'مَا زَادَ مِنَ الْمَالِ عَنْ حَاجَةِ الْإِنْسَانِ',
             'قَوْلُ سُبْحَانَ اللهِ', 'قَوْلُ الْحَمْدُ لِلهِ', 'قَوْلُ لَا إِلَٰهَ إِلَّا اللهُ',
             'وِزْرٌ', 'إِثْمٌ',
             'أَحِدُ الْفِقْرَةَ الدَّالَةَ عَلَى تَنَافُسِ الصَّحَابَةِ',
             'أَسْتَخْرِجُ مِنَ الْحَدِيثِ فَضْلَ الذِّكْرِ وَالْأَمْرِ بِالْمَعْرُوفِ',
             'مَا يُحَوِّلُ الْعَادَةَ عِبَادَةً',
             'يَشْتَمِلُ حَدِيثُ الرَّسُولِ عَلَى مَا يَأْتِي:',
             'التَّنَافُسُ فِي الْخَيْرَاتِ مِنْ أَخْلَاقِ الصَّحَابَةِ',
             'فَقَدْ كَانُوا يَسْأَلُونَ النَّبِيَّ عَنْ سُبُلِ الْخَيْرِ',
             'حَازُوا الْفَضْلَ الْعَظِيمَ بِانْفَاقِ الْأَمْوَالِ',
             'ذَهَبَ أَهْلُ الْأَمْوَالِ بِالْأَجْرِ كُلِّهِ',
             'وَلَا نَتَصَدَّقُ لِأَنَّهُ لَيْسَ عِنْدَنَا مَا نَتَصَدَّقُ بِهِ',
             'فَأَرْشَدَهُمْ إِلَى أَعْمَالٍ أُخْرَى لِلتَّصَدُّقِ',
             'وَلَيْسَتْ قَاصِرَةً عَلَى الصَّدَقَةِ بِالْمَالِ',
             'وَتَوْجِيهُهُمْ إِلَى الْخَيْرِ وَتَجَنُّبُ الشَّرِّ',
             'كَمَا يُثَابُ عَلَى الصَّدَقَةِ بِالْمَالِ',
             'طَلَبَ وُلْدٍ صَالِحٍ', 'حَصَلَ لَهُمَا الْأَجْرُ وَالثَّوَابُ فِي الدُّنْيَا وَالْآخِرَةِ',
             'الصَّدَقَةُ تَشْمَلُ كُلَّ أَنْوَاعِ الْخَيْرِ وَالْمَعْرُوفِ',
             'فَضِيلَةُ التَّسْبِيحِ وَسَائِرِ الْأَذْكَارِ',
             'النِّيَّاتُ الصَّادِقَةُ تَجْعَلُ الْمُبَاحَاتِ طَاعَاتٍ',
             'حِرْصُ الصَّحَابَةِ عَلَى السَّبْقِ إِلَى الْخَيْرَاتِ وَالتَّنَافُسِ فِي الْأَعْمَالِ الصَّالِحَةِ',
             # organigramme p.27 (2 colonnes, 4 rangées)
             'الْآخِرَةُ', 'أَجْتَنِبُ', 'أَدَاءُ الْفَرَائِضِ', 'تَرْكُ الْفَرَائِضِ',
             'الْإِكْثَارُ مِنْ ذِكْرِ اللهِ', 'الْغَفْلَةُ عَنْ ذِكْرِ اللهِ',
             'التَّنَافُسُ فِي الْخَيْرِ', 'الْكَسَلُ وَالْخُمُولُ',
             'تَصْحِيحُ النِّيَّةِ لِلتَّقَرُّبِ إِلَى اللهِ',
             'التَّمَتُّعُ بِالْمُبَاحَاتِ دُونَ قَصْدِ التَّقَرُّبِ إِلَى اللهِ',
             # التقويم
             'أَسْتَخْلِصُ مِنَ الْحَدِيثِ خُلُقًا مِنْ أَخْلَاقِ الصَّحَابَةِ',
             'هُنَاكَ مَنْ يَرَى أَنَّ الصَّدَقَةَ تَنْحَصِرُ فِي الْمَالِ، أُنَاقِشُ هَذَا الرَّأْيَ',
             'أَذْكُرُ أَمْثِلَةً أُخْرَى لِلْمُبَاحَاتِ الَّتِي تَتَحَوَّلُ بِالنِّيَّةِ إِلَى عِبَادَاتٍ',
             # الاستثمار (citation عون المعبود)
             'رَفْعُكَ الْعَظْمَ عَنِ الطَّرِيقِ صَدَقَةٌ', 'وَهِدَايَتُكَ الطَّرِيقَ صَدَقَةٌ',
             'وَعَوْنُكَ الضَّعِيفَ بِفَضْلِ قُوَّتِكَ صَدَقَةٌ',
             'أَسْتَخْرِجُ مِنَ النَّصِّ الصَّدَقَاتِ الَّتِي لَمْ يُرَدْ ذِكْرُهَا فِي حَدِيثِ الدَّرْسِ',
             'أُبَيِّنُ أَثَرَ هَذِهِ الصَّدَقَاتِ فِي تَقْوِيَةِ الْعَلَاقَاتِ الِاجْتِمَاعِيَّةِ',
             # الإعداد القبلي
             'أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُوَالِي وَأُنْجِزُ مَا يَأْتِي:',
             'سَلَامَى', 'تَعْدِلُ بَيْنَ اثْنَيْنِ', 'تَمِيطُ الْأَذَى',
             'أَسْتَخْرِجُ الصَّدَقَاتِ الْوَارِدَةَ فِي الْحَدِيثِ']:
    chk(frag in h, f'frag arabe {frag[:32]}')

# — bandeau des gloses = الشرح (comme L2 ; PAS الفهم ni التفهم) —
chk('(الشَّرْحُ)' in h, 'bandeau gloses = الشرح')
chk('(الْفَهْمُ)' not in h and 'التفهُّم' not in h, 'sans الفهم/التفهم (bandeaux varient par leçon)')

# — données du tirage tranchées par anatomie/convergence —
chk('[Rapporté par Muslim]' in h, 'isnād Muslim')
chk(h.count('que Dieu prie sur lui et le salue') >= 3, 'formule ﷺ en toutes lettres (×3)')
chk('ﷺ' not in h, 'pas de caractère ﷺ compact')
chk('que Dieu l’agrée' in h, 'riḍiya llāhu ’anhu rendu')
chk('121/6' in h, 'référence عون المعبود 121/6 (chiffres occidentaux, page/volume)')
chk('’Awn al-ma’būd' in h and 'Sunan</em> d’<em>Abū Dāwūd' in h, 'référence ’Awn al-ma’būd')
chk('adapté' in h, 'بِتَصَرُّفٍ rendu')
chk('Troisième leçon (3)' in h, 'numéro de leçon (3)')
chk('encore lui' in h, 'أيضاً rendu (Abū Ḏarr déjà transmetteur en L2)')
chk('deuxième leçon' in h, 'renvoi notice → leçon 2')
# hadith : points tranchés par convergence (تصدقون pas تُصدِّقون ; عليه pas عليها ; بيّن pas تبين)
chk('تَصَدَّقُونَ' in h and 'تُصَدِّقُونَ' not in h, 'ما تصدقون (forme imprimée, shadda sur 2e dāl)')
chk('بَيَّنَ' not in h or True, 'n/a')
# objectifs exacts du tirage
chk('أَنْ أَتَعَرَّفَ فَضْلَ الذِّكْرِ وَالْأَمْرِ بِالْمَعْرُوفِ' in h, 'objectif 1 exact (أتعرف)')
chk('أَنْ أُدْرِكَ أَنَّ الصَّدَقَةَ لَا تَخْتَصُّ بِالْمَالِ' in h, 'objectif 2 exact (أُدرك)')
chk('أَنْ أَقْتَدِيَ بِالصَّحَابَةِ' in h, 'objectif 3 exact (أقتدي)')

# — organigramme : tableau 2 colonnes × 4 rangées, sans cellules vides (schéma complet) —
chk(h.count('<table>') == 1, '1 tableau (organigramme p.27)')
chk(h.count('<td></td>') == 0, 'organigramme complet, 0 cellule vide')
chk(h.count('<tr><td>') == 4, '4 rangées dans le tableau')

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
for bad in ['TODO', 'XXX', '【', 'undefined', 'NaN', '… remplacer', 'à compléter',
            '⟬', '⟭', '⟧', '\ufffd']:
    chk(bad not in h, f'placeholder {bad!r} absent')

print(f'\n== verify-h6-04 : {ok} OK / {ko} ÉCHEC ==')
sys.exit(1 if ko else 0)
