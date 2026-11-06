#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-257
(الدرس 3 — al-mutawātir wa-l-āḥād, p.20-25 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.20-25 par DOUBLE sondage
(p.20 = bannière + 3 objectifs + tamhīd ; p.25 = al-iʿdād al-qablī 2 consignes ;
p.26 = bannière + objectifs + muṭūn leçon 4) ; nombres de la couche pdftotext
INVERSÉS tranchés par recadrages 600-1200 dpi + couche logique PyMuPDF FIDÈLE
(mécanisme élucidé : 6/48→84/6→t.6 p.84, 5/892→298/5→t.5 p.298, ṣ951→159,
61→16 ; 31 confirmé) ; conditions du rapporteur (3 pavés graphiques muets)
lues par recadrage 600 dpi ; objectifs (1er muet) et titre at-taqyīm tranchés
par recadrages ; ʿAlqama b. Abī Waqqāṣ al-Laythī et graphie « al-ḫalafīn »
rendus tels qu'imprimés (900 dpi) ; 2 ḥadīṯs prophétiques rendus de l'imprimé,
zéro āya, zéro résidu arabe, zéro apostrophe droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf257.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-257-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 3 : Le massivement transmis (mutawātir) et le singulier (āḥād) »",
    hn.startswith("<h1>Leçon 3 : Le massivement transmis (mutawātir) et le singulier (āḥād)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne conditions et rapporteur", "les conditions de son rapporteur" in h[:500])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.20-25 documentées", "pages 20 à 25" in h)
chk("p.26 leçon 4 non touchée", "pdf-mut23h2u-258" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière tenue par triple concordance", "triple concordance documentée" in h)
chk("caches OCR cités", "tr-tmp/r615/p-020.txt" in h)
chk("tessdata documenté", "tessdata ara disponible en /tmp/tessdata" in hn)
chk("inversion 6/48→84/6 documentée", "6/48" in hn and "84/6" in hn)
chk("Maqāyīs t. 6, p. 84 rendue", "t. 6, p. 84" in hn)
chk("inversion 5/892→298/5 documentée", "5/892" in hn and "298/5" in hn)
chk("Lisān t. 5, p. 298 rendue", "t. 5, p. 298" in hn)
chk("inversion ṣ951→159 documentée", "ṣ951" in hn and "p. 159" in hn)
chk("bāb 61→16 tranché et documenté", "61" in hn and "n° 16" in hn)
chk("usage page/tome documenté", "page/tome" in hn)
chk("mécanisme inversion élucidé (PyMuPDF fidèle)", "PyMuPDF" in hn and "FIDÈLE à l’imprimé" in hn and "miroir" in hn)
chk("recadrages 600 à 1200 dpi documentés", "1200 dpi" in hn)
chk("crops cités", "qa-crops-r615/" in h and "c5-p23-bas-conditions.png" in h
    and "r3-p20-objectifs.png" in h and "c7-p25-titre-taqyim.png" in h
    and "r8-p23-alqama-line2.png" in h and "r10-p25-citation-khatib.png" in h
    and "r11-p22-token16.png" in h)
chk("zéro āya rendue", "Aucune āya rendue" in h)
chk("2 ḥadīṯs prophétiques rendus de l’imprimé",
    "man kaḏaba ʿalayya mutaʿammidan fa-l-yatabawwaʾ maqʿadahū min an-nār" in hn
    and "innamā al-aʿmāl bi-n-niyyāt" in hn)

# ---- objectifs
chk("objectif : concept du mutawātir + conditions + divisions",
    "reconnaisse le concept du massivement transmis (mutawātir) avec ses conditions et ses divisions" in hn)
chk("objectif : concept de l’āḥād et ses divisions",
    "saisisse le concept du singulier (āḥād) et de ses divisions" in hn)
chk("objectif : certification de la science et choix des maîtres",
    "importance de la certification de la science et du bon choix de celui dont on prend la science" in hn)
chk("trois objectifs", "trois objectifs" in hn)

# ---- tamhīd
chk("tamhīd : maqbūl/mardūd", "en accepté (maqbūl) et rejeté (mardūd)" in hn)
chk("tamhīd : qudsī/marfūʿ/mawqūf/maqtūʿ",
    "élevé à Dieu par le sens (qudsī)" in hn and "rattaché au Prophète (marfūʿ)" in hn
    and "arrêté aux Compagnons (mawqūf)" in hn and "tronqué aux Suivants (maqtūʿ)" in hn)
chk("tamhīd : mutawātir/āḥād = considération du propos",
    "en massivement transmis (mutawātir) et singulier (āḥād)" in hn and "dernière considération" in hn)
chk("tamhīd : double question", "deux questions qui orientent la leçon" in hn)

# ---- muṭūn (texte)
chk("muṭūn : « Le premier »", "Le premier" in hn)
chk("muṭūn : producteur de la science certaine selon ses conditions",
    "producteur de la science certaine selon ses conditions" in hn)

# ---- commentaire
chk("exposé : conditions laissées implicites", "conditions du mutawātir implicites dans le texte" in hn)
chk("exposé : uṣūl et non isnād", "ne relève pas des chapitres de la science de l’isnād, mais de ceux de la science des principes (al-uṣūl)" in hn)
chk("exposé : mise en œuvre sans recherche", "sa mise en œuvre étant obligatoire sans recherche" in hn)
chk("extraction : type du ḫabar selon la voie", "un des types du ḫabar selon la voie par laquelle il nous parvient" in hn)
chk("extraction : science certaine + glose marginale",
    "la science certaine (al-ʿilm al-yaqīnī)" in hn and "glose marginale de l’imprimé" in hn
    and "ne demeure plus aucun doute" in hn)

# ---- 1 mutawātir
chk("mutawātir langue : ism fāʿil, tatabbuʿ", "nom d’agent (ism fāʿil) tiré d’at-tawātur, qui est la succession (at-tatabbuʿ)" in hn)
chk("mutawātir terminologie : définition 4 éléments",
    "un grand nombre dont l’usage (al-ʿāda) rend impossible leur collusion sur le mensonge" in hn
    and "rapportant cela de pareils à eux" in hn and "le fondement du rapport est le sensible (al-ḥiss)" in hn)
chk("nombre : divergence des savants", "Les savants ont divergé sur la limite du nombre qui produit le tawātur" in hn)
chk("nombre : dalīl à nombre déterminé non généralisable",
    "un argument où est mentionné un nombre déterminé qui produit la science" in hn
    and "propre à l’affaire en laquelle ce nombre a été mentionné" in hn)
chk("nombre : aucun sens de fixer le nombre sur le ṣaḥīḥ",
    "aucun sens à déterminer le nombre sur le correct (aṣ-ṣaḥīḥ)" in hn)
chk("nombre : istiwāʾ (ne diminue pas, pas qu’elle n’augmente pas)",
    "ne diminue en aucun des lieux — non pas qu’elle n’augmente pas" in hn)
chk("nombre : vu ou entendu, non la raison pure",
    "appuyé sur le vu ou l’entendu, non sur ce qui s’établit par la seule raison pure" in hn
    and "l’un est la moitié de deux" in hn)
chk("existence : Ibn aṣ-Ṣalāḥ (rareté)",
    "Ibn aṣ-Ṣalāḥ que l’exemple du mutawātir, selon la définition précédente, est rare" in hn)
chk("existence : Ṣaḥīḥ al-Buḫārī, Kitāb al-ʿilm, n° 16",
    "Ṣaḥīḥ al-Buḫārī" in hn and "Kitāb al-ʿilm" in hn
    and "Le péché de celui qui ment sur le Prophète" in hn and "n° 16" in hn)
chk("existence : refus (mamlūʿ) + Ibn Ḥibbān et al-Ḥāẓimī",
    "la rareté revendiquée par Ibn aṣ-Ṣalāḥ est refusée (mamlūʿ)" in hn
    and "Ibn Ḥibbān et al-Ḥāẓimī" in hn
    and "défaut d’information sur la multiplicité des voies" in hn)
chk("existence : livres célèbres à consensus", "dont la paternité fait l’objet d’un consensus chez eux" in hn)
chk("existence : Quṭf al-azhār (as-Suyūṭī)", "Quṭf al-azhār al-mutanāṯira fī al-aḫbār al-mutawātira" in hn)
chk("existence : Luqṭ al-laʾālī (az-Zabīdī)", "Luqṭ al-laʾālī al-mutanāṯira fī al-aḫādīṯ al-mutawātira" in hn)
chk("existence : Nazm al-mutanāṯir (al-Kattānī)", "Nazm al-mutanāṯir min al-ḥadīṯ al-mutawātir" in hn)
chk("dallāta : science nécessaire, contrainte de croire",
    "Le mutawātir produit la science nécessaire (al-ʿilm aḍ-ḍarūrī)" in hn
    and "ne pouvant ni le repousser ni hésiter" in hn)
chk("dallāta : objection (homme du commun, naẓar)",
    "comme l’homme du commun" in hn and "ordonnancement de données connues ou probables" in hn)
chk("dallāta : différence nécessaire/théorique en 2 points",
    "sans déduction (istidlāl)" in hn and "pour tout auditeur" in hn
    and "capacité du raisonnement" in hn)
chk("divisions : lafẓī (formulation unique)",
    "rapporté par des voies nombreuses avec une formulation unique" in hn)
chk("divisions : plus de soixante-dix Compagnons", "rapporté par plus de soixante-dix Compagnons" in hn)
chk("divisions : aṭ-Ṭabarānī ǧuzʾ + aṭ-Ṭaḥāwī Šarḥ muškil al-āṯār",
    "réuni ses voies dans un fascicule (ǧuzʾ)" in hn and "Šarḥ muškil al-āṯār" in hn)
chk("divisions : maʿnawī (sens seul, élévations des mains)",
    "le sens seul est massivement transmis, sans la formulation" in hn
    and "élévation des mains dans l’invocation" in hn and "environ cent ḥadīṯs" in hn)

# ---- 2 āḥād
chk("āḥād langue : al-wāḥid, al-Azharī, Abū al-ʿAbbās",
    "porte le sens de al-wāḥid (le seul)" in hn and "al-Azharī a rapporté d’Abū al-ʿAbbās" in hn)
chk("āḥād langue : aḥad n’a pas de pluriel, šāhid/ašhād",
    "al-aḥad n’a pas de pluriel" in hn and "comme šāhid et ašhād" in hn)
chk("āḥād terminologie : pas réuni les conditions",
    "ce qui n’a pas réuni les conditions du mutawātir" in hn)
chk("āḥād exemple : Ṣaḥīḥ al-Buḫārī, Kitāb Badʾ al-waḥy",
    "Kitāb Badʾ al-waḥy" in hn)
chk("āḥād exemple : ʿUmar → ʿAlqama b. Abī Waqqāṣ al-Laythī → at-Taymī",
    "ʿUmar b. al-Khaṭṭāb seul l’a rapporté parmi les Compagnons" in hn
    and "ʿAlqama b. Abī Waqqāṣ al-Laythī seul le rapporta" in hn
    and "Muḥammad b. Ibrāhīm at-Taymī le rapporta seul d’ʿAlqama" in hn
    and "foule nombreuse" in hn)
chk("conditions rapporteur : 3 pavés muets lus par recadrage",
    "trois pavés-flèches graphiques muets pour la couche et pour l’OCR 300 dpi, lus par recadrage 600 dpi" in hn)
chk("conditions rapporteur : probité et véracité",
    "la probité (al-ʿadāla) et la véracité (aṣ-ṣidq) du rapporteur" in hn)
chk("conditions rapporteur : ḍābiṭ taḥammul/adāʾ",
    "précis (ḍābiṭ) dans la mémorisation (at-taḥammul) et la restitution (al-adāʾ)" in hn)
chk("conditions rapporteur : non šāḏḏa", "sa narration ne soit pas anormale (šāḏḏa)" in hn)
chk("divisions : ġarīb/ʿazīz/mašhūr + maqbūl/mardūd",
    "en isolé (ġarīb), rare (ʿazīz) et célèbre (mašhūr)" in hn
    and "en accepté (maqbūl) et rejeté (mardūd)" in hn)
chk("divisions : maqbūl = ǧumhūr, mardūd = véracité ne l’emporte pas",
    "obligatoire selon la majorité (al-ǧumhūr)" in hn
    and "dont la véracité du rapporteur ne l’emporte pas" in hn
    and "contrairement au mutawātir dont tout est accepté" in hn)
chk("divisions : 3 états (racine acceptation/rejet/qarīna-tawaqquf)",
    "racine de la qualité d’acceptation — l’établissement de la véracité du transmetteur" in hn
    and "prédomine la supposition (ġalaba ʿaẓ-ẓann)" in hn
    and "racine de la qualité de rejet" in hn
    and "indication (qarīna)" in hn and "suspension (tawaqquf)" in hn
    and "comme le mardūd — non par l’établissement de la qualité de rejet" in hn)
chk("dallāta : science théorique avec indications, divergence verbale",
    "la science théorique de l’option choisie (al-muḫtār)" in hn
    and "la divergence, dans la recherche précise, est verbale (lafẓī)" in hn
    and "plus solide que ce qui en est dépourvu" in hn)
chk("ḥukm : examen, ṣaḥīḥ ou ḍaʿīf, obligatoire si ṣaḥīḥ",
    "soumis à l’examen" in hn and "authentique (ṣaḥīḥ) ou faible (ḍaʿīf)" in hn
    and "sa mise en œuvre est obligatoire" in hn)

# ---- ahtadī wa-aqtadī (Mālik)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Mālik : la science est une religion", "Cette science est une religion" in hn)
chk("Mālik : soixante-dix rapporteurs", "soixante-dix hommes qui disaient" in hn)
chk("Mālik : bayt māl, dépositaire fidèle",
    "chargé d’un trésor public (bayt māl), en aurait été le dépositaire fidèle" in hn)
chk("Mālik : gens de cette affaire", "ils n’étaient pas des gens de cette affaire" in hn)
chk("Kifāya p. 159", "Al-Kifāya fī ʿilm ar-riwāya d’al-Khaṭīb al-Baġdādī, p. 159" in hn)
chk("tri extrême documenté (spécialité dans l’art)", "le tri extrême que les savants opéraient sur les transmetteurs" in hn)

# ---- évaluation
chk("évaluation : 3 activités", "trois activités" in hn)
chk("évaluation : lafẓī/maʿnawī", "exposer la différence entre le tawātur au mot (lafẓī) et le tawātur au sens (maʿnawī)" in hn)
chk("évaluation : conditions d’acceptation", "exposer les conditions de l’acceptation de la narration du ḫabar āḥād" in hn)
chk("évaluation : différence mutawātir/āḥād", "énoncer la différence entre le mutawātir et l’āḥād" in hn)

# ---- exploitation (al-Khaṭīb)
chk("exploitation : al-Khaṭīb al-Baġdādī, khabar al-wāḥid",
    "La mise en œuvre du ḫabar du seul (khabar al-wāḥid) fut le fait de la totalité des Suivants" in hn)
chk("exploitation : juristes successeurs, contrées des musulmans",
    "parmi les juristes successeurs (al-fuqahāʾ al-ḫalafīn)" in hn
    and "toutes les contrées des musulmans" in hn)
chk("exploitation : aucun désaveu, religion de tous",
    "aucun d’eux de désaveu de cela ni d’objection" in hn
    and "fait partie de la religion de tous" in hn)
chk("exploitation : al-ḫalafīn tel qu’imprimé documenté", "rendue telle qu’imprimée" in hn)
chk("exploitation : Kifāya p. 31", "Al-Kifāya fī ʿilm ar-riwāya, al-Khaṭīb al-Baġdādī, p. 31" in hn)
chk("exploitation : 2 consignes (titre, résumé + arguments)",
    "un titre convenable au texte" in hn and "le résumera et l’appuiera d’arguments" in hn)
chk("exploitation : lien qarīna", "tient lieu d’indication (qarīna) de l’obligation de sa mise en œuvre" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (mašhūr)", "Le hadith célèbre (mašhūr)" in hn)
chk("préparation : relation mašhūr/mustafīḍ", "la relation entre le mašhūr et le mustafīḍ (le diffus) chez le ḥāfiẓ Ibn Ḥaǧar" in hn)
chk("préparation : ḥukm du mašhūr", "exposer le statut (ḥukm) du ḥadīṯ mašhūr" in hn)
chk("préparation : 2 consignes", "deux consignes" in h)

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
chk("registre 258 non touché (htmlFr vide)", (les["pdf-mut23h2u-258"].get("htmlFr") or "") == "")
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
fr = les["pdf-mut23h2u-256"].get("htmlFr") or ""
chk("registre 256 intact (15 854 car)", len(fr) == 15854)
fr7 = les["pdf-mut23h2u-257"].get("htmlFr") or ""
if fr7:
    chk("registre 257 = htmlFr posé (~23 700 car)", 20_000 <= len(fr7) <= 30_000)
    chk("registre 257 == fichier livré", fr7.strip() == h.strip())
else:
    chk("registre 257 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 257", les["pdf-mut23h2u-257"].get("titleAr") == "الدرس 3 : المتواتر والآحاد")
chk("titleFr pré-mappé 257 aligné au h1",
    (les["pdf-mut23h2u-257"].get("titleFr") or "").replace("'", "’").startswith("Leçon 3 : Le massivement transmis (mutawātir) et le singulier (āḥād)"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf257 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
