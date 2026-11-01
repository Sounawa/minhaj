#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 730 (tafsir-5ep, Isrāʾ 86-89).
Vérifie : rendus français des versets 86-89 (rasm warš du cache — dont le
v.89 warš « fa-abā aktharu n-nāsi illā kufūran », distinct de la lecture
ḥafṣī « wa-lākin akthara n-nāsi lā yaʿlamūn »), les gloses lexicales
(at-taṣrīf la répétition et la réitération, min kulli mathal, kufūr le déni
et le refus), les noms portés (Ibn Ḫuwayzmandād, Ibn ʿAṭiyya, al-Fakhr
ar-Rāzī, Bušr, Abū ʿAmr ben al-ʿAlāʾ, al-Aʿšā, Dhū r-Rumma, Jarīr,
al-Farazdaq, al-Asmaʿī, Moïse, Jésus, Ibn ʿAǧība al-Baḥr al-madīd 3/230),
les matières (le retrait de la révélation et le wakīl — la promesse de
l'interprétation de l'esprit, l'exception discontinue de « illā raḥmatan »
et Ibn Ḫuwayzmandād, le sommet de la grâce et le v.87, le défi des hommes
et des djinns — la cause de la descente, le naẓm et l'enveloppement, la
carence humaine —, la grammaire du lām et du jussif, le ẓahīr/muʿīn — lemme
corrompu déclaré —, l'iʿjāz et les maîtres de l'éloquence — Dhū r-Rumma,
Jarīr et al-Farazdaq, le Bédouin, Bušr et al-Aʿšā, al-Asmaʿī —, la magie de
Moïse et la médecine de Jésus, l'épée des intransigeants, le défi par les
dix sūras restreint à l'iftirāʾ et « fa-ʾtū bi-sūratin min miṯlihī » au rasm
du cache al-Baqara 23, Hūd, le taklīf mā lā yuṭāq et les dix inventées, le
v.89 — le li-taṣrīfan et le masdar elidé, les deux lectures de « min kulli
mathal », les gloses médianes à lemmes altérés — kasb/kufr, masdar du faire
d'Allah —, la glose finale de l'exception et « abā » au sens de la négation,
Ibn ʿAǧība 3/230 —, les finalités, l'exploitation ar-Rāzī — l'objection des
djinns, tête/milieu/fin dégradés déclarés —, la préparation 90-93 au DOM —
imprimé « 39 - 09 » inversé —, l'absence de citations hors rasm (17:82-85 =
leçon précédente ; 17:90-93 = leçon suivante — interdites au corps après
l'évaluation), 0 arabe résiduel. Espaces typographiques (NNBSP/insécables)
introduits par l'auto-fix de qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-730.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Et si Nous voulions, Nous emporterions certes ce que Nous t’avons révélé",
    "tu ne trouverais pas, en cela, contre Nous de défenseur",
    "Hors une miséricorde venant de ton Seigneur",
    "Sa faveur envers toi est immense",
    "si les hommes et les djinns se concertaient",
    "ils ne viendraient pas avec son semblable",
    "fussent-ils les uns les soutiens des autres",
    "toute parabole",
    "mais la plupart des gens refusèrent, hormis la dénégation",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(86-89\)", norm):
    errors.append("repère de plage (86-89) absent")

for frag in [
    "répéter et réitérer selon des modes variés",
    "l’affirmation et la fermeté",
    "chaque beau sens, en l’élégance, la singularité et la maîtrise",
    "déni et refus",
    "We emporterions",  # sentinelle — doit échouer (coquille volontaire non introduite)
]:
    if frag == "We emporterions":
        continue  # sentinelle neutre
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

for frag in [
    "une manifestation de Ses manifestations de puissance",
    "l’esprit relève de Son ordre",
    "l’interprétation de l’esprit que tu as voulu interpréter pour les gens",
    "à quoi tu les avais engagés par ta promesse",
    "la protection ou la dispute",
    "exception discontinue (munqaṭiʿ)",
    "une miséricorde de ton Seigneur retient cela de toi",
    "la continue particularise du genre ou de la phrase",
    "hormis un non-Arabe (aʿjamī)",
    "Ibn Ḫuwayzmandād",
    "le sommet de Sa grâce en son privilège de la prophétie",
    "Sa protection contre les associateurs",
    "défier les associateurs par ce Coran",
    "ô Muḥammad, nous venons [à toi] d’une parole étrangère",
    "explicite dans la mise en impuissance (taʿjīz)",
    "hommes et djinns, s’ils unissaient leurs efforts",
    "l’ordonnancement (naẓm) et le rangement de ses sens",
    "l’enveloppement que nul ne possède hormis Allah",
    "l’ignorance, l’oubli, l’inadvertance",
    "indicatrice, non obligatoire",
    "le verbe nié vient au jussif",
    "une négation de réponse",
    "le sens de « soutien » (ẓahīr) est « auxiliaire » (muʿīn)",
    "lemme coranique corrompu dans la couche texte, déclaré perdu",
    "en tout état posé",
    "pure compréhension en la mesure du discours",
    "de nécessité et par témoignage",
    "la science acquise étant décisive",
    "la Loi du Prophète et ses actes par la science du témoignage",
    "transmission de la transmission massive (tawātur)",
    "Dhū r-Rumma",
    "yaʿuddu n-nāsibūna ilā Tamīm",
    "en les vers de Jarīr",
    "l’histoire de Jarīr en ses nawādir avec al-Farazdaq",
    "lāma t-lafatayn",
    "talafat annahā taḥta bni qayn",
    "ʿazza fa-ḥkama fa-qaṭaʿa",
    "Bušr",
    "Abū ʿAmr ben al-ʿAlāʾ",
    "en les vers d’al-Aʿšā",
    "wa-ankartanī wa-mā kāna lladhī nakartu",
    "al-Asmaʿī",
    "un verbe qui surpasse le poli des vers",
    "leurs réponses laconiques",
    "la magie fut au temps de Moïse et la médecine au temps de Jésus",
    "les intransigeants d’entre eux recoururent à l’épée",
    "la profanation des sanctuaires",
    "le défi par les dix sūras",
    "en un point unique — l’ordonnancement en propre",
    "restreint à l’invention (iftirāʾ)",
    "dix sūras inventées de même",
    "fa-ʾtū bi-sūratin min miṯlihī",
    "al-Baqara 23",
    "en sūrat Hūd",
    "l’injonction impossible (taklīf mā lā yuṭāq)",
    "allégé vers les dix inventées",
    "ce qui se dénoue à l’examen",
    "ils persévérèrent en leur tyrannie et leur déni du Noble Coran",
    "« en un dessein de variation » (li-taṣrīfan)",
    "d’un « Nous avons varié » elidé",
    "la variation de la parole est la répétition de l’explication du sens",
    "emphatique redondante",
    "le kufr des mécréants comme acquisition (kasb) de leur part",
    "comme acquisition (kasb) de leur part",
    "le masdar au faire d’Allah",
    "en la création et l’engendrement",
    "par acquisition et persévérance, il est de l’homme",
    "« abā » étant au sens de la négation",
    "hormis le kufr en cela",
    "Ibn ʿAǧība",
    "al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd",
    "3/230",
    "les fondements les plus fermes",
    "une seule sūra à sa semblance",
    "l’adoration de la pierre (ḥaǧar)",
    "Al-Fakhr ar-Rāzī",
    "ce que les djinns auraient lancé sur Muḥammad",
    "le tour se retourne",
    "il est le discours d’Allah",
    "J’extrais l’objection venue dans le texte",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")


def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)


cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v86, v87, v88, v89 = (ar17[i] for i in range(86, 90))
b86, b87, b88, b89 = (bare(v) for v in (v86, v87, v88, v89))
for f in ["ولئن شئنا لنذهبن بلذى أوحينا إليك", "ثم لا تجد لك به علينا وكيلا"]:
    if f not in b86:
        errors.append(f"cache 17:86 inattendu ({f[:35]})")
for f in ["إلا رحمة من ربك", "إن فضله كان عليك كبيرا"]:
    if f not in b87:
        errors.append(f"cache 17:87 inattendu ({f[:35]})")
for f in ["قل لئن جتمعت لإنس ولجن على أن يأتوا بمثل هذا لقرءان", "لا يأتون بمثله ولو كان بعضهم لبعض ظهيرا"]:
    if f not in b88:
        errors.append(f"cache 17:88 inattendu ({f[:35]})")
for f in ["ولقد صرفنا للناس فى هذا لقرءان من كل مثل", "فأبى أكثر لناس إلا كفورا"]:
    if f not in b89:
        errors.append(f"cache 17:89 inattendu ({f[:35]})")
ar2 = dict((i, t) for i, t in cache["2"]["ar"])
if "بسورة من مثله" not in bare(ar2[23]):
    errors.append("cache 2:23 inattendu (lemme « fa-ʾtū bi-sūratin min miṯlihī »)")

# préparation de la leçon suivante au DOM
if "90 à 93" not in norm or "39 - 09" not in norm:
    errors.append("préparation : les versets 90-93 (imprimé « 39 - 09 ») absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation
# (17:82-85 = leçon précédente 729 ; 17:90-93 = leçon suivante 731)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"ce qui est guérison et miséricorde", "al-Isrāʾ 17:82 (leçon précédente — non portée)"),
    (r"il se détourne et s’écarte de côté", "al-Isrāʾ 17:83 (leçon précédente — non portée)"),
    (r"chacun agit selon sa disposition", "al-Isrāʾ 17:84 (leçon précédente — non portée)"),
    (r"l’esprit relève de l’ordre de mon Seigneur", "al-Isrāʾ 17:85 (leçon précédente — non portée)"),
    (r"nous ne croirons pas tant que", "al-Isrāʾ 17:90 (leçon suivante — non portée)"),
    (r"jaillissement", "al-Isrāʾ 17:90 (leçon suivante — non portée)"),
    (r"de dattiers et de vignes", "al-Isrāʾ 17:91 (leçon suivante — non portée)"),
    (r"le ciel tombe sur nous", "al-Isrāʾ 17:92 (leçon suivante — non portée)"),
    (r"des anges en rangs", "al-Isrāʾ 17:93 (leçon suivante — non portée)"),
]:
    if re.search(pat, body, re.IGNORECASE):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", norm):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 730 — versets 86-89 rendus sur le rasm warš du cache (le retrait "
      "possible de la révélation sans défenseur, la miséricorde et la faveur immense, le "
      "défi des hommes et des djinns fussent-ils soutiens les uns des autres, le "
      "déploiement de toute parabole et le refus hors dénégation — rasm warš « fa-abā "
      "aktharu n-nāsi illā kufūran »), les gloses lexicales (at-taṣrīf, min kulli mathal, "
      "kufūr), le tafsīr de la grâce (le wakīl et la promesse de l'interprétation, "
      "l'exception discontinue et Ibn Ḫuwayzmandād, le sommet de la grâce), le défi (la "
      "cause de la descente, le naẓm et l'enveloppement, la carence humaine, le lām et "
      "le jussif, le ẓahīr/muʿīn — lemme corrompu déclaré —, les maîtres de l'éloquence : "
      "Dhū r-Rumma, Jarīr et al-Farazdaq, le Bédouin, Bušr et al-Aʿšā, al-Asmaʿī, la "
      "magie de Moïse et la médecine de Jésus, l'épée des intransigeants —, le défi par "
      "les dix sūras restreint à l'iftirāʾ avec « fa-ʾtū bi-sūratin min miṯlihī » au "
      "rasm du cache al-Baqara 23 et Hūd, le taklīf mā lā yuṭāq —, le v.89 : le "
      "li-taṣrīfan et le masdar elidé, les deux lectures de « min kulli mathal », les "
      "gloses médianes à lemmes altérés — kasb/kufr, masdar du faire d'Allah —, la glose "
      "finale de l'exception avec « abā » au sens de la négation, Ibn ʿAǧība al-Baḥr "
      "al-madīd 3/230), les finalités (2), l'exploitation d'al-Fakhr ar-Rāzī (l'objection "
      "des djinns — tête, milieu et fin dégradés, déclarés), la préparation 90-93 au DOM "
      "(imprimé « 39 - 09 » inversé, lu 90 et 93 par l'étiquette du livre), aucune "
      "citation hors rasm (17:82-85 interdits au corps après l'évaluation — leçon "
      "précédente ; 17:90-93 interdits — leçon suivante), 0 arabe résiduel.")
