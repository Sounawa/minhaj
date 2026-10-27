#!/usr/bin/env python3
# build-19503.py — 19503 « Jurisprudence : l'instrement dans le ḍamān et
# ses annulatifs » (fiqh-tanawi-3, lessons[21], badge Leçon 23/33) — suite
# et clôture du cœur du bāb, dix-neuvième cours consécutif (6e → … → 19e).
# TROIS axes h3 : (1) ce qui produit des conditions dans le ḍamān — l'instrement
# du maître de la dette (prendre de l'un des deux qu'il veut + préférer ;
# la fonction au regard du ḥamīl : absolument au lieu de l'impossibilité ;
# ḫilāf al-aṣl ; l'acquittement instrent ou non) et l'instrement du garant
# (la mort démunie comme condition ; faillite sans mort ; les variantes
# iftaqara/ğaḥida/aqarra ; le paragone ḏī l-wağh / rabb ad-dayn — taṣdīq
# dans l'amener, avec ou sans serment) ; (2) parmi les jugements du garant —
# la demande du dégagement (at-taḫlīṣ) à l'échéance ; la remise refusée
# (ittibāʿ du débiteur après la mort/faillite du kafīl) ; le ḍamān de la
# prise (mutaʿaddin, iqtidāʾ, trois modes) vs l'envoi (amīn, tafrīṭ, wakāla
# pour lui — le garant seul acquitté) ; ce qui lie le garant — l'ajournement
# du démuni (rifq) et les TROIS visages du rempli (savoir+silence / ne pas
# savoir+serment / savoir+refus ibrāʾ) + l'ajournement du ḥamīl entraînant
# celui du débiteur ; (3) les annulatifs — le porté corrompu (ribā : mille
# pour deux mille, dirhems pour dinars ; le prix corrompu : marchandise pour
# du vin) ; la corruption par le juʿl (salaf avec accroissement ; l'un des
# trois qui ne sont que pour Dieu — ḍamān/qarḍ/ğāh ; le retour au tiers
# avant la science du créancier — Ibn al-Qāsim) ; l'exagération : le ḍamān
# du propre maḍmūn nul sauf achat/vente d'une chose déterminée (širka, salam)
# comme leur prêt — au plus correct, Ibn ʿAbd as-Salām. Matn INTÉGRAL (un
# bloc). Exploitation : Dasūqī [Hāšiya 3/339] — cinq espèces de la qabḍ,
# la parole au débiteur dans le litige, le garant ġarīm dans les trois
# figures, « le ġarīm du ġarīm est ġarīm », ar-Rağrāğī. 0 āya / 0 hadīth.
# Fente liminaire VIDE (4e conséc.) ; at-taʿbīm 18e occ. ; double « rahimahu
# llāh » consigné. Préparation préalable → la pluralité des porteurs et la
# division dans le portage.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19503_{i}.html').read())
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
    "Jurisprudence : l'instrement dans le ḍamān et ses annulatifs",
    "ignorant ce que les conditions lui produisent et ce qui ne lui produit point",
    "qu'il croit le lier, alors qu'en réalité elles ne le lient point",
    "Qu'est-ce qui produit, des conditions, dans le ḍamān — et qu'est-ce qui ne produit point ?",
    "Et quels sont les annulatifs du ḍamān ?",
    "dix-neuvième leçon",
    "at-taʿbīm al-ʿatīq",
    "Connaître ce qui produit des conditions dans le ḍamān et ce qui ne produit pas",
    "Connaître les annulatifs du ḍamān",
    "Se représenter les jugements du ḍamān dans les transactions",
    "Le texte",
    "Le cheikh Khalīl — que Dieu lui fasse miséricorde — a dit",
    "Et a produit l'instrement qu'il prenne [son droit] de l'un des deux qu'il veut",
    "ou [qu'il n'en soit pris] que s'il [le garanti] meurt",
    "comme l'instrement du <em>ḏī l-wağh</em> (l'homme de l'intercession), ou du maître de la dette — la véracité (<em>taṣdīq</em>) dans l'amener",
    "la demande du détenteur du droit de le dégager, à son terme — non par la remise du bien à lui",
    "et il garantit [la perte du bien] s'il le requiert, non s'il en est envoyé",
    "Et le lie l'ajournement par son maître du démuni",
    "ou du rempli, s'il se tait, ou ne sait point",
    "s'il jure qu'il ne l'ajourna point en déchargeur",
    "et s'il dénie, il jure qu'il n'en fit point décharge — et cela le lie",
    "et son ġarīm est ajourné par son ajournement — sauf qu'il jure",
    "Et il est nul si le porté par lui est corrompu, ou si elle est corrompue",
    "comme un don récompensé (<em>juʿl</em>) — d'autre que son maître — pour son débiteur",
    "quand bien même [le juʿl] serait le ḍamān de son propre garanti",
    "sauf dans l'achat d'une chose entre eux deux, ou sa vente — comme leur prêt, au plus correct",
    "La compréhension",
    "Le commentaire",
    "Le détenteur du droit (<em>al-mustaḥiqq</em>) : le maître de la dette",
    "ce que l'on établit pour l'ouvrier sur son ouvrage",
    "ce que tu donnes à un autre, d'un bien, pour qu'il s'en acquitte",
    "La synthèse du contenu du texte",
    "quand l'instrement produit de la part du maître du droit et du garant",
    "Je tire du texte les jugements du garant",
    "Je tire du texte les annulatifs du ḍamān",
    "L'analyse",
    "Ce cours comprend les axes suivants",
    "Axe premier : ce qui produit des conditions dans le ḍamān",
    "1. L'instrement du maître de la dette",
    "la fonction de cet instrement est au regard du ḥamīl",
    "tandis qu'ici il est réclamé absolument",
    "tombe sa revendication du débiteur",
    "contre l'origine (<em>ḫilāf al-aṣl</em>)",
    "qu'il ait instrent l'acquittement du débiteur ou non",
    "sauf quand la prise auprès du ḥamīl devient impossible : il revendique alors le débiteur et prend de lui",
    "2. L'instrement du garant",
    "que le maḍmūn meure démuni — son instrement est opéré",
    "s'il tomba en faillite sans mourir, il n'a point de demande de lui sur le ḥamīl",
    "« s'il devient destitué », ou : « s'il dénie », ou : « s'il avoue »",
    "Et le compilateur a PARAGONNÉ la production de l'instrement",
    "si le garant de la face (<em>ḍāmin al-wağh</em>) insta avec le détenteur de la dette qu'il est vérace (<em>muṣaddiq</em>)",
    "sans serment ou avec serment — son instrement est opéré",
    "l'absence de serment dans la véracité de sa prétention de ne point amener le maḍmūn",
    "Axe deuxième : parmi les jugements du garant",
    "1. La revendication du garant au maître de la dette de le dégager du ḍamān",
    "de dégager le droit du débiteur, ou de le dégager lui du ḍamān",
    "quand bien même par la mort du débiteur ou sa faillite, là où le maḍmūn est rempli",
    "ou bien tu réclames ton droit du débiteur, ou bien tu me dégages du ḍamān",
    "quand bien même le maître de la dette ne l'eût point réclamé",
    "il n'a point cela avant l'arrivée du terme",
    "2. La revendication du garant au débiteur de la remise du bien garanti",
    "le garant n'a point la demande du débiteur garanti qu'il remette le bien garanti au garant",
    "le détenteur de la dette pourrait suivre le débiteur et le réclamer",
    "que Dieu lui fasse miséricorde — que Dieu lui fasse miséricorde",
    "le kafīl garantit le bien si celui-ci périt de lui ou se perd",
    "fût-ce un corps (<em>ʿayn</em>), une marchandise, ou un animal",
    "il outrepasse (<em>mutaʿaddin</em>) dans sa prise, s'il la prise sur le mode du requis (<em>iqtidāʾ</em>)",
    "soit qu'il l'eût demandé à l'origine (l'<em>aṣīl</em>) et que celui-ci le lui eût remis",
    "sans demande, en disant : « j'en suis quitte »",
    "par sentence d'un qāḍī, lors de l'absence de son maître et de l'arrivée du terme",
    "pour le mettre à la station de son maître : il est son wakīl",
    "si le débiteur envoya le garant avec le bien garanti vers son maître",
    "sans négligence (<em>tafrīṭ</em>) : nul ḍamān sur lui, car il est son amīn — et c'est le débiteur qui le garantit",
    "alors seul le garant est acquitté, non le ġarīm",
    "3. Qu'est-ce qui lie le garant ?",
    "car l'ajournement est douceur (<em>rifq</em>) envers le ḥamīl",
    "l'affaire n'est point sans trois visages",
    "Le premier visage :",
    "que le garant sache l'ajournement par le maître de la dette du ġarīm, et se taise",
    "Le deuxième visage :",
    "et le ġarīm est devenu démuni — le ḍamān est alors ferme pour le ḥamīl",
    "s'il s'esquive (<em>nakala</em>), le ḍamān tombe",
    "Le troisième visage :",
    "« ton ajournement du débiteur est pour moi acquittement (<em>ibrāʾ</em>) du ḍamān »",
    "le droit est pris de lui à l'instant, et il retourne par lui à l'arrivée du terme de l'ajournement sur le débiteur",
    "si le maître de la dette s'esquive, le ḍamān tombe et l'ajournement lie",
    "l'ajournement du débiteur, par cause de l'ajournement du ḥamīl",
    "l'ajournement du ġarīm lui lie aussi",
    "Axe troisième : les annulatifs du ḍamān",
    "1. La corruption du porté",
    "si la dette portée est corrompue, son ḍamān est nul — rien ne lie le garant",
    "comme si c'était une usure (<em>ribā</em>)",
    "« Verse à celui-ci mille dirhems pour deux mille, jusqu'au mois »",
    "« Verse-lui des dirhems pour des dinars jusqu'au mois, et je suis ton ḥamīl pour cela »",
    "vendre une marchandise pour du vin",
    "2. La corruption du portage par le don récompensé",
    "si la ḥimāla est corrompue en loi (<em>šarʿan</em>) — en ce qu'elle est interdite — le ḍamān est nul",
    "ou du débiteur, ou d'un tiers — au garant",
    "il retourne par ce qu'il a défrayé, avec l'accroissement du don récompensé",
    "car c'est un prêt (<em>salaf</em>) avec accroissement",
    "le ḍamān est l'un des trois qui ne sont que pour Dieu : le deuxième d'entre eux le prêt (<em>qarḍ</em>), le troisième le prestige (<em>ğāh</em>)",
    "elle ne se corrompt point, selon Ibn al-Qāsim et d'autres",
    "Le compilateur alla AU DELÀ sur la nullité du ḍamān par le don récompensé",
    "comme si deux hommes se prêtaient mutuellement une dette d'un homme, ou de deux hommes",
    "quand ils entrèrent en cela PAR l'instrement",
    "excepté l'achat d'une chose déterminée entre eux : une société (<em>širka</em>)",
    "comme si quelqu'un les dotait (<em>aslama</em> — le salam) en une chose",
    "alors c'est permis, au plus correct, selon Ibn ʿAbd as-Salām",
    "la Sharīʿa généreuse vise la garde des droits d'autrui",
    "ou de la spoliation et de l'agression contre eux",
    "l'importance du fiqh des biens",
    "Le contrôle",
    "J'expose quand l'instrement produit de la part du maître du droit et du garant",
    "Je cite les jugements du garant",
    "Je passe en revue les annulatifs du ḍamān",
    "L'exploitation",
    "L'illustre Dasūqī — que Dieu lui fasse miséricorde — a dit",
    "la prise (<em>qabḍ</em>) du ḥamīl de la dette se divise en cinq espèces",
    "ou sur le mode du requis (<em>iqtidāʾ</em>), ou de l'envoi (<em>irsāl</em>), ou de la wakāla pour le maître du droit",
    "la prise se trouve dépouillée des indications contextuelles (<em>qarāʾin</em>)",
    "le débiteur disant : « requis », et le garant : « envoi » — la parole au débiteur",
    "ou que l'affaire devînt ambiguë par absence d'indication",
    "en vérité ou en jugement, qu'il la prenne sur le mode de la wakāla du maître de la dette",
    "le garant est ġarīm dans les trois figures entrant sous son dire « s'il le requiert »",
    "Et il est connu que le ġarīm du ġarīm est ġarīm",
    "le maître de la dette peut donc défrayer l'aṣīl",
    "il peut défrayer le garant en députation du débiteur",
    "comme l'a explicité ar-Rağrāğī dans le Šarḥ muškilāt al-Mudawwana et d'autres",
    "l'aṣīl a le retour sur le kafīl",
    "[Hāšiya d'ad-Dasūqī 3/339]",
    "J'examine ce texte avec soin et je réponds à ce qui suit",
    "Je tire du texte les figures de la prise du garant de la dette",
    "Je montre quand le garant est ġarīm",
    "« le ġarīm du ġarīm est ġarīm »",
    "La préparation préalable",
    "Je lis le matn du cours suivant et j'accomplis ce qui suit",
    "Je recherche les autres jugements du ḍamān",
    "la pluralité des porteurs (<em>taʿaddud al-ḥummal</em>)",
    "la manière de la division dans le portage",
    "Notes du traducteur",
    "l'étiquette GT « stipuler une garantie et ses invalidations »",
    "« stipuler » → « l'instrement »",
    "« ses invalidations » → « ses annulatifs »",
    "seizième tranchage du fil",
    "VIDE pour la quatrième leçon consécutive",
    "une quatorzième fois consécutive (6e → … → 19e)",
    "dix-huitième occurrence",
    "« l'homme de l'intercession »",
    "avec instrement, « absolument »",
    "la lettre exacte du « contre l'origine » laissée sans tranchement",
    "la mort DÉMUNIE du maḍmūn comme condition",
    "« s'il devient destitué », « s'il dénie », « s'il avoue »",
    "le compilateur a PARAGONNÉ",
    "le garant maître du rythme, non l'inverse",
    "la dette ne se déplace point par la possession",
    "la prise sans permission faisant sortir le garant de sa station de porteur",
    "« seul le garant est acquitté, non le ġarīm »",
    "la formule DOUBLÉE rendue telle quelle",
    "l'esquive — <em>nakl</em> — faisant tomber le ḍamān",
    "le temps du garant et le temps du débiteur s'enchaînent",
    "la triple libéralité nommée par le commentaire",
    "l'ombre de la <em>ribā</em>",
    "la science du CRÉDITEUR comme condition de la corruption",
    "la forme du verbe imprimé (<em>aslama</em> — « les dotait »)",
    "la coquille « <em>ʾastaḫliḍ</em> » pour « <em>ʾastaḫliṣ</em> »",
    "les cinq espèces de la prise",
    "ar-Rağrāğī (Šarḥ muškilāt al-Mudawwana) nommé",
    "le retour de l'aṣīl sur le kafīl",
    "la pluralité des porteurs (<em>taʿaddud al-ḥummal</em>) et la manière de la division dans le portage",
    "le bāb du ḍamān se poursuit",
]

missing = [p.replace("'", chr(0x2019)) for p in probes if p.replace("'", chr(0x2019)) not in html]
if missing:
    issues.append(f"SONDES ABSENTES ({len(missing)}): " + " || ".join(missing[:6]))

if issues:
    print("BUILD ÉCHOUÉ :")
    for i in issues:
        print("  -", i[:500])
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19503.html'
open(out, 'w', encoding='utf-8').write(html)
print(f"BUILD OK : {len(html)} caractères, {len(probes)} sondes OK, guillemets {html.count('«')}/{html.count('»')}")
