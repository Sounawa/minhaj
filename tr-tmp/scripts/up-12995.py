#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12995 (hadith-1es, parmi les règles
et l'étiquette du vendredi — 1 — Muwaṭṭaʾ n° 268/269/270/275/276/278/279
+ Nasāʾī + Aṣḥāb al-Sunan + al-Shaykhayn).

Conventions main (cf. 12875-12987 du même livre) :
- h1 = titleFr officiel « Parmi les décisions et l'étiquette du
  vendredi » + « — première partie » (source : « -1- ») + translit.
  (min aḥkām al-jumuʿa wa-ādābihā — 1), 23e leçon, ouverture de la
  2e partie du manuel (mustahl juzʾ thān).
- Préambule : vendredi préféré aux autres jours (Coran/Sunna/athars).
- Hadiths : 268 (Sumayy/Abū Ṣāliḥ/Abū Hurayra : ghusl comme janāba +
  1ʳᵉ heure = badna, 2ᵉ = vache, 3ᵉ = bélier cornu, 4ᵉ = poule,
  5ᵉ = œuf ; sortie de l'imam → les anges assistent, écoutant le
  dhikr) ; 269 (al-Maqburī/Abū Hurayra : « le ghusl du vendredi est
  obligatoire à tout muḥtalim, comme le ghusl de janāba ») ; 275
  (Abū l-Zinad/al-Aʿraj/Abū Hurayra : « si tu dis à ton compagnon :
  tais-toi, tandis que l'imam prêche — tu as parlé vain »).
- Lexique : qarraba, al-badna (al-Azharī : chameaux seuls — avis
  étendu : chameaux/bovins/ovins), al-dhikr (= le sermon),
  unṣut, laghawt (perte de la vertu du vendredi).
- Taḥlīl I : ghusl — accord : pas obligation stricte (wujūb sunna ;
  comparaison par la manière, pas l'obligation) ; preuve Aṣḥāb
  al-Sunan « qui fait wuḍūʾ — cela suffit et quelle bonne chose ;
  qui lave — le lavage est meilleur » ; Mālik/Shāfiʿī/Abū Ḥanīfa :
  sunna confirmée pour la prière non pour le jour ; Ibn al-Mundhir
  (Abū Hurayra/ʿAmmār b. Yāsir : vraie obligation — Ẓāhirites +
  narration d'Aḥmad) ; manière = janāba ; muḥtalim = majeur
  (iḥtilām prépondérant ; hommes et femmes ; le majeur = trope).
- Taḥlīl II : les « heures » — jumhūr : heures du jour (dès le
  lever) vs Mālik + la plupart de ses compagnons : UNE heure,
  instants subtils du zawāl à l'assise de l'imam au minbar (sāʿa =
  part indéterminée du temps ; hājira — Nasāʾī « anges à chaque
  porte, écrivant le premier puis le suivant ; le pressé = l'offrant
  d'une badna ») ; Shāfiʿī (tahjīr = bakūr, pas la canicule) ;
  Ibn ʿAbd al-Barr (Tamhīd : athars + pratique médinoise — Mālik les
  voyait sortir, n'eût pas toléré le lever du soleil) ; récompense
  graduée badna/vache/bélier/poule/œuf.
- Taḥlīl III : écouter le sermon — interdiction de parler (même
  conseil ou tashmīt) ; 279 (l'éternué — Saʿīd b. al-Musayyab : « ne
  recommence pas ») ; l'obligation d'écouter COURT depuis le début
  du sermon (circonstancielle « wa-l-imām ya khuṭub ») ; les anges
  roulent les feuillets (Shaykhayn via Zuhrī/Abū ʿAbd Allāh
  al-Agharr : « quand l'imam s'assied, ils roulèrent les feuillets
  et vinrent écouter ») ; 276 (Thaʿlaba b. Mālik al-Quraẓī sous
  ʿUmar : adhān → on converse ; silence du muezzin + prêche →
  silence total ; Ibn Shihāb : « la sortie de l'imam coupe la
  prière, sa parole coupe la parole ») ; 278 (Ibn ʿUmar jette les
  cailloux aux deux bavards « taisez-vous » — la manière du
  blâme, prière valide ; al-Bājī : même le geste est laghw).
- Istimḥār : 270 (Sālim : l'homme revenu du marché, wuḍūʾ seul —
  ʿUmar : « le wuḍūʾ aussi ! alors que l'Envoyé commandait le
  ghusl ») + 2 questions + 2 cas (éternuement ; vieux shaykh
  admonestant un jeune aux cailloux).
- Préparation préalable : leçon SUIVANTE 12998 — titrer chaque
  hadith + **Jumuʿa 62 : 9 RESTAURÉ** (emplacement span vide — perte
  OCR ; « fa-sʿaw ilā dhikri Llāhi » — le saʿy que Mālik interprète
  : la sortie-marche, pas la course — cf. 12998).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Parmi les décisions et l’étiquette du vendredi — première partie (<em>min aḥkām al-jumuʿa wa-ādābihā — 1</em>)</h1>
<p>Leçon sur les règles et l’étiquette du vendredi, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-troisième leçon, première partie, ouverture de la deuxième partie.</p>
<ol>
<li>Connaître quelques-unes des règles propres à la prière du vendredi.</li>
<li>Comprendre la vertu de l’empressement vers la prière du vendredi.</li>
<li>Ressentir la grandeur du vendredi et mettre en pratique les sunnas de l’Envoyé — paix et bénédiction sur lui — à son sujet.</li>
</ol>
<h2>Préambule</h2>
<p>Le vendredi est un jour que Dieu préféra au reste des jours de la semaine, comme l’indiquent le Coran, la Sunna et les rapports ; la Sunna vint portant l’indication de ses vertus et sa caractérisation par un ensemble de règles et d’étiquettes.</p>
<p>Quelles sont les vertus du vendredi ? Et quelles règles et étiquettes convient-il d’observer en ce grand jour ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Sumayy, affranchi d’Abū Bakr ibn ʿAbd al-Raḥmān, d’après Abū Ṣāliḥ, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Qui se lave le jour du vendredi du lavage de l’impureté majeure, puis s’en va à la première heure, c’est comme s’il offrait une chamelle (<em>badna</em>) ; qui s’en va à la deuxième heure, c’est comme s’il offrait une vache ; qui s’en va à la troisième heure, c’est comme s’il offrait un bélier cornu ; qui s’en va à la quatrième heure, c’est comme s’il offrait une poule ; qui s’en va à la cinquième heure, c’est comme s’il offrait un œuf ; et quand l’imam sort, les anges assistent, écoutant le rappel (<em>al-dhikr</em>). » [Muwaṭṭaʾ, n° 268]</li>
<li>D’après Mālik, d’après Saʿīd ibn Abī Saʿīd al-Maqburī, d’après Abū Hurayra : « qu’il disait : Le lavage du jour du vendredi est obligatoire pour tout pubère (<em>muḥtalim</em>), comme le lavage de l’impureté majeure. » [Muwaṭṭaʾ, n° 269]</li>
<li>D’après Mālik, d’après Abū l-Zinad, d’après al-Aʿraj, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Si tu dis à ton compagnon : “Tais-toi”, tandis que l’imam prêche le jour du vendredi — tu as parlé vain (<em>laghawt</em>). » [Muwaṭṭaʾ, n° 275]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>qarraba</em> (« offrait ») : il s’en rend proche de Dieu — Exalté — en le donnant en charité.</li>
<li><em>al-badna</em> : le chameau, mâle ou femelle. Al-Azharī a dit : la <em>badna</em> n’est que des chameaux ; et il fut dit : des chameaux, des bovins et des ovins.</li>
<li><em>al-dhikr</em> : le sermon du vendredi et les exhortations qu’il renferme.</li>
<li><em>unṣut</em> (« tais-toi ») : se taire de tout parler quel qu’il soit, et écouter le sermon.</li>
<li><em>laghawt</em> (« tu as parlé vain ») : du <em>laghw</em> — en général : le médiocre du parler, où il n’est aucun bien ; le voulu, dans le hadith : la perte de la vertu du vendredi.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Quel est le statut du lavage pour le jour du vendredi ?</li>
<li>Explicite la vertu de l’empressement vers la prière du vendredi.</li>
<li>Cite quelques-unes des étiquettes qu’il convient d’observer pendant le sermon du vendredi.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le lavage pour le jour du vendredi</h3>
<h4>Le statut du lavage</h4>
<p>Les savants furent d’accord que le lavage du vendredi n’est point une obligation contraignante ; ils explicitèrent le hadith d’Abū Saʿīd al-Khudrī et celui d’Abū Hurayra comme une obligation de sunna, et qu’il est comme le lavage de l’impureté majeure en la forme et la manière : c’est sous ce rapport que vint la comparaison au lavage de l’impureté — non du point de vue de l’obligation, mais de la manière et de la description. Leur preuve : le hadith : “Qui fait ses ablutions le jour du vendredi — elles lui suffisent, et quelle bonne chose ; et qui se lave — le lavage est meilleur.” [Rapporté par les auteurs des <em>Sunan</em>]</p>
<p>L’école de Mālik, d’al-Shāfiʿī et d’Abū Ḥanīfa : le lavage est une sunna confirmée, et il est pour la prière, non pour le jour. Ibn al-Mundhir transmit, d’Abū Hurayra, de ʿAmmār ibn Yāsir et d’autres, la vraie obligation — c’est la parole des Ẓāhirites et une narration d’Aḥmad.</p>
<h4>La manière du lavage</h4>
<p>À qui incombe le vendredi, le lavage lui est sunna, et sa manière est comme la manière du lavage de l’impureté majeure. Et sa parole — paix et bénédiction sur lui — : “pour tout <em>muḥtalim</em>” veut dire : tout majeur — l’émission nocturne n’étant mentionnée que parce qu’elle est le prépondérant : cela embrasse les hommes et les femmes ; et son explicitation par le majeur est un trope, car l’émission nocturne entraîne la majorité.</p>
<h3>Deuxièmement : la vertu de l’empressement vers la prière du vendredi</h3>
<p>Le premier hadith indique la vertu de l’empressement pour assister à la prière du vendredi ; les juristes divergèrent sur les “heures” qui y viennent. Le <em>jumhūr</em> alla à ce que ce sont les heures du jour : ils recommandèrent d’y aller dès le lever du soleil ; Mālik et la plupart de ses compagnons : il visa une seule heure — d’instants subtils, dont le début est le déclin du soleil (<em>zawāl</em>) et la fin l’assise de l’imam sur le minbar — car l’“heure” (<em>sāʿa</em>) se dit d’une part de temps non délimitée, et cette heure n’est que au temps de la canicule (<em>hājira</em>), à l’appui de sa parole — paix et bénédiction sur lui — : “Quand vient le jour du vendredi, des anges se tiennent à chaque porte de la mosquée, écrivant le premier, puis le suivant : le pressé vers la prière est comme l’offrant d’une chamelle…” [fin du hadith — rapporté par an-Nasāʾī]</p>
<p>Al-Shāfiʿī s’écarta de cette explicitation et mentionna que l’<em>empressement</em> (<em>tahjīr</em>) ne signifie pas sortir au temps de la canicule, mais le petit matin. L’imam Ibn ʿAbd al-Barr appuya, dans son <em>Tamhīd</em>, l’école de Mālik, et dit : les rapports appuient ce que dit Mālik — cela est clair en la lettre même de “l’empressement” ; et l’imam Mālik s’appuya aussi, en son explicitation, sur ce dont il vit les gens de Médine : Mālik siégeait parmi eux et voyait leur heure de sortie vers le vendredi — s’ils en fussent sortis au lever du soleil, il l’eût désapprouvé, vu son zèle à les suivre.</p>
<p>Le hadith de la leçon montre que la récompense de l’empressement vers le vendredi varie selon les empressés : plus le musulman est matinal et empressé à y assister, plus sa récompense est grande et immense : le premier empressé a la récompense de qui offrit une chamelle, le second celle de qui offrit une vache… et ainsi de suite.</p>
<h3>Troisièmement : le statut de l’écoute du sermon du vendredi</h3>
<p>Le troisième hadith indique l’interdiction de parler — de quelque genre que ce soit — et l’obligation d’écouter le sermon du vendredi, fussent même les paroles un conseil ou le souhait de miséricorde à l’éternué. D’après Mālik : « qu’il lui parvint qu’un homme éternua le jour du vendredi pendant que l’imam prêchait ; un homme à son côté lui dit : “Que Dieu te fasse miséricorde” ; il interrogea Saʿīd ibn al-Musayyab sur cela — il le lui interdit et dit : Ne recommence pas. » [Muwaṭṭaʾ, n° 279]</p>
<p>Et l’obligation d’écouter court depuis le début de l’entreprise du sermon, non depuis la sortie de l’imam, comme l’indique la lettre du hadith : sa parole “tandis que l’imam prêche” est une phrase circonstancielle qui enseigne que l’obligation d’écouter [part] du début du sermon, non de la sortie de l’imam. Les anges eux-mêmes s’arrêtent d’inscrire les devanciers à la mosquée — quand le sermon commence, ils se consacrent à écouter les exhortations qu’il renferme. Dans la narration des deux Shaykhs, par voie d’al-Zuhrī, d’après Abū ʿAbd Allāh al-Agharr, d’après Abū Hurayra, remontant [au Prophète] : “Quand vient le vendredi, les anges se tiennent à la porte de la mosquée, écrivant le premier, puis le suivant… quand l’imam s’assied, ils roulent les feuillets et viennent écouter le rappel” — le roulage des feuillets commence au début de la sortie de l’imam et s’achève à son assise sur le minbar, qui est le début de leur écoute du rappel.</p>
<p>Parmi les rapports que l’imam Mālik conduisit en ce chapitre, ce qu’il rapporta de son shaykh Ibn Shihāb al-Zuhrī, d’après Thaʿlaba ibn Mālik al-Quraẓī : « qu’il l’informa qu’au temps de ʿUmar ibn al-Khaṭṭāb ils priaient le jour du vendredi jusqu’à ce que ʿUmar sorte ; quand ʿUmar sortait, s’asseyait sur le minbar et que le muezzin appelait, Thaʿlaba dit : nous nous asseyions à converser ; quand le muezzin se taisait et que ʿUmar ibn al-Khaṭṭāb se levait pour prêcher, nous nous taisions — nul de nous ne parlait. Ibn Shihāb dit : la sortie de l’imam coupe la prière, et sa parole coupe la parole. » [Muwaṭṭaʾ, n° 276]</p>
<p>Et de ce qui indique la sévérité envers qui parle pendant que l’imam prêche : ce que rapporta Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar vit deux hommes converser pendant que l’imam prêchait le jour du vendredi — il leur jeta des petits cailloux : “Taisez-vous !” » [Muwaṭṭaʾ, n° 278] — “il leur jeta des petits cailloux” : il les visait de cailloux ; et “taisez-vous !” enseigne la manière de désapprouver cela, et que cela ne corrompt pas leur prière : il ne leur ordonna pas de la refaire. Al-Bājī a dit : le requis de l’école de Mālik est de ne pas leur faire signe : car le geste vaut sa parole “taisez-vous” — et c’est là parler vain.</p>
<h2>L’évaluation</h2>
<ol>
<li>Explicite le voulu par sa parole — paix et bénédiction sur lui — : « Le lavage du vendredi est obligatoire à tout pubère. »</li>
<li>Cite ce dont l’imam Mālik appuya la préférence du meilleur temps pour partir au vendredi.</li>
<li>Déduis des hadiths du chapitre les étiquettes que le musulman doit observer le jour du vendredi.</li>
</ol>
<h2>L’exploitation</h2>
<ul>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Sālim ibn ʿAbd Allāh : « qu’il dit : Un homme des Compagnons du Messager de Dieu — paix et bénédiction sur lui — entra à la mosquée le jour du vendredi tandis que ʿUmar ibn al-Khaṭṭāb prêchait. ʿUmar dit : Quelle heure est-ce donc ? Il dit : Ô Commandeur des croyants, je revenais du marché, j’entendis l’appel, et je ne fis rien de plus que mes ablutions. ʿUmar dit : Les ablutions aussi ! — alors que tu savais que le Messager de Dieu — paix et bénédiction sur lui — commandait le lavage. » [Muwaṭṭaʾ, n° 270]</li>
</ul>
<ol>
<li>Que retires-tu de la parole d’ʿUmar — que Dieu soit satisfait de lui — à l’homme : « Quelle heure est-ce donc ? », et de sa parole : « Les ablutions aussi ! » ?</li>
<li>Explicite le statut des deux cas suivants :</li>
</ol>
<ul>
<li>Un homme éternua à la mosquée pendant le sermon du vendredi, et un autre homme à son côté lui souhaita la miséricorde.</li>
<li>Un shaykh âgé admonesta un jeune homme qui touche les petits cailloux et joue avec pendant le sermon du vendredi.</li>
</ul>
<h2>La préparation préalable</h2>
<ol>
<li>Lis les hadiths de la prochaine leçon et donne à chacun un titre qui convienne.</li>
<li>Explicite l’interprétation de l’imam Mālik — que Dieu lui fasse miséricorde — de l’empressement (<em>saʿy</em>) qui vient en la parole de Dieu :</li>
</ol>
<p>« Ô vous qui croyez ! Quand on appelle à la prière le jour du vendredi, courez au rappel de Dieu et délaissez la vente : cela est meilleur pour vous, si vous savez. » (al-Jumuʿa, 62 : 9)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12995":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12995 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12995 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
