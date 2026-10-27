/**
 * R82 — savant(hadith-1es/12884) — Leçon 4 : le mérite des ablutions et de la
 * propreté intime (istiṭāba) — traduction savante FR (agent principal).
 * + QA : titleFr canoniques leçons 1/2 (ToC R81), notes de versets 12875
 *   désimbriquées (« et [lavez] vos pieds » → « et lavez vos pieds » — les
 *   crochets internes tronquaient le chip VERSE_NOTE_RE au premier ]).
 */
import { readFileSync, writeFileSync } from "node:fs";

const BOOK = "content/books/hadith-1es.json";
const REG = "scripts-translate/savant-registry.json";

/** Typographie FR du corpus : espace fine insécable (U+202F) avant ; : ! ?,
 *  et à l'intérieur des « ». Le markup ci-dessous n'a aucun attribut HTML. */
function fr(s: string): string {
  return s
    .replace(/« /g, "«\u202f")
    .replace(/ »/g, "\u202f»")
    .replace(/ ([;:!?])/g, "\u202f$1");
}

const htmlFr = fr(`<h1>Le mérite des ablutions et de la propreté intime (<em>istiṭāba</em>)</h1>
<p>Leçon sur le mérite des ablutions et de la propreté intime (<em>istiṭāba</em>), matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l'imam Mālik avec le commentaire de l'imam al-Zarqānī, à l'intention des élèves de la première année de l'enseignement secondaire traditionnel (<em>ʿatīq</em>) — la quatrième leçon.</p>
<ol>
<li>Connaître les règles de la propreté intime (<em>istiṭāba</em>).</li>
<li>Prendre conscience du mérite des ablutions.</li>
<li>S'appliquer à obtenir le mérite des ablutions.</li>
</ol>
<h2>Préambule</h2>
<p>La purification extérieure par l'eau en vue des prières, et la purification intérieure des péchés, sont une chose que Dieu Très-Haut aime — au vu de la généralité de Sa parole, puissant et majestueux :</p>
<p>[verset reproduit en image dans le manuel : « Certes, Dieu aime ceux qui reviennent repentants, et aime ceux qui se purifient. » — al-Baqara (2) : 222, extrait — le manuel imprime « 220 »]</p>
<p>Et cet amour, comme le reste des vertus, se réalise par la purification au moyen de la propreté intime (<em>istiṭāba</em>) et des ablutions.</p>
<p><em>Qu'est-ce donc que l'<em>istiṭāba</em>, et quelles sont ses règles ? Et quel est le mérite des ablutions ?</em></p>
<h2>Les hadiths</h2>
<ul>
<li>Mālik, d'après Hishām ibn ʿUrwa, d'après son père : « Le Messager de Dieu — paix et bénédiction sur lui — fut interrogé au sujet de la propreté intime (<em>istiṭāba</em>) ; il dit : « L'un de vous ne saurait-il trouver trois pierres ? » » [Muwaṭṭaʾ, n° 65]</li>
<li>Mālik, d'après Zayd ibn Aslam, d'après ʿAṭāʾ ibn Yasār, d'après ʿAbd Allāh al-Ṣunābiḥī : « Le Messager de Dieu — paix et bénédiction sur lui — a dit : Quand le serviteur croyant fait ses ablutions puis se rince la bouche, les fautes sortent de sa bouche ; quand il renifle l'eau puis la rejette (<em>istinthār</em>), les fautes sortent de son nez ; quand il se lave le visage, les fautes sortent de son visage — jusqu'à sortir de dessous les cils de ses yeux ; quand il se lave les mains, les fautes sortent de ses mains — jusqu'à sortir de dessous les ongles de ses mains ; quand il essuie sa tête, les fautes sortent de sa tête — jusqu'à sortir de ses deux oreilles ; et quand il se lave les pieds, les fautes sortent de ses pieds — jusqu'à sortir de dessous les ongles de ses pieds. » Il dit : « Puis sa marche à la mosquée et sa prière lui sont une surérogation (<em>nāfila</em>). » [Muwaṭṭaʾ, n° 68]</li>
</ul>
<h2>La compréhension</h2>
<h3>Explication lexicale</h3>
<ul>
<li><em>la propreté intime</em> (<em>istiṭāba</em>) : la quête du propre. Les gens de la langue ont dit : l'<em>istiṭāba</em>, c'est l'<em>istinjāʾ</em> ; on dit <em>istaṭāba</em> et <em>aṭāba</em> (<em>iṭāba</em>) de même : car celui qui fait l'<em>istinjāʾ</em> se met au propre en ôtant l'impureté de l'issue.</li>
<li><em>les fautes</em> (<em>khaṭāyā</em>) : les péchés.</li>
</ul>
<h3>Extraction des contenus</h3>
<p>Qu'est-ce que la propreté intime (<em>istiṭāba</em>), et quelles sont ses règles ?<br>
Expose le mérite des ablutions.</p>
<h2>L'analyse</h2>
<h3>Premièrement : le concept de la propreté intime (<em>istiṭāba</em>) et ses règles</h3>
<h4>Définition de l'<em>istiṭāba</em></h4>
<p>L'<em>istiṭāba</em> et l'<em>istinjāʾ</em> ont, dans la langue, un seul et même sens : on dit <em>istaṭāba</em> et <em>aṭāba</em> (<em>iṭāba</em>) de même ; car celui qui fait l'<em>istinjāʾ</em> se met au propre en ôtant l'impureté de l'issue. Abū ʿUmar [Ibn ʿAbd al-Barr] a dit : elle — l'<em>istiṭāba</em> —, l'<em>istijmār</em> et l'<em>istinjāʾ</em> ont un même sens, sauf que l'<em>istinjāʾ</em> ne se fait que par les pierres, et que l'<em>istijmār</em> et l'<em>istiṭāba</em> se font, eux, par l'eau et par la pierre.</p>
<h4>Avec quoi l'<em>istiṭāba</em> se fait-elle ?</h4>
<p>Aṣbagh s'est tenu au sens apparent de sa parole — paix et bénédiction sur lui : « L'un de vous ne saurait-il trouver trois pierres ? », restreignant l'<em>istijmār</em> à ce qui est de la nature de la terre : car c'est une dispense (<em>rukhṣa</em>), dont on ne franchit pas le champ de ce qui a été transmis. Le <em>jumhūr</em>, lui, a étendu par analogie, à partir d'elle, tout le reste : tout solide, pur, nettoyant, qui ne nuit pas et n'est pas vénéré — parce que la dispense porte sur l'acte lui-même, non sur ce sur quoi il porte ; parce que le fondement de sa justification, dans le rejet de la bouse, est qu'elle est une impureté (<em>riʾth</em>), non qu'elle n'est pas pierre ; et au vu de sa parole — paix et bénédiction sur lui : « Quand l'un de vous satisfait son besoin, qu'il se nettoie avec trois bâtons, ou trois pierres, ou trois poignées de terre », rapporté par al-Dāraquṭnī ; et parce que « les pierres » (<em>al-aḥjār</em>) est une appellation (<em>laqab</em>), dont le sens implicite n'est pas retenu par le <em>jumhūr</em>.</p>
<h4>Le mérite de l'<em>istiṭāba</em></h4>
<p>Est rapporté sur le mérite de la propreté intime, d'après Abū Ayyūb, Jābir ibn ʿAbd Allāh et Anas ibn Mālik — les Anṣārītes —, d'après le Messager de Dieu — paix et bénédiction sur lui —, au sujet de ce verset :</p>
<p>[verset reproduit en image dans le manuel : « Une mosquée fondée sur la piété dès le premier jour mérite davantage que tu t'y tiennes debout : on y trouve des hommes qui aiment à se purifier, et Dieu aime ceux qui se purifient. » — al-Tawba (9) : 108, extrait — le manuel imprime « 109 »]</p>
<p>il dit : « O communauté des Anṣār, Dieu vous a loués, et bien, pour votre pureté (<em>ṭuhūr</em>) : quelle est donc cette pureté qui est la vôtre ? » Ils dirent : « Ô Messager de Dieu, nous faisons nos ablutions pour la prière, et nous nous lavons de l'impureté majeure (<em>janāba</em>). » Le Messager de Dieu — paix et bénédiction sur lui — dit : « Et y a-t-il, en dehors de cela, autre chose ? » Ils dirent : « Non — sinon que l'un de nous, lorsqu'il sort des lieux, aime à se nettoyer avec l'eau. » Il dit : « C'est cela : faites-le donc. » [rapporté par al-Dāraquṭnī]</p>
<h3>Deuxièmement : le mérite des ablutions</h3>
<p>Les ablutions ont un mérite considérable, comme le hadith l'a détaillé ; en voici l'exposé :</p>
<h4>L'expiation des péchés des membres</h4>
<ul>
<li><em>La sortie des fautes du nez et de la bouche</em>. ʿIyāḍ a dit : la mention de la sortie des fautes est une image (<em>istiʿāra</em>), pour la réalisation du pardon. Al-Bājī a dit : il se peut que le rinçement de bouche soit une expiation de ce qui revient à la bouche comme fautes — exprimé par leur sortie d'elle ; et il se peut que Dieu Très-Haut remette au serviteur le châtiment des fautes qu'il a acquises, même si elles ne reviennent pas à ce membre.</li>
<li><em>La sortie des fautes du visage et des deux yeux</em>. Al-Bājī a dit : Il a fait des deux yeux la sortie des fautes du visage, à la différence de la bouche et du nez : car ces derniers sont propres à une pureté légiférée dans les ablutions, à la différence des deux yeux.</li>
<li><em>La sortie des fautes de la tête et des deux oreilles</em>. Al-Bājī a dit : Il a fait des deux oreilles la sortie des fautes de la tête, tout en les particularisant par la prise d'eau qui leur revient ; et Il n'a pas fait de la bouche et du nez la sortie des fautes du visage, parce qu'ils précèdent le visage : ils n'ont donc pas le statut de dépendance (<em>tabʿ</em>), et leurs fautes sortent d'eux avant de sortir du visage ; les deux oreilles, elles, sont en retrait de la tête : elles ont donc le statut de dépendance. » Fin de citation. Et ceci comporte l'indication que les fautes de la tête tiennent à l'ouïe ; plus explicite encore à cet égard est le hadith d'Abū Umāma chez al-Ṭabarānī, dans le <em>Ṣaghīr</em> : « Et quand il essuie sa tête, cela expie ce que ses deux oreilles ont entendu. »
Et comme l'ôtement de l'impureté matérielle se fait par l'écoulement de l'eau — qui est le lavage —, il était cohérent, en matière d'ôtement de l'impureté intérieure que sont les fautes, de mentionner l'écoulement — qui est le lavage — plutôt que l'essuyage.</li>
<li><em>La sortie des fautes des deux pieds</em> : le pardon de ce qu'il peut avoir commis comme fautes avec ses deux pieds.</li>
</ul>
<h4>Sa prière lui est une surérogation</h4>
<p>Le sens de ce que sa prière lui est une <em>nāfila</em>, comme le hadith de la leçon l'explicite : un accroissement pour lui, en récompense, par-dessus la sortie des fautes et leur pardon — et il est connu, ce qu'il y a de récompense immense dans la marche [à la mosquée] et la prière.</p>
<h4>Quelles sont les fautes que les ablutions expient-elles ?</h4>
<p>Les savants ont restreint le hadith de la leçon et ses semblables — parmi les hadiths où figure le pardon des fautes — aux fautes mineures (<em>ṣaghāʾir</em>) ; quant aux fautes majeures (<em>kabāʾir</em>), rien ne les expie que le repentir (<em>tawba</em>) — au vu du hadith de Muslim dans son <em>Ṣaḥīḥ</em> : « Les cinq prières, du vendredi au vendredi, et du Ramaḍān au Ramaḍān, expient ce qui est entre elles, tant que les fautes majeures sont évitées. » Ils ont fait de la restriction portée par ce hadith la restriction des formulations absolues des autres. Mais Ibn Dīq al-ʿĪd a dit : cela prête à examen. Ibn al-Tīn a dit : on a divergé : les fautes majeures lui sont-elles pardonnées par ceci, s'il ne s'y affermit pas, ou bien rien d'autre que les mineures ne lui est-il pardonné ? Il dit : et tout cela n'entre pas en ligne de compte pour les torts causés aux serviteurs (<em>maẓālim al-ʿibād</em>). Et dans <em>al-Mufhim</em> [de al-Qāḍī ʿIyāḍ], il est dit : il n'est pas exclu qu'à certaines personnes soient pardonnées les fautes majeures et mineures, selon la sincérité (<em>ikhlāṣ</em>) qui les saisit et l'excellence (<em>iḥsān</em>) et les bienséances (<em>ādāb</em>) qu'elles observent — cela relève de la faveur de Dieu, qu'Il accorde à qui Il veut.
Al-Nawawī a dit : ce dont les hadiths font état, c'est que cela expie : s'il trouve des fautes mineures à expier, il les expie ; s'il ne rencontre ni mineure ni majeure, des bonnes actions lui sont écrites par là et des degrés lui sont élevés ; et s'il rencontre une faute majeure ou des majeures sans mineure, nous espérons qu'il en allège les majeures. » Fin de citation.</p>
<h2>L'évaluation</h2>
<ol>
<li>Expose le mérite de la propreté intime (<em>istiṭāba</em>), en t'appuyant sur un texte légal.</li>
<li>Fais ressortir le mérite des ablutions.</li>
<li>Compare les ablutions et la propreté intime quant à la règle.</li>
</ol>
<h2>L'exploitation</h2>
<p>Mālik, d'après al-ʿAlāʾ ibn ʿAbd al-Raḥmān, d'après son père, d'après Abū Hurayra : « Le Messager de Dieu — paix et bénédiction sur lui — sortit vers le cimetière et dit : « La paix soit sur vous, demeure d'un peuple de croyants ; et nous, s'il plaît à Dieu, vous rejoindrons bientôt. Je voudrais avoir déjà vu nos frères. » Ils dirent : « Ne sommes-nous pas tes frères, ô Messager de Dieu ? » Il dit : « Vous, vous êtes mes compagnons ; nos frères, ce sont ceux qui ne sont pas encore venus ; et je suis leur avant-coureur (<em>faraṭ</em>) au Bassin (<em>ḥawḍ</em>). » Ils dirent : « Ô Messager de Dieu, comment reconnaîtras-tu ceux de ta communauté qui viendront après toi ? » Il dit : « Vois-tu : si un homme a des chevaux au front blanc et aux membres blancs, parmi des chevaux noir de jais — ne reconnaît-il pas les siens ? » Ils dirent : « Certes, ô Messager de Dieu. » Il dit : « Eh bien, eux, ils viendront au jour de la Résurrection au front blanc et aux membres blancs, marques de leurs ablutions (<em>ghurran muḥajjalīn</em>) ; et je suis leur avant-coureur au Bassin. Des hommes seront chassés de mon Bassin comme on chasse le chameau égaré : je les appelle — Eh ! venez ! Eh ! venez ! Eh ! venez ! — et l'on me dira : ils ont changé après toi. Je dirai alors : Qu'ils s'en aillent ! qu'ils s'en aillent ! qu'ils s'en aillent ! (<em>fa-suḥqan</em>) » [Muwaṭṭaʾ, n° 68]</p>
<ol>
<li>Expose la conséquence, dans la Loi, du changement (<em>tabdīl</em>).</li>
<li>Extrais le mérite des ablutions rapporté dans le hadith.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Quelle est la règle de l'essuyage sur les deux chaussures (<em>khuffayn</em>), et quelle en est la sagesse ?</li>
<li>Expose la règle de l'essuyage sur le turban à la place de la tête.</li>
</ol>
`);

interface Lesson { docId: string; titleFr?: string; htmlFr?: string }
const book = JSON.parse(readFileSync(BOOK, "utf8")) as { lessons: Lesson[] };

// 1) Leçon 4 — traduction savante + titre canonique (ToC R81).
const l = book.lessons.find((x) => x.docId === "12884");
if (!l) throw new Error("12884 introuvable");
const before = (l.htmlFr ?? "").length;
l.htmlFr = htmlFr;
l.titleFr = "Le mérite des ablutions et de la propreté intime (istiṭāba)";
console.log(`12884 : FR ${before} → ${htmlFr.length} car ; titleFr canonique.`);

// 2) QA — titres canoniques leçons 1-2 (ToC R81 ; le champ restait GT).
const t1 = book.lessons.find((x) => x.docId === "12875");
if (t1) { t1.titleFr = "La pratique des ablutions (al-ʿamal fī al-wuḍūʾ)"; }
const t2 = book.lessons.find((x) => x.docId === "12881");
if (t2) { t2.titleFr = "La pureté requise pour les ablutions"; }
console.log("12875/12881 : titleFr canoniques.");

// 3) QA — 12875 : désimbriquer les crochets internes des notes de verset
//    (« et [lavez] vos pieds » tronquait le chip au premier « ] »).
const l75 = book.lessons.find((x) => x.docId === "12875");
if (l75?.htmlFr) {
  const fixed = l75.htmlFr.replace("et [lavez] vos pieds", "et lavez vos pieds");
  if (fixed !== l75.htmlFr) {
    l75.htmlFr = fixed;
    console.log("12875 : note de verset Māʾida 7 désimbriquée (crochet interne retiré).");
  }
}

writeFileSync(BOOK, JSON.stringify(book, null, 2));

// 4) Registre savant — 12884.
const reg = JSON.parse(readFileSync(REG, "utf8")) as { hand: string[] };
if (!reg.hand.includes("12884")) {
  reg.hand.push("12884");
  reg.hand.sort();
  writeFileSync(REG, JSON.stringify(reg, null, 2) + "\n");
}
console.log(`Registre : hand ${reg.hand.length} (+1).`);
