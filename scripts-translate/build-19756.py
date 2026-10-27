#!/usr/bin/env python3
# build-19756.py — 19756 « Jurisprudence : l'index des figures » (fiqh-tanawi-3,
# lessons[30], badge Leçon 32/33) — INDEX des figures (fihrist al-aʿlām), PAS une
# leçon (règle ah) : ni questions, ni objectifs, ni matn, ni synthèse, ni contrôle,
# ni exploitation, ni préparation préalable. Onze notices bio-bibliographiques
# rendues intégralement dans l'ordre du volume : Ibn ʿĀšir (1040 H, Muršid
# al-Muʿīn + šarḫ de Khalīl ; cité à 19452 via ʿAlīš), Ibn Ġāzī (919 H, fihris de
# ses šuyūḫ, témoignage de l'élève al-Wanšarīsī ; JAMAIS convoqué dans le corps),
# al-Badr ad-Damāmīnī (827 H, compagnon d'Ibn Ḫaldūn ; naẓm rapporté par al-Bannānī
# à 19448), at-Tūnisī (734 H, qāḍī al-quḍāt de Tunis ; recours des ḥamalāt à
# 19517), aṣ-Ṣāwī (1241 H à Médine ; ḥifẓ du ḍamān à 19496), aṭ-Ṭayyibī (743 H,
# hāšiya du Kaššāf ; širkat Allāh = istiʿāra à 19537), ʿAlīš (1299 H, Manḥ
# al-Ğalīl — LA voix la plus citée du cours, 8 leçons), al-Manāwī (1031 H, Fayḍ
# al-qadīr ; le troisième des deux associés à 19537), ad-Damīrī (805 H, TROIS
# šarḫs de Khalīl, riʾāsat al-Mālikiyya ; JAMAIS convoqué — onomastique « Bahrām
# b. ʿAbd Allāh » portée telle quelle, règle ax), al-Qarāfī (684 H, Anwār
# al-barūq, al-Iḥkām, aḏ-Ḏaḫīra — 5 leçons dont la dernière via Ibn al-Qaṣṣār),
# Ibn ʿAbd as-Salām (749 H, peste ; Ǧāmiʿ al-ummahāt ; 19503 + 19744). Fente
# liminaire VIDE portée telle quelle (ax) ; zéro āya/zéro hadith cités dans le
# document — neuvième tour sans protocole triple ; N.d.T. : titre (h1 fait foi,
# 25e tranchage : al-aʿlām vs al-iʿlām), nature d'index, onomastique, dates
# hégiriennes, économie de l'index (Khalīl, al-Bannānī, ad-Dardīr, ad-Dasūqī
# absents), galerie des commentateurs du matn, ancrage, achèvement (19757
# dernier document — livre complet 33/33).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19756_{i}.html').read())
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
    "Jurisprudence : l'index des figures",
    "1. Ibn ʿĀšir :",
    "ʿAbd al-Wāḥid b. Aḥmad b. ʿAlī b. ʿĀšir b. Saʿd al-Anṣārī, al-Andalusī, al-Fāsī, al-Mālikī, Abū Muḥammad",
    "al-Muršid al-Muʿīn",
    "le guide utile vers l'indispensable des sciences de la religion",
    "Fatḥ al-Mannān",
    "sur le rasm du Coran",
    "un commentaire du Mukhtaṣar de Khalīl dans les branches du fiqh mālikite (mort à Fès en 1040 H)",
    "« l'Imām Ibn ʿĀšir — que Dieu lui fasse miséricorde — a dit… »",
    "2. Ibn Ġāzī :",
    "il naquit à Maknāsat az-Zaytūn en 858 et passa à Fès",
    "Iršād al-labīb ilā maqāṣid ḥadīṯ al-ḥabīb",
    "la fihris de ses šuyūḫ",
    "ar-Rawḍ al-hātūn",
    "Son élève al-Wanšarīsī dit dans sa fihris",
    "il surpassa en cela la masse des gens de son temps",
    "(mort en 919 H)",
    "le portrait se fait par la fihris",
    "3. al-Badr ad-Damāmīnī :",
    "connu comme Ibn ad-Damāmīnī",
    "Il naquit à Alexandrie, s'établit au Caire et tint la compagnie d'Ibn Ḫaldūn",
    "il enseigna l'arabe à al-Azhar",
    "Tuḥfat al-ġarīb",
    "le commentaire du <em>Muġnī al-labīb</em>, <em>al-Fatḥ ar-rabbānī</em> dans le ḥadīth",
    "Šams al-maġrib fī l-marqṣ wa-l-maṭrab",
    "son commentaire du Ṣaḥīḥ d'al-Buḫārī (mort en 827 H)",
    "un naẓm abrégé de Badr ad-Dīn ad-Damāmīnī",
    "4. at-Tūnisī :",
    "qāḍī al-quḍāt — le juge des juges — de Tunis",
    "<em>Maʿīn al-ḥukkām</em> en deux volumes, <em>ar-Radd ʿalā Ibn Ḥazm fī iʿtirāḍi-hi ʿalā Mālik</em>",
    "<em>Mukhtaṣar at-tafarruʿ fī l-furūʿ</em> (mort en 734 H)",
    "la leçon des ḥamalāt multiples",
    "« À cela est allé Abū Isḥāq at-Tūnisī »",
    "ce qui fut porté pour autrui fut porté pour lui-même, nul retour n'y a lieu",
    "par la voie des Muqaddimāt d'Ibn Rušd",
    "5. aṣ-Ṣāwī :",
    "Aḥmad b. Muḥammad al-Ḫalwatī, dit aṣ-Ṣāwī",
    "une hāšiya sur le tafsīr des Ğalālayn",
    "des ḥawāšī sur certains livres du šayḫ Aḥmad ad-Dardīr dans le fiqh des Mālikites",
    "al-Farāʾiḍ as-saniyya",
    "le commentaire de la Hamziyya d'al-Būṣīrī (mort à Médine, la cité du Prophète, en 1241 H)",
    "« quant à la langue : c'est le ḥifẓ »",
    "la portée et la caution",
    "6. aṭ-Ṭayyibī :",
    "au kasra du ṭāʾ et du bāʾ, tous deux unifiés",
    "<em>al-Ḫulāṣa</em> dans les fondements du ḥadīth",
    "Fatūḥ al-ġayb fī l-kašf ʿan qināʿ ar-rayb",
    "la hāšiya du Kaššāf",
    "le commentaire des Maṣābīḥ as-sunna d'al-Baġawī",
    "le commentaire de l'Alfiyya d'Ibn Mālik (mort en 743 H)",
    "la širkat Allāh pour les deux est comme une istiʿāra",
    "Son essence nommée un tiers pour eux deux",
    "le nadab de la compagnie",
    "7. ʿAlīš :",
    "Maghrébin d'origine, des gens de Tripoli d'Occident",
    "il y étudia à al-Azhar et y tint la šayḫat des Mālikites",
    "Fatḥ al-ʿAliyy al-Mālik fī l-fatwā ʿalā madhhab al-Imām Mālik",
    "Manḥ al-Ğalīl ʿalā Mukhtaṣar Khalīl",
    "le commentaire de la grande ʿAqīda d'aš-Sanūsī (mort en 1299 H)",
    "huit leçons au moins l'appellent",
    "Manḥ al-Ğalīl 6/75",
    "Manḥ al-Ğalīl 5/71",
    "Manḥ al-Ğalīl 6/83",
    "Manḥ al-Ğalīl 6/196",
    "« et dans son passage au plus bas, il y a hésitation »",
    "le commentaire filaire du matn, fil à fil, de la faillite à la garantie",
    "8. al-Manāwī :",
    "Tāǧ al-ʿĀrifīn b. ʿAlī b. Zayn al-ʿĀbidīn al-Manāwī al-Ḥaddādī al-Miṣrī",
    "le faqīh šāfiʿite",
    "Ġāyat al-amānī fī šarḫ šarḫ al-ʿaqāʾid",
    "al-Fatḥ as-samāwī",
    "<em>Fayḍ al-qadīr fī šarḫ al-Ǧāmiʿ aṣ-Ṣaġīr</em> d'as-Suyūṭī (mort en 1031 H)",
    "sur le même hadith qu'aṭ-Ṭayyibī",
    "« le troisième des deux associés »",
    "l'obtention de la baraka et de l'accroissement",
    "9. ad-Damīrī :",
    "Bahrām b. ʿAbd Allāh b. ʿAbd al-ʿAzīz, Abū l-Baqāʾ Tāǧ ad-Dīn as-Silmī ad-Damīrī al-Qāhirī",
    "à qui aboutit la riʾāsat al-Mālikiyya en son temps",
    "sa nisba à Mīra, village près de Dumyāṭ",
    "donna les fatwās, enseigna, suppléa au jugement en Égypte",
    "s'y tint seul de 791 à 792 H",
    "aš-Šāmil fī fiqh al-Imām Mālik",
    "trois commentaires du Mukhtaṣar de Khalīl dans le fiqh",
    "le commentaire du Mukhtaṣar d'Ibn al-Ḥāǧib dans les fondements (mort en 805 H)",
    "l'index galerie des commentateurs du matn du cours",
    "l'onomastique de l'imprimé se garde telle quelle",
    "10. al-Qarāfī :",
    "Aḥmad b. Idrīs b. ʿAbd ar-Raḥmān, Abū l-ʿAbbās, Šihāb ad-Dīn aṣ-Ṣanhāǧī",
    "al-Qarāfa, le quartier voisin du tombeau de l'Imām aš-Šāfiʿī au Caire",
    "égyptien de naissance, de formation et de mort",
    "Anwār al-barūq fī anwāʾ al-furūq",
    "al-Iḥkām fī tamyīz al-fatāwā ʿan al-aḥkām wa-taṣarrufāt al-qāḍī wa-l-imām",
    "le commentaire du <em>Tanqīḥ al-fuṣūl</em> dans les fondements, et <em>aḏ-Ḏaḫīra fī fiqh al-Mālikiyya</em> (mort en 684 H)",
    "Cinq leçons au moins convoquent sa voix",
    "« la vie a la préséance », dit Mālik par lui",
    "aḏ-Ḏaḫīra 7/85",
    "où il donne la parole à Ibn al-Qaṣṣār sur la šarika des visages",
    "interdite, dit aš-Šāfiʿī, permise par Abū Ḥanīfa",
    "11. Ibn ʿAbd as-Salām :",
    "al-Hawārī al-Munastīrī, Abū ʿAbd Allāh",
    "il fut qāḍī al-ǧamāʿa de Tunis",
    "al-Munastīr, entre al-Mahdiyya et Sūsa, en Ifrīqiya",
    "le commentaire du <em>Ǧāmiʿ al-ummahāt</em> d'Ibn al-Ḥāǧib dans le fiqh des Mālikites",
    "un dīwān de fatwās",
    "il mourut de la peste qui dévaste (mort en 749 H)",
    "la compagnie en une chose et le taḍāmun",
    "« il est permis sur le plus correct selon Ibn ʿAbd as-Salām »",
    "la construction conjointe du bas de l'édifice au haut",
    "le recours s'attache à la récolte, qui a eu lieu par sa cause",
    "Notes du traducteur",
    "vingt-cinquième tranchage du fil",
    "les figures et non les notifications",
    "un index n'est pas une leçon",
    "les onze notices bio-bibliographiques sont rendues dans leur intégralité",
    "elle demeure VIDE dans l'imprimé",
    "neuvième tour sans verset vérifié",
    "« Bahrām b. ʿAbd Allāh », portée comme imprimée",
    "les nisbas — al-Andalusī, al-Fāsī, aṣ-Ṣanhāǧī, al-Hawārī",
    "toutes hégiriennes, rendues par la seule lettre H, telles quelles",
    "791 et 792 H",
    "Khalīl, l'auteur du matn, n'y figure point",
    "al-Bannānī, ad-Dardīr, ad-Dasūqī, Ibn al-Ḥāǧib, Ibn Rušd non plus",
    "Ibn Ġāzī et ad-Damīrī, ne sont point convoquées dans le corps du présent volume",
    "du versificateur andalou au šayḫ de la fatwā du Caire",
    "aṭ-Ṭayyibī et al-Manāwī sur le troisième des deux associés",
    "Manḥ al-Ğalīl 5/71, 6/75, 6/83, 6/196 ; aḏ-Ḏaḫīra 7/85",
    "reste 19757, l'index des sources et références",
    "fihrist al-maṣādir wa-l-marāğiʿ",
    "trente-trois documents couverts en main",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19756.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
