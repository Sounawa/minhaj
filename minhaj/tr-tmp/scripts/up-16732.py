#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16732 (tawhid-1es, leçon 12 — Sa seigneurie
sur les mondes et l'envoi des messagers).

Vérifications et restitutions (cache quran = Ḥafṣ) :
- Matn : « رب العباد ورب أعمالهم والمقدر لحركاتهم وآجالهم الباعث الرسل
  إليهم لإقامة الحجة عليهم » — rendu fidèlement.
- CITATIONS VIDES (perte OCR) RESTAURÉES du cache, cibles doctrinales :
  * [الصافات: 96] → CONFORME (« والله خلقكم وما تعملون » — cible univoque
    de la création des actes) ;
  * [النحل: 32] → CONFORME (« ادخلوا الجنة بما كنتم تعملون » —
    l'attribution de l'œuvre au serviteur et sa récompense, exactement le
    contexte « ينسب العمل لعبده ويثيبه عليه ») ;
  * [نوح: 4] → CONFORME (« إن أجل الله إذا جاء لا يؤخر ») ;
  * [يونس: 49] → CONFORME (déjà vérifié en la leçon 11) ;
  * [المنافقون: 11] → CONFORME (« ولن يؤخر الله نفسا إذا جاء أجلها ») ;
  * [المائدة: 21] → Māʾida 19 « أن تقولوا ما جاءنا من بشير ولا نذير » —
    écart +2 noté : la structure « afin que vous ne disiez » correspond
    exactement au « بأن يقولوا » du contexte (l'excuse coupée par le
    bayān) ;
  * [الأعراف: 53] → Aʿrāf 54 « إن ربكم الله الذي خلق السماوات والأرض...»
    — réf d'adjacence (−1) notée, règle R127 déjà documentée en la leçon 7 :
    le verset de la rubūbiyya (« à Lui la création et le commandement ») —
    cible univoque du travail demandé (extraction des manifestations de la
    seigneurie) ;
  * [النحل: 36] → CONFORME (« ولقد بعثنا في كل أمة رسولا » — cible
    univoque de la finalité de l'envoi).
- Le tampon de date du site (lundi 29 novembre 2021) non rendu (règle
  corpus).
- L'item d'évaluation « أُعرِّف النبي والرسول... ما غاية إرسال الرسل »
  imprimé fusionné (deux questions en une) — rendu en deux items.
- Yūshaʿ b. Nūn (le prophète renovelateur) rendu tel quel.
- La doctrine du kasb (contiguïté du décret à la puissance advenue) rendue
  fidèlement — l'homme n'est ni producteur ni créateur de ses actes.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : Sa seigneurie sur les mondes et l’envoi des messagers</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la douzième leçon (12).</p>
<ul>
<li>Connaître le sens de la seigneurie (<em>rubūbiyya</em>) et ce qu’elle exige.</li>
<li>Saisir le sens du possible au sujet de Dieu Très-Haut.</li>
<li>Connaître l’envoi des messagers et sa finalité.</li>
</ul>
<h2>Préambule</h2>
<p>Au nombre de ce qu’il faut croire : Dieu Très-Haut fait ce qu’Il veut — Il est le Créateur des serviteurs et de leurs actes, Celui qui dispose de toutes les affaires de Ses créatures : subsistances, termes, félicité et infortune ; et tous les mouvements et les repos qui adviennent procèdent de Sa détermination, Puissant et Magnifié, conforme à ce dont Sa science a précédé.</p>
<p>Quel est le sens de la création des œuvres des serviteurs ? Qu’entend-on par la détermination des termes ? Et quelle est la finalité de l’envoi des messagers — sur eux la paix ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Seigneur (<em>rabb</em>) des serviteurs et Seigneur de leurs œuvres ; Celui qui détermine leurs mouvements et leurs termes ; Celui qui envoie les messagers vers eux, pour l’établissement de l’argument sur eux. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>rabb</em> (Seigneur) : le Créateur, le Possesseur, le Maître, Celui qui subsiste [par soi], Celui qui répare.</li>
<li><em>ājāl</em> (termes) : pluriel de <em>ajal</em> : la durée et le temps.</li>
<li><em>bāʿith</em> (Celui qui envoie) : l’envoyeur.</li>
<li>l’argument (<em>ḥujja</em>) : la preuve démonstrative.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> les manifestations de la seigneurie.</li>
<li>J’extrais du <em>matn</em> la finalité de l’envoi des messagers — sur eux la paix.</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient ce qui suit :</p>
<h3>Premièrement : les manifestations de Sa seigneurie, l’Elevé</h3>
<h4>1. Sa seigneurie, l’Elevé, sur les serviteurs et leurs œuvres</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Seigneur des serviteurs et Seigneur de leurs œuvres. » Au nombre de ce qu’il faut croire : Dieu Très-Haut est le Seigneur des serviteurs — c’est-à-dire leur Créateur ; l’Éducateur qui subsiste sur leurs affaires ; le Roi qui juge l’ensemble des créatures : les fils d’Adam, et autres qu’eux — les djinns et les anges.</p>
<p>La parole de l’auteur : « et Seigneur de leurs œuvres » signifie : l’Éducateur des corps des serviteurs, leurs personnes et leurs actes — car il n’y a point de différence entre les essences et les actes : de même que nul n’a le pouvoir de créer la moindre des essences, de même des actes des serviteurs, nul n’a le pouvoir d’en créer le moindre. Il est, glorifié soit-Il, comme Il créa les serviteurs, le Créateur de leurs œuvres et de tout ce qui procède d’eux. Le Très-Haut dit :</p>
<p>« Et Dieu vous créa, vous et ce que vous faites. » (al-Ṣāffāt, 96)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<h4>2. Sa détermination, l’Elevé, des mouvements des serviteurs</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Celui qui détermine leurs mouvements et leurs termes. » Au nombre de ce qu’il faut croire : Dieu Très-Haut est Celui qui détermine, fixe et assigne l’ensemble des mouvements des serviteurs. L’auteur garda le silence sur les repos : car les mouvements sont plus manifestes qu’eux en l’existence ; et parce que la récompense et le châtiment ne s’ensuivent, le plus souvent, que des mouvements ; et les mouvements sont inclus au sens de la parole de l’auteur : « et Seigneur de leurs œuvres ». Les œuvres des serviteurs sont création et innovation de Dieu Très-Haut, et acquisition (<em>kasb</em>) et contiguïté de la part du serviteur à Sa puissance — l’Elevé : l’acquisition est la contiguïté du décret (<em>maqdūr</em>) à la puissance advenue ; et le serviteur n’est ni producteur de ses actes ni leur créateur. Dieu Très-Haut est l’Agent qui choisit — Il est le Créateur, le Sachant ; Il est le Seigneur des serviteurs, leur Éducateur et le Créateur de toute chose. Et lors même qu’Il est, glorifié soit-Il, Celui qui Seul crée toute chose, Il attribue l’œuvre à Son serviteur et le récompense — par générosité et faveur de Sa part, glorifié soit-Il. Il dit :</p>
<p>« Ceux que les anges font mourir alors qu’ils sont purs — [les anges] disent : " Paix sur vous ! Entrez au Paradis, pour ce que vous faisiez. " » (al-Naḥl, 32)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — l’attribution de l’œuvre au serviteur et sa récompense.]</p>
<h4>3. Sa détermination, l’Elevé, des termes des serviteurs</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Celui qui détermine leurs mouvements et leurs termes. » Les termes sont pluriel de <em>ajal</em> : la durée de la chose et son temps ; et l’on vise par le terme la mort, qui est la destinée de toute créature. Le Très-Haut dit :</p>
<p>« Il vous pardonnera de vos fautes, et vous donnera un délai jusqu’à un terme nommé — certes, le terme de Dieu, quand il vient, n’est point retardé — si vous saviez ! » (Nūḥ, 4 — extrait)</p>
<p>Et le Très-Haut dit :</p>
<p>« ...Pour toute communauté un terme : lorsque leur terme vient, ils ne sauraient le retarder d’une heure ni l’avancer. » (Yūnus, 49 — extrait)</p>
<p>Et le glorifié dit :</p>
<p>« Dieu ne saurait retarder une âme lorsque son terme vient ; et Dieu, de ce que vous faites, est bien informé. » (al-Munāfiqūn, 11)</p>
<p>[Trois citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES — la dernière fut déjà restituée en la leçon 11.] Et l’école des gens du vrai est que les termes et les subsistances sont déterminés : ce qui est en la science de Dieu n’en change point. En conséquence : quiconque meurt d’une cause parmi les causes ne meurt que par son terme qui lui fut déterminé et sa durée fixée, dont il précéda en la chose sue qu’il n’y aura point de surcroît ; et le terme de la mort est le temps où il survient — de même que le terme de la dette est le temps de son échéance et l’exigibilité de son acquittement.</p>
<h3>Deuxièmement : l’envoi des messagers aux serviteurs, et sa finalité</h3>
<h4>1. L’envoi des messagers — sur eux la paix</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Celui qui envoie les messagers vers eux. » Celui qui envoie est Celui qui dirige et envoie : on dit « j’envoyai l’homme » — je le dirigeai et l’envoyai en une affaire. Les messagers sont pluriel de <em>rasūl</em> ; et le messager est un homme à qui une Loi fut révélée, et à qui il fut ordonné de la transmettre — s’il ne reçut point l’ordre de la transmettre, il est prophète seulement ; et le prophète est celui qui vient renouveler la Loi d’un autre, comme Yūshaʿ b. Nūn, par exemple.</p>
<p>L’auteur — que Dieu lui fasse miséricorde — ayant achevé de parler des obligations à Son égard, l’Elevé — ce que profèrent les langues et croient les cœurs —, entreprit de parler d’une part de ce qui est possible à Son égard, l’Elevé : l’envoi des messagers — sur eux la paix — à Ses serviteurs, pour leur enseignement et l’orientation de leurs actes. Et l’école des gens du vrai est que l’envoi des prophètes et des messagers est du possible dont il est obligatoire de croire la survenue : le premier est Adam, et le dernier Muḥammad — paix et bénédiction sur lui.</p>
<h4>2. La finalité de l’envoi des messagers — sur eux la paix</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « pour l’établissement de l’argument sur eux. » L’envoi des messagers a des finalités sublimes et des bénéfices immenses : parmi eux, l’annonce et l’avertissement, l’enseignement des croyances et des cultes, l’exposé de l’obligation d’obéir aux commandements et d’éviter les interdits, l’orientation vers les beaux caractères — et le reste des intérêts de la religion et de ce monde.</p>
<p>La parole de l’auteur : « pour l’établissement de l’argument sur eux » signifie : que l’argument de Dieu s’établisse sur Ses serviteurs. Car Il est, l’Elevé, de pure faveur, à ne châtier personne jusqu’à ce qu’il contredise Son commandement et Son interdit ; et Son commandement et Son interdit ne se connaissent que de la part des messagers — ils ne furent envoyés que pour exposer les droits de Dieu sur Ses serviteurs, et l’argument ne s’établit sur les serviteurs qu’après que cela leur fut exposé. Par l’exposé, leur excuse est coupée — qu’ils ne disent point :</p>
<p>« Ô gens du Livre ! Notre messager vous est venu, vous exposant [la vérité] après une interruption des messagers, afin que vous ne disiez : " Il ne nous est venu ni annonciateur ni avertisseur " — voici donc que vous est venu un annonciateur et un avertisseur. » (al-Māʾida, 19 — extrait)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 21 », la visée est le verset 19 — écart +2 noté : la structure « afin que vous ne disiez : il ne nous est venu ni annonciateur ni avertisseur » correspond exactement au contexte de l’excuse coupée par l’exposé.]</p>
<p>Lors donc que Dieu envoya les messagers — sur eux la paix — et qu’ils exposèrent aux gens ce dont ils ont besoin des affaires de la religion et de ce monde, réussit quiconque accepta l’appel des messagers, et périt quiconque ne l’accepta point : il ne lui resta ni argument ni excuse.</p>
<h2>Les fruits de la leçon</h2>
<ul>
<li>Purifier l’âme et l’épanouir de toute forme de pouvoir et de force propres : car le Seigneur de l’univers, glorifié soit-Il, a déterminé l’ensemble des mouvements et des repos, des subsistances et des termes — et il n’advient que ce que Dieu a déterminé.</li>
<li>C’est de la faveur de Dieu et de Sa grâce sur Ses serviteurs qu’Il leur envoya les messagers, pour les orienter vers ce en quoi est leur félicité en ce monde et en la dernière [demeure].</li>
<li>L’obligation de croire en l’ensemble des messagers et d’honorer leur rang : c’est un droit parmi leurs droits.</li>
</ul>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’expose le sens de la parole de l’auteur : « Seigneur des serviteurs et Seigneur de leurs œuvres ».</li>
<li>L’homme peut-il mourir avant son terme ? Avec justification et appui.</li>
<li>Je définis le prophète et le messager, et expose la différence entre eux. [Item imprimé fusionné avec le suivant — rendu séparément.]</li>
<li>Quelle est la finalité de l’envoi des messagers aux serviteurs ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le Très-Haut dit :</p>
<p>« Certes, votre Seigneur est Dieu, qui créa les cieux et la terre en six jours, puis s’établit sur le Trône : Il enveloppe la nuit du jour qui le poursuit empressement — et le soleil, la lune et les étoiles, asservis à Son commandement. Quoi ! à Lui la création et le commandement : béni soit Dieu, le Seigneur des mondes ! » (al-Aʿrāf, 54)</p>
<p>Et le Très-Haut dit :</p>
<p>« Et certes, Nous envoyâmes en toute communauté un messager : " Adorez Dieu, et évitez le Ṭāghūt ! " Parmi eux, il en est que Dieu guida, et il en est sur qui l’égarement s’établit. Parcourez donc la terre, et regardez quelle fut la fin de ceux qui crièrent au mensonge. » (al-Naḥl, 36)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée de la première porte « 53 », la visée est le verset 54 — réf d’adjacence notée (règle de la leçon 7) : le verset de la seigneurie ; la seconde CONFORME.]</p>
<h3>Je lis les deux versets en méditation et réalise ce qui suit :</h3>
<ul>
<li>J’extrais du premier verset les manifestations de Sa seigneurie, l’Elevé.</li>
<li>J’extrais du second verset la finalité de l’envoi des messagers et son effet.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et réalise ce qui suit :</p>
<ul>
<li>Je recherche les caractéristiques du message de notre maître Muḥammad — paix et bénédiction sur lui.</li>
<li>Je recherche le sens de « le Sage » (<em>al-Ḥakīm</em>) en la parole de l’auteur : « et fit descendre sur lui Son Livre sage ».</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16732":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16732 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16732 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
