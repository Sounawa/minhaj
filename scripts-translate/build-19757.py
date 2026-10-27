#!/usr/bin/env python3
# build-19757.py — 19757 « Jurisprudence : l'index des sources et des références »
# (fiqh-tanawi-3, lessons[31], badge Leçon 33/33) — INDEX des sources (fihrist
# al-maṣādir wa-l-marāğiʿ), PAS une leçon (règle ah) — DERNIER document du volume :
# après lui LE LIVRE EST COMPLET (intro + 32 leçons + 2 index = 33/33). Trente-trois
# notices bibliographiques rendues intégralement dans l'ordre du volume (titre,
# auteur + date hégirienne, éditeur, édition, année) ; les deux Ibn Rušd distingués
# par la date (al-Ǧadd 520 H : notices 3/27 ; al-Ḥafīd 595 H : notice 1) ;
# DÉDOUBLEMENTS imprimés portés tels quels (Mudawwana 24/31 ; Muḫtaṣar al-fiqhī
# 23/33) ; onomastique « Bahrām b. ʿAbd Allāh » répétée d'un index à l'autre (ax) ;
# graphies imprimées portées telles quelles (Beyrou coupé, crochet égaré « ] »,
# « 5/32 ] », éditeur « al-Ḫabṭūr ») ; ancrage vérifié par recherche normalisée :
# al-Muqaddimāt 10 leçons (exploitation 3/37, 3/37-38, 3/39 des trois dernières),
# Hāšiya ad-Dasūqī 28 (formule liminaire), Manḫ al-Ğalīl 8, Ibn ʿArafah 7, aḏ-Ḏaḫīra
# 5, az-Zurqānī 5 ; hadith du troisième des deux associés sort des Sunan Abī Dāwūd
# (19537) ; zéro āya/zéro hadith cités dans le document — dixième tour sans
# protocole triple ; N.d.T. : titre (h1 fait foi, 26e tranchage), nature d'index,
# dédoublements, deux Ibn Rušd, chandeliers du Mukhtaṣar, galerie des commentaires
# de Khalīl, onomastique, dates, ancrage, ACHÈVEMENT (livre complet 33/33).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19757_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    ar = [c for c in ar if c != chr(0xFDFA)]
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'dl', 'dt', 'dd', 'br']:
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if tag in ('br',):
        if o and c:
            issues.append(f'balise {tag} fermante inattendue')
        continue
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

norm = lambda s: s.replace("'", chr(0x2019))
probes = [
    "Jurisprudence : l'index des sources et des références",
    "1. Bidāyat al-muğtahid wa-nihāyat al-muqtaṣid :",
    "dit Ibn Rušd al-Ḥafīd (mort en 595 H)",
    "Dār al-ḥadīṯ, le Caire",
    "date de publication : 1425 H – 2004",
    "le petit-fils (al-Ḥafīd, 595 H) à cette notice, le grand-père (al-Ǧadd, 520 H) aux notices 3 et 27",
    "2. Bulġat as-sālik li-aqrab al-masālik :",
    "dit la Hāšiyat aṣ-Ṣāwī ʿalā š-Šarḥ aṣ-ṣaġīr",
    "Aqrab al-masālik li-maḏhab al-Imām Mālik",
    "dit aṣ-Ṣāwī al-Mālikī (mort en 1241 H)",
    "Dār al-maʿārif ; l'édition : sans édition ni date",
    "« quant à la langue : c'est le ḥifẓ »",
    "l'index ne donne point de notice propre au Šarḫ d'ad-Dardīr : il se tient dans celle-ci, par la voix de sa hāšiya",
    "3. al-Bayān wa-t-Taḥṣīl wa-š-šarḥ wa-t-tawǧīh wa-t-taʿlīl li-masāʾil al-mustaḫraǧa, de son auteur Abū l-Walīd Muḥammad b. Aḥmad b. Rušd al-Qurṭubī (mort en 520 H), établi par :",
    "le docteur Muḥammad Ḥiǧǧī et d'autres",
    "l'édition : la deuxième, 1408 H – 1988",
    "L'exploitation de la leçon de la ʿinān (19670) sort de ce livre",
    "4. Tahḏīb al-luġa :",
    "Abū Manṣūr (mort en 370 H)",
    "5. at-Tāǧ wa-l-iklīl li-Mukhtaṣar Khalīl :",
    "al-ʿAbdarī al-Ġarnāṭī, Abū ʿAbd Allāh al-Mawwāq al-Mālikī (mort en 897 H)",
    "l'édition : la première, 1416 H – 1994",
    "Le cours le convoque aux leçons du ṣulḥ du sang et des plaies (19456)",
    "le Tāǧ de la galerie",
    "6. at-Taʿrīfāt :",
    "az-Zayn aš-Šarīf al-Ǧurǧānī (mort en 816 H)",
    "7. at-Tawḍīḥ fī šarḫ al-Muḫtaṣar al-farʿī li-Ibn al-Ḥāǧib :",
    "Ḍiyāʾ ad-Dīn al-Ǧundī al-Mālikī al-Miṣrī (mort en 776 H)",
    "le centre Naǧībawiyya pour les manuscrits et le service du patrimoine",
    "8. Ǧāmiʿ al-ummahāt :",
    "Ǧamāl ad-Dīn Ibn al-Ḥāǧib al-Kurdī al-Mālikī (mort en 646 H)",
    "al-Aḫḍar al-Aḫḍarī",
    "l'édition : la deuxième, 1421 H – 2000",
    "les deux index se répondent",
    "9. al-Ǧāmiʿ al-musnad aṣ-ṣaḥīḥ al-muḫtaṣar des affaires du messager de Dieu — que Dieu le bénisse et le salue —, de ses sunna et de ses jours :",
    "al-Buḫārī al-Ǧaʿfī",
    "numérotation de Muḥammad Fuʾād ʿAbd al-Bāqī",
    "l'édition : la première, 1422 H",
    "10. Ḥāšiyat ad-Dasūqī ʿalā š-Šarḥ al-kabīr :",
    "Muḥammad b. Aḥmad b. ʿArafah ad-Dasūqī al-Mālikī (mort en 1230 H)",
    "La voix la plus omniprésente du volume : vingt-huit leçons au moins convoquent la Hāšiya",
    "de la première leçon du cours (15355, dont le titre même la nomme) à la dernière (19744)",
    "les deux chandeliers du Mukhtaṣar de Khalīl",
    "11. Sunan Abī Dāwūd :",
    "as-Siğistānī (mort en 275 H)",
    "Šuʿayb al-Arnāʾūṭ – Muḥammad Kāmil Qara Ballī",
    "l'édition : la première, 1430 H – 2009",
    "le hadith du troisième des deux associés",
    "« anā ṯāliṯ aš-šarīkayn »",
    "les glossateurs leurs notices là",
    "12. aḏ-Ḏaḫīra :",
    "dit al-Qarāfī (mort en 684 H)",
    "Muḥammad Ḥiǧǧī, Saʿīd Aʿrāb et Muḥammad Buḫabza",
    "aḏ-Ḏaḫīra 7/85 sur l'interdiction de l'aliéné",
    "13. Sunan at-Tirmiḏī :",
    "at-Tirmiḏī, Abū ʿĪsā (mort en 279 H)",
    "Aḥmad Muḥammad Šākir, Muḥammad Fuʾād ʿAbd al-Bāqī et Ibrāhīm ʿAṭwa ʿAwaḍ",
    "la société de la bibliothèque et de l'imprimerie Muṣṭafā al-Bābī al-Ḥalabī – Égypte",
    "l'édition : la deuxième, 1395 H – 1975",
    "14. aš-Šāmil fī fiqh al-Imām Mālik :",
    "Bahrām b. ʿAbd Allāh b. ʿAbd al-ʿAzīz b. ʿUmar b. ʿIwaḍ, Abū l-Baqāʾ, Tāǧ ad-Dīn as-Silmī ad-Damīrī ad-Dimyāṭī al-Mālikī (mort en 805 H)",
    "« Bahrām b. ʿAbd Allāh » ouvre la notice comme elle ouvrait la notice du Damīrī à l'index des figures (19756)",
    "la leçon de l'associé de mufāwaḍa et du litige (19601)",
    "15. Šarḫ az-Zurqānī ʿalā Mukhtaṣar Khalīl, et avec lui al-Fatḥ ar-rabbānī fīmā ḏahala ʿan-hu z-Zurqānī :",
    "ʿAbd al-Bāqī b. Yūsuf b. Aḥmad az-Zurqānī al-Miṣrī (mort en 1099 H)",
    "vocalisé, corrigé, et ses āyas référencées par : ʿAbd as-Salām Muḥammad Amīn",
    "l'édition : la première, 1422 H – 2002",
    "un commentaire double dans une notice double",
    "16. aṣ-Ṣiḥāḥ, tāǧ al-luġa wa-ṣaḥāḥ al-ʿarabiyya :",
    "Ismāʿīl b. Ḥammād al-Ǧawharī",
    "Dār al-ʿilm li-l-malāyīn",
    "l'édition : la première, le Caire, 1376 H – 1956",
    "17. Ṣaḥīḥ Muslim, nommé : al-Musnad aṣ-ṣaḥīḥ al-muḫtaṣar, transmis par les justes d'après les justes, jusqu'au messager de Dieu — que Dieu le bénisse et le salue :",
    "al-Qašayrī an-Nīsābūrī (mort en 261 H)",
    "Dār iḥyāʾ at-turāṯ al-ʿarabī – Beyrou",
    "le nom de Beyrouth est coupé dans l'imprimé à sa dernière lettre et se porte tel quel, sans retouche",
    "18. al-Fikr as-sāmī fī tārīḫ al-fiqh al-islāmī :",
    "al-Ḥiǧāwī aṯ-Ṯaʿālabī al-Ǧaʿfarī al-Fāsī (mort en 1376 H)",
    "l'édition : la première, 1416 H – 1995",
    "la mémoire historique du volume, veille sans citation nommée dans le corps",
    "19. Fayḍ al-qadīr, šarḫ al-Ǧāmiʿ aṣ-ṣaġīr :",
    "al-Ḥaddādī puis al-Manāwī al-Qāhirī (mort en 1031 H)",
    "l'édition : la première, 1356 H",
    "l'œuvre et la figure se répondent d'un index à l'autre",
    "20. al-Qāmūs al-fiqhī, en langue et en terme :",
    "le docteur Saʿdī Abū Ğayb",
    "Dār al-fikr, Damas – Syrie",
    "l'édition : la deuxième, 1408 H – 1988, reproduction : 1993",
    "21. al-Qāmūs al-muḥīṭ :",
    "al-Fīrūzābādī (mort en 817 H)",
    "sous la direction de Muḥammad Naʿīm al-ʿArqasūsī",
    "l'édition : la huitième, 1426 H – 2005",
    "L'Océan du lexique — huitième édition portée telle quelle",
    "22. al-Kāfī fī fiqh ahl al-Madīna :",
    "an-Namarī al-Qurṭubī (mort en 463 H)",
    "Muḥammad Muḥammad Aḥīd Wald Mādayk al-Mūrītānī",
    "l'édition : la deuxième, 1400 H/1980",
    "23. al-Muḫtaṣar al-fiqhī d'Ibn ʿArafah :",
    "Ḥāfiẓ ʿAbd ar-Raḥmān Muḥammad Ḫayr ; l'éditeur : Muʾassasat Ḫalaf Aḥmad pour les œuvres de bien ; l'édition : la première, 1435 H – 2014",
    "sept leçons convoquent sa voix (15355, 19354, 19407, 19449, 19496, 19670, 19744",
    "le Muḫtaṣar al-fiqhī 7/36 sur la šarika des visages",
    "l'index imprimé ne dédouble point",
    "24. La Mudawwana de l'Imām Mālik b. Anas b. Mālik b. ʿAmir al-Aṣbaḥī al-Madanī (mort en 179 H) ; l'éditeur :",
    "l'édition : la première, 1415 H – 1994",
    "la Mudawwana 4/80 à 19373",
    "le loyer corrompu qui oblige au loyer du semblable, à la dernière leçon 19744",
    "25. al-Miṣbāḥ al-munīr fī ġarīb aš-Šarḥ al-kabīr :",
    "al-Fayyūmī puis al-Ḥamawī, Abū l-ʿAbbās (mort vers 770 H)",
    "al-Maktaba al-ʿilmiyya – Beyrouth].",
    "le crochet égaré de l'imprimé se porte tel quel",
    "26. Muʿǧam al-luġa al-ʿarabiyya al-muʿāṣira :",
    "Aḥmad Muḫtār ʿAbd al-Ḥamīd ʿUmar (mort en 1424 H)",
    "ʿĀlam al-kutub ; l'édition : la première, 1429 H – 2008",
    "27. al-Muqaddimāt al-mumahhadāt :",
    "LA source la plus convoquée du volume — dix leçons au moins la nomment (15355, 19354, 19395, 19407, 19496, 19517, 19544…)",
    "3/37, le jugement de la ʿinān ; 3/37-38, la šarika des corps ; 3/39, les ḏimam et les visages",
    "le ğadd des Ibn Rušd",
    "28. al-Muntaqā, šarḫ al-Muwattaʾ :",
    "al-Bāǧī al-Andalusī (mort en 474 H)",
    "maṭbaʿat as-saʿāda ; l'édition : la première, 1332 H",
    "convoqué avec le Muwattaʾ lui-même à la leçon de la ḥawāla (19495)",
    "29. Manḫ al-Ğalīl šarḫ Mukhtaṣar Khalīl :",
    "ʿAlīš al-Mālikī (mort en 1299 H)",
    "Dār al-fikr, sans édition ; date de publication : 1409 H/1989",
    "huit leçons au moins convoquent le Manḫ (19395, 19407, 19441, 19452, 19495, 19496, 19756)",
    "le matn du cours déroulé fil à fil par son commentaire",
    "30. Mawāhib al-Ğalīl fī šarḫ Mukhtaṣar Khalīl :",
    "dit al-Ḥaṭṭāb ar-Ruʿīnī al-Mālikī",
    "l'édition : la première, 1412 H – 1992, 5/32 ]. édition : la première, 1408 H – 1988",
    "le jumeau manḫ/mawāhib des deux grands commentaires de Khalīl",
    "la référence égarée de l'imprimé (« 5/32 ] ») et la double édition se portent telles quelles",
    "31. La Mudawwana de son compilateur :",
    "Saḥnūn b. ʿAbd as-Salām at-Tūnisī (mort en 240 H)",
    "l'index imprimé ne dédouble point ; Mālik dicta, Saḥnūn porta",
    "32. Ṣaḥīḥ Ibn Ḥibbān, selon le classement d'Ibn Balbān :",
    "at-Tamīmī, Abū Ḥātim, ad-Dārimī, al-Bustī (mort en 354 H)",
    "l'édition : la deuxième, 1414 H",
    "33. al-Muḫtaṣar al-fiqhī :",
    "Ibn ʿArafah al-Wargamī at-Tūnisī al-Mālikī, Abū ʿAbd Allāh (mort en 803 H)",
    "Muʾassasat Ḫalaf Aḥmad al-Ḫabṭūr pour les œuvres de bien",
    "la source du fil ferme le livre",
    "Notes du traducteur",
    "vingt-sixième tranchage du fil",
    "un index n'est pas une leçon",
    "les trente-trois notices sont rendues dans leur intégralité",
    "la fin de l'imprimé, aux balises non refermées, est refermée proprement en français sans rien ajouter au contenu",
    "la Mudawwana aux notices 24 et 31 (par l'Imām Mālik, puis par son compilateur Saḥnūn)",
    "le Muḫtaṣar al-fiqhī d'Ibn ʿArafah aux notices 23 et 33",
    "la date fait la distinction entre le grand-père et le petit-fils",
    "l'exploitation des trois dernières leçons du volume suit le ğadd page à page",
    "il se tient dans la notice 2 par la Hāšiyat aṣ-Ṣāwī qui le commente",
    "le matn du cours, Khalīl, veille sur tout le volume sans y porter notice — c'est par ses commentateurs qu'il est là",
    "la variante onomastique se répète d'un index à l'autre et ne se retouche point",
    "le nom de Beyrouth coupé dans l'imprimé à la notice 17, le crochet égaré de la notice 25",
    "la variante de l'éditeur de la notice 33 (« al-Ḫabṭūr ») contre la 23ᵉ",
    "la bénédiction et le salut, portés dans les titres des deux Ṣaḥīḥ, sont rendus par leur sens — convention du corpus",
    "les années grégoriennes se portent après le tiret, comme imprimées (2004, 1988, 2001…)",
    "« mort vers 770 H » porte le « vers » de l'imprimé",
    "al-Muqaddimāt al-Mumahhadāt, dix leçons ; la Hāšiya d'ad-Dasūqī, vingt-huit ; Manḫ al-Ğalīl, huit ; Ibn ʿArafah, sept",
    "le hadith du troisième des deux associés sort des Sunan d'Abū Dāwūd (19537)",
    "cet index est le DERNIER document du volume",
    "l'introduction et les trente-deux leçons, plus les deux index, trente-trois documents couverts en main : LE LIVRE EST COMPLET",
    "le badge « Leçon 33 / 33 » porte le dernier jalon",
    "le prochain tour ouvrira un nouveau livre selon le registre et le worklog",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19757.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
