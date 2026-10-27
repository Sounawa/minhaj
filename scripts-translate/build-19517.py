#!/usr/bin/env python3
# build-19517.py — 19517 « Jurisprudence : les jugements de la pluralité
# des porteurs » (fiqh-tanawi-3, lessons[23], badge Leçon 25/33) — suite
# du bāb du ḍamān, vingt-et-unième cours consécutif (6e → … → 20e
# imprimé). TROIS axes h3 : (1) les formes de la pluralité — porteurs non
# ġurmāʾ (chacun pour sa part, le solvable non pris pour le démuni) /
# porteurs ġurmāʾ solidaires (le tout pris de celui qu'on trouve, šarika
# d'acheteurs, instrement « lequel je veux », science ou absence) ;
# (2) le recours du muʾaddī — payeur au-delà du muʾaddā — tout ce qui est
# sur le maqlī puis l'égalisation (sawā), exemple à trois ġurmāʾ (100+50,
# 50), exemple non ġurmāʾ (150, 50), exemple de la Mudawwana à six
# (100+200, 50+75, 25+25, 12.5, 6.25) ; (3) les annulatifs du ḍamān
# [titre imprimé, contenu = le ḫilāf] — le recours de ce qui concerne
# spécialement le payeur : avis retenu (les parts des autres seules) vs
# avis plié (la moitié de ce qu'il a défrayé, absolument), fruit du
# différend (la moitié du cent), clausule morale (Sharīʿa sage, dessein
# des droits). Matn INTÉGRAL (un bloc). Exploitation : Ibn Rušd [Les
# Muqaddimāt al-Mumahhadāt 2/381-382] — la pluralité en une seule
# transaction, ce qui le représente, les deux dires de Mālik, Abū Isḥāq
# at-Tūnisī, la dette d'origine. 0 āya / 0 hadīth (quatrième tour
# consécutif sans protocole triple). Fente liminaire VIDE (6e conséc.) ;
# at-taʿbīm 20e occ. ; h3 « annulatifs » non concordant consigné ;
# numérotation de l'imprimé (20e) divergente de l'ordre du livre —
# éclaire les deux écarts de préparation préalable (R318 #6 + celui-ci).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19517_{i}.html').read())
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
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

probes = [
    "Jurisprudence : les jugements de la pluralité des porteurs",
    "Après avoir traité les jugements du ḍamān lorsque le porteur (<em>ḥamīl</em>) est unique",
    "pluralité des porteurs (<em>ḥumalāʾ</em>) — solidaires (<em>ġurmāʾ</em>) ou non",
    "ce que recèle leur pluralité de formes et de jugements",
    "Quelles sont les formes et les jugements de la pluralité des porteurs ?",
    "Et quels en sont les effets ?",
    "vingtième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître les jugements de la pluralité des porteurs.",
    "Saisir les effets de la pluralité des porteurs.",
    "Se représenter les jugements du ḍamān dans les transactions financières.",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Et si les porteurs (<em>ḥumalāʾ</em>) sont nombreux, chacun est suivi pour sa part (<em>ḥaṣṣa</em>)",
    "sauf que soit stipulé le portage (<em>ḥimāla</em>) de certains d'entre eux par d'autres, selon leur rang (<em>tarattub</em>)",
    "recouvre tout ce qui est sur le maqlī — celui qu'il rencontre —, puis l'égalise",
    "si six achètent pour six cents avec portage, et qu'il en rencontre un, il prend de lui le tout",
    "il prend de lui cent, puis deux cents",
    "il prend de lui cinquante et soixante-quinze",
    "il prend de lui vingt-cinq et autant, puis douze et demi, puis six et un quart",
    "ne recouvre-t-il pas aussi de ce qui le concerne spécialement (<em>bi-mā yaḫuṣṣu-hu</em>)",
    "Deux interprétations (<em>taʾwīlān</em>)",
    "La compréhension",
    "Le commentaire",
    "pluriel de <em>ḥamīl</em> — et c'est le garant (<em>ḍāmin</em>), le cautionnaire (<em>kafīl</em>)",
    "Pour sa part : son dû et sa part.",
    "Le portage : ce que tu as porté pour autrui.",
    "La synthèse du contenu du texte",
    "Je détermine du matn les jugements de la pluralité des porteurs.",
    "J'extrais du matn le jugement du recours du payeur (<em>ġarim muʾaddī</em>) pour ce qu'il a porté.",
    "quand le porteur recouvre de ce qui le concerne spécialement, et quand il n'y recouvre point.",
    "L'analyse",
    "Ce cours comprend les axes suivants",
    "Axe premier : les formes de la pluralité des porteurs",
    "1. La pluralité de porteurs non <em>ġurmāʾ</em>",
    "le maître de la dette (<em>rabʿ ad-dayn</em>) suit chacun d'eux pour sa seule part de la dette",
    "on ne prend point du solvable (<em>al-maliʾ</em>) pour le démuni (<em>al-maʿdim</em>), ni du présent pour l'absent",
    "« son ḍamān est sur nous », ses compagnons y consentant",
    "« garantissez-vous Zayd, par exemple ? »",
    "tous le profèrent d'un seul tenant",
    "il serait porteur, indépendamment, de tout le droit.",
    "2. La pluralité de porteurs <em>ġurmāʾ</em>",
    "société (<em>šarika</em>) entre eux",
    "chacun d'eux est porteur de ses compagnons",
    "pour la totalité du prix, quand les autres sont démunis (<em>ʿadam</em>) ou ont disparu",
    "a excepté de sa parole",
    "dans le contrat du portage (<em>ʿaqd al-ḥimāla</em>)",
    "plus fort encore s'il est absent ou mort",
    "« lequel d'entre vous je veux, j'en prends mon droit »",
    "dans la science (<em>al-ʿilm</em>) ou l'absence (<em>al-ġayba</em>) seulement",
    "Axe deuxième : le recours de certains porteurs <em>ġurmāʾ</em> contre d'autres porteurs",
    "a défrayé (<em>ġarama</em>) le droit au maître de l'argent",
    "recourt contre celui de ses pareils qu'il a rencontré pour ce qui est sur celui-ci en propre",
    "porteurs tout court (<em>ḥumalāʾ faqaṭ</em>)",
    "si trois personnes, par exemple, achètent une marchandise pour trois cents — cent sur chacun",
    "il prend de lui le tout : cent pour sa part et deux cents pour son compagnon",
    "cinquante — la moitié de ce qui est sur le troisième",
    "quiconque trouve le troisième en prend de lui cinquante",
    "un homme achète une marchandise pour trois cents, et trois hommes le garantissent",
    "quand le terme échoit et qu'il en trouve un, il prend de lui les trois cents",
    "il recourt contre lui pour cent cinquante",
    "l'exemple de la Mudawwana, que les gens ont singularisé par l'insertion dans le matn",
    "avec le fāʾ de l'enchaînement (<em>fāʾ at-tafrīʿ</em>)",
    "Axe troisième : les annulatifs du ḍamān",
    "il a mentionné le recours des porteurs tout court",
    "à l'image de sa non-récupération de ce qui le concerne dans ce qui précède",
    "si le détenteur du droit rencontre l'un d'eux et prend de lui le tout — et c'est l'avis retenu (<em>al-muʿtamad</em>)",
    "est plié (<em>maṭwiyy</em>) — le compilateur ne l'a point énoncé",
    "pour la moitié de ce qu'il a défrayé",
    "sans différence entre ce qu'il a défrayé pour lui-même et ce qu'il a défrayé pour ses compagnons",
    "si trois personnes se portent pour une personne pour trois cents",
    "il partage avec lui les deux cents — cent chacun",
    "le premier recourt ensuite contre le troisième pour cent",
    "il partage avec lui les trois cents — cent cinquante chacun",
    "j'ai acquitté les trois cents, tu es porteur avec moi de cela",
    "chacun des deux recourt contre le troisième pour cinquante",
    "Le fruit du différend (<em>fāʾidat al-ḫilāf</em>)",
    "parce qu'il n'a point trouvé avec lui autre chose",
    "l'un des cautionnaires (<em>kufalāʾ</em>)",
    "recourt-il contre lui pour la moitié du cent, ou ne recourt-il point contre lui pour rien de celui-ci ?",
    "la Sharīʿa sage vise la règle (<em>aḍ-ḍabṭ</em>) dans les affaires",
    "ce qui touche aux droits des fils d'Adam",
    "la fidélité aux pactes et à l'engagement dans les contrats",
    "le dessein des droits (<em>al-maqṣad al-ḥuqūqī</em>)",
    "Le contrôle",
    "J'expose le jugement des porteurs quand ils sont nombreux.",
    "Je précise quand les porteurs recourent, et quand ils ne recourent point.",
    "L'exploitation",
    "L'illustre Ibn Rušd — que Dieu lui fasse miséricorde — a dit",
    "des porteurs se portent pour de l'argent en une seule transaction (<em>ṣafaqa</em>)",
    "chacun d'eux est tenu de ce qui le représente de cet argent, selon leur nombre",
    "le solvable d'entre eux est pris pour le démuni, comme ils sont pris à l'absence du ġarīm — le débiteur",
    "sur l'un des deux dires de Mālik",
    "à cela est allé Abū Isḥāq at-Tūnisī",
    "point de recours pour lui par cela, comme s'il était établi sur lui d'une dette d'origine (<em>aṣl dayn</em>)",
    "[Les Muqaddimāt al-Mumahhadāt 2/381-382]",
    "J'examine ce texte avec soin et j'en extrais ce qui suit :",
    "l'effet (<em>aṯar</em>) de la pluralité des porteurs, et je le compare au dire du compilateur",
    "quand certains porteurs ne recourent point contre d'autres.",
    "La préparation préalable",
    "Je lis le matn du cours suivant et j'accomplis ce qui suit :",
    "Quels sont les types du ḍamān ? Et quel est le jugement de chaque type ?",
    "Quand le garant est-il quitte du ḍamān ?",
    "Que faire lorsque le garant et le garanti diffèrent ?",
    "Notes du traducteur",
    "Règles de jurisprudence pour les grossesses multiples",
    "n'a rien d'une grossesse (<em>ḥaml</em>)",
    "désamorcé par la leçon elle-même",
    "règle av — dix-huitième tranchage du fil",
    "VIDE pour la sixième leçon consécutive",
    "ad-dars al-ʿišrūn",
    "vingtième : la pluralité des porteurs ; vingt-et-unième : les types du ḍamān",
    "chaque préparation pointe la leçon suivante DE L'IMPRIMÉ, non du livre",
    "vingtième occurrence",
    "la glose est établie par le commentaire même",
    "le débiteur grevé, « celui qui porte la dette »",
    "« l'absence du ġarīm » de l'exploitation est l'absence du débiteur, non du créancier",
    "leur densité technique étant portée par le commentaire",
    "la majorité des gens de la science retient la non-récupération",
    "est « plié » (<em>maṭwiyy</em>) : sous-entendu",
    "l'étiquette paraissant reprise du titre de la leçon de l'instrement",
    "consigné sans tranchement",
    "laissée à la densité du matn",
    "l'exemple venant d'au-delà du texte",
    "l'identité du savant visé n'est pas tranchée ici",
    "coquille pour « <em>astaḫriǧ</em> » (j'extrais)",
    "coquille de vocalisation, rendue au sens",
    "sans modification rétrospective (règle ax)",
]

missing = [p for p in probes if p.replace("'", chr(0x2019)) not in html]
if missing:
    issues.append(f"sondes manquantes ({len(missing)}): " + " || ".join(missing[:6]))

if issues:
    print("ÉCHEC build-19517 :")
    for i in issues:
        print(" -", i)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19517.html'
open(out, 'w').write(html)
print(f"OK build-19517 : {len(html)} caractères, {len(probes)} sondes toutes présentes -> {out}")
