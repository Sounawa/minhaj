#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12998 (hadith-1es, des règles et de
l'étiquette du vendredi — suite — Muwaṭṭaʾ n° 281/283/284/292/293/294/
296/297/298/299 + Muslim + Bukhārī/Nasāʾī + Aḥmad/Abū Dāwūd).

Conventions main (cf. 12875-12995 du même livre) :
- h1 « Des décisions et de l'étiquette du vendredi — suite (min
  aḥkām al-jumuʿa wa-ādābihā — tamām) », 24e leçon, 2e partie,
  complément de la 1ʳᵉ (titleFr officiel « …, une suite »
  normalisé « — suite » comme le source « -تتمة- »).
- Préambule : règles/sunnas tenant compte des états du musulman
  (masbūq, voyageur) ; questions : étiquettes + masbūq et rāʿif.
- Hadiths : 281 (Ibn Shihāb : « qui atteint une rakʿa du vendredi
  en prie une autre avec — c'est la sunna ») + 284 (rāʿif sorti
  pendant le prêche, non revenu → 4 rakʿas) ; 292 (l'heure
  d'exaucement — « nul serviteur musulman ne la rencontre debout en
  prière, demandant à Dieu quelque chose, sans qu'Il la lui donne »
  + geste de la main la rapetissant) ; 296 (Ibn Ḥazm/Abū Hurayra :
  prier sur le dos de la ḥarra vaut mieux que s'asseoir puis
  enjamber les nuques).
- Lexique : lā yuwāfiquhā, yuqalliluhā, ẓahr al-ḥarra (terre de
  pierres noires comme brûlées, aux portes de Médine).
- Taḥlīl I : 3 écoles du masbūq d'une rakʿa (Mālik : vendredi
  atteint — sunna + pratique médinoise preuve ; Ibn Masʿūd/Ibn
  ʿUmar/Anas/al-Layth/Shāfiʿī/Aḥmad ; Mujāhid/ʿAṭāʾ : 4 rakʿas —
  consensus sans sermon ; Abū Ḥanīfa/Abū Yūsuf : iḥrām avant le
  salut → 2 rakʿas, Bukhārī « ce que vous atteignez, priez-le ;
  ce qui vous échappe, complétez-le ») ; rājiḥ = jumhūr ; le
  pressé qui ne peut se prosterner → Ẓuhr de 4 (283) ; ruʿāf :
  rien atteint → 4 ; une rakʿa + ruʿāf → bâtir une autre (sans
  parole/souillure/dos tourné/dépassement du lieu le plus proche)
  — jumhūr.
- Taḥlīl II : l'heure cachée comme la Nuit du Destin — zawāl →
  fin de la prière ; sortie de l'imam → départ (Muslim/Abū Mūsā
  « entre l'assise de l'imam et la fin de la prière ») ; après
  ʿAṣr → coucher (ʿAbd Allāh b. Salām vs l'objection d'Abū
  Hurayra — « qui s'assied attendant la prière est en prière
  jusqu'à ce qu'il prie » — Muwaṭṭaʾ 293).
- Taḥlīl III : huile + parfum (Ibn ʿUmar/Nāfiʿ — sauf iḥrām ;
  Salmān Ṣaḥīḥ « lavage + purification + huile ou parfum + ne pas
  séparer deux [hommes] + prier + se taire = pardon d'un vendredi
  à l'autre » ; 294 les deux vêtements) ; ne pas enjamber les
  nuques (296 + Ibn ʿAbd al-Barr : sens remontant ; Aḥmad/Abū
  Dāwūd/Ibn Ḥibbān/Ḥākim d'Abū Saʿīd et Abū Hurayra : le hadith
  complet de l'expiation) ; faire face à l'imam (297 + Ibn
  ʿAbd al-Barr : pas de divergence ; al-Shaʿbī ; Bayhaqī/Ibn
  ʿUmar ; Nuʿaym b. Ḥammād/Anas ; Ibn al-Mundhir) ; récitation —
  Muwaṭṭaʾ 298 (al-Nuʿmān b. Bashīr : après la sūra du Vendredi,
  Hal atāka ḥadīthu l-ghāshiya) + Vendredi/Munāfiqūn (Shāfiʿī, Abū
  Hurayra, ʿAlī) + **TROU OCR RESTAURÉ** : les deux sūras des
  ʿīd et du vendredi = Sabbiḥ isma rabbika l-aʿlā + Hal atāka
  ḥadīthu l-ghāshiya (vérifié web : Muslim de Nuʿmān b. Bashīr —
  même rapporteur que 298 ; la fin du manuel « quand ʿīd et
  vendredi coïncident il lit les deux » scelle l'identification) ;
  iḥtibāʾ (permis — Ibn Bukayr/Mālik/Ibn ʿUmar vs interdit —
  sommeil + ʿawra) ; délaisser 3 vendredis sans excuse = cœur
  scellé (299 ; ʿudhr = boue, ʿilla = maladie ; ṭabʿ sukūn/voyelle).
- Istimḥār : 293 (Abū Hurayra : « le meilleur jour où se lève le
  soleil… : en lui Adam fut créé, chassé, repentit, mourut ; l'Heure
  s'y dresse ; toute bête écoute le vendredi au lever, craignant
  l'Heure — hormis jinn et hommes ; l'heure d'exaucement »).
- Préparation préalable : leçon SUIVANTE 13001 (tarāwīḥ — définition,
  institution, nombre des rakʿas).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Des décisions et de l’étiquette du vendredi — suite (<em>min aḥkām al-jumuʿa wa-ādābihā — tamām</em>)</h1>
<p>Leçon sur les règles et l’étiquette du vendredi, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-quatrième leçon, deuxième partie, complément de la première.</p>
<ul>
<li>Connaître quelques-unes des sunnas et étiquettes propres à la prière du vendredi.</li>
<li>Comprendre la vertu de l’heure d’exaucement le jour du vendredi.</li>
<li>Veiller à me conformer aux règles et à l’étiquette du vendredi.</li>
</ul>
<h2>Préambule</h2>
<p>Il vint, au sujet du jour du vendredi, maints rapports indiquant son rang et sa faveur ; ce jour fut aussi caractérisé par des règles, des sunnas et des étiquettes qui prennent en compte les états du musulman et ses circonstances — être devancé, être en voyage, ou autre.<br>
Quelles sont les étiquettes du jour du vendredi ? Et quels sont les statuts du devancé et de celui au nez duquel le sang coule, en la prière du vendredi ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Ibn Shihāb : « qu’il disait : Quiconque atteint, de la prière du vendredi, une rakʿa, qu’il en prie une autre avec elle. Yaḥyā a dit : Mālik dit : Ibn Shihāb dit : “Et c’est là la sunna.” » [Muwaṭṭaʾ, n° 281]<br>
Yaḥyā a dit : Mālik dit : « Quiconque saigne du nez le jour du vendredi pendant que l’imam prêche, puis sort et ne revient pas jusqu’à ce que l’imam en ait fini de sa prière — il prie quatre [rakʿas]. » [Muwaṭṭaʾ, n° 284]</li>
<li>D’après Mālik, d’après Abū l-Zinad, d’après al-Aʿraj, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — mentionna le jour du vendredi et dit : En lui est une heure qu’aucun serviteur musulman ne rencontre, debout en prière, demandant à Dieu quelque chose, sans qu’Il ne la lui donne — et le Messager de Dieu — paix et bénédiction sur lui — fit un geste de la main pour la rapetisser. » [Muwaṭṭaʾ, n° 292]</li>
<li>D’après Mālik, d’après ʿAbd Allāh ibn Abī Bakr ibn Ḥazm, d’après celui qui le lui rapporta, d’après Abū Hurayra : « qu’il disait : Que l’un de vous prie sur le dos de la <em>ḥarra</em> vaut mieux pour lui que de s’asseoir jusqu’à ce que, l’imam se levant pour prêcher, il vienne enjamber les nuques des gens le jour du vendredi. » [Muwaṭṭaʾ, n° 296]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>lā yuwāfiquhā</em> (« ne la rencontre ») : ne tombe pas sur elle.</li>
<li><em>yuqalliluhā</em> (« la rapetisser ») : il indique par le geste la brièveté de son temps.</li>
<li><em>bi-ẓahr al-ḥarra</em> (« sur le dos de la ḥarra ») : terre de pierres noires, comme si le feu l’avait brûlée, à l’extérieur de Médine.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Par quoi le vendredi fut-il préféré au reste des jours ?</li>
<li>Explicite le statut de qui vint en retard et n’atteignit qu’une seule rakʿa de la prière du vendredi.</li>
<li>Que doit faire celui au nez duquel le sang coule, dans la deuxième rakʿa du jour du vendredi ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : des règles du jour du vendredi</h3>
<p>La leçon précédente parla de quelques règles du vendredi ; voici la suite :</p>
<h4>Le statut de qui atteint une rakʿa de la prière du vendredi</h4>
<p>En la question, trois avis :</p>
<ul>
<li>Le premier : quiconque vint en retard pour une excuse légale le vendredi et trouva l’imam ayant fini les deux sermons et entrepris la prière, atteignant avec lui une seule rakʿa — il aura atteint la prière du vendredi : c’est la parole de Mālik. [Ibn Shihāb] explicita que cela est la sunna et la pratique des gens de Médine — leur pratique est preuve. Du même avis : Ibn Masʿūd, Ibn ʿUmar, Anas et d’autres des Compagnons et des Suivants, al-Layth, al-Shāfiʿī et Aḥmad. Et cela est une généralité embrassant le vendredi et les autres prières obligatoires.</li>
<li>Le deuxième : la parole de Mujāhid, ʿAṭāʾ et d’un groupe de Suivants : celui qui a manqué le sermon prie quatre — appuyée du consensus que, quand l’imam ne prêche pas, ils ne prient que quatre.</li>
<li>Le troisième : la parole d’Abū Ḥanīfa, d’Abū Yūsuf et d’un groupe : quiconque entre en prière avant le salut de l’imam prie deux rakʿas, du hadith d’al-Bukhārī : “Ce que vous atteignez, priez-le ; et ce qui vous échappe, complétez-le” — il a atteint une partie avant le salut, il lui est commandé d’entrer avec lui, et ce qui lui échappa est de deux rakʿas qu’il accomplit : il aura ainsi atteint la vertu du vendredi.</li>
</ul>
<p>Et le prépondérant de ces avis est l’école du <em>jumhūr</em>, dont l’imam Mālik.</p>
<p>S’y rattache ce que mentionna Mālik : celui que la foule atteignit et ne put se prosterner — “qu’il se prosterne quand les gens se lèvent ; et s’il ne peut se prosterner jusqu’à ce que l’imam en finisse de sa prière, il m’est plus aimable qu’il entreprenne sa prière en Ẓuhr de quatre” [Muwaṭṭaʾ, n° 283] — à titre obligatoire, car il n’a point atteint avec lui une rakʿa sur laquelle bâtir.</p>
<h4>Le statut de qui saigne du nez le jour du vendredi</h4>
<p>L’imam Mālik dit : « Quiconque saigne du nez le jour du vendredi pendant que l’imam prêche, puis sort et ne revient pas jusqu’à ce que l’imam en ait fini de sa prière — il prie quatre [rakʿas]. » [Muwaṭṭaʾ, n° 284] — parce qu’il n’a rien atteint. Il dit aussi, de celui qui s’incline d’une rakʿa avec l’imam le vendredi, puis saigne du nez et sort laver le sang, et revient alors que l’imam a prié les deux rakʿas : qu’il bâtisse avec une autre rakʿa — pourvu qu’il n’ait point parlé, point foulé une souillure, point tourné le dos sans excuse, et point dépassé le lieu le plus proche possible. De même l’affaire quand le touche une chose qui requiert de sortir pendant que l’imam prêche — l’annulation d’ablutions ou autre. Du même avis : le <em>jumhūr</em> des juristes.</p>
<h3>Deuxièmement : l’heure d’exaucement le jour du vendredi</h3>
<p>En le jour du vendredi est une heure qu’aucun musulman ne rencontre sans que Dieu l’exauce. Cette heure fut cachée, comme fut cachée la Nuit du Destin. Les rapports divergèrent sur sa détermination : il fut rapporté qu’elle va du début du déclin du soleil à la fin de la prière ; il fut dit : de la sortie de l’imam au minbar à son départ — selon ce qui vient dans la narration de Muslim, d’après Abū Mūsā : “J’entendis le Messager de Dieu — paix et bénédiction sur lui — dire : Elle est entre l’assise de l’imam et l’achèvement de la prière…” ; et il fut dit : d’après la prière de l’ʿaṣr au coucher du soleil — et c’est l’avis où alla ʿAbd Allāh ibn Salām — que Dieu soit satisfait de lui — quand Abū Hurayra l’interrogea ; Abū Hurayra dit, en objectant : “… je dis : Comment serait-elle la dernière heure d’un vendredi, alors que le Messager de Dieu — paix et bénédiction sur lui — a dit : aucun serviteur musulman ne la rencontre alors qu’il prie — et cette heure est une heure où l’on ne prie point ? ʿAbd Allāh ibn Salām dit : Le Messager de Dieu — paix et bénédiction sur lui — n’a-t-il pas dit : quiconque s’assied en une assise attendant la prière, il est en prière jusqu’à ce qu’il prie ? Abū Hurayra dit : je dis : Si. Il dit : C’est cela même.” » [Muwaṭṭaʾ, n° 293]</p>
<h3>Troisièmement : des sunnas et étiquettes du jour du vendredi</h3>
<h4>La recommandation de la parure et du parfum</h4>
<p>Mālik rapporta, d’après Nāfiʿ, d’après Ibn ʿUmar : il ne partait pas au vendredi sans s’oindre — c’est-à-dire employer l’huile pour ôter le dépeigné des cheveux — et se parfumer : il réunissait les deux, en signe de parure et de bonne odeur pour ce jour — sauf s’il était en état de sacralisation pour le pèlerinage ou la ʿumra : il ne les faisait pas. Dans le <em>Ṣaḥīḥ</em>, de Salmān, remontant [au Prophète] : “Qu’aucun homme ne se lave le jour du vendredi et ne se purifie de toute la pureté dont il peut, ne s’oigne de son huile ou ne touche du parfum de sa maison, puis ne sorte sans séparer deux [hommes], puis ne prie ce qui lui est écrit, puis ne se taise quand l’imam parle — sans qu’il ne lui soit pardonné ce qui est entre ce vendredi et l’autre.” [Rapporté par al-Bukhārī et an-Nasāʾī]<br>
Et appuie cela le hadith de l’Envoyé — paix et bénédiction sur lui — : « Il sied à quiconque d’entre vous, s’il prend deux vêtements pour son vendredi en dehors de ses vêtements de besogne. » [Muwaṭṭaʾ, n° 294] — l’exhortation à prendre un vêtement propre au jour du vendredi.</p>
<h4>L’interdiction d’enjamber les nuques</h4>
<p>L’Envoyé — paix et bénédiction sur lui — encouragea l’empressement vers la mosquée le vendredi, ordonna de s’asseoir là où s’achève le cercle, et interdit de léser les orants par quelque genre de lésion que ce soit — y compris enjamber leurs nuques. Il fut rapporté d’Abū Hurayra qu’il disait : « Que l’un de vous prie sur le dos de la <em>ḥarra</em> vaut mieux pour lui que de s’asseoir jusqu’à ce que, l’imam se levant pour prêcher, il vienne enjamber les nuques des gens le jour du vendredi. » Ibn ʿAbd al-Barr a dit : ce sens est remontant [au Prophète] ; puis il conduisit ce que firent sortir Aḥmad et Abū Dāwūd — validé par Ibn Ḥibbān et al-Ḥākim — d’après Abū Saʿīd et Abū Hurayra : le Prophète — paix et bénédiction sur lui — dit : “Quiconque se lave le vendredi, se frotte les dents, touche du parfum s’il en a, revêt le plus beau de ses vêtements, puis sort jusqu’à venir à la mosquée sans enjamber les nuques des gens, puis s’incline autant que Dieu veut, puis se tait quand l’imam sort — ne parlant pas jusqu’à ce qu’il en finisse de sa prière — cela est expiation de ce qui est entre ce vendredi et l’autre.”</p>
<h4>Faire face à l’imam pendant son sermon</h4>
<p>Mālik dit : « La sunna chez nous est que les gens font face à l’imam le jour du vendredi quand il veut prêcher, quiconque d’eux jouxte la qibla ou autre chose. » [Muwaṭṭaʾ, n° 297] — pour qu’ils se consacrent à écouter son exhortation, méditent ses paroles, ne s’occupent pas d’autre chose, et que cela soit plus enclin à leur profit : qu’ils œuvrent selon ce qu’ils apprennent. Ibn ʿAbd al-Barr a dit : ils ne divergèrent pas en cela, et je n’y connais pas de hadith pourvu d’une chaîne — sinon que al-Shaʿbī dit : de la sunna est de faire face à l’imam le vendredi. Al-Bayhaqī rapporta qu’Ibn ʿUmar achevait son <em>tasbīḥ</em> le vendredi avant la sortie de l’imam ; quand celui-ci sortait, il ne s’asseyait pas avant de lui faire face. Nuʿaym ibn Ḥammād rapporta, par une chaîne saine, d’après Anas : quand l’imam entrait en son sermon le vendredi, il lui faisait face de son visage jusqu’à ce qu’il en finît. Ibn al-Mundhir a dit : je n’y connais pas de divergence entre les savants.</p>
<h4>La récitation le jour du vendredi</h4>
<p>Mālik rapporta dans le <em>Muwaṭṭaʾ</em>, d’après al-Nuʿmān ibn Bashīr : « que le Messager de Dieu — paix et bénédiction sur lui — récitait, à la suite de la sūra du Vendredi, <em>Hal atāka ḥadīthu l-ghāshiya</em> (“T’est-il parvenu le récit de l’Enveloppante ?”) » [Muwaṭṭaʾ, n° 298]. Il y a des rapports sains sur sa récitation en la prière du vendredi, parmi eux : ce qui fut rapporté du Prophète — paix et bénédiction sur lui — qu’il récita la sūra du Vendredi en la première rakʿa et <em>Idhā jāʾaka l-munāfiqūn</em> en la deuxième — al-Shāfiʿī le choisit, et c’est la parole d’Abū Hurayra et de ʿAlī — que Dieu soit satisfait des deux. Parmi eux : ce qui fut rapporté qu’il — paix et bénédiction sur lui — récitait aux deux fêtes et au vendredi <em>Sabbiḥ isma rabbika l-aʿlā</em> (“Glorifie le nom de ton Seigneur, le Très-Haut !”) et <em>Hal atāka ḥadīthu l-ghāshiya</em>. Et quand les deux fêtes se rencontrent — la fête du vendredi et l’une des deux fêtes, la Rupture ou le Sacrifice — en un jour, il récitait les deux.</p>
<p>[Les deux sūras de la récitation des fêtes et du vendredi restaurées d’après le texte attesté chez Muslim (même rapporteur : al-Nuʿmān ibn Bashīr) : la coupure de paragraphe dans la source numérisée avait perdu leur nom ; la fin du passage — “quand les deux fêtes se rencontrent en un jour, il récitait les deux” — scelle l’identification.]</p>
<h4>L’iḥtibāʾ</h4>
<p>Il est de joindre le dos aux jambes dans un vêtement ou autre — il peut aussi être des deux mains. Vinrent sur l’<em>iḥtibāʾ</em> deux paroles :</p>
<ul>
<li>La première, la permission : il vient dans la narration d’Ibn Bukayr, de Mālik, qu’il lui parvint qu’ʿAbd Allāh ibn ʿUmar faisait l’<em>iḥtibāʾ</em> le vendredi pendant que l’imam prêchait ; il dit : il ne fut pas rapporté d’aucun des Compagnons le contraire, et il ne fut pas rapporté de qui que ce soit des Suivants la répréhension de l’<em>iḥtibāʾ</em> le vendredi, sans qu’il soit aussi rapporté de lui la permission.</li>
<li>La deuxième, la non-permission, à cause de son interdiction — paix et bénédiction sur lui — de l’<em>iḥtibāʾ</em> le vendredi pendant que l’imam prêche. L’interdiction fut motivée par le fait que l’<em>iḥtibāʾ</em> est un lieu d’origine du sommeil, et une mise à nu de la nudité.</li>
</ul>
<h4>Délaisser le vendredi sans excuse</h4>
<p>Il vint du Prophète — paix et bénédiction sur lui — qu’il dit : « Quiconque délaisse le vendredi trois fois, sans excuse ni indisposition, Dieu scelle son cœur. » [Muwaṭṭaʾ, n° 299] — l’excuse voulue : la boue épaisse et ce qui s’y ramène ; l’indisposition : la maladie et ce qui s’y ramène. “Dieu scelle son cœur” : Il le cachète, le couvre et le prive de Ses bontés — rien du bien ne l’atteint ; ou Il met en lui l’ignorance, la dureté et la rudesse ; ou Il fait son cœur un cœur d’hypocrite. Le <em>ṭabʿ</em>, avec sukūn du <em>bāʾ</em> : le cachet ; avec voyelle : la souillure.</p>
<h2>L’évaluation</h2>
<ol>
<li>Explicite l’avis prépondérant sur ce par quoi la prière du vendredi est atteinte.</li>
<li>Cite quelques-unes des étiquettes que l’orant doit observer le jour du vendredi.</li>
<li>Qu’entraîne le délaissement du vendredi sans excuse ?</li>
</ol>
<h2>L’exploitation</h2>
<p>Mālik rapporta, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — dit : “… Le meilleur jour où se lève le soleil est le jour du vendredi : en lui Adam fut créé ; en lui il fut descendu du Paradis ; en lui il reçut le repentir ; en lui il mourut ; en lui l’Heure se dressera. Et il n’est de bête qu’elle n’écoute, le vendredi, depuis que paraît l’aube jusqu’à ce que se lève le soleil — en crainte de l’Heure —, hormis les jinn et les hommes. Et en lui est une heure qu’aucun serviteur musulman ne rencontre alors qu’il prie, demandant à Dieu quelque chose, sans qu’Il ne la lui donne.” » [Muwaṭṭaʾ, n° 293]</p>
<ul>
<li>Extrais du hadith les vertus du jour du vendredi qu’il renferme.</li>
</ul>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ul>
<li>Qu’entend-on par la prière du <em>tarāwīḥ</em> ?</li>
<li>Quand la prière du <em>tarāwīḥ</em> fut-elle instituée en sunna ?</li>
<li>Cite les paroles venues sur le nombre de ses rakʿas.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12998":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12998 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12998 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
