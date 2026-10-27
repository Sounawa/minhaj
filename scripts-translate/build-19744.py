#!/usr/bin/env python3
# build-19744.py — 19744 « Jurisprudence : les jugements de la šarika des
# ḏimam et des visages » (fiqh-tanawi-3, lessons[29], badge Leçon 31/33) —
# vingt-septième cours imprimé (27e confirmation : 24e dispositions+litige →
# 25e ʿinān → 26e ğabr+travail → 27e ḏimam+visages — DERNIÈRE leçon de
# l'imprimé). DEUX axes h3 : (1) les jugements de la šarika des ḏimam —
# concept (achat sans capital sur le rang et la confiance des marchands) +
# jugement (NON licite : la compagnie s'attache au bien ou à l'ouvrage ;
# type « porte mon fardeau » — garantie avec juʿl et salaf ğarr an-nafʿ) ;
# la šarika des visages (Ibn ʿArafah 7/36 : le considéré vend le bien du
# sans-renom contre une part du profit — al-Qarāfī/Ibn al-Qaṣṣār :
# interdite, dit aš-Šāfiʿī, permise par Abū Ḥanīfa ; les Mālikites :
# l'essence de la compagnie requiert bien ou corps au contrat) ; la meule/
# maison/bête (loyer inégal + récolte égale = corruption ; la cause tourne
# avec l'effeté) ; (2) le jugement — restitution mutuelle des locations
# (exemple mille/deux mille/trois mille, fractions portées telles quelles) ;
# l'ouvrage du maître de la bête conditionné (récolte à lui, loyer des deux
# sur lui, Mudawwana) ; le jugement en ce qui ne se divise pas (reconstruire
# ou vendre — bain, four, boutique) ; les biens en copropriété (étage bas :
# étaiement, toit, balayage des latrines — non l'escalier, non le carrelage) ;
# sans accroissement d'étage sauf le léger ; le toit au bas au litige —
# renvoi « à la parole du Très-Haut » avec FENTE DE VERSET VIDE dans
# l'imprimé (portée telle quelle, aucun protocole triple) ; la bête au
# cavalier non au tenant de la lisière ; la meule dressée quand les deux
# refusent (récolte à tous, remboursement d'abord — cause efficiente vs
# responsabilité) ; le barrage des moyens (sadd aḏ-ḏarāʾiʿ). Fentes : fente
# du verset VIDE (0 āya cité — 8e tour sans protocole triple) ; exploitation
# = Ibn Rušd al-Muqaddimāt al-Mumahhadāt 3/39 (MÊME ouvrage que R323 3/37 et
# R324 3/37-38 — troisième leçon consécutive) ; AUCUNE préparation préalable
# (dernière leçon de l'imprimé) ; at-taʿbīm 26e occ. ; fente liminaire avec
# date imprimée (Lundi 22 avril 2024).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19744_{i}.html').read())
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
    "Jurisprudence : les jugements de la šarika des ḏimam et des visages",
    "Lundi 22 avril 2024",
    "La compagnie entre les gens diffère et se diversifie, et selon sa différence et sa diversification les jugements diffèrent et se distinguent",
    "pour prononcer sur elles un jugement — de la validité ou de la corruption",
    "dans la présente leçon, le compilateur — que Dieu lui fasse miséricorde — traite de la šarika des ḏimam",
    "Quel est donc le concept de la šarika des ḏimam ?",
    "Et quels sont ses jugements ?",
    "vingt-septième leçon, au profit des élèves et des élèves de la troisième année secondaire",
    "at-taʿbīm al-ʿatīq",
    "1. Connaître les jugements de la šarika des ḏimam.",
    "2. Distinguer entre les jugements de la šarika des ḏimam.",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Et leur association par les ḏimam : qu'ils achètent sans bien, celui-ci étant entre eux deux",
    "et comme la vente d'un considéré du bien d'un sans-renom contre une part de son profit",
    "et comme [l'association] d'un détenteur de meule, d'un détenteur de maison et d'un détenteur de bête pour qu'ils ouvrissent",
    "si le loyer ne s'égalise pas et qu'ils s'égalent dans la récolte ; et qu'ils se rendent mutuellement les locations",
    "et si l'ouvrage du maître de la bête est conditionné, la récolte est à lui, et le loyer des deux est sur lui",
    "et il est jugé sur un associé en ce qui ne se divise pas : qu'il rebâtisse ou qu'il vende — comme le détenteur du bas, s'il l'affaiblit",
    "et sur lui le soutènement et le toit et le balayage des latrines — non l'escalier",
    "et sans accroissement de l'étage haut — sauf le léger",
    "et le toit est au bas, et la bête au cavalier — non à qui tient la lisière",
    "et si l'un d'eux dresse une meule quand les deux refusent, la récolte est à eux, et il se rembourse d'elle ce qu'il a dépensé",
    "aḏ-ḏimam :",
    "en langue : l'engagement ; et en Loi : une qualité par laquelle la personne devient éligible à l'obligation",
    "wajīh :",
    "il est considéré lorsqu'il a une part et un rang",
    "al-ġalla :",
    "tout ce qui provient du rendement de la terre ou de sa location",
    "ḫāmil :",
    "il est tombé en renommée, sans éclat",
    "1. J'extrais du texte le jugement de la šarika des ḏimam et ce par quoi elle se corrompt.",
    "2. Je mets en relief, à partir du texte, les formes du jugement dans la šarika des ḏimam.",
    "La présente leçon comprend les deux axes qui suivent",
    "Axe premier : les jugements de la šarika des ḏimam",
    "a. Son concept :",
    "en s'appuyant sur leur rang et sur la confiance que les marchands leur portent",
    "elle est donc une compagnie sur les ḏimam, sans industrie ni bien",
    "b. Son jugement :",
    "la šarika des ḏimam n'est pas licite ; car la compagnie ne s'attache qu'au bien ou à l'ouvrage, tous deux absents ici",
    "porte mon fardeau et je porte le tien, et avance-moi et je t'avance",
    "du type de la garantie avec don récompensé (<em>juʿl</em>) et de l'avance qui attire le profit — et cela ne se permet pas",
    "2. La définition de la šarika des visages et son jugement",
    "a. Sa définition :",
    "que le considéré vende le bien du sans-renom avec un visage d'accroissement de profit, pour qu'une part lui en soit",
    "[Le Muḫtaṣar al-fiqhī d'Ibn ʿArafah 7/36]",
    "al-Qāḍī Abū Muḥammad l'a expliquée en ce qu'elle est",
    "et sur ce [mode] elle serait la synonyme de la šarika des ḏimam",
    "b. Son jugement :",
    "pour l'ignorance de la rémunération et pour l'incertitude qui l'entoure",
    "Al-Qarāfī a dit : Ibn al-Qaṣṣār a dit : la šarika des visages est interdite",
    "et c'est le dire d'aš-Šāfiʿī — et Abū Ḥanīfa l'a permise",
    "l'essence de la compagnie est que les deux s'associent en quelque chose au moment du contrat — soit un bien, soit un corps",
    "pour l'incertitude qu'elle contient, laquelle est objet d'interdiction",
    "[aḏ-Ḏaḫīra 8/29, avec retouche]",
    "c'est-à-dire que la compagnie se corrompt si le loyer des associés ne s'égalise pas, et qu'ils ouvrissent de leurs mains",
    "ce qui provient de la récolte devant se diviser entre eux au prorata de leur nombre",
    "car la cause tourne avec l'effeté en existence et en absence",
    "si chacun prend de la récolte selon la mesure de son loyer, il n'y a pas de corruption non plus",
    "Axe deuxième : le jugement dans la šarika des ḏimam",
    "1. Le jugement après la corruption de la compagnie",
    "si la compagnie se corrompt pour quelque raison que ce soit, les associés se rendent mutuellement les locations",
    "en ce que chacun rend ce qui est sur lui et qu'il ne mérite pas",
    "si le loyer du matériel de l'un d'eux est de mille dirhams, celui de l'autre de deux mille et celui du troisième de trois mille",
    "réclame à chacun de ses deux compagnons ce qui échoit sur lui de l'excès de son loyer au regard du moindre des deux loyers",
    "ainsi celui dont le loyer du matériel est de trois mille réclame à chacun de ses deux compagnons les deux tiers du loyer",
    "celui dont le loyer du matériel est de deux mille réclame à chacun de ses deux compagnons le tiers du loyer",
    "chacun de ces deux a donc deux créanciers",
    "le premier prend de celui dont le loyer du matériel est de mille dirhams les deux tiers du loyer",
    "et le second prend de celui dont le loyer du matériel est de mille dirhams le tiers du loyer",
    "que quiconque conditionne dans le contrat de la compagnie l'ouvrage du maître de la bête — et qu'il ouvre —, la récolte née de son ouvrage est à lui seul",
    "car son ouvrage est comme un capital",
    "le loyer du semblable : la maison, l'atelier et leur semblable — est sur le maître de la bête",
    "Et s'il ne réalise rien, selon la Mudawwana ; car quiconque loue quelque chose à un loyer corrompu doit le loyer de son semblable",
    "2. Le jugement en ce qui ne se divise pas",
    "comme un bain, un four, une boutique dont son associé a demandé la reconstruction avec lui, et que le premier a refusé",
    "préservation du bien et allègement des associés",
    "s'il refuse la reconstruction, il est jugé vendre la totalité de sa part à qui rebâtira",
    "laquelle monte avec la mesure du besoin",
    "3. Le jugement dans les biens en copropriété",
    "ce qui n'y contient point de compagnie, et il a dit : « comme le détenteur du bas, s'il l'affaiblit »",
    "il est jugé au détenteur de l'étage bas la reconstruction s'il faiblit et que la chute de l'étage haut soit crainte sur ce qui appartient à autrui",
    "s'il s'y refuse, le juge vend à qui rebâtira",
    "d'une demeure composée de deux étages ou plus, s'il faiblit et que la chute du haut est crainte",
    "L'étaiement de la construction et son renforcement ; car le renforcement vaut la construction, et il est sur le détenteur du bas",
    "La réparation du toit de sa maison ; car il est terre pour le haut, et parce que le toit est au bas au litige, comme cela vient",
    "Le balayage des latrines où le haut jette ses déchets ; car elles valent le toit du bas",
    "Et il n'y a pas, sur le détenteur du bas, d'escalier vers le haut ; et de même, le bas n'a pas le carrelage de la maison du haut",
    "de ne point accroître l'étage haut sur le bas, sauf le léger — qui est ce qui ne nuit pas, selon l'usage, présentement ni en issue, au bas",
    "4. Le jugement du toit au bas au litige",
    "il est jugé que le toit portant le haut est au bas au litige — pour la parole du Très-Haut",
    "Il a rattaché le toit à la maison, et la maison au bas",
    "et la bête est au cavalier — peut-être par un droit — non au conducteur ni au meneur",
    "sauf par un usage ou un indice circonstanciel, et plus fort, une preuve",
    "5. Le jugement de la récolte aux associés au litige",
    "si trois associés, par exemple, se sont associés dans une aire préparée pour une récolte dont les meules se sont effondrées",
    "et que l'un d'eux dresse une meule avant le jugement de reconstruction ou de vente par ceux qui rebâtiront",
    "de leur permission à lui de la reconstruire après le leur avoir montré, comme on le fait savoir au refusant",
    "qu'ils aient refusé du premier de la reconstruction à son dernier, ou qu'ils se soient tus au moment de la demande de permission",
    "la récolte est à eux tous, selon le dire le plus probable, comme l'a dit Ibn ʿAbd as-Salām",
    "Mais seulement après qu'il se soit d'abord remboursé d'elle ce qu'il a dépensé",
    "il n'a été donné recours dans la récolte que parce qu'elle s'est produite par sa cause",
    "il n'a point été donné recours dans la responsabilité, parce qu'il ne lui fut point permis de reconstruire",
    "Le barrage des moyens est un fondement des fondements de l'école de Mālik — que Dieu lui fasse miséricorde",
    "interdire le négoce par le hasard et l'incertitude, par lesquels les droits s'en vont tout d'une pièce et se font piétiner",
    "1. Je connais la šarika des ḏimam et j'expose son jugement.",
    "2. Je connais la šarika des visages et j'expose son jugement.",
    "3. Je mets en relief comment se fait le jugement dans la šarika des ḏimam.",
    "Quant à la šarika des ḏimam, Mālik ne l'a pas permise",
    "car elle est une compagnie sans bien ni industrie",
    "acquiers pour moi la moitié de ce que j'achète, à condition que je t'acquière la moitié de ce que tu achètes",
    "Et cela est incertitude et hasard",
    "La šarika des visages est permise, et elle se conclut sur la wakāla",
    "une part en est pour lui et une part pour son compagnon, sur le mode de la wakāla",
    "Et cette wakāla se corrige dans l'état — et cela ne se corrige point",
    "à condition que tu aies le profit de ma marchandise que j'aurai achetée, cela ne convient pas ; car cela est inconnu des deux ensemble",
    "[al-Muqaddimāt al-Mumahhadāt 3/39]",
    "J'examine ce texte et j'expose le jugement de la šarika des ḏimam chez les Imams, avec preuve et raisonnement",
    "Notes du traducteur",
    "vingt-quatrième tranchage du fil",
    "ad-dars as-sābiʿ wa-l-ʿišrūn",
    "vingt-quatrième (les dispositions de l'associé et le litige) → vingt-cinquième (la ʿinān) → vingt-sixième (le ğabr et le travail) → vingt-septième (les ḏimam et les visages)",
    "c'est la DERNIÈRE leçon de l'imprimé",
    "fihrist al-iʿlām",
    "fihrist al-maṣādir wa-l-marāğiʿ",
    "elle porte ici une date imprimée — « Lundi 22 avril 2024 » — rendue telle quelle, sans retouche",
    "le fiqh du crédit personnel, où le capital est le rang (ǧāh) et la confiance",
    "le rang du vendeur n'est pas un prix",
    "le don récompensé (<em>juʿl</em>, terme du registre depuis les leçons du ḍamān)",
    "l'avance qui attire le profit (<em>ğarr an-nafʿ</em>, établi à la leçon des dispositions de l'associé)",
    "la garantie sans compensation est du même bois que la compagnie sans capital",
    "le jugement suit la cause, pas l'étiquette",
    "avec ses fractions (les deux tiers du loyer, le tiers du loyer) rendues comme elles se tiennent",
    "l'arithmétique du texte ne se retouche point",
    "la fente du verset demeure VIDE dans l'imprimé",
    "aucun protocole triple requis, huitième tour sans verset vérifié",
    "la possession suit l'usage du bien, pas la main qui le tient",
    "l'usage fait la frontière du préjudice, et l'issue pèse autant que l'instant",
    "la dépense suit le fruit, le consentement fait la dette",
    "bloquer le moyen, c'est épargner le dommage",
    "le MÊME ouvrage d'Ibn Rušd pour la troisième leçon consécutive (3/37, le jugement de la ʿinān ; 3/37-38, la šarika des corps ; 3/39, les ḏimam et les visages)",
    "que la wakāla à profit inconnu ne se corrige point",
    "AUCUNE section de préparation préalable ne clôt cette leçon — elle est la dernière du cours imprimé",
    "19756, l'index des personnages ; 19757, l'index des sources et références",
    "Dispositions jurisprudentielles de la société sur les responsabilités et les visages",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19744.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
