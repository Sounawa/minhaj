#!/usr/bin/env python3
# build-19515.py — 19515 « Jurisprudence : les types du ḍamān et leurs
# jugements » (fiqh-tanawi-3, lessons[22], badge Leçon 24/33) — suite du
# bāb, vingtième cours consécutif (6e → … → 21e imprimé). DEUX axes h3 :
# (1) les jugements du ḍamān de la face (wağh = la personne, métonymie ;
# le ḍamān de l'épouse — rejet par le mari, le tiers de sa fortune ;
# l'acquittement par la remise — prison, personne remise sur ordre,
# hors du siège du jugement, hors du pays si juge fût-il démuni ;
# le ġurm après léger blâme si l'absence approche comme un jour ; le
# recours du garant amendé contre le débiteur — mort dans l'absence ou
# démuni à l'échéance) ; (2) le ḍamān de la recherche (valide même en
# qiṣāṣ — ḥudūd et taʿzīrāt, droits corporels ; la formule : porteur de
# sa recherche, instrement de la négation de l'argent, Dardīr : lire au
# passé, la ville et ses environs, jurer quand il a manqué — dallāsa,
# mustaqarr ; le ġurm du garant — négligence spéciale ou fuite, la peine
# ne se joignant point au ġurm, le naql ; le différend garant/réclamant
# — parole au garant par serment, ʿimāra sur la ḏimma, ġins et qadr,
# Zayd ; les trois questions du wakīl et du kafīl — pas de wakīl de la
# contestation, pas de garant de la face sauf avec un témoin, la
# rétention par le qāḍī, mulāzama sans prison ; la Sharīʿa sage et la
# bonne intercession). Matn INTÉGRAL (un bloc). Exploitation : Ibn Rušd
# [al-Bayān wa-t-Taḥṣīl 11/373] — le porteur de la face seulement, le
# porté disparu, le muḥīl ajoutant terme après terme, Ibn al-Qāsim par
# Mālik. 0 āya / 0 hadīth (troisième tour consécutif sans protocole
# triple). Fente liminaire VIDE (5e conséc.) ; at-taʿbīm 19e occ. ;
# المقترض rendu au sens. Préparation préalable → la šarika (écart de
# séquence consigné : le cours suivant du livre est la pluralité des
# porteurs, 19517).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19515_{i}.html').read())
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
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

probes = [
    "Jurisprudence : les types du ḍamān et leurs jugements",
    "L'homme est nécessiteux, par le fait du besoin pressant qui le jette à l'emprunt",
    "Il lui arrive de solliciter un prêt, et celui qui le prête exige de lui qu'il amène une personne connue qui le garantisse",
    "Lorsque l'homme vint à lui avec un porteur (<em>ḥāmil</em>)",
    "je veux prêter, de cet argent, telle et telle somme, et je ne connais point celui qui l'emportera",
    "le garantiras-tu, et viendras-tu avec lui au moment du besoin de lui ?",
    "Oui, je le garantis, et je m'engage à l'amener au moment du besoin de lui",
    "le garant et le garanti peuvent entrer en dispute (<em>tanāzuʿ</em>)",
    "il s'ensuit de cela des effets (<em>āṯār</em>)",
    "Comment nomme-t-on ce ḍamān ? Et quel est son jugement ?",
    "Et quels sont les effets de la dispute entre le garant et le garanti ?",
    "vingt-et-unième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître les jugements du ḍamān de la face",
    "Saisir les jugements du garant et du garanti",
    "Se représenter la gravité du ḍamān sur le garant et le garanti",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Et il est valide par la face (<em>al-wağh</em>)",
    "et au mari le rejet de lui, venu de son épouse",
    "et il est quitte par la remise de lui à lui — fût-ce en prison —",
    "ou par la remise que fait de sa propre personne [le garanti], si [le garant] l'en ordonne, quand le droit est échu",
    "et hors du siège du jugement (<em>maǧlis al-ḥukm</em>), si cela n'a point été instrent",
    "et hors de son pays, s'il s'y trouve un juge, fût-il démuni (<em>ʿadīm</em>)",
    "sinon, il est amendé après un léger blâme, si l'absence de son ġarīm approche : comme un jour",
    "Et le ġurm ne tombe point par le fait de l'amener si la sentence en a été rendue",
    "si est établie son absence, ou sa mort dans son absence, fût-ce hors de son pays — et il recourt par lui",
    "Et [il est valide] par la recherche (<em>aṭ-ṭalab</em>), quand bien même en qiṣāṣ",
    "comme : « je suis porteur de sa recherche »",
    "ou qu'il ait instrent la négation de l'argent",
    "ou qu'il ait dit : « je ne garantis que sa face »",
    "et qu'il le recherche avec ce sur quoi l'on peut se porter, et qu'il jure quand il a manqué",
    "et il est amendé s'il a négligé ou l'a fait fuir, et il est châtié",
    "Et le portage s'impose dans toute formule",
    "« le zaʿīm », « l'aḏīn », « le qabīl », « il est chez moi », « il m'incombe »",
    "pour l'argent — sur le préféré et le manifeste, sauf s'ils diffèrent",
    "Et n'est point dû, pour la contestation, un wakīl, ni, par la prétention, un garant de la face — sauf avec un témoin",
    "et s'il allègue une preuve telle qu'une au souk, le qāḍī le retient auprès de lui",
    "La compréhension",
    "Le commentaire",
    "La face (<em>al-wağh</em>) : la personne même (<em>aḏ-ḏāt</em>)",
    "une métonymie (<em>maǧāz mursal</em>) : on énonce la partie en visant le tout",
    "Démuni (<em>ʿadīm</em>) : qui n'a point de biens",
    "La recherche (<em>aṭ-ṭalab</em>) : la quête et la fouille",
    "Le zaʿīm : de la zaʿāma — la maîtrise (<em>as-siyāda</em>) en langue",
    "L'aḏīn : de l'iḏn — l'information —, ou de l'iḏāna au sens de l'offre (<em>al-iǧāb</em>)",
    "Et le qabīl : de la qabāla — la garde",
    "le reçu (<em>aṣ-ṣakk</em>) se nomme qabāl : il garde le droit",
    "La synthèse du contenu du texte",
    "Je tire du texte les types du ḍamān",
    "J'établis du texte le jugement de chaque type du ḍamān",
    "Je précise, à partir du texte, les jugements de la dispute entre le garant et le garanti",
    "L'analyse",
    "Ce cours comprend les axes suivants",
    "Axe premier : les jugements du ḍamān de la face",
    "1. Sa définition",
    "Le ḍamān de la face (<em>ḍamān al-wağh</em>) : l'engagement du garant d'amener le ġarīm — celui qui porte la dette — au moment du besoin de lui",
    "2. Son jugement",
    "Le ḍamān est valide par la personne (<em>aḏ-ḏāt</em>), c'est-à-dire en l'amenant elle-même au détenteur de la dette au moment du besoin",
    "le ḍamān de la face n'est valide que là où le garanti porte une dette — non dans le qiṣāṣ et leurs pareils, comme le ḥadd et la peine corrective",
    "c'est pourquoi le compilateur l'a omis ici, pour le mentionner dans le ḍamān de la recherche",
    "3. Le ḍamān de l'épouse par la face",
    "Au mari de rejeter le ḍamān de la face s'il émane de son épouse",
    "quand bien même la dette de celle dont elle a garanti la face n'atteindrait pas le tiers de sa fortune",
    "elle serait peut-être emprisonnée si elle se révélait impuissante à amener la débitrice, ou sortirait pour la contestation",
    "et cela est pour moi une tache (<em>maʿrā</em>)",
    "l'établissement de la cause mentionné (<em>taʿlīl</em>) est manifeste dans son ḍamān pour autrui",
    "et le pareil de son ḍamān de la face est le ḍamān de la recherche — au mari le rejet de lui",
    "quant à son ḍamān pour l'argent, il est déjà passé (<em>marra</em>)",
    "4. L'acquittement du garant par la face",
    "Le garant de la face est quitte, quand le droit est échu à la charge du garanti",
    "en remettant le garanti à celui pour qui il est garanti",
    "en un lieu où le détenteur de la dette est capable de le dégager du débiteur",
    "ou par la remise que le garanti fait de sa propre personne au créancier, si le garant lui en donne l'ordre",
    "ou en remettant le garanti hors du siège du jugement, si l'amener en celui-ci n'a point été instrent",
    "ou en le remettant hors du pays du ḍamān, s'il s'y trouve un juge",
    "5. Le recours du garant contre le débiteur",
    "Le garant sur qui la sentence du ġurm a été rendue recourt — pour le ġurm — par ce qu'il a versé au détenteur du droit",
    "s'il établit que le ġarīm est mort dans son absence avant la sentence, ou s'est trouvé démuni à l'échéance de la dette",
    "Axe deuxième : le ḍamān de la recherche",
    "Le ḍamān de la recherche (<em>ḍamān aṭ-ṭalab</em>) : l'engagement de rechercher le ġarīm et de le quêter, sans l'amener",
    "Le ḍamān est valide par la recherche, quand bien même son ḍamān porterait sur le qiṣāṣ",
    "parmi les droits corporels (<em>ḥuqūq badaniyya</em>) — des ḥudūd et des peines correctives (<em>taʿzīrāt</em>)",
    "3. Sa formule",
    "elle est tantôt à la lettre de son lexème, tantôt à la formule du ḍamān de la face avec l'instrement de la négation de l'argent",
    "ou : « je le recherche », ou : « je ne garantis que la recherche », ou : « je suis requis de sa recherche », et leurs pareilles",
    "c'est-à-dire à la lettre : « je garantis sa face, et rien de l'argent n'est sur moi »",
    "Ad-Dardīr a dit : il convient de lire — c'est-à-dire le dire du compilateur : « et qu'il le recherche » — à la formule du passé, pour signifier l'obligation de la recherche",
    "qu'il ignore son lieu ou le connaisse : il le recherche dans la ville et ce qui en est proche",
    "dans sa recherche, sans subornation (<em>dallāsa</em>), et sans que lui soit connu de séjour stable (<em>mustaqarr</em>) : il n'est point amendé alors",
    "4. L'amende du garant de la face",
    "Le garant est amendé s'il a négligé une négligence spéciale",
    "en le trouvant puis le laissant là où le détenteur du droit ne peut le prendre de lui",
    "ou en le faisant fuir, de sorte que le détenteur du droit ne peut prendre son droit de lui",
    "Et il est châtié, sans ġurm, dans une autre espèce de négligence",
    "le ġarīm étant établi pour lui dans une ville précise",
    "ainsi que le naql le transmet, il en ressort que la peine (<em>al-ʿuqba</em>) ne se joint point au ġurm, puisque celle-ci est elle-même une peine",
    "5. Le différend du garant et du réclamant alléguant l'argent",
    "Ad-Dasūqī a dit : c'est un échappement hors de l'estimé",
    "dans l'instrement ou l'intention — ; il n'y est point alors tenu",
    "je n'ai instrent que le ḍamān de la face, ou je l'ai voulu",
    "la parole est au garant, par serment",
    "le réclamant allègue une charge dressée sur la ḏimma — dont l'origine est l'innocence",
    "le cas où ils diffèrent sur le genre (<em>ğins</em>) du garanti et sa quantité (<em>qadr</em>)",
    "le cas où ils diffèrent sur le ḍamān et son absence",
    "comme le dire d'un homme : « je suis garant de Zayd », et que Zayd dise : « il n'est pas garant de moi » : la parole est au garant, non au dire de Zayd",
    "a visé les questions du wakīl et du kafīl, qui sont :",
    "le réclamant prétendant une preuve absente et demandant au défendeur d'établir un wakīl qui le contredise en son nom",
    "car il craint de ne point le trouver au moment d'amener sa preuve",
    "car il appartient au qāḍī d'entendre la preuve en l'absence du requis",
    "quand bien même le demandeur aurait établi un témoin de la vérité sans jurer avec lui — et cela est manifeste",
    "et rien n'est dû au défendeur dénieur d'un garant de la face — c'est-à-dire qu'on lui garantisse sa face — jusqu'à ce que le demandeur amène sa preuve",
    "par le fait de la seule allégation (<em>muǧarrad ad-daʿwā</em>) — sauf par le témoignage d'un seul témoin",
    "alors le garant de la face devient dû, la prétention se renforçant par le témoin",
    "et si le réclamant prétend une preuve présente au souk, ou de certaines tribus",
    "le qāḍī retient auprès de lui — c'est-à-dire : le requis, dénieur de la prétention du demandeur",
    "quand bien même le lien (<em>al-ḫilṭa</em>) ne s'établirait point",
    "et députe à son sujet qui le garde en compagnie (<em>mulāzama</em>), sans le jeter en prison",
    "s'il vient avec une preuve, il en tire la sentence ; sinon, il relâche le défendeur",
    "La Sharīʿa sage a incité à ouvrir la voie aux gens des intentions bonnes et des buts nobles",
    "ceux qui veulent secourir le nécessiteux, relever l'abattu, remplir les besoins d'autrui en quête de l'agrément de Dieu",
    "a fait désirer la bonne intercession (<em>šafāʿa ḥasana</em>) en faveur de qui reste inactif, sans renom auprès de qui emprunte chez lui",
    "Le contrôle",
    "Je connais le ḍamān de la face et le ḍamān de la recherche, et j'établis leur jugement",
    "Je dis quand le garant est amendé et quand il est quitte",
    "J'établis les jugements de la dispute entre le garant et le réclamant",
    "L'exploitation",
    "L'illustre Ibn Rušd — que Dieu lui fasse miséricorde — a dit",
    "un homme qui se porte porteur de la face d'un homme, avec instrement contre lui qu'il n'est tenu que de la face",
    "qu'il ne réponde pas d'argent si la dette vient à échoir sur lui — il n'est tenu que de la face : je le recherche là où il se trouve",
    "Le porté (<em>al-maḥmūl</em>) disparaît de lui, et le muḥīl ajoute terme après terme, sans qu'il l'amène",
    "Ibn al-Qāsim a dit : Mālik a dit : il n'est tenu que de la face, jamais — quand bien même il ajouterait de nombreux termes",
    "et l'instrement du portage (<em>aš-šarṭ bil-ḥimāla</em>) est licite",
    "[al-Bayān wa-t-Taḥṣīl 11/373]",
    "J'examine ce texte avec soin et j'en extrais les questions qu'il contient",
    "La préparation préalable",
    "Je lis le matn du cours suivant et j'accomplis ce qui suit",
    "Je détermine par le matn le concept de la šarika (la société)",
    "J'établis le jugement de la šarika et ses conditions",
    "Je mets en relief les jugements de la šarika et ses effets",
    "Je cherche dans la Mudawwana du commerce marocaine ce qui suit",
    "les types des sociétés",
    "les deux règles de la liberté de la preuve et de la présomption de la solidarité",
    "le bāb du ḍamān se poursuivant",
    "Notes du traducteur",
    "règle av — dix-septième tranchage du fil",
    "VIDE pour la cinquième leçon consécutive",
    "la coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa dix-neuvième occurrence",
    "le lexème imprimé <em>al-muqtariḍ</em> (l'emprunteur) ne concorde pas avec la scène",
    "le « garant de la face » (<em>ḍāmin al-wağh</em>) établi à la leçon précédente",
    "distinct du « requis » (<em>iqtidāʾ</em>) de la leçon précédente",
    "la lecture de Dardīr est suivie, les prononces du matn étant laissés à leur densité",
    "le lexème <em>al-ʿimāra</em> (l'habitation) est pris au sens d'une imputation sur la ḏimma",
    "le lexème de la <em>ḥawāla</em> (le transitaire) ; le référent paraissant être celui en faveur de qui le portage opère — laissé sans tranchement",
    "elle annonce la šarika (la société) et la Mudawwana du commerce marocaine, alors que le cours suivant du livre est la pluralité des porteurs (19517)",
    "la clausule morale de la Sharīʿa sage est rendue telle quelle, à l'intérieur du dernier item, comme dans l'imprimé",
]

missing = [p.replace("'", chr(0x2019)) for p in probes if p.replace("'", chr(0x2019)) not in html]
if missing:
    issues.append(f"SONDES ABSENTES ({len(missing)}): " + " || ".join(missing[:6]))

if issues:
    print("BUILD ÉCHOUÉ :")
    for i in issues:
        print("  -", i[:500])
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19515.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"BUILD OK : {len(html)} caractères, {len(probes)} sondes OK, guillemets {html.count('«')}/{html.count('»')}")
