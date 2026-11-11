#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12961 (hadith-1es, la vertu de la
Fātiḥa et le statut de sa lecture dans la prière — Muwaṭṭaʾ n° 224-232,
+ Bukhārī-Muslim/Abū Dāwūd/Nasāʾī).

Conventions main (cf. 12875, 12884-12958 du même livre) :
- h1 « La vertu de la Fātiḥa et le statut de sa lecture dans la prière
  (faḍl al-Fātiḥa wa-ḥukm qirāʾatihā fī l-ṣalāh) », 18e leçon ; objectifs
  en infinitifs (source 1re personne — « صلى الله علي » OCR tronqué).
- Tamhīd : Muwaṭṭaʾ 226 — hadith qudsī « J'ai partagé la prière entre Moi
  et Mon serviteur, moitié moitié... et à Mon serviteur ce qu'il demanda ».
- Muwaṭṭaʾ 224 (Ubayy b. Kaʿb appelé en prière ; la main sur sa main à la
  porte de la mosquée ; « nulle pareille en Torah, Évangile ni Coran » ;
  Ubayy ralentit le pas ; « comment récites-tu quand tu ouvres ? » ; «
  c'est elle, les sept mathānī et le Coran immense qui m'est donné »),
  232 (Abū Hurayra : « l'un de vous a-t-il récité avec moi à l'instant ?
  ... je dis : quoi ! le Coran me serait disputé ? » — les gens cessèrent
  de réciter avec lui dans les jahriyya).
- Taḥlīl I : (1) réunir les sens du bien — Ibn ʿAbd al-Barr (la louange
  revenant à Dieu, la magnification, le Seigneur des mondes, le Maître des
  deux demeures, l'Invocé-Secourable, l'appel à la guidance, l'invocation
  noyau de l'adoration) + Bājī (un shaykh : elle tient lieu des autres
  sūras, nul ne tient lieu d'elle) + tafḍīl disputé (réponse : le mérite
  est dans les sens/récompenses, non dans l'attribut divin) + **Baqara
  2 : 105 restauré** ; (2) basmala hors Fātiḥa — al-ḥamdu nom de sūra
  (comme Yā-Sīn ; « c'est elle cette sūra... les sept mathānī ») + **
  Ḥijr 15 : 87 restauré** ; (3) l'obligation de répondre au Prophète
  même en prière — « wayhaka ! qu'est-ce qui t'a empêché de me répondre ?
  ne trouve-t-on pas en ce qui m'a été révélé... » + **Anfāl 8 : 24
  restauré** + « je n'y reviendrai pas, si Dieu veut » (Nasāʾī, Kubrā) ;
  (4) nulle prière sans elle — « lā ṣalāta li-man lam yaqraʾ
  bi-fātiḥati l-kitāb » (Bukhārī-Muslim) + « khidāj ×3 — incomplète »
  (Muwaṭṭaʾ 226) + Jābir (« sauf derrière un imam » — la règle uṣūl :
  l'exception mesure la généralité).
- Taḥlīl II : 3 écoles ; Mālik distingue : sirri — permis (Abū Hurayra /
  Abū l-Sāʾim le Persan « récite-la en toi-même » ; ʿUrwa, al-Qāsim b.
  Muḥammad, Nāfiʿ b. Jubayr — Muwaṭṭaʾ 227-229 « c'est le plus cher que
  j'aie entendu ») ; jahri — le maʾmūm se tait (la réprimande « le Coran
  me serait disputé » + « l'imam est là pour être suivi : quand il
  récite, taisez-vous » (Abū Dāwūd/Nasāʾī) + **Aʿrāf 7 : 204 restauré**).
- Istimḥār : Muwaṭṭaʾ 230 (Ibn ʿUmar : la récitation de l'imam suffit) +
  231 (Mālik : récite dans le sirri, s'abstient dans le jahri).
- Lexique : ḥattā taʿlama sūra, sabʿ al-mathānī (répétées à chaque rakʿa /
  louange doublée), unāziʿu (je le tire à moi — l'autre le tire de moi).
- Préparation préalable : leçon SUIVANTE 12980 (āmīn et taḥmīd).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>La vertu de la Fātiḥa et le statut de sa lecture dans la prière (<em>faḍl al-Fātiḥa wa-ḥukm qirāʾatihā fī l-ṣalāh</em>)</h1>
<p>Leçon sur la vertu de la Fātiḥa et le statut de sa lecture dans la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la dix-huitième leçon.</p>
<ol>
<li>Connaître la vertu de la sūra de la Fātiḥa et le statut de sa lecture dans la prière.</li>
<li>Distinguer le statut de la lecture de la Fātiḥa selon l’imam, le solitaire et le suivi.</li>
<li>Prendre pour modèle le Messager de Dieu — paix et bénédiction sur lui — dans sa récitation dans la prière.</li>
</ol>
<h2>Préambule</h2>
<p>Plusieurs hadiths vinrent du Prophète — paix et bénédiction sur lui — sur la vertu de la sūra de la Fātiḥa ; parmi eux ce qui fut rapporté d’Abū Hurayra — que Dieu soit satisfait de lui —, remontant [au Prophète] : « Dieu — Béni et Très-Haut — a dit : J’ai partagé la prière entre Moi et Mon serviteur, en deux moitiés : une moitié à Moi, une moitié à Mon serviteur — et à Mon serviteur ce qu’il a demandé… » [Muwaṭṭaʾ, n° 226]</p>
<p>Quelle est donc la vertu de la sūra de la Fātiḥa ? Et quel est le statut de sa lecture dans la prière ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après al-ʿAlāʾ ibn ʿAbd al-Raḥmān ibn Yaʿqūb : « qu’Abū Saʿīd, affranchi de ʿĀmir ibn Kurayz, l’informa : Le Messager de Dieu — paix et bénédiction sur lui — appela Ubayy ibn Kaʿb pendant qu’il priait ; quand il eut achevé sa prière, il le rejoignit — le Messager de Dieu — paix et bénédiction sur lui — posa sa main sur la sienne, alors qu’il voulait sortir par la porte de la mosquée, et dit : “J’espère bien que tu ne sortiras pas de la mosquée avant d’avoir appris une sūra qui n’a point de pareille en ce que Dieu a fait descendre — ni dans la Torah, ni dans l’Évangile, ni dans le Coran.” Ubayy dit : je ralentis donc ma marche dans l’espoir de cela ; puis je dis : Ô Messager de Dieu, la sūra que tu m’as promise ! Il dit : “Comment récites-tu quand tu ouvres la prière ?” Il dit : je récitai [la Fātiḥa] jusqu’à en atteindre la fin. Le Messager de Dieu — paix et bénédiction sur lui — dit : “C’est elle, cette sūra — et ce sont les sept répétées (<em>al-sabʿ al-mathānī</em>) et le Coran immense qui m’a été donné.” » [Muwaṭṭaʾ, n° 224]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Ibn ʿUkayma al-Laythī, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — sortit d’une prière où il avait récité à voix haute, et dit : “L’un de vous a-t-il récité avec moi à l’instant ?” Un homme dit : Oui, moi, ô Messager de Dieu. Le Messager de Dieu — paix et bénédiction sur lui — dit : “Je dis : quoi ! le Coran me serait-il disputé ?” — les gens cessèrent alors de réciter avec le Messager de Dieu — paix et bénédiction sur lui — en ce qu’il récitait à voix haute, quand ils eurent entendu cela du Messager de Dieu — paix et bénédiction sur lui. » [Muwaṭṭaʾ, n° 232]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>ḥattā taʿlama sūra</em> (« avant d’avoir appris une sūra ») : c’est-à-dire : que tu apprennes d’elle ce que tu ne connaissais pas auparavant — sinon, il la connaissait déjà et la savait par cœur.</li>
<li><em>al-sabʿ al-mathānī</em> (« les sept répétées ») : on vise les sept versets — car elles sont sept versets, nommés <em>mathānī</em> parce qu’elles sont reprises à chaque rakʿa — c’est-à-dire répétées — ou parce que la louange de Dieu y est doublée.</li>
<li><em>unāziʿu al-Qurʾān</em> (« le Coran me serait disputé ») : avec fatha du <em>zāy</em>, au passif — c’est-à-dire : je tire sur sa récitation, comme si je l’attirais à moi contre un autre, et un autre l’attire à lui contre moi.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Où la vertu de la sūra de la Fātiḥa se manifeste-t-elle sur le reste du Coran ?</li>
<li>Cite le statut de la lecture de la Fātiḥa dans la prière.</li>
<li>Extrais des hadiths l’école de l’imam Mālik sur le statut de la lecture de la Fātiḥa derrière l’imam.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la vertu de la sūra de la Fātiḥa</h3>
<p>Le Prophète — paix et bénédiction sur lui — mentionna en maints hadiths la vertu de la sūra de la Fātiḥa et les privilèges qu’elle renferme ; parmi cela :</p>
<ul>
<li>Qu’elle rassemble les sens du bien, du mérite et de la bénédiction — c’est le sens de sa parole — paix et bénédiction sur lui —, au hadith d’Ubayy ibn Kaʿb : « qui n’a point de pareille en ce que Dieu a fait descendre — ni dans la Torah, ni dans l’Évangile, ni dans le Coran. » Ibn ʿAbd al-Barr a dit, sur le sens du hadith : il veut dire [par sa supériorité] son rassemblement des sens du bien — car elle contient la louange de Dieu par le <em>ḥamd</em>, qui Lui revient en propre : tout bien vient de Lui, et si un autre que Lui est loué, la louange lui revient [en fin de compte] ; elle contient Sa magnification, et qu’Il est le Seigneur du monde entier, le Maître de la demeure-bas et de la demeure-dernier, l’Adoré-Invocable au secours ; elle contient l’appel à la guidance et l’évitement de qui s’égarra — et l’invocation est le noyau de l’adoration : c’est la sūra la plus rassembleuse du bien. Al-Bājī a dit : un de nos shaykhs mentionna que le sens de cela est qu’elle tient lieu des autres [sūras] dans la prière, et que nul ne tient lieu d’elle — tandis que les autres sūras se suppléent l’une l’autre. Et certains savants se fondèrent sur sa parole — paix et bénédiction sur lui — : « qui n’a point de pareille… » pour la permission de préférer certaines [parties] du Coran à d’autres ; un groupe de savants l’interdit — estimant que le préféré-contre est diminué du degré du préféré, or les noms de Dieu, Ses attributs et Sa parole n’ont aucune déficience. On y répondit : le sens de la préférence est que la récompense des unes est plus grande que la récompense des autres — la préférence tient aux sens, non à l’attribut ; et appuie la préférence la parole de Dieu — Exalté :</li>
</ul>
<p>« …Mais Dieu réserve à qui Il veut Sa miséricorde — Dieu est détenteur du faveur immense. » (al-Baqara, 2 : 105, extrait)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<ul>
<li>Que la basmala n’est pas de la Fātiḥa — certains le déduisirent [du hadith], car Ubayy, quand le Prophète — paix et bénédiction sur lui — lui demanda sa récitation dans la prière, dit : « je récitai “La louange à Dieu, Seigneur des mondes” » — mais il n’y a là nulle preuve : car “La louange à Dieu, Seigneur des mondes” est un nom de la sūra, comme l’on dit : je récitai <em>Yā-Sīn</em>, et les autres noms des sūras. Et ce qui montre que c’est la sūra entière qui est visée : sa parole — paix et bénédiction sur lui — : “C’est elle, cette sūra” — et sa parole : “ce sont les sept répétées”, mentionnées en la parole de Dieu — Exalté :</li>
</ul>
<p>« Nous t’avons donné sept [versets] parmi les répétées, et le Coran immense. » (al-Ḥijr, 15 : 87)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>— les “sept” visés étant les versets.</p>
<p>Le hadith montre aussi l’obligation de répondre au Prophète — paix et bénédiction sur lui —, fût-on appelé dans la prière, et que sa réponse [à lui] n’invalide pas la prière — d’après ce qui vient dans le hadith, par la narration d’Abū Hurayra : « Malheur à toi ! qu’est-ce qui t’a empêché, quand je t’ai appelé, de me répondre ? Ne trouve-t-on pas en ce que Dieu m’a révélé :</p>
<p>« Ô vous qui croyez ! répondez à Dieu et au Messager quand Il vous appelle à ce qui vous donne la vie… » (al-Anfāl, 8 : 24, extrait)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>— J’ai dit : Si, ô Messager de Dieu — je n’y reviendrai plus, si Dieu veut. » [Rapporté par an-Nasāʾī dans la <em>Sunan al-kubrā</em>]</p>
<ul>
<li>Que la récitation, dans la prière, n’est valable que par elle — d’après ce qui fut rapporté de lui — paix et bénédiction sur lui — : « Point de prière pour qui ne récite pas la Fātiḥat al-Kitāb. » [Rapporté par al-Bukhārī et Muslim] Et au hadith d’Abū Hurayra du chapitre : « Quiconque prie une prière sans y réciter la Mère du Coran, elle est boiteuse — boiteuse — boiteuse — incomplète. » [Muwaṭṭaʾ, n° 226] — hadith porté, chez Mālik et ses alliés, sur l’imam et le solitaire, d’après ce qui fut rapporté de Jābir ibn ʿAbd Allāh : « Quiconque prie une rakʿa sans y réciter la Mère du Coran n’a pas prié — sauf derrière un imam » : il nie la validité de la prière à qui ne récite pas la Mère du Coran, et excepte de cela le suivi — on sait donc que l’imam a le statut du solitaire, par la règle uṣūlique : “l’exception mesure la généralité”.</li>
</ul>
<h3>Deuxièmement : le statut de la lecture de la Fātiḥa derrière l’imam</h3>
<p>Les savants divergèrent sur la lecture de la Fātiḥa par le suivi derrière l’imam, en trois avis : les uns l’obligèrent, les autres l’interdirent, d’autres enfin distinguèrent la prière récitée à voix haute de la prière silencieuse — et c’est l’école [mālikite]. En voici l’exposé :</p>
<h4>Le statut de la lecture de la Fātiḥa derrière l’imam en ce qui se récite à voix basse</h4>
<p>L’imam Mālik tint la permission de la réciter derrière l’imam dans la prière silencieuse — et c’est ce qui fut rapporté des Compagnons et des Suivants :</p>
<ul>
<li>des Compagnons : ce qui fut rapporté d’Abū Hurayra — que Dieu soit satisfait de lui — quand Abū l-Sāʾim, affranchi de Hishām ibn Zuhra, lui demanda : « Ô Abū Hurayra, il m’arrive d’être derrière l’imam… ? » Il dit : il me serra le bras, puis dit : “Récite-la en toi-même, ô Persan !..” » [Muwaṭṭaʾ, n° 226]</li>
<li>des Suivants : ce qui fut rapporté de Hishām ibn ʿUrwa, d’après son père, d’al-Qāsim ibn Muḥammad et de Nāfiʿ ibn Jubayr ibn Muṭʿim — tous récitaient derrière l’imam en ce que l’imam ne récitait pas à voix haute.</li>
</ul>
<p>L’imam Mālik dit, après avoir mentionné ces athars : « Et c’est ce que j’ai entendu de plus aimable en la matière. » [Muwaṭṭaʾ, n° 227-229]</p>
<h4>Le statut de la lecture de la Fātiḥa derrière l’imam en ce qui se récite à voix haute</h4>
<p>L’imam Mālik tint que le suivi ne récite pas derrière l’imam en ce qu’il récite à voix haute. Sa preuve : le désaveu du Prophète — paix et bénédiction sur lui — à celui des Compagnons qui récitait derrière lui, comme il vient au hadith d’Abū Hurayra — que Dieu soit satisfait de lui — : « Je dis : quoi ! le Coran me serait-il disputé ? » — le rapporteur du hadith dit : « Les gens cessèrent alors de réciter avec le Messager de Dieu — paix et bénédiction sur lui — en ce qu’il récitait à voix haute, quand ils eurent entendu cela de lui » ; et sa parole — paix et bénédiction sur lui — : « L’imam n’est institué que pour être suivi : quand il fait le takbīr, faites-le ; et quand il récite, taisez-vous. » [Rapporté par Abū Dāwūd et an-Nasāʾī] Et par la généralité de la parole de Dieu — Exalté :</p>
<p>« Et quand le Coran est récité, écoutez-le et soyez silencieux — peut-être vous sera-t-il fait miséricorde. » (al-Aʿrāf, 7 : 204)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h2>L’évaluation</h2>
<ol>
<li>Appuie par un texte légal la vertu de la Fātiḥa.</li>
<li>Cite l’école de l’imam Mālik et sa preuve sur le statut de la lecture de la Fātiḥa derrière l’imam.</li>
<li>Qu’indique sa parole — paix et bénédiction sur lui — : « Je dis : quoi ! le Coran me serait-il disputé ? » ?</li>
</ol>
<h2>L’exploitation</h2>
<ul>
<li>D’après Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar, quand on lui demandait : “L’un [de nous] récite-t-il derrière l’imam ?”, disait : Quand l’un de vous prie derrière l’imam, la récitation de l’imam lui suffit ; et quand il prie seul, qu’il récite. — et ʿAbd Allāh ibn ʿUmar ne récitait pas derrière l’imam. » [Muwaṭṭaʾ, n° 230]</li>
<li>Yaḥyā a dit : « j’ai entendu Mālik dire : “La chose chez nous est que l’homme récite derrière l’imam en ce que l’imam ne récite pas à voix haute, et qu’il délaisse la récitation en ce que l’imam récite à voix haute.” » [Muwaṭṭaʾ, n° 231]</li>
</ul>
<ol>
<li>Extrais de la parole d’Ibn ʿUmar et de celle de l’imam Mālik le statut de la lecture du suivi derrière l’imam.</li>
<li>Quel est le rapport de la parole de l’imam Mālik à celle d’Ibn ʿUmar ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Explique ce qui suit : <em>āmīn</em> (« ainsi soit-il ») – <em>samiʿa Llāhu li-man ḥamidahu</em> (« Dieu entend celui qui Le loue »).</li>
<li>Cite le mérite du <em>taʾmīn</em> (dire āmīn) et du <em>taḥmīd</em> (la louange) dans la prière.</li>
<li>Que signifie la concordance du <em>taʾmīn</em> de celui qui prie avec le <em>taʾmīn</em> des anges ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12961":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12961 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12961 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
