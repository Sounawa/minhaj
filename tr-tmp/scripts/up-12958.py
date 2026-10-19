#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12958 (hadith-1es, la pratique de la
lecture dans la prière — Muwaṭṭaʾ n° 214-219, + Muslim/Tirmidhī/Nasāʾī).

Conventions main (cf. 12875, 12884-12953 du même livre) :
- h1 « Travailler la lecture dans la prière (al-ʿamal fī l-qirāʾa fī
  l-ṣalāh) », 17e leçon ; le h1 CMS amalgame le titre du livre — nettoyé ;
  objectifs en infinitifs (source 1re personne).
- Muwaṭṭaʾ 214 (ʿAlī : interdits du qassī, de l'anneau d'or, de la
  récitation en rukūʿ), 215 (al-Bayāḍī : « celui qui prie s'entretient avec
  son Seigneur — que nul ne domine l'autre en récitation »), 216 (Anas :
  derrière Abū Bakr, ʿUmar et ʿUthmān — **basmala OCR-vide ﴿﴾ RESTAURÉE
  du corps même de la leçon (taḥlīl la cite en entier)**), 217 (ʿUmar :
  récitation entendue d'Abū Jahm par al-Balāṭ), 218 (Ibn ʿUmar rattrape à
  voix haute ce qui lui manqua d'une jahriyya), 219 (Yazīd b. Rūmān :
  Nāfiʿ b. Jubayr le pousse du coude — l'iftāḥ en prière).
- Taḥlīl I : rukūʿ/sujūd makrūh (Mālik et al. ; Muslim Ibn ʿAbbās :
  « magnifiez le Seigneur en rukūʿ, forcez l'invocation en sujūd — qamin
  ʾan yustajāba lakum ») ; qassī (toile de lin mêlée de soie, d'Égypte,
  village al-Qas) ; anneau d'or (hommes — Tirmidhī « la soie et l'or
  interdits aux mâles de ma communauté ») ; voix : le solitaire au mosque
  (nuire à autrui) vs imam/maison (Bājī, Ashhab « peut-être plus vif et
  plus fort »).
- Basmala : Mālik — pas une āya de la Fātiḥa (donc non obligatoire) ;
  narrations d'Anas divergentes (mawqūf/marfūʿ/« ils ne récitaient pas »/
  « ils ne la faisaient pas entendre »/« ils ouvraient par al-ḥamdu ») ;
  deux voies de jamʿ : (1) négation de récitation = négation d'audition =
  négation de jahr (Ibn Khuzayma « ils la tenaient secrète ») — objection
  : ne couvre pas tout ; (2) multiplicité de sa pratique — les sept aḥruf
  (malik/mālik, tajrī/min taḥtihā, ʾanna Llāha huwa/ʾanna Llāha l-ghaniyy
  — l'addition et la suppression toutes deux massives, la basmala dans
  certains aḥruf).
- Taḥlīl II : le rattrapage du maʾmūm (Ibn ʿUmar 218 : rattrape à voix
  haute ; ou bâtit sur ce qu'il a saisi ; cas où la divergence tombe —
  dernière rakʿa) ; l'iftāḥ : du maʾmūm à l'imam (permis — Mālik/
  Shāfiʿī/la plupart ; Nasāʾī Ubayy « n'y avait-il pas Ubayy pour me
  l'ouvrir ? » ; coufides karāha) ; d'un priant non-associé (219 —
  Ibn al-Qāsim : invalide la prière du prompteur, « sens de la
  conversation ») ; d'un non-priant (Mālik : pas de mal).
- Istimḥār : Muslim Ibn ʿAbbās (« on m'a interdit de réciter incliné ou
  prosterné… »).
- Préparation préalable : leçon SUIVANTE 12961 (vertu de la Fātiḥa) —
  sabʿ al-mathānī (sept versets répétés à chaque rakʿa / louange doublée),
  unāziʿu (« je tire le Coran à moi — l'autre le tire de moi »), ḥattā
  taʿlama sūra + vertus de la Fātiḥa + Mālik sur la Fātiḥa derrière l'imam.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Travailler la lecture dans la prière (<em>al-ʿamal fī l-qirāʾa fī l-ṣalāh</em>)</h1>
<p>Leçon sur la pratique de la lecture dans la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la dix-septième leçon.</p>
<ol>
<li>Connaître la manière dont le Prophète — paix et bénédiction sur lui — récitait dans la prière.</li>
<li>Distinguer la récitation de l’imam, du suivi et du solitaire dans la prière.</li>
<li>Prendre pour modèle le Messager de Dieu — paix et bénédiction sur lui — dans sa manière de réciter dans la prière.</li>
</ol>
<h2>Préambule</h2>
<p>Le Prophète — paix et bénédiction sur lui — prit grand soin de la lecture dans la prière : il en exposa le volume, la manière et le statut — quant à l’imam, au suivi et au solitaire.</p>
<p>Comment donc était la récitation du Prophète — paix et bénédiction sur lui — dans la prière ? Et la <em>basmala</em> est-elle un verset de la Fātiḥa, ou non ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Nāfiʿ, d’après Ibrāhīm ibn ʿAbd Allāh ibn Ḥunayn, d’après son père, d’après ʿAlī ibn Abī Ṭālib : « que le Messager de Dieu — paix et bénédiction sur lui — interdit de porter le <em>qassī</em>, de se baguer d’or, et de réciter le Coran dans l’inclinaison. » [Muwaṭṭaʾ, n° 214]</li>
<li>D’après Mālik, d’après Yaḥyā ibn Saʿīd, d’après Muḥammad ibn Ibrāhīm ibn al-Ḥārith al-Taymī, d’après Abū Ḥāzim al-Tammār, d’après al-Bayāḍī : « que le Messager de Dieu — paix et bénédiction sur lui — sortit vers des gens qui priaient, et dont les voix s’étaient élevées par la récitation ; il dit : “Celui qui prie s’entretient à voix basse avec son Seigneur : qu’il considère donc ce par quoi il s’entretient avec Lui — et que nul parmi vous ne domine l’autre en [récitant] le Coran.” » [Muwaṭṭaʾ, n° 215]</li>
<li>D’après Mālik, d’après Ḥumayd al-Ṭawīl, d’après Anas ibn Mālik : « qu’il dit : Je me tins [en prière] derrière Abū Bakr al-Ṣiddīq, ʿUmar et ʿUthmān — tous ne récitaient pas “Au nom de Dieu, le Miséricordieux, le Très-Miséricordieux” quand ils ouvraient la prière. » [Muwaṭṭaʾ, n° 216]</li>
<li>D’après Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar, quand une partie de la prière lui échappait avec l’imam — de ce où l’imam récitait à voix haute —, quand l’imam avait salué, se levait, récitait pour lui-même ce qu’il rattrapait, et le faisait à voix haute. » [Muwaṭṭaʾ, n° 218]</li>
<li>D’après Mālik, d’après Yazīd ibn Rūmān : « qu’il dit : Je priais aux côtés de Nāfiʿ ibn Jubayr ibn Muṭʿim : il me poussait du coude, et je lui ouvrais [le verset] — tandis que nous priions. » [Muwaṭṭaʾ, n° 219]</li>
</ul>
<p>[La <em>basmala</em> du hadith d’Anas a été restaurée d’après le corps même de la leçon : son emplacement imprimé ﴿﴾ est vide dans la source numérisée — perte OCR.]</p>
<h3>Explication lexicale</h3>
<ul>
<li><em>al-qassī</em> : avec fatha du <em>qāf</em> et kasre du <em>sīn</em> doublé — des étoffes rayées de soie, qui se fabriquaient à al-Qas, lieu d’Égypte.</li>
<li><em>yunājī</em> (« s’entretient à voix basse ») : de l’entretien confidentiel (<em>munājāt</em>) — qui est la présence du cœur et l’humilité recueillie dans la prière ; et l’entretien confidentiel du Seigneur avec Son serviteur est Sa conversion vers lui par miséricorde et agrément, et ce qu’Il lui ouvre des sciences et des secrets.</li>
<li><em>yaghmizunī</em> (« il me pousse du coude ») : avec kasre du <em>mīm</em>, présent de <em>ghamaza</em>, sur la mesure de <em>ḍaraba</em> — il me fait signe.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Expose le statut de la récitation dans l’inclinaison et la prosternation.</li>
<li>Quand est-il permis d’élever la voix dans la récitation de la prière, et quand ne l’est-il pas ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : les règles de la lecture dans la prière</h3>
<h4>Le statut de la lecture dans l’inclinaison et la prosternation</h4>
<p>L’imam Mālik et d’autres savants tinrent que la lecture dans l’inclinaison et la prosternation est réprouvée — d’après ce qui fut rapporté de ʿAlī ibn Abī Ṭālib — que Dieu soit satisfait de lui — : « que le Messager de Dieu — paix et bénédiction sur lui — interdit de porter le qassī, de se baguer d’or, et de réciter le Coran dans l’inclinaison » — une narration ajoute : « et dans la prosternation » ; et d’après ce que rapporta Muslim, d’après Ibn ʿAbbās, remontant [au Prophète] : « Or donc : il m’a été interdit de réciter dans l’inclinaison et la prosternation. Quant à l’inclinaison : magnifiez-y le Seigneur ; et quant à la prosternation : forcez-y l’invocation — il est digne qu’elle vous soit exaucée. » — l’interdit vaut ici répugnance. Et le hadith du chapitre comprend :</p>
<ul>
<li>l’interdit de porter le <em>qassī</em> — étoffes de lin mêlé de soie, apportées d’Égypte, rapportées à un village du littoral nommé al-Qas ;</li>
<li>l’interdit de se baguer d’or — général, dans la prière et hors d’elle ; l’interdit y vaut prohibition, et vise les hommes à l’exclusion des femmes — d’après sa parole — paix et bénédiction sur lui — : « La soie et l’or ont été interdits aux mâles de ma communauté, et rendus licites à ses femelles. » [Rapporté par at-Tirmidhī dans ses <em>Sunan</em>]</li>
</ul>
<h4>Le statut de l’élévation de la voix dans la lecture de la prière</h4>
<p>Il vient dans le hadith de la leçon que le Prophète — paix et bénédiction sur lui — sortit vers les Compagnons qui priaient, leurs voix s’étant élevées par la récitation, et qu’il les en interdit, en sa parole : « que nul parmi vous ne domine l’autre en [récitant] le Coran » — hadith porté sur celui qui prie seul dans la mosquée alors que d’autres sont avec lui : car à élever la voix en récitation, il nuit à autrui, en l’empêchant de se tourner vers la prière avec recueillement et quiétude, et de méditer ce dont il s’entretient avec son Seigneur du Coran.</p>
<p>Quant à la lecture de l’imam — dans l’obligatoire ou autre —, ou celle du solitaire en sa maison : élever la voix n’y fait aucun mal — d’après ce que rapporta l’imam Mālik de son oncle Abū Suhayl ibn Mālik, d’après son père : « Nous entendions la récitation de ʿUmar ibn al-Khaṭṭāb depuis la maison d’Abū Jahm, sur le <em>balāṭ</em> [pavé]. » [Muwaṭṭaʾ, n° 217]</p>
<p>Al-Bājī a dit : « Nul mal que l’imam élève la voix en ce qu’il récite à voix haute parmi les obligations — et de même les surérogatoires. » Et Ashhab rapporta de Mālik : « Nul mal que celui qui prie en surérogation en sa maison élève la voix en récitation — peut-être est-il plus vif et plus fort [à réciter]. »</p>
<h4>La lecture de la basmala dans la prière</h4>
<p>Les imams divergèrent sur le statut de la lecture de la basmala dans la prière, et la cause de leur divergence remonte au désaccord sur la basmala elle-même : est-elle un verset de la Fātiḥa, ou n’en est-elle pas un ?</p>
<p>L’imam Mālik tint qu’elle n’est pas un verset de la Fātiḥa — partant, sa lecture n’est pas obligatoire dans la prière. Au nombre de ses preuves : le hadith d’Anas ibn Mālik : « Je me tins [en prière] derrière Abū Bakr al-Ṣiddīq, ʿUmar et ʿUthmān — tous ne récitaient pas “Au nom de Dieu, le Miséricordieux, le Très-Miséricordieux” quand ils ouvraient la prière. »</p>
<p>Les narrations d’Anas ibn Mālik divergèrent en ce hadith : les uns le rapportèrent arrêté (<em>mawqūf</em>), comme dans le <em>Muwaṭṭaʾ</em> ; les autres, remontant [au Prophète] : « Je priai derrière le Messager de Dieu — paix et bénédiction sur lui —, Abū Bakr, ʿUmar et ʿUthmān — tous… » [le hadith] ; d’autres [rapportèrent] : « ils ne récitaient pas “Au nom de Dieu, le Miséricordieux, le Très-Miséricordieux” » ; d’autres : « ils ne la faisaient pas entendre » ; d’autres : « ils ouvraient la récitation par “Louange à Dieu, Seigneur des mondes” » — et d’autres formules encore, qu’al-Zarqānī mentionne. Les savants ont, pour concilier ces narrations, deux voies :</p>
<ul>
<li>La première voie : porter la négation de la récitation sur la négation de l’audition, et la négation de l’audition sur la négation [de la récitation] à voix haute — l’appuie ce qui vient dans la narration d’Ibn Khuzayma : « ils tenaient secrète “Au nom de Dieu, le Miséricordieux, le Très-Miséricordieux”. » [Ṣaḥīḥ d’Ibn Khuzayma] Et quand la conciliation est possible, il faut s’y arrêter. On objecta à cette conciliation qu’elle ne s’étend pas à toutes les narrations : certaines ont « ils la faisaient entendre », d’autres « ils ne la délaissaient pas ».</li>
<li>La seconde voie : tous les hadiths venus sur la basmala — en l’affirmatif comme en le négatif — sont sains, et portés sur leur apparent ; et la conciliation entre eux : ils se rapportent à la multiplicité de son acte — paix et bénédiction sur lui —, puisqu’il lut avec elle, la délaissa, la fit entendre et la cacha. Et nulle étrangeté en cela : le Coran descendit en sept lectures (<em>aḥruf</em>), et descendit en reprises réitérées — en certaines avec addition, en certaines avec retranchement : comme la lecture <em>malik/mālik</em> dans la Fātiḥa, <em>tajrī taḥtahā/min taḥtihā</em> dans Barāʾa, <em>inna Llāha huwa l-ghaniyy/inna Llāha l-ghaniyy</em> dans al-Ḥadīd. Nul ne doute que la lecture avec l’affirmation de l’alif, de <em>min</em>, de <em>huwa</em> et leurs semblables soit massivement transmise, d’affirmation certaine, ni que la lecture avec le retranchement de cela soit massivement transmise, de retranchement certain — et la balance de l’affirmation et du retranchement y est égale. Il en va de même de la basmala : elle descendit en certains des sept <em>aḥruf</em> et ne descendit pas en certains — son affirmation est certaine, son retranchement certain, et chacune massivement transmise, et chacune dans les sept : on ne s’étonne donc pas de l’affirmation par qui affirma, ni de la négation par qui nia.</li>
</ul>
<h3>Deuxièmement : le statut de la lecture par le suivi de ce qui lui échappa, et l’iftāḥ sur l’imam</h3>
<h4>Le rattrapage par le suivi de ce qui lui échappa de la prière récitée à voix haute</h4>
<p>Il fut rapporté de ʿAbd Allāh ibn ʿUmar qu’il rattrapait ce qui lui avait échappé de la prière à voix haute sur le mode de ce qui lui avait échappé — comme il vient dans le hadith : « il récitait pour lui-même ce qu’il rattrapait, et le faisait à voix haute » ; et il se peut qu’il bâtissait sur ce qu’il avait saisi et y récitât à voix haute, parce que c’est la fin de sa prière — comme quand lui échappe une rakʿa de l’aube, ou deux du maghrib, ou trois de la ʿishāʾ : la divergence tombe alors, et le suivi doit réciter à voix haute dans son rattrapage selon les deux avis.</p>
<h4>L’iftāḥ (l’ouverture du verset) sur celui qui prie, pendant la prière</h4>
<ul>
<li>L’iftāḥ sur l’imam par le suivi : Mālik, al-Shāfiʿī et la plupart des savants tinrent sa permission — car ni Dieu ni Son Messager ne l’interdirent sur un mode probant ; et [le Prophète] — paix et bénédiction sur lui — « hésita sur un verset ; quand il se détourna [de la prière], il dit : N’y avait-il pas, parmi les gens, Ubayy, pour me l’ouvrir ? » [Rapporté par an-Nasāʾī] — les coufides le réprouvèrent.</li>
<li>L’iftāḥ sur celui qui prie par un autre qui prie : l’apparent de l’athar que rapporta l’imam Mālik de Yazīd ibn Rūmān est qu’il est permis à celui qui prie d’ouvrir [le verset] pour un autre qui n’est pas avec lui dans sa prière — car c’est là une récitation de Coran dans une prière ; et c’est pourquoi Yazīd ibn Rūmān dit : « Je priais aux côtés de Nāfiʿ ibn Jubayr ibn Muṭʿim : il me poussait du coude, et je lui ouvrais [le verset] — tandis que nous priions. » Ibn al-Qāsim tint, lui, que la prière de qui ouvre [le verset] à qui n’est pas avec lui dans une prière est invalide — car, si c’est une récitation de Coran, c’est cependant dans le sens de la conversation.</li>
<li>L’iftāḥ sur celui qui prie par qui n’est pas en prière : il fut rapporté de l’imam Mālik qu’il n’y a pas de mal.</li>
</ul>
<h2>L’évaluation</h2>
<ol>
<li>Comment le suivi récite-t-il ce qui lui a échappé de la prière à voix haute ?</li>
<li>Expose la cause de la divergence des juristes sur le statut de la lecture de la basmala dans la prière.</li>
<li>Est-il permis d’ouvrir [le verset] à celui qui prie, par un autre qui prie ?</li>
</ol>
<h2>L’exploitation</h2>
<p>D’après Ibn ʿAbbās — que Dieu soit satisfait de lui — : « que le Messager de Dieu — paix et bénédiction sur lui — a dit : Il m’a été interdit de réciter incliné ou prosterné. Quant à l’inclinaison : magnifiez-y le Seigneur ; et quant à la prosternation : forcez-y l’invocation — il est digne qu’elle vous soit exaucée. » [Rapporté par Muslim dans son <em>Ṣaḥīḥ</em>]</p>
<ol>
<li>Quel est le statut de la récitation du Coran dans l’inclinaison et la prosternation ?</li>
<li>Pourquoi le Prophète — paix et bénédiction sur lui — a-t-il interdit la récitation dans l’inclinaison ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Explique ce qui suit : <em>as-sabʿ al-mathānī</em> (« les sept répétées ») – <em>unāziʿu al-Qurʾān</em> (« je tire le Coran à moi ») – <em>ḥattā taʿlama sūra</em> (« jusqu’à ce que tu apprennes une sūra »).</li>
<li>Cite quelques mérites de la sūra de la Fātiḥa.</li>
<li>Quel est l’avis de l’imam Mālik sur la lecture de la Fātiḥa derrière l’imam ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12958":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12958 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12958 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
