#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-267
(الدرس 13 — anšaṭa taṭbīqiyya « activités pratiques », p.72-73 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.72-73 par DOUBLE sondage (p.71 =
clôture de la leçon 12 livrée en R632 ; p.72 = bannière ad-dars 13 : anšaṭa
taṭbīqiyya + 3 objectifs + champ des activités + activités de préparation
(4 items) + activités de réalisation (3 items) ; p.73 = activités de
présentation (2 items) + al-iʿdād al-qiblī ; p.74 = bannière ad-dars 14
(mardūd) NON TOUCHÉE, docId pdf-mut23h2u-268 registre vide) ; claim repris
(takeover du claim subagent-r635 périmé — même ouvrier, slot demeuré libre) ;
extraction multicouche tr-tmp/r635/ (pdftotext + PyMuPDF + tesseract 300 dpi,
pages 72-74) réutilisant le sondage R632 (tr-tmp/r632/, p.66-75) ; recadrages
864-1500 dpi + lectures VLM bornées read-*.txt (dossier R635 antérieur
repris et vérifié lecture par lecture) ; titleAr du registre
« الدرس 13 : أنشطة تطبيقية » confirme la bannière lue en image (correction
documentée de la consigne R632 qui portait « أهداف الأنشطة » = première
rubrique intérieure) ; zéro renvoi chiffré (loi d'inversion non sollicitée),
zéro āya (cache non sollicité), zéro arabe, zéro apostrophe droite.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf267.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-267-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"
REG1 = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"
SREG = "/home/z/my-project/scripts-translate/savant-registry.json"

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
chk("h1 = titleFr pré-mappé « Leçon 13 : Activités pratiques »",
    hn.startswith("<h1>Leçon 13 : Activités pratiques"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le chapitre-atelier", "chapitre-atelier" in h[:2200])
chk("h1 mentionne la Bayqūniyya et la Nuḫbat al-fikr",
    "Bayqūniyya" in h[:2200] and "Nuḫbat al-fikr" in h[:2200])
chk("h1 liste les neuf termes (mutawātir…muḫtalaf)",
    "mutawātir" in h[:2200] and "šāḏḏ" in h[:2200] and "munkar" in h[:2200]
    and "muḫtalaf al-ḥadīṯ" in h[:2200])
chk("h1 mentionne la leçon suivante mardūd", "mardūd" in h[:2400])

# ---- méta : bornes et méthode
chk("méta : treizième leçon", "Treizième leçon" in hn)
chk("méta : pages 72 à 73", "pages 72 à 73" in hn)
chk("méta : item archive.org", "1_20220304_20220304_2251" in hn)
chk("méta : source locale ulum-hadith-2-thanawi_text.pdf",
    "ulum-hadith-2-thanawi_text.pdf" in hn)
chk("méta : bannière ad-dars 13 : anšaṭa taṭbīqiyya",
    "ad-dars 13" in hn and "anšaṭa taṭbīqiyya" in hn)
chk("méta : correction documentée de la lecture R632 (ahdāf al-anšaṭa)",
    "ahdāf al-anšaṭa" in hn and "correction documentée" in hn)
chk("méta : p.71 clôt la leçon 12", "la page 71 clôt la leçon 12" in hn)
chk("méta : p.72 ouvre la leçon 13", "la page 72 ouvre la leçon 13" in hn)
chk("méta : p.73 clôt la leçon 13", "la page 73 clôt la leçon 13" in hn)
chk("méta : p.74 ouvre la leçon 14 (mardūd, non touchée)",
    "la page 74 ouvre la leçon 14" in hn and "non touchée" in hn)
chk("méta : docId voisin 268 registre vide",
    "pdf-mut23h2u-268" in hn and "registre vide" in hn)
chk("méta : chapitre sans matn ni glose",
    "ni matn de ḥadīṯ ni glose" in hn)
chk("méta : loi d’inversion non sollicitée",
    "loi d’inversion des chiffres" in hn and "n’est pas sollicitée" in hn)
chk("méta : zéro āya, cache non sollicité",
    "zéro āya imprimée" in hn and "cache coranique non sollicité" in hn)
chk("méta : trois couches + dossiers r632/r635",
    "trois couches de lecture" in hn and "tr-tmp/r632/" in hn and "tr-tmp/r635/" in hn)
chk("méta : dossier R635 antérieur repris et vérifié",
    "repris et vérifié lecture par lecture" in hn)

# ---- méta : apparat des divergences
chk("apparat : bande verte, lecture isolée maǧālāt consignée",
    "maǧālāt" in hn and "consignée, non retenue" in hn)
chk("apparat : couche incorporée brouillée (al-asālbiqbiyamaqnūniyya)",
    "al-asālbiqbiyamaqnūniyya" in hn)
chk("apparat : préposition min retenue, variante fī consignée",
    "quatre lectures d’image concordantes avec la préposition" in hn
    and "« fī » isolée consignée" in hn)
chk("apparat : iḥḍār contre iḥṣār/iḥyāz",
    "iḥḍār" in hn and "iḥṣār" in hn and "iḥyāz" in hn)
chk("apparat : al-maktaba al-madrasiyya contre al-kutub ad-dirāsiyya",
    "al-maktaba al-madrasiyya" in hn and "al-kutub ad-dirāsiyya" in hn)
chk("apparat : anšaṭat al-inǧāz contre lectures isolées",
    "anšaṭat aṯ-ṯanāʾ" in hn and "an-našāṭ al-inǧāz" in hn)
chk("apparat : 3e item des réalisation absent des couches, établi par 4 lectures",
    "absent des deux couches texte" in hn
    and "quatre lectures d’image concordantes de recadrages 900 à 1500" in hn)
chk("apparat : wa-l-ḥukm ʿalayh (wāw porté par la couche logique)",
    "wāw porté par la couche logique" in hn)
chk("apparat : al-iʿdād al-qiblī contre lectures dégradées",
    "al-iʿdād at-tālī" in hn and "aṣ-ṣiḥḥī" in hn)
chk("apparat : citation tranchee à 864 dpi + épellation ḍād-alif-mīm-yāʾ-nūn",
    "864 points au pouce" in hn and "ḍād — alif — mīm — yāʾ — nūn" in hn)
chk("apparat : al-maḍāmīn retenu (cohérence leçon 14), variantes consignées",
    "al-maḍāmīn" in hn and "al-maʿānī" in hn and "aṣ-ṣifāt" in hn
    and "al-faṣārīm" in hn)

# ---- sections
for sec in ("Les objectifs des activités", "Le champ des activités",
            "Les activités de préparation", "Les activités de réalisation",
            "Les activités de présentation", "La préparation de la leçon suivante"):
    chk(f"section h2 : {sec}", f"<h2>{sec}" in h)
chk("rubriques translittérées (ahdāf/maǧāl/iʿdād/iʿdād al-qiblī)",
    "(ahdāf al-anšaṭa)" in h and "(maǧāl al-anšaṭa)" in h
    and "(anšaṭat al-iʿdād)" in h and "(anšaṭat al-inǧāz)" in h
    and "(anšaṭat al-ʿarḍ)" in h and "(al-iʿdād al-qiblī)" in h)

# ---- contenus clés traduits
chk("objectif 1 : fixe mes connaissances / investisse mes acquis",
    "que je fixe mes connaissances et que j’investisse mes acquis dans la terminologie du ḥadīṯ" in hn)
chk("objectif 2 : développe par les applications pratiques",
    "que je développe mes acquis à travers les applications pratiques" in hn)
chk("objectif 3 : coopère avec mes amis (sciences du ḥadīṯ)",
    "que je coopère avec mes amis pour développer mes habiletés et mes capacités dans les sciences du ḥadīṯ" in hn)
chk("champ : applications dans les sources du ḥadīṯ et ses sciences",
    "applications dans les sources du ḥadīṯ et ses sciences" in hn
    and "taṭbīqāt fī maṣādir al-ḥadīṯ wa-ʿulūmih" in hn)
chk("préparation : groupes sous la direction du maître",
    "constituer des groupes de travail sous la direction du maître (de la maîtresse)" in hn)
chk("préparation : déterminer une source parmi les sources",
    "déterminer une source parmi les sources pour y mener la recherche" in hn)
chk("préparation : déterminer les termes (ṣaḥīḥ/ḥasan/muḫtalaf)",
    "déterminer les termes objet de la recherche et de l’étude" in hn)
chk("préparation : investir les acquis de la Bayqūniyya et de la Nuḫbat al-fikr",
    "investir les acquis antérieurs de la Bayqūniyya et de la Nuḫbat al-fikr" in hn)
chk("préparation : copie pour y travailler (bibliothèque de l’école)",
    "se procurer une copie pour y travailler (la bibliothèque de l’école)" in hn
    and "bibliothèque scolaire" in hn)
chk("réalisation : fiche (nom, titre, auteur, méthodologie)",
    "préparer une fiche portant sur le nom de la source, son titre, son auteur et la méthodologie de la recherche en son sein" in hn)
chk("réalisation : choisir un modèle parmi les hadiths jugés",
    "choisir un modèle parmi les hadiths que les savants ont jugés selon l’un des termes établis" in hn)
chk("réalisation : liste des neuf termes intégrale",
    "le mutawātir, le ṣaḥīḥ, le ḥasan, le ʿazīz, le ġarīb, le šāḏḏ, la ġarāba, le munkar, le muḫtalaf al-ḥadīṯ" in hn)
chk("réalisation : recherche pratique (méthode du jugement)",
    "mener une recherche pratique dans la source pour connaître la méthode du jugement sur le ḥadīṯ" in hn)
chk("présentation : résultats dans la salle + source et son auteur",
    "présenter les résultats de la recherche et de l’étude dans la salle" in hn
    and "faire connaître la source et son auteur" in hn)
chk("présentation : modèle appliqué de la méthode des savants (sanad)",
    "présenter un modèle appliqué de la méthode des savants dans l’étude du sanad du ḥadīṯ" in hn)
chk("iʿdād : citation (lire le texte de la leçon suivante)",
    "je lis le texte de la leçon suivante, et j’accomplis les questions de la rubrique" in hn)
chk("iʿdād : istiḫlāṣ al-maḍāmīn",
    "istiḫlāṣ al-maḍāmīn" in hn)
chk("iʿdād : double question de la leçon 14 (omission/atteinte)",
    "espèces de l’omission dans l’isnād" in hn
    and "espèces de l’atteinte au rapporteur" in hn)
chk("rappel de la consigne de la leçon 12 (coopération)",
    "prépare, en coopération avec tes amis, la leçon des activités" in hn)

# ---- hygiène FR
chk("zéro caractère arabe",
    not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<p>") == h.count("</p>") and h.count("<dl") == h.count("</dl>")
    and h.count("<dt>") == h.count("</dt>") and h.count("<dd>") == h.count("</dd>"))
chk("volume dans la fourchette du livre (25 000-35 000 car)",
    25_000 <= len(h) <= 35_000)

# ---- registre : htmlFr posé, voisins intacts, savants
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 263 intact (33 055 car)", len(les["pdf-mut23h2u-263"].get("htmlFr") or "") == 33055)
chk("registre 264 intact (25 976 car)", len(les["pdf-mut23h2u-264"].get("htmlFr") or "") == 25976)
chk("registre 265 intact (31 943 car)", len(les["pdf-mut23h2u-265"].get("htmlFr") or "") == 31943)
chk("registre 266 intact (30 346 car)", len(les["pdf-mut23h2u-266"].get("htmlFr") or "") == 30346)
chk("registre 268 non touché (htmlFr vide)", (les["pdf-mut23h2u-268"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-267"].get("htmlFr") or ""
if fr:
    chk("registre 267 = htmlFr posé (~25 000 car)", 24_000 <= len(fr) <= 30_000)
    chk("registre 267 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 267 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 267 (الدرس 13 : أنشطة تطبيقية)",
    les["pdf-mut23h2u-267"].get("titleAr") == "الدرس 13 : أنشطة تطبيقية")
chk("titleFr pré-mappé 267 aligné au h1",
    (les["pdf-mut23h2u-267"].get("titleFr") or "") == "Leçon 13 : Activités pratiques")
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)

sreg = json.load(open(SREG, encoding="utf-8"))
hand, llm = sreg.get("hand", []), sreg.get("llm", [])
n_sav = len(hand) + len(llm)
already = "pdf-mut23h2u-267" in json.dumps(hand)
chk(f"registre savants = len(hand)+len(llm) == {1179 + (1 if already else 0)}",
    n_sav == 1179 + (1 if already else 0))

print(f"verify-ulumhadith2-pdf267 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
