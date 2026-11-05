#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2r-141
(al-maṣādir wa-l-marāǧiʿ — sources et références, p.140-143 du manuel
ulum-hadith-1-thanawi.pdf) : bannière « al-maṣādir wa-l-marāǧiʿ » ; bornes
p.140-143 par DOUBLE sondage (p.140 = bannière + 1re entrée al-Iḥsān ; p.143
fin = an-Nukat ; p.144 = fahris al-muḥtawāt non touché) ; 41 notices
bibliographiques en ordre alphabétique strict du titre d'œuvre (10+12+12+7) ;
matière extraite de la couche texte incorporée (pdftotext) recoupée INTÉGRALEMENT
par OCR tesseract arabe 300 dpi (t140-t143) — zéro recadrage image requis,
concordance 41/41 documentée ; recoupements tranchés sans image (ligne parasite
1407 = ad-Dārimī ; aṯ-ṯāniya dégradée ; nasab ibn Murī correct ; parenthèses du
titre al-ʿIrāqī tenues ; édition de Fès 1354 H ; année grégorienne 2009 seule de
la liste) ; dates H imprimées + CE « vers » indicatifs ; renvois aux notices du
manuel (3/7/8/12/14/15/16/17/20/21/23) ; zéro āya rendue, zéro résidu arabe,
zéro apostrophe droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf141.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2r-141-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

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
chk("h1 = titleFr « Sources et références »", hn.startswith("<h1>Sources et références :"))
chk("h1 mentionne manẓūma d’al-Bayqūnī", "manẓūma d’al-Bayqūnī" in h[:400])
chk("h1 mentionne bibliographie terminale du manuel", "bibliographie terminale du manuel" in h[:400])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("bannière al-maṣādir wa-l-marāǧiʿ citée", "al-maṣādir wa-l-marāǧiʿ" in h)
chk("titleAr pré-mappé cité en dd", "المصادر والمراجع" not in h and "les sources et références" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("bornes p.140-143 documentées", "pages 140 à 143" in h)
chk("p.144 index non touché", "fahris al-muḥtawāt" in h and "non touché" in h)
chk("répartition 10/12/12/7", "10 en la page 140, 12 en la page 141, 12 en la page 142, 7 en la page 143" in h)
chk("41 notices annoncées", "quarante et une notices bibliographiques" in h)
chk("R611 référencé", "R611" in h)
chk("cache couche incorporée cité", "tr-tmp/r612-incorporated-p140-144.txt" in h)
chk("cache OCR r611 cité", "tr-tmp/r611/t140.txt" in h)
chk("zéro recadrage requis documenté", "AUCUN recadrage image ne fut requis" in h)
chk("concordance 41/41", "concordent sur les quarante et une entrées" in h)
chk("nombres sans inversion (marqueurs bidirectionnels)", "en ordre logique" in h and "sans aucune inversion" in h)
chk("ligne parasite 1407 = ad-Dārimī documentée", "appartient en réalité à" in hn and "Sunan ad-Dārimī" in hn)
chk("aṯ-ṯāniya dégradée documentée", "dégradé en" in hn and "aṯ-ṯāʾiya" in hn)
chk("nasab ibn Murī correct documenté", "Murī est le grand-père canonique de l’imām" in h)
chk("parenthèses du titre al-ʿIrāqī tenues", "tenues telles quelles" in h)
chk("édition de Fès 1354 H documentée", "Fès" in h and "1354 H" in h)
chk("2009 grégorienne signalée", "la seule année grégorienne de toute la bibliographie" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("dates CE « vers » indicatives documentées", "à titre indicatif" in h)
chk("entrées sans date renvoyées au manuel/canon", "renvoient aux notices du manuel ou au canon" in h)
chk("livre complet 30/30 documenté", "COMPLET" in h and "trente entrées au registre" in h)

# ---- structure : 41 fiches numérotées + intro
n_h2 = h.count("<h2>")
chk("42 h2 (1 intro + 41 fiches)", n_h2 == 42)
chk("fiche 1 — al-Iḥsān", "1 — al-Iḥsān fī taqrīb Ṣaḥīḥ Ibn Ḥibbān" in h)
chk("fiche 41 — an-Nukat", "41 — an-Nukat ʿalā kitāb Ibn aṣ-Ṣalāḥ" in h)
numeros = [str(i) for i in range(1, 42)]
pos = 0
ordre_num = True
for n in numeros:
    m = re.search(r"<h2>%s — " % n, h[pos:])
    if not m:
        ordre_num = False
        break
    pos += m.start() + 4
chk("numérotation 1..41 croissante sans saut", ordre_num)

# ---- ordre alphabétique strict des 41 titres
titres = ["al-Iḥsān fī taqrīb Ṣaḥīḥ Ibn Ḥibbān", "al-Iršād fī maʿrifat ʿulamāʾ al-ḥadīṯ",
          "al-Iqtirāḥ fī bayān al-iṣṭilāḥ", "Tārīḫ Baġdād", "Tadrīb ar-rāwī fī šarḥ Taqrīb an-Nawawī",
          "at-Taqrīb wa-t-taysīr li-maʿrifat sunan al-Bašīr an-Naḏīr",
          "at-Tamhīd li-mā fī l-Muwaṭṭaʾ", "Tawḍīḥ al-afkār li-maʿānī tanqīḥ al-anẓār",
          "Taysīr muṣṭalaḥ al-ḥadīṯ", "aṯ-Ṯiqāt",
          "al-Ǧawāhir wa-d-durar bi-tarǧama šayḫ al-islām Ibn Ḥaǧar",
          "Sunan Ibn Māǧa al-Qazwīnī", "Sunan Abī Dāwūd", "Sunan al-Bayhaqī al-kubrā",
          "Sunan at-Tirmiḏī", "Sunan ad-Dāraquṭnī", "Sunan ad-Dārimī", "as-Sunan al-kubrā",
          "Sīr aʿlām an-nubalāʾ", "Šarḥ (at-tabṣira wa-t-taḏkira, alfiyyat al-ʿIrāqī)",
          "Šarḥ an-Nawawī ʿalā Ṣaḥīḥ Muslim", "Šarḥ Ṣaḥīḥ al-Buḫārī",
          "aṣ-Ṣiḥāḥ, tāǧ al-luġa wa-ṣiḥāḥ al-ʿarabiyya", "Ṣaḥīḥ al-Buḫārī", "Ṣaḥīḥ Muslim",
          "aḍ-Ḍuʿafāʾ al-kabīr", "Ṭabaqāt al-ḥuffāẓ", "al-ʿIlal aṣ-ṣaġīr",
          "Fatḥ al-bārī, šarḥ Ṣaḥīḥ al-Buḫārī", "Fatḥ al-bāqī bi-šarḥ alfiyyat al-ʿIrāqī",
          "Fatḥ al-muġīṯ bi-šarḥ alfiyyat al-ḥadīṯ li-l-ʿIrāqī", "Kašf aẓ-ẓunūn",
          "Maʿālim as-sunan", "Maʿrifat ʿulūm al-ḥadīṯ",
          "al-Maqāṣid al-ḥasana fī bayān kaṯīr min al-aḥādīṯ al-maštahara ʿalā l-alsina",
          "Muqaddimat Ibn aṣ-Ṣalāḥ", "al-Mawḍūʿāt", "Muwaṭṭaʾ al-imām Mālik",
          "al-Mūqiza fī ʿilm muṣṭalaḥ al-ḥadīṯ",
          "Nuzhat an-naẓar fī tawḍīḥ Naḫbat al-fikr fī muṣṭalaḥ ahl al-aṯar",
          "an-Nukat ʿalā kitāb Ibn aṣ-Ṣalāḥ"]
chk("41 titres listés dans le verify", len(titres) == 41)
pos = 0
ordre_alpha = True
titre_manquant = None
for t in titres:
    i = hn.find(t, pos)
    if i < 0:
        ordre_alpha = False
        titre_manquant = t
        break
    pos = i + len(t)
chk("41 titres en ordre alphabétique strict (séquence croissante)", ordre_alpha)
if titre_manquant:
    chk(f"titre manquant : {titre_manquant}", False)

# ---- entrées clés (auteur + dates H + éditeur + maison + ville + année)
entrees = [
    ("ibn Ḥibbān al-Bustī", "notice 7"), ("Ibn Balbān al-Fārisī", "739 H"), ("Muʾassasat ar-Risāla", "1408 H"),
    ("al-Khalīlī al-Qazwīnī", "446 H"), ("Maktabat ar-Rašd", "Riyad"), ("1409 H", "1409 H"),
    ("Ibn Daqīq al-ʿĪd", "702 H"), ("Qaḥṭān ad-Dūrī", "Amman"), ("1427 H", "1427 H"),
    ("al-Ḫaṭīb al-Baġdādī", "Baššār ʿAwwād Maʿrūf"), ("Dār al-Ġarb al-islāmī", "1422 H"),
    ("Ǧalāl ad-Dīn as-Suyūṭī", "911 H"), ("Dār Ṭayba", "Dār Ṭayba"),
    ("an-Nawawī", "676 H"), ("Dār al-Kitāb al-ʿarabī", "1405 H"),
    ("ʿAbd al-Barr an-Namarī", "Ministère des Habous"), ("1387 H", "1387 H"),
    ("aṣ-Ṣanʿānī", "1188 H"), ("ʿAwīḍa", "1417 H"),
    ("Maḥmūd aṭ-Ṭaḥḥān an-Naʿīmī", "dixième édition"), ("Maktabat al-Maʿārif", "1425 H"),
    ("Dār al-Fikr", "1395 H"),
    ("as-Saḫāwī", "902 H"), ("Ibrāhīm Bāǧis", "Dār Ibn Ḥazm"), ("1419 H", "1419 H"),
    ("Ibn Māǧa al-Qazwīnī", "273 H"), ("Muḥammad Fuʾād ʿAbd al-Bāqī", "ʿAbd al-Bāqī"),
    ("as-Siǧistānī", "275 H"), ("Qara Ballī", "1430 H"),
    ("al-Bayhaqī", "458 H"), ("ʿAbd al-Qādir ʿAṭā", "troisième édition"),
    ("at-Tirmiḏī", "279 H"), ("Aḥmad Muḥammad Šākir", "Ibrāhīm ʿAṭwa ʿAwaḍ"),
    ("Muṣṭafā l-Bābī l-Ḥalabī", "1395 H"),
    ("ad-Dāraquṭnī", "385 H"), ("1424 H", "1424 H"),
    ("ad-Dārimī", "255 H"), ("1407", "1407"),
    ("an-Nasāʾī", "303 H"), ("ʿAbd al-Munʿim Šalabī", "1422 H"),
    ("aḏ-Ḏahabī", "748 H"), ("Ḥusayn al-Asad", "huitième édition"),
    ("ʿAbd ar-Raḥīm al-ʿIrāqī", "806 H"), ("Muḥammad ibn Rašīd al-ʿIrāqī", "Fès"),
    ("ibn Murī an-Nawawī", "1392 H"),
    ("Ibn Baṭṭal", "443 H"), ("Yāsir ibn Ibrāhīm", "1423 H"),
    ("al-Ǧawharī al-Fārābī", "393 H"), ("ʿAbd al-Ġafūr ʿAṭṭār", "Dār al-ʿilm li-l-malāyīn"),
    ("al-Buḫārī", "256 H"), ("Zuhayr ibn Nāṣir an-Nāṣir", "Ṭawq an-naǧāh"),
    ("Muslim ibn al-Ḥaǧǧāǧ an-Nīsābūrī", "261 H"),
    ("al-ʿAqīlī al-Makkī", "322 H"), ("Qalʿaǧī", "1404 H"),
    ("ʿAlī Muḥammad ʿUmar", "Maktabat aṯ-ṯaqāfa ad-dīniyya"), ("1417 H", "1417 H"),
    ("ibn Sawra at-Tirmiḏī", "al-ʿIlal aṣ-ṣaġīr"),
    ("Ḥaǧar al-ʿAsqalānī", "852 H"), ("Dār al-maʿrifa", "1379 H"),
    ("Zakariyyā ibn Muḥammad ibn Zakariyyā al-Anṣārī", "926 H"), ("ʿAbd al-Laṭīf Hammīm", "1422 H"),
    ("ʿAlī Ḥusayn ʿAlī", "Maktabat as-sunna"),
    ("al-Qusṭanṭīnī ar-Rūmī al-Ḥanafī", "1067 H"), ("1413 H", "1413 H"),
    ("al-Ḫaṭṭābī", "388 H"), ("Alep", "1351 H"),
    ("al-Ḥākim", "Muʿaẓẓam Ḥusayn"), ("1397 H", "1397 H"),
    ("al-Ḫašt", "1405 H"),
    ("ʿUthmān ibn ʿAbd ar-Raḥmān", "Nūr ad-Dīn ʿIṭr"), ("Dār al-Fikr al-muʿāṣir", "1406 H"),
    ("Ibn al-Ǧawzī", "al-Mawḍūʿāt"), ("1386 H", "1386 H"),
    ("Mālik ibn Anas al-Aṣbaḥī", "Muwaṭṭaʾ"),
    ("ʿAbd al-Fattāḥ Abū Ġudda", "Maktabat al-maṭbūʿāt al-islāmiyya"), ("1412 H", "1412 H"),
    ("Maṭbaʿat aṣ-Ṣabāḥ", "Damas"), ("troisième édition, 1421 H", "1421 H"),
]
for a, b in entrees:
    chk(f"entrée : {a}", a in hn)
    chk(f"entrée : {b}", b in hn)

# ---- renvois internes aux notices du manuel + canon documenté
for ref in ["notice 7", "notice 16", "notice 23", "notice 12", "notice 20",
            "notice 21", "notice 8", "notice 17", "notice 3", "notice 14",
            "597 H", "179 H", "928 pour le même savant"]:
    chk(f"renvoi/canon : {ref}", ref in h)

# ---- conversions CE « vers » (spot checks)
for ce in ["vers 965", "vers 1338", "vers 1054", "vers 1302", "vers 1071", "vers 1505",
           "vers 1277", "vers 1774", "vers 1496", "vers 886", "vers 888", "vers 1066",
           "vers 892", "vers 995", "vers 869", "vers 915", "vers 1347", "vers 1403",
           "vers 1051", "vers 1003", "vers 870", "vers 875", "vers 933", "vers 1520",
           "vers 1656", "vers 998", "vers 1201", "vers 796"]:
    chk(f"CE : {ce}", ce in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<p>") == h.count("</p>") and h.count("<dl") == h.count("</dl>")
    and h.count("<dt>") == h.count("</dt>") and h.count("<dd>") == h.count("</dd>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre 136 intact (20 967 car)", len(les["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)
chk("registre 137 intact (15 268 car)", len(les["pdf-mut23h2r-137"].get("htmlFr") or "") == 15268)
chk("registre 138 intact (17 739 car)", len(les["pdf-mut23h2r-138"].get("htmlFr") or "") == 17739)
chk("registre 139 intact (20 803 car)", len(les["pdf-mut23h2r-139"].get("htmlFr") or "") == 20803)
chk("registre 140 intact (16 018 car)", len(les["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("total lessons = 30", len(reg["lessons"]) == 30)
fr = les["pdf-mut23h2r-141"].get("htmlFr") or ""
chk("registre 141 = htmlFr posé (~24 320 car)", 23_000 <= len(fr) <= 25_500)
chk("registre 141 == fichier livré", fr.strip() == h.strip())
chk("titleAr pré-mappé 141 = al-maṣādir wa-l-marāǧiʿ", les["pdf-mut23h2r-141"].get("titleAr") == "المصادر والمراجع")
chk("titleFr pré-mappé 141 aligné au h1", les["pdf-mut23h2r-141"].get("titleFr") == "Sources et références")

print(f"verify-ulumhadith1-pdf141 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
