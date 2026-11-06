#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-256
(الدرس 2 — al-ḫabar wa-l-ḥadīṯ wa-l-aṯar, p.17-19 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.17-19 par DOUBLE sondage
(p.17 = objectifs + tamhīd + muṭūn ; p.19 = al-iʿdād al-qablī 3 consignes ;
p.20 = bannière leçon 3) ; nombres de la couche INVERSÉS tranchés par OCR
300 dpi + recadrages 600/900/1200 dpi (1/871→1/178, 2/54→2/45, ṣ51→15,
1ṣ7:5→157 ; 36/2, 56/1 lus 300 dpi concordants canon Hārūn) ; 3ᵉ hémistiche
d'as-Suyūṭī muet couche+OCR tranché par image (lection imprimée
« wa-šahhirū radaf al-ḥadīṯ wa-l-aṯar », variante du v.12 documentée d'après
le šarḥ d'al-Āṯiobī) ; tronçon moyen de l'histoire de Mālik tenu par la couche
; zéro āya, zéro hadith prophétique, zéro résidu arabe, zéro apostrophe
droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf256.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-256-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 2 : Le ḫabar, le hadith et l’aṯar »",
    hn.startswith("<h1>Leçon 2 : Le ḫabar, le hadith et l’aṯar"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les trois termes", "trois termes de la transmission" in h[:500])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.17-19 documentées", "pages 17 à 19" in h)
chk("p.20 leçon 3 non touchée", "pdf-mut23h2u-257" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière tenue par triple concordance", "triple concordance documentée" in h)
chk("caches OCR cités", "tr-tmp/r614/p-017.txt" in h)
chk("tessdata documenté", "tessdata ara disponible en /tmp/tessdata" in hn)
chk("inversion 1/871→1/178 documentée", "1/871" in hn and "1/178" in hn)
chk("inversion 2/54→2/45 documentée", "2/54" in hn and "2/45" in hn)
chk("inversion ṣ51→15 documentée", "ṣ51" in hn and "p. 15" in hn)
chk("fragment 1ṣ7:5→157 documenté", "1ṣ7:5" in hn and "p. 157" in hn)
chk("références 36/2 et 56/1 documentées", "36/2" in hn and "56/1" in hn)
chk("usage page/tome documenté", "« page/tome »" in hn or "page/tome" in hn)
chk("recadrages 600 dpi documentés", "600 dpi" in hn)
chk("crops cités", "qa-crops-r614/" in h and "p19-verse3-word2.png" in h)
chk("zéro āya rendue", "Aucune āya rendue" in h)
chk("zéro hadith prophétique cité", "aucun ḥadīṯ prophétique cité" in h)

# ---- objectifs
chk("objectif : concept des trois termes", "reconnaisse le concept du ḥadīṯ, du ḫabar et de l’aṯar" in hn)
chk("objectif : distinguer les termes", "distingue entre les termes précédents" in hn)
chk("objectif : vénérer les savants", "vénère les savants et estime leurs efforts" in hn)

# ---- tamhīd
chk("tamhīd : méthode coranique et prophétique", "méthode coranique et prophétique unique" in hn)
chk("tamhīd : héritiers des prophètes", "héritiers des prophètes héritent de cet héritage" in hn)
chk("tamhīd : ḥamāl al-wuǧūh", "supporte de multiples acceptions (ḥamāl al-wuǧūh)" in hn)
chk("tamhīd : double question", "deux questions qui orientent la leçon" in hn)

# ---- muṭūn (texte)
chk("muṭūn : « je dis donc »", "Je dis donc" in hn)
chk("muṭūn : voies sans nombre déterminé", "voies de transmission (ṭuruq) sans nombre déterminé" in hn)
chk("muṭūn : restriction au-delà de deux", "restriction à ce qui dépasse les deux" in hn)
chk("muṭūn : les deux / une seule", "par les deux, ou par une seule" in hn)

# ---- commentaire (glosses + extraction)
chk("glose ṭuruq = asānīd", "ce sont les chaînes de transmission (al-asānīd)" in hn)
chk("glose isnād", "l’isnād est la relation de la voie du muṭūn" in hn)
chk("glose ḥaṣr : trois tant que le mutawātir n’est pas réuni",
    "à partir de trois et au-delà, tant que ne sont pas réunies les conditions du mutawātir" in hn)
chk("glose ḫabbartu l-amra", "je l’ai connu selon sa réalité" in hn)
chk("extraction : types du ḫabar selon la voie", "les types du ḫabar selon la voie par laquelle il nous est parvenu" in hn)

# ---- 1 ḫabar
chk("ḫabar langue : aḫbartuhu bi-kayda", "aḫbartuhu bi-kayda" in hn)
chk("ḫabar langue : istiḫbār", "al-istiḫbār est la question portant sur le ḫabar" in hn)
chk("ḫabar langue : muḫbir/manqir, ḫabīr", "al-muḫbir est le contraire d’al-manqir" in hn and "al-ḫabīr est le savant" in hn)
chk("Ṣiḥāḥ 1/178 tranchée", "aṣ-Ṣiḥāḥ d’al-Ǧawharī, t. 1, p. 178" in hn)
chk("ḫabar terminologie : synonyme du ḥadīṯ", "est synonyme du ḥadīṯ" in hn)
chk("ḫabar : ašmal (plus englobant)", "pour qu’il soit plus englobant" in hn)
chk("ḫabar : aʿamm muṭlaq", "le ḫabar est plus général en absolu" in hn)
chk("ḫabar : chaque fois que l’aʿamm s’établit", "chaque fois que le plus général s’établit, le plus particulier s’établit" in hn)
chk("ḫabar : rang inférieur", "il est de rang inférieur à ce ḥadīṯ" in hn)
chk("Qārī p. 157", "šarḥ Nuḫbat al-fikr d’al-Qārī, p. 157" in hn)

# ---- 2 ḥadīṯ
chk("ḥadīṯ langue : le neuf", "Le ḥadīṯ est le neuf (al-ǧadīd)" in hn)
chk("ḥadīṯ langue : chose après l’autre", "une chose advient après l’autre" in hn)
chk("Maqāyīs 2/36", "Maqāyīs al-luġa d’Ibn Fāris, t. 2, p. 36" in hn)
chk("ḥadīṯ terminologie : 4 catégories", "en parole, ou en acte, ou en approbation (taqrīr), ou en qualité" in hn)
chk("différence : 3 avis (mutarādifān…)", "ils sont synonymes (mutarādifān)" in hn)
chk("différence : iḫbārī/muḥaddiṯ", "« al-iḫbārī » celui qui s’occupe des chroniques" in hn and "« al-muḥaddiṯ » celui qui s’occupe de la Sunna" in hn)
chk("différence : ʿumūm wa-ḫuṣūṣ muṭlaq", "généralisation et la particularisation absolues (ʿumūm wa-ḫuṣūṣ muṭlaq)" in hn)
chk("différence : tout ḥadīṯ est un ḫabar", "tout ḥadīṯ est un ḫabar, sans que ce soit le cas de l’inverse" in hn)

# ---- 3 aṯar
chk("aṯar langue : trace, 3 acceptions", "précéder la chose, mentionner la chose, et tracer la chose restante" in hn)
chk("Maqāyīs 1/56", "Maqāyīs al-luġa d’Ibn Fāris, t. 1, p. 56" in hn)
chk("aṯar langue : ce que les anciens ont laissé", "ce que les anciens ont laissé derrière eux" in hn)
chk("aṯar terminologie : Ṣaḥīḥ Muslim, āṯār", "muqaddima du Ṣaḥīḥ de l’imām Muslim" in hn and "nommés « āṯār »" in hn)
chk("aṯar terminologie : aṯarī", "« al-aṯarī » celui qui s’occupe du ḥadīṯ" in hn)
chk("aṯar terminologie : aʿamm (Ṣaḥāba, tābiʿīn)", "l’aṯar englobe ce qui est rapporté de lui et d’autres" in hn and "les Suivants (at-tābiʿīn)" in hn)
chk("aṯar terminologie : mutabāyinān", "ils sont dissemblables (mutabāyinān)" in hn)

# ---- ahtadī wa-aqtadī (Mālik)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Mālik : question préalable", "voulez-vous le ḥadīṯ, ou les questions juridiques" in hn)
chk("Mālik : bain, ablutions, parfum", "il entrait à son bain, faisait ses ablutions, se parfumait" in hn)
chk("Mālik : habits neufs, turban, minbar", "revêtait des habits neufs et se coiffait du turban" in hn and "l’on dressait pour lui son minbar" in hn)
chk("Mālik : ḫušūʿ et ʿūd", "humilité recueillie (ḫušūʿ)" in hn and "brûler de l’encens (al-ʿūd)" in hn)
chk("Mālik : Ibn Abī ʿUways", "Ibn Abī ʿUways" in hn)
chk("Mālik : pureté assurée", "à ne le transmettre qu’en état de pureté assurée" in hn)
chk("aš-Šifā 2/45 tranchée", "aš-Šifā bi-taʿrīf ḥuqūq al-Muṣṭafā d’al-Qāḍī ʿIyāḍ, t. 2, p. 45" in hn)

# ---- évaluation
chk("évaluation : 2 activités", "deux activités" in hn)
chk("évaluation : différence exposée", "exposer la différence entre le ḥadīṯ, le ḫabar et l’aṯar" in hn)
chk("évaluation : deux manifestations", "extraire deux manifestations" in hn)

# ---- exploitation (vers as-Suyūṭī)
chk("exploitation : as-Suyūṭī, Alfiyya", "l’imām as-Suyūṭī" in hn and "Alfiyya" in hn)
chk("vers 1 : attribué au Prophète en parole", "attribué au Prophète en parole" in hn)
chk("vers 1 : acte, approbation, semblables", "en acte, en approbation et en leurs semblables" in hn)
chk("vers 2 : ne se restreint pas au marfūʿ", "il ne se restreint pas au marfūʿ" in hn)
chk("vers 2 : mawqūf et maqtūʿ", "vaut aussi pour le mawqūf et le maqtūʿ" in hn)
chk("vers 3 : synonyme du ḫabar", "il est, d’après cela, synonyme du ḫabar" in hn)
chk("vers 3 : lection imprimée rendue", "wa-šahhirū radaf al-ḥadīṯ wa-l-aṯar" in hn)
chk("vers 3 : variante canonique documentée", "wa-šahhirū šumūl haḏayn al-aṯar" in hn)
chk("vers 3 : tranchage 900/1200 dpi + psm 8", "900 et 1200 dpi" in hn and "psm 8" in hn)
chk("Alfiyya p. 15", "Alfiyya d’as-Suyūṭī, p. 15" in hn)
chk("consigne : style propre", "avec son propre style le contenu de ces vers" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée", "Le massivement transmis (mutawātir) et le singulier (āḥād)" in hn)
chk("préparation : mutawātir types/conditions", "les types et les conditions" in hn)
chk("préparation : āḥād et subdivisions", "le concept de l’āḥād et de ses subdivisions" in hn)
chk("préparation : mutawātir lafẓī", "exemples de mutawātir lafẓī" in hn)
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
chk("registre 257 non touché (htmlFr vide)", (les["pdf-mut23h2u-257"].get("htmlFr") or "") == "")
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
fr = les["pdf-mut23h2u-256"].get("htmlFr") or ""
if fr:
    chk("registre 256 = htmlFr posé (~15 854 car)", 15_000 <= len(fr) <= 16_800)
    chk("registre 256 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 256 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 256", les["pdf-mut23h2u-256"].get("titleAr") == "الدرس 2 : الخبر والحديث والأثر")
chk("titleFr pré-mappé 256 aligné au h1",
    (les["pdf-mut23h2u-256"].get("titleFr") or "").replace("'", "’").startswith("Leçon 2 : Le ḫabar, le hadith et l’aṯar"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf256 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
