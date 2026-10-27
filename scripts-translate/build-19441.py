#!/usr/bin/env python3
# build-19441.py — 19441 « Jurisprudence : les jugements des dispositions
# du prodigue majeur et le rang des tuteurs » (fiqh-tanawi-3, lessons[12],
# badge Leçon 14/33) — suite du bāb, dixième cours consécutif (… → 10e).
# 2 axes : dispositions du prodigue majeur abandonné (Mālik vs Ibn
# al-Qāsim — la cause : ḥağr vs safah ; retournement au rašid ; actes du
# mağhūl al-ḥāl licites à l'unanimité, actes du mineur rejetés — Mawāhib
# al-Ğalīl 5/57 ; al-ġālib ka-l-muḥaqqaq) / rang des tuteurs (père rašid —
# vente en absolu sans énoncé de cause ; non-rašid exclu a fortiori ;
# grand-père, frère, oncle par iṣāʾ ; waṣī — deux dires, ʿAlīš Minḥ
# al-Ğalīl 6/83 vs Dardīr ; nul don, nul bayʿ bi-l-qīma ; juge en dernier
# rang) + huit conditions de la vente judiciaire (orphelinat, abandon,
# propriété, dignité du bien, prise de corps, mise en marché, absence de
# surenchère, justesse du prix — tardud sur l'énoncé des noms des
# témoins) + le gardien (ḥāḍin/maḥḍūn, kāfil al-yatīm — ʿurf comme
# texte, al-maʿrūf ʿurfan ka-l-mašrūṭ šarṭan, la chose facile, Dasūqī
# depuis Ibn Hilāl via al-Bannānī). CINQ fentes de versets remplies :
# an-Nisāʾ 4:5 (entier + extrait) et 4:6 (extrait ×3) — rendus corpus de
# 19407 repris à l'identique, cache vérifié au tour R307. Fente liminaire
# NON VIDE (lundi 12 février 2024 — même date que 19407, 3e du fil) ;
# 0 hadīth ; coquille التعبيم 9e ; contrôle dédoublé (items 1 = 3) ;
# préparation préalable annonçant 19448 (vente du bien-fonds de
# l'orphelin).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19441_{i}.html').read())
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
    'Jurisprudence : les jugements des dispositions du prodigue majeur et le rang des tuteurs',
    'Lundi 12 février 2024',
    'Le bien (<em>al-māl</em>) est la substance même de la vie',
    '(Sourate an-Nisāʾ, verset 5)',
    'Quel est le jugement des dispositions du prodigue ?',
    'Et qui sont les tuteurs de l’interdit, et quels sont leurs rangs ?',
    'quelles sont les conditions de la vente par le juge du bien de l’orphelin ?',
    'dixième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    '(<em>at-taʿbīm</em>)',
    '1. Connaître les jugements des dispositions du prodigue majeur.',
    '2. Connaître le rang des tuteurs de l’orphelin.',
    '3. Saisir les conditions de la vente par le juge du bien de l’orphelin.',
    '4. Distinguer les dispositions du père de celles des autres tuteurs dans le bien de l’interdit.',
    '<h2>Le texte</h2>',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    'est approuvable chez Mālik, non chez Ibn al-Qāsim',
    'quand il devient raisonnable après elle [l’interdiction]… Le tuteur : le père',
    'Puis son tuteur testamentaire, fût-il éloigné.',
    'ne peut-il vendre] que le bien-fonds moyennant l’énoncé de la cause ? Divergence.',
    'Il n’a point de don pour récompense. Puis le juge.',
    'de la prise de corps des témoins de cela, de la mise en marché, de ce que nul n’offre davantage',
    'Nul gardien [n’est tuteur] comme le grand-père [l’est de par son origine].',
    'la ratification de la chose facile, et sur sa mesure, hésitation',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    '« le bien-fonds » (<em>ar-rabʿ</em>) : l’immeuble (<em>al-ʿaqār</em>)',
    '« la justesse du prix » (<em>wa-s-sadād fī ṯ-ṯaman</em>) : payer le prix sans diminution',
    '« sa mesure » (<em>ḥaddi-hi</em>) : sa quantité (<em>qudri-hi</em>)',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du texte les jugements des dispositions du prodigue.',
    '2. J’extrais du texte les tuteurs de l’interdit et leurs rangs.',
    '3. J’extrais du texte les conditions de la vente par le juge du bien de l’orphelin.',
    '<h2>L’analyse</h2>',
    '<h3>Axe premier : les jugements des dispositions du prodigue majeur</h3>',
    'Les dispositions du prodigue [mâle] majeur abandonné (<em>al-muhmal</em>)',
    'licites, définitives et contraignantes, chez Mālik',
    'comme Ibn Kināna et Ibn Nāfiʿ — et c’est le dire retenu (<em>ar-rāğiḥ</em>)',
    'l’objet de la cause suit la cause, en existence comme en inexistence',
    'les dispositions du prodigue majeur abandonné sont rejetées (<em>mardūda</em>)',
    'la cause chez lui est la prodigalité (<em>as-safah</em>) elle-même',
    'en préservant son bien après l’interdiction [qui l’a frappé] et avant le jugement de sa levée (<em>fakk</em>)',
    'les actes de celui dont l’état est inconnu (<em>mağhūl al-ḥāl</em>) sont licites à l’unanimité',
    'les actes du mineur sont rejetés, garçon comme fille',
    '<span>[Mawāhib al-Ğalīl 5/57]</span>',
    'la jeunesse (<em>aṣ-ṣabā</em>) est le lieu habituel de la prodigalité',
    'l’habituel est comme le constaté (<em>al-ġālib ka-l-muḥaqqaq</em>)',
    '<h3>Axe deuxième : le rang des tuteurs de l’interdit et les conditions de la vente par le juge de son bien</h3>',
    'L’islam s’est appliqué à préserver le bien, en sauvegarde des droits de Dieu',
    '(Sourate an-Nisāʾ, extrait du verset 5)',
    '(Sourate an-Nisāʾ, extrait du verset 6)',
    'la protection du bien des prodigues ne s’accomplit que par la tutelle (<em>al-wilāya</em>)',
    '<h4>1. Les tuteurs de l’interdit</h4>',
    '<span>a. Le père raisonnable :</span>',
    'il n’a point de droit à la tutelle',
    'à plus forte raison (<em>bāb awlā</em>)',
    'le grand-père, le frère et l’oncle paternel tiennent lieu du père par son testament (<em>iṣāʾ</em>)',
    'ses actes sont portés, en général, à la justesse et à l’intérêt',
    '<span>b. Le tuteur testamentaire :</span>',
    'parmi ses proches et ses amis et autres de ceux en qui il voit la capacité de cela',
    '1. Le tuteur testamentaire tient lieu du père en toute chose',
    'sont portés sur l’examen et la justesse, jusqu’à établissement du contraire',
    '<span>[Minḥ al-Ğalīl 6/83]</span>',
    '2. Le tuteur testamentaire tient lieu du père dans la vente du bien de l’interdit, hors le bien-fonds',
    'demeure, boutique ou terre',
    'une fois échappé de la main du donataire, n’oblige plus qu’à la valeur',
    'ne vend point à la valeur estimée (<em>bi-l-qīma</em>), contrairement au père — ainsi Dardīr',
    '<span>c. Le juge :</span>',
    'de tuteur testamentaire ni de préposé (<em>muqaddam</em>) institué par un juge',
    '<h4>2. Les conditions de la vente par le juge du bien de l’orphelin</h4>',
    'Le juge vend du bien de l’orphelin ce que la nécessité appelle de vendre, aux conditions suivantes',
    'La constatation de son orphelinat, par des moyens probatoires suffisants',
    'car demeure possible la vie de son père',
    'La constatation de son abandon (<em>ihmāl</em>)',
    'eux sont plus dignes de la vente que le juge',
    'La constatation de sa propriété de ce qui est vendu',
    'le plus digne d’être vendu parmi ses biens',
    'La prise de corps (<em>ḥiyāza</em>) des témoins du bien vendu',
    'ceci que nous avons arpenté et que nous vous avons montré est celui dont nous attestons qu’il appartient à l’orphelin',
    'il dispense du témoignage de la prise de corps',
    'La mise en marché (<em>at-tasawwuq</em>) du bien vendu',
    'afin qu’il ne soit pas vendu au-dessous de son prix',
    'Que nul n’offre davantage sur ce qui en a été donné comme prix',
    'que le prix soit celui du semblable (<em>ṯaman al-miṯl</em>) ou davantage',
    'une chose corporelle immédiate, non des denrées ni à terme',
    'par crainte de la dépréciation et de l’indisponibilité',
    'd’énoncer les noms des témoins de la vente : hésitation (<em>tardud</em>)',
    'le kāfil de l’orphelin — sa mère, son oncle ou autre — n’est point tuteur de lui',
    "un usage (<em>ʿurf</em>) de sa prise en charge de l’affaire de l’orphelin",
    'sa disposition est alors valide du peu et du beaucoup',
    "l’usage est comme le texte (<em>al-ʿurf ka-n-naṣṣ</em>)",
    'le connu par usage est comme le stipulé par condition',
    'le père meurt sans instituer de tuteur testamentaire pour ses enfants',
    'connu pour sa tendresse et sa bonne éducation de l’orphelin',
    'il faut un jugement judiciaire pour vendre son bien',
    'la disposition du gardien (<em>al-ḥāḍin</em>) dans une chose facile du bien du protégé (<em>al-maḥḍūn</em>)',
    'sa mesure renvoie à l’usage, lequel varie selon les personnes, le lieu et le temps',
    'ce qu’ad-Dasūqī a transmis d’Ibn Hilāl par voie d’al-Bannānī',
    '<h2>Le contrôle</h2>',
    '1. J’expose à fond la disposition du gardien dans le bien du protégé.',
    '2. Je détermine les conditions de la vente du bien de l’orphelin, avec leur argumentation.',
    '<h2>L’exploitation</h2>',
    'Dieu le Très-Haut a dit : « Éprouvez les orphelins',
    'Je lis le verset en méditant et j’accomplis ce qui suit',
    'le concept de la raison (<em>ar-rušd</em>) dans la parole du Très-Haut',
    '2. J’indique les jugements contenus dans le verset.',
    'les objectifs (<em>maqāṣid</em>) de l’interdiction dans la Loi'.replace('les objectifs', '3. Je mentionne quelques objectifs'),
    '4. Je recherche dans la Moudawana de la Famille marocaine les règles de la capacité civile et ses types.',
    '<h2>La préparation préalable</h2>',
    '1. Quelles sont les causes qui ne sont tranchées que par les juges ?',
    '2. Quelles sont les causes de la vente du bien-fonds de l’orphelin ?',
    '<h2>Le sens de cette leçon</h2>',
    'Cette leçon achève, sur le prodigue, l’édifice que la précédente avait dressé',
    'la vente du bien-fonds de l’orphelin.</p>',
    '<h2>Notes du traducteur</h2>',
    'le h1 imprimé fait foi : les jugements (<em>aḥkām</em>) des dispositions (<em>taṣarrufāt</em>) du prodigue majeur et le rang (<em>tartīb</em>) des tuteurs',
    '« actes » est ramené à « dispositions », terme de famille (19395, 19407)',
    '(règle av — septième tranchage du fil)',
    'même date que la leçon 19407 (leçon 9 du fil)',
    'troisième fente liminaire renseignée du fichier (après 19383 et 19407)',
    '(6e → 7e → 8e → 9e → 10e) — <em>ad-dars al-ʿāšir</em>',
    'atteint sa neuvième occurrence',
    'l’intermédiaire omis relève de l’interdit lui-même après l’interdiction',
    'déjà traité par la leçon 19407 (son axe troisième)',
    'le glossaire du cours glose <em>ar-rabʿ</em> par <em>al-ʿaqār</em>',
    'la seconde occurrence lit « <em>ʿadam ilġfāʾ zāʾid</em> » (avec <em>ġ</em>)',
    'la première lit « <em>ʿadam ilġāʾ zāʾid</em> » (avec <em>ā</em>)',
    'première occurrence de cette formule axiomatique au fichier',
    'énoncée deux fois dans la leçon : au prodigue et au père',
    'le triptyque étaye tout le volet du gardien',
    'celui qui n’a point de tuteur (<em>man lā walī la-hu</em>)',
    'la défaillance, leçons 19353–19395',
    'le champ propre de la vente judiciaire',
    'sans tutelle légale (mère, oncle, grand-mère)',
    'le kāfil de l’orphelin (<em>kāfil al-yatīm</em>) du commentaire en est l’équivalent',
    'la racine <em>ḥ-ḍ-n</em>, le geste de plier l’objet contre soi',
    '(<em>hiba li-ṯ-ṯawāb</em>)',
    'rendue littéralement ; le sens d’ensemble est clair',
    'les trois rendus français établis par la leçon 19407 sont repris à l’identique',
    'l’extrait de 4:6 à l’épreuve de gestion (deux fois, à l’analyse et à l’exploitation)',
    'les items 1 et 3 du contrôle sont identiques',
    'dédoublement typographique du document source, consigné tel quel, sans rétro-révision (règle ax)',
    'les quatre tâches répètent celles de la leçon 19407',
    'le manuel enchaîne deux leçons sur le même verset de clôture',
    '(doc 19448 : la vente du bien-fonds de l’orphelin)',
    'continuité du fil consignée telle quelle (règle ax)',
]

missing = [p for p in PROBES if p not in html]
if missing:
    issues.append(f"SONDES MANQUANTES ({len(missing)}):")
    for m in missing:
        issues.append("   - " + m[:110])

n = len(html)
print(f"LONGUEUR: {n} caractères")
print(f"SONDES: {len(PROBES) - len(missing)}/{len(PROBES)}")
print(f"guillemets: {html.count('«')} / {html.count('»')}")
print(f"NBSP-br: {html.count(chr(0xA0))} insécables")
if issues:
    print("PROBLÈMES:")
    for i in issues:
        print(" ", i)
    raise SystemExit(1)

with open('/home/z/my-project/tr-tmp/19441.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("OK -> tr-tmp/19441.html")
