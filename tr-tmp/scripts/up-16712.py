#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16712 (tawhid-1es, leçon 3 — la science
du Tawḥīd : sa définition et son importance).

Vérifications et restitutions :
- Matn : fin de la khutba de la Risāla (« وقد فرض الله سبحانه على القلب
  عملا من الاعتقادات... ») — rendu fidèlement ; « وإياه نستخير » rendu
  « c'est à Lui que nous demandons le choix » (istikhhār).
- Définition canonique d'al-Ījī [المواقف 1/31 بتصرف] — CONFORME (mawāqif
  d'al-Ījī : « علم يقتدر به على إثبات العقائد الدينية المكتسبة من
  أدلتها اليقينية ») — rendue telle quelle avec la réf imprimée.
- QUATRE CITATIONS VIDES (perte OCR — réfs imprimées seules) RESTAURÉES du
  corpus canonique : al-Naḥl 51 (« Ne prenez pas deux dieux... »),
  Muḥammad 19 (« Sache donc qu'il n'est de dieu que Dieu... »),
  al-Anbiyāʾ 25 (« Et Nous n'avons envoyé avant toi nul messager... »),
  al-Baqara 132 (« Et Abraham en fit l'injonction à ses fils... ») —
  chacune notée.
- Tamhīd : « ومنهم الإمام ابن أبي زيد القيرواني في مقدمة رسالته؟ » —
  le « ؟ » est un artefact OCR (point attendu) — rendu en point.
- « الإعدادي القبلي » (titre imprimé de l'iʿdād) = coquille pour
  « الإعداد القبلي » — rendu « La préparation préalable », noté.
- « أبى محمد » (ISTITMĀR, coquille pour أبي محمد) — rendu normalement.
- Qāḍī ʿAbd al-Wahhāb [شرح عقيدة... ص 7] : citation INTÉGRALE —
  « مالك الصغير » rendu « le petit Mālik » (Mālik al-aṣghar/al-ṣaghīr,
  les deux graphies transmises — l'imprimé de la leçon 1 porte
  « Mālik al-aṣghar »).
- FIX GT-ismes : « la théologie speculative » → registre savant ; « la
  religion est prise de dana yadin s'il obéit » → rendu morphologique
  correct ; « mill a » (ملة) = l'imlāʾ de l'ange au messager — folk
  étymologie imprimée conservée et rendue.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>La science du Tawḥīd : sa définition et son importance</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la troisième leçon (3), portant sur la définition de la science du Tawḥīd et son importance.</p>
<ul>
<li>Connaître le sens du Tawḥīd, au sens propre et au sens technique.</li>
<li>Distinguer entre : le Tawḥīd, le credo (<em>ʿaqīda</em>) et la science du kalām.</li>
<li>Saisir l’importance du credo en la droiture de l’individu et la réforme de la société.</li>
</ul>
<h2>Préambule</h2>
<p>Le fondement de la droiture de l’individu est la santé de son credo et la force de sa foi ; et c’est pourquoi les savants de la communauté prirent soin du credo : ils composèrent en la matière des livres propres, et certains consacrèrent une part de leurs ouvrages au discours sur le credo et la science du Tawḥīd — parmi eux l’imam Ibn Abī Zayd al-Qayrawānī, en l’introduction de sa <em>Risāla</em>.</p>
<ul>
<li>Qu’entend-on par la science du Tawḥīd ?</li>
<li>Et quelle est la différence entre le Tawḥīd et le credo ?</li>
<li>Et quelle est l’importance du credo en la droiture de l’individu et la réforme de la société ?</li>
</ul>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Certes, Dieu, Puissant et Élevé, a imposé au cœur une œuvre, en fait de croyances (<em>iʿtiqādāt</em>), et aux membres apparents une œuvre, en fait d’obéissances. Je détaillerai pour toi ce que je t’ai promis d’en mentionner, chapitre par chapitre, pour qu’il soit à la portée de la compréhension de ses apprentis, s’il plaît à Dieu Très-Haut. C’est à Lui que nous demandons le choix (<em>istikhhār</em>), et par Lui que nous demandons secours ; il n’est de force ni de puissance qu’en Dieu, le Très-Haut, l’Immense. Et que Dieu prie sur notre maître Muḥammad, Son prophète, ainsi que sur sa famille et ses compagnons, et les salue d’un salut abondant. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>iʿtiqādāt</em> (les croyances) : de <em>iʿtaqada yaʿtaqidu iʿtiqādan</em> — croire d’une croyance, c’est-à-dire tenir pour vrai d’une adhésion ferme.</li>
<li><em>jawāriḥ</em> (les membres) : pluriel de <em>jāriḥa</em>, qui sont les organes : l’œil est un organe, la main est un organe, et ainsi de suite.</li>
</ul>
<h3>L’extraction des contenus</h3>
<ul>
<li>J’extrais du <em>matn</em> ce qui fut imposé au cœur et aux membres.</li>
</ul>
<p>La leçon contient les axes suivants :</p>
<h3>Premièrement : la définition de la science du Tawḥīd et son importance</h3>
<h4>1. La définition de la science du Tawḥīd</h4>
<p>Au sens propre : la science que la chose est une. En la Loi, elle est nommée science du Tawḥīd, science des principes de la religion (<em>uṣūl al-dīn</em>) et science du kalām ; et elle est : la science par laquelle on est capable d’établir les doctrines religieuses, acquises (<em>muktasaba</em>) de leurs preuves certaines. [Les <em>Mawāqif</em> de ʿAḍud al-Dīn al-Ījī : 1/31, adapté — réf imprimée CONFORME.]</p>
<p>C’est une science qui traite des questions de la croyance — comme la survenance du monde — pour parvenir à la connaissance de l’existence de Dieu, de ce qui Lui est dû, de ce qui Lui est impossible et de ce qui Lui est possible, parmi les attributs ; de même que ce qui est dû aux envoyés, ce qui leur est possible et ce qui leur est impossible — jusqu’à d’autres réalités rapportées (<em>samʿiyyāt</em>) : la foi aux anges, aux livres célestes, aux états du retour, de ce en quoi aboutira l’affaire des deux pesants (<em>al-thaqalān</em>) — félicité et infortune, châtiment et délice. Comme elle se nomme science du Tawḥīd, elle se nomme aussi science des principes de la religion, science du kalām et Grand Droit (<em>al-fiqh al-akbar</em>). Elle est des plus nobles sciences et des plus hautes.</p>
<h4>2. L’importance de la science du Tawḥīd</h4>
<p>La science du Tawḥīd a un rang éminent : car sa fin est la connaissance de l’existence du Créateur, Puissant et Élevé, et le fait qu’Il soit paré de l’ensemble des attributs de perfection, de beauté et de majesté. Et le Tawḥīd a un effet sur la droiture de l’individu et la réforme de la société humaine : car la santé des œuvres dépend de la droiture du credo, et parce que le credo est l’appui ferme et le fondement solide sur lequel se dresse l’édifice de l’islam — sans lui, ses piliers ne se dressent pas et son ordre ne se tient pas. C’est pourquoi le Coran prit un soin extrême à réformer le credo, en enraciner les racines et le purifier des illusions et des doutes : le credo correct est celui qui offre à l’homme l’explication correcte de l’existence humaine ; et la déviation du credo entraîne la corruption du comportement social.</p>
<p>Et Dieu, Puissant et Élevé, guida tout redevable à L’unifier et à savoir que son Créateur et Pourvoyeur est un, sans associé ; le Très-Haut dit :</p>
<p>« Et Dieu dit : “ Ne prenez pas deux dieux — [il n’en est qu’]Un. Certes, Il est un dieu unique : craignez-Moi donc. ” » (al-Naḥl, 51)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée seule.]</p>
<h3>Deuxièmement : la notion de credo (<em>ʿaqīda</em>)</h3>
<p><em>ʿAqīda</em> est un schème <em>faʿīla</em> au sens de <em>mafʿūla</em> — “ chose nouée ” (<em>maʿqūda</em>) ; son pluriel est <em>ʿaqāʾid</em>. Et ce sont : les matières que le redevable doit tenir pour vraies d’une adhésion ferme, qui apaise son cœur et où son âme se repose, jusqu’à ce qu’elles soient chez lui certitude (<em>yaqīn</em>) — que n’ébranle aucun doute et où ne s’infiltre nulle illusion —, comme si le croyant en avait rendu le nœud ferme et l’avait nouées à son cœur, au point qu’elles soient chez lui nouées, sans qu’il soit voie de les dénouer par quelque moyen de mise en doute que ce soit.</p>
<p>Et les credos religieux sont ceux rapportés à la religion par laquelle nous “ dînons ” Dieu et nous inclinons à Lui. Elle se nomme aussi <em>mill a</em> (religion), en tant que l’ange la dicte (<em>yumlīhā</em>) au messager, et le messager la dicte à la communauté ; elle se nomme aussi Loi et <em>sharīʿa</em>, parce que Dieu nous l’a léguée ; et elle se nomme aussi la voie droite (<em>ṣirāṭ mustaqīm</em>).</p>
<p>Le noble Coran a traité les questions du credo, exposé ses principes, les a établis et affermi ses règles. Le Très-Haut dit :</p>
<p>« Sache donc qu’il n’est de dieu que Dieu, et demande pardon pour ton péché, ainsi que pour les croyants et les croyantes ; et Dieu connaît vos allées et venues et votre demeure. » (Muḥammad, 19)</p>
<p>Et le Puissant, le Majestueux, dit :</p>
<p>« Et Nous n’avons envoyé avant toi nul messager, sans lui révéler : “ Il n’est de dieu que Moi : adorez-Moi donc. ” » (al-Anbiyāʾ, 25)</p>
<p>Et dit le Puissant, le Parleur :</p>
<p>« Et Abraham en fit l’injonction à ses fils, ainsi que Jacob : “ Ô mes fils ! Certes, Dieu vous a choisi la religion : ne mourez donc qu’en état de soumission. ” » (al-Baqara, 132)</p>
<p>[Trois citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées seules.]</p>
<p>Les principes des credos et leurs détails se trouvent donc dans le noble Coran ; et la Sunna purifiée a, elle aussi, sa part ample en la détaillée exposition de maintes matières du credo.</p>
<p>[Au nombre] des fins de la science du Tawḥīd : connaître le Créateur, Puissant et Élevé, par Ses noms et Ses attributs, à travers les signes qu’Il a dressés en les âmes et aux horizons ; et élever le croyant à la sincérité de l’adoration rendue au Créateur, Puissant et Élevé, pour obtenir la félicité d’ici-bas et de l’au-delà par l’obtention de l’agrément de Dieu et de Sa miséricorde.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Je définis la science du Tawḥīd.</li>
<li>Je mentionne les noms de la science du Tawḥīd, et pourquoi ses noms se multiplièrent.</li>
<li>J’expose l’importance de la science du Tawḥīd.</li>
<li>Quel est le rang de la science du Tawḥīd parmi les sciences religieuses ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le cadi ʿAbd al-Wahhāb dit : « Certes, le credo de l’imam Abū Muḥammad ʿAbd Allāh b. Abī Zayd al-Qayrawānī — surnommé le petit Mālik (<em>Mālik al-ṣaghīr</em>) — est un credo aux repères clairs, aux preuves lumineuses, aux constructions saines, aux fins et aux sens purs : il en fit l’ouverture de son livre fameux nommé la <em>Risāla</em>, qu’il dressa sur la proposition de son disciple vertueux, le shaykh Muḥriz b. Khalaf al-Bukrī. » [Le commentaire du credo de l’imam Ibn Abī Zayd al-Qayrawānī, de l’imam le cadi ʿAbd al-Wahhāb : p. 7 — citation intégrale et conforme.]</p>
<p>Je contemple le texte et réalise ce qui suit : je mentionne quelques traits distinctifs de la <em>Risāla</em>.</p>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<ul>
<li>Je mémorise, de la parole de l’auteur : “ Chapitre de ce que prononcent les langues... ” jusqu’à : “ ...ni à Sa postériorité d’achèvement ”.</li>
<li>En quoi croit le cœur, et que prononce la langue ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16712":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16712 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16712 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
