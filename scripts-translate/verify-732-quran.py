#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 732 (tafsir-5ep, Isrāʾ 94-98).
Vérifie : rendus français des versets 94-98 (rasm warš du cache — le refus de
croire à la venue du guide, « a-baʿaṯa llāhu bašaran rasūlan », les anges
marchant tranquillement et l'ange-messager, « kafā bi-llāhi šahīdan », le
guidé et l'égarement, la résurrection sur les visages et l'Enfer qui
s'apaise, la sanction des ossements et de la poussière), les gloses lexicales
et matières (le défini de « les gens » pour l'immersion, la mission des
humains ni innovation ni chose étrange, la mise en demeure corrompue et
l'entêtement vain, les mécréants de Quraysh, l'ifhām et les anges s'établissant
résidents, les natures qui fuiraient, la royauté et la richesse offertes, « qui
donc témoignera pour toi », la troupe des anges, le qāḍī Abū Muḥammad, la
création de la guidance et de l'égarement, « ce qui dépasse la transmission
n'est pas en ma main », le Connaisseur et le Clairvoyant, al-Bayḍāwī
3/762 — consolation et menace —, les métaphores de la perplexité et la vérité
du lever des tombes, le retour des vues et de l'ouïe, « il s'en est allé sur
son visage », le chameau abattu, la capacité au transport sur les visages, le
hadith d'Anas et la réponse du Prophète ﷺ, Qatāda, Ṣaḥīḥ al-Bukhārī, le ḫabat
du Feu et l'apaisement de la flamme, les preuves et les arguments, « et
poussière » le reste réduit à la poussière, la résurrection mouvoir l'immobile),
les noms portés (Anas, Qatāda, al-Bukhārī, al-Bayḍāwī, Muḥammad), les finalités
(3), les fragments de rasm du cache (17:94-98 ; 17:99 « aǧalan lā rayba fīh »
et 17:100 « ḫazāʾin raḥmatin » et « qatūran » pour la préparation), la
préparation 99-100 au DOM — imprimé « 99 - 001 » inversé —, l'absence de
citations hors rasm (17:90-93 = leçon précédente ; 17:99-100 = leçon suivante
— interdites au corps après l'évaluation), 0 arabe résiduel. Espaces
typographiques (NNBSP/insécables) introduits par l'auto-fix de qa-lesson
normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-732.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Et rien n’empêcha les gens de croire, quand le guide leur est parvenu",
    "Allah envoie-t-Il un être humain messager",
    "S’il y avait sur terre des anges marchant tranquillement",
    "un ange-messager",
    "Allah suffit comme témoin entre vous et moi",
    "parfaitement Connaisseur et Clairvoyant",
    "Celui qu’Allah guide, c’est lui le bien-guidé",
    "tu ne leur trouveras jamais d’alliés en dehors de Lui",
    "Nous les rassemblerons traînés sur leurs visages",
    "aveugles, muets et sourds",
    "chaque fois que son feu s’affaiblit",
    "la flamme ardente",
    "Telle sera leur sanction",
    "ossements et poussière",
    "une nouvelle création",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(94-98\)", norm):
    errors.append("repère de plage (94-98) absent")

for frag in [
    "le style sage de la réponse d’Allah",
    "ce dont je n’ai pas la capacité",
    "des choses ridicules",
    "leur prétention que le Messager ne peut être un être humain",
    "le déni par les associateurs de la mission du Prophète ﷺ",
    "en sanction de leur entêtement, leur obstination et leur déni des āyāt de leur Seigneur",
    "Quelles sont les prétentions qu’Allah — très-Haut — a annulées",
    "Pour qui Allah — très-Haut — a-t-Il préparé le châtiment",
    "la réalisation de demandes se bousculant",
    "exposant la cause de leur mécréance",
    "la première lecture au régime de l’accusatif par élision",
    "la seconde au régime du nominatif",
    "le défini de « les gens » pour l’immersion",
    "leur fausse imagination et leur étonnement",
    "des messagers d’entre les humains",
    "ni une innovation ni une chose étrange",
    "enverrait un ange comme messager aux créatures",
    "ils ne croiraient qu’en son être messager de la part d’Allah",
    "l’attestation de sa mission s’impose",
    "ils ont nié les miracles que le Prophète ﷺ apporta",
    "une mise en demeure corrompue et un entêtement vain",
    "L’ensemble de cette āya embrassa les mécréants de Quraysh",
    "cette équivoque effondrée",
    "du blâme et de la noue de la part du Prophète — paix sur lui",
    "cette cause repoussante (lemme imprimé altéré)",
    "l’exclusion qui ne s’appuie sur aucun argument",
    "le sens d’écarter et la possibilité de considérer",
    "des anges l’habitants tranquillement",
    "s’y établissant résidents",
    "leurs natures fuiraient à sa vue",
    "leurs yeux ne le soutiendraient pas",
    "leurs cœurs ne lui tiendraient pas",
    "leurs états courent sur leur habitude",
    "Puis Allah réveilla Son messager ﷺ",
    "l’offre de la royauté et de la richesse",
    "qui donc témoignera pour toi que tu es véridique en ta prophétie",
    "une troupe des anges témoignant pour toi",
    "et cette āya descendit",
    "le qāḍī Abū Muḥammad",
    "la demande d’un témoignage sans qu’ils le mentionnent",
    "la nouvelle et la vue de nous tous",
    "du véridique et du menteur",
    "Sa production de la guidance et de l’égarement dans les cœurs des humains",
    "ce qui dépasse la transmission n’est pas en ma main",
    "Anwār at-tanzīl wa-asrār at-taʾwīl",
    "al-Bayḍāwī : 3/762",
    "consolation pour le Messager ﷺ et menace pour les mécréants",
    "l’immensité de Sa puissance sur Ses créatures",
    "la pénétration de Son jugement en elles",
    "la menace globale",
    "ce sont des métaphores",
    "de perplexité, d’angoisse et de stupeur",
    "ils ne voient pas ce qui les réfute",
    "tels sont leurs attributs en vérité",
    "à leur lever de leurs tombes",
    "Allah retourne alors à eux leurs vues, leur ouïe et leur parole",
    "ils voient le Feu, entendent son souffle",
    "« il s’en est allé sur son visage »",
    "« comme s’il marchait sur son visage »",
    "Allah les rend capables du transport sur les visages",
    "du transport sur les pieds",
    "le hadith d’Anas — qu’Allah l’agrée",
    "le mécréant sera-t-il rassemblé sur son visage au Jour de la Résurrection",
    "Celui qui le fait marcher sur ses deux pieds en ce bas-monde",
    "Qatāda dit : « oui, par notre Seigneur et Sa puissance »",
    "Ṣaḥīḥ al-Bukhārī",
    "chapitre de ceux qui seront rassemblés sur leurs visages",
    "le ḫabat du Feu, son sens : l’apaisement de la flamme",
    "la braise sur son état",
    "elle s’embrase et s’accroît en embrasement et en flamme",
    "Une bande de citation imprimée du milieu est lacerée",
    "embrasse les preuves et les arguments que Muḥammad — paix sur lui — apporta",
    "de rapport, d’ordre et d’interdit",
    "l’affaire du reniement de la Résurrection et la particularisa par la mention",
    "« et poussière » (rufāt)",
    "la corrosion a réduit à l’état de poussière",
    "la résurrection : mouvoir la chose qui est immobile",
    "du côté du déni et de l’exclusion de l’état",
    "aux déniateurs des missions de Ses messagers",
    "des justifications dont ils se prévalent",
    "Il le déchargea du démenti des associateurs",
    "la remise de l’affaire à Allah et Sa mise en arbitre envers Ses ennemis",
    "démentant la mission divine et reniant la Résurrection et le compte",
    "en quoi s’accomplit la justice divine",
    "d’entre les humains, et non des anges",
    "sur la forme venue dans les āyāt",
    "fa-huwa l-muhtadī",
    "[La quatrième consigne est dégradée dans la couche texte — déclarée perdue.]",
    "la clarté du pardon et le secret de la singularité",
    "il est le bien-guidé — Allah le guidant",
    "vers la compagnie des siens",
    "voilé d’Allah — comme il vécut voilé",
    "Il meurt sur ce sur quoi il vécut",
    "il est ressuscité sur ce sur quoi il mourut",
    "aux secrets de l’Essence dans les manifestations de la félicité",
    "en colloque avec le Tout-Miséricordieux, le Miséricordieux",
    "le colloque de la Vérité avec les Proches",
    "son reniement de Lui en Ses attributs",
    "[les membres finaux sont dégradés — déclarés]",
    "ce qui agit sur la guidance de l’homme et son égarement",
    "« le terme » (aǧal)",
    "« les trésors » (ḫazāʾin)",
    "« retenir » (la-ʾamsaktum)",
    "« l’avare » (qatūr)",
    "Par quoi Allah — très-Haut — a-t-Il décrit l’homme dans les deux āyāt",
    "les styles rhétoriques",
    "des fragments de « awa-lam » et de « alā »",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v94, v95, v96, v97, v98 = (bare(ar17[i]) for i in range(94, 99))
for f in ["وما منع لناس أن يؤمنوا إذ جاءهم لهدى", "أبعث لله بشرا رسولا"]:
    if f not in v94:
        errors.append(f"cache 17:94 inattendu ({f[:30]})")
for f in ["لو كان فى لأرض ملئكة يمشون مطمئنين", "لنزلنا عليهم من لسماء ملكا رسولا"]:
    if f not in v95:
        errors.append(f"cache 17:95 inattendu ({f[:30]})")
for f in ["كفى بلله شهيدا بينى وبينكم", "كان بعباده خبيرا بصيرا"]:
    if f not in v96:
        errors.append(f"cache 17:96 inattendu ({f[:30]})")
for f in ["ومن يهد لله فهو لمهتد", "فلن تجد لهم أولياء من دونه", "نحشرهم يوم لقيمة على وجوههم",
          "مأوىهم جهنم", "كلما خبت زدنهم سعيرا"]:
    if f not in v97:
        errors.append(f"cache 17:97 inattendu ({f[:30]})")
for f in ["ذلك جزاؤهم بأنهم كفروا بايتنا", "كنا عظما ورفتا", "لمبعوثون خلقا جديدا"]:
    if f not in v98:
        errors.append(f"cache 17:98 inattendu ({f[:30]})")
if "أولم يروا أن لله لذى خلق لسموت ولأرض" not in bare(ar17[99]) or "أجلا لا ريب فيه" not in bare(ar17[99]):
    errors.append("cache 17:99 inattendu (préparation : aǧalan lā rayba fīh)")
if "تملكون خزائن رحمة ربى" not in bare(ar17[100]) or "وكان لإنسن قتورا" not in bare(ar17[100]):
    errors.append("cache 17:100 inattendu (préparation : ḫazāʾin raḥma, qatūran)")

# préparation de la leçon suivante au DOM
if "99 et 100" not in norm or "99 - 001" not in norm:
    errors.append("préparation : les āyāt 99-100 (imprimé « 99 - 001 ») absentes du DOM")
for f in ["aǧal", "ḫazāʾin", "la-ʾamsaktum", "qatūr"]:
    if f not in norm:
        errors.append(f"préparation : lemme attendu absent : {f}")

# citations hors rasm — interdites au corps après l'évaluation
# (17:90-93 = leçon précédente 731 ; 17:99-100 = leçon suivante 733)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"jaillir de terre", "al-Isrāʾ 17:90 (leçon précédente — non portée)"),
    (r"jardin de palmiers", "al-Isrāʾ 17:91 (leçon précédente — non portée)"),
    (r"le ciel en morceaux", "al-Isrāʾ 17:92 (leçon précédente — non portée)"),
    (r"maison d’ornements", "al-Isrāʾ 17:93 (leçon précédente — non portée)"),
    (r"Ne suis-je qu’un être humain", "al-Isrāʾ 17:93 (leçon précédente — non portée)"),
    (r"faire venir Allah et les anges", "al-Isrāʾ 17:92 (leçon précédente — non portée)"),
    (r"N’ont-ils pas vu", "al-Isrāʾ 17:99 (leçon suivante — non portée)"),
    (r"un terme, sur lequel il n’y a aucun doute", "al-Isrāʾ 17:99 (leçon suivante — non portée)"),
    (r"les injustes s’obstinent", "al-Isrāʾ 17:99 (leçon suivante — non portée)"),
    (r"les trésors de la miséricorde", "al-Isrāʾ 17:100 (leçon suivante — non portée)"),
    (r"vous lésineriez", "al-Isrāʾ 17:100 (leçon suivante — non portée)"),
    (r"l’homme est très avare", "al-Isrāʾ 17:100 (leçon suivante — non portée)"),
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
print("PASS : leçon 732 — versets 94-98 rendus sur le rasm warš du cache (le refus de "
      "croire à la venue du guide, « a-baʿaṯa llāhu bašaran rasūlan », les anges "
      "marchant tranquillement et l'ange-messager, « kafā bi-llāhi šahīdan », le guidé "
      "et l'égarement — la résurrection sur les visages et l'Enfer qui s'apaise —, la "
      "sanction des ossements et de la poussière), le tafsīr de la réfutation (le "
      "défini de « les gens » pour l'immersion, la mission des humains ni innovation "
      "ni chose étrange, le miracle pareil par l'ange ou l'humain, la mise en demeure "
      "corrompue et l'entêtement vain, les mécréants de Quraysh, l'ifhām et les anges "
      "s'établissant résidents, les natures qui fuiraient, le cours habituel des "
      "états, la royauté et la richesse offertes, « qui donc témoignera pour toi », "
      "le qāḍī Abū Muḥammad, la création de la guidance et de l'égarement, « ce qui "
      "dépasse la transmission n'est pas en ma main », le Connaisseur et le "
      "Clairvoyant — al-Bayḍāwī 3/762), le châtiment (les métaphores de la "
      "perplexité et la vérité du lever des tombes, le retour des vues et de "
      "l'ouïe, « il s'en est allé sur son visage », le chameau abattu, la capacité "
      "au transport sur les visages, le hadith d'Anas avec la réponse du Prophète ﷺ "
      "et Qatāda au Ṣaḥīḥ al-Bukhārī, le ḫabat du Feu et l'apaisement de la flamme, "
      "« et poussière » le reste réduit à la poussière, la résurrection mouvoir "
      "l'immobile), les finalités (3), l'évaluation (3 lisibles + 1 déclarée "
      "perdue), l'exploitation (le passage de la guidance — tête et membres finaux "
      "dégradés, déclarés), la préparation 99-100 au DOM (imprimé « 99 - 001 » "
      "inversé, lu 99 et 100 par l'étiquette du livre — aǧal, ḫazāʾin, la-ʾamsaktum, "
      "qatūr au rasm du cache 17:99-100), aucune citation hors rasm (17:90-93 "
      "interdits au corps après l'évaluation — leçon précédente ; 17:99-100 "
      "interdits — leçon suivante), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)
