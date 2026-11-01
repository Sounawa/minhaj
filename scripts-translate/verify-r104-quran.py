#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R104 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-613 + -614.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Tafsīr al-Ṭabarī 23/77, Ṣaḥīḥ al-Buḫārī/Livre des injustices,
     Mafātīḥ al-Ghayb 30/566 + 2/383, al-Taḥrīr wa-t-Tanwīr 28/340,
     Tafsīr al-Bayḍāwī 5/223, al-Baḥr al-Muḥīṭ 10/207,
     al-Ḥuṣūl fī uṣūl al-fiqh 109), évaluation, istithmār, préparation
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
    "pdf-mut23h36-613": {
        "title": "Exégèse de la sourate aṭ-Ṭalāq, verset 12",
        "asserts": [
            "vingt-et-unième leçon (21)",
            "Connaître quelques-unes des preuves de la puissance de Dieu — Puissant et Majestueux — et de Son omniscience.",
            "Saisir que tout ce qui se produit dans cet univers tout entier se produit par le commandement de Dieu.",
            "Craindre Dieu — le Très-Haut — en secret et en public, dans tous mes états.",
            "Quelles sont donc les manifestations de la puissance de Dieu et de Sa science ?",
            "[Mithlahunna :]",
            "dans le nombre, ou dans la création.",
            "[Yatanazzalu l-amru :]",
            "le commandement est la révélation, ou les jugements de Dieu et Sa détermination pour Ses créatures.",
            "Quels sont les attributs divins que ces versets établissent ?",
            "À la fin de cette sourate, le Vrai — le Transcendant — nous informe de certaines manifestations de Sa grandeur",
            "Dieu seul est Celui qui les a créées, nul autre",
            "[l’énoncé imprimé à ce point est altéré ; rendu par le sens]",
            "Al-Ṭabarī a dit : « non point ce que les associateurs adorent, parmi les divinités et les idoles qui n’ont pas le pouvoir de créer quoi que ce soit. »",
            "[Tafsīr d’aṭ-Ṭabarī : 23/77]",
            "Sa puissance, qui s’attache à tout ce qui est possible, dans l’existence et dans l’anéantissement.",
            "Nul désaccord : les cieux sont sept, en vertu des textes explicites du Coran et de la Sunna",
            "les récits du récit du Voyage nocturne (al-Isrāʾ)",
            "Quant à la terre, on y a divergé : on a dit qu’elles sont sept terres, d’après la manifestation de ce verset",
            "« quiconque commet une injustice contre un empan de terre, on l’en enveloppera des sept terres »",
            "« quiconque prend de la terre quelque chose sans droit, elle l’enfoncera au Jour de la Résurrection jusqu’aux sept terres. »",
            "[Ṣaḥīḥ d’al-Buḫārī ; Livre des injustices ; chapitre du péché de celui qui commet une injustice envers quelque chose de la terre]",
            "On a dit : elle est une seule.",
            "elle signifie la ressemblance dans le nombre",
            "la ressemblance dans la grandeur du corps, la multiplicité des habitations et autres — le premier est le plus fondé.",
            "Fakhr ad-Dīn ar-Rāzī a indiqué que certains y répugnent à la raison",
            "les sept terres sont les strates de la terre, ou les régions différentes de la terre que séparent les mers et les océans",
            "« voilà les interprétations que la raison ne répugne pas ; tout le reste des interprétations transmises des exégètes relève de ce à quoi la raison répugne. »",
            "[Mafātīḥ al-Ghayb : 30/566]",
            "Le Ṭāhir ibn ʿĀšūr a dit : « la majorité des exégètes ont entendu la ressemblance dans le nombre de sept et ont dit : la terre a sept strates",
            "sept strates étendues que séparent les mers — cela est transmis d’Ibn ʿAbbās, selon la transmission d’al-Kalbī, d’Abū Ṣāliḥ, de lui",
            "sept strates, les unes au-dessus des autres — c’est l’avis de la majorité.",
            "l’avis des savants des strates de la terre (la géologie), qui établissent des strates terrestres qui n’atteignent pas sept strates.",
            "[al-Taḥrīr wa-t-Tanwīr : 28/340]",
            "il se peut que le commandement désigne la révélation, ou les jugements de Dieu et Sa détermination pour Ses créatures.",
            "Al-Bayḍāwī a dit : « c’est-à-dire que le commandement de Dieu et Son décret se déroulent entre elles, et Son jugement s’y exécute. »",
            "[Tafsīr d’al-Bayḍāwī : 5/223]",
            "c’est la cause de la création des cieux et de la terre",
            "c’est la cause de la descente du commandement entre elles",
            "« une cause de la création ou de la descente du commandement, ou [un mot] sous-entendu qui les embrasse toutes deux ; car chacune des deux atteste la perfection de Sa puissance et de Sa science. »",
            "L’Imam ar-Rāzī — que Dieu lui fasse miséricorde — a dit : « il n’est pas possible qu’Il soit le Créateur de la terre et de ce qu’elle contient",
            "sans qu’Il soit Celui qui les connaît, embrassant leurs parties et leurs ensembles. »",
            "[Mafātīḥ al-Ghayb : 2/383]",
            "rien ne Lui fait défaut sur la terre ni dans les cieux.",
            "Il connaît, transcendant soit-Il, la trahison des yeux et ce que cachent les poitrines",
            "jusqu’à adorer Dieu comme s’il Le voyait ; s’il ne Le voit pas, Dieu le voit — réalisant ainsi le degré de l’excellence (iḥsān) dans la servitude.",
            "Quels sont les avis des exégètes au sujet du nombre des cieux et de la terre ?",
            "Quelle est la finalité du rappel de la création des cieux et de la terre ?",
            "les principales règles légales relatives au divorce, à la reprise, à la période d’attente et à l’allaitement, établies dans la sourate aṭ-Ṭalāq",
            "Je révise l’exégèse des versets 1 et 2 de la sourate aṭ-Ṭarīm",
            "en établissant l’avis le plus fondé parmi eux.",
            "un sujet suivi sur l’infaillibilité du Prophète — que Dieu prie sur lui et le salue —, en partant de mes acquis de la matière du tawḥīd.",
        ],
        "verses": {
            "65:12": ["ٱللَّهُ ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ وَمِنَ ٱلْأَرْضِ مِثْلَهُنَّ",
                       "يَتَنَزَّلُ ٱلْأَمْرُ بَيْنَهُنَّ",
                       "لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ",
                       "وَأَنَّ ٱللَّهَ قَدْ أَحَاطَ بِكُلِّ شَىْءٍ عِلْمًۢا"],
        },
    },
    "pdf-mut23h36-614": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, versets 1 et 2",
        "asserts": [
            "vingt-deuxième leçon (22)",
            "Connaître ce que le Prophète — que Dieu prie sur lui et le salue — a interdit à lui-même.",
            "Saisir la cause de son interdiction — que Dieu prie sur lui et le salue — de ce qu’il s’était interdit.",
            "M’assurer que la révélation seule est la source de l’interdit.",
            "La sourate aṭ-Ṭarīm est médinoise et compte douze versets ; on l’appelle la sourate du Prophète",
            "le reproche que Dieu lui adressa à ce sujet, avec délicatesse.",
            "Quelle est donc la cause de la descente du début de cette sourate ?",
            "[Tabtaġī :]",
            "elle cherche.",
            "[Murāḍāti azwāǧika :]",
            "l’agrément de tes femmes.",
            "[Faraḍa :]",
            "Il a légiféré et précisé.",
            "[Taḥlīlata aymanikum :]",
            "l’expiation de vos serments et de vos jurements.",
            "[Mawlākum :]",
            "le mawlā est le défenseur, ou le seigneur suprême.",
            "J’expose une partie du fiqh de l’interdit (taḥrīm).",
            "Quel est le jugement qui en résulte pour le serment, en vue de s’en libérer ?",
            "Premièrement : la cause de la descente des deux versets au début de la sourate",
            "rendait visite à son épouse Zaynab bint Ǧaḥš et buvait chez elle du miel.",
            "ʿĀʾiša, Ḥafṣa et Sawda bint Zamʿa convinrent que celle d’entre elles qu’il approcherait dirait : tu as mangé du maghāfīr.",
            "Les maghāfīr sont la gomme du gurfah : sucrée et d’odeur repoussante.",
            "il dit : non, mais j’ai bu du miel ; elles dirent : les abeilles ont pris la palme du ḥurfah ; il dit : je n’en boirai plus jamais.",
            "Il répugnait qu’une odeur repoussante fût trouvée sur lui.",
            "Le verset descendit alors comme un reproche pour lui, pour ce qu’il s’était imposé une contrainte à lui-même en interdisant une partie de ce que Dieu lui avait rendu licite. Al-Buḫārī et d’autres l’ont rapporté.",
            "Deuxièmement : une partie des règles du fiqh de l’interdit (taḥrīm)",
            "apostrophe d’honneur et d’attention, par la qualité de la prophétie, pour attester son infaillibilité quant à ce que commet celui qui n’est pas infaillible",
            "Le sens de l’interdit ici est de s’en abstenir, non de le croire illicite selon la Loi",
            "« Dis : “Qui a interdit la parure de Dieu, qu’Il a produite pour Ses serviteurs, ainsi que les bonnes nourritures ?” »",
            "[al-Aʿrāf, 30 — tel qu’imprimé ; le passage canonique se trouve en 7 :32, risque documenté]",
            "Abū Ḥayyān a dit : « le sens de “t’interdis-tu” : tu te prives ; l’interdit selon la Loi ne procède pas d’une révélation de Dieu ; ce n’est qu’une abstention pour réjouir le cœur de certains de ceux avec qui il se tient en belle compagnie. »",
            "[al-Baḥr al-Muḥīṭ : 10/207]",
            "quant à l’interdit portant sur la nourriture, le bien et le reste des choses, hormis les femmes, il ne lie pas : rien ne pèse sur lui, chez Mālik ; Abū Ḥanīfa lui a rendu obligatoire l’expiation.",
            "Quant à l’interdit portant sur l’épouse, les gens y ont divergé en de nombreux avis",
            "Abū Bakr aṣ-Ṣiddīq, ʿUmar ibn al-Ḫaṭṭāb, Ibn ʿAbbās, ʿĀʾiša et d’autres ont dit : il n’en résulte qu’une répudiation [la suite de l’énoncé imprimé à ce point n’est pas restituable].",
            "Mālik a dit, selon ce qui fait autorité chez lui : trois répudiations pour celle qui a été approchée",
            "pour celle qui ne l’a pas été, la suspension : on juge selon son intention, une répudiation, deux ou trois.",
            "Ibn al-Māǧišūn a dit : elles sont trois, selon les deux sens.",
            "Il est transmis de Mālik qu’elle est une répudiation définitive ; on a dit : une répudiation révocable.",
            "tu cherches l’agrément de tes femmes par l’interdit de ce que Dieu t’a rendu licite.",
            "il y a en cela l’indication que Dieu lui a pardonné ce qu’il s’était imposé comme interdit qu’Il lui reprocha",
            "Son reproche en cela ne fut que générosité à son égard",
            "le reproche ne porta que sur le resserrement qu’il s’imposa — que Dieu prie sur lui et le salue — et son abstention de ce qui comportait pour lui un profit.",
            "La taḥlīla est le nom d’action de ḥalla, et le sens en est l’expiation",
            "Il vous a légiféré la libération de ce sur quoi vous avez juré, par l’expiation",
            "« Dieu ne vous sanctionne pas pour la frivolité dans vos serments, mais Il vous sanctionne pour les serments que vous avez l’intention d’exécuter. L’expiation en sera de nourrir dix pauvres, de ce dont vous nourrissez normalement vos familles, ou de les habiller, ou de libérer un esclave. Quiconque n’en trouve pas les moyens devra jeûner trois jours. Voilà l’expiation pour vos serments, lorsque vous avez juré. Et tenez à vos serments. Ainsi Dieu vous explique Ses versets, afin que vous soyez reconnaissants ! »",
            "[la Table servie, 91 — tel qu’imprimé ; le passage canonique se trouve en 5 :89, risque documenté]",
            "celui qui rend obligatoire l’expiation pour l’interdit de la nourriture a dit : cette expiation est pour l’interdit.",
            "cette expiation est pour le fait qu’il ait juré de ne plus le boire.",
            "elle porte sur son serment — que Dieu prie sur lui et le salue — de ne pas approcher ses femmes pendant un mois.",
            "il se peut que le mawlā ait le sens de défenseur, ou le sens de seigneur suprême.",
            "Il ne leur ordonne ni ne leur interdit que conformément à ce qu’exigent leurs intérêts.",
            "il ne convient pas qu’il interdise à lui-même ce que Dieu a rendu licite, pour satisfaire autrui.",
            "si sa violation est meilleure que son observation, se doit de l’expirer et de faire ce qui est meilleur.",
            "Dieu — Puissant et Majestueux — est Celui qui rend licite aux gens ce qui leur est utile, et interdit ce qui leur nuit",
            "J’expose le récit venu au sujet de la cause de la descente du début de la sourate.",
            "Quel est le jugement de celui qui s’interdit une chose parmi ce que Dieu a rendu licite ?",
            "Ibn al-ʿArabī al-Māʿafirī — que Dieu lui fasse miséricorde — a dit : « La communauté s’accorde sur l’infaillibilité des prophètes — que les prières de Dieu soient sur eux — à l’égard des grands péchés",
            "et l’on a divergé au sujet des petits péchés : certains les autorisent, d’autres les refusent.",
            "Les manifestations apparentes du Livre, parmi les versets, attestent qu’ils commirent des fautes légères",
            "que leur infaillibilité est nécessaire de manière absolue, en tout sens, en toute chose et en tout état. »",
            "[al-Ḥuṣūl fī uṣūl al-fiqh, d’Ibn al-ʿArabī : 109]",
            "J’expose la position des savants à l’égard de l’infaillibilité des prophètes, et le classement d’Ibn al-ʿArabī.",
            "Avec quoi réponds-tu, dans la sourate objet de la leçon, au reproche que Dieu adresse à Son Prophète ?",
            "Je révise l’exégèse des versets 3 et 4 de la sourate aṭ-Ṭarīm",
            "[la liste imprimée de ces expressions est en calligraphie dégradée et son texte n’est pas restituable]",
            "Je cherche le secret que Ḥafṣa — que Dieu l’agrée — a divulgué.",
        ],
        "verses": {
            "66:1": ["يَٰٓأَيُّهَا ٱلنَّبِىُّ لِمَ تُحَرِّمُ مَآ أَحَلَّ ٱللَّهُ لَكَ",
                      "تَبْتَغِى مَرْضَاتَ أَزْوَٰجِكَ", "وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ"],
            "66:2": ["قَدْ فَرَضَ ٱللَّهُ لَكُمْ تَحِلَّةَ أَيْمَٰنِكُمْ", "وَٱللَّهُ مَوْلَىٰكُمْ", "وَهُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ"],
            "7:32": ["قُلْ مَنْ حَرَّمَ زِينَةَ ٱللَّهِ ٱلَّتِىٓ أَخْرَجَ لِعِبَادِهِۦ"],
            "5:89": ["لَا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ", "فَكَفَّٰرَتُهُۥٓ إِطْعَامُ عَشَرَةِ مَسَٰكِينَ", "وَٱحْفَظُوٓا۟ أَيْمَٰنَكُمْ"],
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
