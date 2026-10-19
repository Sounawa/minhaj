#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12929 (hadith-1es, dispositions de
l'appel à la prière — Muwaṭṭaʾ n° 174, 179-183, 188, + Bukhārī Anas).

Conventions main (cf. 12875, 12884-12924 du même livre) :
- h1 « Dispositions de l'appel à la prière (aḥkām al-nidāʾ li-l-ṣalāh) »,
  13e leçon ; le h1 CMS amalgame le titre du livre — nettoyé ; objectifs en
  infinitifs (source 1re personne).
- Tamhīd : 2 versets à emplacements OCR vides. (1) al-Jumuʿa 62 : 9
  (restauré, réf imprimée concordante). (2) Le manuel imprime « al-Māʾida :
  60 » pour « Il blâma ceux qui n'ont pas répondu à cet appel » — réf sans
  rapport avec le propos en l'un ou l'autre décompte (maghrébin 60 =
  oriental 59 « vous reprochez-vous… » ; oriental 60 = singes et porcs) ;
  contenu canonique restitué = al-Jumuʿa 62 : 11, blâme immédiatement
  consécutif au v. 9 cité (doctrine R115 : contenu canonique en principal
  + note de la réf imprimée). Vérifié : CMS habous.gov.ma (le verset y est
  une image perdue, la réf « المائدة 60 » y est constante) ; aucun PDF
  papier trouvable.
- Muwaṭṭaʾ 174 (Yaḥyā b. Saʿīd : le nāqūs envisagé, songe de ʿAbd Allāh b.
  Zayd al-Anṣārī de Banū l-Ḥārith b. al-Khazraj, ordre du adhān), 179 (Abū
  Hurayra : Satan recule d'un ḍirāṭ, revient au tathwīb, s'insinue — «
  rappelle-toi ceci »), 182 (iqāma non doublée, se lever selon la capacité —
  le lourd et le léger), 183 (adhān obligatoire dans les mosquées de
  jamaʿa), 180 (Sahl b. Saʿd : deux heures d'exaucement — hadra du nidāʾ et
  rang dans la voie de Dieu), Abū Saʿīd al-Khudrī (tout être qui entend le
  muezzin témoignera pour lui), 181 (vendredi : après le zawāl), 188 (ʿUmar
  : « la prière est meilleure que le sommeil » → adhān de l'aube).
- Bukhārī (Anas) : « Bilāl reçut l'ordre de doubler le adhān et de rendre
  l'iqāma impaire » ; al-Zayn ibn al-Munayyir (mathnā = deux fois deux,
  shahāda finale simple) ; Ibn ʿAbd al-Barr (takbīr ×2, adhān d'Abū
  Maḥdhūra et d'Ibn Zayd) ; al-Ḥāfiẓ (sagesse : informer les absents).
- Leçons fiqh : obligation = sunna confirmée / farḍ kifāya (miṣr et
  assimilés) — Zarqānī ; se lever : Mālik (capacité) vs majorité (fin de
  l'iqāma / vue de l'imam) vs Anas (qad qāmat).
- Isnād de 180 dupliqué par l'OCR (« عن أبي حازم… عن سهل… أنه قال : عن
  أبي حازم… ») — traduit une seule fois.
- Lexique : khashabatayn (nāqūs), ḍirāṭ, thawb bi-l-ṣalāh (iqāma, racine
  thāba « revenir »), yakhṭir (waswasa ; khaṭr du chameau ; lecture ḍamma
  = passer entre l'homme et son cœur).
- Préparation préalable : leçon SUIVANTE 12945 (adhān en voyage) —
  al-raḥāl (montures/bâts).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les dispositions de l’appel à la prière (<em>aḥkām al-nidāʾ li-l-ṣalāh</em>)</h1>
<p>Leçon sur les règles de l’appel à la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la treizième leçon.</p>
<ol>
<li>Connaître le statut de l’appel à la prière et sa légitimité.</li>
<li>Distinguer les mérites de l’appel à la prière.</li>
<li>Éprouver la manière optimale d’accomplir le <em>adhān</em> et l’<em>iqāma</em>.</li>
</ol>
<h2>Préambule</h2>
<p>Dieu — Exalté — a institué l’appel (<em>adhān</em>) comme annonce de l’entrée du temps de la prière : Il a ordonné à Ses serviteurs croyants de s’empresser vers elle dès qu’ils l’entendent, en Sa parole — gloire à Lui :</p>
<p>« Ô vous qui croyez ! quand on appelle à la prière un jour de vendredi, accourez à l’invocation de Dieu, et laissez tout commerce : cela est meilleur pour vous, si vous saviez. » (al-Jumuʿa, 62 : 9)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>Et Il a blâmé ceux qui n’ont pas répondu à cet appel, en Sa parole — gloire à Lui :</p>
<p>« Et quand ils voient commerce ou divertissement, ils s’y dispersent et te laissent debout. Dis : ce qui est auprès de Dieu est meilleur que le divertissement et le commerce — et Dieu est le meilleur des pourvoyeurs. » (al-Jumuʿa, 62 : 11)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR. Le manuel imprime « al-Māʾida, 5 : 60 », référence sans rapport avec le propos en l’un ou l’autre décompte : le blâme canonique de ceux qui délaissent l’appel suit immédiatement le verset 9 cité ci-dessus.]</p>
<p>Quel est donc le statut de l’appel à la prière ? Et quelle est la formule en laquelle il s’accomplit ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Yaḥyā ibn Saʿīd : « qu’il dit : Le Messager de Dieu — paix et bénédiction sur lui — avait voulu faire confectionner deux pièces de bois qu’on frapperait l’une contre l’autre, pour rassembler les gens à la prière. Or ʿAbd Allāh ibn Zayd al-Anṣārī — des Banū l-Ḥārith ibn al-Khazraj — se vit montrer les deux pièces de bois en songe ; il dit : Ces deux-là sont proches de ce que veut le Messager de Dieu — paix et bénédiction sur lui. On lui dit : Ne ferais-tu pas l’appel à la prière ? Il vint trouver le Messager de Dieu — paix et bénédiction sur lui — dès qu’il s’éveilla, et lui fit part de cela. “Le Messager de Dieu — paix et bénédiction sur lui — ordonna alors l’appel à la prière.” » [Muwaṭṭaʾ, n° 174]</li>
<li>D’après Mālik, d’après Abū l-Zinād, d’après al-Aʿraj, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — a dit : Quand on appelle à la prière, Satan tourne le dos, avec un petit vent sonore, afin de ne pas entendre l’appel ; et quand l’appel est achevé, il revient ; puis, quand l’iqāma de la prière est faite, il s’écarte ; et quand le tathwīb est achevé, il revient — pour s’insinuer entre l’homme et son âme, en disant : Rappelle-toi ceci, rappelle-toi cela — pour ce dont il ne se rappelait pas — jusqu’à ce que l’homme ne sache plus combien il a prié. » [Muwaṭṭaʾ, n° 179]</li>
<li>Yaḥyā a dit : on interrogea Mālik au sujet de la réduplication de l’appel et de l’iqāma, et du moment où il incombe aux gens de se lever quand la prière est mise en place. Il dit : « Rien ne m’est parvenu, au sujet de l’appel et de l’iqāma, sinon ce que j’ai trouvé les gens pratiquer. Quant à l’iqāma : elle n’est pas rédupliquée — et tel est ce sur quoi n’ont cessé de se tenir les gens de science de notre cité. Quant au lever des gens au moment où la prière est mise en place : je n’ai rien entendu en la matière d’une limite où l’on doive se tenir debout — si ce n’est que je l’estime à la mesure de la capacité des gens : il y a parmi eux le pesant et le léger, et ils ne peuvent être comme un homme unique. » [Muwaṭṭaʾ, n° 182]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>khashabatayn</em> (« deux pièces de bois ») : c’est le <em>nāqūs</em> — une longue pièce de bois qu’on frappe d’une pièce plus petite, et dont sort d’elles deux un son.</li>
<li><em>ḍirāṭ</em> (« un petit vent sonore ») : le son du vent qui sort de l’anus.</li>
<li><em>thawb bi-l-ṣalāh</em> (« l’iqāma de la prière ») : avec ḍamma du <em>thāʾ</em> (trilittère pointé), shadda du <em>wāw</em> et <em>bāʾ</em> — c’est-à-dire : il fut établi ; et la racine est <em>thāba</em>, « revenir » — comme si le muezzin revenait à une sorte d’adhān pour la prière.</li>
<li><em>yakhṭir</em> (« s’insinuer ») : avec fatha de sa première [lettre] et kasre du <em>ṭāʾ</em> ; son sens est « souffler [le doute] » (<em>waswasa</em>) — et son origine est le <em>khaṭr</em> du chameau avec sa queue, quand il l’agite et en frappe ses cuisses. Il fut entendu de la plupart des rapporteurs avec ḍamma du <em>ṭāʾ</em>, et son sens est alors « passer » : il s’approche de lui et passe entre lui et son cœur, le distrayant de ce qu’il faisait.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Extrais du premier hadith le statut de l’adhān et sa légitimité.</li>
<li>Détermine quelques mérites de l’appel à la prière.</li>
<li>Quelle est la formule en laquelle s’accomplissent le adhān et l’iqāma ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de l’appel à la prière</h3>
<p>L’imam Mālik — que Dieu lui fasse miséricorde — et ses compagnons ont tenu l’avis de l’obligation de l’adhān dans les mosquées de congrégations, là où les gens se rassemblent. Ainsi, dans le <em>Muwaṭṭaʾ</em> : « On interrogea Mālik au sujet d’un groupe présent qui voulait accomplir en commun l’[office] obligatoire, et qui voulait faire l’iqāma sans faire l’adhān ? Mālik dit : “Cela leur tient lieu [d’adhān]. L’appel n’est obligatoire que dans les mosquées de congrégations où la prière se fait en commun.” » [Muwaṭṭaʾ, n° 183] Et al-Zarqānī a précisé la nature de l’obligation en sa parole : obligation des sunnas confirmées, selon l’école ; et les tardifs parmi les compagnons de Mālik divergèrent là-dessus en deux avis : le premier — que c’est une sunna confirmée, obligatoire par suppléance (<em>ʿalā l-kifāya</em>) dans la métropole, et ce qui joue le rôle de métropole parmi les bourgades ; le second — que c’est une obligation communautaire (<em>farḍ kifāya</em>) absolument.</p>
<h3>Deuxièmement : le mérite de l’appel à la prière, et sa manière</h3>
<h4>Le mérite de l’appel à la prière</h4>
<p>L’appel à la prière a de nombreux mérites, parmi lesquels :</p>
<ul>
<li>La protection contre Satan : quand Satan entend l’adhān, il s’enfuit, tournant le dos et s’éloignant — l’homme est ainsi préservé de ses suggestions et de ses ruses ; tel est le sens de la parole du Messager de Dieu — paix et bénédiction sur lui — : « Quand on appelle à la prière, Satan tourne le dos, avec un petit vent sonore, afin de ne pas entendre l’appel. »</li>
<li>L’abondance du témoignage du bien : l’imam Mālik a rapporté dans le <em>Muwaṭṭaʾ</em> qu’Abū Saʿīd al-Khudrī dit : « Il n’est nul — djinn, humain ni chose aucune — qui entende la portée de la voix du muezzin sans qu’il ne lui témoigne au Jour de la Résurrection. » Ce que vise ce témoignage, c’est la proclamation publique, au Jour de la Résurrection, du mérite et du degré élevé de celui pour qui l’on témoigne ; et de même que Dieu dénonce par le témoignage les uns, de même Il en honore d’autres.</li>
<li>L’exaucement de l’invocation : au nombre des mérites de l’appel à la prière, son moment est un moment d’exaucement de l’invocation. L’imam Mālik a rapporté dans le <em>Muwaṭṭaʾ</em>, d’après Abū Ḥāzim ibn Dīnār, d’après Sahl ibn Saʿd al-Sāʿidī, qu’il dit : « Deux heures où les portes du ciel sont ouvertes pour elles, et où rares sont les invocateurs dont l’invocation est repoussée : le moment de l’appel à la prière, et le rang dans la voie de Dieu. » [Muwaṭṭaʾ, n° 180]</li>
</ul>
<h4>La manière de l’appel à la prière</h4>
<ul>
<li>La réduplication du adhān et le singlement de l’iqāma
<p>Les imams des capitales divergèrent sur la manière du adhān et de l’iqāma. Mālik et ses compagnons tinrent que le adhān est rédupliqué — chaque formule deux fois — et l’iqāma une fois une. On l’interrogea — que Dieu lui fasse miséricorde — sur la manière de l’appel à la prière ; il dit : « Rien ne m’est parvenu, au sujet de l’appel et de l’iqāma, sinon ce que j’ai trouvé les gens pratiquer : c’est la réduplication du adhān » — du fait de ce qu’il y a dans [le <em>Ṣaḥīḥ</em> d’]al-Bukhārī, d’après Anas, qui dit : « Bilāl reçut l’ordre de doubler le adhān et de rendre l’iqāma impaire. » Al-Zayn ibn al-Munayyir a dit : sa description du adhān comme doublé, Son explication est sa parole « rédupliqué » (<em>mathnā</em>) — c’est-à-dire deux fois deux — et cela requiert que toutes ses formules soient égales en cela ; mais il n’est pas contesté que la parole d’unicité qui est à sa fin est singulière : sa parole « deux fois deux » porte donc sur tout le reste. Fin de citation. Il y a là preuve que le takbīr n’est pas quadruplé. Ibn ʿAbd al-Barr a dit : Mālik et ses compagnons tinrent que le takbīr au début du adhān est [dit] deux fois — cela a été rapporté par des voies saines dans le adhān d’Abū Maḥdhūra et dans le adhān d’ʿAbd Allāh ibn Zayd, et la pratique chez eux, à Médine, est sur cela.</p>
<p>Quant à l’iqāma, elle n’est pas rédupliquée — jusqu’à « La prière est mise en place » : elle est au contraire singulière. L’imam Mālik a dit : « Et tel est ce sur quoi n’ont cessé de se tenir les gens de science de notre cité » — c’est-à-dire Médine — avec l’appui que lui apporte le hadith précédent d’Anas : « Bilāl reçut l’ordre de doubler le adhān et de rendre l’iqāma impaire. »</p></li>
<li>La sagesse de la réduplication du adhān et du singlement de l’iqāma
<p>La sagesse qu’il y a à rédupliquer le adhān et à singler l’iqāma est que le adhān informe les absents : on l’a donc répété pour qu’il leur parvienne mieux — à la différence de l’iqāma, qui s’adresse aux présents. C’est pourquoi il est recommandé que le adhān soit [fait] en un lieu élevé, à la différence de l’iqāma, et que la voix du adhān soit plus haute que celle de l’iqāma. Al-Ḥāfiẓ [Ibn Ḥajar] a dit : c’est là une orientation apparente.</p></li>
</ul>
<h3>Troisièmement : le moment où les gens se lèvent pour la prière à l’iqāma</h3>
<p>Les juristes divergèrent sur le moment où les gens se lèvent quand la prière est mise en place, en plusieurs avis :</p>
<ol>
<li>Mālik — que Dieu lui fasse miséricorde — voit que cela varie selon la variété des gens, pesanteur et légèreté ; tel est le sens de sa parole dans le hadith : « Quant au lever des gens au moment où la prière est mise en place : je n’ai rien entendu en la matière d’une limite où l’on doive se tenir debout — si ce n’est que je l’estime à la mesure de la capacité des gens : il y a parmi eux le pesant et le léger, et ils ne peuvent être comme un homme unique. » [Muwaṭṭaʾ, n° 182]</li>
<li>Le plus grand nombre est allé à [l’avis] que, si l’imam est avec eux dans la mosquée, ils ne se lèvent qu’à l’achèvement de l’iqāma ; et s’il n’est pas dans la mosquée, ils ne se lèvent qu’à ce qu’ils le voient.</li>
<li>Quelques-uns ont dit : les gens se lèvent quand le muezzin dit « La prière est mise en place » — il fut rapporté qu’Anas ibn Mālik — que Dieu soit satisfait de lui — faisait cela.</li>
</ol>
<h2>L’évaluation</h2>
<ol>
<li>Cite le statut de l’appel à la prière et la preuve de sa légitimité.</li>
<li>Expose les mérites de l’appel à la prière.</li>
<li>Quand les gens se lèvent-ils pour la prière au moment de l’iqāma ?</li>
</ol>
<h2>L’exploitation</h2>
<ul>
<li>Yaḥyā a dit : on interrogea Mālik au sujet de l’appel le jour du vendredi — a-t-il lieu avant que le temps ne devienne licite ? Il dit : « Il n’a lieu qu’après que le soleil décline [du zénith]. » [Muwaṭṭaʾ, n° 181]</li>
<li>D’après Mālik : « qu’il lui parvint que le muezzin vint auprès de ʿUmar ibn al-Khaṭṭāb pour lui faire l’appel de la prière de l’aube, et le trouva endormi. Il dit : “La prière est meilleure que le sommeil” — et ʿUmar lui ordonna de la placer dans l’appel de l’aube. » [Muwaṭṭaʾ, n° 188]</li>
</ul>
<p>Lis les deux hadiths et réponds à ce qui suit :</p>
<ol>
<li>Extrais du premier hadith ce qui y est mentionné des conditions du adhān.</li>
<li>Quel est le statut de l’appel à la prière du vendredi avant le déclin [du soleil] ?</li>
<li>Par quoi le adhān de la prière de l’aube se distingue-t-il des autres temps ?</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Explique : <em>al-raḥāl</em> (« les montures »).</li>
<li>Expose le statut de l’appel [à la prière] en voyage.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12929":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12929 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12929 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
