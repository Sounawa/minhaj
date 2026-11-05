#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2r-136
(les transmetteurs homonymes muʾtalif/muḫtalif, p.121-124 du manuel
ulum-hadith-1-thanawi.pdf) : bannière « ad-dars 25 » ; bornes p.121-124 par
DOUBLE sondage (iʿdād qablī p.124 ×2 q. munkar + bannière ad-dars 26 et
objectifs p.125 lus à l'OCR) ; bayt « muʾtalifun muttafiqu l-khaṭṭi faqaṭun *
* * wa-ḍidduhu muḫtalifun fa-ḥḏari l-ġalaṭ » tranché image 4800 dpi (ġayn à
point unique + ḍamma, concordant canon + citation p.122) ; glose (ittilāf,
ḍād = opposé/semblable) ; istiḫlāṣ al-mafāhīm ×2 ; taḥlīl : définition (accord
en l'écriture seule, divergence prononciation/personnes, domaine noms/titres/
généalogies/kunyas, condition de deux transmetteurs, exclusion du raoui
unique), différence d'avec le muttafiq-muftariq (muštarak lafẓī), « fann
important » dafʿ maʿarrat at-taḥrīf + citation Bayqūnī « fa-ḥḏari l-ġalaṭ »
(graphie fautrice documentée) ; aqsām ×2 (I : sans règle, naql/ḥifẓ, Asīd
muṣaġġar/mukabbar, trio Ḥabān/Ḥayyān/Ǧayyān concordant R601 ; II : règle par
la rareté (qilla), deux formes — taʿmīm tranché 1800 dpi, exemple Sulaym ×8
porteurs (Ibn Salām Israélite, sœur d'Ibn Salām, aïeul al-Ǧubbāʾī, aïeul
an-Nasafī, aïeul as-Sayyidī, père al-Baykandī, Sulaym ibn Abī l-Ḥaqīq, Sulaym
ibn Miškam — taḫfīf Ibn Ḥaǧar + « poésie » découverte image), fin d'OCR
récupérée ; forme 2 : maḫṣūṣ bi-ṣ-ṣaḥīḥayn wa-l-Muwaṭṭaʾ DÉCOUVERTE IMAGE,
istiqrāʾ, exemple Ḫāzim iǧmāʿ — Muḥammad ibn Ḫāzim aḍ-Ḍarīr vs Ḥāzim ihmāl
(al-Aʿraǧ, Ǧarīr ibn Ḥāzim)) ; taqwīm ×3 (« quatre divisions » tel qu'imprimé) ;
istiṯmār Ibn Ḥaǧar « fann ǧalīl yaqiʿu ǧahluhu bi-ahli l-ʿilmi » (Ikmāl Ibn
Mākūlā, Funak restitué canon, [Tadrīb ar-Rāwī : 2/790] tel qu'imprimé) ;
iʿdād qablī ×2 munkar (coquature « 1- 1- » documentée) ; bornes p.121-124 ;
zéro āya rendue, zéro résidu arabe, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf136.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2r-136-fr.html"
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
# copie normalisée (l'auto-fix QA insère U+202F à côté des &nbsp;) pour les contrôles textuels
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "").replace("\u2009", ""))
txt = re.sub(r"<[^>]+>", "", h)

# h1 aligné au titleFr pré-mappé
chk("h1 = titleFr « Les transmetteurs homonymes (mutalif / muḫtalif) »",
    hn.startswith("<h1>Les transmetteurs homonymes (mutalif / muḫtalif) :"))
chk("h1 mentionne le leçon 25", "leçon 25" in h[:400])
chk("h1 mentionne manẓūma d’al-Bayqūnī", "manẓūma d’al-Bayqūnī" in h[:400])

# bayt et glose
chk("bayt hémistiche 1", "muʾtalifun muttafiqu l-khaṭṭi faqaṭun" in h)
chk("bayt hémistiche 2 « wa-ḍidduhu muḫtalifun fa-ḥḏari l-ġalaṭ »",
    "wa-ḍidduhu muḫtalifun fa-ḥḏari l-ġalaṭ" in h)
chk("adjudication 4800 dpi du dernier mot", "4800&nbsp;dpi" in h)
chk("glose ism fāʿil", "nom d’agent (ism fāʿil) tiré de l’ittilāf" in h)
chk("glose ḍād opposé/semblable", "ce qui est visé ici est ce qui lui ressemble" in h)

# istiḫlāṣ al-mafāhīm ×2
chk("istiḫlāṣ 2 questions", "Qu’est-ce que le muʾtalif et le muḫtalif" in h
    and "Quelles sont ses divisions" in h)

# taḥlīl : définition
chk("défin. accord en l’écriture seule", "en l’écriture seule, du nom de deux transmetteurs" in h)
chk("défin. divergence prononciation/personnes",
    "diffèrent en la prononciation et en la personne" in h)
chk("défin. domaine noms/titres/généalogies/kunyas",
    "leurs généalogies et leurs kunyas" in h)
chk("défin. condition deux transmetteurs", "entre deux transmetteurs ou davantage" in h)
chk("exclusion transmetteur unique", "transmetteur unique, cela n’y entre point" in h)
chk("différence avec le muttafiq-muftariq", "homonyme verbal (al-muštarak al-lafẓī)" in h)
chk("maʿarra documentée", "maʿarra" in h and "lu à 2400&nbsp;dpi" in h)
chk("citation Bayqūnī fa-ḥḏari l-ġalaṭ + graphie fautrice documentée",
    "fa-ḥḏari l-ġalaṭ" in h and "graphie fautrice" in h)
chk("taḥrīf ihlāl/takšīd", "avec le redoublement ce dont la lecture juste est la légèreté" in h)

# aqsām
chk("division I sans règle naql/ḥifẓ", "par la transmission (an-naql) et la mémorisation (al-ḥifẓ)" in h)
chk("Asīd muṣaġġar/mukabbar", "(muṣaġġar)" in h and "(mukabbar)" in h)
chk("trio Ḥabān/Ḥayyān/Ǧayyān + concordance R601",
    "« Ḥabān »" in hn and "« Ǧayyān »" in hn and "R601, p.118" in hn)
chk("division II règle par la rareté qilla + note OCR",
    "la rareté (qilla)" in h and "li-qillatihi" in h)
chk("forme 1 taʿmīm tranché 1800 dpi", "at-taʿmīm" in h and "1800&nbsp;dpi" in h)
chk("exemple Sulaym — Ibn Salām Israélite", "ʿAbdallāh ibn Salām l’Israélite, le Compagnon" in h)
chk("exemple Sulaym — al-Ǧubbāʾī", "Abū ʿAlī al-Ǧubbāʾī" in h)
chk("exemple Sulaym — an-Nasafī", "Abū Naṣr Muḥammad ibn Yaʿqūb ibn Isḥāq" in h)
chk("exemple Sulaym — as-Sayyidī", "Saʿd ibn Ǧaʿfar ibn Sulaym" in h)
chk("exemple Sulaym — al-Baykandī", "le père d’al-Baykandī" in h)
chk("exemple Sullym — Ibn Abī l-Ḥaqīq", "Sulaym ibn Abī l-Ḥaqīq" in h)
chk("exemple Sulaym — Ibn Miškam + taḫfīf Ibn Ḥaǧar",
    "Sulaym ibn Miškam" in h and "at-taḫfīf" in h)
chk("fin « poésie » découverte image", "parvenu dans la poésie" in h
    and "DÉCOUVERTE PAR L’IMAGE" in h)
chk("qualificatif Sulaym non restituable (honnêteté d’apparat)",
    "non restituable avec certitude" in h)
chk("forme 2 maḫṣūṣ aṣ-ṣaḥīḥayn wa-l-Muwaṭṭaʾ découverte image",
    "aux deux Ṣaḥīḥ et au Muwaṭṭaʾ" in h and "DÉCOUVERT PAR L’IMAGE" in h)
chk("istiqrāʾ", "induction (istiqrāʾ)" in h)
chk("exemple Ḫāzim/Ḥāzim (aḍ-Ḍarīr, al-Aʿraǧ, Ǧarīr)",
    "Muḥammad ibn Ḫāzim Abū Muʿāwiya aḍ-Ḍarīr" in h
    and "Abū Ḥāzim al-Aʿraǧ" in h and "Ǧarīr ibn Ḥāzim" in h)

# taqwīm ×3
chk("taqwīm 3 questions", "Je définis le muʾtalif et le muḫtalif" in h
    and "quatre divisions du muʾtalif et du muḫtalif" in h)
chk("« quatre divisions » tel qu’imprimé noté", "tel qu’imprimé" in h)

# istiṯmār
chk("istiṯmār fann ǧalīl", "fannun ǧalīlun yaqiʿu ǧahluhu bi-ahli l-ʿilmi" in h)
chk("istiṯmār lā siyyamā ahli l-ḥadīṯ", "lā siyyamā ahli l-ḥadīṯi" in h)
chk("istiṯmār man lam yaʿrifhu", "wa-man lam yaʿrifhu bi-kaṯratin ḫaṭaʾuhu" in h)
chk("istiṯmār al-Ikmāl Ibn Mākūlā", "al-Ikmāl d’Ibn Mākūlā" in h
    and "l-Ikmālu li-bni Mākūlā" in h)
chk("al-Funak restitué canon documenté", "al-Funak" in h
    and "restitué al-Funak d’après la source canonique" in h)
chk("référence [Tadrīb ar-Rāwī : 2/790] telle qu’imprimée",
    "Tadrīb ar-Rāwī : 2/790" in hn)

# iʿdād qablī
chk("iʿdād munkar ×2", "al-ḥadīṯ al-munkar" in h and "est-il permis d’agir par le ḥadīṯ munkar" in h)
chk("coquature numérotation 1-1 documentée", "coquature de numérotation rendue telle quelle" in h)

# bornes double sondage
chk("bornes p.121-124", "s’ouvre en la page imprimée 121 et s’achève en la page 124" in h)
chk("sondage p.125 bannière ad-dars 26 + objectifs",
    "ad-dars 26" in h and "p125-300.txt" in h)
chk("double sondage jamais devinée", "jamais devinée" in h)

# hygiene FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("aucune āya rendue (assertion méta présente)", "aucune āya rendue" in h)
chk("balises appariées", h.count("<ol>") == h.count("</ol>")
    and h.count("<li>") == h.count("</li>") and h.count("<h2>") == h.count("</h2>"))

# registre : htmlFr posé, slot unique, voisin 135 intact
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre 135 intact (17 265 car)", len(les["pdf-mut23h2q-135"].get("htmlFr") or "") == 17265)
chk("registre 137 toujours vide (pas de doublon parallèle)",
    not (les["pdf-mut23h2r-137"].get("htmlFr") or "").strip())
fr = les["pdf-mut23h2r-136"].get("htmlFr") or ""
chk("registre 136 = htmlFr posé (~20 968 car)", 20_000 <= len(fr) <= 21_500)
chk("registre 136 == fichier livré", fr.strip() == h.strip() or len(fr) == len(h.rstrip("\n")))

print(f"verify-ulumhadith1-pdf136 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
