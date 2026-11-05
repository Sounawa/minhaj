#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-133
(le ḥadīṯ mudraǧ, p.108-112 du manuel ulum-hadith-1-thanawi.pdf) :
bannière « ad-dars 22 » ; bornes p.108-112 par DOUBLE sondage (bannière ad-dars
23 + objectifs المُدَبَّج lus à l'OCR p.113, concordants avec l'iʿdād qablī p.112
المدبج ×2) ; bayt — « wa-l-mudraǧātu fī l-ḥadīṯi mā atat *** min baʿḍi alfāẓi
r-ruwāti ttaṣalat » tranché image (OCR psm6 « aqat » récusé, rendu ×2 bannière
p.108 + reprise p.109) ; glose (mudraǧ, ism mafʿūl, adraǧa) ; istikhlāṣ ×2 ;
taḥlīl : définition (types faibles, ajout sans séparation, nom transmetteur /
fil isnād / isnād étranger / phrase explicative), condition (non-distinction,
totalité du Prophète ﷺ), émanations (Compagnon/Successeur, mot rare, sens
obscur, compréhension crainte) ; divisions : sanad ×4 formes (1° ʿĀṣim ibn
Kulayb → Wāʾil ibn Ḥuǧr « ṯumma ǧiʾtuhum » [Sunan Abī Dāwūd, rafʿ al-yadayn],
ʿĀṣim ibn ʿAbd al-Ǧabbār, Zuhayr ibn Muʿāwiya, Mūsā ibn Hārūn al-Ḥimmāl, wahm,
Ibn aṣ-Ṣalāḥ — « Wāʾil ibn 2 » récusé image ; 2° Saʿīd ibn Abī Maryam « lā
tabāġaḍū » [al-Muwaṭṭaʾ], Abū az-Zinād, al-Aʿraǧ, « iyyākum wa-ẓ-ẓann »,
al-Ḫaṭīb — « tabāʿaḍū » psm6 récusé image ; 3° Ibn Masʿūd « saʾaltu n-nabiyya
ﷺ… an tazāniya ḫalīlata ǧārik » [Ṣaḥīḥ al-Buḫārī, tafsīr, al-Baqara : 22 telle
qu'imprimée], al-Aʿmaš + Manṣūr ibn al-Muʿtamar + Šuqaym + ʿAmr ibn Šurahbīl,
Wāṣil al-Asadī omettant ʿAmr, aṯ-Ṯawrī, al-Qaṭṭān — fin « wa-ruwiya ʿani
l-Aʿmaš annahu asqata » découverte image 600 dpi, « an turāniya » psm4 récusé ;
4° incident + propos propre « fayurwā ʿanhu ka-ḏālika », sans exemple imprimé,
gap p.110→p.111 résolu image) ; matn ×3 formes (1° « asbiġū l-wuḍūʾa waylun
li-l-aʿqābi mina n-nār » [Ṣaḥīḥ al-Buḫārī, ġasl al-aʿqāb], Šabbāba ibn Sawwār,
Muḥammad ibn Ziyād, Abū l-Qāsim ﷺ ; 2° Hišām ibn ʿUrwa, Buṣra bint Ṣafwān « man
masssa ḏakarahu aw anṯaytih aw rifġahu fal-yatawaḍḍaʾ » [Sunan al-Bayhaqī],
additions de ʿUrwa, Ayyūb + Ḥammād ibn Zayd, restreint tenu ; 3° al-Ḥasan ibn
al-Ḥurr + al-Qāsim ibn Muḫāmira + ʿAlqama « iḏan qulta hāḏā aw qaḍayta hāḏā
faqad qaḍayta ṣalātak, in šiʾta an taqūma faqum, wa-in šiʾta an taqʿuda
faqʿud » [Sunan Abī Dāwūd, at-tašahhud], Zuhayr interpolé sans séparation,
ʿAbd ar-Raḥmān ibn Ṯābit de Ṯawbān, an-Nawawī accord des ḥuffāẓ — « kulta/
faq/tafʿud » OCR récusés image) ; clôture (interdiction du taʿammud, qāḍī
Zakariyyā al-Anṣārī, az-Zuhrī) ; taqwīm ×3 (image, Q1 à 4800 dpi « al-mudraǧ »
rāʾ ≠ bāʾ) ; istiṯmār (Ibn Ḥaǧar [Nuzhat an-naẓar, p. 116], vocalisation
« yuʿrafu l-idrāǧu », consigne unique) ; iʿdād qablī (mudabbaǧ ×2) ; bornes
p.108-112 ; ﷺ tenu (U+FDFA ×13), zéro āya rendue, zéro résidu.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf133.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-133-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")


h = open(HTML, encoding="utf-8").read()
plain = re.sub(r"[\s\u202f\u00a0]+", " ", h.replace("&nbsp;", " "))

# 1. h1 aligné au titleFr pré-mappé du registre
tf = [l for l in json.load(open(REG, encoding="utf-8"))["lessons"]
      if l["docId"] == "pdf-mut23h2q-133"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 22", "leçon 22" in (m.group(1) if m else ""))

# 2. bannière / bornes
chk("badge ad-dars 22", "ad-dars 22" in plain)
chk("bornes p.108-112 documentées", "page imprimée 108" in plain and "page 112" in plain)
chk("bannière ad-dars 23 p.113 (sondage)", "ad-dars 23" in plain and "page 113" in plain)
chk("double sondage (jamais deviné)", "double sondage" in plain and "jamais devinée" in plain)
chk("concordance iʿdād qablī p.112", "concordants" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. tamhīd
chk("tamhīd : Sunna révélation killa", "en un seul bloc (killa)" in plain)
chk("tamhīd : yudriǧūna", "interpolent (yudriǧūna)" in plain)
chk("tamhīd question double", "Par quel nom se nomme donc le ḥadīṯ" in plain)

# 4. bayt
chk("bayt : wa-l-mudraǧātu fī l-ḥadīṯi mā atat", "wa-l-mudraǧātu fī l-ḥadīṯi mā atat" in plain)
chk("bayt : min baʿḍi alfāẓi r-ruwāti ttaṣalat", "min baʿḍi alfāẓi r-ruwāti ttaṣalat" in plain)
chk("OCR aqat récusé (image)", "mā aqat" in plain and "récusée" in plain)
chk("bayt rendu deux fois (bannière + reprise)", "concordante avec la bannière p.108" in plain)
chk("traduction bayt", "quelques formules des transmetteurs" in plain)

# 5. glose
chk("glose : pluriel de mudraǧ", "pluriel de mudraǧ" in plain)
chk("glose : ism mafʿūl de adraǧa", "participe passif (ism mafʿūl) de adraǧa" in plain)

# 6. istikhlāṣ ×2
chk("istikhlāṣ deux questions", "sous la forme de deux questions" in plain)
chk("IS1 maqṣūd", "Qu’est-ce qui est visé par le ḥadīṯ mudraǧ" in plain)
chk("IS2 aqsām + ḥukm", "les divisions de l’idrāǧ dans le ḥadīṯ, et quel est son jugement" in plain)

# 7. taḥlīl — définition
chk("mudraǧ du faible", "des types des ḥadīṯs faibles" in plain)
chk("définition ajout sans séparation", "sans séparation ni explicitation" in plain)
chk("nom d’un transmetteur déterminé", "le nom d’un transmetteur déterminé" in plain)
chk("fil de l’isnād altéré", "altéré le fil de l’isnād" in plain)
chk("isnād qui n’est pas le sien", "un autre isnād qui n’est pas le sien" in plain)
chk("phrase explicative du matn", "phrase explicative sans l’annoncer" in plain)
chk("condition non-distinction", "la non-distinction de cette addition" in plain)
chk("condition totalité du Prophète", "la totalité provient du Prophète ﷺ" in plain)
chk("émanations Compagnon/Successeur", "du Compagnon, du Successeur ou de qui se situe au-dessous" in plain)
chk("motifs mot rare/sens obscur/crainte", "un mot rare" in plain and "un sens obscur" in plain and "comprenne à tort" in plain)

# 8. idrāǧ sanad — 4 formes
chk("deux divisions", "un idrāǧ dans l’isnād et un idrāǧ dans le matn" in plain)
chk("4 formes sanad", "comporte quatre formes" in plain)
chk("F1 définition extrémité", "à l’exception d’une de ses extrémités" in plain)
chk("F1 ʿĀṣim ibn Kulayb", "ʿĀṣim ibn Kulayb" in plain)
chk("F1 Wāʾil ibn Ḥuǧr (OCR « 2 » récusé image)", "Wāʾil ibn Ḥuǧr" in plain)
chk("F1 ṯumma ǧiʾtuhum", "ṯumma ǧiʾtuhum baʿda ḏālika fī zamānin fīhi bardun šadīd" in plain)
chk("F1 suite matn", "fa-raʾaytu n-nāsa ʿalayhim ǧulla aṯ-ṯiyāb, taḥarraku aydīhim taḥta aṯ-ṯiyāb" in plain)
chk("F1 réf Sunan Abī Dāwūd rafʿ al-yadayn", "chapitre de l’élévation des mains dans la prière" in plain)
chk("F1 ʿĀṣim ibn ʿAbd al-Ǧabbār", "ʿĀṣim ibn ʿAbd al-Ǧabbār ibn Wāʾil" in plain)
chk("F1 Zuhayr ibn Muʿāwiya détaillé", "en le détaillant, Zuhayr ibn Muʿāwiya" in plain)
chk("F1 Mūsā ibn Hārūn al-Ḥimmāl", "Mūsā ibn Hārūn al-Ḥimmāl" in plain)
chk("F1 wahm + Ibn aṣ-Ṣalāḥ", "l’illusion (wahm) — jugement qu’Ibn aṣ-Ṣalāḥ a approuvé" in plain)
chk("F2 définition contraire", "qui lui est contraire dans l’isnād" in plain)
chk("F2 Saʿīd ibn Abī Maryam", "Saʿīd ibn Abī Maryam" in plain)
chk("F2 lā tabāġaḍū (psm6 tabāʿaḍū récusé)", "lā tabāġaḍū wa-lā taḥāsadū wa-lā tanāfasū" in plain)
chk("F2 wa-lā tanāfasū d’un autre ḥadīṯ", "Son mot « wa-lā tanāfasū » provient d’un autre ḥadīṯ" in plain)
chk("F2 Abū az-Zinād + al-Aʿraǧ", "d’Abū az-Zinād, d’al-Aʿraǧ, d’Abū Hurayra" in plain)
chk("F2 iyyākum wa-ẓ-ẓann", "iyyākum wa-ẓ-ẓann, fa-inna ẓ-ẓanna akḏaba l-ḥadīṯ" in plain)
chk("F2 réf al-Muwaṭṭaʾ", "al-Muwaṭṭaʾ, livre de l’excellent caractère" in plain)
chk("F2 al-Ḫaṭīb jzām", "al-Ḫaṭīb l’a affirmé de manière catégorique" in plain)
chk("F2 totalité des transmetteurs de Mālik", "la totalité des transmetteurs de Mālik" in plain)
chk("F3 définition isnāds différents", "selon des isnāds différents" in plain)
chk("F3 saʾaltu n-nabiyya", "saʾaltu n-nabiyya ﷺ" in plain)
chk("F3 an taǧʿala li-llāhi niddan", "an taǧʿala li-llāhi niddan wa-huwa ḫalaqak" in plain)
chk("F3 wa-an taqtula waladaka", "wa-an taqtula waladaka taḫāfu an yuṭʿima maʿak" in plain)
chk("F3 an tazāniya ḫalīlata ǧārik (psm4 turāniya récusé)", "an tazāniya ḫalīlata ǧārik" in plain)
chk("F3 réf Ṣaḥīḥ al-Buḫārī tafsīr", "Ṣaḥīḥ al-Buḫārī, livre du tafsīr" in plain)
chk("F3 réf āya imprimée al-Baqara : 22", "al-Baqara : 22" in plain and "telle quelle, translittérée" in plain)
chk("F3 al-Aʿmaš + Manṣūr ibn al-Muʿtamar", "Al-Aʿmaš et Manṣūr ibn al-Muʿtamar" in plain)
chk("F3 Šuqaym + ʿAmr ibn Šurahbīl", "de Šuqaym, de ʿAmr ibn Šurahbīl" in plain)
chk("F3 Wāṣil al-Asadī omettant ʿAmr", "Wāṣil al-Asadī le transmit de Šuqaym, d’Ibn Masʿūd, en omettant ʿAmr" in plain)
chk("F3 aṯ-Ṯawrī → interpolation", "aṯ-Ṯawrī le transmit d’eux, la transmission de Wāṣil devint une interpolation" in plain)
chk("F3 al-Qaṭṭān sépara", "Yaḥyā ibn Saʿīd al-Qaṭṭān sépara l’un des deux isnāds" in plain)
chk("F3 Wāṣil établit / al-Aʿmaš omit", "qu’il avait établi ʿAmr comme al-Aʿmaš et Manṣūr" in plain and "qu’il l’avait omis" in plain)
chk("F3 fin découverte image 600 dpi", "découverte par recadrage image à 600 dpi" in plain)
chk("F4 définition incident", "qu’un incident lui survienne, qu’il prononce des propos de son propre chef" in plain)
chk("F4 fayurwā ʿanhu ka-ḏālika", "fayurwā ʿanhu ka-ḏālika" in plain)
chk("F4 sans exemple + gap résolu", "n’imprime point d’exemple pour cette forme" in plain and "aucune ligne manquée" in plain)

# 9. idrāǧ matn — 3 formes
chk("matn nombreux et célèbre ×3 formes", "nombreux et célèbre" in plain and "trois formes" in plain)
chk("M1 début rare", "l’idrāǧ au début du ḥadīṯ" in plain and "est rare" in plain)
chk("M1 asbiġū l-wuḍūʾa", "asbiġū l-wuḍūʾa, waylun li-l-aʿqābi mina n-nār" in plain)
chk("M1 Šabbāba ibn Sawwār + Šuʿba + Muḥammad ibn Ziyād", "Šabbāba ibn Sawwār" in plain and "de Šuʿba, de Muḥammad ibn Ziyād, d’Abū Hurayra" in plain)
chk("M1 les deux phrases élevées / première d’Abū Hurayra", "en élevant les deux phrases, alors que la première est du propos d’Abū Hurayra" in plain)
chk("M1 transmission al-Buḫārī + ṭaḥūra", "j’ai entendu Abū Hurayra — et il passait près de nous" in plain and "ṭaḥūra" in plain)
chk("M1 Abū l-Qāsim ﷺ", "car Abū l-Qāsim ﷺ a dit" in plain)
chk("M1 réf ġasl al-aʿqāb", "livre des ablutions, chapitre du lavage des talons" in plain)
chk("M2 milieu peu fréquent", "l’idrāǧ en plein milieu du ḥadīṯ" in plain and "est peu fréquent" in plain)
chk("M2 Hišām ibn ʿUrwa ibn az-Zubayr", "Hišām ibn ʿUrwa ibn az-Zubayr, de son père, de Buṣra bint Ṣafwān" in plain)
chk("M2 man masssa ḏakarahu aw anṯaytih aw rifġahu", "man masssa ḏakarahu aw anṯaytih aw rifġahu fal-yatawaḍḍaʾ" in plain)
chk("M2 réf Sunan al-Bayhaqī telle qu’imprimée", "Sunan al-Bayhaqī, livre de la pureté, chapitre du toucher des deux parties féminines" in plain)
chk("M2 additions du propos de ʿUrwa", "ne proviennent que du propos de ʿUrwa" in plain)
chk("M2 Ayyūb + Ḥammād ibn Zayd", "parmi lesquels Ayyūb et Ḥammād ibn Zayd" in plain)
chk("M2 restreint tenu", "se sont tenus à l’élevé seul, à savoir « man masssa ḏakarahu fal-yatawaḍḍaʾ »" in plain)
chk("M3 fin le plus fréquent", "l’idrāǧ à la fin du ḥadīṯ" in plain and "survient le plus" in plain)
chk("M3 chaîne al-Ḥasan ibn al-Ḥurr / al-Qāsim ibn Muḫāmira / ʿAlqama", "al-Ḥasan ibn al-Ḥurr" in plain and "al-Qāsim ibn Muḫāmira" in plain and "de ʿAlqama" in plain)
chk("M3 iḏan qulta (OCR kulta récusé)", "iḏan qulta hāḏā aw qaḍayta hāḏā faqad qaḍayta ṣalātak" in plain)
chk("M3 faqum / faqʿud (OCR faq/tafʿud récusés)", "in šiʾta an taqūma faqum, wa-in šiʾta an taqʿuda faqʿud" in plain)
chk("M3 réf at-tašahhud", "livre de la prière, chapitre du tashahhud" in plain)
chk("M3 Zuhayr interpolé sans séparation", "que Zuhayr ibn Muʿāwiya transmit interpolé" in plain and "sans séparation" in plain)
chk("M3 ʿAbd ar-Raḥmān ibn Ṯābit de Ṯawbān", "ʿAbd ar-Raḥmān ibn Ṯābit le sépara, de Ṯawbān" in plain)
chk("M3 an-Nawawī accord des ḥuffāẓ", "an-Nawawī a rapporté l’accord des ḥuffāẓ sur le fait qu’il est mudraǧ" in plain)

# 10. clôture — taʿammud + exception
chk("interdiction taʿammud", "d’interpoler délibérément (taʿammud al-idrāǧ)" in plain)
chk("qāḍī Zakariyyā al-Anṣārī", "Zakariyyā al-Anṣārī excepta de cela l’explication du mot rare" in plain)
chk("az-Zuhrī + imâms", "az-Zuhrī et d’autres des imâms l’ont fait" in plain)

# 11. taqwīm — 3 questions
chk("taqwīm 3 questions", "sous la forme de trois questions" in plain)
chk("TQ1 définition", "Qu’est-ce que le ḥadīṯ mudraǧ" in plain)
chk("TQ2 formes sanad+matn", "les formes de l’idrāǧ dans l’isnād et dans le matn" in plain)
chk("TQ3 ḥukm taʿammud", "le jugement de l’idrāǧ délibéré dans le ḥadīṯ" in plain)
chk("TQ1 tranchée 4800 dpi", "4800 dpi" in plain and "nettement distinct du bāʾ" in plain)

# 12. istiṯmār — Ibn Ḥaǧar
chk("Ibn Ḥaǧar cité", "Ibn Ḥaǧar dit" in plain)
chk("riwāya mufaṣṣala", "d’une transmission qui précise le locuteur" in plain)
chk("taṣrīḥ ar-rāwī / al-aʾimma", "du transmetteur, ou de quelques-uns des imâms avertis" in plain)
chk("istiḥālatun yaqūla", "l’impossibilité que le Prophète ﷺ dise cela" in plain)
chk("réf. Nuzhat an-naẓar p. 116", "Nuzhat an-naẓar d’Ibn Ḥaǧar, p. 116" in plain)
chk("vocalisation tenue", "yuʿrafu l-idrāǧu bi-wurūdi riwāyatin mufaṣṣalatin" in plain)
chk("consigne unique", "j’en extrais les voies par lesquelles l’idrāǧ" in plain)

# 13. iʿdād qablī — leçon suivante mudbaǧ
chk("préparation mudabbaǧ ×2", "je connais le ḥadīṯ mudabbaǧ" in plain and "connaissance du ḥadīṯ mudabbaǧ" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 14. ﷺ tenu, zéro āya rendue, zéro résidu
chk("ﷺ tenu (U+FDFA ×13)", h.count("\ufdfa") == 13)
chk("doc mentionne aucune āya rendue", "aucune āya rendue" in plain)
residus = ["TODO", "XXX", "undefined", "NaN", "【", "____", "recycle", "takeover", "mtime", "⟨AR⟩"]
chk("zéro résidu technique", not any(r in plain for r in residus))

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)
