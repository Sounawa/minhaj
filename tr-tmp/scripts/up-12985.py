#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12985 (hadith-1es, la pratique de
l'assise et du tashahhud dans la prière — Muwaṭṭaʾ n° 237-243/246 +
Bukhārī/Muslim + Abū Dāwūd).

Conventions main (cf. 12875-12980 du même livre) :
- h1 = titleFr officiel conservé « Travailler à s'asseoir et à réciter
  le tashahhud dans la prière » (GT-isme « Travailler » toléré — précédent
  12958) + translit. (al-ʿamal fī l-julūs wa-l-tashahhud fī l-ṣalāh),
  20e leçon ; intro interrogative (source : « ما العمل…؟ »).
- Préambule : Muwaṭṭaʾ 239 (Ṣadaqa b. Yasār/al-Mughīra b. Ḥakīm :
  Ibn ʿUmar se rassoit entre les deux prosternations sur le DESSUS de
  ses pieds — « ce n'est point la sunna… je souffre »).
- Hadiths : 237 (Muslim b. Abī Maryam/ʿAlī b. ʿAbd al-Raḥmān
  al-Muʿāwī : pebbles interdits + description de l'assise — paume
  droite sur cuisse droite, doigts resserrés, index pointé [doigt qui
  jouxte le pouce], paume gauche sur cuisse gauche) ; 242 (Ibn Shihāb/
  ʿUrwa/ʿAbd al-Raḥmān b. ʿAbd al-Qārī : ʿUmar enseigne le tashahhud
  sur le minbar — al-tahiyyāt/al-zākiyāt/al-ṭayyībāt wa-l-ṣalawāt).
- Taḥlīl I : assise — 237 + Muwaṭṭaʾ « redresse le pied droit, replie
  le gauche » + 241 (Yaḥyā b. Saʿīd/al-Qāsim b. Muḥammad : assise sur
  la hanche gauche, démontrée par ʿAbd Allāh b. ʿAbd Allāh b. ʿUmar) ;
  sagesses : repos/hanche gauche + l'index « poignard du diable »
  (Sufyān b. ʿUyayna de Muslim b. Abī Maryam) + al-Bājī (repousse le
  sahw, mate le diable — ou tawḥīd).
- Taḥlīl II : statut (Mālik/Abū Ḥanīfa : sunna ; Aḥmad : obligatoire
  aux deux assises ; Shāfiʿī : la dernière seule ; preuve Bukhārī
  « quand l'un de vous prie, qu'il dise : al-tahiyyāt… » ; réponse
  mālikite : l'ordre ≠ obligation — tasbīḥ du rukūʿ recommandé malgré
  l'ordre) + **Wāqiʿa 56 : 77 RESTAURÉ** (emplacement span vide — perte
  OCR ; « fa-sabbiḥ bi-smi rabbika l-ʿaẓīm » ; numérotation MANUEL
  77 = décompte médinois/maghrébin — 74 dans le décompte oriental ;
  hadith ʿUqba b. ʿĀmir « faites-en [le tasbīḥ] dans vos inclinaisons »
  vérifié web) ; écarte l'obligation : hadith de celui qui fit mal sa
  prière. Formule : ʿUmar + le choix des imams — Mālik (tawātur
  sukūtī — Ibn ʿAbd al-Barr ; objection mawqūf → Ibn Mardawayh
  remontant) ; Shāfiʿī (Ibn ʿAbbās, Muslim : al-mubārakāt substitué
  aux al-zākiyāt — al-Ḥāfiẓ : « pour ainsi dire au sens près ») ;
  Abū Ḥanīfa+Aḥmad (Ibn Masʿūd, Bukhārī : « Dieu, Lui, est la Paix…
  elle atteint tout serviteur vertueux au ciel et sur la terre »).
  Invocation : mashhūra — répréhensible au premier tashahhud (abréger),
  permise (Ibn Nāfiʿ) ; au dernier : pas de divergence — Muwaṭṭaʾ 243
  (« il avançait le tashahhud puis invoquait ce qu'il voulait ») ;
  invocation non limitée (dunya/ākhira).
- Istimḥār : 238 (ʿAbd Allāh b. Dīnār : l'homme en tailleur à la
  quatrième ; « moi, je souffre ») + 246 (Mālik/Ibn Shihāb+Nāfiʿ : le
  masbūq d'une rakʿa récite le tashahhud avec l'imam — witr inclus) ;
  2 questions (parole vs acte ; règles du tashahhud du masbūq).
- Préparation préalable : leçon SUIVANTE 12986 (sahw — nāṣiya/
  li-yuʾtama bihi/aqṣarat al-ṣalāt ; salut au bout de deux rakʿas ;
  relever la tête avant l'imam).
- OCR : « صدور قدميه » = le dessus des pieds (pas « poitrine ») ;
  objectifs numérotés 1./2./3. rendus sans numéros (convention) ;
  « عمر » de la question d'istimḥār = Ibn ʿUmar (hadith explicite),
  rendu « Ibn ʿUmar ».
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Travailler à s’asseoir et à réciter le tashahhud dans la prière (<em>al-ʿamal fī l-julūs wa-l-tashahhud fī l-ṣalāh</em>)</h1>
<p>Que dit la pratique (<em>al-ʿamal</em>) sur l’assise de l’orant et son <em>tashahhud</em> dans la prière ? — matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingtième leçon.</p>
<ul>
<li>Connaître la manière dont s’asseyait le Prophète — paix et bénédiction sur lui — dans la prière.</li>
<li>Connaître la formule du <em>tashahhud</em> qu’ʿUmar — que Dieu soit satisfait de lui — enseigna aux gens.</li>
<li>Mettre en pratique la Sunna authentique dans l’assise et le <em>tashahhud</em>.</li>
</ul>
<h2>Préambule</h2>
<p>Certains gens se soucient peu de certaines attitudes qu’il est recommandable que le musulman adopte dans sa prière ; or les Compagnons — que Dieu soit satisfait d’eux — veillaient à prendre le Prophète — paix et bénédiction sur lui — pour modèle dans les paroles et les actes touchant la prière, au point que, si un homme en voyait un autre s’en écarter, il le lui interdisait. Parmi cela, ce qui vient dans le <em>Muwaṭṭaʾ</em>, d’après Mālik, d’après Ṣadaqa ibn Yasār, d’après al-Mughīra ibn Ḥakīm : « qu’il vit ʿAbd Allāh ibn ʿUmar, dans les deux prosternations de la prière, se rasseoir sur le dessus de ses pieds ; quand il eut achevé, on le lui mentionna. Il dit : “Ce n’est point là la sunna de la prière — je ne fais ainsi que parce que je souffre.” » [Muwaṭṭaʾ, n° 239]</p>
<p>Comment donc le Prophète — paix et bénédiction sur lui — s’asseyait-il dans sa prière pour le <em>tashahhud</em> ? Et quelle est la formule optimale du <em>tashahhud</em> dans la prière ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Muslim ibn Abī Maryam, d’après ʿAlī ibn ʿAbd al-Raḥmān al-Muʿāwī : « ʿAbd Allāh ibn ʿUmar me vit pendant que je jouais avec les petits cailloux (<em>al-ḥaṣbāʾ</em>) dans la prière. Quand il eut achevé, il me l’interdit et dit : Fais comme faisait le Messager de Dieu — paix et bénédiction sur lui. Je dis : Et comment faisait le Messager de Dieu — paix et bénédiction sur lui ? Il dit : “Quand il s’asseyait dans la prière, il posait sa paume droite sur sa cuisse droite, resserrait tous ses doigts, et pointait avec le doigt qui jouxte le pouce ; et il posait sa paume gauche sur sa cuisse gauche” — et il dit : C’est ainsi qu’il faisait. » [Muwaṭṭaʾ, n° 237]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿUrwa ibn al-Zubayr, d’après ʿAbd al-Raḥmān ibn ʿAbd al-Qārī : « qu’il entendit ʿUmar ibn al-Khaṭṭāb — sur le minbar — enseigner aux gens le <em>tashahhud</em>, dire : Dites : “Les salutations sont à Dieu, les purs hommages sont à Dieu, les bonnes paroles et les prières sont à Dieu ; que le salut soit sur toi, ô Prophète, ainsi que la miséricorde de Dieu ; que le salut soit sur nous et sur les serviteurs vertueux de Dieu ; j’atteste qu’il n’est de dieu que Dieu ; et j’atteste que Muḥammad est le serviteur de Dieu et Son messager.” » [Muwaṭṭaʾ, n° 242]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>al-ḥaṣbāʾ</em> : les petits cailloux.</li>
<li><em>al-tahiyyāt</em> : pluriel de <em>tahiyya</em> ; son sens : le salut, ou la permanence, ou la grandeur, ou la préservation des afflictions et des défauts, ou la royauté.</li>
<li><em>al-zākiyāt</em> : les œuvres pies dont la récompense croît pour son auteur en la demeure dernière.</li>
<li><em>al-ṭayyibāt</em> : ce qui est pur de la parole, et ce dont il est beau de louer Dieu.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Extrais du premier hadith la manière dont s’asseyait le Prophète — paix et bénédiction sur lui — dans sa prière.</li>
<li>Comment notre maître ʿUmar — que Dieu soit satisfait de lui — récitait-il le <em>tashahhud</em> dans la prière ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la manière de s’asseoir dans la prière et sa sagesse</h3>
<h4>La manière de s’asseoir dans la prière</h4>
<p>Dans le hadith de la leçon, le noble Compagnon ʿAbd Allāh ibn ʿUmar expose la manière dont s’asseyait le Prophète — paix et bénédiction sur lui — dans la prière ; il dit : « Le Prophète — paix et bénédiction sur lui —, quand il s’asseyait dans la prière, posait sa paume droite sur sa cuisse droite, resserrait tous ses doigts et pointait avec le doigt qui jouxte le pouce, et posait sa paume gauche sur sa cuisse gauche », et il dit : “C’est ainsi qu’il faisait.” D’autres hadiths précisent la manière des jambes : dans le <em>Muwaṭṭaʾ</em> : « La sunna de la prière est seulement que tu redresses ton pied droit et replies ton pied gauche. » Mais il n’y précisa pas ce qu’il fait après le repli — s’assied-il par-dessus, ou s’assied-il en <em>tawarruk</em> ? Une autre narration le précise : l’imam Mālik rapporta dans le <em>Muwaṭṭaʾ</em>, d’après Yaḥyā ibn Saʿīd : « qu’al-Qāsim ibn Muḥammad leur montra l’assise du <em>tashahhud</em> : il redressa son pied droit, replia son pied gauche et s’assit sur sa hanche gauche, sans s’asseoir sur son pied » ; puis il dit : ʿAbd Allāh ibn ʿAbd Allāh ibn ʿUmar ibn al-Khaṭṭāb me montra cette assise, et m’informa que son père faisait ainsi. [Muwaṭṭaʾ, n° 241]</p>
<h4>La sagesse de cette manière de s’asseoir</h4>
<p>Cette manière de s’asseoir renferme plusieurs sagesses, parmi elles :</p>
<ul>
<li>Le redressement du pied droit, le repli du gauche et l’assise sur la hanche gauche inclinent davantage au repos et éloignent de toute distraction — sauf si l’orant souffre des jambes.</li>
<li>Le geste du doigt qui jouxte le pouce — l’index (<em>sabbāba</em>) — éloigne l’orant de la distraction : l’indique la narration de Sufyān ibn ʿUyayna, de Muslim ibn Abī Maryam : le doigt pointé, il disait : “C’est le poignard (<em>mūdiya</em>) du diable : nul d’entre vous ne se laisse distraire tant qu’il pointe son doigt, en disant : ainsi.” Al-Bājī a dit : cela montre que le sens du geste est de repousser la distraction et de mater le diable qui insuffle [le doute] ; et l’on a dit que le geste signifie ici l’unicité (<em>tawḥīd</em>).</li>
</ul>
<h3>Deuxièmement : les règles du tashahhud</h3>
<h4>Le statut du tashahhud</h4>
<p>Mālik, Abū Ḥanīfa et un groupe ne l’obligèrent pas — Mālik dit : c’est une sunna ; Aḥmad et un groupe l’obligèrent dans les deux assises ensemble ; al-Shāfiʿī l’obligea dans la dernière à l’exclusion de la première. Leurs preuves de l’obligation : ce qui est dans le <em>Ṣaḥīḥ</em> d’al-Bukhārī, que le Prophète — paix et bénédiction sur lui — dit : “Quand l’un de vous prie, qu’il dise : Les salutations sont à Dieu…” [fin du hadith]. Certains Mālikites répondirent que l’ordre n’entraîne pas nécessairement l’obligation — ne vois-tu pas que le <em>tasbīḥ</em> dans l’inclinaison et la prosternation est recommandé, alors qu’il en fut ordonné quand descendit :</p>
<p>« Glorifie donc le nom de ton Seigneur, le Très-Grand ! » (al-Wāqiʿa, 56 : 77 dans la numérotation du manuel — 74 dans le décompte oriental)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR. Numérotation maghrébine (décompte médinois de la sūra : 99 versets), cohérente avec les cas précédents du manuel.]</p>
<p>et qu’il dit : “Faites-en [le tasbīḥ] dans vos inclinaisons” [fin du hadith — ʿUqba ibn ʿĀmir]. De même le <em>tashahhud</em> ; et ce qui l’écarte de l’obligation : le hadith de celui qui fit mal sa prière — il ne lui mentionna pas le <em>tashahhud</em>. Dieu sait mieux.</p>
<h4>La formule du tashahhud</h4>
<p>Plusieurs hadiths vinrent sur la formule du <em>tashahhud</em> ; ils se rapprochent les uns des autres — soit par l’addition ou le retranchement d’un mot, soit par l’avance ou le retard d’un mot. Parmi eux, le <em>tashahhud</em> d’ʿUmar — que Dieu soit satisfait de lui —, dont voici le texte : « Les salutations sont à Dieu, les purs hommages sont à Dieu, les bonnes paroles et les prières sont à Dieu ; que le salut soit sur toi, ô Prophète, ainsi que la miséricorde de Dieu ; que le salut soit sur nous et sur les serviteurs vertueux de Dieu ; j’atteste qu’il n’est de dieu que Dieu, et j’atteste que Muḥammad est le serviteur de Dieu et Son messager. » Voici ensuite le choix des imams — que Dieu soit satisfait d’eux tous.</p>
<h5>Le choix de l’imam Mālik</h5>
<p>L’imam Mālik et ses compagnons — que Dieu soit satisfait d’eux tous — choisirent ce <em>tashahhud</em> d’ʿUmar, parce qu’il l’enseignait aux gens sur le minbar alors que les Compagnons étaient présents en grand nombre, sans que personne le lui reprochât : indice qu’il est supérieur aux autres. On objecta qu’il est interrompu (<em>mawqūf</em>) [sur ʿUmar] et ne rejoint pas ce qui remonte [au Prophète] ; on répondit qu’Ibn Mardawayh le rapporta, dans le livre du <em>tashahhud</em>, comme remontant [au Prophète].<br>
Ibn ʿAbd al-Barr a dit : « Et la preuve de la justesse de l’école de Mālik est que le <em>tashahhud</em> d’ʿUmar ibn al-Khaṭṭāb vaut le hadith massivement transmis (<em>mutawātir</em>) : car ʿUmar ibn al-Khaṭṭāb l’enseigna aux gens sur le minbar, en présence du groupe des Compagnons et des imams des musulmans, sans que personne le lui reprochât ni s’y opposât. »</p>
<h5>Le choix de l’imam al-Shāfiʿī</h5>
<p>L’imam al-Shāfiʿī choisit le <em>tashahhud</em> d’Ibn ʿAbbās — ce que Muslim et les auteurs des <em>Sunan</em> rapportèrent d’Ibn ʿAbbās, qui dit : « Le Messager de Dieu — paix et bénédiction sur lui — nous enseignait le <em>tashahhud</em> comme il nous enseignait une sūra du Coran ; il disait : Les salutations, les bénies, les prières et les bonnes paroles sont à Dieu ; que le salut soit sur toi, ô Prophète, ainsi que la miséricorde de Dieu et Ses bénédictions ; que le salut soit sur nous et sur les serviteurs vertueux de Dieu ; j’atteste qu’il n’est de dieu que Dieu, et j’atteste que Muḥammad est le messager de Dieu. » [Rapporté par Muslim dans son <em>Ṣaḥīḥ</em>] Il est proche du hadith d’ʿUmar, sauf qu’il substitue aux purs hommages (<em>al-zākiyāt</em>) les bénées (<em>al-mubārakāt</em>). Al-Ḥāfiẓ [Ibn Ḥajar] dit : c’est pour ainsi dire au sens près.</p>
<h5>Le choix des deux imams Abū Ḥanīfa et Aḥmad</h5>
<p>Les deux imams Abū Ḥanīfa et Aḥmad, les auteurs de hadith et la majorité des savants choisirent le <em>tashahhud</em> d’Ibn Masʿūd — ce que les six imams rapportèrent de lui ; il dit : « Quand nous priions derrière le Prophète — paix et bénédiction sur lui —, nous disions : Que le salut soit sur Dieu, que le salut soit sur Gabriel et Mīkhāʾīl, que le salut soit sur untel et untel. Le Messager de Dieu — paix et bénédiction sur lui — se tourna vers nous et dit : “Dieu, Lui, est la Paix (<em>al-Salām</em>) : quand l’un de vous prie, qu’il dise : Les salutations sont à Dieu, ainsi que les prières et les bonnes paroles ; que le salut soit sur toi, ô Prophète, ainsi que la miséricorde de Dieu et Ses bénédictions ; que le salut soit sur nous et sur les serviteurs vertueux de Dieu — quand vous dites cela, elle atteint tout serviteur vertueux de Dieu au ciel et sur la terre — ; j’atteste qu’il n’est de dieu que Dieu, et j’atteste que Muḥammad est Son serviteur et Son messager.” » [Rapporté par al-Bukhārī dans son <em>Ṣaḥīḥ</em>]</p>
<h4>L’invocation dans le tashahhud</h4>
<p>Selon l’école connue de l’imam Mālik, l’invocation dans le premier <em>tashahhud</em> est répréhensible, car ce qui est requis est de l’abréger ; Mālik la permit dans la narration d’Ibn Nāfiʿ.</p>
<p>Quant à l’invocation dans le dernier <em>tashahhud</em>, il n’y a pas de divergence sur sa permission, du fait de ce qui est établi de Mālik, au hadith d’ʿAbd Allāh ibn ʿUmar : “… quand il s’asseyait à la fin de sa prière, il récitait le <em>tashahhud</em> de même — sinon qu’il avançait le <em>tashahhud</em>, puis invoquait ce qu’il voulait…” [Muwaṭṭaʾ, n° 243]. En cela, preuve que l’invocation n’est pas limitée : il invoque de ce qu’il veut, de l’ordre de la demeure-bas et de la demeure-dernier.</p>
<h2>L’évaluation</h2>
<ol>
<li>Cite le <em>tashahhud</em> d’ʿUmar qu’il enseigna aux gens sur le minbar.</li>
<li>Explicite la manière dont s’asseyait le Prophète — paix et bénédiction sur lui — dans le dernier <em>tashahhud</em>.</li>
<li>Compare le <em>tashahhud</em> d’ʿUmar à ceux d’Ibn ʿAbbās et d’Ibn Masʿūd.</li>
</ol>
<h2>L’exploitation</h2>
<ul>
<li>D’après Mālik, d’après ʿAbd Allāh ibn Dīnār : « qu’il entendit ʿAbd Allāh ibn ʿUmar — un homme pria à son côté ; quand l’homme s’assit en la quatrième, il s’assit en tailleur et replia ses jambes ; quand ʿAbd Allāh eut achevé, il le lui reprocha. L’homme dit : Mais toi, tu fais cela ! ʿAbd Allāh ibn ʿUmar dit : “Moi, je souffre.” » [Muwaṭṭaʾ, n° 238]</li>
<li>Mālik : « qu’il interrogea Ibn Shihāb et Nāfiʿ, affranchi d’Ibn ʿUmar, sur un homme qui entra avec l’imam dans la prière alors que l’imam l’avait déjà devancé d’une rakʿa : récite-t-il le <em>tashahhud</em> avec lui aux deux [rakʿas] et aux quatre, quand cela est impair pour lui ? Tous deux dirent : “Qu’il récite le <em>tashahhud</em> avec lui.” Mālik dit : “Et c’est la chose chez nous.” » [Muwaṭṭaʾ, n° 246]</li>
</ul>
<h3>Médite les deux hadiths et réponds à ce qui suit :</h3>
<ul>
<li>La parole d’Ibn ʿUmar concorde-t-elle avec son acte, dans le premier hadith ?</li>
<li>Extrais du second hadith les règles propres au <em>tashahhud</em> de celui qui a été devancé d’une rakʿa.</li>
</ul>
<h2>La préparation préalable</h2>
<ul>
<li>Explique : <em>nāṣiya</em> (le front) – <em>li-yuʾtama bihi</em> (pour qu’on le prenne pour imam) – <em>aqṣarat al-ṣalāt</em> (la prière fut abrégée).</li>
<li>Que fait celui qui a fait le salut final au bout de deux rakʿas ?</li>
<li>Explicite le statut de celui qui releva la tête de l’inclinaison avant l’imam.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12985":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12985 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12985 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
