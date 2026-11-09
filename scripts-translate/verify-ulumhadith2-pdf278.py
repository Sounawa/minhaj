#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-278
(الدرس 24 : الاختصار في الحديث وروايته بالمعنى — p.125-128 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.125-128 par sondage image
(p.124 = clôture de la leçon 23, réservée par un autre ouvrier ;
p.125 = bannière médaillon « 24 » + 4 objectifs + tamhīd + matn Ibn Ḥaǧar
« il n'est pas permis de procéder de dessein au changement du texte et du
synonyme... » + gloses الغريب/المشكل + extraction 2 items ; p.126 = التحليل
أولا اختصار الحديث : définition + 3 positions + détail [Muqaddima ص 324] +
exception « ne vendez pas l'or contre l'or » [Ṣaḥīḥ al-Buḫārī, البيوع] +
découpage des recueils (Mālik/Aḥmad/Abū Dāwūd/an-Nasāʾī) ; p.126-127 =
ثانيا رواية الحديث بالمعنى : majorité + refuseurs (Ibn Sīrīn, Ibn as-Sumaynī,
Mālik) [al-Qārī ص 500] + position détaillée 3 clauses + portée + citation
répétée + pratique des savants + ʿIyāḍ « fermer la porte » [al-Ilmāʿ ص 179] ;
p.128 = أهتدي وأقتدي Ibn aṣ-Ṣalāḥ [Muqaddima ص 247 بتصرف] + التقويم 3 items +
الاستثمار ʿIyāḍ [al-Ilmāʿ ص 174] + الاعداد القبلي 3 items imprimés 1-2-4
(coquille d'éditeur documentée) ; p.129 = أهداف الأنشطة leçon 25 (bannière
sondage, non touchée, registre vide). Adjudications documentées (ONZE lectures
d'images, tr-tmp/qa-crops-r658/) : matn rendu tel qu'imprimé (تغيير اللفظ
والمرادف, احتاج, وبيان المشكل) tranché par zoom 900 dpi contre conflit de
couches, forme canonique Muqaddima « تغيير المتن بالنقص والمرادف » corroborée
EN LIGNE (libmim, ketabonline, hwazen) ; source de l'exception = Ṣaḥīḥ
al-Buḫārī (zoom 900 dpi lettre par lettre contre couche « مسلم »), corroborée
EN LIGNE (bukhari.bham/ketabonline) ; réf pages tranchées digit-by-digit :
324, 500 (×2), 179, 247, 174 ; الاعداد القبلي 1-2-4 confirmé image ; ZÉRO ĀYA
(cache coranique non sollicité — l'énoncé de la vente est un ḥadīṯ du Ṣaḥīḥ).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf278.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-278-fr.html"
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
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u2009", " "))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 24 : L’abrègement du hadith et sa transmission selon le sens »",
    hn.startswith("<h1>Leçon 24 : L’abrègement du hadith et sa transmission selon le sens"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le matn d’Ibn Ḥaǧar (changement du texte et du synonyme, significations)",
    "changement du texte et du synonyme" in h[:1600] and "maîtrise les significations" in h[:1700])
chk("h1 mentionne Muqaddimat Ibn aṣ-Ṣalāḥ page 324", "Muqaddimat Ibn aṣ-Ṣalāḥ, page 324" in h[:6000])
chk("h1 mentionne Ṣaḥīḥ al-Buḫārī (vente de l’or)", "Ṣaḥīḥ al-Buḫārī, le livre des ventes" in h[:6000])
chk("h1 mentionne trois positions et le détail juste", "trois positions" in h[:3200] and "c’est le juste" in h[:3300])
chk("h1 mentionne al-Qārī page 500 et al-Ilmāʿ page 179", "al-Qārī, page 500" in h[:9000] and "page 179" in h[:9500])
chk("h1 mentionne Ibn Sīrīn, Ibn as-Sumaynī, Mālik et les quatre imams",
    "Ibn Sīrīn" in h[:8000] and "Ibn as-Sumaynī" in h[:8500] and "quatre imams" in h[:7500])
chk("h1 mentionne ahtadī wa-aqtadī Ibn aṣ-Ṣalāḥ page 247", "page 247, adapté" in h[:13000])
chk("h1 mentionne ʿIyāḍ page 174 et les activités pratiques",
    "page 174" in h[:13500] and "activités pratiques" in h[:14000])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.125-128 documentées", "pages 125 à 128" in h)
chk("p.124 clôture leçon 23 (autre ouvrier)", "leçon 23" in h and "jamais retouchée" in h)
chk("p.129 bannière leçon 25 sondage, registre vide", "leçon 25" in h and "non touchée" in h)
chk("ONZE lectures d’images consignées", "ONZE lectures d’images" in h and "qa-crops-r658" in h)
chk("corroboration EN LIGNE matn canonique Muqaddima documentée", "corroborée EN LIGNE" in h and "libmim.com" in h)
chk("réf pages tranchées digit-by-digit (324, 500, 179, 247, 174) documentées",
    "324" in h and "500" in h and "179" in h and "247" in h and "174" in h)
chk("titre ʿIyāḍ discordance الإملاء/الإلماع consignée", "discordantes" in h and "al-Ilmāʿ" in h)
chk("coquille 1-2-4 documentée", "1, 2 et 4" in h and "coquille de numérotation" in h)

# ---- objectifs
chk("section objectifs présente", "Les objectifs de la leçon" in h)
chk("objectif 1 (jugement de la transmission selon le sens)", "je reconnais le jugement de la transmission du ḥadīṯ selon le sens" in h)
chk("objectif 2 (distinguer qui peut transmettre selon le sens)", "je distingue entre celui à qui il est permis de transmettre le ḥadīṯ selon le sens" in h)
chk("objectif 3 (mémoriser et transmettre par son texte)", "je veille à mémoriser le ḥadīṯ et à le transmettre par son texte" in h)
chk("objectif 4 (éthique des hommes de science)", "je m’imprègne de l’éthique des hommes de science" in h)

# ---- tamhīd
chk("tamhīd présent", "Le tamhīd (l’introduction)" in h)
chk("tamhīd « l’original chez celui qui a entendu »", "L’original chez celui qui a entendu le ḥadīṯ" in h)
chk("tamhīd question finale", "Quel est donc le jugement de l’abrègement du ḥadīṯ" in h)

# ---- matn
chk("section matn Ibn Ḥaǧar", "le matn du ḥāfiẓ Ibn Ḥaǧar" in h)
chk("matn « changement du texte et du synonyme »", "il n’est pas permis de procéder de dessein au changement du texte et du synonyme" in h)
chk("matn « si la signification est voilée »", "car si la signification est voilée, il faudra l’explication de l’étranger et l’éclaircissement de l’équivoque" in h)

# ---- commentaire (šarḥ + istiḫlāṣ)
chk("gloses lexicales (aš-šarḥ) présentes", "Les gloses lexicales du manuel (aš-šarḥ)" in h)
chk("glose الغريب (loin de son pays, signification cachée)", "celui qui est loin de son pays" in h
    and "ce dont la signification est cachée et dissimulée" in h)
chk("glose المشكل (embrouillée, apparente contradiction)", "s’est embrouillée et est devenue équivoque, par une apparente contradiction" in h)
chk("extraction 2 items", "j’extrais du texte le jugement de l’abrègement du ḥadīṯ" in h
    and "j’extrais du texte le jugement de la transmission du ḥadīṯ selon le sens pour celui qui n’est pas l’homme de science" in h)

# ---- tabṣīṭ première partie (al-iḫtiṣār)
chk("première partie présente", "l’abrègement du ḥadīṯ (al-iḫtiṣār)" in h)
chk("définition iḫtiṣār (économie sur une partie, suppression d’une autre)",
    "l’économie sur une partie du ḥadīṯ et la suppression d’une autre" in h)
chk("position 1 (refus absolu de la transmission selon le sens)",
    "en s’appuyant sur la position du refus absolu de la transmission selon le sens" in h)
chk("position 2 (refus avec transmission au complet une autre fois)",
    "n’a pas transmis le ḥadīṯ au complet une autre fois, et ne sait pas qu’un autre l’a transmis au complet" in h)
chk("position 3 (permis de façon absolue sans détail)", "l’a permis de façon absolue, sans détail" in h)
chk("détail juste (ce qu’il a laissé se distingue, exposé non altéré)",
    "quand ce qu’il a laissé se distingue de ce qu’il a transmis, sans lien avec lui" in h
    and "l’exposé ne soit pas altéré, ni la signification différente" in h)
chk("source Muqaddimat Ibn aṣ-Ṣalāḥ page 324", "Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 324" in h)
chk("exception (permis qu’à l’homme de science)", "cela n’a été permis qu’à l’homme de science, pas à l’autre" in h)
chk("exemple exception « ne vendez pas l’or contre l’or »",
    "ne vendez pas l’or contre l’or, sinon à égalité" in h)
chk("source Ṣaḥīḥ al-Buḫārī البيوع (image contre couche « masḥ »)",
    "Ṣaḥīḥ al-Buḫārī (le correct), le livre des ventes, le chapitre de la vente de l’or contre l’or" in h)
chk("découpage des recueils (plus proche de la permission)",
    "le découpage du recueil unique du ḥadīṯ et son partage en chapitres pour l’argumentation dans les occurrences dispersées" in h
    and "il est plus proche de la permission" in h)
chk("imams Mālik/Aḥmad/Abū Dāwūd/an-Nasāʾî", "comme Mālik, et Aḥmad, et Abū Dāwūd, et an-Nasāʾī, et d’autres" in h)

# ---- tabṣīṭ seconde partie (ar-rawāya bi-l-maʿnā)
chk("seconde partie présente", "le jugement de la transmission du ḥadīṯ selon le sens (ar-rawāya bi-l-maʿnā)" in h)
chk("majorité permise (quatre imams, achève par la signification)",
    "la majorité des anciens et des modernes parmi les traditionalistes, et les gens du fiqh et des principes l’ont permise, parmi eux les quatre imams" in h
    and "le narrateur achève par la signification" in h)
chk("refuseurs (Ibn Sīrīn et d’autres, circonspects)",
    "la transmission du ḥadīṯ n’est pas permise que par son texte" in h
    and "rapporté d’Ibn Sīrīn et d’autres, des circonspects dans la religion de Dieu" in h)
chk("Ibn as-Sumaynī de ʿUmar + Mālik + transmission de la tolérance",
    "Ibn as-Sumaynī l’a rapporté de ʿUmar" in h
    and "c’est peut-être la transmission de la tolérance à ce sujet" in h)
chk("restriction (non adoré par son texte, ni somme des paroles)",
    "à ce qui n’est pas de ce qui est adoré par son texte, ni de la somme des paroles" in h)
chk("source Šarḥ Nuḫbat al-fikr al-Qārī page 500 (×2)",
    h.count("al-Qārī, page 500") >= 1 and "le commentaire de la quintessence de la compréhension dans la terminologie des gens de la tradition" in h)
chk("clause a (mots simples, synonymie, composés)",
    "cela est permis dans les mots simples, pour la clarté de leur synonymie" in h
    and "pas dans les composés, pour leur besoin d’une augmentation" in h)
chk("clause b (texte présent à l’esprit + objection)",
    "cela n’est permis qu’à celui qui a le texte présent à l’esprit" in h
    and "s’il a le texte présent à l’esprit, pourquoi la transmission selon le sens" in h)
chk("clause c (oublié le texte, signification dessinée)",
    "qui mémorisait le ḥadīṯ puis a oublié son texte, et sa signification est restée dessinée dans son esprit" in h)
chk("clause c suite (somme des paroles, sans ajouter ni retrancher)",
    "les paroles de celui qui a reçu la somme des paroles, en rendant toutes leurs significations sans ajouter ni retrancher" in h)
chk("clause c fin (bénédiction du porteur de la Loi révélée, portes du doute)",
    "le prive de la bénédiction des paroles du porteur de la Loi révélée, et ouvre les portes du doute et de la suspicion dans les occurrences de la Sunna" in h)
chk("portée (pas homme de science des mots → pas permis)",
    "si celui-là n’est pas homme de science des mots et de leurs objectifs" in h
    and "cela ne lui est pas permis" in h)
chk("citation répétée (suppression et synonyme)", "au changement du texte, par la suppression et le synonyme" in h)
chk("préférable : rapporter par ses mots sans se permettre de le modifier",
    "le préférable est de rapporter le ḥadīṯ par ses mots, sans se permettre de le modifier" in h)
chk("pratique des savants (comme elle est parvenue, sans la changer dans leurs livres)",
    "la transmission soit rapportée comme elle est parvenue, sans qu’ils la changent dans leurs livres" in h)
chk("ʿIyāḍ « fermer la porte de la transmission selon le sens »",
    "il faut fermer la porte de la transmission selon le sens, pour que ne s’y précipite pas celui qui ne fait pas bien parmi celui qui croit bien faire" in h)
chk("chapitre d’al-Ilmāʿ (vérification de la transmission)",
    "le chapitre de la vérification de la transmission et de la venue par le texte" in h
    and "le préférable est la venue par le texte même, autant qu’on le peut" in h)
chk("source al-Ilmāʿ page 179", "le juge ʿIyāḍ, page 179" in h)

# ---- ahtadī wa-aqtadī
chk("section « je m’oriente et j’imite » présente", "Je m’oriente et j’imite (ahtadī wa-aqtadī)" in h)
chk("citation Ibn aṣ-Ṣalāḥ (facilitation, secours, réussite)",
    "la facilitation, le secours et la réussite" in h and "aux mœurs pures, et aux règles de conduite agréées" in h)
chk("citation Ibn aṣ-Ṣalāḥ (avidité, facilitation dans l’audition)",
    "l’avidité, et la convoitise sur la facilitation dans l’audition" in h)
chk("source Muqaddimat Ibn aṣ-Ṣalāḥ page 247 adapté", "page 247, adapté" in h)

# ---- taqwīm
chk("évaluation présente", "L’évaluation (at-taqwīm)" in h)
chk("taqwīm 3 items (différence / préférable / schéma)",
    "j’extrais de ce qui précède la différence entre l’abrègement du ḥadīṯ et sa transmission selon le sens." in h
    and "je montre le préférable parmi les positions des hommes de science dans l’abrègement du ḥadīṯ." in h
    and "je compose en schéma l’éthique de l’étudiant du ḥadīṯ." in h)

# ---- istiṯmār
chk("exploitation présente", "L’exploitation (al-istiṯmār)" in h)
chk("citation ʿIyāḍ (l’ignorant et le débutant)",
    "sur l’ignorant, et le débutant, et celui qui ne s’est pas exercé dans la science" in h)
chk("citation ʿIyāḍ (que sur le texte entendu, interdiction d’exprimer autrement)",
    "ni ne rapporte de ḥadīṯ que sur le texte qu’il a entendu" in h
    and "il lui est interdit d’exprimer par autre que le texte entendu" in h)
chk("citation ʿIyāḍ (statuer par l’ignorance, attribuer à Dieu)",
    "statuer par l’ignorance" in h and "attribuer à Dieu et à Son Envoyé ce dont il n’a pas la connaissance" in h)
chk("source al-Ilmāʿ page 174", "le juge ʿIyāḍ, page 174" in h)
chk("activité : valeurs de loyauté, sincérité, crainte",
    "je montre ce qui est exigé de l’étudiant du ḥadīṯ de respecter des valeurs de loyauté, de sincérité et de crainte." in h)

# ---- iʿdād al-qiblī
chk("préparation leçon suivante présente", "La préparation de la leçon suivante (al-iʿdād al-qiblī)" in h)
chk("iʿdād leçon 25 activités pratiques (3 points)",
    "La leçon 25 est «\u202f&nbsp; les activités pratiques&nbsp;\u202f»" in h
    and "réalisée au sein de l’établissement" in h
    and "répartis en groupes, chaque groupe réalisant son travail sous la supervision de l’enseignant(e)" in h
    and "présentés en classe pour discussion" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", chr(39) not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd/strong/ol/ul/li)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>") and h.count("<strong>") == h.count("</strong>")
    and h.count("<ol>") == h.count("</ol>") and h.count("<ul>") == h.count("</ul>")
    and h.count("<li>") == h.count("</li>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 274 intact (28 082 car)", len(les["pdf-mut23h2u-274"].get("htmlFr") or "") == 28082)
chk("registre 275 intact (39 200 car)", len(les["pdf-mut23h2u-275"].get("htmlFr") or "") == 39200)
chk("registre 276 intact (25 364 car)", len(les["pdf-mut23h2u-276"].get("htmlFr") or "") == 25364)
fr = les["pdf-mut23h2u-278"].get("htmlFr") or ""
if fr:
    chk("registre 278 = htmlFr posé (24 000-40 000 car)", 24_000 <= len(fr) <= 40_000)
    chk("registre 278 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 278 encore vide (avant hand-set)", True)
fr277 = les["pdf-mut23h2u-277"].get("htmlFr") or ""
chk("registre 277 jamais écrit par ce worker (vide ou contenu d’un autre)",
    fr277 == "" or fr277 != fr)
chk("titleAr pré-mappé 278 intact (leçon 24)",
    les["pdf-mut23h2u-278"].get("titleAr") == "الدرس 24 : الاختصار في الحديث وروايته بالمعنى")
chk("titleFr pré-mappé 278 aligné au h1 (apostrophes normalisées)",
    (les["pdf-mut23h2u-278"].get("titleFr") or "").replace(chr(39), "\u2019")
    == "Leçon 24 : L’abrègement du hadith et sa transmission selon le sens")

print(f"verify-ulumhadith2-pdf278 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
