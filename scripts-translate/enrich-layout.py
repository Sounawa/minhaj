#!/usr/bin/env python3
"""
Minhāj — Enrichissement de la mise en page des traductions françaises
====================================================================

Conventions de translittération validées par l'utilisateur :
  ج (Jîm)      → j  (jardin / djudo)   — INTERDIT : ǧ
  ش (Chîn)     → ch (chat)             — INTERDIT : š
  ع (ʿAyn)     → '  (apostrophe)       — INTERDIT : ʿ
  غ (Ghayn)    → gh (r grasseyé)       — INTERDIT : ġ
  خ (Khâ')     → kh (Bach allemand)    — INTERDIT : ḫ
  ء (Hamza)    → '  (apostrophe)       — INTERDIT : ʾ
  ث (Thâ')     → th (thing anglais)    — préféré à ṯ
  ذ (Dhâl)     → dh (this anglais)     — préféré à ḏ
  ح (Hâ')      → ḥ  (conservé)
  ص (Sâd)      → ṣ  (conservé)
  ض (Dâd)      → ḍ  (conservé)
  ط (Tâ')      → ṭ  (conservé)
  ظ (Zâ')      → ẓ  (conservé)
  ق (Qâf)      → q  (conservé)
  Voyelles longues : ā, ī, ū (conservées)

Améliorations appliquées :
  1. Conversion de l'ancienne translittération vers la nouvelle
  2. Balises <em> sur les termes arabes translittérés
  3. Ajout de l'écriture arabe entre parenthèses après chaque terme
     (harakat seulement sur les termes à vocalisation certaine/figée)
  4. Espaces insécables &nbsp; pour la typographie française
  5. Encadrés "Texte fondateur (matn)"
  6. Nettoyage HTML (paragraphes vides)

Usage: python3 scripts-translate/enrich-layout.py [--apply]
  Sans --apply : mode simulation (rapport + fichiers dans books-enriched/)
  Avec --apply : applique les modifications définitivement
"""
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime

# ============================================================
# ÉTAPE 0 : CONVERSION ANCIENNE → NOUVELLE TRANSLITTÉRATION
# ============================================================

def convert_translit(text):
    """Convertit les symboles de translittération périmés vers la convention validée."""
    # Ordre important : les digrammes d'abord, puis les simples
    conversions = [
        ('ǧ', 'j'),      # ج → j (jardin)
        ('Ǧ', 'J'),
        ('š', 'ch'),     # ش → ch (chat)
        ('Š', 'Ch'),
        ('ʿ', "'"),      # ع → ' (apostrophe)
        ('ġ', 'gh'),     # غ → gh
        ('Ġ', 'Gh'),
        ('ḫ', 'kh'),     # خ → kh
        ('Ḫ', 'Kh'),
        ('ʾ', "'"),      # ء → ' (hamza → apostrophe)
        ('ṯ', 'th'),     # ث → th
        ('Ṯ', 'Th'),
        ('ḏ', 'dh'),     # ذ → dh
        ('Ḏ', 'Dh'),
    ]
    for old, new in conversions:
        text = text.replace(old, new)
    return text

# ============================================================
# DICTIONNAIRE ENRICHI : translittération → (arabe, arabe_harakat)
# arabe_harakat = None → pas de harakat (contexte variable ou incertain)
# Règle de sécurité : harakat seulement sur mots FIGÉS à vocalisation CERTAINE
# ============================================================

AR_DICT = {
    # ===== Noms d'Allah (harakat certains) =====
    'allāh': ('الله', 'اللَّه'),
    'ar-raḥmān': ('الرحمن', 'الرَّحْمَٰن'),
    'ar-raḥīm': ('الرحيم', 'الرَّحِيم'),
    'ar-raḥmāni r-raḥīm': ('الرحمن الرحيم', 'الرَّحْمَٰنِ الرَّحِيمِ'),
    
    # ===== Noms de prophètes et personnalités (harakat certains) =====
    'muḥammad': ('محمد', 'مُحَمَّد'),
    'muḥammadun': ('محمد', 'مُحَمَّدٌ'),
    'abū': ('أبو', 'أَبُو'),
    'abī': ('أبي', 'أَبِي'),
    "'alī": ('علي', 'عَلِيّ'),
    "'umar": ('عمر', 'عُمَر'),
    "'uṯmān": ('عثمان', 'عُثْمَان'),
    "'uthmān": ('عثمان', 'عُثْمَان'),
    'mālik': ('مالك', 'مَالِك'),
    'aḥmad': ('أحمد', 'أَحْمَد'),
    "sa'īd": ('سعيد', 'سَعِيد'),
    'khalīl': ('خليل', 'خَلِيل'),
    "nāfi'": ('نافع', 'نَافِع'),
    "'aṭiyya": ('عطية', 'عَطِيَّة'),
    'ibn': ('ابن', 'ابْن'),
    "ibn 'abbās": ('ابن عباس', 'ابْنِ عَبَّاسٍ'),
    "'ā'isha": ('عائشة', 'عَائِشَةُ'),
    'bakr': ('بكر', 'بَكْرٍ'),
    'abū bakr': ('أبو بكر', 'أَبُو بَكْرٍ'),
    'ibrāhīm': ('إبراهيم', 'إِبْرَاهِيمُ'),
    'mūsā': ('موسى', 'مُوسَى'),
    "'īsā": ('عيسى', 'عِيسَى'),
    'dāwūd': ('داود', 'دَاوُدُ'),
    'sulaymān': ('سليمان', 'سُلَيْمَانُ'),
    'yūsuf': ('يوسف', 'يُوسُفُ'),
    'yūnus': ('يونس', 'يُونُسُ'),
    'nūḥ': ('نوح', 'نُوحٌ'),
    'hūd': ('هود', 'هُودٌ'),
    'lūṭ': ('لوط', 'لُوطٌ'),
    "ismā'īl": ('إسماعيل', 'إِسْمَاعِيلُ'),
    "isḥāq": ('إسحاق', 'إِسْحَاقُ'),
    "ya'qūb": ('يعقوب', 'يَعْقُوبُ'),
    'yaḥyā': ('يحيى', 'يَحْيَى'),
    'zakariyyā': ('زكريا', 'زَكَرِيَّا'),
    'maryam': ('مريم', 'مَرْيَمُ'),
    
    # ===== Sciences religieuses (harakat certains) =====
    'tafsīr': ('تفسير', 'تَفْسِير'),
    "ta'wīl": ('تأويل', 'تَأْوِيل'),
    'ḥadīth': ('حديث', 'حَدِيث'),
    'aḥādīth': ('أحاديث', 'أَحَادِيث'),
    'fiqh': ('فقه', 'فِقْه'),
    'uṣūl al-fiqh': ('أصول الفقه', 'أُصُولُ الفِقْهِ'),
    "'aqīda": ('عقيدة', 'عَقِيدَة'),
    'sīra': ('سيرة', 'سِيرَة'),
    'tajwīd': ('تجويد', 'تَجْوِيد'),
    "qirā'āt": ('قراءات', 'قِرَاءَات'),
    'taqtīt': ('تقطيع', 'تَقْطِيع'),
    'manṭiq': ('منطق', 'مَنْطِق'),
    'uṣūl al-ḥadīth': ('أصول الحديث', 'أُصُولُ الحَدِيثِ'),
    'ulum al-ḥadīth': ('علوم الحديث', 'عُلُومُ الحَدِيثِ'),
    'mustalah al-ḥadīth': ('مصطلح الحديث', 'مُصْطَلَحُ الحَدِيثِ'),
    
    # ===== Piliers et adorations (harakat certains) =====
    'ṣalāt': ('صلاة', 'صَلَاة'),
    'ṣalāh': ('صلاة', 'صَلَاة'),
    'zakāt': ('زكاة', 'زَكَاة'),
    'ṣawm': ('صوم', 'صَوْم'),
    'ḥajj': ('حج', 'حَجٌّ'),
    "i'tikāf": ('اعتكاف', 'اعْتِكَاف'),
    "du'ā'": ('دعاء', 'دُعَاء'),
    "'ibāda": ('عبادة', 'عِبَادَة'),
    "chahāda": ('شهادة', 'شَهَادَة'),
    'iḥsān': ('إحسان', 'إِحْسَان'),
    'īmān': ('إيمان', 'إِيمَان'),
    'islām': ('إسلام', 'إِسْلَام'),
    'aḏān': ('أذان', 'أَذَان'),
    'iqāma': ('إقامة', 'إِقَامَة'),
    "jumu'a": ('جمعة', 'جُمُعَة'),
    "'īd": ('عيد', 'عِيد'),
    
    # ===== Temps de prière (harakat certains) =====
    'ṣubḥ': ('صبح', 'صُبْح'),
    'fajr': ('فجر', 'فَجْر'),
    'ẓuhr': ('ظهر', 'ظُهْر'),
    "'aṣr": ('عصر', 'عَصْر'),
    'maghrib': ('مغرب', 'مَغْرِب'),
    "'ishā'": ('عشاء', 'عِشَاء'),
    "i'dād": ('إعداد', 'إِعْدَاد'),
    'tamhīd': ('تمهيد', 'تَمْهِيد'),
    'witr': ('وتر', 'وِتْر'),
    'tarāwīḥ': ('تراويح', 'تَرَاوِيح'),
    
    # ===== Terminologie juridique — HARAKAT RETIRÉS (sécurité) =====
    # Ces noms communs changent de vocalisation selon le contexte grammatical
    'ḥukm': ('حكم', None),
    'aḥkām': ('أحكام', None),
    "farā'iḍ": ('فرائض', None),
    'farīḍa': ('فريضة', None),
    'mīrāth': ('ميراث', None),
    'tawrīth': ('توريث', None),
    'naqṣ': ('نقص', None),
    'isqāṭ': ('إسقاط', None),
    'chirkat': ('شركة', None),
    'ḥajb': ('حجب', None),
    'al-ḥajb': ('الحجب', None),
    'fiqh al-ḥajb': ('فقه الحجب', None),
    'ar-rasmūkī': ('الرسموكي', None),
    'rasmūkī': ('الرسموكي', None),
    "ta'ṣīb": ('تعصيب', None),
    'aṣḥāb': ('أصحاب', None),
    'furūḍ': ('فروض', None),
    "aṣḥāb al-furūḍ": ('أصحاب الفروض', None),
    "'aql": ('عقل', None),
    'qiyās': ('قياس', None),
    "ijmā'": ('إجماع', None),
    'ijtihād': ('اجتهاد', None),
    'ḥalāl': ('حلال', None),
    'ḥarām': ('حرام', None),
    'mubāḥ': ('مباح', None),
    'makrūh': ('مكروه', None),
    'wājib': ('واجب', None),
    'fard': ('فرض', None),
    'sunnat': ('سنة', None),
    'sunna': ('سنة', None),
    'maṣlaḥa': ('مصلحة', None),
    "'urf": ('عرف', None),
    'istiḥsān': ('استحسان', None),
    "sadd al-dharā'i'": ('سد الذرائع', None),
    'dalīl': ('دليل', None),
    'adilla': ('أدلة', None),
    'maqṣad': ('مقصد', None),
    'maqāṣid': ('مقاصد', None),
    "charī'a": ('شريعة', None),
    "charī'": ('شرعي', None),
    'taklīf': ('تكليف', None),
    'asbāb': ('أسباب', None),
    'churūṭ': ('شروط', None),
    'arkān': ('أركان', None),
    'ṣiḥḥa': ('صحة', None),
    'butlān': ('بطلان', None),
    'fāsid': ('فاسد', None),
    'ṣaḥīḥ': ('صحيح', None),
    'bāṭil': ('باطل', None),
    "'umūm": ('عموم', None),
    'khuṣūṣ': ('خصوص', None),
    'iṭlāq': ('إطلاق', None),
    'taqyīd': ('تقييد', None),
    "'āmm": ('عام', None),
    'khāṣṣ': ('خاص', None),
    'muṭlaq': ('مطلق', None),
    'muqayyad': ('مقيد', None),
    'nāsikh': ('ناسخ', None),
    'mansūkh': ('منسوخ', None),
    'nasḫ': ('نسخ', None),
    'zāhir': ('ظاهر', None),
    'bāṭin': ('باطن', None),
    
    # ===== Textes et ouvrages (harakat certains sur noms propres) =====
    "Qur'ān": ('قرآن', 'قُرْآن'),
    "al-Qur'ān": ('القرآن', 'الْقُرْآن'),
    "qur'ān": ('قرآن', 'قُرْآن'),
    "al-qur'ān": ('القرآن', 'الْقُرْآن'),
    'muṣḥaf': ('مصحف', 'مُصْحَف'),
    "muwaṭṭa'": ('موطأ', 'مُوَطَّأ'),
    "al-muwaṭṭa'": ('الموطأ', 'الْمُوَطَّأ'),
    'bukhārī': ('البخاري', 'الْبُخَارِيّ'),
    'muslim': ('مسلم', 'مُسْلِم'),
    'ṣaḥīḥ muslim': ('صحيح مسلم', 'صَحِيحُ مُسْلِم'),
    'ṣaḥīḥ al-bukhārī': ('صحيح البخاري', 'صَحِيحُ الْبُخَارِيّ'),
    'tirmidī': ('الترمذي', 'التِّرْمِذِيّ'),
    "nasā'ī": ('النسائي', 'النَّسَائِيّ'),
    'abū dāwūd': ('أبو داود', 'أَبُو دَاوُدَ'),
    'ibn māja': ('ابن ماجه', 'ابْنِ مَاجَهْ'),
    'ar-risāla': ('الرسالة', 'الرِّسَالَة'),
    'kifāyat aṭ-ṭālib': ('كفاية الطالب', 'كِفَايَةُ الطَّالِبِ'),
    'ash-sharḥ': ('الشرح', 'الشَّرْح'),
    'az-zarqānī': ('الزرقاني', 'الزَّرْقَانِيّ'),
    'sharḥ az-zarqānī': ('شرح الزرقاني', 'شَرْحُ الزَّرْقَانِيّ'),
    'jawāhir al-maknūna': ('جواهر المكنونة', 'جَوَاهِرُ الْمَكْنُونَةِ'),
    'manẓūma jawāhir al-maknūna': ('منظومة جواهر المكنونة', 'مَنْظُومَةُ جَوَاهِرِ الْمَكْنُونَةِ'),
    'ad-dardīr': ('الدردير', 'الدَّرْدِيرُ'),
    'ad-dasūqī': ('الدسوقي', 'الدَّسُوقِيُّ'),
    'tafsīr al-jalālayn': ('تفسير الجلالين', 'تَفْسِيرُ الْجَلَالَيْنِ'),
    "tashīl 'ulūm at-tanzīl": ('تسهيل علوم التنزيل', 'تَسْهِيلُ عُلُومِ التَّنْزِيلِ'),
    'ibn jazayy': ('ابن جزي', 'ابْنِ جُزَيْ'),
    'ibn qayyim': ('ابن قيم', 'ابْنِ قَيِّمٍ'),
    'ibn taymiyya': ('ابن تيمية', 'ابْنِ تَيْمِيَّةَ'),
    "ash-shāfi'ī": ('الشافعي', 'الشَّافِعِيُّ'),
    'abū ḥanīfa': ('أبو حنيفة', 'أَبُو حَنِيفَةَ'),
    'aḥmad ibn ḥanbal': ('أحمد بن حنبل', 'أَحْمَدُ بْنُ حَنْبَلَ'),
    'mālik ibn anas': ('مالك بن أنس', 'مَالِكُ بْنُ أَنَسٍ'),
    'sufyān ath-thawrī': ('سفيان الثوري', 'سُفْيَانُ الثَّوْرِيُّ'),
    "al-'aẓīm": ('العظيم', 'الْعَظِيمُ'),
    'al-ḥakīm': ('الحكيم', 'الْحَكِيمُ'),
    
    # ===== Sourates du Coran (harakat certains) =====
    'al-fātiḥa': ('الفاتحة', 'الْفَاتِحَة'),
    'al-baqara': ('البقرة', 'الْبَقَرَة'),
    "āl 'imrān": ('آل عمران', 'آلِ عِمْرَانَ'),
    "an-nisā'": ('النساء', 'النِّسَاء'),
    "al-mā'ida": ('المائدة', 'الْمَائِدَة'),
    "al-an'ām": ('الأنعام', 'الْأَنْعَام'),
    "al-a'rāf": ('الأعراف', 'الْأَعْرَاف'),
    'al-anfāl': ('الأنفال', 'الْأَنْفَال'),
    'at-tawba': ('التوبة', 'التَّوْبَة'),
    'yūnus': ('يونس', 'يُونُسَ'),
    'hūd': ('هود', 'هُودٌ'),
    'yūsuf': ('يوسف', 'يُوسُفُ'),
    "ar-ra'd": ('الرعد', 'الرَّعْدُ'),
    'ibrāhīm': ('إبراهيم', 'إِبْرَاهِيمُ'),
    'al-ḥijr': ('الحجر', 'الْحِجْرُ'),
    'an-naḥl': ('النحل', 'النَّحْلُ'),
    "al-isrā'": ('الإسراء', 'الْإِسْرَاءُ'),
    'al-kahf': ('الكهف', 'الْكَهْفُ'),
    'maryam': ('مريم', 'مَرْيَمُ'),
    'ṭāhā': ('طه', 'طه'),
    "al-mu'minūn": ('المؤمنون', 'الْمُؤْمِنُونَ'),
    'an-nūr': ('النور', 'النُّورُ'),
    'al-furqān': ('الفرقان', 'الْفُرْقَانُ'),
    "ash-shu'arā'": ('الشعراء', 'الشُّعَرَاءُ'),
    'an-naml': ('النمل', 'النَّمْلُ'),
    'al-qaṣaṣ': ('القصص', 'الْقَصَصُ'),
    "al-'ankabūt": ('العنكبوت', 'الْعَنْكَبُوتُ'),
    'ar-rūm': ('الروم', 'الرُّومُ'),
    'luqmān': ('لقمان', 'لُقْمَانُ'),
    'as-sajda': ('السجدة', 'السَّجْدَةُ'),
    'al-aḥzāb': ('الأحزاب', 'الْأَحْزَابُ'),
    "saba'": ('سبأ', 'سَبَأٌ'),
    'fāṭir': ('فاطر', 'فَاطِرٌ'),
    'yāsīn': ('يس', 'يس'),
    'aṣ-ṣāffāt': ('الصافات', 'الصَّافَّاتُ'),
    'ṣād': ('ص', 'ص'),
    'az-zumar': ('الزمر', 'الزُّمَرُ'),
    'ghāfir': ('غافر', 'غَافِرٌ'),
    'fuṣṣilat': ('فصلت', 'فُصِّلَتْ'),
    'ash-shūrā': ('الشورى', 'الشُّورَى'),
    'az-zukhruf': ('الزخرف', 'الزُّخْرُفُ'),
    'ad-dukhān': ('الدخان', 'الدُّخَانُ'),
    'al-jāthiya': ('الجاثية', 'الْجَاثِيَةُ'),
    'al-aḥqāf': ('الأحقاف', 'الْأَحْقَافُ'),
    'muḥammad': ('محمد', 'مُحَمَّدٌ'),
    'al-fatḥ': ('الفتح', 'الْفَتْحُ'),
    'al-ḥujurāt': ('الحجرات', 'الْحُجُرَاتُ'),
    'qāf': ('ق', 'ق'),
    'adh-dhāriyāt': ('الذاريات', 'الذَّارِيَاتُ'),
    'aṭ-ṭūr': ('الطور', 'الطُّورُ'),
    'an-najm': ('النجم', 'النَّجْمُ'),
    'al-qamar': ('القمر', 'الْقَمَرُ'),
    'ar-raḥmān': ('الرحمن', 'الرَّحْمَٰنُ'),
    "al-wāqi'a": ('الواقعة', 'الْوَاقِعَةُ'),
    'al-ḥadīd': ('الحديد', 'الْحَدِيدُ'),
    'al-mujādala': ('المجادلة', 'الْمُجَادَلَةُ'),
    'al-ḥashr': ('الحشر', 'الْحَشْرُ'),
    'al-mumtaḥana': ('الممتحنة', 'الْمُمْتَحَنَةُ'),
    'aṣ-ṣaff': ('الصف', 'الصَّفُّ'),
    "al-jumu'a": ('الجمعة', 'الْجُمُعَةُ'),
    'al-munāfiqūn': ('المنافقون', 'الْمُنَافِقُونَ'),
    'at-taghābun': ('التغابن', 'التَّغَابُنُ'),
    'aṭ-ṭalāq': ('الطلاق', 'الطَّلَاقُ'),
    'at-taḥrīm': ('التحريم', 'التَّحْرِيمُ'),
    'al-mulk': ('الملك', 'الْمُلْكُ'),
    'al-qalam': ('القلم', 'الْقَلَمُ'),
    'al-ḥāqqa': ('الحاقة', 'الْحَاقَّةُ'),
    "al-ma'ārij": ('المعارج', 'الْمَعَارِجُ'),
    'nūḥ': ('نوح', 'نُوحٌ'),
    'al-jinn': ('الجن', 'الْجِنُّ'),
    'al-muzzammil': ('المزمل', 'الْمُزَّمِّلُ'),
    'al-mudaththir': ('المدثر', 'الْمُدَّثِّرُ'),
    'al-qiyāma': ('القيامة', 'الْقِيَامَةُ'),
    'al-insān': ('الإنسان', 'الْإِنْسَانُ'),
    'al-mursalāt': ('المرسلات', 'الْمُرْسَلَاتُ'),
    "an-naba'": ('النبأ', 'النَّبَأُ'),
    "an-nāzi'āt": ('النازعات', 'النَّازِعَاتُ'),
    "'abasa": ('عبس', 'عَبَسَ'),
    'at-takwīr': ('التكوير', 'التَّكْوِيرُ'),
    'al-infiṭār': ('الإنفطار', 'الْإِنْفِطَارُ'),
    'al-muṭaffifīn': ('المطففين', 'الْمُطَفِّفِينَ'),
    'al-inshiqāq': ('الإنشقاق', 'الْإِنْشِقَاقُ'),
    'al-burūj': ('البروج', 'الْبُرُوجُ'),
    'aṭ-ṭāriq': ('الطارق', 'الطَّارِقُ'),
    "al-a'lā": ('الأعلى', 'الْأَعْلَى'),
    'al-ghāshiya': ('الغاشية', 'الْغَاشِيَةُ'),
    'al-fajr': ('الفجر', 'الْفَجْرُ'),
    'al-balad': ('البلد', 'الْبَلَدُ'),
    'ash-shams': ('الشمس', 'الشَّمْسُ'),
    'al-layl': ('الليل', 'اللَّيْلُ'),
    'aḍ-ḍuḥā': ('الضحى', 'الضُّحَى'),
    'ash-sharḥ': ('الشرح', 'الشَّرْحُ'),
    'at-tīn': ('التين', 'التِّينُ'),
    "al-'alaq": ('العلق', 'الْعَلَقُ'),
    'al-qadr': ('القدر', 'الْقَدْرُ'),
    'al-bayyina': ('البينة', 'الْبَيِّنَةُ'),
    'az-zalzala': ('الزلزلة', 'الزَّلْزَلَةُ'),
    "al-'ādiyāt": ('العاديات', 'الْعَادِيَاتُ'),
    "al-qāri'a": ('القارعة', 'الْقَارِعَةُ'),
    'at-takāthur': ('التكاثر', 'التَّكَاثُرُ'),
    "al-'aṣr": ('العصر', 'الْعَصْرُ'),
    'al-humaza': ('الهمزة', 'الْهُمَزَةُ'),
    'al-fīl': ('الفيل', 'الْفِيلُ'),
    'quraysh': ('قريش', 'قُرَيْشٌ'),
    "al-mā'ūn": ('الماعون', 'الْمَاعُونُ'),
    'al-kawthar': ('الكوثر', 'الْكَوْثَرُ'),
    'al-kāfirūn': ('الكافرون', 'الْكَافِرُونَ'),
    'an-naṣr': ('النصر', 'النَّصْرُ'),
    'al-masad': ('المسد', 'الْمَسَدُ'),
    'al-ikhlāṣ': ('الإخلاص', 'الْإِخْلَاصُ'),
    'al-falaq': ('الفلق', 'الْفَلَقُ'),
    'an-nās': ('الناس', 'النَّاسُ'),
    
    # ===== Lettres de l'alphabet (harakat certains) =====
    'alif': ('ألف', 'أَلِف'),
    "bā'": ('باء', 'بَاء'),
    "tā'": ('تاء', 'تَاء'),
    "thā'": ('ثاء', 'ثَاء'),
    'jīm': ('جيم', 'جِيم'),
    "ḥā'": ('حاء', 'حَاء'),
    "khā'": ('خاء', 'خَاء'),
    'dāl': ('دال', 'دَال'),
    'dhāl': ('ذال', 'ذَال'),
    "rā'": ('راء', 'رَاء'),
    'zāy': ('زاي', 'زَاي'),
    'sīn': ('سين', 'سِين'),
    'shīn': ('شين', 'شِين'),
    'ṣād': ('صاد', 'صَاد'),
    'ḍād': ('ضاد', 'ضَاد'),
    "ṭā'": ('طاء', 'طَاء'),
    "ẓā'": ('ظاء', 'ظَاء'),
    "'ayn": ('عين', 'عَيْن'),
    'ghayn': ('غين', 'غَيْن'),
    "fā'": ('فاء', 'فَاء'),
    'qāf': ('قاف', 'قَاف'),
    'kāf': ('كاف', 'كَاف'),
    'lām': ('لام', 'لَام'),
    'mīm': ('ميم', 'مِيم'),
    'nūn': ('نون', 'نُون'),
    "hā'": ('هاء', 'هَاء'),
    'wāw': ('واو', 'وَاو'),
    "yā'": ('ياء', 'يَاء'),
    
    # ===== Autres termes courants — HARAKAT RETIRÉS =====
    'imām': ('إمام', 'إِمَام'),
    "'ālim": ('عالم', 'عَالِم'),
    "'ulamā'": ('علماء', 'عُلَمَاء'),
    'muftī': ('مفتي', 'مُفْتِي'),
    'faqīh': ('فقيه', 'فَقِيه'),
    "fuqahā'": ('فقهاء', 'فُقَهَاء'),
    'muḥaddith': ('محدث', 'مُحَدِّث'),
    'mufassir': ('مفسر', 'مُفَسِّر'),
    'rasūl': ('رسول', 'رَسُول'),
    'nabī': ('نبي', 'نَبِيّ'),
    'ṣaḥāba': ('صحابة', 'صَحَابَة'),
    'ṣaḥābī': ('صحابي', 'صَحَابِيّ'),
    "tābi'ūn": ('تابعون', 'تَابِعُونَ'),
    'umma': ('أمة', 'أُمَّة'),
    'dīn': ('دين', 'دِين'),
    'ḥikma': ('حكمة', 'حِكْمَة'),
    "'ilm": ('علم', 'عِلْم'),
    "'amal": ('عمل', 'عَمَل'),
    'qalb': ('قلب', 'قَلْب'),
    'nafs': ('نفس', 'نَفْس'),
    'rūḥ': ('روح', 'رُوح'),
    'dunyā': ('دنيا', 'دُنْيَا'),
    'ākhira': ('آخرة', 'آخِرَة'),
    'janna': ('جنة', 'جَنَّة'),
    'nār': ('نار', 'نَار'),
    'jahannam': ('جهنم', 'جَهَنَّمَ'),
    'barzakh': ('برزخ', 'بَرْزَخ'),
    'tawba': ('توبة', 'تَوْبَة'),
    'istighfār': ('استغفار', 'اسْتِغْفَار'),
    'shukr': ('شكر', 'شُكْر'),
    'ṣabr': ('صبر', 'صَبْر'),
    "'adl": ('عدل', 'عَدْل'),
    'raḥma': ('رحمة', 'رَحْمَة'),
    'baraka': ('بركة', 'بَرَكَة'),
    "ni'ma": ('نعمة', 'نِعْمَة'),
    'fitna': ('فتنة', 'فِتْنَة'),
    "bid'a": ('بدعة', 'بِدْعَة'),
    'ijāza': ('إجازة', 'إِجَازَة'),
    'riwāya': ('رواية', 'رِوَايَة'),
    'isnād': ('إسناد', 'إِسْنَاد'),
    'matn': ('متن', 'مَتْن'),
    'sharḥ': ('شرح', 'شَرْح'),
    'ḥāshiyya': ('حاشية', 'حَاشِيَة'),
    "ta'līq": ('تعليق', 'تَعْلِيق'),
    'manẓūma': ('منظومة', 'مَنْظُومَة'),
    'rasm': ('رسم', 'رَسْم'),
    "qirā'a": ('قراءة', 'قِرَاءَة'),
    'ḥafṣ': ('حفص', 'حَفْصٌ'),
    'warsh': ('ورش', 'وَرْشٌ'),
    "rak'a": ('ركعة', 'رَكْعَة'),
    "rak'at": ('ركعات', 'رَكَعَاتُ'),
    'sujūd': ('سجود', 'سُجُود'),
    'sajda': ('سجدة', 'سَجْدَة'),
    'qiyām': ('قيام', 'قِيَام'),
    "rukū'": ('ركوع', 'رُكُوع'),
    'tashahhud': ('تشهد', 'تَشَهُّد'),
    'taslīm': ('تسليم', 'تَسْلِيم'),
    'waqf': ('وقف', 'وَقْف'),
    'ṣadaqa': ('صدقة', 'صَدَقَة'),
    'bayt al-māl': ('بيت المال', 'بَيْتُ الْمَالِ'),
    'ḥadd': ('حد', 'حَدٌّ'),
    'qiṣāṣ': ('قصاص', 'قِصَاصٌ'),
    'diyya': ('دية', 'دِيَةٌ'),
}

# Construire l'index de recherche insensible à la casse
AR_INDEX = {}
for key, (ar, ar_harakat) in AR_DICT.items():
    AR_INDEX[key.lower()] = (ar, ar_harakat)

# ============================================================
# MOTIFS DE DÉTECTION — NOUVELLE CONVENTION
# ============================================================

# Caractères de translittération arabe (nouvelle convention)
# Ce sont les marqueurs qui signalent qu'un mot est arabe translittéré
TRANSLIT_CHARS = "ḥḍṭẓāīūĀĪŪ"
TRANSLIT_SET = set(TRANSLIT_CHARS)

# Mot qui contient au moins un caractère de translittération OU commence par un digramme arabe
# Les digrammes : ch, gh, kh, th, dh (mais aussi q qui est rare en français sauf exceptions)
TRANSLIT_PATTERN = re.compile(
    rf'(?<![a-zA-Z{TRANSLIT_CHARS}])'
    rf'([a-zA-Z{TRANSLIT_CHARS}][a-zA-Z{TRANSLIT_CHARS}-]*)'
    rf'(?![a-zA-Z{TRANSLIT_CHARS}])'
)

# Mots français à exclure (faux positifs avec 'q' ou autres)
FRENCH_EXCLUDE = {
    'jusqu', 'lorsqu', 'laquelle', 'pourquoi', 'chaque', 'quiconque', 'cinq',
    'chacune', 'chacun', 'quelque', 'jusque', 'lorsque', 'qu', 'quelqu',
    'chacqu', 'cinqu', 'ce', 'cet', 'cette', 'ces', 'mon', 'ton', 'son',
    'ma', 'ta', 'sa', 'mes', 'tes', 'ses', 'le', 'la', 'les', 'un', 'une',
    'des', 'du', 'de', 'et', 'ou', 'où', 'est', 'que', 'qui', 'quoi', 'dont',
    'ne', 'pas', 'plus', 'moins', 'très', 'trop', 'peu', 'bien', 'mal',
    'sans', 'avec', 'pour', 'par', 'sur', 'sous', 'dans', 'entre', 'vers',
    'chez', 'depuis', 'pendant', 'avant', 'après', 'comme', 'si', 'car',
    'donc', 'alors', 'ainsi', 'encore', 'toujours', 'jamais', 'souvent',
    'parfois', 'ici', 'là', 'où', 'quand', 'comment', 'pourquoi',
    'chapitre', 'leçon', 'page', 'ligne', 'mot', 'texte', 'point',
    'saint', 'sainte', 'grand', 'grande', 'petit', 'petite', 'bon', 'bonne',
    'chose', 'choses', 'homme', 'femme', 'enfant', 'gens', 'personne',
    'temps', 'jour', 'nuit', 'mois', 'année', 'an', 'fois', 'partie',
    'question', 'réponse', 'savoir', 'pouvoir', 'vouloir', 'devoir',
    'falloir', 'faire', 'dire', 'aller', 'venir', 'voir', 'croire',
    'penser', 'trouver', 'donner', 'prendre', 'mettre', 'passer',
    'quand', 'quant', 'quanta', 'quinze', 'quatorze', 'treize', 'douze',
    'onze', 'dix', 'neuf', 'huit', 'sept', 'six', 'cinq', 'quatre',
    'trois', 'deux', 'un', 'premier', 'deuxième', 'troisième',
    'chaud', 'froid', 'chaude', 'froide', 'coeur', 'coeurs',
    'alors', 'aucun', 'aucune', 'beaucoup', 'plusieurs', 'certains',
    'certaines', 'tous', 'toutes', 'tout', 'toute', 'même', 'aussi',
    'seul', 'seule', 'seuls', 'seules', 'propre', 'propres',
    'autre', 'autres', 'même', 'memes', 'tels', 'telles', 'tel', 'telle',
}

# ============================================================
# FONCTIONS D'AMÉLIORATION
# ============================================================

def add_nbsp_french(text):
    """Ajoute les espaces insécables pour la typographie française."""
    text = re.sub(r'(\S)\s+([;!?»])', r'\1&nbsp;\2', text)
    text = re.sub(r'(«)\s+(\S)', r'\1&nbsp;\2', text)
    text = re.sub(r'([a-zA-Zàâäéèêëîïôöùûüÿçœæ])\s+(:)', r'\1&nbsp;\2', text)
    return text

def clean_empty_paragraphs(html):
    """Supprime les paragraphes vides."""
    html = re.sub(r'<p>\s*</p>', '', html)
    html = re.sub(r'<p>\s*&nbsp;\s*</p>', '', html)
    return html

def has_translit_marker(word):
    """Vérifie si un mot contient un marqueur de translittération arabe."""
    # 1. Caractères spéciaux : ḥ ḍ ṭ ẓ ā ī ū
    if any(c in TRANSLIT_SET for c in word):
        return True
    # 2. Lettre q isolée ou en début de mot (rare en français hors qu-/q-)
    # On exclut les cas français courants
    if 'q' in word.lower():
        wl = word.lower()
        if not any(wl.startswith(excl) for excl in ['qu', 'cinq', 'jusqu', 'lorsqu', 'chacqu', 'quelqu', 'cinqu']):
            return True
    return False

def add_em_and_arabic(html):
    """Ajoute les balises <em> et l'arabe aux termes translittérés."""
    
    parts = []
    last_end = 0
    tag_pattern = re.compile(r'<[^>]+>')
    
    def safe_replace(m):
        term = m.group(1)
        term_lower = term.lower()
        
        # Vérifier si c'est un marqueur de translittération
        if not has_translit_marker(term):
            return term
        
        # Exclure les mots français courants
        if term_lower in FRENCH_EXCLUDE:
            return term
        
        # Chercher dans le dictionnaire
        ar_entry = AR_INDEX.get(term_lower)
        if ar_entry:
            ar, ar_harakat = ar_entry
            ar_display = ar_harakat if ar_harakat else ar
            return f'<em>{term}</em> <span dir="rtl" lang="ar">({ar_display})</span>'
        
        return f'<em>{term}</em>'
    
    for tag_match in tag_pattern.finditer(html):
        text_part = html[last_end:tag_match.start()]
        if text_part:
            text_part = TRANSLIT_PATTERN.sub(safe_replace, text_part)
            parts.append(text_part)
        parts.append(tag_match.group(0))
        last_end = tag_match.end()
    
    text_part = html[last_end:]
    if text_part:
        text_part = TRANSLIT_PATTERN.sub(safe_replace, text_part)
        parts.append(text_part)
    
    return ''.join(parts)

def create_matn_box(html):
    """Encadre le texte du matn (texte fondateur cité)."""
    patterns = [
        r'(<p>[^<]*(?:a dit|que Dieu lui fasse miséricorde|raḥimahu llāh|ibn abī zayd)[^<]*</p>)',
        r'(<p>[^<]*ar-rasmūkī[^<]*</p>)',
        r'(<p>[^<]*mālik[^<]*a dit[^<]*</p>)',
    ]
    
    for pat in patterns:
        match = re.search(pat, html, re.IGNORECASE)
        if match:
            before = html[:match.start()]
            if 'matn-box' in before[-200:]:
                continue
            
            start = match.start()
            rest = html[start:]
            end_match = re.search(r'<h[23]', rest)
            if end_match:
                end = start + end_match.start()
            else:
                end = len(html)
            
            matn_content = html[start:end]
            if len(matn_content) < 8000:
                html = html[:start] + f'\n<div class="matn-box">\n<span class="matn-label">Texte fondateur</span>\n{matn_content}\n</div>\n' + html[end:]
                break
    
    return html

def enrich_html(html):
    """Applique toutes les améliorations au HTML."""
    
    # 0. D'ABORD : convertir l'ancienne translittération vers la nouvelle
    html = convert_translit(html)
    
    # 1. Nettoyage paragraphes vides
    html = clean_empty_paragraphs(html)
    
    # 2. Ajout des balises <em> et de l'arabe
    html = add_em_and_arabic(html)
    
    # 3. Espaces insécables français
    html = add_nbsp_french(html)
    
    # 4. Encadré matn
    html = create_matn_box(html)
    
    # Nettoyer les doubles sauts de ligne excessifs
    html = re.sub(r'\n{3,}', '\n\n', html)
    
    return html

def compute_changes(original, modified):
    """Calcule des statistiques sur les changements."""
    return {
        'em_added': modified.count('<em>') - original.count('<em>'),
        'arabic_added': modified.count('dir="rtl" lang="ar"'),
        'nbsp_added': modified.count('&nbsp;') - original.count('&nbsp;'),
        'objectives_boxes': modified.count('objectives-box'),
        'matn_boxes': modified.count('matn-box'),
        'empty_p_removed': original.count('<p></p>') - modified.count('<p></p>'),
    }

# ============================================================
# EXÉCUTION PRINCIPALE
# ============================================================

def main():
    apply_changes = '--apply' in sys.argv
    
    books_dir = 'content/books'
    output_dir = 'content/books-enriched' if not apply_changes else books_dir
    
    if not apply_changes:
        os.makedirs(output_dir, exist_ok=True)
    
    total_stats = Counter()
    lessons_processed = 0
    books_processed = 0
    
    print(f"{'='*60}")
    print(f"MINHĀJ — ENRICHISSEMENT DE LA MISE EN PAGE")
    print(f"{'='*60}")
    print(f"Mode : {'APPLICATION DÉFINITIVE' if apply_changes else 'SIMULATION (rapport seulement)'}")
    print(f"Convention phonétique : j (jim), ch (chîn), ' (ʿayn/hamza), gh, kh, th, dh")
    print(f"Dictionnaire : {len(AR_DICT)} entrées")
    print(f"Règle harakat : seulement sur termes FIGÉS à vocalisation CERTAINE")
    print(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    books = sorted(f for f in os.listdir(books_dir) if f.endswith('.json'))
    
    for book_file in books:
        book_path = os.path.join(books_dir, book_file)
        data = json.load(open(book_path, encoding='utf-8'))
        
        book_modified = False
        book_stats = Counter()
        lessons_in_book = 0
        
        for lesson in data.get('lessons', []):
            fr = lesson.get('htmlFr', '')
            if not fr or len(fr.strip()) < 100:
                continue
            
            lessons_in_book += 1
            enriched = enrich_html(fr)
            
            if enriched != fr:
                lesson['htmlFr'] = enriched
                book_modified = True
                changes = compute_changes(fr, enriched)
                book_stats.update(changes)
        
        if lessons_in_book > 0:
            books_processed += 1
            lessons_processed += lessons_in_book
            
            if book_modified:
                total_stats.update(book_stats)
                
                if apply_changes:
                    with open(book_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                else:
                    out_path = os.path.join(output_dir, book_file)
                    with open(out_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                
                print(f"✅ {book_file:35s} | {lessons_in_book:3d} leçons | "
                      f"em:{book_stats['em_added']:+5d} | ar:{book_stats['arabic_added']:5d} | "
                      f"nbsp:{book_stats['nbsp_added']:+5d} | matn:{book_stats['matn_boxes']}")
            else:
                print(f"⏭️  {book_file:35s} | {lessons_in_book:3d} leçons | AUCUN CHANGEMENT")
    
    print()
    print(f"{'='*60}")
    print(f"RAPPORT GLOBAL")
    print(f"{'='*60}")
    print(f"Livres traités      : {books_processed}")
    print(f"Leçons traitées      : {lessons_processed}")
    print(f"Balises <em> ajoutées : {total_stats['em_added']:+d}")
    print(f"Mots arabes ajoutés  : {total_stats['arabic_added']}")
    print(f"&nbsp; ajoutés       : {total_stats['nbsp_added']:+d}")
    print(f"Encadrés objectifs   : {total_stats['objectives_boxes']}")
    print(f"Encadrés matn        : {total_stats['matn_boxes']}")
    print(f"<p></p> supprimés    : {total_stats['empty_p_removed']}")
    print()
    
    if not apply_changes:
        print(f"💾 Fichiers enrichis sauvegardés dans : {output_dir}/")
        print(f"   (originaux non touchés)")
        print()
        print("Pour appliquer définitivement :")
        print("  python3 scripts-translate/enrich-layout.py --apply")
    else:
        print(f"✅ Modifications appliquées directement dans {books_dir}/")

if __name__ == '__main__':
    main()
