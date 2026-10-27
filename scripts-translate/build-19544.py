#!/usr/bin/env python3
# build-19544.py — 19544 « Jurisprudence : les jugements de la šarika de
# mufāwaḍa » (fiqh-tanawi-3, lessons[25], badge Leçon 27/33) — vingt-troisième
# cours imprimé (CONFIRMATION : 20e pluralité → 21e types → 22e šarika → 23e
# mufāwaḍa). TROIS axes h3 : (1) définition (iṭlāq réciproque, tous genres ou
# un genre) + types (générale/particulière) + non-corruption (isolement sur
# bien hors šarika, égalité du travail) ; (2) DIX dispositions de l'un des
# deux (don conditionné istiʾlāf/légèreté, ibḍāʿ, muqāraḍa, dépôt pour
# excuse, association déterminée, iqāla, tawliya, retour pour défaut — wa-in
# abā l-āḫar double rattachement, reconnaissance de dette, vente à crédit ≠
# achat à crédit) ; (3) TROIS istibdād (preneur de qirāḍ — muqāraḍa hors
# commerce, salarié ; emprunteur de bête — wāw ḥāl + in zāʾida, profit
# location chargé / perte garantie, fa-lā taḍman ; commerçant avec dépôt —
# exception Mudawwana) + clausule morale (attrait des clients).
# Fentes : AUCUNE liminaire ; TROIS fentes de verset vides dans
# l'exploitation (candidats documentaires : Ṣād 38:24 ḫulaṭāʾ, An-Nisāʾ
# 4:12 šurakāʾ fi ṯ-ṯuluṯ, Az-Zumar 39:29 parabole des associés rivaux —
# tous vérifiés au cache, AUCUNE insertion) ; exploitation = Ibn Rušd
# al-Ğadd, Muqaddimāt Mumahhidāt 3/33-34 (ḫalīṭ = l'indivisaire, terme fixé
# R318 — tout associé indivisaire, tout indivisaire non associé) ; at-taʿbīm
# 22e occ. ; préparation préalable → 19601 (suite de la mufāwaḍa).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19544_{i}.html').read())
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
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'dl', 'dt', 'dd']:
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

norm = lambda s: s.replace("'", chr(0x2019))
probes = [
    "Jurisprudence : les jugements de la šarika de mufāwaḍa",
    "en considération des qualités qu'il a vues en lui et qui le portent à l'association avec lui",
    "sur la base de l'application libre, chez chacun des deux, du droit de disposer",
    "pour entrer dans la šarika sur la claire connaissance de son affaire",
    "Quel est donc le concept de ce type de šarika ?",
    "Et chacun des deux associés a-t-il le droit de disposer du bien de la šarika ?",
    "vingt-troisième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître le concept de la šarika de mufāwaḍa.",
    "Saisir les jugements de la šarika de mufāwaḍa.",
    "Se représenter les jugements de certaines sections de la šarika dans les transactions.",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Puis, s'ils ont tous deux donné libre la disposition — fût-ce en un genre —, c'est la mufāwaḍa",
    "et ne la corrompt point que l'un des deux s'isole par quelque chose",
    "s'il s'est servi du don pour s'attacher les gens, ou si (le donné) est léger",
    "comme le prêt d'usage (<em>iʿāra</em>) d'un outil, et le don d'une bouchée (<em>kisra</em>)",
    "et qu'il fasse l'ibḍāʿ ; et qu'il fasse la muqāraḍa",
    "et qu'il dépose pour une excuse — sinon il garantit",
    "et qu'il s'associe avec un étranger en un (bien) déterminé",
    "et qu'il reprenne ; et qu'il fasse la tawliya",
    "et qu'il accepte le retour pour défaut, dût l'autre refuser",
    "et qu'il reconnaisse une dette pour qui n'est pas suspect (contre lui)",
    "et qu'il vende à crédit — non l'achat à crédit",
    "le preneur de qirāḍ, et l'emprunteur d'une bête sans permission — et pour la šarika —",
    "et qui commerce avec un dépôt, au profit et à la perte",
    "sauf que son associé sache de sa transgression dans le dépôt",
    "La compréhension",
    "Le commentaire",
    "La mufāwaḍa : la šarika de mufāwaḍa est que chaque associé donne libre à son associé la disposition du bien de la šarika",
    "librement — totalement ou partiellement — tant que cela demeure dans l'intérêt de la šarika",
    "l'ibḍāʿ est l'acquisition de la marchandise pour la šarika, sur son bien (propre)",
    "contre une part connue de son profit",
    "chez un homme de confiance",
    "qu'il résilie ce qu'il a vendu du bien de la šarika à un autre",
    "qu'il vende la marchandise à son prix d'achat",
    "La synthèse du contenu du texte",
    "J'extrais du matn la définition de la šarika de mufāwaḍa.",
    "Je détermine, à travers le matn, certaines dispositions de l'un des deux associés.",
    "L'analyse",
    "Ce cours comporte les axes qui suivent",
    "Axe premier : la définition de la šarika de mufāwaḍa et ses types",
    "1. La définition de la šarika de mufāwaḍa",
    "nous nous sommes associés (<em>aštaraknā</em>)",
    "par la vente et l'achat, la location et la prise en location",
    "cette šarika s'appelle šarika de mufāwaḍa",
    "2. Ses types",
    "La générale : celle où chacun des deux associés a donné libre à son compagnon la disposition de tous les genres",
    "la particulière : celle où chacun des deux associés a donné libre à son compagnon la disposition d'un genre",
    "où il travaille pour lui-même particulièrement, quand les deux sont égaux dans le travail de la šarika",
    "Axe deuxième : les dispositions de l'un des deux associés de la mufāwaḍa",
    "il est permis à chacun des deux associés de la mufāwaḍa de disposer du bien de la šarika par ce qui suit",
    "s'il s'est servi du don pour s'attacher les gens (<em>istaʾlafa</em>)",
    "en le donnant pour attirer les clients",
    "comme le prêt d'usage d'un outil, et le don d'une bouchée à un pauvre",
    "à qui achètera avec une marchandise connue d'une telle ville",
    "si le bien s'est élargi au point que cela en ait besoin ; sinon, il s'abstient sans la permission de son associé",
    "le dépôt devient obligatoire, quand bien même le dépôt ne serait pas pour excuse",
    "le garant est le disposant des deux associés",
    "il convient qu'il soit véridique dans sa prétention d'excuse, car il est un associé digne de confiance (<em>muʾtaman</em>)",
    "en une (part) déterminée du bien de la šarika, sans que sa main circule en tout",
    "qu'il rende une marchandise à la šarika à son prix, celui auquel lui-même l'a vendue, ou son associé",
    "s'il craint son dépréciation ou sa perte",
    "la valeur de sa part du profit qui est dans cette marchandise",
    "pour un défaut (<em>maʿīb</em>) ancien",
    "de son dire « faire un don » jusqu'ici — et il porte sur ce qui le précède immédiatement seulement",
    "avant la séparation et la mort, une dette",
    "son associé choisit entre l'acceptation et le retour, et le prix demeure alors sur l'acheteur particulièrement",
    "Axe troisième : le jugement de l'istibdād de l'un des deux associés de la mufāwaḍa",
    "1. L'istibdād du preneur de qirāḍ",
    "prend seul (istabadda) un qirāḍ d'un étranger",
    "il n'est qu'un salarié qui s'est loué contre une part du profit — et son associé n'a rien en cela",
    "2. L'istibdād de l'emprunteur d'une bête",
    "pour y charger les effets de la šarika",
    "le wāw dans le dire : « et pour la šarika » est pour l'état, et le (in) est redondant",
    "il est seul dans le profit — qui est la location — et il en charge son associé",
    "tu l'aurais louée — ne garantis donc point",
    "il s'arroge son profit et sa perte, qu'il l'ait empruntée avec permission ou sans",
    "3. L'istibdād de qui commerce avec un dépôt",
    "quand bien même il l'aurait mêlé au bien de son commerce",
    "comme dans la Mudawwana —, le profit est alors entre les deux, et la perte sur eux deux",
    "l'attrait des clients et l'attachement des cœurs des bénéficiaires",
    "Le contrôle",
    "Je détermine le concept de la šarika de mufāwaḍa et son jugement.",
    "Je cite ce qui est permis des dispositions de l'un des deux associés de la mufāwaḍa.",
    "J'expose ce en quoi s'arrogent les associés, ou l'un des deux, et l'effet de cela.",
    "L'exploitation",
    "Ibn Rušd al-Ğadd — que Dieu lui fasse miséricorde — a dit : « Faṣl :",
    "sinon s'il partage avec lui les capitaux des biens en propriété commune",
    "tout associé est un indivisaire, et tout indivisaire n'est pas un associé",
    "Et l'indivision est plus générale que l'association.",
    "Dieu — le Très-Haut — les a donc nommés <em>ḫulaṭāʾ</em> (indivisaires)",
    "quand ils ne se furent point associés dans les corps mêmes des brebis",
    "[Al-Muqaddimāt al-Mumahhidāt, 3/33-34, avec aménagement]",
    "Je détermine la relation entre l'indivisaire et l'associé, en employant mes acquis de la science de la logique.",
    "La préparation préalable",
    "Je lis le matn du cours suivant et j'y réponds par ce qui suit",
    "1. Quels sont les jugements des deux associés de la mufāwaḍa ?",
    "2. Par quoi la šarika de mufāwaḍa se corrompt-elle ?",
    "3. Je cite certaines dispositions des deux associés, ou de l'un des deux.",
    "Notes du traducteur",
    "vingtième tranchage du fil",
    "« le vingt-troisième cours » (<em>ad-dars aṯ-ṯāliṯ wa-l-ʿišrūn</em>)",
    "la forme liée (l'ʿinān, où la disposition requiert le consentement de l'autre)",
    "Sur l'istibdād : de la racine b-d-d, l'isolement",
    "la clausule imprimée (<em>fa-lā taḍman</em>) portée telle quelle",
    "l'unique occurrence coranique de <em>ḫulaṭāʾ</em>",
    "An-Nisāʾ 4:12, où les seuls <em>šurakāʾ</em> de biens figurent",
    "Az-Zumar 39:29, « l'homme aux associés rivaux contre l'homme dévoué à un seul homme »",
    "identification purement documentaire, AUCUNE insertion",
    "vingt-deuxième occurrence de la coquille, consignée",
]
missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("sonde absente: " + p[:70])

out = '/home/z/my-project/tr-tmp/19544.html'
open(out, 'w').write(html)
print(f"caractères: {len(html)}")
print(f"sondes: {len(probes) - len(missing)}/{len(probes)}")
if issues:
    print("PROBLÈMES:")
    for i in issues:
        print(" -", i)
    raise SystemExit(1)
print("BUILD OK ->", out)
