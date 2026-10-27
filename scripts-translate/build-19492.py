#!/usr/bin/env python3
# build-19492.py — 19492 « Jurisprudence : les jugements du ṣulḥ de l'un de
# deux héritiers ou de deux associés » (fiqh-tanawi-3, lessons[17], badge
# Leçon 19/33) — suite du bāb, quinzième cours consécutif (… → 15e). TROIS
# axes h3 : (1) la conciliation de l'un de deux héritiers — l'entrée du
# copartageant « comme un droit pour eux deux », l'exception de l'aliment
# (Mudawwana, taraddud), les deux livres comme muqāsama, l'iʿdār pivot de
# l'empêchement, le muʿtamad de Dardīr/Dasūqī ; (2) le retour de l'un de
# deux associés — qui choisit le débiteur ne revient plus (muqāsama), les
# dix des cinquante (islām ou partage), renvoi à al-Bannānī et ʿAlīš ;
# (3) la chose consommée pour une chose différée (fasḫ dīn fī dīn, salaf
# ğarr nafʿ, sarf différé, aliment mesuré) et les deux muḍīḥas (la šufʿa
# coupe le šiqṣ : moitié de la valeur + diya de l'erreur = 50 dinars ;
# différend des blessures : ʿAbd al-Ḥakam moitié-moitié vs mesure aux
# deux diyas 500/1000/1500). Matn INTÉGRAL (un seul bloc). Exploitation :
# Ibn al-Qāsim [at-Tāğ wa-l-Iklīl, d'al-Mawwāq 7/20] — le šiqṣ réparti
# entre les deux muḍīḥas. 0 āya / 0 hadīth. Préparation préalable =
# reprise des questions mêmes de la leçon (règle ax). Fente liminaire NON
# VIDE (lundi 26 février 2024 — même date que 19456) ; at-taʿbīm 14e occ.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19492_{i}.html').read())
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
    'Jurisprudence : les jugements du ṣulḥ de l’un de deux héritiers ou de deux associés',
    '<dt></dt>\n<dd>Lundi 26 février 2024</dd>',
    'Tu as su auparavant que le ṣulḥ est de deux types : un ṣulḥ sur les biens, et un ṣulḥ sur les sangs',
    'une personne consomme pour un homme, par exemple, une chose parmi les biens meubles, l’aliment ou l’animal',
    'Quel est le jugement du ṣulḥ de l’un des héritiers, ou de l’un des associés ?',
    'Et quel est le jugement du ṣulḥ sur la chose consommée par la chose différée ?',
    'quinzième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    '(<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Définir le jugement de la conciliation de l’un de deux héritiers.',
    '2. Saisir les jugements de la conciliation de l’un de deux associés.',
    '3. Se représenter ces jugements dans les transactions.',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    'Et si l’un de deux fils héritiers concilie — fût-ce en déniant —, l’entrée appartient à son associé : comme un droit pour eux deux',
    'excepté l’aliment, au sujet duquel ils ont hésité',
    'et qu’il accomplisse l’iʿdār envers lui dans la sortie, ou [dans] la wakāla',
    'quand il n’y a rien autre que le requis',
    'ou que ce soit en deux livres',
    'et pour ce qui n’est pas à eux deux, quand il fut écrit dans un livre : deux sayings',
    'Et point de retour s’il choisit ce qui est sur le débiteur, quand même il périrait',
    'Et s’il concilie sur dix de ses cinquante : l’autre a le choix de les laisser, ou de prendre cinq de son associé, et de revenir avec quarante-cinq, et l’autre prend cinq',
    'cela ne vaut qu’en dirhams — de sa valeur, ou moins —, ou en or de même',
    'dès lors qu’il est de ce qui se vend avec [l’argent]',
    'et s’il concilie un šiqṣ pour deux muḍīḥas, l’intentionnelle et l’erreur : la préemption [se fait] pour la moitié de la valeur du šiqṣ et pour la diya de la muḍīḥa',
    'est-il de même si la blessure diffère ? Deux interprétations',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    '<em>Yašḫaṣu</em> : l’on dit : <em>šaḫaṣa yašḫaṣu</em>, du chapitre de <em>ʿilm</em> ou de <em>ḍarb</em>',
    '<em>Yuʿḏiru</em> : présent du quadrilittère <em>aʿḏara</em> — c’est-à-dire qu’il coupe l’excuse',
    'Le wakāla : établir un autre en lieu et place de soi-même, absolument ou avec restriction',
    'Le šiqṣ — avec la kasra du šīn muʿğam, le sukūn du qāf, et un ṣād non assimilée — : part d’un bien-fonds indivis',
    'La muḍīḥa — avec la ḍamma du mīm, la kasra du ḍād muʿğam, la fatḥa du ḥāʾ muḥmal et la tāʾ suscrite — : blessure qui a dénudé l’os',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du texte quand l’héritier entre dans la conciliation avec son associé, et quand il n’y entre pas.',
    '2. J’extrais du texte ce qui s’ensuit de la conciliation par le šiqṣ pour la muḍīḥa.',
    '<h2>L’analyse</h2>',
    'Cette leçon comprend les axes suivants :',
    '<h3>Axe premier : le jugement de la conciliation de l’un de deux héritiers</h3>',
    'un indivisaire (<em>ḫalīṭ</em>) de leur père',
    'revendique contre lui un bien de leur père, d’un commerce ou d’un dépôt',
    'que ce soit de l’or, de l’argent, ou des biens meubles',
    'en cas de reconnaissance, il lui est loisible de la laisser tout entière',
    's’il n’a point de preuve, il n’a sur son débiteur que le serment',
    'et les conciliants reviennent contre le débiteur de ce qu’il en a pris',
    'il fut excepté dans la Mudawwana, et ils ont hésité sur le sens de cette exception',
    'l’on a dit : excepté à la fin de la question',
    'car cela serait division de l’aliment, laquelle est une vente obligeant [la livraison] avant la prise',
    'Se trouver empêché de se joindre à son associé dans ce sur quoi il a concilié — et cela selon les figures suivantes',
    'devant le juge, ou devant une preuve présente',
    'Et le pivot est l’iʿdār, quand bien même il n’y aurait point de voyage',
    'son abstention du šuḫūṣ avec lui, et de la wakāla, est la preuve qu’il n’y est point entré avec lui',
    'et qu’il s’est contenté de suivre la ḏimma du débiteur absent',
    'car leur écriture commune en deux livres est comme la muqāsama',
    'et qu’ils l’aient pourtant vendu ensemble pour un prix unique, non pour deux prix',
    'selon que leur rassemblement dans un livre unique les rend communs, ou ne les rend point communs',
    'ad-Dasūqī a dit : « le retenu est que le pivot, au lieu du désaccord, est leur vente pour un prix unique dans un contrat unique',
    'alors même que le prix fut écrit dans un livre unique',
    '<h3>Axe deuxième : le retour de l’un de deux associés sur la conciliation de l’autre</h3>',
    'L’un de deux associés, face à l’autre, a deux états :',
    'car son choix de suivre le débiteur est comme la muqāsama, et nul retour après elle',
    'chacun des deux propos faisant ce que fait l’autre',
    'ce qui a précédé visait le cas où il n’y avait rien autre que le requis au moment de la sortie',
    'et la perte ici a eu lieu après le choix de suivre le débiteur',
    'ici, il préleva sans sa permission, puis confirma sa prise, et choisit de suivre le débiteur',
    'si deux associés ont cent sur un débiteur, et que l’un d’eux concilie sur dix à la place de ses cinquante',
    'a le choix de laisser les dix au conciliant (<em>islām</em> — le laisser)',
    'ou de prendre cinq de son associé conciliant, et de revenir contre le débiteur pour quarante-cinq, complet de ses cinquante',
    'et l’autre prend cinq du débiteur',
    'elle fut discutée dans ce qui se sait de la Hāšiya d’al-Bannānī et du Šarḥ d’ʿAlīš',
    '<h3>Axe troisième : le jugement de la conciliation sur une chose consommée et sur deux muḍīḥas</h3>',
    '<h4>1. La conciliation sur une chose consommée pour une chose différée</h4>',
    'car il a annulé une dette dans une dette',
    'la valeur devint due à la charge du consommateur sur-le-champ',
    'l’annulation d’une dette dans une dette ne se trouve empêchée que dans [une chose d’]autre genre, ou dans son genre avec davantage',
    'si le ṣulḥ évite cela, il vaut',
    'Et ici deux questions, que le compilateur a signalées par son propos',
    'car il l’a différé sur la valeur, ce qui est un bon prélèvement',
    'Si c’est davantage que la valeur, cela est empêché : car ce serait un prêt (<em>salaf</em>) attirant un profit',
    'que la valeur du consommé soit de ce qu’il est loisible de vendre pour l’argent de la conciliation, en dirhams ou en or',
    'empêché pour l’échange (<em>sarf</em>) différé',
    'le consommé serait un aliment mesuré, dont le semblable est dû',
    '<h4>2. La conciliation sur deux muḍīḥas, l’intentionnelle et l’erreur</h4>',
    'un auteur du sang concilie, sur la reconnaissance de la victime, un šiqṣ pour deux muḍīḥas, intentionnelle et d’erreur',
    'et le copartageant de la victime veut prendre la préemption',
    'la valeur du šiqṣ est de vingt — par exemple — : la préemption se fait pour la moitié de la valeur du šiqṣ, qui est dix',
    'en contrepartie de l’intentionnelle, car il n’y a point d’argent estimé en elle',
    'qui est la moitié du dixième de la diya entière : cinquante dinars',
    'comme une âme et une main — et c’est le propos de ʿAbd al-Ḥakam',
    'ou bien qu’à la différence des blessures, le šiqṣ soit mis à la mesure de leurs deux diyas',
    'car la diya de la main d’erreur est de cinq cents, et la diya de l’âme, si elle était d’erreur, de mille',
    'quand cinq cents sont rapportés à la somme de mille et cinq cents, ils font un tiers',
    'en contrepartie de l’âme intentionnelle, sont grevés les deux tiers de la valeur du šiqṣ',
    'pour la préemption sont pris la diya de l’âme, et le tiers de la valeur du šiqṣ',
    'l’encouragement du ṣulḥ entre tous les membres de la communauté',
    'qui ne recèle ni rancunes, ni ressentiment, ni haine',
    'et le resserrement des chemins de Satan et de l’âme qui commande le mal',
    '<h2>Le contrôle</h2>',
    '1. J’indique le jugement de la conciliation de l’un de deux héritiers sans l’autre.',
    '2. Je mentionne les jugements de la conciliation de l’un de deux associés.',
    '3. Je saisis le jugement du ṣulḥ sur une chose différée.',
    '4. Je clarifie le sens de « deux muḍīḥas, l’intentionnelle et l’erreur », et le jugement de la conciliation sur cela.',
    '<h2>L’exploitation</h2>',
    'Ibn al-Qāsim — que Dieu lui fasse miséricorde — a dit',
    'un šiqṣ d’une maison où il y a préemption : [la préemption se fait] pour la diya de la muḍīḥa d’erreur, et pour la moitié de la valeur du šiqṣ',
    'car nous avons réparti le šiqṣ entre les deux muḍīḥas, dont l’une porte une diya connue, et l’autre est inconnue',
    '[Le Tāğ wa-l-Iklīl, commentaire du Mukhtaṣar de Khalīl, d’al-Mawwāq 7/20]',
    'Je contemple ce texte avec soin, j’en extrais les jugements qu’il embrasse, et je le compare au texte du cheikh Khalīl.',
    '<h2>La préparation préalable</h2>',
    'Je lis le texte de la leçon à venir et j’y cherche :',
    '1. Quel est le jugement de la conciliation de l’un de deux héritiers ? Et quelles en sont les conditions ?',
    '2. Quel est le jugement de la conciliation de l’un de deux associés ?',
    '3. Quel est le jugement de celui qui a consommé une chose d’autrui, puis a concilié avec lui sur une chose différée ?',
    '<h2>Le sens de cette leçon</h2>',
    'Cette leçon fait entrer le ṣulḥ dans la maison',
    'l’entrée lui appartient « comme un droit pour eux deux », non comme une grâce du conciliant',
    'l’écriture en deux livres, qui divise le droit comme la muqāsama',
    'qui a été formellement mis en demeure s’est contenté de suivre la ḏimma du débiteur absent',
    'le choix ferme la porte du retour, comme la muqāsama',
    'les dix lui laissés, ou les cinq partagés, et le débiteur poursuivi pour quarante-cinq, complet des cinquante',
    'une dette ne s’annule point dans une dette',
    'davantage serait un prêt attirant un profit',
    'l’or consommé ne se remplace point par de l’argent différé, ni l’aliment mesuré par une chose différée — son semblable est dû',
    'la préemption coupe le šiqṣ en deux : la moitié de sa valeur pour l’intentionnelle, qui n’a point d’argent estimé',
    'cinq cents, tiers de mille cinq cents, pour la main d’erreur, et les deux tiers de la valeur pour l’âme intentionnelle',
    'le contrat de conciliation, jusqu’au bout, sait compter le connu et l’inconnu',
    '<h2>Notes du traducteur</h2>',
    '« réconciliation » est ramené à « conciliation » (terme de famille depuis 19448)',
    '(règle av — douzième tranchage du fil)',
    'NON VIDE — « Lundi 26 février 2024 »',
    'deux leçons consécutives du fil datées du même lundi',
    'la ligne de cours imprimée se confirme une dixième fois consécutive (6e → … → 15e)',
    'coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa quatorzième occurrence',
    'reprise des deux sections du ṣulḥ (biens / sangs) établies à 19449',
    'le texte de Khalīl se cite d’une traite, et ses ellipses sont portées par les crochets du traducteur',
    'la muḍīḥa s’ajoute à la famille des blessures (l’arš au tour R312)',
    'l’entrée du copartageant n’est point une grâce du conciliant, mais un droit commun aux deux parts',
    'l’écriture commune en deux livres est « comme la muqāsama » — nouveau terme de famille',
    'la formule est rendue littéralement, sans tranchement (règle ax)',
    'le pivot est l’iʿdār, quand bien même il n’y aurait point de voyage',
    'le retenu : la vente pour un prix unique dans un contrat unique',
    '<em>islām</em>, « le laisser » : l’abandon des dix au conciliant est la première des deux voies laissées au copartageant',
    'la distinction entre le ṣulḥ sur le déni et le ṣulḥ sur la reconnaissance est renvoyée par le document à la Hāšiya d’al-Bannānī et au Šarḥ d’ʿAlīš — renvoi rendu tel quel, sans développement (règle ax)',
    'davantage serait « un prêt (<em>salaf</em>) attirant un profit » — formule rendue littéralement',
    'l’or consommé contre de l’argent différé, ou le contraire : empêché pour l’échange (<em>sarf</em>) différé',
    'le document écrit « <em>ṯulṯā</em> » là où l’arithmétique commande un tiers (cinq cents sur la somme de mille cinq cents)',
    'rendu selon l’arithmétique, écart consigné (règle ax)',
    'troisième citation du commentaire au fil (7/13-17 au tour R312)',
    'le dire d’Ibn al-Qāsim épouse le partage moitié-moitié, pendant que Khalīl laisse le différend des blessures aux deux interprétations',
    'trois items qui reprennent'.replace('trois items qui reprennent', 'reprise de révision consignée telle quelle, sans tranchement sur sa portée (règle ax)'),
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

out = '/home/z/my-project/tr-tmp/19492.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
