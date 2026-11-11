# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-409
(les règles de la tonsure et de la coupe — أحكام الحلق والتقصير, leçon 20
imprimée, p.136-140 du manuel hadith-3-iadadi_text.pdf, 196 p.) — contrôles
sur le texte débarrassé de ses balises (N = normalisation de convention),
+ 4 contrôles typographiques sur le HTML brut.
Usage: python3 scripts-translate/verify-hadith3-pdf409.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-409-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-409.claim.json"

NORM_MAP = [("Ǧ", "J"), ("ǧ", "j"), ("ṯ", "th"), ("Ṯ", "TH"), ("š", "ch"),
            ("Š", "CH"), ("č", "ch"), ("Č", "CH"), ("ḫ", "kh"), ("Ḫ", "KH"),
            ("ġ", "gh"), ("Ġ", "GH"), ("ʿ", "\u2019"), ("ʾ", "\u2019"),
            ("'", "\u2019")]


def N(s):
    for a, b in NORM_MAP:
        s = s.replace(a, b)
    return s


ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
# texte pur : balises ôtées, entités résolues, espaces compactés, N appliqué
t = re.sub(r"<[^>]+>", "", h)
t = t.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u2009", " ")
t = N(re.sub(r" +", " ", t))

# --- 1) squelette ---
chk("h1 Leçon 20", "<h1>Leçon 20" in h and N("règles de la tonsure et de la coupe") in t)
chk("h1 translittération imprimée", N("(ḥalq et taqṣīr) — le livre d’al-Ḥadīth") in t)
chk("lesson-meta present", 'class="lesson-meta"' in h)
chk("meta bornes p.136-140", N("p.136-140") in t)
chk("meta slot 409", N("pdf-mut23h2x-409") in t)
chk("meta 19e slot / compteur 19/29", "dix-neuvième slot livré" in t and N("compteur 19/29") in t)
chk("meta continuité canal principal", "main-channel-reprise-r686" in t and N("21h40 UTC") in t)
chk("meta refresh trace r687", "22h11 UTC" in t and N("1a1cca61c050ffdd-r687-main") in t)
chk("meta borne sup p.141 médaillon 21", "p.141" in t and "médaillon 21" in t and N("borne supérieure exclusive") in t)
chk("meta voisin 408 livré R684", "R684" in t and N("58 683 car") in t)
chk("meta doctrine R511 / cache", "R511" in t and "décalage régional" in t and N("al-Baqara 196") in t)
chk("meta OCR inversés 1174/1178", "4711" in t and "8711" in t and N("1187") in t)
chk("meta OCR inversés 1184/1177/1179", "4811" in t and "7711" in t and N("9711") in t)
chk("meta OCR inversés 1180/1175", "0811" in t and N("5711") in t)
chk("meta doctrine WIP-10min", "WIP-10min" in t and N("PUSH À CHAQUE FIN DE PASSE") in t)
chk("meta matière r686 réutilisée", "r686" in t and N("sans perte") in t)
chk("meta PARALLÈLE 1", "PARALLÈLE" in t and N("aucun autre slot en cours") in t)

# --- 2) sections (titres réels débarrassés des balises) ---
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (تَمْهِيد) (l’ouverture de la leçon)",
    "Les textes du cours : les hadiths du Muwaṭṭa’ traduits du manuel",
    "La notice du transmetteur (tarjamat ar-rāwī)",
    "La glose des mots (ach-charḥ) du manuel",
    "Le résumé du cours (istikhlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīth)",
    "L’évaluation du cours (at-taqwīm)",
    "L’exploitation du cours (al-istithmār) : l’athar de la délivrance différée (n° 1175) et l’invite à preuve",
    "La préparation préalable (al-i’dād al-qablī) de la leçon suivante",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", N(sec) in t)

# --- 3) objectifs ---
chk("obj 1 aḥkām", N("an a-ta’rraf aḥkāma l-ḥalq wa-t-taqṣīr") in t)
chk("obj 2 takrār", N("sababa takrāri n-nabiyyi ﷺ ad-du’ā’a li-l-muḥalliqīn") in t)
chk("obj 3 maqāṣid", N("an adrika maqāṣida l-ḥalq wa-t-taqṣīr fī l-ḥajj") in t)
chk("objectifs cadrent la matière", N("précellence de la tonsure") in t)

# --- 4) tamhīd ---
chk("tamhīd incipit nusk", N("nuskun min manāsiki l-ḥajj") in t)
chk("tamhīd āya Fatḥ incipit", N("laqd ṣadaqa llāhu rasūlahu r-ru’yā bi-l-ḥaqq") in t)
chk("tamhīd āya Fatḥ muḥalliqīn", N("āminīna muḥalliqīna ru’ūsakum wa-muqaṣṣirīna") in t)
chk("tamhīd Fatḥ imprimé 27 identique", "sūrat al-Fatḥ, l’āya 27 — al-Fatḥ 27 du cache ḥafṣ" in t and N("numéro identique") in t)
chk("tamhīd āya 25 récusée", "āya 25" in t and N("récusée") in t)
chk("tamhīd argument maqṣūd", N("wa-lau lam yakun nuskan maqṣūdan lam yaṣif dukhūlahum bi-dhālik") in t)
chk("question d'ouverture", N("fa-mā hiya aḥkām al-ḥalq wa-t-taqṣīr") in t)

# --- 5) textes ---
chk("1174 triade invocations", "allāhumma rḥam al-muḥalliqīn" in t and N("wa-l-muqaṣṣirīn yā rasūla llāh") in t)
chk("1174 numéro + OCR", "n° 1174" in t and N("4711") in t)
chk("1174 isnād", N("de Nāfi', de ʿAbd Allāh") in t and N("b. ʿUmar") in t)
chk("1178 ordre sans divergence", N("al-amru alladhī lā ikhtilāf fīhi") in t)
chk("1178 bimannā yawm an-naḥr", N("ḥattā yaḥill bimannā yawm an-naḥr") in t)
chk("1178 āya Baqara citée", N("wa-lā taḥliqū ru’ūsakum ḥattā yabluġa l-hady maḥillah") in t)
chk("1178 imprimé 195 cache 196", "l’āya 195" in t and N("al-Baqara 196 du cache") in t)
chk("1178 OCR 8711 recouvert", "8711" in t and N("1187") in t)
chk("1184 Sālim Jalmayn", N("kān idhā arād an yaḥrim dā bi-l-Jalmayn") in t)
chk("1184 faqaṣṣ + qabl an yuḥil", N("faqaṣṣ charibah wa-akhadh min liḥyatih qabl an yuḥil muḥriman") in t)
chk("1184 buliġah", N("annahū buliġah") in t)
chk("1177 nasiya l-ḥalāq", N("rajulun nasiya l-ḥalāq bimannā fī l-ḥajj") in t)
chk("1177 wāsiʿ + aḥabb ilayy", "dhālik wāsi’" in t and N("aḥabb ilayy") in t)
chk("textes quatre lames", N("quatre textes dans les cadres") in t)

# --- 6) notice ---
chk("notice renvoi sīqat tarjamatuh", N("sīqat tarjamatuh") in t)
chk("notice rubrique tarjamat al-murāwī", N("tarjamat al-murāwī") in t)
chk("notice consignée sans date", N("aucune date, aucune généalogie nouvelle") in t)

# --- 7) gloses ---
chk("glose Jilm miqrāḍ", "tathniyat al-Jilm" in t and N("al-miqrāḍ") in t)
chk("glose maqṣadayn", N("ay qul wa-rḥam al-muqaṣṣirīn") in t)
chk("glose ʿaṭf maḥdhūf", N("fa-l-’aṭf ’alā maḥdhūf") in t)
chk("glose aṭf ath-thaqafī", N("l-’aṭf ath-thaqafī") in t)

# --- 8) résumé 3 items ---
chk("résumé item 1 ḥukm+mīqāt", N("ubīn ḥukm al-ḥalq wa-t-taqṣīr wa-mīqātahumā") in t)
chk("résumé item 2 tawfīr", N("mā ḥukm tawfīr ach-cha’r li-l-ḥalāq fī l-ḥajj") in t)
chk("résumé item 3 matā d'a", N("matā d’a an-nabiyyu ﷺ li-l-muḥalliqīn wa-mā sabab dhālik") in t)
chk("résumé miroir objectifs", N("miroirent exactement les trois objectifs") in t)

# --- 9) fiqh ---
chk("fiqh bannière translit", N("fiqh al-ḥadīth") in t)
chk("fiqh deux grandes sections", "awwalan" in t and N("thāniyan") in t)
chk("fiqh statut wājib", N("wājibun min wājibāti l-ḥajj") in t)
chk("fiqh statut dam", N("fa-’alayhi ad-dam") in t)
chk("fiqh statut taqṣīr sunna femme", N("sunnatun li-l-mar’ah") in t)
chk("fiqh athar Ibn ʿAbbās", "laysa ’alā n-nisā’i ḥalq" in t and N("innamā ’alā n-nisā’i t-taqṣīr") in t)
chk("fiqh Sunan Abī Dāwud + marfūʿ", "Sunan Abī Dāwud" in t and N("marfū’") in t)
chk("fiqh coupe suffit + mujmaʿ", "wa-yujzī ar-rajul ’an al-ḥalāq" in t and N("mujma’") in t)
chk("fiqh temps aube+Jamra", N("ba’d ṭulū’ al-fajr ba’d ramy jamrat al-’aqabah") in t)
chk("fiqh temps immole d'abord", "naḥara hadyan in kān ma’ah" in t and N("thumma yaḥliq aw yaqṣir ba’d dhālik") in t)
chk("fiqh 1178 re-cité jamais re-numéroté", "n° 1178 — re-citation" in t and N("jamais re-numérotée") in t)
chk("fiqh maḥall naḥr/dhabḥ", N("ḥaythu yaḥill naḥrah aw dhabḥah") in t)
chk("fiqh bulāgh = naḥr/nabb", N("an-naḥr aw an-naḥḥ, lā mujarrad al-wuṣūl") in t)
chk("fiqh lieu minā aw makkah", N("minā aw makkah") in t)
chk("fiqh 1177 re-cité", N("n° 1177 — re-citation") in t)
chk("fiqh épargne yastaḥibb", N("yastaḥibb li-murīd al-ḥajj tawfīr cha’rih li-l-ḥalāq") in t)
chk("fiqh muʿtamir proche du ḥajj", N("an lā yaḥliq idhā kān yuqarrib al-ḥajj") in t)
chk("fiqh 1179 ʿAmr b. ʿAbd Allāh", "innah kān idhā afṭar min Ramaḍān wa-huwa yurīd al-ḥajj" in t and N("’Amr b. ’Abd Allāh") in t)
chk("fiqh 1179 rūwiya 'an Nāfiʿ", N("rūwiya ’an Nāfi’") in t)
chk("fiqh 1179 chuʾth", N("li-mazīd ach-chu’th al-maṭlūb fī l-ḥajj") in t)
chk("fiqh 1179 second alā n-nās", "wa-laysa dhālik ’alā n-nās" in t and N("n° 1179 — seconde citation") in t)
chk("fiqh machaqqah chadīdah", N("li-mā fīh min al-machaqqah ach-chadīdah") in t)
chk("fiqh 1184 re-cité", "n° 1184 — re-citation" in t and N("jamais re-numérotée") in t)
chk("fiqh tawābiʿ al-ghusl", N("min jumlat at-tanẓīf wa-tawābi’ al-ghusl li-l-iḥrām") in t)
chk("fiqh 1180 Ibn ʿUmar liḥya+chārib", "akhadh min liḥyatih wa-chāribih" in t and N("n° 1180") in t)
chk("fiqh 1180 chawwāl", N("min awwal chawwāl") in t)
chk("fiqh 1180 pas du taḥallul", N("wa-lays al-akhdh minhumā min tamām at-taḥallul") in t)
chk("fiqh 1180 istaḥabb Mālik", N("wa-qad istaḥabb dhālik Mālik") in t)
chk("fiqh 1180 yutta-rak tranché", "yutta-rak" in t and N("bi-tark") in t)
chk("fiqh 1173 lien leçon précédente", N("n° 1173") in t)

# --- 10) évaluation ---
chk("taqwīm q1 ṣifat", N("ubīn ṣifat al-ḥalāq wa-t-taqṣīr wa-ḥukmahumā") in t)
chk("taqwīm q2 thalāth", N("limādhā khaṣṣ an-nabiyyu ﷺ al-muḥalliqīn bi-d-du’ā’ thalāth") in t)
chk("taqwīm q3 istidlāl", N("ma’a al-istidlāl") in t)
chk("taqwīm résolues en place", N("les voici résolues en place") in t)

# --- 11) exploitation ---
chk("istithmār 1175 muʿtamir nuit", N("yadkhul makkah laylan wa-huwa mu’tamir") in t)
chk("istithmār 1175 ṭawāf+saʿy", N("fa-yaṭūf bi-l-bayt wa-bayn aṣ-Ṣafā wa-l-Marwah") in t)
chk("istithmār 1175 taʾḫīr ḥalāq", N("wa-yu’akhkhar al-ḥalāq ḥattā yuṣbiḥ") in t)
chk("istithmār 1175 walākinnah", N("wa-lākinnah lā ya’ūd ilā l-bayt fa-yaṭūf bih ḥattā yaḥliq ra’sah") in t)
chk("istithmār 1175 witr + lā yaqrub", "wa-rubbamā dkhal al-masjid fa-awtar fīh" in t and N("wa-lā yaqrub al-bayt") in t)
chk("istithmār 1175 tranché 1200 dpi", "wa-aktah" in t and N("1200 dpi") in t)
chk("istithmār invite Zarqānī", N("asta’īn bi-charḥ az-Zarqānī") in t)
chk("istithmār invite taʾḫīr saʿy", N("ḥukm ta’khīr al-ḥalāq aw at-taqṣīr ’an as-sa’y") in t)
chk("istithmār ordre des œuvres rappelé", N("l’ordre des œuvres") in t)

# --- 12) préparation ---
chk("iʿdād invite aḥfiẓ", N("aḥfiẓ aḥādīth") in t)
chk("iʿdād q1 fidiya gibier", N("pour exposer la fidiya de ce qui a été atteint, du gibier ou de la bête sauvage") in t)
chk("iʿdād q2 dafʿ al-adhā", N("fidiyat daf’ al-adhā") in t)
chk("iʿdād borne leçon 21 médaillon", "médaillon 21" in t and N("pdf-mut23h2x-410") in t)

# --- 13) apparat ---
chk("apparat bornes p.136-140 détaillées", "bornes" in t and N("p.136-140 du PDF source") in t)
chk("apparat 7 numéros", all(x in t for x in ("1174", "1175", "1177", "1178", "1179", "1180", "1184")))
chk("apparat āyas Fatḥ/Baqara", "al-Fatḥ 27" in t and N("al-Baqara 196") in t)
chk("apparat Amr 1000 dpi wāw", "1000 dpi" in t and N("wāw") in t)
chk("apparat rubrique istiḫlāṣ par série R681", "R681" in t and N("convergence de série") in t)
chk("apparat crops r686/r687", "qa-crops-r686" in t and N("qa-crops-r687") in t)
chk("apparat qa-lesson PASS comptée", N("53 872 car au brouillon") in t)

# --- 14) typographie (HTML brut) ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", re.sub(r"<span dir=\"rtl\" lang=\"ar\">[^<]*</span>", "", h)))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("ﷺ présent", "ﷺ" in h)

# --- 15) registre : pas de doublon ---
d = json.load(open(REG, encoding="utf-8"))
les = d.get("lessons", d if isinstance(d, list) else [])
mine = [l for l in les if str(l.get("docId") or "") == "pdf-mut23h2x-409"]
chk("registre contient slot 409", len(mine) == 1)
if mine:
    chk("409 htmlFr vide avant hand-set", mine[0].get("htmlFr") in (None, ""))
done = sum(1 for l in les if l.get("htmlFr"))
chk("doublons impossibles (19 livrées avant hand-set)", done == 19)
voisins = [l for l in les if str(l.get("docId") or "") in ("pdf-mut23h2x-408", "pdf-mut23h2x-410")]
chk("voisins 408 livré / 410 non livré", voisins and len(voisins) == 2 and voisins[0].get("htmlFr") and not voisins[1].get("htmlFr"))

# --- 16) claim actif ---
c = open(CLAIM, encoding="utf-8").read()
chk("claim 409 trace r687", "1a1cca61c050ffdd-r687-main" in c)

print(f"VERIFY pdf-409 : {ok} OK, {fail} échecs")
if fail:
    raise SystemExit(1)
