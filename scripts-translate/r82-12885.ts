/**
 * R82 — savant(hadith-1es/12885) — Leçon 5 : l'essuyage de la tête, des
 * oreilles et des chaussures (khuffayn) — traduction savante FR.
 */
import { readFileSync, writeFileSync } from "node:fs";

const BOOK = "content/books/hadith-1es.json";
const REG = "scripts-translate/savant-registry.json";

function fr(s: string): string {
  return s
    .replace(/« /g, "«\u202f")
    .replace(/ »/g, "\u202f»")
    .replace(/ ([;:!?])/g, "\u202f$1");
}

/** Note de verset Māʾida 7 — texte au pixel près de 12875 (post-désimbriquage
 *  R82) : même verset-image, même restitution, cohérence du corpus. */
const MAIDA7 =
  "[verset reproduit en image dans le manuel\u202f: «\u202fÔ vous qui croyez\u202f! Quand vous vous levez pour la prière, lavez vos visages et vos mains jusqu’aux coudes, et essuyez vos têtes, et lavez vos pieds jusqu’aux chevilles. Et si vous êtes en état d’impureté majeure, purifiez-vous. Et si vous êtes malades, ou en voyage, ou si l’un de vous revient de la selle, ou si vous avez touché des femmes et ne trouvez pas d’eau, alors recourez à une terre pure…\u202f» — al-Māʾida (5)\u202f: 7, extrait]";

const htmlFr = fr(`<h1>L'essuyage de la tête, des oreilles et des chaussures</h1>
<p>Leçon sur l'essuyage de la tête, des oreilles et des chaussures (<em>khuffayn</em>), matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l'imam Mālik avec le commentaire de l'imam al-Zarqānī, à l'intention des élèves de la première année de l'enseignement secondaire traditionnel (<em>ʿatīq</em>) — la cinquième leçon.</p>
<ol>
<li>Connaître la règle de l'essuyage de la tête et des oreilles.</li>
<li>Prendre conscience de la preuve de la pérennité de l'essuyage sur les deux chaussures.</li>
<li>Incarner la méthode requise dans l'essuyage sur les deux chaussures.</li>
</ol>
<h2>Préambule</h2>
<p>Les ablutions sont lavage et essuyage : les parties essuyées sont les deux oreilles, la tête et les deux chaussures. L'essuyage de la tête relève des obligations des ablutions : elles ne sont pas valides sans lui — comme l'indique Sa parole, exalté soit-Il :</p>
<p>${MAIDA7}</p>
<p>Et dans le <em>Muwaṭṭaʾ</em> : « Yahyā a dit : on interrogea Mālik au sujet d'un homme qui fit ses ablutions et oublia d'essuyer sa tête, jusqu'à ce que l'eau de ses ablutions eût séché. Il dit : j'estime qu'il essuie sa tête ; et s'il a déjà prié, qu'il répète la prière. » [Muwaṭṭaʾ, n° 80]</p>
<p><em>Quelle est donc l'origine de la méthode d'essuyage des deux oreilles ? Et est-il permis d'essuyer sur le turban (<em>ʿimāma</em>), sur le voile (<em>khimār</em>) et sur les deux chaussures ?</em></p>
<h2>Les hadiths</h2>
<ul>
<li>Mālik, d'après Nāfiʿ : « ʿAbd Allāh ibn ʿUmar prenait l'eau avec ses deux doigts pour ses deux oreilles. » [Muwaṭṭaʾ, n° 75]</li>
<li>Yahyā a dit : on interrogea Mālik sur l'essuyage sur le turban et le voile ; il dit : « Il ne convient ni que l'homme ni que la femme essuie sur un turban ou sur un voile : qu'ils essuient tous deux sur leurs têtes. » [Muwaṭṭaʾ, n° 79]</li>
<li>Mālik, d'après Ibn Shihāb, d'après ʿAbbād ibn Ziyād — qui est de la descendance d'al-Mughīra ibn Shuʿba —, d'après son père al-Mughīra ibn Shuʿba : « Le Messager de Dieu — paix et bénédiction sur lui — s'en fut pour son besoin lors de l'expédition de Tabūk. Al-Mughīra dit : je m'en allai avec lui, portant de l'eau. Le Messager de Dieu — paix et bénédiction sur lui — vint, et je versai l'eau sur lui : il lava son visage ; puis il voulut faire sortir ses deux mains des manches de sa <em>jubba</em>, et ne put — tant les manches de la <em>jubba</em> étaient étroites : il les fit sortir de dessous la <em>jubba</em>, lava ses deux mains, essuya sa tête et essuya sur ses deux chaussures. Le Messager de Dieu — paix et bénédiction sur lui — arriva, tandis que ʿAbd al-Raḥmān ibn ʿAwf les conduisait en prière et leur avait déjà fait une <em>rakʿa</em> ; le Messager de Dieu — paix et bénédiction sur lui — pria la <em>rakʿa</em> qui leur restait — et les gens furent saisis d'alarme. Quand le Messager de Dieu — paix et bénédiction sur lui — eut achevé sa prière, il dit : « Vous avez bien fait. » » [Muwaṭṭaʾ, n° 81]</li>
</ul>
<h2>La compréhension</h2>
<h3>Explication lexicale</h3>
<ul>
<li><em>Tabūk</em> : le nom d'un lieu appelé la Source de Tabūk (<em>ʿAyn Tabūk</em>).</li>
<li><em>je versai</em> (<em>saqabtu</em>) : je répandis.</li>
<li><em>la jubba</em> : ce qui est coupé des étoffes, remonté de manches.</li>
<li><em>les deux chaussures</em> (<em>khuffān</em>) : deux bas de cuir cousus qui couvrent les deux talons.</li>
<li><em>les gens furent saisis d'alarme</em> (<em>fazaʿa al-nās</em>) : ils craignirent d'avoir failli, pour avoir précédé le Messager de Dieu — paix et bénédiction sur lui — dans la prière.</li>
</ul>
<h3>Extraction des contenus</h3>
<p>Quelle est l'origine de l'essuyage des deux oreilles, et quelle est sa méthode ?<br>
Est-il permis d'essuyer sur le turban et sur le voile ?<br>
Détermine la règle de l'essuyage sur les deux chaussures, et expose sa méthode.</p>
<h2>L'analyse</h2>
<p>Les hadiths mentionnés comportent trois règles parmi les actes des ablutions, à savoir :</p>
<h3>Premièrement : l'essuyage des deux oreilles</h3>
<p>L'essuyage des deux oreilles relève des sunnas des ablutions, avec la recommandation de renouveler l'eau pour elles — comme l'indique le hadith du chapitre. La méthode de leur essuyage : qu'il resserre les doigts de ses deux mains et fasse passer ses deux index, puis essuie avec eux ses deux oreilles, par le dedans et par le dehors. Al-Bājī a dit : il se peut qu'il prenne l'eau avec deux doigts de chaque main et essuie de eux ses deux oreilles — à l'image du hadith d'Ibn ʿAbbās : le dedans des deux oreilles s'essuie avec les index, et leur dehors avec les pouces.</p>
<h3>Deuxièmement : l'essuyage de la tête</h3>
<p>L'essuyage de la tête relève des obligations des ablutions, sans quoi elles ne sont pas valides — au vu de la parole de Dieu, exalté soit-Il :</p>
<p>${MAIDA7}</p>
<p>Et le fondement, dans le discours, est le sens propre, non le sens figuré : il n'est donc pas permis d'essuyer sur le turban. Al-Zarqānī a dit : l'ont permis Aḥmad, al-Awzāʿī, Dāwūd et d'autres — au vu des rapports, et par analogie sur les deux chaussures ; l'ont interdit Mālik, al-Shāfiʿī et Abū Ḥanīfa : car l'essuyage sur les deux chaussures procède des rapports, non de l'analogie — et si c'était de l'analogie, il serait permis d'essuyer sur les deux gants (<em>qaffāzān</em>).
Al-Khaṭṭābī a dit : Dieu a érigé l'essuyage de la tête en obligation ; et le hadith de l'essuyage sur le turban se prête à l'interprétation : on n'abandonne pas le certain pour l'ambigu ; et son analogie sur le khuff est éloignée — la dispense du khuff tenant à la difficulté de l'ôter, à la différence du turban. Ce qui en a été rapporté et qui indique sa permission est donc interprété des états d'excuse, au vu du hadith de l'essuyage sur la mèche (<em>naṣīya</em>) avec le turban.
Et ce qui indique la pérennité de la pratique de l'ôtement du turban — de même que du voile —, ce sont les rapports du <em>Muwaṭṭaʾ</em> :</p>
<ul>
<li>Mālik : « il lui parvint que Jābir ibn ʿAbd Allāh l'Anṣārīte fut interrogé au sujet de l'essuyage sur le turban ; il dit : non — jusqu'à ce qu'il essuie les cheveux avec l'eau. » [Muwaṭṭaʾ, n° 76]</li>
<li>Mālik, d'après Hishām ibn ʿUrwa : « son père ʿUrwa ibn al-Zubayr ôtait le turban et essuyait sa tête avec l'eau. » [Muwaṭṭaʾ, n° 77]</li>
<li>Mālik, d'après Nāfiʿ : « il vit Ṣafiyya bint Abī ʿUbayd, femme de ʿAbd Allāh ibn ʿUmar, ôter son voile et essuyer sa tête avec l'eau — Nāfiʿ étant ce jour-là tout jeune. » [Muwaṭṭaʾ, n° 78]</li>
</ul>
<h3>Troisièmement : l'essuyage sur les deux chaussures</h3>
<h4>Sa règle</h4>
<p>L'essuyage sur les deux chaussures est une dispense (<em>rukhṣa</em>) en fiqh mālikī. Une compagnie de maîtres du hadith (<em>muḥaddithīn</em>) et de gardiens (<em>ḥuffāẓ</em>) a déclaré formellement son établissement par transmission massive (<em>tawātur</em>) ; certains en ont compté les rapporteurs, qui excédèrent les quatre-vingts. De ce qui atteste son établissement : le hadith d'al-Mughīra ibn Shuʿba, dont le lieu pertinent est sa parole : « et il essuya sur les deux chaussures ». Al-Zarqānī a dit : il y a là réfutation de quiconque a prétendu que l'essuyage sur elles deux était abrogé par le verset d'al-Māʾida — car il fut révélé lors de l'expédition d'al-Muraysiʿ, tandis que ce récit est de l'expédition de Tabūk, postérieure à celui-là de consensus, celle-ci étant la dernière des expéditions ; et d'ailleurs l'essuyage sur les deux chaussures est propre aux ablutions : le lavage n'y a aucune part, de consensus.
Et attestent encore l'établissement de l'essuyage des rapports des Compagnons, dont Mālik a mentionné une partie dans le <em>Muwaṭṭaʾ</em>, d'après Saʿd ibn Abī Waqqāṣ, ʿAbd Allāh ibn ʿUmar et Anas ibn Mālik ; et c'est là le sain [transmis] de l'imam Mālik — que Dieu lui fasse miséricorde. Et dans [le commentaire d']al-Zarqānī : Ibn Wahb a dit : la dernière chose sur laquelle j'ai quitté Mālik est l'essuyage, en résidence comme en voyage. De même que le <em>mashhūr</em> du <em>madhhab</em> en permet l'usage au voyageur comme au résident — mais il n'essuie qu'à condition de les avoir endossées en une pureté d'eau complète, c'est-à-dire après l'achèvement de ses ablutions. Ainsi dans le <em>Muwaṭṭaʾ</em> : « Yahyā a dit : on interrogea Mālik au sujet d'un homme qui fit les ablutions de la prière, puis endossa ses deux chaussures, puis urina, puis les ôta, puis les remit à ses deux pieds : reprend-il les ablutions ? Il dit : qu'il ôte ses deux chaussures, puis qu'il fasse ses ablutions et lave ses deux pieds ; car n'essuie sur les deux chaussures que celui qui a introduit ses deux pieds dans les deux chaussures alors qu'elles étaient toutes deux pures de la pureté des ablutions ; quant à celui qui a introduit ses deux pieds dans les deux chaussures alors qu'elles n'étaient pas toutes deux pures de la pureté des ablutions — il n'essuie pas sur les deux chaussures. » [Muwaṭṭaʾ, n° 85]</p>
<h4>La méthode de l'essuyage sur elles</h4>
<p>Cette méthode, l'expose ce que Mālik a rapporté d'après Hishām ibn ʿUrwa : « il vit son père essuyer sur les deux chaussures — il ne rajoutait pas, en essuyant sur elles, à l'essuyage de leurs deux dos, et n'essuyait pas leurs deux semelles. » [Muwaṭṭaʾ, n° 88]
Al-Zarqānī a dit : « parce que le dos du khuff est le lieu de l'obligation de l'essuyage, de consensus ; et le apparent du <em>madhhab</em> veut qu'on les couvre entièrement tous les deux : s'il essuie le dessus sans le dessous, il répète dans le temps ; et s'il fait l'inverse, il répète toujours (<em>abada</em>). ʿAlī — que Dieu l'agrée — a dit : si la religion relevait de l'opinion, le dessous du khuff serait plus en droit d'être essuyé que son dessus — or j'ai vu le Messager de Dieu — paix et bénédiction sur lui — essuyer sur le dos de ses deux khuffs. » Et al-Mughīra a transmis le semblable. Son fondement est ce que l'Imam a transmis d'Ibn Shihāb : « il demanda à Ibn Shihāb comment se fait l'essuyage sur les deux chaussures ; Ibn Shihāb introduisit l'une de ses mains sous le khuff et l'autre au-dessus de lui, puis les fit toutes deux couler. Yahyā a dit : Mālik a dit : la parole d'Ibn Shihāb est ce que j'ai entendu de plus aimé en cela. » [Muwaṭṭaʾ, n° 89]
Et dans le <em>Jāmiʿ</em> d'Ibn Yūnus : « Ibn al-Qāsim a dit : Mālik nous montra l'essuyage sur les deux chaussures : il posa sa main droite sur les bouts de ses orteils, du dessus de son pied droit, et posa la gauche sous les bouts des orteils du dessous de son khuff, puis les fit aller toutes deux jusqu'aux places des ablutions — c'est-à-dire la base du tibia et l'alignement des deux talons. Abū Muḥammad a dit : de même sa main gauche, du dessus de son pied gauche, et sa main droite de dessous. Ibn Ḥabīb a dit : de même nous le montrèrent al-Muṭarrif et Ibn al-Mājishūn. »
Et l'acquis : celui qui essuie — de quelque façon qu'il essuie — est acquitté, dès lors que son essuyage couvre les deux khuffs ; ainsi a dit al-Zarqānī.</p>
<h2>L'évaluation</h2>
<ol>
<li>Cite ce qui indique la non-permission d'essuyer sur le turban et sur le voile.</li>
<li>Explicite la méthode de l'essuyage des deux oreilles.</li>
<li>Expose le meilleur dans la méthode de l'essuyage sur les deux chaussures, et argumente sa non-abrogation.</li>
</ol>
<h2>L'exploitation</h2>
<p>Yahyā a dit : on interrogea Mālik au sujet d'un homme qui fit ses ablutions, ses deux chaussures aux pieds, et qui s'oublia quant à l'essuyage sur elles, jusqu'à ce que ses ablutions eussent séché et qu'il eût prié. Il dit : « qu'il essuie sur ses deux chaussures, et qu'il répète la prière — et qu'il ne répète pas les ablutions. » [Muwaṭṭaʾ, n° 86]
Yahyā a dit : on interrogea Mālik au sujet d'un homme qui lava ses deux pieds, puis endossa ses deux chaussures, puis recommença les ablutions. Il dit : « qu'il ôte ses deux chaussures, puis qu'il fasse ses ablutions et lave ses deux pieds. » [Muwaṭṭaʾ, n° 87]</p>
<ol>
<li>Extrais du premier texte la règle de la continuité (<em>muwālāt</em>) entre l'essuyage sur les deux chaussures et le reste des membres des ablutions.</li>
<li>Expose, au fil du second texte, la règle de celui qui a renversé l'ordre des actes des ablutions, puis endossa ses deux chaussures avant l'achèvement de ses ablutions.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Expose ce qu'on entend par l'épistaxis (<em>ruʿāf</em>), et son rapport aux annulateurs des ablutions.</li>
<li>Qu'est-il obligatoire à celui qui a une hémorragie de nez dans la prière ?</li>
<li>Médite les hadiths de la leçon à venir, et détermine les règles qu'ils comportent.</li>
</ol>
`);

interface Lesson { docId: string; titleFr?: string; htmlFr?: string }
const book = JSON.parse(readFileSync(BOOK, "utf8")) as { lessons: Lesson[] };

const l = book.lessons.find((x) => x.docId === "12885");
if (!l) throw new Error("12885 introuvable");
const before = (l.htmlFr ?? "").length;
l.htmlFr = htmlFr;
l.titleFr = "L'essuyage de la tête, des oreilles et des chaussures";
console.log(`12885 : FR ${before} → ${htmlFr.length} car ; titleFr canonique (ToC R81).`);

writeFileSync(BOOK, JSON.stringify(book, null, 2));

const reg = JSON.parse(readFileSync(REG, "utf8")) as { hand: string[] };
if (!reg.hand.includes("12885")) {
  reg.hand.push("12885");
  reg.hand.sort();
  writeFileSync(REG, JSON.stringify(reg, null, 2));
}
console.log(`Registre : hand ${reg.hand.length} (+1).`);
