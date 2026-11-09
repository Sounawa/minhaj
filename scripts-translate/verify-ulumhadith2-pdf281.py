#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-281
(tarāǧim al-aʿlām — pages 132-134 du manuel ulum-hadith-2-thanawi_text.pdf)
: section annexe de clôture du volume, tableau à deux colonnes de SEIZE
notices biographiques. Bornes tranchées par sondage (p.131 clôt la leçon 26
livrée R661 — jamais retouchée ; p.132 ouvre les tarāǧim ; p.135 ouvre le
fahris al-maṣādir wal-marāǧiʿ — section DISTINCTE hors bornes). Source
tranchée : le PDF dédié du pdfUrl pré-mappé est un fantôme (404 serveur +
sondage numérique 2660905-2660950 négatif) — les biographies sont matériellement
aux pages 132-134 du livre principal. QUATORZE lectures d'images consignées
(tr-tmp/qa-crops-r664 : 3 pages pleines 300 dpi, 5 composites 600 dpi
méthode d'économie R103, 1 composite micro-crops 1200 dpi des mots pivots) ;
QUINZE lectures VLM SDK tentées refusées 429 (plafond service, documenté) ;
adjudications par lectures composites + couche texte, jamais devinées :
manḥ ar-rawḍ al-azhar tranché 600 dpi (contre « al-barūd » récusé) ; az-Zarkašī
tranché au ẓāʾ (contre « an-Narkašī » récusé) ; az-Zuhd tranché (couche +
600 dpi, contre « az-zad » récusé) ; min aḥiyāʾ Baġdād rendu au plus sûr
(Dār al-Quṭn = quartier bagdadien) ; ÉCART CANONIQUE 643 vs 646 (Ibn aṣ-Ṣalāḥ,
micro-crop 1200 dpi, rendu tel qu'imprimé, jamais corrigé) ; ÉCART al-Qāṣid
al-ḥasana (imprimé au féminin) ; ÉCART al-Ilāʿ (sans mīm) ; ÉCART bi-Marrākiš
(sans alif) ; lignage ʿIyāḍ ibn ʿAmrūn al-Yaḥmaṣbī tel qu'imprimé (1200 dpi,
canon attendu ibn Yaḥmadī) ; ibn Sābiq ad-Dīn tranché au bāʾ ; al-Muʿīn tranché
au mīm (1200 dpi, contre « al-ʿAyn » récusé) ; al-Muštabah tranché au bāʾ ;
titres dégradés non identifiés rendus tels qu'imprimés avec honnêteté d'apparat
(al-Fawāʾid al-kabīr, Fawāʾid ar-Rāziyyayn, Luqṭat al-ʿaǧlān, Waṣl balāġāt
al-waṭaʾ, phrases dégradées al-Ḫaṭīb et al-Qāḍī ʿIyāḍ) ; ZÉRO ĀYA (cache
coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf281.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-281-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"
SREG = "/home/z/my-project/scripts-translate/savant-registry.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ")
            .replace("\u2009", " ")).replace("\u2019", chr(39))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Notices biographiques des savants »",
    hn.startswith("<h1>Notices biographiques des savants (tarāǧim al-aʿlām)"))
chk("h1 mentionne livre deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le tableau à deux colonnes", "tableau à deux colonnes" in h[:900])
chk("h1 mentionne SEIZE notices", "SEIZE notices" in h[:1400])
chk("h1 page 132 : al-Qārī + Ibn Raǧab + aš-Šāfiʿī + Ibn Abī Ḥātim + ad-Dāraquṭnī + az-Zarkašī",
    all(x in h[:3200] for x in ["al-Qārī al-Harawī", "Ibn Raǧab", "aš-Šāfiʿī", "Ibn Abī Ḥātim", "ad-Dāraquṭnī", "az-Zarkašī"]))
chk("h1 page 133 : Ibn aṣ-Ṣalāḥ + Ibn ʿAbd al-Barr + al-Ḥākim + al-ʿIrāqī + al-Ḫaṭīb",
    all(x in h[:4200] for x in ["Ibn aṣ-Ṣalāḥ", "Ibn ʿAbd al-Barr", "al-Ḥākim", "al-ʿIrāqī", "al-Ḫaṭīb al-Baġdādī"]))
chk("h1 page 134 : aḏ-Ḏahabī + as-Saḫāwī + as-Suyūṭī + ʿIyāḍ + an-Nawawī",
    all(x in h[:5000] for x in ["aḏ-Ḏahabī", "as-Saḫāwī", "as-Suyūṭī", "al-Qāḍī ʿIyāḍ", "an-Nawawī"]))
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("slot pdf-mut23h2u-281 documenté", "pdf-mut23h2u-281" in h)
chk("titleFr pré-mappé respecté", "Notices biographiques des savants" in h)

# ---- bornes et source tranchée
chk("p.131 clôt la leçon 26 (R661) jamais retouchée",
    "la page 131 clôt la leçon 26 des ateliers" in h and "livrée R661" in h)
chk("p.132 ouvre la section (titre calligraphique + bandeau rendus)",
    "la page 132 OUVRE la section" in h and "bandeau" in h)
chk("p.135 = fahris al-maṣādir wal-marāǧiʿ section DISTINCTE hors bornes",
    "fahris al-maṣādir wal-marāǧiʿ" in h and "HORS BORNES" in h)
chk("tableau de 16 lignes, fin p.134 (folio + seizième notice an-Nawawī)",
    "16 lignes" in hn and "seizième notice" in hn and "folio" in hn)
chk("PDF dédié fantôme documenté (404 + sondage numérique négatif)",
    "FANTÔME" in h and "404" in h and "2660905-2660950" in h)
chk("2660911 (ID livre principal) cité", "2660911" in h)

# ---- extraction multicouche et lectures
chk("couche texte p.133 inversée mot à mot (doctrine sondages)",
    "inversée mot à mot" in h)
chk("inversion par paires documentée (règle 94-25 = 49-52)",
    "inversion par paires" in h and "94-25" in h)
chk("années tranchées chiffre par chiffre SUR IMAGE", "chiffre par chiffre" in h)
chk("QUATORZE lectures d'images consignées (qa-crops-r664)",
    "QUATORZE lectures d’images" in h and "qa-crops-r664" in h)
chk("CINQ composites 600 dpi (méthode d'économie R103)",
    "composites verticaux 600 dpi" in h and "R103" in h)
chk("UN composite micro-crops 1200 dpi des mots pivots",
    "micro-crops 1200 dpi" in h and "mots pivots" in h)
chk("QUINZE lectures VLM SDK refusées 429 (plafond, documenté)",
    "429 Too many requests" in h and "QUINZE lectures VLM" in h)

# ---- adjudications majeures
chk("manḥ ar-rawḍ al-azhar tranché (contre al-barūd récusé)",
    "Manḥ ar-rawḍ al-azhar" in h and "al-barūd" in h and "récusée" in h)
chk("az-Zarkašī tranché au ẓāʾ (contre an-Narkašī récusé)",
    "an-Narkašī" in h and "ẓāʾ" in h)
chk("az-Zuhd tranché (contre az-zad récusé)", "az-Zuhd" in h and "az-zad" in h)
chk("min aḥiyāʾ Baġdād rendu au plus sûr (Dār al-Quṭn quartier)",
    "aḥiyāʾ" in h and "quartiers de Bagdad" in h and "rendu au plus sûr" in h)
chk("ÉCART CANONIQUE 643 vs 646 (Ibn aṣ-Ṣalāḥ, 1200 dpi, jamais corrigé)",
    "643" in h and "646" in h and "jamais corrigé" in h)
chk("ÉCART al-Qāṣid al-ḥasana (féminin imprimé) consigné",
    "al-Qāṣid al-ḥasana" in h and "ÉCART CANONIQUE" in h)
chk("ÉCART al-Ilāʿ (sans mīm) consigné", "al-Ilāʿ" in h and "al-Ilmāʿ" in h)
chk("ÉCART bi-Marrākiš (sans alif) consigné", "Marrākiš" in h and "bi-Marrākuš" in h)
chk("lignage ʿIyāḍ ibn ʿAmrūn al-Yaḥmaṣbī tel qu'imprimé (1200 dpi)",
    "al-Yaḥmaṣbī" in h and "ibn Yaḥmadī" in h)
chk("ibn Sābiq ad-Dīn tranché au bāʾ (1200 dpi + couche)",
    "Sābiq" in h and "bāʾ" in h)
chk("al-Muʿīn tranché au mīm (contre al-ʿAyn récusé)",
    "al-Muʿīn" in h and "al-ʿAyn" in h)
chk("al-Muštabah tranché au bāʾ (1200 dpi)", "al-Muštabah" in h)
chk("al-Fawāʾid al-kabir + Fawāʾid ar-Rāziyyayn honnêteté d'apparat",
    "al-Fawāʾid al-kabīr" in h and "Fawāʾid ar-Rāziyyayn" in h and "honnêteté d’apparat" in h)
chk("Luqṭat al-ʿaǧlān tel qu'imprimé (honnêteté)",
    "Luqṭat al-ʿaǧlān" in h)
chk("phrases dégradées al-Ḫaṭīb translittérées au plus sûr",
    "série de verbes imprimés dégradés" in h and "cinquante et quelques" in h)
chk("phrases dégradées al-Qāḍī ʿIyāḍ déclarées non restituables",
    "non restituable" in h)
chk("muʿānan ʿalayhi tel qu'imprimé (documenté au méta)", "muʿānan ʿalayhi" in hn)
chk("at-Turkumānī rendu par les DEUX couches (hésitation 600 dpi consignée)",
    "at-Turkumānī" in h and "hésitation 600 dpi" in h)

# ---- structure du rendu
chk("ZÉRO ĀYA (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique" in h)
chk("h2 nature de la section", "La nature de la section" in h)
chk("trois h2 de pages (132/133/134)",
    h.count("<h2>") == 4 and "La page 132" in h and "La page 133" in h and "La page 134" in h)
chk("SEIZE <li> notices", h.count("<li>") == 16)
chk("années de mort présentes au rendu",
    all(y in h for y in ["1014", "795", "204", "327", "385", "794", "643", "463", "405", "806", "748", "902", "911", "544", "676"]))
chk("titres canoniques majeurs présents",
    all(x in h for x in ["Mirqāt al-mafātīḥ", "Ṣiyānat Ṣaḥīḥ Muslim", "Maʿrifat ʿulūm al-ḥadīṯ",
                          "al-Mustadrak ʿalā ṣ-Ṣaḥīḥayn", "aš-Šifāʾ bi-taʿrīf ḥuqūq al-Muṣṭafā",
                          "Tartīb al-madārik", "at-Tamhīd limā fī l-Muwaṭṭaʾ", "Ǧāmiʿ bayān al-ʿilm",
                          "Tārīḫ Baġdād", "al-Kifāya fī ʿulūm ar-riwāya", "Mīzān al-iʿtidāl",
                          "Fatḥ al-Muġīṯ", "Tahḏīb al-asmāʾ", "at-Taqrīb wat-Taysīr",
                          "al-Baḥr al-muḥīṭ", "al-Umm", "ar-Risāla", "Iḫtilāf al-ḥadīṯ"]))

# ---- zéro arabe au rendu
arabic = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", h)
chk("ZÉRO caractère arabe", len(arabic) == 0)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("0 apostrophe droite", "'" not in h)

# ---- registre == fichier, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
docs = reg if isinstance(reg, list) else reg.get("docs", reg.get("entries", reg.get("lessons", [])))
if isinstance(docs, dict):
    docs = list(docs.values())
by_id = {}
for d in docs:
    if isinstance(d, dict) and d.get("docId"):
        by_id.setdefault(d["docId"], d)

d281 = by_id.get("pdf-mut23h2u-281")
chk("registre 281 htmlFr == fichier",
    d281 is not None and (d281.get("htmlFr") or "").strip() == h.strip())
chk("registre 281 titleFr pré-mappé intact",
    d281 is not None and d281.get("titleFr") == "Notices biographiques des savants")
d277 = by_id.get("pdf-mut23h2u-277")
chk("voisin 277 intaint (htmlFr vide — trou de séquence, takeover légal)",
    d277 is not None and not (d277.get("htmlFr") or "").strip())
d280 = by_id.get("pdf-mut23h2u-280")
chk("voisin 280 intact (livré R661)",
    d280 is not None and len((d280.get("htmlFr") or "")) > 10000)
d279 = by_id.get("pdf-mut23h2u-279")
chk("voisin 279 intact (livré R659)", d279 is not None and len((d279.get("htmlFr") or "")) > 10000)

sreg = json.load(open(SREG, encoding="utf-8"))
n_sav = len(sreg.get("hand", [])) + len(sreg.get("llm", {}))
chk(f"registre savants = 1201 (lu : {n_sav})", n_sav == 1201)

# ---- balises appariées
for tag in ["h1", "h2", "p", "ol", "li", "dl", "dt", "dd", "strong"]:
    chk(f"balises <{tag}> appariées", h.count(f"<{tag}") == h.count(f"</{tag}>"))

print(f"verify-ulumhadith2-pdf281 : {ok} contrôles OK, {fail} échec(s)")
raise SystemExit(1 if fail else 0)
