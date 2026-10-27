#!/usr/bin/env python3
# build-19395.py — 19395 « Jurisprudence : l'effet de la défaillance du
# commanditaire d'ouvrage, du loueur et du vendeur » (fiqh-tanawi-3,
# lessons[10], badge Leçon 12/33) — suite du bāb du taflīs, huitième cours
# consécutif (4e → … → 8e). 4 axes : défaillance des maîtres des ouvrages
# (fabricant prioritaire — ouvrage pareil au gage ; tissage = ajout ;
# partage proportionnel ; choix avant l'ouvrage), défaillance du loueur et
# du locataire (désignation tient lieu de réception ; bête remplacée ;
# charge portée ; réception de restitution ; proche), défaillance du vendeur
# (vente corrompue — 3 avis Sahnūn / Ibn al-Mawwāz / Ibn al-Mājišūn ;
# revendication du vendu contre vendu), l'acte de dette (acte acquitté rendu
# et déchiré ; acte de dot chez l'épouse ; acte du gage et tafrīṭ ; témoin
# de l'acte). Ibn Rushd, Muqaddimāt 2/187. Fente liminaire VIDE (35e) ;
# fente tableau VIDE (3e) ; coquille التعبيم 7e ; 0 āya, 0 hadīth.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19395_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'br']:
    if tag in ('br',):
        continue
    o, c = html.count(f'<{tag}>'), html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')

# sondes de contenu (adaptées au balisage <em>)
PROBES = [
    'Jurisprudence : l\u2019effet de la défaillance du commanditaire d\u2019ouvrage, du loueur et du vendeur',
    'Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit',
    'Le fabricant est le plus en droit — et ce, quand bien même [le maître de l\u2019ouvrage] serait mort',
    'il partage alors, tel l\u2019ajout, à la valeur de celui-ci',
    'Le locataire [a le droit] sur la bête désignée',
    'et son maître [a le droit] sur la charge portée',
    'ce sont des avis. Mais il est le plus en droit sur son prix',
    'et sur la marchandise si elle a été vendue contre marchandise et revendiquée',
    'Il est jugé que le débiteur reprenne l\u2019acte [de dette], ou qu\u2019on le déchire',
    'nulle dot dont l\u2019acte serait rendu',
    'et au donneur de gage, son gage qui est en sa main, moyennant paiement de la dette',
    'dont le témoin ne témoigne qu\u2019en l\u2019apportant',
    'huitième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    'l\u2019ancien enseignement (at-taʿbīm)',
    'Distinguer le cas où l\u2019acheteur est le plus en droit de sa marchandise',
    'l\u2019ouvrage qui demeure sous sa main est pareil au gage',
    'tels le tailleur, le joaillier et le maçon',
    'comme le teinturier qui teint le tissu avec une teinture de lui',
    'ou le raccommodeur qui pose sur lui une pièce de lui',
    'il incombe alors au fabricant de partager [avec les créanciers] de ce qui lui a été alloué de salaire',
    'ou il résilie le contrat de louage',
    'il est alors l\u2019homologue des créanciers',
    'tels le tailleur, le foulon, le maçon et le tisserand',
    'quelle est la valeur du tissu sans teinture, et quelle la valeur de la teinture',
    'la désignation de la chose louée tient lieu de sa réception, plaçant l\u2019absent au rang du présent',
    'chez les maîtres mālikites, que Dieu leur fasse miséricorde',
    'le dire d\u2019Aṣbagh : le locataire n\u2019est pas le plus en droit d\u2019elle si elle a été remplacée',
    'Transmis par Muḥammad Ibn ʿĀʾish [Mīnāḥ al-ẓalīl 6/75]',
    'jusqu\u2019à ce qu\u2019il ait recouvré de ses bénéfices ce qu\u2019il a dépensé de loyer',
    'a. Le loueur est le plus en droit de la charge portée',
    'b. Le locataire est le plus en droit de la charge',
    's\u2019il l\u2019a reçue en réception de restitution, à l\u2019achèvement de la distance',
    'le locataire est le plus en droit de la chose louée qu\u2019il a reçue',
    'Quiconque a acheté une marchandise par un achat corrompu',
    'parce qu\u2019il l\u2019a prise contre une chose qui ne s\u2019est point achevée',
    'Ce sont trois avis : le premier est celui de Sahnūn, le deuxième celui d\u2019Ibn al-Mawwāz',
    'le troisième celui de ʿAbd al-Malik ibn al-Mājišūn',
    'la vente, quand elle s\u2019est corrompue, est devenue semblable au dépôt',
    'et le dépôt doit être rendu en son identique',
    'si elle est revenue au vendeur, et qu\u2019il devienne défaillant après cela, il est l\u2019homologue des créanciers',
    'la vente ici a porté sur un désigné, et par la revendication la vente se résilie d\u2019elle-même',
    'quiconque a vendu une marchandise contre marchandise, et que [la chose] est revendiquée de sa main',
    'l\u2019identique de sa chose si elle existe, ou sa valeur si elle a péri',
    'afin que le maître de la dette ne s\u2019en prévale une autre fois',
    'après avoir fait témoigner l\u2019acquittement de ce qu\u2019elle contient, ou écrit un acte qui la contredit',
    'sans preuve pour le débiteur de la restitution de la dette',
    'si son maître prête serment de sa persistance',
    'de ne point sortir sinon par témoignage de la décharge',
    'ce qui était demeure en son état, jusqu\u2019à ce que s\u2019établisse ce qui indique le contraire',
    'les stipulations qu\u2019il contient, la filiation si elle est contestée, le montant du mahr',
    'l\u2019achèvement de la retraite de veuvage',
    'la parole est à la parole du donneur de gage : il a acquitté ce qui était sur lui, avec serment',
    'en raison de la négligence du gagiste à recouvrer l\u2019acte du gage',
    'mais s\u2019il s\u2019élève de proche, la parole est à la parole du gagiste, avec serment',
    'car ce qui s\u2019approche d\u2019une chose en reçoit le jugement',
    'la perte de l\u2019acte de la main du demandeur — qui est le maître de la dette — tient lieu de témoin pour le défendeur',
    'les procès d\u2019argent sont de ceux qu\u2019on instruit par témoin et serment',
    'nul témoignage par acte n\u2019est reçu qu\u2019en apportant cet acte',
    'Quand le fabricant est-il le plus en droit de l\u2019ouvrage, quand son maître devient défaillant ?',
    'un homme a une dette sur un autre ; quand il la lui réclama',
    'Ibn Rushd — que Dieu lui fasse miséricorde — a dit',
    'Le louage n\u2019est point résilié par la mort de la bête, dans le louage garanti',
    'ne peut la remplacer sous lui qu\u2019avec son agrément',
    'il est le plus en droit de ce qui était sous lui le jour de la défaillance',
    'C\u2019est le dire d\u2019Ibn al-Qāsim, dans la transmission de Sahnūn, du Livre de la Mudawwana',
    'Muḥammad ibn al-Mawwāz a fait signe vers ce dire d\u2019Ibn al-Qāsim',
    'la bête de route n\u2019est pas, en soi, pareille au garanti',
    '[al-Muqaddimāt al-mumahhadāt 2/187]',
    'J\u2019explique ce qui est souligné dans le texte, et j\u2019identifie les savants mentionnés',
    'Le concept de l\u2019interdiction (<em>al-ḥağr</em>) et ses causes',
    'Les jugements de l\u2019interdiction du fou',
    'rien de la dignité du travail ne se perd dans la chute de la fortune',
    'translittérations fautives (al-mustaṣnaʿ, non « mustasna\u2019 »',
    'Sur le tissage : compté pour un ajout (<em>al-mazīd</em>)',
    'tanzīl al-maʿdūm manzilat al-mawğūd',
    'Mīnāḥ al-ẓalīl 6/75',
    'Sur les trois avis de l\u2019axe du vendeur : Sahnūn, Ibn al-Mawwāz et ʿAbd al-Malik ibn al-Mājišūn',
    'Sur l\u2019acte de dot : la restitution n\u2019est point jugée en faveur de l\u2019époux répudiateur',
    'Sur « négligence » (<em>tafrīṭ</em>)',
    'Coquille « al-Madīān » pour « al-Madīna » (la Mudawwana) consignée telle quelle',
    '35e fente du fil',
    'troisième fois dans le fichier',
    'sans rétro-révision (règle ax)',
]
for probe in PROBES:
    if probe not in html:
        issues.append('SONDE ABSENTE: ' + probe[:80])

n = len(html)
print(f"longueur totale: {n} caractères (≥ 12000 requis)")
if n < 12000:
    issues.append(f"longueur insuffisante: {n}")
print(f"sondes de contenu: {len(PROBES) - sum(1 for i in issues if i.startswith('SONDE'))}/{len(PROBES)} présentes")
print(f"guillemets: {html.count('«')} / {html.count('»')} ; em: {html.count('<em>')} / {html.count('</em>')} ; li: {html.count('<li>')} / {html.count('</li>')}")

if issues:
    print("PROBLÈMES:")
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
out = '/home/z/my-project/tr-tmp/19395.html'
open(out, 'w').write(html)
print("OK →", out)
