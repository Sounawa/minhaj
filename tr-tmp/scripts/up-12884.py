#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 12884 (hadith-1es, la vertu des ablutions
et de l'istitāba — Muwaṭṭaʾ n° 65 et 68).

Conventions main (cf. 12875, 12881, 12883 du même livre) :
- h1 « La vertu des ablutions et de l'istitāba (faḍl al-wuḍūʾ wa-l-istitāba) ».
- Paragraphe d'ouverture : Muwaṭṭaʾ de l'imam Mālik, commentaire al-Zarqānī,
  1re année secondaire traditionnel (ʿatīq), leçon 4.
- Sections : Préambule / Les hadiths / Explication lexicale / Extraction des
  contenus / L'analyse (Premièrement, Deuxièmement) / L'évaluation /
  L'exploitation / La préparation préalable.

Vérifications :
- Versets PERDUS par l'OCR (paragraphes vides avant les spans de référence) →
  restaurés du canonique quran-cache.json :
  · Préambule : al-Baqara 222 « Dieu aime ceux qui reviennent [à Lui] et aime
    ceux qui se purifient » (le manuel imprime « 220 » — numérotation maghrébine) ;
  · Mérite de l'istitāba : at-Tawba 108 « y sont des hommes qui aiment à se
    purifier, et Dieu aime ceux qui se purifient » (le manuel imprime « 109 » —
    le verset imprimé ne peut être que 108 : c'est lui que le hadith des Anṣār
    commente ; convention cache en principal + note imprimée).
- Hadiths du Muwaṭṭaʾ : n° 65 (trois pierres) et n° 68 (Ṣanābiḥī — les fautes
  sortent avec l'eau des ablutions) traduits intégralement avec les chaînes.
- Hadiths Dāraquṭnī : « trois bâtons, trois pierres, trois poignées de terre »
  (istijmār) ; Anṣār « Dieu vous a loués au sujet du ṭuhūr » ; Muslim « les
  cinq prières… si l'on évite les fautes majeures ».
- Exploitation : hadith du cimetière (ghurra muḥajjala — les marques
  resplendissantes des ablutions ; فَسُحْقًا = « qu'ils soient éloignés ! » —
  le GT imprimait « Putain », scandaleux, corrigé).
- Préparation préalable : questions de la leçon SUIVANTE 12885 (essuyage sur
  les chaussettes et le turban) — la baseline y mettait à tort le thème courant.
- ʿIyāḍ, al-Bājī, Ibn Daqīq al-ʿĪd, Ibn al-Tīn, al-Mufhim, al-Nawawī,
  Asbagh : raḥima (non-Compagnons — pas de « Dieu soit satisfait de lui »).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>La vertu des ablutions et de l'istitāba (<em>faḍl al-wuḍūʾ wa-l-istitāba</em>)</h1>
<p>Leçon sur la vertu des ablutions et de l'istitāba, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l'imam Mālik avec le commentaire de l'imam al-Zarqānī, à l'intention des élèves de la première année de l'enseignement secondaire traditionnel (<em>ʿatīq</em>) — la quatrième leçon.</p>
<ul>
<li>Connaître les règles de l'istitāba.</li>
<li>Saisir la vertu des ablutions.</li>
<li>S'appliquer à obtenir la vertu des ablutions.</li>
</ul>
<h2>Préambule</h2>
<p>La purification extérieure par l'eau en vue des prières, et la purification intérieure des fautes, sont une chose que Dieu Très-Haut aime — selon la généralité de Sa parole, Puissant et Majestueux :</p>
<p>« Ils t'interrogent sur la menstruation. Dis : "C'est une nuisance. Éloignez-vous donc des femmes pendant la menstruation, et ne les approchez pas qu'elles ne se soient purifiées. Puis, quand elles se sont purifiées, venez à elles comme Dieu vous l'a ordonné." Dieu aime ceux qui reviennent [à Lui] et aime ceux qui se purifient. » (al-Baqara, 2 : 222 — le manuel imprime « 220 »)</p>
<p>[Verset restauré d'après le corpus canonique : l'emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>Cet amour, et les autres vertus encore, se réalisent par la purification au moyen de l'istitāba et des ablutions. Qu'est-ce que l'istitāba, et quelles sont ses règles ? Et quelle est la vertu des ablutions ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D'après Mālik, d'après Hishām ibn ʿUrwa, d'après son père : « Le Messager de Dieu — paix et bénédiction sur lui — fut interrogé au sujet de l'istitāba (le nettoiement après les besoins) ; il dit : "L'un de vous ne trouve-t-il pas trois pierres ?" » [Muwaṭṭaʾ, n° 65]</li>
<li>D'après Mālik, d'après Zayd ibn Aslam, d'après ʿAṭāʾ ibn Yasār, d'après ʿAbd Allāh al-Ṣanābiḥī : « Le Messager de Dieu — paix et bénédiction sur lui — a dit : Quand le serviteur croyant fait ses ablutions et se rince la bouche, les fautes sortent de sa bouche ; et quand il aspire [l'eau] par le nez, les fautes sortent de son nez ; et quand il lave son visage, les fautes sortent de son visage — jusqu'à sortir de sous les cils de ses deux yeux ; et quand il lave ses deux mains, les fautes sortent de ses deux mains — jusqu'à sortir de sous les ongles de ses deux mains ; et quand il essuie sa tête, les fautes sortent de sa tête — jusqu'à sortir de ses deux oreilles ; et quand il lave ses deux pieds, les fautes sortent de ses deux pieds — jusqu'à sortir de sous les ongles de ses deux pieds. Il dit : "Puis, sa marche jusqu'à la mosquée et sa prière seront pour lui une surérogation (<em>nāfila</em>)." » [Muwaṭṭaʾ, n° 68]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>l'istitāba</em> (<em>al-istitāba</em>) : la quête de la pureté (<em>ṭīb</em>). Les gens de la langue ont dit : l'istitāba est l'istinjāʾ — le nettoiement ; on dit <em>istaṭāba</em> et <em>aṭāba</em> (<em>iṭābatan</em>) tout autant : car celui qui se nettoie (<em>al-mustanjī</em>) rend son âme agréable en ôtant l'impureté (<em>khabath</em>) de l'issue.</li>
<li><em>les fautes</em> (<em>al-khaṭāyā</em>) : les péchés.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Qu'est-ce que l'istitāba et quelles sont ses règles ?</li>
<li>Expose la vertu des ablutions.</li>
</ul>
<h2>L'analyse</h2>
<h3>Premièrement : le concept de l'istitāba et ses règles</h3>
<h4>Définition de l'istitāba</h4>
<p>L'istitāba et l'istinjāʾ sont, en langue, de même signification. On dit : <em>istaṭāba</em> et <em>aṭāba</em> — <em>iṭābatan</em> — car celui qui se nettoie rend son âme agréable en ôtant l'impureté de l'issue. Abū ʿUmar [Ibn ʿAbd al-Barr] a dit : « L'istitāba, l'istijmār et l'istinjāʾ sont de même signification — sauf que l'istinjāʾ ne se fait que par les pierres, tandis que l'istijmār et l'istitāba se font, eux, par l'eau et par la pierre. »</p>
<h4>Avec quoi l'istitāba se fait-elle ?</h4>
<p>Asbagh s'est cramponné au sens littéral (<em>ẓāhir</em>) de sa parole — paix et bénédiction sur lui : « L'un de vous ne trouve-t-il pas trois pierres ? » — et a restreint l'istijmār à ce qui est de l'espèce même de la terre : car c'est une dispense (<em>rukhṣa</em>), dont on ne va pas au-delà de ce qui a été transmis. Et le <em>jumhūr</em> a étendu, par analogie avec elle [la pierre], tout autre [substitut] : tout solide pur, nettoyant, non nuisible et non vénéré. C'est que la dispense réside dans l'acte même, et non dans ce sur quoi il porte ; que la portée de sa motivation (<em>taʿlīl</em>) est le rejet de la bouse en tant qu'impureté (<em>rijās</em>), et non en tant que non-pierre ; et [cela] du fait de sa parole — paix et bénédiction sur lui : « Quand l'un de vous satisfait son besoin, qu'il se nettoie avec trois bâtons, ou trois pierres, ou trois poignées de terre » [rapporté par al-Dāraquṭnī] ; et parce que « pierres » est un intitulé (<em>laqab</em>) dont le <em>jumhūr</em> ne tire pas le sens restrictif (<em>mafʿūm</em>).</p>
<h4>La vertu de l'istitāba</h4>
<p>Sur la vertu de l'istitāba, il a été rapporté d'après Abū Ayyūb, Jābir ibn ʿAbd Allāh et Anas ibn Mālik — les Anṣārites —, d'après le Messager de Dieu — paix et bénédiction sur lui —, au sujet de ce verset :</p>
<p>« Ne te tiens jamais debout [dans cette mosquée]. Une mosquée fondée sur la piété, dès le premier jour, mérite davantage que tu t'y tiennes debout : y sont des hommes qui aiment à se purifier — et Dieu aime ceux qui se purifient. » (at-Tawba, 9 : 108 — le manuel imprime « 109 »)</p>
<p>[Verset restauré d'après le corpus canonique : l'emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>Il dit : « Ô communauté des Anṣār : Dieu vous a loués en bien au sujet de la purification (<em>ṭuhūr</em>) — quelle est donc cette purification qui est la vôtre ? » Ils dirent : « Ô Messager de Dieu, nous faisons nos ablutions pour la prière, et nous nous lavons de l'impureté majeure (<em>janāba</em>). » Le Messager de Dieu — paix et bénédiction sur lui — dit : « Y a-t-il autre chose encore, par-delà cela ? » Ils dirent : « Non — sinon que l'un de nous, quand il sortait de la selle, aimait à se nettoyer avec l'eau. » Il dit : « C'est cela même : faites-le donc. » [Rapporté par al-Dāraquṭnī]</p>
<h3>Deuxièmement : la vertu des ablutions</h3>
<p>Les ablutions ont une immense vertu, comme le hadith la dénombre ; en voici l'exposé :</p>
<h4>L'expiation des fautes des membres</h4>
<ul>
<li>La sortie des fautes du nez et de la bouche. ʿIyāḍ a dit : la mention de la sortie des fautes est une métaphore (<em>istiʿāra</em>), marquant l'obtention du pardon ; et al-Bājī a dit : il se peut que le rinçage de la bouche soit une expiation des fautes propres à la bouche — d'où l'expression de leur sortie de lui ; et il se peut que Dieu Très-Haut remette à l'homme le châtiment des fautes qu'il a acquises, même si elles ne sont pas propres à ce membre.</li>
<li>La sortie des fautes du visage et des deux yeux. Al-Bājī a dit : Il a fait des deux yeux une issue pour les fautes du visage — à l'exclusion de la bouche et du nez, car ces deux-là sont concernés par une purification prescrite dans les ablutions, à la différence des deux yeux.</li>
<li>La sortie des fautes de la tête et des deux oreilles. Al-Bājī a dit : Il a fait des deux oreilles une issue pour les fautes de la tête, tout en les distinguant par la prise d'eau qui leur est propre ; et Il n'a pas fait de la bouche et du nez des issues pour les fautes du visage, car ils sont antérieurs au visage : ils n'ont donc pas le statut du suiveur (<em>tabʿ</em>), et leurs fautes sortent d'eux avant de sortir du visage ; et les deux oreilles sont postérieures à la tête : elles ont donc le statut du suiveur. Fin de citation. Il y a en cela une indication que les fautes de la tête se rapportent à l'ouïe ; plus explicite encore est le hadith d'Abū Umāma rapporté par al-Ṭabarānī dans le <em>Ṣaghīr</em> : « Et quand il essuie sa tête, cela expie ce que ses deux oreilles ont entendu. »<br>
Et puisque l'ôtement de l'impureté concrète se fait par l'écoulement de l'eau — qui est le lavage —, il convenait, pour l'ôtement de l'impureté intérieure que sont les fautes, de mentionner l'écoulement qu'est le lavage, plutôt que l'essuyage.</li>
<li>La sortie des fautes de ses deux pieds : par le pardon de ce qu'il peut avoir perpétré comme fautes avec ses deux pieds.</li>
</ul>
<h4>Sa prière lui sera une surérogation</h4>
<p>Le sens de sa prière étant surérogatoire — comme le hadith de la leçon le stipule — est un surcroît de récompense pour lui, par-dessus la sortie des fautes et leur pardon ; et l'on sait quelle immense récompense il y a dans la marche [à la mosquée] et dans la prière.</p>
<h4>Quelles sont les fautes qu'expient les ablutions ?</h4>
<p>Les savants ont restreint le hadith de la leçon et ses semblables — parmi les hadiths comportant le pardon des fautes — aux fautes vénielles (<em>ṣaghāʾir</em>) ; quant aux fautes majeures (<em>kabāʾir</em>), rien ne les expie si ce n'est le repentir — du fait du hadith de Muslim dans son <em>Ṣaḥīḥ</em> : « Les cinq prières, du vendredi au vendredi, et du Ramadan au Ramadan : expiations de ce qui s'est écoulé entre elles, si l'on évite les fautes majeures. » Ils ont donc fait de la restriction contenue dans ce hadith une restriction de l'absolu posé dans les autres. Mais Ibn Daqīq al-ʿĪd a dit : cela appelle examen ; et Ibn al-Tīn a dit : on a divergé : les fautes majeures lui seront-elles pardonnées par ceci, s'il n'y a pas persisté, ou bien rien ne sera-t-il pardonné que les vénielles ? Il dit : « Et tout cela n'englobe pas les torts causés aux serviteurs de Dieu (<em>maẓālim al-ʿibād</em>). » Et il a dit dans <em>al-Mufhim</em> : il n'est pas exclu que certaines personnes voient se faire pardonner les majeures comme les vénielles, selon la sincérité qui les saisit et la bienveillance et les bienséances qu'elles observent — et c'est là faveur de Dieu, qu'Il accorde à qui Il veut.<br>
Et al-Nawawī a dit : selon ce dont les hadiths font état, cela expie s'il trouve à expier des vénielles ; s'il ne rencontre ni vénielle ni majeure, des mérites lui en sont inscrits et des degrés lui en sont élevés ; et s'il rencontre une majeure, ou des majeures, sans rencontrer de vénielle, nous espérons qu'il en résulte un allègement des majeures. Fin de citation.</p>
<h2>L'évaluation</h2>
<ol>
<li>Expose la vertu de l'istitāba en t'appuyant sur un texte religieux.</li>
<li>Mets en relief la vertu des ablutions.</li>
<li>Compare les ablutions et l'istitāba quant au statut juridique.</li>
</ol>
<h2>L'exploitation</h2>
<p>D'après Mālik, d'après al-ʿAlāʾ ibn ʿAbd al-Raḥmān, d'après son père, d'après Abū Hurayra : « Le Messager de Dieu — paix et bénédiction sur lui — sortit vers le cimetière et dit : "La paix soit sur vous, demeure d'un peuple de croyants ! Et nous, si Dieu le veut, vous rejoindrons certainement. Je souhaiterais avoir déjà vu nos frères." Ils dirent : Ô Messager de Dieu, ne sommes-nous pas tes frères ? Il dit : "Vous êtes mes compagnons ; et nos frères sont ceux qui ne sont pas encore venus — et je suis leur avant-coureur au Bassin (<em>ḥawḍ</em>)." Ils dirent : Ô Messager de Dieu, comment reconnaîtras-tu ceux de ta communauté qui viendront après toi ? Il dit : "Que t'en semble : si un homme a des chevaux au front blanc et aux extrémités blanches — dans un troupeau de chevaux noirs à la robe unie —, ne reconnaît-il pas les siens ?" Ils dirent : Certes, ô Messager de Dieu. Il dit : "Eux, ils viendront au Jour de la Résurrection le front et les extrémités resplendissants de leurs ablutions — et je suis leur avant-coureur au Bassin. Des hommes seront certes repoussés de mon Bassin comme on repousse le chameau égaré ! Je les appellerai : Eh ! venez ! Eh ! venez ! Eh ! venez ! On me dira : ils ont fait altération après toi. Je dirai : Qu'ils soient éloignés ! — qu'ils soient éloignés ! — qu'ils soient éloignés !" » [Muwaṭṭaʾ, n° 68]</p>
<ol>
<li>Expose la conséquence de l'altération (<em>tabdīl</em>) en matière religieuse.</li>
<li>Tire du hadith la vertu des ablutions qui y figure.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Quel est le statut — et quelle la sagesse — de l'essuyage sur les deux chaussettes (<em>masḥ ʿalā al-khuffayn</em>) ?</li>
<li>Expose la règle de l'essuyage sur le turban (<em>ʿimāma</em>) en lieu et place de la tête.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12884":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12884 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12884 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
