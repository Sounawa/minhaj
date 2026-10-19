#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12908 (hadith-1es, dispositions du
tayammum — Muwaṭṭaʾ n° 136-146).

Conventions main (cf. 12875, 12884-12901 du même livre) :
- h1 « Les dispositions du tayammum (aḥkām al-tayammum) », 10e leçon.
- Objectifs en infinitifs (le source imprime « أن أميز » — hamza coupée,
  calque de « أن تميّز ») ; question intrusive « ? » de l'objectif 2 omise.
- Muwaṭṭaʾ 136 (collier de ʿĀʾisha : al-Bayḍāʾ ou Dhāt al-Jaysh, Abū Bakr
  frappe le flanc, Usayd « ô famille d'Abū Bakr », collier sous le chameau),
  137 (tayammum pour chaque prière), 138 (imamat du mutayammim — karāha),
  139 (l'eau survient pendant la prière : ne pas interrompre), 140 (le
  purificateur n'est pas plus pur), 141 (ḥizb et nafl du junub), 143 (Ibn
  ʿUmar jusqu'aux coudes), 144 (deux frappes), 145 (Saʿīd b. al-Musayyab :
  lavage pour l'avenir), 146 (pollution en voyage, eau comptée).
- VERSETS restaurés du quran-cache (emplacements OCR vides) : Māʾida (5) : 7
  ×3 (numérotation du manuel, cohérence 12875/12885 — le décompte oriental
  imprime « 6 »), an-Nisāʾ (4) : 43 (extrait tayammum) et (4) : 29
  (« ne vous tuez pas vous-mêmes » — hadith ʿAmr b. al-ʿĀṣ, Dhāt al-Salāsil).
- Taḥlīl : Qurṭubī (verset de al-Nisāʾ) vs Ibn Ḥajar (al-Bukhārī, Tafsīr,
  riwāya ʿAmr b. al-Ḥārith → verset de al-Māʾida) ; tayammum mubīḥ non
  rāfiʿ al-ḥadath (mashhūr) ; analogies ẓihār / ʿidda ; ʿAmmār (les deux
  Ṣaḥīḥ — roulement dans la poussière) ; sabkha (terre salée).
- Lexique : al-Bayḍāʾ (plateau avant Dhū l-Ḥulayfa), Dhāt al-Jaysh,
  khāṣira (flanc), adhā (impureté).
- Préparation préalable : questions de la leçon SUIVANTE 12911 (ḥayḍ /
  istiḥāḍa).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les dispositions du tayammum (<em>aḥkām al-tayammum</em>)</h1>
<p>Leçon sur les dispositions du tayammum, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la dixième leçon.</p>
<ul>
<li>Connaître la légitimité (<em>mashrūʿiyya</em>) du tayammum et sa méthode (<em>kayfiyya</em>).</li>
<li>Distinguer les obligations du tayammum de ses recommandations.</li>
<li>Éprouver la facilité de la Shariʿa à travers la légitimité du tayammum.</li>
</ul>
<h2>Préambule</h2>
<p>La Shariʿa islamique se distingue par la facilité (<em>yusr</em>) et la levée de la gêne : elle prend en compte les états des assujettis par des règles appropriées, entre exigences (<em>ʿazāʾim</em>) et concessions (<em>rukhaṣ</em>). Parmi ces concessions : la concession du tayammum lorsque survient l’empêchement qui interdit les ablutions.</p>
<p>Quelle est donc la preuve de la légitimité du tayammum ? Et quelle est sa méthode ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après ʿAbd al-Raḥmān ibn al-Qāsim, d’après son père, d’après ʿĀʾisha, mère des croyants : « qu’elle dit : Nous sortîmes avec le Messager de Dieu — paix et bénédiction sur lui — dans l’un de ses voyages ; lorsque nous fûmes à al-Bayḍāʾ — ou à Dhāt al-Jaysh —, mon collier se détacha. Le Messager de Dieu — paix et bénédiction sur lui — s’arrêta pour le chercher, et les gens s’arrêtèrent avec lui — alors qu’ils n’étaient pas près d’eau et n’avaient pas d’eau avec eux. Les gens vinrent trouver Abū Bakr al-Ṣiddīq et dirent : Ne vois-tu pas ce qu’a fait ʿĀʾisha ? Elle a retenu le Messager de Dieu — paix et bénédiction sur lui — et les gens, alors qu’ils ne sont pas près d’eau et n’ont pas d’eau avec eux. ʿĀʾisha dit : Abū Bakr vint alors que le Messager de Dieu — paix et bénédiction sur lui — avait posé la tête sur ma cuisse et dormait. Il dit : Tu as retenu le Messager de Dieu — paix et bénédiction sur lui — et les gens, alors qu’ils ne sont pas près d’eau et n’ont pas d’eau avec eux ! ʿĀʾisha dit : Abū Bakr me blâma et dit ce que Dieu voulut qu’il dise, et il se mit à me frapper de la main au flanc — mais rien ne m’empêchait de bouger sinon la place de la tête du Messager de Dieu — paix et bénédiction sur lui — sur ma cuisse. Le Messager de Dieu — paix et bénédiction sur lui — dormit jusqu’au matin sans eau : Dieu — Béni et Très-Haut — fit alors descendre le verset du tayammum. Usayd ibn al-Ḥuḍayr dit : Ce n’est pas la première de vos bénédictions, ô famille d’Abū Bakr ! Elle dit : Nous fîmes alors lever le chameau sur lequel j’étais montée, et nous trouvâmes le collier dessous. » [Muwaṭṭaʾ, n° 136]</li>
<li>On interrogea Mālik : « Comment fait-on le tayammum, et jusqu’où remonter avec lui ? » Il dit : « Il frappe une frappe pour le visage et une frappe pour les deux mains, et il les essuie jusqu’aux deux coudes. » [Muwaṭṭaʾ, n° 144]</li>
<li>Mālik, d’après ʿAbd al-Raḥmān ibn Harmala : « qu’un homme interrogea Saʿīd ibn al-Musayyab au sujet de l’homme en état d’impureté majeure qui fait le tayammum puis trouve l’eau. Saʿīd dit : S’il trouve l’eau, le lavage lui incombe pour ce qui lui reste à faire. » [Muwaṭṭaʾ, n° 145]</li>
<li>Yaḥyā a dit : Mālik dit, au sujet de celui qui a eu une pollution nocturne en voyage et ne dispose d’eau que la mesure des ablutions, sans craindre la soif jusqu’à parvenir à l’eau : « Qu’il lave avec cela son sexe et l’impureté qui l’a atteint, puis qu’il fasse le tayammum sur une surface de sol pure, comme Dieu — Puissant et Majestueux — le lui a commandé. » [Muwaṭṭaʾ, n° 146]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>al-Bayḍāʾ</em> : avec fatha du bāʾ et allongement ; c’est le plateau qui se trouve devant Dhū l-Ḥulayfa, sur la route de La Mecque.</li>
<li><em>Dhāt al-Jaysh</em> : lieu proche de Médine.</li>
<li><em>khāṣiratī</em> (« mon flanc ») : le flanc est le milieu du corps de l’homme ; et <em>khaṣr</em> — avec fatha du <em>khāʾ</em> et sukūn du <em>hāʾ</em> — désigne son milieu.</li>
<li><em>al-adhā</em> (la souillure) : l’impureté.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Indique la preuve de la légitimité du tayammum à partir du premier hadith.</li>
<li>Expose le statut de la répétition du tayammum pour chaque prière, et celui de l’imamat en cet état.</li>
<li>Quelle est la description du tayammum ? Et comment l’impur majeur fait-il le tayammum ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le verset du tayammum visé dans le hadith</h3>
<p>Le verset du tayammum fut révélé à cause de l’histoire du collier de ʿĀʾisha — que Dieu soit satisfait d’elle —, et le hadith contient : « Dieu — Béni et Très-Haut — fit alors descendre le verset du tayammum. » Al-Qurṭubī a dit : c’est le verset de sourate <em>al-Nisāʾ</em>, car le verset de <em>al-Māʾida</em> est appelé « le verset des ablutions », tandis que le verset de <em>al-Nisāʾ</em> ne comporte aucune mention des ablutions. Ibn Ḥajar a dit : « Échappa à tous ce qui fut manifeste à al-Bukhārī : c’est le verset de <em>al-Māʾida</em>, sans hésitation — du fait de la narration de ʿAmr ibn al-Ḥārith, d’après ʿAbd al-Raḥmān ibn al-Qāsim, chez al-Bukhārī dans le [livre du] Tafsīr, où il dit : “Alors fut révélé le verset :” »</p>
<p>« Ô vous qui croyez ! quand vous vous levez pour la prière, lavez vos visages et vos mains jusqu’aux coudes, passez [vos mains mouillées] sur vos têtes et [lavez] vos pieds jusqu’aux chevilles. Si vous êtes en état d’impureté majeure, purifiez-vous. Et si vous êtes malades, ou en voyage, ou si l’un de vous revient de la selle, ou si vous avez touché des femmes et ne trouvez pas d’eau, alors recourez à une terre pure et passez-en sur vos visages et vos mains. Dieu ne veut pas vous imposer de gêne, mais Il veut vous purifier et parfaire Son bienfait sur vous — afin que vous soyez reconnaissants. » (al-Māʾida, 5 : 7)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR. Numérotation du manuel, en cohérence avec les leçons 12875 et 12885 du même livre.]</p>
<h3>Deuxièmement : le statut de la répétition du tayammum pour chaque prière, et de l’imamat en cet état</h3>
<p>On ne prie avec le tayammum qu’une seule prière obligatoire : car répéter la purification pour chaque prière est la règle originaire — l’impératif [coranique] entraînant la répétition — ; la faveur est advenue pour les ablutions, en ceci qu’on prie avec elles plusieurs prières, et le tayammum est demeuré sur la règle originaire : parce qu’il ne comporte aucune peine, et parce qu’il incombe de rechercher l’eau à chaque prière. Tel est le contexte de la parole du Très-Haut :</p>
<p>« …Et si vous êtes malades, ou en voyage, ou si l’un de vous revient de la selle, ou si vous avez touché des femmes et ne trouvez pas d’eau, alors recourez à une terre pure et passez-en sur vos visages et vos mains. Dieu, en vérité, est Absoluteur et Pardonneur. » (an-Nisāʾ, 4 : 43, extrait)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>Oui : il est permis de faire suivre la prière obligatoire d’une surérogatoire ou d’une funéraire avec le tayammum de l’obligatoire. Yaḥyā a dit : on interrogea Mālik au sujet d’un homme qui fit le tayammum pour une prière survenue, puis qu’une autre prière survint : doit-il faire le tayammum pour elle, ou son tayammum antérieur lui suffit-il ? Il dit : « Qu’il fasse plutôt le tayammum pour chaque prière : car il lui incombe de rechercher l’eau pour chaque prière — quiconque recherche l’eau et ne la trouve pas, alors qu’il fasse le tayammum. » [Muwaṭṭaʾ, n° 137]</p>
<p>Dès lors, quiconque recherche l’eau et ne la trouve pas fait le tayammum : car le tayammum est un permis de prier, non une levée de l’impureté rituelle — selon l’avis répandu — ; c’est pourquoi il est requis pour chaque prière.</p>
<p>Quant à l’imamat de l’homme purifié par tayammum sur des gens en état d’ablutions : on interrogea Mālik au sujet d’un homme qui fit le tayammum : « Peut-il diriger ses compagnons alors qu’ils sont en état d’ablutions ? Il dit : Que les dirige un autre que lui m’est plus aimable ; et s’il les dirigeait lui-même, je n’y verrais aucun mal. » [Muwaṭṭaʾ, n° 138] — c’est-à-dire : permis, avec répugnance.</p>
<p>Et la preuve de la permission est le hadith de ʿAmr ibn al-ʿĀṣ : « J’eus une pollution nocturne par une nuit froide, lors de l’expédition de Dhāt al-Salāsil ; je craignis, si je me lavais, de me perdre. Je fis donc le tayammum, et dirigeai mes compagnons dans la prière de l’aube. Ils en firent mention au Prophète — paix et bénédiction sur lui —, qui dit : Ô ʿAmr, tu as dirigé tes compagnons alors que tu étais en état d’impureté majeure ? Je l’informai de ce qui m’avait empêché de me laver, et je dis : J’ai entendu Dieu dire :</p>
<p>« Ô vous qui croyez ! ne dévorez pas vos biens entre vous par de faux moyens — à moins que ce ne soit un commerce conclu d’un commun consentement entre vous — et ne vous tuez pas vous-mêmes. Dieu, en vérité, est Miséricordieux envers vous. » (an-Nisāʾ, 4 : 29)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>Le Messager de Dieu — paix et bénédiction sur lui — sourit, et ne dit rien. » Rapporté par Abū Dāwūd dans ses <em>Sunan</em> — et son isnād est solide — ; et par al-Ḥākim dans le <em>Mustadrak</em>.</p>
<h3>Troisièmement : le statut de celui qui entama la prière avec le tayammum, et à qui quelqu’un apporte de l’eau</h3>
<p>Yaḥyā a dit : Mālik dit, au sujet d’un homme qui fit le tayammum faute d’avoir trouvé de l’eau, puis se tint debout, prononça le <em>takbīr</em> et entra dans la prière — et voilà qu’un homme surgit auprès de lui portant de l’eau : « Qu’il n’interrompe pas sa prière : qu’il l’achève avec le tayammum, et qu’il fasse ses ablutions pour les prières à venir. » [Muwaṭṭaʾ, n° 139]</p>
<p>Car il ne s’est établi ni dans la Sunna ni par consensus rien qui impose de rompre sa prière ; et son cas est celui de l’homme à qui incomba le jeûne [expiatoire] du ẓihār, qui en jeûna la plus grande partie puis s’enrichit : il ne passe pas à un autre des modes de l’expiation. C’est l’avis d’al-Shāfiʿī et de Dāwūd. Abū Ḥanīfa, Aḥmad et d’autres ont dit : il interrompt la prière, fait ses ablutions et la reprend — en raison du consensus relatif à la femme en délai de viduité compté en mois : si, n’en ayant laissé s’écouler que la moindre part, elle a ses règles, elle reprend son délai à compter de la menstruation. Quant à celui qui trouve l’eau avant d’entrer dans la prière : les ablutions s’imposent à lui, par consensus selon Ibn ʿAbd al-Barr ; et s’il la trouve après [la prière], il est recommandé de la refaire dans son temps — selon notre école.</p>
<p>Puis : celui qui fait le tayammum conformément à la forme légale est pur, comme celui qui fait ses ablutions, selon la parole de Dieu — Puissant et Majestueux — dans le contexte du verset du tayammum :</p>
<p>« …Dieu ne veut pas vous imposer de gêne, mais Il veut vous purifier et parfaire Son bienfait sur vous — afin que vous soyez reconnaissants. » (al-Māʾida, 5 : 7, extrait)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>Quatrièmement : la description du tayammum, et la façon dont l’impur majeur fait le tayammum</h3>
<p>Le tayammum est de deux frappes : une frappe dont il essuie son visage et ses mains jusqu’aux poignets — obligatoirement —, et une frappe dont il essuie ses mains jusqu’aux coudes — en réalisation de la sunna, afin de réunir l’obligatoire et la sunna. S’il s’en tient, pour les deux, à une seule frappe, elle lui suffit — et il n’y a pas à refaire [la prière] selon notre école ; et s’il les essuie jusqu’aux poignets, c’est valable, mais il est recommandé de la refaire dans le temps. Il — que Dieu lui fasse miséricorde — répondit donc par la description complète. Et ce qui indique que le tayammum jusqu’aux coudes est recommandé : ce que rapporta Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar faisait le tayammum jusqu’aux deux coudes. » [Muwaṭṭaʾ, n° 143]</p>
<p>On interrogea Mālik : « Comment [fait-on] le tayammum, et jusqu’où remonter avec lui ? » Il dit : « Il frappe une frappe pour le visage, et une frappe pour les deux mains, et il les essuie jusqu’aux deux coudes. » [Muwaṭṭaʾ, n° 144]</p>
<p>Et l’impur majeur fait le tayammum comme le fait celui qui ne l’est pas : ils ne diffèrent que par l’intention. Dans les deux <em>Ṣaḥīḥ</em>, au hadith de ʿAmmār : il se trouva en état d’impureté majeure, se roula dans la poussière et pria. Il dit : J’en fis mention au Prophète — paix et bénédiction sur lui —, et il dit : « Il t’aurait suffi de faire ainsi » — et le Prophète — paix et bénédiction sur lui — frappa la terre avec ses deux paumes, souffla sur elles, puis essuya avec elles son visage et ses deux mains. Il le lui enseigna ainsi, en acte et en parole.</p>
<p>Ce hadith montre que le tayammum de l’impur majeur est comme celui de qui ne l’est pas ; et l’on en tire pareillement que ce qui n’y est pas mentionné n’a pas le caractère d’obligation.</p>
<h2>L’évaluation</h2>
<ol>
<li>Explique combien de prières obligatoires on prie avec le tayammum, preuve et justification à l’appui.</li>
<li>Expose la méthode du tayammum.</li>
<li>Quel est le statut de celui qui entama la prière, et à qui l’on apporta de l’eau ?</li>
</ol>
<h2>L’exploitation</h2>
<p>Mālik a dit : « Quiconque se lève pour la prière, ne trouve pas d’eau et fait ce que Dieu lui a commandé — le tayammum — : il a obéi à Dieu ; et celui qui a trouvé l’eau n’est pas plus pur que lui, ni plus complet dans sa prière, car tous deux ont reçu l’ordre, et chacun a fait ce que Dieu lui a commandé. N’incombe en effet que d’accomplir ce que Dieu a commandé : les ablutions, à qui trouve l’eau ; le tayammum, à qui ne la trouve pas — avant d’entrer dans la prière. » [Muwaṭṭaʾ, n° 140]</p>
<p>Et Mālik dit, au sujet de l’homme en état d’impureté majeure : « Qu’il fasse le tayammum, récite sa part (<em>ḥizb</em>) du Coran et prie en surérogation tant qu’il ne trouve pas d’eau — cela toutefois au lieu où il lui est permis de prier avec le tayammum. » [Muwaṭṭaʾ, n° 141]</p>
<p>On interrogea Mālik au sujet d’un homme en état d’impureté majeure qui voulut faire le tayammum et ne trouva de terre que la terre d’une <em>sabkha</em> : peut-il faire le tayammum avec les terres salées, et la prière dans les terres salées est-elle réprouvée ? Mālik dit : « Il n’y a aucun mal à prier dans les terres salées, ni à en faire le tayammum, car Dieu — Béni et Très-Haut — a dit :</p>
<p>« …et si vous ne trouvez pas d’eau, alors recourez à une terre pure, et passez-en sur vos visages et vos mains. » (al-Māʾida, 5 : 7, extrait)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>» Dès lors, tout ce qui est surface de sol (<em>ṣaʿīd</em>) convient au tayammum, salée ou autre.</p>
<p><em>Terre de sabkha</em> : terre salée où presque rien ne pousse.</p>
<ol>
<li>Indique, à partir du premier texte, si celui qui fait ses ablutions a un mérite sur celui qui fait le tayammum.</li>
<li>Extrais du deuxième texte ce que le tayammum permet à l’impur majeur.</li>
<li>Explique ce qu’on entend par « surface de sol pure » (<em>ṣaʿīd ṭayyib</em>), avec des exemples.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Qu’entend-on par les menstrues (<em>ḥayḍ</em>) et la métrorragie (<em>istiḥāḍa</em>) ?</li>
<li>Quelle est la marque de la purification des menstrues ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12908":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12908 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12908 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
