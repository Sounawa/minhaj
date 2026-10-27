#!/usr/bin/env python3
# build-19456.py — 19456 « Jurisprudence : les jugements du ṣulḥ dans les
# sangs et les blessures » (fiqh-tanawi-3, lessons[16], badge Leçon 18/33)
# — suite du bāb, quatorzième cours consécutif (… → 14e). DEUX axes h3 :
# (1) la conciliation du groupe à propos du sang — chaque tueur conciliable
# / pardonné ; le coupé qui concilie puis meurt : retour au tuteur, qasāma
# (cinquante serments successifs) comme la diya dans l'erreur, le ṣulḥ
# découvre l'invisible (l'agression était sur une âme) ; diya entière
# après qasāma dans la blessure de l'erreur. (2) intitulé imprimé « à
# propos de l'épouse » SANS rapport avec son contenu (écart consigné, règle
# ax) : le malade qui concilie sa blessure en maladie (taʾwīlān, la seconde
# plus probable) ; l'un de deux tuteurs (l'autre entre par ğabr, ou diya de
# l'intentionnel) ; le muqirr de l'erreur — deux figures (lien absolu vs ce
# qu'il a versé ; règle du ḡalaṭ : rendu tant que subsiste, non ce qui a
# péri ; le vaincu mağlūb ʿalay-hi) + maqāṣid. Matn INTÉGRAL (un seul
# bloc). Exploitation : Mālik + Ibn al-Qāsim [at-Tāğ wa-l-Iklīl, d'al-Mawwāq
# 7/13-17] — nağğamū-hu (l'augure), règle du muqirr dédoublée. 0 āya /
# 0 hadīth (3e leçon sans citation). Préparation préalable → 19492.
# Fente liminaire NON VIDE (lundi 26 février 2024) ; at-taʿbīm 13e occurrence.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19456_{i}.html').read())
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
    'Jurisprudence : les jugements du ṣulḥ dans les sangs et les blessures',
    '<dt></dt>\n<dd>Lundi 26 février 2024</dd>',
    'il peut même s’y associer avec autrui',
    'Quel est le jugement de la conciliation à propos du sang de l’intentionnel ou de l’erreur ?',
    'Et quel est le jugement de la conciliation de l’un des deux tuteurs sans l’autre ?',
    'Et quel est le jugement de la conciliation du reconnaissant de l’homicide par erreur ?',
    'quatorzième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    '(<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Définir les jugements du ṣulḥ sur le sang de l’intentionnel et de l’erreur, et ses conditions.',
    '2. Saisir les jugements de la conciliation du malade lorsqu’une blessure intentionnelle d’une personne est établie contre lui.',
    '3. Examiner les jugements de la conciliation de l’un de deux tuteurs, et de la conciliation du reconnaissant d’un homicide par erreur.',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    'Et si un groupe tue, ou coupe, la conciliation de chacun est admise, et le pardon d’eux',
    'le retour appartient au tuteur, non à lui ; et la mise à mort se [fait] par la qasāma',
    'comme leur prise de la diya dans l’erreur',
    'Deux interprétations',
    'l’autre a l’entrée avec lui',
    'comme [dans] ta supposition : sa conciliation, et il [le] dément',
    's’il est établi, qu’il a ignoré son lien, qu’il a juré, et que l’on rend',
    'si l’on exige absolument, ou s’il l’exige et que l’on retrouve',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    '<em>Nuziya</em> : le sang de celui dont un membre fut coupé a coulé',
    'La qasāma — avec l’ouverture du qāf — : cinquante serments que les tuteurs du tué prêtent successivement',
    'l’arš est le nom du bien exigible pour la destruction de ce qui est au-dessous de l’âme',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du texte le jugement du groupe lorsqu’elle tue une personne ou en coupe un membre.',
    '2. J’indique, à travers le texte, les conditions du jugement précédent.',
    '3. J’extrais du texte le jugement du malade s’il est blessé, puis concilie, puis meurt.',
    '4. J’indique le jugement de la conciliation de l’un des deux tuteurs et du reconnaissant de l’erreur.',
    '<h2>L’analyse</h2>',
    'Cette leçon comprend les axes suivants :',
    '<h3>Axe premier : la conciliation du groupe à propos du sang</h3>',
    'les propos du compilateur embrassent les figures suivantes',
    'il est admis à celui sur qui l’on a commis le crime, ou à son tuteur, de concilier chacun des membres du groupe des tueurs ou des coupeurs, et il lui est admis de pardonner à chacun',
    'au tuteur du mort de trancher, non au coupeur : deux figures',
    '<span>La première :</span> le retour du bien concilié au coupeur ou au blessant',
    'la mise à mort du coupeur par la qasāma, en ce qu’il est mort de cette blessure',
    'elle a découvert l’invisible : que l’agression portait sur une âme',
    'en raison de la souplesse de la mort par rapport à la blessure',
    'il leur est loisible d’être contents de ce avec quoi le coupé a concilié',
    'les tuteurs du blessé peuvent prendre la diya entière après la qasāma',
    '<h3>Axe deuxième : les jugements du ṣulḥ à propos de l’épouse</h3>',
    '<h4>1. La conciliation du malade</h4>',
    'cette conciliation est admise dès le départ et devient contraignante une fois conclue',
    'la plus probable des deux est la seconde',
    '<h4>2. La conciliation de l’un de deux tuteurs</h4>',
    'd’entrer avec lui par voie de contrainte (<em>ğabr</em>) dans ce qu’il a concilié',
    'en prenant sa part du tueur, et la mise à mort tombe',
    'de poursuivre le tueur pour sa part de la diya de l’intentionnel',
    '<h4>3. La conciliation du reconnaissant de l’homicide par erreur</h4>',
    'les propos du compilateur ont embrassé deux figures',
    'sur la base que la ʿāqila ne supporte point la reconnaissance — qui est le répandu',
    'le reste à la charge de la ʿāqila par la qasāma des tuteurs du tué',
    'car de la faiblesse du fondement ne suit point la faiblesse de ce qui y est bâti',
    'il jure qu’il n’a concilié que sur sa croyance que la diya lui était contraignante',
    'pour son volontariat à l’accélérer, et son ignorance n’y est point excuse',
    'il est comme le vaincu (<em>mağlūb ʿalay-hi</em>) dans le ṣulḥ',
    'cela est comme celui qui récompense une aumône, croyant la récompense contraignante',
    'les questions de l’erreur — l’on y rend ce dont l’erreur avait frappé le lien, tant qu’il subsiste — non ce qui a péri',
    'la solidarité sociale entre les membres d’une même famille',
    'le souci de la sacralité des sangs et leur préservation de couler sans droit ou de devenir pure perte',
    'la fin des droits entre les créatures tout entières',
    '<h2>Le contrôle</h2>',
    '1. J’indique le jugement de la conciliation du groupe lorsqu’elle a partagé le meurtre ou la coupure.',
    '2. Je clarifie le sens de la qasāma et ce qui en découle.',
    '3. Je mentionne le jugement de la conciliation d’un malade blessé intentionnellement.',
    '4. Je détermine les figures de la conciliation du reconnaissant de l’homicide par erreur.',
    '<h2>L’exploitation</h2>',
    'Mālik — que Dieu lui fasse miséricorde — a dit',
    'sur un bien qu’ils ont auguré pour lui, et qu’il leur verse l’augure',
    'Je croyais la diya contraignante pour moi, non pour la ʿāqila',
    'cela est à lui, on le lui rend, et les tuteurs du tué poursuivent la ʿāqila',
    'Ibn al-Qāsim a dit',
    'Si un groupe coupe la main d’un homme ou le blesse intentionnellement',
    'de concilier l’un d’eux, et de pardonner à qui il veut d’entre eux, et de faire le talion de qui il veut',
    '[Le Tāğ wa-l-Iklīl, commentaire du Mukhtaṣar de Khalīl, d’al-Mawwāq 7/13-17]',
    'Je lis ce texte et j’en accomplis ce qui suit :',
    '1. J’explique ce qui est souligné dans le texte.',
    '2. Je compare le texte de l’imām Mālik au texte du cheikh Khalīl.',
    '3. Je rédige une page qui fait connaître l’imām al-Mawwāq et son livre : le Tāğ wa-l-Iklīl.',
    '<h2>La préparation préalable</h2>',
    '1. Quel est le jugement de la conciliation de l’un de deux héritiers ? Et quelles en sont les conditions ?',
    '2. Quel est le jugement de la conciliation de l’un de deux associés ?',
    '3. Quel est le jugement de celui qui a consommé une chose d’autrui, puis a concilié avec lui sur une chose différée ?',
    '<h2>Le sens de cette leçon</h2>',
    'Cette leçon fait rencontrer la conciliation et le sang',
    'le crime collectif n’abolit pas la paix individuelle',
    'le ṣulḥ découvre l’invisible : l’agression était sur une âme',
    'cinquante serments successifs, comme la diya se prend dans l’erreur',
    'le sang ne se transporte point par supposition',
    'le pardon de l’un lie le groupe des héritiers',
    'l’on rend ce dont l’erreur avait frappé le lien tant qu’il subsiste, non ce qui a péri',
    'la famille qui porte le sang de son sang, solidarité sociale rendue visible',
    'La leçon à venir fera entrer le ṣulḥ dans la maison',
    '<h2>Notes du traducteur</h2>',
    '« réconciliation » est ramené à « conciliation » (terme de famille depuis 19448)',
    '(règle av — onzième tranchage du fil)',
    'NON VIDE — « Lundi 26 février 2024 »',
    'après les deux fentes vides de 19449 et 19452',
    'la ligne de cours imprimée se confirme une neuvième fois consécutive (6e → … → 14e)',
    'coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa treizième occurrence',
    'l’intitulé est rendu à la lettre et l’écart consigné, sans rétro-révision (règle ax)',
    'l’arš n’avait pas encore été nommé au fil — il s’ajoute à la famille de la diya',
    'la formule de Khalīl revient trois fois dans ce matn',
    '« les questions de l’erreur : l’on y rend ce dont l’erreur avait frappé le lien, tant qu’il subsiste — non ce qui a péri »',
    'rendue littéralement, sans tranchement sur son ellipsis (règle ax)',
    'reprise directe du terme de famille (19452 : le lésé comme vaincu, <em>mağlūb ʿalay-hi</em>, dans la preuve)',
    'ici le vaincu est le tueur lui-même : la contrainte supposée du sang retourne en sa faveur',
    'cinquante serments dans le sang équivalent à la prise de la diya dans l’erreur',
    'l’augure (<em>nağm</em>) désigne ici la fixation du montant par les tuteurs',
    'même règle que la seconde figure du muqirr — l’exploitation dédouble le cœur de la leçon',
    'second grand commentaire du Mukhtaṣar nommé au fil, après le Manḥ al-Ğalīl d’Ibn ʿĀšir (6/148 au tour R311)',
    'trois items annonçant la leçon à venir (doc 19492 : les jugements du ṣulḥ de l’un de deux héritiers ou associés)',
    'continuité du fil consignée telle quelle (règle ax)',
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

out = '/home/z/my-project/tr-tmp/19456.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
