#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-273
(الدرس 19 : الموضوع والمتروك — al-mawḍūʿ wa-l-matrūk, p.97-101 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.97-101 par sondage image (p.96 = clôture
de la leçon 18, livrée R653, docId pdf-mut23h2u-272 ; p.97 = bannière médaillon « 19 »
+ 4 objectifs + tamhīd sur l'isnād + matn Ibn Ḥaǧar aux cinq visés + gloses + استخلاص ;
p.98-99 = أولا : le forgé (définition, voies du forgeage, marques, causes, jugement,
rang) ; p.99-100 = ثانيا : le délaissé (définition, causes du soupçon, jugement) +
أهتدي وأقتدي ابن الصلاح [ص 236 imprimée — inversion « 632 » récusée par l'image] +
التقويم 2 + الاستثمار السخاوي [فتح المغيث، 1/113] + consigne ; p.101 = الإعداد القبلي
2 items (image p101-idad, « كتب العلال » contre bruit OCR) ; p.102 = ouverture leçon 20
« الحديث المعلل » (sondage, non touchée, registre vide).
Adjudications documentées (SEIZE lectures d'images, tr-tmp/qa-crops-r654/) : matn
« فالأول: الموضُوع، والثاني: المتروك، والثالث: المنكر على رأي، وكذا الرابع والخامس »
contre bruit « الرطام » ; objectif 2 « أسباب وضع الحديث » contre artefact « سات » ;
glose 3 « في منكر قيد الخافة » telle qu'imprimée (600 dpi) ; اصطلاحا complétée « متعمدا
لذلك. وسمي بالموضوع؛ لأن واضعه وضعه من عنده، ويُذكر ضمن أنواع الحديث مع أنه ليس بحديث »
contre couche tronquée ; marque 2 « الأخذ عن شيخه » contre « 3ل تسخه » ; « والإغراب
قصدًا للاشتهار » imprimé ; hadith « ...ومن كذب علي متعمدا فليتبوأ مقعده من النار »
[البخاري، العلم، باب إثم من كذب على النبي] + « القصص » + récusation de « أو غيرها » ;
رتبة « الموضوع شر أنواع الضعيف » + suite المتروك/المنكر/المعلل/المدرج/المقلوب/المضطرب ;
أسباب اتهام (أ) « إلا من جهته...مخالفًا للقواعد المعلومة من الدين بالضرورة » contre
couche illisible ; الاستثمار « بالنظر إلى زعم واضعه » contre « لا في زعم » + « لما
سمي...مع أنه مكذوب على النبي ﷺ » contre « كله » ; أهتدي « وليطهر قلبه » contre
« وليطير » + ص 236 contre inversion « 632 » ; مقاييس اللغة 6/117 contre « 611 » ;
المصباح المنير 1/74 (convergence double couche + identité bibliographique, page
1/74 image autoritaire contre « 1/4 ») ; الإعداد (2) « كتب العلال...عما استفدته »
contre « الغال/هما » ; ZÉRO ĀYA (cache coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf273.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-273-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 19 : Le fabriqué (mawḍūʿ) et le délaissé (matrūk) »",
    hn.startswith("<h1>Leçon 19 : Le fabriqué (mawḍūʿ) et le délaissé (matrūk)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le mensonge délibéré sur le Messager",
    "le mensonge délibéré du rapporteur sur le Messager de Dieu" in h[:800])
chk("h1 mentionne pire des types du faible et plus léger en mal",
    "pire des types du faible" in h[:2000] and "plus léger en mal que le forgé" in h[:2600])
chk("h1 mentionne les voies du forgeage et les quatre marques",
    "les trois voies du forgeage" in h[:2500] and "quatre marques" in h[:3500])
chk("h1 mentionne ahtadī wa-aqtadī Ibn aṣ-Ṣalāḥ et istiṯmār as-Saḫāwī",
    "Ibn aṣ-Ṣalāḥ" in h[:3000] and "as-Saḫāwī" in h[:3200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.97-101 documentées", "pages 97 à 101" in h)
chk("p.96 clôture leçon 18 (R653, 272)", "R653" in h and "pdf-mut23h2u-272" in h)
chk("p.102 leçon 20 sondée, non touchée, registre vide",
    "la leçon 20" in h and "non touchée" in h and "registre vide" in h)
chk("sondage « jamais devinées »", "jamais devinées" in h)
chk("matière multi-couches citée (uh2-l273-raw.txt) + passation R653 (b) + R654",
    "uh2-l273-raw.txt" in h and "passation R653 (b)" in h and "R654" in h)
chk("SEIZE lectures d’images consignées + noms de crops",
    "SEIZE lectures d’images" in h and "p97-banner.png" in h and "p97-objectifs.png" in h
    and "p97-matn-b.png" in h and "p97-istikhlas.png" in h and "p97-sharh3-zoom.png" in h
    and "p98-istilah-zoom.png" in h and "p98-item2-zoom.png" in h and "p99-asbab-wadh.png" in h
    and "p99-hadith.png" in h and "p99-rutba2-zoom.png" in h and "p99-misbah-zoom.png" in h
    and "p100-tuham-a.png" in h and "p100-ahtadi.png" in h and "p100-istithmar.png" in h
    and "p101-idad.png" in h)
chk("matn adjudiqué contre « الرطام » inversé (documenté en FR)",
    "aṭ-ṭalāṯ" in h and "convergence avec les trois gloses" in h)
chk("objectif 2 « causes du forgeage » contre artefact « sāt »",
    "les causes du forgeage du ḥadīṯ" in h and "sāt" in h)
chk("glose 3 « al-ḫāfa » telle qu’imprimée au zoom 600 dpi",
    "al-ḫāfa" in h and "forme imprimée documentée au zoom 600 dpi" in h)
chk("اصطلاحا complétée par l’image contre couche tronquée",
    "fabriqué de son propre cru" in h and "couche tronquée" in h)
chk("marque 2 « l’étude auprès de son maître » contre artefact « 3l tskhh »",
    "l’étude auprès de son maître" in h and "3l tskhh" in h)
chk("« al-iġrāb » imprimé contre variante « al-iġrāʾ »",
    "al-iġrāb" in h and "al-iġrāʾ" in h)
chk("hadith « siège dans le Feu » + البخاري + récusation de « ou autre »",
    "qu’il prépare son siège dans le Feu" in hn and "Ṣaḥīḥ al-Buḫārī" in hn
    and "l’artefact « ou autre » de la couche récusé à l’image" in hn)
chk("رتبة « le pire des types du faible » contre fragment de couche",
    "le forgé est le pire des types du faible" in h and "fragment de couche" in h)
chk("causes du soupçon lues intégralement contre couche illisible",
    "que de son seul côté" in h and "par nécessité" in h and "couche illisible" in h)
chk("استثمار « regard sur la prétention » contre « ou non » + consigne contre « tout entier »",
    "le regard sur la prétention de son fabricateur" in h and "ou non sur la prétention" in h
    and "sur le Prophète tout entier" in h)
chk("أهتدي « purifie son cœur » contre artefact « écarte son cœur »",
    "qu’il purifie son cœur des visées d’ici-bas" in h and "qu’il écarte son cœur" in h)
chk("renvoi Ibn aṣ-Ṣalāḥ page 236 imprimé, inversion 632 récusée par l’image",
    "page 236" in hn and "l’inversion « 632 »" in hn and "non à l’image" in hn)
chk("renvoi Maqāyīs al-luġa 6/117 imprimé contre « 611 »",
    "tome six, page 117" in h and "611" in h)
chk("renvoi al-Miṣbāḥ al-Munīr 1/74 par double convergence + identité bibliographique",
    "al-Miṣbāḥ al-Munīr fī ġarīb aš-Šarḥ al-Kabīr" in h and "double convergence" in h
    and "identité bibliographique" in h and "page 74" in h)
chk("الإعداد (2) « livres des causes » contre bruits « al-ġālī / humā »",
    "un livre des livres des causes" in h and "al-ġālī" in h and "humā" in h)
chk("zéro āya (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)

# ---- objectifs (4)
chk("objectif 1 : reconnaître le concept du forgé et du délaissé",
    "que je reconnaisse le concept du ḥadīṯ forgé (al-mawḍūʿ) et du délaissé (al-matrūk)" in hn)
chk("objectif 2 : comprendre les causes du forgeage (image)",
    "que je comprenne les causes du forgeage du ḥadīṯ (asbāb waḍʿ al-ḥadīṯ)" in hn)
chk("objectif 3 : distinguer forgé et délaissé",
    "que je distingue entre le ḥadīṯ forgé et le ḥadīṯ délaissé" in hn)
chk("objectif 4 : éviter le mensonge sur le Messager + valeur de la véracité (image)",
    "que j’évite le mensonge sur le Messager de Dieu" in hn
    and "que je recherche la valeur de la véracité" in hn)

# ---- tamhīd + matn
chk("tamhīd : isnād particularité de l’Oumma + « sans l’isnād »",
    "particularités de la communauté islamique" in hn and "sans l’isnād, chacun aurait dit ce qu’il veut" in hn)
chk("tamhīd : chaîne menant au texte + probité/precision + préservation/défense",
    "la chaîne des hommes menant au texte" in hn and "de leur probité et de leur précision" in hn
    and "en préservation de la Sunna et en défense d’elle" in hn)
chk("tamhīd : triple question (nom du reconnu menteur / soupçonné / différence)",
    "qu’est-ce donc qu’on nomme le ḥadīṯ de celui qui est reconnu menteur" in hn
    and "le ḥadīṯ du soupçonné de cela" in hn and "la différence entre les deux" in hn)
chk("matn : ordre adjudiqué — forgé, délaissé, réprouvé sur avis, 4ᵉ et 5ᵉ",
    "Le premier : le forgé (al-mawḍūʿ)" in hn and "le deuxième : le délaissé (al-matrūk)" in hn
    and "le troisième : le réprouvé sur avis (al-munakkar ʿalā raʾy), ainsi le quatrième et le cinquième" in hn)

# ---- gloses + istiḫlāṣ
chk("glose 1 : visé par l’atteinte pour le mensonge du rapporteur",
    "ce qui est visé par l’atteinte pour le mensonge du rapporteur" in hn)
chk("glose 2 : visé par l’atteinte pour le soupçon de mensonge",
    "ce qui est visé par l’atteinte pour le soupçon de mensonge porté contre le rapporteur" in hn)
chk("glose 3 : gravité de l’erreur + limite de la légèreté al-ḫāfa (telle qu’imprimée)",
    "celui dont l’erreur est grave" in hn and "la limite de la légèreté (al-ḫāfa) — tel qu’imprimé" in hn)
chk("istiḫlāṣ : définition du forgé et du délaissé",
    "j’extrait de la leçon la définition du forgé (al-mawḍūʿ) et du délaissé (al-matrūk)" in hn)

# ---- tabṣīṭ 1 : le forgé
chk("intro tabṣīṭ : triple question + cinq visés + deux premiers déployés",
    "la triple question" in hn and "l’ordre des cinq visés par l’atteinte" in hn
    and "l’exposition du manuel déploie les deux premiers" in hn)
chk("intro tabṣīṭ : réprouvé sur avis exposé seulement par sa glose",
    "le réprouvé sur avis, n’est exposée ici que par sa glose" in hn)
chk("forgé luga : nom d’agent du posage + abaissement du rang + contigu + origine",
    "un nom d’agent d’une action accomplie" in hn and "l’abaissement de son rang" in hn
    and "le contigu (al-mulṣaq)" in hn and "l’abaissement de la chose et son dépôt" in hn)
chk("forgé luga : renvoi Maqāyīs al-luġa Ibn Fāris 6/117",
    "Maqāyīs al-luġa (les échelles de la langue), Ibn Fāris, tome six, page 117" in hn)
chk("forgé istiilāh : mensonge délibéré + fabriqué de son propre cru + mentionné alors qu’il n’est pas un ḥadīṯ",
    "ce que celui-ci n’a pas dit, délibérément à cela" in hn
    and "son fabricateur l’a fabriqué de son propre cru" in hn
    and "il se mentionne parmi les types du ḥadīṯ alors qu’il n’est pas un ḥadīṯ" in hn)
chk("forgé istiilāh : jugement par opinion dominante non certitude + kaddūb ṣādiq + précaution",
    "la voie de l’opinion dominante (aẓ-ẓann al-ġālib), non par la certitude" in hn
    and "le menteur habituel peut dire vrai, comme le véridique peut mentir" in hn
    and "en précaution pour la Sunna prophétique noble" in hn)
chk("voies du forgeage : trois (invente / prend un propos / monte chaîne authentique)",
    "invente le propos de son propre fonds, puis lui forge une chaîne et le rapporte" in hn
    and "un propos de certains ancêtres, ou de sages, ou d’autres" in hn
    and "lui monte une chaîne authentique pour qu’il circule" in hn)
chk("voies : jugement par l’aperçu total des chaînes + esprit pénétrant",
    "un aperçu total de la connaissance des chaînes et des hommes du ḥadīṯ" in hn
    and "l’esprit pénétrant et à la compréhension forte" in hn)
chk("marque 1 : aveu ʿUmar b. Ṣabīḥ (image)",
    "comme la parole de ʿUmar b. Ṣabīḥ" in hn and "celui qu’on lui a attribué" in hn)
chk("marque 2 : date de naissance impossible l’étude auprès de son maître (image)",
    "l’indication de la date de sa naissance" in hn
    and "rend impossible avec cela l’étude auprès de son maître" in hn)
chk("marque 3 : maître décédé avant la naissance du fabricateur + connu menteur",
    "d’un maître décédé avant la naissance du fabricateur" in hn
    and "le rapporteur soit connu menteur" in hn)
chk("marque 4 : contradiction Coran/Sunna mutawātira (hors mašhūrāt/āḥād) + iǧmāʿ tawātur",
    "le texte du Coran et la Sunna mutawātira" in hn
    and "des célèbres (al-mašhūrāt) et de ce qui suit parmi les ḥadīṯ isolés" in hn
    and "l’accord (al-iǧmāʿ) certain transmis par voie de tawātur" in hn
    and "l’accord par silence et de l’accord conjectural" in hn
    and "on ne déclare pas alors forgé le récit contradictoire" in hn)
chk("marque 4 : pur sens de l’intellect + médiocrité du mot et du sens + témérité promesse/menace",
    "le pur sens de l’intellect" in hn and "la médiocrité du mot et du sens, ou de l’un d’eux" in hn
    and "la témérité dans la promesse et la menace" in hn)
chk("causes du forgeage : ignorance, manque de religion, sectarisme, iġrāb, gain",
    "l’ignorance, le manque de religion, le sectarisme (at-taʿaṣṣub)" in hn
    and "le fait de paraître étranger (al-iġrāb) dans l’intention de se faire connaître" in hn
    and "le gain (at-taksīb)" in hn)
chk("jugement : très grands péchés + interdiction unanime + sauf avec exposé",
    "parmi les très grands péchés" in hn
    and "l’interdiction de rapporter le forgé quand on sait qu’il est forgé" in hn
    and "sauf accompagné de l’exposé de ce qu’il est forgé" in hn)
chk("jugement : hadith siège dans le Feu + renvoi البخاري",
    "« …et quiconque ment sur moi délibérément, qu’il prépare son siège dans le Feu »" in hn
    and "le livre de la science, le chapitre du péché de qui ment sur le Prophète" in hn)
chk("jugement : liste règles/récits/vertus/incitation-avertissement (sans « ou autre »)",
    "que le forgeage touche les règles, ou les récits, ou les vertus, ou l’incitation et l’avertissement" in hn
    and "ce que celui-ci n’a pas dit, en aucun cas" in hn)
chk("rang : pire des types du faible + partie indépendante + suite des six",
    "le forgé est le pire des types du faible" in hn
    and "comme une partie indépendante, non comme un type des types des ḥadīṯ faibles" in hn
    and "et le suit le délaissé, puis le réprouvé, puis le motivé (al-muʿallal)" in hn
    and "puis l’inséré (al-mudraǧ), puis le renversé (al-maqlūb), puis le troublé (al-muḍṭarib)" in hn)

# ---- tabṣīṭ 2 : le délaissé
chk("délaissé luga : laisser la demeure/quitter + emprunté pour les sens",
    "quand il l’a écartée" in hn and "je suis parti d’elle" in hn
    and "emprunté pour l’abandon dans les sens" in hn)
chk("délaissé luga : renvoi al-Miṣbāḥ al-Munīr al-Fayyūmī 1/74 (image)",
    "[al-Miṣbāḥ al-Munīr fī ġarīb aš-Šarḥ al-Kabīr (la lampe éclairante dans le rare du grand commentaire), Aḥmad al-Fayyūmī, tome un, page 74]" in hn)
chk("délaissé istiilāh : chaîne porte un rapporteur soupçonné de mensonge",
    "le ḥadīṯ dont la chaîne porte un rapporteur soupçonné de mensonge" in hn)
chk("délaissé istiilāh : motif de la nomination — isolement + non accepté + dépôt",
    "avec son isolement dans le ḥadīṯ, rend son ḥadīṯ non accepté" in hn
    and "il ne se justifie pas de juger avec son dépôt" in hn)
chk("causes du soupçon : un seul de deux ordres (image)",
    "un seul de deux ordres" in hn)
chk("cause (a) : ne rapporte que de son seul côté + contraire aux règles connues par nécessité (image)",
    "qu’il ne rapporte ce ḥadīṯ que de son seul côté (min ǧihatihi)" in hn
    and "contraire aux règles connues de la religion par nécessité (bi-ḍ-ḍarūra)" in hn)
chk("cause (b) : connu menteur dans son propos même sans mensonge dans le ḥadīṯ",
    "connu menteur dans son propos, même si le mensonge ne paraît pas de lui dans le ḥadīṯ prophétique" in hn)
chk("jugement du délaissé : genre du faible + plus léger en mal que le forgé",
    "le délaissé est du genre du faible" in hn
    and "plus léger en mal que le forgé, dont le possesseur est reconnu menteur" in hn)

# ---- ahtadī + taqwīm + istiṯmār + iʿdād
chk("ahtadī : Ibn aṣ-Ṣalāḥ + science noble + mœurs généreuses/belles dispositions",
    "L’imām Ibn aṣ-Ṣalāḥ, que Dieu lui fasse miséricorde, a dit" in hn
    and "une science noble" in hn and "mœurs généreuses et aux belles dispositions" in hn)
chk("ahtadī : sciences de l’au-delà non de l’ici-bas + rectification de l’intention",
    "des sciences de l’au-delà, non des sciences de l’ici-bas" in hn
    and "la rectification de l’intention et sa pureté" in hn)
chk("ahtadī : renvoi Muqaddimat Ibn aṣ-Ṣalāḥ page 236 imprimé",
    "[Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 236]" in hn)
chk("taqwīm 1 : voies par lesquelles se connaît le forgé",
    "je cite les voies par lesquelles se connaît le ḥadīṯ forgé" in hn)
chk("taqwīm 2 : narration sans exposé de son forgeage",
    "la narration du ḥadīṯ forgé sans exposé de son forgeage" in hn)
chk("istiṯmār : Saḫāwī citation — dispute sur l’insertion + genre commun",
    "la dispute sur l’insertion du forgé parmi les types du ḥadīṯ, pour ce qu’il n’est pas un ḥadīṯ" in hn
    and "l’intention du genre commun (al-qadr al-muštarik)" in hn
    and "ce par quoi se fait le récit" in hn)
chk("istiṯmār : plus belle des deux réponses — connaître les voies + écarter l’accepté",
    "la plus belle des deux réponses" in hn
    and "la connaissance des voies par lesquelles on parvient à sa connaissance" in hn
    and "afin d’écarter l’accepté et le pareil" in hn)
chk("istiṯmār : renvoi Fatḥ al-Muġīṯ 1/113",
    "Fatḥ al-Muġīṯ bi-šarḥ Alfīyat al-ḥadīṯ li-l-ʿIrāqī" in hn
    and "tome un, page 113" in hn)
chk("consigne 1 : pourquoi nommé ḥadīṯ alors mensonge sur le Prophète",
    "pour quoi le « ḥadīṯ forgé » s’est-il nommé ḥadīṯ, alors qu’il est mensonge sur le Prophète" in hn)
chk("iʿdād : leçon 20 le ḥadīṯ défectueux + 2 items",
    "La leçon 20 est" in hn and "le ḥadīṯ défectueux" in hn
    and "(al-ḥadīṯ al-muʿallal)" in hn and "à deux items" in hn)
chk("iʿdād 1 : voies de connaissance du ḥadīṯ motivé dans les livres de terminologie",
    "les voies de connaissance du ḥadīṯ motivé" in hn
    and "les livres de la terminologie du ḥadīṯ" in hn)
chk("iʿdād 2 : introduction d’un livre des causes + résumé concis + exposé aux amis (image)",
    "l’introduction d’un livre des livres des causes (al-ʿilal)" in hn
    and "un résumé concis de ce que j’en ai profité" in hn
    and "je l’expose à mes amis dans la séance suivante" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", chr(39) not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
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
chk("registre 271 intact", 21_000 <= len(les["pdf-mut23h2u-271"].get("htmlFr") or "") <= 26_000)
chk("registre 270 intact (20 432 car)", len(les["pdf-mut23h2u-270"].get("htmlFr") or "") == 20432)
chk("registre 274 non touché (htmlFr vide)", (les["pdf-mut23h2u-274"].get("htmlFr") or "") == "")
fr272 = les["pdf-mut23h2u-272"].get("htmlFr") or ""
chk("registre 272 intact (19 801 car)", len(fr272) == 19801)
fr = les["pdf-mut23h2u-273"].get("htmlFr") or ""
if fr:
    chk("registre 273 = htmlFr posé (19 000-25 000 car)", 19_000 <= len(fr) <= 25_000)
    chk("registre 273 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 273 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 273", les["pdf-mut23h2u-273"].get("titleAr") == "الدرس 19 : الموضوع والمتروك")
chk("titleFr pré-mappé 273 aligné au h1",
    (les["pdf-mut23h2u-273"].get("titleFr") or "") == "Leçon 19 : Le fabriqué (mawḍūʿ) et le délaissé (matrūk)")
chk("titleAr pré-mappé 274 intact (leçon 20, non touchée)",
    les["pdf-mut23h2u-274"].get("titleAr") == "الدرس 20 : الحديث المعلل")

print(f"verify-ulumhadith2-pdf273 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
