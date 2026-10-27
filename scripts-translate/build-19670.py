#!/usr/bin/env python3
# build-19670.py — 19670 « Jurisprudence : les jugements de la šarika de
# ʿinān » (fiqh-tanawi-3, lessons[27], badge Leçon 29/33) — vingt-cinquième
# cours imprimé (25e confirmation : 22e šarika → 23e mufāwaḍa → 24e
# dispositions+litige → 25e ʿinān). DEUX axes h3 : (1) définition (Ibn
# ʿArafah : l'associé spécifié, non la mufāwaḍa ; langue = la bride, l'image
# de l'avant-tête) + jugement (Ibn Rušd, Muqaddimāt 3/37 : licite entre tous,
# contraignante pour les marchés sans enchère) ; (2) le licite — quatre items
# : accord sur la dépense (poussins/couvaison, chaque oiseau à son maître) /
# wakāla restreinte à l'achat (le dire « pour moi et pour toi » fonde la
# šarika d'après-coup) / le comptant pour l'autre (salaf qui attire le
# profit — ğarr an-nafʿ établi R321 — sans corrompre la vente ; le juʿl de
# l'avanceur ; le ḥabs comme le gage rahn, exception du ladd craint) /
# contrat contenant l'avance (limite : kabasīra — expérience du marché,
# wuğāha). Fentes : AUCUNE (0 āya / 0 hadīth — 6e tour sans protocole
# triple) ; exploitation = Ibn Rušd al-Ğadd, al-Bayān wa-t-Taḥṣīl 12/5
# (Sahnūn/Ibn al-Qāsim/Mālik : le lien vs la capture du regard du frère) ;
# at-taʿbīm 24e occ. ; préparation préalable → ğabr et ʿamal (19671). Fil :
# 19544 avait annoncé la forme liée « aux leçons suivantes de l'imprimé » —
# refermé ici.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19670_{i}.html').read())
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
    "Jurisprudence : les jugements de la šarika de ʿinān",
    "l'homme discerne la voie de la droiture et de la conduite droite",
    "c'est la šarika de ʿinān",
    "Quel est donc le reste des dispositions des deux associés de mufāwaḍa ?",
    "vingt-cinquième leçon, au profit des élèves et des élèves de la troisième année secondaire",
    "at-taʿbīm al-ʿatīq",
    "1. Connaître le concept de la šarika de ʿinān et son jugement.",
    "2. Se représenter les jugements de la šarika de ʿinān dans mes transactions financières.",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Et s'ils conditionnent la négation de l'istibdād, c'est la ʿinān",
    "au détenteur d'oiseaux et à la détentrice de volailles de s'accorder sur la compagnie dans les poussins",
    "achète pour moi et pour toi — c'est la wakāla",
    "passe-moi le comptant de ma part, s'il ne dit pas : et je te la vends",
    "sauf à dire : et retiens-la — elle est alors comme le gage",
    "Et si autre que l'acheteur fait l'avance, c'est licite — sauf pour l'expérience du marché de l'acheteur",
    "wa-nqud :",
    "acquitte le prix au comptant, en espèces",
    "baṣīra :",
    "science et expérience",
    "1. J'extrais du texte quelques dispositions des deux associés.",
    "2. Je détermine, à travers le texte, le concept de la šarika de ʿinān et son jugement.",
    "3. Je montre du texte ce qui est permis aux deux associés de ʿinān et ce qui ne l'est pas.",
    "La présente leçon comprend ce qui suit",
    "Axe premier : la définition de la šarika de ʿinān et son jugement",
    "a. En langue :",
    "avec la kasra de la ʿayn et l'allègement de la nūn",
    "le nom de ce par quoi on conduit la bête",
    "le nom de la pluie ou du nuage",
    "b. En convention :",
    "l'ʿAllāma Ibn ʿArafah — que Dieu lui fasse miséricorde — a dit",
    "la compagnie de l'associé spécifié, non de la mufāwaḍa",
    "la compagnie sur une chose déterminée",
    "à la condition que chacun des deux ne vende que par la permission de l'autre",
    "[Le Muḫtaṣar al-fiqhī d'Ibn ʿArafah 7/17, avec retouche]",
    "ne s'arrogER aucune action de la compagnie sans la permission de son associé et à sa connaissance",
    "comme s'il avait pris son ʿinān, à savoir son avant-tête",
    "pour ne faire aucune action sans sa permission",
    "2. Son jugement",
    "Ibn Rušd — que Dieu lui fasse miséricorde — a dit d'elle",
    "Elle est licite entre tous les gens lorsqu'ils s'accordent sur elle et l'agrèent",
    "contraignante pour les gens des marchés en ce qu'ils ont acheté pour le commerce sans mise aux enchères",
    "[al-Muqaddimāt al-Mumahhadāt 3/37]",
    "Axe deuxième : ce qui est licite dans la šarika de ʿinān",
    "1. L'accord des deux associés sur la dépense",
    "s'accorder à dépenser chacun sur ce qu'il tient en main du bien de la compagnie",
    "comme les poules et leur semblable, pour le besoin qu'en a la compagnie de la couvaison",
    "à la condition que chaque oiseau demeure dans la propriété de son détenteur",
    "2. La wakāla dans la šarika de ʿinān",
    "une wakāla de sa part dans la moitié de la marchandise, une wakāla restreinte qui ne dépasse pas l'achat",
    "ce wakīl n'a donc pas le droit de vendre la moitié de son associé sans sa permission",
    "indique qu'après l'achat il y a entre eux deux une šarika",
    "s'est tu dessus pour ce qu'il en est su",
    "le versant de la wakāla n'eût demeuré caché que s'il n'en avait pas fait mention",
    "3. Le comptant de l'un des deux associés pour l'autre",
    "acquitte le comptant qui échoit à ma part",
    "un usage connu de sa part envers lui",
    "une avance qu'il lui fit tout en prenant en charge pour lui l'achat",
    "que l'ordonnateur ne dise pas : « et moi, je la vends, ou je te la confie en location »",
    "une avance qui attire le profit, à savoir pour l'avanceur du comptant",
    "ne corrompt pas la vente quand bien même la condition ne serait pas levée, faute d'effet sur l'essence même de la vente",
    "il a un don récompensé (juʿl) pareil",
    "une avance dégagée de toute condition, qui n'ouvre que la revendication",
    "passe-le pour moi et retiens-la jusqu'à ce que tu en reçoives le prix de moi",
    "en ce qu'il est le plus digne d'elle et dans la garantie",
    "que pèse sur lui sa garantie à la manière de la garantie du gage",
    "si l'ordonnateur est de ceux dont on craint l'opposition",
    "4. Le contrat contenant l'avance est licite",
    "je te fais l'avance de ce qui échoit à ta part dans son prix",
    "un usage connu de sa part, sans compensation",
    "a l'expérience de la vente et de l'achat, la connaissance et la considération",
    "cela l'empêche, car cela attire le profit pour l'avanceur",
    "Si l'avanceur est un étranger qui ne vise que le profit de l'ordonné, c'est licite",
    "la Loi sage prend ses précautions et se garde de tout ce qui pourrait conduire à faire perdre les droits en bloc",
    "la considération des issues est tenue pour significative par la Loi",
    "1. Je connais la šarika de ʿinān et je montre son jugement.",
    "2. Je montre ce qui est permis et ce qui ne l'est pas dans la šarika de ʿinān.",
    "Sahnūn a dit : Ibn al-Qāsim m'a informé de Mālik",
    "lui faire l'avance d'or et à en sortir le semblable",
    "sur le mode du lien et de l'usage connu, de lui à son frère",
    "il n'a besoin de lui en rien sinon de la compagnie bienveillante",
    "son regard dans la vente et l'achat, ou son influence dans le commerce, et son enseignement",
    "[al-Bayān wa-t-Taḥṣīl 12/5]",
    "1. Je recherche, à travers le texte, les dispositions des deux associés de mufāwaḍa.",
    "le concept des deux compagnies : le ğabr et le travail, et j'extrais du texte leur jugement.",
    "Notes du traducteur",
    "vingt-deuxième tranchage du fil",
    "ad-dars al-ḫāmis wa-l-ʿišrūn",
    "vingt-deuxième (la šarika) → vingt-troisième (la mufāwaḍa) → vingt-quatrième (les dispositions de l'associé et le litige) → vingt-cinquième (la ʿinān)",
    "de la racine ʿ-n-n, la bride et la rêne",
    "la forme liée, où la disposition requiert le consentement de l'autre — le fil annoncé est ici refermé",
    "le mâle et la femelle ; la compagnie porte sur les poussins",
    "l'avanceur acquitte le prix, l'ordonnateur le lui rendra à l'échéance",
    "le terme établi <em>ğarr an-nafʿ</em>, de la leçon des dispositions de l'associé",
    "<em>rahn</em>, terme fixé au registre",
    "fixé au registre depuis les leçons du ḍamān",
    "Mālik condamne l'avance faite pour s'attacher le regard du frère dans la vente",
    "<em>wuğāha</em> est le rang qui fait la valeur et la considération de l'homme au marché",
    "seule la wakāla aurait pu passer inaperçue",
    "al-Bayān wa-t-Taḥṣīl, l'œuvre du grand Ibn Rušd (al-Ğadd)",
    "<em>ar-rifq</em>, terme du registre",
    "la kabasīra du matn et le regard de l'exploitation sont une même frontière",
    "19671, « les jugements de la šarika du ğabr et de la šarika du travail »",
    "Le fiqh : les règles de l'association inan (širka ʿinān) (2)",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19670.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
