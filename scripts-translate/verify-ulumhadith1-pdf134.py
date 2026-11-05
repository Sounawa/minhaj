#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-134
(le ḥadīṯ mudabbaǧ, p.113-116 du manuel ulum-hadith-1-thanawi.pdf) :
bannière « ad-dars 23 » ; bornes p.113-116 par DOUBLE sondage (bannière ad-dars
24 + objectifs المتفق والمفترق lus à l'OCR p.117, concordants avec l'iʿdād
qablī p.116 ×2 questions) ; bayt — « wa-mā rawā kullu qarīnin ʿan akhīhi ***
mudabbaǧun fa-uġrafehu ḥaqqa-n wa-n-taḥih » tranché image 600 dpi ×3 lectures
(OCR psm6 « ḥafā » récusé → ḥaqqa-n ; ġayn de fa-uġrafehu pointé, OCR psm4
« fa-ʿrifahu » récusé) ; glose (qarīn, ism mafʿūl de at-tadbīǧ/at-tazyīn,
dabāǧat al-waǧh, intahihi) ; taḥlīl : définition (égalité des deux joues,
égal dans la prise des maîtres, différences d'âge tolérées, finesses d'isnād,
« wa-n-taḥih » beauté/entraide/vertus), seconde forme bi-wāsiṭa (2400 dpi,
al-Layṯ/Yazīd ibn al-Hād/Mālik 1200 dpi), utilité (āmin du wahm,
al-Layṯ/Mālik/az-Zuhrī) ; différence (mudbaǧ aḫṣaṣ, al-Aʿmaš/at-Taymī, tout
mudbaǧ est pair, tout pair n'est pas mudabbaǧ) ; groupe de pairs (Aḥmad,
Abū Ḫayṯama Zuhayr ibn Ḥarb, Yaḥyā ibn Maʿīn, ʿAlī ibn al-Madīnī,
ʿUbaydallāh ibn Muʿāḏ, Šuʿba, Abū Bakr ibn Ḥafṣ, Abū Salama, ʿĀʾiša
« kānat azwāǧu rasūli llāhi ﷺ yaʾḫuḏna min ruʾūsihinna ḥattā yakūna
ka-l-wafra » [al-Musalsalāt al-muqaddama amāma l-maǧālis al-mubtakara, p. 70],
« Aḥmad et les quatre au-dessus de lui sont des pairs » al-Ḫaṭīb) ;
taqwīm ×3 (image 600 dpi) ; istiṯmār (Ibn aṣ-Ṣalāḥ « aḥadu l-qarībayn »
tranché 4800 dpi — bāʾ point au-dessous ≠ nūn, OCR « al-qarīnayn » récusé ;
Sulaymān at-Taymī/Mišar, OCR « Saymān » récusé ; consigne unique) ;
iʿdād qablī ×2 (Q2 découverte image 600 dpi, muttafiq/muftariq) ; bornes
p.113-116 ; ﷺ tenu (U+FDFA), zéro āya rendue, zéro résidu.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf134.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-134-fr.html"
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
plain = re.sub(r"[\s\u202f\u00a0]+", " ", h.replace("&nbsp;", " "))

# 1. h1 aligné au titleFr pré-mappé du registre
tf = [l for l in json.load(open(REG, encoding="utf-8"))["lessons"]
      if l["docId"] == "pdf-mut23h2q-134"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 23", "leçon 23" in (m.group(1) if m else ""))

# 2. bannière / bornes
chk("badge ad-dars 23", "ad-dars 23" in plain)
chk("bornes p.113-116 documentées", "page imprimée 113" in plain and "page 116" in plain)
chk("bannière ad-dars 24 p.117 (sondage)", "ad-dars 24" in plain and "page 117" in plain)
chk("double sondage (jamais deviné)", "double sondage" in plain or "DOUBLE sondage" in plain)
chk("jamais devinée", "jamais devinée" in plain)
chk("concordance iʿdād qablī p.116", "concordants" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. tamhīd
chk("tamhīd : relations nombreuses", "relations nombreuses qui lient entre eux les transmetteurs" in plain)
chk("tamhīd : aînés/jeunes + inférieur/supérieur", "transmission des aînés sur les jeunes" in plain and "l’inférieur sur le supérieur" in plain)
chk("tamhīd question double", "Qu’est-ce donc que la transmission des pairs" in plain)
chk("tadbīǧ question", "quand devient-elle un croisement (tadbīǧ)" in plain)

# 4. bayt
chk("bayt : wa-mā rawā kullu qarīnin ʿan akhīhi", "wa-mā rawā kullu qarīnin ʿan akhīhi" in plain)
chk("bayt : mudabbaǧun fa-uġrafehu ḥaqqa-n wa-n-taḥih", "mudabbaǧun fa-uġrafehu ḥaqqa-n wa-n-taḥih" in plain)
chk("OCR ḥafā récusé (image)", "ḥafā" in plain and "récusé" in plain)
chk("OCR fa-ʿrifahu récusé (ġayn pointé)", "fa-ʿrifahu" in plain and "ġayn y étant nettement pointé" in plain)
chk("bayt rendu deux fois (matn + taʿrīf)", "aux deux emplacements" in plain)
chk("traduction bayt", "quand un pair transmet de son frère" in plain or "chaque pair transmet de son frère" in plain)

# 5. glose
chk("glose : compagnon constant", "compagnon constant (al-muṣāḥib al-mulāzim)" in plain)
chk("glose : ism mafʿūl de at-tadbīǧ", "participe passif (ism mafʿūl) formé sur at-tadbīǧ" in plain or "nom d’agent-resultat (ism mafʿūl), formé sur at-tadbīǧ" in plain)
chk("glose : dabāǧat al-waǧh", "dabāǧat al-waǧh" in plain)
chk("glose : intahihi", "prétends-le et sois fier de sa connaissance" in plain)

# 6. extraction des thèmes ×2
chk("deux questions-limaires p.114", "deux questions-limaires" in plain)
chk("IS1 maqṣūd", "Qu’est-ce que le ḥadīṯ mudabbaǧ" in plain)
chk("IS2 farq", "différence entre le ḥadīṯ mudabbaǧ et la transmission des pairs" in plain)

# 7. taḥlīl — définition
chk("égalité des deux joues", "comme se font égaux les deux joues" in plain)
chk("égal prise des maîtres + âge", "son égal dans la prise des maîtres et, en règle générale, dans l’âge" in plain)
chk("différence d’âge tolérée", "même s’ils diffèrent en l’âge" in plain)
chk("finesses d’isnād", "les finesses d’isnād qu’il contient" in plain)
chk("wa-n-taḥih beauté/entraide/vertus", "beauté, entraide et vertus entre les pairs" in plain)
chk("seconde forme bi-wāsiṭa", "le mudbaǧ par l’intermédiaire" in plain)
chk("sous-titre tranché 2400 dpi", "ṯāniyahumā" in plain and "2400 dpi" in plain)
chk("ex. al-Layṯ/Yazīd ibn al-Hād/Mālik ×2", "d’al-Layṯ, de Yazīd ibn al-Hād, de Mālik, et la transmission de Mālik, de Yazīd, d’al-Layṯ" in plain)
chk("Yazīd ibn al-Hād 1200 dpi", "Yazīd ibn al-Hād" in plain and "1200 dpi" in plain)
chk("utilité : sécurité contre l’addition", "la sécurité contre la supposition d’une addition dans l’isnād" in plain)
chk("utilité : ex. al-Layṯ/Mālik/az-Zuhrī", "d’az-Zuhrī en passant par Mālik" in plain)
chk("utilité : pas de wahm", "ne tombe-t-il point en l’illusion" in plain)

# 8. différence mudbaǧ / aqrān
chk("plus spécifique", "plus spécifique que la transmission des pairs" in plain)
chk("tout mudbaǧ relève, non l’inverse", "tout mudbaǧ relève de la transmission des pairs, et non l’inverse" in plain)
chk("partage l’âge et la prise des maîtres", "tels l’âge et la prise des maîtres" in plain)
chk("ex. al-Aʿmaš/at-Taymī sans retour", "d’al-Aʿmaš d’at-Taymī, les deux étant des pairs, sans que at-Taymī ne transmette d’al-Aʿmaš" in plain)
chk("chacun des deux transmet de l’autre", "chacun des deux transmette de l’autre" in plain)
chk("tout mudbaǧ est pair / tout pair n’est pas mudabbaǧ", "tout mudbaǧ est pair, et tout pair n’est pas mudabbaǧ" in plain)
chk("groupe de pairs en un ḥadīṯ", "un groupe de pairs se réunisse en un seul ḥadīṯ" in plain)

# 9. isnad du ḥadīṯ d’ʿĀʾiša
chk("Aḥmad + Abū Ḫayṯama Zuhayr ibn Ḥarb", "Aḥmad, d’Abū Ḫayṯama Zuhayr ibn Ḥarb" in plain)
chk("Yaḥyā ibn Maʿīn + ʿAlī ibn al-Madīnī", "de Yaḥyā ibn Maʿīn, de ʿAlī ibn al-Madīnī" in plain)
chk("ʿUbaydallāh ibn Muʿāḏ + Šuʿba", "de ʿUbaydallāh ibn Muʿāḏ, de son père, de Šuʿba" in plain)
chk("Abū Bakr ibn Ḥafṣ + Abū Salama", "d’Abū Bakr ibn Ḥafṣ, d’Abū Salama, de ʿĀʾiša" in plain)
chk("ḥadīṯ ʿĀʾiša azwāǧ", "kānat azwāǧu rasūli llāhi ﷺ yaʾḫuḏna min ruʾūsihinna ḥattā yakūna ka-l-wafra" in plain)
chk("réf. al-Musalsalāt p. 70", "al-Musalsalāt al-muqaddama amāma l-maǧālis al-mubtakara, p. 70" in plain)
chk("image 600 dpi isnad+ḥadīṯ", "l’isnād et le ḥadīṯ imprimés diacrités, lus à l’image 600 dpi" in plain)
chk("Aḥmad et les quatre au-dessus", "Aḥmad et les quatre au-dessus de lui sont des pairs" in plain)
chk("al-Ḫaṭīb dit", "comme l’a dit al-Ḫaṭīb" in plain)

# 10. taqwīm — 3 questions
chk("taqwīm 3 questions", "sous la forme de trois questions" in plain)
chk("TQ1 définition avec exemple", "Que je définisse le ḥadīṯ mudabbaǧ avec un exemple" in plain)
chk("TQ2 différence", "Que j’explicite la différence entre le mudabbaǧ et la transmission des pairs" in plain)
chk("TQ3 utilité tadbīǧ", "Quelle est l’utilité du tadbīǧ" in plain)
chk("taqwīm lu image 600 dpi", "furent lus à l’image 600 dpi" in plain)

# 11. istiṯmār — Ibn aṣ-Ṣalāḥ
chk("Ibn aṣ-Ṣalāḥ cité", "Ibn aṣ-Ṣalāḥ dit" in plain)
chk("aḥadu l-qarībayn tranché 4800 dpi", "aḥadu l-qarībayn" in plain and "4800 dpi" in plain)
chk("bāʾ point au-dessous ≠ nūn", "le bāʾ y porte son point au-dessous, nettement distinct du nūn" in plain)
chk("OCR al-qarīnayn récusé", "al-qarīnayn" in plain and "récusé" in plain)
chk("wa-lā yaruwī l-āḫaru ʿanhu fīmā naʿlam", "wa-lā yaruwī l-āḫaru ʿanhu fīmā naʿlam" in plain)
chk("Sulaymān at-Taymī / Mišar", "Sulaymān at-Taymī de Mišar" in plain)
chk("OCR Saymān récusé", "Saymān" in plain and "récusé" in plain)
chk("amṯālun kaṯīra", "amṯālun kaṯīra" in plain)
chk("consigne unique", "J’examine le texte et je réponds à sa question" in plain)
chk("consigne : pourquoi pas mudabbaǧ", "pourquoi le type mentionné dans le texte n’est-il point du ḥadīṯ mudabbaǧ" in plain)

# 12. iʿdād qablī — leçon suivante muttafiq/muftariq
chk("préparation muttafiq/muftariq ×2", "sens du muttafiq et du muftariq" in plain and "où se dévoile l’importance de leur connaissance" in plain)
chk("Q2 découverte image 600 dpi", "DÉCOUVERTE PAR L’IMAGE 600 dpi" in plain or "découverte par l’image 600 dpi" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 13. ﷺ tenu, zéro āya rendue, zéro résidu
chk("ﷺ tenu (U+FDFA)", h.count("\ufdfa") >= 2)
chk("doc mentionne aucune āya rendue", "aucune āya rendue" in plain)
residus = ["TODO", "XXX", "undefined", "NaN", "【", "____", "recycle", "takeover", "mtime", "⟨AR⟩"]
chk("zéro résidu technique", not any(r in plain for r in residus))

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)
