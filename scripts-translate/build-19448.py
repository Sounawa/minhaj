#!/usr/bin/env python3
# build-19448.py — 19448 « Jurisprudence : les jugements de la vente du
# bien-fonds de l'orphelin » (fiqh-tanawi-3, lessons[13], badge Leçon 15/33)
# — suite du bāb, onzième cours consécutif (… → 11e). 3 axes : dispositions
# du tuteur (laisser de la préemption et du talion — naẓar wa-sawād,
# dispositions māḍiya ; pardon du tuteur — pas de pardon gratuit, dédommage
# sur son bien, Mudawwana) / dix causes réservées aux juges (rašd/safah,
# waṣiyya, ḥubs muʿaqqab, amr al-ġāʾib, nasab, ḥudūd, qiṣāṣ, māl yatīm —
# gravité, droit de Dieu, droit de l'absent, māniʿ ḫalw lā māniʿ ğamʿ,
# juge atteignable ḥaqīqatan aw ḥukman) / neuf causes de la vente du
# bien-fonds (besoin, ġibṭa d'un tiers, muwaẓẓaf kharāj/loyer, ḥiṣṣa,
# qillat ġalla — istibdāl bi-ḫilāf-hi, voisins mauvais, associé pressant —
# indivisible, départ de la ʿimāra, ruine + ʿawlā) + maqāṣid (justice,
# dignité, catégories faibles). AUCUNE citation (0 āya, 0 hadīth — 2e
# leçon du fichier sans citation, après 19395). Exploitation : poème
# didactique (naẓm) de Badr ad-Dīn ad-Damāmīnī rapporté par al-Bannānī
# [al-Fatḥ ar-Rabbānī 5/541] — quart de l'orphelin, jugement/dépense/
# prétention d'associé/indivisible/occupation/démolition/remplacement/
# prix/licite/profit lourd. Préparation préalable → 19449 (ṣulḥ : vente ou
# donation ; sections du ṣulḥ). Fente liminaire NON VIDE (lundi 12 février
# 2024 — même date que 19407 et 19441, 4e du fil) ; at-taʿbīm 10e.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19448_{i}.html').read())
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
    'Jurisprudence : les jugements de la vente du bien-fonds de l’orphelin',
    'Lundi 12 février 2024',
    'La Loi a préféré la conciliation (<em>aṣ-ṣulḥ</em>) entre les gens',
    'l’arbitrage des gens d’expérience et d’intégrité',
    'dans certaines causes touchant l’interdit (<em>al-maḥğūr ʿalay-hi</em>)',
    'Quelles sont les causes où l’arbitrage n’est point admis dans les affaires de l’interdit ?',
    'Et quelles sont les causes qui poussent à la vente de son bien-fonds ?',
    'onzième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    '(<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Définir les causes qui ne sont jugées que par les juges.',
    '2. Connaître les causes de la vente du bien-fonds de l’orphelin.',
    '3. Saisir les effets de la consommation du bien de l’orphelin.',
    '<h2>Le texte</h2>',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    '« Il appartient au tuteur (<em>al-walī</em>) de laisser la préemption (<em>at-tašaffuʿ</em>) et le talion, et ils tombent tous deux',
    'et il ne pardonne point…',
    'de la raison et de son contraire, du testament, du habous suivi de descendance',
    'de l’affaire de l’absent et de la filiation…, d’un châtiment fixé, du talion et du bien de l’orphelin',
    'Et son bien-fonds n’est vendu que pour un besoin, ou pour une tentation du prix',
    'ou pour être chargé d’une redevance, ou être une quote-part',
    'ou que son rendement a faibli — on le remplace alors par son contraire…',
    'ou pour des voisins mauvais, ou pour que son associé en veuille la vente et qu’il n’a point de bien',
    'ou par crainte du départ de la construction ou de la ruine — et nul bien à lui —, ou qu’il en a, et la vente est préférable',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    '« Quiconque a la charge de l’affaire d’un autre est son tuteur. »',
    '<span>[Maqāyīs al-luġa, entrée w-l-y, 6/141]</span>',
    '« La raison » (<em>ar-rašd</em>) : la droiture (<em>aṣ-ṣalāḥ</em>)',
    'son contraire de la prodigalité (<em>as-safah</em>)',
    '« Le habous suivi de descendance » (<em>al-ḥubs al-muʿaqqab</em>)',
    '« La tentation du prix » (<em>al-ġibṭa</em>)',
    'd’une valeur d’un tiers, tout en demeurant licite',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. Je détermine les jugements de l’interdiction (<em>al-ḥağr</em>) mentionnés dans le texte.',
    '2. J’extrais du texte les dispositions du tuteur.',
    '3. J’indique, à travers le texte, les questions mentionnées incidemment dans le volet de l’interdiction.',
    '<h2>L’analyse</h2>',
    '<h3>Axe premier : les dispositions du tuteur</h3>',
    'La tutelle de l’interdit requiert la validité des dispositions du tuteur',
    '<h4>1. Le laisser de la préemption et du talion</h4>',
    'à bon escient et avec justesse (<em>naẓar wa-sawād</em>) pour le droit de l’interdit',
    'les dispositions du tuteur sont licites et exécutoires (<em>māḍiya</em>)',
    'de laisser le talion pour les membres de celui qui a blessé le mineur',
    'il n’a point, une fois grandi, de talion sur le malfaiteur',
    '« ou qu’un tuteur testamentaire ou un père a fait tomber sans considération »',
    '<h4>2. Le pardon du tuteur</h4>',
    'gratuitement (<em>tiṭāʿan</em>), ni pour un montant inférieur à la diya (<em>ad-diya</em>)',
    'sauf pour la gêne (<em>ʿusr</em>) du malfaiteur — comme il viendra au chapitre des blessures',
    'il dédommage l’interdit sur son propre bien pour ce qu’il lui a fait perdre par son pardon',
    'ainsi qu’il est consigné dans la Moudawwana (<em>al-Mudawwana</em>)',
    '<h3>Axe deuxième : les causes qui ne sont jugées que par les juges</h3>',
    'à l’exclusion des arbitres — par voie d’énumération limitative (<em>ʿalā sabīl al-ḥaṣr</em>)',
    'à cause de leur gravité (<em>ḫuṭūr</em>)',
    'nul ne juge que tel est raisonnable ou prodigue, en cas de dispute à ce sujet, sinon le juge',
    'en préposant un tuteur testamentaire à un autre',
    'les légataires multiples soient associés dans la tutelle ou que l’un d’eux en ait la charge seule',
    'comme le habous constitué à une personne et à sa descendance — car le jugement y tombe sur un absent',
    'quant au habous non suivi de descendance, comme le habous constitué à tel et à tel, il n’exige point la voie judiciaire',
    'ce qui est vendu sur lui pour la dépense de sa femme ou de son enfant, ou pour sa dette',
    '« tel est de la filiation de tel » ne s’établit que par jugement du juge',
    'les détermine, les établit ou les dénie — en protection de la sécurité et de la salubrité de la société',
    'de la personne ou des membres. Le compilateur a mentionné ces causes ici pour le rassemblement des analogues (<em>ğamʿ an-naẓāʾir</em>)',
    'sa mise en prodigalité et sa mise en raison (<em>tasfīh</em> et <em>taršīd</em>), sa vente, son partage',
    'La cause pour laquelle ces dix causes ne sont point jugées que par le juge est la gravité de ces causes',
    'ou leur attachement au droit de Dieu le Très-Haut, ou au droit de quelqu’un qui n’est point présent',
    'une cause empêchant par sa vacance, non par son agrégat (<em>māniʿ ḫalw lā māniʿ ğamʿ</em>)',
    'quand il existe un juge et que l’on n’atteint pas de lui de façon impossible, réellement (<em>ḥaqīqatan</em>) ou juridiquement (<em>ḥukman</em>)',
    '<h3>Axe troisième : les causes de la vente du bien-fonds de l’orphelin</h3>',
    'ne vend point son bien-fonds, sauf s’il énonce la cause de la vente',
    'elles sont, sur l’ordre du texte :',
    'telle la dépense (<em>nafaqa</em>) ou l’acquittement d’une dette qui ne s’acquitte que par le prix du vendu',
    'd’une valeur d’un tiers, au-delà de son semblable parmi les biens licites',
    'de kharāj (<em>ḫarāğ</em>) ou de loyer, annuel ou mensuel',
    'un bien-fonds qui ne porte point de redevance chaque année ou chaque mois — afin que le kharāj ne le consume point',
    'en protection du bien de l’orphelin contre les dispositions de quelques-uns des associés',
    'et c’est encore plus digne (<em>awlā</em>) quand il n’a point de rendement',
    'il est alors vendu pour qu’on le remplace par son contraire (<em>ḫilāf</em>)',
    'dont on ne craint point le mal — en religion, en entendement, en bien et en honneur',
    'de ce qui ne se partage point, et que l’orphelin n’a point de bien avec quoi acheter la part de l’associé',
    'le départ de la construction (<em>al-ʿimāra</em>), de sorte qu’il devienne isolé (<em>munfarid</em>) et que son prix diminue',
    'La crainte de la ruine (<em>al-ḫarāb</em>) du bien-fonds',
    'mais que la vente soit plus digne pour lui que la restauration, pour un but parmi les buts',
    'certains des objectifs (<em>maqāṣid</em>) que le fiqh islamique s’attache à établir, à faire valoir et à fixer',
    'tel l’objectif juridique (<em>ḥuqūqī</em>) par la réalisation de la justice entre les gens en général',
    'des procédures préventives et des initiatives pratiques qui respectent les droits des catégories faibles',
    '<h2>Le contrôle</h2>',
    '1. J’expose les causes qui ne sont jugées que par les juges, avec l’argumentation.',
    '2. Quelles sont les conditions de la vente du bien-fonds de l’orphelin, avec l’argumentation ?',
    '<h2>L’exploitation</h2>',
    'un poème bref de Badr ad-Dīn ad-Damāmīnī',
    '« Si le quart d’un orphelin est vendu, alors vendez-le — pour des causes que l’homme d’intelligence dénombre avec son entendement :',
    'un jugement prononcé, une dépense indispensable, la prétention d’un associé — qui poussent à la vente de ce qu’il n’y a point de moyen de partager ;',
    'et la crainte qu’autrui s’y installe, ou la crainte de sa démolition — et le remplacement du tout, ou d’un bien-fonds déterminé ;',
    'et la dépense, en prix, de beaucoup de licite — et la légèreté du profit qu’il porte, ou la lourdeur de sa charge. »',
    '<span>[al-Fatḥ ar-Rabbānī fī-mā duhila ʿan-hu az-Zarqānī 5/541]</span>',
    'Je contemple ce poème et je réponds à ce qui suit :',
    '1. J’en extrais les causes de la vente du bien-fonds de l’orphelin, et je compare avec la leçon.',
    '2. Je donne une notice brève sur ad-Damāmīnī, auteur du poème — que Dieu lui fasse miséricorde.',
    '<h2>La préparation préalable</h2>',
    '1. Quand la conciliation (<em>aṣ-ṣulḥ</em>) est-elle une vente ? Et quand est-elle une donation ?',
    '2. Je détermine les sections du ṣulḥ et leurs jugements.',
    '<h2>Le sens de cette leçon</h2>',
    'voici le monopole judiciaire — les causes où l’arbitre n’a point d’accès',
    'Dix causes sont réservées aux juges',
    'le bien-fonds de l’orphelin ne se vend pas parce qu’un tuteur le veut, mais parce qu’un intérêt dit son nom',
    'Le poème d’ad-Damāmīnī condense le catalogue en registre didactique',
    'la préparation préalable ouvre la salle suivante : la conciliation — quand elle vaut vente, quand elle vaut donation',
    '<h2>Notes du traducteur</h2>',
    'l’étiquette GT du registre rend le titre par « Arrêts de jurisprudence sur la vente des biens d’un orphelin »',
    '(règle av — huitième tranchage du fil)',
    'NON VIDE au contrôle — « lundi 12 février 2024 »',
    'trois leçons consécutives parues le même lundi',
    'quatrième fente liminaire renseignée du fichier',
    'la coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa dixième occurrence',
    'deuxième leçon du fichier sans aucune citation (0 āya, 0 hadīth — après 19395)',
    'aucune vérification de cache requise ce tour',
    'le document écrit « <em>mugāyīs al-ġa</em> » (la graphie du mot « langue » y est dépourvue du lām initial)',
    'le compilateur annonce « dix causes »',
    'écart de compte consigné tel quel, sans rétro-révision (règle ax)',
    'une cause empêchant par sa vacance, non par son agrégat',
    'attribuée nommément à la Moudawwana (<em>al-Mudawwana</em>)',
    'comme il viendra au chapitre des blessures',
    'disposé dans le document en table à deux colonnes, direction imposée « <em>ltr</em> »',
    'le « quart » (<em>ar-rubʿ</em>) du poème désigne le bien-fonds ou la quote-part de bâtiment de l’orphelin',
    'lit « <em>ḥal</em> » pour « <em>ḥalāl</em> » — coquille translittérée',
    'Badr ad-Dīn Muḥammad ibn Aḥmad ad-Damāmīnī (Le Caire, 861–928 H)',
    'hāšiyya célèbre sur le Šarḥ al-iḍāḥ d’al-ʿUqbarī en morphologie',
    'al-Bannānī = Muḥammad ibn Aḥmad al-Bannānī al-Fāsī (m. 1180 H)',
    '« <em>yaḫtaḍu</em> » pour « <em>yaḫtaṣṣu</em> »',
    '« <em>ibā l-quḍāt</em> » pour « <em>illā li-l-quḍāt</em> » (le sauf y est lu comme la particule du serment)',
    'le renvoi vise les huit conditions de la leçon 19441',
    'le poème condense le catalogue en registre didactique',
    'la tâche 1 de l’exploitation, laissée à l’élève',
    'deux items annonçant la leçon à venir (doc 19449 : les sections du ṣulḥ et leurs jugements)',
    'la boucle du fil est bouclée d’un tour à l’autre (règle ax)',
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

out = f'/home/z/my-project/tr-tmp/19448.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
