#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-128
(le ḥadīṯ mudallas, p.85-90 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « al-dars 17 » + الحديث المدلس (OCR 300 dpi
cache R593), matn du nāẓim — « wa-mā atā mudallasan nawʿāni », « al-awwalu
l-isqāṭu li-sh-shaykhi wa-an », « yankila ʿamman fawqahu bi-ʿan wa-an » (fatha
tenue, ḍamma VLM récusée), « wa-th-thāni lā yusqiṭuhū lākin yaṣif » (ḍamma du
préfixe tranchée 4 lectures image, « yasquṭuhū » récusée), « awṣāfahu bi-mā bihi
lā yanʿarif » (énumération des lettres à 3600 dpi) — le PREMIER hémistiche du
premier bayt imprimé EN POINTS DE SUITE (blanc pédagogique), tenu tel quel,
jamais reconstitué ; gloses (d-l-s = ténèbres ; marchandise/acheteur —
al-mushtarī tranché 1200 dpi) ; phrase « wa-awhama samāʿahu » + « li-ishtirākihimā
fī l-khafāʾ » (2400 dpi) ; mursal khafī « wa-lam yasmaʿ minhu » (« yalqahu »
récusé par l’image) ; tadlīs al-isnād (définition, formules ʿan/an, Bayqūnī
« al-isqāṭ li-sh-shaykh », qāla/ḏakara, Mālik) ; espèces qaṭʿ (ʿAlī ibn Khašram /
Ibn ʿUyayna / az-Zuhrī / ʿAbd ar-Razzāq / Maʿmar ; Ibn ʿAdī / aṭ-Ṭanāfisī /
Hišām ibn ʿUrwa / ʿĀʾiša) ; ʿaṭf (Hušaym / Ḥuṣayn / Muġīra / Ibrāhīm) ; taswiya
(an-Nawawī / al-ʿIrāqī / Ibn Ḥaǧar le plus juste — choix du nāẓim ; Baqiyya ibn
al-Walīd al-Ḥimṣī / Ibn Abī Ḥātim ; al-Walīd ibn Muslim / Abū Mišhar) ;
tadlīs aš-šuyūḫ (titre tranché 2 lectures image ; al-Ḫaṭīb / al-Ḥasan ibn
Muḥammad al-Ḫallāl trois noms une personne, m. 439 H) ; causes (faiblesse —
illicite ; petitesse de l’âge « ou plus âgé » — fin de ligne tranchée 3600 dpi,
suite fantôme récusée ; insinuation de l’abondance — al-Ḫaṭīb) ; statut
(tafṣīl : samiʿtu/ḥaddathanā/aḫbaranā accepté, équivoque = mursal ; aš-Šāfiʿī /
Yaḥyā ibn Maʿīn / Ibn al-Madīnī / validé par al-Ḫaṭīb et Ibn aṣ-Ṣalāḥ ; shuyūḫ :
accepté s’il explique ; mutūn : rejeté par consensus + ḥadīṯ qudsī Bukhārī
janāʾiz/niyāḥa) ; taqwīm ×3 ; istiṯmār (Ibn aṣ-Ṣalāḥ 1/74 : ḏammahu aktharu
l-ʿulamāʾ, Šuʿba, aš-Šāfiʿī « aḫū l-kadb », « lāʾan azniya », ifrāṭ, wa-t-tanfīr) ;
at-taʿammul ×3 (Q1 et Q3 recouvrées à l’image 1200 dpi ; az-Zarqānī /
Bayqūnīyya) ; iʿdād qablī (šāḏḏ / munkar / statut) ; bornes p.85-90 (bannière
dars 18 p.91 OCR 300 dpi passe R594, concordante), aucune āya, ﷺ tenu (U+FDFA
exempté).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf128.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-128-fr.html"
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
      if l["docId"] == "pdf-mut23h2q-128"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 17", "leçon 17" in (m.group(1) if m else ""))

# 2. bannière / badge al-dars 17
chk("badge al-dars 17", "al-dars 17" in plain)

# 3. matn — bayts du nāẓim + points de suite
chk("bayt 1 translittéré", "wa-mā atā mudallasan nawʿāni" in plain)
chk("bayt 2 translittéré", "al-awwalu l-isqāṭu li-sh-shaykhi wa-an" in plain)
chk("bayt 2 gauche translittéré", "yankila ʿamman fawqahu bi-ʿan wa-an" in plain)
chk("bayt 3 translittéré", "wa-th-thāni lā yusqiṭuhū lākin yaṣif" in plain)
chk("bayt 3 gauche translittéré", "awṣāfahu bi-mā bihi lā yanʿarif" in plain)
chk("premier hémistiche en points de suite déclaré", "PREMIER hémistiche" in plain)
chk("blanc pédagogique jamais reconstitué", "jamais reconstitué" in plain)
chk("fatha yankila documentée", "fatha finale de yankila" in plain)
chk("ḍamma yusqiṭuhū documentée", "quatre lectures image" in plain)
chk("yanʿarif énumération lettres", "yāʾ-nūn-ʿayn-rāʾ-fāʾ" in plain)
chk("bandeau al-matn", "al-matn" in plain)

# 4. gloses
chk("glose d-l-s ténèbres", "ad-dulas" in plain and "les ténèbres" in plain)
chk("glose marchandise acheteur (1200 dpi)", "la marchandise à l’acheteur" in plain)
chk("al-mushtarī confirmé", "al-mushtarī" in plain)
chk("bandeau aš-šarḥ", "aš-šarḥ" in plain)
chk("wa-awhama samāʿahu (2400 dpi)", "wa-awhama samāʿahu" in plain)
chk("li-ishtirākihimā fī l-khafāʾ", "li-ishtirākihimā fī l-khafāʾ" in plain)

# 5. istikhlāṣ al-maḍāmīn — 3 questions
chk("istikhlāṣ 3 questions", "sous la forme de trois questions" in plain)
chk("Q1 mudallas et types", "Qu’est-ce que le mudallas et quels sont ses types" in plain)
chk("Q2 causes", "J’expose les causes du tadlīs" in plain)
chk("Q3 statut", "Quel est le statut du tadlīs" in plain)

# 6. tadlīs al-isnād — définition et cadre
chk("définition : rapporte de celui dont il a entendu", "rapporte de celui dont il a entendu, ce qu’il n’a point entendu de lui" in plain)
chk("mursal khafī wa-lam yasmaʿ minhu (2400 dpi)", "wa-lam yasmaʿ minhu" in plain)
chk("récusation yalqahu", "wa-lam yalqahu" in plain)
chk("formules ambiguës ʿan/an", "ʿan Fulān" in plain and "an Fulānan" in plain)
chk("Bayqūnī al-isqāṭ li-sh-shaykh", "al-isqāṭ li-sh-shaykh" in plain)
chk("qāla/ḏakara + Mālik", "qāla Fulān" in plain and "ḏakara Fulān" in plain and "l’imām Mālik" in plain)

# 7. espèces — qaṭʿ, ʿaṭf, taswiya
chk("tadlīs al-qaṭʿ", "tadlīs al-qaṭʿ" in plain)
chk("exemple Ibn ʿUyayna/az-Zuhrī", "nous étions chez Ibn ʿUyayna" in plain and "az-Zuhrī a dit" in plain)
chk("ʿAlī ibn Khašram", "ʿAlī ibn Khašram" in plain)
chk("ʿAbd ar-Razzāq/Maʿmar", "ʿAbd ar-Razzāq me l’a rapporté, de Maʿmar" in plain)
chk("Ibn ʿAdī aṭ-Ṭanāfisī", "Ibn ʿAdī" in plain and "aṭ-Ṭanāfisī" in plain)
chk("Hišām ibn ʿUrwa / ʿĀʾiša", "Hišām ibn ʿUrwa" in plain and "de ʿĀʾiša" in plain)
chk("tadlīs al-ʿaṭf", "tadlīs al-ʿaṭf" in plain)
chk("exemple Hušaym", "les compagnons de Hušaym" in plain)
chk("Ḥuṣayn/Muġīra/Ibrāhīm", "Ḥuṣayn et Muġīra nous ont rapporté, d’Ibrāhīm" in plain)
chk("aveu de Hušaym", "tout ce que je vous ai rapporté de Ḥuṣayn, je l’ai entendu" in plain)
chk("tadlīs at-taswiya", "tadlīs at-taswiya" in plain)
chk("faible entre deux fiables", "d’un [transmetteur] faible placé entre deux fiables" in plain)
chk("an-Nawawī/al-ʿIrāqī vs Ibn Ḥaǧar", "an-Nawawī et al-ʿIrāqī" in plain and "Ibn Ḥaǧar" in plain)
chk("le plus juste + choix du nāẓim", "l’avis le plus juste, et c’est celui sur lequel marcha le nāẓim" in plain)
chk("la plus nuisible + ġarar šadīd", "la plus nuisible des espèces du tadlīs" in plain and "ġarar šadīd" in plain)
chk("Baqiyya al-Ḥimṣī/Ibn Abī Ḥātim", "Baqiyya ibn al-Walīd al-Ḥimṣī" in plain and "Ibn Abī Ḥātim" in plain)
chk("al-Walīd ibn Muslim/Abū Mišhar", "al-Walīd ibn Muslim" in plain and "Abū Mišhar ad-Dimašqī" in plain)

# 8. tadlīs aš-šuyūḫ
chk("titre tadlīs des shaykhs", "tadlīs aš-šuyūḫ" in plain)
chk("définition : ne supprime pas, décrit", "ne supprime point son shaykh, mais qu’il le décrive" in plain)
chk("qualification/surnom/généalogie/kunya", "surnom, une généalogie ou une kunya" in plain)
chk("plus léger + partage l’ihām", "plus léger que le tadlīs de l’isnād" in plain)
chk("jugé inconnu alors que célèbre", "il le jugera inconnu (maǧhūl)" in plain)
chk("exemple al-Ḫaṭīb al-Ḫallāl", "al-Ḥasan ibn Muḥammad al-Ḫallāl" in plain)
chk("trois noms une personne m. 439", "une seule et même personne" in plain and "439 H" in plain)

# 9. causes
chk("cause faiblesse illicite", "cela est illicite" in plain)
chk("cause petitesse de l’âge", "La petitesse de son âge" in plain)
chk("ou plus âgé — fin tranchée 3600", "ou plus âgé" in plain and "ne porte rien après" in plain)
chk("cause insinuation abondance", "L’insinuation de l’abondance des shaykhs" in plain)
chk("al-Ḫaṭīb compilations", "dans ses compilations" in plain)

# 10. statut — 3 sections
chk("tafṣīl samiʿtu/ḥaddathanā/aḫbaranā", "samiʿtu" in plain and "ḥaddathanā" in plain and "aḫbaranā" in plain)
chk("équivoque = statut du mursal", "son statut est celui du mursal" in plain)
chk("aš-Šāfiʿī/Yaḥyā ibn Maʿīn/Ibn al-Madīnī", "aš-Šāfiʿī, de Yaḥyā ibn Maʿīn et d’Ibn al-Madīnī" in plain)
chk("validé par al-Ḫaṭīb et Ibn aṣ-Ṣalāḥ", "que validèrent al-Ḫaṭīb et Ibn aṣ-Ṣalāḥ" in plain)
chk("pas un mensonge mais embellie", "n’est point un mensonge" in plain and "embellie de l’apparence" in plain)
chk("shuyūḥ accepté s’il explique", "tant que — s’il est interrogé — il l’explique" in plain)
chk("mutūn rejeté consensus", "n’est point accepté, par consensus" in plain)
chk("ḥadīṯ qudsī", "que celui qui ment sur moi délibérément se prépare un siège dans le Feu" in plain)
chk("translittéré man kadaẖa", "man kadaẖa ʿalayya mutaʿammidan fa-yatabawwaʾa maqʿadahu min an-nār" in plain)
chk("réf Bukhārī janāʾiz/niyāḥa", "le livre des funérailles (al-ǧanāʾiz)" in plain and "lamentations sur le mort" in plain)

# 11. taqwīm ×3
chk("taqwīm 3 questions", "rappel (at-taqwīm) sous la forme de trois questions" in plain)
chk("Q rappel 1 types", "Quels sont les types du tadlīs" in plain)
chk("Q rappel 2 définit isnād", "Je définis le tadlīs de l’isnād" in plain)
chk("Q rappel 3 statut", "par tadlīs de l’isnād" in plain)

# 12. istiṯmār — citation Ibn aṣ-Ṣalāḥ
chk("istiṯmār Ibn aṣ-Ṣalāḥ", "la plupart des savants l’ont blâmé" in plain)
chk("ḏammahu aktharu l-ʿulamāʾ", "ḏammahu aktharu l-ʿulamāʾ" in plain)
chk("Šuʿba des plus véhéments", "des plus véhéments à le blâmer" in plain)
chk("fa-ruwīnā š-Šāfiʿī l-imām", "fa-ruwīnā ʿani š-Šāfiʿīyi l-imām" in plain)
chk("aḫū l-kadb", "at-tadlīsu aḫū l-kadb" in plain)
chk("lāʾan azniya", "lāʾan azniya aḥabbu ilayya min an udallisa" in plain)
chk("ifrāṯ + wa-t-tanfīr", "un excès" in plain and "wa-t-tanfīr" in plain)
chk("réf Muqaddima 1/74", "Muqaddimat Ibn aṣ-Ṣalāḥ : 1/74" in plain)

# 13. at-taʿammul ×3 (Q1/Q3 recouvrées)
chk("az-Zarqānī / Bayqūnīyya", "az-Zarqānī sur la Bayqūnīyya" in plain)
chk("Q1 blâmable (recouvrée)", "Pourquoi le tadlīs est-il blâmable" in plain)
chk("Q2 une seule fois", "qu’une seule fois" in plain)
chk("Q3 statut avec tarǧīḥ (recouvrée)", "avec la préférence (tarǧīḥ)" in plain)
chk("recouvrement image documenté", "furent recouvrées à l’image" in plain)

# 14. iʿdād qablī + bornes
chk("Q prép 1 šāḏḏ", "je définis le ḥadīṯ šāḏḏ" in plain)
chk("Q prép 2 différence munkar", "différence entre lui et le ḥadīṯ munkar" in plain)
chk("Q prép 3 statut acceptation/rejet", "quant à l’acceptation et au rejet" in plain)
chk("bornes p.85-90", "page imprimée 85 et s’achève en la page 90" in plain)
chk("leçon suivante p.91 šāḏḏ", "page 91 du même manuel" in plain)
chk("bannière dars 18 lue R594", "p.88-93" in plain)
chk("interdiction double rendu", "interdite de double rendu" in plain)
chk("aucune āya déclarée", "ne contient aucune āya" in plain)

# 15. hygiene typographique
chk("0 caractère arabe (hors ﷺ U+FDFA)", not re.search(r"[\u0600-\u06FF]", h.replace("\ufdfa", "")))
chk("ﷺ tenu", "\ufdfa" in h)
chk("0 apostrophe droite", "'" not in h.replace("&nbsp;", " "))

print()
print(f"RÉSULTAT verify-128 : {ok} PASS / {fail} FAIL")
sys.exit(1 if fail else 0)
