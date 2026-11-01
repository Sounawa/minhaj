#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R102 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-609 + -610.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Tafsīr al-Qurṭubī 18/165, Tafsīr Ibn Kathīr 8/152, Sunan at-Tirmiḏī,
     Musnad Aḥmad, al-Mustadrak, Muwaṭṭaʾ, Musnad aṭ-Ṭayālisī,
     al-Taḥrīr wa-t-Tanwīr 28/327, Aḥkām al-Qurʾān 4/287),
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
    "pdf-mut23h36-609": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, versets 4 et 5",
        "asserts": [
            "dix-septième leçon (17)",
            "Connaître les délais fixés légalement pour la période d’attente des femmes.",
            "Saisir la finalité de la différence des délais de la période d’attente des femmes.",
            "Craindre Dieu — le Très-Haut — dans l’observation des règles de la période d’attente des femmes.",
            "Al-Ḥākim a rapporté d’Ubayy ibn Kaʿb — que Dieu l’agrée",
            "les petites et celles d’âge avancé chez qui les menstrues ont cessé, ainsi que les femmes enceintes",
            "[al-Mustadrak ʿalā aṣ-Ṣaḥīḥayn ; kitāb at-tafsīr, bāb sūrat aṭ-Ṭalāq]",
            "Quelle est donc la période d’attente des femmes enceintes et de celles qui ne menstruent pas ?",
            "[Yāʾisna min al-maḥīḍ :]",
            "la femme dont les menstrues ont cessé par avancement d’âge.",
            "[Ir-tabtum :]",
            "[Wa-allāʾī lam yaḥiḍn :]",
            "les petites qui n’ont pas encore atteint l’âge des menstrues.",
            "[Amra Llāhi :]",
            "[Wa-yuʿaẓẓim :]",
            "Je détermine la période d’attente de la répudiée qui ne menstrue pas.",
            "J’explique la période d’attente de la femme enceinte dans le divorce ou le décès.",
            "J’expose les profits de la crainte de Dieu et de l’engagement dans Ses règles.",
            "Premièrement : la période d’attente de celles qui ne menstruent pas, parmi les femmes répudiées",
            "Deuxièmement : la période d’attente des femmes enceintes, dans le divorce ou le décès",
            "Troisièmement : les profits de la crainte de Dieu et de l’engagement dans Ses règles",
            "la sourate la Vache avait montré que la période d’attente de la répudiée qui menstrue est de trois périodes de pureté",
            "les répudiées observent d’elles-mêmes un délai » [la Vache, 226]",
            "par jeunesse ou par vieillesse ? Alors ce verset fut révélé",
            "la mention est coordonnée à la précédente, ou constitue un thème dont le prédicat est omis",
            "Al-Qurṭubī a dit :",
            "les règles, Dieu les a établies selon les habitudes",
            "le substitut perd son statut",
            "retourne au décompte des mois. Et cela fait consensus.",
            "[Tafsīr d’al-Qurṭubī : 18/165]",
            "deux sens y sont donnés",
            "si vous doutez du statut de leur période d’attente, sachez qu’elle est de trois mois.",
            "se sont-elles arrêtées ou non ?",
            "celle chez qui la menstruation s’est interrompue alors qu’elle est en âge de menstruer",
            "divergé au sujet de sa période d’attente en trois avis",
            "elle est de trois mois seulement, selon ce que le verset exige sur ce sens.",
            "elle est de trois mois après neuf mois d’attente, pour écarter par là tout terme de grossesse",
            "c’est le madhhab mālikite, et ʿUmar ibn al-Ḫaṭṭāb fut son précurseur en cela.",
            "elle compte en périodes de pureté, même si elle reste trente ans",
            "c’est le madhhab d’aš-Šāfiʿī et d’Abū Ḥanīfa.",
            "chez Mālik, aš-Šāfiʿī, Abū Ḥanīfa et la plupart des savants, général aux répudiées et à celles dont l’époux est décédé",
            "sa période d’attente est la mise au monde.",
            "ʿAlī ibn Abī Ṭālib et Ibn ʿAbbās ont dit : ce verset ne concerne que les répudiées enceintes",
            "le plus lointain des deux termes : la mise au monde, ou l’écoulement de quatre mois et dix jours.",
            "La preuve de la majorité est le ḥadīth de Subayʿa al-Aslamiyya",
            "il décéda d’elle durant l’année du Pèlerinage de l’Adieu, alors qu’elle était enceinte",
            "Abū Sanābil ibn Baʿkak la demanda en mariage",
            "épouse qui tu veux.",
            "Ibn ʿAbbās revint sur son avis lorsque ce ḥadīth lui parvint ; et si ʿAlī l’avait appris, il y serait revenu également.",
            "les Femmes la petite, c’est-à-dire la sourate aṭ-Ṭalāq, fut révélé après le verset de la Vache",
            "[la Vache, 232]",
            "il est donc sa spécification, selon ce qu’ont dit la plupart des savants.",
            "le Coran rappelle deux profits de la crainte de Dieu — le Très-Haut — dans l’engagement envers ces règles",
            "« son affaire lui est rendue facile, Il la lui facilite, et Il lui accorde une délivrance proche et une issue rapide » [Tafsīr d’Ibn Kathīr : 8/152]",
            "le commandement de Dieu, de ce qu’Il a fait descendre des règles de la période d’attente et d’autres, Il l’a fait descendre sur vous et vous l’a exposé.",
            "« crains Dieu où que tu sois ; fais suivre la mauvaise action d’une bonne action qui l’effacera ; et traite les gens avec une belle moralité » [Sunan at-Tirmiḏī ; kitāb al-birr wa-ṣ-ṣila, bāb mā ǧāʾa fī muʿāšarati n-nās]",
            "« les cinq prières, le Vendredi jusqu’au Vendredi, le Ramadan jusqu’au Ramadan, sont des expiations de ce qui les sépare, tant que les grands péchés sont évités » [Musnad de l’Imam Aḥmad ; musnad d’Abū Hurayra]",
            "attestent la souplesse de la loi islamique, sa perfection et son réalisme, ainsi que sa prise en compte des situations des gens.",
            "pour préserver les filiations et sauvegarder les liens les plus forts entre les gens.",
            "en raison des immenses profits qu’elle apporte ici-bas et dans l’au-delà.",
            "le secret de sa différence avec celle qui menstrue.",
            "dans l’état du divorce et dans l’état du décès.",
            "J’analyse grammaticalement Sa parole",
            "[la Vache, 226]",
            "[aṭ-Ṭalāq, 3]",
            "J’applique mes acquis des règles des principes pour montrer la relation entre les versets.",
            "Je révise l’exégèse du verset 6 de la sourate aṭ-Ṭalāq",
            "Je cherche le sens des deux expressions",
            "le statut de la résidence de la répudiée, enceinte ou non enceinte, et leur pension.",
        ],
        "verses": {
            "65:4": ["يَئِسْنَ مِنَ ٱلْمَحِيضِ", "فَعِدَّتُهُنَّ ثَلَٰثَةُ أَشْهُرٍ",
                      "وَٱلَّٰٓـِٔى لَمْ يَحِضْنَ", "وَأُو۟لَٰتُ ٱلْأَحْمَالِ أَجَلُهُنَّ أَن يَضَعْنَ حَمْلَهُنَّ",
                      "يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًۭا"],
            "65:5": ["ذَٰلِكَ أَمْرُ ٱللَّهِ أَنزَلَهُۥٓ إِلَيْكُمْ", "يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ",
                      "وَيُعْظِمْ لَهُۥٓ أَجْرًا"],
            "2:228": ["ٱلْمُطَلَّقَٰتُ يَتَرَبَّصْنَ بِأَنفُسِهِنَّ"],
            "2:234": ["وَٱلَّذِينَ يُتَوَفَّوْنَ مِنكُمْ وَيَذَرُونَ أَزْوَٰجًا", "أَرْبَعَةَ أَشْهُرٍۢ وَعَشْرًا"],
            "11:114": ["إِنَّ ٱلْحَسَنَٰتِ يُذْهِبْنَ ٱلسَّيِّـَٔاتِ"],
        },
    },
    "pdf-mut23h36-610": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, verset 6",
        "asserts": [
            "dix-huitième leçon (18)",
            "Connaître le statut de la résidence de la répudiée pendant sa période d’attente et celui de sa pension.",
            "Saisir certaines règles de l’allaitement dans l’état du divorce.",
            "Me conformer aux règles de la résidence, de la pension et de l’allaitement selon la Loi de Dieu — Puissant et Majestueux.",
            "parmi les manifestations de la crainte de Dieu envers les femmes en période d’attente, il y a le fait de les loger et de ne pas leur faire de tort",
            "Quel est donc le statut de la pension de la femme en période d’attente et de sa résidence ?",
            "[Min ḥayṯu sakantum :]",
            "[Min wuǧdikum :]",
            "le wuǧd est la capacité et l’aisance dans le bien.",
            "[Wa-lā tuḍārrūhunna :]",
            "[Li-tuḍayyiqū ʿalayhinna :]",
            "[Wa-ʾtamirū baynakum :]",
            "[Bi-maʿrūfin :]",
            "Quelles sont les règles propres à la répudiée non enceinte dans les versets ?",
            "Quel est le droit de l’enceinte répudiée ou devenue veuve ?",
            "Qu’incombe à la répudiée qui allaite après le divorce ?",
            "Premièrement : le statut de la résidence de la répudiée non enceinte et de sa pension",
            "Deuxièmement : le statut de la pension de la répudiée enceinte",
            "Troisièmement : le statut de l’allaitement et de son salaire après le divorce",
            "c’est un ordre de Dieu — le Très-Haut — de loger la répudiée toute la durée de sa période d’attente",
            "La répudiée par divorce révocable — c’est-à-dire celle qui n’est pas majeure",
            "d’accord ; car elle a le statut d’épouse.",
            "trois avis la concernent",
            "la résidence lui est due sans la pension ; c’est le madhhab mālikite et celui d’aš-Šāfiʿī.",
            "Mālik a rapporté dans le Muwaṭṭaʾ de Fāṭima bint Qays",
            "Abū ʿAmr ibn Ḥafṣ la répudia définitivement alors qu’il était absent, en Syrie",
            "il dit : par Dieu, tu n’as rien à nous demander",
            "il lui dit : tu n’as pas de pension sur lui.",
            "[Livre du divorce ; chapitre de la pension de la répudiée]",
            "On tire de ceci qu’elle a la résidence sans la pension.",
            "c’est le madhhab d’Abū Ḥanīfa.",
            "la parole d’ʿUmar ibn al-Ḫaṭṭāb",
            "« Nous n’abandonnons pas le Livre de Dieu ni la Sunna du Prophète — que Dieu prie sur lui et le salue — pour la parole d’une femme : nous ne savons si elle l’a altéré ou si elle a oublié. » [la fin de la citation imprimée est altérée]",
            "Le troisième : elle n’a ni résidence ni pension.",
            "« mon époux m’a répudiée trois fois et n’a fixé pour moi ni résidence ni pension",
            "il dit : tu as dit vrai.",
            "[Musnad d’Abū Dāwūd aṭ-Ṭayālisī ; ḥadīth des femmes ; ce que Fāṭima bint Qays a transmis du Prophète — que Dieu prie sur lui et le salue]",
            "le mot « où » indique ici la répartition",
            "s’il n’avait pour tout logement qu’une seule maison, il la logerait dans une partie de ses côtés.",
            "complément apposé à « où vous demeurez »",
            "la lecture avec la damma est la plus fréquente et la plus connue.",
            "Le Ṭāhir ibn ʿĀšūr a dit :",
            "par un logement étroit, une parcimonie dans la pension, ou une reprise suivie d’un divorce pour allonger leur période d’attente, avec l’intention de la raillerie et du tourment",
            "“et ne prenez pas les signes de Dieu en objet de raillerie”, dans la sourate la Vache",
            "ou pour les contraindre à se racheter de la reprise par le ḫulʿ.",
            "[al-Taḥrīr wa-t-Tanwīr : 28/327]",
            "Ils s’accordent sur l’obligation de la pension, durant la période d’attente, pour la répudiée enceinte, que le divorce soit révocable ou définitif, en application de ce verset.",
            "elle n’a pas de pension, chez Mālik et la majorité",
            "D’autres ont dit : elle a la pension sur la succession.",
            "il doit verser son salaire à l’épouse répudiée si elle allaite, ou à une autre selon les situations",
            "lequel est la pension et le reste des dépenses, selon ce qui est mentionné dans les livres de fiqh.",
            "l’adresse est aux hommes et aux femmes",
            "le sens de « délibérez » est « consultez-vous »",
            "[la citation imprimée à l’appui est en calligraphie ornée et son texte n’est pas restituable ; le renvoi imprimé porte : al-Qaṣaṣ, 19]",
            "si la mère se montre excessive envers le père au sujet du salaire de l’allaitement, et en demande beaucoup",
            "sauf si l’enfant n’accepte d’autre sein que celui de sa mère",
            "moyennant un salaire équivalent, semblable à celui de l’époux.",
            "a honoré la femme et rendu obligatoire sur l’époux sa résidence, toute la durée de la période d’attente.",
            "en considération de son état et de celui de son fœtus.",
            "L’islam appelle à la préservation des relations humaines et interdit tout ce qui porte atteinte à ces liens",
            "la garde, l’allaitement, et autres.",
            "[Tableau à compléter : les colonnes portent (la résidence), (la pension) et (l’argument)",
            "Sur qui repose l’allaitement dans les états du mariage et du divorce ?",
            "L’Imam Abū Bakr Ibn al-ʿArabī — que Dieu lui fasse miséricorde — a dit :",
            "n’a pas mentionné la résidence pour toute répudiée",
            "pourquoi donc a-t-Il mentionné la pension en association avec la grossesse ?",
            "la répudiée par divorce définitif n’a pas de pension",
            "[Aḥkām al-Qurʾān, d’Ibn al-ʿArabī : 4/287]",
            "J’expose le verset absolu et le verset restreint désignés dans le texte.",
            "le fondement de la non-éligibilité de la répudiée par divorce définitif à la pension, et l’éligibilité de l’enceinte.",
            "Je révise l’exégèse du verset 7 de la sourate aṭ-Ṭalāq",
            "Je résume le critère de détermination du montant de la pension en fiqh islamique.",
            "qui n’impose pas aux gens ce qu’ils ne peuvent porter, avec argumentation par les textes légaux convenables.",
        ],
        "verses": {
            "65:6": ["أَسْكِنُوهُنَّ مِنْ حَيْثُ سَكَنتُم مِّن وُجْدِكُمْ", "وَلَا تُضَآرُّوهُنَّ لِتُضَيِّقُوا۟ عَلَيْهِنَّ",
                      "وَإِن كُنَّ أُو۟لَٰتِ حَمْلٍۢ فَأَنفِقُوا۟ عَلَيْهِنَّ حَتَّىٰ يَضَعْنَ حَمْلَهُنَّ",
                      "فَإِنْ أَرْضَعْنَ لَكُمْ فَـَٔاتُوهُنَّ أُجُورَهُنَّ", "وَأْتَمِرُوا۟ بَيْنَكُم بِمَعْرُوفٍۢ",
                      "وَإِن تَعَاسَرْتُمْ فَسَتُرْضِعُ لَهُۥٓ أُخْرَىٰ"],
            "2:231": ["وَلَا تَتَّخِذُوٓا۟ ءَايَٰتِ ٱللَّهِ هُزُوًۭا"],
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
