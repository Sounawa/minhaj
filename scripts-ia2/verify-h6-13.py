#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — QA de la livraison L12 «لا ضرر ولا ضرار» (docId pdf-mut23h3b-692, pp.71-75).
# Conventions série hadith-6ep (cf. verify-h6-12.py) : ’ U+2019 seul, U+202F, ﷺ,
# arabe uniquement en spans RTL, médaillons ۝ dans le span arabe seul, 0 apostrophe droite.
import re, sys, unicodedata

F = '/home/z/my-project/scripts-ia2/livraisons/hadith-6ep/pdf-mut23h3b-692.html'
h = open(F, encoding='utf-8').read()
ok, fail = 0, 0
def T(name, cond, extra=''):
    global ok, fail
    if cond: ok += 1; print(f'  OK  {name}')
    else: fail += 1; print(f'FAIL  {name} {extra}')

print(f'== verify-h6-13 : {len(h)} caractères ==')

# 1) structure
T('h1 présent', h.startswith('<h1>'))
for t in ['أَهْدَافُ الدَّرْسِ', 'تَمْهِيد', 'تَرْجَمَةُ الرَّاوِي', 'الشَّرْحُ', 'التَّحْلِيلُ',
          'التَّقْوِيمُ', 'الِاسْتِثْمَارُ', 'الْإِعْدَادُ الْقَبْلِيُّ']:
    T(f'titre arabe {t[:12]}', t in h)
T('hadith verbatim', '«لَا ضَرَرَ وَلَا ضِرَارَ»' in h)
T('notice 74h', '«74ه»' in h)
T('notice 1170', '1170' in h)

# 2) les 4 textes sourcés de l'enrichissement
T('verset Nisa 29 (début)', 'لَا تَأْكُلُوا أَمْوَالَكُمْ بَيْنَكُمْ بِالْبَاطِلِ' in h)
T('verset Nisa 29 (fin)', 'إِنَّ اللهَ كَانَ بِكُمْ رَحِيمًا' in h)
T('réf verset [an-Nisa: 29]', '[Les femmes (<em>an-Nisāʾ</em>)\u202f: 29]' in h)
T('hadith Tirmidhi dépôt', '«أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ وَلَا تَخُنْ مَنْ خَانَكَ»' in h)
T('réf Tirmidhi باب 38', 'بَابُ 38]' in h)
T('hadith Abu Dawud maudits', 'اتَّقُوا الْمَلَاعِنَ الثَّلَاثَ: الْبَرَازَ فِي الْمَوَارِدِ، وَقَارِعَةَ الطَّرِيقِ، وَالظِّلِّ' in h)
T('réf Abu Dawud 26', 'الْحَدِيثُ رَقْمُ 26]' in h)

# 3) gloses et analyse
T('glose 1 ضرر', 'الضَّرَرُ الْإِسَاءَةُ الْمُوَجَّهَةُ إِلَى الْغَيْرِ ابْتِدَاءً' in h)
T('glose 2 ضرار (مجازاة)', 'إِيقَاعُ الضَّرَرِ بِالْغَيْرِ مُجَازَاةً' in h)
T('يشتمل هذا الدرس', 'يَشْتَمِلُ هَذَا الدَّرْسُ عَلَى مَا يَأْتِي' in h)
T('أولا تعريف', 'أَوَّلًا: تَعْرِيفُ الضَّرَرِ وَالضِّرَارِ' in h)
T('ثانيا الأمر برفع', 'ثَانِيًا: الْأَمْرُ بِرَفْعِ الضَّرَرِ وَالضِّرَارِ' in h)
T('قاعدة الضرر يزال', '«الضَّرَرُ يُزَالُ»' in h)
T('لها طرق يقرر', 'وَلَهُ طُرُقٌ يُقَرِّرُ بَعْضُهَا بَعْضًا' in h)
T('لا وقوع لهما (avec lâm)', 'وَلَا إِيقَاعُ لَهُمَا' in h)
T('والضرار بالوقوف', 'وَالضِّرَارِ بِالْوُقُوفِ عِنْدَ الْحَقِّ فِيهِ' in h)
T('ونفع الغير', 'وَنَفْعُ الْغَيْرِ' in h)
T('يا عبادي (وجعلته)', 'وَجَعَلْتُهُ بَيْنَكُمْ مُحَرَّمًا' in h)
T('دماءكم + réf Boukhari', '«إِنَّ دِمَاءَكُمْ وَأَمْوَالَكُمْ وَأَعْرَاضَكُمْ عَلَيْكُمْ حَرَامٌ»' in h and 'لِيَبْلُغَ الشَّاهِدُ الْغَائِبُ' in h)
T('ضَرَّرًا ×2', h.count('ضَرَّرًا') == 2, f'(trouvé {h.count("ضَرَّرًا")})')

# 4) schéma et évaluation
T('bandeau synthèse', 'أَتَجَنَّبُ الضَّرَرَ وَالْإِضْرَارَ اسْتِجَابَةً لِلَّهِ' in h)
T('3 colonnes droits', 'حَقُّ النَّفْسِ' in h and 'حَقُّ الْغَيْرِ' in h and 'حَقُّ الْبِيئَةِ' in h)
T('6 comportements', all(x in h for x in [
    'أُطَهِّرُ نَفْسِي مِنَ الرَّذَائِلِ', 'أُحَافِظُ عَلَى نَظَافَةِ جِسْمِي',
    'أَتَجَنَّبُ إِلْحَاقَ الضَّرَرِ بِغَيْرِي', 'أُحْسِنُ فِي مُعَامَلَتِي لِغَيْرِي',
    'أَتَجَنَّبُ الْإِضْرَارَ بِالْبِيئَةِ', 'اسْتِغْلَالِ الْمَوَارِدِ الْبِيئِيَّةِ بِاعْتِدَالٍ']))
T('items 1-3 évaluation', all(x in h for x in [
    'أُبَيِّنُ الْفَرْقَ بَيْنَ الضَّرَرِ وَالضِّرَارِ',
    'لِرَفْعِ الضَّرَرِ مِنْ وَاقِعِي',
    'بَعْدَ نَقْلِهِ لِدَفْتَرِي']))
T('tableau 4 rangées', all(x in h for x in [
    'إِيذَاءُ الْجِيرَانِ', 'تَنَاوُلُ الْمُخَدِّرَاتِ',
    'احْتِرَامُ قَانُونِ السَّيْرِ', 'رَمْيُ الْأَزْبَالِ فِي الشَّارِعِ']))
T('en-têtes tableau bas', 'السُّلُوكُ' in h and 'صَحِيحٌ أَوْ خَطَأٌ' in h and 'التَّعْلِيلُ' in h)
T('item enrichissement', 'صُوَرًا لِلضَّرَرِ الْمُحَرَّمِ' in h)
T('préparation préalable', '«الْبَيِّنَةُ عَلَى الْمُدَّعِي، وَالْيَمِينُ عَلَى مَنْ أَنْكَرَ»' in h)
T('الموالى (alif maqsura)', 'الدَّرْسِ الْمُوَالَى' in h)

# 5) conventions typographiques (sur le texte débalisé)
body_only = re.sub(r'<[^>]+>', '', h)
T('0 apostrophe droite', "'" not in body_only)
T("0 double quote droite", '"' not in body_only)
T('’ U+2019 présent (>60)', h.count('\u2019') > 60, f'({h.count(chr(0x2019))})')
T('U+202F présent (>60)', h.count('\u202f') > 60, f'({h.count(chr(0x202f))})')
T('ﷺ présent', '\ufdfa' in h)

# 6) arabe uniquement dans les spans RTL (ﷺ = convention série, autorisé hors span)
spans = re.findall(r'<span dir="rtl"[^>]*>(.*?)</span>', h, re.S)
arabic_outside = re.sub(r'<span dir="rtl"[^>]*>.*?</span>', '', h, flags=re.S)
arabic_outside = re.sub(r'<[^>]+>', '', arabic_outside)
arabic_outside = re.sub(r'[\s\u202f\u00a0]', '', arabic_outside)
bad = [c for c in arabic_outside if '\u0600' <= c <= '\u06ff']
T('0 caractère arabe hors spans RTL (hors ﷺ)', not bad, f'({len(bad)} trouvés: {bad[:5]})')
T('span vide absent', '<span dir="rtl" lang="ar">()</span>' not in h)

# 7) médaillons U+06DD uniquement dans les spans
outside_no_spans = re.sub(r'<span dir="rtl"[^>]*>.*?</span>', '', h, flags=re.S)
T('0 médaillon ۝ hors spans', '\u06dd' not in outside_no_spans)
T('médaillon ۝٢٩ dans un span', 'رَحِيمًا ۝٢٩»' in h)

# 8) aucun placeholder
T('0 placeholder', not re.search(r'XXX|TODO|À COMPLÉTER|\[أدخل|\[أَدْخِل', h))

# 9) apostrophes doubles / espaces normaux dans guillemets FR
double_apos = re.findall(r"(\w)'(\w)", h)
T("0 apostrophe entre lettres", not double_apos, f'({double_apos[:3]})')

# 10) nombres du tirage en clair
T('«74 de l\'Hégire»', '74 de l\u2019Hégire' in h)
T('hadith numéro 26', 'hadith numéro 26' in h)
T('chapitre 38 (Tirmidhi)', 'chapitre\u202f38' in h)

print(f'\n== {ok} contrôles OK / {fail} échec ==')
sys.exit(1 if fail else 0)
