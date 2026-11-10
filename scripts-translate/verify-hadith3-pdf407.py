# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-407
(les règles de la bête d'offrande (hady) (2) — الدرس 18, p.124-129 du manuel
hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé 29 slots
pdf-mut23h2x-390..418) : bornes p.124-129 (p.123 = iʿdād de la leçon 17
annonçant les deux questions du cours — le manqué du pèlerinage et l'approche
de l'épouse en ihrām, sondées en couche texte ; p.130 = objectifs de la leçon
19 sondés couche texte + image = borne supérieure) ; 12 numéros du Muwaṭṭaʾ
tranchés chiffre par chiffre (1121, 1135, 1122, 1124, 1125, 1134, 1136, 1128,
1129, 1138, 1139, 1140) ; citation coranique rendue du cache ḥafṣ (22:28)
sous étiquette imprimée (26) — décalage régional −2 consigné (plage R673/R676) ;
notice Sulaymān b. Yasār 104 H / 73 ans ; honnêteté d'apparat (membre divergent
de l'ordre de ʿUmar, incise de l'athar d'ʿIkrima, ism Nawwār, coquille de
l'exercice d'exploitation, entrées lexicales de l'iʿdād tranchées par les
gloses p.132 de la leçon suivante — preuve croisée r679) ; 0 arabe,
0 apostrophe droite, guillemets appariés.
Usage: python3 scripts-translate/verify-hadith3-pdf407.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-407-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-407.claim.json"

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
chk("h1 Leçon 18", "<h1>Leçon 18" in hn and "bête d’offrande" in hn)
chk("h1 titleFr registre", "les règles de la bête d’offrande (hady) (2)" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.124-129", "p.124-129" in hn)
chk("meta slot 407", "pdf-mut23h2x-407" in hn)
chk("meta takeover trace r681", "1a1c5474aaf02af9-r681" in hn and "11h51 UTC" in hn and "takeover" in hn)
chk("meta claim r679 périmé", "r679" in hn and "11h22 UTC" in hn)
chk("meta borne sup p.130 sondée", "p.130" in hn and "borne supérieure exclusive" in hn)
chk("meta voisins 406/408", "leçon 17" in hn and "pdf-mut23h2x-408" in hn)
chk("meta doctrine R511 / décalage −2", "R511" in hn and "décalage régional" in hn)
chk("meta OCR inversés", "1211" in hn and "5311" in hn and "0411" in hn)
chk("meta diagnostic cadence (concurrency R680 mort)", "model concurrency limit exceeded" in hn and "R680" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "La conclusion d’édification (al-ḫaṭimah)",
    "L’exploitation du cours (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les deux objectifs ---
chk("obj 1 manqué + délivrance ihrām", "ḥukma man fātahu l-ḥaǧǧ" in hn and "taḥallulih min iḥrāmih" in hn)
chk("obj 2 ʿaṭb avant le lieu", "aḥkāma ʿaṭbi l-hady qabla bulūğihi maḥallah" in hn)

# --- 3) tamhīd ---
chk("tamhīd rite + proximity + hôtes + pauvres", "aḥad manāsiki l-ḥaǧǧ" in hn and "taqarruban ilā llāhi taʿālā" in hn and "ḍuyūfi r-Raḥmān" in hn and "fuqarāʾi Makkah" in hn)
chk("tamhīd āya Ḥaǧǧ cache 28 / imprimé 26", "fa-kulū minhā wa-aṭʿimū l-bāʾisa l-faqīr" in hn and "al-Ḥaǧǧ 28 du cache ḥafṣ" in hn and "l’āya 26" in hn)
chk("tamhīd réparation 3 causes", "naqṣin" in hn and "katarki baʿḍi l-wāǧibāt" in hn and "ka-tamattuʿi wa-l-qirān" in hn and "maḥẓūrāti l-iḥrām" in hn)
chk("tamhīd questions ×2", "bête d’offrande qui périt avant d’atteindre son lieu" in hn and "pèlerinage a été manqué" in hn)

# --- 4) les deux textes ---
chk("texte 1121 ṣāḥib hady + kayfa aṣnaʿu", "n° 1121" in hn and "ṣāḥib hadyi rasūli llāhi ﷺ" in hn and "kayfa aṣnaʿu" in hn)
chk("1121 fanḥarhā/qilādah/ḫall baynahā", "fan-ḥarhā" in hn and "alqi qilādatahā fī damihā" in hn and "ḫall baynahā wa-bayna n-nāsi yaʾkulūnahā" in hn)
chk("texte 1135 Ḥibbār + aḫṭaʾnā l-ʿiddah", "n° 1135" in hn and "Ḥibbār b. al-Aswad" in hn and "aḫṭaʾnā l-ʿiddah" in hn and "yawmu ʿArafah" in hn)
chk("1135 iḏhab/ṭawāf/immolation + membre divergent consigné", "iḏhab ilā Makkah" in hn and "fa-ṭuf anta wa-man maʿak" in hn and "wa-n-ḥur hadyak" in hn and "lecture divergente" in hn)
chk("1135 iḥlāl/taqsīr + retour + année suivante", "i-ḥluqū aw qaṣṣirū wa-rǧiʿū" in hn and "ʿāman qābilan" in hn and "fa-ḥuǧǧū wa-ahdū" in hn)
chk("1135 jeûne 3+7", "ṯalāṯati ayyāmin fī l-ḥaǧǧi wa-sabʿatin iḏā raǧaʿa" in hn)

# --- 5) notice + glose + résumé ---
chk("notice Sulaymān Hāšimī/mawlā Maymūna/Umm Salama", "Sulaymān b. Yasār" in hn and "al-Hāšimī al-Madanī" in hn and "mawlā) de Maymūna" in hn and "Umm Salama" in hn)
chk("notice 7 fuqahāʾ + ṯiqah", "fuqahāʾi s-sabʿati bi-l-Madīnah" in hn and "ṯiqah" in hn)
chk("notice an 104 (OCR « 855 » consigné) + 73", "104" in hn and "855" in hn and "73" in hn)
chk("glose ʿaṭaba", "uṣība bi-āfah" in hn and "yuḫāfu ʿalayhi l-halāku" in hn)
chk("résumé 2 items", "ubayyinu ḥukma l-hady iḏā ʿaṭaba aw ḍalla" in hn and "fātahu l-ḥaǧǧ" in hn and "yaǧibu ʿalayh" in hn)

# --- 6) fiqh : awwalan (bête) ---
chk("ʿaṭb immolation obligatoire + interdit manger tatawwuʿ", "yunḥaruh waǧaban" in hn and "wa-lā yaʾkulu minhu ṣāḥibuhū wa-lā ahlu rifqatih" in hn and "saddan li-ḏarīʿati t-tasāhuli" in hn)
chk("re-citation 1121 en preuve", "re-citation du texte n° 1121" in hn)
chk("1122 Saʿīd badanatan tatawwuʿan + ġaramahā", "n° 1122" in hn and "man sāqa badanatan tatawwuʿan" in hn and "ġaramahā" in hn)
chk("wāǧib mange + aġniyāʾ (couche texte consignée)", "fa-yaʾkulu minhu ṣāḥibuhū wa-l-aġniyāʾ" in hn and "couche texte" in hn)
chk("1124 Ibn Šihāb ǧazāʾ/naḏr/tamattuʿ + badal", "n° 1124" in hn and "Ibn Šihāb" in hn and "ǧazāʾan" in hn and "naḏran" in hn and "hadya tamattuʿ" in hn and "fa-ʿalayhi l-badal" in hn)
chk("ḍiyāʿ wāǧib badal / tatawwuʿ muḫayyar", "iḏā ḍalla l-hady" in hn and "aḫraǧa badalah" in hn and "muḫayyar" in hn)
chk("1125 Ibn ʿUmar naḏr abdal / tatawwuʿ option", "n° 1125" in hn and "in kānat naḏran" in hn and "abdalhā" in hn and "tarakahā" in hn)

# --- 7) fiqh : ṯāniyan (manqué) ---
chk("titre sous-section sans rapports (tranché structurel)", "bi-ġayri mubāšarati z-zawǧah" in hn and "cohérence structurelle" in hn)
chk("causes ×5 (montures/compte/maladie/croissant/empêchement)", "iḍlāli rawāḥilih" in hn and "ḫaṭaʾin fī ʿadad" in hn and "bi-maraḍ" in hn and "ḫafāʾi hilāl" in hn and "bi-šuġl" in hn)
chk("délivrance ʿumra complète + ḥaǧǧ qābil + hady", "bi-ʿumratin kāmilah" in hn and "yuḥuǧǧa qābilan wa-yuhdī" in hn)
chk("jeûne 3+7 pour l'homme", "ṯalāṯati ayyāmin fī l-ḥaǧǧi wa-sabʿatin iḏā raǧaʿa ilā ahlih" in hn)
chk("1134 Abū Ayyūb an-Nāziyya + aḍalla rawāḥilah", "n° 1134" in hn and "Abū Ayyūb al-Anṣārī" in hn and "bi-n-Nāziyyati min ṭarīqi Makkah" in hn and "aḍalla rawāḥilah" in hn)
chk("1134 aṣnaʿ mā yaṣnaʿu l-muʿtamir + ḥalalta", "aṣnaʿ mā yaṣnaʿu l-muʿtamir" in hn and "ṯumma qad ḥalalta" in hn)
chk("1134 stayasara (contre istaṭaʿta consigné)", "mā stayasara mina l-hady" in hn and "récusée" in hn)
chk("1134 rapport de Ḥibbār", "wa-rawā miṯlahū ʿan Hibbār" in hn)
chk("1136 qārin comme mufrarad + une bête (OCR deux consigné)", "n° 1136" in hn and "miṯlu l-mufaradi fī ḏālika l-qārin" in hn and "wa-man qarana l-ḥaǧǧa wa-l-ʿumrah" in hn and "deux bêtes" in hn)
chk("b) rapports avant Ǧamra : corruption + achèvement + réparation + bête chacun", "bi-mubāšarati z-zawǧah" in hn and "afsadā ḥaǧǧahumā" in hn and "itmāmuh" in hn and "ǧabran li-fiʿlihimā" in hn)
chk("1128 Saʿīd mā tarawna + séparation récusée + yaqḍiyā", "n° 1128" in hn and "mā tarawna fī" in hn and "yufraq baynahumā ilā ʿāmin qābil" in hn and "fa-li-yaqḍiyā ḥaǧǧahumā lladhī afsadā" in hn)
chk("1128 yuhdiyāni badanatan badanatan", "yuhdiyāni ǧamīʿan badanatan badanatan" in hn)
chk("1129 zones avant/après Ǧamra + Ibn ʿAbbās", "n° 1129" in hn and "mā baynahū wa-bayna an yadfaʿa min ʿArafah" in hn and "fa-innamā ʿalayhi an yaʿtamira wa-yuhdiya" in hn and "mašhūru ʿan Ibn ʿAbbās" in hn)
chk("1138 Nawwār (lectures fragmentaires récusées) + ʿIkrima", "n° 1138" in hn and "Nawwār" in hn and "ʿIkrimata mawlā Ibn ʿAbbās" in hn and "lā aẓunnuhū illā ʿan ʿAbdi llāhi bni ʿAbbās" in hn)
chk("1139 Rabīʿa + aḥabb ilayya (aujourd'hui récusé)", "n° 1139" in hn and "Rabīʿata bni ʿAbdi r-Raḥmān" in hn and "aḥabbu mā samiʿtu ilayya" in hn)
chk("régulateur après Ǧamra avant Ifāḍa : ʿumra + bête, ḥaǧǧ valide", "ṭawāfi l-ifāḍah" in hn and "ḥaǧǧuhū l-awwalu ṣaḥīḥ" in hn and "naqṣun" in hn and "taʿayyanati l-ʿumrah" in hn)

# --- 8) conclusion + exploitation + iʿdād ---
chk("conclusion taǧarrud + malaḏḏāt + ibtʿād", "taǧarruda min mataʿi d-dunyā wa-malaḏḏātihā" in hn and "ibtʿādi l-muʾaqqati" in hn and "ṭalaban li-riḍā llāhi taʿālā" in hn)
chk("1140 fatwā nasiya ṭawāf + nisāʾ", "n° 1140" in hn and "nasiya ṭawāfa l-ifāḍah" in hn and "aṣāba n-nisāʾ" in hn and "l-yaʿtamir wa-l-yuhd" in hn)
chk("invite Zarqānī + examen du texte", "ataʾammalu n-naṣṣ" in hn and "šarḥi z-Zarqānī" in hn)
chk("exo 1 coquille ʿaṭbi l-ḥaǧǧ consignée", "ubayyinu aḥkāma ʿaṭbi l-hady qabla bulūği maḥallih" in hn and "coquille" in hn)
chk("exo 2 car Maghrébins mufradīn + aḍḥā", "al-ḥāfilah" in hn and "l-maġāriba" in hn and "mufarradīna bi-l-ḥaǧǧ" in hn and "yawmi l-aḍḥā" in hn)
chk("exo 2 réponse ʿumra de délivrance 1134/1135", "ʿumra complète de délivrance" in hn and "n° 1134" in hn)
chk("iʿdād ilqāʾ at-tafath + labidtu raʾsī (preuve croisée p.132)", "ilqāʾ at-tafath" in hn and "labidtu raʾsī" in hn and "p.132" in hn and "vlm-408" in hn)
chk("iʿdād matā yataḥallalu + aʿmāl yawm naḥr", "matā yataḥallalu l-muḥrim" in hn and "yaqūmu bihā l-ḥāǧǧu yawma n-naḥr" in hn)
chk("iʿdād lien leçon 19 slot 408", "pdf-mut23h2x-408" in hn and "Les rites du pèlerin au jour du sacrifice" in hn)

# --- 9) apparat ---
chk("apparat numéros tranchés chiffre par chiffre", "chiffre par chiffre" in hn and "tr-tmp/vlm-407/" in hn)
chk("apparat 73 lectures", "soixante-treize lectures" in hn)
chk("apparat bornes p.123/p.130 sondées", "p.123" in hn and "jamais devinée" in hn)
chk("apparat preuve croisée r679 gloses p.132", "x6-p132-gloses.txt" in hn and "r679" in hn)
chk("apparat qa browser r681", "qa-r681-407-{desktop,mobile}.png" in hn)
chk("apparat claim takeover + refresh", "takeover" in hn and "12h11 UTC" in hn)
chk("apparat PARALLÈLE maintenu slot 405/408", "PARALLÈLE" in hn and "405" in hn)

# --- 10) typographie ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F]", re.sub(r"\uFDFA", "", h)))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))

# --- 11) registre : pas de doublon ---
d = json.load(open(REG, encoding="utf-8"))
les = d.get("lessons", d if isinstance(d, list) else [])
mine = [l for l in les if str(l.get("docId") or "") == "pdf-mut23h2x-407"]
chk("registre contient slot 407", len(mine) == 1)
if mine:
    chk("407 htmlFr vide avant hand-set", mine[0].get("htmlFr") in (None, ""))
done = sum(1 for l in les if l.get("htmlFr"))
chk("doublons impossibles (16 livrées avant hand-set)", done == 16)
voisins = [l for l in les if str(l.get("docId") or "") in ("pdf-mut23h2x-406", "pdf-mut23h2x-408")]
chk("voisins 406 livré / 408 non livré", voisins and len(voisins) == 2 and voisins[0].get("htmlFr") and not voisins[1].get("htmlFr"))

# --- 12) claim actif ---
c = open(CLAIM, encoding="utf-8").read()
chk("claim 407 trace r681", "1a1c5474aaf02af9-r681" in c)

print(f"VERIFY pdf-407 : {ok} OK, {fail} échecs")
