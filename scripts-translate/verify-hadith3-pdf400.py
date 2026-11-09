# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-400
(aḥkām aṭ-ṭawāf (2) — الدرس 11, p.78-83 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) : bornes
p.78-83 (bannière الدرس الحادي عشر p.78, médaillon 11, lu par image 600 dpi ;
p.84 = bannière الدرس الثاني عشر médaillon 12 « aḥkām as-saʿy » = borne
supérieure exclusive ; p.77 = clôture leçon 10, iʿdād « mūrāhiq / ṭawāf
al-ḥāʾiḍ » convergence) ; 12 numéros de référence tranchés chiffre par chiffre
(1088, 1080, 1081, 1087, 1230, 1232, 1083, 1089, 1086, 1231, 1231 doublon
imprimé consigné, 1085) ; citations coraniques rendues du cache ḥafṣ (22:32,
22:33, 22:29) sous étiquettes imprimées warš 30/31 — décalage warš = ḥafṣ − 2
sur la zone (doctrine R511 « moins un » non vérifiable ici, texte tranchant
primant, précédent al-Isrāʾ R552) ; écart canonique consigné : citation de
p.80 étiquetée « 31 » au texte ḥafṣ 29 ; honnêteté d’apparat ×14 (année 23
vs couche 32 retournée, volumes dégradés, verbe de l’interdit, liste des
personnes, objet du pagne, formule d’interprétation, rubrique du fiqh masquée,
répétition triple confirmée, incipit d’ʿUrwa 1200 dpi, verbe final tafīḍ
tranché à la couche, masṭūr vs mustūr récusé, afāḍat lettre à lettre, mots
glossés lettre à lettre, coquille cache 22:29 écartée) ; WIP R660 réutilisé
(extraction 32 021 car, 21 lectures VLM réexploitées) + 6 lectures ciblées
R662 ; rasm nu interdit, double rendu interdit (1080/1087 re-cités au fiqh par
renvoi, suite du 1230 en prose de renvoi) ; 0 arabe, 0 apostrophe droite,
0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf400.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-400-fr.html"
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
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u2009", " "))

# --- 1) squelette ---
chk("h1 Leçon 11", "<h1>Leçon 11" in hn and "aḥkām aṭ-ṭawāf" in hn)
chk("h1 titleFr registre", "les règles de la circumambulation (ṭawāf) (2)" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.78-83", "p.78-83" in hn)
chk("meta trace tick job", "1a1a172f41684dc9-cron-agent-loop-202611091434" in hn and "14h34" in hn and "499558" in hn)
chk("meta takeover légal r660bis", "takeover" in hn and "r660bis" in hn and "06h46 UTC" in hn)
chk("meta voisins 399/401-418/uh2-277/281", "pdf-mut23h2x-399" in hn and "pdf-mut23h2x-401" in hn and "pdf-mut23h2u-277" in hn and "pdf-mut23h2u-281" in hn)
chk("meta titre bannière", "aḥkām aṭ-ṭawāf (2)" in hn)
chk("meta p.84 exclusive médaillon 12", "médaillon" in hn and "12" in hn and "borne supérieure exclusive" in hn)
chk("meta WIP R660 réutilisé", "32 021" in hn and "WIP R660" in hn)
chk("meta token + 13 commits poussés", "f54192e0..d65828e2" in hn and "treize commits" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’évaluation (at-taqwīm)",
    "L’exploitation pédagogique (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les trois objectifs ---
chk("obj 1 qudūm ET wadāʿ", "le jugement du ṭawāf d’arrivée et du ṭawāf d’adieu" in hn)
chk("obj 1 double attestation zoom", "tranchée par zoom 600 dpi de la bannière" in hn)
chk("obj 2 ḥāʾiḍ", "connaître les règles du ṭawāf de la menstruée" in hn)
chk("obj 3 sunna", "suivre la sunna du Prophète et sa conduite dans le ṭawāf" in hn)

# --- 3) tamhīd ---
chk("tamhīd convenances", "Le ṭawāf a des convenances" in hn)
chk("tamhīd 1088 conversation", "je n’aime pas cela pour lui" in hn and "1088" in hn)
chk("tamhīd espèces", "le ṭawāf d’arrivée diffère du ṭawāf d’adieu" in hn and "ṭawāf d’ifāḍa" in hn)
chk("tamhīd deux questions", "Quel donc est le jugement du ṭawāf d’adieu et d’arrivée" in hn and "sans pureté rituelle" in hn)

# --- 4) les numéros tranchés ---
for num in ("1088", "1080", "1081", "1087", "1230", "1232", "1083", "1089", "1086", "1231", "1085", "23"):
    chk(f"numéro {num} présent", num in hn)

# --- 5) texte 1080 (ʿUmar) + commentaire 1081 ---
chk("1080 chaîne Nāfiʿ", "d’après Nāfiʿ, d’après ʿAbd Allāh b. ʿUmar" in hn)
chk("1080 que personne ne reparte", "Que personne ne reparte" in hn and "(lā yaṣaddiranna)" in hn)
chk("1080 dernière des dévotions", "la dernière des dévotions (an-nusk)" in hn)
chk("1081 commentaire Mālik", "au sujet de la parole d’ʿUmar" in hn and "à notre avis — et Dieu sait mieux" in hn)
chk("1081 verset injonctions sacrées (cache 32)", "quiconque exalte les injonctions sacrées d’Allah, s’inspire en effet de la piété des cœurs" in hn)
chk("1081 verset warš 30 → ḥafṣ 32", "āya : 30 — imprimé warš" in hn and "āya 32" in hn)
chk("1081 verset fragment Antique Maison (cache 33)", "puis son lieu d’immolation est auprès de l’Antique Maison" in hn)
chk("1081 verset warš 31 → ḥafṣ 33", "āya : 31 — imprimé warš" in hn and "āya 33" in hn)
chk("1081 glose de Mālik", "le lieu des rites sacrés tout entier, et leur achèvement" in hn)

# --- 6) texte 1087 (Saʿd) ---
chk("1087 mūrāhiq", "Saʿd b. Abī Waqqāṣ, lorsqu’il entrait à La Mecque comme mūrāhiq" in hn)
chk("1087 sortait vers ʿArafa", "sortait vers ʿArafa avant de tourner autour de la Maison" in hn)
chk("1087 ample", "cela est ample, si Dieu le veut" in hn)

# --- 7) texte 1230 (ʿĀʾiša) ---
chk("1230 chaîne Qāsim", "d’après ʿAbd ar-Raḥmān b. al-Qāsim, d’après son père" in hn)
chk("1230 arrivée menstruée", "Je suis arrivée à La Mecque alors que j’avais mes menstrues" in hn)
chk("1230 fais ce que fait le pèlerin", "fais ce que fait le pèlerin" in hn)
chk("1230 jusqu’à pureté", "jusqu’à ce que tu sois pure" in hn)

# --- 8) notice transmetteur (ʿUmar) ---
chk("tarǧama Abū Ḥafṣ nasab", "Abū Ḥafṣ ʿUmar b. al-Ḫaṭṭāb b. Nufayl, le Qurayšite al-ʿAdawī" in hn)
chk("tarǧama émir des croyants", "émir des croyants, calife du Messager de Dieu" in hn)
chk("tarǧama justice ascétisme", "on le cite en exemple dans la justice, l’ascétisme, l’humilité" in hn)
chk("tarǧama mort 23 image vs couche 32 récusée", "Il fut martyrisé en l’an 23 de l’Hégire" in hn and "(deux, trois)" in hn and "retournée par paires" in hn)
chk("tarǧama volumes dégradés", "des volumes ont été consacrés à sa biographie" in hn and "dégradé aux deux couches" in hn)

# --- 9) gloses ---
chk("glose lā yaṣaddiranna", "ne s’en aille pas (lā yanṣarifanna" in hn)
chk("glose maḥalluhā", "le lieu où son immolation devient licite (makān ḥill naḥrihā)" in hn)
chk("glose mūrāhiq kasra fatḥa", "admet le kasra et le fatḥa sur le hāʾ" in hn)
chk("glose mūrāhiq temps resserré", "dont le temps s’est resserré au point qu’il craint de manquer le stationnement à ʿArafa" in hn)

# --- 10) istiḫlāṣ ---
chk("istiḫlāṣ item 1 adieu", "j’expose les règles du ṭawāf d’adieu" in hn)
chk("istiḫlāṣ item 2 mūrāhiq", "j’extrais des recueils le jugement du ṭawāf d’arrivée pour le mūrāhiq" in hn)
chk("istiḫlāṣ item 3 ḥāʾiḍ", "quel est le jugement du ṭawāf de la menstruée" in hn)

# --- 11) fiqh : premièrement (wadāʿ) ---
chk("fiqh rubrique masquée documentée", "lettre médiane masquée par le point décoratif" in hn)
chk("wadāʿ recommandé chez Mālik", "est recommandé (mustaḥabb) chez Mālik" in hn)
chk("1080 re-cité par renvoi", "déjà rendue au premier texte (n° 1080, renvoi, jamais re-traduite)" in hn)
chk("nusk adoration", "il l’a nommé dévotion (nusk) parce qu’il est une adoration" in hn)
chk("fiqh verset 29 (ḥafṣ) étiquette 31 — écart consigné", "Puis qu’ils mettent fin à leurs interdits" in hn and "l’étiquette imprimée « 31 »" in hn and "l’écart est consigné tel qu’imprimé, jamais corrigé" in hn)
chk("fiqh šaʿāʾir marques et actes", "les marques du Pèlerinage et ses actes (aʿlām al-ḥaǧǧ wa-afʿāluhū)" in hn)
chk("retour après départ recommandé", "recommandé, de l’ordre du méritoire (mustaḥabb mandūb ilayhi) chez Mālik" in hn)
chk("Ṣafiyya dialogue", "Nous retient-elle donc ?" in hn and "(a-ḥābisatunā hiya" in hn)
chk("Ṣafiyya afāḍat tranché lettre à lettre", "elle a déjà fait l’ifāḍa (inna-hā qad afāḍat" in hn and "alif, fāʾ, ḍād, tāʾ" in hn)
chk("Ṣafiyya alors non", "Alors, non" in hn and "(fa-lā iḏā)" in hn)
chk("ʿUrwa incipit 1200 dpi", "man afāḍa fa-qaḍā qaḍāʾa llāhi ḥaǧǧahū" in hn and "zoom 1200 dpi" in hn)
chk("ʿUrwa dernier lien", "son dernier lien soit la circumambulation de la Maison" in hn)

# --- 12) fiqh : deuxièmement (qudūm) ---
chk("qudūm obligation", "compte parmi les obligations du Pèlerinage (min wāǧibāt al-ḥaǧǧ)" in hn)
chk("damm Ibn al-Qāsim", "l’offrande de sang (ad-damm) selon Ibn al-Qāsim" in hn)
chk("mūrāhiq Pilier", "stationnement-pilier (al-wuqūf, rukn)" in hn)
chk("qudūm tombe de lui", "le ṭawāf d’arrivée tombe de lui" in hn)
chk("1087 re-cité par renvoi", "n° 1087, renvoi, jamais re-traduit" in hn)
chk("lā ḥaraǧ", "nul reproche (lā ḥaraǧ)" in hn)

# --- 13) fiqh : troisièmement (ḥāʾiḍ) ---
chk("ǧumhūr interdit jusqu’à pureté", "il n’est pas permis à la menstruée de tourner avant d’être pure" in hn)
chk("verbe de l’interdit dégradé documenté", "le verbe imprimé est dégradé entre les couches, le sens de l’interdit rendu" in hn)
chk("1230 re-cité en prose de renvoi", "n° 1230, renvoi" in hn)
chk("ʿilla absence de pureté", "l’absence de pureté rituelle (ʿadam aṭ-ṭahāra" in hn)
chk("liste des personnes dégradée documentée", "le verbe et la liste des personnes sont dégradés aux couches" in hn)
chk("1089 jugement Mālik", "que personne ne tourne autour de la Maison ni entre aṣ-Ṣafā et al-Marwa sans être pur" in hn)
chk("1086 femme triple scène", "chaque fois que je me trouvais à la porte de la mosquée, le sang a coulé" in hn and "la scène imprimée se répète trois fois" in hn)
chk("1086 ruée de Satan", "ce n’est là qu’une ruée de Satan" in hn)
chk("1086 lave-toi + pagne", "lave-toi (fa-ġtasilī), puis noue ton pagne (ṯumma stitfirī" in hn)
chk("1086 variante vieille femme", "qu’une vieille femme le consulta" in hn and "(an ʿaǧūzan staftat" in hn)
chk("1086 istiḥāḍa", "désigne la métrorragie (al-istiḥāḍa)" in hn)
chk("1086 ṭawāf permis = prière permise", "le ṭawāf n’est permis qu’à celle pour qui la prière est permise" in hn)
chk("1086 lavage méritoire", "le lavage pour le ṭawāf est de l’ordre du méritoire (nadb)" in hn)
chk("mutamattiʿa couplage", "comme celui qui a couplé le Pèlerinage et la ʿumra (qarana)" in hn)
chk("mutamattiʿa un seul ṭawāf", "un seul ṭawāf lui suffit" in hn)
chk("après rakʿa — saʿy ʿArafa stèles", "elle fait la course entre aṣ-Ṣafā et al-Marwa, elle stationne à ʿArafa et à al-Muzdalifa, elle lapide les stèles" in hn)
chk("verbe final tafīḍ tranché", "elle ne fait pas le ṭawāf d’ifāḍa tant qu’elle n’est pas pure" in hn and "(ġayra anna-hā lā tafīḍu" in hn)
chk("doublon 1231 consigné", "référence imprimée identique à celle de la rubrique précédente" in hn and "superposables chiffre à chiffre" in hn)

# --- 14) taqwīm + istiṯmār + iʿdād ---
chk("taqwīm item 1 adieu oublié", "celui qui a oublié le ṭawāf d’adieu puis s’en souvient après avoir quitté la Maison" in hn)
chk("taqwīm item 2 métrorragie", "la femme en métrorragie chez qui le sang est revenu après qu’elle s’est purifiée" in hn)
chk("taqwīm réponses", "le retour est recommandé, s’il ne lui en coûte pas de peine" in hn and "c’est une ruée de Satan" in hn)
chk("istiṯmār 1085 chaîne", "d’après Abū l-Aswad Muḥammad b. ʿAbd ar-Raḥmān b. Nawfal, d’après ʿUrwa b. az-Zubayr, d’après Zaynab bt. Abī Salāma, d’après Umm Salama" in hn)
chk("istiṯmār tourne à l’écart montée", "tourne à l’écart des gens, montée (ṭūfī min warāʾi n-nāsi wa-anti rākiba)" in hn)
chk("istiṯmār fa-ṭuftu net à la couche", "fa-ṭuftu" in hn and "net à la couche texte" in hn)
chk("istiṯmār aṭ-Ṭūr masṭūr récusé", "un Livre inscrit" in hn and "(wa-kitābin masṭūr" in hn and "mustūr" in hn and "récusée" in hn)
chk("istiṯmār Zarqānī ṭawāf monté", "j’expose le jugement du ṭawāf monté" in hn)
chk("iʿdād mémorise", "mémorise les hadiths de la leçon suivante" in hn)
chk("iʿdād mots glossés lettre à lettre", "Manāt (manāt)" in hn and "yaʿtalūn" in hn and "ḥaḏwā Qudayd" in hn)
chk("iʿdād saʿy leçon 12", "le jugement de la course (saʿy) entre aṣ-Ṣafā et al-Marwa" in hn)

# --- 15) apparat ---
chk("apparat bornes p.78/83", "ouverture p.78 (bannière" in hn and "clôture p.83" in hn)
chk("apparat p.84 exclusive", "p.84 = bannière du cours 12" in hn and "borne supérieure exclusive, jamais devinée" in hn)
chk("apparat jonction p.77 convergence", "jonction p.77 = clôture du cours 10" in hn and "convergence de bornes" in hn)
chk("apparat 21 lectures R660 réexploitées", "les vingt et une lectures VLM de la passe R660" in hn)
chk("apparat 6 lectures R662", "six lectures complémentaires R662" in hn)
chk("apparat cartographie citations", "cartographie fragment-étiquette tranchée" in hn)
chk("apparat warš = ḥafṣ − 2 + R511 non applicable", "vaut ici DEUX unités" in hn and "NE SE VÉRIFIE PAS sur cette zone" in hn)
chk("apparat écart étiquette 31 / ḥafṣ 29", "porte l’étiquette imprimée « 31 »" in hn and "āya 29 du cache (ḥafṣ)" in hn)
chk("apparat coquille cache 22:29", "guillemet parasite" in hn)
chk("apparat honnêteté ×14", "année de la mort d’ʿUmar" in hn and "l’objet du pagne" in hn and "l’incipit d’ʿUrwa" in hn)
chk("apparat numéros bleus chiffre par chiffre", "chiffres bleus lus chiffre par chiffre" in hn and "doublon imprimé consigné" in hn)
chk("apparat double rendu interdit", "double rendu interdit" in hn)
chk("apparat voisins 399/401-418/uh2", "livraison R650" in hn and "pdf-mut23h2x-401" in hn)
chk("apparat machine token 13 commits", "treize commits locaux R657-R661 ont été poussés" in hn)
chk("apparat machine claim 07h49/08h09", "posé à 07h49 UTC" in hn and "rafraîchi à 08h09 UTC" in hn)

# --- 16) 0 arabe script, rasm nu, doublons ---
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", h)
chk("0 caractère arabe", len(arab) == 0)
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("h1 unique", h.count("<h1>") == 1)

# --- 17) registre (avant hand-set : slot vide ; après : htmlFr présent) ---
try:
    reg = json.load(open(REG, encoding="utf-8"))
    lessons = reg if isinstance(reg, list) else reg.get("lessons", [])
    slot = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-400"), None)
    if slot and slot.get("htmlFr"):
        chk("registre htmlFr 400 rempli", len(slot["htmlFr"]) > 15000)
        chk("titleAr/titleFr pré-mappés intacts", slot.get("titleAr") == "أحكام الطواف (2)" and slot.get("titleFr", "").startswith("Les règles de la circumambulation (ṭawāf) (2)"))
        voisins = [l.get("docId") for l in lessons if l.get("docId") in ("pdf-mut23h2x-399", "pdf-mut23h2x-401")]
        chk("voisin 399 intact / 401 jamais écrit par ce worker", "pdf-mut23h2x-399" in voisins and "pdf-mut23h2x-401" in voisins)
        v399 = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-399"), None)
        chk("htmlFr 399 intact (R650)", v399 is not None and len(v399.get("htmlFr") or "") == 32320)
        sav = json.load(open(SAV, encoding="utf-8"))
        savh = sav.get("hand", {})
        chk("savant-registry 400 posé", "pdf-mut23h2x-400" in json.dumps(savh))
        n = sav.get("count") or (len(savh) if isinstance(savh, dict) else 0)
        chk("registre savants ≥ 1199", int(n if isinstance(n, (int, float)) else 0) >= 1199 or len(json.dumps(savh)) > 100)
    else:
        chk("registre 400 encore vide (pré-hand-set)", slot is None or not slot.get("htmlFr"))
except Exception as e:
    chk(f"registres lisibles ({e})", False)

print(f"\nverify-hadith3-pdf400 : {ok} OK / {fail} échec(s)")
raise SystemExit(1 if fail else 0)
