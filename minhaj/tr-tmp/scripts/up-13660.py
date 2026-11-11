#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13660 (tafsir-tanawi-2, Sourate al-Isrāʾ
73-77, leçon 19 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:73-77) : <p> vide → 5 versets restaurés du
  quran-cache.
- Lexique : 4 vedettes perdues (kādū/yastafizzūnaka/l-taftarīya/laqadta) —
  restituées du tafsīr et du texte d'Ibn ʿAṭiyya.
- Citations inline perdues :
  * v73 + « إن » (la allégée de la lourde — Sībawayh ; = mā selon
    al-Farrāʾ, avec le lām = illā — VÉRIFIÉ) + « ليفتنونك » (le lām
    d'affirmation) + « كادوا » (le pronom : Quraysh ou Thaqīf — VÉRIFIÉ :
    l'original met le pronom en « كادوا », non « ليفتنونك ») + « عن الذي
    أوحينا إليك » (l'arrêt sur ce dont Dieu le sauva) ;
  * la version Quraysh : la Pierre noire + leurs idoles (Ibn Jubayr/
    Mujāhid) + la pensée intime du Prophète (al-Zajjāj — intact) + la
    rencontre nocturne d'Ibn Isḥāq (intacte) + le parallèle **Qalam 9
    « ودّوا لو تدهن فيدهنون » VÉRIFIÉ** ;
  * la version Thaqīf : différer le culte d'al-Lāt une année (Ibn
    ʿAbbās — intacte) + la faiblesse (datation médinoise) ;
  * v74 + « لولا » (la particule d'empêchement pour existence — Abū
    Ḥayyān [Baḥr 7/90] intact) + « ثبتناك » (le tathbīt, emprunté à la
    permanence) + « قد لقـدت » (il s'en fallut de peu) + « إليهم » (du
    rukūn : serrer le dos à la chose, comme au pilier du mur — VÉRIFIÉ)
    + le parallèle **Hūd 80 « أو آوي إلى ركن شديد » VÉRIFIÉ** + le duʿāʾ
    « اللهم لا تكلني إلى نفسي طرفة عين » (intact) ;
  * v75 + « ضعف الحياة وضعف الممات » (le ṭibāq — l'antithèse vie/mort ;
    Ibn ʿAbbās/Mujāhid/Qatāda/al-Ḍaḥḥāk : le double du châtiment de la
    vie et de la mort) + la glose d'Ibn ʿAṭiyya (intacte : le doublement,
    répandu pour le Prophète — salaire, douleur, châtiment de ses épouses) ;
  * v76 + « منها » (le pronom : les Juifs de Médine — l'histoire de la
    terre des prophètes en Syrie, Ḥuyayy b. Akhṭab — vs le plus juste :
    Quraysh, la sourate étant mecquoise — VÉRIFIÉ) + l'« istifzāz »
    d'Ibn ʿAbbās/Qatāda (Dār al-Nadwa, le siège du défilé, la grotte,
    Badr — al-Zajjāj) + « من الأرض » (général : du monde — ou particulier :
    La Mecque ou Médine) + le parallèle **Māʾida 33 « أو ينفوا من الأرض »
    VÉRIFIÉ** (le manuel imprime « 35 » — erreur d'adjacence notée) ;
  * v77 + « سنة » (le naṣb de maṣdar ; al-Farrāʾ : elision du kāf — d'où
    l'interdit de s'arrêter sur « قليلا » — VÉRIFIÉ : l'original met la
    pause sur « قليلاً », non « من رسلنا » comme ma première analyse le
    suggérait) ;
  * taqwīm 2 : « لولا » (l'empêchement pour existence — le Prophète
    n'inclina point) ;
  * istithmār : citation d'Ibn al-ʿArabī [Aḥkām al-Qurʾān 3/306]
    INTACTE (le pavillon de l'infaillibilité) ;
  * iʿdād : 3 expressions du lexique de 13676 (v78-80 : dulūk al-shams/
    ghasaq al-layl/qurʾān al-fajr) + la divergence du **dulūk** en « أقم
    الصلاة لدلوك الشمس » (v78 — confirmée par la discussion de la leçon
    suivante : le déclin vs le coucher) — noté."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 73 à 77</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 73 à 77, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 19).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître les grâces de Dieu, le Très-Haut, envers Son prophète — paix et bénédiction sur lui —, et Sa préservation de lui des tentations des associateurs.</li>
<li>Conclure les causes du complot des associateurs pour faire sortir le Prophète — paix et bénédiction sur lui — de La Mecque.</li>
<li>Se rappeler le soin de Dieu, le Très-Haut, envers Ses serviteurs, et leur garde de tout mal.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Quand Dieu, le Très-Haut, eut dénombré Ses grâces envers Sa création aux versets précédents, et éclairci leurs degrés, le Glorifié informa, en ces versets, de Son soutien à Son messager — paix et bénédiction sur lui —, avec l’affirmation de Sa préservation de lui face aux associateurs et leurs tromperies, quand ils tentèrent de lui confondre les choses — paix et bénédiction sur lui —, de le détourner de la loi de Dieu, le Très-Haut, et de le porter à modifier la révélation de Dieu et à agréer ce qu’ils adorent en dehors de Dieu.</p>
<p>Comment Dieu, le Très-Haut, préserva-t-Il Son messager — paix et bénédiction sur lui — de la tentation des associateurs ? Et quelle est la fin de qui guerre contre Dieu et Son messager ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Ils ont failli te détourner de ce que Nous t’avions révélé, [dans l’espoir] qu’à la place de ceci, tu inventes quelque chose d’autre et (l’imputes) à Nous. (73) Et alors, ils t’auraient pris pour ami intime. (74) Et si Nous ne t’avions pas raffermi, tu aurais bien failli t’incliner quelque peu vers eux. (75) Alors, Nous t’aurions certes fait goûter le double [supplice] de la vie et le double [supplice] de la mort ; et ensuite tu n’aurais pas trouvé de secoureur contre Nous. (76) En vérité, ils ont failli t’inciter à fuir du pays pour t’en bannir. Mais dans ce cas, ils n’y seraient pas restés longtemps après toi. (77) Telle fut la règle appliquée par Nous à Nos messagers que Nous avons envoyés avant toi. Et tu ne trouveras pas de changement en Notre règle. » (al-Isrāʾ, 73-77)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>kādū</em> (ils ont failli) : ils approchèrent.</li>
<li><em>yastafizzūnaka</em> (t’inciter à fuir) : te délogent et te détournent.</li>
<li><em>l-taftarīya</em> (tu inventes) : que tu forges sur Nous autre que ce que Nous t’avons révélé.</li>
<li><em>laqadta</em> (tu aurais failli) : incliner et s’établir.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Quel est le stratagème des associateurs contre le Prophète — paix et bénédiction sur lui — porté par les versets ?</li>
<li>Quel fut le second plan des associateurs après l’échec du premier ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la tentative des associateurs de tenter le Prophète — paix et bénédiction sur lui</h3>
<p>Dieu, le Très-Haut, expose en ces versets la tentative des associateurs de tenter le Messager — paix et bénédiction sur lui. Le Glorifié dit :</p>
<p>« Ils ont failli te détourner de ce que Nous t’avions révélé, [dans l’espoir] qu’à la place de ceci, tu inventes quelque chose d’autre et (l’imputes) à Nous. Et alors, ils t’auraient pris pour ami intime. » (al-Isrāʾ, 73)</p>
<p>L’<em>inna</em> ici est, chez Sībawayh, l’allégée de la lourde ; et le <em>lām</em> de Sa parole : <em>li-yaftinūnak(a)</em> (“ ils détournent ”) est <em>lām</em> d’affirmation. Et cet <em>inna</em> est, chez al-Farrāʾ, au sens de <em>mā</em> (négation), le <em>lām</em> au sens de <em>illā</em>. Et le pronom de Sa parole : <em>kādū</em> (“ ils ont failli ”) — on dit qu’il est pour Quraysh, on dit pour Thaqīf.</p>
<p>[Citation coranique (v. 73) et mots « inna », « li-yaftinūnak(a) », « kādū » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; l’analyse de l’inna allégée et le pronom de « kādū » vérifiées sur le texte d’Ibn ʿAṭiyya (« ﴿إن﴾ هذه عند سيبويه هي المخففة من الثقيلة... والضمير في قوله ﴿كادوا﴾ قيل هو لقريش وقيل لثقيف »).]</p>
<p>Sur le dire qu’il est pour Quraysh : dit Ibn Jubayr et Mujāhid : le verset descendit parce qu’ils dirent au Messager de Dieu — paix et bénédiction sur lui : “ nous ne te laisserons toucher la Pierre noire que si tu touches aussi nos idoles ” — en manière d’institution. Dit al-Ṭabarī et d’autres : le Messager de Dieu — paix et bénédiction sur lui — pensa leur montrer cela, son cœur le niant — et le verset descendit là-dessus.</p>
<p>Dit al-Zajjāj : le Messager de Dieu — paix et bénédiction sur lui — dit en son for : “ Qu’y a-t-il à ce que je leur fasse cela, quand Dieu, le Très-Haut, connaît ce qui est en mon for ? ” Et dit Ibn Isḥāq et d’autres : ils se réunirent à lui une nuit, le magnifièrent et lui dirent : “ tu es notre maître — mais acquiesce à une part de notre affaire, et nous acquiescerons à une part de la tienne ” : le verset descendit là-dessus. Il est au sens de Sa parole :</p>
<p>« Ils aimeraient bien que tu transiges avec eux afin qu’ils transigent avec toi. » (al-Qalam, 9)</p>
<p>[Citations d’al-Zajjāj et d’Ibn Isḥāq intactes. Citation coranique (al-Qalam, 9 — span imprimé « [القلم: 9] ») restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Sur le dire qu’il est pour Thaqīf : dit Ibn ʿAbbās et d’autres : parce qu’ils demandèrent au Messager de Dieu — paix et bénédiction sur lui — de les différer, après leur islam, d’une année où ils adoreraient al-Lāt — et dirent : “ nous voulons prendre ce qui nous en sera offert ; mais si tu crains que les Arabes ne le blâment chez toi, dis : Dieu l’a révélé à moi ”. Le verset descendit là-dessus. Et ce dire est faible : il oblige son tenant à faire le verset médinois — ce qui fut rapporté ; et les tenants des autres dis rapportèrent qu’il est mecquoise.</p>
<p>Dit Ibn ʿAṭiyya : tout ce qui fut voulu du Prophète — paix et bénédiction sur lui — selon cette divergence, Dieu lui révéla le contraire — soit par miracle, soit sans. Et son faire, s’il advenait, serait forfaiture sur Dieu : car ses actes et ses paroles ne sont, tous, que Loi.</p>
<p>Et Sa parole, glorifié soit-Il : <em>ʿan alladhī awḥaynā ilayk(a)</em> (“ de ce que Nous t’avions révélé ”) — arrêt sur ce dont Dieu le sauva : l’opposition aux dénégateurs et leur prise en amitié.</p>
<p>[Clause « ʿan alladhī awḥaynā ilayk(a) » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Et si Nous ne t’avions pas raffermi, tu aurais bien failli t’incliner quelque peu vers eux. » (al-Isrāʾ, 74)</p>
<p>— et <em>lawlā</em> (“ si… ne ”) est particule d’empêchement pour existence : elle induit l’empêchement de sa réponse par l’existence de sa condition — “ la réponse d’un <em>lawlā</em> affirmatif étant empêchée par l’existence de ce qui le précède : sur ce, l’approche de l’inclinaison n’advint pas de lui — paix et bénédiction sur lui —, à plus forte raison l’inclinaison ; et ce qui l’empêche est l’existence de l’affermissment de Dieu, le Très-Haut ”. [al-Baḥr al-Muḥīṭ fī l-tafsīr, d’Abū Ḥayyān : 7/90 — réf. imprimée « 7/90 », conforme]</p>
<p>Et <em>thabbatnāk(a)</em> (“ Nous t’avions raffermi ”) : du tathbīt — faire la chose ferme : emprunté à la permanence en son état, sans changement. Et <em>la-qadta</em> (“ tu aurais failli ”) : tu aurais approché.</p>
<p>Et <em>ilayhim</em> (“ vers eux ”) : du <em>rukūn</em> (l’inclinaison) — serrer le dos à la chose, ou s’y blottir, en manière de repos en elle : comme fait l’homme au pilier (<em>rukūn</em>) des murs — d’où Sa parole, rapportant [le propos de Loth] :</p>
<p>« …ou [si] je trouvais un appui solide ! » (Hūd, 80 — extrait)</p>
<p>[Citations coraniques (v. 74 ; Hūd, 80 — span imprimé « [هود: 80] ») et mots « lawlā », « thabbatnāk(a) », « la-qadta », « ilayhim » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; citation d’Abū Ḥayyān intacte ; le rukūn et le parallèle de Hūd 80 vérifiés sur le texte d’Ibn ʿAṭiyya (« و «الركون» شد الظهر... ومنه قوله تعالى حكاية ﴿أو آوي إلى ركن شديد﴾ »).]</p>
<p>En le verset il y a dénombrement des grâces de Dieu sur le Prophète — paix et bénédiction sur lui. Et il fut rapporté que le Messager de Dieu — paix et bénédiction sur lui —, quand ce verset descendit, dit : “ Ô Dieu, ne me remets point à moi-même le temps d’un clin d’œil. ”</p>
<p>Puis le Glorifié exposa à Son prophète — paix et bénédiction sur lui — la fin de l’inclinaison vers les associateurs. Le Puissant, le Majestueux, dit :</p>
<p>« Alors, Nous t’aurions certes fait goûter le double [supplice] de la vie et le double [supplice] de la mort ; et ensuite tu n’aurais pas trouvé de secoureur contre Nous. » (al-Isrāʾ, 75)</p>
<p>En Sa parole : <em>ḍiʿfa l-ḥayāti wa-ḍiʿfa l-mamāt</em> (“ le double de la vie et le double de la mort ”) il y a antithèse (<em>ṭibāq</em>). Dit Ibn ʿAbbās, Mujāhid, Qatāda et al-Ḍaḥḥāk : Il veut le double du châtiment de la vie et le double du châtiment de la mort.</p>
<p>Dit Ibn ʿAṭiyya : au sens que ce que ce pécheur mériterait de Notre châtiment, en ce monde et en l’au-delà, Nous te l’aurions doublé. Et ce doublement est répandu pour le Prophète — paix sur lui — en son salaire, en sa douleur, et en le châtiment de ses épouses.</p>
<p>[Citation coranique (v. 75) et clause « ḍiʿfa l-ḥayāti wa-ḍiʿfa l-mamāt » (le ṭibāq) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Deuxièmement : la tentative des associateurs de faire sortir le Prophète — paix et bénédiction sur lui — de La Mecque</h3>
<p>Quand Dieu, le Très-Haut, eut exposé Sa préservation du Prophète — paix et bénédiction sur lui —, et le désespoir des associateurs de pouvoir l’attirer — paix et bénédiction sur lui — à l’écart de l’appel en dehors de ce que Dieu révéla, Il y fit suivre l’exposé de leur tentative de le harceler et le déloger — paix et bénédiction sur lui — pour le faire sortir de La Mecque. Le Très-Haut dit :</p>
<p>« En vérité, ils ont failli t’inciter à fuir du pays pour t’en bannir. Mais dans ce cas, ils n’y seraient pas restés longtemps après toi. » (al-Isrāʾ, 76)</p>
<p>On dit : le pronom de <em>minhā</em> (“ d’elle ”) est pour les Juifs de Médine et ses environs, comme Ḥuyayy b. Akhṭab et d’autres : car ils allèrent au stratagème contre le Messager de Dieu — paix et bénédiction sur lui — et lui dirent : “ cette terre n’est pas une terre de prophètes — la terre des prophètes est en Syrie ; mais tu crains les Romains : si tu es prophète, sors vers elle, Dieu te protégera comme Il protégea l’autre que toi des prophètes ”. Le verset descendit là-dessus. Et Dieu, Puissant et Majestueux, informa que le Messager de Dieu — paix et bénédiction sur lui —, s’il était sorti, n’aurait laissé derrière eux [d’attente] que peu.</p>
<p>[Citation coranique (v. 76) et mot « minhā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et le plus juste est que le pronom de <em>minhā</em> soit pour Quraysh — car la sourate est mecquoise, et ce qui la précède est un rapport sur les gens de La Mecque, sans qu’il ait couru mention des Juifs. Et al-Zajjāj rapporta d’Ibn ʿAbbās et Qatāda que leur “ délogement ” est ce qu’ils avaient résolu en la maison al-Nadwa — le tuer — comme ils allèrent avant au siège du défilé (<em>al-shaʿb</em>), le resserrant jusqu’à il sortit et ils le suivirent à la grotte et autre : la menace s’exécuta sur eux en ce qu’ils ne demeurèrent derrière lui que peu — au jour de Badr. Et Sa parole : <em>min al-arḍ</em> (“ du pays ”) est, sur ce dire, général pour le monde — comme s’Il avait dit : “ te faire sortir du monde ” ; et sur les autres dis, c’est une terre particulière — La Mecque ou Médine — comme Dieu, le Très-Haut, a dit :</p>
<p>« …ou qu’ils soient bannis du pays » (al-Māʾida, 33 — extrait ; le manuel imprime « 35 »)</p>
<p>— dont le sens est : de la terre où se trouve leur agir.</p>
<p>[Mots « minhā », « min al-arḍ » et citation d’al-Māʾida 33 (span imprimé « [المائدة: 35] ») restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le parallèle vérifié sur le texte d’Ibn ʿAṭiyya (« كما قال تعالى ﴿أو ينفوا من الأرض﴾ » — Māʾida 33 ; le manuel imprime « 35 », erreur d’adjacence notée).]</p>
<p>Puis Dieu, glorifié et élevé soit-Il, exposa que telle est Sa règle (<em>sunna</em>) en les communautés antérieures. Le Très-Haut dit :</p>
<p>« Telle fut la règle appliquée par Nous à Nos messagers que Nous avons envoyés avant toi. Et tu ne trouveras pas de changement en Notre règle. » (al-Isrāʾ, 77)</p>
<p>Sa parole : <em>sunna</em> (“ règle ”) est à l’accusatif comme infinitif (<em>maṣdar</em>). Et dit al-Farrāʾ : son accusatif est sur l’élision de la préposition — car le sens : “ comme la règle de ” : le <em>kāf</em> fut omis et l’accusatif mis — ce qui lui oblige, sur cela, de ne point s’arrêter sur Sa parole : <em>qalīlā</em> (“ peu ”).</p>
<p>Et le sens du verset : l’information que la règle de Dieu, le Très-Haut, en les communautés révolues, et Son habitude, est que, quand elle fit sortir son prophète d’entre ses propres, le châtiment l’atteignit et l’extirpation l’anéantit : elle ne demeura derrière lui que peu.</p>
<p>[Citations coraniques (v. 77) et mots « sunna », « qalīlā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le naṣb de maṣdar et l’interdit de pause vérifiés sur le texte d’Ibn ʿAṭiyya (« ويلزمه على هذا أن لا يقف على قوله ﴿قليلاً﴾ » — la pause porte sur « qalīlā », fin du v. 76).]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d’un ensemble de finalités éducatives, dont :</p>
<ul>
<li>Le dénombrement des grâces de Dieu, le Très-Haut, sur Son messager — paix et bénédiction sur lui —, Sa douceur envers lui et Sa préservation de lui des tentations des associateurs et de leurs machinations : ils pensèrent que, par ces machinations et tromperies, ils détourneraient le Prophète — paix et bénédiction sur lui — de ce que Dieu, le Très-Haut, révéla, et lui enjoliveraient l’invention de ce qui ne descendit point sur lui — agréant ce qu’ils étaient sur l’adoration des idoles et des statues.</li>
<li>L’affirmation de l’importance, pour l’homme, de se rappeler la faveur de Dieu, le Très-Haut, sur lui, Sa guidance au chemin du vrai et du juste, la perception de Sa crainte, glorifié soit-Il, et la constance sur la doctrine droite.</li>
<li>La réalisation de la victoire de Dieu, le Très-Haut, pour Ses prophètes et messagers appelant au vrai : Dieu leur promit Sa victoire, et les préservera du mal des agresseurs qu’Il promit à l’anéantissement et au châtiment — telle est la règle de Dieu, le Très-Haut, en Sa création : tu ne lui trouveras ni modification ni changement.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Je conclus des versets l’effet de la grâce de Dieu, le Très-Haut, sur Son messager — paix et bénédiction sur lui — et sur sa communauté.</li>
<li>J’expose : le Prophète — paix et bénédiction sur lui — pensa-t-il (hamma) à l’inclinaison aux demandes des associateurs ? — m’appuyant sur le sens de « lawlā » (“ si… ne ”).</li>
</ul>
<ul>
<li>Quelle fut la fin, pour les associateurs, de faire sortir le Prophète — paix et bénédiction sur lui — de La Mecque ? Et quel est le rapport de cela avec les règles de Dieu, le Très-Haut, en les communautés antérieures ?</li>
</ul>
<p>[Mot « lawlā » (objet de la deuxième question — l’empêchement pour existence) restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>L’investissement (istithmār)</h3>
<p>Dit Ibn al-ʿArabī — Dieu lui fasse miséricorde —, en [son commentaire de] la parole du Très-Haut [al-Isrāʾ, 74] :</p>
<p>« Dieu, glorifié et élevé soit-Il, informa qu’Il l’affermi, et établit l’unicité et la connaissance en son cœur, et tendit sur lui le pavillon de l’infaillibilité, et l’hébergea en l’abri de la vénération. Et s’Il l’avait remis à lui-même, et ôté de lui l’ombre de Son infaillibilité un instant, il eût touché ce qu’ils visèrent — mais Nous décrétâmes sur toi la sauvegarde, et fîmes rayonner de la lumière de la guidance ton cœur, et il s’éclaircit ; et repousse loin de toi le faux, et terrasse-le. Ce verset est un texte en Son infaillibilité de tout ce qu’on Lui attribua : comment donc quelqu’un l’interpréterait-il ? » [Aḥkām al-Qurʾān, d’Ibn al-ʿArabī : 3/306 — réf. imprimée « 3/306 », conforme]</p>
<p>[Citation d’Ibn al-ʿArabī intégrale et conforme : aucun emplacement vide.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>Comment répondrai-je, à travers le texte, à ce qui vient en certains livres d’exégèse : que le Prophète — paix et bénédiction sur lui — pencha (<em>hamma</em>) vers l’inclinaison aux associateurs, et approcha de l’exécution de ce qu’ils demandaient ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 78 à 80 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>dulūka l-shams</em> (دُلُوكِ ٱلشَّمْسِ — le déclin du soleil).</p>
<p><em>ghasaqa l-layl</em> (غَسَقِ ٱللَّيْلِ — l’obscurcissement de la nuit).</p>
<p><em>qurʾāna l-fajr</em> (قُرْءَانَ ٱلْفَجْرِ — la lecture de l’aube).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 78-80) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Comment la persévérance en la prière agit-elle sur l’affinement des âmes et leur purification ?</li>
<li>Je recherche l’effet de la divergence sur le sens de « dulūk » en l’interprétation de la parole du Glorifié :</li>
</ul>
<p>« Et accomplis la prière au déclin du soleil » (al-Isrāʾ, 78 — extrait)</p>
<p>[Vocable « dulūk » et citation coranique (v. 78 — de la leçon suivante) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. Elle prépare la divergence sur le dulūk — le déclin du zénith vs le coucher (le hadith de Jibrīl et la parole d’Abū Bakr, “ voici quand décline le soleil ”) — le crux de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13660":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13660 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13660 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
