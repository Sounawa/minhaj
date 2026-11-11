#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16741 (tawhid-1es, leçon imprimée 17 — la
présentation des créatures devant Dieu Très-Haut).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 8 emplacements de citation vides (perte OCR systématique CMS) :
  Fajr 24 → 22 écart −2 (les DEUX occurrences ; cible univoque : « وجاء ربك
  والملك صفا صفا » = 89:22 Ḥafṣ, repris mot à mot par le matn ; le 24
  imprimé = « يا ليتني قدمت لحياتي ») ; Hajj 1-2 CONFORME (le tremblement +
  la nourrice qui oublie, miroir exact du propos) ; Ḥāqqa 17 CONFORME (les
  anges sur les confins + le Trône porté par huit — la scène de la
  présentation ; le v18 adjacent « تعرضون » noté) ; Kahf 47 CONFORME (le
  rassemblement intégral « فلم نغادر منهم أحدا » ; le v48 adjacent
  « وعُرضوا على ربك صفا » = le membre propre de la présentation, noté) ;
  Ghāshiya paire descendante 26-25 → restituée 25-26 CONFORME (« ثم إن علينا
  حسابهم » — le verset du compte) ; Āl ʿImrān 199 CONFORME (la finale
  « إن الله سريع الحساب », miroir exact du propos) ; Qāriʿa 5-8 CONFORME
  (préparation de la leçon suivante — la Balance).
- Doublons OCR MASSIFS : le bloc entier du compte (citation de Ghāshiya +
  Āl ʿImrān 199 + réplique d'Ibn ʿAṭiyya) imprimé DEUX FOIS — rendu une
  fois, dans sa version complète (la 2e occurrence porte seule la suite du
  propos sur le fruit du compte et les priorités prière/sang) ; dans la
  citation d'al-Lawh, le membre « في رفع عنهم الحجاب… » répété en
  coupe-collage au sein du premier item — rendu une fois ; titre
  « التحليل » absent de l'extraction → h2 restitué d'après la série ;
  points doubles et deux-points parasites non rendus ; orthographe
  maghrébine « اُلْ » du matn rendue normalement ; dl/dt/dd vides + <p>
  vides + echo du titre en queue + divs vides — artefacts non rendus.
- Passages théologiques : la discussion ashʿarite du « venir » (majīʾ) —
  Mālik « اقرؤوها كما جاءت بلا كيف », les taʾwīl des mutakallimūn, la
  position d'Abū l-Ḥasan al-Ashʿarī (nuzūl/istiwāʾ/sāq/qadam/janb/ʿayn/wajh)
  rendue au plus près ; l'ontologie angélique (corps subtils lumineux) ;
  le ḥashr des animaux ; les trois positions d'al-Rāʾid fī ʿilm al-ʿaqāʾid.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la présentation des créatures devant Dieu Très-Haut (2)</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la dix-septième leçon (17).</p>
<ul>
<li>Connaître les scènes de la présentation et du compte au Jour de la Résurrection.</li>
<li>Mettre devant les yeux les scènes du Jour de la Résurrection, à travers ce dont le Noble Coran ou la Sunna prophétique ont informé.</li>
</ul>
<h2>Préambule</h2>
<p>Tu as su, en ce qui a précédé, que Dieu Très-Haut a préparé le Paradis comme demeure d’éternité pour Ses alliés et les y a honorés de la contemplation de Sa Noble Visage ; et qu’Il — exalté soit-Il — a préparé le Feu comme demeure de châtiment pour quiconque mécroit en Lui. Tu feras connaissance, en cette leçon, de ce dont la foi est obligatoire, parmi ce qui survient dans les parvis du Jour de la Résurrection, des terreurs nombreuses.</p>
<p>Que survient-il donc, ce jour-là, de terreurs et de rigueurs ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que Dieu — béni et exalté soit-Il — vient au Jour de la Résurrection, et les anges rang sur rang, pour la présentation des nations, leur compte, leur punition et leur récompense. » [Le <em>matn</em> reprend mot à mot al-Fajr 22 ; l’orthographe maghrébine de l’imprimé (<em>u-l-</em> prosthétique) rendue normalement.]</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>qiyāma</em> (Résurrection) : la levée des tombeaux — le jour où les gens se tiennent debout pour le Seigneur des mondes.</li>
<li><em>ʿarḍ</em> (présentation) : l’apparition devant l’assemblée.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> les scènes du Jour de la Résurrection.</li>
<li>Je dégage du <em>matn</em> la finalité de la présentation des nations à Dieu Très-Haut.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>[Titre absent de l’extraction — restitué d’après la série.] La leçon comprend les axes suivants :</p>
<h3>Premièrement : la foi que Dieu vient au Jour de la Résurrection, et les anges rang sur rang</h3>
<h4>1. La foi que Dieu vient au Jour de la Résurrection</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que Dieu — béni et exalté soit-Il — vient au Jour de la Résurrection. » Il est de la croyance obligatoire de tout croyant, et de la conviction de sa survenance, que Dieu — béni et exalté soit-Il — vient au Jour de la Résurrection ; et l’attribution du venir à Lui — exalté soit-Il — est, à l’unanimité, détournée de son sens littéral : directions, lieux et transfert étant impossibles de Lui. Dieu Très-Haut dit :</p>
<p>« Et ton Seigneur vient, et les anges, rang sur rang. » (al-Fajr, 22)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Fajr 24] — écart −2 : le verset du venir et des rangs est 89:22 en Ḥafṣ (le 24 imprimé est « ah ! si seulement j’avais avancé quelque chose pour ma vie ») ; cible univoque — le <em>matn</em> reprend le verset mot à mot.]</p>
<p>Les anciens vertueux dirent : ceci relève du secret bien gardé, qui ne s’interprète point. Mālik — que Dieu l’agrée — et d’autres disaient, au sujet de ce verset et de ses semblables : « Récitez-le comme il est venu, sans [interroger] le comment. » La majorité des théologiens dialecticiens (<em>mutakallimūn</em>) l’ont interprété : les uns ont dit que le sens de Son venir — exalté soit-Il — est Sa manifestation, car la manifestation, en l’usage, ne vient que par venue et transfert ; et il a été dit : le venir, en propre à Lui — exalté soit-Il —, est un attribut dont l’affirmation est obligatoire par le texte coranique, et qu’il faut détourner du sens littéral impossible — comme la descente (<em>nuzūl</em>), l’établissement (<em>istiwāʾ</em>), le tibia (<em>sāq</em>), le pied, le flanc, l’œil et la face, et leurs semblables —, sauf si un doute se présente : on retient alors, de leur interprétation, ce qu’exige la transcendance. Telle est la doctrine du maître Abū l-Ḥasan al-Ashʿarī.</p>
<p>La parole de l’auteur — « au Jour de la Résurrection » — : il fut nommé ainsi pour la levée de toute la création, ce jour-là, de ses tombeaux, et sa station debout devant son Seigneur et Créateur ; et pour la levée de l’argument, en leur faveur et contre eux. Le Jour de la Résurrection est le jour de l’extinction du bas-monde et de son anéantissement, le jour de la ruine du monde, le jour des terreurs qui font que la nourrice oublie celui qu’elle nourrit. Dieu Très-Haut dit :</p>
<p>« Ô hommes, craignez votre Seigneur : le tremblement de l’Heure est chose immense. Le jour où vous la verrez, toute nourrice oubliera son nourrisson, et toute femelle enceinte déposera sa charge ; et tu verras les hommes comme ivres — mais ils ne sont pas ivres : le châtiment de Dieu sera pourtant terrible. » (al-Ḥajj, 1-2)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — « toute nourrice oubliera son nourrisson » : miroir exact du propos.]</p>
<h4>2. La foi que les anges viennent au Jour de la Résurrection, rang sur rang</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et les anges rang sur rang » : l’attribution du venir aux anges reste sur son sens littéral. « Al-malak » vise les anges : les serviteurs de Dieu, honorés par l’obéissance à Lui, qui ne désobéissent point à Dieu en ce qu’Il leur commande, et font ce qui leur est commandé ; et la majorité des adeptes des Lois tenaient qu’ils sont des corps subtils, lumineux, capables de se figurer en des formes différentes — leur attribution est le bien, la science et la puissance ; ils ne se décrivent ni comme femelles ni comme mâles. Le sens de la parole de l’auteur — « rang sur rang » — : rangées après rangées, cernant les créatures, de sorte que l’Appelant est entendu d’eux et que le regard les traverse.</p>
<p>Et ce que l’auteur mentionne y fait allusion à la parole de Dieu Très-Haut :</p>
<p>« Et ton Seigneur vient, et les anges, rang sur rang. » (al-Fajr, 22)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la même cible que la première occurrence — écart −2, le <em>matn</em> reprenant le verset mot à mot.]</p>
<h3>Deuxièmement : la présentation des nations à Dieu Très-Haut et leur compte au Jour de la Résurrection</h3>
<h4>1. La présentation des nations à Dieu — exalté soit-Il</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « pour la présentation des nations ». Sa parole — « pour la présentation » — dépend de « vient » ; et la présentation (<em>ʿarḍ</em>) est la mise à part de ceux qui sont présentés, l’examen de leurs états et leur identification. Le sens apparent de sa parole — « les nations » — est que toutes les nations, de la création entière, sont présentées ; il fut dit : ne sont rassemblés pour la présentation que ceux dont on prend le compte et qu’on punit — les fils d’Adam, non les bêtes ni les animaux en général ; et la position juste est que l’animal en général est rassemblé.</p>
<p>Sur la présentation des nations pour le compte, Dieu Très-Haut dit :</p>
<p>« Et les anges seront sur ses confins ; et le Trône de ton Seigneur, ce jour-là, sera porté au-dessus d’eux par huit. » (al-Ḥāqqa, 17)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — les anges sur les confins et le portage du Trône : la scène de la présentation ; le verset suivant (« ce jour-là, vous êtes présentés : rien de vous ne demeure caché », al-Ḥāqqa, 18) la complète — noté.]</p>
<p>et Il dit :</p>
<p>« … le jour où Nous ferons marcher les montagnes, où tu verras la terre apparente, et où Nous les aurons rassemblés sans en laisser aucun. » (al-Kahf, 47)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le rassemblement intégral (« sans en laisser aucun ») prépare la présentation ; le verset adjacent (al-Kahf, 48 : « et ils sont présentés à ton Seigneur, en rangs ») en est le membre propre — noté.]</p>
<h4>2. Le compte des nations selon leurs œuvres</h4>
<p>L’auteur — que Dieu Très-Haut lui faisse miséricorde — dit : « leur compte, leur punition et leur récompense » — en apposition à sa parole « pour la présentation ». Son sens est que les scènes de la Résurrection sont la présentation d’abord, puis le compte, puis le châtiment ou la récompense. Sur le compte des nations selon leurs œuvres, Dieu Très-Haut dit :</p>
<p>« Vers Nous est leur retour ; puis, sur Nous est leur compte. » (al-Ghāshiya, 25-26)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : la paire écrite en ordre descendant « 26-25 » — restituée 25-26 CONFORME (Ḥafṣ) ; le verset du compte, miroir exact du propos.]</p>
<p>Sur la mesure du temps du compte, Dieu Très-Haut dit :</p>
<p>« … ceux-là ont leur salaire auprès de leur Seigneur : Dieu, certes, est prompt au compte. » (Āl ʿImrān, 199)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — « prompt au compte » (<em>sarīʿ al-ḥisāb</em>) : le propos l’explicite.] Le Vrai — exalté soit-Il — a informé de Lui-même qu’Il est prompt au compte des créatures, malgré leur grand nombre, la multitude de leurs œuvres et leur diversité : cela indique la perfection de Sa puissance — exalté soit-Il.</p>
<p>Ibn ʿAṭiyya — que Dieu lui fasse miséricorde — rapporte : on dit à ʿAlī b. Abī Ṭālib — que Dieu l’agrée : « Comment Dieu prendra-t-Il les créatures à compte ? » Il dit : « Comme Il les pourvoit en un jour. » [<em>Al-Muḥarrar al-wajīz</em>, 12/414 — réf imprimée conservée. Le bloc de citations et de la réplique d’Ibn ʿAṭiyya est imprimé deux fois — doublon d’extraction intégral : rendu une fois, en sa version complète.]</p>
<p>La parole de l’auteur — « et leur punition et leur récompense » — : la récompense et le châtiment sont le fruit du compte, son utilité et son issue ; et il est venu que la première des œuvres du serviteur dont il est pris à compte est la prière, et que la première affaire tranchée entre les gens est celle du sang.</p>
<h2>Les fruits de la leçon</h2>
<p>L’éducation du croyant à la vigilance envers Dieu Très-Haut et à la présence intérieure de la station debout devant Lui, et la provision pour ces scènes par la piété de Dieu Très-Haut et l’obéissance à Lui. En le compte : la manifestation des rangs des maîtres de la perfection et les disgrâces des tenants de la déficience, à la tête des témoins assemblés — accroissement des délices et des joies de ceux-ci, des peines et des chagrins de ceux-là : il y a là incitation aux bonnes œuvres et répression des mauvaises.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’explicite la doctrine des anciens sur le sens de la parole de l’auteur : « Et que Dieu — béni et exalté soit-Il — vient au Jour de la Résurrection. »</li>
<li>Quel est le sens de la parole de l’auteur : « rang sur rang » ?</li>
<li>Comment Dieu prend-Il les créatures à compte ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le maître al-ʿArabī al-Lawh — que Dieu lui fasse miséricorde — dit : « Les savants ont divergé sur le sens de Sa prise à compte de Ses serviteurs, en plusieurs propos :</p>
<ul>
<li>La première : Il — exalté soit-Il — leur parle de l’affaire de leurs œuvres, et de ce qu’elles ont comme récompense et de ce qu’elles encourent comme châtiment, en levant sur eux le voile et en leur faisant entendre Sa parole éternelle ; ou un son qui L’indique, qu’Il crée — exalté et magnifié soit-Il — dans l’oreille de chacun des responsables, ou en un lieu proche de son oreille, sans que la puissance de ce son n’empêche autrui d’entendre ce qui lui fut dit. Et c’est ce qu’attestent les hadiths authentiques. [Le membre « en levant sur eux le voile… » est imprimé deux fois au sein de l’item — coupe-répétition d’extraction : rendu une fois.]</li>
<li>La deuxième : Dieu crée en leurs cœurs une science nécessaire (<em>ḍarūriyya</em>) des mesures de leurs œuvres — récompense ou châtiment ; position du Fakhr al-Rāzī. La troisième : Il — exalté soit-Il — les stationne devant Lui et leur remet les livres de leurs œuvres, où sont leurs mauvaises et leurs bonnes actions, et dit : “ Voici vos mauvaises actions — Je les ai passées outre ; et voici vos bonnes actions — Je les vous ai multipliées. ” — rapporté d’Ibn ʿAbbās — que Dieu les agrée. ” » [<em>Al-Rāʾid fī ʿilm al-ʿaqāʾid</em>, p. 218 — réf imprimée conservée ; la graphie « al-Lawh » suit l’imprimé « اللوه » telle quelle.]</li>
</ul>
<p>Je lis le texte avec attention et méditation, puis je réponds à ce qui suit :</p>
<ul>
<li>Quelle est la position qui s’accorde avec ce que j’ai acquis de la leçon précédente sur la manière du compte ?</li>
<li>J’extrais du texte ce qui indique que Dieu Très-Haut prend Lui-même Ses serviteurs à compte.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Il est venu, en la sourate al-Qāriʿa, la parole de Dieu Très-Haut :</p>
<p>« … et les montagnes seront comme la laine cardée. Quant à celui dont les balances seront lourdes : il sera en une vie satisfaite ; et quant à celui dont les balances seront légères… » (al-Qāriʿa, 5-8)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — les quatre versets 5 à 8, préparation de la leçon suivante (la Balance).]</p>
<ul>
<li>Je recherche l’interprétation de ces versets, et les compare aux versets d’al-Aʿrāf sur le même sujet.</li>
<li>Qu’est-ce qui est pesé en ces balances ? Et comment est-il pesé ?</li>
<li>Et quelle est la récompense de celui dont les balances seront lourdes ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16741":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16741 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16741 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
