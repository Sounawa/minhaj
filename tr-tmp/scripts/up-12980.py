#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12980 (hadith-1es, le dire de « āmīn »
et la louange dans la prière — Muwaṭṭaʾ n° 233/234/235/236 + Muslim).

Conventions main (cf. 12875-12961 du même livre) :
- h1 « Le dire de « āmīn » et la louange dans la prière (al-taʾmīn
  wa-l-taḥmīd fī l-ṣalāh) », 19e leçon ; FIX titleFr : la baseline
  imprimait « Assurance et louange » — contresens : التأمين = le dire de
  āmīn, non « assurance » (précédent 12897 القبلة/baiser).
- Préambule : Muwaṭṭaʾ 235 (Abū l-Zinad/al-Aʿraj/Abū Hurayra : « quand
  l'un de vous dit āmīn et que les anges au ciel disent āmīn... »).
- Hadiths : 233 (Ibn Shihāb/Saʿīd b. al-Musayyab+Abū Salama : « quand
  l'imam dit āmīn, dites āmīn... » + Ibn Shihāb : « il disait āmīn ») ;
  236 (Sumayy mawlā Abī Bakr/Abū Ṣāliḥ al-Sammān : « quand l'imam dit :
  Dieu entend celui qui Le loue, dites : Ô Dieu, notre Seigneur, à Toi
  la louange... ») — wording vérifié web (Muwaṭṭaʾ éd. ʿAbd al-Bāqī
  p. 88, hadith 47 : sumiyy/Sumayy).
- Taḥlīl I : divergence des narrations mālikites sur le taʾmīn de
  l'imam en jahr : Médinois/Shāfiʿī (il le dit) vs Ibn al-Qāsim
  (mashhūra : non) ; 4 réponses : (1) tarjīḥ (l'imam est invocateur,
  nulle récitation n'incombe au suivi) ; (2) « quand l'imam dit āmīn » =
  quand il invoque — dénomination croisée dāʿī/muʾmin + **Yūnus 10 : 89
  RESTAURÉ** (emplacement span vide — perte OCR) ; Mūsā invocateur /
  Hārūn diseur de āmīn ; objection de non-implication + réplique
  taghlīb (al-qamarān = « les deux lunes » pour soleil+lune ;
  al-abawayn = « les deux pères ») ; (3) « atteignit l'emplacement » —
  anjada/Najd + Ibn Daqīq al-ʿĪd (majāz, preuve Muwaṭṭaʾ 234) + **MILIEU
  DU HADITH 234 RESTAURÉ** « ghayri l-maghḍūbi ʿalayhim wa-lā
  l-ḍāllīn » (coupure de paragraphe OCR — texte attesté web, éd.
  ʿAbd al-Bāqī p. 87) ; (4) l'addition d'Ibn Shihāb portée sur les
  débuts de l'islam (instruction) puis abrogation/permission.
- Taḥlīl I bis : mashhūra — recommandé pour solitaire/suivi/imam en
  sirr, ordre porté sur le ndb — hadith de celui qui fit mal sa prière
  (al-musīʾ ṣalātuhu) : limitation aux obligations.
- Taḥlīl II : formule (imam : samiʿa Allāhu li-man ḥamidahu ; suivi :
  Allāhumma rabbanā laka l-ḥamd ; solitaire réunit — preuve 236 +
  Abū Mūsā chez Muslim « Dieu vous entend » ; réponse aux athars de
  la réunion : solitaire/nāfila/permission) ; description (divergence
  sur la formule du suivi : wāw ou non — Ibn al-Qāsim [addition du sûr]
  vs Ashhab [le wāw surrogatoire n'apporte rien]) ; coïncidence avec
  les anges : 4 avis (entrée en matière/fruit/manière/instant).
- Taḥlīl III : vertu — général mineurs+majeurs vs Muslim « les cinq
  prières... si l'on évite les majeurs » ; à plus forte raison ;
  réponse : ce qui expie = la coïncidence avec les anges, faveur de
  Dieu (pas l'acte du croyant).
- Istimḥār : Zarqānī 1/33 citant Ibn ʿAbd al-Barr (« magnification de
  la vertu du rappel... ») avec **Ghāfir 40 : 7 ENCHÂSSÉ référencé**
  (citation coranique dans la parole d'Ibn ʿAbd al-Barr, non marquée
  dans la source).
- Préparation préalable : leçon SUIVANTE 12985 (tashahhud —
  al-ḥaṣbāʾ/al-tahiyyāt/al-ṭayyibāt ; assise ; statut+formule).
- OCR : « صلى الله عليه وسلم وسلم » (duplication) rendu une fois ;
  « إذا اجتنب الكبائر » (t de اجتنبت tombée) — sens identique, rendu
  « si l'on évite les péchés majeurs » sans note.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Le dire de « āmīn » et la louange dans la prière (<em>al-taʾmīn wa-l-taḥmīd fī l-ṣalāh</em>)</h1>
<p>Leçon sur le dire de « āmīn » et la louange dans la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la dix-neuvième leçon.</p>
<ol>
<li>Connaître la vertu du dire de « āmīn » et de la louange dans la prière.</li>
<li>Distinguer ce que disent l’imam, le suivi et le solitaire en matière de dire de « āmīn » et de louange.</li>
<li>Ressentir dans ma prière les sens du dire de « āmīn » et de la louange.</li>
</ol>
<h2>Préambule</h2>
<p>L’imam Mālik rapporta dans le <em>Muwaṭṭaʾ</em>, d’après Abū l-Zinad, d’après al-Aʿraj, d’après Abū Hurayra — que Dieu soit satisfait de lui —, que le Messager de Dieu — paix et bénédiction sur lui — dit : « Quand l’un de vous dit “āmīn” et que les anges au ciel disent “āmīn”, et que l’un des deux coïncide avec l’autre, il lui est pardonné ce qui a précédé de son péché. » [Muwaṭṭaʾ, n° 235]</p>
<p>Qu’entend-on par le dire de « āmīn » et par la louange dans la prière ? Et quelle est leur vertu ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Saʿīd ibn al-Musayyab et Abū Salama ibn ʿAbd al-Raḥmān : « que tous deux l’informèrent, d’après Abū Hurayra, que le Messager de Dieu — paix et bénédiction sur lui — dit : “Quand l’imam dit ‘āmīn’, dites ‘āmīn’, car celui dont le ‘āmīn’ coïncide avec le ‘āmīn’ des anges, il lui est pardonné ce qui a précédé de son péché.” Ibn Shihāb dit : “Le Messager de Dieu — paix et bénédiction sur lui — disait ‘āmīn’.” » [Muwaṭṭaʾ, n° 233]</li>
<li>D’après Mālik, d’après Sumayy, affranchi d’Abū Bakr, d’après Abū Ṣāliḥ al-Sammān, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — dit : “Quand l’imam dit : ‘Dieu entend celui qui Le loue’, dites : ‘Ô Dieu, notre Seigneur, à Toi la louange’, car celui dont la parole coïncide avec la parole des anges, il lui est pardonné ce qui a précédé de son péché.” » [Muwaṭṭaʾ, n° 236]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>āmīn</em> : avec allongement [de l’ālif] et allègement [du mīm] dans toutes les narrations ; son sens : ô Dieu, exauce.</li>
<li><em>fa-aminū</em> (« dites “āmīn” ») : c’est-à-dire : dites « āmīn ».</li>
<li><em>samiʿa Llāhu li-man ḥamidahu</em> (« Dieu entend celui qui Le loue ») : Dieu accueille la louange de celui qui Le loue, comme l’on dit : Dieu a entendu ton invocation — c’est-à-dire : Il y a répondu et l’a accueillie.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Cite la vertu du dire de « āmīn » et de la louange dans la prière.</li>
<li>Quel est le statut du dire de « āmīn » par l’imam dans la prière ?</li>
<li>Explicite le sens de la coïncidence du « āmīn » de l’orant avec le « āmīn » des anges.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le dire de « āmīn » dans la prière</h3>
<h4>Le statut du dire de « āmīn » par l’imam dans la prière à voix haute</h4>
<p>La narration divergea, de l’imam Mālik, sur le dire de « āmīn » par l’imam :</p>
<ul>
<li>La narration des Médinois, de lui : l’imam dit « āmīn » dans la prière à voix haute, selon l’apparent du hadith d’Abū Hurayra — que Dieu soit satisfait de lui — : « Quand l’imam dit ‘āmīn’, dites ‘āmīn’ » ; et c’est l’école de l’imam al-Shāfiʿī.</li>
<li>La narration d’Ibn al-Qāsim, de lui : l’imam ne dit pas « āmīn » dans la prière à voix haute — c’est la narration connue. Au hadith d’Abū Hurayra on répondit par plusieurs réponses, parmi lesquelles :
<ul>
<li>La préférence de l’abstention du « āmīn » du point de vue du sens : l’imam est un invocateur, il sied donc que le suivi soit seul à dire « āmīn » — ce qui s’accorde avec leur parole : nulle récitation n’incombe au suivi.</li>
<li>Que le sens de sa parole — paix et bénédiction sur lui — : « quand l’imam dit ‘āmīn’ » est : quand il invoque — la dénomination de l’invocateur comme diseur de « āmīn » étant recevable, comme en la parole de Dieu — Exalté :</li>
</ul></li>
</ul>
<p>« Il dit : “Votre invocation à vous deux a déjà été exaucée ; tenez-vous droit, et ne suivez pas la voie de ceux qui ne savent pas.” » (Yūnus, 10 : 89)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>Mūsā était l’invocateur, et Hārūn le diseur de « āmīn » ; on répliqua par l’absence d’implication : nommer le diseur de « āmīn » invocateur n’entraîne pas l’inverse, à savoir nommer l’invocateur diseur de « āmīn » ; on répliqua aussi que cela relève de la prédominance (<em>taghlīb</em>), comme « les deux lunes » (<em>al-qamarān</em>) pour le soleil et la lune, et « les deux pères » (<em>al-abawayn</em>) pour le père et la mère.</p>
<ul>
<li>Que le sens de « quand l’imam dit ‘āmīn’ » est : quand il atteint l’emplacement du « āmīn » — comme l’on dit : <em>anjada</em> : il atteignit Najd, sans y entrer. Ibn Daqīq al-ʿĪd dit : cela relève du trope (<em>majāz</em>) ; s’il se rencontre une preuve qui le fait préférer, on s’y conforme — et sa preuve est le hadith que rapporta l’imam Mālik dans le <em>Muwaṭṭaʾ</em>, d’après Abū Hurayra, remontant [au Prophète] : « Quand l’imam dit : “…ni ceux qui ont encouru la colère, ni les égarés”, dites : “āmīn”… » [Muwaṭṭaʾ, n° 234]. Concilier les deux hadiths exige donc de porter « dit ‘āmīn’ » sur le trope.</li>
</ul>
<p>[Milieu du hadith restauré d’après le texte attesté du <em>Muwaṭṭaʾ</em> — « <em>ghayri l-maghḍūbi ʿalayhim wa-lā l-ḍāllīn</em> » (fin de la Fātiḥa) : la coupure de paragraphe dans la source numérisée avait perdu le milieu de la citation.]</p>
<ul>
<li>Que la parole d’Ibn Shihāb à la fin du hadith : « Le Messager de Dieu — paix et bénédiction sur lui — disait “āmīn” » est portée sur ce qu’il — paix et bénédiction sur lui — disait « āmīn » à voix haute aux débuts de l’islam, pour les instruire ; puis vint ce qui indique son abrogation — ou [elle vise] l’exposé de la permission.</li>
</ul>
<h4>Le statut du dire de « āmīn » par le solitaire, le suivi et l’imam dans la prière silencieuse</h4>
<p>L’imam Mālik tint que le dire de « āmīn » est recommandé pour le solitaire, le suivi et l’imam dans la prière silencieuse, à l’exclusion de la voix haute — selon la narration connue —, et porta l’ordre de sa parole — paix et bénédiction sur lui — : « dites ‘āmīn’ » sur la recommandation, à cause du hadith de celui qui fit mal sa prière (<em>al-musīʾ ṣalātuhu</em>) : il s’en tint, pour lui — paix et bénédiction sur lui —, aux obligations, sans lui mentionner le « āmīn » ni rien d’autre — indice qu’il s’agit d’une recommandation.</p>
<h3>Deuxièmement : la louange dans la prière</h3>
<h4>La formule de la louange</h4>
<p>L’imam Mālik tint que l’imam est seul à dire « Dieu entend celui qui Le loue », et que le suivi est seul à dire « Ô notre Seigneur, à Toi la louange », tandis que le solitaire réunit les deux. Sa preuve est le hadith du chapitre : « Quand l’imam dit : “Dieu entend celui qui Le loue”, dites : “Ô Dieu, notre Seigneur, à Toi la louange” » — et le renforce le hadith d’Abū Mūsā chez Muslim et ailleurs : « Et quand il dit : “Dieu entend celui qui Le loue”, dites : “Ô Dieu, notre Seigneur, à Toi la louange — Dieu vous entend.” » Quant à ce qui fut rapporté de lui — paix et bénédiction sur lui —, selon quoi il réunissait les deux formules, on y répondit qu’il priait alors en solitaire, ou en prière surérogatoire, ou pour l’exposé de la permission.</p>
<h4>La description de la louange</h4>
<p>Les savants ne divergèrent pas sur la description de ce que dit l’imam ; ils divergèrent sur ce que dit le suivi, en raison de la divergence des rapports en la matière : dans le hadith du chapitre : « Ô Dieu, notre Seigneur, à Toi la louange » ; et dans une narration : « Ô Dieu, notre Seigneur, et à Toi la louange », avec le <em>wāw</em>. Les deux furent rapportés de l’imam Mālik : Ibn al-Qāsim choisit l’addition du <em>wāw</em> — son motif : c’est l’addition d’un transmetteur sûr, et l’on préfère l’addition quand elle vient d’un sûr ; et, du point de vue du sens, c’est un accroissement dans la formule du rappel. Ashhab choisit : « Notre Seigneur, à Toi la louange », sans <em>wāw</em> — son motif : le <em>wāw</em> surrogatoire dans le discours n’apporte aucun sens, il est donc préférable de le retrancher.</p>
<h4>Le sens de la coïncidence de la parole de l’orant avec la parole des anges</h4>
<p>Les savants ont, sur le sens de la coïncidence de la parole de l’orant — « āmīn », ou « Dieu entend celui qui Le loue », ou « Notre Seigneur, à Toi la louange » — avec la parole des anges, plusieurs avis, dont les plus importants :</p>
<ul>
<li>La coïncidence dans l’entrée en matière : l’intention et la sincérité — il n’est d’acceptation que par elles.</li>
<li>La coïncidence dans le fruit : l’exaucement — le sens : celui à qui il fut répondu comme il est répondu aux anges, il lui est pardonné ce qui a précédé de son péché.</li>
<li>La coïncidence dans la manière : qu’il invoque pour lui-même et pour les musulmans, comme le font les anges — elles invoquent pour toute la création.</li>
<li>La coïncidence dans l’instant : qu’ils y convergent tous ensemble, afin que s’étende aux gens la bénédiction qui accompagne le partage avec les anges.</li>
</ul>
<h3>Troisièmement : la vertu du dire de « āmīn » et de la louange dans la prière</h3>
<p>Le Prophète — paix et bénédiction sur lui — exposa la vertu du dire de « āmīn » par sa parole : « celui dont le ‘āmīn’ coïncide avec le ‘āmīn’ des anges, il lui est pardonné ce qui a précédé de son péché », et la vertu de la louange par sa parole : « celui dont la parole coïncide avec la parole des anges » — c’est-à-dire : sa louange, leur louange — « il lui est pardonné ce qui a précédé de son péché ». Et cela est général, quant aux péchés mineurs et majeurs ; mais il est établi dans le Ṣaḥīḥ : « Les cinq prières, du vendredi au vendredi, et du ramadan au ramadan, expient ce qui se trouve entre elles, si l’on évite les péchés majeurs » [Rapporté par Muslim]. Si les prières obligatoires n’expient pas les péchés majeurs, à plus forte raison le « āmīn », qui est recommandé ! On répondit : ce qui expie n’est pas le « āmīn », qui est un acte du croyant, mais la coïncidence avec les anges — et cela relève de la faveur de Dieu.</p>
<h2>L’évaluation</h2>
<ol>
<li>Cite le statut du dire de « āmīn » par l’imam dans ce qu’il récite à voix haute.</li>
<li>Explicite la description du dire de « āmīn » et de la louange dans la prière.</li>
<li>Le hadith de la leçon porte que le dire de « āmīn » — recommandé — fait pardonner les péchés sans restriction, tandis qu’un autre hadith porte que les cinq prières — obligations — ne font pardonner que les péchés mineurs. Comment concilier les deux ?</li>
</ol>
<h2>L’exploitation</h2>
<p>Al-Zarqānī a dit : « Ibn ʿAbd al-Barr a dit, sur le sens de sa parole — paix et bénédiction sur lui — : “celui dont la parole coïncide avec la parole des anges, il lui est pardonné ce qui a précédé de son péché” : “Et l’avis, à mes yeux — Dieu sait mieux —, est la magnification de la vertu du rappel, et le fait qu’il abat les charges et fait pardonner les péchés ; Dieu a informé des anges qu’ils demandent pardon pour ceux qui ont cru et qu’ils disent :</p>
<p>« Notre Seigneur ! Tu embrasses toute chose en miséricorde et en science : pardonne donc à ceux qui se sont repentis et ont suivi Ta voie… » (Ghāfir, 40 : 7, extrait)</p>
<p>[Citation coranique enchâssée dans la parole d’Ibn ʿAbd al-Barr, référencée d’après le corpus canonique.]</p>
<p>— quiconque tient de sa parole quelque chose de tel, avec sincérité, effort, intention véridique et repentir sain, ses péchés seront pardonnés, si Dieu le veut.” » [Commentaire d’al-Zarqānī sur le <em>Muwaṭṭaʾ</em>, 1/33]</p>
<ol>
<li>Extrais du texte la vertu du rappel.</li>
<li>Explicite quand cette vertu se réalise.</li>
<li>Quel est le rapport du texte avec les hadiths de la leçon ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Explique ce qui suit : <em>al-ḥaṣbāʾ</em> (les petits cailloux) – <em>al-tahiyyāt</em> (les salutations) – <em>al-ṭayyibāt</em> (les bonnes choses).</li>
<li>Cite la manière de s’asseoir pour le <em>tashahhud</em> dans la prière.</li>
<li>Cite le statut du <em>tashahhud</em> et sa formule dans la prière.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12980":
            l["htmlFr"] = HTML_FR
            # FIX contresens de la baseline : التأمين = le dire de āmīn
            # (« Assurance » = GT-isme ; précédent 12897 القبلة/baiser)
            l["titleFr"] = "Le dire de « āmīn » et la louange dans la prière"
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12980 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12980 upgradée main: FR {len(HTML_FR)} car + titleFr corrigé")


if __name__ == "__main__":
    main()
