# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-404
(aʿmāl ayyām Minā (1) — الدرس 15, p.103-109 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) : bornes
p.103-109 (page-bannière quasi muette p.103, médaillon 15 lu par image 600 dpi ;
p.110 = bannière الدرس السادس عشر médaillon 16 = borne supérieure ; bas p.109 =
iʿdād al-qablī de la leçon 16 inclus comme aux livraisons précédentes) ;
9 numéros du Muwaṭṭaʾ tranchés chiffre par chiffre (1105, 1197, 1204, 1102,
1103, 1203, 1202, 1198, 1200) + références al-Muntaqā l-Bāǧī 4/81 et 4/82 et
ḥāšiyat al-ʿAdawī 1/395 ; citations coraniques rendues du cache ḥafṣ (Baqara
203, Baqara 196) sous étiquettes imprimées 201/195 — écart 201 vs 203 consigné,
195 = 196 − 1 conforme à la doctrine R511 ; honnêteté d’apparat (qīmahumā,
yatlaʿa n-niyyat, duplication rakʿatayn aw rakʿatayn, yuṭallib vs yunādī,
fa-qālat/fa-qāla rendu neutre, asḫlaṣ rendu « j’extrais ») ; 0 arabe,
0 apostrophe droite, guillemets appariés.
Usage: python3 scripts-translate/verify-hadith3-pdf404.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-404-fr.html"
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
chk("h1 Leçon 15", "<h1>Leçon 15" in hn and "aʿmāl ayyām Minā" in hn)
chk("h1 titleFr registre", "les rites des journées à Minā (1)" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.103-109", "p.103-109" in hn)
chk("meta slot 404", "pdf-mut23h2x-404" in hn)
chk("meta tick trace", "workerC-tick499558-0034-r670" in hn and "16h44 UTC" in hn)
chk("meta médaillon 15", "médaillon" in hn and "15" in hn)
chk("meta neighbours 402/403", "pdf-mut23h2x-402" in hn and "403" in hn)
chk("meta doctrine R511", "R511" in hn)
chk("meta OCR inversés", "5011" in hn and "0021" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’évaluation (at-taqwīm)",
    "L’exploitation du cours (al-istišhād)",
    "La préparation préalable (al-iʿdād al-qablī)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les trois objectifs ---
chk("obj 1 actes", "les actes des jours de Minā" in hn)
chk("obj 2 sunna jeûne/prière/takbīr", "la sunna" in hn and "le jeûne, la prière et le takbīr" in hn)
chk("obj 3 mašʿar", "mašʿar" in hn and "desseins" in hn)

# --- 3) tamhīd + versets cache ---
chk("tamhīd mabīt 2/3 nuits", "deux nuits pour" in hn and "trois nuits pour" in hn)
chk("āya Baqara 203 cache", "Baqara 203 du cache ḥafṣ" in hn)
chk("āya imprimée 201 consignée", "l’āya 201" in hn)
chk("wa-ḏkurū translitéré", "wa-ḏkurū llāha fī ayyāmin maʿdūdāt" in hn)
chk("pas d’arabe dans citation imprimée", "آية" not in h)

# --- 4) les trois textes ---
chk("texte 1105 ʿAbdallāh b. ʿʿAmr", "n° 1105" in hn and "ʿAbdallāh b. ʿʿAmr b. al-ʿʿĀṣ" in hn)
chk("isnad Abū Murra Umm Hāniʾ ʿAqīl", "Abū Murra" in hn and "Umm Hāniʾ" in hn and "ʿAqīl b. Abī Ṭālib" in hn)
chk("isnad Yazīd b. ʿAbdallāh b. al-Hādī", "Yazīd b. ʿAbdallāh b. al-Hādī" in hn)
chk("matn fa-daʿānī", "fa-daʿānī" in hn and "innī ṣāʾim" in hn)
chk("matn rupture", "bi-faṭrihinna" in hn)
chk("Mālik jours de tashrīq", "ayyām at-tašrīq)" in hn)
chk("texte 1197 Hishām b. ʿʿUrwa", "n° 1197" in hn and "Hishām b. ʿʿUrwa" in hn)
chk("1197 quatre priants", "Abū Bakr" in hn and "ʿUmar b. al-Khaṭṭāb" in hn and "ʿUthmān b. ʿAffān" in hn)
chk("1197 šaṭra imāratih + atammahā", "šaṭra imāratihi" in hn and "a-tammahā baʿdu" in hn)
chk("texte 1204 takbīr", "n° 1204" in hn and "riǧāli wa-n-nisāʾi" in hn)
chk("1204 ǧamāʿa/waḥdahu/āfāq", "fī ǧamāʿatin" in hn and "aw waḥdahu" in hn and "bil-āfāq" in hn)
chk("1204 maʿdūdāt tashrīq", "al-ayyām al-maʿdūdāt" in hn)

# --- 5) transmetteur + gloses ---
chk("notice Qurayšite Sahm Abū Muḥammad", "Sahm" in hn and "Abū Muḥammad" in hn)
chk("notice al-ʿIbādila", "al-ʿIbādila" in hn)
chk("notice avant Hégire + Šām 65", "avant l’Hégire" in hn and "Šām en l’an 65" in hn)
chk("glose Minā vallée est de Makka", "vallée entourée de montagnes" in hn and "l’est de Makka" in hn)
chk("glose ǧimār 2/3 jours", "deux jours pour" in hn and "trois pour celui" in hn)

# --- 6) fiqh : jeûne ---
chk("fiqh interdit surérogatoire consensus", "ṭāʿatan" in hn and "iǧmāʿan" in hn)
chk("fiqh 1102 Salamān b. Yasār", "n° 1102" in hn and "Salamān b. Yasār" in hn)
chk("fiqh 1103 Ibn Shihāb Ḥuḏāfa", "n° 1103" in hn and "ʿAbdallāh b. Ḥuḏāfa" in hn and "Ibn Shihāb" in hn)
chk("1103 akl šurb ḏikr", "akl wa-šurb wa-ḏikrillāh" in hn)
chk("fiqh ḍiyāfa invité", "hospitalité" in hn and "sans la permission de celui qui l’a reçu" in hn)
chk("fiqh mutamattiʿ mašhūr Mālik", "al-mašhūr" in hn and "mutamattiʿ" in hn)
chk("fiqh āya Baqara 196 cache", "Baqara 196 du cache ḥafṣ" in hn)
chk("āya imprimée 195 doctrine", "l’āya 195" in hn)
chk("fa-ṣiyāmu translitéré", "fa-ṣiyāmu ṯalāṯati ayyāmin fī l-ḥaǧǧi wa-sabʿatin iḏā raǧaʿtum" in hn)

# --- 7) fiqh : takbīr ---
chk("takbīr ḥaṣṣa aʿqāb", "ḥaṣṣa" in hn and "aʿqāb aṣ-ṣalawāt" in hn)
chk("1203 al-amr ʿindanā dubur", "al-amr ʿindanā" in hn and "dubur aṣ-ṣalawāt" in hn and "n° 1203" in hn)
chk("muʾaddā/maqḍiyya zoom", "al-muʾaddā" in hn and "al-maqḍiyya" in hn)
chk("qīmahumā consigné", "qīmahumā" in hn)
chk("Ibn al-Ḥadīb Muntaqā 4/81", "Ibn al-Ḥadīb" in hn and "4/81" in hn)
chk("ʿUmar Yaḥyā b. Saʿīd 1202", "Yaḥyā b. Saʿīd" in hn and "n° 1202" in hn)
chk("1202 rtafaʿat/zāġat/yarmī", "rtafaʿati š-šams" in hn and "zāġat aš-šams" in hn and "yarmī" in hn)
chk("yatlaʿa n-niyyat consigné", "wa-yatlaʿa n-niyyat" in hn)
chk("initiation ẓuhr naḥr / fin ṣubḥ tashrīq", "ṣalāt aẓ-ẓuhr" in hn and "yawm an-naḥr" in hn and "āḫir ayyām at-tašrīq" in hn)
chk("yaqṭaʿ at-takbīr", "yaqṭaʿu t-takbīr" in hn)
chk("ḥtiǧāǧ par la pratique", "bil-ʿamal" in hn)
chk("formule triple Muntaqā 4/82", "4/82" in hn and "Allāhu akbar, Allāhu akbar, Allāhu akbar" in hn)
chk("ʿAbd ar-Razzāq Salmān isnad ṣaḥīḥ", "ʿAbd ar-Razzāq" in hn and "bisnad ṣaḥīḥ" in hn and "Salmān" in hn)
chk("Šāfiʿī addition + man zāda", "al-Šāfiʿī" in hn and "man zāda aw naqaṣ falā ḥaraǧ" in hn)
chk("yaǧharūna", "yaǧharūna" in hn)
chk("concernés mandūb", "mandūb" in hn and "al-munfarid wal-ǧamāʿa" in hn)

# --- 8) fiqh : qasr ---
chk("qasr yusannu ribāʿiyya makiyyan", "yusannu" in hn and "al-ribāʿiyya" in hn and "makiyyan" in hn)
chk("qasr nusk ʿibāda pas de distance", "qasrun nusk wa-ʿibāda" in hn and "distance de réduction" in hn)
chk("qasr 1198 Saʿīd b. al-Musayyib", "n° 1198" in hn and "Saʿīd b. al-Musayyab" in hn)
chk("1198 a-timmū ṣalātakum qawmun safar", "a-timmū ṣalātakum" in hn and "qawmun safar" in hn)
chk("1198 seconde prière sans parole", "qu’il ait dit quoi que ce soit aux gens" in hn)
chk("sunna non abrogée", "lam yunsāḫ" in hn)

# --- 9) évaluation + istithmar + iʿdād ---
chk("éval 3 items", "maʿa l-istidlāl" in hn and "maʿa t-taʿlīl" in hn)
chk("éval cas réducteur de Minā", "un homme de Minā a réduit sa prière" in hn and "muḥtaǧan" in hn)
chk("istithmar n° 1200", "n° 1200" in hn and "arkaʿān am arbaʿ" in hn)
chk("1200 duplication consignée", "rakʿatayn, aw rakʿatayn" in hn and "consignée jamais corrigée" in hn)
chk("1200 a-timmū sākin muqīm", "sākinan muqīman" in hn and "fī iqāmatihim" in hn)
chk("iʿdād leçon 16 lancer", "mabīt" in hn and "hors de Minā" in hn and "description du lancer des ǧimār" in hn)

# --- 10) apparat ---
chk("apparat numéros tranchés", "chiffre par chiffre" in hn and "tr-tmp/qa-crops-r670/" in hn)
chk("apparat ʿAdawī 1/395", "1/395" in hn and "ʿAdawī" in hn)
chk("apparat canon Abū Murra", "couche canonique" in hn and "client de Umm Hānī" in hn)
chk("apparat yuṭallib vs yunādī", "yuṭallib" in hn and "yunādī" in hn)
chk("apparat précédents", "R664/R665" in hn)

# --- 11) typographie ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F]", re.sub(r"\uFDFA", "", h)))
chk("0 apostrophe droite", "'" not in h)

# --- 12) registre : pas de doublon ---
d = json.load(open(REG, encoding="utf-8"))
les = d.get("lessons", d if isinstance(d, list) else [])
mine = [l for l in les if "404" in str(l.get("docId") or "")]
chk("registre contient slot 404", len(mine) == 1)
if mine:
    chk("404 htmlFr vide avant hand-set", mine[0].get("htmlFr") in (None, "",))
done = sum(1 for l in les if l.get("htmlFr"))
chk("doublons impossibles (12 livrées)", done == 12)

# --- 13) claim actif ---
import os
c = open("/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-404.claim.json", encoding="utf-8").read()
chk("claim 404 trace", "workerC-tick499558-0034-r670" in c)

print(f"VERIFY pdf-404 : {ok} OK, {fail} échecs")
raise SystemExit(1 if fail else 0)
