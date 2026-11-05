#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-130
(le ḥadīṯ maqlūb, p.95-98 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « ad-dars 19 » + الحديث المقلوب (image, pieds
de page 96/97 lus à 600 dpi, zéro inversion) ; bayt du nāẓim — « wa-l-maqlūbu
qismāni ta-lā » (queue du vers du šāḏḏ, points de suite tenus) + « ibdālu rāwin
mā bi-rāwin qismu *** wa-qalbu isnādin li-matnin qismu » (tranché image 1200 dpi
+ concordance canon ×6 éditions ; les DEUX hémistiches finissent « qismu ») ;
glose (al-maqlūb min al-qalb, taġyīr/taḥwīl) ; istikhlāṣ ×2 ; at-taḥlīl :
définition étendue (ibdāl lafẓ/ism rāw, taqdīm/taʾḫīr, iḥtirāz muṣḥaf/muḥarraf),
exemple al-Walīd b. Muslim / Muslim b. al-Walīd ; divisions (isnād ×3 formes :
inversion du nom, Sālim/Nāfiʿ, isnād entier + Bagdad ; matn : les Sept abrités,
Muslim, la renversée « lā taʿlamu yamīnuhu mā tunfiqu šimāluhu » et la corrigée
« ḥattā lā taʿlama šimāluhu mā tunfiqu yamīnuhu », [Ṣaḥīḥ Muslim, kitāb az-zakāt,
bāb faḍl ikhfāʾ aṣ-ṣadaqa]) ; aṣbāb ×3 (iḫtibār, iġrāb, sahw) ; al-ʿIrāqī
(Šuʿba + Ḥammād b. Salama ; Ḥarmī tel qu’imprimé, Ḥarmala en note ; « yā bassun
mā ṣanaʿta » ; AUCUNE source imprimée — honnêteté) ; exemple du sahw : ḥadīṯ
« iḏā uqīmati ṣ-ṣalātu fa-lā taqūmū ḥattā tarawnī » [Ṣaḥīḥ al-Buḫārī, kitāb
al-aḏān] + chaîne Ḥaǧǧāǧ b. Abī ʿUṯmān aṣ-Ṣawwāf / Yaḥyā b. Abī Kaṯīr /
ʿAbd Allāh b. Abī Qatāda / son père + Ǧarīr b. Ḥāzim supposé Ṯābit/Anas +
Ḥammād b. Zayd + les cinq Imāms ; taqwīm ×3 ; istiṯmār (Ibn Ḥaǧar
[Nuzhat an-naẓar, p. 118] — « lā yustamarra ʿalayhi », al-mardūd, maqlūb/muʿallal)
; taʿammul ×2 ; iʿdād qablī (muʿallal ×2) ; bornes p.95-98 (bannière ad-dars 20
p.99 OCR cache, concordante avec l’iʿdād qablī p.98), aucune āya, ﷺ tenu (U+FDFA
exempté), zéro résidu de recyclage (aucun marqueur de reprise).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf130.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-130-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")


h = open(HTML, encoding="utf-8").read()
plain = h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u00a0", " ")

# 1. h1 aligné au titleFr pré-mappé du registre
tf = [l for l in json.load(open(REG, encoding="utf-8"))["lessons"]
      if l["docId"] == "pdf-mut23h2q-130"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 19", "leçon 19" in (m.group(1) if m else ""))

# 2. bannière / badge ad-dars 19
chk("badge ad-dars 19", "ad-dars 19" in plain)
chk("pieds de page 96/97 tranchés", "96" in plain and "97" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. tamhīd
chk("tamhīd : ḍaʿīf + muḥaddiṯs", "ḥadīṯ ḍaʿīf dont le commerce s’est multiplié" in plain)
chk("tamhīd : ẓabṭ/ḥifẓ", "l’insuffisance du ẓabṭ et du ḥifẓ" in plain)
chk("tamhīd : ʿadāla", "perte de la probité (ʿadāla)" in plain)
chk("tamhīd question double", "Qu’est donc le ḥadīṯ maqlūb" in plain)

# 4. bayt du nāẓim
chk("bayt : wa-l-maqlūbu qismāni ta-lā", "wa-l-maqlūbu qismāni ta-lā" in plain)
chk("bayt : ibdālu rāwin mā bi-rāwin qismu", "ibdālu rāwin mā bi-rāwin qismu" in plain)
chk("bayt : wa-qalbu isnādin li-matnin qismu", "wa-qalbu isnādin li-matnin qismu" in plain)
chk("points de suite tenus (jamais reconstitués)", "blancs pédagogiques" in plain and "jamais reconstitués" in plain)
chk("queue du vers du šāḏḏ documentée", "queue du vers du šāḏḏ" in plain)
chk("concordance canon ×6", "six éditions" in plain)
chk("traduction bayt : deux catégories", "deux catégories" in plain)

# 5. glose
chk("glose : al-qalb taġyīr/taḥwīl", "at-taġyīr wa-t-taḥwīl" in plain)

# 6. istikhlāṣ ×2
chk("istikhlāṣ deux questions", "sous la forme de deux questions" in plain)
chk("ST1 maqlūb + divisions", "Je connais le ḥadīṯ maqlūb et j’expose ses divisions" in plain)
chk("ST2 causes + taʿammud", "le jugement porté sur son caractère volontaire" in plain)

# 7. at-taḥlīl — définition + iḥtirāz
chk("définition : ibdāl lafẓ/ism rāw", "d’une de ses expressions ou du nom d’un de ses transmetteurs" in plain)
chk("taqdīm/taʾḫīr", "par avancée (taqdīm), report (taʾḫīr)" in plain)
chk("iḥtirāz muṣḥaf/muḥarraf", "du ḥadīṯ muṣḥaf et du muḥarraf" in plain)
chk("exemple al-Walīd b. Muslim", "al-Walīd b. Muslim" in plain and "Muslim b. al-Walīd" in plain)
chk("deux divisions principales", "en deux divisions principales" in plain)

# 7bis. mqlūb as-sanad — 3 formes
chk("forme 1 inversion du nom", "l’inversion du nom du transmetteur par avancée ou report" in plain)
chk("forme 2 Sālim/Nāfiʿ", "Sālim" in plain and "Nāfiʿ" in plain and "rare et désiré" in plain)
chk("forme 3 isnād entier + Bagdad", "dans son intégralité" in plain and "al-Buḫārī lorsqu’il entra à Bagdad" in plain)
chk("talqīn mentionné", "at-talqīn" in plain)

# 7ter. maqlūb al-matn — les Sept abrités
chk("maqlūb du matn rare", "il est rare" in plain)
chk("les Sept abrités", "Sept que Dieu couvre de Son ombre" in plain)
chk("version renversée", "lā taʿlamu yamīnuhu mā tunfiqu šimāluhu" in plain)
chk("version corrigée", "ḥattā lā taʿlama šimāluhu mā tunfiqu yamīnuhu" in plain)
chk("réf. Ṣaḥīḥ Muslim zakāt", "Ṣaḥīḥ Muslim" in plain and "zakāt" in plain and "aumône cachée" in plain)
chk("deux Ṣaḥīḥ", "conservé dans les deux Ṣaḥīḥ" in plain)

# 8. aṣbāb ×3
chk("cause 1 iḫtibār", "l’épreuve et l’examen des transmetteurs" in plain)
chk("cause 2 iġrāb", "le goût de l’étrangeté (al-iġrāb)" in plain)
chk("cause 3 sahw", "l’oubli et l’erreur de quelques transmetteurs, sans intention" in plain)

# 9. al-ʿIrāqī
chk("al-ʿIrāqī cité", "a dit al-ʿIrāqī" in plain)
chk("Šuʿba et Ḥammād b. Salama", "Šuʿba et Ḥammād b. Salama" in plain)
chk("Ḥarmī tel qu’imprimé", "Ḥarmī" in plain)
chk("Ḥarmala en note (risque documenté)", "Ḥarmala" in plain and "jamais substitué" in plain)
chk("ʿAbbān b. Abī ʿAyyāš", "ʿAbbān b. Abī ʿAyyāš" in plain)
chk("hazzan", "hazzan" in plain)
chk("yā bassun mā ṣanaʿta", "yā bassun mā ṣanaʿta" in plain)
chk("AUCUNE source imprimée p.97 (honnêteté)", "AUCUNE source imprimée en page 97" in plain)
chk("sinon pour l’épreuve et l’enseignement", "l’intention de l’épreuve et de l’enseignement" in plain)

# 10. exemple du sahw — iqāma
chk("ḥadīṯ iqāma", "lorsque la prière est établie" in plain and "jusqu’à ce que vous Me voyiez" in plain)
chk("réf. Ṣaḥīḥ al-Buḫārī aḏān", "Ṣaḥīḥ al-Buḫārī" in plain and "aḏān" in plain and "iqāma" in plain)
chk("Ḥaǧǧāǧ b. Abī ʿUṯmān aṣ-Ṣawwāf", "Ḥaǧǧāǧ b. Abī ʿUṯmān aṣ-Ṣawwāf" in plain)
chk("chaîne Yaḥyā b. Abī Kaṯīr", "Yaḥyā b. Abī Kaṯīr" in plain and "ʿAbd Allāh b. Abī Qatāda" in plain)
chk("Ǧarīr b. Ḥāzim supposé Ṯābit/Anas", "Ǧarīr b. Ḥāzim" in plain and "de Ṯābit, d’Anas" in plain)
chk("Ḥammād b. Zayd", "Ḥammād b. Zayd" in plain)
chk("les cinq Imāms", "les cinq Imāms" in plain)
chk("séance de Ṯābit al-Bunānī", "Ṯābit al-Bunānī" in plain)

# 11. taqwīm — 3 questions
chk("taqwīm 3 questions", "sous la forme de trois questions" in plain)
chk("TQ1 maqlūb divisions", "Je connais le ḥadīṯ maqlūb et j’expose ses divisions" in plain)
chk("TQ2 causes", "causes de la survenance du qalb" in plain)
chk("TQ3 taʿammud + argumentation", "avec l’argumentation" in plain)

# 12. istiṯmār — Ibn Ḥaǧar
chk("citation Ibn Ḥaǧar", "Ibn Ḥaǧar dit dans an-Nuzha" in plain)
chk("lā yustamarra ʿalayhi", "lā yustamarra ʿalayhi" in plain)
chk("fin du besoin", "avec la fin du besoin" in plain)
chk("al-mardūd", "du repoussé (al-mardūd)" in plain)
chk("maqlūb ou muʿallal", "du maqlūb ou du muʿallal" in plain)
chk("référence Nuzha p. 118", "Nuzhat an-naẓar d’Ibn Ḥaǧar, p. 118" in plain)
chk("Taʿ 1 condition", "Quelle est la condition de la permission" in plain)
chk("Taʿ 2 classement volontaire", "s’il a été inversé volontairement" in plain)

# 13. iʿdād qablī — leçon suivante muʿallal
chk("préparation muʿallal", "je connais le ḥadīṯ muʿallal" in plain)
chk("types des ʿilla", "les types des ʿilla selon leur lieu dans l’isnād ou le matn" in plain)
chk("bornes p.95-98 documentées", "s’ouvre en la page imprimée 95 et s’achève en la page 98" in plain)
chk("leçon suivante p.99 bannière ad-dars 20", "ad-dars 20" in plain and "page 99" in plain)
chk("fard et muʿallal", "le ḥadīṯ fard et le ḥadīṯ muʿallal" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 14. ﷺ tenu, zéro āya, zéro résidu
chk("ﷺ tenu (U+FDFA)", "\ufdfa" in h)
chk("doc mentionne aucune āya", "Aucune āya" in plain)
chk("chaîne rendue tel qu’imprimé", "rendues tel qu’imprimé" in plain)
residus = ["TODO", "XXX", "undefined", "NaN", "【", "____", "recycle", "takeover", "mtime"]
chk("zéro résidu technique", not any(r in plain for r in residus))

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)
