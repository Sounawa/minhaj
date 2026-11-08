# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-399
(aḥkām aṭ-ṭawāf (1) — الدرس 10, p.71-77 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) : bornes
p.71-77 (bannière الدرس العاشر p.71, médaillon 10, lu par image 600 dpi ;
p.78 = bannière الدرس الحادي عشر médaillon 11 = borne supérieure exclusive,
couches + bandes + onze lectures VLM R647 réexploitées) ; 14 numéros de
référence tranchés (1059, 1065, 1067, 1075, 1060, 1061, 1063, 1068, 1066,
1064, 1079, 1078, 1056, réf. Fatḥ al-Bārī /4/270) ; double chaîne du 1075
(p.72 Ibn Shihāb/Ḥumayd b. ʿAbd ar-Raḥmān b. ʿAwf ; p.75 ʿAbd ar-Raḥmān b.
ʿAbd al-Qārī) rendue telle qu'imprimée ; honnêteté d'apparat ×9 (fin bi-baladin,
fin glose istilām, milieu ḏū Ṭuwā, verbe de l'allée pressée, suite du duʿā
couverte par bandeau, commentaire d'ʿUmar, milieu du 1064, fin du 1078, duel
du 1056, première recherche d'iʿdād) ; ZÉRO āya (cache coranique non sollicité),
rasm nu interdit, double rendu interdit (1065/1067 re-cités au fiqh par renvoi,
matn du 1075 du fiqh en prose de renvoi) ; 0 arabe, 0 apostrophe droite,
0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf399.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-399-fr.html"
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
chk("h1 Leçon 10", "<h1>Leçon 10" in hn and "aḥkām aṭ-ṭawāf" in hn)
chk("h1 titleFr registre", "les règles de la circumambulation (ṭawāf) (1)" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.71-77", "p.71-77" in hn)
chk("meta trace tick job", "1a19c7c0ffb4f845-cron-agent-loop-202611081822" in hn and "18h22" in hn and "496554" in hn)
chk("meta takeover + R508-bis", "takeover" in hn and "R508-bis" in hn)
chk("meta voisins 397/398/uh2 269-271", "pdf-mut23h2x-397" in hn and "pdf-mut23h2x-398" in hn and ("uh2-pdf-mut23h2u-269/270/271" in hn or "uh2-pdf-mut23h2u-271" in hn))
chk("meta titre bannière", "aḥkām aṭ-ṭawāf (1)" in hn)
chk("meta p.78 exclusive", "borne supérieure exclusive" in hn and "médaillon «&nbsp;&nbsp;11&nbsp;»" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "médaillon « 11 »" in hn or "«&nbsp;11&nbsp;»" in hn)
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
chk("obj 1 istilām Pierre noire", "les jugements de l’istilām de la Pierre noire" in hn)
chk("obj 2 jugement et moment des deux rakʿa", "le jugement et le moment de la prière des deux rakʿa du ṭawāf" in hn)
chk("obj 3 grandeur du ṭawāf", "saisir la grandeur de l’adoration du ṭawāf et la finalité de l’istilām du coin noir" in hn)

# --- 3) tamhīd ---
chk("tamhīd adoration du consacré", "Le ṭawāf est une adoration que le consacré accomplit" in hn)
chk("tamhīd qibla des musulmans", "la qibla des musulmans" in hn)
chk("tamhīd sept tours façon particulière", "en sept tours, selon une façon particulière" in hn)
chk("tamhīd questions d’ouverture", "Quels sont donc les jugements du ṭawāf" in hn and "comment salue-t-on le coin noir et le coin yéménite" in hn)

# --- 4) les numéros tranchés ---
for num in ("1059", "1065", "1067", "1075", "1060", "1061", "1063", "1066", "1068", "1064", "1079", "1078", "1056", "/4/270", "78"):
    chk(f"numéro {num} présent", num in hn)

# --- 5) texte 1059 (Jābir, raml) ---
chk("1059 Jābir vu le Messager", "J’ai vu le Messager de Dieu faire le raml depuis la Pierre noire" in hn)
chk("1059 trois tours", "jusqu’à ce qu’il parvînt au terme de trois tours" in hn)
chk("1059 remarque Mālik cité", "l’ordre que les gens de science n’ont pas observé dans une cité" in hn)
chk("1059 bi-baladin dégradé documenté", "bi-baladin" in hn and "dégradée aux couches, le sens rendu au plus sûr" in hn)
chk("1059 chaîne dégradée documentée", "chaîne imprimés de façon dégradée, restitués au plus sûr des couches" in hn)

# --- 6) texte 1065 (ʿAwf) ---
chk("1065 question du Prophète", "Qu’as-tu fait, ô Abū Muḥammad, dans l’istilām du coin" in hn)
chk("1065 réponse", "Je l’ai salué et je l’ai délaissé" in hn)
chk("1065 aṣabta", "Tu es droit (aṣabta)" in hn)

# --- 7) texte 1067 (ʿUmar à la pierre) ---
chk("1067 tu n’es qu’une pierre", "Tu n’es qu’une pierre" in hn)
chk("1067 vu le Messager t’embrasser", "si je n’avais pas vu le Messager de Dieu t’embrasser, je ne t’aurais pas embrassé" in hn)
chk("1067 puis il l’embrassa", "puis il l’embrassa" in hn)
chk("1067 cœur théologique", "aucun pouvoir, aucun effet ne lui est prêté" in hn)

# --- 8) texte 1075 (ʿUmar après l’aube) ---
chk("1075 Ḥumayd", "d’après Ḥumayd b. ʿAbd ar-Raḥmān b. ʿAwf" in hn)
chk("1075 après la prière de l’aube", "avec ʿUmar b. al-Ḫaṭṭāb après la prière de l’aube" in hn)
chk("1075 ne vit pas le soleil", "il regarda et ne vit pas le soleil" in hn)
chk("1075 Ḏū Ṭuwā", "Ḏū Ṭuwā" in hn)
chk("1075 deux rakʿa", "puis il pria deux rakʿa" in hn)
chk("1075 verbe dégradé documenté", "verbe de l’étape imprimé à Ḏū Ṭuwā est dégradé" in hn)
chk("1075 double chaîne documentée", "la chaîne imprimée de cette page diffère de celle de la rubrique du fiqh" in hn)
chk("1075 seconde chaîne au fiqh", "d’après ʿAbd ar-Raḥmān b. ʿAbd al-Qārī" in hn)

# --- 9) notice transmetteur ---
chk("tarǧama Jābir nasab", "Jābir b. ʿAbd Allāh b. ʿAmr b. Ḥarām b. Ṯaʿlaba al-Anṣārī al-Ḫazraǧī" in hn)
chk("tarǧama fils de son compagnon", "compagnon du Messager de Dieu et fils de son compagnon" in hn)
chk("tarǧama mukṯirūn", "grands rapporteurs (al-mukṯirūn)" in hn)
chk("tarǧama ʿAqaba", "parmi ceux qui assistèrent à ʿAqaba" in hn)
chk("tarǧama mort 78 chiffres", "il mourut en l’an 78 de l’Hégire" in hn and "lue chiffre par chiffre (7, 8)" in hn)

# --- 10) gloses ---
chk("glose istilām iftiʿāl", "du schème dérivatif iftiʿāl sur as-salām&nbsp; : la salutation" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "du schème dérivatif iftiʿāl sur as-salām : la salutation" in hn)
chk("glose istilām taslīm + fin suspendue", "certains disent&nbsp; : de at-taslīm" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "certains disent : de at-taslīm" in hn)
chk("glose istilām fin dégradée", "la fin de la glose imprimée est dégradée aux deux couches" in hn)
chk("glose raml", "accélérer la marche en rapprochant les pas" in hn)
chk("glose anāḫa chameaux", "il fit reposer (sa monture)" in hn and "il les fit agenouiller et ils s’agenouillèrent" in hn)
chk("glose ḏū Ṭuwā lieu", "un lieu proche de la Mecque" in hn and "le milieu de la glose (le dérivé imprimé de la lettre ṭāʾ) est dégradé" in hn)

# --- 11) istiḫlāṣ ---
chk("istiḫlāṣ item 1 raml", "j’explique le jugement du raml dans le ṭawāf" in hn)
chk("istiḫlāṣ item 2 coins", "quels sont les coins que l’on salue dans le ṭawāf" in hn)
chk("istiḫlāṣ item 3 quand rakʿa", "quand le ṭāʾif prie-t-il les deux rakʿa du ṭawāf" in hn)

# --- 12) fiqh : premièrement (raml) ---
chk("Bukhārī trois tours pressés quatre", "il allait d’un pas pressé trois tours et marchait quatre" in hn)
chk("Bukhārī verbe dégradé documenté", "le verbe imprimé de l’allée est dégradé entre les couches et l’image" in hn)
chk("deux fils d’az-Zubayr", "les deux fils d’az-Zubayr, ʿAbd Allāh et ʿUrwa" in hn)
chk("1060 Pierre à Pierre", "il faisait le raml de la Pierre noire à la Pierre noire, trois tours, et marchait quatre tours" in hn)
chk("1061 ʿUrwa duʿā", "Maître, donne-nous la bonne en ce bas-monde et la bonne dans l’au-delà" in hn)
chk("1061 duʿā suite couverte bandeau", "couverte par le bandeau décoratif de l’image et dégradée aux couches, suspendue, jamais devinée" in hn)
chk("1061 sans occuper les gens", "sans occuper les gens en les faisant entendre sa voix" in hn)
chk("Mālik raml sunna dans les trois", "le raml est une sunna dans les trois [premiers tours]" in hn)
chk("délaissé délibérément ne reprend pas", "ne la reprend pas sur le reste des tours" in hn)
chk("Ibn ʿAbbās seul divergé", "seul Ibn ʿAbbās — que Dieu l’agrée — a divergé sur ce point" in hn)
chk("Fatḥ al-Bārī /4/270", "Fatḥ al-Bārī d’Ibn Ḥaǧar, /4/270" in hn)
chk("Ibn Ḥaǧar quiconque veut", "quiconque veut fait le raml et quiconque veut ne le fait pas" in hn)
chk("exception mecquoise", "celui qui se consacre depuis la Mecque&nbsp; : le raml ne lui est pas recommandé" in hn.replace("&nbsp; ", "&nbsp;&nbsp;") or "celui qui se consacre depuis la Mecque : le raml ne lui est pas recommandé" in hn)
chk("1063 Ibn ʿUmar limite", "il ne faisait le raml que pour un ṭawāf autour de la Maison quand il se consacrait depuis la Mecque" in hn)

# --- 13) fiqh : deuxièmement (istilām) ---
chk("baiser coin noir capacité", "d’embrasser le coin noir pour qui en a la capacité" in hn)
chk("créature ne nuit ne profite", "c’est une créature qui ne nuit et ne profite pas" in hn)
chk("1067 re-cité par renvoi", "texte déjà rendu au troisième texte (n° 1067, renvoi, jamais re-traduit)" in hn)
chk("suivre requis même si sens échappe", "suivre le Prophète est requis même quand le sens échappe à l’intelligence" in hn)
chk("yéménite main bouche sans baiser", "la main y est posée, puis portée à la bouche sans baiser" in hn)
chk("1068 Mālik relève sa main", "lorsque celui qui tourne autour de la Maison relève sa main du coin yéménite, il la pose sur sa bouche" in hn)
chk("bousculade toucher main", "si l’on est bousculé loin du baiser, on le touche de la main" in hn)
chk("bousculade de loin sans nuire", "si la main ne peut atteindre, alors de loin — si cela ne nuit à personne" in hn)
chk("pas de bousculade", "l’on ne se bouscule pas pour saluer le coin" in hn)
chk("ʿAwf saluait de face takbīr", "il le saluait de face, prononçait la grandeur (le takbīr) et invoquait" in hn)
chk("ʿAwf khalwa", "s’il trouvait un moment dégagé il le saluait" in hn)
chk("1065 renvoi au fiqh", "la scène entière déjà rendue au deuxième texte (n° 1065, renvoi)" in hn)
chk("ǧumhūr deux coins", "aucun coin n’est salué hormis le coin noir et le yéménite" in hn)
chk("coins syriens non salués", "les deux coins syriens ne sont pas salués" in hn)
chk("1066 ʿUrwa tous les coins", "saluait tous les coins" in hn)
chk("1066 yéménite sauf empêché", "il ne délaissait pas le yéménite — sauf s’il en était empêché" in hn)
chk("az-Zubayr fondations Ismaïl", "acheva la Maison sur les fondations d’Ismaïl" in hn)
chk("az-Zubayr jusqu’à tué", "la chose demeura ainsi jusqu’à ce qu’ʿAbd Allāh fût tué" in hn)
chk("1064 après rakʿa avant Ṣafā", "après l’accomplissement du ṭawāf et de la prière des deux rakʿa, avant de sortir vers aṣ-Ṣafā" in hn)
chk("1064 milieu dégradé documenté", "le milieu du hadith imprimé de façon dégradée entre les couches, sens rendu" in hn)
chk("1064 sans nuire", "sans nuire à soi-même ni à autrui" in hn)

# --- 14) fiqh : troisièmement (rakʿa) ---
chk("ʿUmar nafl après aube", "n’aimait pas la prière surérogatoire après la prière de l’aube avant que le soleil se fût levé" in hn)
chk("1075 renvoi prose", "revient ici sous une seconde chaîne imprimée" in hn)
chk("Mālik tour unique", "fasse un ṭawāf unique après l’aube et après l’asr" in hn)
chk("Mākrit rien au-delà des sept", "sans y ajouter un seul tour au-delà des sept" in hn)
chk("Mālik retarder jusqu’au lever", "il retarde les deux rakʿa jusqu’à ce que le soleil se lève, comme l’a fait ʿUmar b. al-Ḫaṭṭāb" in hn)
chk("1079 après asr coucher", "les retarde après l’asr jusqu’à ce que le soleil se couche" in hn)
chk("1079 maghrib", "ou les retarde jusqu’à la prière du maghrib" in hn)
chk("1078 iqāma", "si la prière de l’aube ou de l’asr est convoquée et que le ṭāʾif n’a pas achevé ses sept tours" in hn)
chk("1078 prier avec l’imām puis achever", "s’il prie avec l’imām, il achève ensuite le reste de ses tours" in hn)
chk("1078 fin dégradée documentée", "la fin du jugement imprimée de façon dégradée" in hn)

# --- 15) taqwīm + istiṯmār + iʿdād ---
chk("taqwīm bousculade", "j’explique le jugement de la bousculade sur l’istilām du coin" in hn)
chk("taqwīm coin yéménite", "comment salue-t-on le coin yéménite" in hn)
chk("taqwīm prière convoquée sept", "n’a pas achevé ses sept tours" in hn)
chk("taqwīm trois items testent", "la foule (jusqu’où le corps peut céder sans renoncer au salut)" in hn)
chk("istiṯmār 1056 N’as-tu pas vu", "N’as-tu pas vu que ton peuple, lorsqu’il rebâtit la Kaʿba, s’en est tenu aux fondations d’Ibrāhīm" in hn)
chk("1056 question de ʿĀʾiša", "ne la ramènerais-tu pas sur les fondations d’Ibrāhīm" in hn)
chk("1056 récente incroyance", "Si ton peuple n’était pas de récente incroyance" in hn)
chk("1056 duel dégradé documenté", "la formule imprimée porte une marque du duel dégradée" in hn)
chk("1056 coda Ibn ʿUmar", "Si ʿĀʾiša a entendu cela du Messager de Dieu" in hn)
chk("1056 deux coins jouxtent la Pierre", "les deux coins qui jouxtent la Pierre [noire]" in hn)
chk("istiṯmār sagesse abstention", "la sagesse de l’abstention du Prophète de rebâtir la Kaʿba" in hn)
chk("istiṯmār explique coins syriens", "expliquer pourquoi le Prophète ne saluait pas les deux coins syriens" in hn)
chk("iʿdād mémorise + Zarqānī", "mémorise les hadiths de la leçon suivante et aide-toi du Šarḥ az-Zarqānī" in hn)
chk("iʿdād première recherche suspendue", "la formule imprimée est dégradée aux deux couches" in hn)
chk("iʿdād ṭawāf de la menstruante", "le jugement du ṭawāf de la menstruante (baḥṯ ʿan ḥukm ṭawāf al-ḥāʾiḍ)" in hn)

# --- 16) apparat ---
chk("apparat bornes", "ouverture p.71 (bannière" in hn and "clôture p.77" in hn)
chk("apparat p.78 exclusive médaillon 11", "p.78 = bannière du cours 11 (médaillon «" in hn.replace("&nbsp;", " ") and "borne supérieure exclusive, jamais devinée" in hn)
chk("apparat jonction p.70", "jonction p.70 = fin de la leçon 9" in hn)
chk("apparat onze lectures VLM", "les onze lectures VLM de la passe R647 réexploitées" in hn)
chk("apparat zéro āya", "zéro āya (leçon de hadith — le cache coranique n’a pas été sollicité)" in hn)
chk("apparat double rendu interdit", "double rendu interdit" in hn)
chk("apparat voisins 400", "pdf-mut23h2x-400 (leçon 11) vide et sans claim" in hn)
chk("apparat R508-bis + e040cc52", "R508-bis" in hn and "e040cc52" in hn and "minhaj-reprise-web-r649.bundle" in hn)
chk("apparat registre 1189 vérifié", "registre 1189 savants vérifié (1132 main + 57 llm)" in hn)
chk("apparat machine heartbeat claim", "heartbeat tr-tmp/cron-alive.log" in hn and "repris à 11h35 UTC" in hn)

# --- 17) 0 arabe script, rasm nu, doublons ---
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", h)
chk("0 caractère arabe", len(arab) == 0)
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("0 rasm nu « ... » sans contenu", "«&nbsp;&nbsp;&nbsp;»" not in h)
chk("h1 unique", h.count("<h1>") == 1)

# --- 18) registre (avant hand-set : slot vide ; après : htmlFr présent) ---
try:
    reg = json.load(open(REG, encoding="utf-8"))
    lessons = reg if isinstance(reg, list) else reg.get("lessons", [])
    slot = next((l for l in lessons if l.get("docId") == "pdf-mut23h2x-399"), None)
    if slot and slot.get("htmlFr"):
        chk("registre htmlFr 399 rempli", len(slot["htmlFr"]) > 15000)
        sav = json.load(open(SAV, encoding="utf-8"))
        savh = sav.get("hand", {})
        chk("savant-registry 399 posé", "pdf-mut23h2x-399" in json.dumps(savh))
    else:
        chk("registre 399 encore vide (pré-hand-set)", slot is None or not slot.get("htmlFr"))
except Exception as e:
    chk(f"registres lisibles ({e})", False)

print(f"\nverify-hadith3-pdf399 : {ok} OK / {fail} échec(s)")
raise SystemExit(1 if fail else 0)
