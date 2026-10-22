#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16715 (tawhid-1es, leçon 5 — la transcendance
divine à l'égard de l'embrassement de Son essence et de Sa science par la créature).

Vérifications et restitutions (cache quran = Ḥafṣ ; sunnah.com) :
- Matn : le passage fameux de la Risāla (« لا يبلغ كنه صفته الواصفون... وسع
  كرسيه السماوات والأرض ولا يؤوده حفظهما وهو العلي العظيم ») — rendu
  fidèlement (la fin reprend Baqara 255).
- CITATIONS VIDES (perte OCR — réfs imprimées seules) RESTAURÉES :
  * [فصلت: 52] → Fuṣṣilat 53 Ḥafṣ « سنريهم آياتنا في الآفاق وفي أنفسهم » —
    réf d'adjacence erronée (52→53, 6e du corpus) notée ;
  * [الصافات: 180] → Ṣāffāt 180 « سبحان ربك رب العزة عما يصفون » — CONFORME ;
  * [طه: 107] → Ṭā-Hā 110 Ḥafṣ « ولا يحيطون به علما » — la visée doctrinale
    (non-compassée de l'essence) ; la leçon suit un décalage −1 pour Ṭā-Hā
    (cf. leçon 7 : 4→5 et 7→8), ici l'écart est de 3 — noté ;
  * [الرحمن: 29] → Raḥmān 29 « كل يوم هو في شأن » — CONFORME ;
  * [البقرة: 254] → Baqara 255 = āyat al-Kursī — règle −1 déjà documentée
    (R96 : [البقرة: 28] imprimé = Ḥafṣ 29) — notée ;
  * [الغاشية: 17-20] → les 4 versets des signes — CONFORME ;
  * [الأنعام: 104] → Anʿām 104 « قد جاءكم بصائر من ربكم » — CONFORME.
- Hadith d'Abū Dharr (Kursī/anneau dans le désert) [صحيح ابن حبان بترتيب
  ابن بلبان 3/69] — rendu INTÉGRALEMENT tel qu'imprimé (réf rendue telle
  quelle) ; le hadith d'Ubayy sur la grandeur d'āyat al-Kursī (Muslim) est
  cité en l'exploitation de la leçon suivante.
- « فَأَيُّ مَا أَنْزَلَ اللهُ عَلَيْكَ أَعْظَمُ » : rendu tel qu'imprimé.
- FIX GT-ismes : « le trône de son fauteuil » → le Kursī/le Trône ;
  « ne le fatigue pas sa sauvegarde » → « ne L'accable point leur garde ».
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la transcendance divine à l’égard de l’embrassement de Son essence et de Sa science par la créature</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la cinquième leçon (5).</p>
<ul>
<li>Connaître le sens de la transcendance (<em>tanazzuh</em>) et de la sanctification (<em>taqdīs</em>) envers Dieu Très-Haut.</li>
<li>Saisir que l’embrassement (<em>iḥāṭa</em>) de Son affaire, Puissant et Élevé, est impossible.</li>
<li>Réaliser la grandeur du Créateur par la méditation de Ses créatures, l’Elevé.</li>
</ul>
<h2>Préambule</h2>
<p>La plupart des ashʿarites tinrent que la première obligation du redevable est la connaissance de Dieu Très-Haut ; et ce que l’on vise par la connaissance de Dieu est la connaissance de Ses attributs, qu’indiquent Ses signes, Puissant et Élevé, en les âmes et aux horizons, selon Sa parole :</p>
<p>« Nous leur montrerons Nos signes aux horizons et en eux-mêmes, jusqu’à ce qu’il leur soit manifeste que c’est la vérité. » (Fuṣṣilat, 53)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 52 », la visée est le verset 53 — réf d’adjacence erronée notée.] Ce que l’on vise par la connaissance obligatoire n’est pas la connaissance de la réalité de Son essence : car le survenu est, de par sa nature, trop court pour le sublime de ce rang.</p>
<p>Par quoi donc le croyant connaît-il son Seigneur ? Et de quoi les penseurs tirent-ils considération ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Les décrivants n’atteignent point la réalité (<em>kunh</em>) de Son attribut, et les méditants n’embrassent point Son affaire. Les méditants tirent considération de Ses signes, et ne méditent pas la quiddité (<em>māhiyya</em>) de Son essence ; ils n’embrassent de Sa science rien, sinon ce qu’Il a voulu. Son Kursī embrasse les cieux et la terre, et leur garde ne L’accable point — et Il est le Très-Haut, l’Immense. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>kunh</em> (la réalité) : la réalité (<em>ḥaqīqa</em>) d’une chose.</li>
<li><em>yaʿtabiru</em> (tire considération) : médite et tire leçon.</li>
<li><em>māhiyya</em> (la quiddité) : avec yāʾ redoublé — l’hamza peut s’échanger en hāʾ (māhiya) ; c’est-à-dire : la réalité.</li>
<li><em>lā yaʾūduhu</em> (ne L’accable point) : ne L’appesantit point et ne L’ennuie point.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> ce que les décrivants de Dieu Très-Haut ne peuvent atteindre.</li>
<li>J’extrais du <em>matn</em> quelques manifestations de la grandeur de Dieu Très-Haut.</li>
<li>J’extrais du <em>matn</em> la grandeur de la science du Créateur, Puissant et Élevé.</li>
</ul>
<p>La leçon contient les axes suivants :</p>
<h3>Premièrement : l’impossibilité de saisir la réalité des attributs de Dieu Très-Haut</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Les décrivants n’atteignent point la réalité de Son attribut. » La connaissance des attributs divins, et la saisie de leurs réalités telles qu’elles sont, n’ont pour nous nulle voie ; et nul indice ne nous en fut dressé : car les intelligences sont impuissantes à saisir leur réalité — les intelligences ont une limite et une fin, et n’embrassent point ce qui est sans fin. Quiconque connaît ce qui lui est dû, et confesse son impuissance sur ce qui est au-delà, a rendu le vrai à qui de droit et mis l’équité en son lieu.</p>
<p>La parole de l’auteur : « la réalité (<em>kunh</em>) » — il se peut que l’on vise par <em>kunh</em> la réalité (<em>ḥaqīqa</em>) : les décrivants ne saisissent donc pas la réalité de Son attribut ; et il se peut que l’on vise par <em>kunh</em> la limite (<em>ghāya</em>) — le sens étant : il n’est pas de limite à Ses attributs, que les décrivants puissent atteindre. Et la preuve en est Sa parole :</p>
<p>« Gloire à ton Seigneur, le Seigneur de la puissance, au-dessus de ce qu’ils décrivent ! » (al-Ṣāffāt, 180)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Et le fait que l’auteur s’en tienne à l’attribut montre que, si nous n’atteignons pas les réalités des attributs qu’indiquèrent Ses actes, notre non-saisie de la réalité de Son essence, l’Elevé — qu’indiquèrent Ses attributs — est à plus forte raison. Et c’est ce qu’indique Sa parole :</p>
<p>« Il sait ce qui est devant eux et ce qui est derrière eux : ils n’en cernent point la science. » (Ṭā-Hā, 110 — extrait)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 107 », la visée doctrinale est « ...ils n’en cernent point la science » (Ṭā-Hā 110 Ḥafṣ) — la leçon suit un décalage −1 pour Ṭā-Hā (cf. leçon 7 : 4→5 et 7→8), ici l’écart est de 3 : noté.]</p>
<h3>Deuxièmement : l’impossibilité que les méditants embrassent Son affaire</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Et les méditants n’embrassent point Son affaire. Les méditants tirent considération de Ses signes, et ne méditent pas la quiddité de Son essence. » Au nombre de ce qu’il faut croire : Dieu Très-Haut — les méditants et les contemplateurs n’embrassent point Son affaire et Sa dispensation, quelque effort et application qu’ils fournissent ; selon Sa parole :</p>
<p>« Ceux qui sont dans les cieux et la terre L’interrogent ; chaque jour, Il est en une affaire. » (al-Raḥmān, 29)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.] — c’est-à-dire : chaque jour, Il est, Puissant et Élevé, en une affaire : donner la vie et donner la mort, honorer et humilier, appauvrir et enrichir, et le reste des dispensations divines. Le sens en est que les gens de pensée et de considération ne parviennent pas à embrasser Son affaire qui court en Sa création, ni n’atteignent l’embrassement de ce qui est de Sa dispensation, Puissant et Élevé : s’ils parviennent à Le connaître, c’est du côté de l’établissement et de la transcendance, non du côté de l’embrassement et de la détermination. Si le serviteur était chargé d’embrasser Son essence, il n’y pourrait.</p>
<p>Voici son ouïe, sa vue, son intelligence, son esprit, son existence et son agir : il ne peut les embrasser — comment donc l’affaire de son Créateur, l’Elevé ? Notre Seigneur, Puissant et Majestueux, est trop saint pour que les méditants L’embrassent. « Et ils n’embrassent de Sa science rien, sinon ce qu’Il a voulu. »</p>
<h3>Troisièmement : quelques manifestations de Sa grandeur, Puissant et Élevé</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — cite Sa parole :</p>
<p>« Dieu — il n’est de dieu que Lui, le Vivant, le Subsistant. Ni somnolence ni sommeil ne Le saisissent. À Lui ce qui est dans les cieux et ce qui est dans la terre... Son Kursī embrasse les cieux et la terre, et leur garde ne L’accable point — et Il est le Très-Haut, l’Immense. » (al-Baqara, 255 — āyat al-Kursī, extraits)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 254 », le verset du Kursī est 255 Ḥafṣ — règle −1 de la Baqara déjà documentée (R96 : [البقرة: 28] imprimé = Ḥafṣ 29), notée.]</p>
<p>Le Kursī est une créature immense parmi les créatures de Dieu, Puissant et Élevé ; et le Trône est plus grand que lui. Les cieux et la terre, auprès du Kursī, sont comme un anneau jeté dans un désert de la terre ; et le Kursī, auprès du Trône, est comme un anneau jeté dans un désert. D’Abū Dharr — que Dieu l’agrée — : « Je dis : ô Messager de Dieu, quelle est la plus grande de ce que Dieu fit descendre sur toi ? Il dit : le verset du Kursī. Puis il dit : ô Abū Dharr, les sept cieux, auprès du Kursī, ne sont que comme un anneau jeté en une terre déserte ; et la prééminence du Trône sur le Kursī est comme la prééminence du désert sur l’anneau. » [Ṣaḥīḥ d’Ibn Ḥibbān, ordonné par Ibn Balbān : 3/69 — citation intégrale et conforme ; réf rendue telle qu’imprimée.]</p>
<p>Et le sens de : « leur garde ne L’accable point » — Sa garde des deux et la dispensation de leur affaire ne L’appesantissent point ni ne L’ennuient, par la perfection de Sa puissance et l’universalité de Son agir en toute chose, au commencement et durablement : toute chose subsiste par Dieu.</p>
<p>Et le sens de : « et Il est le Très-Haut, l’Immense » — le Très-Haut (<em>al-ʿAlī</em>) : par le rang, le Grand au-dessus de Sa création en Son essence, Ses attributs et Ses noms, trop saint pour que L’embrasse description d’un décrivant ou connaissance d’un connaissant ; et l’Immense (<em>al-ʿAẓīm</em>) : le Grand au rang, le Haut à la description, auprès de Qui toute chose devient petite quand Sa grandeur est mentionnée.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’expose le motif de l’impossibilité d’embrasser la réalité des attributs du Créateur, en l’appuyant du Coran.</li>
<li>J’expose ce qui est permis et ce qui ne l’est pas de la méditation de l’affaire de Dieu et de Sa dispensation.</li>
<li>Qu’entend-on par le <em>Kursī</em> en Sa parole — [al-Baqara : 254, réf imprimée] ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le Très-Haut dit :</p>
<p>« Ne considèrent-ils pas les chameaux : comment ils furent créés ? Et le ciel : comment il fut élevé ? Et les montagnes : comment elles furent dressées ? Et la terre : comment elle fut étendue ? » (al-Ghāshiya, 17-20)</p>
<p>Et le Très-Haut dit :</p>
<p>« Des lumières de votre Seigneur vous sont déjà venues. Celui qui voit, c’est en sa faveur ; et celui qui s’aveugle, c’est à son détriment — et je ne suis pas gardien sur vous. » (al-Anʿām, 104)</p>
<p>[Citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.] Je médite les premières [versets] et m’y arrête à quelques manifestations de la grandeur de Dieu Très-Haut. Je médite le second, aidé des livres d’exégèse, et relie sa fin à son commencement.</p>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et réalise ce qui suit : j’en extrais les noms de Dieu qu’il contient ; et je recherche le sens de ces noms après les avoir extraits.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16715":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16715 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16715 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
