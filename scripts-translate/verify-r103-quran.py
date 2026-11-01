#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R103 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-611 + -612.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Tafsīr Ibn ʿAǧība 7/73, al-Buḫārī/Hind, al-Baḥr al-Muḥīṭ 10/203 + 3/358,
     Tafsīr al-Ṭabarī 23/69, al-Taḥrīr wa-t-Tanwīr 28/337 + 28/338,
     Tafsīr Ibn Kathīr 8/177 adapté), évaluation, istithmār, préparation
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
    "pdf-mut23h36-611": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, verset 7",
        "asserts": [
            "dix-neuvième leçon (19)",
            "Connaître l’appréciation de la pension de la répudiée et de la nourrice dans l’aisance et la contrainte.",
            "Extraire le critère légal de détermination du montant de la pension en général.",
            "M’inspirer du jugement de Dieu — le Très-Haut — en matière de dépense et d’ampleur en cela.",
            "Comment donc la Loi a-t-elle déterminé les montants de la pension ?",
            "[Dhū s-saʿa(t) :]",
            "un homme aisé, à la mesure de sa richesse.",
            "[Wa-man qudira ʿalayhi rizquhū :]",
            "il a été restreint dans ses moyens.",
            "[Mimmā ātāhu Llāhu :]",
            "[Mā ātāhā :]",
            "ce qu’Il lui a donné de subsistance, peu ou beaucoup.",
            "Quel est le critère de détermination du montant de la pension ?",
            "Quelle est la limite de l’engagement légal ?",
            "Il expose ici le montant de cette pension",
            "l’époux n’est pas chargé de ce qu’il ne supporte pas, et l’épouse n’est pas laissée à l’abandon : la situation demeure modérée.",
            "qu’il dépense à la mesure de sa capacité, et qu’on ne lui réclame pas davantage",
            "Ibn ʿAǧība a dit :",
            "de quoi réjouir le cœur de l’éprouvé, et de quoi l’engager à déployer son effort.",
            "la coutume du Très-Haut est de faire suivre la gêne de l’aisance",
            "« A côté de la difficulté est, certes, une facilité ! » [aš-Šarḥ, 5]",
            "un mal ne saurait donc vaincre deux aises.",
            "[Tafsīr d’Ibn ʿAǧība : 7/73]",
            "c’est le madhhab de Mālik, contrairement à Abū Ḥanīfa, car celui-ci a considéré la suffisance.",
            "« et sur celui auquel l’enfant est né : leur subsistance et leur vêtement, de façon convenable »",
            "[la Vache, 234 — tel qu’imprimé ; le passage canonique se trouve en 2 :233, risque documenté]",
            "la citation ornée à l’appui est partiellement restituable ; le renvoi imprimé porte : la Vache, 231",
            "Hind dit au Prophète — que Dieu prie sur lui et le salue : Abū Sufyān est un homme avare",
            "« prends ce qui te suffit, toi et ton enfant, de façon convenable. »",
            "[Livre des jugements ; chapitre du jugement rendu sur l’absent]",
            "Abū Ḥayyān a dit :",
            "un fondement de l’obligation de la pension de l’enfant au père, non à la mère.",
            "Muḥammad ibn al-Muwazz a dit : elle est à la charge des deux parents à la mesure de l’héritage.",
            "[al-Baḥr al-Muḥīṭ, d’Abū Ḥayyān : 10/203]",
            "son énoncé est un énoncé général : il embrasse le reste des situations où la pension envers autrui est due",
            "la pension des parents envers leurs enfants ; celle des enfants envers leurs parents pauvres",
            "le madhhab de Mālik et d’aš-Šāfiʿī est que la pension lui demeure due, contrairement à Abū Ḥanīfa",
            "deux avis existent, dans le madhhab, au sujet du divorce pour cela.",
            "La législation islamique est une législation souple",
            "L’islam est une religion réaliste : il ne charge les gens que de ce qu’ils peuvent",
            "L’époux aisé doit faire preuve d’ampleur envers lui-même, son épouse et ceux à qui sa pension incombe.",
            "L’optimisme quant à l’aisance et à la fin de la gêne est une confiance dans la promesse de Dieu.",
            "J’expose le critère de détermination du montant de la pension due aux répudiées et aux nourrices, avec argumentation.",
            "Je dégage les principales finalités légales tirées du jugement de la Loi sur le montant de la dépense.",
            "dans le Tafsīr d’Ibn Ǧarīr aṭ-Ṭabarī — que Dieu lui fasse miséricorde —, d’Abū Sinān :",
            "ʿUmar ibn al-Ḫaṭṭāb — que Dieu l’agrée — s’informa auprès de Abū ʿUbayda",
            "il porte la plus grossière des étoffes et mange la plus rugueuse des nourritures.",
            "Il lui envoya mille dinars",
            "que Dieu lui fasse miséricorde : il a donné l’interprétation de ce verset",
            "[Tafsīr d’aṭ-Ṭabarī : 23/69]",
            "J’expose le critère de la dépense à partir du texte.",
            "la fonction de l’argent, les voies de son acquisition, et les formes de sa dépense en islam.",
            "Je révise l’exégèse des versets 8 à 11 de la sourate aṭ-Ṭalāq",
            "ʿattat, nukran, wa-bāla amrihā, ḫusran.",
            "J’expose le châtiment de ceux qui ont désobéi à Dieu et à Ses messagers, à travers les versets.",
        ],
        "verses": {
            "65:7": ["لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ", "وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ",
                      "لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا مَآ ءَاتَىٰهَا", "سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا"],
            "94:5": ["فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا"],
        },
    },
    "pdf-mut23h36-612": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, versets 8 à 11",
        "asserts": [
            "vingtième leçon (20)",
            "Connaître le châtiment de la désobéissance au commandement de Dieu et de la mise en cause de Ses messagers.",
            "Saisir la finalité de la descente des Écritures célestes et de l’envoi des messagers à l’humanité.",
            "M’engager dans la foi et l’œuvre bonne pour obtenir l’agrément de Dieu et Son Paradis.",
            "Comment donc Dieu a-t-Il châtié ces communautés passées ?",
            "[ʿAttat :]",
            "elle s’est enflée d’orgueil et a désobéi au commandement de Dieu.",
            "[Nukran :]",
            "le nukr est la chose dont on n’a pas vu de semblable.",
            "[Wa-bāla amrihā :]",
            "[Ḫusran :]",
            "on entend ici le compte de l’au-delà et son châtiment.",
            "[Ūlī l-albāb :]",
            "les albāb sont le pluriel de lubb, et le lubb est l’intellect.",
            "[Dhikrā :]",
            "le dhikr, ici, est le Coran.",
            "[Mubaynināt :]" if False else "[Mubayyināt :]",
            "claires, explicites.",
            "[Rizqan :]",
            "le Paradis, dont la faveur ne s’interrompt pas.",
            "Par quoi Dieu menace-t-Il celui qui désobéit à Son commandement ?",
            "À qui Dieu — le Très-Haut — a-t-Il adressé Son ordre de Le craindre ?",
            "Premièrement : le châtiment de ceux qui ont désobéi au commandement de Dieu et à ce qu’ont apporté leurs messagers",
            "on a dit que le kāf est une préposition entrée sur ayy — c’est la lecture de la majorité, et il existe d’autres lectures",
            "Abū Ḥayyān a dit : « ce qui apparaît manifestement, c’est qu’il est un nom indéclinable simple, sans composition, qui vient pour exprimer la multitude, à la manière de kam. »",
            "[al-Baḥr al-Muḥīṭ : 3/358]",
            "Le sens de la cité, ce sont ses habitants, selon la règle de l’emploi figuré avec ellipse.",
            "elles se sont enflées d’orgueil et ont dépassé la limite dans la désobéissance au commandement de leur Seigneur",
            "avec l’insolence et l’obstination.",
            "les exégètes ont divergé sur le sens du compte ici",
            "il s’agit du compte dans l’au-delà ; de même du châtiment mentionné ensuite.",
            "il s’agit de l’ici-bas — et c’est le plus fondé",
            "c’est une réalité en ce qui est advenu, et un emploi figuré pour ce qui n’est pas advenu.",
            "Nous les avons saisies pour leurs fautes, sans que rien de leurs fautes légères ne soit négligé",
            "et l’inouï est le sévère dont on n’a pas vu de semblable.",
            "elle a éprouvé la conséquence de sa mécréance et la rétribution de sa faute.",
            "et le dénouement de son détournement fut la perte dans l’au-delà.",
            "un châtiment atteignant l’extrême de la sévérité et de la douleur, en plus de ce qu’Il leur hâta comme châtiment dans l’ici-bas.",
            "Deuxièmement : l’ordre de Dieu aux croyants, doués d’intelligence saine, de Le craindre",
            "pour que leur dénouement soit loué",
            "craignez Son châtiment et ne contrariez pas Ses règles, ô vous aux intellects sains",
            "de peur que ne vous atteigne ce qui les atteignit comme châtiment dans l’ici-bas et comme perte dans l’au-delà.",
            "l’exposé de ceux qui sont doués d’intelligence",
            "il y a en cela l’indication que la crainte de Dieu est exigée par la foi",
            "la crainte de Dieu — le Très-Haut — et l’engagement en Sa loi sont exigés par l’intellect sain et la foi saine.",
            "le Ṭāhir ibn ʿĀšūr a dit : « dans cette phrase se trouve le sens de la cause de l’ordre de Le craindre",
            "car la descente du Livre est pour eux un immense profit, digne de leur gratitude envers cela",
            "la confirmation du récit par qad exprime le soin à son sujet",
            "l’élan des âmes à parcourir ce Livre, et à suivre la direction du Messager — que Dieu prie sur lui et le salue.",
            "[al-Taḥrīr wa-t-Tanwīr : 28/337]",
            "Le dhikr, ici, est le Coran ; et le messager est Muḥammad — que Dieu prie sur lui et le salue.",
            "objet direct d’un verbe sous-entendu, dont le sens est : Il a envoyé un messager.",
            "C’est ce qu’a choisi Ibn ʿAṭiyya, et c’est l’avis le plus manifeste.",
            "« messager » a, selon cela, le sens de la mission.",
            "un rappel, celui d’un messager.",
            "[l’analyse imprimée à ce point est altérée ; rendue par le sens]",
            "Et az-Zamaḫšarī a dit : le messager est Ǧibrīl, en remplacement du dhikr",
            "ou il fut appelé dhikr pour la fréquence de son rappel de Dieu — tout cela est loin d’être juste.",
            "il vous récite des versets dans l’état où ils sont des preuves claires, explicites, limpides, sans obscurité ni équivoque",
            "pour les faire sortir des ténèbres de la mécréance et de l’ignorance vers la lumière de la foi et de la science.",
            "« un livre que nous avons fait descendre sur toi, afin que - par la permission de leur Seigneur - tu fasses sortir les gens des ténèbres vers la lumière, sur la voie du Tout Puissant, du Digne de louange. » [Ibrāhīm, 1]",
            "« Dieu est le défenseur de ceux qui ont la foi : Il les fait sortir des ténèbres à la lumière. »",
            "[la Vache, 256 — tel qu’imprimé ; le passage canonique se trouve en 2 :257, risque documenté]",
            "a nommé la révélation qu’Il fit descendre « lumière », pour le guidage qui s’obtient par elle.",
            "[Tafsīr d’Ibn Kathīr (adapté) : 8/177]",
            "Puis Il a exposé la récompense de la foi et de l’œuvre bonne",
            "C’est la promesse de Dieu — Puissant et Majestueux — à quiconque croit en Lui et fait une œuvre bonne",
            "La désobéissance au commandement de Dieu par les désobéissances et les actes répréhensibles est la cause du malheur dans l’ici-bas et de la perte dans l’au-delà.",
            "L’engagement dans le commandement de Dieu et le recours à Sa loi est la voie du bonheur dans l’ici-bas et du salut dans l’au-delà.",
            "a établi la preuve sur Ses serviteurs par la mission des messagers et la descente des Livres portant des versets",
            "La foi en Dieu et le constant respect de Sa crainte sont exigés par l’intellect sain et la raison droite.",
            "Quel est le châtiment d’ici-bas et de l’au-delà par lequel Dieu a châtié les communautés passées",
            "Pourquoi Dieu a-t-Il rapporté à cette communauté ce qui advint aux communautés passées ?",
            "Pourquoi Dieu a-t-Il ordonné à ceux qui sont doués d’intelligence de Le craindre ?",
            "Je dégage, à partir des versets, le châtiment de ceux qui s’engagent dans la loi de Dieu et celui des obstinés qui La mettent en cause.",
            "Le Ṭāhir ibn ʿĀšūr — que Dieu lui fasse miséricorde — a dit, au sujet de Sa parole — le Très-Haut :",
            "« [C’est] une coordination au commandement de la piété, et une indication par l’exaltation : cette promesse frappe leur obéissance par l’octroi d’une demeure éternelle, dans la forme du conditionnel",
            "que ce bienfait, son obtention appartient à ceux qui le désirent, à ce qu’ils croient et fassent les bonnes œuvres.",
            "elle est indéterminée dans le contexte du conditionnel, exprimant la généralité, comme elle l’exprime dans le contexte de la négation.",
            "c’est-à-dire que le commandement en est catégorique, par l’indice des preuves multipliées de la Loi.",
            "[al-Taḥrīr wa-t-Tanwīr : 28/338]",
            "en mettant en œuvre les règles d’origine (uṣūl) suivantes :",
            "les règles des formules de généralité ;",
            "les règles de la spécification.",
            "Je révise l’exégèse du verset 12 de la sourate aṭ-Ṭalāq",
            "je résume la notion des deux attributs — la puissance de Dieu — le Très-Haut — et Sa science —, et ce à quoi chacun des deux se rattache.",
            "Je cherche quelques-unes des preuves de la puissance de Dieu — le Très-Haut — et de Son omniscience dans le verset.",
        ],
        "verses": {
            "65:8": ["وَكَأَيِّن مِّن قَرْيَةٍ عَتَتْ عَنْ أَمْرِ رَبِّهَا وَرُسُلِهِۦ",
                      "فَحَاسَبْنَٰهَا حِسَابًۭا شَدِيدًۭا وَعَذَّبْنَٰهَا عَذَابًۭا نُّكْرًۭا"],
            "65:9": ["فَذَاقَتْ وَبَالَ أَمْرِهَا وَكَانَ عَٰقِبَةُ أَمْرِهَا خُسْرًا"],
            "65:10": ["أَعَدَّ ٱللَّهُ لَهُمْ عَذَابًۭا شَدِيدًۭا", "فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ ٱلَّذِينَ ءَامَنُوا۟",
                       "قَدْ أَنزَلَ ٱللَّهُ إِلَيْكُمْ ذِكْرًۭا"],
            "65:11": ["رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ",
                       "لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ",
                       "وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ", "قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا"],
            "14:1": ["كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ", "لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ"],
            "2:257": ["ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ"],
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
