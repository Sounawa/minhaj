#!/usr/bin/env python3
# build-19601.py — 19601 « Jurisprudence : les dispositions de l'associé de
# mufāwaḍa et les jugements du litige » (fiqh-tanawi-3, lessons[26], badge
# Leçon 28/33) — vingt-quatrième cours imprimé (24e confirmation : 21e types
# ḍamān → 22e šarika → 23e mufāwaḍa → 24e dispositions+litige). QUATRE axes
# h3 : (1) jugements des deux associés — wakāla analogique (non-wakīl en
# vérité) / radd sur le présent n'ayant pas disposé comme l'absent lointain
# sinon attendu, profit-perte à mesure des deux capitaux / corruption
# (tafāwut + faskh avant œuvre, sixième du profit + salaire du sixième de
# l'œuvre après) ; (2) dispositions — tabarruʿ (mafhum de la condition),
# salaf, hiba après contrat (ğarr an-nafʿ, lāḥiq li-l-ʿuqūd) ; (3) litige —
# talaf (sans mouvement) vs ḫusr (avec mouvement), amīn garantit au farṭ /
# lāʾiq nourriture-vêtement seulement / attribution du profit (demi à
# serment, ištirāk porté sur le demi) / exclusivité (ka-īrṯih, TROIS cas,
# aṣaḥḥ) / demeure auprès d'un associé mort (ḥay munkir, takḏīb nafsa-hu) /
# ṣadāq (aṣl, un an, bayyina) ; (4) iqrār de dette après séparation ou mort
# (témoin hors sa part, mubarriz fī l-ʿadāla, mullāṭaf) + nafaqa/kiswa
# (deux villes de prix différent, ʿiyāl rapprochés, isqāṭ de la condition
# munāṣafa). Fentes : AUCUNE (0 āya / 0 hadīth — 5e tour sans protocole
# triple) ; exploitation = Bahrām, aš-Šāmil fī fiqh al-Imām Mālik 2/697
# (wadīʿa taʿaddī, tafāḍul, ğr al-miṯl, le sixième se partage) ; at-taʿbīm
# 23e occ. ; préparation préalable → ʿinān (19670, première des cinq).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19601_{i}.html').read())
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
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'dl', 'dt', 'dd', 'br']:
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if tag in ('br',):
        if o and c:
            issues.append(f'balise {tag} fermante inattendue')
        continue
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

norm = lambda s: s.replace("'", chr(0x2019))
probes = [
    "Jurisprudence : les dispositions de l'associé de mufāwaḍa et les jugements du litige",
    "il devient alors, en vertu du contrat de šarika, comme le wakīl de son associé",
    "il faut alors recourir au jugement (<em>al-qaḍāʾ</em>) pour trancher la matière du différend",
    "Quels sont donc les jugements de la šarika de mufāwaḍa ?",
    "Et par quoi la šarika de mufāwaḍa se corrompt-elle ?",
    "vingt-quatrième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître quelques jugements de la šarika de mufāwaḍa.",
    "Saisir les dispositions des deux associés de mufāwaḍa.",
    "Se représenter les jugements de la šarika de mufāwaḍa dans mes transactions financières.",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Chacun des deux est un wakīl",
    "comme (il le serait sur) l'absent, si son absence est lointaine ; sinon, il est attendu",
    "Et le profit et la perte à la mesure des deux capitaux",
    "Et elle se corrompt par la condition de la disparité",
    "Et à chacun le salaire de son œuvre pour l'autre",
    "Et il a le tabarruʿ, et le salaf, et la hiba après le contrat",
    "au revendicateur du demi — et (l'association) est portée sur le demi en leur contestation",
    "excepté par une bayyina, à la manière de son héritage",
    "fût-on pas témoigné de son iqrār — sur l'assez-sûr",
    "que (la somme) demeure — si l'on en témoigne au moment de la prise",
    "comme le paiement d'un ṣadāq pour son associé",
    "sauf si le temps s'allonge à une année",
    "La compréhension",
    "Le commentaire",
    "Le ḫusr (la perte) : l'antonyme du profit",
    "Le tabarruʿ : le donner sans contrepartie",
    "Le lāʾiq (le convenable) : ce qui convient",
    "la chose se perd (<em>ṭalifa</em>) d'une perte et périt",
    "La synthèse du contenu du texte",
    "J'extrais du texte les jugements de la šarika de mufāwaḍa.",
    "Je mets en relief du texte les jugements du litige entre les deux associés.",
    "L'analyse",
    "Cette leçon comprend les axes suivants :",
    "Axe premier : les jugements des deux associés dans la mufāwaḍa",
    "1. La wakāla de l'un des deux pour l'autre",
    "dans la vente et l'achat, le prendre et le donner, la location et la prise en location",
    "la réclamation du dû et du défaut — non qu'il soit wakīl en vérité",
    "car il est associé, et l'associé n'est pas le wakīl",
    "2. Ce qui découle de leur wakāla",
    "Est restitué (le bien vendu) dont un associé absent d'une absence lointaine s'était chargé de la vente",
    "comme la restitution du bien vendu défectueux à son vendeur absent",
    "car l'acheteur a été tenu en place par l'affaire du bien vendu",
    "à plus forte raison si tous deux sont présents",
    "3. La corruption de la šarika de mufāwaḍa",
    "a. La cause de sa corruption",
    "quand l'un des deux conditionne, dans son contrat, la disparité dans le partage du profit et de la perte",
    "b. L'œuvre quand elle est corrompue",
    "S'il s'avise de la corruption du contrat de la šarika avant l'œuvre, il résilie le contrat",
    "et qu'ils soient entrés sur le partage à l'égal (<em>munāṣafa</em>) dans l'œuvre et le profit",
    "le détenteur des deux tiers a un recours contre le détenteur du tiers pour le sixième du profit",
    "le détenteur du tiers a un recours pour le salaire du sixième de l'œuvre",
    "Axe deuxième : les dispositions des deux associés de mufāwaḍa",
    "1. Que l'un des deux fasse le tabarruʿ à son associé",
    "d'une part du profit ou de l'œuvre — et c'est le sens impliqué (<em>mafhum</em>)",
    "s'il s'est servi du don pour s'attacher les gens, ou si (le donné) est léger",
    "2. Que l'un des deux fasse le salaf à son associé",
    "Il est permis à l'un des deux associés de faire le salaf à son associé de quelque chose.",
    "3. Que l'un des deux fasse la hiba à son associé",
    "doivent se faire après le contrat, non avant ou en lui",
    "ouvre sur la disparité ou le soupçon (<em>tuhma</em>) de celle-ci",
    "pour attirer le profit (<em>ğarr an-nafʿ</em>) dans le salaf",
    "même à son strict sillage (<em>bi-āṯarih</em>)",
    "ce qui est postérieur aux contrats n'est pas comme ce qui se produit en eux",
    "Axe troisième : les jugements du litige entre les deux associés",
    "1. Le litige des deux associés sur la prétention de la péremption et de la perte",
    "au revendicateur de la péremption — qui est ce qui naît sans mouvement — et de la perte — qui est ce qui naît d'un mouvement",
    "de la perte — qui est ce qui naît d'un mouvement",
    "car il est l'amīn du bien de la šarika",
    "tant que son démenti ne se manifeste pas par la bayyina ou par les indices (<em>qarāʾin</em>)",
    "alors qu'il était en une compagnie (<em>rifqa</em>) où cela ne saurait se dissimuler à eux",
    "pour la renommée de son prix ou choses pareilles",
    "il garantit et est frappé d'amende (<em>ġurima</em>)",
    "car l'amīn garantit à la négligence (<em>farṭ</em>)",
    "2. Le litige des deux associés sur la prétention de la prise du convenable",
    "la parole, sans serment, est au revendicateur de l'achat du convenable (<em>lāʾiq</em>)",
    "pour lui et ses personnes à charge (<em>ʿiyāl</em>), en nourriture et en vêtement seulement",
    "tant que son associé ne l'a pas crédité sur ce point",
    "cela n'est pas crédité et retourne à la šarika",
    "3. Le litige des deux associés sur la prétention de l'attribution du profit",
    "la parole, avec serment, est au revendicateur du demi",
    "la coparticipation est portée sur le demi dans l'état de leur litige",
    "si leur šarika est au demi ou autre",
    "4. Le litige des deux associés sur la prétention de l'exclusivité dans la détention d'une chose",
    "détient une chose et revendique son exclusivité (<em>iḫtiṣāṣ</em>)",
    "non au revendicateur pour lui-même, excepté par une bayyina qu'établit le détenteur",
    "alors il a seul ce qui est en sa main de l'un des deux associés",
    "il n'est pas a fortiori en exclusivité — le (bien) est entre eux deux",
    "nous ne savons ni sa précédence ni sa postériorité",
    "Et les cas sont au nombre de trois.",
    "de ce que leur disposition fut la disposition des mufāwaḍīn",
    "la šarika s'est nouée entre eux sur le visage de la mufāwaḍa",
    "voire même si elle ne témoigne pas contre eux deux de son iqrār, sur l'assez-sûr",
    "5. Le litige des deux associés sur la prétention que demeure une part du bien de la šarika auprès d'un associé mort",
    "de la prise de cent par exemple — selon l'exemple de l'auteur",
    "c'est-à-dire que le mort l'a prise avant sa mort",
    "sa prétention de renvoi au bien de la šarika n'est pas reçue, dût la durée s'allonger",
    "car il se fait mensonge à lui-même par le démenti de la prise",
    "contre lui-même, la prise ; ou si en témoigne son associé, le repousseur",
    "6. Le paiement d'un ṣadāq sur le bien de la šarika",
    "pour s'être tenu à l'original (<em>aṣl</em>)",
    "car son abstention de réclamer son associé durant cette durée atteste sa véracité",
    "elle ne tombe pas par l'allongement d'une année, et sa bayyina est reçue",
    "Axe quatrième : quelques dispositions des deux associés de mufāwaḍa",
    "1. La reconnaissance par l'un des deux associés d'une dette pesant sur eux deux",
    "sans besoin du serment du bénéficiaire de l'iqrār",
    "il est témoin hors de sa part ; attendu que le bénéficiaire",
    "comme son oncle paternel, le fils de son oncle, comme son frère ou son familier (<em>mullāṭaf</em>)",
    "si le reconnaissant est manifeste en justice (<em>mubarriz fī l-ʿadāla</em>)",
    "le bénéficiaire prête alors serment avec lui, et la dette est due",
    "Quant à sa propre part, il en est tenu compte après la séparation ou la mort",
    "2. Les dépenses des deux associés sur le bien de la šarika",
    "fût-ce en deux villes de prix différent — dût la différence de prix entre les deux villes être manifeste",
    "chacun des deux n'a contracté que pour le commerce avec la réduction du fardeau de chacun",
    "si elles se rapprochent en années et en nombre, selon la parole des gens de connaissance",
    "celle que le bien soit entre eux deux à l'égal — cela seulement en la question des personnes à charge",
    "afin que nul ne prenne du bien de la šarika plus que son dû",
    "la vie des gens n'est pas sans participation ni mélange ni besoin de chacun envers l'autre",
    "elle a posé pour cela des garde-fous et des liens par lesquels les transactions se règlent",
    "Le contrôle",
    "Je mentionne quelques jugements de la šarika de mufāwaḍa.",
    "L'exploitation",
    "L'ʿAllāma Bahrām — que Dieu lui fasse miséricorde — a dit",
    "si l'un des deux commerce avec un dépôt (<em>wadīʿa</em>) par transgression (<em>taʿaddī</em>)",
    "il a seul, si l'autre n'en sait rien ; sinon, (le profit) est pour eux deux et sur eux deux",
    "Et le profit et l'œuvre à la mesure de leurs deux capitaux",
    "la condition de la préférence (<em>tafāḍul</em>), fût-ce en l'un des deux",
    "par le salaire du semblable (<em>ağr al-miṯl</em>) pour le surplus — sur l'assez-sûr",
    "s'il a profité, le moindre est à lui ; et qui a profité d'une part",
    "Et le tabarruʿ, la hiba et le salaf après le contrat, de l'un des deux vers l'autre, sont permis",
    "il est crédité de tout ce qui lui fut concédé, et le sixième se partage entre eux deux",
    "ils prêtent serment tous deux et (le différend) est partagé au demi",
    "[aš-Šāmil fī fiqh al-Imām Mālik 2/697]",
    "J'examine ce texte et je réponds à ce qui suit :",
    "je les compare avec ce qui est dans le texte",
    "Je fais connaissance avec l'ʿAllāma Bahrām et son livre aš-Šāmil.",
    "La préparation préalable",
    "Je lis le texte de la leçon prochaine et je réponds à ce qui suit :",
    "Je montre du texte les dispositions des deux associés de mufāwaḍa.",
    "Je détermine le concept de la šarika de ʿinān et son jugement.",
    "Je recherche ce qui est permis et ce qui ne l'est pas dans la šarika de ʿinān.",
    "Notes du traducteur",
    "vingt-et-unième tranchage du fil",
    "ad-dars ar-rābiʿ wa-l-ʿišrūn",
    "première des cinq leçons qui la portent",
    "il est associé, et l'associé n'est pas le wakīl",
    "le prolongement, dans le litige, de l'iṭlāq réciproque",
    "la formule de Khalīl dit que le revendicateur qui établit la bayyina emporte le bien comme l'héritier",
    "entre deux transmissions du Mukhtaṣar, la plus solide",
    "le verbe arabe (<em>aqaʿada</em>) peint la monture qui s'assoit et refuse d'avancer",
    "le talaf est ce qui naît SANS mouvement de la chose, le ḫusr ce qui naît D'UN mouvement",
    "la parole allant au revendicateur tant que nul indice ne le démente",
    "la bayyina établie contre lui ruine sa prétention de renvoi",
    "le passage est dense, porté tel quel",
    "l'iqrār du reconnaissant ne vaut pour autrui que comme TÉMOIGNAGE",
    "celui dont la droiture éclate aux yeux des gens",
    "celui qu'on traite avec douceur et familiarité",
    "les connaisseurs du prix courant en une ville ou deux",
    "que la leçon précédente développait sous l'istibdād de qui commerce avec un dépôt",
    "le dépassement de la part du profit que commande la mesure des deux capitaux",
    "Bahrām donne ici un avis que le matn n'exprime pas en cet endroit",
    "comme le demande la première tâche de l'exploitation",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19601.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
