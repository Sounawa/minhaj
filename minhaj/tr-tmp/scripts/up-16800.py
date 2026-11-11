#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16800 (tawhid-1es, leçon imprimée 24 —
la hiérarchie des générations et la supériorité des califes bien guidés).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations :
- 2 citations vides (perte OCR systématique CMS) :
  Āl ʿImrān 110 CONFORME (كنتم خير أمة — l'ancre de l'excellence de la
  communauté/génération) ; Fatḥ 18 CONFORME (لقد رضي الله عن المؤمنين إذ
  يبايعونك تحت الشجرة — l'agrément divin des gens de l'allégeance de
  al-Ḥudaybiyya, exactement visés par le propos).
- 2 hadiths VÉRIFIÉS sunnah.com :
  ʿImrān b. Ḥuṣayn « خيركم قرني » = Bukhārī 6695, Kitāb al-Aymān wa-l-Nudhūr,
  bāb إثم من لا يفي بالنذر EXACT (narré par Ẓahdam b. Mudarrib) — texte
  VÉRIFIÉ CONFORME MOT À MOT sur sunnah.com, réserve d'ʿImrān (« je ne sais
  s'il mentionna deux ou trois ») incluse ;
  Anas « أنت مع من أحببت » = Bukhārī 3688, Kitāb Faḍāʾil al-Ṣaḥāba, bāb
  مناقب عمر بن الخطاب EXACT — CONFORME avec variantes mineures (« qu'as-tu
  préparé » vs وَمَاذَا أَعْدَدْتَ ; l'addition « après l'islam » suit
  l'imprimé).
- Doctrines rendues au plus près : la hiérarchie des trois générations (le
  qarn = cent ans, l'avis le plus solide) ; la lecture de 3:110 (interpella-
  tion de vive voix / l'ensemble de la communauté) ; les degrés d'excellence
  des Compagnons (Ḥudaybiyya > Badr > les Dix > les Quatre) ; l'intégrité
  (ʿadāla) par la certification divine et le choix ; l'étymologie du califat
  (succéder dans les jugements) ; les quatre notices (noms, kunya, surnoms,
  durées, âges) ; la justification du titre de commandeur des croyants.
- OCR/artefacts : dl/dt/dd vides + <p> vides + écho du titre en queue + divs
  vides — artefacts non rendus.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la hiérarchie des générations et la supériorité des califes bien guidés</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingt-quatrième leçon (24).</p>
<ul>
<li>Connaître la hiérarchie des générations et la cause de l’excellence de la génération du Prophète ﷺ et de ses Compagnons.</li>
<li>Saisir la supériorité des califes bien guidés.</li>
<li>Prendre pour modèle la conduite des califes bien guidés.</li>
</ul>
<h2>Préambule</h2>
<p>Parmi les choses auxquelles nous croyons : le Prophète ﷺ fut envoyé aux hommes tous ensemble, annonciateur et avertisseur ; et il ﷺ transmit le message, acquitta le dépôt et conseilla la Communauté, jusqu’à ce que lui vînt la certitude — il rejoignit alors le Compagnon suprême (<em>al-Rafīq al-Aʿlā</em>), laissant derrière lui une génération de Compagnons qui portèrent après lui la charge de la transmission de la religion aux mondes — et, en leur troupe, les quatre califes ; après eux, les Suivants (<em>tābiʿūn</em>) et les suiveurs des Suivants avec bonté — les générations préférées.</p>
<p>Quelles sont les générations préférées ? Et en quoi consiste la supériorité des califes bien guidés ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que la meilleure des générations est la génération de ceux qui virent le Messager de Dieu ﷺ et crurent en lui ; puis ceux qui les suivent ; puis ceux qui les suivent. Et les meilleurs des Compagnons sont les califes bien guidés, guidés dans la droite voie : Abū Bakr, puis ʿUmar, puis ʿUthmān, puis ʿAlī — que Dieu les agrée tous. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>yalūnahum</em> (ceux qui les suivent) : ils viennent après eux, sans séparation.</li>
<li><em>al-mahdiyyūn</em> (guidés dans la droite voie) : les droits, droits en leur conduite.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> la meilleure des générations.</li>
<li>Je dégage du <em>matn</em> la supériorité des califes bien guidés.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon embrasse les axes suivants :</p>
<h3>Premièrement : la supériorité des trois premiers siècles de l’ère prophétique</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que la meilleure des générations est la génération de ceux qui virent le Messager de Dieu ﷺ et crurent en lui ; puis ceux qui les suivent ; puis ceux qui les suivent. » Ce qu’il faut tenir pour vrai : le meilleur des siècles et des temps est le temps où se trouvèrent les croyants qui virent le Messager de Dieu ﷺ, crurent en lui, le vérifièrent, le suivirent et le soutinrent — selon la parole de Dieu Très-Haut :</p>
<p>« Vous êtes la meilleure communauté qu’on ait fait surgir pour les hommes : vous ordonnez le convenable, interdisez le blâmable et croyez en Dieu… » (Āl ʿImrān, 110)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — « la meilleure communauté », l’ancre de l’excellence de la génération.] Le sens : Dieu n’a pas fait surgir des hommes une communauté meilleure que la communauté de Muḥammad ﷺ. Il fut dit : Dieu les interpella par une parole de vive voix ; il fut dit : ce qui est visé, c’est l’ensemble de sa communauté.</p>
<p>On a divergé sur la mesure du siècle (<em>qarn</em>) — plusieurs avis, dont le plus solide : cent années. La meilleure des générations est donc la génération des Compagnons ; puis la génération de ceux qui les suivent — les Suivants (<em>tābiʿūn</em>), qui virent les Compagnons ; puis la génération de ceux qui les suivent — les suiveurs des Suivants (<em>atbāʿ al-tābiʿīn</em>). D’après ʿImrān b. Ḥuṣayn — que Dieu l’agrée — : le Messager de Dieu ﷺ a dit : « Les meilleurs d’entre vous êtes ma génération, puis ceux qui les suivent, puis ceux qui les suivent — dit ʿImrān : je ne sais s’il mentionna deux ou trois [générations] après la sienne — ; puis viennent des gens qui font des vœux et ne s’en acquittent pas, trahissent et ne sont pas dignes de confiance, témoignent sans être appelés à témoigner ; et l’embonpoint paraîtra parmi eux. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Aymān wa-l-Nudhūr, bāb de la faute de qui ne s’acquitte pas du vœu — bāb imprimé EXACT (hadith 6695, d’ʿImrān b. Ḥuṣayn — narré par Ẓahdam b. Mudarrib) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com, la réserve d’ʿImrān incluse.]</p>
<p>La parole de l’auteur : « puis ceux qui les suivent ; puis ceux qui les suivent » — sur ces générations pivote la religion, et par elles se fait la prise de modèle.</p>
<h3>Deuxièmement : les degrés des Compagnons — que Dieu les agrée — en excellence</h3>
<h4>1. La supériorité des Compagnons — que Dieu les agrée</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et les meilleurs des Compagnons sont les califes bien guidés, guidés dans la droite voie. » Ce qu’il faut tenir pour vrai, catégoriquement : les meilleurs de cette communauté sont les Compagnons de notre Prophète Muḥammad ﷺ — tous intègres (<em>ʿudūl</em>), par la certification que Dieu Très-Haut en fit, et par le choix qu’ils firent de la compagnie du Messager de Dieu ﷺ. Les meilleurs des Compagnons : les gens de al-Ḥudaybiyya, qui lui prêtèrent le serment d’allégeance — que Dieu les agrée ; sur leur supériorité, Dieu Très-Haut dit :</p>
<p>« Dieu a très certainement agréé les croyants quand ils t’ont prêté le serment d’allégeance sous l’arbre : Il a su ce qu’il y avait dans leurs cœurs, et a fait descendre sur eux la quiétude… » (al-Fatḥ, 18)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — l’agrément divin des gens de l’allégeance sous l’arbre, exactement visés par le propos.] Les meilleurs des gens de al-Ḥudaybiyya : les gens de Badr ; les meilleurs des gens de Badr : les dix annoncés du Paradis — Abū Bakr, ʿUmar b. al-Khaṭṭāb, ʿUthmān b. ʿAffān, ʿAlī b. Abī Ṭālib, Ṭalḥa b. ʿUbayd Allāh, al-Zubayr b. al-ʿAwwām, Saʿd b. Abī Waqqāṣ, Saʿīd b. Zayd, ʿAbd al-Raḥmān b. ʿAwf et Abū ʿUbayda ʿĀmir b. al-Jarrāḥ ; les meilleurs des dix : les quatre califes bien guidés. Ils furent nommés califes (<em>khulafāʾ</em>) parce qu’ils succédèrent au Messager de Dieu ﷺ dans les jugements.</p>
<h4>2. La supériorité des califes bien guidés</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Abū Bakr, puis ʿUmar, puis ʿUthmān, puis ʿAlī — que Dieu les agrée tous. » Eux sont les califes bien guidés :</p>
<ul>
<li>1. Abū Bakr al-Ṣiddīq — que Dieu l’agrée —, de nom ʿAbd Allāh b. Abī Quḥāfa. On lui prêta le serment d’allégeance pour le califat le jour même de la mort du Prophète ﷺ, par le consensus des Compagnons. La durée de son califat : deux ans, trois mois et trois jours. Il mourut à l’âge du Prophète ﷺ : soixante-trois ans.</li>
<li>2. ʿUmar b. al-Khaṭṭāb — que Dieu l’agrée —, <em>kunya</em> Abū Ḥafṣ, surnommé al-Fārūq. Il reçut le califat par la désignation qu’en fit Abū Bakr al-Ṣiddīq — que Dieu l’agrée —, et les Compagnons convinrent de son califat. La durée de son califat : dix ans, six mois et cinq nuits ; son âge : celui d’Abū Bakr. Il fut le premier à porter le titre de commandeur des croyants (<em>amīr al-muʾminīn</em>).</li>
<li>3. ʿUthmān b. ʿAffān — que Dieu l’agrée —, surnommé l’homme aux deux lumières (<em>Dhū l-Nūrayn</em>) : il épousa les deux filles du Messager de Dieu ﷺ, Ruqayya et Umm Kulthūm, l’une après la mort de l’autre. Il reçut le califat après ʿUmar b. al-Khaṭṭāb — que Dieu l’agrée. La durée de son califat : douze ans moins douze jours.</li>
<li>4. ʿAlī b. Abī Ṭālib — que Dieu l’agrée —, de <em>kunya</em> Abū l-Ḥasan ; le Prophète ﷺ lui donna la <em>kunya</em> d’Abū Turāb. La durée de son califat : quatre ans et neuf mois.</li>
</ul>
<p>Les hadiths rapportés des mérites (<em>manāqib</em>) des califes bien guidés sont nombreux, attestant la hauteur de leur rang, la grandeur de leur station et les beautés de leur caractère.</p>
<h2>Les fruits de la leçon</h2>
<ul>
<li>Mettre en relief la station des Compagnons — que Dieu les agrée — en général, et la supériorité des quatre califes en particulier : les aimer, prendre exemple sur leur caractère et les défendre — car telle est la conduite des vertueux prédécesseurs en l’amour des Compagnons et l’agrément de tous.</li>
</ul>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>1. Je mentionne l’avis le plus solide parmi les paroles des savants sur le sens du siècle (<em>qarn</em>).</li>
<li>2. J’explicite la supériorité des Compagnons en général et des califes bien guidés en particulier, en l’appuyant de preuves.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Il vient, dans le Ṣaḥīḥ d’al-Bukhārī, d’après Anas — que Dieu l’agrée —, qu’un homme interrogea le Prophète ﷺ sur l’Heure : « Quand viendra l’Heure ? » Il dit : « Qu’as-tu préparé pour elle ? » Il dit : « Rien, sinon que j’aime Dieu et Son Messager. » Il dit : « Tu es avec ceux que tu aimes. » Anas dit : rien ne nous réjouit, après l’islam, comme la parole du Messager de Dieu ﷺ : « Tu es avec ceux que tu aimes. » Anas dit : j’aime le Prophète ﷺ, Abū Bakr et ʿUmar, et j’espère être avec eux par mon amour d’eux — dussé-je ne pas œuvrer comme leurs œuvres. [Ṣaḥīḥ d’al-Bukhārī, Kitāb Faḍāʾil al-Ṣaḥāba, bāb des mérites de ʿUmar b. al-Khaṭṭāb — bāb imprimé EXACT (hadith 3688, d’Anas) : texte VÉRIFIÉ sur sunnah.com ; « après l’islam » et « qu’as-tu préparé » suivent la leçon de l’imprimé (variantes mineures de leçon notées).]</p>
<h3>Je médite le hadith et réalise ce qui suit :</h3>
<ul>
<li>Je recherche les méthodes du Messager de Dieu ﷺ dans l’enseignement.</li>
<li>Je recherche les effets de l’amour du Prophète ﷺ et de ses Compagnons — que Dieu les agrée.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qu’il faut croire au sujet des Compagnons — que Dieu les agrée —, et les convenances que cela requiert.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16800":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16800 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16800 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
