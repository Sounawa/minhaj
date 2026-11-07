# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-397
(aḥkām ṣayd al-muḥrim wa-l-ǧazāʾ fīhi — الدرس 8, p.58-64 du manuel
hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé 29 slots
pdf-mut23h2x-390..418) : bornes p.58-64 (bannière p.65 = leçon 9, couches
+ bandes) ; 13 numéros de référence tranchés (1024, 1025, 1027, 1028, 1026,
1030, 1031, 1032, 1033, 1036, 1038, 1040, réf. al-Bāǧī 3/437) — dont six par
image directe 380-900 dpi (1024, marque verset « 97 », 1025 zoom, 1028 zoom,
1030, 1032 découverte) ; récusations par image : « šaqq al-muḥrim dummālah »
contre OCR « kalaf » (zoom 900 dpi), liste du 1028 rétablie à cinq, « ǧanāḥun »
contre « ǧazāʾun », « naha Allāhu ʿanhu » contre « ʿan qatlihi » (zoom 900
dpi), « al-faʾratu » rétabli ; UN verset imprimé (āya 95 ḥafṣ de la sourate 5,
marque imprimée « al-āya 97 », écart warš/ḥafṣ documenté) rendu une SEULE FOIS
du cache coranique (double rendu interdit — seconde occurrence par référence) ;
0 arabe, 0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf397.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-397-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
SAV = "/home/z/my-project/scripts-translate/savant-registry.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "").replace("\u2009", ""))

# --- 1) squelette ---
chk("h1 Leçon 8", "<h1>Leçon 8" in hn and "ǧazāʾ" in hn)
chk("h1 titleFr registre", "La chasse commise en état d’iḥrām et sa réparation (ǧazāʾ)" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.58-64", "p.58-64" in hn)
chk("meta trace tick job", "1a19c7c0ffb4f845-cron-agent-loop-202611071107" in hn and "11h07" in hn and "496554" in hn)
chk("meta takeover WIP-R641", "takeover" in hn and "WIP-R641" in hn)
chk("meta voisins 396/398/uh2-268", "pdf-mut23h2x-396" in hn and "pdf-mut23h2x-398" in hn and "uh2-pdf-mut23h2u-268" in hn)
chk("meta titre bannière", "aḥkām ṣayd al-muḥrim wa-l-ǧazāʾ" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’apparat de preuve de la livraison",
    "L’évaluation (at-taqwīm)",
    "L’exploitation pédagogique (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī)",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les trois objectifs ---
chk("obj 1 chasse + réparation", "le jugement de la chasse dans le ḥarām et sa réparation" in hn)
chk("obj 2 finalité de la permission", "la finalité de la permission donnée par le Législateur au consacré de tuer" in hn)
chk("obj 3 Sunna du Prophète", "me conformer à la Sunna du Prophète" in hn)

# --- 3) tamhīd ---
chk("tamhīd effort adoration", "de déployer un effort (yaǧtahid) dans l’adoration" in hn)
chk("tamhīd tawḥīd al-qaṣd", "l’unification du dessein (tawḥīd al-qaṣd)" in hn)
chk("tamhīd refus chasse", "il s’abstient donc de poursuivre le gibier" in hn)
chk("question d’ouverture triple", "quelle est donc la réparation du gibier dans le ḥarām" in hn and "la raison" in hn)

# --- 4) les numéros tranchés ---
for num in ("1024", "1025", "1026", "1027", "1028", "1030", "1031", "1032", "1033", "1036", "1038", "1040", "3/437", "234", "97"):
    chk(f"numéro {num} présent", num in hn)

# --- 5) texte 1024 ---
chk("1024 chasse ḥarām interdite", "tout gibier que le consacré chasse dans le ḥarām" in hn)
chk("1024 chien envoyé", "il envoie son chien dans le ḥarām" in hn)
chk("1024 yuẓlimuhu", "le harcèle (yuẓlimuhu)" in hn)
chk("1024 proximité", "alors qu’il était proche du ḥarām" in hn)
chk("1024 s’il envoie proche", "s’il l’envoie proche du ḥarām, la réparation pèse sur lui" in hn)

# --- 6) verset cache coranique, rendu UNE fois ---
chk("verset cache coranique (source)", "rendu ici intégralement du cache coranique (sourate 5, āya 95 du comptage du cache)" in hn)
chk("verset FR cache", "Ô les croyants&nbsp; ! Ne tuez pas de gibier pendant que vous êtes en état d’Ihram" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "Ne tuez pas de gibier pendant que vous êtes en état d’Ihram" in hn)
chk("verset marque 97", "sūrat al-Māʾida&nbsp; : al-āya 97" in hn or "al-Māʾida : al-āya 97" in hn)
chk("verset écart documenté", "écart de numérotation warš/ḥafṣ" in hn)
chk("double rendu interdit", hn.count("Ne tuez pas de gibier pendant que") == 1)
chk("seconde occurrence par référence", "re-convoquée par référence" in hn or "convoque ici la āya par référence" in hn)
chk("āya énumère les trois réparations", "il énumère d’avance les trois modes de réparation" in hn)

# --- 7) texte 1025 ---
chk("1025 chasse licite puis tué", "chasse un gibier alors qu’il est licite (ḥalāl), puis le tue alors qu’il est consacré" in hn)
chk("1025 rang de l’acheteur", "au rang de celui qui l’achète alors qu’il est consacré puis le tue" in hn)
chk("1025 naha ʿanhu", "Dieu a certes interdit cela, et la réparation pèse sur lui" in hn)
chk("1025 aṣāba-hū ṣ-ṣayd", "celui à qui le gibier échoit (aṣāba-hū ṣ-ṣayd)" in hn)
chk("1025 zoom 900", "n° 1025 — queue calée par zoom 900" in hn)

# --- 8) texte 1028 ---
chk("1028 chaîne Nāfiʿ", "Mālik, d’après Nāfiʿ, d’après ʿAbd Allāh b. ʿUmar" in hn)
chk("1028 formule", "cinq bêtes (ḫamsun min ad-dawābb) ne constituent pas, pour le consacré, de péché à leur mise à mort" in hn)
chk("1028 ǧanāḥ", "laysa ʿalā al-muḥrim fī qatlihinna ǧanāḥun" in hn)
chk("1028 cinq bêtes", "le corbeau, l’épervier (al-ḥidāʾ), le scorpion, la souris, et le chien vorace (al-kalb al-ʿaqūr)" in hn)
chk("1028 zoom 900", "n° 1028 — liste calée par zoom 900" in hn)

# --- 9) notice transmetteur ---
chk("tarǧama Layṯī", "Yaḥyā b. Yaḥyā b. Kaṯīr al-Layṯī" in hn)
chk("tarǧama Šibṭūn", "al-Maʿrūf bi-Šibṭūn" in hn)
chk("tarǧama ʿāqil al-Andalus", "l’intelligent d’al-Andalus" in hn and "ʿāqil al-Andalus" in hn)
chk("tarǧama riyāsa", "la direction du fiqh (riyāsat al-fiqh) aboutit à lui en al-Andalus" in hn)
chk("tarǧama mort 234", "en l’an 234 de l’Hégire" in hn)

# --- 10) gloses ---
chk("glose ṣayd", "ce que le terme vise ici est ce dont la chair se mange" in hn)
chk("glose ḥuruma nuskayn", "vous vous êtes consacrés à l’un des deux rites (aḥad an-nuskayn" in hn)
chk("glose ḥidāʾ", "l’épervier, oiseau vil qui ravit la nourriture des gens" in hn)
chk("glose kalb ʿaqūr", "toute bête qui perce et terrorise les gens" in hn and "le lion, le léopard, le guépard et le loup" in hn)

# --- 11) istiḫlāṣ ---
chk("istiḫlāṣ item 1 réparation", "je distingue le jugement de la réparation du gibier dans le ḥarām" in hn)
chk("istiḫlāṣ item 2 six bêtes", "pourquoi la Loi a-t-elle permis au consacré de tuer les bêtes nuisibles, au nombre de six" in hn)

# --- 12) fiqh : premièrement ---
chk("fiqh 1 sorties du ḥarām purgent", "la sortie du territoire ne purge pas la chasse" in hn)
chk("fiqh 2 non-consacré", "si un non-consacré poursuit un gibier dans le permis et le prend dans le ḥarām" in hn)
chk("fiqh 2 ni fait ni pouvoir", "entrer dans l’interdit n’est ni de son fait ni en son pouvoir" in hn)
chk("fiqh 2 reprise citation Mālik", "s’il l’envoie proche du ḥarām, la réparation pèse sur lui&nbsp; »" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "s’il l’envoie proche du ḥarām, la réparation pèse sur lui" in hn)

# --- 13) fiqh : deuxièmement ---
chk("ǧumhūr délibéré et errant", "délibérément ou par erreur, doit la réparation" in hn)
chk("Ibn Shihāb āya/Sunna", "la réparation est exigée du délibéré par la āya, et de l’errant par la Sunna" in hn)
chk("Bāǧī 3/437", "al-Bāǧī, 3/437" in hn)
chk("1027 jugement pareil", "comme on juge le consacré qui tue le gibier dans le ḥarām alors qu’il est consacré" in hn)
chk("deux juristes", "deux juristes (faqīhān) d’entre les musulmans prononcent sur lui ce jugement" in hn)
chk("deux justes ʿadlān", "les deux justes (al-ʿadlān) lui font choisir" in hn)
chk("voie a équivalent", "livrer l’équivalent du gibier" in hn)
chk("forme et allure", "la ressemblance et la proximité s’entendant de la forme et de l’allure" in hn)
chk("voie b valeur nourriture", "livrer la valeur du gibier en nourriture" in hn)
chk("voie b lieu du meurtre", "la valeur s’appréciant au lieu où il l’a tué" in hn)
chk("voie c jeûne par modʿ", "jeûner un jour pour chaque modʿ" in hn)
chk("pauvres dix", "s’ils sont dix, il jeûne dix jours" in hn)
chk("1026 aḥsan mā samiʿtu", "le plus beau de ce que j’ai entendu sur celui qui tue le gibier" in hn)
chk("1026 estimer + nourrir", "faire estimer le gibier atteint" in hn and "chaque pauvre d’une modʿ" in hn)
chk("1026 vingt pauvres", "s’ils sont vingt pauvres, il jeûne vingt jours" in hn)
chk("1026 phrase tronquée documentée", "la phrase imprimée s’achève sur ces mots" in hn)
chk("vers didactique", "vers didactique" in hn and "mises en ordre" in hn)

# --- 14) fiqh : troisièmement ---
chk("six bêtes", "les six bêtes (ad-dawābb as-sitt)" in hn)
chk("1030 cinq nuisibles", "cinq bêtes nuisibles sont tuées dans le ḥarām&nbsp; : la souris, le scorpion, le corbeau, l’épervier, et le chien vorace" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "cinq bêtes nuisibles sont tuées dans le ḥarām : la souris, le scorpion, le corbeau, l’épervier, et le chien vorace" in hn)
chk("1031 serpents ʿUmar", "ʿUmar b. al-Ḫaṭṭāb ordonna la mise à mort des serpents dans le ḥarām" in hn)
chk("Ṣaḥīḥ Muslim Ibn ʿUmar", "Ṣaḥīḥ de Muslim d’après Ibn ʿUmar" in hn)
chk("ʿilla muʾḏiyya", "qu’elles sont chacune nuisible (muʾḏiyya)" in hn)
chk("qiyās", "par analogie (qiyās) avec ces mentions" in hn)
chk("1033 oiseaux corbeau+ḥidāʾ", "autre chose que le corbeau et l’épervier que le Prophète (que la prière et la paix soient sur lui) a nommés" in hn)
chk("Bāǧī pas d’initiative", "de sa propre initiative, de tuer des bêtes de proie parmi les oiseaux autres que celles mentionnées" in hn)
chk("Bāǧī initiateur du dommage", "est l’initiateur du dommage, aucune réparation ne pèse sur celui qui l’a tué" in hn)
chk("1032 ḍabuʿ ṯaʿlab hirr", "le chacal (ḍabuʿ), le renard, le chat, et ce qui leur ressemble" in hn)
chk("1032 découverte", "découverte de la livraison, l’OCR «&nbsp;&nbsp;102(…)&nbsp; » tranché «&nbsp;&nbsp;1032&nbsp; » par image" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "tranché « 1032 » par image" in hn)
chk("ḥurma bayt al-ḥarām", "l’inviolabilité (ḥurma) de la Maison du ḥarām" in hn and "en sécurité contre les hommes et contre les bêtes" in hn)
chk("ḥurma suite dégradée documentée", "la suite de la phrase imprimée est dégradée aux couches" in hn)

# --- 15) taqwīm + istiṯmār + iʿdād ---
chk("taqwīm serpent aigle scorpion", "le serpent, l’aigle (an-nasr), le scorpion" in hn)
chk("taqwīm aigle hors liste", "l’aigle n’y est pas" in hn and "emporte la compensation" in hn)
chk("taqwīm Zarqānī", "je m’appuie sur le Šarḥ az-Zarqānī sur le Muwaṭṭaʾ" in hn)
chk("taqwīm yabṭuwa + ʿirq", "que le consacré fasse percer son abcès (yabṭuwa ḫurāǧah) et coupe sa veine (wa-yaqṭaʿa ʿirqatahu)" in hn)
chk("taqwīm ẓufr + dummāl", "le consacré coupe son ongle (ẓufr) s’il se casse" in hn and "le consacré fend son furoncle (šaqq al-muḥrim dummālah)" in hn)
chk("taqwīm cas limites", "l’aigle teste la frontière de la liste des bêtes" in hn)
chk("istiṯmār 1036 miroir", "regarda dans le miroir pour se plaindre (li-yaškū)" in hn and "n° 1036" in hn)
chk("istiṯmār 1038 ongle", "au sujet d’un ongle à lui qui s’était brisé (ẓufr lahu nkasar)" in hn and "«&nbsp;&nbsp;coupe-le&nbsp; » (iqṭaʿhu)" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "« coupe-le » (iqṭaʿhu)" in hn)
chk("istiṯmār 1040 lā baʾs", "il n’y a pas de mal (lā baʾs) à ce que le consacré fasse percer son abcès" in hn)
chk("istiṯmār frontière soin", "ce qui perce, coupe ou fend quand la nécessité l’exige est une œuvre de soin" in hn)
chk("iʿdād leçon 9", "al-ʿaǧz wa-l-iḥṣār ʿan al-ḥaǧǧ, slot pdf-mut23h2x-398" in hn)
chk("iʿdād muḥṣar + muḫtam", "explique le muḥṣar — le muḫtam" in hn)
chk("iʿdād iḥṣār Zarqānī", "les jugements de l’empêchement (al-iḥṣār) dans le ḥaǧǧ ou la ʿumra" in hn)
chk("iʿdād femme de Ḫuṯʿam", "la femme de Ḫuṯʿam qui interroge le Prophète" in hn)

# --- 16) apparat ---
chk("apparat bornes tranchées", "bornes tranchées" in hn)
chk("apparat WIP-R641 réutilisé", "réutilisation intégrale du WIP-R641" in hn and "44&nbsp;953 car" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "44 953 car" in hn)
chk("apparat récusations image", "récusations de la couche texte par preuve d’image" in hn)
chk("apparat dummālah vs kalaf", "šaqq al-muḥrim dummālah" in hn and "šaqq al-muḥrim kalaf" in hn)
chk("apparat ǧanāḥ vs ǧazāʾ", "«&nbsp;&nbsp;ǧanāḥun&nbsp; »" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "« ǧanāḥun »" in hn)
chk("apparat naha ʿanhu vs qatlihi", "wa-qad naha Allāhu ʿanhu" in hn and "ʿan qatlihi" in hn)
chk("apparat al-faʾratu", "«&nbsp;&nbsp;al-faʾratu&nbsp; »" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "« al-faʾratu »" in hn)
chk("apparat zones omises", "zones dégradées rendues au plus sûr et documentées" in hn)
chk("apparat 1033 ouverture éclatée", "l’ouverture de la citation de Mālik précédant le n° 1033" in hn)
chk("apparat ḥurma omise", "la suite de la phrase imprimée est dégradée aux couches, documentée à l’apparat" in hn)
chk("apparat verse cache + marque", "un verset coranique imprimé en thuluth, rendu une seule fois du cache coranique" in hn)

# --- 17) registre : voisins intacts, 398 pas encore livré ---
reg = json.load(open(REG, encoding="utf-8"))
lessons = reg.get("lessons", reg)
if isinstance(lessons, dict):
    lessons = list(lessons.values())
l396 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-396" and l.get("htmlFr")]
l395 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-395" and l.get("htmlFr")]
chk("voisin 396 intact", len(l396) >= 1)
chk("voisin 395 intact", len(l395) >= 1)
chk("398 non livré (avant hand-set)", not [l for l in lessons if l.get("docId") == "pdf-mut23h2x-398" and l.get("htmlFr")])

# --- 18) savant-registry ---
sav = json.load(open(SAV, encoding="utf-8"))
hand = len(sav["hand"]) if isinstance(sav, dict) and "hand" in sav else (len(sav) if isinstance(sav, list) else 0)
llm = len(sav["llm"]) if isinstance(sav, dict) and "llm" in sav else 0
tot = hand + llm
chk(f"registre savants ≥ 1185 (actuel {tot} = hand {hand} + llm {llm})", tot >= 1185)

print(f"verify-hadith3-pdf397 : {ok}/{ok + fail} PASS")
if fail:
    raise SystemExit(1)
