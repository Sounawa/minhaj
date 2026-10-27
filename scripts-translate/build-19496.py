#!/usr/bin/env python3
# build-19496.py — 19496 « Jurisprudence : des jugements du garant et du
# garanti » (fiqh-tanawi-3, lessons[19], badge Leçon 21/33) — suite du bāb,
# dix-septième cours consécutif (6e → … → 17e). DEUX axes h3 : (1) la
# définition du ḍamān (langue : Fayyūmī ḍāmin/ḍamīn, Māzarī ḥimāla/kafāla/
# ḍamān/zaʿāma, Ṣāwī la garde + āḏāna + qubāla ; terminologie : Khalīl
# « l'occupation d'une autre ḏimma par le droit » + Ibn ʿArafa « le rejet
# de la dette d'une ḏimma, à l'identique, dans une autre »), ses piliers
# (Ibn al-Ḥāğib : cinq), son jugement (jāʾiz ; Yūsuf 12:72 + Ibn ʿAbbās +
# hadīth d'Abū Umāma [Abū Dāwūd] + ijmāʿ), ses types (bien/visage/recherche) ;
# (2) les jugements du garant (tabarruʿ valide, malade par le tiers, surcroît
# rendu aux héritiers, safīh/ṣabī/mağnūn corrupt), du garanti (le mort
# insolvable — Abū Ḥanīfa et an-Nawawī contre ; le garant), de la dette
# (huit items : liquide/différé avec Yūsuf... non — Baqara 2:280 ; solvable/
# insolvable non ensemble ; dette ferme ou āʾil non déterminé ; waʿd ; ce qui
# lie ; le retour ; la condition ; les trois ignorances + douceur/peine +
# science du vendeur Ibn Yūnus). Matn INTÉGRAL (un bloc, guillemet fermant
# présent). Exploitation DOUBLE : Ibn Rušd [Muqaddimāt 2/378] + Māzarī
# [Manḥ al-Ğalīl 6/202]. TROIS fentes de versets : Yūsuf 12:72 ×2 (extrait,
# rendu du traducteur) + Baqara 2:280 (extrait, rendu corpus établi repris
# à l'identique). 1 hadīth (Abū Umāma, Abū Dāwūd). Préparation préalable =
# UNE phrase (ḍamān de l'absent → 19500). Fente liminaire VIDE (2e conséc.) ;
# at-taʿbīm 16e occ.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19496_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    ar = [c for c in ar if c != chr(0xFDFA)]
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'br', 'dl', 'dt', 'dd']:
    if tag in ('br',):
        continue
    o, c = html.count(f'<{tag}>'), html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')

PROBES = [
    'Jurisprudence : des jugements du garant et du garanti',
    '<dt></dt>\n<dd></dd>',
    'il cherche alors ici et là quelqu’un qui le garantisse auprès du détenteur du droit',
    'Et Dieu — le Très-Haut — est miséricordieux envers les serviteurs, subtil avec eux',
    'Qu’est-ce que le ḍamān ? Et quels sont ses types et ses piliers ? Et quels sont ses jugements et ses conditions ?',
    '— Livre de jurisprudence, du Mukhtaṣar du cheikh Khalīl, avec le Šarḥ d’ad-Dardīr et la Hāšiya d’ad-Dasūqī — dix-septième leçon, au profit des élèves et des élèves de la troisième année secondaire de l’ancien enseignement (<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Connaître le concept du ḍamān, son jugement et ses types.',
    '2. Saisir les jugements du ḍamān et ses conditions.',
    '3. Se représenter les jugements du ḍamān dans mes transactions.',
    '<h2>Le texte</h2>',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    '« Le ḍamān est l’occupation d’une autre ḏimma par le droit ; et il est valide [venant] du peuple de la libéralité... — et [du] malade, par le tiers... —',
    'et [il est valide] sur le mort insolvable, et sur le garant',
    'et [il garantit] le différé liquide, s’il est de ce qui peut être accéléré — et son contraire, s’il a facilité son débiteur, ou ne l’a point facilité dans le terme',
    'et [il garantit] par ce dont il est solvable, ou ce dont il est insolvable — non par les deux ensemble',
    '[il est valide] d’une dette ferme, ou s’abîmant (<em>āʾil</em>) vers elle',
    '« et je fais crédit à un tel »',
    'et il lie en ce qui s’est établi — et est-il restreint à ce par quoi l’on traite ? Deux interprétations.',
    'Il a le retour avant la transaction — à l’encontre de « jure, et je le garantis par cela »...',
    'mais comme un don récompensé (<em>juʿl</em>) — [le ḍamān n’étant valide que] si son recouvrement est possible auprès de son garant',
    'et sans sa permission : comme le paiement avec douceur, non avec peine — il est rendu : comme son achat — et, s’il le sait, son vendeur — lequel est le plus apparent ? Deux interprétations.',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    'Le peuple de la libéralité (<em>ahl at-tabarruʿ</em>) : l’ici-visé est le responsable (<em>mukallaf</em>) solvable.<br>\nSon débiteur (<em>ġarīm-hu</em>) : l’ici-visé est le débiteur (<em>maḍīn</em>).<br>\n<em>Āʾil</em> : qui s’achemine et revient.<br>\nAvec peine (<em>ʿanatan</em>) : peine et dommage.',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du matn la définition du ḍamān.',
    '2. Je dégage à travers le matn les jugements du ḍamān et ses types.',
    '3. Je montre à travers le matn de qui le ḍamān est valide, et de qui il n’est pas valide.',
    '<h2>L’analyse</h2>',
    'Cette leçon comprend les axes suivants :',
    '<h3>Axe premier : la définition du ḍamān, ses piliers, son jugement et ses types</h3>',
    '<h4>1. Le concept du ḍamān dans la langue et dans la terminologie</h4>',
    '<span>a. Dans la langue :</span> a dit al-Fayyūmī',
    '« J’ai garanti (<em>ḍamintu</em>) le bien, et par lui est le ḍamān — je suis le garant (<em>ḍāmin</em>) ; et le garanti (<em>ḍamīn</em>) — je m’y suis engagé. » [Le Miṣbāh al-Munīr, matière : ḍamn]',
    '« La ḥimāla, la kafāla, le ḍamān et la zaʿāma sont, dans la langue, un seul et même sens',
    'les Arabes disent aussi : qabīl, au sens de ḍamīn. » [Le Manḥ al-Ğalīl, commentaire du Mukhtaṣar de Khalīl, de Muḥammad ʿAlīš, 6/196]',
    '« Quant à la langue : c’est la garde (<em>al-ḥifẓ</em>).',
    '« Et pour qui l’apportera, une charge de chameau — et j’en suis le garant. » (Sourate Yūsuf, extrait du verset 72) — c’est-à-dire kafīl et ḍāmin',
    'ou l’<em>āḏāna</em> est au sens de l’engagement (<em>iğāb</em>), car il a rendu le droit obligatoire pour lui-même ; on l’appelle aussi <em>qubāla</em>. » [Bulġat as-Sālik li-aqrab al-masālik, d’aṣ-Ṣāwī 3/429]',
    '<span>b. Dans la terminologie :</span> l’auteur l’a défini par son dire : « l’occupation d’une autre ḏimma par le droit »',
    'et Ibn ʿArafa l’a défini par son dire : « le rejet de la dette d’une ḏimma, à l’identique, dans une autre. » [Le Mukhtaṣar al-fiqhī 6/488]',
    '<h4>2. Ses piliers</h4>',
    'A dit Ibn al-Ḥāğib : ses piliers sont cinq : le maḍmūn ʿan-hu — qui est le débiteur ; le maḍmūn la-hu — qui est le créancier ; le ḍāmin — qui est le kafīl ; le maḍmūn — qui est la dette',
    '« je me suis chargé », « je me suis porté garant », « j’ai garanti », « je suis zaʿīm », et semblables. [Ğāmiʿ al-ummahāt, d’Ibn al-Ḥāğib, p. 391-392, remanié]',
    '<h4>3. Son jugement</h4>',
    'Le ḍamān est révocable (<em>jāʾiz</em>) : il est une bienfaisance connue, que l’on fait de bon gré, et l’intérêt le requiert — la nécessité même y appelle',
    'il est de l’entraide dans la piété et la crainte de Dieu ; il accomplit le besoin du musulman et desserre sa peine',
    'Et la preuve de sa légalité est la légalité de la kafāla, globalement, par le Livre, la Sunna et l’Ijmāʿ',
    '« Ils dirent : nous avons perdu la coupe du roi ; pour qui l’apportera, une charge de chameau — et j’en suis le garant. » (Sourate Yūsuf, extrait du verset 72)',
    'A dit Ibn ʿAbbās : le zaʿīm est le kafīl.',
    'j’ai entendu le Messager de Dieu — que la prière et le salut de Dieu soient sur lui — dire : « L’emprunt à usage doit être rendu, la donation est reprise, la dette doit être acquittée, et le garant est un endetté. » [Sunan d’Abī Dāwūd, Livre des ventes, chapitre : sur la garantie de l’emprunt à usage]',
    'Et les musulmans ont été unanimes sur la licéité du ḍamān globalement — pour le besoin des gens en lui, et pour l’éloignement du dommage du débiteur',
    '<h4>4. Ses types</h4>',
    '<span>a. Le ḍamān du bien</span> ; c’est-à-dire la kafāla du débiteur et la prise en charge de ce qui est sur lui de bien, s’il ne le verse pas au créancier.',
    '<span>b. le ḍamān du visage</span> ; c’est-à-dire [celui] de la personne même du débiteur, en la présentant au seigneur de la dette au besoin de la dette',
    'ce type appartient aux gens de l’intercession (<em>ahl al-wağāha</em>) entre les gens, dont l’intercession n’est point repoussée',
    '<span>c. le ḍamān de la recherche</span> ; c’est-à-dire la prise en charge de la quête du débiteur absent.',
    '<h3>Axe deuxième : les jugements du garant, du garanti et de la dette</h3>',
    '<h4>1. Les jugements du garant</h4>',
    'le ḍamān est valide et lie quand il émane de qui, de lui, le tabarruʿ est valide — le responsable (<em>mukallaf</em>) sur qui n’est point d’interdiction (<em>ḥağr</em>) dans ce qu’il garantit',
    'comme lorsqu’un malade, atteint d’une maladie dont l’issue est redoutée, garantit une personne par le tiers, ou par ce qui la dépasse de peu — pourvu que l’on ne vise point par là le dommage',
    'car ce qui approche la chose reçoit son jugement — non ce qui l’excède de beaucoup : cela ne lie point, bien que valide',
    'Si le ḍamān d’un malade porte sur un surcroît au-delà du tiers : il est valide aussi, mais non liant — aux héritiers de rendre ce qui excède le tiers, et à eux la ratification (<em>iğāza</em>) du tout.',
    'S’il émane d’un faible d’esprit (<em>safīh</em>), d’un mineur ou d’un fou : il est corrompu, il doit être rendu, et le tuteur n’a point la ratification de cela — que le mineur fût discernant ou non.',
    '<h4>2. Les jugements du garanti</h4>',
    '<span>a. Le ḍamān du mort insolvable</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « et [il est valide] sur le mort insolvable »',
    'si quelqu’un se porte garant pour lui en connaissance de son insolvabilité, puis acquitte pour lui, il n’a point de retour sur un bien qui surviendrait ensuite — car son portage est une bienfaisance connue, un tabarruʿ de sa part',
    'mais s’il savait qu’il a un bien, ou le pensait, ou doutait, puis qu’un bien apparut — il revient par ce qu’il a versé pour lui',
    'Abū Ḥanīfa et an-Nawawī l’ont interdit — nul bien n’est espéré de qui paierait entier ce qui est sur lui',
    'le mort solvable, lui, ne fait point dispute sur la validité de son ḍamān — et le ḍāmin prend de sa succession ce qu’il a versé pour lui',
    'de même le vivant, solvable ou insolvable — et le ḍāmin revient contre lui par ce qu’il a versé pour lui.',
    '<span>b. Le ḍamān du garant</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « et sur le garant »',
    'un garant garantissant un garant, un seul ou plusieurs, et le garant du garant garantissant un autre.',
    '<h4>3. Les jugements de la dette</h4>',
    '<span>a. Le ḍamān de la dette :</span> le maḍmūn peut être autre chose qu’une dette, et peut être une dette',
    '<span>Première :</span> que la dette soit liquide (<em>ḥāʾila</em>) — et à cela l’auteur a fait allusion par son dire : « et [il garantit] le différé liquide, s’il est de ce qui peut être accéléré »',
    's’il décharge de la dette celui sur qui elle est de son droit au report, et qu’un autre garantisse pour la dévolution (<em>ḥulūl</em>) — par crainte des atermoiements, par exemple',
    'à condition que cette dette soit de ce qu’il est permis d’accélérer — l’<em>ʿayn</em> absolument, et les denrées et l’aliment par le prêt (<em>qarḍ</em>), non par la vente',
    'pour ce qu’elle contient de « prends le ḍamān et je te donne davantage », en guise de sûreté (<em>tuwṯīqa</em>) par le garant ; car cela est spécifique à la vente seulement',
    '<span>Seconde :</span> que la dette soit différée — et à cela l’auteur a fait allusion par son dire : « et son contraire, s’il a facilité son débiteur, ou ne l’a point facilité dans le terme »',
    'la première par son dire : « s’il a facilité son débiteur » — c’est-à-dire son débiteur, par la dette liquide, quand bien même au début du terme ; car la considération est à l’état présent, non à sa totalité',
    'c’est pour la sûreté contre un prêt (<em>salaf</em>) attirant un profit, par la capacité de [le créancier] à prendre son droit de lui',
    'c’est comme s’il s’agissait d’un prêt initial adossé au garant — le garant le facilitant au début du terme, nul profit n’advient par le ḍamān, quand bien même un prêt adviendrait par son report',
    'c’est-à-dire que le débiteur n’est point facilité dans le terme, mais accablé, et son accablement se prolonge jusqu’à l’échéance du terme que le garant a garanti',
    'à cause de l’obligation d’accorder le sursis à l’insolvable, par le mot du Très-Haut : « À celui qui est dans la gêne, accordez un sursis jusqu’à ce qu’il soit dans l’aisance. » (Sourate al-Baqara, extrait du verset 280)',
    '<span>b. Le ḍamān du débiteur par ce dont il est solvable, ou ce dont il est insolvable</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « et [il garantit] par ce dont il est solvable, ou ce dont il est insolvable — non par les deux ensemble »',
    'le ḍamān différé est valide par ce dont il est solvable seulement — en totalité ou en partie — à condition que sa facilité dure le terme entier',
    'car cela serait un prêt (<em>salaf</em>) attirant un profit : il serait prêteur pour ce dont il est solvable, en le différant sur ce qui est porté par lui — et profitant du ḍamān en ce dont il est insolvable',
    '<span>c. Le ḍamān dans une dette ferme, ou s’abîmant vers elle — non dans un déterminé</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « [il est valide] d’une dette ferme, ou s’abîmant vers elle »',
    'son dire « d’une dette » exclut la validité du ḍamān des déterminés : un dépôt (<em>wadīʿa</em>), un emprunt à usage (<em>ʿāriya</em>), un capital de muqāraḍa, une société (<em>širka</em>)',
    'sur la supposition que, s’ils périssent, il les rapporte en leur être même (<em>bi-ʿayni-hā</em>) — pour l’impossibilité de cela',
    's’il garantit ce qui en résulte, par un excès ou une négligence, à titre de ḍamān de la VALEUR — cela est valide et lie',
    'comme il arrive aux marchés : certains garantissent d’autres à condition que, si l’acheteur s’en va et ne rapporte pas le prix, le ḍāmin soit tenu de la valeur de ce par quoi il s’est enfui',
    '<span>d. Le ḍamān de la dette à venir</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « et je fais crédit à un tel »',
    '« je fais crédit à un tel », ou « je vends à un tel », ou « j’engage un tel — et je garantis ce que je lui aurai prêté, vendu ou engagé »',
    'car cela est une promesse (<em>waʿd</em>) de ḍamān, et la promesse doit être tenue — d’autant plus que le promis entre dans ce qui lui fut promis — et c’est une règle : la tenue de la promesse, lie-t-elle ou non ?',
    '<span>e. Ce qui lie le ḍamān</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « et il lie en ce qui s’est établi — et est-il restreint à ce par quoi l’on traite ? Deux interprétations »',
    'le ḍamān lie en ce qui s’est établi par une preuve (<em>bayyina</em>), et de même par l’aveu (<em>iqrār</em>) du maḍmūn, s’il est solvable',
    'si l’on dit : « engage (<em>ʿāmil</em>) un tel, et je le garantis », et que l’affaire d’un tel est d’être engagé pour mille dirhams — par exemple — et qu’il l’engage pour dix mille — par exemple —, le déclarant ne garantit point le surcroît au-delà du mille',
    '<span>f. Le retour du ḍāmin dans la promesse de ḍamān</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « Il a le retour avant la transaction — à l’encontre de « jure, et je le garantis par cela » »',
    'car il s’est engagé en une quantité qui n’a point de fin (<em>qadar lā ġāya la-hu</em>)',
    '« jure que ce que tu réclames contre lui est un droit, ou que tu as sur lui un droit, et je le garantis par cela » — point de retrait pour lui, quand bien même avant son serment',
    'car par son engagement, [le droit] est devenu comme un droit dû — on le place à la station du défendeur, plaçant l’inexistant à la station de l’existant',
    '<span>g. Une condition de la validité du ḍamān</span> — le dire de l’auteur — que Dieu lui fasse miséricorde — : « si son recouvrement est possible auprès de son garant »',
    'et cette condition est rendue superflue par son dire antérieur « d’une dette » — ce qui est visé par elle est l’exclusion des déterminés, des limites légales (<em>ḥudūd</em>) et de ce qui leur ressemble, comme les peines correctives (<em>taʿzīrāt</em>), la mise à mort, les blessures',
    '<span>h. Ce qui n’affecte point la validité du ḍamān</span> — a dit l’auteur — que Dieu lui fasse miséricorde — : « et quand bien même [la quantité] serait ignorée, ou [qu’on ignore] à qui elle appartient',
    '<span>La première :</span> s’il ignore la quantité du droit garanti, sur-le-champ et à l’échéance — comme lorsque le ḍāmin dit : « je garantis pour ʿAmr tout ce qui est sur Zayd »',
    '<span>La seconde :</span> si l’on ignore qui détient la dette — et c’est le maḍmūn la-hu — le pronom de « la-hu » est pour le seigneur de la dette',
    'c’est-à-dire quand bien même le seigneur de la dette serait inconnu : on garantit la dette d’un inconnu.',
    '<span>La troisième :</span> le ḍamān est valide sans la permission de celui sur qui est la dette — et c’est le maḍmūn ʿan-hu',
    'comme il est valide qu’une personne acquitte la dette d’une autre, sans sa permission, si elle l’acquitte pour elle avec douceur — et le seigneur de la dette doit en accepter la prise',
    'non si l’on visait, par le paiement ou par le ḍamān pour elle, une peine (<em>ʿanatan</em>) — c’est-à-dire un dommage — comme viser son emprisonnement pour une inimitié entre eux deux',
    'le paiement est rendu — c’est-à-dire que son acte est rendu sur lui — et il revient contre celui qui lui a payé, par ce qu’il lui a saisi pour lui — s’il périt à sa main, il lui rend son équivalent (<em>ʿiwaḍ</em>)',
    'et si le rendre devient impossible, pour l’absence du vendeur de la dette, le juge établit un homme qui saisit du débiteur et verse au payeur — avec peine',
    'à ceci : le rendement de l’achat de la dette avec peine a-t-il lieu si le vendeur de la dette SAIT que l’acheteur visait, par son achat, la peine ?',
    'la dette est vendue à l’acheteur, à une personne entre qui et le débiteur il n’y a point d’inimitié — pour que le dommage s’élève par cela',
    'et la restriction à la science de son vendeur est la plus apparente, selon Ibn Yūnus — deux interprétations',
    'Il ressort de la leçon que la Loi sage exhorte les gens du bienfait à porter secours aux autres',
    'et cela réalise la fin du bien (<em>al-ğawdī</em>), qui enracine l’affection entre les gens et fortifie la familiarité et le lien',
    'mais à condition que celui qui se charge soit conscient de la gravité de ce qu’il porte pour autrui, résolu à tenir les contrats',
    '<h2>Le contrôle</h2>',
    '1. Je définis le ḍamān.',
    '2. Je montre les types du ḍamān et ses piliers.',
    '3. J’éclaircis les jugements du ḍamān de la dette.',
    '<h2>L’exploitation</h2>',
    'A dit Ibn Rušd — que Dieu lui fasse miséricorde — : « La ḥimāla, selon le madhhab de Mālik, est permise sur le vivant et le mort',
    'le retour contre lui lui appartient par ce qu’il a versé pour lui, et le suivre (<em>ittibāʿ</em>) de lui, quand bien même il serait démuni',
    'qu’il se soit chargé pour lui avec sa permission ou sans sa permission',
    's’il s’est chargé pour un mort, sans qu’il y ait de quoi acquitter ce par quoi il s’est chargé, il n’a point à revenir par ce qu’il a versé contre un bien — s’il en survient un. »',
    '[Les Muqaddimāt al-Mumahhadāt, d’Ibn Rušd 2/378]',
    'Les gens de science n’ont point différé sur la licéité de la ḥimāla pour le vivant — solvable ou insolvable —, ni sur la ḥimāla pour le mort quand il est solvable',
    'la majorité (<em>al-ğumhūr</em>) est pour sa licéité, et seuls Abū Ḥanīfa et ṯ-Thawrī — que Dieu les agrée — l’ont interdite. »',
    '[Manḥ al-Ğalīl 6/202]',
    'Je contemple ces deux textes et je réponds à ce qui suit :',
    'J’extrais des deux textes les jugements qu’ils renferment, et je les compare à ce qu’il y a dans le matn.',
    'Je montre, à partir des deux textes, ce sur quoi l’on s’accorde et ce sur quoi l’on diffère au sujet de la ḥimāla, et la cause de ce désaccord.',
    '<h2>La préparation préalable</h2>',
    'Je lis le matn de la leçon à venir et je recherche les jugements du ḍamān de l’absent.',
    '<h2>Le sens de cette leçon</h2>',
    'Cette leçon fait entrer la garantie dans le droit commun des ḏimmas : « le ḍamān est l’occupation d’une autre ḏimma par le droit »',
    'la validité court du peuple de la libéralité au malade par le tiers — « ce qui approche la chose reçoit son jugement »',
    'aux héritiers le rendement du surcroît, ou la ratification du tout',
    'du mort insolvable comme du garant : le portage bienfaisant ne regarde ni la vie ni la solvabilité — sauf la richesse su puis apparue : retour de ce qui fut versé',
    'le différé liquide s’il est accélérable, et son contraire si le débiteur fut facilité ou ne le fut point dans le terme — le ḍamān encadre le temps de la dette dans les deux sens',
    'par ce dont il est solvable, ou ce dont il est insolvable — jamais les deux ensemble : la moitié solvable différerait un prêt attirant un profit',
    'dans une dette ferme ou s’abîmant vers elle — non dans un bien déterminé : dépôt, emprunt à usage, capital de muqāraḍa, société — dont seule la valeur se garantit, quand l’excès ou la négligence y est',
    'la promesse lie : « je fais crédit à un tel » oblige d’autant plus que le promis est entré en possession de ce qui fut promis — mais le retour reste ouvert avant la transaction, sauf le serment acheté : « jure, et je le garantis par cela »',
    'la quantité ignorée, le créancier ignoré, l’absence de permission du débiteur : trois ignorances qui n’affectent point la validité',
    'le paiement avec douceur lie, le paiement avec peine est rendu « comme son achat » — et c’est la science du vendeur qui attache le rendement, « lequel est le plus apparent »',
    'la fin du bien s’accomplit par la garantie : l’affection enracinée, la familiarité et le lien fortifiés — pourvu que celui qui se charge connaisse la gravité de ce qu’il porte et soit résolu à tenir les contrats',
    '<h2>Notes du traducteur</h2>',
    'l’étiquette GT « l’une des dispositions du garant et de la garantie » est ramenée au h1 imprimé « des jugements du garant et du garanti »',
    '(règle av — quatorzième tranchage du fil)',
    'VIDE pour la deuxième leçon consécutive (après 19495) — rendue telle quelle, sans date inventée',
    'La ligne de cours imprimée se confirme une douzième fois consécutive (6e → … → 17e)',
    'la coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa seizième occurrence',
    'le ḍamān rangé « parmi ce qu’Il a légiféré à Ses serviteurs » par la miséricorde et la subtilité divines',
    'le guillemet fermant du matn EST présent ici (contrairement à 19495) — l’assemblage n’a rien ajouté',
    'le jeu d’al-Fayyūmī (« je suis le garant ; et le garanti — je m’y suis engagé ») est rendu par la paire garant/garanti',
    'troisième citation du Manḥ al-Ğalīl au fil (6/191 au tour R314, 6/148 au R311)',
    'le commentaire du Mukhtaṣar par les hāšiya-mukhtaṣar rejoint la ligne de cours (Dardīr/Dasūqī) et le Tāğ wa-l-Iklīl d’al-Mawwāq (R312-R313)',
    'Sur la fente de verset A (dans la citation d’aṣ-Ṣāwī) : Yūsuf 12:72 — protocole triple',
    'AUCUN rendu établi au corpus → rendu de la main du traducteur d’après l’arabe vérifié',
    'la zaʿāma prouvée par le langage même des frères de Yūsuf',
    'Sur la fente de verset B (preuve du Livre) : Yūsuf 12:72 encore, avec Ibn ʿAbbās « le zaʿīm est le kafīl » — la même āya sert la langue (axe 1) et la légalité (axe 1, jugement)',
    'Sur la fente de verset C (l’instrement de l’insolvable) : Baqara 2:280 — rendu établi du corpus REPRIS À L’IDENTIQUE',
    '« À celui qui est dans la gêne, accordez un sursis jusqu’à ce qu’il soit dans l’aisance » — établi par 19407, même livre',
    'la ṣalawāt écrite en toutes lettres dans le document est rendue en toutes lettres (convention de la famille)',
    'la carte des quatre personnes de la ḥawāla (R314) retrouvée et renommée',
    'écho exact de la définition de la ḥawāla par Dardīr (R314 : « le transfert de la dette, d’une ḏimma à l’identique, vers une autre »)',
    'le bracket du document « Le Mukhtaṣar al-fiqhī 6/488 » est rendu tel quel',
    'l’arithmétique du tiers liant et du surcroît valide-sans-lier',
    'Abū Ḥanīfa et an-Nawawī contre la majorité',
    'la formule usuraire consignée, la sûreté (<em>tuwṯīqa</em>) par le garant « spécifique à la vente »',
    '« la considération est à l’état présent »',
    'la part solvable différée ferait du garant « un prêteur » — prêt attirant un profit',
    'l’usage marchand nommé par le document',
    'l’inexistant placé « à la station de l’existant »',
    'portée exacte laissée sans tranchement (règle ax)',
    'le rendement de l’achat avec peine attaché à la SCIENCE du vendeur, selon Ibn Yūnus',
    'le suivre (<em>ittibāʿ</em>) du démuni, la permission et son absence',
    'le travail demandé à l’élève (accord, désaccord, cause du désaccord) épouse exactement la découverte de l’axe deuxième (« le site du désaccord entre les imāms »)',
    'UNE phrase continue, sans items numérotés — « je lis le matn de la leçon à venir et je recherche les jugements du ḍamān de l’absent » — rendue telle quelle',
    'le prochain cours est le ḍamān de l’absent (19500) : le fil du bāb s’annonce',
    'le triple étage rendu tel quel, sans aplanissement',
]

missing = [p for p in PROBES if p not in html]
if missing:
    issues.append(f"sondes manquantes: {len(missing)}")
    for m in missing:
        issues.append("  ✗ " + m[:110])

if issues:
    print("ÉCHEC:")
    for i in issues:
        print(" -", i)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19496.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
