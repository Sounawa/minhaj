#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-262
(الدرس 8 — ziyādat aṯ-ṯiqa wa-l-maḥfūẓ wa-š-šāḏḏ, p.47-51 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.47-51 par DOUBLE sondage (p.47 =
bannière الدرس 8 + 4 objectifs + tamhīd + matn Ibn Ḥaǧar + fahm ; p.51 =
évaluation 3 items + istiṯmār Muqaddima ṣ 79 + iʿdād qablī 2 consignes ;
p.52 = bannière leçon 9 المعروف والمنكر) ; WIP sous-agent interrompu recoupé
(20 zones VLM A-S3 + 12 pages 4 couches, claim expiré 50,8 min, takeover
légitime par mtimes, registre 262 vide) ; SIX recadrages d'adjudication
450-900 dpi lecture image directe ; nombres pdftotext INVERSÉS tranchés
(2/78→t. 2 p. 87 Maqāyīs ḥ-f-ẓ, 3/081→t. 3 p. 180 š-ḏ-ḏ بتصرف,
2/802→t. 2 p. 208 al-Ǧāmiʿ, 97→p. 79 Muqaddima) ; matn du quote tranché par
QUATRE lectures concordantes (mā lam tanāfiʿa manāfiyatan li-man huwa awṯaq,
fa-in ḫuwwifa bi-arǧaḥ ; vlm-A tanāfiʾ manāṭ al-ʿadl récusé, vlm-P ḫullifa
documenté) ; diagramme p. 48 (عدد→2 cases, موطن الزيادة→3 cases, ADJ1 image
directe, vlm-Q fragmentaire récusé) ; schéma p. 49 quatre cas concordant à
trois lectures ; matn muḥfūẓ p. 49→50 porté avec points de suspension
IMPRIMÉS, fa-rāwā-hu rétabli par ADJ3 ; renvoi Tirmiḏī bāb mā ǧāʾa fī
l-iḍṭiǧāʿ (vlm-G al-inḍibāʿ récusé) ; renvoi Bukhārī kitāb al-ǧumuʿa, bāb
aḍ-ḍiǧāʿa ʿalā š-šiqq al-ayman tranché au zoom 900 dpi ×4 (lectures
intermédiaires aṣ-ṣubḥ / aḍ-ḍuḥā récusées, OCR concordant) ; Abū l-Aswad
(OCR concordant, vlm-H récusé) ; citation al-Ḫaṭīb tranchée par ADJ4/ADJ5
(yatamahhar, yaqifu, yastanīru, mutašattita, wa-ḍamma ; wa-ḏakkā l-qalb non
al-hamma) ; istiṯmār aqrāʾu n-naṣṣa (vlm-I récusé) ; deux hadiths prophétiques
rendus (fragment du mourant avec points de suspension imprimés ; les deux
rakʿas de l'aube en versions Tirmiḏī/Buḫārī) ; zéro āya, zéro résidu arabe,
zéro apostrophe droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf262.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-262-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"
REG1 = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

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
chk("h1 = titleFr pré-mappé « Leçon 8 : L'ajout du transmetteur fiable, le retenu (maḥfūẓ) et l'anomal (šāḏḏ) »",
    hn.startswith("<h1>Leçon 8 : L’ajout du transmetteur fiable, le retenu (maḥfūẓ) et l’anomal (šāḏḏ)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le schéma des quatre cas", "le schéma des quatre cas" in h[:1500])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.47-51 documentées", "pages 47 à 51" in h)
chk("p.41-46 leçon 7 non touchée", "pdf-mut23h2u-261" in h and "non touché" in h)
chk("p.52 leçon 9 non touchée", "pdf-mut23h2u-263" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière concordante au registre et à la table des matières",
    "titleAr pré-mappé" in h and "table des matières" in h)
chk("extraction multicouche tr-tmp/r621/ citée", "tr-tmp/r621/" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couches logiques p047-pymu à p051-pymu citées",
    "p047-pymu" in h and "p051-pymu" in h)
chk("WIP sous-agent interrompu recoupé", "WIP de la passe sous-agent interrompue" in h
    and "vingt zones VLM" in hn)
chk("claim expiré 50,8 min + takeover légitime", "50,8 min" in hn and "takeover légitime" in hn)
chk("recadrages ADJ cités (450-900 dpi, image directe)",
    "450-900 dpi" in hn and "image DIRECTE" in hn)
chk("inversion 2/78→t. 2, p. 87 documentée", "2/78" in hn and "t. 2, p. 87" in hn)
chk("Maqāyīs t. 2, p. 87 rendue (ḥ-f-ẓ)", "Maqāyīs al-luġa (les mesures de la langue) d’Ibn Fāris, t. 2, p. 87" in hn)
chk("inversion 3/081→t. 3, p. 180 documentée", "3/081" in hn and "t. 3, p. 180" in hn)
chk("inversion 2/802→t. 2, p. 208 documentée", "2/802" in hn and "t. 2, p. 208" in hn)
chk("inversion 97→p. 79 documentée (Muqaddima)", "97" in hn and "p. 79" in hn
    and "vlm-I concordant" in hn)
chk("mécanisme inversion élucidé (miroir, jamais devinée)", "INVERSÉS EN MIROIR" in hn and "jamais devinée" in hn)
chk("matn du quote tranché par QUATRE lectures", "QUATRE lectures concordantes" in hn
    and "mā lam tanāfiʿa manāfiyatan li-man huwa awṯaq" in hn)
chk("fa-in ḫuwwifa porté, ḫullifa vlm-P documenté", "ḫuwwifa" in hn and "ḫullifa" in hn and "vlm-P" in hn)
chk("vlm-A tanāfiʾ manāṭ al-ʿadl récusé", "tanāfiʾ manāṭ al-ʿadl" in hn)
chk("diagramme p. 48 : 2 cases nombre, 3 cases lieu (ADJ1, vlm-Q récusé)",
    "DEUX cases (un seul, plus d’un)" in hn and "TROIS cases" in hn and "vlm-Q" in hn)
chk("schéma p. 49 : quatre cas, trois lectures concordantes",
    "yatawaqqafu fī-hā" in hn and "trois lectures concordantes" in hn)
chk("matn muḥfūẓ points de suspension imprimés", "points de suspension IMPRIMÉS" in hn)
chk("fa-rāwā-hu rétabli par ADJ3", "fa-rāwā-hu" in hn and "ADJ3" in hn)
chk("renvoi Tirmiḏī iḍṭiǧāʿ (vlm-G récusé)", "bāb mā ǧāʾa fī l-iḍṭiǧāʿ" in hn and "al-inḍibāʿ" in hn)
chk("renvoi Bukhārī ḍiǧāʿa tranché zoom 900 dpi ×4 (ADJ7o)",
    "bāb aḍ-ḍiǧāʿa ʿalā š-šiqq al-ayman" in hn and "ADJ7o" in hn and "aṣ-ṣubḥ" in hn and "aḍ-ḍuḥā" in hn)
chk("Abū l-Aswad porté (vlm-H récusé)", "Abū l-Aswad" in hn and "Abū Hurayra" in hn and "récusé" in hn)
chk("citation al-Ḫaṭīb tranchée (ADJ4/ADJ5)", "yatamahhar" in hn and "yastanīru" in hn
    and "wa-ḍamma" in hn and "ADJ5" in hn)
chk("al-Ḫaṭīb : wa-ḏakkā l-qalb (non al-hamma)", "wa-ḏakkā l-qalb" in hn and "al-hamma" in hn)
chk("wa-lā yatāʾtā tel qu'imprimé + sens restitué",
    "wa-lā yatāʾtā ḏālika ʿalā ṭarīq al-muḥaddiṯīn" in hn and "sens doctrinal restitué en traduction" in hn)
chk("istiṯmār aqrāʾu n-naṣṣa (vlm-I récusé)", "aqrāʾu n-naṣṣa" in hn and "vlm-I « afrā" in hn)
chk("zéro āya rendue", "aucune āya rendue" in hn)
chk("hadiths rendus de l'imprimé",
    "qu’un homme mourut du vivant du Messager de Dieu" in hn
    and "Lorsque l’un de vous prie les deux rakʿas de l’aube, qu’il s’allonge sur son côté droit" in hn
    and "s’allongeait sur son côté droit" in hn)

# ---- objectifs
chk("objectif : concept ziyādat aṯ-ṯiqa, formes, statut",
    "concept de l’ajout du transmetteur fiable (ziyādat aṯ-ṯiqa), ses formes et son statut" in hn)
chk("objectif : concept šāḏḏ et maḥfūẓ",
    "concept du hadith anomal (šāḏḏ) et du retenu (maḥfūẓ)" in hn)
chk("objectif : relation šāḏḏ/munkar + utilité",
    "relation entre l’anomal et le méconnu (munkar) et l’utilité de leur connaissance" in hn)
chk("objectif : retenir par cœur et par livre",
    "retenir ce qu’il entend et à le maîtriser" in hn)
chk("quatre objectifs", "quatre buts" in hn)

# ---- tamhīd
chk("tamhīd : contradiction → terminologies des gens du hadith",
    "produit un certain nombre de terminologies des gens du hadith" in hn)
chk("tamhīd : relative à l'isnād ou au matn",
    "relative à l’isnād" in hn and "relative au matn" in hn)
chk("tamhīd : selon l'état du rapporteur, accepté/rejeté",
    "selon l’état du rapporteur et sa description" in hn and "tantôt accepté, tantôt rejeté" in hn)
chk("tamhīd : double question finale",
    "l’ajout du transmetteur fiable qui contredit plus fiable que lui et l’ajout du transmetteur faible qui contredit le fiable" in hn)

# ---- muṭūn (texte)
chk("muṭūn : citation Ibn Ḥaǧar complète",
    "l’ajout du rapporteur des deux est accepté" in hn
    and "s’il est contredit par plus fort, le plus fort est le retenu (al-maḥfūẓ), et son contraire est l’anomal (aš-šāḏḏ)" in hn)
chk("fahm : aṯ-ṯiqa = al-muʾtaman, yuṯaq ṯiqatan, ṯiqāt",
    "dont on garantit la fiabilité (al-muʾtaman)" in hn and "yuṯaq ṯiqatan" in hn and "ṯiqāt" in hn)
chk("fahm : maḥfūẓ = ce que rapporta l'awṯaq contredisant ceux d'en dessous",
    "ce que rapporta le plus fiable (al-awṯaq) en contredisant ceux qui sont en dessous de lui parmi les fiables" in hn)
chk("fahm : deux tâches d'extraction", "le statut de l’ajout du transmetteur fiable" in hn
    and "la définition du retenu et de l’anomal" in hn)

# ---- 1 ziyādat aṯ-ṯiqa
chk("définition : infirād du rapporteur accepté avec addition",
    "l’isolement (infirād) du rapporteur dont le hadith est accepté avec une addition que le reste des rapporteurs n’a pas mentionnée" in hn)
chk("ce qu'on en tire : aḥkām, taqyīd al-iṭlāq, iḍāḥat al-maʿānī",
    "l’augmentation des jugements (ziyādat al-aḥkām)" in hn
    and "la restriction de l’absolu (taqyīd al-iṭlāq)" in hn
    and "l’éclaircissement des sens (iḍāḥat al-maʿānī)" in hn
    and "la réunion des voies du hadith" in hn)
chk("formes : nombre (wāḥid / akṯar min wāḥid)",
    "bi-iʿtibār al-ʿadad" in hn and "wāḥid" in hn and "akṯar min wāḥid" in hn)
chk("formes : lieu (sanad / matn / les deux)",
    "bi-iʿtibār mawḍiʿ az-ziyāda" in hn and "fī s-sanad" in hn and "fī l-matn" in hn
    and "fī s-sanad wa-l-matn" in hn)
chk("statut : condition de non-contradiction du plus fiable",
    "accepté à condition qu’il ne survienne pas en contradiction et en opposition avec la narration de quelqu’un de plus fiable" in hn)
chk("cas a : non-contradiction → accepté en absolu (rang du hadith indépendant)",
    "un tel ajout est accepté en absolu, car il est au rang du hadith indépendant" in hn
    and "que le fiable transmet seul de son maître" in hn)
chk("cas b : contradiction → tarǧīḥ, on accepte le plus fort",
    "s’exerce le tarǧīḥ entre lui et ce qui le contredit" in hn
    and "on accepte le plus fort et on rejette le plus faible" in hn)
chk("doctrine : troupe de savants + voie des muḥaddiṯūn (šāḏḏ = contradiction du plus fiable)",
    "le dire de l’acceptation de l’ajout en absolu, sans détail" in hn
    and "expliquent l’anomalie par la contradiction du fiable envers plus fiable que lui" in hn)
chk("imams anciens listés (Ibn al-Mahdī → ad-Dāraquṭnī)",
    "ʿAbd ar-Raḥmān b. Mahdī" in hn and "Yaḥyā al-Qaṭṭān" in hn and "Aḥmad b. Ḥanbal" in hn
    and "Yaḥyā b. Maʿīn" in hn and "ʿAlī b. al-Madīnī" in hn and "al-Buḫārī" in hn
    and "Abū Zurʿa" in hn and "Abū Ḥātim" in hn and "an-Nasāʾī" in hn and "ad-Dāraquṭnī" in hn)
chk("aucun d'eux n'a accepté l'ajout en absolu",
    "l’on ne connaît aucun d’entre eux qui ait accepté l’ajout en absolu" in hn)
chk("quatre cas numérotés (maqbūl/mardūd/mimṯāl/suspension)",
    "(1) l’ajout n’est pas contradictoire&nbsp;: il est accepté (maqbūl)".replace("&nbsp;", " ") in hn
    and "(2) il contredit plus fiable que lui&nbsp;: il est rejeté (mardūd)".replace("&nbsp;", " ") in hn
    and "(3) il contredit quelqu’un de moins fiable que lui&nbsp;: il est accepté".replace("&nbsp;", " ") in hn
    and "(4) il contredit son pareil (mimṯāl)" in hn)

# ---- 2 maḥfūẓ
chk("langue : chose protégée, ḥifẓ, ḥafaẓtu š-šayʾa ḥifẓan, taḥaffuẓ",
    "la chose protégée qui demeure en son état" in hn and "ḥafaẓtu š-šayʾa ḥifẓan" in hn
    and "le peu de négligence" in hn)
chk("terminologie : awṯaq contredisant fiable en dessous + citation Ibn Ḥaǧar",
    "ce que rapporta le plus fiable (al-awṯaq) en contredisant la narration d’un fiable en dessous de lui" in hn
    and "s’il est contredit par plus fort, le plus fort est le retenu" in hn)
chk("tarǧīḥ : ḍabṭ accru, multitude, autres voies",
    "une maîtrise de la mémoire accrue" in hn and "une multitude de rapporteurs" in hn
    and "d’autres voies encore de tarǧīḥ" in hn)
chk("exemple : Tirmiḏī/Nasāʾī/Ibn Māǧah via Ibn ʿAyna → ʿAmr b. Dīnār → ʿAwṣaǧa → Ibn ʿAbbās",
    "at-Tirmiḏī, an-Nasāʾī et Ibn Māǧah, de la voie d’Ibn ʿAyna, de ʿAmr b. Dīnār, de ʿAwṣaǧa, d’Ibn ʿAbbās" in hn)
chk("exemple : renvoi abwāb al-farāʾiḍ", "abwāb al-farāʾiḍ (les chapitres des successions)" in hn)
chk("exemple : Ibn Ǧurayǧ suit le waṣl, Ḥammād b. Zayd contredit sans Ibn ʿAbbās",
    "Ibn ʿAyna fut suivi sur son lien (waṣl) par Ibn Ǧurayǧ" in hn
    and "les contredit Ḥammād b. Zayd" in hn and "sans mentionner Ibn ʿAbbās" in hn)
chk("Abū Ḥātim : « le retenu est le hadith d'Ibn ʿAyna » + justice et maîtrise de Ḥammād + multitude préférée",
    "le retenu est le hadith d’Ibn ʿAyna" in hn
    and "Ḥammād b. Zayd est du nombre des hommes de justice et de maîtrise de la mémoire" in hn
    and "préféra la narration de ceux qui sont plus nombreux que lui" in hn)
chk("statut du maḥfūẓ : du genre du maqbūl",
    "il est du genre du hadith accepté (al-maqbūl)" in hn)

# ---- 3 šāḏḏ
chk("langue : infirād et mufāraqa, šāḏa yašīḏu šuḏūḏan",
    "l’isolement et le fait de sortir du rang (al-infirād wa-l-mufāraqa)" in hn
    and "šāḏa š-šayʾu yašīḏu šuḏūḏan" in hn)
chk("terminologie : maqbūl contredisant plus digne",
    "ce que rapporta l’accepté (al-maqbūl) en contredisant celui qui est plus digne (awlā) que lui" in hn)
chk("Ibn aṣ-Ṣalāḥ unifiait munkar/šāḏḏ, Ibn Ḥaǧar distinguait",
    "avait unifié le méconnu (al-munkar) et l’anomal (aš-šāḏḏ)" in hn
    and "l’anomal a un rapporteur fiable, et le méconnu a un rapporteur faible" in hn)
chk("distinction aqwam wa-asadd, as-Saḫāwī préféra",
    "plus droite et plus ferme (aqwam wa-asadd)" in hn
    and "l’imām as-Saḫāwī préféra ce qu’avait établi le ḥāfiẓ Ibn Ḥaǧar" in hn)
chk("šuḏūḏ : sanad / matn / les deux + chaque type a des exemples",
    "peut être dans l’isnād, et elle peut être dans le matn, et elle peut être dans les deux ensemble" in hn
    and "chaque type a des exemples" in hn)
chk("exemple précédent = šāḏḏ dans l'isnād (médite-le)",
    "il est un exemple de l’anomalie dans l’isnād (médite-le !)" in hn)
chk("exemple matn : isnād Bušr b. Muʿāḏ → ʿAbd al-Wāhid b. Ziyād → al-Aʿmaš → Abū Ṣāliḥ → Abū Hurayra",
    "Bušr b. Muʿāḏ al-ʿUqadī nous a rapportés" in hn
    and "ʿAbd al-Wāhid b. Ziyād nous a rapportés" in hn
    and "al-Aʿmaš nous a rapportés, d’Abū Ṣāliḥ, d’Abū Hurayra" in hn)
chk("exemple matn : renvoi abwāb aṣ-ṣalāt complet",
    "abwāb aṣ-ṣalāt (les chapitres de la prière), bāb mā ǧāʾa fī l-iḍṭiǧāʿ (chapitre de ce qui fut rapporté sur le fait de s’allonger)" in hn)
chk("correctif : acte non parole, Buḫārī + isnād ʿAbd Allāh b. Yazīd → Saʿīd b. Abī Ayyūb → Abū l-Aswad → ʿUrwa → ʿĀʾiša",
    "ne relève pas de la parole du Prophète, que la prière et le salut de Dieu soient sur lui, mais de son acte" in hn
    and "ʿAbd Allāh b. Yazīd nous a rapportés" in hn and "Saʿīd b. Abī Ayyūb nous a rapportés" in hn
    and "Abū l-Aswad m’a informé, de ʿUrwa b. az-Zubayr, de ʿĀʾiša" in hn)
chk("exemple matn : renvoi kitāb al-ǧumuʿa complet",
    "kitāb al-ǧumuʿa (le livre de la prière du vendredi), bāb aḍ-ḍiǧāʿa ʿalā š-šiqq al-ayman (chapitre du fait de s’allonger sur le côté droit)" in hn)
chk("statut du šāḏḏ : du genre du mardūd (contredit plus fiable et plus maître)",
    "il est du genre du rejeté (al-mardūd)" in hn
    and "a contredit quelqu’un de plus fiable et plus maître de sa mémoire que lui" in hn)

# ---- ahtadī wa-aqtadī (al-Ḫaṭīb)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("al-Ḫaṭīb : citation complète (yatamahhar → taḫlīd)",
    "Rarement quelqu’un s’applique avec ardeur dans la science du hadith" in hn
    and "s’arrête sur ses énigmes" in hn
    and "réuni ses passages dispersés" in hn
    and "classification de ses chapitres et à l’ordonnance de ses espèces" in hn
    and "fortifient l’âme, affermissent la mémoire, réveillent le cœur" in hn
    and "la belle mémoire et sa perpétuité jusqu’à la fin des temps" in hn)
chk("renvoi al-Ǧāmiʿ t. 2, p. 208 rendu",
    "al-Ǧāmiʿ li-aḫlāq ar-rāwī wa-ādāb as-sāmiʿ (le recueil des qualités du transmetteur et des règles de l’auditeur) d’al-Ḫaṭīb al-Baġdādī, t. 2, p. 208" in hn)
chk("lien pédagogique : réunion des voies révèle l'ajout",
    "c’est en réunissant les voies, en classant les chapitres et en comparant les versions que l’ajout se révèle" in hn)

# ---- évaluation
chk("évaluation : 3 activités", "trois activités" in hn)
chk("évaluation : types selon le lieu de l'ajout",
    "énoncer les types de l’ajout du transmetteur fiable selon le lieu de l’ajout" in hn)
chk("évaluation : différence šāḏḏ/maḥfūẓ",
    "expliciter la différence entre l’anomal et le retenu" in hn)
chk("évaluation : exemple šāḏḏ + exemple maḥfūẓ",
    "évoquer un exemple de hadith anomal et un exemple de hadith retenu" in hn)

# ---- exploitation (Ibn aṣ-Ṣalāḥ)
chk("exploitation : citation Ibn aṣ-Ṣalāḥ complète",
    "Lorsque le rapporteur s’isole avec une chose qui fait l’objet d’un examen" in hn
    and "ce par quoi il s’isole est anomal, rejeté" in hn
    and "une affaire qu’il a rapportée sans que d’autres la rapportent" in hn
    and "s’il est probe, mémorisateur, digne de confiance par l’accomplissement et la maîtrise de sa mémoire" in hn
    and "son isolement l’exclut, le déplace du domaine de l’authentique" in hn)
chk("exploitation : renvoi Muqaddima p. 79 rendu",
    "Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), p. 79" in hn)
chk("exploitation : deux questions",
    "lire le texte et expliciter la différence entre l’isolement du fiable dans la narration et l’isolement du faible" in hn
    and "l’importance de l’accomplissement (al-itqān) et de la maîtrise (aḍ-ḍabṭ) pour l’étudiant du hadith" in hn)
chk("exploitation : l'isolement n'est pas en soi un défaut",
    "l’isolement n’est pas, en lui-même, un défaut" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (maʿrūf/munkar)", "Le hadith reconnu (maʿrūf) et le méconnu (munkar)" in hn)
chk("préparation : sens maʿrūf et munkar",
    "le sens du hadith reconnu (al-maʿrūf) et du méconnu (al-munkar)" in hn)
chk("préparation : différence munkar/šāḏḏ",
    "la différence entre le méconnu (al-munkar) et l’anomal (aš-šāḏḏ)" in hn)
chk("préparation : 2 consignes", "deux consignes" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("zéro artefact de réflexion", not re.search(r"hmm|non plus|plutôt —", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
chk("registre 256 intact (15 854 car)", len(les["pdf-mut23h2u-256"].get("htmlFr") or "") == 15854)
chk("registre 257 intact (~23 700 car)", 20_000 <= len(les["pdf-mut23h2u-257"].get("htmlFr") or "") <= 30_000)
chk("registre 258 intact (19 291 car)", len(les["pdf-mut23h2u-258"].get("htmlFr") or "") == 19291)
chk("registre 259 intact (~23 800 car)", 20_000 <= len(les["pdf-mut23h2u-259"].get("htmlFr") or "") <= 30_000)
chk("registre 260 intact (29 786 car)", len(les["pdf-mut23h2u-260"].get("htmlFr") or "") == 29786)
chk("registre 261 intact (~28 600 car)", 25_000 <= len(les["pdf-mut23h2u-261"].get("htmlFr") or "") <= 32_000)
chk("registre 263 non touché (htmlFr vide)", (les["pdf-mut23h2u-263"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-262"].get("htmlFr") or ""
if fr:
    chk("registre 262 = htmlFr posé (~28 000 car)", 24_000 <= len(fr) <= 33_000)
    chk("registre 262 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 262 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 262", les["pdf-mut23h2u-262"].get("titleAr") == "الدرس 8 : زيادة الثقة والمحفوظ والشاذ")
chk("titleFr pré-mappé 262 aligné au h1",
    (les["pdf-mut23h2u-262"].get("titleFr") or "").replace("'", "’").startswith("Leçon 8 : L’ajout du transmetteur fiable"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf262 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
