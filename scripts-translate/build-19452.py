#!/usr/bin/env python3
# build-19452.py — 19452 « Jurisprudence : les jugements de la conciliation
# de l'injuste et du tuteur du sang » (fiqh-tanawi-3, lessons[15], badge
# Leçon 17/33) — suite du bāb, treizième cours consécutif (… → 13e).
# Deux axes annoncés / TROIS développés (écart consigné). Axe 1 : jugement
# du ṣulḥ de l'injuste (ni pris ni laissé licites — entre lui et Dieu,
# dette occupée pour le lésé ; le jugement manifeste ne purifie point —
# Ibn Rushd Bidāya 4/244 + hadith Muslim « part de feu ») + huit questions
# de rupture (six : quatre iğmāʿan + deux mašhūr ; deux de non-rupture).
# Axe 2 : ṣulḥ pour l'épouse (laqab sans mafhūm ; qadr mūrithi-hā / moins
# — hiba aux cohéritiers, ḥiyāza avant mort / davantage — vente+ṣarf
# assemblés dans un dinar / hors succession — six conditions a-f).
# Axe 3 : ṣulḥ des sangs (ʿamd — moins ou plus DÉTERMINÉ, mubham vaut
# l'accidentel — Ibn Rushd ; ġarar — riṭl de mouton vivant, fruit non
# vendeur : talion levé, diya de l'intentionnel ; créancier muḥīṭ — veto,
# don vs nafaqa ; retour du muqawwam — ʿayb/istiḥqāq/šafʿa — nikāḥ/ḫulʿ)
# + maqāṣid. Matn du Le texte EXTRAIT (passages du sang cités en analyse
# seulement). Exploitation : Ibn ʿĀšir via al-ʿAlīš [Manḥ al-Ğalīl 6/148]
# — clause de l'acte, istiʾrāʾ/ibrāʾ. Préparation préalable → 19456.
# Fente liminaire VIDE ; at-taʿbīm 12e occurrence.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19452_{i}.html').read())
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
    'Jurisprudence : les jugements de la conciliation de l’injuste et du tuteur du sang',
    '<dt></dt>\n<dd></dd>',
    'le compilateur a montré les jugements de cela, avec leurs conditions',
    'Quel est le jugement de la conciliation de l’injuste ? Et quels sont les cas où la conciliation se rompt ?',
    'Et quel est le jugement de la conciliation de quelques héritiers avec l’épouse héritière ?',
    'treizième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    '(<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Définir les jugements de la conciliation de l’injuste.',
    '2. Saisir les conditions et les causes de la rupture du ṣulḥ.',
    '3. Se représenter ces jugements dans mes transactions.',
    '4. Montrer les jugements de la conciliation pour les sangs.',
    '<h2>Le texte</h2>',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    '« Et il n’est point licite pour l’injuste ; s’il reconnaît ensuite, ou qu’une preuve témoigne qu’il n’ignorait point',
    'ou qu’il fasse témoigner et déclare qu’il s’en tient, ou qu’il retrouve son acte ensuite — il lui est permis de le rompre',
    'comme celui qui ne déclare point, ou reconnaît en secret seulement — selon le plus beau (<em>al-aḥsan</em>)',
    'ton droit est établi, viens avec lui — puis il a concilié, puis l’a retrouvé',
    'Et pour l’héritage de l’épouse : des objets d’apparat, de l’argent, de l’or avec de l’or, de la succession',
    'à la mesure de ce dont son de cujus disposait ; moins, ou davantage, si les dirhams sont rares',
    'point d’autre chose en absolu, sauf par des objets d’apparat',
    'et pour des dirhams et des objets d’apparat laissés, avec de l’or : comme vente et change',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    'L’acte (<em>al-waṯīqa</em>) : un écrit documentaire qui a de l’importance',
    'L’acte (<em>aṣ-ṣakk</em>) : l’écrit que l’on rédige dans les transactions et les reconnaissances',
    'son pluriel est <em>ṣukūk</em>, <em>aṣukk</em> et <em>ṣikāk</em>',
    '<span>[al-Miṣbāḥ al-munīr fī ġarīb aš-Šarḥ al-kabīr, entrée ṣ-k-k]</span>',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du texte le jugement de la conciliation de l’injuste.',
    '2. J’extrais, à travers le texte, les cas de la rupture du ṣulḥ.',
    '3. J’indique, d’après le texte, le jugement de la conciliation de quelques héritiers avec l’épouse héritière.',
    '<h2>L’analyse</h2>',
    'Cette leçon comporte deux axes :',
    '<h3>Axe premier : le jugement du ṣulḥ de l’injuste et ce par quoi le ṣulḥ se rompt</h3>',
    '<h4>1. Le jugement du ṣulḥ de l’injuste</h4>',
    'La conciliation de l’injuste n’est point licite, que ce par quoi l’on concilie soit pris ou laissé',
    'si l’injuste est le demandeur, la chose prise lui est interdite',
    'si l’injuste est le défendeur, la chose laissée lui est interdite',
    'et cela, en ce qui est entre lui et Dieu',
    'sa dette (<em>ḏimma</em>) est même occupée pour le lésé (<em>al-maẓlūm</em>)',
    'quand bien même un juge jugerait pour lui un jugement dont il voit l’apparence',
    'le jugement a eu lieu dans ce dont l’apparence contredit l’intérieur',
    '« Ils se sont accordés sur ce que le jugement manifeste du juge auquel s’applique son propre jugement ne rend licite nul interdit, et n’interdit nul licite',
    '“Je ne suis qu’un être humain',
    'ce n’est qu’une part de feu que je lui découpe.',
    '<span>[Ṣaḥīḥ de Muslim, livre du jugement, chapitre du jugement selon l’apparence et l’argument]</span>',
    '<span>[Bidāyat al-muğtahid wa-nihāyat al-muqtaṣid 4/244]</span>',
    '<h4>2. Ce par quoi le ṣulḥ se rompt, et ce par quoi il ne se rompt point</h4>',
    'six où la rupture du ṣulḥ est admise pour le lésé, à l’unanimité ou sur le répandu (<em>al-mašhūr</em>)',
    '<span>La première :</span>',
    'il est comme celui qui a été vaincu (<em>al-mağlūb ʿalay-hi</em>)',
    '<span>La deuxième :</span>',
    'avec son serment qu’il n’en avait point connaissance',
    '<span>La troisième :</span>',
    's’est éloignée d’une distance qui n’est point grande',
    '<span>La quatrième :</span>',
    'la rupture lui est alors permise dans les quatre questions, à l’unanimité ; et la ratification (<em>al-imḍāʾ</em>) lui est permise',
    '<span>La cinquième :</span>',
    'comme celui qui a fait témoigner et déclaré',
    '<span>La sixième :</span>',
    'de crainte que le demandeur ne le réclame sur-le-champ, ou ne le retienne',
    'pour la force de l’affaire du ṣulḥ, et parce qu’il est comme celui qui l’a laissée au moment du ṣulḥ',
    'et parce que c’est une vente, ou un louage, ou une donation',
    'l’écrit qui témoigne pour lui de son droit',
    'car il n’a concilié avec lui que sur la remise de son droit',
    '<h3>Axe deuxième : les jugements du ṣulḥ pour l’épouse</h3>',
    'la contestation qui vient d’elle est plus fréquente, en ce qu’elle est la plus souvent une étrangère (<em>aǧnabiyya</em>) à la famille',
    'la désignation (<em>laqab</em>) — et la désignation n’a point d’entendement (<em>mafhūm</em>) chez les fondamentalistes (<em>al-uṣūlīyūn</em>)',
    'Qu’elle prenne la mesure de ce dont son de cujus disposait (<em>qadr mūrithi-hā</em>) de l’or',
    'de la substance même de la succession (<em>min ʿayn at-tarika</em>)',
    'cela n’est point admis. Et à cela le compilateur a fait allusion par sa parole : « à la mesure de ce dont son de cujus disposait »',
    'Ou qu’elle prenne moins que ce dont son de cujus disposait de l’or',
    'le reste étant donation (<em>hiba</em>) de sa part aux autres héritiers',
    's’ils en prennent possession (<em>ḥiyāza</em>) avant sa mort, la donation est valide',
    'les héritiers d’elle ont alors un droit de parole',
    'Qu’elle prenne davantage que son héritage de l’or',
    'de sorte que la vente et le change s’assemblent dans un dinar',
    'la vente et le change se sont assemblés dans un dinar',
    'Que la conciliation porte sur une chose qu’il lui donne de ce qui n’est point la succession',
    'si c’est en dinars ou en dirhams, cela n’est point admis en absolu',
    '<li>a. que l’héritier et l’épouse connaissent la totalité de la succession, afin que la conciliation porte sur du connu ;</li>',
    '<li>b. que la totalité de la succession soit présente ;</li>',
    '<li>c. que le débiteur reconnaisse ce qui lui incombe, quand il y a dans la succession une dette, fût-ce en objets d’apparat ;</li>',
    '<li>d. que le moment du ṣulḥ soit présent ;</li>',
    '<li>e. qu’il soit de ceux dont les jugements prennent prise ;</li>',
    '<li>f. que l’objet d’apparat qu’il lui donne en conciliation soit d’espèce différente de l’objet d’apparat qui est sur le débiteur (<em>al-ġarīm</em>)',
    '<h3>Axe troisième : le jugement du ṣulḥ pour les sangs</h3>',
    'Le ṣulḥ dans les sangs est sur deux visages',
    '<h4>1. Le ṣulḥ pour le sang de l’intentionnel</h4>',
    '<span>a. Ce par quoi le ṣulḥ pour le sang de l’intentionnel est admis :</span>',
    '« et pour l’intentionnel, avec ce qui est moindre et ce qui est nombreux »',
    'avec moins que la diya de l’accidentel, ou davantage, cela étant déterminé (<em>muʿayyan</em>) à l’instant du contrat du ṣulḥ',
    'car le sang de l’intentionnel n’a point de diya',
    'si son temps survient indéterminé (<em>mubham</em>), il se conclut et devient comme l’accidentel — dire d’Ibn Rushd',
    '<span>b. Ce par quoi le ṣulḥ pour l’intentionnel n’est point admis :</span>',
    '« nul risque (<em>ġarar</em>), comme le riṭl d’un mouton »',
    'comme un riṭl, ou des riṭls, de mouton, dont le propriétaire concilie avec cela un endetté, alors qu’il est vivant',
    'ou comme un fruit dont la salubrité de la vente n’est point apparue',
    'si le ṣulḥ a lieu sur le risque, le talion est levé, et l’on juge la diya de l’intentionnel',
    '« et pour le détenteur d’une dette : l’empêchement de cela »',
    'd’empêcher le débiteur blessant ou tuant de concilier sur le talion contre un bien',
    'car cela est une perte de son bien sur ce pour quoi ses créanciers n’ont point traité avec lui — comme son don',
    'car ceux-ci ont traité avec lui sur cela',
    'il est atteint par le défaut (<em>al-ʿayb</em>), la revendication (<em>al-istiḥqāq</em>) et la prise de la préemption (<em>al-akd bi-š-šafʿa</em>)',
    '« et si l’on rend un bien estimé (<em>muqawwam</em>) atteint d’un défaut, ou revendiqué, on retourne à sa valeur, comme le mariage et le <em>ḫulʿ</em> »',
    'le conciliant retourne contre le payeur à sa valeur, au jour du ṣulḥ, saine et entière',
    'l’épouse retourne dans le mariage à la valeur du bien estimé par lequel le mariage a eu lieu',
    'le mari retourne dans le <em>ḫulʿ</em> à la valeur du bien estimé par lequel le <em>ḫulʿ</em> a eu lieu',
    'Parmi les objectifs (<em>maqāṣid</em>) de cette leçon : l’appel à l’indulgence (<em>at-tasāmuḥ</em>) et à la conciliation',
    'et resserrer les voies du démon et de l’âme qui commande le mal',
    '<h2>Le contrôle</h2>',
    '1. J’indique le jugement du ṣulḥ pour l’injuste, et ses conditions.',
    '2. Je clarifie quand le ṣulḥ se rompt et quand il ne se rompt point, avec l’argumentation.',
    '3. J’indique le jugement de la conciliation de quelques héritiers entre eux au sujet de la succession, et ses conditions.',
    '4. Je mentionne les visages du ṣulḥ pour le sang de l’intentionnel.',
    '<h2>L’exploitation</h2>',
    'L’illustre Muḥammad al-ʿAlīš — que Dieu lui fasse miséricorde — a dit',
    '« L’imām Ibn ʿĀšir — que Dieu lui fasse miséricorde — a dit : …',
    'sa prise est nulle et son argument réfutable',
    'et que la preuve qui témoigne pour lui — l’empruntée (<em>al-mustaʾrāʾ</em>) ou autre — est forgée',
    'l’emprunt, ce qui se répète',
    'nulle preuve n’est alors entendue du demandeur après ce dégagement (<em>ibrāʾ</em>)',
    'et si cette clause tombe de l’acte, la prise sur une preuve qu’il n’a point connue lui est permise',
    '<span>[Manḥ al-Ğalīl, commentaire du Mukhtaṣar de Khalīl 6/148]</span>',
    '1. J’extrais du texte la preuve recevable dans l’attestation, et celle qui ne l’est point.',
    '2. J’explique les deux termes mentionnés dans le texte : l’emprunt (<em>al-istiʾrāʾ</em>) — le dégagement (<em>al-ibrāʾ</em>).',
    '<h2>La préparation préalable</h2>',
    '1. Les cas où le ṣulḥ est sur un sang de blessure intentionnelle.',
    '2. Le jugement de la conciliation dans la blessure au-dessous de la personne, et sur la blessure de la personne.',
    '3. Le jugement de la conciliation du malade avec celui qui l’a blessé volontairement.',
    '<h2>Le sens de cette leçon</h2>',
    'car le ṣulḥ peut être la robe du vol',
    'le jugement manifeste ne rend licite nul interdit, ni ne découpe au lésé autre chose qu’une part de feu',
    'jamais d’or du dehors — sauf objets d’apparat connus, présents, reconnus',
    'la conciliation est admise pour éteindre le différend, non pour fabriquer le droit',
    'le malade qui concilie celui qui l’a blessé volontairement',
    '<h2>Notes du traducteur</h2>',
    'l’étiquette GT du registre rend le titre par « Jurisprudence, arrêts sur la réconciliation avec l’oppresseur et le gardien du sang »',
    '(règle av — dixième tranchage du fil)',
    'VIDE au contrôle — deuxième fente vide consécutive (après 19449)',
    'la coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa douzième occurrence',
    'l’introduction de l’analyse annonce « deux axes »',
    'écart de compte consigné tel quel, sans rétro-révision',
    'les passages du sang',
    'le texte rendu est celui du document, non celui complet du Mukhtaṣar (règle ax)',
    'la formule « sur lui la prière et la paix » est rendue en toutes lettres',
    'nulle ligature ﷺ au document en ce passage',
    'deux mots pour l’écrit probatoire',
    'la désignation (<em>laqab</em>) mentionnée pour le compte n’a point d’entendement (<em>mafhūm</em>) chez les fondamentalistes',
    'L’arithmétique des exemples du commentaire est laissée à l’élève',
    'nul diya — le ṣulḥ s’y fait avec moins ou davantage que la diya de l’accidentel',
    'distinction fine entre le don et la nafaqa, rendue littéralement',
    'double parallèle explicite du document : le mariage dont le ṣadāq était ce vêtement ou cette part de demeure',
    '« l’emprunt, ce qui se répète » : formule elliptique du document, rendue littéralement sans tranchement',
    'le titre de la famille (6/83 au tour R308)',
    'l’emprunt (<em>al-istiʾrāʾ</em>) = le fait pour le demandeur de consulter d’avance la preuve d’autrui',
    'trois items annonçant la leçon à venir (doc 19456 : les jugements du ṣulḥ dans les sangs et les blessures)',
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

out = '/home/z/my-project/tr-tmp/19452.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
