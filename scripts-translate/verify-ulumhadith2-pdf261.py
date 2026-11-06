#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-261
(الدرس 7 — al-ḥadīṯ al-ḥasan, p.41-46 du manuel ulum-hadith-2-thanawi_text.pdf)
: bornes p.41-46 par DOUBLE sondage (p.41 = bannière verte + badge 7 + boîte
jaune 3 objectifs + tamhīd + matn ; p.46 = évaluation 4 items + istiṯmār
adh-Dhahabī + renvoi al-Mūqiẓa ṣ:28-29 + atāmal an-naṣṣ 2 questions +
al-iʿdād al-qablī 3 consignes ; p.47 = objectifs leçon 8 زيادة الثقة والمحفوظ
والشاذ) ; nombres de la couche pdftotext INVERSÉS tranchés par recadrages
600-1500 dpi + lecture image directe + couche logique PyMuPDF FIDÈLE
(114/13→t.13 p.114, 32-31→p.31-32, 45/2→t.2 p.45, 29-28→p.28-29) ; matn du
quote tranché au 900 dpi (fa-l-tatardad fī t-taqlīd ḥayṯu t-tafarrud) ;
« yarfaʿu ʿan ḥālin » porté tel qu'imprimé (600/900/1200 dpi concordantes,
sens doctrinal d'Ibn aṣ-Ṣalāḥ restitué en FR) ; matn Ibn Ḥibbān tranché par
l'OCR 300 dpi concordant au renvoi (ibnatān, vlm-C2 divergent récusé) ; récit
Mālik « tawaḍḍaʾa wa-tahayyaʾa wa-labisa ṯiyāba-hu » tranché par l'OCR
(vlm-E3 « wa-lam yuṯbit » récusé par le sens) ; istiṯmār « la tazunnanna » à
trois lectures image (OCR « la tatmaʿ » documenté en divergence) ; WIP de la
passe interrompue recoupé (crops G1-G6 + 13 verdicts VLM A1-F1), registre 261
vide au départ ; un seul hadith prophétique rendu des exemples (siwāk) + deux
matns d'exemples (deux filles, vin des orphelins) ; zéro āya, zéro résidu
arabe, zéro apostrophe droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf261.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-261-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 7 : Le hadith satisfaisant (ḥasan) »",
    hn.startswith("<h1>Leçon 7 : Le hadith satisfaisant (ḥasan)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les deux sections d'Ibn aṣ-Ṣalāḥ", "les deux sections du satisfaisant par lui-même d’après Ibn aṣ-Ṣalāḥ" in h[:1200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.41-46 documentées", "pages 41 à 46" in h)
chk("p.47 leçon 8 non touchée", "pdf-mut23h2u-262" in h and "non touché" in h)
chk("p.35-40 leçon 6 non touchée", "pdf-mut23h2u-260" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière concordante au registre et à la table des matières",
    "titleAr pré-mappé" in h and "table des matières" in h)
chk("couches OCR citées", "tr-tmp/r619/" in h and "tr-tmp/r620/" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couche logique PyMuPDF citée", "p041-pymu.txt" in h and "p046-pymu.txt" in h)
chk("WIP de la passe interrompue recoupé", "WIP de la passe interrompue" in h and "claimant défunt recoupé" in h)
chk("verdicts VLM préparatoires cités", "vlm-verdicts" in h and "treize zones A1 à F1" in h)
chk("recadrages d'adjudication 600-1500 dpi cités", "ADJ1 à ADJ12" in h and "1500 dpi" in h)
chk("inversion 114/13→t. 13, p. 114 documentée", "114/13" in hn and "t. 13, p. 114" in hn)
chk("Lisān al-ʿarab t. 13, p. 114 rendue", "Lisān al-ʿarab (la langue des Arabes) d’Ibn Manẓūr, t. 13, p. 114" in hn)
chk("inversion 32-31→p. 31-32 documentée", "32-31" in hn and "p. 31-32" in hn)
chk("Muqaddima p. 35 rendue", "Muqaddimat Ibn aṣ-Ṣalāḥ, p. 35" in hn)
chk("inversion 45/2→t. 2, p. 45 documentée", "45/2" in hn and "t. 2, p. 45" in hn)
chk("aš-Šifāʾ du qāḍī ʿIyāḍ rendue", "Aš-Šifāʾ bi-taʿrīf ḥuqūq al-Muṣṭafā (la guérison par la reconnaissance des droits de l’Élu) du qāḍī ʿIyāḍ, t. 2, p. 45" in hn)
chk("inversion 29-28→p. 28-29 documentée", "29-28" in hn and "p. 28-29" in hn)
chk("al-Mūqiẓa p. 32 rendue (degrés)", "adh-Dhahabī, p. 32" in hn)
chk("mécanisme inversion élucidé (PyMuPDF fidèle)", "PyMuPDF" in hn and "FIDÈLE" in hn and "miroir" in hn)
chk("matn du quote tranché au 900 dpi", "tranché au recadrage 900 dpi" in hn
    and "fa-l-tatardad fī t-taqlīd ḥayṯu t-tafarrud" in hn)
chk("mašhūrīn/šuhūrīn documenté (même racine)", "al-mašhūrīn" in hn and "aš-šuhūrīn" in hn)
chk("« yarfaʿu ʿan ḥālin » tel qu'imprimé (600/900/1200 dpi)",
    "yarfaʿu ʿan ḥālin min baʿdi mā nfarada bi-hi min ḥadīṯi-hi munkaran" in hn
    and "600/900/1200 dpi" in hn and "tel qu’imprimé" in hn)
chk("nom b. ʿĀqiba documenté (divergence OCR)", "b. ʿĀqiba" in hn and "b. ʿAlqama" in hn)
chk("matn Ibn Ḥibbān tranché par le renvoi (ibnatān)", "deux filles" in hn and "vlm-C2" in hn)
chk("récit Mālik tranché par l'OCR (vlm-E3 récusé)", "wa-labisa ṯiyāba-hu" in hn and "vlm-E3" in hn)
chk("istiṯmār « la tazunnanna » à trois lectures image", "la tazunnanna" in hn and "la tatmaʿ" in hn)
chk("zéro āya rendue", "aucune āya rendue" in hn)
chk("hadiths rendus de l'imprimé",
    "Si je n’avais pas éprouvé de la peine pour ma communauté, je leur aurais ordonné le siwāk à chaque prière" in hn
    and "Il n’est aucun musulman qui ait deux filles" in hn
    and "Nous avions chez nous le vin d’orphelins" in hn)

# ---- objectifs
chk("objectif : significations du ḥasan chez les muḥaddiṯūn",
    "reconnaisse les significations (dalālāt) du ḥasan et ses sens (maʿānī) chez les muḥaddiṯūn" in hn)
chk("objectif : distinguer ḥasan li-ḏāti-hi / li-ġayri-hi",
    "distingue le satisfaisant par lui-même (al-ḥasan li-ḏāti-hi) et le satisfaisant par autre que lui" in hn)
chk("objectif : vénérer le hadith du Messager",
    "tienne en vénération le hadith du Messager de Dieu, que la prière et le salut de Dieu soient sur lui, en parole et en acte" in hn)
chk("trois objectifs", "trois buts" in hn)

# ---- tamhīd
chk("tamhīd : rang unique et variation des rapporteurs",
    "n’est pas d’un rang unique" in hn and "selon la variation des qualités de ses rapporteurs" in hn)
chk("tamhīd : tāmm aḍ-ḍabṭ vs ḫafīf aḍ-ḍabṭ",
    "parfaitement maître de sa mémoire (tāmm aḍ-ḍabṭ)" in hn and "maîtrise faible (ḫafīf aḍ-ḍabṭ)" in hn)
chk("tamhīd : question maqbūl/mardūd",
    "relève-t-il du genre de l’accepté (maqbūl) ou du rejeté (mardūd)" in hn)

# ---- muṭūn (texte)
chk("muṭūn : citation Ibn Ḥaǧar complète",
    "Si la maîtrise est faible" in hn and "la multitude de ses voies il s’authentifie" in hn
    and "ne tarde donc pas dans l’attribution (taqlīd) là où est l’unicité (tafarrud)" in hn
    and "considère deux isnād" in hn)
chk("fahm : ḫaffa, fa-in ǧumiʿā, taqlīd",
    "ḫaffa l-qawmu ḫuqūqan" in hn and "l’authentique et le satisfaisant, en un seul et même descriptif" in hn
    and "l’iǧtihād à attribuer le hadith" in hn)
chk("fahm : tâche d'extraction (définition du ḥasan)",
    "extraire du texte la définition du ḥadīṯ ḥasan" in hn)

# ---- 1 ḥasan
chk("langue : ṣifa mušabbaha du ḥusn, contraire du qubḥ",
    "qualité ressemblante (ṣifa mušabbaha) tirée du ḥusn — la beauté —, contraire de la laideur (al-qubḥ)" in hn)
chk("terminologie : division en deux sections",
    "un satisfaisant par lui-même (ḥasan li-ḏāti-hi) et un satisfaisant par autre que lui (ḥasan li-ġayri-hi)" in hn)
chk("Ibn Ḥaǧar : concision du matn, conditions de l'authentique ajoutées",
    "s’est contenté, dans le matn, de dire" in hn and "le reste des conditions énumérées auparavant pour l’authentique" in hn)
chk("Ibn aṣ-Ṣalāḥ : « obscur et ne guérit pas la douleur »",
    "Tout cela demeure obscur et ne guérit pas la douleur" in hn)
chk("section 1 : mastūr, ni muġfal ni muttaham",
    "l’état est voilé (mastūr) sans que son éligibilité ait été vérifiée" in hn
    and "ni négligent (muġfal) commettant de nombreuses erreurs" in hn
    and "ni soupçonné de mensonge (muttaham bi-l-kiḏb)" in hn)
chk("section 1 : muwāfaqa et šāhid, sortie du šāḏḏ/munkar",
    "la concordance (muwāfaqa) de celui qui suit le rapporteur" in hn
    and "le témoin (šāhid)" in hn and "d’être anomal (šāḏḏ) et méconnu (munkar)" in hn)
chk("section 1 : propos d'at-Tirmiḏī", "le propos d’at-Tirmiḏī se rapporte à cette section" in hn)
chk("section 2 : mašhūrīn par ṣidq et amāna, en deçà en ḥifẓ et itqān",
    "du nombre des plus célèbres par la véracité et la fiabilité (al-mašhūrīn bi-aṣ-ṣidq wa-l-amāna)" in hn
    and "en la mémorisation (al-ḥifẓ) et la maîtrise (al-itqān)" in hn)
chk("section 2 : préservation du muʿallal + al-Ḫaṭābī",
    "sa préservation d’être porteur d’un défaut caché (muʿallal)" in hn
    and "les propos d’al-Ḫaṭābī" in hn)
chk("ḥasan li-ġayri-hi : définition Muqaddima p. 31",
    "un homme voilé (mastūr) sans que son éligibilité ait été vérifiée" in hn
    and "[Muqaddimat Ibn aṣ-Ṣalāḥ, p. 31]" in hn)
chk("ḥasan li-ġayri-hi : cause du nom (adjonction des voies)",
    "la qualité du satisfaisant ne vint pas de la chaîne première en soi, mais de l’adjonction d’autres chaînes à elle" in hn)
chk("ḥasan li-ġayri-hi : l'image combinée répare le déficit de maîtrise",
    "l’image combinée possède une force qui répare la part où la maîtrise du rapporteur du satisfaisant resta en deçà" in hn)
chk("exemple siwāk : matn + renvoi Tirmiḏī ṭahāra",
    "bāb mā ǧāʾa fī s-siwāk (chapitre de ce qui fut rapporté sur le siwāk)" in hn)
chk("exemple siwāk : commentaire Ibn aṣ-Ṣalāḥ complet",
    "certains l’affaiblirent pour la mauvaise qualité de sa mémorisation" in hn
    and "cette légère déficience se trouva réparée" in hn
    and "rejoignit le degré de l’authentique" in hn and "Dieu est plus savant" in hn)
chk("exemple Ibn Ḥibbān : isnād (Abū Yaʿlā → Abū Ḫayṯama → Ǧarīr → Fiṭr → Šurayḥ → Ibn ʿAbbās)",
    "Abū Yaʿlā nous a rapportés" in hn and "Abū Ḫayṯama nous a rapportés" in hn
    and "Ǧarīr nous a rapportés, de Fiṭr, de Šurayḥ (Šurayḥ b. Saʿd), d’Ibn ʿAbbās" in hn)
chk("exemple Ibn Ḥibbān : renvoi complet + šawāhid + ad-Dāraquṭnī +",
    "ṣuḥbata-hā fī ḥayāti-hi" in hn and "satisfaisant par ses témoins (bi-šawāhidi-hi)" in hn
    and "comme le dit ad-Dāraquṭnī" in hn and "Ǧarīr : c’est Ibn ʿAbd al-Ḥamīd" in hn
    and "Fiṭr : c’est Ibn Ḫalīfa al-Maḫzūmī" in hn)
chk("exemple vin : isnād ʿĪsā b. Yūnus → Maǧlad → Abī l-Wiḏāk → Abī Saʿīd",
    "ʿĪsā b. Yūnus, de Maǧlad, d’Abī l-Wiḏāk, d’Abī Saʿīd al-Ḫudrī" in hn)
chk("exemple vin : renvoi buyūʿ + commentaire Maǧlad",
    "abwāb al-buyūʿ (les chapitres des ventes)" in hn
    and "le taxèrent d’erreur et de faute" in hn and "rapporté du Prophète, que la prière et le salut de Dieu soient sur lui, par d’autres voies encore" in hn)

# ---- 2 marātib/maṣādir/ḥukm
chk("degrés : variation comme l'authentique",
    "varient comme varient les degrés de l’authentique" in hn and "les uns au-dessus des autres" in hn)
chk("degrés : Baḥz b. Ḥakīm et ʿAmr b. Šuʿayb (père, grand-père)",
    "la chaîne de Baḥz b. Ḥakīm, de son père, de son grand-père" in hn
    and "la chaîne de ʿAmr b. Šuʿayb, de son père, de son grand-père" in hn)
chk("degrés : le plus bas des degrés de l'authentique + al-Ḥāriṯ et ʿĀṣim",
    "le plus bas des degrés de l’authentique" in hn
    and "le hadith d’al-Ḥāriṯ b. ʿAbd Allāh et celui de ʿĀṣim b. Ḍamura" in hn)
chk("sources : Sunan, Musnads, Muṣannafs",
    "les livres des Sunan, des Musnads et des Muṣannafs" in hn)
chk("sources : Ǧāmiʿ at-Tirmiḏī source du ḥasan, sans réserve exclusive",
    "le Ǧāmiʿ at-Tirmiḏī est une source en la connaissance du satisfaisant" in hn
    and "sans qu’il y ait lieu de réserver aux Sunan at-Tirmiḏī" in hn)
chk("statut : maqbūl, variable, li-ḏāti-hi plus fort que li-ġayri-hi",
    "relève du genre de l’accepté : on argumente par lui" in hn
    and "le satisfaisant par lui-même est plus fort que le satisfaisant par autre que lui" in hn)
chk("statut : sens de « ḥasan ṣaḥīḥ » (deux isnād)",
    "l’application des deux descriptifs ensemble au hadith se fait par la considération de deux isnād" in hn
    and "l’un authentique, l’autre satisfaisant" in hn)
chk("statut : « ḥasan ṣaḥīḥ » au-dessus de « ṣaḥīḥ » seul si unique",
    "est au-dessus de ce qu’il désigna « ṣaḥīḥ » seulement — lorsque le hadith est unique — car la multitude des voies renforce" in hn)
chk("statut : objection « ḥasan ġarīb » et réponse",
    "ḥasan ġarīb : nous n’en connaissons pas d’autre voie que celle-ci" in hn
    and "ne définit pas le satisfaisant en absolu" in hn)
chk("statut : les sept formules de Tirmiḏī",
    "« ḥasan ṣaḥīḥ ġarīb »" in hn and "« ṣaḥīḥ ġarīb »" in hn and "sa définition ne porta que sur le premier seul" in hn)
chk("statut : citation finale de Tirmiḏī (ḥasanat isnādi-hi)",
    "Ce que nous désignons en notre livre « ḥasan », nous n’avons voulu dire par là que la bonté de son isnād" in hn
    and "tout hadith rapporté dont le rapporteur n’est pas soupçonné de mensonge" in hn)
chk("statut : dispense de définition + terminologie nouvelle + « chez nous »",
    "par dispens de leur célébrité chez les gens de l’art" in hn
    and "soit parce que c’est une terminologie nouvelle" in hn and "sans la rapporter aux gens du hadith" in hn)

# ---- ahtadī wa-aqtadī (Mālik)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Mālik : ablutions par vénération",
    "sans être en état d’ablutions, par vénération pour lui" in hn)
chk("Mālik : se préparait, revêtait ses vêtements",
    "il faisait ses ablutions et se préparait, revêtait ses vêtements, puis il rapportait" in hn)
chk("Mālik : réponse « c'est le hadith du Messager de Dieu »",
    "on l’interrogea sur cela, et il répondit : c’est le hadith du Messager de Dieu" in hn)
chk("lien à l'étiquette du porteur",
    "celui qui transmet la parole prophétique la porte en état de pureté et de préparation" in hn)

# ---- évaluation
chk("évaluation : 4 activités", "quatre activités" in hn)
chk("évaluation : types + exemples", "énoncer les types du ḥadīṯ ḥasan et en donner des exemples" in hn)
chk("évaluation : conditions ḥasan vs ṣaḥīḥ", "distinguer les conditions du ḥadīṯ ḥasan et celles du ḥadīṯ ṣaḥīḥ" in hn)
chk("évaluation : sens de « ḥasan ṣaḥīḥ »", "expliciter le sens de l’expression « ḥasan ṣaḥīḥ »" in hn)
chk("évaluation : étiquettes du chercheur de hadith", "extraire les étiquettes du chercheur de hadith" in hn)

# ---- exploitation (adh-Dhahabī)
chk("exploitation : citation adh-Dhahabī complète",
    "Ne pense pas que le satisfaisant constitue une règle où viendraient se ranger tous les hadiths satisfaisants — j’en désespère" in hn
    and "Combien de hadiths firent hésiter les ḥuffāẓ" in hn
    and "Le ḥāfiẓ seul et unique voit son iǧtihād changer en un hadith unique" in hn
    and "un autre jour il le décrit par le satisfaisant, et parfois il l’affaiblit" in hn)
chk("exploitation : atāmal an-naṣṣ deux questions",
    "méditer le texte et à répondre aux deux questions" in hn
    and "le jugement du savant sur un hadith — par l’authenticité ou la faiblesse — est-il définitif, ou susceptible de changement" in hn)
chk("exploitation : leçon d'humilité scientifique",
    "les degrés du hadith ne sont pas des cases rigides" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (ziyādat aṯ-ṯiqa…)", "L’ajout du transmetteur fiable, le retenu (maḥfūẓ) et l’anomal (šāḏḏ)" in hn)
chk("préparation : statut de l'ajout du fiable", "le statut (ḥukm) de l’ajout du transmetteur fiable (ziyādat aṯ-ṯiqa)" in hn)
chk("préparation : définir šāḏḏ et maḥfūẓ + exemple", "définir l’anomal (aš-šāḏḏ) et le retenu (al-maḥfūẓ) et donner un exemple de chacun des deux" in hn)
chk("préparation : différence šāḏḏ/maḥfūẓ", "la différence entre l’anomal et le retenu" in hn)
chk("préparation : 3 consignes", "trois consignes" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
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
chk("registre 262 non touché (htmlFr vide)", (les["pdf-mut23h2u-262"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-261"].get("htmlFr") or ""
if fr:
    chk("registre 261 = htmlFr posé (~28 600 car)", 20_000 <= len(fr) <= 35_000)
    chk("registre 261 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 261 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 261", les["pdf-mut23h2u-261"].get("titleAr") == "الدرس 7 : الحديث الحسن")
chk("titleFr pré-mappé 261 aligné au h1",
    (les["pdf-mut23h2u-261"].get("titleFr") or "").replace("'", "’").startswith("Leçon 7 : Le hadith satisfaisant (ḥasan)"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf261 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
