#!/usr/bin/env python3
# build-19500.py — 19500 « Jurisprudence : les jugements du ḍamān de l'absent
# et la différence entre le garant et le garanti » (fiqh-tanawi-3, lessons[20],
# badge Leçon 22/33) — suite du bāb, dix-huitième cours consécutif (6e → … →
# 18e). DEUX axes h3 : (1) le ḍamān de l'absent et le retour du garant —
# le ḍamān de l'absent et du déniant (farʿ/aṣl, waʿd, ġarayān al-ʿurf, iqrār,
# deux taʾwīlān, tawāṭuʿ) ; le retour bi-mā addā wa-law muqawwam in thabata
# ad-dafʿ (comme le muslif) ; la conciliation à la station du ġarīm (al-aṣaḥḥ,
# bi-l-aqall, lā ʿaksu-hu, le don de la dette au garant — Dardīr) ; (2) les
# jugements de l'accélération — deux figures (mort/fals du garant + héritier
# après terme ; mort du ġarīm « s'il en laisse »), la revendication (deux
# figures + le ḥamīl), le litige (al-qawl la-hu fī malāʾi-hi, taṣdīq, l'aveu
# qui stoppe, bayyina de l'insolvabilité, richesse renouvelée). Matn INTÉGRAL
# (un bloc, guillemet fermant présent). Exploitation : al-Mudawwana [4/98]
# (kafīl de sa personne → garant du bien ; preuve avant prise sur le kafīl ;
# « Le barres-tu de ton bien ? — Non. ») + deux tâches. 0 āya / 0 hadīth.
# Fente liminaire VIDE (3e conséc.) ; at-taʿbīm 17e occ. Préparation
# préalable → 19503 (ištirāṭ, jugements du garant, mubṭilāt).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19500_{i}.html').read())
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
    o, c = html.count(f'<{tag}'), html.count(f'</{tag}>')
    # h4 counted within h4 etc. — count exact tokens with word boundary
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

probes = [
    "Jurisprudence : les jugements du ḍamān de l'absent et la différence entre le garant et le garanti",
    "Les états du ḍamān ne se ressemblent point",
    "rempli ou démuni",
    "l'authentifier (<em>taḥrīğ</em>) par eux",
    "Quels sont les jugements du ḍamān de l'absent ?",
    "Et par quoi le garant revient-il sur le garanti ?",
    "Et quel est le jugement de leur litige ?",
    "dix-huitième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître les jugements du ḍamān de l'absent",
    "s'il a dû payer (<em>ġarima</em>)",
    "la station du ḍamān et sa responsabilité",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "si l'on réclame contre un absent et qu'il garantisse",
    "puis que l'absent dénie",
    "un réclamant contre un déniant",
    "Si je ne te l'apporte pas — lui, en personne — pour demain, je suis garant",
    "sauf que [le réclamant] établisse son droit par une preuve (<em>bayyina</em>)",
    "Et est-ce par son aveu (<em>iqrār</em>) ? Deux interprétations (<em>taʾwīlān</em>)",
    "Diffère-moi aujourd'hui ; si je ne viens pas à toi demain",
    "ce que tu réclames contre moi est un droit",
    "fût-ce un estimé (<em>muqawwam</em>), si le versement s'établit",
    "sa conciliation (<em>ṣulḥ</em>) est valide — au plus correct (<em>al-aṣaḥḥ</em>)",
    "par ce qui est valide pour le ġarīm",
    "il revient par le moindre de celle-ci ou de sa valeur",
    "Et si la racine (<em>al-aṣl</em>) est acquittée : acquittée — non le reverse",
    "s'accélère par la mort du garant",
    "son héritier revient après son terme — ou le ġarīm, s'il [le mort] en laisse",
    "si le ġarīm est présent rempli (<em>muwsir</em>)",
    "ou si son établissement contre lui n'est point difficile",
    "la parole est à lui quant à sa capacité (<em>malāʾa</em>)",
    "La compréhension",
    "Le commentaire",
    "<em>Muqawwam</em> (estimé) : ce qui a une valeur",
    "ce qu'on entend par elle ici est le débiteur (<em>al-madīn</em>)",
    "sa puissance de verser, d'acquitter",
    "La synthèse du contenu du texte",
    "Je tire du texte les jugements du ḍamān de l'absent",
    "par quoi le garant revient sur le maḍmūn ʿan-hu à son sujet",
    "l'effet du litige entre le maḍmūn la-hu et le garant",
    "L'analyse",
    "Ce cours comprend les axes suivants",
    "Axe premier : le ḍamān de l'absent et le retour du garant",
    "1. Le ḍamān de l'absent et du déniant de ce qui est réclamé",
    "l'établissement du ḍamān est corollaire (<em>farʿ</em>) de l'établissement de la dette",
    "quand la racine est nulle, le corollaire est nul",
    "une promesse (<em>waʿd</em>), qui n'est point exécutée en justice",
    "le cours de l'ʿurf (<em>ğarayān al-ʿurf</em>) par l'absence de témoignage",
    "ne regarde que la deuxième figure seule",
    "n'oblige nullement le garant en quoi que ce soit, absolument",
    "collusion (<em>tawāṭuʿ</em>) de lui avec le réclamant",
    "2. Par quoi le garant revient-il sur le garanti ?",
    "il est comme le prêteur (<em>muslif</em>)",
    "un semblable (<em>miṯlī</em>), comme un corps (<em>ʿayn</em>) ou un aliment",
    "par une preuve ou par l'aveu du détenteur du droit",
    "3. La conciliation du garant avec le détenteur de la dette",
    "car on le met à sa station (<em>manzila</em>)",
    "pour des dirhams bons avec des moindres qu'eux, ou le reverse",
    "un aliment prêté (<em>qarḍ</em>) avant le terme avec davantage",
    "le garant, le ġārim (le réclamant), revient sur le débiteur",
    "le moindre des deux ordres — qui sont la dette, ou la valeur",
    "par le don de la dette que le créancier lui fit",
    "l'échéance de la durée de son ḍamān",
    "le maître de la dette fait don de sa dette au garant",
    "la racine est réclamée pour lui, ainsi que le dit Dardīr",
    "Axe deuxième : les jugements de l'accélération de la dette garantie",
    "1. Par quoi la dette différée s'accélère-t-elle ?",
    "son décret de faillite (<em>fals</em>) de son bien",
    "n'a point de revendication sur la succession du garant",
    "le kafīl n'est point réclamé par elle jusqu'à ce que le terme arrive",
    "car sa ḏimma demeure : [la dette] arrive par la mort du débiteur",
    "2. La revendication du détenteur de la dette contre le garant",
    "que le ġarīm — c'est-à-dire le débiteur garanti — soit présent, rempli",
    "la demande est sur le garant",
    "l'établissement du bien de l'absent",
    "sans peine sévère, selon l'ʿurf — sinon il a la demande du ḥamīl (le garant-porteur)",
    "3. Les jugements du litige entre le maître de la dette et le garant",
    "la parole est au ḥamīl quant à sa capacité — c'est-à-dire [celle] du maḍmūn",
    "ce qui l'emporte chez les gens est la capacité par le gain",
    "véracité présumée (<em>taṣdīq</em>) du garant",
    "parce qu'il a avoué [l'] insolvabilité [de celui-ci]",
    "sauf qu'il dresse une preuve de l'insolvabilité",
    "ou que du bien se renouvelle pour le débiteur",
    "et cela est apparent",
    "la précaution et le scrupule (<em>al-iḥtiyāṭ wa-l-iḥtirāz</em>)",
    "garder les droits et de les préserver de la manipulation et de l'abus",
    "ils sont le pilier (<em>qiwām</em>) de la vie",
    "Le contrôle",
    "Je montre les jugements du ḍamān de l'absent et du déniant du droit",
    "J'expose les jugements de l'accélération de la dette garantie",
    "Je départage le dire dans le litige du garant et du maḍmūn la-hu",
    "L'exploitation",
    "Il est venu dans la Mudawwana",
    "Vois-tu si un homme réclame contre un homme un droit",
    "et que le réclamé-contre dénie",
    "Je suis pour toi kafīl de sa personne jusqu'à demain",
    "si je ne te l'apporte pas, je suis garant du bien",
    "Établis ton droit, et dresse la preuve sur ton droit — sinon tu n'as rien",
    "il ne lui est point donné de prendre du kafīl quoi que ce soit",
    "Le barres-tu de ton bien ? Il dit : Non.",
    "[La Mudawwana 4/98]",
    "J'examine ces deux textes et je réponds comme suit",
    "Je compare entre ce qui est dans ce texte et le dire du compilateur",
    "qui est le demandeur et qui est le répondant",
    "La préparation préalable",
    "Je lis le matn du cours à venir et je réponds comme suit",
    "Quand l'instrement (<em>al-ištirāṭ</em>) dans le ḍamān profite-t-il ?",
    "Je recherche quelques jugements du garant",
    "Quels sont les annulatifs (<em>mubṭilāt</em>) du ḍamān ?",
    "Notes du traducteur",
    "l'étiquette GT « la caution de l'absent et le différend entre garant et garanti »",
    "« les jugements » (<em>ahkām</em>) est porté par le h1 et manque à l'étiquette",
    "« le différend » → « la différence »",
    "quinzième tranchage du fil",
    "VIDE pour la troisième leçon consécutive",
    "une treizième fois consécutive (6e → … → 18e)",
    "dix-septième occurrence",
    "le <em>lā</em> initial du Mukhtaṣar",
    "le pont du kafīl au ḍāmin",
    "l'ʿurf suppléant la preuve là où le témoignage manque",
    "le soupçon de collusion (<em>tawāṭuʿ</em>)",
    "les deux ordres du retour — l'estimé en valeur et le semblable fongible",
    "la préférence doctrinale de Khalīl entre deux dires",
    "la dévolution du rang (<em>manzila</em>)",
    "le garant devient réclamant (<em>ġārim</em>)",
    "la règle de la racine et du corollaire",
    "l'anatomie commune du ḍamān et de la ḥawāla (R314-R315)",
    "rendue avec crochets du traducteur",
    "nom mālikite du kafīl, déjà sous la plume d'al-Māzarī",
    "l'aveu du créancier — son propre dire le lie et le stoppe",
    "la convention éditoriale de la Mudawwana",
    "sa portée exacte laissée sans tranchement (règle ax)",
    "le bāb du ḍamān compte trois cours (19496 → 19500 → 19503)",
    "les biens, « le pilier de la vie » — est porté par l'imprimé en clôture de l'axe deuxième",
]

missing = [p.replace("'", chr(0x2019)) for p in probes if p.replace("'", chr(0x2019)) not in html]
if missing:
    issues.append(f"SONDES ABSENTES ({len(missing)}): " + " || ".join(missing[:6]))

if issues:
    print("BUILD ÉCHOUÉ :")
    for i in issues:
        print("  -", i[:500])
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19500.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"BUILD OK : {len(html)} caractères, {len(probes)} sondes OK, guillemets {html.count('«')}/{html.count('»')}")
