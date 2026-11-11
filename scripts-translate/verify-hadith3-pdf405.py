# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-405
(les rites des journées à Minā (2) — أعمال أيام منى (2), leçon 16 imprimée,
p.110-116 du manuel hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé
29 slots pdf-mut23h2x-390..418) : bornes p.110-116 (p.117 = leçon 17/406
« أحكام الهدي (1) » — médaillon 17 + objectifs, borne supérieure exclusive) ;
15 numéros du Muwaṭṭaʾ tranchés chiffre par chiffre (1209, 1210, 1211, 1212,
1213, 1214, 1216, 1217, 1218, 1219, 1220, 1221, 1223, 1224, 1225 — 1215/1222
absents de l'imprimé, consigné) ; aucune āya — cache ḥafṣ non mobilisé ; notice
Nāfiʿ 117 H ; adjudications image r685 (isnād 1221 ʿĀṣim b. ʿUmar, al-baytūta
contre al-bayna du canon, tachattara contre tanāsara, ṣarraḥa, khadhf/ḥadhf,
samiʾa, ya-khburu, yuhʾrīqu damāʾa contre yuhdī dumiyyatan, an turmā, b. ʿUmar
contre b. ʿAmr, Abū Bakr b. Nāfiʿ, bintu akhī li-Ṣafiyyata, min aḥadi manāsiki
l-ḥajj, naʾam, al-aʾimmati l-arbaʾa) ; convention phonétique R685 (j, ch, ',
gh, kh, th, dh + ā ī ū + ḥ ṣ ḍ ṭ ẓ) ; 0 arabe hors spans lang="ar", 0 apostrophe
droite, guillemets appariés.
Usage: python3 scripts-translate/verify-hadith3-pdf405.py [--pre-handset]
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-405-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-405.claim.json"

PRE = "--pre-handset" in sys.argv

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
# normalisation apostrophes : le brouillon porte U+2019 après qa-lesson.py
hn = hn.replace("\u2019", "'")
hnt = re.sub(r" +", " ", re.sub(r"<[^>]+>", "", hn))

# --- 1) squelette ---
chk("h1 Leçon 16", "<h1>Leçon 16" in hn and "les rites des journées à Minā (2)" in hnt)
chk("h1 translit imprimée", "a'māl ayyām Minā (2)" in hnt)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.110-116", "p.110-116" in hnt)
chk("meta slot 405", "pdf-mut23h2x-405" in hnt)
chk("meta 19e slot / compteur 18/29", "dix-neuvième leçon livrée" in hnt and "compteur 18/29" in hnt)
chk("meta takeover trace r685", "R685-main-1a1cbd7356c09219" in hnt and "takeover" in hnt)
chk("meta claim r685 périmé", "subagent-r685-405" in hnt and "22h07 UTC" in hnt)
chk("meta borne sup p.117 sondée", "p.117" in hnt and "borne supérieure" in hnt)
chk("meta voisins 404/406", "Les rites des journées à Minā (1)" in hnt and "pdf-mut23h2x-406" in hnt)
chk("meta doctrine WIP-10min", "WIP-10min" in hnt and "~10 minutes" in hnt)
chk("meta convention phonétique R685", "convention phonétique R685" in hnt)
chk("meta extraction 2 couches", "h3-405-readable.txt" in hnt and "12 529 car" in hnt)
chk("meta bandes VLM 405", "vlm-405" in hnt and "b110-b116" in hnt)
chk("meta crops r685 déframés récusés", "déframés" in hnt and "récusés" in hnt)
chk("meta 8 micro-crops 600 dpi", "m-H-tamhid" in hnt and "m-F-dumiya" in hnt and "m-D2-khidhf" in hnt)
chk("meta OCR inversés consignés", "9021" in hnt and "2121" in hnt and "4221" in hnt and "5221" in hnt)
chk("meta 1215/1222 absents", "1215 et 1222 n'apparaissent pas" in hnt)
chk("meta date 117 H", "117 H" in hnt and "711" in hnt)
chk("meta token absent / bundle", "token push ABSENT" in hnt and "bundle de sûreté" in hnt)
chk("meta PARALLÈLE: 1", "PARALLÈLE" in hnt and "1" in hnt)

# --- 2) objectifs ---
chk("obj 1 mabīt", "an ata'arrafa ḥukma al-mabīt bi-Minā ayyāma ramyi al-jamār" in hnt)
chk("obj 2 ṣifat ar-ramy", "an ata'arrafa ṣifata ramyi al-jamār wa-aḥkāmahu" in hnt)
chk("obj 3 ādāb", "an altazima al-ādāb al-islāmiyya" in hnt and "wa-l-mabīt bi-Minā" in hnt)
chk("médaillon 16", "le nombre 16" in hnt and "16 lu sur image" in hnt)

# --- 3) tamhīd ---
chk("tamhīd min aḥadi manāsiki al-ḥajj", "ayyām min aḥadi manāsiki al-ḥajj" in hnt and "l'imprimé tenu tel quel" in hnt)
chk("tamhīd taqarruban", "taqarruban ilā Allāhi subḥānahu" in hnt)
chk("tamhīd iqtidāʾ", "wa-iqtidā'an bi-n-nabiyyi ﷺ" in hnt)
chk("tamhīd tadhkira Ibrāhīm", "tadhkiratun li-qiṣṣati Ibrāhīma" in hnt)
chk("tamhīd 3 questions", "ṣifatu ramyi al-jamār" in hnt and "wa-mā ādābuh" in hnt and "ḥukmu al-mabīt bi-Minā ayyāma ar-ramy" in hnt)

# --- 4) textes du cours ---
chk("texte 1209 intro", "Premier texte" in hnt and "n° 1209" in hnt)
chk("1209 za'amū 'Umar", "za'amū anna 'Umara bna al-Khaṭṭāb qāla" in hnt)
chk("1209 lā yabītanna", "lā yabītanna aḥadun mina al-ḥājji layāliya Minā min warā'i al-'Aqaba" in hnt)
chk("texte 1221 intro", "Deuxième texte" in hnt and "n° 1221" in hnt)
chk("1221 isnād", "b. Abī Bakr b. Ḥazm, d'après son père" in hnt and "'Āṣim b. 'Umar, d'après son père" in hnt)
chk("1221 ar-khaṣa bouviers", "ar-khaṣa li-ru'ā'i al-ibīl" in hnt and "khārijīna 'an Minā" in hnt)
chk("1221 calendrier", "yarmūna yawma an-naḥr" in hnt and "thumma yarmūna al-ghad" in hnt and "li-yawmayn" in hnt and "yarmūna yawma an-nafar" in hnt)
chk("1221 baytūta/bayna consigné", "al-baytūta" in hnt and "al-bayna" in hnt and "écart consigné jamais corrigé" in hnt)
chk("couches récusées isnād", "'Ubayd Allāh" in hnt and "Abū l-Badāḥ" in hnt)
chk("texte 1212 intro", "Troisième texte" in hnt and "n° 1212" in hnt)
chk("1212 yaqīf jamratayn", "yaqifu 'inda al-jamratayn al-ūlayayn wuqūfan ṭawīlan" in hnt)
chk("1212 takbīr/tasbīḥ/ḥamd/du'āʾ", "yukabbiru Allāha" in hnt and "wa-yusabbiḥuhu" in hnt and "wa-yaḥmaduhu" in hnt and "wa-yad'ū Allāha" in hnt)
chk("1212 lā yaqīf 'Aqaba", "wa-lā yaqifu 'inda jamrati al-'Aqaba" in hnt)
chk("1212 b. 'Umar + bande 'Amr récusée", "la bande « b. 'Amr » récusée" in hnt)
chk("texte 1224 intro", "Quatrième texte" in hnt and "n° 1224" in hnt)
chk("1224 isnād Abū Bakr b. Nāfiʿ", "Abū Bakr b. Nāfi', d'après son père" in hnt and "la bande « Ibn Bakr b. Nāfi' » récusée" in hnt)
chk("1224 incipit Ṣafiyya", "bintu akhī li-Ṣafiyyata binti Abī 'Ubayd" in hnt)
chk("1224 nafasat + Muzdalifa", "nafasat" in hnt and "al-Muzdalifa" in hnt)
chk("1224 gharabat ach-chams", "gharabati ach-chamsu min yawmi an-naḥr" in hnt)
chk("1224 ordre + nulle chose", "an tarmiyā al-jamrata ḥīna atatā" in hnt and "wa-lam yar 'alayhimā chay'an" in hnt)

# --- 5) notice Nāfiʿ ---
chk("notice intro", "tarjamat ar-rāwī" in hnt)
chk("Nāfiʿ mawlā + rāwīyatihi", "mawlā 'Abdi Allāhi bni 'Umar wa-rāwīyatih" in hnt)
chk("Nāfiʿ a'immat at-tābi'īn", "min a'immati at-tābi'īn bi-l-Madīna" in hnt)
chk("Nāfiʿ Daylamī", "Daylamī al-aṣl" in hnt)
chk("Nāfiʿ 'allāma + thiqa", "'allāmatan fī al-fiqh" in hnt and "thiqa" in hnt)
chk("Mālik fa-khtim", "idhā qāla Nāfi'un chay'an fa-khtim 'alayh" in hnt)
chk("Bukhārī aṣaḥḥu al-asānīd", "aṣaḥḥu al-asānīd kulluhā Mālikun 'an Nāfi'in 'ani bni 'Umar" in hnt)
chk("Nāfiʿ charges", "ṣadaqāt al-Yaman" in hnt and "li-yu'allima ahlahā as-sunna" in hnt)
chk("Nāfiʿ 117 H", "tuwuffiya sanata 117 H" in hnt)

# --- 6) gloses ---
chk("glose al-'Aqaba bay'a", "makān mubāya'ati al-Anṣār li-n-nabiyyi ﷺ 'alā al-hijra" in hnt)
chk("glose al-jamār", "jam'u jamratin" in hnt and "al-ḥajaru aṣ-ṣaghīr" in hnt and "mujtama'i al-ḥaṣā" in hnt)
chk("glose nafastu", "wa-nafastu waladtu" in hnt and "fa-yuḍamm an-nūn faqaṭ" in hnt)
chk("glose al-baytūta", "maṣdaru bāta yabītu" in hnt and "wa-biyattu baytūtatan idhā dakhala fī al-layl" in hnt)
chk("glose yawm at-tafarr", "yawm al-inṣirāf min Minā" in hnt)

# --- 7) istikhlāṣ ---
chk("istikhlāṣ 3 items", "ubīnu ḥukma al-mabīt bi-Minā ayyāma ar-ramy" in hnt
    and "ubīnu ṣifata ar-ramy wa-ādābah" in hnt and "ubīnu ḥukm ta'khīri ar-ramy" in hnt)

# --- 8) fiqh premièrement : le séjour ---
chk("fiqh awwalan", "awwalan : al-mabīt bi-Minā ayyām ar-ramy" in hnt)
chk("3 nuits/2 nuits wājib", "thalāthu layālin li-man lam yata'ajjal" in hnt
    and "wa-lilaytayni li-l-muta'ajjil" in hnt and "wājibun min wājibāti al-ḥajj" in hnt)
chk("dam fa-man tarakahu", "fa-man tarakahu ra'san aw jalla laylatan fa-'alayhi ad-dam" in hnt
    and "hady 'an kulli laylatin" in hnt)
chk("preuve 1210 Hichām", "Hichām b. 'Urwa" in hnt and "lā yabītanna aḥadun illā bi-Minā" in hnt
    and "[al-Muwaṭṭa', n° 1210]" in hnt)
chk("mabīt li-ḍarūratin", "wa-law li-ḍarūratin" in hnt and "ka-l-marḍi wa-l-khawfi 'alā al-matā'" in hnt)
chk("ḥabasahu marḍun", "ḥabasahu marḍun fa-bāta bi-Makkati fa-'alayhi hady" in hnt
    and "illā man rak-khaṣa lahumu an-nabiyyu ﷺ" in hnt)
chk("re-citation 1221", "la re-citation du second texte du cours (n° 1221)" in hnt)
chk("tafsīr Mālik 1223", "wa-tafsīru al-ḥadīth alladhī ar-khaṣa fīhi rasūlu Allāhi ﷺ" in hnt
    and "fīmā narā wa-Allāhu a'lam" in hnt)
chk("tafsīr calendrier", "ramaw mina al-ghad" in hnt and "yawmu an-nafar al-awwal" in hnt
    and "li-l-yawmi alladhī maḍā" in hnt)
chk("lā yaqḍī avant wujūb", "lā yaqḍī aḥadun chay'an ḥattā yajiba 'alayh" in hnt
    and "al-qaḍā'u ba'da dhālika" in hnt)
chk("farreghū / nafarū", "fa-qad farreghū" in hnt and "yawma an-nafar al-ākhir wa-nafarū" in hnt)
chk("extension aux excuses", "ahlu al-a'dhār al-ukhrā ghayr ar-ra'y" in hnt)

# --- 9) fiqh deuxièmement : le jet ---
chk("fiqh thāniyan", "Deuxièmement : le jet des jamarāt (ramy al-jamār)" in hnt)
chk("temps lā turmā", "lā turmā al-jamār fī al-ayyām ath-thalātha li-ghayri al-muta'ajjil" in hnt
    and "wa-l-yawmayni li-l-muta'ajjil" in hnt)
chk("recommandé avant ẓuhr", "wa-yustahabbu ramyuhā qabla ṣalāti aẓ-ẓuhr" in hnt)
chk("réitération 4 imams", "a'āda ramyahā 'inda al-a'immati al-arba'a" in hnt)
chk("1220 ḥattā tazūla ach-chams", "ḥattā tazūla ach-chams" in hnt and "[al-Muwaṭṭa', n° 1220]" in hnt)
chk("an turmā + bande narmī récusée", "an turmā" in hnt and "la bande « an narmī » récusée" in hnt)
chk("1217 min ḥaythu tachattara", "min ḥaythu tachattara" in hnt and "[al-Muwaṭṭa', n° 1217]" in hnt)
chk("canon tanāsara consigné", "tanāsara" in hnt and "divergence d'imprimé consignée" in hnt)
chk("ṣarraḥa + baṭn al-wādī", "ṣarraḥa" in hnt and "min baṭn al-wādī" in hnt and "la bande « ṣaḥḥa » récusée" in hnt)
chk("4 singularités", "ikhtiṣāṣuhā bi-yawmi an-naḥr" in hnt and "wa-an lā yūqafa 'indahā" in hnt
    and "wa-turmā ḍuḥan in umkin" in hnt and "wa-min asfaliha nadban 'inda al-imkān" in hnt)

# --- 10) manière du jet ---
chk("zālati ach-chams thāniya", "idhā zālati ach-chams thāniya ayyāmi an-naḥr" in hnt)
chk("māchiyan mutawaḍḍi'an qabla ẓuhr", "māchiyan mutawaḍḍi'an qabla ṣalāti aẓ-ẓuhr" in hnt)
chk("21 cailloux", "wa-ma'ahu iḥdā wa-'ichrīna ḥaṣātan" in hnt)
chk("1re jamra masjid Minā", "fa-yabtadī bi-al-jamrati al-ūlā" in hnt and "allatī talī masjidi Minā" in hnt)
chk("qibla + du'āʾ", "mustaqbilu al-qibla" in hnt and "wa-yad'ū" in hnt)
chk("wusṭā + chamālan", "al-jamrata al-wusṭā" in hnt and "chamālan wa-yad'ū" in hnt)
chk("'Aqaba 7 cailloux", "bi-sab'i ḥaṣayātin ayḍan" in hnt)
chk("3 jours + ta'ajjul condition", "wa-hākadhā yaf'alu thalātha ayyāmi an-naḥr" in hnt
    and "laylata ar-rābi'a" in hnt and "bi-charti al-khurūj min Minā qabla al-ghurūb" in hnt
    and "wa-illā lazimahu al-mabīt bi-Minā wa-ramyu al-yawm ar-rābi'" in hnt)
chk("1211 'Umar waqūf", "ḥattā yamalla al-qā'im" in hnt and "[al-Muwaṭṭa', n° 1211]" in hnt)
chk("1213 takbīr chaque caillou", "kullamā ramā bi-ḥaṣātin" in hnt and "[al-Muwaṭṭa', n° 1213]" in hnt)
chk("1214 khidhf", "mithlu ḥaṣā al-khadhf" in hnt and "[al-Muwaṭṭa', n° 1214]" in hnt)
chk("1214 a'jaba ilayy", "wa-akbaru min dhālika qalīlan a'jaba ilayy" in hnt)
chk("khidhf/ḥadhf divergence interne", "ḥaṣā al-ḥadhf" in hnt and "divergence interne de l'imprimé" in hnt)
chk("samiʾa + bande summiʾa récusée + canon", "sami'a" in hnt and "la bande « summi'a » récusée" in hnt)
chk("istaḥabba + ichtiyāṭ + ḥajar", "fa-staḥabba Mālikun" in hnt and "ichtiyāṭ" in hnt
    and "mā lā yaṣduqu 'alayhi ismu ḥajarin" in hnt)
chk("1219 ṭahāra", "tastahabbu aṭ-ṭahāra 'inda ramyi al-jamār" in hnt
    and "lā arā 'alā alladhī yarmī al-jamār aw yachā bayna aṣ-Ṣafā wa-al-Marwa" in hnt
    and "i'ādatan" in hnt and "lā yata'ammud dhālika" in hnt and "[al-Muwaṭṭa', n° 1219]" in hnt)
chk("1216 machy", "machaw dhāhibīna wa-rāji'īn" in hnt
    and "wa-awwalu man rakiba Mu'āwiyatu bnu Abī Sufyān" in hnt and "[al-Muwaṭṭa', n° 1216]" in hnt)
chk("murād ṣaḥāba + ya-khburu", "wa-murāduh bi-an-nās aṣ-ṣaḥāba" in hnt
    and "ya-khburu anna an-nabiyya ﷺ fa'ala dhālika" in hnt)
chk("yakhruju bandes récusées", "les bandes « yakhruju » récusées" in hnt)
chk("Muʿāwiya li-ḍarūratin", "fa-kāna li-ḍarūratin" in hnt)

# --- 11) garçon et malade ---
chk("1218 ṣiḥḥa + ḥaml", "yaṣiḥḥu ar-ramy 'ani aṣ-ṣabī wa-al-marīḍ" in hnt
    and "in lam yamkun ḥamluhumā" in hnt and "wa-ramayā bi-anfusihimā" in hnt)
chk("1218 naʾam + mutaḥarrā", "na'am" in hnt and "wa-yataḥarrā al-marīḍ ḥīna yurmā 'anhu" in hnt
    and "fa-yukabbiru wa-huwa fī manzilihi" in hnt)
chk("1218 yuhʾrīqu damāʾa + canon dumiyya", "wa-yuh'rīqu damā'a" in hnt
    and "wa-yuhdī dumiyyatan" in hnt and "divergence d'imprimé consignée" in hnt)
chk("1218 tachrīq + ramā + ahdā", "fī ayyāmi at-tachrīq" in hnt
    and "ramā alladhī ramā 'anhu" in hnt and "wa-ahdā" in hnt and "[al-Muwaṭṭa', n° 1218]" in hnt)
chk("naʾam double lecture", "double lecture concordante" in hnt)

# --- 12) troisièmement ---
chk("fiqh thālithan", "Troisièmement : le report du jet de la Jamra de al-'Aqaba pour excuse" in hnt)
chk("re-citation 1224", "la re-citation du quatrième texte du cours (n° 1224)" in hnt)
chk("adrakatā qaḍāʾ + ḥabasahumā", "adrakatā waqta al-qaḍā'i ar-ramy" in hnt and "ḥabasahumā al-'udhr" in hnt)
chk("yustahabb ḥady Ṣafiyya", "yustahabbu 'inda Mālik" in hnt
    and "mithlu mā 'araḍa li-Ṣafiyyata an yahdiya" in hnt)
chk("lam yarmi al-waqt al-maṭlūb", "lam yarmi fī al-waqt al-maṭlūb" in hnt)

# --- 13) taqwīm ---
chk("taqwīm 2 questions", "at-taqwīm" in hnt and "deux questions" in hnt and "istidlāl" in hnt)
chk("cas 1 pèlerin day/night", "ḥājj yaḥḍuru nahāran li-ramyi al-jamarāt" in hnt
    and "yadhhabu li-l-bayt bi-Makkata thumma ya'ūdu ṣabāḥan ilā Minā" in hnt)
chk("cas 1 preuve 1210", "n° 1210" in hnt and "un hady" in hnt)
chk("cas 2 wuḍūʾ rompu", "intaqaḍa wuḍū' ḥājjin athnā'a ramyi al-jamrati al-wusṭā" in hnt)
chk("cas 2 preuve 1219", "n° 1219" in hnt and "valide et n'est point réitéré" in hnt)

# --- 14) istithmār 1225 ---
chk("istithmār bandeau", "al-istithmār" in hnt and "l'exploitation" in hnt)
chk("1225 suʾila nasīya", "su'ila Mālikun 'an man nasiya jamratan mina al-jamār" in hnt
    and "ḥattā umsī" in hnt and "[al-Muwaṭṭa', n° 1225]" in hnt)
chk("1225 ayya sāʿa", "l-yarji' ayya sā'ata dhakaraha min laylin aw nahār" in hnt)
chk("1225 ka-mā ṣalāt", "kamā yuṣallī aṣ-ṣalāt idhā nasiyahā" in hnt)
chk("1225 baʿda ṣadara + hady", "ba'da mā ṣadara wa-huwa bi-Makkata" in hnt and "fa-'alayhi al-hady" in hnt)
chk("invite atāmmalu", "ata'ammalu an-naṣṣ wa-ubīnu naw'a ad-dalīl" in hnt)
chk("type de preuve", "l'analogie du rite au rite" in hnt and "la règle du lieu" in hnt)

# --- 15) iʿdād ---
chk("iʿdād consigne coquille muqbūl", "al-muqbūl" in hnt and "coquille d'imprimé" in hnt)
chk("iʿdād 3 entrées", "natadjjatha" in hnt and "at-taqlīd" in hnt and "al-ich'ār" in hnt)
chk("iʿdād mustaysar", "al-mustaysar min al-hady" in hnt)
chk("relais leçon 17", "Les règles de la bête d'offrande (hady) (1)" in hnt and "pdf-mut23h2x-406" in hnt)
chk("3 occurrences hady", "la bête des nuits manquées" in hnt and "le hady recommandé de l'accouchée" in hnt
    and "le hady de l'oubli" in hnt)

# --- 16) apparat ---
chk("apparat présent", "L'apparat de preuve de la livraison" in hnt)
chk("apparat bornes 110-116 + 117", "p.110-116" in hnt and "p.117 ouvre la leçon 17" in hnt)
chk("apparat 15 numéros", all(n in hnt for n in
    ["1209", "1210", "1211", "1212", "1213", "1214", "1216", "1217", "1218", "1219", "1220", "1221", "1223", "1224", "1225"]))
chk("apparat R511 sans objet", "doctrine R511 sans objet" in hnt)
chk("apparat versets aucun", "aucune āya" in hnt or "ne cite pas d'āya" in hnt)

# --- 17) claim + registre ---
try:
    c = json.load(open(CLAIM, encoding="utf-8"))
    chk("claim trace", c.get("trace_id") == "R685-main-1a1cbd7356c09219")
except Exception as e:  # noqa: BLE001
    chk(f"claim lisible ({e})", False)

data = json.load(open(REG, encoding="utf-8"))
les = {l.get("docId"): l for l in data["lessons"]}
chk("registre slot 405 connu", "pdf-mut23h2x-405" in les)
if PRE:
    chk("GARDE-DOUBLON htmlFr vide avant pose", not (les["pdf-mut23h2x-405"].get("htmlFr") or "").strip())
else:
    chk("htmlFr posée", len((les["pdf-mut23h2x-405"].get("htmlFr") or "")) > 40000)
n_done = sum(1 for l in data["lessons"] if (l.get("htmlFr") or "").strip())
chk("compteur hadith-3es", (n_done == 18) if PRE else (n_done == 19))

# --- 18) typographie (double contrôle) ---
chk("0 apostrophe droite", "'" not in re.sub(r"<[^>]+>", "", h))
chk("guillemets appariés", h.count("«") == h.count("»"))
AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
chk("0 arabe hors spans", not AR.search(re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', h)))
chk("0 gaucha/0 cyrillique", not re.search(r"[а-яА-Я]", h))
chk("size plausible", 70000 < len(h) < 120000)

print(f"\nverify-hadith3-pdf405 : {ok} PASS / {fail} ÉCHEC")
if fail:
    sys.exit(1)
print("PASS — leçon 405 conforme à la méthode R657-R685")
