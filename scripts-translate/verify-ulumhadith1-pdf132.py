#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-132
(le ḥadīṯ muḍṭarib, p.104-107 du manuel ulum-hadith-1-thanawi.pdf) :
bannière « ad-dars 21 » ; bornes p.104-107 par DOUBLE sondage (bannière ad-dars
22 + objectifs المدرج lus à l'OCR p.108, concordants avec l'iʿdād qablī p.107
الإدراج ×2) ; bayt — « wa-ḏū ḫtilāfi sanadin aw maʿnan *** muḍṭaribun ʿinda
ahli l-fanni » tranché image (OCR « sanʿ » récusé, « amayl » récusé, rendu ×2
bannière p.104 + reprise p.105) ; glose (mawǧ, ahīl) ; istikhlāṣ ×2 ; taḥlīl :
définition (muʿallal, terminologie), faces différentes égales, exemple mrafūʿ/
mawqūf iṯbāt/nafy + « kamā yaqaʿu fī s-sanadi qad yaqaʿu fī l-matni » (lu à
l'image), non-muḍṭarib ×3 (concordantes, différence sans effet, ǧamʿ/tarǧīḥ
possibles), conditions ×2 ; divisions : sanad (ḥadīṯ Abū Bakr Hūd + ad-Dāraquṭnī
dix faces, murṣal/mauṣūl, musnads Abū Bakr/Saʿd/ʿĀʾiša, ṯiqāt, ǧamʿ difficile,
[Tadrīb ar-rāwī 1/312]) + matn (Fāṭima bint Qays, at-Tirmiḏī « inna fī l-māli
ḥaqqan siwā z-zakāt » / Ibn Māǧah « laysa fī l-māli ḥaqqun siwā z-zakāt »,
réfs imprimées translittérées, Mīmūn al-Aʿwar faible, « sawā l-iḍṭirāb » tranché
au bord gauche, « ṯāniyan » tenu, ǧamʿ possible mustaḥabb/wāǧib) ; taqwīm ×3 ;
istiṯmār (Ibn aṣ-Ṣalāḥ [Muqaddima 1/93] — tasāwī, tarǧīḥ, aḥfaẓ/aṯṯub) ;
taʿammul ×2 ; iʿdād qablī (mudraǧ ×2 questions) ; bornes p.104-107 ; ﷺ tenu
(U+FDFA), zéro āya, zéro résidu.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf132.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-132-fr.html"
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
      if l["docId"] == "pdf-mut23h2q-132"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 21", "leçon 21" in (m.group(1) if m else ""))

# 2. bannière / bornes
chk("badge ad-dars 21", "ad-dars 21" in plain)
chk("bornes p.104-107 documentées", "page imprimée 104" in plain and "page 107" in plain)
chk("bannière ad-dars 22 p.108 (sondage)", "ad-dars 22" in plain and "page 108" in plain)
chk("double sondage (jamais deviné)", "double sondage" in plain and "jamais devinée" in plain)
chk("concordance iʿdād qablī p.107", "concordants" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. tamhīd
chk("tamhīd : ḍabṭ condition", "figure la rétention (aḍ-ḍabṭ)" in plain)
chk("tamhīd : yuḍṭarib ḥifẓuhum", "peut se troubler" in plain)
chk("tamhīd question double", "Qu’est-ce donc que le ḥadīṯ muḍṭarib" in plain)

# 4. bayt
chk("bayt : wa-ḏū ḫtilāfi sanadin aw maʿnan", "wa-ḏū ḫtilāfi sanadin aw maʿnan" in plain)
chk("bayt : muḍṭaribun ʿinda ahli l-fanni", "muḍṭaribun ʿinda ahli l-fanni" in plain)
chk("OCR sanʿ récusé (image)", "sanʿ" in plain and "récusée" in plain)
chk("OCR amayl récusé (image)", "amayl" in plain)
chk("bayt rendu deux fois (bannière + reprise)", "concordante avec la bannière, tranchée deux fois" in plain)
chk("traduction bayt", "variation d’isnād ou de sens" in plain)

# 5. glose
chk("glose : mawǧ", "la vague s’est troublée" in plain)
chk("glose : ahīl diminutif", "diminutif de ahl" in plain)

# 6. istikhlāṣ ×2
chk("istikhlāṣ deux questions", "sous la forme de deux questions" in plain)
chk("IS1 maqṣūd", "Qu’est-ce qui est visé par le ḥadīṯ muḍṭarib" in plain)
chk("IS2 aqsām al-ḥukm", "les divisions du jugement d’iḍṭirāb" in plain)

# 7. taḥlīl — définition
chk("muḍṭarib du faible", "des types des ḥadīṯs faibles" in plain)
chk("inscrit dans le muʿallal", "inscrit dans le ḥadīṯ muʿallal" in plain)
chk("terminologie isole", "l’isoler par l’étude" in plain)
chk("définition faces différentes", "transmis sur des faces différentes" in plain)
chk("faces égales", "ces faces sont égales" in plain)
chk("exemple mrafūʿ/mawqūf", "un ḥadīṯ élevé, et que l’autre le transmette arrêté" in plain)
chk("exemple iṯbāt/nafy", "avec l’affirmation d’une chose, et que d’autres le transmettent avec sa négation" in plain)
chk("sanad→matn", "de même qu’ils se produisent dans l’isnād, peuvent se produire dans le matn" in plain)
chk("non-muḍṭarib : concordantes", "des faces concordantes" in plain)
chk("non-muḍṭarib : différence d’expression", "différence d’expression" in plain)
chk("non-muḍṭarib : ǧamʿ/tarǧīḥ possibles", "le trouble disparaît" in plain)
chk("condition 1 égalité", "les faces soient égales en force auprès du critique" in plain)
chk("condition 2 ǧamʿ/tarǧīḥ impossibles", "que le rassemblement entre elles ne soit point possible, ni la préférence" in plain)

# 8. muḍṭarib sanad — Abū Bakr + Dāraquṭnī
chk("deux divisions", "un muḍṭarib de son isnād, et un muḍṭarib de son matn" in plain)
chk("ḥadīṯ Abū Bakr", "ô Messager de Dieu, je te vois avoir blanchi" in plain)
chk("šayibtanī Hūd wa-aḫawātuhā", "m’ont fait blanchir Hūd et ses sœurs" in plain)
chk("Dāraquṭnī cité", "Ad-Dāraquṭnī a dit" in plain)
chk("Abū Isḥāq voie unique", "que par la voie d’Abū Isḥāq" in plain)
chk("dix faces", "d’environ dix faces" in plain)
chk("murṣal/mauṣūl", "murṣal" in plain and "mauṣūl" in plain)
chk("musnads ×3", "musnad d’Abū Bakr" in plain and "musnad de Saʿd" in plain and "musnad de ʿĀʾiša" in plain)
chk("ṯiqāt sans tarǧīḥ", "hommes de confiance, sans que la préférence" in plain)
chk("ǧamʿ difficile", "le rassemblement est difficile" in plain)
chk("réf. Tadrīb ar-rāwī 1/312", "Tadrīb ar-rāwī d’as-Suyūṭī, 1/312" in plain)

# 9. muḍṭarib matn — Fāṭima bint Qays
chk("exemplification difficile", "l’exemplification en est difficile, car ses exemples sont peu nombreux" in plain)
chk("chaîne Sharīk/Abū Ḥamza/aš-Šaʿbī/Fāṭima", "de Sharīk, d’Abū Ḥamza, d’aš-Šaʿbī, de Fāṭima bint Qays" in plain)
chk("sālat aw sullit", "j’ai demandé, ou on me fit demander, au Prophète ﷺ" in plain)
chk("Tirmiḏī inna fī l-māli ḥaqqan", "il est dans le bien un droit en dehors de la zakāt" in plain)
chk("réf. Tirmiḏī imprimée translittérée", "chapitre de ce qui fut rapporté" in plain)
chk("Ibn Māǧah laysa fī l-māli ḥaqqun", "il n’est dans le bien aucun droit en dehors de la zakāt" in plain)
chk("réf. Ibn Māǧah imprimée translittérée", "mā addā zakātahu laysa bi-kanz" in plain)
chk("iḍṭirāb lafẓ + maʿnā", "dans la formule et dans le sens" in plain)
chk("Mīmūn al-Aʿwar faible", "Mīmūn al-Aʿwar, et il est faible" in plain)
chk("sawā l-iḍṭirāb tranché bord gauche", "recadrage du bord gauche" in plain and "autre facteur que l’iḍṭirāb" in plain)
chk("ṯāniyan tenu", "secondement" in plain and "tenue telle quelle" in plain)
chk("ǧamʿ possible mustaḥabb/wāǧib", "sur le recommandé, et chez la seconde sur l’obligatoire" in plain)
chk("muḍṭarib type du faible", "des types du faible, par l’insinuation" in plain)

# 10. taqwīm — 3 questions
chk("taqwīm 3 questions", "sous la forme de trois questions" in plain)
chk("TQ1 définition + conditions", "j’en expose les conditions" in plain)
chk("TQ2 divisions", "Quelles sont les divisions du ḥadīṯ muḍṭarib" in plain)
chk("TQ3 ḥukm al-ʿamal", "le jugement de l’action faite du ḥadīṯ muḍṭarib" in plain)

# 11. istiṯmār — Ibn aṣ-Ṣalāḥ
chk("Ibn aṣ-Ṣalāḥ cité", "Ibn aṣ-Ṣalāḥ dit" in plain)
chk("taḫtalif ar-riwāya", "dont la transmission varie" in plain)
chk("tasāwat ar-riwāyatān", "les deux transmissions s’égalisent" in plain)
chk("tarǧaḥat iḥdāhumā", "l’une des deux prend le dessus" in plain)
chk("aḥfaẓ/aṯṯub", "plus retentif, ou plus compagn de celui dont il transmet" in plain)
chk("al-ḥukm li-r-rāǧiḥa", "le jugement appartient à la préférée" in plain)
chk("réf. Muqaddima 1/93", "Muqaddimat Ibn aṣ-Ṣalāḥ, 1/93" in plain)
chk("Taʿ 1 muḍṭarib", "visé par le nom de muḍṭarib" in plain)
chk("Taʿ 2 tarǧīḥ", "Par quoi une transmission prend-elle le dessus" in plain)

# 12. iʿdād qablī — leçon suivante mudraǧ
chk("préparation mudraǧ", "je connais la signification du ḥadīṯ mudraǧ" in plain)
chk("aqsām al-idrāǧ", "les divisions de l’idrāǧ" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 13. ﷺ tenu, zéro āya, zéro résidu
chk("ﷺ tenu (U+FDFA ×3)", h.count("\ufdfa") == 3)
chk("doc mentionne aucune āya", "aucune āya" in plain)
residus = ["TODO", "XXX", "undefined", "NaN", "【", "____", "recycle", "takeover", "mtime", "⟨AR⟩"]
chk("zéro résidu technique", not any(r in plain for r in residus))

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)
