#!/usr/bin/env python3
# build-19537.py — 19537 « Jurisprudence : qui conclut la šarika et par
# quoi elle se conclut » (fiqh-tanawi-3, lessons[24], badge Leçon 26/33)
# — vingt-deuxième cours imprimé (CONFIRMATION de l'hypothèse de l'ordre
# imprimé de R319 : 20e pluralité → 21e types → 22e šarika). TROIS axes
# h3 : (1) le concept — langue (3 formes, Ibn Fāris, deux origines) /
# terminologie (ğins + faṣl + avec leurs propres personnes, duel sans
# implication) / jugement (ğawāz, 2 fentes de verset VIDES + glose
# ḫulaṭāʾ, hadīth qudsī + Manāwī/Ṭaybī, iğmāʿ, bāliġ rāšid) / formes
# (ʿurf, silence = consentement, zarʿ exige ʿamal) / 4 biens (deux ors
# ṣarf uni, or+argent égaux, ʿayn+ʿaraḍ, deux ʿaraḍ absolument) /
# estimation (yūm uḥḍir, la-fāta, ḏī-t-tawfiya) ; (2) le ḍamān du bien —
# des deux si mélange (ḥukman compris) / de l'un sinon — acheté sans lui
# partagé, moitié du prix sur le mutlif, tardud + naql ; (3) valide /
# non valide — numéraire absent (2 conditions) / or+argent (ṣarf+šarika
# se joignent), deux aliments (vente avant saisie) + clausule morale.
# Fente liminaire VIDE (7e conséc.) ; at-taʿbīm 21e occ. ; TROIS fentes
# de verset vides consignées (candidats documentaires : Ṭā-Hā 32, Ṣād
# 38:24 — vérifiés au cache, AUCUNE insertion) ; exploitation = Muwaṭṭaʾ
# (salaf vs vente nouvelle) ; préparation préalable → 19544/19601.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19537_{i}.html').read())
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

probes = [
    "Jurisprudence : qui conclut la šarika et par quoi elle se conclut",
    "l'exposition qui désaltère et le détail qui suffit des jugements de la šarika",
    "autour de qui conclut la šarika et par quoi elle se conclut",
    "Quel est donc le concept de la šarika ? De qui est-elle valide ? Et par quoi se conclut-elle ?",
    "vingt-deuxième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître le concept de la šarika, de qui elle est valide et par quoi elle se conclut.",
    "Saisir les effets rattachés au contrat de la šarika.",
    "Se représenter les jugements de la šarika dans mes transactions financières.",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "une permission de disposer pour tous deux, avec leurs propres personnes",
    "elle n'est valide que de l'homme du mandat (<em>at-tawkīl</em>) et de la confiance (<em>at-tawakkul</em>)",
    "comme leur dire : nous nous sommes associés (<em>aštaraknā</em>)",
    "par deux ors, ou deux argents, sous condition que leur frappe (<em>aṣ-ṣarf</em>) s'accorde",
    "et par les deux venant de chacun d'eux",
    "et par une substance et une marchandise",
    "et par deux marchandises absolument",
    "et chacune [s'estime] à sa valeur le jour où elle est apportée",
    "point d'estimation au jour de la perdition",
    "si les deux se mélangent, fût-ce par décision",
    "ce qui a péri est au compte de son maître",
    "et ce qui a été acheté sans lui est entre eux deux, et sur celui dont le bien a péri la moitié du prix",
    "sauf s'il savait de la perdition : alors pour lui et contre lui ?",
    "Ou absolument, sauf s'il allègue la prise pour lui ? Hésitation.",
    "Et si le numéraire de l'un d'eux vient à s'absenter, pourvu qu'il ne soit pas lointain",
    "ni par un or et un argent, ni par deux aliments, dussent-ils s'accorder",
    "La compréhension",
    "Le mandat (<em>at-tawkīl</em>) : la députation (<em>al-ināba</em>)",
    "La confiance (<em>at-tawakkul</em>) : l'acceptation de la procuration (<em>al-wakāla</em>)",
    "La coutume (<em>al-ʿurf</em>) : ce sur quoi les âmes se sont établies",
    "Le change (<em>aṣ-ṣarf</em>) : la vente d'une monnaie contre une autre",
    "Le péri (<em>at-tālif</em>) : ce qui s'en est allé, égaré",
    "Le numéraire (<em>an-naqd</em>) : le numéraire, dans la vente, est l'opposé du différé (<em>an-nasīʾa</em>)",
    "La synthèse du contenu du texte",
    "J'extrais du matn le concept de la šarika et son jugement.",
    "J'extrais du matn de qui la šarika est valide et de qui elle ne l'est point.",
    "J'extrais du matn les conditions de la šarika.",
    "L'analyse",
    "Axe premier : le concept de la šarika, son jugement et ses conditions",
    "1. La définition de la šarika",
    "a. En langue :",
    "selon les schèmes de <em>niʿma</em>, de <em>raḥma</em> et de <em>nabīqa</em>",
    "les lettres šīn, rāʾ et kāf portent deux origines",
    "l'une indique la proximité — s'opposant à l'isolement de la singularité —",
    "que la chose soit entre deux, sans que l'un d'eux y soit seul",
    "je me suis associé (<em>šārakta</em>) à un tel en une chose",
    "Dieu — que Sa gloire soit exaltée — a dit dans l'histoire de Mūsā — sur lui le salut :",
    "[Maqāyīs al-luġa, entrée « š-r-k » 3/265]",
    "Et le pluriel de <em>šarīk</em> se ramène à <em>šurakāʾ</em> et <em>ašrāk</em>.",
    "b. En terminologie :",
    "Sa parole : « une permission de disposer » est comme le genre (<em>al-ğins</em>)",
    "elle inclut la procuration (<em>al-wakāla</em>) et le qirāḍ",
    "sa parole : « pour tous deux » est comme le séparateur (<em>al-faṣl</em>)",
    "une personne mandate une personne pour disposer de ses biens à elle",
    "chacun a autorisé pour son compagnon la disposition pour le mandant seulement",
    "fait sortir quelques formes du qirāḍ",
    "non avec la persistance de la disposition de l'autorisant lui-même",
    "Et il n'y a point d'implication du duel : la šarika peut être entre plus de deux.",
    "2. Son jugement et ses formes",
    "a. Son jugement et de qui elle est valide :",
    "le jugement de la šarika est la licéité dans l'ensemble (<em>al-ğawāz fī-l-ğumla</em>)",
    "le Livre, la Sunna et le consensus (<em>al-iğmāʿ</em>)",
    "du Livre, la parole du Très-Haut :",
    "et Sa parole, le Transcendant :",
    "« et les <em>ḫulaṭāʾ</em> : ce sont les associés. »",
    "le hadīth divin (<em>ḥadīth qudsī</em>) rapporté d'Abū Hurayra",
    "Je suis le troisième des deux associés tant qu'aucun des deux ne trahit son compagnon",
    "s'il le trahit, Je sors d'entre eux deux.",
    "[Sunan Abī Dāwūd, Livre des ventes, chapitre : de la šarika]",
    "Al-Manāwī — que Dieu lui fasse miséricorde — a dit",
    "par l'abandon de l'acquittement du dépôt (<em>al-amāna</em>)",
    "la baraka est arrachée de leurs deux biens",
    "Aṭ-Ṭaybī a dit : la šarika de Dieu pour eux deux est une métaphore",
    "la baraka au rang du bien mêlé",
    "« elle sort » est l'adoucissement de la métaphore",
    "Dieu est au secours du serviteur tant que le serviteur est au secours de son frère",
    "[Fayḍ al-qadīr 2/308]",
    "Et les musulmans se sont accordés sur la licéité de la šarika dans l'ensemble.",
    "le pubère discernant (<em>al-bāliġ ar-rāšid</em>)",
    "la šarika de l'enfant (<em>aṣ-ṣabī</em>) n'est pas valide, ni celle de l'insensé (<em>al-mağnūn</em>), ni celle du prodigue (<em>as-safīh</em>)",
    "b. Ses formes :",
    "chacun des deux le prononçant, ou l'un des deux le prononçant et l'autre se taisant, y consentant",
    "sans besoin de plus, selon Ibn al-Qāsim",
    "le mélange des deux biens n'est point requis, ni le commerce en eux",
    "la šarika de la culture (<em>az-zarʿ</em>) ne se lie point sans le travail (<em>al-ʿamal</em>)",
    "c. Ce en quoi la šarika est licite :",
    "Les deux ors :",
    "la frappe des deux ors, ou des deux argents, s'unifie au temps du contrat",
    "la différence de frappe après le contrat ne nuit point",
    "de même s'accordent leur poids et leur qualité — bonne ou mauvaise",
    "l'accord de leur valeur, qu'unisse ou non leur frappe",
    "L'or et l'argent :",
    "l'un des deux associés sort des dīnārs et des dirhams, et que l'autre en sort leur pareil",
    "l'égalité de l'or de l'un avec l'or de l'autre — en poids, en frappe et en valeur",
    "La substance et la marchandise :",
    "il a entendu par elle ce qui comprend l'aliment",
    "Les deux marchandises :",
    "chacune des deux apportant une marchandise qui n'est point un aliment — pour ce qui va venir",
    "y entre ainsi le cas où l'une est une marchandise et l'autre un aliment",
    "le ḍamān de l'acheteur par le contrat",
    "par la saisie (<em>al-qabḍ</em>)",
    "comme le mesurable (<em>ḏī-t-tawfiya</em>) : ce qui se cale, se pèse ou se compte, autre que la substance",
    "l'absent d'une absence proche",
    "le jour de son entrée dans le ḍamān de la vente, non le jour de son entrée dans le ḍamān de la šarika — qui est le mélange (<em>al-ḫalṭ</em>)",
    "parce que les marchandises sont des biens substantiels",
    "en considération de ce qui ne se départage pas",
    "par vente, ou par hawāla du marché (<em>ḥiwālat sūq</em>), ou par destruction",
    "comme lorsqu'elle a lieu sur la différence du profit ou du travail",
    "le supposé étant que les deux biens sont égaux en quantité, alors point d'estimation",
    "Axe deuxième : le ḍamān du bien de la šarika",
    "1. Le ḍamān des deux associés",
    "mais encore fût-ce par décision (<em>ḥukman</em>)",
    "que chacun des deux biens fût dans une bourse tenue à part",
    "qu'ils l'eussent mis en la détention d'un tiers, ou de l'un des deux seulement",
    "2. Le ḍamān de l'un des deux",
    "le maître du sauf (<em>aṣ-ṣālim</em>) et le maître du péri",
    "s'il y a profit, à tous deux ; et s'il y a perte, sur tous deux",
    "si la šarika est par moitié ; sinon, il ne ḍamine que sa part seulement",
    "Et le naql (<em>an-naql</em>) : qu'il est laissé au choix",
    "le maître du péri est laissé au choix d'entrer avec lui ou de n'y point entrer",
    "alors il s'y réserve seul, et point de choix pour son associé. Hésitation.",
    "Axe troisième : ce par quoi la šarika est valide et ce par quoi elle n'est pas valide",
    "1. Ce par quoi elle est valide",
    "si chacun des deux associés a apporté ce qu'il avait sorti",
    "mais proche, comme les deux jours",
    "que l'on ne commercerait point par le présent avant la saisie de l'absent",
    "2. Ce par quoi elle n'est pas valide",
    "quand même chacun des deux aurait pressé de livrer à son compagnon ce qu'il avait sorti",
    "par le fait que se joignent le change (<em>aṣ-ṣarf</em>) et la šarika",
    "s'ils opèrent, à chacun son capital, et ils partagent le profit",
    "elle n'est pas valide par deux aliments différant en espèce, en qualité et en mesure",
    "parce que cela mène à la vente de l'aliment avant sa saisie",
    "la šarika est une cause de l'obtention de la baraka et de l'accroissement du bien",
    "les projets industriels, l'urbanisme, le commerce, l'agriculture et leur pareil",
    "le dessein moral (<em>al-maqṣad al-ğawdī</em>) parmi les gens",
    "Le contrôle",
    "Je détermine le concept de la šarika et son jugement.",
    "J'expose les jugements du ḍamān du bien de la šarika.",
    "Je cite les conditions de la šarika.",
    "L'exploitation",
    "Mālik a dit",
    "achète cette marchandise entre moi et toi, et avance le prix à ma place, et je te la vendrai",
    "cela ne va point, lorsqu'il dit : avance le prix à ma place, et je te la vendrai",
    "cela n'est qu'un prêt (<em>salaf</em>) qu'il lui prête, à condition de lui vendre la marchandise",
    "associe-moi à la moitié de cette marchandise, et je te la vendrai tout entière",
    "cela est licite, sans reproche",
    "c'est une vente nouvelle — il lui vend la moitié de la marchandise, à condition de lui vendre l'autre moitié",
    "[Le Muwaṭṭaʾ, chapitre : ce qui est venu concernant la šarika, la tawliya et l'iqāla]",
    "J'examine ce texte et j'y réponds par ce qui suit :",
    "J'expose du texte les formes licites et ce qui ne l'est point, avec le raisonnement.",
    "J'expose l'espèce de la šarika venue dans le texte.",
    "La préparation préalable",
    "Je lis le matn du cours suivant et j'en extrais ce qui suit :",
    "J'extrais du matn une section des sections de la šarika, et j'entreprends de la définir.",
    "Quel est le jugement de la disposition de l'un des deux associés sans la permission de son associé ?",
    "Notes du traducteur",
    "Sur le titre : l'étiquette GT « La jurisprudence est celle qui conclut l'entreprise",
    "dix-neuvième tranchage du fil",
    "Sur la numérotation de l'imprimé : « le vingt-deuxième cours »",
    "CONFIRMATION de première main de l'hypothèse du tour précédent",
    "vingtième : la pluralité des porteurs → vingt-et-unième : les types du ḍamān → vingt-deuxième : la šarika",
    "Sur les trois fentes de verset VIDES",
    "Ṭā-Hā 32 (« <em>ašrik-hu fī amrī</em> »",
    "Ṣād 38:24, où le mot « al-ḫulaṭāʾ » figure",
    "aucune restitution de verset",
    "Sur « hors l'écart de poids » de la glose du change",
    "Sur la triple distinction du commentaire",
    "Sur le duel sans implication",
    "Sur « en considération de ce qui ne se départage pas »",
    "Sur le mesurable (<em>ḏī-t-tawfiya</em>)",
    "Sur le naql du commentaire",
    "Sur la clausule morale : rendue à sa place imprimée",
    "Sur la coquille « <em>at-taʿbīm</em> » : vingt-et-unième occurrence",
    "Sur la coquille de la préparation préalable : le lexème imprimé « <em>asaḫruǧ</em> »",
    "Sur la préparation préalable : deux items pointant l'imprimé suivant",
    "la mufāwaḍa, 19544",
    "(19601)",
]

missing = [p for p in probes if p.replace("'", chr(0x2019)) not in html]
if missing:
    issues.append(f"sondes manquantes: {len(missing)}/{len(probes)}")
    for m in missing[:12]:
        issues.append("  MISSING: " + m[:90])

out = '/home/z/my-project/tr-tmp/19537.html'
open(out, 'w', encoding='utf-8').write(html)

print(f"taille: {len(html)} car (cible ≥ 12000)")
print(f"sondes: {len(probes) - len(missing)}/{len(probes)}")
print(f"guillemets: {html.count('«')} / {html.count('»')}")
if issues:
    print("ÉCHEC:")
    for i in issues:
        print(" -", i)
    raise SystemExit(1)
print("BUILD OK ->", out)
