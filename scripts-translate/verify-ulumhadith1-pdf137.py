#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2r-137
(le ḥadīṯ méconnu munkar, p.125-128) — LIVRAISON CONSOLIDÉE DOUBLE-PASS :
corpus rédigé par la passe parallèle de l'ouvrier D (bayt « wa-l-munkaru
l-fardu bi-rāwin ʿadā * * * taʿdīluhu lā yaḥmilu t-tafarrudā » tranché bande
fine 2400 dpi — CONFIRMÉ indépendamment par la passe R607 en bande pleine
ligne 2400 dpi, concordance des occurrences pp.125-126), corrections de
consolidation R607 : coquille « conforming » → « conforme » ; bilan final
rétabli sur la lecture image 2400 dpi « wa-qad ġafala min siwā baynahumā »
(lecture « wa-man sawwā baynahumā fa-qad ġafala » récusée) ; contre-vérification
documentée au meta. Contrôles : structure complète (objectifs, tamhīd, matn,
glose, extraction, analyse 2 définitions + 2 exemples canoniques, farq,
taqwīm ×3, istiṯmār Muslim Muqaddima 1/7, iʿdād ×2 matrūk), noms propres
(Ḫubayb b. Ḥabīb, al-Ġayzār b. Ḥurayth rasm discuté, as-Sabīʿī restitué,
Abū Zakīr, Hišām b. ʿUrwa, ʿĀʾiša, Maʿmar, ʿAmmār b. Ruzayq, al-Ḥarabī,
Ḥamza az-Zayyāt, Abū Zurʿa, al-ʿAqīlī, Ibn aṣ-Ṣalāḥ, Ibn Ḥaǧar, aḏ-Dhahabī),
bornes p.125-128 par double sondage (p.129 ad-dars 27 matrūk), hygiène FR.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf137.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2r-137-fr.html"
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
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "")
            .replace("\u2009", "").replace("\u2019", "'"))
hq = h.replace("\u2019", "'").replace("\u202f", "").replace("\u2009", "")
hq2 = hq.replace("&nbsp;", " ")

# h1 aligné au titleFr pré-mappé
chk("h1 = titleFr « Le hadith méconnu (munkar) »",
    hn.startswith("<h1>Le hadith méconnu (munkar) : le livre des sciences"))
chk("h1 mentionne la leçon 26", "leçon 26" in h[:400])
chk("h1 mentionne manẓūma d'al-Bayqūnī", "manẓūma d'al-Bayqūnī" in hq[:400])

# bayt (matn + reprise) et adjudications
chk("bayt hémistiche 1", "wa-l-munkaru l-fardu bi-rāwin ʿadā" in h)
chk("bayt hémistiche 2", "taʿdīluhu lā yaḥmilu t-tafarrudā" in h)
chk("bayt rendu DEUX fois (matn + reprise)", h.count("wa-l-munkaru l-fardu bi-rāwin") >= 2)
chk("bande fine 2400 dpi (adjudication passe D)", "bande fine 2400&nbsp;dpi" in h)
chk("contre-vérification R607 pleine ligne (meta)", "contre-vérifiée PAR L’IMAGE en bande pleine ligne" in h)
chk("adjudication ʿadā (ʿayn creux ouvert, dāl)", "ʿayn au creux ouvert" in h)
chk("coquille « conforming » corrigée", "conforming" not in h and "conforme à la première" in h)

# glose
chk("glose munkar/maʿrūf", "le contraire du reconnu (maʿrūf)" in h)
chk("glose inkār/iqrār", "le contraire de l’aveu (iqrār)" in h)
chk("glose taʿdīl = degré en droiture", "le degré du rapporteur au regard de la droiture" in h)

# extraction des thèmes
chk("extraction 2 questions liminaires", "deux questions liminaires" in h
    and "Qu’est-ce que le ḥadīṯ méconnu" in h)
chk("vue d’ensemble imprimée", "Cette leçon comprend ce qui suit" in h)

# définition I + exemple hadith balah/tamr
chk("déf. I unicité du faible non supportée",
    "rapporteur faible dont l’unicité n’est pas supportée" in h)
chk("déf. I fāsiq/fāḥiš al-ġalaṭ", "pervers (fāsiq)" in h and "fāḥiš al-ġalaṭ" in h)
chk("chaîne hadith 1 (Abū Zakīr ← Hišām ← père ← ʿĀʾiša)",
    "Abū Zakīr Yaḥyā b. Muḥammad b. Qays" in h
    and "Hišām b. ʿUrwa" in h and "de ʿĀʾiša" in h)
chk("hadith 1 translit kulū l-balaḥa", "kulū l-balaḥa bi-t-tamri" in h
    and "ġaḍiba š-šayṭānu" in h)
chk("hadith 1 FR dattier frais/datte sèche", "dattier frais (balah)" in h
    and "datte sèche (tamr)" in h)
chk("source hadith 1 telle qu’imprimée", "kitāb al-walīma" in h
    and "al-balaḥ bi-t-tamr" in h and "tenue telle qu’imprimée" in h)
chk("jugement an-Nasāʾī + Ibn aṣ-Ṣalāḥ + aḏ-Dhahabī",
    "an-Nasāʾī, Ibn aṣ-Ṣalāḥ, aḏ-Dhahabī" in h)
chk("al-ʿAqīlī unicité non suivie", "comme l’a dit al-ʿAqīlī" in h)
chk("Muslim mutābaʿāt + rang non atteint", "mutābaʿāt" in h
    and "n’a pas atteint le rang de celui dont on admet l’unicité" in h)
chk("restitution image tafarrudahu lettre à lettre", "tafarrudahu" in h
    and "tranché lettre à lettre" in h)
chk("sens rakīk + Satan/vie soumise", "rakīk" in h and "Satan ne se courrouce" in h)

# définition II + exemple hadith entrée au Paradis
chk("déf. II faible contredisant plus digne de foi",
    "le faible en contradiction avec celui qui est plus digne de foi que lui" in h)
chk("source Ibn Abī Ḥātim al-ʿIlal", "Ibn Abī Ḥātim dans al-ʿIlal" in h)
chk("chaîne hadith 2 (Ḫubayb b. Ḥabīb ← Abū Isḥāq ← al-Ġayzār ← Ibn ʿAbbās)",
    "Ḫubayb b. Ḥabīb" in h and "al-muqriʾ" in h and "al-Ġayzār b. Ḥurayth" in h
    and "Ibn ʿAbbās" in h)
chk("rasm al-Ġayzār discuté (ġayn vs ʿayn)", "ġayn-yāʾ-zāy" in h
    and "ʿayn-yāʾ-zāy" in h and "la lecture ġayn est retenue" in h)
chk("as-Sabīʿī restitué d’après at-Tibiʿī dégradé", "as-Sabīʿī" in h
    and "at-Tibiʿī" in h and "risque documenté" in h)
chk("hadith 2 translit man aqāma", "man aqāma ṣ-ṣalāta wa ātā z-zakāta" in h
    and "daḫala l-ǧannata" in h)
chk("qarā ḍ-ḍayfa (hôte)", "wa qarā ḍ-ḍayfa" in h and "honore l’hôte" in h)
chk("Abū Zurʿa mawqūf", "Abū Zurʿa" in h and "mawqūf" in h)
chk("wāhī al-ḥadīṯ + Ḥamza az-Zayyāt",
    "wāhī al-ḥadīṯ" in h and "Ḥamza az-Zayyāt" in h)
chk("contradiction des ṯiqāt (Maʿmar Ǧāmiʿ + ʿAmmār b. Ruzayq + al-Ḥarabī)",
    "Maʿmar dans son Ǧāmiʿ" in h and "ʿAmmār b. Ruzayq" in h
    and "ǧuzʾ ikrām aḍ-ḍayf" in h and "al-Ḥarabī" in h)
chk("clôture « Et c’est là la correcte »", "Et c’est là la correcte" in h)

# farq munkar/šāḏḏ
chk("Ibn aṣ-Ṣalāḥ synonymes (mutarādifān)", "mutarādifān" in h
    and "de même sens que lui" in h)
chk("Ibn Ḥaǧar divergence (mutaġāyirān)", "mutaġāyirān" in h
    and "Ibn Ḥaǧar" in h)
chk("šāḏḏ = ṯiqa/qalīl al-ḍabṭ", "plus digne de foi que lui" in h
    and "qalīl al-ḍabṭ" in h)
chk("munkar = mastūr", "mastūr" in h)
chk("maḥfūẓ/maʿrūf", "contraire le préservé (maḥfūẓ)" in h
    and "contraire le reconnu (maʿrūf)" in h)
chk("ʿumūm wa ḫuṣūṣ min waǧh", "ʿumūm wa ḫuṣūṣ min waǧh" in h)
chk("ṣadūq", "véridique (ṣadūq)" in h)
chk("bilan final TRANCHÉ R607 : wa-qad ġafala min siwā baynahumā",
    "wa-qad ġafala min siwā baynahumā" in h)
chk("adjudication 2400 dpi ligne complète (ġayn/fāʾ nets)",
    "2400&nbsp;dpi en ligne complète" in h and "la ġayn et le fāʾ y sont nets" in h)
chk("lecture sawwā récusée", "wa-man sawwā baynahumā fa-qad ġafala" in h
    and "récusée" in h)
chk("demeuré inaperçu (rendu par le sens)", "demeuré inaperçu" in h)

# taqwīm ×3
chk("taqwīm 3 questions", "Quelle est la définition du ḥadīṯ méconnu" in h
    and "Je donne un exemple du ḥadīṯ méconnu" in h)

# istiṯmār Muslim
chk("istiṯmār Muslim Muqaddima 1/7", "Muqaddima" in h and "1/7" in h)
chk("ʿAbd al-Bāqī tel qu’imprimé", "Muḥammad Fuʾād ʿAbd al-Bāqī" in h)
chk("mahǧūra l-ḥadīṯ", "mahǧūra l-ḥadīṯ" in h)
chk("ahl al-ḥifẓ wa-r-riḍā", "ahl al-ḥifẓ wa-r-riḍā" in h)
chk("translittération du squelette attesté", "Translittération du squelette attesté" in h)
chk("2 questions exploitation", "la cause du rejet du ḥadīṯ méconnu" in h
    and "rapporteur “méconnu” du ḥadīṯ" in h)

# iʿdād
chk("iʿdād matrūk ×2", "définition du ḥadīṯ délaissé (matrūk)" in h
    and "causes du délaissement du ḥadīṯ d’un rapporteur" in h)

# bornes double sondage
chk("bornes p.125-128", "s'ouvre en la page imprimée 125 et s'achève en la page 128" in hn)
chk("sondage p.129 (leçon suivante matrūk)", "page 129" in h
    and "sondage dédié p. 129" in h)
chk("objectifs de 27 (mawḍūʿ cité)", "fabriqué (mawḍūʿ)" in h)
chk("double sondage jamais devinée", "jamais devinée" in h)
chk("interdiction de double rendu", "interdite de double rendu" in h)

# hygiene FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("aucune āya rendue (assertion méta présente)", "Aucune āya" in h)
chk("balises appariées", h.count("<ol>") == h.count("</ol>")
    and h.count("<li>") == h.count("</li>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>"))

# registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre 136 intact (20 967 car)", len(les["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)
chk("registre 138 toujours vide (pas de doublon parallèle)",
    not (les["pdf-mut23h2r-138"].get("htmlFr") or "").strip())
chk("registre 137 htmlFr posé (livraison double-pass)",
    len(les["pdf-mut23h2r-137"].get("htmlFr") or "") > 12_000)
chk("titleFr pré-mappé 137 confirmé", les["pdf-mut23h2r-137"].get("titleFr") == "Le hadith méconnu (munkar)")

print(f"verify-ulumhadith1-pdf137 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)
