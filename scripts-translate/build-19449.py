#!/usr/bin/env python3
# build-19449.py — 19449 « Jurisprudence : les sections de la conciliation
# et leurs jugements » (fiqh-tanawi-3, lessons[14], badge Leçon 16/33) —
# suite du bāb, douzième cours consécutif (… → 12e). 3 axes : concept et
# jugement du ṣulḥ (Ibn Fāris ṣ-l-ḥ 3/303 ; définition d'Ibn ʿArafa —
# transfert d'un droit ou d'une prétention moyennant contrepartie pour
# lever un différend ; mandūb de par sa substance, obligation à taʿyīn de
# la maṣlaḥa, interdit/réprobé selon la mafsada ; hadīth d'Abū Hurayra —
# Sunan Abī Dāwūd ; fente de verset an-Nisāʾ 4:114 — protocole triple,
# cache vérifié, rendu de la main du traducteur) / sections et conditions
# (iqrār/sukūt/inkār × vente/louage/donation ; vente du réclamé —
# conditions de la vente ; louage — muʿayyan vs maḍmūn fī ḏ-ḏimma,
# faḫḫ interdit, hadīth du kālīʾ — al-Bayhaqī ; donation = ibrāʾ — nul
# accueil, nul renouvellement de possession) / ce par quoi et ce sur quoi
# (or-argent ṣarf — deux conditions ; iftidāʾ du jāhim ; silence — ḥabs
# wa-taʿzīr ; déni — trois conditions selon Mālik, tuhma fasād) + fruits.
# Exploitation : cinq exemples d'az-Zarqānī [Šarḥ az-Zarqānī avec la
# hāšiyya d'al-Bannānī 6/8-9]. Préparation préalable → 19452 (ṣulḥ de
# l'injuste et tuteur du sang ; rupture ; héritiers/épouse ; sangs).
# Fente liminaire VIDE ; at-taʿbīm 11e occurrence (+ al-ʿatīq).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19449_{i}.html').read())
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
    'Jurisprudence : les sections de la conciliation et leurs jugements',
    '<dt></dt>\n<dd></dd>',
    'par la nature du mélange des hommes, par l’effet des passions de l’âme et des penchants humains',
    'qui détourne les accusations, écarte les soupçons, contente les deux parties ou les deux adversaires',
    'Qu’est-ce que la conciliation ? Et quelles sont ses sections ? Et quel est son jugement ?',
    'douzième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    '(<em>at-taʿbīm al-ʿatīq</em>)',
    '1. Définir le concept de la conciliation, ses sections et son jugement.',
    '2. Saisir les effets qui en découlent et la sagesse de sa légitimation.',
    '3. Se représenter les jugements de la conciliation dans les transactions financières.',
    '<h2>Le texte</h2>',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    '« La conciliation sur autre que ce qui est réclamé : vente ou louage ; et sur une part de ce qui est réclamé : donation.',
    'Et elle est admise pour une dette avec ce par quoi l’on vend, et pour de l’or avec de l’argent, ou l’inverse',
    's’ils sont licites et payés sur-le-champ — comme cent dinars et dirhams pour leurs deux cents',
    'et sur le rachat (<em>al-iftidāʾ</em>) de celui qui a prêté serment, ou sur le silence, ou sur le déni',
    's’il est admis sur la prétention de chacun et sur la manifeste du jugement',
    '<h2>La compréhension</h2>',
    '<h3>Le commentaire</h3>',
    'Le louage (<em>al-iğāra</em>) : transfert de la jouissance d’une chose par compensation (<em>bi-ʿiwaḍ</em>)',
    'La donation (<em>al-hiba</em>) : transfert de la chose même ou de ses jouissances sans compensation',
    '<h3>La synthèse du contenu du texte</h3>',
    '1. J’extrais du texte les sections de la conciliation qui y sont mentionnées.',
    '2. J’extrais du texte quand se rompt validement la conciliation.',
    '3. J’extrais du texte le jugement de la conciliation pour l’injuste (<em>aẓ-ẓālim</em>).',
    '<h2>L’analyse</h2>',
    '<h3>Axe premier : le concept de la conciliation et son jugement</h3>',
    '<span>a. Dans la langue :</span>',
    '« La ṣād, le lām et le ḥāʾ ont un seul fond, qui désigne l’opposé de la corruption.',
    '<span>[Maqāyīs al-luġa d’Abū al-Ḥusayn Aḥmad ibn Fāris, entrée ṣ-l-ḥ, 3/303]</span>',
    '<span>b. En terminologie :</span>',
    '« Transfert d’un droit ou d’une prétention moyennant une contrepartie, pour lever un différend ou la crainte de sa survenue. »',
    '<span>[al-Mukhtaṣar al-fiqhī 6/477]</span>',
    '<h4>2. Son jugement</h4>',
    '« De par sa substance, il est recommandé (<em>mandūb</em>)',
    'quand on spécifie son intérêt',
    'quand il entraîne une corruption dont le détournement est obligatoire, ou [dont le détournement est] préférable',
    '<span>[al-Mukhtaṣar al-fiqhī, vol. 6/478-477]</span>',
    'd’Abū Hurayra — que Dieu l’agrée : l’Envoyé de Dieu ﷺ a dit',
    '« La conciliation est admise entre les musulmans, sauf une conciliation qui rend licite un interdit, ou interdit un licite',
    'et les musulmans sont aux conditions qu’ils posent. »',
    '<span>[Sunan d’Abī Dāwūd, livre du jugement, chapitre sur la conciliation]</span>',
    'parmi les plus nobles actes de dévotion (<em>qurbāt</em>) et les plus grands actes d’obéissance',
    '« Pas de bien dans beaucoup de leurs consultations secrètes, sauf si l’un ordonne une aumône, ou une œuvre convenable, ou une réconciliation entre les gens',
    'et quiconque fait cela en quête de l’agrément de Dieu — Nous lui donnerons bientôt une récompense immense. »',
    '(Sourate an-Nisāʾ, verset 114)',
    '<h3>Axe deuxième : les sections de la conciliation et leurs conditions</h3>',
    'conciliation sur reconnaissance (<em>iqrār</em>), ou sur silence (<em>sukūt</em>), ou sur déni (<em>inkār</em>)',
    'elle est vente, ou louage, ou donation, selon ce par quoi l’on concilie (<em>al-muṣālaḥa bi-hi</em>)',
    '<span>a. Que la conciliation soit une vente de ce qui est réclamé</span>',
    'on y exige alors les conditions de la vente',
    'apparents (<em>ẓāhir</em>), dont on jouit, que l’on est capable de livrer, et l’absence de leurs empêchements',
    'un objet d’apparat (<em>ʿaraḍ</em>), ou une voiture, ou de la nourriture',
    'c’est alors une compensation (<em>muʿāwaḍa</em>)',
    'comme celui qui concilie une personne sur sa marchandise contre un vêtement, à condition de ne point le porter, ou de ne point le vendre',
    'une chose inconnue, ou sur un terme inconnu, ou contre une chose impure, ou que l’on n’est point capable de livrer',
    'alors cela n’est point admis, ni valide',
    '<span>b. Que la conciliation soit un louage</span>',
    'comme habiter une demeure, ou l’usage d’une voiture, durant une année',
    'garanties dans la dette (<em>maḍmūna fī ḏ-ḏimma</em>)',
    'en l’absence d’annulation d’une dette par une dette (<em>faḫḫ</em>)',
    'ce n’est autre que la vente d’une chose déterminée contre des jouissances',
    'comme des dirhams, ou un vêtement décrit',
    'car cela est l’annulation d’une dette par une dette (<em>faḫḫ</em>)',
    'et le Prophète ﷺ a interdit la vente de la dette par la dette',
    '« a interdit la vente du différé (<em>al-kālīʾ</em>) par le différé »',
    '<span>[as-Sunan al-kubrā d’al-Bayhaqī, livre des ventes, chapitre de ce qui est rapporté sur l’interdiction de vendre la dette par la dette]</span>',
    '<span>c. Que la conciliation soit une donation</span>',
    'la part laissée étant donation, et dégagement de la dette du débiteur (<em>ibrāʾ</em>)',
    'telle qu’elle exigerait l’accueil (<em>qabūl</em>) du demandeur avant la mort du donateur, qui est le demandeur',
    'nul accueil n’est exigé, et nul renouvellement de prise de possession',
    '<h3>Axe troisième : ce par quoi la conciliation est admise, ce sur quoi elle est admise, et leurs conditions</h3>',
    'avec ce par quoi la compensation est valide',
    'contre de l’argent accéléré, ou contre de l’or',
    'à condition que la contrepartie reçue s’acquitte sur-le-champ (<em>ḥulūl</em>)',
    'que son ajournement ne soit point stipulé, et qu’il soit accéléré en acte',
    'et sur ce modèle, la conciliation d’une monnaie contre une autre monnaie',
    'serment réclamé du défendeur pour une prétention nue, ou avec un témoin, quand bien même il saurait son innocence',
    'ce que le silence requiert, et ce qui en découle de détention (<em>ḥabs</em>) et de correction (<em>taʿzīr</em>)',
    'au titre du contrat et de la manifeste de la situation (<em>ẓāhir al-ḥāl</em>)',
    'si le déniant est véridique, ce qui est pris de lui est illicite — comme il le mentionnera ensuite ; sinon, licite',
    'trois conditions selon Mālik — qui est la doctrine (<em>al-maḏhab</em>)',
    'l’emploi absolu de la prétention pour les deux est un usage métonymique (<em>mağāz</em>)',
    '« il n’est point en ma possession ce que tu réclames contre moi »',
    'la condition est que la conciliation ne soit admise que sur la prétention du demandeur seulement',
    '« et sur la manifeste du jugement » — c’est-à-dire le légal (<em>aš-šarʿī</em>)',
    'qu’il n’y ait point là de soupçon de corruption (<em>tuhma fasād</em>)',
    '<span>Des fruits de cette leçon :</span>',
    'ainsi les âmes se clarifient, les rancunes s’en vont, et les cœurs se rassemblent',
    '<h2>Le contrôle</h2>',
    '1. J’expose le concept de la conciliation.',
    '2. Je clarifie les sections de la conciliation et les conditions de chaque section.',
    '3. J’expose l’effet de la conciliation dans les transactions et les dispositions des gens.',
    '<h2>L’exploitation</h2>',
    'L’illustre az-Zarqānī — que Dieu lui fasse miséricorde — a dit',
    '« Exemple de celui qui réunit les trois conditions',
    'dix tenues (<em>ḥulla</em>) exigibles',
    'pour huit, accélérées, ou pour un objet d’apparat exigible',
    'Et exemple de ce qui est admis sur la prétention d’eux deux, mais empêché sur la seule manifeste du jugement',
    'le demandeur a ajourné son associé, ou a remis une part de son droit et ajourné le reste',
    's’est racheté du serment (<em>iftaḍā min al-yamīn</em>) par ce qu’il s’est engagé à payer au terme',
    'car c’est une avance (<em>salf</em>) entraînant un avantage',
    'Et exemple de ce qui est empêché sur la prétention d’eux deux',
    'Ibn Rushd a rapporté l’accord sur sa corruption',
    'd’avance avec augmentation (<em>salf bi-ziyāda</em>) et de change ajourné (<em>aṣ-ṣarf al-muʾaḫḫar</em>)',
    'Et exemple de ce qui est empêché sur la prétention du demandeur seul',
    'pour cent dirhams à terme — cela est empêché sur la prétention du demandeur seul',
    'Et exemple de ce qui est empêché sur la prétention du défendeur seul',
    'dix ardabbes (<em>arḍabb</em>) de blé d’un prêt (<em>qarḍ</em>)',
    '« Il ne te doit que cinq, d’un salam (<em>salaf</em>) »',
    'car la nourriture du prêt (<em>qarḍ</em>) peut être vendue avant la prise de possession',
    'car la nourriture du salam (<em>as-salam</em>) ne peut être vendue avant la prise de possession',
    '<span>[Šarḥ az-Zarqānī sur le Mukhtaṣar de Khalīl, avec la hāšiyya d’al-Bannānī 6/8-9]</span>',
    'et sa cause (<em>ʿilla</em>) ; et je compare ce qu’il comporte avec ce qui est présent dans la leçon',
    '<h2>La préparation préalable</h2>',
    '1. Quand la conciliation se rompt-elle, et quand ne se rompt-elle point ?',
    '2. Quand est admise la conciliation de quelques héritiers avec l’épouse, et quand ne l’est-elle point ?',
    '3. Quel est le jugement de la conciliation pour les sangs (<em>ad-dimāʾ</em>) ? Et quelles sont ses conditions ?',
    '<h2>Le sens de cette leçon</h2>',
    'La définition d’Ibn ʿArafa en donne la mécanique',
    'le ṣulḥ est donc un acte patrimonial au service de la paix',
    'le hadīth du différé vendu au différé',
    'la rupture du ṣulḥ, la conciliation des héritiers avec l’épouse, et le ṣulḥ pour les sangs',
    '<h2>Notes du traducteur</h2>',
    'l’étiquette GT du registre rend le titre par « Jurisprudence, sections de réconciliation et ses décisions »',
    '(règle av — neuvième tranchage du fil)',
    'VIDE au contrôle — cinquième leçon du fil à fente vide',
    'la coquille « <em>at-taʿbīm</em> » pour « <em>at-taʿlīm</em> » atteint sa onzième occurrence',
    'DEUX hadīths et UNE fente de verset remplie',
    'an-Nisāʾ 4:114 vérifiée lettre à lettre',
    'aucun rendu établi de 4:114 au corpus (la leçon 19407 n’a établi que 4:5 et 4:6)',
    '« (Sourate an-Nisāʾ, verset 114) » au verset entier',
    '« l’opposé de la corruption » (<em>ḫilāf al-fasād</em>)',
    'la corruption à détourner obligatoirement rend le ṣulḥ interdit, celle dont le détournement est préférable le rend réprobé',
    'le ṣulḥ SUR reconnaissance/silence/déni (l’assise du différend) et le ṣulḥ PAR vente/louage/donation',
    'le kālīʾ (<em>al-kālīʾ</em>) = le différé, ce qui est dû à terme',
    'donation PAR LA FORME, dégagement (<em>ibrāʾ</em>) PAR LA RÉALITÉ',
    'le dāl et le rāʾ y sont échangés d’ordre',
    'cinq exemples numérotés par la formule « exemple de… »',
    'le salam/salaf = la vente à terme par avance',
    'trois items annonçant la leçon à venir (doc 19452 : les jugements du ṣulḥ de l’injuste et du tuteur du sang',
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

out = '/home/z/my-project/tr-tmp/19449.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"OK {out} — {len(html)} car — {len(PROBES)} sondes OK — guillemets {html.count('«')}/{html.count('»')}")
