#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-277
(leçon 23 — al-muṣaḥḥaf wal-muḥarrif — pages 120-124 du manuel
ulum-hadith-2-thanawi_text.pdf) : le trou de séquence du volume comblé
(la dernière leçon sans htmlFr — takeover légal du claim R658 périmé).
Bornes tranchées par sondage R657 (p.119 clôt la leçon 22 livrée R658 —
jamais retouchée ; p.120 ouvre la leçon 23 par bannière + objectifs ;
p.124 porte l'exploitation al-istiṯmār ; p.125 ouvre la leçon 24
« al-iḫtiṣār wat-tarwīya bil-maʿnā » livrée R659 — jamais touchée).
Extraction multicouche héritée R658 (raw/decoded/readable) recomplétée ;
CHIFFRES DES CITATIONS adjudiqués SUR IMAGE (l'image fait autorité,
inversion par paires documentée, règle « 94-25 » = 49-52, jamais devinée) :
Qāmūs 826 (couche 628), Muqaddima 384 (×2), ʿIlal Dāraquṭnī 287 (couche 782),
Muqaddima 385 (×2, couche 583), 389 (×2, couche 983), Musnad 18761
(DECODE 16781 RÉCUSÉ par l'image), 387 (couche 783), Maqāyīs 2/43
(couche 43/2), Tamhīd 1/70 (couche 1/07), Muqaddima 218 (couche 812) ;
NEUF lectures d'images héritées R658 (crops p.120-p.123) + TROIS nouvelles
(composites bande gauche p.123/p.124 600 dpi, tr-tmp/qa-crops-r665) ;
lectures VLM SDK refusées 429 ce jour (documenté R664) ; ADJUDICATIONS :
matn Ibn Ḥaǧar tel qu'imprimé (as-siyāq — DECODE « baqāʾ as-sāq » récusée) ;
tamhīd rendu au plus sûr (couche wat-taġyīr, image wat-taʿyīr, sens
at-taḥrīf — hésitation consignée) ; mazāḥim (zāy) contre marāḥim (rāʾ
muhmala + ḥāʾ + jīm) ; ÉCART CANONIQUE al-ǧammāʾ (canon Muslim al-ǧalāʾ)
et yuqass (canon yuqād) ; ÉCART iḥtaǧama fi s-saʿd tel qu'imprimé (canon
iḥtaǧara, correction « bi-r-rāʾ ») ; ʿĀṣim al-Aḥwal / Wāḍil al-Aḥḏab tels
qu'imprimés ; ʿanaza = la lance (Musnad 18761) ; al-Aḥzāb rendu par le sens
(glyphes indistinctes, DECODE al-Aḫrāb récusé) ; Ġundar / Ubayy b. Kaʿb ;
exploitation Ibn aṣ-Ṣalāḥ p.218 avec segment dégradé NON RESTITUABLE déclaré
(précédents R103/R664) ; ZÉRO ĀYA (cache coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf277.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-277-fr.html"
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
chk("h1 = titleFr pré-mappé « Le hadith altéré dans la graphie (muṣaḥḥaf) ou la vocalisation (muḥarrif) »",
    hn.startswith("<h1>Leçon 23 : Le hadith altéré dans la graphie (muṣaḥḥaf) ou la vocalisation (muḥarrif)"))
chk("h1 mentionne livre deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne pages 120 à 124", "pages 120 à 124" in h[:400])
chk("h1 Qāmūs 826", "826" in h[:3000])
chk("h1 Muqaddima 384 + ʿIlal 287", all(x in h[:3600] for x in ["384", "287"]))
chk("h1 Musnad 18761", "18761" in h[:7000])
chk("h1 Tamhīd 1/70", "1/70" in h[:9000])
chk("h1 exploitation Muqaddima 218", "218" in h[:9800])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("slot pdf-mut23h2u-277 documenté", "pdf-mut23h2u-277" in h)
chk("titleFr pré-mappé respecté", "Le hadith altéré dans la graphie" in h)
chk("translittération titleAr consignée", "titleAr translittéré" in h)

# ---- bornes et takeover
chk("p.119 clôt la leçon 22 (R658) jamais retouchée",
    "la page 119 clôt la leçon 22" in h and "R658" in h)
chk("p.120 ouvre la leçon 23 (bannière + objectifs, sondage R657)",
    "la page 120 OUVRE la leçon 23" in h and "R657" in h)
chk("p.124 porte l'exploitation (al-istiṯmār)", "l'exploitation (al-istiṯmār) tient la page 124" in hn)
chk("p.125 = leçon 24 jamais touchée (livrée R659)",
    "la page 125 OUVRE la leçon 24" in h and "R659" in h)
chk("trou de séquence comblé (seule leçon sans htmlFr)",
    "TROU DE SÉQUENCE COMBLÉ" in h and "seule du volume restée sans htmlFr" in h)
chk("takeover légal du claim R658 périmé documenté",
    "takeover légal" in h and "09h44 UTC" in h)
chk("artefacts d'extraction R658 réutilisés",
    "uh2-l277-raw.txt" in hn and "uh2-l277-decoded.txt" in hn and "uh2-l277-readable.txt" in hn)

# ---- extraction multicouche et lectures
chk("couche BRUTE en ordre LTR brut (texte arabe mot à mot inversé)",
    "couche texte BRUTE en ordre LTR brut" in h)
chk("inversion par paires documentée (règle 94-25 = 49-52)",
    "inversion par paires" in h and "94-25" in h)
chk("image fait autorité", "l'IMAGE fait autorité" in hn)
chk("NEUF lectures héritées R658 + TROIS nouvelles (qa-crops-r665)",
    "qa-crops-r665" in hn and "NEUF lectures d'images héritées" in hn)
chk("lectures VLM SDK refusées 429 (plafond, documenté)",
    "429" in h and "VLM" in h)

# ---- adjudications des chiffres (image > couches)
chk("Qāmūs : couche 628 → image 826", "couche 628, image 826" in h)
chk("ʿIlal Dāraquṭnī : couche 782 → image 287", "couche 782, image 287" in h)
chk("Muqaddima : couche 583 → image 385", "couche 583, image 385" in h)
chk("Muqaddima : couche 983 → image 389", "couche 983, image 389" in h)
chk("Musnad : DECODE 16781 RÉCUSÉ par l'image (18761)",
    "16781" in h and "RÉCUSÉE par l'image" in hn)
chk("Maqāyīs : couche 43/2 → image 2/43", "couche 43/2, image 2/43" in h)
chk("Tamhīd : couche 1/07 → image 1/70", "couche 1/07, image 1/70" in h)
chk("Muqaddima exploitation : couche 812 → image 218", "couche 812, image 218" in h)
chk("Muqaddima ʿanaza : couche 783 → image 387", "couche 783, image 387" in h)

# ---- adjudications majeures
chk("matn Ibn Ḥaǧar tel qu'imprimé (as-siyāq)",
    "le maintien du contexte (as-siyāq)" in h and "baqāʾ as-sāq" in h and "récusée" in h)
chk("commentaire : le contexte = l'indice qui désigne le visé",
    "l'indice qui désigne ce qui est visé" in hn)
chk("tamhīd rendu au plus sûr (hésitation couche/image/sens consignée)",
    "hesitation" in hn.lower() or "hésitation consignée" in h)
chk("mazāḥim (zāy) contre marāḥim (rāʾ muhmala + ḥāʾ + jīm)",
    "mazāḥim" in h and "marāḥim" in h and "zāy" in h and "jīm" in h)
chk("ÉCART CANONIQUE al-ǧammāʾ (canon Muslim al-ǧalāʾ) jamais corrigé",
    "al-ǧammāʾ" in h and "al-ǧalāʾ" in h and "jamais corrigé" in h)
chk("ÉCART yuqass (canon yuqād) consigné", "yuqass" in h and "yuqād" in h)
chk("ÉCART iḥtaǧama fi s-saʿd tel qu'imprimé (canon iḥtaǧara)",
    "iḥtaǧama" in hn and "iḥtaǧara" in hn and "tel qu'imprimé" in hn)
chk("ʿĀṣim al-Aḥwal / Wāḍil al-Aḥḏab tels qu'imprimés (convergence)",
    "ʿĀṣim al-Aḥwal" in h and "Wāḍil al-Aḥḏab" in h)
chk("taṣḥīf de la vue / de l'ouïe rendus (aṣ-Ṣūlī sittā → šayʾ)",
    "taṣḥīf de la vue" in hn and "taṣḥīf de l'ouïe" in hn and "aṣ-Ṣūlī" in hn and "šayʾ" in hn)
chk("ʿanaza = la lance (Musnad 18761) — comprehension non voulue",
    "la lance que l'on plante devant l'orant" in hn)
chk("al-Aḥzāb rendu par le sens (DECODE al-Aḫrāb récusé)",
    "le jour des coalisés (al-Aḥzāb)" in h and "al-Aḫrāb" in h)
chk("Ġundar / Ubayy b. Kaʿb (père martyr à Uḥud)",
    "Ġundar" in h and "Ubayy b. Kaʿb" in h and "Uḥud" in h)
chk("akḥal = veine de la main au milieu de l'avant-bras",
    "une veine de la main au milieu de l'avant-bras" in hn)
chk("exploitation Ibn aṣ-Ṣalāḥ p.218 segment dégradé NON RESTITUABLE déclaré",
    "segment imprimé dégradé non restituable" in h and "218" in h)
chk("Maqāyīs Ibn Fāris 2/43 cité", "Ibn Fāris" in h and "2/43" in h)
chk("différence muṣaḥḥaf/muḥarrif (changement commun, espèce différente)",
    "les deux partagent le changement et diffèrent par son espèce" in h)
chk("jugement : faute rare ne porte pas atteinte au ḍabṭ / multipliée = faible de mémoire",
    "faute légère n'épargne personne" in hn and "faible de mémoire" in hn)
chk("rejet du mot faussé hors de son origine", "hors de son origine" in h)

# ---- structure du rendu
chk("ZÉRO ĀYA (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique" in h)
chk("neuf h2 pédagogiques du gabarit", h.count("<h2>") == 9)
chk("h2 objectifs + tamhīd + matn + commentaire présents",
    all(x in h for x in ["Les objectifs de la leçon", "Le tamhīd (l’introduction)",
                         "le matn du ḥāfiẓ Ibn Ḥaǧar", "Le commentaire"]))
chk("h2 analyse + ahtadī + taqwīm + istiṯmār + iʿdād présents",
    all(x in h for x in ["L’analyse (at-taḥlīl)", "Je m’oriente et j’imite (ahtadī wa-aqtadī)",
                         "L’évaluation (at-taqwīm)", "L’exploitation (al-istiṯmār)",
                         "La préparation de la leçon suivante (al-iʿdād al-qiblī)"]))
chk("trois objectifs de la leçon listés",
    "les deux notions du muṣaḥḥaf et du muḥarrif" in h and "l’écriture et la transmission" in h)
chk("trois divisions du taṣḥīf (emplacement / manšaʾ / lafẓ-maʿnā)",
    "selon son emplacement" in h and "selon sa source (manšaʾ)" in h and "selon le mot ou le sens" in h)
chk("leçon 24 annoncée (pré-mappée 278)",
    "l’abrègement du ḥadīṯ et sa transmission selon le sens" in h)
chk("recherche Mālik + fawāʾid lafẓ/maʿnā au iʿdād qiblī",
    "doctrine de l’imam Mālik" in h and "ce qui en découle" in h)

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

d277 = by_id.get("pdf-mut23h2u-277")
chk("registre 277 htmlFr == fichier",
    d277 is not None and (d277.get("htmlFr") or "").strip() == h.strip())
chk("registre 277 titleFr pré-mappé intact",
    d277 is not None and d277.get("titleFr") == "Leçon 23 : Le hadith altéré dans la graphie (muṣaḥḥaf) ou la vocalisation (muḥarrif)")
d276 = by_id.get("pdf-mut23h2u-276")
chk("voisin 276 intact (livré R658)",
    d276 is not None and len((d276.get("htmlFr") or "")) > 10000)
d278 = by_id.get("pdf-mut23h2u-278")
chk("voisin 278 intact (livré R659)",
    d278 is not None and len((d278.get("htmlFr") or "")) > 10000)
d281 = by_id.get("pdf-mut23h2u-281")
chk("voisin 281 intact (livré R664)",
    d281 is not None and len((d281.get("htmlFr") or "")) > 10000)

sreg = json.load(open(SREG, encoding="utf-8"))
n_sav = len(sreg.get("hand", [])) + len(sreg.get("llm", {}))
chk(f"registre savants = 1202 (lu : {n_sav})", n_sav == 1202)

n_done = sum(1 for x in docs if isinstance(x, dict) and (x.get("htmlFr") or "").strip())
chk(f"volume uh2 CLOSE 27/27 (lu : {n_done}/27)", n_done == 27)

# ---- balises appariées
for tag in ["h1", "h2", "p", "ol", "li", "dl", "dt", "dd", "strong"]:
    chk(f"balises <{tag}> appariées", h.count(f"<{tag}") == h.count(f"</{tag}>"))

print(f"verify-ulumhadith2-pdf277 : {ok} contrôles OK, {fail} échec(s)")
raise SystemExit(1 if fail else 0)
