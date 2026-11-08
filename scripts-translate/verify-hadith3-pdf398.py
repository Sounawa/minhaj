# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-398
(al-ʿaǧz wa-l-iḥṣār ʿan al-ḥaǧǧ — leçon 9, p.65-70 du manuel
hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé 29 slots
pdf-mut23h2x-390..418) : bornes p.65-70 (bannière leçon 9 au médaillon lue
p.65 par image 300 dpi ; bannière « leçon 10 — aḥkām aṭ-ṭawāf (1) » avec
objectifs propres lue p.71 par image → borne supérieure exclusive, la p.70 ne
portant que questions de révision et préparation) ; dix numéros du Muwaṭṭaʾ
tranchés (1041, 1042, 1043, 1044, 1045 ×2 occurrences, 1046, 1047, 1051,
1052, 1269 — inversions OCR par paires systématiquement documentées) ; deux
āya rendues du cache coranique (Āl ʿImrān 97 — numérotation alignée ;
Génisse marque imprimée 195 = cache 196, écart warš/ḥafṣ −1 propre à la
sourate, documenté) ; adjudications par preuve d’image (chiffres de la notice
d’Ibn ʿAbbās 68 H / 71-72 ans ; noms Abū Ayyūb al-Anṣārī et Habār b.
al-Aswad ; litière miḥaffa confirmée par la question p.70 ; lettre non
pointée du mot « consacré » dans la parole d’ʿĀʾiša contre la couche texte) ;
honnêtetés résiduelles documentées (clause médiane de l’ordre de ʿUmar ;
instabilité thuluth du fragment de la Génisse) ; rasm nu interdit, double
rendu interdit (āya d’Āl ʿImrān convoquée une fois intégralement puis par
référence) ; 0 arabe, 0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf398.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-398-fr.html"
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
chk("h1 Leçon 9", "<h1>Leçon 9" in hn and "al-ʿaǧz wa-l-iḥṣār ʿan al-ḥaǧǧ" in hn)
chk("h1 titleFr registre", "l’incapacité et l’empêchement d’accomplir le pèlerinage" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.65-70", "p.65-70" in hn)
chk("meta slot 398", "pdf-mut23h2x-398" in hn)
chk("meta voisins 397/399 livrés", "pdf-mut23h2x-397" in hn and "pdf-mut23h2x-399" in hn and "déjà livrées au registre" in hn)
chk("meta borne sup preuve image leçon 10 p.71", "bannière du dixième cours" in hn and "leçon 10" in hn and "page 71" in hn)
chk("meta 196 pages + source PDF", "hadith-3-iadadi_text.pdf" in hn and "196 pages" in hn)
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

# --- 2) les deux objectifs ---
chk("obj 1 substitution", "que je connaisse le statut de la substitution (istināba) dans le pèlerinage obligatoire" in hn)
chk("obj 2 empêchement", "que je saisisse les statuts et les figures de l’empêchement (iḥṣār) du pèlerinage" in hn)

# --- 3) tamhīd : trois genres d'adoration ---
chk("tamhīd pur corps — prière et jeûne", "une adoration de pur corps, dans laquelle la substitution est écartée, comme la prière et le jeûne" in hn)
chk("tamhīd pur argent — zakāt", "une adoration de pur argent, dans laquelle la substitution est permise, comme la dîme de la zakāt et l’aumône" in hn)
chk("tamhīd mixte — pèlerinage", "une adoration qui réunit l’argent et le corps : le pèlerinage" in hn)
chk("tamhīd double question", "Quel est donc le statut de la substitution dans le pèlerinage ? Et quel est le statut de celui que l’empêchement saisit dans le pèlerinage ?" in hn)

# --- 4) les numéros tranchés ---
for num in ("1041", "1042", "1043", "1044", "1045", "1046", "1047", "1051", "1052", "1269"):
    chk(f"numéro {num} présent", num in hn)
chk("1045 deux occurrences", hn.count("n° 1045") >= 2 or ("n° 1045" in hn and "même numéro que la position précédente" in hn))
for inv in ("1401", "2401", "3401", "4401", "5401", "6401", "7401", "1501", "2501", "9621"):
    chk(f"inversion OCR « {inv} » documentée", inv in hn)

# --- 5) texte 1041 (la Khathʿamiyya) ---
chk("1041 chaîne Sulaymān b. Yasār", "d’après Ibn Šihāb (az-Zuhrī), d’après Sulaymān b. Yasār, d’après ʿAbd Allāh b. ʿAbbās" in hn)
chk("1041 al-Faḍl en croupe", "al-Faḍl b. ʿAbbās était en croupe du Messager de Dieu" in hn)
chk("1041 détourne le visage", "tourna le visage d’al-Faḍl vers l’autre joue" in hn)
chk("1041 vieillard en selle", "un très vieillard qui ne peut se tenir fermement en selle" in hn)
chk("1041 Oui + Pèlerinage d’Adieu", "Il dit : « Oui ». Et c’était lors du Pèlerinage d’Adieu" in hn.replace("  »", " »") or "« Oui »" in hn and "Pèlerinage d’Adieu" in hn)

# --- 6) texte 1043 (Ḥudaybiyya) ---
chk("1043 il lui fut transmis", "Mālik relate qu’il lui fut transmis" in hn)
chk("1043 désacralisation", "se désacralisa, lui et ses Compagnons, à Ḥudaybiyya" in hn)
chk("1043 avant la circumambulation", "libérés de toute interdiction avant de tourner autour de la Maison" in hn)
chk("1043 sans rien reprendre", "n’ordonna à aucun de ses Compagnons" in hn and "de rien reprendre" in hn)

# --- 7) texte 1046 (empêché malade) ---
chk("1046 chaîne Sālim/Ibn ʿUmar", "d’après Sālim b. ʿAbd Allāh, d’après ʿAbd Allāh b. ʿUmar" in hn)
chk("1046 non délié jusqu'à ṭawāf+saʿy", "ne sera pas délié jusqu’à ce qu’il tourne autour de la Maison et parcoure entre Ṣafā et Marwa" in hn)
chk("1046 vêtement/remède + rachat", "contraint de porter un des vêtements qu’il ne peut éviter, ou le remède, qu’il le fasse et se rachète" in hn)

# --- 8) notice Ibn ʿAbbās ---
chk("notice nasab complet", "ʿAbd Allāh b. al-ʿAbbās b. ʿAbd al-Muṭṭalib al-Hāšimī" in hn)
chk("notice cousin + tarǧumān", "cousin du Messager de Dieu" in hn and "traducteur du Coran (tarǧumān al-Qurʾān)" in hn)
chk("notice ḥibr + baḥr", "l’érudit et l’océan (al-ḥibr wa-l-baḥr)" in hn)
chk("notice invocation sagesse", "le Prophète invoqua pour lui la sagesse" in hn)
chk("notice mort Ṭāʾif 68 H", "il mourut à Ṭāʾif l’an 68 de l’hégire" in hn.replace("Il mourut", "il mourut") or "mourut à Ṭāʾif l’an 68" in hn)
chk("notice âge 71-72", "âgé de 71 ou 72 ans" in hn)
chk("notice chiffres adjudiqués par image", "adjudication dédiée" in hn and "« 86 » pour 68" in hn)

# --- 9) glose ---
chk("glose al-muḥṣar", "al-muḥṣar — l’entravé : l’enfermé et l’empêché de se rendre au pèlerinage" in hn)
chk("glose unique documentée", "cette seule glose" in hn)

# --- 10) istiḫlāṣ 3 items ---
chk("istiḫlāṣ item 1 substitution", "quel est le statut de la substitution dans le pèlerinage ?" in hn)
chk("istiḫlāṣ item 2 par ennemi", "celui que l’empêchement a saisi du pèlerinage par (la cause d’) un ennemi" in hn)
chk("istiḫlāṣ item 3 sans ennemi", "qu’incombe-t-il à celui que l’empêchement a saisi du pèlerinage sans ennemi ?" in hn)

# --- 11) fiqh : premièrement (substitution) ---
chk("le Oui emporte la validité", "emporte la validité de la substitution dans le pèlerinage obligatoire au profit de l’incapable" in hn)
chk("ʿIyāḍ pas de preuve", "il n’y a pas là de preuve" in hn and "lā ḥuǧǧa fīhi" in hn)
chk("ʿIyāḍ capacité", "le pèlerinage est devenu obligatoire sous la condition de la capacité (istīṭāʿa)" in hn)
chk("version accomplis-le pour lui = nadb", "accomplis-le pour lui" in hn and "guidance et de recommandation (nadb)" in hn)
chk("Ibn ʿAbd al-Barr spécificité", "Ibn ʿAbd al-Barr tient le hadith de la femme de Ḫuṯʿam pour propre à elle" in hn)
chk("Mālik et ses compagnons", "Mālik et ses compagnons" in hn)
chk("principe du qiyās", "ne point s’écarter des normes de l’analogie" in hn)

# --- 12) les deux āya (cache, écart documenté) ---
chk("āya ʿImrān rendue du cache", "Là sont des signes évidents, parmi lesquels l’endroit où Abraham s’est tenu debout" in hn)
chk("āya ʿImrān capacité rendue", "c’est un devoir envers Allah pour les gens qui ont les moyens, d’aller faire le pèlerinage de la Maison" in hn)
chk("āya ʿImrān numérotation alignée", "famille de ʿImrān, marque imprimée « āya 97 », coïncidant avec le comptage du cache" in hn)
chk("āya ʿImrān un seul rendu + renvoi", "convoqué une seule fois, intégralement" in hn and "re-convoqueront par référence" in hn)
chk("āya Génisse clause d'empêchement", "Et si vous en êtes empêchés, alors faites un sacrifice qui vous soit facile" in hn)
chk("āya Génisse marque 195 = cache 196", "marque imprimée du manuel « āya 195 », c’est-à-dire l’āya 196 du comptage du cache" in hn)
chk("écart warš/ḥafṣ documenté (sens inverse Table)", "écart de numérotation warš/ḥafṣ propre à cette sourate" in hn and "sens inverse sur la Table (97 imprimé pour 95 du cache)" in hn)
chk("écart documenté sourate par sourate", "l’écart se documente sourate par sourate, jamais ne se devine" in hn)
chk("instabilité thuluth documentée", "instabilité de lecture du fragment thuluth est documentée" in hn)
chk("quand vous êtes en sécurité", "quand vous êtes en sécurité" in hn)

# --- 13) fiqh : deuxièmement (empêchement) ---
chk("règle de partage deux causes", "le statut de l’empêchement du pèlerinage varie selon sa cause" in hn)
chk("ennemi : déliaison sur place", "il se délie sur place de toutes les interdictions de la consécration" in hn)
chk("1042 citation Mālik", "quiconque est retenu par un ennemi qui se dresse entre lui et la Maison se délie de toute chose" in hn)
chk("1044 commandement un", "leur commandement n’est qu’un" in hn and "visant le pèlerinage et la ʿumra" in hn)
chk("1045 position Mālik", "telle est notre position sur l’empêché par ennemi" in hn)
chk("sans ennemi : qu'à la Maison", "ne se délie qu’à la Maison" in hn)
chk("1045 bis citation", "quant à celui que l’empêchement a saisi sans ennemi, il ne sera pas délié en deçà de la Maison" in hn)
chk("sécurité contre l'ennemi", "la législation de la déliaison visait la réalisation de la sécurité contre l’ennemi" in hn)
chk("ni dalāla ni qiyās", "on ne l’y agrège ni par indicatif (dalāla) ni par analogie (qiyās)" in hn)
chk("à rebours de l'analogie", "procède à rebours de l’analogie (ʿalā ḫilāf al-qiyās)" in hn)
chk("ʿĀʾiša citation + ḥ adjudiqué", "le consacré — seule la Maison le délie" in hn and "la lecture d’image du mot à fort grossissement a tranché" in hn)

# --- 14) figures + ʿUmar + Mālik 1052 ---
chk("figures : comput, croissant, fracture", "l’erreur sur le comput (du mois), l’occultation du croissant, la fracture d’un membre" in hn)
chk("figures : diarrhée, enfantement, ʿArafa", "la diarrhée et la douleur du ventre, l’enfantement" in hn and "empêche du stationnement à ʿArafa" in hn)
chk("figure : pèlerinage manqué + jour du Sacrifice", "celui à qui le pèlerinage échappe puis qui arrive au jour du Sacrifice" in hn)
chk("1051 ʿUmar ordonne", "ʿUmar b. al-Ḫaṭṭāb ordonna à Abū Ayyūb al-Anṣārī et à Habār b. al-Aswad" in hn)
chk("1051 noms par preuve d'image", "établis par preuve d’image" in hn and "confirmé par la lecture zoomée" in hn)
chk("1051 déliaison par ʿumra + rattrapage", "de se délier par une ʿumra, puis de rentrer libérés de toute interdiction, puis d’accomplir le pèlerinage l’année suivante avec la bête d’offrande" in hn)
chk("1051 jeûne 3+7", "trois jours de jeûne dans le pèlerinage et sept lorsqu’il rentre auprès des siens" in hn)
chk("1051 clause médiane honnête", "incertitude résiduelle honnêtement documentée" in hn)
chk("1052 citation Mālik", "par maladie, ou par sa monture, ou par erreur sur le comput, ou occultation du croissant : c’est un empêché, à sa charge ce qui incombe à l’empêché" in hn)

# --- 15) taqwīm + istiṯmār + iʿdād ---
chk("taqwīm accord verset/hadith", "la voie des mālikites pour accorder le verset qui conditionne l’obligation du pèlerinage à la capacité et le hadith de la femme de Ḫuṯʿam" in hn)
chk("taqwīm évanissement ʿArafa", "un consacré par pèlerinage que frappe un évanissement empêchant d’atteindre ʿArafa" in hn)
chk("taqwīm ʿumra empêchée", "un homme consacré par ʿumra, puis empêché d’atteindre la Maison" in hn)
chk("istiṯmār chaîne Krayb", "d’après Ibrāhīm b. ʿUqba, d’après Krayb, l’affranchi (mawlā) d’Ibn ʿAbbās" in hn)
chk("istiṯmār litière", "elle était dans sa litière (miḥaffa)" in hn)
chk("istiṯmār enfant par les aisselles", "saisit alors un enfant par les aisselles" in hn)
chk("istiṯmār Oui et tu as salaire", "Oui, et tu as salaire" in hn)
chk("istiṯmār litière doublement confirmée", "confirmée doublement" in hn and "par la question de révision imprimée p.70" in hn)
chk("istiṯmār questions de révision", "expliquer les deux syntagmes de la scène, puis statuer sur le statut du pèlerinage de l’enfant" in hn)
chk("iʿdād ʿAbd ar-Raḥmān b. ʿAbd al-Qārī", "je fais connaissance de ʿAbd ar-Raḥmān b. ʿAbd al-Qārī" in hn)
chk("iʿdād circuits + ʿasr", "une partie des circuits de la circumambulation, puis fut interpellé par l’imposition de la prière de l’après-midi" in hn)
chk("iʿdād bannière leçon 10 lue p.71", "bannière « leçon 10 — les règles de la circumambulation (1) »" in hn)

# --- 16) apparat ---
chk("apparat bornes preuve image", "preuve d’image : bannière au médaillon du neuvième cours lue p.65" in hn)
chk("apparat bannière leçon 10 p.71", "bannière « leçon 10 — les règles de la circumambulation (1) » avec objectifs propres lue p.71" in hn)
chk("apparat couches + zooms", "couches texte du PDF recoupées" in hn and "zooms 4-16× par boîtes de lignes et par mots" in hn)
chk("apparat dix numéros + inversions", "1041 (« 1401 »)" in hn and "1269 (« 9621 »)" in hn)
chk("apparat adjudications image ×4", "les chiffres de la notice d’Ibn ʿAbbās (68 H ; 71-72 ans), les noms Abū Ayyūb al-Anṣārī et Habār b. al-Aswad, la litière (miḥaffa)" in hn)
chk("apparat 0 arabe 0 apostrophe", "zéro caractère arabe, zéro apostrophe droite, guillemets français appariés" in hn)
chk("apparat voisins intacts", "slot pdf-mut23h2x-398 du livre hadith-3es rempli (leçons voisines 397 et 399 intactes" in hn)
chk("apparat PDF source suivi git", "exclusivement sur le PDF source déposé au dépôt (hadith-3-iadadi_text.pdf, suivi par git)" in hn)

# --- 17) 0 arabe script, rasm nu, doublons ---
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", h)
chk("0 caractère arabe", len(arab) == 0)
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("h1 unique", h.count("<h1>") == 1)

# --- 18) registre (avant hand-set : slot vide ; après : htmlFr présent) ---
try:
    reg = json.load(open(REG, encoding="utf-8"))
    lessons = reg if isinstance(reg, list) else reg.get("lessons", [])
    slot = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-398"), None)
    if slot and slot.get("htmlFr"):
        chk("registre htmlFr 398 rempli", len(slot["htmlFr"]) > 15000)
        sav = json.load(open(SAV, encoding="utf-8"))
        savh = sav.get("hand", {})
        chk("savant-registry 398 posé", "pdf-mut23h2x-398" in json.dumps(savh))
    else:
        chk("registre 398 encore vide (pré-hand-set)", slot is None or not slot.get("htmlFr"))
except Exception as e:
    chk(f"registres lisibles ({e})", False)

print(f"\nverify-hadith3-pdf398 : {ok} OK / {fail} échec(s)")
raise SystemExit(1 if fail else 0)
