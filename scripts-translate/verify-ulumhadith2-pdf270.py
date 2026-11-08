#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-270
(الدرس 16 : المعضل والمنقطع — al-ḥadīṯ al-muʿḍal wa-l-munqaṭiʿ, p.83-87 du
manuel ulum-hadith-2-thanawi_text.pdf) : bornes p.83-87 par sondage (p.82 =
clôture de la leçon 15, livrée R645, docId pdf-mut23h2u-269 ; p.83 = bannière
ad-dars 16 « المعضل والمنقطع » + 3 objectifs + vertu + tamhīd + matn
« والثالث: إن كان باثنين فصاعدا مع التوالي فهو المعضل وإلا فالمنفطع »
(image) + الشرح + استخلاص ; p.84 = أولا الحديث المعضل (لغة [مقاييس 4/345] /
اصطلاحا [فتح المغيث 1/199] + قول ابن الصلاح [ص 136] + شرط التتابع + اجتماع/
افتراق مع المعلق + مثال الأعمش) ; p.85 = fin المثال [ص 60] + حكم المعضل +
ثانيا الحديث المنقطع (لغة [مقاييس 5/101] / اصطلاحا + المتأخرين + صور ثلاث
exceptées + ابن الصلاح [ص 58] + اختلاف المنقطع والمرسل، ابن حجر) ; p.86 =
مثال الحاكم [معرفة علوم الحديث ص 28] + حكم المنقطع + أهتدي وأقتدي (ابن عبد
البر) + التقويم ; p.87 = الاستثمار [فتح المغيث 1/201 بتصرف] + consigne +
الإعداد القبلي (2 items) ; p.88 = ouverture leçon 17 « السقط الظاهر والخفي »
(sondage couche brute, non touchée, registre vide)) ; extraction MULTICOUCHE
(brute + fix p.83-91 = tr-tmp/uh2-l270-raw.txt, embed p.83 = p83-embed.txt
R645b, embed livre complet = r635/fullbook-embed.txt) ; DIX lectures d'images
consignées (R646 : 6 ; R646c : 4 — p83-a-matn, p84-a-tasmia, p84-b-sokhawi,
p84-c/d/e, p83-b-istihlas, p86-a-isnad-matn, p86-b-hukm, p87-a-istithmar) ;
VÉRIFICATION EXTERNE du texte du Ḥākim (Maʿrifat ʿulūm al-ḥadīṯ — ablibrary)
: chaîne et commentaire conformes nom à nom (al-Faqīh, al-Ḥaḍramī, Zayd b.
Yaṯīʿ rétablis) ; CORRIGÉS D'OCR : échange ṭāʾ/qāf (طقسلا=السقط, عطقنملا=
المنقطع) ; LOI DES NOMBRES R646 : groupes chiffrés à oblique = échange des
deux groupes (199/1→1/199, 345/4→4/345, 201/1→1/201 — image-confirmés), sans
oblique = ordre logique (28 image-confirmé ; 58, 60, 101, 136) ; renvoi
lexicographie [ص 136] — lecture initiale « 631 » récusée par la loi, consignée.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf270.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-270-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 16 : Le hadith à double rupture (muʿḍal) et à rupture simple (munqaṭiʿ) »",
    hn.startswith("<h1>Leçon 16 : Le hadith à double rupture (muʿḍal) et à rupture simple (munqaṭiʿ)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne la chute dans la chaîne (as-suqūṭ / al-isnād)",
    "la chute (as-suqūṭ) dans la chaîne (al-isnād)" in h[:1400])
chk("h1 mentionne Maqāyīs al-luġa et Ibn Fāris", "Maqāyīs al-luġa d’Ibn Fāris" in h[:2200])
chk("h1 mentionne Fatḥ al-Maġīṯ d’aṯ-Ṣaḫāwī", "Fatḥ al-Maġīṯ d’aṯ-Ṣaḫāwī" in h[:1600])
chk("h1 mentionne les postérieurs (al-mutaʾaḫḫirūn)", "al-mutaʾaḫḫirūn" in h[:3000])
chk("h1 mentionne le Ḥākim et Ḥuḏayfa", "Ḥākim an-Naysābūrī" in h[:3200] and "Ḥuḏayfa" in h[:3200])
chk("h1 mentionne ʿAbd ar-Razzāq et aṯ-Ṯawrí/ṯawrī",
    "ʿAbd ar-Razzāq" in h[:3400] and "aṯ-Ṯawrī" in h[:3400])
chk("h1 mentionne la rupture aux deux places",
    "la rupture aux deux places" in h[:3200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.83-87 documentées", "pages 83 à 87" in h)
chk("p.82 clôture leçon 15 (R645, 269)", "R645" in h and "pdf-mut23h2u-269" in h)
chk("p.88 leçon 17 sondée, non touchée, registre vide",
    "la leçon 17" in h and "non touchée" in h and "registre vide" in h)
chk("sondage « jamais devinées »", "jamais devinées" in h)
chk("couches brute + fix p.83-91 citées (uh2-l270-raw.txt)",
    "uh2-l270-raw.txt" in h and "mots réinversés" in h)
chk("couches incorporées citées (p83-embed R645b + livre complet)",
    "p83-embed.txt" in h and "fullbook-embed.txt" in h)
chk("DIX lectures d’images consignées (6 R646 + 4 R646c)",
    "p83-a-matn.png" in h and "p86-a-isnad-matn.png" in h
    and "p87-a-istithmar.png" in h and "DIX lectures d’images" in h)
chk("vérification externe du Ḥākim documentée (ablibrary)",
    "ablibrary.net" in h and "Maʿrifat ʿulūm al-ḥadīṯ" in h)
chk("rétablissements al-Faqīh et Zayd b. Yaṯīʿ consignés",
    "al-Faqīh" in hn and "Zayd b. Yaṯīʿ" in hn and "jamais devinés" in h)
chk("corrigé d’OCR السقط/المنقطع (échange ṭāʾ/qāf) documenté",
    "ṭāʾ/qāf" in h)
chk("LOI DES NOMBRES définie et appliquée",
    "LOI DES NOMBRES" in h and "199/1" in h and "345/4" in h and "201/1" in h)
chk("renvoi lexicographie 136 — lecture initiale 631 récusée consignée",
    "page 136" in hn and "631" in h)

# ---- nombres tranchés
chk("Maqāyīs 4/345 (العُضل)", "tome 4, page 345" in hn)
chk("Fatḥ al-Maġīṯ 1/199 (dénomination du muʿḍal)", "tome 1, page 199" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.136 (luġa)", "page 136" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.60 (exemple al-Aʿmaš)", "page 60" in hn)
chk("Maqāyīs 5/101 (القطع)", "tome 5, page 101" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.58 (usage irrāsal/inqiṭāʿ)", "page 58" in hn)
chk("Maʿrifat ʿulūm al-ḥadīṯ p.28 (exemple du Ḥākim)",
    "le Ḥākim an-Naysābūrī, page 28" in hn)
chk("Fatḥ al-Maġīṯ 1/201 بتصرف (exploitation)",
    "tome 1, page 201" in hn and "en remaniement (bi-taṣrīf)" in hn)

# ---- objectifs (3 + 1 vertu)
chk("objectif 1 : concept du muʿḍal et du manqaṭiʿ",
    "le concept du ḥadīṯ muʿḍal" in hn)
chk("objectif 2 : cause du rejet", "la cause du rejet" in hn)
chk("objectif 3 : distinguer muʿḍal / manqaṭiʿ",
    "que je distingue le muʿḍal du manqaṭiʿ" in hn)
chk("objectif 4 : fidélité + restituer le propos à son auteur",
    "la fidélité (al-amāna)" in hn and "restitue le propos à son auteur" in hn)

# ---- tamhīd
chk("tamhīd : chute selon la place + deux hommes succession/hors succession",
    "selon la place de la chute" in hn
    and "deux hommes, en succession, ou hors succession" in hn)
chk("tamhīd : double question + faces d’intersection et de divergence",
    "la première espèce" in hn and "la deuxième" in hn
    and "les faces d’intersection et de divergence entre eux deux" in hn)

# ---- matn Ibn Ḥaǧar + gloses + istiḫlāṣ
chk("matn : « Le troisième »",
    "Le troisième (wa-ṯ-ṯāliṯ)" in hn)
chk("matn : deux hommes et au-delà + en succession + muʿḍal",
    "deux hommes et au-delà (bi-ṯnayn fa-ṣāʿidan), en succession" in hn)
chk("matn : « sinon, c’est le munfaṭiʿ »",
    "c’est le munfaṭiʿ" in hn)
chk("glose : troisième espèce des espèces de la chute",
    "la troisième espèce parmi les espèces de la chute" in hn)
chk("glose : hors le premier et hors le dernier",
    "hors le premier (de la chaîne) et hors le dernier" in hn)
chk("glose : fa-ṣāʿidan = au-dessus de cela",
    "Fa-ṣāʿidan" in hn and "au-dessus de cela" in hn)
chk("istiḫlāṣ 1 : définition du muʿḍal du texte",
    "j’extrais du texte la définition du ḥadīṯ muʿḍal" in hn)
chk("istiḫlāṣ 2 : différence muʿḍal/manqaṭiʿ",
    "la différence entre le muʿḍal et le manqaṭiʿ" in hn)

# ---- taḥlīl 1 : muʿḍal
chk("luġa muʿḍal : aʿṭaltu l-amra / aʿyaytuhu / intensité et torsion",
    "aʿṭaltu l-amra" in hn and "aʿyaytuhu" in hn and "l’intensité et la torsion" in hn)
chk("iṣṭilāḥ muʿḍal : succession + estropié + rétréci + taʿdīl/ǧarḥ",
    "en succession (ʿalā t-tawālī)" in hn and "il l’a estropié (aʿṭalahu)" in hn
    and "rétréci pour celui qui le transmet" in hn
    and "at-taʿdīl" in hn and "al-ǧarḥ" in hn)
chk("iṣṭilāḥ muʿḍal : šaddada ʿalayhi l-ḥāl tranché en image",
    "šaddada ʿalayhi l-ḥāl" in hn and "tranché par la lecture d’image à 1100 dpi" in hn)
chk("Ibn aṣ-Ṣalāḥ luġa : dād ouverte / muʿṣal / trilitère hamzé / ʿaḍīl / faʿīl-fāʿil",
    "dād ouverte" in hn and "muʿṣal" in hn and "hamza" in hn
    and "affaire ʿaḍīl" in hn and "faʿīl au sens de fāʿil" in hn)
chk("condition : succession + mafhūm (si pas de succession → pas muʿḍal)",
    "le sens implicite (mafhūmuhu)" in hn and "il ne se nomme pas muʿḍal" in hn)
chk("réunion : début deux successifs = muʿḍal et muʿallaq",
    "il est muʿḍal et muʿallaq à la fois" in hn)
chk("divergence : milieu deux successifs = muʿḍal ; début un seul = muʿallaq",
    "mais pas muʿallaq" in hn and "mais pas muʿḍal" in hn)
chk("exemple al-Aʿmaš/aš-Šaʿbī + sceau sur sa bouche",
    "al-Aʿmaš" in hn and "aš-Šaʿbī" in hn and "un sceau sera apposé sur sa bouche" in hn)
chk("exemple : omis Anas et le Prophète",
    "al-Aʿmaš y a donc omis Anas et le Prophète" in hn)
chk("statut muʿḍal : faible, pire que manqaṭiʿ/mursal, multiplicité des omis",
    "relève du faible (aḍ-ḍaʿīf)" in hn and "en pire état que le manqaṭiʿ et le mursal" in hn
    and "la multiplicité des omis" in hn)

# ---- taḥlīl 2 : manqaṭiʿ
chk("luġa manqaṭiʿ : ism fāʿil + contraire de la liaison + rupture sèche",
    "nom d’agent (ism fāʿil)" in hn and "le contraire de la liaison (al-ittiṣāl)" in hn
    and "rupture sèche (ṣaram)" in hn)
chk("iṣṭilāḥ manqaṭiʿ : un homme ou plus + absence de succession + munfaṭiʿ",
    "un homme ou plus, sous la condition de l’absence de succession" in hn
    and "c’est le munfaṭiʿ" in hn)
chk("iṣṭilāḥ : nom général + trois figures exceptées (début/fin/deux successifs)",
    "nom général pour toute rupture" in hn and "sauf trois figures" in hn
    and "l’omission du début de l’isnād" in hn and "l’omission de sa fin" in hn
    and "deux hommes successifs de quelque place que ce soit" in hn)
chk("iṣṭilāḥ : plus général + exclusivités (tābiʿīn / deux en succession / début)",
    "plus général (aʿamm)" in hn and "li-iḫtiṣāṣ" in hn and "aux Successeurs (at-tābiʿīn)" in hn)
chk("citation Ibn aṣ-Ṣalāḥ : usage + Successeur du Prophète + Mālik/Ibn ʿUmar",
    "l’angle de l’usage" in hn and "narre le Successeur (at-tābiʿī) du Prophète" in hn
    and "Mālik d’après Ibn ʿUmar" in hn)
chk("divergence Ibn Ḥaǧar : mutagāyirān + verbe dérivé + arsalahu + nukta",
    "mutagāyirān" in hn and "verbe dérivé" in hn and "l’a émis (arsalahu)" in hn
    and "la finesse (an-nukta)" in hn)
chk("exemple Ḥākim : chaîne complète (Abū an-Naḍr…ʿAbd ar-Razzāq…Ḥuḏayfa)",
    "Abū an-Naḍr Muḥammad b. Muḥammad b. Yūsuf al-Faqīh" in hn
    and "Muḥammad b. Sulaymān al-Ḥaḍramī" in hn and "Muḥammad b. Sahl" in hn
    and "ʿAbd ar-Razzāq" in hn and "Zayd b. Yaṯīʿ" in hn and "Ḥuḏayfa" in hn)
chk("matn Ḥākim : Abū Bakr fort/digne de confiance + blâme du blâmeur",
    "Abū Bakr" in hn and "fort, digne de confiance" in hn
    and "le blâme du blâmeur ne le saisit pas dans Dieu" in hn)
chk("matn Ḥākim : ʿAlī guide bien-guidé + chemin droit",
    "ʿAlī — alors il est guide, bien-guidé" in hn and "un chemin droit" in hn)
chk("commentaire Ḥākim : deux fiables + rupture en deux places",
    "deux fiables (ṯiqatān)" in hn and "rupture (inqiṭāʿ) en deux places" in hn
    and "ne l’a pas entendu d’aṯ-Ṯawrī" in hn and "ne l’a pas entendu d’Abū Isḥāq" in hn)
chk("statut manqaṭiʿ : faible + condition manquante = liaison de la chaîne",
    "relève du faible (min qabīl aḍ-ḍaʿīf)" in hn
    and "une condition parmi les conditions de l’acceptation" in hn
    and "la liaison de la chaîne (ittiṣāl as-sanad)" in hn)

# ---- ahtadī wa-aqtadī + taqwīm + istiṯmār + iʿdād
chk("ahtadī : Ibn ʿAbd al-Barr + bénédictions de la science + restituer",
    "Ibn ʿAbd al-Barr" in hn and "les bénédictions de la science (barakat al-ʿilm)" in hn
    and "que tu restitues la chose à son auteur" in hn)
chk("taqwīm 1 : différence muʿḍal/manqaṭiʿ", "je décris la différence entre le muʿḍal et le manqaṭiʿ" in hn)
chk("taqwīm 2 : figures non embrassées chez les postérieurs",
    "que n’embrasse pas le nom du manqaṭiʿ chez les postérieurs" in hn)
chk("taqwīm 3 : valeur du propos d’Ibn ʿAbd al-Barr + importance",
    "la valeur tirée du propos d’Ibn ʿAbd al-Barr" in hn
    and "l’étudiant en science" in hn)
chk("istiṯmār : aṯ-Ṣaḫāwī + rien ne s’interrompt absolument + difficulté du sens",
    "ne s’interrompt absolument rien" in hn and "la difficulté de leur sens" in hn)
chk("istiṯmār : consigne face de dénomination chez quelques rapporteurs",
    "la face de la dénomination «\u202f&nbsp;\u202fmuʿḍal&nbsp;\u202f» de ce dont le sens" in h)
chk("iʿdād : leçon 17 chute apparente/cachée + 2 items",
    "la chute apparente et la chute cachée" in hn and "deux items" in hn
    and "chacune se connaît" in hn and "espèces inscrites" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd/strong/ol/li)",
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
chk("registre 267 intact (25 238 car)", len(les["pdf-mut23h2u-267"].get("htmlFr") or "") == 25238)
chk("registre 268 intact (20 715 car)", len(les["pdf-mut23h2u-268"].get("htmlFr") or "") == 20715)
chk("registre 269 = htmlFr posé (~25 778 car)", len(les["pdf-mut23h2u-269"].get("htmlFr") or "") >= 23_000)
chk("registre 271 non touché (htmlFr vide)", (les["pdf-mut23h2u-271"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-270"].get("htmlFr") or ""
if fr:
    chk("registre 270 = htmlFr posé (~20 000 car)", 18_000 <= len(fr) <= 24_000)
    chk("registre 270 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 270 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 270", les["pdf-mut23h2u-270"].get("titleAr") == "الدرس 16 : المعضل والمنقطع")
chk("titleFr pré-mappé 270 aligné au h1",
    (les["pdf-mut23h2u-270"].get("titleFr") or "")
    == "Leçon 16 : Le hadith à double rupture (muʿḍal) et à rupture simple (munqaṭiʿ)")
chk("titleAr pré-mappé 271 intact (leçon 17, non touchée)",
    les["pdf-mut23h2u-271"].get("titleAr") == "الدرس 17 : السقط الظاهر والخفي")

print(f"verify-ulumhadith2-pdf270 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
