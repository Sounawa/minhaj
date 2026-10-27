#!/usr/bin/env python3
# savant(fiqh-1es/11437) — Les règles du qunūt et du tashahhud
# Leçon 12 — Risāla d'Ibn Abī Zayd al-Qayrawānī, comm. Kifāyat aṭ-ṭālib ar-rabbānī (Abū al-Ḥasan), ḥāshiya al-ʿAdawī
# Traduction savante : hadith al-Ḥākim/Abū Saʿīd vérifié (dorar.net n°13 : ṣaḥīḥ al-isnād ʿalā sharṭ Muslim,
# Mustadrak n°462, Livre de la purification ; parallèles Ṭabarānī Awsaṭ 2390, Tirmidhī 238, Ibn Mājah 276) ;
# verset al-Ḥajj 22:7 vérifié contre quran-cache (correspondance exacte warsh/Hafs).
import json, re, sys

BOOK = 'content/books/fiqh-1es.json'
DOC = '11437'

html_fr = """
<h1>Les règles du qunūt et du tashahhud (aḥkām al-qunūt wa-t-tashahhud) — leçon de fiqh de la Risāla d'Ibn Abī Zayd al-Qayrawānī avec le commentaire Kifāyat aṭ-ṭālib ar-rabbānī</h1>
<p>Leçon sur les règles du qunūt et du tashahhud, matière Fiqh, sur la base de la <em>Risāla</em> d'Ibn Abī Zayd al-Qayrawānī avec le commentaire d'Abū al-Ḥasan, <em>Kifāyat aṭ-ṭālib ar-rabbānī</em>, en marge de la <em>ḥāshiya</em> d'al-ʿAdawī — livre de l'élève (kitāb at-tilmīdh wa-t-talmīdha) de la première année de l'enseignement secondaire traditionnel (<em>ʿatīq</em>) — la douzième leçon.</p>
<p>Objectifs de la leçon :</p>
<ol>
<li>Connaître la règle du qunūt et sa formule.</li>
<li>Distinguer la manière de l'assise, du tashahhud et de la salutation finale, avec leurs règles.</li>
<li>Incarner la manière du qunūt et du tashahhud dans ma prière.</li>
</ol>
<p>L'invocation (<em>duʿāʾ</em>) est de ce que la prière recèle de plus important. C'est pourquoi l'invocation y a été placée en plusieurs lieux, pour ce qu'elle montre d'abaissement, de soumission et de prosternement du cœur devant la majesté de Dieu. Et parmi cela : ce qui est venu dans le qunūt et dans le tashahhud.<br>
Qu'est-ce que le qunūt, et quelle est sa formule ? Et qu'est-ce que le tashahhud, et quels sont ses termes ?</p>
<h2>Le texte (matn)</h2>
<p>Ibn Abī Zayd — que Dieu lui fasse miséricorde — a dit :</p>
<p>« Cependant, tu fais le qunūt après l'inclinaison ; et si tu veux, tu le fais avant l'inclinaison, après l'achèvement de la récitation. Le qunūt : “Ô Dieu, nous T'implorons à l'aide, nous Te demandons pardon, nous croyons en Toi, nous nous en remettons à Toi, nous nous courbons devant Toi, et nous désavouons et délaissons quiconque Te renie. Ô Dieu, c'est Toi que nous adorons ; c'est pour Toi que nous prions et que nous nous prosternons ; c'est vers Toi que nous allons et nous hâtons ; nous espérons Ta miséricorde et nous craignons Ton châtiment — le dur — : certes, Ton châtiment atteindra les infidèles.” »</p>
<p>« Puis tu agis dans la prosternation et l'assise selon la description qui précède. Quand tu t'assieds après les deux prosternations, tu dresses ton pied droit, les plantes de ses orteils vers le sol, tu replies le gauche, tu appliques ta fesse à terre — sans t'asseoir sur ton pied gauche ; et si tu veux, tu inclines le droit en le dressant, posant ainsi le flanc de ses orteils au sol : c'est là une latitude. Puis tu récites le tashahhud. Le tashahhud : “Les salutations sont à Dieu, les pures [hommages] à Dieu, les bonnes choses et les prières à Dieu. Que la paix soit sur toi, ô Prophète, ainsi que la miséricorde de Dieu et Ses bénédictions. Que la paix soit sur nous et sur les serviteurs vertueux de Dieu. J'atteste qu'il n'est de divinité que Dieu, Lui seul, sans associé, et j'atteste que Muḥammad est Son serviteur et Son messager.” Si tu salues après cela, il t'en est quitte. »</p>
<p>« Et de ce que tu ajoutes si tu veux : "J'atteste que ce qu'a apporté Muḥammad est vérité, que le Paradis est vérité, que le Feu est vérité, « et que l'Heure vient — nul doute à son sujet — et que Dieu ressuscitera ceux qui sont dans les tombeaux » (al-Ḥajj, 22 : 7). Ô Dieu, prie sur Muḥammad et sur la famille de Muḥammad, aie miséricorde de Muḥammad et de la famille de Muḥammad, et bénis Muḥammad et la famille de Muḥammad, comme Tu as prié, eu miséricorde et béni Ibrāhīm et la famille d'Ibrāhīm parmi les mondes — certes, Tu es digne de louange, Glorieux. Ô Dieu, prie sur Tes anges et les rapprochés, sur Tes prophètes et les envoyés, et sur l'ensemble des gens de Ton obéissance. Ô Dieu, pardonne-moi, ainsi qu'à mes parents et à nos imams, et à ceux qui nous ont précédés dans la foi — un pardon ferme. Ô Dieu, je Te demande tout bien que T'a demandé Ton prophète Muḥammad, et je cherche refuge auprès de Toi contre tout mal contre lequel Ton prophète Muḥammad a cherché refuge auprès de Toi. Ô Dieu, pardonne-nous ce que nous avons avancé et différé, ce que nous avons caché et manifesté, et ce dont Tu as plus de science que nous. Notre Seigneur, donne-nous en ce monde une bonne chose, dans l'autre une bonne chose, et préserve-nous du châtiment du Feu. Et je cherche refuge auprès de Toi contre la tentation de la vie et de la mort, contre la tentation de la tombe, contre la tentation du Messie imposteur, contre le châtiment du Feu et le mauvais devenir. Que la paix soit sur toi, ô Prophète, ainsi que la miséricorde de Dieu et Ses bénédictions ; que la paix soit sur nous et sur les serviteurs vertueux de Dieu." »</p>
<p>« Puis tu dis : “as-salāmu ʿalaykum” (que la paix soit sur vous) — une seule salutation, sur ta droite, en visant par elle ce qui fait face à ton visage, et tu portes légèrement la tête à droite. Ainsi font l'imām et l'homme qui prie seul. Quant au suivi (<em>maʾmūm</em>), il salue d'une [seule] salutation qu'il accompagne d'une légère inclination [de tête] à droite ; il en rend une autre à son imām qui lui fait face, la lui désignant d'un signe ; et il rend [la salutation] à quiconque l'a salué sur sa gauche — et si personne ne l'a salué, il ne rend rien sur sa gauche. [Le prieur] pose ses mains, dans son tashahhud, sur ses cuisses ; il replie les doigts de sa main droite et étend l'index : il pointe avec lui, le flanc dressé vers son visage. On a divergé sur le fait de le mouvoir. Il a été dit : il atteste, en pointant ainsi, que Dieu est une divinité unique ; et qui le meut l'interprète [ainsi] : c'est un fouet pour Satan (<em>maqmāʿa</em>) — et j'estime que l'interprétation en est qu'il évoque par là, de l'affaire de la prière, ce qui le préservera, s'il plaît à Dieu, de la distraction (<em>sahw</em>) en elle et de l'occupation qui en détourne. Il étend sa main gauche sur sa cuisse gauche, et ne la meut ni ne pointe avec elle. »</p>
<h2>La compréhension</h2>
<h3>Explication lexicale</h3>
<ul>
<li><em>al-qunūt</em> : l'invocation avec recueillement.</li>
<li><em>nakhnaʿu</em> : nous nous soumettons et nous nous humilions.</li>
<li><em>nakhlaʿu</em> : ôter les choses ; les délaisser.</li>
<li><em>naḥfidu</em> : nous nous hâtons dans l'œuvre.</li>
<li><em>ḥarfhā</em> : son flanc.</li>
<li><em>maqmāʿa</em> : ce qui refoule et met en fuite.</li>
</ul>
<h3>Extraction des contenus du matn</h3>
<ul>
<li>Détermine, à partir du matn, la règle du qunūt et sa formule.</li>
<li>Extrais du matn la règle du tashahhud et sa formule.</li>
<li>Expose, au fil du matn, la règle de la prière sur le Prophète dans le tashahhud.</li>
</ul>
<h2>L'analyse</h2>
<p>Cette leçon embrasse le reste de la description de la prière, en voici le détail :</p>
<h3>Premièrement : la règle du qunūt et sa formule</h3>
<h4>a. La règle du qunūt</h4>
<p>Le prieur fait le qunūt — par voie recommandée (<em>mandūb</em>) — dans la prière de l'aube (<em>ṣubḥ</em>), en la deuxième rakʿa, après l'achèvement de la sourate et avant l'inclinaison, selon l'avis prévalent (<em>mashhūr</em>). Dans la <em>ḥāshiya</em> d'ad-Dasūqī : ce que l'auteur expose — que le qunūt est recommandé — est l'avis prévalent. Saḥnūn a dit : c'est une sunna. Yaḥyā ibn ʿUmar a dit : il n'est pas institué. Ibn Ziyād a dit : qui le délaisse, sa prière est viciée — et cela indique l'obligation selon lui. (<em>Ḥāshiya</em> d'ad-Dasūqī, t. I, p. 248.) Il a été dit aussi : c'est un mérite (<em>faḍīla</em>) — on ne se prosterne pas [de distraction] pour l'avoir délaissé, et qui s'y prosterne, sa prière est nulle. La discrétion en est préférable, car c'est une invocation. Qui l'oublie avant l'inclinaison le fait après celle-ci ; et qui n'a rejoint [la prière commune] qu'après une rakʿa le fait dans la rakʿa de rattrapage, selon l'avis prévalent. Il n'est recommandé en rien d'autre que l'aube — ni dans le <em>witr</em> ni dans quelque autre [prière].</p>
<h4>b. La formule du qunūt</h4>
<p>Sa formule : « Ô Dieu, nous T'implorons à l'aide, nous Te demandons pardon, nous croyons en Toi, nous nous en remettons à Toi, nous nous courbons devant Toi, et nous désavouons et délaissons quiconque Te renie. Ô Dieu, c'est Toi que nous adorons ; c'est pour Toi que nous prions et que nous nous prosternons ; c'est vers Toi que nous allons et nous hâtons ; nous espérons Ta miséricorde et nous craignons Ton châtiment — le dur — : certes, Ton châtiment atteindra les infidèles. » En cela, parole de l'auteur : « Cependant, tu fais le qunūt après l'inclinaison, et si tu veux, tu le fais avant l'inclinaison… jusqu'à Sa parole : certes, Ton châtiment atteindra les infidèles. » Puis, lorsqu'il a achevé la récitation du qunūt, il se prosterne.</p>
<h3>Deuxièmement : l'assise et le tashahhud</h3>
<h4>a. La manière de l'assise</h4>
<p>Le prieur se prosterne — obligatoirement — selon la manière exposée ci-dessus, après avoir achevé la récitation du qunūt ; puis il s'assoit — par voie de Sunna — pour le tashahhud et le reste, en <em>tawarruk</em> dans son assise. Le tawarruk : qu'il s'asseye en dressant le pied droit, les plantes de ses orteils au sol — il est permis d'appliquer à terre le flanc de ses orteils —, qu'il replie le pied gauche sans s'asseoir dessus, et qu'il applique sa hanche au sol.</p>
<h4>b. La formule du tashahhud</h4>
<p>Le prieur récite — par voie de Sunna — le tashahhud dans son assise après les deux prosternations, et sa formule : « Les salutations sont à Dieu… jusqu'à : et j'atteste que Muḥammad est Son serviteur et Son messager » — puis il salue. Ou il ajoute, s'il veut : « et j'atteste que ce qu'a apporté Muḥammad est vérité… jusqu'à : que la paix soit sur nous et sur les serviteurs vertueux de Dieu. » Et tel est le terme de l'œuvre dans la prière paire (<em>thunāʾiyya</em>). Quant à la prière quadruple (<em>rubāʿiyya</em>), il y récite le tashahhud jusqu'à : « et j'atteste que Muḥammad est Son serviteur et Son messager » ; puis il se lève, et ne dit le takbīr qu'en se levant — car qui se dresse pour la troisième [rakʿa] est comme celui qui ouvre une prière nouvelle.</p>
<h4>c. La manière du tashahhud</h4>
<p>La manière d'agir dans le tashahhud : que le prieur pose ses mains, dans son tashahhud, sur ses genoux, qu'il replie les doigts de sa main droite, étende l'index et pointe avec lui, posant son flanc en face de son visage. L'avis prévalent est de le mouvoir dans son tashahhud, à droite et à gauche ; il pose la main gauche sur la cuisse gauche et l'étend par recommandation. En cela, parole de l'auteur : « Puis tu agis dans la prosternation et l'assise… jusqu'à Sa parole : que la paix soit sur nous et sur les serviteurs vertueux de Dieu. »</p>
<h3>Troisièmement : la règle de la salutation finale et sa formule</h3>
<h4>a. Sa formule</h4>
<p>Le prieur sort de la prière par la salutation (<em>taslīm</em>), en la formule déterminée : « as-salāmu ʿalaykum » — c'est une obligation sans divergence, en vertu du hadith d'Abū Saʿīd : le Messager de Dieu — paix et bénédiction sur lui — a dit : « La clé de la prière est la purification (<em>wuḍūʾ</em>) ; sa mise en sacralisation, le takbīr ; et sa dissolution, le taslīm. » [al-Mustadrak de l'Ḥākim, Livre de la purification.] Nulle autre formule n'en tient lieu, et il n'est pas valable [de dire] : « salām ʿalaykum », ou : « ʿalaykum as-salām », ou quelque autre des formules et locutions.</p>
<h4>b. Sa règle</h4>
<p>Le prieur salue d'une seule salutation sur sa droite, en visant par elle ce qui fait face à son visage — c'est une obligation —, et il porte la tête à droite, légèrement, par recommandation, qu'il soit imām ou [qu'il prie] isolément (<em>fādhdh</em>). Quant au suivi (<em>maʾmūm</em>), il salue — obligatoirement — d'une salutation sur sa droite ; il en rend une autre — par recommandation — à son imām, et il en salue une autre — par recommandation — sur sa gauche, s'il y a auprès de lui quelque prieur. En cela, parole de l'auteur : « Puis tu dis : as-salāmu ʿalaykum… jusqu'à Sa parole : et il ne la meut ni ne pointe avec elle. »</p>
<p>De ce que l'on tire du terme « salām » : cette religion est une religion de paix, que le croyant déverse sur son entourage, maintes fois dans le jour ; et la paix est un principe fondateur de l'islam : l'islam dérive de <em>salām</em> ; la rencontre entre les hommes se fait par la salutation ; la dissolution de la prière se fait par la salutation ; et les occasions du salām dans les rapports entre les hommes sont nombreuses et variées.</p>
<h2>L'évaluation</h2>
<ul>
<li>Quand le suivi (<em>maʾmūm</em>) doit-il saluer sur sa gauche ?</li>
<li>Mets en relief la sagesse qu'il y a à mouvoir l'index dans le tashahhud.</li>
<li>Expose la règle du qunūt dans l'aube, le <em>witr</em> et les <em>tarāwīḥ</em>.</li>
</ul>
<h2>L'enrichissement</h2>
<p>Le versificateur (<em>an-nāẓim</em>) dit :</p>
<table dir="ltr">
<tbody>
<tr><td>Quatre [pratiques] comptent au fiqh de l'imām :</td><td></td><td>hâter l'iḥrām, et hâter le salām.</td></tr>
<tr><td>Son entrée au miḥrāb sitôt l'iqāma prononcée,</td><td></td><td>et l'abrègement du premier tashahhud est le but visé.</td></tr>
</tbody>
</table>
<p>(<em>Ḥāshiya</em> de Muḥammad aṭ-Ṭālib ibn al-Ḥājj sur le commentaire de Mayyāra du <em>Murshid al-muʿīn</em>, t. I, p. 184.)</p>
<p>Lis les deux vers en explicitant les règles qu'ils renferment.</p>
<h2>La préparation préalable</h2>
<p>Lis le matn de la prochaine leçon et réponds à ce qui suit :</p>
<ul>
<li>Distingue les prières où il est recommandé d'allonger la sourate de celles où la concision est demandée.</li>
<li>Quelles sont les sourates dont la récitation est demandée dans le <em>shafʿ</em> et le <em>witr</em> ?</li>
</ul>
"""

# Typographie française : espaces fines insécables (U+202F) dans les guillemets
# et avant : ; ? ! — convention du corpus (leçons récentes).
html_fr = html_fr.replace('« ', '«\u202f').replace(' »', '\u202f»')
html_fr = re.sub(r' ([;?!])', '\u202f\\1', html_fr)
# l'espace avant « : » français — seulement hors balises d'attributs (aucune ici)
html_fr = html_fr.replace(' :', '\u202f:')

# Nettoyage des espaces parasites en tête de fichier
html_fr = html_fr.strip()

book = json.load(open(BOOK))
found = False
for d in book['lessons']:
    if d['docId'] == DOC:
        d['htmlFr'] = html_fr
        d['titleFr'] = 'Les règles du qunūt et du tashahhud'
        found = True
        print(f"OK: {DOC} -> htmlFr ({len(html_fr)} car), titleFr mis à jour")
if not found:
    sys.exit(f"ERREUR: {DOC} introuvable dans {BOOK}")
json.dump(book, open(BOOK, 'w'), ensure_ascii=False, indent=2)
print(f"{BOOK} réécrit.")

# Contrôle qualité immédiat : aucun caractère arabe ne doit rester dans la traduction
arabic = re.findall(r'[\u0600-\u06FF]+', html_fr)
print('Caractères arabes résiduels:', len(arabic), arabic[:5] if arabic else '')
