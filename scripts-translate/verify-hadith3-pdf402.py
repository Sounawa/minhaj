# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-402
(aʿmāl yawm ʿArafa — leçon 13, p.90-96 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) : bornes
p.90-96 (bannière « aʿmāl yawm ʿArafa » p.90 — titleAr du registre, médaillon
calligraphique, cours 13 par convergence bannière-registre-bornes ; p.97 =
bannière du cours 14 « Les règles du séjour à Muzdalifa » = borne supérieure
exclusive ; p.89 = clôture du cours 12, iʿdād « prière et sermon à ʿArafa /
jeûne du jour de ʿArafa » convergence) ; dix numéros de référence + l'année
106 tranchés chiffre par chiffre (1271, 1157 ×2 p.90/p.93, 1100, 1188, 1152,
1155, 1101, 1190, 1191, 1270) ; ZÉRO āya dans la leçon (la formule du tamhīd
n° 1271 est la kalima, pas une āya — aucun recours au cache) ; quatre
adjudications majeures par preuve image (matn 1188 complet p.91 r669-f ;
prière/ǧumʿa p.94 entier r669-d avec [1190]/[1191] ; second cas de
l'évaluation p.95 r669-e « reparti avant le coucher, rejoignant
al-Muzdalifa » ; tamhīd p.90 r669-h) ; segments dégradés déclarés (isnād
introductif du n° 1100, ordre des conclusions du n° 1157 p.90/p.93, complément
« taqwī ʿalā … », segment médian p.95, « fa-l-yuqriba ʿan-hu ʿaǧuz ») ;
écarts canoniques consignés (note Ṣaḥīḥ Muslim telle qu'imprimée, épithètes
adḥar/adḥkar et aḥqar/aḥfar, Ǧibrīl) ; machine : token restauré au chat par
l'utilisateur, distant == local 1952684b avant livraison (aucun reset
destructif — sixième recyclage reconstitué sans perte), claim
workerD-tick0456-r670 refresh 21h27/21h37 UTC ; 0 arabe, 0 apostrophe droite,
0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf402.py
"""
import json
import re

import sys
HTML = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-402-fr.html"
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
chk("h1 Leçon 13", "<h1>Leçon 13" in hn and "aʿmāl yawm ʿArafa" in hn)
chk("h1 titleFr registre", "les rites du jour de ʿArafa" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.90-96", "p.90-96" in hn)
chk("meta trace tick job", "1a1c23c49937a9b9" in hn and "04h56" in hn and "499559" in hn)
chk("meta claim r670 refresh", "workerD-tick0456-r670" in hn and "21h27" in hn and "21h37" in hn)
chk("meta token restauré + distant == local", "1952684b" in hn and "Everything up-to-date" in hn)
chk("meta aucun reset destructif", "aucun reset destructif" in hn and "recyclage" in hn)
chk("meta voisins 401/403", "pdf-mut23h2x-401" in hn and "pdf-mut23h2x-403" in hn)
chk("meta p.97 exclusive cours 14", "p.97" in hn and "borne supérieure exclusive, jamais devinée" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours : les hadiths du Muwaṭṭaʾ traduits du manuel",
    "Premier texte — ʿAbd Allāh b. ʿUmar : l’aube de la nuit de al-Muzdalifa, limite du stationnement (al-Muwaṭṭaʾ, n° 1157)",
    "Deuxième texte — Umm al-Faḍl bint al-Ḥāriṯ : la coupe de lait du jour de ʿArafa (al-Muwaṭṭaʾ, n° 1100)",
    "Troisième texte — Sālim b. ʿAbd Allāh : le voile teint, le départ au plus tôt et la sunna (al-Muwaṭṭaʾ, n° 1188)",
    "La notice des transmetteurs (tarǧamat ar-ruwāt)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ) : le stationnement d’ʿArafa — le lieu, le temps, les convenances, la prière et la sermon",
    "Premièrement : le lieu du stationnement (makān al-wuqūf)",
    "Deuxièmement : le temps du stationnement (waqt al-wuqūf)",
    "Troisièmement : les convenances du jour de ʿArafa (ādāb yawm ʿArafa)",
    "Quatrièmement : la prière et la sermon (aṣ-ṣalāt wa-l-ḫuṭba) le jour de ʿArafa",
    "L’évaluation (at-taqwīm) de la leçon",
    "L’exploitation du cours (al-istitmār) : la petitesse du diable le jour de ʿArafa",
    "La préparation préalable (al-iʿdād al-qablī) de la leçon suivante",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:46]} »", sec in hn)

# --- 2) les trois objectifs ---
chk("obj 1 wuqūf", "que je reconnaisse (an a-taʿarrafa) les règles du stationnement (aḥkām al-wuqūf) à ʿArafa" in hn)
chk("obj 2 ṣalāt/ḫuṭba ʿArafāt", "que je reconnaisse les règles de la prière et de la sermon (aḥkām aṣ-ṣalāt wa-l-ḫuṭba) à ʿArafāt" in hn)
chk("obj 3 maqāṣid", "que je saisisse (an a-drika) les finalités religieuses (maqāṣid aš-šarʿ) du stationnement à ʿArafa" in hn)
chk("obj 3 visée finale", "le stationnement n’est pas seulement une règle, il est une fin" in hn)

# --- 3) tamhīd (1271) ---
chk("tamhīd chaîne Ziyād/Ṭalḥa", "Ziyād b. Abī Ziyād" in hn and "Ṭalḥa b. ʿUbayd Allāh b. Kryz" in hn)
chk("tamhīd meilleure invocation", "La meilleure des invocations (afḍal ad-duʿāʾ) est l’invocation du jour de ʿArafa" in hn)
chk("tamhīd kalima (pas d'āya)", "lā ilāha illā llāh waḥda-hu lā šarīka la-h" in hn)
chk("tamhīd ZÉRO āya noté", "ZÉRO citation coranique" in hn)
chk("tamhīd double question", "les règles du stationnement à ʿArafa (famā hiya ḥukm al-wuqūf bi-ʿArafa), et quels sont les actes" in hn)

# --- 4) les numéros tranchés ---
for num in ("1271", "1157", "1100", "1188", "1152", "1155", "1101", "1190", "1191", "1270", "106", "13"):
    chk(f"numéro {num} présent", num in hn)

# --- 5) texte 1157 (Ibn ʿUmar) ---
chk("1157 chaîne Nāfiʿ", "Mālik rapporte de Nāfiʿ que ʿAbd Allāh b. ʿUmar disait" in hn)
chk("1157 man lam yaqif", "(man lam yaqif bi-ʿArafa)" in hn)
chk("1157 conclusions croisées consignées", "fāta-hu l-ḥaǧǧ" in hn and "fa-qad adraka l-ḥaǧǧ" in hn and "l’ordre des conclusions" in hn)
chk("1157 rattrapage ʿumra + qaḍāʾ", "qu’il sorte de l’état de sacralisation par une ʿumra (fa-l-yataḥallal bi-ʿumra)" in hn and "l’année suivante (fī ʿāmin qābil)" in hn)

# --- 6) texte 1100 (Umm al-Faḍl) ---
chk("1100 isnād dégradé déclaré", "déclaré non restituable" in hn and "l’échanson" in hn)
chk("1100 dispute du jeûne", "Les gens disputaient (tamārawa n-nās" in hn and "il jeûne" in hn and "il ne jeûne pas" in hn)
chk("1100 coupe de lait", "une coupe (bi-qadaḥin) de lait (laban)" in hn and "debout sur sa monture à ʿArafa" in hn)
chk("1100 acte = sentence", "l’acte en ce jour vaut sentence" in hn)

# --- 7) texte 1188 (Sālim — le récit complet) ---
chk("1188 lettre d'ʿAbd al-Malik", "kataba ʿAbdu l-Malik b. Marwāna ilā l-Ḥaǧǧāǧ b. Yūsuf" in hn)
chk("1188 voile teint", "vêtu d’un pagne teint de carthame (wa-ʿalay-hi milḥafatun muʿaṣfara)" in hn)
chk("1188 ar-rawāḥ image", "Le départ au plus tôt (ar-rawāḥ) — si tu veux la sunna (in kunta turīdu s-sunna)" in hn)
chk("1188 délai + ablution", "Accorde-moi un délai (fa-nẓurnī) jusqu’à ce que je verse de l’eau sur moi (ḥattā afīḍa ʿalā māʾ)" in hn)
chk("1188 qaṣr + taʿǧīl", "écourte la sermon (fa-qṣuri l-ḫuṭba) et hâte la prière (wa-ʿaǧǧil ṣ-ṣalāt)" in hn)
chk("1188 ṣadaqa", "Il a dit vrai (ṣadaqa)" in hn)
chk("1188 note Ṣaḥīḥ Muslim consignée", "il patienta alors peu" in hn and "telle qu’imprimée" in hn)

# --- 8) notices des transmetteurs ---
chk("notice Umm al-Faḍl = Lubāba", "Lubāba al-Kubrā bint al-Ḥāriṯ al-Hilāliyya" in hn and "an-naǧabāʾ" in hn)
chk("notice Umm al-Faḍl mort ʿUṯmān", "mourut sous le califat de ʿUṯmān, avant son époux al-ʿAbbās" in hn)
chk("notice Sālim nasab", "Sālim b. ʿAbd Allāh b. ʿUmar b. al-Ḫaṭṭāb al-ʿAdawī" in hn)
chk("notice Sālim éloge de Mālik", "Nul, au temps de Sālim" in hn and "le renoncement" in hn)
chk("notice Sālim mort 106 H", "Il mourut l’an 106 de l’Hégire (tawuffiya sanata 106" in hn and "artefact, récusée" in hn)

# --- 9) gloses (4) ---
chk("glose tamārawā", "ils divergèrent (iḫtalafū)" in hn)
chk("glose surādiq", "le surādiq est ce qui entoure (mā yuḥīṭu) la tente" in hn)
chk("glose muʿaṣfara", "un grand pagne (milḥafa kabīra) teint avec le carthame (maṣbūġun bi-l-ʿuṣfur)" in hn)
chk("glose nẓurnī", "accorde-moi un délai (aẓhir-nī" in hn)

# --- 10) istiḫlāṣ (3 items) ---
chk("istiḫlāṣ item 1 lieu+temps", "que je détermine (an uḥaddida) le lieu et le temps (makān wa-zamān) du stationnement" in hn)
chk("istiḫlāṣ item 2 fiṭr/rukūb/ṭahāra", "le jugement de la rupture du jeûne (ḥukma l-fiṭr), de la monture (wa-r-rukūb) et de la pureté (wa-ṭ-ṭahāra)" in hn)
chk("istiḫlāṣ item 3 ṣalāt/ḫuṭba", "comment (kayfa) se tiennent la prière et la sermon" in hn)
chk("istiḫlāṣ monture = 1100", "le Prophète ﷺ stationne debout sur sa monture — le stationnement monté est valide" in hn)

# --- 11) fiqh : le lieu ---
chk("1152 tout est stationnement", "ʿArafa tout entière est stationnement (ʿArafa kullu-hā mawqif)" in hn)
chk("1152 ʿUrnā", "wa-rtafiʿū ʿan baṭni ʿUrnā" in hn and "un lieu entre Minā et ʿArafāt" in hn)
chk("1152 sunna d'Ibrāhīm", "vient avec la sunna d’Ibrāhīm, sur lui la paix" in hn)
chk("Nawāwī ascension = erreur", "An-Nawāwī a dit" in hn and "l’ascension de la montagne" in hn and "est une erreur (ġalaṭ)" in hn)
chk("Nawāwī permission tout lieu", "la permission du stationnement en toute partie" in hn)
chk("rochers + incapacité au plus sûr", "rochers" in hn and "bi-ḥasabi l-imkān" in hn)

# --- 12) fiqh : le temps ---
chk("temps zawāl → aube", "au déclin du soleil (min zawāli) du neuvième jour de Ḏū al-Ḥiǧǧa" in hn and "l’approche de l’aube" in hn)
chk("temps après coucher bref", "ne serait-ce qu’un bref moment (wa-law zamānan yasīran)" in hn)
chk("temps rukn non compensé", "compensation n’acquite" in hn)
chk("temps jour/nuit/pilier", "le jour pour le mérite, la nuit pour le pilier" in hn)

# --- 13) fiqh : les convenances ---
chk("rawāḥ sunna", "la hâte du départ de Minā vers ʿArafa relève de la sunna" in hn)
chk("ṭahāra recommandée wuḍūʾ", "d’être en ablutions (mutawaḍḍiʾan)" in hn)
chk("1155 question de Mālik", "Mālik fut interrogé" in hn and "lapider les stèles" in hn and "courir entre aṣ-Ṣafā et al-Marwa" in hn)
chk("1155 parallèle ḥāʾiḍ", "Tout acte (kullu amrin) qu’accomplit la femme menstruée" in hn)
chk("1155 rien ne pèse + pas délibéré", "rien alors ne pèse sur lui" in hn and "qu’il le fasse délibérément" in hn)
chk("fiṭr afḍal + choix du Prophète", "kāna l-fiṭru yawma ʿArafa afḍala" in hn and "min iḫtiyāri n-nabiyyi" in hn)
chk("fiṭr taqwī complément déclaré", "complément imprimé dégradé, déclaré non restituable" in hn)
chk("ǧumhūr fût-il robuste", "fût-il robuste (wa-in kāna qawiyyan)" in hn)
chk("ʿĀʾiša ne tenait pas", "ne tenait pas (lā tarā) la rupture du jeûne recommandable" in hn)
chk("1101 al-Qāsim poussée du départ", "dans la poussée du départ de l’imām (yadfaʿu l-imām — leçon de l’image r667)" in hn)
chk("1101 blanchir + boisson", "yubayyaḍa mā bayna-hā wa-bayna n-nāsi min al-arḍ" in hn and "tadʿū bi-šarābin" in hn)
chk("1101 permission + facilitation", "comme permission" in hn and "facilitation pour les gens (wa-t-tas-hīli ʿalā n-nās)" in hn)

# --- 14) fiqh : la prière et la sermon ---
chk("ẓuhr voix basse + siriyya", "récite pas à voix haute (lā yuǧharu l-imāmu bi-l-qirāʾa)" in hn and "(li-anna ẓ-ẓuhr siriyya" in hn)
chk("Namīra + enseignement", "wa-yakhṭibu n-nāsa bi-ǧāmiʿi Namīra" in hn and "ce qu’ils feront ensuite" in hn)
chk("1190 pas de divergence", "sur quoi il n’y a pas de divergence" in hn and "n’est que ẓuhr (innamā hiya ẓuhr)" in hn)
chk("1190 écourtée voyage", "écourtée toutefois (wa-lākinna-hā quṣirat) en raison du voyage (min aǧli s-safar)" in hn)
chk("1190 pas de vendredi voyageur", "il n’y a pas de vendredi pour le voyageur (li-anna-hu lā ǧumʿata ʿalā musāfir)" in hn)
chk("1191 aucun groupement", "il n’y a pas lieu de groupement (inna-hu lā yuǧmaʿu)" in hn)
chk("1191 sens confirmé par leçon 14", "la description du ǧamʿ et sa cause" in hn and "confirme le sens de l’intérieur du manuel" in hn)
chk("hâte + brièveté = sunna", "que la hâte de la prière et son écourtement" in hn and "la brièveté de la sermon" in hn)
chk("unité + égalité", "dīnu l-waḥda" in hn and "les plus hautes manifestations de l’unité et de l’égalité entre les gens" in hn)

# --- 15) taqwīm + istitmār + iʿdād ---
chk("taqwīm item 1 jeûne + preuve", "quel est le jugement (mā l-ḥukmu) du jeûne du pèlerin (ṣawmi l-ḥāǧǧ) à ʿArafa, avec preuve" in hn)
chk("taqwīm cas 1 avant coucher (r669-e)", "puis s’en est retourné (raǧulun waqafa bi-ʿArafa ṯumma n-ṣarafa) avant le coucher du soleil" in hn and "second cas récupéré sur l’image" in hn)
chk("taqwīm cas 2 impureté", "(raǧulun waqafa bi-ʿArafa ġayra ṭāhir)" in hn)
chk("taqwīm réponses", "ne serait-ce qu’un bref moment" in hn and "rien ne pèse sur lui" in hn)
chk("istitmār 1270 chaîne", "Ibrāhīm b. ʿAbd Allāh b. Abī ʿAbla" in hn)
chk("istitmār quatre épithètes", "plus petit (aṣġa" in hn and "(adḥara" in hn and "(aḥqara" in hn and "(aġyaẓa" in hn)
chk("istitmār miséricorde + Badr", "la descente de la miséricorde (li-mā raʾā min tanazzuli r-raḥma)" in hn and "excepté (illā) ce qu’il vit le jour de Badr" in hn)
chk("istitmār Ǧibrīl rangeant", "Ǧibrīl rangeant les anges (Ǧibrīla yazaʿu l-malāʾika)" in hn)
chk("istitmār consigne famille", "je le répands au sein de ma famille (wa-ušīʿu ḏālika bayna ʿāʾilatī)" in hn)
chk("iʿdād mabīt Muzdalifa", "du repos de la nuit (ḥukma l-mabīt) et du stationnement (wa-l-wuqūf) à Muzdalifa" in hn)
chk("iʿdād ǧamʿ + cause", "la description de la prière réunie (ṣifata l-ǧamʿ)" in hn and "sa cause (wa-sababa-hu)" in hn)
chk("iʿdād contrepoint 1191", "nul ǧamʿ (n° 1191) — à Muzdalifa, le ǧamʿ décrit et motivé" in hn)

# --- 16) apparat ---
chk("apparat bornes p.90/p.96", "ouverture p.90 (bannière" in hn and "clôture p.96" in hn)
chk("apparat p.97 exclusive cours 14 registre", "p.97 = bannière du cours 14" in hn and "borne supérieure exclusive, jamais devinée" in hn)
chk("apparat jonction p.89 convergence", "jonction p.89 = clôture du cours 12" in hn and "convergence de bornes" in hn)
chk("apparat couches R667/R669", "R667" in hn and "R669" in hn and "_r669-adjud2.json" in hn)
chk("apparat numéros votes consignés", "votes de chiffres" in hn and "artefact de cadre, récusée" in hn)
chk("apparat adjudications majeures ×4", "matn complet du n° 1188" in hn and "r669-d p.94" in hn and "r669-e p.95" in hn)
chk("apparat segments dégradés déclarés", "segments imprimés dégradés non restituables déclarés" in hn)
chk("apparat écarts consignés", "note croisée du Ṣaḥīḥ Muslim" in hn and "adḥar/adḥkar" in hn and "aḥqar/aḥfar" in hn)
chk("apparat ZÉRO āya / zéro cache", "ZÉRO citation coranique" in hn and "aucun recours au cache" in hn)
chk("apparat GARDE-DOUBLON + machine", "GARDE-DOUBLON" in hn and "superviseur vivant" in hn and "portail :3000 OUVERT" in hn)
chk("apparat PARALLÈLE slot 403 next", "pdf-mut23h2x-403" in hn and "htmlFr vide pour le prochain ouvrier" in hn)
chk("apparat R671 et suivants", "R671 et suivants" in hn)

# --- 17) 0 arabe script, apostrophes, appariement ---
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", h)
chk("0 caractère arabe", len(arab) == 0)
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("h1 unique", h.count("<h1>") == 1)

# --- 18) registre (avant hand-set : slot vide ; après : htmlFr présent) ---
try:
    reg = json.load(open(REG, encoding="utf-8"))
    lessons = reg if isinstance(reg, list) else reg.get("lessons", [])
    slot = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-402"), None)
    if slot and slot.get("htmlFr"):
        chk("registre htmlFr 402 rempli", len(slot["htmlFr"]) > 15000)
        chk("titleFr pré-mappé intact", slot.get("titleFr", "").startswith("Les rites du jour de ʿArafa"))
        voisins = [l.get("docId") for l in lessons if l.get("docId") in ("pdf-mut23h2x-401", "pdf-mut23h2x-403")]
        chk("voisins 401/403 présents", "pdf-mut23h2x-401" in voisins and "pdf-mut23h2x-403" in voisins)
        v401 = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-401"), None)
        chk("htmlFr 401 intact (R668)", v401 is not None and len(v401.get("htmlFr") or "") == 36732)
        v403 = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-403"), None)
        chk("htmlFr 403 jamais écrit par ce worker", v403 is not None and not v403.get("htmlFr"))
        sav = json.load(open(SAV, encoding="utf-8"))
        savh = sav.get("hand", {})
        chk("savant-registry 402 posé", "pdf-mut23h2x-402" in json.dumps(savh))
    else:
        chk("registre 402 encore vide (pré-hand-set)", slot is None or not slot.get("htmlFr"))
except Exception as e:
    chk(f"registres lisibles ({e})", False)

print(f"\nverify-hadith3-pdf402 : {ok} OK / {fail} échec(s)")
raise SystemExit(1 if fail else 0)