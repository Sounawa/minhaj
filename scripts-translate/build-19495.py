#!/usr/bin/env python3
# build-19495.py — 19495 « Jurisprudence : les jugements de la ḥawāla »
# (fiqh-tanawi-3, lessons[18], badge Leçon 20/33) — suite du bāb, seizième
# cours consécutif (6e → … → 16e). TROIS axes h3 : (1) la définition de la
# ḥawāla (langue/terminologie — Dardīr « le transfert de la dette, d'une
# ḏimma à l'identique, vers une autre » + Dasūqī sur « à l'identique »),
# son jugement (contrat jāʾiz ; ruḫṣa exceptée de la vente de la dette par
# la dette — Dasūqī 3/325, Qāḍī ʿIyāḍ ; al-Bāğī al-Muntaqā 5/66, hadīth du
# Muwaṭṭaʾ « renvoyé vers un homme rempli » — « du chapitre du liquide »),
# ses cinq piliers (muḥīl/muḥāl/muḥāl ʿalay-hi/muḥāl bi-hi/ṣīġa) ;
# (2) les conditions — contentement du muḥīl et du muḥāl seul (sauf
# inimitié antérieure), dette ferme (garde mineur/safīh), dévolution (non
# peuplement d'une ḏimma d'une ḏimma — sauf liquide saisi avant séparation,
# comme le ṣarf), égalité en quantité et qualité (az-Zurqānī 6/34 : cinq
# sur dix se transfèrent ; ʿAlīš Manḥ al-Ğalīl 6/191 : licéité tenue par la
# plupart des maîtres), non-aliment issu d'une vente (ṭaʿām min bayʿ) ;
# (3) les jugements — validité et absence de retour (non-révélation de la
# ḏimma ; faillite su du muḥāl ʿalay-hi seul → muḥīl trompé ; serment sur
# la négation de la science) ; la vente rendue pour vice (Ibn al-Qāsim :
# non-dissolution « car cela est connu » vs Ašhab/Ibn al-Mawwāz : dissolution,
# majorité) ; le litige (parole au muḥīl sur la dette, non dans la wakāla
# ou le salaf ; ġayba inqiṭāʿ ; parole au saisisseur ou au seigneur du bien)
# ; fawā'id (mise à l'abri des biens, fin des droits et fin du bien).
# Matn INTÉGRAL (un seul bloc). Exploitation : Ibn ʿAbd al-Barr [Le Kāfī
# dans la jurisprudence des gens de Médine 2/797] — « la ḥawāla est le
# transfert des ḏimmas ». 0 āya / 1 hadīth (Muwaṭṭaʾ, via al-Bāğī).
# Préparation préalable → ḍamān (deux items). Fente liminaire VIDE ;
# at-taʿbīm 15e occ. ; guillemet fermant du matn absent du document — ajouté.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19495_{i}.html').read())
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
    'Jurisprudence : les jugements de la ḥawāla',
    '<dt></dt>\n<dd></dd>',
    'Lorsque l’auteur eut achevé le discours sur les questions de la conciliation, la ḥawāla lui ressemblait',
    'la conciliation, en effet, déplace la chose réconciliée de la créance réclamée vers sa contrepartie',
    'comme la ḥawāla déplace le transféré de la demande de sa créance vers la créance de son créancier',
    'il la fit donc suivre [à la conciliation], et mentionna ses conditions et ses jugements',
    'Qu’est-ce que la ḥawāla ? Et quels sont ses piliers et ses conditions ? Et quels sont ses jugements ?',
    '— Livre de jurisprudence, du Mukhtaṣar du cheikh Khalīl, avec le Šarḥ d’ad-Dardīr et la Hāšiya d’ad-Dasūqī — seizième leçon, au profit des élèves et des élèves de la troisième année secondaire de l’ancien enseignement (<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Connaître le concept de la ḥawāla et ses piliers.',
    '2. Saisir les jugements de la ḥawāla et ses conditions.',
    '3. Se représenter les jugements de la ḥawāla dans mes transactions financières.',
    '<h2>Le texte</h2>',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    'La condition de la ḥawāla est le contentement du muḥīl et du muḥāl seulement, et l’établissement d’une dette ferme',
    's’il l’informait de son absence [de dette], et qu’il conditionnât la garantie contre les vices (<em>barāʾa</em>), cela vaut',
    'et [l’étend-elle à] ce qu’il fût déclaré en faillite ou qu’il mourût ? Deux interprétations.',
    'et la dévolution du muḥāl bi-hi [par elle], fût-ce par écriture, non sur lui',
    'et l’égalité des deux dettes en quantité et en qualité',
    'et sur son transfert vers l’inférieur, hésitation',
    'et que les deux ne soient pas un aliment issu d’une vente',
    'Non pas la révélation de sa ḏimma, celle du muḥāl ʿalay-hi',
    'et le droit du muḥāl se transfère sur le muḥāl ʿalay-hi quand bien même il serait en faillite ou dénierait',
    'excepté que le muḥīl sache de sa faillite seulement — et il jure sa négation, si l’on soupçonne de lui la science',
    'Si un vendeur transférait sur un acheteur pour le prix, puis [le bien] était rendu pour un vice, ou que l’option eût été usée, la ḥawāla ne se dissout pas — et son contraire a été choisi',
    'Et la parole est au muḥīl si l’on réclamait contre lui la négation de la dette pour le muḥāl ʿalay-hi — non dans sa revendication de wakāla ou de salaf',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    'La ḥawāla : le transfert de la dette d’une ḏimma à une autre.<br>\nLa barāʾa : la garantie contre les vices.<br>\n<em>Yufallas</em> : le juge prononce contre lui le décret de faillite (<em>fals</em>).<br>\nLa ḏimma — avec la kasra du ḏāl — : un trait de l’homme qui accepte l’obligation et l’engagement.<br>\nLa wakāla : <em>wakkala-hu tawkīlan</em>, et le nom est <em>al-wakāla</em>, lu aussi à la kasra — : l’établir en sa place pour l’accomplissement de son affaire.',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du texte les conditions de la ḥawāla.',
    '2. Je détermine, à travers le texte, les piliers de la ḥawāla.',
    '3. Je montre les jugements de la ḥawāla.',
    '<h2>L’analyse</h2>',
    'Cette leçon comprend les axes suivants :',
    '<h3>Axe premier : la définition de la ḥawāla, son jugement et ses piliers</h3>',
    '<h4>1. La définition de la ḥawāla</h4>',
    '<span>a. Dans la langue :</span> elle est tirée du <em>taḥawwul</em>',
    'il a transféré (<em>ḥawwala</em>) la chose de son lieu — il l’a portée vers un autre lieu',
    'et il a tourné (<em>ḥawwala</em>) son visage — il l’a détourné',
    '<span>b. Dans la terminologie :</span> a dit l’illustre Dardīr',
    '« Elle est le transfert (<em>naql</em>) de la dette, d’une ḏimma à l’identique (<em>bi-miṯli-hi</em>), vers une autre, par laquelle la première est dégagée. »',
    'L’illustre Dasūqī, expliquant son propos, a dit : son dire « à l’identique » se rapporte au « transfert »',
    'en raison de l’existence d’une pareille dans l’autre',
    '<h4>2. Son jugement</h4>',
    'La ḥawāla est un contrat révocable (<em>jāʾiz</em>).',
    'et le plus tenu est qu’elle est une licence (<em>ruḫṣa</em>) exceptée de la vente de la dette par la dette — ainsi l’a dit Qāḍī ʿIyāḍ',
    '[La Hāšiya d’ad-Dasūqī 3/325]',
    'Et l’imām al-Bāğī, au commentaire du hadīth du Muwaṭṭaʾ : « Quand l’un de vous est renvoyé vers un homme rempli, qu’il suive »',
    'son sens, et Dieu sait mieux : la ḥawāla...',
    'elle n’est point valide excepté d’une dette établie pour le muḥīl sur le muḥāl ʿalay-hi — et cela parce que le muḥīl dégage sa ḏimma par la ḥawāla même ; elle est donc du chapitre du liquide (<em>naqd</em>)',
    'qu’elle repose sur la permission (<em>ibāḥa</em>)',
    'acquitte-moi mon droit, et ton affaire est avec le tien',
    '[Al-Muntaqā, commentaire du Muwaṭṭaʾ, d’Abū l-Walīd al-Bāğī 5/66]',
    '<h4>3. Ses piliers</h4>',
    'La ḥawāla a cinq piliers :',
    '<span>a. Le muḥīl</span>, qui est celui sur qui est la dette ;',
    '<span>b. le muḥāl</span>, qui est celui à qui est la dette ;',
    '<span>c. le muḥāl ʿalay-hi</span>, qui est celui sur qui est une dette pareille à celle qui est sur le premier débiteur ;',
    '<span>d. le muḥāl bi-hi</span>, qui est la dette pareille ;',
    '<span>e. un formulaire</span> (<em>ṣīġa</em>) qui indique le transfert et le passage, fût-ce par un signe ou par une écriture.',
    '<h3>Axe deuxième : les conditions de la ḥawāla</h3>',
    'Les conditions de validité de la ḥawāla sont celles que l’auteur a signalées, en résumé, par son propos',
    'et son détail est comme suit :',
    'Le contentement du muḥīl et du muḥāl seulement, non du muḥāl ʿalay-hi — car son contentement n’est point conditionné selon le retenu',
    'elle est donc valide, qu’il y ait consenti ou non — excepté s’il y avait entre lui et le muḥāl une inimitié antérieure au temps de la ḥawāla : la ḥawāla n’est alors point valide, selon le retenu',
    'L’établissement d’une dette pour le muḥīl sur la ḏimma du muḥāl ʿalay-hi — et de même pour le muḥāl ʿalay-hi sur le muḥīl —, autrement ce serait une wakāla, non une ḥawāla',
    'la description de la dette par « ferme » (<em>lāzim</em>) est une garde contre la dette d’un mineur ou d’un interdit (<em>safīh</em>) sans la permission de son tuteur',
    'La dévolution (<em>ḥulūl</em>) de la dette transférée — laquelle est la dette qui est au muḥāl ʿalay-hi sur le muḥīl',
    'cela mènerait à peupler une ḏimma d’une ḏimma, et y entrerait ce dont il a interdit la mention : la vente de la dette par la dette',
    'et la vente de l’or par l’or, ou du papier, non main dans la main, si les deux dettes étaient or ou papier',
    'excepté que la dette vers laquelle le transfert s’est fait soit liquide, et que [le muḥāl] la saisisse avant qu’ils ne se séparent, comme le change (<em>ṣarf</em>) : cela est alors permis',
    'L’égalité des deux dettes en quantité et en qualité. A dit l’illustre az-Zurqānī',
    'au point qu’il deviendrait impossible de transférer [la dette de] cinq sur dix sur son débiteur — comme l’ont imaginé certains de ceux dont on ne tient pas compte',
    'mais ce qu’on entend par leur égalité est que ce qui est pris du muḥāl ʿalay-hi ne soit ni plus, ni moins que la dette transférée',
    '[Le Šarḥ d’az-Zurqānī sur le Mukhtaṣar de Khalīl, avec la Hāšiya d’al-Bannānī 6/34]',
    'Puis l’auteur a enchaîné par son propos : « et sur son transfert vers l’inférieur, hésitation »',
    'A dit l’illustre Muḥammad ʿAlīš : il entend que les maîtres tardifs ont hésité sur la licéité de son transfert de la dette supérieure vers ce qui est inférieur d’elle — qu’on le veuille ou non —, ou du plus grand au moindre',
    'et la plupart des maîtres sont pour la licéité. [Le Manḥ al-Ğalīl, commentaire du Mukhtaṣar de Khalīl 6/191]',
    'Que les deux dettes — le transféré et celle [sur laquelle il est transféré] — ne soient pas un aliment issu d’une vente (<em>ṭaʿām min bayʿ</em>)',
    'c’est-à-dire [ce qui est dû] par le <em>salam</em> — afin que n’y entre pas la vente de l’aliment avant la prise',
    'que les capitaux s’accordent, ou qu’ils diffèrent',
    '<h3>Axe troisième : les jugements de la ḥawāla</h3>',
    '<h4>1. La validité de la ḥawāla et l’absence de retour du muḥāl ʿalay-hi sur le muḥīl</h4>',
    'Quand le muḥāl ʿalay-hi revient-il sur le muḥīl ? Et quand revient-on contre lui ?',
    'Il n’est point des conditions de la ḥawāla que le muḥāl dévoile l’état de la ḏimma de la personne du muḥāl ʿalay-hi — est-il riche, ou pauvre ?',
    'mais la ḥawāla est valide, selon le madhhab, avec l’absence de dévoilement, et le droit du muḥāl se transfère sur le muḥāl ʿalay-hi au seul fait du contrat de ḥawāla',
    'quand bien même il serait en faillite au temps de la ḥawāla, ou dénierait ce qui est sur lui après l’achèvement de la ḥawāla, non avant elle — car il n’y a point de preuve contre lui, faute de dette établie sur lui',
    'excepté que le muḥīl sache de la faillite du muḥāl ʿalay-hi seulement, non du muḥāl : alors il revient sur le muḥīl, car il l’a trompé (<em>ğarra-hu</em>)',
    'et l’apparent est que la croyance du muḥīl, au temps de la ḥawāla, en la faillite du muḥāl ʿalay-hi est comme sa science de cela',
    'il jure la négation de la science, si l’on soupçonne de lui la science — c’est-à-dire qu’il est de ceux qu’on soupçonne de connaître la faillite de son pareil',
    'sinon il ne jure point, quand bien même le muḥāl le soupçonnerait',
    'Qu’un vendeur d’une marchandise transfère une personne — par une dette qu’il a sur le vendeur — sur un acheteur de cette marchandise, pour son prix',
    'puis le vendu est rendu à son vendeur, le muḥīl, pour un vice, ou pour une corruption, ou que [l’acheteur] eût usé de son option de la main de son acheteur',
    'et que tout cela eût lieu avant que le muḥāl ne saisisse le prix de l’acheteur — : la ḥawāla ne se dissout point, selon Ibn al-Qāsim ; car cela est connu',
    'l’acheteur est tenu de verser le prix au muḥāl, et il revient, par son pareil, contre son vendeur, le muḥīl',
    'Et cela est fondé sur ce que le retour pour le vice est une vente initiale',
    'Et Ibn al-Mawwāz et d’autres ont choisi le contraire du dire d’Ibn al-Qāsim — lequel est le dire d’Ašhab — : la dissolution de la ḥawāla ; et sur lui est la majorité',
    '<h4>2. Le litige entre le muḥīl et le muḥāl</h4>',
    'Puisque l’origine est que la parole soit au réclamant de la validité contre le réclamant de l’invalidité, et à l’affirmateur contre le déniateur',
    'C’est-à-dire : si le muḥāl ʿalay-hi réclamait contre le muḥīl qu’il dénie la dette du muḥāl ʿalay-hi, et qu’il [le muḥīl] eût transféré sur ce qui n’est point dette — la parole est au muḥīl, par serment',
    'et que celui-ci mourût, ou fût déclaré en faillite, ou s’absentât d’une absence de rupture (<em>ġayba inqiṭāʿ</em>)',
    's’il était présent, et mentionnait ce qui s’accorde avec le dire de l’un des deux, serait-il comme le témoin, ou non ?',
    'Et l’on n’agit point selon le dire du muḥīl dans sa revendication d’une wakāla pour le muḥāl ʿalay-hi afin de saisir son bien d’un débiteur, ni d’un salaf du muḥīl au muḥāl, quand bien même la parole de la ḥawāla serait sortie entre eux deux',
    'la parole est alors au saisisseur, par son serment, que cela est de sa dette, s’il est plus apparent que son pareil soit une dette pour lui sur le muḥīl',
    'sinon, la parole est au seigneur du bien, par son serment, que cela est wakāla ou salaf',
    'Et des profits de la leçon : Dieu — le Très-Haut — a légiféré la ḥawāla pour la mise à l’abri des biens, et pour l’accomplissement du besoin de l’homme',
    'car l’homme peut avoir besoin de dégager sa ḏimma du droit de son créancier, ou de recouvrer son droit d’un débiteur à lui',
    'soit pour la peine de son port, soit pour la longueur de la distance et du chemin, soit parce que la route n’est point sûre, ou autre',
    'Dieu a donc légiféré la ḥawāla pour la réalisation de ces intérêts, et pour la facilitation du remboursement et du recouvrement entre les gens',
    'Et par cela se réalisent la fin des droits (<em>al-maqṣad al-ḥuqūqī</em>) et la fin du bien (<em>al-ğawdī</em>)',
    '<h2>Le contrôle</h2>',
    '1. Je montre le jugement de la ḥawāla et sa sagesse.',
    '2. Je mentionne les piliers de la ḥawāla et ses conditions.',
    '3. Je montre le jugement de la figure suivante, avec son argumentation : un débiteur en aliment (<em>ṭaʿām</em>) d’une valeur de trois mille dirhams a transféré son créancier sur un débiteur à lui d’une somme de mille dirhams, qu’il lui prêta en liquide.',
    '<h2>L’exploitation</h2>',
    'A dit l’imām Ibn ʿAbd al-Barr — que Dieu lui fasse miséricorde — : « La ḥawāla est le transfert des ḏimmas',
    'alors le créancier transfère sur celui qui a sur lui le pareil de sa dette',
    'quand il se retourne sur lui, et que celui-ci a consenti, la ḏimma passe à la ḏimma de l’autre — le muḥīl est dégagé de la dette, et nulle charge d’elle n’est sur lui, et le droit devient sur le muḥāl ʿalay-hi',
    'et point de retour pour lui sur le muḥīl, jamais, que le muḥāl ʿalay-hi fût déclaré en faillite ou mourût démuni',
    'excepté qu’il ait été trompé par un homme démuni ou en faillite, dont le seigneur du droit ne savait point qu’il fût ainsi',
    'si cela est, alors lui est la faculté de revenir sur celui sur qui était le droit d’abord',
    'et s’il savait de son dénuement, et consentit à la ḥawāla sur lui — point de retour pour lui sur le premier, en aucune des manières',
    '[Le Kāfī dans la jurisprudence des gens de Médine, d’Ibn ʿAbd al-Barr 2/797]',
    'Je contemple ce texte et je réponds à ce qui suit :',
    '1. J’extrais du texte une définition de la ḥawāla, et je montre la différence entre la définition d’Ibn ʿAbd al-Barr et la définition de Dardīr.',
    '2. Je dégage du texte les jugements de la ḥawāla, et je les compare à ce qu’il y a dans la leçon.',
    '<h2>La préparation préalable</h2>',
    'Je lis le texte de la leçon à venir et j’y accomplis ce qui suit :',
    '1. Je me familiarise avec le ḍamān, et je détermine ses types et ses piliers.',
    '2. Je montre le jugement du ḍamān et ses conditions.',
    '<h2>Le sens de cette leçon</h2>',
    'Cette leçon fait entrer la dette dans le droit commun du transfert : le muḥīl dégage sa ḏimma par la ḥawāla même — elle est « du chapitre du liquide », non de la dette par la dette',
    'le contentement du muḥīl et du muḥāl seulement : le muḥāl ʿalay-hi n’est point consulté — sauf inimitié antérieure au temps de la ḥawāla',
    'la dette est « ferme » : garde contre la dette du mineur et de l’interdit sans la permission de son tuteur',
    'la dévolution, non le peuplement d’une ḏimma d’une ḏimma — sauf la dette liquide saisie avant la séparation, comme le change',
    'l’égalité des deux dettes n’est point l’identité des chiffres : cinq sur dix se transfèrent, pourvu que ce qui est pris ne dépasse point la dette transférée — ni en plus, ni en moins',
    'sur le transfert vers l’inférieur, hésitation — et la licéité est tenue par la plupart des maîtres',
    'point de révélation de la ḏimma du muḥāl ʿalay-hi : le droit se transfère quand bien même il serait en faillite ou dénierait — sauf le muḥīl trompé par la faillite qu’il savait seule, et dont il jure la négation si l’on le soupçonne',
    'la vente rendue pour vice n’emporte point la dissolution de la ḥawāla selon Ibn al-Qāsim — le contraire selon Ašhab, suivi d’Ibn al-Mawwāz, et sur lui la majorité',
    'la parole est au muḥīl par serment sur la négation de la dette — non dans sa revendication de wakāla ou de salaf : là, la parole est au saisisseur, ou au seigneur du bien',
    'Dieu a légiféré la ḥawāla pour la mise à l’abri des biens et l’accomplissement du besoin : la fin des droits et la fin du bien se réalisent par elle',
    '<h2>Notes du traducteur</h2>',
    'l’étiquette GT « les règles de la cession de dette » est ramenée au h1 imprimé « les jugements de la ḥawāla »',
    '(règle av — treizième tranchage du fil)',
    'VIDE en ce tour — ni date, ni mention —, au contraire des leçons précédentes du fil',
    'La ligne de cours imprimée se confirme une onzième fois consécutive (6e → … → 16e)',
    'La coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa quinzième occurrence',
    'le fil du bāb s’enchaîne : la ḥawāla « suit » la conciliation',
    'le guillemet fermant du matn manque dans le document (le guillemet ouvert après « a dit » ne se referme point) — ajouté par le traducteur pour l’appariement (règle ax)',
    'le muḥīl, le muḥāl, le muḥāl ʿalay-hi, le muḥāl bi-hi — quatre termes nouveaux de famille',
    'les deux interprétations ne sont point développées dans le document — rendues telles quelles, sans tranchement (règle ax)',
    'az-Zurqānī (6/34) interdit de lire l’égalité comme impossibilité de transférer cinq sur dix',
    'ʿAlīš, au Manḥ al-Ğalīl (6/191) : « la plupart des maîtres sont pour la licéité » — le Manḥ al-Ğalīl nommé au fil pour la deuxième fois (6/148 au tour R311)',
    'le document écrit « <em>yurīd</em> » là où le commentaire imprimé porte « <em>yaʿnī</em> » (« c’est-à-dire »)',
    'rendu « qu’on le veuille ou non », écart consigné sans rétro-révision (règle ax)',
    'le <em>salam</em> entre au fil comme source de la dette d’aliment',
    '« Quand l’un de vous est renvoyé vers un homme rempli, qu’il suive » — cité en toutes lettres selon la graphie du document',
    'le Muwaṭṭaʾ entre au fil du bāb, et la leçon porte ainsi une citation du Prophète — première depuis 19441',
    'l’ellipse du document est conservée telle quelle (règle ax)',
    '« acquitte-moi mon droit, et ton affaire est avec le tien »',
    '« la croyance du muḥīl... est comme sa science » : la présomption vaut la science',
    'le serment du muḥāl ʿalay-hi sur la négation de la science n’a lieu que s’il est soupçonné — « quand bien même le muḥāl le soupçonnerait » sans suspicion fondée',
    'Ibn al-Qāsim — non-dissolution, « car cela est connu » (le retour pour vice est « une vente initiale »)',
    'Ibn al-Mawwāz et autres — dissolution, « lequel est le dire d’Ašhab », et sur lui « la majorité » : deuxième mise en scène des dires des compagnons de Mālik au fil (Ibn al-Qāsim cité à l’exploitation de 19492)',
    '« l’option eût été usée » rend le <em>istiḥiqāq</em> du Khiyār',
    'la parole au réclamant de la validité « et à l’affirmateur contre le déniateur » — règle de charge de la preuve',
    'l’absence de rupture (<em>ġayba inqiṭāʿ</em>) est un nouveau terme de famille',
    'la ressemblance fait le droit, le serment tranche le reste',
    'un aliment de trois mille dirhams transféré sur une dette de mille dirhams prêtée en liquide — la figure touche à la fois l’aliment issu d’une vente, l’égalité (mille au plus, jamais davantage), et la dévolution d’une dette liquide',
    'l’argumentation est laissée à l’élève, selon la coutume de la famille',
    'Ibn ʿAbd al-Barr [Le Kāfī dans la jurisprudence des gens de Médine 2/797] définit la ḥawāla « le transfert des ḏimmas » — par les ḏimmas, non par la dette',
    'la tâche première demande la différence avec la définition de Dardīr (le transfert de la dette, d’une ḏimma à l’identique, vers une autre)',
    'l’exception du trompé rejoint la règle du muḥīl trompé de l’axe troisième, et le « jamais » de l’absence de retour épouse le matn',
    'le ḍamān (la garantie) entre en scène — deux items (types et piliers ; jugement et conditions)',
    'le fil des contrats d’obligations se poursuit après la ḥawāla, selon l’ordre du Mukhtaṣar',
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

out = '/home/z/my-project/tr-tmp/19495.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
