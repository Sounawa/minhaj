#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13659 (tafsir-tanawi-2, Sourate al-Isrāʾ
70-72, leçon 18 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:70-72) : <p> vide → 3 versets restaurés du
  quran-cache.
- Lexique : 4 vedettes perdues (karramnā/bi-imāmihim/fatīlan/aḍalla
  sabīlā) — restituées du tafsīr et du texte d'Ibn ʿAṭiyya.
- Citations inline perdues :
  * v70 + « كرمنا » (le redoublement de karam — l'honneur de négation du
    défaut, non l'honneur du bien : « ثوب كريم » — VÉRIFIÉ) + « وحملناهم
    في البر والبحر » (les bêtes, les trains et les voitures —
    modernisation du manuel) + « ورزقناهم من الطيبات » (le rizq : tout ce
    dont l'usage est sain — VÉRIFIÉ) + « وفضلناهم على كثير ممن خلقنا
    تفضيلا » + la citation de Qurṭubī [10/295] ;
  * les critères du tafḍīl : manger des deux mains (al-Ṭabarī) / la vue
    dressée, la marche debout / et le refus d'Ibn ʿAṭiyya (le cheval
    court, l'éléphant fort, le lion brave, le coq généreux — le vrai
    critère : l'intellect) — intacts ;
  * l'objection des anges : le parallèle « ولا الملائكة المقربون » =
    **Nisāʾ 172 VÉRIFIÉ** (le manuel imprime « 171 » — erreur d'adjacence
    notée) + la réponse (non contraignant ; l'égalité possible ; la
    supériorité des anges établie ailleurs) ;
  * v71 + l'iʿrāb de « يوم » (ẓarf par verbe omis « اذكر » — le manuel ;
    l'original porte « أنكر », Abū Ḥayyān note « sur l'estimation اذكر, il
    serait objet » ; ou opérateur « ولا يظلمون » puis « يظلمون » dernier ;
    ou **« وفضلناهم » VÉRIFIÉ** — le manuel ; ou mabnī sur le fatḥ,
    mawḍiʿ au nominatif, le khabar dans la répartition « فمن أوتي » →
    « ومن كان » — VÉRIFIÉ ; Abū Ḥayyān discute la terminologie — noté) ;
  * « كل أناس » (nom de collectif sans singulier de son lexème —
    VÉRIFIÉ) + « بإمامهم » (le bāʾ : par le nom de leur imām — « يا أمة
    محمد » — ou avec leur imām — VÉRIFIÉ) + l'imām disputé (Mujāhid/
    Qatāda : leur prophète ; Ibn Zayd : leur livre révélé ; Ibn ʿAbbās/
    al-Ḥasan : leur livre d'œuvres ; une frange : leur suivi — VÉRIFIÉ) ;
  * « فمن أوتي كتابه بيمينه » (la réalité des feuillets — VÉRIFIÉ) +
    « يقرؤون كتابهم » (l'expression de la joie — VÉRIFIÉ) + « فتيلا »
    (le fil de la fente du noyau — l'emprunt par ressemblance ; le dit
    du silence comme le dit du mentionné — VÉRIFIÉ) + les deux parallèles
    « فلا تقل لهما أف » (Isrāʾ 23) et « إن الله لا يظلم مثقال ذرة »
    (Nisāʾ 40) — **VÉRIFIÉS** ;
  * v72 + « ومن كان في هذه أعمى » + Muḥammad b. Abī Mūsā (hādhihī = les
    grâces de « ولقد كرمنا بني آدم » — VÉRIFIÉ) + Ibn ʿAbbās/Mujāhid/
    Qatāda/Ibn Zayd (hādhihī = ce monde) + la préférence du cadi (la
    demeure présente) + les lectures de « أعمى » (imāla : Ibn Kathīr/
    Ibn ʿĀmir/Qālūn/Ḥafṣ sans — Ḥamza/Kisāʾī/ʿĀṣim avec — Abū ʿAmr la
    première avec, la seconde au fatḥ : « plus aveugle » — VÉRIFIÉ) +
    Abū ʿAlī (l'imāla aux finales) + « وأضل سبيلا » (le ʿaṭf de l'afʿal
    sur son pareil) + Sībawayh (la cécité de l'œil congénitale — sans
    intensif ; celle du cœur : de degrés) ;
  * iʿdād : 4 expressions du lexique de 13660 (v73-77 : kādū/
    yastafizzūnaka/liftarīya/laqadta) + le pronom → « منها » en « وإن
    كادوا ليستفزونك من الأرض ليخرجوك منها » (v76 — la divergence Juifs
    de Médine/Quraysh, confirmée par la discussion de la leçon suivante)
    — noté.
- Citation d'al-Rāzī [Mafātīḥ al-ghayb 21/372] INTACTE (l'âme humaine,
  les cinq puissances, la puissance raisonnable)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 70 à 72</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 70 à 72, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 18).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Découvrir les figures de l’honneur que Dieu, le Très-Haut, accorde à l’homme.</li>
<li>Conclure les causes de la différence des gens au Jour de la résurrection.</li>
<li>Se rappeler sans cesse les grâces de Dieu, le Très-Haut, pour persévérer en Son obéissance.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Quand Dieu, le Très-Haut, eut exposé aux versets précédents les grâces dont Il gratifia Ses serviteurs, Il magnifia en ces versets Son honneur des fils d’Adam et leur préférence sur le reste des créatures ; puis mentionna, glorifié soit-Il, ce qu’il y aura en l’au-delà de grande différence entre les gens : ils se diviseront en heureux qui prendront leurs livres en leurs mains droites, et malheureux qui les prendront en leurs mains gauches — alors Dieu fera à tous le compte, et rendra à chacun selon son œuvre.</p>
<p>Quelles sont les figures de la préférence et de l’honneur que Dieu, le Très-Haut, accorde à l’homme ? Et sur quelle base les gens diffèrent-ils au Jour de la résurrection ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Certes, Nous avons honoré les fils d’Adam. (70) Nous les avons transportés sur terre et sur mer, leur avons attribué de bonnes choses comme nourriture, et Nous les avons nettement préférés à plusieurs de Nos créatures. (71) Le jour où Nous appellerons chaque groupement d’hommes par leur chef, ceux à qui on remettra leur livre dans la main droite liront leur livre [avec plaisir] et ne subiront pas la moindre injustice. (72) Et quiconque aura été aveugle ici-bas, sera aveugle dans l’au-delà, et sera plus égaré [encore] par rapport à la bonne voie. » (al-Isrāʾ, 70-72)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>karramnā</em> (Nous avons honoré) : Nous fîmes aux fils d’Adam honneur, rang et excellence sur l’ensemble des créatures.</li>
<li><em>bi-imāmihim</em> (par leur guide) : par celui qu’ils prenaient pour modèle et suivaient, en le bien ou en le mal.</li>
<li><em>fatīlā</em> (d’un futfīl) : du poids d’un fil — fine pellicule semblable au fil, dans la fente du noyau.</li>
<li><em>aḍalla sabīlā</em> (plus égaré en voie) : et plus éperdu, et plus proche du châtiment.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Qui Dieu, le Très-Haut, honora-t-Il en ces versets ? Et par quoi ?</li>
<li>Les gens seront-ils, en l’au-delà, à un seul degré ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’honneur que Dieu, le Très-Haut, accorde à l’homme</h3>
<p>Quand Dieu, le Très-Haut, eut mentionné de la mise en garde de l’homme ce qu’Il mentionna aux versets précédents, Il exposa Sa grâce sur eux et leur honneur sur les autres. Le Glorifié dit :</p>
<p>« Certes, Nous avons honoré les fils d’Adam. Nous les avons transportés sur terre et sur mer, leur avons attribué de bonnes choses comme nourriture, et Nous les avons nettement préférés à plusieurs de Nos créatures. » (al-Isrāʾ, 70)</p>
<p><em>Karramnā</em> (« Nous avons honoré ») est redoublement de <em>karam</em> — le sens : Nous fîmes pour eux honneur, rang et excellence sur l’ensemble des créatures. Et c’est là l’honneur de négation du défaut, non l’honneur du bien : il en est comme tu dis : “ un tissu généreux ” (<em>thawb karīm</em>) — c’est-à-dire : ses beautés sont abondantes.</p>
<p>[Citation coranique (v. 70) et mot « karramnā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le redoublement de karam vérifié sur le texte d’Ibn ʿAṭiyya (« ﴿كرمنا﴾ تضعيف كرم... وهذا هو كرم نفي النقصان، لا كرم المال »).]</p>
<p>Et Sa parole : « Nous les avons transportés sur terre et sur mer » — c’est-à-dire : et Nous les avons portés, par Notre puissance et Notre soin, sur les bêtes et le reste des moyens de transport — trains, voitures et autres —, et les avons portés en mer sur les navires qui les transportent d’un lieu à un autre : exposé d’une espèce des espèces de l’honneur.</p>
<p>[Clause « wa-ḥamalnāhum fī l-barri wa-l-baḥr » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Puis le Glorifié exposa la seconde espèce de l’honneur de l’homme. Le Puissant, le Majestueux, dit :</p>
<p>« …leur avons attribué de bonnes choses comme nourriture » (al-Isrāʾ, 70 — extrait)</p>
<p>— le <em>rizq</em> (subsistance) : tout ce dont l’usage est sain.</p>
<p>[Clause « wa-razaqnāhum min aṭ-ṭayyibāt » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Quant à la troisième espèce de ce dont Dieu, le Très-Haut, honora l’homme, le Glorifié l’exposa par Sa parole :</p>
<p>« …et Nous les avons nettement préférés à plusieurs de Nos créatures. » (al-Isrāʾ, 70 — fin)</p>
<p>— c’est-à-dire : sur les bêtes, les montures, les fauves et les oiseaux — par la maîtrise et la prise, la rétribution et le compte, la sauvegarde et le discernement, la justesse du coup d’œil. [al-Jāmiʿ li-aḥkām al-Qurʾān, d’al-Qurṭubī : 10/295 — réf. imprimée « 10/295 », conforme]</p>
<p>[Clause « wa-faḍḍalnāhum ʿalā kathīrin mimman khalaqnā tafḍīlā » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; citation d’al-Qurṭubī intacte.]</p>
<p>Dit Ibn ʿAṭiyya — Dieu lui fasse miséricorde : « En ce verset, Dieu, le Très-Haut, dénombre sur les fils d’Adam ce dont Il les particularisa au sein du reste des animaux — l’animal et le djinn étant le grand nombre préféré <em>de</em>, et les anges ceux qui sortent de cela. Et leur port en la terre ferme et la mer — de ce qui ne sied à nul animal sinon aux fils d’Adam, qui porte par son vouloir, son dessein et son gouvernement, en la terre ferme comme en la mer. Et la subsistance des bonnes choses n’y s’étend pour nul animal comme elle s’étend pour les fils d’Adam : car eux gagnent l’argent, à la différence de l’animal, et portent les vêtements, et mangent les mets composés — l’extrême de tout animal étant de manger de la chair crue, ou un mets non composé. »</p>
<p>Et al-Ṭabarī rapporta d’un groupe qu’il dit : “ la préférence ” (<em>al-tafḍīl</em>), c’est qu’il mange des deux mains, le reste des animaux de la gueule. Et dit un autre : et qu’il regarde du haut, dressé, plus que tout animal, et marche debout — et pareille préférence.</p>
<p>Et tout cela n’est pas général : car l’animal a, de cette espèce, ce qui le fait préférer au fils d’Adam — la course du cheval, son ouïe et sa vue, la force de l’éléphant, le courage du lion, la générosité du coq. L’honneur et la préférence ne sont que par l’intellect, dont l’homme domine tout l’animal, par lequel il connaît Dieu, Puissant et Majestueux, comprend Sa parole, et parvient à Sa félicité.</p>
<p>Un groupe dit : ce verset tranche de la préférence des anges sur les hommes, puisqu’ils sont les exceptés. Et Dieu, le Très-Haut, a dit :</p>
<p>« [Le Messie ne trouvera jamais indigne d’être le serviteur d’Allah,] ni les Anges rapprochés. » (an-Nisāʾ, 172 — extrait ; le manuel imprime « 171 »)</p>
<p>— ce qui n’est point contraignant du verset : la préférence entre les hommes et les djinns n’y est pas visée — il se peut que les anges soient meilleurs, il se peut l’égalité ; c’est d’ailleurs d’autres lieux de la Loi que la préférence des anges est établie.</p>
<p>[Citation coranique (an-Nisāʾ, 172 — span imprimé « [النساء: 171] ») restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; identification vérifiée sur le texte d’Ibn ʿAṭiyya (« وقد قال تعالى ﴿ولا الملائكة المقربون﴾ » — Nisāʾ 172 ; le manuel imprime « 171 », erreur d’adjacence notée).]</p>
<h3>Deuxièmement : la différence des états des gens en l’au-delà</h3>
<p>Après que Dieu, glorifié soit-Il, eut exposé les espèces de l’honneur de Dieu, le Très-Haut, envers l’homme, et Ses grâces sur lui en ce monde — et qu’Il le préféra à beaucoup de Sa création —, Il exposa en ces versets ce qu’il y aura en l’au-delà de grande différence entre les gens de la félicité et les gens de l’égarement. Le Très-Haut dit :</p>
<p>« Le jour où Nous appellerons chaque groupement d’hommes par leur chef, ceux à qui on remettra leur livre dans la main droite liront leur livre [avec plaisir] et ne subiront pas la moindre injustice. » (al-Isrāʾ, 71)</p>
<p>Il se peut que Sa parole : <em>yawma</em> (« le jour ») soit à l’accusatif comme adverbe (<em>ẓarf</em>), l’opérateur en étant un verbe omis — l’estimation : “ rappelle ” —, ou un verbe qu’indique Sa parole : <em>wa-lā yuẓlamūna</em> (« ne subiront pas l’injustice ») — l’estimation : “ et ils ne seront point lésés le jour où Nous appellerons ” —, puis <em>yuẓlamūna</em> l’explique en dernier. Il est valable aussi que l’opérateur en soit <em>wa-faḍḍalnāhum</em> (« Nous les avons préférés ») — car la préférence des humains, au Jour de la résurrection, sur le reste des animaux est claire : ce sont eux les gratifiés, les interpellés, les comptés, qui ont le rang. Il se peut aussi que <em>yawma</em> soit à l’accusatif par construction (<em>bināʾ</em>) pour avoir été annexé à un non-pleinement-déclinable, sa position étant au nominatif de <em>mubtadaʾ</em>, le prédicat en la répartition venue après, en Sa parole : <em>fa-man ūtiya kitābahū bi-yamīnih</em> (« ceux à qui on remettra leur livre dans la main droite »), jusqu’à Sa parole : <em>wa-man kāna fī hādhihī aʿmā</em> (« et quiconque aura été aveugle ici-bas »).</p>
<p>[Citation coranique (v. 71) et mots « yawma », « wa-lā yuẓlamūna », « wa-faḍḍalnāhum », « fa-man ūtiya kitābahū bi-yamīnih », « wa-man kāna fī hādhihī aʿmā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la reconstruction de l’iʿrāb vérifiée sur le texte d’Ibn ʿAṭiyya (« أو فعل يدل عليه قوله ﴿ولا يظلمون﴾... ويصح أن يعمل فيه ﴿وفضلناهم﴾... والخبر في التقسيم الذي أتى بعد في قوله ﴿فمن أوتي﴾ إلى قوله ﴿ومن كان﴾ ») ; le texte en ligne porte « تقديره أنكر » où le manuel imprime « اذكر » — Abū Ḥayyān note : sur l’estimation « اذكر », il serait objet, non adverbe ; et discute la terminologie du bināʾ — noté.]</p>
<p>Et <em>kulla unāsin</em> (« chaque groupement d’hommes ») est un nom de collectif, qui n’a point de singulier de son lexème. Et Sa parole : <em>bi-imāmihim</em> (« par leur chef ») — il se peut que le <em>bāʾ</em> de <em>bi-imāmihim</em> se rattache à <em>nadʿū</em> (« Nous appellerons ») : c’est-à-dire, Nous appelons par le nom de leur imām ; il se peut qu’Il veuille : avec leur imām. Sur la première interprétation, l’on dit : “ communauté de Muḥammad ! ”, “ partisans de Pharaon ! ” et pareil. Sur la seconde, toute communauté vient avec son imām — conducteur ou égarant.</p>
<p>Et les exégètes divergèrent sur le visé par “ l’imām ” : dit Mujāhid et Qatāda : leur prophète. Et dit Ibn Zayd : leur livre qui descendit sur eux. Et dit Ibn ʿAbbās et al-Ḥasan : leur livre où sont leurs œuvres. Et un groupe dit : leur suivi, conducteur ou égarant. Et le vocable “ imām ” englobe tout cela : car l’imām est ce qu’on prend pour guide et par quoi on se dirige vers le visé.</p>
<p>[Mots « kulla unāsin », « bi-imāmihim » (×2), « nadʿū » et « al-imām » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les deux sens du bāʾ et les quatre avis sur l’imām vérifiés sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et Sa parole, le Très-Haut : <em>fa-man ūtiya kitābahū bi-yamīnih</em> (« ceux à qui on remettra leur livre dans la main droite ») — la chose est de vérité : au Jour de la résurrection, des feuillets voletent, mis aux mains droites des gens de la foi, aux mains gauches des gens du déni, et aux mains droites des pécheurs sur qui la menace s’exécutera — ils en apprendront qu’ils ne sont pas éternels en Enfer. Et Sa parole : <em>yaqraʾūna kitābahum</em> (« liront leur livre ») est expression de la joie d’elle : c’est-à-dire, ils la redisent et la contemplent. Et Sa parole : <em>fatīlā</em> (« d’un futfīl ») — le <em>fatīl</em> est le fil qui est en la fente du noyau de la datte : on le prend en exemple pour la petitesse et l’insignifiance de la valeur. Il y a en cela emprunt par ressemblance (<em>istiʿāra tamthīliyya</em>) — c’est-à-dire : on ne retranche rien des récompenses de leurs salaires, fût-ce du poids d’un fil de la fente du noyau — ni moins, ni plus. Tel est le compris du dire : le jugement du tu est comme celui du dit. C’est comme la parole du Très-Haut :</p>
<p>« …ne leur dis point : “ Ouf ! ” » (al-Isrāʾ, 23 — extrait)</p>
<p>et comme Sa parole :</p>
<p>« Certes, Allah ne lèse [personne] du poids d’un atome » (an-Nisāʾ, 40 — extrait)</p>
<p>[Clauses « fa-man ūtiya kitābahū bi-yamīnih », « yaqraʾūna kitābahum », « fatīlā » et citations d’al-Isrāʾ 23 et an-Nisāʾ 40 (spans imprimés « [الإسراء: 23] » et « [النساء: 40] ») restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les deux parallèles vérifiés sur le texte d’Ibn ʿAṭiyya (« كقوله تعالى ﴿فلا تقل لهما أف﴾ وكقوله ﴿إن الله لا يظلم مثقال ذرة﴾ »).]</p>
<p>Et le sens du verset : rappelle, Messager, le Jour de la résurrection, quand Dieu, Puissant et Majestueux, appellera tout groupe des gens avec leur imām, celui qu’ils prenaient pour modèle en ce monde — quand les feuillets des œuvres volettent, mis aux mains droites des gens de la foi, aux mains gauches des gens du déni, et aux mains droites des pécheurs sur qui la menace s’exécutera — ils en apprendront qu’ils ne sont pas éternels en Enfer.</p>
<p>Quant à celui à qui son livre sera donné en sa main gauche, Dieu, le Très-Haut, l’exprima par Sa parole :</p>
<p>« Et quiconque aura été aveugle ici-bas, sera aveugle dans l’au-delà, et sera plus égaré [encore] par rapport à la bonne voie. » (al-Isrāʾ, 72)</p>
<p>Dit Muḥammad b. Abī Mūsā : l’indiqué par “ celle-ci ” (<em>hādhihī</em>) est les grâces qu’Il mentionna en Sa parole :</p>
<p>« Certes, Nous avons honoré les fils d’Adam » (al-Isrāʾ, 70 — extrait requoté)</p>
<p>— c’est-à-dire : qui fut aveugle à la gratitude de ces grâces et à la foi en Celui qui les accorde, il est, des affaires de l’au-delà et de leur ordre, aveugle.</p>
<p>[Citations coraniques (v. 72 ; v. 70 requoté) et mot « wa-laqad karramnā banī Ādama » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la glose de Muḥammad b. Abī Mūsā vérifiée sur le texte d’Ibn ʿAṭiyya (« الإشارة بهذه إلى النعم التي ذكرها في قوله ﴿ولقد كرمنا بني آدم﴾ »).]</p>
<p>Dit Ibn ʿAṭiyya : il se peut que le second “ aveugle ” soit au rang du premier — comme comparaison (<em>tashbīh</em>) à l’aveugle de la vue ; et il se peut qu’il soit attribut de préférence — c’est-à-dire : plus intensément aveugle. Et la cécité en ce verset est cécité du cœur, au premier comme au second.</p>
<p>Et dit Ibn ʿAbbās, Mujāhid, Qatāda et Ibn Zayd : l’indiqué par “ celle-ci ” est ce monde (<em>al-dunyā</em>) — c’est-à-dire : qui fut, en cette demeure, aveugle à la considération des signes de Dieu et de Ses leçons et à la foi en Ses prophètes, il est, en l’au-delà, aveugle — soit sur l’élision d’un complément : “ en l’ordre de l’au-delà ” ; soit : il est, au Jour de la résurrection, aveugle, au sens : éperdu — le juste ne s’ouvre pas à lui, la réussite ne luît pas pour lui. Dit Mujāhid : “ aveugle en l’au-delà ” — contre sa preuve.</p>
<p>Dit le cadi Abū Muḥammad : et l’apparent, pour moi, est que l’indiqué par “ celle-ci ” est ce monde — c’est-à-dire : qui fut, en sa demeure présente, au temps de sa perception et de son intelligence, aveugle à la considération des signes de Dieu, il est, au Jour de la résurrection, plus éperdu et plus aveugle : car il a touché la déception et vu les prodromes du châtiment. Et sur cette interprétation, [la phrase] se met en équilibre avec la précédente — le rappel de celui à qui son livre est donné en sa main droite ; et si nous faisons Sa parole : “ en l’au-delà ” au sens de “ en l’ordre de l’au-delà ”, l’équilibre des deux versets ne court pas [de bout en bout].</p>
<p>Et Ibn Kathīr, Ibn ʿĀmir, Qālūn d’après Nāfiʿ et Ḥafṣ d’après ʿĀṣim lurent : <em>aʿmā</em>, aux deux places, sans inclinaison (<em>imāla</em>) ; et Ḥamza, al-Kisāʾī et ʿĀṣim — divergemment rapporté de lui — aux deux places, avec inclinaison ; et Abū ʿAmr : inclinaison du premier, <em>fatḥa</em> du second — l'interprétant : plus intensément aveugle ; c'est pourquoi il ne l'inclina pas. Dit Abū ʿAlī : car l'inclinaison n'est belle qu'aux finales — et <em>aʿmā</em> n'est tel pas : son estimation est “ plus aveugle que ” (<em>aʿmā min</em>), il ne s'achève qu'en notre dire “ que ” : il n'est donc pas final. Et affermit cette interprétation Sa parole, en coordination sur lui :</p>
<p>« …et sera plus égaré [encore] par rapport à la bonne voie » (al-Isrāʾ, 72 — fin)</p>
<p>— on ne coordonne <em>aḍall(u)</em>, qui est de l'<em>afʿal</em> “ que ”, que sur ce qui lui ressemble. Et s'Il le fit, en l'au-delà, “ plus égaré en voie ” : c'est que le dénégateur, en ce monde, peut croire et être sauvé — en l'au-delà, il ne le peut : il est plus égaré en voie, plus éperdu, plus proche du châtiment.</p>
<p>Et la parole de Sībawayh — Dieu lui fasse miséricorde : on ne dit pas “ plus aveugle que ” (<em>aʿmā min</em>) pour la cécité de l'œil, où il n'y a point de degrés ; mais pour la cécité du cœur on le dit — car les degrés s'y trouvent.</p>
<p>[Mots « aʿmā » (les lectures de l'imāla), « wa-aḍalla sabīlā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les lectures et la glose d'Abū ʿAlī vérifiées sur le texte d'Ibn ʿAṭiyya ; la parole de Sībawayh intacte.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont :</p>
<ul>
<li>L’honneur que Dieu, le Très-Haut, accorde à l’homme, et Sa préférence de lui : Il le créa en la plus belle conformation, lui donna l’intellect et la pensée, lui prépara les moyens de son aise, ce qu’il monte en terre ferme et mer, le sustenta des bonnes choses, et le préféra à beaucoup des créatures.</li>
<li>L’obligation de la sincérité envers Dieu, Puissant et Majestueux, seul — et la reconnaissance de Sa faveur et de Ses grâces, aux répondre par la gratitude et l’aveu : en quoi se réalise la purification de l’âme et son affinement des contrariants.</li>
<li>Le compte des serviteurs, au Jour de la résurrection, en la justice absolue : les gens recevront leurs livres contenants leurs œuvres, petites et grandes.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Par quoi Dieu, le Très-Haut, préféra-t-Il l’homme à l’autre en les versets ?</li>
<li>Je conclus des versets les procédés rhétoriques qu’ils contiennent, et j’expose l’effet de cela sur le sens.</li>
<li>Quel est le visé de l’enregistrement des œuvres des serviteurs et de leur remise à leurs auteurs au Jour de la résurrection ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>« Et sache que l’homme est une substance composée de l’âme et du corps. L’âme humaine est la plus noble des âmes existant au monde inférieur, et son corps la plus noble des corps existant au monde inférieur. L’établissement de cette excellence en l’âme humaine est que les puissances originaires de l’âme humaine sont trois : la nutrition, la croissance et la génération ; et l’âme animale a deux puissances : la sensation, externe ou interne, et le mouvement volontaire. Ces cinq puissances — j’entends la nutrition, la croissance, la génération, la sensation et le mouvement — sont acquises à l’âme humaine. Puis l’âme humaine est particularisée d’une autre puissance : la puissance raisonnable, percevant les réalités des choses comme elles sont — celle où se manifeste la lumière de la connaissance de Dieu, le Très-Haut, où rayonne la clarté de Sa magnificence : elle qui s’élance sur les secrets des deux mondes de la création et du commandement, et embrasse les espèces des créatures de Dieu, les esprits et les corps, comme elles sont. Et cette puissance procède de l’insémination des substances saintes et des esprits dépouillés divins : elle n’a point de part, en noblesse et excellence, avec ces puissances végétatives et animales. Quand il en est ainsi, paraît que l’âme humaine est la plus noble des âmes existant en ce monde. » [Mafātīḥ al-ghayb, de Fakhr al-Dīn al-Rāzī : 21/372 — réf. imprimée « 21/372 », conforme]</p>
<p>[Citation d’al-Rāzī intégrale et conforme : aucun emplacement vide.]</p>
<h3>Je contemple le texte et réponds à ce qui suit :</h3>
<ul>
<li>Je compare l’âme humaine et l’âme animale.</li>
<li>Je démontre, à travers le texte, que l’âme humaine est plus noble que toute autre.</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 73 à 77 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>kādū</em> (كَادُوا۟ — ils faillirent).</p>
<p><em>yastafizzūnaka</em> (يَسْتَفِزُّونَكَ — te délogent).</p>
<p><em>l-taftarīya</em> (لِتَفْتَرِىَ — pour forger).</p>
<p><em>laqadta</em> (لَّقَدْتَ — incliner).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 73-77) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche la cause de la descente des versets.</li>
<li>Sur qui revient le pronom de « d’elle » (<em>minhā</em>) en la parole du Glorifié :</li>
</ul>
<p>« Et ils ont failli te déloger de [cette] terre pour t’en faire sortir » (al-Isrāʾ, 76 — extrait)</p>
<p>[Vocable « minhā » et citation coranique (v. 76 — de la leçon suivante) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. Elle prépare la divergence sur le pronom de « minhā » — les Juifs de Médine (l’histoire de la terre des prophètes en Syrie) ou Quraysh (la leçon suivante : “ le plus juste, car la sourate est mecquoise ”) — le crux de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13659":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13659 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13659 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
