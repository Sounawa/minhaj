# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-408
(les rites du pèlerin au jour du sacrifice — ما يفعله الحاج يوم النحر, leçon 19
imprimée, p.130-135 du manuel hadith-3-iadadi_text.pdf, 196 p., livre portail
pré-mappé 29 slots pdf-mut23h2x-390..418) : bornes p.130-135 (p.129 = annonce
iʿdād de la leçon 407 livrée R681 — re-cadrage r684 du crop x0 raté : la page ne
porte QUE l'annonce, bas blanc ; p.136 = objectifs de la leçon 20/409, borne
supérieure exclusive) ; 9 numéros du Muwaṭṭaʾ tranchés chiffre par chiffre
(1173, 1267, 1169, 1167, 1170, 1226, 1186, 1185, 1183) ; fatwā n° 1140
(p.128, leçon 18) rappelée en règle connectée — jamais re-numérotée ; deux
āyas rendues du cache ḥafṣ (at-Tawba 3 imprimé « 3 » — identique ; al-Māʾida
95 imprimé « 97 » — décalage régional +2 consigné, sens inverse de la plage
Ḥaǧǧ −2 de la leçon 18) ; notice Ḥafṣa 41 H / 45 H ; iʿdād ×3 p.129 résolu par
les gloses p.132 (preuve croisée de leçon, consignée R681) ; iʿdād ×2 p.135 ;
adjudications image (lieu « à Médine » de l'athar 1183, finale « il revient —
l'Ifāḍa accomplie », bandeau al-istiṯmār, ʿAmr b. al-ʿĀṣ de la re-citation,
membre ʿAlī restitué sur couche texte, « a approché son épouse », « en cet
âge », triade ẓafarahū/ḍafara) ; 0 arabe, 0 apostrophe droite, guillemets
appariés.
Usage: python3 scripts-translate/verify-hadith3-pdf408.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-408-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-408.claim.json"

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
chk("h1 Leçon 19", "<h1>Leçon 19" in hn and "rites du pèlerin au jour du sacrifice" in hn)
chk("h1 titleFr registre", "les rites du pèlerin au jour du sacrifice" in hn)
chk("h1 translittération imprimée", "mā yafʿaluhu l-ḥāǧǧ yawma n-naḥr" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.130-135", "p.130-135" in hn)
chk("meta slot 408", "pdf-mut23h2x-408" in hn)
chk("meta 18e slot / compteur 17/29", "dix-huitième leçon livrée" in hn and "compteur 17/29" in hn)
chk("meta takeover trace r684", "subagent-r684-408" in hn and "21h08 UTC" in hn and "takeover" in hn)
chk("meta claim r683 périmé", "r683-408" in hn and "18h31 UTC" in hn)
chk("meta borne sup p.136 sondée", "p.136" in hn and "borne supérieure exclusive" in hn)
chk("meta voisins 407/409", "R681" in hn and "pdf-mut23h2x-409" in hn)
chk("meta doctrine R511 / décalage +2 al-Māʾida", "R511" in hn and "décalage régional" in hn and "+2" in hn)
chk("meta OCR inversés", "3711" in hn and "7621" in hn and "6221" in hn and "1183" in hn)
chk("meta doctrine WIP-10min", "WIP-10min" in hn and "tous les ~10 minutes" in hn)
chk("meta re-cadrage x0 p.129 raté", "x0-p129-annonce" in hn and "zone blanche" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots (aš-šarḥ) du manuel",
    "Le résumé du cours (istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’évaluation du cours (at-taqwīm)",
    "L’exploitation du cours (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:44]} »", sec in hn)

# --- 2) les trois objectifs + médaillon + iʿdād résolu ---
chk("obj 1 œuvres du jour", "an a-taʿrraf aʿmāla yawmi n-naḥr" in hn)
chk("obj 2 délivrance du rite", "an adrika aḥkāma t-taḥalluli mina n-nusk" in hn)
chk("obj 3 sunna prophétique", "an altazima sunnata n-nabiyi ﷺ fī adāʾi aʿmāli yawmi n-naḥr" in hn)
chk("médaillon 19 + lien slot 408 (18e/29)", "le nombre 19" in hn and "pdf-mut23h2x-408" in hn and "dix-huitième" in hn)
chk("iʿdād ×3 p.129 résolu — les deux entrées par les gloses p.132", "ilqāʾ at-tafath" in hn and "labidtu raʾsī" in hn and "p.132" in hn and "vlm-408" in hn)
chk("iʿdād question 2 + 3 résolues", "matā yataḥallalu l-muḥrim" in hn and "aʿmāla yawmi n-naḥr" in hn)

# --- 3) tamhīd ---
chk("tamhīd jour proclamé + plus grand pèlerinage", "ayyāmi l-ḥaǧǧi l-mašhūdah" in hn and "yawma l-ḥaǧǧi l-akbar" in hn)
chk("tamhīd āya at-Tawba cache 3 / imprimé 3", "wa-aḏānun mina llāhi wa-rasūlihī ilā n-nāsi yawma l-ḥaǧǧi l-akbar" in hn and "at-Tawba 3 du cache ḥafṣ" in hn and "l’āya 3" in hn)
chk("tamhīd lectures divergentes récusées (4)", "Ṭā-Hā" in hn and "ne t’attriste pas" in hn and "proclame aux gens le pèlerinage" in hn and "récusées" in hn)
chk("tamhīd questions ×2", "fa-mā hiya aʿmālu yawmi n-naḥr" in hn and "wa-matā yataḥallalu l-muḥrimu bi-n-nuski fī hāḏā l-yawm" in hn)

# --- 4) les trois textes ---
chk("texte 1173 Mālik + ḥattā yanḥura hadyah", "n° 1173" in hn and "lā yaǧūzu li-aḥadin an yaḥliqa raʾsahu ḥattā yanḥura hadyah" in hn)
chk("1173 l’œuvre entière + liste", "wa-innamā l-ʿamalu kulluhu yawmu n-naḥr" in hn and "aḍ-ḏabḥu" in hn and "wa-lubsu ṯ-ṯiyāb" in hn and "wa-ilqāʾu t-tafṯi wa-l-ḥalāq" in hn)
chk("texte 1267 ʿĪsā b. Ṭalḥa + isnād complet", "n° 1267" in hn and "ʿĪsā b. Ṭalḥa" in hn and "ʿAbd Allāh b. ʿAmr b. al-ʿĀṣ" in hn)
chk("1267 waqafa bi-Minā + anḥur/irmi/ifʿal", "waqafa rasūlu llāhi ﷺ li-n-nāsi bi-Minā" in hn and "an-ḥur wa-lā ḥaraǧ" in hn and "irmi wa-lā ḥaraǧ" in hn and "ifʿal wa-lā ḥaraǧ" in hn)
chk("texte 1169 Ḥafṣa + labadtu/qalladtu", "n° 1169" in hn and "innī labadtu raʾsī" in hn and "wa-qalladtu hadyī" in hn and "fa-lā aḥillu ḥattā anḥur" in hn)

# --- 5) notice + glose + résumé ---
chk("notice Ḥafṣa umm al-muʾminīn + fille de ʿUmar", "Ḥafṣatu raḍiya llāhu ʿanhā" in hn and "bintu ʿUmara bni l-Ḫaṭṭābi amīri l-muʾminīn" in hn and "šaqīqatu ṣ-ṣaḥābiyyi l-ǧalīli" in hn)
chk("notice Khunays + Uḥud + 41/45 (OCR « 14 » consigné)", "Khunaysi bni Ḥuḏāfata s-Sahmī" in hn and "Uḥud" in hn and "sanah 41" in hn and "sanah 45" in hn and "« 14 »" in hn)
chk("glose ilqāʾ at-tafath (rasage/vêtements/ongles/souillures)", "ḥalāqu š-šaʿr" in hn and "wa-lubsu ṯ-ṯiyāb" in hn and "wa qaṣṣu l-aẓāfir" in hn and "l-awsāḫ" in hn)
chk("glose labidtu raʾsī talbīd + gomme", "min at-talbīd" in hn and "min nawʿi ṣamġ" in hn and "li-yaǧtamiʿa š-šaʿr" in hn)
chk("résumé 3 items", "astaḫliṣu mina l-aḥādīṯi aʿmāla yawmi n-naḥr" in hn and "maḥalla naḥri l-hadyi wa-ṣifatah" in hn and "matā yataḥallalu l-muḥrimu bi-n-nusk" in hn)

# --- 6) fiqh : awwalan (œuvres du jour) ---
chk("fiqh1 ordre des quatre œuvres", "ramyu ǧamrati l-ʿAqabah" in hn and "ṯumma naḥru l-hadyi aw ḏabḥuh" in hn and "ṯumma l-ḥalqu aw taqṣīr" in hn and "ṯumma ṭawāfu l-ifāḍah" in hn)
chk("fiqh1 re-citation 1267 + divergence ʿAmr consignée", "re-citation du second texte" in hn and "« ʿAmr b. al-ʿĀṣ »" in hn and "divergence propre de l’imprimé" in hn)
chk("fiqh1 consensus + dam", "aǧmaʿa l-ʿulamāʾu ʿalā l-iǧāzati fī t-taqdīmi wa-t-taʾḫīr" in hn and "li-allā yakūna wasīlatan ilā n-nisāʾi qabla r-ramy" in hn)
chk("fiqh1 fidyah du rasage avancé", "wa-awǧaba l-fidyata fī taqdīmi l-ḥalqi ʿalā r-ramy" in hn and "bi-ilqāʾi t-tafṯi fa-ʿala šayʾan mina t-taḥallul" in hn and "qiyāsan ʿalā man bi-raʾsihi aḏan" in hn)
chk("fiqh1 a) interdit avant l’aube + re-citation 1173", "an yanḥura qabla l-faǧri yawmi n-naḥr" in hn and "re-citation" in hn and "n° 1173" in hn)
chk("fiqh1 b) lieu 1167 + tout Minā", "n° 1167" in hn and "hāḏā l-munaḥar, wa-kullu Minā munaḥar" in hn and "l-munaḥaru l-afḍal" in hn)
chk("fiqh1 c) ʿAlī 1170 + membre restitué couche texte", "n° 1170" in hn and "naḥara baʿḍa hadyihī bi-yadih" in hn and "couche texte" in hn)
chk("fiqh1 c) délégation moderne", "wa-fī hāḏā l-ʿaṣr" in hn and "bi-dafʿi taklifati l-hadyi li-l-ǧihāti l-muḫtaṣṣah" in hn)

# --- 7) fiqh : ṯāniyan (délivrance) + fatwā 1140 ---
chk("fiqh2 moindre délivrance au jet + 1226", "at-taḥallulu l-aṣġaru yaḥṣulu bi-ramyi ǧamrati l-ʿAqabati yawma l-ʿĪd" in hn and "n° 1226" in hn)
chk("1226 discours de ʿUmar à ʿArafa", "ḫaṭaba n-nāsa bi-ʿArafah" in hn and "iḏā jiʾtum min Minā" in hn and "fa-qad ḥalla lahu mā ḥurrima ʿalayhi l-ḥāǧǧu illā n-nisāʾa wa-ṭ-ṭīb" in hn)
chk("1226 nul ne touche avant le ṭawāf", "lā yamassa aḥadun nisāʾahu wa-lā ṭīban ḥattā yaṭūfa bi-l-bayt" in hn)
chk("fiqh2 restes + fin de la délivrance", "illā n-nisāʾa wa-ṭ-ṭība wa-ṣ-ṣayd" in hn and "nihāyatu t-taḥallul" in hn and "wa-karraha-hu Mālik faqaṭ" in hn)
chk("fiqh2 āya al-Māʾida 95 / imprimé 97 (+2 consigné)", "lā taqtulū ṣ-ṣayda wa-antum ḥurum" in hn and "al-Māʾida 95 du cache ḥafṣ" in hn and "l’āya 97" in hn and "+2" in hn)
chk("fiqh2 majeure par l’Ifāḍa seul", "wa-ammā t-taḥallulu l-akbaru min ǧamīʿi maḥẓūrāti l-iḥrām" in hn and "fa-lā yaḥṣulu illā bi-ṭawāfi l-ifāḍah" in hn)
chk("fatwā 1140 règle connectée (oubli + nisāʾ + ʿumra + hady)", "n° 1140" in hn and "nasiya ṭawāfa l-ifāḍah" in hn and "aṣāba n-nisāʾ" in hn and "l-yaʿtamir wa-l-yuhd" in hn and "règle connectée" in hn)
chk("fatwā 1140 provenance p.128 consignée (jamais re-numérotée)", "p.128" in hn and "jamais re-numérotée" in hn)
chk("fiqh2 1186 triade + consensus", "n° 1186" in hn and "man ʿaqaṣa raʾsahū aw ḍafara aw labbada" in hn and "fa-qad waǧabat ʿalayhi l-ḥalāq" in hn and "l-ǧumhūr" in hn)
chk("fiqh2 1185 natté + feutrage + ressemblance", "n° 1185" in hn and "man ḍaffara raʾsahū" in hn and "fa-l-yaḥliq" in hn and "wa-lā tuašabbahū bi-t-talbīd" in hn and "man tašabbaha bihī" in hn)
chk("fiqh2 triade ẓafarahū/ḍafara divergence consignée", "ẓafarahū" in hn and "ḍafara" in hn and "divergence" in hn)

# --- 8) évaluation + exploitation + iʿdād suivant ---
chk("taqwīm q1 ordre pratique", "bi-t-tartībi l-ʿamalī" in hn)
chk("taqwīm q3 pèlerin a approché son épouse + preuve", "bāšara ahlahū baʿda ramyi ǧamrati l-ʿAqabati wa-qabla ṭawāfi l-ifāḍah" in hn and "maʿa l-istidlāl" in hn)
chk("taqwīm q3 réponse : 1226 + régulateur 1128/1129/1136/1138", "n° 1128" in hn and "n° 1129" in hn and "n° 1136" in hn and "n° 1138" in hn and "ʿumra et la bête" in hn)
chk("taqwīm verbe « approché » tranché (lecture récusée)", "a approché son épouse" in hn and "récusée" in hn)
chk("exploitation athar 1183 + à Médine + ignorance", "n° 1183" in hn and "laqiya raǧulan min ahlihī bi-l-Madīnah" in hn and "qad afaḍa wa-lam yaḥliq wa-lam yuqaṣṣir" in hn and "ǧahlan" in hn)
chk("1183 ordre retour + Ifāḍa acquise", "an yarǧiʿa fa-yaḥliqa aw yuqaṣṣira" in hn and "ṯumma yarǧiʿu ilā lladhī qad afaḍa" in hn)
chk("exploitation invite Zarqānī", "ataʾammalu n-naṣṣ" in hn and "šarḥi z-Zarqānī" in hn)
chk("exploitation bandeau al-istiṯmār (lecture récusée)", "al-istiṯmār" in hn and "al-istišhād" in hn and "récusée" in hn)
chk("exercices ×2 à preuve (istiḫlāṣ + taqwīm)", "istiḫlāṣ al-muḍāmīn" in hn and "at-taqwīm" in hn and "preuve" in hn)
chk("iʿdād suivant ×2 : deux sortes + rasage/coupe", "nawʿayi t-taḥallul" in hn and "ḥukma l-ḥalāqi wa-t-taqṣīri wa-ṣifatahimā" in hn)
chk("iʿdād 3e question cherchée inexistante (consigné)", "une troisième cherchée" in hn)
chk("iʿdād lien leçon 20 slot 409", "pdf-mut23h2x-409" in hn and "Les règles de la tonsure et de la coupe" in hn)

# --- 9) apparat ---
chk("apparat numéros tranchés chiffre par chiffre", "chiffre par chiffre" in hn and "tr-tmp/vlm-408/" in hn)
chk("apparat 56 lectures + r684", "cinquante-six lectures" in hn and "r684" in hn and "qa-crops-r684" in hn)
chk("apparat bornes p.129/p.136 sondées", "p.129" in hn and "jamais devinée" in hn)
chk("apparat dates 41/45 image", "4-1" in hn and "4-5" in hn)
chk("apparat qa browser r684", "qa-r684-408-{desktop,mobile}.png" in hn)
chk("apparat WIP-10min (3 pushes)", "WIP-10min" in hn and "trois pushes WIP" in hn)
chk("apparat PARALLÈLE maintenu slot 405/409", "PARALLÈLE" in hn and "405" in hn)

# --- 10) typographie ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F]", re.sub(r"\uFDFA", "", h)))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))

# --- 11) registre : pas de doublon ---
d = json.load(open(REG, encoding="utf-8"))
les = d.get("lessons", d if isinstance(d, list) else [])
mine = [l for l in les if str(l.get("docId") or "") == "pdf-mut23h2x-408"]
chk("registre contient slot 408", len(mine) == 1)
if mine:
    chk("408 htmlFr vide avant hand-set", mine[0].get("htmlFr") in (None, ""))
done = sum(1 for l in les if l.get("htmlFr"))
chk("doublons impossibles (17 livrées avant hand-set)", done == 17)
voisins = [l for l in les if str(l.get("docId") or "") in ("pdf-mut23h2x-407", "pdf-mut23h2x-409")]
chk("voisins 407 livré / 409 non livré", voisins and len(voisins) == 2 and voisins[0].get("htmlFr") and not voisins[1].get("htmlFr"))

# --- 12) claim actif ---
c = open(CLAIM, encoding="utf-8").read()
chk("claim 408 trace r684", "subagent-r684-408" in c)

print(f"VERIFY pdf-408 : {ok} OK, {fail} échecs")
