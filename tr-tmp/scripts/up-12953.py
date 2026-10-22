#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12953 (hadith-1es, la lecture dans la
prière — Muwaṭṭaʾ n° 209-213, 220-223, + Bukhārī/Muslim/Ibn Māja).

Conventions main (cf. 12875, 12884-12948 du même livre) :
- h1 « Lire dans la prière (al-qirāʾa fī l-ṣalāh) », 16e leçon ; objectifs
  en infinitifs (source 1re personne).
- Muwaṭṭaʾ 211 (al-Ṣunābiḥī derrière Abū Bakr au maghrib : Umm al-Qurʾān
  + qiṣār aux deux premières, 3e rakʿa Umm al-Qurʾān + Āl ʿImrān 3 : 8),
  212 (Ibn ʿUmar seul : les quatre rakʿa — Umm + sūra, parfois 2-3 sūras),
  213 (al-Barāʾ : ʿishāʾ avec al-Tīn), 220 (Abū Bakr : ṣubḥ avec la
  Baqara aux deux rakʿa), 221 (ʿUmar : Yūsuf + al-Ḥajj, lecture lente —
  Ibn ʿĀmir b. Rabīʿa), 222 (Furāfiṣa b. ʿUmayr : ʿUthmān répétait Yūsuf),
  223 (Ibn ʿUmar en voyage : les dix premières sūras du mufaṣṣal) ; taḥlīl
  cite 209 (Jubayr b. Muṭʿim : Ṭūr au maghrib) et 210 (Umm al-Faḍl :
  Mursalāt — la dernière qu'elle lui entendit).
- « الدمنة » (OCR) = المدينة (Jubayr vint à Médine au sujet des captifs
  de Badr, encore polythéiste) — restitué du contexte historique.
- VERSETS restaurés (emplacements OCR vides) : Āl ʿImrān 3 : 8 (dans le
  hadith 211) ; al-Insān 76 : 6 (exemple du bā' portant sens de min —
  Ibn al-Jawzī) ; aṭ-Ṭūr 52 : 33-35 (« mon cœur faillit s'envoler » —
  Bukhārī, Tafsīr) ; al-Mursalāt 77 : 1 ; al-Inshiqāq 84 : 1 (Abū
  Hurayra, Ṣaḥīḥayn). Réfs imprimées toutes concordantes.
- Taḥlīl I : maghrib — qiṣār (Sulaymān b. Yasār/Abū Hurayra, Ibn Māja) ;
  Ṭūr (Jubayr + Ibn al-Jawzī bā' = min + Bukhārī le cœur) ; Mursalāt
  (Umm al-Faḍl ; conciliation avec ʿĀʾisha Bukhārī : mosquée vs maison,
  Nasāʾī ; « il sortit vers nous » = du lieu où il était couché) ; ṭūlā
  l-ṭūlayayn (Marwān/Zayd b. Thābit, Bukhārī — Aʿrāf + Māʾida/Anʿām/
  Yūnus disputés) ; jamʿ (bayān al-jawāz / absence de peine ; Ibn
  Khuzayma : ikhtilāf mubāḥ, allègement pour l'imam).
- Taḥlīl II : ʿishāʾ — Inshiqāq (awṣāṭ, ḥaḍar — Abū Hurayra Ṣaḥīḥayn) vs
  al-Tīn (qiṣār — Barāʾ, voyage : Bukhārī « en voyage »).
- Taḥlīl III : ṣubḥ — Abū Bakr (Baqara), ʿUmar (Yūsuf+Ḥajj lentes),
  ʿUthmān (Yūsuf répétée), Ibn ʿUmar (voyage), Umm Salama (Ṭūr,
  Bukhārī), Jābir b. Samura (Qāf, Muslim) ; Ibn ʿAbd al-Barr (ils
  connaissaient le zèle de ceux derrière eux) ; recommandation (Mālik et
  groupe — hiver plus qu'été) ; aujourd'hui : allègement requis —
  Bukhārī (« le faible, le malade, le vieillard ») + Muʿādh («
  a-fatānun anta — sabbiḥ, al-shams, al-layl »).
- Taḥlīl IV : Abū Qatāda Ṣaḥīḥayn (ẓuhr/ʿaṣr : Umm + 2 sūras aux deux
  premières, Umm al-Kitāb aux deux dernières, allongement de la 1re) ;
  l'usage d'Ibn ʿUmar (212) contredit par Mālik et le jumhūr (karāha
  après la Fātiḥa aux deux dernières + 3e du maghrib).
- Istimḥār : Ibn ʿAbd al-Barr via Zarqānī 1/306 (mubāḥ, nulle mesure
  fixée après la Fātiḥa — consensus ; pas de prière sans récitation).
- Lexique : mufaṣṣal et ses trois divisions mālikites (ṭiwāl Ḥujurāt→
  Nāziʿāt ; awṣāṭ ʿAbasa→Layl ; qiṣār Ḍuḥā→fin), Umm al-Qurʾān (3
  étymologies), fī l-arbaʿ jamīʿan, sūra sūra.
- Préparation préalable : leçon SUIVANTE 12958 — al-qassī (brocart),
  yunājī (s'entretient à voix basse), yaghmizunī (me pousse du coude) +
  lecture au rukūʿ/sujūd + basmala.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Lire dans la prière (<em>al-qirāʾa fī l-ṣalāh</em>)</h1>
<p>Leçon sur la lecture dans la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la seizième leçon.</p>
<ol>
<li>Connaître ce que le Prophète — paix et bénédiction sur lui — récitait dans sa prière.</li>
<li>Saisir les motifs de l’allongement et de l’allègement dans la prière.</li>
<li>S’appliquer à réciter dans ma prière ce que récitait le Messager de Dieu — paix et bénédiction sur lui — autant qu’il m’est possible.</li>
</ol>
<h2>Préambule</h2>
<p>Dieu — Puissant et Majestueux — a ordonné de réciter dans la prière ce qui est facilité du Coran ; et les hadiths rapportés du Prophète — paix et bénédiction sur lui —, comme les athars transmis des Compagnons et des Suivants, sont nombreux quant au volume de Coran que le Prophète — paix et bénédiction sur lui — récitait dans la prière. En retournant à ces hadiths et à ces athars, nous trouvons que le volume de sa récitation — paix et bénédiction sur lui — variait d’une prière à l’autre.</p>
<p>Quel était donc ce volume qu’il récitait — paix et bénédiction sur lui — dans sa prière ? Et d’où vient qu’il variait d’une prière à l’autre ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Abū ʿUbayd, affranchi de Sulaymān ibn ʿAbd al-Malik, d’après ʿAbbād ibn Nusayy, d’après Qays ibn al-Ḥārith, d’après Abū ʿAbd Allāh al-Ṣunābiḥī : « qu’il dit : J’arrivai à Médine sous le califat d’Abū Bakr al-Ṣiddīq, et je priai derrière lui au maghrib : aux deux premières rakʿa il récita la Mère du Coran et une sūra [puis une] sūra des courtes du <em>mufaṣṣal</em> ; puis il se tint debout à la troisième, et je m’approchai de lui — mes vêtements allaient presque toucher les siens — et je l’entendis réciter la Mère du Coran et ce verset :</li>
</ul>
<p>« Ô notre Seigneur ! ne fais pas dévier nos cœurs après que Tu nous as guidés, et accorde-nous de Ta part une miséricorde — c’est Toi, certes, le Donateur. » (āl ʿImrān, 3 : 8)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>[Muwaṭṭaʾ, n° 211]</p>
<ul>
<li>D’après Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar, quand il priait seul, récitait dans les quatre [rakʿa] toutes — à chaque rakʿa la Mère du Coran et une sūra du Coran ; et il récitait parfois de deux sūras, ou de trois, en une seule rakʿa de la prière obligatoire ; et il récitait aux deux rakʿa du maghrib, de la même façon, la Mère du Coran et une sūra [puis une] sūra. » [Muwaṭṭaʾ, n° 212]</li>
<li>D’après Mālik, d’après Yaḥyā ibn Saʿīd, d’après ʿAdī ibn Thābit al-Anṣārī, d’après al-Barāʾ ibn ʿĀzib : « qu’il dit : Je priai avec le Messager de Dieu — paix et bénédiction sur lui — la ʿishāʾ, et il y récita <em>al-Tīn wa-l-zaytūn</em> (le figuier et l’olivier). » [Muwaṭṭaʾ, n° 213]</li>
<li>D’après Mālik, d’après Hishām ibn ʿUrwa, d’après son père : « qu’Abū Bakr al-Ṣiddīq fit la prière de l’aube et y récita la sūra de la Vache aux deux rakʿa toutes deux. » [Muwaṭṭaʾ, n° 220]</li>
<li>D’après Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar récitait à l’aube, en voyage, les dix premières sūras du <em>mufaṣṣal</em> — à chaque rakʿa la Mère du Coran et une sūra. » [Muwaṭṭaʾ, n° 223]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>qiṣār al-mufaṣṣal</em> (« les courtes du mufaṣṣal ») : le <em>mufaṣṣal</em> désigne les sūras courtes du Coran, que sépare fréquemment la <em>basmala</em> ; ses longues (<em>ṭiwāl</em>), chez les mālikites, vont d’al-Ḥujurāt à an-Nāziʿāt ; ses moyennes (<em>awṣāṭ</em>), de ʿAbasa à al-Layl ; ses courtes (<em>qiṣār</em>), d’aḍ-Ḍuḥā à la fin du Coran.</li>
<li><em>Umm al-Qurʾān</em> (« la Mère du Coran ») : la <em>mère</em> d’une chose est son principe ; la Fātiḥa fut ainsi nommée parce qu’elle est le principe du Coran et la première récitée dans la prière ; et il a été dit : parce qu’elle précède [le reste], comme si elle le conduisait.</li>
<li><em>fī l-arbaʿ jamīʿan</em> (« dans les quatre toutes ») : dans les quatre rakʿa.</li>
<li><em>sūra sūra</em> (« une sūra [puis une] sūra ») : c’est-à-dire une sūra à chaque rakʿa.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Expose ce que le Prophète — paix et bénédiction sur lui — récitait dans sa prière.</li>
<li>D’où vient la variation du volume qu’il récitait — paix et bénédiction sur lui — en une même prière ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le volume de la lecture au maghrib</h3>
<p>Les narrations divergèrent sur ce que le Prophète — paix et bénédiction sur lui — récitait au maghrib. Il fut rapporté de lui :</p>
<ul>
<li>qu’il récitait en cette prière les courtes du <em>mufaṣṣal</em> — d’après le hadith de Sulaymān ibn Yasār, d’après Abū Hurayra : « Je n’ai vu personne dont la prière ressemblât davantage à celle du Messager de Dieu — paix et bénédiction sur lui — que tel homme. Sulaymān dit : il récitait à l’aube les longues du <em>mufaṣṣal</em>, et au maghrib les courtes du <em>mufaṣṣal</em>. » [Rapporté par Ibn Māja dans ses <em>Sunan</em>] — et c’est ce que faisait Abū Bakr al-Ṣiddīq — que Dieu soit satisfait de lui — sous son califat.</li>
<li>qu’il récitait en cette prière la sūra de aṭ-Ṭūr — l’atteste le hadith de Jubayr ibn Muṭʿim, quand il vint à Médine au sujet des captifs de Badr, étant alors encore en son polythéisme : « J’ai entendu le Messager de Dieu — paix et bénédiction sur lui — réciter aṭ-Ṭūr au maghrib. » [Muwaṭṭaʾ, n° 209] — Ibn al-Jawzī a dit : il se peut que le <em>bāʾ</em> [de « réciter AVEC aṭ-Ṭūr »] porte le sens de « de » [une partie de], comme la parole de Dieu — Exalté :</li>
</ul>
<p>« ...une source où boivent les serviteurs de Dieu, et qu’ils font jaillir à profusion. » (al-Insān, 76 : 6)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR. Le <em>bāʾ</em> de « boivent par elle » y porte le sens de « de laquelle » — l’exemple invoqué par Ibn al-Jawzī.]</p>
<p>Et d’autres narrations indiquent qu’il — paix et bénédiction sur lui — récita la sūra entière : ainsi, chez al-Bukhārī, au [livre du] Tafsīr : « Quand il atteignit ces versets :</p>
<p>« Ou bien disent-ils : “Il l’a forgé” ? — non : ils ne croient pas. Qu’ils produisent donc un pareil discours, s’ils sont véridiques. Ont-ils été créés de rien ? Ou sont-ils eux-mêmes les créateurs ? » (aṭ-Ṭūr, 52 : 33-35)</p>
<p>[Versets restaurés d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>— mon cœur faillit s’envoler. »</p>
<ul>
<li>qu’il récitait en cette prière al-Mursalāt — l’atteste le hadith d’Umm al-Faḍl bint al-Ḥārith, quand elle entendit son fils ʿAbd Allāh ibn ʿAbbās réciter :</li>
</ul>
<p>« Par les envoyées, en rafales » (al-Mursalāt, 77 : 1)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>— elle lui dit : « Mon fils, tu viens de me rappeler, par ta récitation de cette sūra, [un souvenir] : c’est bien la dernière que j’entendis réciter au Messager de Dieu — paix et bénédiction sur lui — au maghrib. » [Muwaṭṭaʾ, n° 210] — Et il n’y a nulle contradiction entre sa parole et ce que contient le <em>Ṣaḥīḥ</em> d’al-Bukhārī, au hadith d’ʿĀʾisha — que Dieu soit satisfait d’elle : la prière que le Prophète — paix et bénédiction sur lui — fit avec ses Compagnons durant sa maladie de mort était le ẓuhr — car celle que rapporta ʿĀʾisha eut lieu dans la mosquée, et celle que rapporta Umm al-Faḍl, dans sa maison, comme le rapporte an-Nasāʾī. Et ce qui vint en certaines narrations de sa parole « il sortit vers nous » se rapporte à ceci : il sortit du lieu où il était couché, vers ceux qui étaient dans la maison, et pria avec eux.</li>
<p>Et qu’il récitait en cette prière « la plus longue des deux longues » (<em>ṭūlā l-ṭūlayayn</em>) — c’est-à-dire la plus longue des deux [ grandes ] sūras longues — d’après ce que rapporta al-Bukhārī de Marwān ibn al-Ḥakam, qui dit : « Zayd ibn Thābit me dit : Qu’as-tu à réciter au maghrib les courtes du <em>mufaṣṣal</em>, alors que j’ai entendu le Prophète — paix et bénédiction sur lui — réciter la plus longue des deux longues ? » — les narrations s’accordèrent à identifier « la plus longue » à al-Aʿrāf, et divergèrent sur l’autre : al-Māʾida, al-Anʿām ou Yūnus.</p>
<p>La voie de conciliation de ces hadiths : il — paix et bénédiction sur lui — allongeait parfois la lecture au maghrib, soit pour faire connaître la permission, soit par la connaissance qu’il n’y avait nulle peine pour ceux qui suivaient ; et rien, dans les hadiths de l’allongement, n’indique que cela se répéta de lui — paix et bénédiction sur lui. Ibn Khuzayma a dit : ceci relève de la divergence permise (<em>ikhtilāf mubāḥ</em>) — il est loisible à celui qui prie de réciter au maghrib, comme en toutes prières, ce qu’il aime ; seulement, s’il est imam, l’allègement de la lecture lui est recommandé.</p>
<h3>Deuxièmement : le volume de la lecture à la ʿishāʾ</h3>
<p>Le Prophète — paix et bénédiction sur lui — pria en cette prière avec la sūra de l’Inshiqāq — qui est des moyennes du <em>mufaṣṣal</em> — comme il y pria aussi avec la sūra du figuier, qui est des courtes du <em>mufaṣṣal</em> : d’après al-Barāʾ ibn ʿĀzib : « Je priai avec le Messager de Dieu — paix et bénédiction sur lui — la ʿishāʾ, et il y récita <em>al-Tīn wa-l-zaytūn</em> » — c’est-à-dire : il récita en une rakʿa une sūra commençant par « le figuier et l’olivier ». Et s’il n’y récita que les courtes du <em>mufaṣṣal</em>, c’est qu’il était en voyage — comme l’indique la version d’al-Bukhārī : « il était en voyage… » — or le voyage appelle l’allègement.</p>
<p>Quant à ce qui fut rapporté d’Abū Hurayra — que Dieu soit satisfait de lui — dans les deux <em>Ṣaḥīḥ</em> : qu’il récita en cette prière :</p>
<p>« Quand le ciel se fendra » (al-Inshiqāq, 84 : 1)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>— cela se rapporte à la résidence : c’est pourquoi il y récita les moyennes du <em>mufaṣṣal</em>.</p>
<h3>Troisièmement : le volume de la lecture à l’aube</h3>
<p>Les athars des Compagnons divergèrent en cela : il fut rapporté d’Abū Bakr qu’il récita en cette prière la sūra de la Vache aux deux rakʿa ; ʿUmar ibn al-Khaṭṭāb y récita la sūra de Yūsuf et la sūra du Pèlerinage — d’après ce que rapporta l’imam Mālik, d’après Hishām ibn ʿUrwa, d’après son père, qu’il entendit ʿAbd Allāh ibn ʿĀmir ibn Rabīʿa dire : « Nous avons prié derrière ʿUmar ibn al-Khaṭṭāb la prière de l’aube, et il y récita la sūra de Yūsuf et la sūra du Pèlerinage, en une lecture lente. Je dis : par Dieu, il devait donc se tenir debout quand l’aube se levait ! Il dit : Oui. » [Muwaṭṭaʾ, n° 221]</p>
<ul>
<li>ʿUthmān y récita, maintes fois, la sūra de Yūsuf — d’après ce que rapporta l’imam Mālik par sa chaîne : al-Furāfiṣa ibn ʿUmayr al-Ḥanafī dit : « Je ne tins la sūra de Yūsuf que de la récitation qu’en faisait ʿUthmān ibn ʿAffān à l’aube, tant il la répétait. » [Muwaṭṭaʾ, n° 222] Et ʿAbd Allāh ibn ʿUmar y récita, en voyage, les dix premières sūras du <em>mufaṣṣal</em>. L’imam Mālik ne mentionna, en cette question, aucun hadith remontant [au Prophète] ; or il est établi dans le <em>Ṣaḥīḥ</em> d’al-Bukhārī, d’après Umm Salama : « qu’il — paix et bénédiction sur lui — y récita aṭ-Ṭūr » ; et dans le <em>Ṣaḥīḥ</em> de Muslim, d’après Jābir ibn Samura : « qu’il — paix et bénédiction sur lui — récita à l’aube la sūra de Qāf ».</li>
</ul>
<p>Cette divergence suit la diversité des circonstances. Ibn ʿAbd al-Barr a dit : je ne doute pas qu’Abū Bakr, ʿUmar et ʿUthmān connaissaient, du zèle de ceux qui étaient derrière eux, ce qui les portait à allonger par moments.</p>
<p>En cela [se trouve] la recommandation d’une longue lecture à l’aube — Mālik et un groupe l’ont recommandée — et cela vaut mieux en hiver qu’en été. Quant à aujourd’hui : l’allègement s’impose, selon sa parole — paix et bénédiction sur lui — : « Quand l’un de vous prie pour les gens, qu’il allège : il y a parmi eux le faible, le malade et le vieillard ; et quand l’un de vous prie pour soi-même, qu’il allonge à son gré. » [Rapporté par al-Bukhārī dans son <em>Ṣaḥīḥ</em>] Et il dit à Muʿādh : « Es-tu un tentateur ? Plût au ciel que tu eusses prié avec <em>sabbiḥ isma rabbika</em>, <em>al-shams wa-ḍuhāhā</em>, <em>al-layl idhā yaghshā</em> — car prient derrière toi le vieillard, le faible et celui qui a un besoin. » [Rapporté par al-Bukhārī dans son <em>Ṣaḥīḥ</em>]</p>
<h3>Quatrièmement : la lecture au ẓuhr et à lʿasr</h3>
<p>Il est établi dans les deux <em>Ṣaḥīḥ</em>, d’après Abū Qatāda : « que le Prophète — paix et bénédiction sur lui — récitait au ẓuhr, aux deux premières, la Mère du Coran et deux sūras ; et aux deux dernières rakʿa, la Mère du Livre seul — allongeant la première rakʿa plus que la seconde ; et de même à lʿasr. »</p>
<p>Quant à ce que rapporta l’imam Mālik de Nāfiʿ — « que ʿAbd Allāh ibn ʿUmar, quand il priait seul, récitait dans les quatre [rakʿa] toutes, à chaque rakʿa la Mère du Coran et une sūra du Coran » — Mālik n’y consentit pas, ni le plus grand nombre : ils réprouvèrent plutôt de réciter quoi que ce soit après la Fātiḥa aux deux dernières [rakʿa] et à la troisième du maghrib.</p>
<h2>L’évaluation</h2>
<ol>
<li>Expose le statut de l’allongement de la lecture dans la prière.</li>
<li>Par quoi le Prophète — paix et bénédiction sur lui — récitait-il au maghrib et à la ʿishāʾ ?</li>
<li>Qu’indique la variation de la récitation du Prophète — paix et bénédiction sur lui — en une même prière ?</li>
</ol>
<h2>L’exploitation</h2>
<p>Al-Zarqānī a dit : Ibn ʿAbd al-Barr a dit : « La récitation du Prophète au maghrib d’aṭ-Ṭūr et d’al-Mursalāt, à la ʿishāʾ d’al-Tīn wa-l-zaytūn, et la récitation d’Abū Bakr de ce qui fut mentionné — tout cela relève du permis : on récite ce qu’on veut avec la Mère du Coran, pourvu qu’on ne soit pas imam — auquel cas on n’allonge pas sur ceux qui sont derrière. Son allègement — paix et bénédiction sur lui — en une occasion, et peut-être son allongement en une autre, indiquent qu’il n’est aucune mesure fixée dans la récitation après la Fātiḥa — et ceci est l’objet d’un consensus. Il a dit : “Quiconque dirige les gens, qu’il allège” — sans rien délimiter ; et ils sont d’accord qu’il n’est de prière sans récitation. » [<em>Sharḥ al-Zarqānī ʿalā l-Muwaṭṭaʾ</em>, 1/306]</p>
<ol>
<li>Qu’indique la divergence des Compagnons dans la récitation de la prière ?</li>
<li>Pourquoi demande-t-on à l’imam l’allègement dans la prière ?</li>
<li>Comment concilies-tu les hadiths de l’allongement et ceux de l’allègement dans la prière ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Explique les mots suivants : <em>al-qassī</em> (« le brocart ») – <em>yunājī</em> (« s’entretient à voix basse ») – <em>yaghmizunī</em> (« me pousse du coude »).</li>
<li>Quel est le statut de la récitation dans l’inclinaison et la prosternation ?</li>
<li>Cite le statut de la récitation de la <em>basmala</em> dans la prière.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12953":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12953 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12953 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
