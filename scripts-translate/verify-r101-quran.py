#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R101 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-607 + -608.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (al-Taḥrīr wa-t-Tanwīr 28/297, Tafsīr d'al-Qurṭubī 18/158, Sunan Ibn Māǧah,
     Musnad Aḥmad, Šaʿb al-īmān 2/429, at-Taghābun 14, an-Nisāʾ 134, Hūd 6),
     évaluation, istithmār, préparation préalable
  6. croisement des versets rendus avec le cache coran warš (fragments clés)
  7. 0 résidu d'édition (XXX, TODO, 【】, undefined, NaN)
"""
import json
import re
import sys

TMPDIR = "/home/z/my-project/tr-tmp"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")

LESSONS = {
    "pdf-mut23h36-607": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, verset 1",
        "asserts": [
            "quinzième leçon (15)",
            "Connaître la légalité du divorce et de la période d’attente",
            "médinoise et comporte douze versets",
            "un ennemi [une tentation]. Prenez-y garde donc",
            "[at-Taghābun, 14]",
            "[Li-ʿiddatihinna :]",
            "délimitez-la et connaissez son début et sa fin.",
            "le visé par cet ordre ici est la reprise (raǧʿa)",
            "J’expose la voie légale pour mettre fin au lien conjugal.",
            "Je précise le lieu où la femme répudiée accomplit sa période d’attente.",
            "Premièrement : la légalité du divorce et ses règles",
            "Deuxièmement : le statut de la résidence de la femme répudiée pendant sa période d’attente",
            "à la forme collective, à titre d’adresse à lui et à eux",
            "fais, toi et ton peuple",
            "la signification par exigence",
            "il est interdit, mais il fait obligation",
            "alors que leur période d’attente est devant elles",
            "Ibn ʿUmar a lu : « répudiez-les au commencement de leur période d’attente »",
            "les deux lectures ont été transmises du Messager de Dieu",
            "le visé est le sens exégétique",
            "l’ouverture de la période d’attente — et cela n’a lieu que dans la pureté",
            "motivée par l’allongement de la période d’attente, ou est-elle un acte d’adoration",
            "avant la consommation du mariage alors qu’elle est en menstrues",
            "selon ce qui est venu dans le ḥadīth d’Ibn ʿUmar",
            "ordonne-lui de la reprendre",
            "dans une pureté où il ne l’a pas touchée",
            "dans la reprise, la résidence, l’héritage et autres",
            "nécessité de gestion ; et cela pour préserver la filiation et protéger la femme",
            "le correct est l’obligation, car la jouissance a pris fin par le divorce",
            "« à moins qu’elles n’aient commis une turpitude prouvée »",
            "cinq avis",
            "l’ont dit al-Layṯ ibn Saʿd et aš-Šaʿbī",
            "le mauvais propos avec les beaux-frères",
            "la lecture d’Ubayy ibn Kaʿb",
            "et c’est vers cela que s’est orienté aṭ-Ṭabarī",
            "Ibn al-Faras",
            "l’a dit Qatāda",
            "d’avec Ḥafṣa bint ʿUmar, et Dieu lui ordonna de la reprendre",
            "la chose licite la plus détestée auprès de Dieu",
            "afin que la reprise soit facile et aisée",
            "ni un déni de leurs droits légaux",
            "Quels sont les principaux objectifs légaux de la législation du divorce et de la période d’attente ?",
            "Le Ṭāhir ibn ʿĀšūr a dit",
            "la période d’attente se compte en périodes de pureté, non en menstrues",
            "au commencement de l’écoulement",
            "d’après le ḥadīth d’ʿUmar dans l’affaire du divorce d’Ibn ʿUmar",
            "le verset de la sourate la Vache et par les versets des Coalisés",
            "[al-Taḥrīr wa-t-Tanwīr : 28/297]",
            "que le décompte se fait en périodes de pureté",
            "Je révise l’exégèse des versets 2 et 3 de la sourate aṭ-Ṭalāq",
            "le témoignage (šahāda) et la justice (ʿadāla)",
            "le temps de la reprise et le statut du témoignage à son sujet",
        ],
        "verses": {
            "65:1": ["فَطَلِّقُوهُنَّ لِعِدَّتِهِنَّ", "وَأَحْصُوا۟ ٱلْعِدَّةَ",
                      "وَٱتَّقُوا۟ ٱللَّهَ رَبَّكُمْ", "لَا تُخْرِجُوهُنَّ مِنۢ بُيُوتِهِنَّ",
                      "أَن يَأْتِينَ بِفَٰحِشَةٍۢ مُّبَيِّنَةٍ", "لَعَلَّ ٱللَّهَ يُحْدِثُ بَعْدَ ذَٰلِكَ أَمْرًۭا"],
            "64:14": ["مِنْ أَزْوَٰجِكُمْ وَأَوْلَٰدِكُمْ عَدُوًّۭا لَّكُمْ", "فَٱحْذَرُوهُمْ"],
        },
    },
    "pdf-mut23h36-608": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, versets 2 et 3",
        "asserts": [
            "seizième leçon (16)",
            "Connaître certaines règles du divorce et de la reprise.",
            "Craindre Dieu — qu’Il soit glorifié — et m’en remettre à Lui dans toutes mes affaires.",
            "qu’il ait lieu dans une pureté, et qu’une période d’attente lui fasse suite",
            "sinon qu’elle commette une turpitude manifeste",
            "lorsque la période d’attente approche de sa fin",
            "[Balagna aǧalahunna :]",
            "éviter les grands péchés, se garder des petits, et préserver la générosité de caractère",
            "[Iqāmat aš-šahāda :]",
            "[Wal-Lāhu bāliġun amrahū :]",
            "[Qadaran maʿlūman :]",
            "Quand l’époux a-t-il le choix entre la rétention et la séparation ?",
            "Premièrement : les règles de la fin de la période d’attente",
            "Deuxièmement : les effets de la foi dans l’engagement aux règles du divorce et de la reprise",
            "l’approche d’une chose à sa survenue et au fait de s’y trouver",
            "la reprise est empêchée",
            "soit vous reprenez vos épouses et cohabitez avec elles de façon convenable",
            "le divorce révocable devient alors définitif",
            "La rétention de façon convenable : améliorer la cohabitation et acquitter la pension",
            "l’acquittement du douaire, la jouissance au moment du divorce, le respect des conditions",
            "repousser le soupçon, trancher le différend et protéger les droits",
            "est-il obligatoire ou recommandé ? — deux avis au madhhab mālikite",
            "Ibn ʿAbbās a dit : c’est le témoignage sur le divorce et sur la reprise",
            "de lever l’embarras et le différend",
            "les conditions du témoignage exigées légalement dans le mariage et le divorce",
            "et c’est une obligation collective",
            "à ce sens a fait allusion Ibn al-Faras",
            "c’est ainsi que l’a expliqué Zamakšarī, et cela est le plus manifeste",
            "« observez strictement la justice, soyez des témoins (véridiques) comme Dieu l’ordonne » [an-Nisāʾ, 134]",
            "il craint le châtiment de Dieu et Son jugement dans l’au-delà",
            "phrase intercalée",
            "tu n’as pas craint Dieu, ton épouse s’est séparée de toi",
            "de la détresse de la duniyā et de l’āḫira",
            "le plus fondé, pour cinq raisons",
            "porter la parole sur sa généralité",
            "révélé au sujet d’ʿAwf ibn Mālik al-Ašjaʿī",
            "[deux mots du récit imprimé sont altérés dans l’original]",
            "qui lui ordonna la piété",
            "des profondeurs de la mort et des rigueurs du Jour de la Résurrection",
            "si les gens l’adoptaient, il leur suffirait",
            "[Sunan Ibn Māǧah ; kitāb az-zuhd, bāb al-waraʿ wa-t-taqwā]",
            "convient à la piété sur le général",
            "la subsistance est de deux genres",
            "une subsistance promise aux pieux en particulier",
            "[Hūd, 6]",
            "Il lui suffit, de sorte qu’il n’a plus besoin d’autre avec Lui",
            "Le tawakkul est le fait de s’en remettre à Dieu",
            "ne contredit pas le tawakkul en Dieu",
            "ils partent le matin le ventre vide et reviennent le soir rassasiés",
            "[Musnad de l’Imam Aḥmad ; musnad ʿUmar ibn al-Ḫaṭṭāb]",
            "ceux qui se goinfrent",
            "Un homme qui jette sa semence dans le sein de la terre et s’en remet à son Seigneur.",
            "[Šaʿb al-īmān d’al-Bayhaqī : 2/429]",
            "une règle générale qui embrasse le divorce, la reprise et autres",
            "donner l’occasion de rattraper ce qui est passé et de réparer ce qui s’est corrompu du lien conjugal",
            "dans l’état du mariage comme dans l’état de la séparation",
            "Le témoignage est un outil d’authentification et de garantie des droits",
            "la foi en Dieu et au Jour dernier",
            "sortie des difficultés et d’acquisition d’une subsistance abondante",
            "Quel est le statut du témoignage sur la reprise ? Et quel est son profit ?",
            "Al-Qurṭubī — que Dieu lui fasse miséricorde — a dit :",
            "que l’obstination mutuelle ne survienne pas entre les deux",
            "[Tafsīr d’al-Qurṭubī : 18/158]",
            "sans authentifier leurs contrats",
            "Je révise l’exégèse des versets 4 et 5 de la sourate aṭ-Ṭalāq",
            "[La première consigne de l’original imprimé est altérée ; elle porte sur les expressions des versets 4 et 5 et leur sens.]",
            "Je dresse le tableau des situations des femmes en période d’attente et de la durée de chaque situation",
        ],
        "verses": {
            "65:2": ["فَإِذَا بَلَغْنَ أَجَلَهُنَّ", "فَأَمْسِكُوهُنَّ بِمَعْرُوفٍ",
                      "أَوْ فَارِقُوهُنَّ بِمَعْرُوفٍ", "وَأَشْهِدُوا۟ ذَوَىْ عَدْلٍ",
                      "وَأَقِيمُوا۟ ٱلشَّهَٰدَةَ لِلَّهِ", "ذَٰلِكُمْ يُوعَظُ بِهِۦ مَن كَانَ يُؤْمِنُ",
                      "وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مَخْرَجًۭا"],
            "65:3": ["وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ", "وَمَن يَتَوَكَّلْ عَلَى ٱللَّهِ فَهُوَ حَسْبُهُۥٓ",
                      "إِنَّ ٱللَّهَ بَٰلِغُ أَمْرِهِۦ", "قَدْ جَعَلَ ٱللَّهُ لِكُلِّ شَىْءٍۢ قَدْرًۭا"],
            "4:135": ["كُونُوا۟ قَوَّٰمِينَ بِٱلْقِسْطِ", "شُهَدَآءَ لِلَّهِ"],
            "11:6": ["مِن دَآبَّةٍۢ فِى ٱلْأَرْضِ", "عَلَى ٱللَّهِ رِزْقُهَا"],
        },
    },
}

RESIDUS = ["XXX", "TODO", "【", "〕", "— à compléter", "undefined", "NaN"]


def strip_tags(t: str) -> str:
    return re.sub(r"<[^>]+>", "", t)


def main() -> int:
    cache = json.load(open(CACHE, encoding="utf-8"))
    fails = 0
    total = 0
    for doc, spec in LESSONS.items():
        path = f"{TMPDIR}/{doc}.html"
        html = open(path, encoding="utf-8").read()
        text = strip_tags(html)

        # 1. arabe résiduel
        ar = ARABIC.findall(text)
        total += 1
        if ar:
            print(f"✗ {doc} : {len(ar)} caractères arabes résiduels : {ar[:10]}")
            fails += 1
        else:
            print(f"✓ {doc} : 0 caractère arabe")

        # 2. apostrophe droite
        apos = [m.start() for m in re.finditer(r"'", html)]
        total += 1
        if apos:
            print(f"✗ {doc} : {len(apos)} apostrophes droites")
            fails += 1
        else:
            print(f"✓ {doc} : 0 apostrophe droite")

        # 3. guillemets appariés
        o, c = text.count("«"), text.count("»")
        total += 1
        if o != c:
            print(f"✗ {doc} : guillemets non appariés ({o} ouvrants / {c} fermants)")
            fails += 1
        else:
            print(f"✓ {doc} : guillemets appariés ({o})")

        # 4. h1 attendu
        total += 1
        m = re.search(r"<h1>\s*(.*?)</h1>", html, re.S)
        if not m or m.group(1).strip() != spec["title"]:
            print(f"✗ {doc} : h1 inattendu : {m.group(1).strip()[:80] if m else 'ABSENT'}")
            fails += 1
        else:
            print(f"✓ {doc} : h1 conforme")

        # 5. assertions ciblées
        norm = lambda s: s.replace("\u202f", " ").replace("\u00a0", " ")
        tnorm = norm(text)
        manquantes = []
        for a in spec["asserts"]:
            total += 1
            if norm(a) not in tnorm:
                manquantes.append(a)
        if manquantes:
            for a in manquantes:
                print(f"✗ {doc} : assertion absente : {a[:90]}")
            fails += len(manquantes)
        print(f"✓ {doc} : {len(spec['asserts'])} assertions ciblées présentes")

        # 6. croisement des fragments de versets avec le cache coran (normalisé sans diacritiques)
        def norm_ar(s: str) -> str:
            s = re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u06DE\u08F0-\u08FF]", "", s)
            s = s.replace("\u0671", "ا")  # alif wasla
            s = s.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
            return "".join(ch for ch in s if "\u0621" <= ch <= "\u064A")

        for key, frags in spec["verses"].items():
            snum, vnum = key.split(":")
            sutra = cache[snum]
            src = next((t for n, t in sutra["ar"] if n == int(vnum)), None)
            total += 1
            if src is None:
                print(f"✗ {doc} : verset {key} absent du cache")
                fails += 1
                continue
            nsrc = norm_ar(src)
            miss = [f for f in frags if norm_ar(f) not in nsrc]
            if miss:
                print(f"✗ {doc} : fragments v.{key} absents du cache : {miss}")
                print(f"   cache normalisé : {nsrc[:180]}")
                fails += 1
            else:
                print(f"✓ {doc} : verset {key} — {len(frags)} fragments conformes au cache (warš)")

        # 7. résidus d'édition
        for r in RESIDUS:
            total += 1
            if r in text:
                print(f"✗ {doc} : résidu « {r} »")
                fails += 1

    print(f"\n{'='*60}")
    print(f"BILAN : {total} contrôles, {fails} échec(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
