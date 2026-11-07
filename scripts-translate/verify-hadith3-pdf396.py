# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-396
(al-ikāḥ fī-l-iḥrām wa-akl min aṣ-ṣayd — الدرس 7, p.52-57 du manuel
hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé 29 slots
pdf-mut23h2x-390..418) : bornes p.52-57 (passation R639-bis, reconfirmées
par inspections d'image 600-1500 dpi) ; 13 numéros de référence tranchés
(999, 1001, 1002, 1003, 1007, 1008, 1009, 1015, 1017, 1019, 1020, 1021, 54)
— dont six par image directe (999, 1007, 1017, 1019, 1020, 54) et le reste
par couches + suite numérique (1001, 1002, 1003, 1008, 1009, 1015, 1021) ;
« 939 ? » de la passation R639-bis réfuté par image (n° 999 imprimé en bleu) ;
récusations par image : Zayd b. Aslam « hal maʿakum min laḥmihi šayʾ » contre
OCR « aḫmatihi fī ẓannik », mort d'Abū Qatāda 54 H contre OCR « 45 » ; UN
verset imprimé (fin de l'āya 96 warš de la sourate 5, cache coranique idx 96,
écart warš/ḥafṣ documenté) rendu du cache coranique ; 0 arabe, 0 apostrophe
droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf396.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-396-fr.html"
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
chk("h1 Leçon 7", "<h1>Leçon 7" in hn and "iḥrām" in hn)
chk("h1 titleFr registre", "le mariage en état d’iḥrām et la consommation du gibier" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.52-57", "p.52-57" in hn)
chk("meta trace tick job", "1a19c7c0ffb4f845-cron-agent-loop-202611070837" in hn and "08h37" in hn and "496554" in hn)
chk("meta voisins 395/397/uh2-268", "pdf-mut23h2x-395" in hn and "pdf-mut23h2x-397" in hn and "uh2-pdf-mut23h2u-268" in hn)
chk("meta bannière at-tamrīn 7", "at-tamrīn 7" in hn)
chk("meta titre bannière al-ikāḥ", "al-ikāḥ fī-l-iḥrām wa-akl min aṣ-ṣayd" in hn)
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

# --- 2) les deux objectifs ---
chk("obj 1 jugement mariage + gibier", "reconnaître le jugement du mariage du consacré" in hn and "manger du gibier" in hn)
chk("obj 2 sagesse de l’interdiction", "saisir la sagesse de l’interdiction" in hn)

# --- 3) tamhīd ---
chk("tamhīd dépouillement", "dépouillement (taǧarrud)" in hn and "des plaisirs d’ici-bas" in hn)
chk("tamhīd deux voies", "a interdit certaines pratiques, pour réaliser les desseins du ḥaǧǧ" in hn)
chk("tamhīd taysīr", "tolérance (taysīr) envers le consacré" in hn)
chk("question d’ouverture", "quelles sont donc les choses interdites et les choses permises au consacré" in hn)

# --- 4) les numéros tranchés ---
for num in ("999", "1001", "1002", "1003", "1007", "1008", "1009", "1015", "1017", "1019", "1020", "1021", "54"):
    chk(f"numéro {num} présent", num in hn)

# --- 5) texte 999 ---
chk("999 chaîne Nubayh", "Nubayh b. Wahb, frère des Banū ʿAbd ad-Dār" in hn)
chk("999 ʿUmar b. ʿUbayd Allāh", "ʿUmar b. ʿUbayd Allāh" in hn)
chk("999 Abān commandant", "Abān b. ʿUthmān" in hn and "commandant du pèlerinage" in hn)
chk("999 Ṭalḥa + Šuʿayb", "Ṭalḥa b. ʿUmar à la fille de Šuʿayb b. Ǧubayr" in hn)
chk("999 ʿUthmān b. ʿAffān", "ʿUthmān b. ʿAffān" in hn)
chk("999 formule hadith", "le consacré ne marie pas (lā yunkiḥu) et n’est pas marié (wa-lā yunkaḥu)" in hn)

# --- 6) texte 1007 ---
chk("1007 chaîne Abū an-Naḍr", "Abū an-Naḍr, mawla de ʿUmar b. ʿUbayd Allāh at-Tamīmī" in hn)
chk("1007 chaîne Nāfiʿ mawlā", "Nāfiʿ, mawlā d’Abū Qatāda al-Anṣārī" in hn)
chk("1007 fouet + lance", "son fouet (sawṭahu)" in hn and "sa lance (rumḥahu)" in hn)
chk("1007 âne sauvage", "âne sauvage (ḥimār waḥšī)" in hn)
chk("1007 partie mange", "une partie des compagnons du Messager de Dieu en mangea, une partie refusa" in hn)
chk("1007 ṭaʿma", "ce n’est qu’une bouchée (ṭaʿma) que Dieu vous a donnée à manger" in hn)
chk("1007 iǧtihād al-furūʿ", "licéité de l’effort d’interprétation dans les branches" in hn)

# --- 7) notice transmetteur ---
chk("tarǧama Sulamī + fāris", "le Sulamī, cavalier (fāris) du Messager de Dieu" in hn)
chk("tarǧama Uḥud + Ḥudaybiya", "il a pris part à Uḥud et à al-Ḥudaybiya" in hn)
chk("tarǧama Ḥāriṯ b. Ribʿī", "son nom est al-Ḥāriṯ b. Ribʿī d’après la version sûre" in hn)
chk("tarǧama 4 transmetteurs", "Anas b. Mālik" in hn and "Saʿīd b. al-Musayyab" in hn and "ʿAṭāʾ b. Yasār" in hn and "ʿAlī b. Rabāḥ" in hn)
chk("tarǧama mort 54", "mort à Médine en l’an 54 de l’Hégire" in hn)

# --- 8) gloses ---
chk("glose yunkiḥu", "il ne conclut pas de contrat pour lui-même" in hn)
chk("glose yunkaḥu", "il ne conclut pas de contrat pour autrui" in hn)

# --- 9) fiqh mariage ---
chk("wilāya + wikāla", "ni tutelle (wilāya) ni mandat (wikāla)" in hn)
chk("al-Ḫaṭābī ǧazm", "al-Ḫaṭābī, que la prohibition du hadith est catégorique" in hn)
chk("wa-lā taḫṭub", "et qu’elle ne se fiance pas" in hn)
chk("nullité + dissolution", "le contrat n’est pas valable (lā yaṣiḥḥu) et se dissout (yufsaḫu)" in hn)
chk("Tuḥfa Ibn ʿĀṣim", "Ibn ʿĀṣim l’a formulé dans la Tuḥfa" in hn and "ṭalāqa tuʿaddu fī ṭ-ṭalāq" in hn)
chk("1001 Saʿīd fiançailles", "aucune demande en mariage, ni pour sa promise ni pour une autre" in hn)
chk("1002 trois savants", "Saʿīd b. al-Musayyab, Salām b. ʿAbd Allāh et Sulaymān b. Yasār, interrogés" in hn)
chk("1003 reprise ʿidda", "il reprend (yurāǧiʿu) son épouse s’il veut, lorsqu’elle est en période d’attente (ʿidda)" in hn)
chk("1003 sortie d’ʿidda", "si elle est sortie de sa période d’attente, elle ne rentre plus dans le hadith" in hn)
chk("Abū ʿUmar amṣār", "les imams des capitales du droit (aʾimmat al-fatwā bi-l-amṣār)" in hn)
chk("reprise sans walī ni ṣadāq", "la reprise n’exige ni tuteur (walī) ni dot (ṣadāq)" in hn)

# --- 10) fiqh gibier ---
chk("gibier d’autrui licite", "il est permis au consacré de manger du gibier de terre lorsque c’est un non-consacré qui l’a chassé" in hn)
chk("1009 Zayd b. Aslam", "Dans le hadith de Zayd b. Aslam" in hn and "avez-vous de sa viande quelque chose avec vous" in hn)
chk("dalāla iʿāna išāra", "d’indication (dalāla), d’assistance (iʿāna) ou de signe (išāra)" in hn)
chk("ǧumhūr interdit chassé pour lui", "s’il l’a chassé lui-même, ou si on l’a chassé pour lui" in hn)
chk("hadith Ǧābir", "le gibier de la terre vous est licite tant que vous ne l’avez pas chassé ou qu’on ne l’a pas chassé pour vous" in hn)
chk("Ǧābir 3 rapporteurs", "Abū Dāwūd, at-Tirmiḏī et an-Nasāʾī" in hn)
chk("1008 az-Zubayr ṣafīḥ", "az-Zubayr b. al-ʿAwwām se provisionnait de ṣafīḥ" in hn and "le ṣafīḥ, c’est le qadīd" in hn)
chk("1015 ʿinda ahlihi", "il n’y a pas de mal à ce qu’il le place chez les siens (ʿinda ahlihi)" in hn)
chk("Ibn Wahb qafṣ", "Ibn Wahb a dit" in hn and "dans une cage (qafṣ)" in hn)
chk("1017 aṣ-Ṣalṭ b. Ǧaʿda", "aṣ-Ṣalṭ b. Ǧaʿda al-Layṯī" in hn)
chk("1017 chaîne ʿUtba", "ʿAbd Allāh b. ʿAbd Allāh b. ʿUtba b. Masʿūd, d’après ʿAbd Allāh b. ʿAbbās" in hn)
chk("1017 Abwāʾ/Waddān", "à al-Abwāʾ ou à Waddān" in hn)
chk("1017 radd + raison", "le lui retourna (raddahū ʿalayhi)" in hn and "parce que nous sommes consacrés" in hn)
chk("verset cache coranique", "rendue ici du cache coranique" in hn and "vous est illicite la chasse à terre tant que vous êtes en état d’iḥrām" in hn)
chk("verset āya 96 sourate 5", "fin de l’āya 96 de la sourate 5" in hn and "écart warš/ḥafṣ documenté" in hn)
chk("principe du doute", "de laisser ce qui le trouble (mā yurībih) pour ce qui ne le trouble pas" in hn)
chk("1019 ʿĀʾiša dix nuits", "ce ne sont que dix nuits" in hn and "si quelque doute s’agite en toi, laisse-le" in hn)
chk("1019 vise viande gibier", "cela vise la consommation de la viande du gibier" in hn)
chk("1020 pénalité entière", "la pénalité (ǧazāʾ) du gibier entier pèse sur lui" in hn)
chk("1020 lā yutabaʿʿaḍ", "la pénalité ne se divise pas (al-ǧazāʾ lā yutabaʿʿaḍ)" in hn)

# --- 11) taqwīm + istiṯmār + iʿdād ---
chk("taqwīm istidlāl", "avec l’argumentation (al-istidlāl)" in hn)
chk("taqwīm deux figures", "un homme qui reprend son épouse alors qu’il est consacré" in hn and "un consacré qui mange un gibier sur sa route vers La Mecque" in hn)
chk("istiṯmār 1021 muḍṭarr", "l’homme contraint (yuḍṭarru) de manger de la bête morte (al-mayta)" in hn)
chk("1021 ruxṣa + aḥwāl", "la permission (rukhṣa) a été accordée au consacré pour le gibier" in hn and "en aucune circonstance (fī ḥāl min al-aḥwāl)" in hn)
chk("iʿdād leçon 8", "aḥkām ṣayd al-muḥrim wa-l-ǧazāʾ fīhi" in hn and "slot pdf-mut23h2x-397" in hn)
chk("iʿdād dawābb", "les bêtes (ad-dawābb) qu’il est permis de tuer dans le territoire sacré" in hn)

# --- 12) apparat ---
chk("apparat bornes tranchées", "bornes tranchées" in hn and "médaillon stylisé" in hn)
chk("apparat 939 réfuté", "l’hypothèse « 939 » de la passation R639-bis" in hn)
chk("apparat récusations image", "récusations de la couche texte par preuve d’image" in hn)
chk("apparat zones omises", "zones omises comme indéchiffrables" in hn and "Ṭarīf b. Ghaṭafān" in hn)

# --- 13) registre : voisins intacts, 396 pas encore livré ---
reg = json.load(open(REG, encoding="utf-8"))
lessons = reg.get("lessons", reg)
if isinstance(lessons, dict):
    lessons = list(lessons.values())
l395 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-395" and l.get("htmlFr")]
l394 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-394" and l.get("htmlFr")]
chk("voisin 395 intact", len(l395) >= 1)
chk("voisin 394 intact", len(l394) >= 1)
chk("396 non livré (avant hand-set)", not [l for l in lessons if l.get("docId") == "pdf-mut23h2x-396" and l.get("htmlFr")])

# --- 14) savant-registry ---
sav = json.load(open(SAV, encoding="utf-8"))
hand = len(sav["hand"]) if isinstance(sav, dict) and "hand" in sav else (len(sav) if isinstance(sav, list) else 0)
llm = len(sav["llm"]) if isinstance(sav, dict) and "llm" in sav else 0
tot = hand + llm
chk(f"registre savants ≥ 1183 (actuel {tot} = hand {hand} + llm {llm})", tot >= 1183)

print(f"verify-hadith3-pdf396 : {ok}/{ok + fail} PASS")
if fail:
    raise SystemExit(1)
