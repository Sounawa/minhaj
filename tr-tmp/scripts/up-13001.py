#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13001 (hadith-1es, l'encouragement
à la prière [du tarāwīḥ] en Ramadan — Muwaṭṭaʾ n° 301/302/303/304/305/
306/313/317 + Tirmidhī/Abū Dāwūd + Ibn Baṭṭāl + al-Bājī).

Conventions main (cf. 12875-12998 du même livre) :
- h1 « Encouragement à prier pendant le Ramadan (al-targhīb fī
  ṣalāt al-tarāwīḥ) », 25e leçon ; titleFr officiel conservé.
- Préambule : Ramadan = jeûne + qiyām + Coran ; le qiyām nocturne =
  « tarāwīḥ » en les livres de fiqh.
- Hadiths : 301 (Ibn Shihāb/ʿUrwa/ʿĀʾisha : le Prophète pria une nuit
  au mosque, des gens prièrent avec lui ; 2e nuit plus nombreux ;
  3e ou 4e nuit il ne sortit pas — « j'ai vu ce que vous avez fait ;
  rien ne m'a retenu de sortir vers vous sinon la crainte qu'elle ne
  vous fût imposée — et cela en Ramadan ») ; 303 (ʿUrwa/ʿAbd
  al-Raḥmān b. ʿAbd al-Qārī : ʿUmar trouva le peuple en groupes
  épars — « si je les rassemblais sur un seul récitant, ce serait
  plus convenable » → Ubayy b. Kaʿb ; « quelle excellente innovation
  que celle-ci ! Et celle que vous dormez vaut mieux que celle où
  vous vous tenez debout » — fin de la nuit, le peuple se tenait au
  début).
- Lexique : al-qābila, awzāʿ, la-kāna amthal, bidʿa (3 définitions).
- Taḥlīl I : tarwīḥa (une reposée — comme taslīma de salām ; repos
  entre chaque deux salutations) ; 301 = l'origine légale ; Ibn
  Baṭṭāl (le qiyām lui était obligatoire à lui seul — crainte de
  l'égalisation du statut).
- Taḥlīl II : la sincérité âme des adorations (« les actes ne sont
  que par les intentions ») ; 302 (« qui se tient debout en Ramadan,
  en foi et en quête [de récompense], il lui est pardonné ce qui a
  précédé de son péché ») ; īmānan/iḥtisāban explicités ; le péché :
  2 avis (majorité = mineurs ; Ibn al-Mundhar = les deux ; al-Ḥāfiẓ =
  l'apparent du hadith).
- Taḥlīl III : mort du Prophète sur le délaissement du groupe ;
  Abū Bakr idem ; ʿUmar rétablit en l'an 14 H ; Ubayy choisi
  (« l'imam des gens = leur meilleur récitant », « leur meilleur
  récitant est Ubayy », ʿUmar : « ʿAlī le plus ǧuge, Ubayy le
  meilleur récitant » — Ibn ʿAbd al-Barr) ; « quelle excellente
  innovation » — l'origine est sunna (Ibn ʿAbd al-Barr : « prenez
  pour guides ceux d'après moi » Tirmidhī ; « ma sunna et celle des
  califes bien guidés — mordez-la des molaires » Tirmidhī+Abū
  Dāwūd) ; consensus des Compagnons = le nom de bidʿa tombe.
- Taḥlīl IV : le nombre — 317 (ʿĀʾisha : jamais plus de onze rakʿas,
  Ramadan ou non) ; 304 (ʿUmar/ʿUbayy+Tamīm al-Dārī : onze) ; 305
  (Yazīd b. Rūmān : vingt-trois du temps de ʿUmar) ; al-Bājī
  (d'abord prolonger la récitation — le mieux ; puis affaiblissement
  → 23, allègement compensé par l'ajout de rakʿas) ; 306 (al-Aʿraj :
  la Baqara en huit rakʿas ; en douze = « il a allégé ») ; pas de
  limite — « quiconque guide les gens, qu'il allège » + Muʿādh au
  Yémen « prolonge selon leur endurance, qu'ils ne se lassent pas de
  l'ordre de Dieu » — à plus forte raison les surérogatoires (Abū
  ʿUmar).
- Istimḥār : 313 (Zayd b. Aslam/son père : ʿUmar priait, et au
  dernier tiers réveillait les siens « la prière ! la priée ! » puis
  récitait le verset) + **Ṭā-Hā 20 : 131 RESTAURÉ** (emplacement
  span vide — perte OCR ; « la subsistance de ton Seigneur est
  meilleure et plus durable » ; numérotation imprimée = décompte
  standard, aucune divergence) + 2 questions.
- Préparation préalable : leçon SUIVANTE 13002 (witr + 2 rakʿas de
  l'aube ; le qaḍāʾ des sunnas/nawāfil).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Encouragement à prier pendant le Ramadan (<em>al-targhīb fī ṣalāt al-tarāwīḥ</em>)</h1>
<p>Leçon sur l’encouragement à prier en Ramadan, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-cinquième leçon.</p>
<ol>
<li>Connaître l’origine légale de la prière du <em>tarāwīḥ</em> et sa vertu.</li>
<li>Comprendre la miséricorde de l’Envoyé — paix et bénédiction sur lui — et sa tendresse pour sa communauté.</li>
<li>Veiller à la station de la nuit en Ramadan et hors de lui, sur le modèle de l’Envoyé — paix et bénédiction sur lui — et de ses Compagnons.</li>
</ol>
<h2>Préambule</h2>
<p>Ramadan est le mois du jeûne, de la station nocturne et de la lecture du Coran — l’occasion que saisissent les musulmans pour se rapprocher de Dieu — Puissant et Exalté — et obtenir la récompense doublée, en peuplant les maisons de Dieu et en veillant sur le Noble Coran, lecture et méditation, en particulier ou en groupe. Parmi les surérogations recommandées en ce grand mois : la station de la nuit (<em>qiyām al-layl</em>), connue en les livres de fiqh sous le nom de prière du <em>tarāwīḥ</em>.</p>
<p>Quelle est son origine ? Et quelle récompense le musulman obtient-il par cette adoration ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿUrwa ibn al-Zubayr, d’après ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui — : « que le Messager de Dieu — paix et bénédiction sur lui — pria une nuit dans la mosquée ; des gens prièrent de sa prière ; puis il pria la nuit suivante, et les gens furent plus nombreux ; puis ils se rassemblèrent à la troisième ou quatrième nuit, et le Messager de Dieu — paix et bénédiction sur lui — ne sortit pas vers eux. Au matin, il dit : “J’ai vu ce que vous avez fait ; et rien ne m’a retenu de sortir vers vous, sinon que je craignais qu’elle ne vous fût imposée — et cela était en Ramadan.” » [Muwaṭṭaʾ, n° 301]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿUrwa ibn al-Zubayr, d’après ʿAbd al-Raḥmān ibn ʿAbd al-Qārī : « qu’il dit : Je sortis avec ʿUmar ibn al-Khaṭṭāb en Ramadan vers la mosquée : les gens étaient des groupes épars — tel priait pour soi, tel priait, et le groupe (<em>raḥṭ</em>) priait de sa prière. ʿUmar dit : Par Dieu ! il me semble que, si je rassemblais ceux-ci sur un seul récitant, ce serait plus convenable. Il les rassembla sur Ubayy ibn Kaʿb. Il dit : Puis je sortis avec lui une autre nuit, et les gens priaient de la prière de leur récitant ; ʿUmar dit : “Quelle excellente innovation (<em>niʿmati l-bidʿa</em>) que celle-ci ! Et celle que vous dormez vaut mieux que celle où vous vous tenez debout” — il voulait dire la fin de la nuit ; or le peuple se tenait debout en son début. » [Muwaṭṭaʾ, n° 303]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>al-qābila</em> (« la suivante ») : la nuit à venir.</li>
<li><em>awzāʿ</em> (« groupes épars ») : des troupes.</li>
<li><em>la-kāna amthal</em> (« ce serait plus convenable ») : plus convenable et meilleur.</li>
<li><em>bidʿa</em> (« innovation ») : linguistiquement, ce qui est nouveauté sans exemple antérieur ; légalement, ce qui est innové en la religion de ce qui n’a point d’origine — et elle se dit en contrepartie de la sunna.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Pourquoi l’Envoyé — paix et bénédiction sur lui — ne sortit pas, les troisième et quatrième nuits de Ramadan, pour prier avec les Compagnons ?</li>
<li>Quelle est la récompense de la station de Ramadan ?</li>
<li>Ce que fit ʿUmar — que Dieu soit satisfait de lui — en l’affaire du <em>tarāwīḥ</em> compte-t-il comme innovation ? Appuie ta réponse.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : l’origine de la prière du tarāwīḥ</h3>
<p><em>Al-tarāwīḥ</em> : pluriel de <em>tarwīḥa</em> — une instance de repos, comme <em>taslīma</em> de <em>salām</em> ; la prière surérogatoire en groupe après la prière de la ʿishāʾ en les nuits de Ramadan fut nommée <em>tarāwīḥ</em> parce que les musulmans, quand ils s’y rassemblèrent d’abord, se reposaient entre chaque deux salutations.</p>
<p>Le premier hadith du chapitre est l’origine légale dont s’appuyèrent les juristes et les savants en la prière du <em>tarāwīḥ</em>. Ibn Baṭṭāl dit, sur sa parole — paix et bénédiction sur lui — : « rien ne m’a retenu de sortir vers vous, sinon que je craignais qu’elle ne vous fût imposée » : il se peut que cette parole procédât de lui parce que la station de la nuit lui était une obligation, à lui sans sa communauté — il craignit que, s’il sortait vers eux et qu’ils s’y tenaient avec lui, [Dieu] n’égalisât le statut des leurs au sien.</p>
<h3>Deuxièmement : la récompense de la station de Ramadan</h3>
<p>Il est notoire que la sincérité est l’âme des adorations, et que l’homme est récompensé de ses actes selon son intention, du hadith sain : “Les actes ne sont que par les intentions…” Parmi les surérogations où l’Envoyé — paix et bénédiction sur lui — encouragea sa communauté : revivifier les nuits de Ramadan par la station et la récitation du Coran — il y attacha l’immense récompense et la récompense doublée, à condition que cela s’accompagne de foi véridique, de quête [de la récompense] et de sincérité que n’entache nulle ostentation ni recherche de réputation. Mālik rapporta, d’après Abū Hurayra, que le Messager de Dieu — paix et bénédiction sur lui — dit : « Quiconque se tient debout en Ramadan, en foi et en quête [de récompense], il lui est pardonné ce qui a précédé de son péché. » [Muwaṭṭaʾ, n° 302]</p>
<p>Le sens de “en foi” (<em>īmānan</em>) : tenir cela pour vrai, croyant à sa précellence. “En quête” (<em>iḥtisāban</em>) : rechercher la récompense de la demeure dernière, non l’ostentation et ce qui s’y ramène — contraire de la sincérité ; l’âme apaisée en cela, sans trouver la station pesante ni longue.<br>
On divergea sur le sens du péché mentionné au hadith, en deux paroles :</p>
<ul>
<li>La plupart des savants allèrent à ce que le voulu, par les péchés, est les mineurs, non les majeurs.</li>
<li>Ibn al-Mundhir trancha qu’il embrasse les deux ; al-Ḥāfiẓ dit : c’est l’apparent du hadith.</li>
</ul>
<h3>Troisièmement : la restauration de la prière du tarāwīḥ par ʿUmar ibn al-Khaṭṭāb — que Dieu soit satisfait de lui</h3>
<p>L’Envoyé de Dieu — paix et bénédiction sur lui — mourut sur le délaissement du groupe en la prière du <em>tarāwīḥ</em> ; l’affaire demeura ainsi au califat d’Abū Bakr et au début du califat de ʿUmar ; les traditionnistes mentionnent que ʿUmar établit la prière du <em>tarāwīḥ</em> et la revivifia en l’an quatorze de l’Hégire. Le hadith du chapitre montre qu’il — que Dieu soit satisfait de lui — sortit vers les gens une nuit de Ramadan : le peuple dispersé, en surérogatoire dans la mosquée après la ʿishāʾ, en particulier, tel priant et le groupe de gens priant de sa prière. ʿUmar résolut de les rassembler sur un seul récitant : il les rassembla sur Ubayy ibn Kaʿb — que Dieu soit satisfait de lui — car il était le meilleur récitant des Compagnons. Ibn ʿAbd al-Barr a dit : il choisit Ubayy pour sa parole — paix et bénédiction sur lui — : “L’imam des gens est leur meilleur récitant”, et sa parole : “Leur meilleur récitant est Ubayy” ; et ʿUmar disait : “ʿAlī est notre plus grand juge, et Ubayy notre meilleur récitant.”</p>
<p>Quant à la parole de ʿUmar : “Quelle excellente innovation que celle-ci !” — c’est que l’origine de ce qu’il fit est sunna : l’innovation interdite n’est que la contraire de la sunna. Ibn ʿAbd al-Barr a dit : ʿUmar n’institua que ce dont satisfait le Prophète — paix et bénédiction sur lui — ; or il dit : “Prenez pour guides ceux qui [viendront] après moi : Abū Bakr et ʿUmar.” [Rapporté par at-Tirmidhī dans ses <em>Sunan</em>] Et au hadith sain, il dit — paix et bénédiction sur lui — : “Tenez-vous à ma sunna et à la sunna des califes bien guidés après moi : mordez-la des molaires (<em>bi-l-nawājid</em>).” [Rapporté par at-Tirmidhī et Abū Dāwūd] Et quand les Compagnons s’accordèrent avec ʿUmar sur cela, le nom d’innovation en tomba.</p>
<h4>Quatrièmement : ce qui vint du nombre des rakʿas de la station de Ramadan</h4>
<p>Les rapports et narrations se multiplièrent sur le nombre des rakʿas de la prière du <em>tarāwīḥ</em> ; parmi ce qui vint sur le sujet, le hadith de ʿĀʾisha, interrogée sur sa prière en Ramadan : « Le Messager de Dieu — paix et bénédiction sur lui — n’ajoutait, en Ramadan ni hors de lui, rien à onze rakʿas. » [Muwaṭṭaʾ, n° 317]</p>
<p>Et Mālik rapporta par sa chaîne jusqu’à al-Sāʾib ibn Yazīd : « qu’il dit : ʿUmar ibn al-Khaṭṭāb ordonna à Ubayy ibn Kaʿb et à Tamīm al-Dārī de se tenir debout pour les gens en onze rakʿas… » [Muwaṭṭaʾ, n° 304] ; et Mālik rapporta aussi, d’après Yazīd ibn Rūmān : « qu’il dit : Le peuple se tenait debout, au temps de ʿUmar ibn al-Khaṭṭāb, en Ramadan, en vingt-trois rakʿas. » [Muwaṭṭaʾ, n° 305]</p>
<p>Al-Bājī a dit : peut-être ʿUmar le prit-il de la prière du Prophète — paix et bénédiction sur lui — : il leur ordonna d’abord de prolonger la récitation, car c’est le meilleur ; puis les gens faiblirent, et il leur ordonna vingt-trois : il allégea la longueur de la récitation et compensa quelque vertu par l’addition des rakʿas. Et Mālik rapporta d’al-Aʿraj sa parole : “Le récitant — en Ramadan — récitait la sūra de la Vache en huit rakʿas ; quand il se tenait avec elle en douze rakʿas, les gens voyaient qu’il avait allégé.” [Muwaṭṭaʾ, n° 306]<br>
Et le mot de la fin : il n’y a point de limite au montant de la récitation — il dit — paix et bénédiction sur lui — : “Quiconque guide les gens, qu’il allège”, et il dit à Muʿādh — que Dieu l’agrée — quand il l’envoya au Yémen : “Et prolonge la récitation à la mesure de ce qu’ils peuvent porter — qu’ils ne se lassent point de l’ordre de Dieu ni ne le haïssent.” Cela pour les obligations — que dire des surérogations ! C’est la parole d’Abū ʿUmar.</p>
<h2>L’évaluation</h2>
<ol>
<li>Explicite l’origine de la prière du <em>tarāwīḥ</em>.</li>
<li>Déduis du premier hadith ce qui indique la tendresse de l’Envoyé — paix et bénédiction sur lui — et sa miséricorde pour sa communauté, et appuie cela d’un texte coranique convenable.</li>
<li>Qu’entend-on par sa parole — paix et bénédiction sur lui — : « en foi et en quête [de récompense] » ?</li>
</ol>
<h2>L’exploitation</h2>
<p>Mālik, d’après Zayd ibn Aslam, d’après son père : « que ʿUmar ibn al-Khaṭṭāb priait de la nuit ce que Dieu voulait ; quand c’en était au dernier de la nuit, il réveillait sa famille pour la prière, leur disant : “La prière ! la prière !” — puis il récitait ce verset :</p>
<p>« Ne tends point tes yeux vers ce dont Nous avons fait jouir certains couples d’entre eux — la floraison de la vie d’ici-bas — pour les y éprouver : la subsistance de ton Seigneur est meilleure et plus durable. » (Ṭā-Hā, 20 : 131)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>» [Muwaṭṭaʾ, n° 313]</p>
<ol>
<li>Déduis du hadith ce qui indique l’importance de la station de la nuit et sa vertu.</li>
<li>Cherche dans le commentaire d’al-Zarqānī la raison de la répréhension du sommeil avant la ʿishāʾ.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Recherche l’importance de la prière de l’<em>witr</em> et des deux rakʿas de l’aube.</li>
<li>Explicite : les sunnas et surérogations se rattrapent-elles comme se rattrapent les prières écrites ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13001":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13001 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13001 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
