#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-269
(الدرس 15 : الحديث المرسل — al-ḥadīṯ al-mursal, p.78-82 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.78-82 par DOUBLE sondage (p.77 =
clôture de la leçon 14, livrée R642, docId pdf-mut23h2u-268 ; p.78 = bannière
ad-dars 15 « الحديث المرسل » + 3 objectifs + tamhīd + matn « والثاني: المُرْسَلُ »
+ الشرح + استخلاص ; p.79 = التحليل : أولا تعريف المرسل (لغة [مقاييس اللغة 2/392] /
اصطلاحا) + تعريف الفقهاء والأصوليين [فتح المغيث 1/172] + أقوال ابن عبد البر
[التمهيد 1/17] + ثانيا صور المرسل (Ibn aṣ-Ṣalāḥ [ص 51]) ; p.80 = 4 cas des
صور + ثالثا حكم المرسل [التمهيد 1/2 و 1/71] + أقوال العلماء (التوقف / قبول
مطلق / قبول مع الاعتضاد) ; p.81 = الباجي + توجيه الأقوال [فتح المغيث 1/176] +
من قال لا يجوز + ahtadī wa-aqtadī (أبي العالية، سنن الدارمي) + التقييم (2) +
الاستئناس [التمهيد 1/2] + ناقش ; p.82 = الإعداد القبلي (2 items) ; p.83 =
ouverture leçon 16 « المعضل والمنقطع » (sondage, non touchée, docId
pdf-mut23h2u-270, registre vide)) ; reprise R645c après deux passes
interrompues (claim périmé, takeover autorisé, refresh ×2) ; extraction
MULTICOUCHE : couches brute + fix p.78-79 (tr-tmp/uh2-l268-raw.txt),
couches incorporées p.80-83 (p80/p81/p82/p83-embed.txt), 5 lectures VLM
consignées R645b (vlm-p078-survey, vlm-r78-top, vlm-r79-top/mid/bot) + 5
lectures d'adjudication R645c (read-r80-top/bot, read-r81-top/bot, read-r82-full) ;
CORRIGÉ D'OCR documenté : inversions « طقسلا »=السقط et « عطقنملا »=المنقطع
(échange ط/ق) ; NOMBRES tranchés sur les couches et l'image, jamais devinés :
Maqāyīs 2/392 (suite visuelle « 392/2 »), Fatḥ al-Maġīṯ 1/172 et 1/176 (176
tranché par l'image contre fragment « 1/ »), Tamhīd 1/17, 1/2, 1/71,
Muqaddimat Ibn aṣ-Ṣalāḥ p.51 et p.53 (53 porté par l'image contre « صص 3 »
dégradé) ; zones dégradées consignées : jeton « TST » tranché par l'image
(« سألت من شئت منهم عن مراسيل الموطأ »), fin de condition d'Ibn ʿAbd al-Barr
(p.79) brouillée dans les deux couches, fragment final de la citation du
ḥukm (p.80) divergent entre couches (rendu par le sens convergent),
al-imtidād (image) contre al-mutamād (couche fixe), phrase al-Ḥākim d'après
Mālik portée par l'image seule ; zéro āya, zéro arabe, zéro apostrophe droite.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf269.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-269-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"

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

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 15 : Le hadith à transmetteur omis (mursal) »",
    hn.startswith("<h1>Leçon 15 : Le hadith à transmetteur omis (mursal)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne la chute dans la chaîne (as-saqaṭ / al-isnād)",
    "la chute (as-saqaṭ) dans la chaîne (al-isnād)" in h[:1200])
chk("h1 mentionne la fin de la chaîne après le Successeur",
    "après le Successeur (tābiʿī)" in h[:1500])
chk("h1 mentionne Maqāyīs al-luġa et Ibn Fāris", "Maqāyīs al-luġa d’Ibn Fāris" in h[:2400])
chk("h1 mentionne Fatḥ al-Maġīṯ d’aṯ-Ṣaḫāwī", "Fatḥ al-Maġīṯ d’aṯ-Ṣaḫāwī" in h[:1800])
chk("h1 mentionne le Tamhīd d’Ibn ʿAbd al-Barr", "Tamhīd d’Ibn ʿAbd al-Barr" in h[:1800])
chk("h1 mentionne Ibn aṣ-Ṣalāḥ et les quatre cas en divergence",
    "Ibn aṣ-Ṣalāḥ" in h[:3000] and "les quatre cas en divergence" in h[:3000])
chk("h1 mentionne al-Bāǧī et Abū Bakr ar-Rāzī",
    "al-Bāǧī" in h[:3000] and "Abū Bakr ar-Rāzī" in h[:3000])
chk("h1 mentionne Abū al-ʿĀliya et Sunan ad-Dārimī",
    "Abū al-ʿĀliya" in h[:3200] and "Sunan ad-Dārimī" in h[:3200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.78-82 documentées", "pages 78 à 82" in h)
chk("p.77 clôture leçon 14 (R642, 268)", "R642" in h and "pdf-mut23h2u-268" in h)
chk("p.83 leçon 16 sondée, non touchée, registre vide",
    "pdf-mut23h2u-270" in h and "registre vide" in h and "non touchée" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière : registre autorité + lecture dégradée consignée non retenue",
    "ad-dars 15" in h and "zéro devinette" in h and "consignée et non retenue" in h)
chk("reprise R645c + lectures consignées R645b citées",
    "R645c" in h and "R645b" in h and "vlm-p078-survey.json" in h
    and "vlm-r79-mid.json" in h)
chk("couches brute + fix p.78-79 citées (uh2-l268-raw.txt)",
    "uh2-l268-raw.txt" in h and "mots réinversés" in h)
chk("couches incorporées p.80-83 citées", "p80-embed.txt" in h and "p83-embed.txt" in h)
chk("5 lectures d’adjudication R645c citées", "read-r80-top.txt" in h
    and "read-r81-bot.txt" in h and "read-r82-full.txt" in h)
chk("corrigé d’OCR السقط/المنقطع (échange ط/ق) documenté",
    "échange des deux lettres" in h and "as-saqaṭ" in h and "al-munqaṭiʿ" in h)

# ---- nombres miroir tranchés
chk("Maqāyīs 2/392 tranché (suite visuelle « 392/2 »)",
    "tome 2, page 392" in hn and "392/2" in h)
chk("Fatḥ al-Maġīṯ 1/172 (définition des juristes)", "tome 1, page 172" in hn)
chk("Tamhīd 1/17 (circonstances de l’émission)", "tome 1, page 17" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.51 (figures)", "page 51" in hn)
chk("Tamhīd 1/2 + 1/71 (statut)", "tome 1, page 2" in hn and "tome 1, page 71" in hn)
chk("Fatḥ al-Maġīṯ 1/176 tranché par l’image (fragment « 1/ » dégradé consigné)",
    "tome 1, page 176" in hn and "tranché par la lecture d’image" in hn)
chk("Muqaddima p.53 portée par l’image contre « pages 3 » dégradé",
    "pages 53" in hn and "pages 3" in h)
chk("jeton fantôme « TST » tranché par l’image (marāsīl du Muwaṭṭaʾ)",
    "TST" in h and "marāsīl du Muwaṭṭaʾ" in hn)
chk("divergence al-imtidād / al-mutamād consignée",
    "al-imtidād" in h and "al-mutamād" in h)
chk("fragment final de la condition d’Ibn ʿAbd al-Barr (p.79) dégradé consigné",
    "fragment final de la condition dégradé dans les deux couches" in h)
chk("fragment final du ḥukm (p.80) divergent, rendu par le sens convergent",
    "la preuve s’impose et la pratique en est obligatoire" in h
    and "rendu par le sens convergent" in h)
chk("item « Mālikites et Kūfīyūn » en fragments colonnés + image",
    "Kūfīyūn" in hn and "fragments colonnés" in h)
chk("phrase al-Ḥākim d’après Mālik portée par l’image seule",
    "passage rapporté étrange (mustaġrab)" in hn and "lecture d’image seule" in h)

# ---- objectifs (3)
chk("trois objectifs annoncés", "trois objectifs" in hn)
chk("objectif 1 : réalité du mursal et statut", "la réalité du ḥadīṯ mursal et son statut" in hn)
chk("objectif 2 : mursal du Compagnon vs autres",
    "distingue le mursal du Compagnon de celui des autres rapporteurs" in hn)
chk("objectif 3 : assemblées des savants et audition",
    "assister aux assemblées des savants et à entendre la science d’eux-mêmes" in hn)

# ---- tamhīd
chk("tamhīd : espèces de la chute nommées selon la place",
    "un nom propre selon la place où la chute a eu lieu" in hn)
chk("tamhīd : commencement / milieu / fin après le Successeur",
    "au commencement de la chaîne, au milieu de celle-ci, ou bien à sa fin après le Successeur" in hn)
chk("tamhīd : double question (nom de la dernière espèce / ce qui la distingue)",
    "comment se nomme la dernière espèce de la chute" in hn
    and "qu’est-ce qui la distingue des autres espèces de la chute" in hn)

# ---- matn Ibn Ḥaǧar + glose + istiḫlāṣ
chk("matn : « et le deuxième : le mursal »",
    "et le deuxième&nbsp;: le mursal (al-mursal)" in h or "et le deuxième : le mursal (al-mursal)" in hn)
chk("matn : continuité mot pour mot avec la leçon 14 (muʿallaq au 1er rang)",
    "le premier rang de la chute était le suspendu (al-muʿallaq)" in hn)
chk("glose : deuxième espèce des catégories de la chute",
    "la deuxième espèce des catégories de la chute (aqsām as-saqaṭ)" in hn)
chk("glose : omis de sa fin, celui qui vient après le Successeur",
    "ce dont on a omis, de sa fin, celui qui vient après le Successeur (man baʿd at-tābiʿī)" in hn)
chk("istiḫlāṣ : nom d’une catégorie des catégories de la chute",
    "le nom d’une catégorie des catégories de la chute" in hn)

# ---- taḥlīl 1 : définition
chk("luġa : extension, élan, émancipation, non-empêchement",
    "l’extension (al-imtidād" in hn and "l’élan (al-inbiʿāṯ)" in hn
    and "l’émancipation (al-iṭlāq) et le non-empêchement (ʿadam al-manʿ)" in hn)
chk("luġa : « émission dispersée » + partie de la chaîne tronquée de son reste",
    "en émission dispersée (arsālan)" in hn and "tronquée de son reste" in hn)
chk("luġa : renvoi Maqāyīs 2/392 en modifiant",
    "d’Ibn Fāris, tome 2, page 392" in hn and "en modifiant" in hn)
chk("istiṣilāḥ : figure du Successeur grand ou petit + variantes « a dit / a fait »",
    "qu’il soit grand ou petit" in hn and "a dit ceci" in hn
    and "il a fait ceci de sa présence" in hn)
chk("juristes/uṣūlīyūn : rupture de quelque façon, commencement ou fin = munqaṭiʿ",
    "au sens du tronqué (al-munqaṭiʿ)" in hn
    and "au commencement ou à la fin" in hn)
chk("juristes : « elle qui importe » (terminologie des muḥaddithīn)",
    "c’est elle qui importe" in hn)
chk("Ibn ʿAbd al-Barr : circonstances de l’émission qui ne nuisent pas",
    "des circonstances qui ne lui nuisent pas" in hn)
chk("Ibn ʿAbd al-Barr : émission en connaissance de l’authenticité",
    "en connaissance de l’authenticité de ce qu’il émet" in hn)
chk("Ibn ʿAbd al-Barr : oubli + séance de révision (mudākara)",
    "se séance de révision (mudākara)" in hn or "séance de révision (mudākara)" in hn)
chk("Ibn ʿAbd al-Barr : renvoi Tamhīd 1/17",
    "d’Ibn ʿAbd al-Barr, tome 1, page 17" in hn)

# ---- taḥlīl 2 : figures
chk("Ibn aṣ-Ṣalāḥ : figure sans divergence = ḥadīṯ du grand Successeur",
    "sa figure qui ne comporte aucune divergence est le ḥadīṯ du grand Successeur" in hn)
chk("Ibn aṣ-Ṣalāḥ : ʿUbayd Allāh b. ʿUbayd b. al-Ḫayyār + Saʿīd b. al-Musayyib",
    "ʿUbayd Allāh b.&nbsp;ʿUbayd b.&nbsp;al-Ḫayyār" in h
    and "Saʿīd b.&nbsp;al-Musayyib" in h)
chk("Ibn aṣ-Ṣalāḥ : renvoi p.51", "Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 51" in hn)
chk("mašhūr : égalité des Successeurs dans le nom d’émission",
    "mettre les Successeurs en égalité (at-taswiya) dans le nom d’émission" in hn)
chk("figures : rupture avant le Successeur = munqaṭiʿ / muʿḍal (jamais mursal)",
    "il se nomme seulement tronqué (munqaṭiʿ)" in hn
    and "il se nomme à double rupture (muʿḍal), et il se nomme aussi tronqué" in hn)
chk("figures : émission propre au seul rang des Successeurs (al-Ḥākim)",
    "l’émission (al-irrāsal) est propre au seul rang des Successeurs (at-tābiʿīn)" in hn)
chk("figures : jeunes Successeurs az-Zuhrī + Yaḥyā b. Saʿīd al-Anṣārī",
    "comme az-Zuhrī et Yaḥyā b.&nbsp;Saʿīd al-Anṣārī" in h)
chk("figures : Ibn ʿAbd al-Barr, des gens le disent tronqué (rencontre du seul et du deux)",
    "ne le nomment pas mursal mais tronqué" in hn and "le seul et le deux" in hn)
chk("figures : « untel d’après un homme » = munqaṭiʿ d’après al-Ḥākim (Maʿrifat)",
    "d’après un homme (fulān ʿan raǧul)" in hn
    and "Maʿrifat ʿulūm al-ḥadīṯ" in hn)
chk("figures : dénombré parmi les espèces du mursal dans uṣūl al-fiqh",
    "dénombré parmi les espèces du mursal" in hn)
chk("figures : récits des jeunes Compagnons (Ibn ʿAbbās) = mawṣūl musnad, ʿudūl",
    "des jeunes Compagnons (aḥdāth aṣ-ṣaḥāba)" in hn
    and "au rang du continu lié (al-mawṣūl al-musnad)" in hn
    and "tous les Compagnons sont justes (ʿudūl)" in hn)

# ---- taḥlīl 3 : statut (aḥkām)
chk("ḥukm : ouverture « le mursal est une preuve à laquelle on se conforme »",
    "le mursal est une preuve (ḥuǧǧa) à laquelle on se conforme" in hn)
chk("ḥukm : iḫtalat + yutaʿabbad bihi + yūʾaḫuḍ bihi",
    "se sont entendus (iḫtalat)" in hn and "on se conforme religieusement (yutaʿabbad bihi)" in hn
    and "que l’on prend (yūʾaḫuḍ bihi)" in hn)
chk("ḥukm : renvoi Tamhīd 1/2", "d’Ibn ʿAbd al-Barr, tome 1, page 2" in hn)
chk("ḥukm : principe de Mālik = fiabilité, renvoi Tamhīd 1/71",
    "est de ne prendre que d’après des fiables" in hn and "tome 1, page 71" in hn)
chk("aḥkām 1 : tawaqquf, ǧumhūr des muḥaddithīn, un des deux dits d’Aḥmad",
    "la suspension (at-tawaqquf)" in hn
    and "la doctrine de la plupart des ḥadīṯistes" in hn
    and "un des deux dits de l’imām Aḥmad" in hn)
chk("aḥkām 2 : qubūl muṭlaq, Mālikites et Kūfīyūn",
    "l’acceptation sans restriction (qubūl muṭlaq)" in hn
    and "le dire des Mālikites et des Kūfīyūn" in hn)
chk("aḥkām 3 : iʿtaḍḍada par une voie distincte, dire de aš-Šāfiʿī",
    "l’acceptation quand il est renforcé (iʿtaḍḍada)" in hn
    and "distincte des premières voies" in hn
    and "c’est le dire de l’imām aš-Šāfiʿī" in hn)
chk("al-Bāǧī : fiables et autres → mursal non accepté, iṭlāq du 2e dit comporte examen",
    "n’est pas accepté du tout (ittifāqan)" in hn
    and "comporte examen (nazar)" in hn)
chk("tawǧīh : condition de fiabilité du rapporteur du mursal (ḍuʿafāʾ)",
    "n’émette pas d’après des faibles (aḍ-ḍuʿafāʾ)" in hn
    and "exigence de la fiabilité du rapporteur du mursal" in hn)
chk("tawǧīh : Ibn ʿAbd al-Barr + al-Bāǧī + Abū Bakr ar-Rāzī (Ḥanafites)",
    "l’a dit Ibn ʿAbd al-Barr" in hn and "Abū al-Walīd al-Bāǧī des Mālikites" in hn
    and "Abū Bakr ar-Rāzī des Ḥanafites" in hn)
chk("tawǧīh : renvoi Fatḥ al-Maġīṯ 1/176",
    "aṯ-Ṣaḫāwī, tome 1, page 176" in hn)
chk("ceux qui interdisent : rapporteur non précautionneux (mutaḥarriǧ)",
    "n’était pas précautionneux (mutaḥarriǧ)" in hn)
chk("al-Ḥākim d’après Mālik : mustaġrab, le célèbre est le contraire",
    "le mursal n’est pas une preuve" in hn and "le célèbre est le contraire" in hn
    and "sauf si c’est le mursal d’un non-fiable" in hn)

# ---- ahtadī wa-aqtadī (Abū al-ʿĀliya)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Abū al-ʿĀliya : narration à Baṣra un à un, non satisfaits, embarquement vers Médine",
    "la narration à Baṣra d’après les Compagnons du Messager de Dieu" in hn
    and "un à un" in hn and "embarquions vers Médine" in hn
    and "l’entendions de leurs bouches" in hn)
chk("renvoi Sunan ad-Dārimī (voyage en quête de la science)",
    "Sunan ad-Dārimī, chapitre du voyage en quête de la science et de la charge supportée dans celui-ci" in hn)

# ---- évaluation (2 items)
chk("évaluation : deux items", "convoque deux items" in hn)
chk("évaluation : définir + statut / différence entre rapporteurs",
    "je définis le ḥadīṯ mursal et j’expose son statut" in hn
    and "celui qui n’émet que d’après des fiables et celui qui émet d’après des fiables et d’autres" in hn)

# ---- exploitation (al-istiʾnās)
chk("istiʾnās : Ibn ʿAbd al-Barr, dépositaire de l’école de Mālik",
    "dépositaire de l’école de Mālik (li-Mālik wa-ntaḥalahu)" in hn)
chk("istiʾnās : ṣaḥāḥ, attaque illicite, fiabilité et amāna des émetteurs",
    "des recueils authentiques (ṣaḥāḥ)" in hn
    and "la fiabilité de leurs rapporteurs et de la sincérité (amāna) de ceux qui les ont émis" in hn)
chk("istiʾnās : renvoi Tamhīd 1/2", "[at-Tamhīd, d’Ibn ʿAbd al-Barr, tome 1, page 2" in hn)
chk("istiʾnās : consigne de discussion (iʿdād qiblī de la leçon précédente)",
    "je discute le dire du ḥāfiẓ Ibn ʿAbd al-Barr" in hn
    and "préparation préalable de la leçon précédente" in hn)

# ---- préparation leçon suivante (p.82)
chk("iʿdād : leçon 16 muʿḍal / munqaṭiʿ",
    "Le hadith à double rupture (muʿḍal) et à rupture tronquée (munqaṭiʿ)" in hn)
chk("iʿdād : muʿḍal plus faible que munqaṭiʿ et mursal",
    "plus faible que le tronqué et le mursal" in hn)
chk("iʿdād : deux figures (petit tābiʿī / tābiʿ at-tābiʿī)",
    "le petit Successeur (aṭ-ṭābiʿī aṣ-ṣaġīr)" in hn
    and "le successeur de Successeur (tābiʿ at-tābiʿī)" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd/strong/ul/li)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>") and h.count("<strong>") == h.count("</strong>")
    and h.count("<ul>") == h.count("</ul>") and h.count("<li>") == h.count("</li>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 268 intact (20 715 car)", len(les["pdf-mut23h2u-268"].get("htmlFr") or "") == 20715)
chk("registre 267 intact (25 238 car)", len(les["pdf-mut23h2u-267"].get("htmlFr") or "") == 25238)
chk("registre 270 non touché (htmlFr vide)", (les["pdf-mut23h2u-270"].get("htmlFr") or "") == "")
chk("registre 271 non touché (htmlFr vide)", (les["pdf-mut23h2u-271"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-269"].get("htmlFr") or ""
if fr:
    chk("registre 269 = htmlFr posé (~25 000 car)", 23_000 <= len(fr) <= 28_000)
    chk("registre 269 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 269 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 269", les["pdf-mut23h2u-269"].get("titleAr") == "الدرس 15 : الحديث المرسل")
chk("titleFr pré-mappé 269 aligné au h1",
    (les["pdf-mut23h2u-269"].get("titleFr") or "") == "Leçon 15 : Le hadith à transmetteur omis (mursal)")
chk("titleAr pré-mappé 270 intact (leçon 16, non touchée)",
    les["pdf-mut23h2u-270"].get("titleAr") == "الدرس 16 : المعضل والمنقطع")

print(f"verify-ulumhadith2-pdf269 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
