#!/usr/bin/env python3
# build-19671.py — 19671 « Jurisprudence : les jugements de la šarika du
# ğabr et de la šarika du travail » (fiqh-tanawi-3, lessons[28], badge
# Leçon 30/33) — vingt-sixième cours imprimé (26e confirmation : 23e
# mufāwaḍa → 24e dispositions+litige → 25e ʿinān → 26e ğabr+travail).
# DEUX axes h3 : (1) la šarika du ğabr — concept (l'acheteur du marché
# obligé d'y associer les marchands de la chose), jugement (obligatoire :
# ʿUmar l'a jugée, Mālik et ses compagnons l'ont dite — particularité de
# l'école, prolongement du fiqh de ʿUmar, précellence de l'intérêt de
# l'individu, maṣlaḥa), six conditions (3 dans la chose : marché/commerce/
# pays ; 3 dans le demandeur : présence, qualité de marchand, silence) +
# la ruelle (deux dires — absence de contrainte plus probable) ; (2) la
# šarika du travail — définition, jugement (licite, ne contraint point
# par le contrat), cinq conditions (union / dépendance mutuelle : filage-
# tissage, plongeur-rameur / égalité / proximité selon l'usage /
# coopération fût-ce en deux lieux), l'outil (propriété ou location :
# deux interprétations), exemples (médecins, gerfauts, fouisseurs du
# kirkāz ; oculiste+chirurgien tombent pour l'incertitude), l'héritage du
# reste du gisement (non hérité, l'Imam concède restreint à ce qui n'a
# pas paru), l'obligé (ouvrer + garantir ce que le compagnon accepte, même
# après séparation ; maladie annulée deux jours, au-delà le salaire sort
# de la part du non-ouvrant), la corruption (condition d'annuler beaucoup
# de maladie/absence ; les deux jours — hésitation). Fentes : AUCUNE
# (0 āya / 0 hadīth — 7e tour sans protocole triple) ; exploitation = Ibn
# Rušd, al-Muqaddimāt al-Mumahhadāt 3/37-38 (šarika des corps : Mālik/
# Ašhab/Ibn Ḥabīb vs aš-Šāfiʿī/Abū Ḥanīfa — la garantie fait la compagnie)
# — même ouvrage que le jugement de la ʿinān cité R323 (3/37) ; at-taʿbīm
# 25e occ. ; préparation préalable → les ḏimam (19744). Fil : la
# préparation préalable de la ʿinān (19670) annonçait le ğabr et le
# travail — refermé ici.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19671_{i}.html').read())
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
    "Jurisprudence : les jugements de la šarika du ğabr et de la šarika du travail",
    "l'homme a connu la compagnie où chacun tient la bride de son compagnon",
    "croyant qu'elle lui est propre et qu'il s'en réserve l'exclusivité contre autrui",
    "d'être surpris que cette chose soit partagée entre lui et un autre",
    "sans son choix ni sa volonté, alors même qu'il ne saisit pas les conditions qui corrigent cela",
    "Quel est donc le concept de la šarika du ğabr ?",
    "Et quelles sont ses conditions ? Et quel est le concept de la šarika du travail ?",
    "vingt-sixième leçon, au profit des élèves et des élèves de la troisième année secondaire",
    "at-taʿbīm al-ʿatīq",
    "1. Connaître la šarika du ğabr et du travail, leur jugement et leurs conditions.",
    "2. Se représenter les jugements de la šarika du ğabr et du travail dans mes transactions financières.",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Et il est contraint pour elle — s'il a acheté une chose en son marché, non pour un voyage ni pour une acquisition",
    "alors qu'un autre est présent, sans avoir parlé, du nombre des marchands de celle-ci — non en sa maison ?",
    "Et dans la ruelle, non comme sa maison ? Deux dires.",
    "Et il est permis par le travail, s'ils se sont unis, ou se sont mutuellement dépendus, ou égaux en lui, ou proches",
    "et que la coopération s'est réalisée — fût-ce en deux lieux",
    "ou faut-il une propriété ou une location ? Deux interprétations",
    "comme deux médecins qui se sont associés dans le médicament, et deux chasseurs dans les gerfauts",
    "On l'a rapporté sur eux deux, et [sur] deux fouisseurs d'un kirkāz et d'un gisement",
    "Et l'héritier de l'un n'a pas mérité son reste, et l'Imam le concède, restreint à ce qui n'a pas encore paru",
    "Et il lui est obligé ce que son compagnon accepte, et sa garantie, même s'ils se séparent",
    "Et la maladie est annulée pour deux jours, et leur absence — non si cela croît",
    "Et elle est corrompue par la condition de cela, comme le grand nombre de l'āla",
    "Et les deux jours sont-ils annulés, comme [dans] la saine — hésitation",
    "qiniya :",
    "je l'ai prise pour moi-même comme une acquisition, non pour le commerce",
    "rikāz :",
    "l'enfoui de la Jāhiliyya",
    "aqṭaʿa-hu :",
    "l'Imam a concédé à la troupe le pays en iqṭāʿ",
    "il a fait de sa récolte une subsistance",
    "1. J'extrais du texte le concept de la šarika du ğabr, ses conditions et son jugement.",
    "2. J'extrais du texte le concept de la šarika du travail et ses conditions.",
    "3. Je détermine du texte ce qui corrompt la šarika du ğabr.",
    "La présente leçon comprend ce qui suit",
    "Axe premier : la šarika du ğabr — son concept, ses conditions et son jugement",
    "le fait d'obliger l'acheteur de la marchandise venue du marché, pour le commerce, d'y associer d'autres",
    "la šarika du ğabr est obligatoire, car ʿUmar — que Dieu l'agrée — l'a jugée ainsi",
    "et Mālik et ses compagnons l'ont dite",
    "compte parmi les particularités de l'école de Mālik — que Dieu lui fasse miséricorde",
    "laquelle est le prolongement du fiqh de ʿUmar ibn al-Khaṭṭāb — que Dieu l'agrée",
    "elle tient compte des droits des marchands, et en particulier des petits d'entre eux",
    "elle y donne la précellence à l'intérêt de l'individu sur celui de la collectivité",
    "et l'agir selon l'intérêt est des fondements de l'école mālikite",
    "L'acheteur est contraint d'y associer autrui selon six conditions, dont trois touchent la chose achetée",
    "Qu'il achète une chose — denrée ou autre — en son marché, à savoir le marché de cette chose",
    "Que l'achat en soit pour le commerce",
    "Que le commerce s'en fasse dans le pays",
    "Que le demandeur de la compagnie soit présent au marché au moment de l'achat de la marchandise",
    "Que le demandeur de la compagnie soit du nombre des marchands de cette marchandise qui fut vendue en sa présence",
    "Que le demandeur de la compagnie ne parle pas au moment de l'achat de la marchandise",
    "Et vers ces conditions s'oriente le compilateur par son dire",
    "est-on aussi contraint à la compagnie si l'achat a lieu dans la ruelle, fût-elle éloignée de son marché",
    "Deux dires, et le plus probable des deux est l'absence de contrainte",
    "Axe deuxième : la šarika du travail — son concept, son jugement et ses conditions",
    "l'association de deux ouvriers ou plus dans un ouvrage, la rémunération étant entre eux deux",
    "la šarika dans l'ouvrage est licite, et elle ne contraint point par le contrat",
    "La šarika du travail a des conditions qui sont, selon l'ordre du compilateur",
    "Que les deux associés s'unissent dans l'ouvrage",
    "comme lorsqu'ils sont deux tailleurs",
    "Ou qu'ils se rendent mutuellement dépendants",
    "comme le tissage et l'ouvrage dans le filage dont dépend le tissage",
    "telles la torsion du fil, son enroulement et son montage sur le fuseau",
    "ou comme l'un des deux qui plonge pour demander la perle et l'autre qui le tient et rame",
    "Qu'ils s'égalent dans l'ouvrage",
    "en ce que chacun des deux prenne selon la mesure de son ouvrage de la production",
    "Ou qu'ils se rapprochent dans l'ouvrage selon l'usage",
    "en ce qu'il surpasse son compagnon en ouvrage d'un peu",
    "Que la coopération se réalise entre eux deux, fût-ce en deux lieux",
    "comme deux tailleurs en deux boutiques, la main de chacun circulant sur ce qui est chez l'autre",
    "comme l'orfèvrerie, la menuiserie et la chasse",
    "la condition que les deux soient égaux dans l'outil, par propriété ou par location",
    "en ce qu'ils l'achèteraient ensemble, ou que le propriétaire de chaque outil en vendrait la moitié à l'autre",
    "de sorte que sa garantie devienne celle des deux ensemble",
    "si leur médecine diffère — comme l'oculiste et le chirurgien —, elle n'est pas licite pour l'incertitude",
    "car la pratique de l'un peut circuler sans celle de l'autre",
    "ou deux fouisseurs qui se sont associés dans la fouille d'un rikāz et d'un métal et leur semblable",
    "que le reste de l'ouvrage dans le gisement n'est pas mérité par l'héritier de l'un des deux associés",
    "et qu'il appartient à l'Imam de le concéder à qui il veut, héritier ou autre",
    "4. Ce qui est obligé à l'un des deux associés dans la šarika du travail",
    "a. Il lui est obligé d'ouvrer avec lui en ce qu'il accepte :",
    "b. Il lui est obligé la garantie de ce que son compagnon accepte :",
    "qu'il a prétendu être abîmé ou son semblable",
    "leur garantie est la garantie des artisans dans leur ouvrage",
    "Et le compilateur a poussé à l'extrême la garantie de l'abîmé par son dire : « même s'ils se séparent »",
    "avec la présence de son associé, ou sa maladie, ou son absence proches — lesquels annulent",
    "s'il l'accepte après la longueur de son absence ou de sa maladie",
    "son compagnon ne lui est pas obligé d'ouvrer en cela, ni de garantie sur lui en cela",
    "par le dit et par le compris",
    "si la durée de la maladie ou de l'absence dépasse deux jours, elle n'est pas annulée",
    "du profit qu'ils avaient conditionné sur le col d'un vêtement qu'ils cousent tous deux pour lui",
    "et de la part de celui qui n'a pas ouvré sort le salaire de l'ouvrage",
    "5. Ce par quoi la šarika du travail se corrompt",
    "la šarika du travail se corrompt si elle est conclue entre eux deux sur la condition d'annuler beaucoup de maladie ou d'absence",
    "et ce qu'ils ont accompli ensemble demeure entre eux deux, et ce que l'un a accompli seul lui est en propre",
    "que s'ils n'avaient pas conditionné cela, et que l'un des deux ait aimé donner à son compagnon une part de son ouvrage",
    "ou rien ne s'y annule — hésitation ; et si elle s'est corrompue pour autre que cela, rien de la durée ne s'annule, sans hésitation",
    "1. J'expose le jugement de la šarika du ğabr et ses conditions.",
    "2. Je cite le jugement de la šarika du travail et ses conditions.",
    "3. Je détermine ce par quoi la šarika du travail se corrompt.",
    "Quant à la šarika des corps, Mālik et ses compagnons l'ont permise chez les artisans et autres",
    "l'ouvrage étant un, qu'ils coopèrent en lui et ne se séparent pas dans les lieux",
    "et Ašhab a permis — en l'audition d'Aṣbagh rapportant de lui — la séparation des deux artisans associés en deux boutiques",
    "et Ibn Ḥabīb a permis la séparation des journaliers dans les lieux et les pays, les bêtes de somme étant partagées entre eux",
    "Et ce dire n'est pas, à mon avis, en désaccord avec l'école d'Ibn al-Qāsim",
    "la šarika des corps n'est pas permise d'aucune façon",
    "et Abū Ḥanīfa l'a permise entre les artisans et ne l'a pas permise dans la chasse ni le ramassage du bois",
    "chacun des deux garantit ce que son compagnon accepte de l'ouvrage",
    "et chacun des deux fut ainsi un wakīl pour son compagnon en cela",
    "[al-Muqaddimāt al-Mumahhadāt 3/37-38]",
    "1. Je recherche le concept de la šarika des ḏimam et son jugement.",
    "2. Je mets en relief quelques espèces du jugement dans la šarika des ḏimam.",
    "Notes du traducteur",
    "vingt-troisième tranchage du fil",
    "ad-dars as-sādis wa-l-ʿišrūn",
    "vingt-troisième (la mufāwaḍa) → vingt-quatrième (les dispositions de l'associé et le litige) → vingt-cinquième (la ʿinān) → vingt-sixième (le ğabr et le travail)",
    "de la racine ğ-b-r, la contrainte",
    "la contrainte est l'affaire du marché, le consentement l'affaire des ouvriers",
    "la première graphie du matn porte un kāf de surcroît au mot du voyage (kasafar)",
    "les deux graphies ne diffèrent que du point du lām au fā",
    "le zuqāq est la voie étroite où se tient un commerce de voisinage",
    "la ruelle n'égale pas le marché, comme la maison ne l'égale pas",
    "le marché n'est le lieu des droits des marchands que pour qui y commerce",
    "glosé « l'enfoui de la Jāhiliyya »",
    "la récolte est la <em>ġalla</em>, terme fixé au registre",
    "elle porte sur le reliquat enfoui, non sur ce qui fut déjà tiré de terre",
    "minéral que les lexicographes rapportent comme une espèce de plomb ou d'argent impur",
    "le bāz est une espèce de faucon de haute volée",
    "« le col d'un vêtement qu'ils cousent tous deux pour lui » rend le ribb du matn",
    "la maladie passée deux jours ne s'annule pas, elle se paie",
    "le même ouvrage d'Ibn Rušd déjà invoqué pour le jugement de la ʿinān (la leçon précédente, 3/37)",
    "la compagnie de la bride et la compagnie des corps se partagent le même exposé",
    "c'est la garantie qui fait la compagnie des corps",
    "19744, « les jugements de la šarika des ḏimam et des visages »",
    "il ne reste après elle que les deux index finaux de l'imprimé",
    "Jurisprudence, arrêts sur l'entreprise de réparation et l'entreprise de travail",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19671.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
