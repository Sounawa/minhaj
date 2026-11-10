# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-406
(aḥkām al-hady (1) — الدرس 17, p.116-123 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) : bornes
p.116-123 (page d'annonce p.116 sans médaillon, clôture p.123 ; p.124 =
bannière du cours 18 médaillon 18 = borne supérieure ; p.129 sondée) ;
14 numéros du Muwaṭṭaʾ tranchés chiffre par chiffre (1111, 1141, 1113, 1106,
1118, 1144, 1142, 1143, 1120, 1114, 1107, 1112, 1126, 1108) ; citations
coraniques rendues du cache ḥafṣ (3:97 composite, 2:196, 5:97, 22:32, 22:33,
22:37) sous étiquettes imprimées (Ḥaǧǧ 34-35, Baqara 195, Māʾida 97, Ḥaǧǧ 30,
« l'āya 31 », Baqara 184) — écarts consignés ; honnêteté d'apparat (terme
d'iʿdād et tête de gloss coquilles non résolues, fāʾida dégradée, matn en
instance double, akramuh tranché, maṣlaḥah/mahall, nuhbī, rubrique double) ;
0 arabe, 0 apostrophe droite, guillemets appariés.
Usage: python3 scripts-translate/verify-hadith3-pdf406.py
"""
import json
import os
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-406-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-406.claim.json"

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
chk("h1 Leçon 17", "<h1>Leçon 17" in hn and "aḥkām al-hady" in hn)
chk("h1 titleFr registre", "les règles de la bête d’offrande (hady) (1)" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.116-123", "p.116-123" in hn)
chk("meta slot 406", "pdf-mut23h2x-406" in hn)
chk("meta tick trace", "workerC-tick0919-r673" in hn and "01h29 UTC" in hn)
chk("meta médaillon 18 borne", "médaillon" in hn and "18" in hn)
chk("meta neighbours 404/405", "pdf-mut23h2x-405" in hn and "403" in hn)
chk("meta doctrine R511", "R511" in hn)
chk("meta OCR inversés", "1411" in hn and "6011" in hn and "8011" in hn)
chk("meta session jumelle", "R668-bis" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’évaluation (at-taqwīm)",
    "L’exploitation du cours",
    "La préparation préalable (al-iʿdād al-qablī)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les deux objectifs ---
chk("obj 1 aḥkām fī l-ḥaǧǧ", "aḥkām al-hady fī l-ḥaǧǧ" in hn)
chk("obj 2 maqāṣid", "maqāṣid al-hady fī l-ḥaǧǧ" in hn)

# --- 3) tamhīd + bloc composite + versets cache ---
chk("tamhīd minasik šaʿāʾir", "minasik" in hn and "šaʿāʾir" in hn)
chk("āya Āl ʿImrān 97 cache", "Āl ʿImrān 97 du cache ḥafṣ" in hn)
chk("bloc composite médaillons 34-35", "médaillons" in hn and "34 et 35" in hn)
chk("imprimé Ḥaǧǧ 34-35 consigné", "les āyāt 34-35" in hn)
chk("cache 22:36-37 consigné", "22:36-37" in h.replace("\u202f", "").replace("\u00a0", " "))
chk("questions d’ouverture ×4", "sunna mūǧazza dans le hady" in hn and "sūq" in hn and "desseins" in hn)
chk("pas d’arabe dans la livraison", not re.search(r"[\u0600-\u06FF\u0750-\u077F]", re.sub(r"\uFDFA", "", h)))

# --- 4) les quatre textes ---
chk("texte 1111 budna nuḥiyat", "n° 1111" in hn and "nuḥiyat" in hn and "falyuṣill waladuhā" in hn)
chk("1111 muṣill/ḥumila", "muṣill" in hn and "ḥumila ʿalā ummih" in hn)
chk("texte 1141 istaqbala shāt", "n° 1141" in hn and "istaqbala" in hn and "shāt" in hn)
chk("1141 isnād Ǧaʿfar", "Ǧaʿfar b. Muḥammad" in hn and "de son père" in hn)
chk("texte 1113 qaddahu/ašʿarah Ḏī l-Ḥulayfa", "n° 1113" in hn and "qaddahu" in hn and "ašʿarah" in hn and "Ḏī l-Ḥulayfa" in hn)
chk("1113 shiqq aysar + ʿArafa + Minā", "ash-shiqq al-aysar" in hn and "ʿArafa" in hn and "ġadāta n-naḥr" in hn)
chk("1113 yaḥliqa/yaqaṣṣir + main + qibla", "yaḥliqa aw yaqaṣṣir" in hn and "qiyāman" in hn and "yuwaǧǧihuhunā lil-qibla" in hn)
chk("texte 1106 Abū Ǧahl", "n° 1106" in hn and "Abū Ǧahl b. Hishām" in hn and "ḥaǧǧ ou une ʿumra" in hn)

# --- 5) notices + gloses + résumé ---
chk("notice ʿAlī 40", "quatrième calife" in hn and "an 40 de l’Hégire" in hn)
chk("notice Ibn Abī Bakr 135", "Anṣārī" in hn and "an 135 de l’Hégire" in hn and "az-Zuhrī" in hn)
chk("notice nuhbī consignée", "nuhbī" in hn)
chk("glose wuḍiʿat coquille consignée", "wuḍiʿat" in hn and "coquille d’impression" in hn)
chk("glose quaddahu naʿlayn", "quaddahu" in hn and "naʿlayn" in hn)
chk("glose ašʿarah šaqq as-sunāma", "ašʿarah" in hn and "šaqq as-sunāma" in hn)
chk("résumé 3 items", "mūǧiz" in hn and "ṣifat sūq al-hady" in hn and "profit tiré du hady" in hn)

# --- 6) fiqh : awwalan ---
chk("fiqh 1118 thanī fawqah", "n° 1118" in hn and "aṯ-ṯanī wa-mā fawqah" in hn)
chk("tableau jadʿ qamariyya", "jadʿ" in hn and "qamariyya" in hn)
chk("tableau thanī bouc duwḫūlan bayyinan", "al-maʿaz" in hn and "duwḫūlan bayyinan" in hn)
chk("tableau vache 3/4", "trois années" in hn and "quatrième" in hn)
chk("tableau chameau 5/6", "cinq années" in hn and "sixième" in hn)
chk("fāʾida dégradée consignée", "fāʾida" in hn and "dégradée" in hn and "consignée" in hn)
chk("istaysara Baqara 196 cache / imprimé 195", "al-Baqara 196 du cache ḥafṣ" in hn and "l’āya 195" in hn)
chk("1144 badna/baqara", "n° 1144" in hn and "chamelle à sacrifier ou une vache" in hn)
chk("1142 Ibn ʿAbbās shāt + Mālik aḥabb", "n° 1142" in hn and "j’aime le plus entendre" in hn)
chk("Māʾida 97 cache aucun écart", "al-Māʾida 97 du cache ḥafṣ" in hn and "aucun écart" in hn)
chk("1143 baʿīr/baqara/kaffāra", "n° 1143" in hn and "baʿīr" in hn and "kaffāra" in hn)

# --- 7) fiqh : ṯāniyan ---
chk("Ḥaǧǧ 32 cache imprimé 30", "al-Ḥaǧǧ 32 du cache ḥafṣ" in hn and "l’āya 30" in hn)
chk("šaʿāʾir mušaʿʿara tasmīn", "al-anʿām al-mušaʿʿara" in hn and "tasmīn" in hn)
chk("ʿUrwa 1120 akramuh tranché", "n° 1120" in hn and "akramuh" in hn and "900 dpi" in hn)
chk("1114 bismi llāhi wa-llāhu akbar", "n° 1114" in hn and "bismi llāhi wa-llāhu akbar" in hn)
chk("Baqara 184 imprimé erroné Ḥaǧǧ 37", "al-Baqara, « l’āya 184 »" in hn and "al-Ḥaǧǧ 37 du cache ḥafṣ" in hn)
chk("litukabbirū consigné", "litukabbirū llāha ʿalā mā hadākum" in hn)

# --- 8) fiqh : ṯāliṯan ---
chk("1107 irkaḇhā waylak badna", "n° 1107" in hn and "irkaḇhā waylak" in hn and "badna" in hn)
chk("1107 riwāya note consignée", "deuxième ou la troisième riwāya" in hn)
chk("22:33 cache imprimé āya 31", "al-Ḥaǧǧ 33 du cache ḥafṣ" in hn and "l’āya 31" in hn)
chk("ǧumhūr/Mālik blâme sauf ḍarūra", "al-mašhūr" in hn and "ḍarūra" in hn)
chk("remplacement moderne aṣl", "al-ġālib al-aʿam" in hn and "al-aṣl" in hn)
chk("1112 laban raǧʿ ṣadaqa ġarm", "n° 1112" in hn and "raǧʿ fī aṣ-ṣadaqa" in hn and "ġarm" in hn)
chk("1112 yurawwaf fiṣīlahā", "yurawwaf fiṣīluhā" in hn and "faǧʿal fiṣīlahā maʿahā" in hn)
chk("1126 nusk + mašhūr + 3 exceptions", "n° 1126" in hn and "wa-n-nusk" in hn and "ǧazāʾ aṣ-ṣayd" in hn and "fidyat al-aḏā" in hn and "mā nuḏir li-l-masākīn" in hn)
chk("1126 maṣlaḥah/mahall consigné", "maṣlaḥah" in hn and "mahall" in hn)
chk("istifāda tamattuʿ takrīma", "tamattuʿ" in hn and "takrīma" in hn and "hôtes du Miséricordieux" in hn)

# --- 9) éval + exploitation + iʿdād ---
chk("éval 2 items", "abīn as-sunna al-mūǧazza" in hn and "maʿa t-tafṣīl wa-l-istidlāl" in hn)
chk("éval an-nās rejeté", "an-nās" in hn and "rejetée" in hn)
chk("exploitation 1108 Ibn Dīnār", "n° 1108" in hn and "ʿAbdallāh b. Dīnār" in hn)
chk("1108 badnatayn badnatayn", "badnatayn badnatayn" in hn)
chk("1108 qāʾima Ḫālid b. ʿAsīd minzalah", "qāʾima" in hn and "Ḫālid b. ʿAsīd" in hn and "minzalah" in hn)
chk("1108 libba ḥarba katif", "libba" in hn and "al-ḥarba" in hn and "katif" in hn)
chk("consigne ukhruǧ aḥkām", "ukhruǧ aḥkām al-hady" in hn)
chk("rubrique double consignée", "al-istiḫlāṣ / al-istiṯnāʾ" in hn)
chk("iʿdād fātahu + taḥallul", "man fātahu l-ḥaǧǧ" in hn and "taḥallul" in hn)
chk("iʿdād muḥrim épouse", "touché son épouse" in hn and "muḥrim" in hn)

# --- 10) apparat ---
chk("apparat numéros tranchés", "chiffre par chiffre" in hn and "tr-tmp/qa-crops-r673/" in hn)
chk("apparat 23 lectures", "vingt-trois lectures d’image" in hn)
chk("apparat adjudications 900 dpi", "900 dpi" in hn)
chk("apparat baʿīr adjudication", "rejet documenté des lectures" in hn)
chk("apparat précédents", "R664/R665/R670" in hn)
chk("apparat QA browser", "qa-r673-406-{desktop,mobile}.png" in hn)

# --- 11) typographie ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F]", re.sub(r"\uFDFA", "", h)))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))

# --- 12) registre : pas de doublon ---
d = json.load(open(REG, encoding="utf-8"))
les = d.get("lessons", d if isinstance(d, list) else [])
mine = [l for l in les if "406" in str(l.get("docId") or "")]
chk("registre contient slot 406", len(mine) == 1)
if mine:
    chk("406 htmlFr vide avant hand-set", mine[0].get("htmlFr") in (None, ""))
done = sum(1 for l in les if l.get("htmlFr"))
chk("doublons impossibles (14 livrées)", done == 14)

# --- 13) claim actif ---
c = open(CLAIM, encoding="utf-8").read()
chk("claim 406 trace", "workerC-tick0919-r673" in c)

print(f"VERIFY pdf-406 : {ok} OK, {fail} échecs")
raise SystemExit(1 if fail else 0)
