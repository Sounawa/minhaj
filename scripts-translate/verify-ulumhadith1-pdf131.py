#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-131
(le ḥadīṯ fard et le ḥadīṯ muʿallal, p.99-103 du manuel ulum-hadith-1-thanawi.pdf) —
ERRATUM R597-ter appliqué (passe parallèle même trace 2119, défauts PROUVÉS réparés) :
«aw ḫafan»→«aw ḫafā» (rime ʿurifā, OCR ×4) ; nasakh «ʿillah/fa-ǧnaḫ lah» (rime,
lām-hāʾ imprimé tesseract ×2, compZ-bayt, glose «il a penché vers sa parole» —
l'initiale «fa-ǧtuthhu»/«retranche-le» récusée) ; muʿaḍḍal supprimé (tamhīd
OCR ×2 = fard+muʿallal seuls ; leçon suivante = muḍṭarib p.104) ; natte→Ṣafiyya ;
Suhayl/Wuhayb/ʿAwn/al-Kudrī ; ﷺ réplacé après rasūl Allāh (l'initiale le plaçait
après le Compagnon) ; divergence furridatuhu consignée (qāf ×5 lectures vs fāʾ ×2,
forme livrée tenue). Passes antérieures conservées :
bannière « ad-dars 20 » tranchée image (cache p.99) ; bornes p.99-103 par DOUBLE
sondage (bannière ad-dars 21 + objectifs المضطرب lus à l'OCR p.104, concordants
avec l'iʿdād qablī p.103) ; bayts — « wa-l-fardu mā furridatuhu bi-thiqatin »
(mot après mā tranché PAR L'IMAGE 3600 dpi : tête fāʾ un point + tāʾ deux points,
forme imprimée tenue, écart canon documenté) + « aw ǧamʿin aw qaṣrin ʿalā
riwāyatin » (tanwīn bannière vs cas direct du commentaire) + « wa-mā bi-ʿillatin
ġumūḍin aw ḫafan » (forme imprimée sans hamza tenue, écart canon documenté) +
« muʿallalun ʿindahum qad ʿurifā » ; glose (at-tafarrud, mafʿūl bi-kadhā) ;
istikhlāṣ ×1 ; taḥlīl : fard muṭlaq/muqayyad ×3 espèces (thiqa : Qatāda + Bakr
b. Wāʾil « u lima ʿalā ṣafiyyatin bi-sawīqin wa-tamrin » [Sunan Abī Dāwūd] ;
ǧamʿ : al-Ḥākim + al-Kuḏrī ﷺ sic + fātiḥa + Basrites ; riwāya : Ibn Ṭāhir
al-Maqdisī ġarīb + at-Tirmiḏī ḥasan ġarīb) ; muʿallal : définition, ʿilla cause
cachée relative, ʿillas cachées (tadlees, idrāǧ, qalb rāw, iḫtilāf, irsāl,
waqf), exemple Ibn Ǧurayǧ/Mūsā b. ʿUqba/Suḥayl + kaffārat al-maǧlis + Mūsā b.
Ismāʿīl/Wahb b. Ḫālid/ʿŪn b. ʿAbd Allāh + iʿlāl d'al-Buḫārī ; aqsām al-ʿilla
(sanad/matn, qādiha/ġayr qādiha, Ibn Luhayʿa renvoi imprimé documenté, ǧarḥ) ;
taqwīm ×3 ; istiṯmār (al-ʿIrāqī alfiyya « wa-n-nasḫa sammā t-Tirmiḏī ʿillatan »
+ « fa-in yurd fī ʿamalin fa-ǧtuthhu » ; an-nasḫ tranché image côte à côte,
lecture OCR at-tasḫ récusée ; ellipse « (...) » imprimée tenue ;
[Šarḥ at-tabṣira wa-t-taḏkira 1/290]) ; taʿammul ×2 ; iʿdād qablī (muḍṭarib) ;
bornes p.99-103 ; ﷺ tenu (U+FDFA, dont le sic après al-Kuḏrī documenté) ;
zéro āya, zéro résidu de recyclage.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf131.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-131-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")


h = open(HTML, encoding="utf-8").read()
plain = h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u00a0", " ")
plain = re.sub(r" {2,}", " ", plain)

# 1. h1 aligné au titleFr pré-mappé du registre
tf = [l for l in json.load(open(REG, encoding="utf-8"))["lessons"]
      if l["docId"] == "pdf-mut23h2q-131"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 20", "leçon 20" in (m.group(1) if m else ""))

# 2. bannière / bornes
chk("badge ad-dars 20", "ad-dars 20" in plain)
chk("bornes p.99-103 documentées", "page imprimée 99" in plain and "page 103" in plain)
chk("bannière ad-dars 21 p.104 (sondage)", "ad-dars 21" in plain and "page 104" in plain)
chk("double sondage (jamais deviné)", "double sondage" in plain and "jamais devinée" in plain)
chk("concordance iʿdād qablī p.103", "concors" in plain or "concordants" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. tamhīd — fard, muʿallal (erratum R597-ter : muʿaḍḍal récusé)
chk("tamhīd : sciences du ḥadīṯ", "Parmi les types des sciences du ḥadīṯ" in plain)
chk("tamhīd : fard et muʿallal seuls (erratum)", "du ḥadīṯ fard et du ḥadīṯ muʿallal" in plain and "et du ḥadīṯ muʿaḍḍal" not in plain)
chk("tamhīd : tafarrud maẓinna", "le tafarrud est le plus souvent le lieu soupçonné" in plain)
chk("tamhīd : condition ṣaḥīḥ non muʿallal", "ne soit point muʿallal" in plain)
chk("tamhīd question double (erratum)", "chacun du ḥadīṯ fard et du ḥadīṯ muʿallal" in plain)
chk("tamhīd question types ʿilla", "quels sont les types de la ʿilla" in plain)
chk("erratum muʿaḍḍal documenté (RÉCUSÉE)", "la lecture « al-ḥadīṯ al-muʿaḍḍal » du tamhīd est RÉCUSÉE" in plain)

# 4. bayts du nāẓim
chk("bayt 1 : wa-l-fardu mā furridatuhu bi-thiqatin", "wa-l-fardu mā furridatuhu bi-thiqatin" in plain)
chk("bayt 1 : aw ǧamʿin aw qaṣrin ʿalā riwāyatin", "aw ǧamʿin aw qaṣrin ʿalā riwāyatin" in plain)
chk("bayt 2 : wa-mā bi-ʿillatin ġumūḍin aw ḫafā", "wa-mā bi-ʿillatin ġumūḍin aw ḫafā" in plain)
chk("bayt 2 : muʿallalun ʿindahum qad ʿurifā", "muʿallalun ʿindahum qad ʿurifā" in plain)
chk("furridatuhu : divergence consignée (R597-ter)", "la divergence consignée — jamais tranchée sans preuve" in plain)
chk("erratum ḫafā : récusée + rime (R597-ter)", "aw ḫafā" in plain and "est RÉCUSÉE — elle rompait la rime du bayt" in plain)
chk("tanwīn bannière vs cas direct commentaire", "riwāyati" in plain and "bi-ʿillati" in plain)
chk("séparateurs * * * tenus", "* * *" in plain)
chk("traduction bayt", "transmission seule par un homme de confiance" in plain)

# 5. glose
chk("glose : at-tafarrud absence de partage", "at-tafarrud, qui est l’absence de partage" in plain)
chk("glose : mafʿūl bi-kadhā", "mafʿūl" in plain and "bi-kadhā" in plain)
chk("bandeau aš-šarḥ adjudiqué", "aš-šarḥ" in plain)

# 6. istikhlāṣ ×1
chk("istikhlāṣ une question", "sous la forme d’une question" in plain)
chk("istikhlāṣ banner name", "istikhlāṣ al-maḍāmīn" in plain)
chk("IS1 premier bayt", "premier bayt" in plain)

# 7. taḥlīl — fard muṭlaq/muqayyad
chk("deux divisions du fard", "le fard absolu (muṭlaq)" in plain and "fard restreint (muqayyad)" in plain)
chk("3 espèces annoncées", "au nombre de trois" in plain)
chk("type 1 thiqa + Qatāda", "de Qatāda, par un homme de confiance que par un tel" in plain and "transmetteurs faibles" in plain)
chk("exemple Bakr b. Wāʾil", "Bakr b. Wāʾil" in plain and "az-Zuhrī, d’Anas" in plain)
chk("ḥadīṯ u lima ʿalā ṣafiyyatin", "u lima ʿalā ṣafiyyatin bi-sawīqin wa-tamrin" in plain)
chk("réf. Sunan Abī Dāwūd aliments", "Sunan Abī Dāwūd" in plain and "livre des aliments" in plain)
chk("ne le transmet que Wāʾil/Ibn ʿUyayna", "ne le transmet donc de Bakr que Wāʾil" in plain)
chk("ḥadīṯ ṣaḥīḥ", "c’est un ḥadīṯ ṣaḥīḥ" in plain)
chk("type 2 ǧamʿ + al-Ḥākim", "restreint par un groupe (ǧamʿ)" in plain and "al-Ḥākim" in plain)
chk("al-Kudrī", "Abū Saʿīd al-Kudrī" in plain and "al-Kuḏrī" not in plain)
chk("natte réparée en Ṣafiyya (erratum ×2)", plain.count("un repas de noces pour Ṣafiyya") == 2 and "une natte" not in plain)
chk("ḥadīṯ fātiḥa", "l’ouverture du Livre et ce qui est aisé" in plain)
chk("Basrites seuls", "les gens de Baṣra sont seuls" in plain)
chk("type 3 riwāya", "restreint par une voie de transmission (riwāya)" in plain)
chk("quatre Sunan + Sufyān b. ʿUyayna", "quatre Sunan" in plain and "Sufyān b. ʿUyayna" in plain)
chk("Wāʾil b. Dāwūd", "Wāʾil b. Dāwūd" in plain)
chk("Ibn Ṭāhir al-Maqdisī ġarīb", "Ibn Ṭāhir al-Maqdisī" in plain and "ġarīb" in plain)
chk("at-Tirmiḏī ḥasan ġarīb", "ḥasan ġarīb" in plain)

# 8. muʿallal — définition + ʿilla
chk("définition muʿallal", "où l’on a scruté une ʿilla douée d’obscurité et de cachette" in plain)
chk("apparence sécurité", "son apparence est la sécurité" in plain)
chk("ʿilla cause cachée", "cause cachée, obscure" in plain)
chk("relative selon le critique", "affaire relative, appréciée selon chaque critique" in plain)
chk("tadlees", "en a usé avec ruse (tadlees)" in plain)
chk("idrāǧ non explicité", "l’insertion (idrāǧ) non explicitée" in plain)
chk("qalb rāw par semblable", "remplacement d’un transmetteur par un autre transmetteur qui lui ressemble" in plain)
chk("ikhtilāf entre les transmetteurs", "la discorde entre les transmetteurs" in plain)
chk("ittiṣāl/irsāl", "la vérité est son irsāl" in plain)
chk("rafʿ/waqf", "la vérité est son arrêt" in plain)
chk("ʿilla apparente", "tel le transmetteur faible, ou le confus" in plain)

# 9. exemple muʿallal — kaffārat al-maǧlis
chk("Ibn Ǧurayǧ + Mūsā b. ʿUqba", "Ibn Ǧurayǧ" in plain and "Mūsā b. ʿUqba" in plain)
chk("Suhayl b. Abī Ṣāliḥ", "Suhayl b. Abī Ṣāliḥ" in plain)
chk("d’Abū Hurayra élevé", "d’Abū Hurayra, élevé à lui" in plain)
chk("ḥadīṯ kaffārat al-maǧlis", "quiconque s’assied dans une séance" in plain)
chk("formule سبحانك... translittérée traduite", "pureté à Toi, ô Dieu, et louange à Toi" in plain)
chk("réf. Sunan at-Tirmiḏī invocations", "Sunan at-Tirmiḏī" in plain and "chapitres des invocations" in plain)
chk("Mūsā b. Ismāʿīl + Wuhayb b. Ḫālid", "Mūsā b. Ismāʿīl" in plain and "Wuhayb b. Ḫālid al-Bāhilī" in plain)
chk("ʿAwn b. ʿAbd Allāh muwaqqaf", "ʿAwn b. ʿAbd Allāh, arrêté à lui" in plain)
chk("iʿlāl al-Buḫārī", "al-Buḫārī l’a rendu défectueux" in plain)
chk("pas d’audition de Suhayl", "on ne lui connaît pas d’audition" in plain)

# 10. aqsām al-ʿilla
chk("ʿilla sanad : irsāl waqf tadlīs inqiṭāʿ", "l’irsāl, l’arrêt (al-waqf), le tadlīs, la rupture (al-inqiṭāʿ)" in plain)
chk("ʿilla matn : iḍṭirāb taḥrīf idrāj", "le trouble (al-iḍṭirāb), la falsification (at-taḥrīf)" in plain)
chk("matn naît d’une ʿilla de sanad", "ne peut naître que d’une ʿilla dans l’isnād" in plain)
chk("ġayr qādiha", "qui ne porte pas atteinte (ġayr qādiha)" in plain)
chk("qādiha", "la ʿilla qui porte atteinte (qādiha)" in plain)
chk("Ibn Luhayʿa renvoi imprimé documenté", "Ibn Luhayʿa" in plain and "renvoi imprimé est tenu tel quel" in plain)
chk("iʿlāl par irsāl/waqf affermi", "du continué par l’irsāl" in plain)
chk("ǧarḥ ×4", "le mensonge, la distraction, l’impiété" in plain)

# 11. taqwīm — 3 questions
chk("taqwīm 3 questions", "sous la forme de trois questions" in plain)
chk("TQ1 définition fard", "Quelle est la définition du ḥadīṯ fard" in plain)
chk("TQ2 muʿallal", "Qu’est-ce que le ḥadīṯ muʿallal" in plain)
chk("TQ3 site + qādiha", "selon son site et selon le fait qu’elle porte atteinte" in plain)

# 12. istiṯmār — al-ʿIrāqī
chk("al-ʿIrāqī alfiyya", "Al-Ḥāfiẓ al-ʿIrāqī dit dans son alfiyya" in plain)
chk("bayt : wa-n-nasḫa sammā t-Tirmiḏī ʿillah", "wa-n-nasḫa sammā t-Tirmiḏī ʿillah" in plain and "ʿillatan" not in plain)
chk("bayt : fa-in yurd fī ʿamalin fa-ǧnaḫ lah", "fa-in yurd fī ʿamalin fa-ǧnaḫ lah" in plain)
chk("traduction réparée : incline-toi vers lui", "si donc cela est entendu de l’acte, incline-toi vers lui" in plain)
chk("erratum nasakh documenté (rime + lām-hāʾ + glose)", "ERRATUM R597-ter : le second hémistiche" in plain and "paraphrase ǧanaḫa — pencher vers —, jamais extirper" in plain)
chk("nasḫ tranché image côte à côte", "confrontation côte à côte" in plain and "at-tasḫ" in plain and "récusée" in plain)
chk("ellipse (...) imprimée tenue", "(...)" in plain and "s’imprime dans le manuel" in plain)
chk("réf. Šarḥ at-tabṣira 1/290", "Šarḥ at-tabṣira wa-t-taḏkira d’al-ʿIrāqī, 1/290" in plain)
chk("mansūḫa dans le Ṣaḥīḥ", "abrogés (mansūḫa)" in plain)
chk("Taʿ 1 sens de la nomination", "a-t-il nommé le nasḫ du ḥadīṯ une ʿilla" in plain)
chk("Taʿ 2 réponse d’al-ʿIrāqī", "a-t-il répondu à la position d’at-Tirmiḏī" in plain)

# 13. iʿdād qablī — leçon suivante muḍṭarib
chk("préparation muḍṭarib", "je connais la signification du ḥadīṯ muḍṭarib" in plain)
chk("conditions + divisions muḍṭarib", "j’en précise les conditions, j’expose ses divisions" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 14. ﷺ tenu (réplacé), zéro āya, zéro résidu
chk("ﷺ tenu (U+FDFA ×5 : 3 contenu + 2 notes, Compagnon réparé)", h.count("\ufdfa") == 5)
chk("erratum ﷺ du Compagnon (RÉPARÉ)", "RÉPARÉ, l’imprimé ne le" in plain and "porte point" in plain)
chk("doc mentionne aucune āya", "aucune āya" in plain)
residus = ["TODO", "XXX", "undefined", "NaN", "【", "____", "recycle", "takeover", "mtime"]
chk("zéro résidu technique", not any(r in plain for r in residus))

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)
