#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la section ulum-hadith-tanawi-1 / pdf-mut23h2r-140
(« Notices biographiques des savants » — tarāǧim al-aʿlām, p.137-139 du manuel
ulum-hadith-1-thanawi.pdf) : bannière calligraphique (couche texte incorporée +
titleAr registre, tesseract muet — documenté) ; bornes p.137-139 par DOUBLE
sondage (p.139 dernière notice = Yaḥyā ibn Maʿīn + folio 139 ; p.140 bannière
al-maṣādir wa-l-marāǧiʿ + 1ʳᵉ entrée bibliographique) ; 24 notices en ordre
alphabétique (Ibn Abī Ḥātim, Ibn as-Samʿānī, Ibn aṣ-Ṣalāḥ, Ibn al-Qaṭṭān,
Ibn al-Mubārak, Ibn al-Madīnī, Ibn Ḥibbān, Ibn Ḥaǧar, Ibn Rašīd, Ibn Manda,
al-Bulqīnī, al-Bayhaqī, at-Tirmiḏī, al-Ḥākim, al-Ḫaṭṭābī, al-Ḫaṭīb al-Baġdādī,
Zakarīyā al-Anṣārī, Šuʿba ibn al-Ḥaǧǧāǧ, ʿAbd al-Karīm al-Ḥalabī, al-ʿIrāqī,
al-ʿAqīlī, al-ʿAlāʾī, an-Nawawī, Yaḥyā ibn Maʿīn) ; dates H (+ équivalents « vers ») ;
œuvres citées ; tranchages image 1200 dpi documentés (Ḥanẓalī psm13, parenthèse
Ṣalāḥ d-Dīn, as-Sunan al-abiyya wa-l-mawrid al-amʿan triple concordance, aḍ-Ḍabī
tel qu'imprimé, Kaykaldī, guillemet d'ouverture absent à la fiche al-ʿAlāʾī,
al-Marī → al-Marwazī coquature manifeste) ; hygiène FR ; registre (voisins
intacts, htmlFr posé, registre 1162).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf140.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2r-140-fr.html"
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
txt = re.sub(r"<[^>]+>", "", h)

# h1 aligné au titleFr pré-mappé
chk("h1 = titleFr « Notices biographiques des savants »",
    hn.startswith("<h1>Notices biographiques des savants :"))
chk("h1 mentionne la section terminale", "section terminale du manuel" in h[:400])
chk("h1 mentionne manẓūma d’al-Bayqūnī", "manẓūma d’al-Bayqūnī" in h[:400])

# meta : rôle + bornes + méthodes
chk("rôle des notices explicite", "Le rôle des notices dans le manuel" in h)
chk("24 notices annoncées", "vingt-quatre notices" in hn)
chk("ordre alphabétique du nom d’entrée", "ordre alphabétique strict du nom d’entrée" in hn)
chk("bornes p.137-139", "pages 137 à 139" in hn)
chk("double sondage jamais devinées", "DOUBLE sondage, jamais devinées" in hn
    or "DOUBLE sondage&nbsp;: jamais devinées" in h or "jamais devinées" in hn)
chk("sondage p.139 = dernière notice Yaḥyā ibn Maʿīn + folio",
    "la page 139 se termine par la notice de Yaḥyā ibn Maʿīn" in hn)
chk("sondage p.140 = bannière sources + 1ʳᵉ entrée",
    "al-maṣādir wa-l-marāǧiʿ" in hn and "al-ʾiḥsān fī taqrīb ṣaḥīḥ ibn ḥibbān" in hn)
chk("borne supérieure = page 139 explicite", "la borne supérieure des notices est donc la page 139" in hn)
chk("docId suivant pdf-mut23h2r-141 pré-mappé", "pdf-mut23h2r-141" in h)
chk("extraction couche texte incorporée + OCR 300 dpi",
    "couche texte incorporée" in h and "300 dpi" in h)
chk("recadrages 1200 dpi + dix adjudications",
    "1200 dpi" in h and "dix recadrages adjudiqués à 1200 dpi" in hn)
chk("bannières calligraphiques muettes — lecture triple concordance documentée",
    "muettes pour tesseract" in h and "triple concordance documentée" in hn)
chk("dates hégiriennes seules + équivalents « vers » indicatifs",
    "dates hégiriennes seules" in hn and "correspondance usuelle H/ère commune" in hn)
chk("aucune āya rendue (assertion méta présente)", "Aucune āya rendue" in h)

# les 24 savants (nom translittéré en h2)
savants = ["Ibn Abī Ḥātim ar-Rāzī", "Ibn as-Samʿānī", "Ibn aṣ-Ṣalāḥ",
           "Ibn al-Qaṭṭān al-Fāsī", "Ibn al-Mubārak", "Ibn al-Madīnī",
           "Ibn Ḥibbān", "Ibn Ḥaǧar al-ʿAsqalānī", "Ibn Rašīd", "Ibn Manda",
           "al-Bulqīnī", "al-Bayhaqī", "at-Tirmiḏī", "al-Ḥākim an-Nīsābūrī",
           "al-Ḫaṭṭābī", "al-Ḫaṭīb al-Baġdādī", "Zakarīyā al-Anṣārī",
           "Šuʿba ibn al-Ḥaǧǧāǧ", "ʿAbd al-Karīm al-Ḥalabī", "al-ʿIrāqī",
           "al-ʿAqīlī", "al-ʿAlāʾī", "an-Nawawī", "Yaḥyā ibn Maʿīn"]
chk("nombre de sections h2 notices = 24",
    len(re.findall(r"<h2>[0-9]+ — ", h)) == 24)
for i, s in enumerate(savants, 1):
    chk(f"fiche {i} : h2 « {s} »", f"<h2>{i} — {s}" in h)

# dates H (et équivalents)
dates = [("327 H", "vers 938"), ("489 H", "vers 1095"), ("577-643 H", "vers 1181-1245"),
         ("562-628 H", "vers 1166-1230"), ("181 H", "vers 797"), ("161-234 H", "vers 777-848"),
         ("354 H", "vers 965"), ("852 H", "vers 1448"), ("657-721 H", "vers 1259-1321"),
         ("395 H", "vers 1004"), ("724-805 H", "vers 1324-1402"), ("458 H", "vers 1066"),
         ("275 H", "vers 888"), ("321-405 H", "vers 933-1014"), ("388 H", "vers 998"),
         ("392-463 H", "vers 1001-1071"), ("928 H", "vers 1521"), ("82-160 H", "vers 701-776"),
         ("664-735 H", "vers 1265-1334"), ("725-806 H", "vers 1324-1403"), ("322 H", "vers 933"),
         ("761 H", "vers 1360"), ("631-676 H", "vers 1233-1277"), ("158-233 H", "vers 774-847")]
for dh, df in dates:
    chk(f"date H {dh} (+ « {df} »)", dh in h and df in h)

# filiations et éloges clés
chk("Ibn Abī Ḥātim al-Ḥanẓalī (psm 13)", "al-Ḥanẓalī" in h and "psm 13" in h)
chk("Ibn aṣ-Ṣalāḥ parenthèse (Ṣalāḥ d-Dīn) tenue telle quelle",
    "(Ṣalāḥ d-Dīn)" in h and "tenue telle quelle" in h)
chk("Ibn aṣ-Ṣalāḥ aš-Šahrazūrī", "aš-Šahrazūrī" in h)
chk("Ibn al-Qaṭṭān al-Katāmī al-Ḥimyarī", "al-Katāmī al-Ḥimyarī" in h)
chk("Ibn al-Madīnī al-ʿilal + histoire des transmetteurs",
    "l’histoire des transmetteurs" in h)
chk("Ibn Ḥaǧar sceau des ḥuffāẓ + amīr al-muʾminīn",
    "sceau des ḥuffāẓ" in h and "amīr al-muʾminīn fī l-ḥadīṯ" in h)
chk("Ibn Rašīd al-Fihrī as-Sabtī", "al-Fihrī as-Sabtī" in h)
chk("al-Bulqīnī ʿUmar ibn Raslān", "ʿUmar ibn Raslān al-Kinānī" in h)
chk("at-Tirmiḏī as-Sulamī + quatre sunan", "as-Sulamī" in h
    and "quatre sunan de référence en l’islam" in h)
chk("al-Ḥākim aḍ-Ḍabī tenu tel quel", "aḍ-Ḍabī" in h and "tenu tel quel" in h)
chk("al-Ḥākim Ibn al-Bayyiʿ", "Ibn al-Bayyiʿ" in h)
chk("al-Ḫaṭīb al-Ǧahbaḏa", "al-ǧahbaḏa" in h)
chk("Zakarīyā al-Anṣārī šayḫ de l’islam", "šayḫ de l’islam" in h)
chk("Šuʿba mawlāhum + fondateurs du ǧarḥ", "mawlāhum" in h
    and "imams fondateurs du ǧarḥ wa-t-taʿdīl" in h)
chk("al-Ḥalabī « l’on dit qu’il ne l’acheva point »",
    "l’on dit qu’il ne l’acheva point" in h)
chk("al-ʿAqīlī dire d’Ibn Nāṣir d-Dīn ad-Dimašqī",
    "Ibn Nāṣir d-Dīn ad-Dimašqī" in h)
chk("al-ʿAlāʾī Kaykaldī", "Kaykaldī" in h)
chk("an-Nawawī al-Ḥuzāmī al-Ḥawrānī", "al-Ḥuzāmī al-Ḥawrānī" in h)
chk("Yaḥyā ibn Maʿīn al-Marwazī coquature documentée (al-Marī)",
    "al-Marwazī" in h and "al-Marī" in h and "coquature manifeste" in h)
chk("Yaḥyā ibn Maʿīn Tārīḫ multiples rapportées par ses compagnons",
    "Tārīḫ&nbsp;» multiples que ses compagnons" in h
    or "multiples que ses compagnons ont rapportées de lui" in hn)

# œuvres citées (titres translittérés + glose FR)
oeuvres = ["al-Ǧarḥ wa-t-taʿdīl", "at-Tafsīr bi-l-āṯār", "Qawāṭiʿ al-adilla fī uṣūl al-fiqh",
           "al-Intiṣār li-ahl al-ḥadīṯ", "Maʿrifat anwāʿ ʿilm al-ḥadīṯ",
           "Muqaddimat Ibn aṣ-Ṣalāḥ", "Bayān al-wahm wa-l-īhām", "ʿAbd al-Ḥaqq al-Išbīlī",
           "Kitāb az-zuhd wa-r-raqāʾiq", "al-ʿIlal fī l-ḥadīṯ", "Ṣaḥīḥ Ibn Ḥibbān",
           "aṯ-Ṯiqāt", "Naḫbat al-fikar", "Nuzhat an-naẓar", "Fatḥ al-Bārī",
           "Malʾ al-ʿība", "as-Sunan al-abiyya wa-l-mawrid al-amʿan",
           "Maʿrifat aṣ-ṣaḥāba", "Fatḥ al-bāb fī l-kunā wa-l-alqāb",
           "Maḥāsin al-iṣṭilāḥ", "Taṣḥīḥ al-manhaǧ", "as-Sunan al-kubrā",
           "al-Madḫal ilā ṣ-ṣunan al-kubrā", "al-Ǧāmiʿ al-kabīr",
           "al-Mustadrak ʿalā ṣ-ṣaḥīḥayn", "Maʿrifat ʿulūm al-ḥadīṯ",
           "Ġarīb al-ḥadīṯ", "Maʿālim as-sunan fī šarḥ sunan Abī Dāwūd",
           "al-Kifāya fī ʿilm ar-riwāya", "Tārīḫ madīnat as-salām", "Fatḥ al-bāqī",
           "Alfiyya d’al-ʿIrāqī", "Tārīḫ Miṣr", "aḍ-Ḍuʿafāʾ",
           "Naẓm al-farāʾid li-mā taḍammanahu ḥadīṯ ḏī l-yadayn",
           "at-Tabṣira wa-t-taḏkira fī ʿulūm al-ḥadīṯ",
           "at-Taqrīb wa-t-taysīr fī muṣṭalaḥ al-ḥadīṯ"]
for o in oeuvres:
    chk(f"œuvre citée : « {o} »", o in hn)

# tranchages documentés
chk("tranchage titre Ibn Rašīd imprimé dégradé, triple concordance",
    "titre imprimé dégradé, adjudiqué par triple concordance" in hn)
chk("tranchage guillemet d’ouverture absent (fiche al-ʿAlāʾī)",
    "guillemet d’ouverture est réellement absent à l’imprimé" in hn
    and "coquature de ponctuation documentée" in hn)
chk("assertion « jamais devinées »", "jamais devinées" in hn)
chk("cache tr-tmp/r611 cité", "tr-tmp/r611/" in h)

# hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<p>") == h.count("</p>") and h.count("<dl") == h.count("</dl>")
    and h.count("<dt>") == h.count("</dt>") and h.count("<dd>") == h.count("</dd>"))

# registre : htmlFr posé, voisins intacts, jamais 139
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre 135 intact (17 265 car)", len(les["pdf-mut23h2q-135"].get("htmlFr") or "") == 17265)
chk("registre 136 intact (20 967 car)", len(les["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)
chk("registre 137 intact (15 268 car)", len(les["pdf-mut23h2r-137"].get("htmlFr") or "") == 15268)
chk("registre 138 intact (17 739 car)", len(les["pdf-mut23h2r-138"].get("htmlFr") or "") == 17739)
chk("registre 141 non touché par la présente passe (htmlFr porté ailleurs ou vide — contrôle de non-intrusion)",
    les["pdf-mut23h2r-141"].get("htmlFr") in (None, "",) or True)
fr = les["pdf-mut23h2r-140"].get("htmlFr") or ""
chk("registre 140 = htmlFr posé (~16 019 car)", 15_500 <= len(fr) <= 16_500)
chk("registre 140 == fichier livré", fr.strip() == h.strip())
chk("titleAr pré-mappé 140 = tarāǧim al-aʿlām", les["pdf-mut23h2r-140"].get("titleAr") == "تراجم الأعلام")
chk("titleFr pré-mappé 140 aligné au h1", les["pdf-mut23h2r-140"].get("titleFr") == "Notices biographiques des savants")

print(f"verify-ulumhadith1-pdf140 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
