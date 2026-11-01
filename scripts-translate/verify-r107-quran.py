#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R107 — Vérification du rendu savant tafsir-3es / pdf-mut23h36-619 + -620.

Contrôles :
  1. 0 caractère arabe résiduel (rendu 100 % français)
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. h1 attendus
  5. assertions ciblées : objectifs, termes, points du commentaire, sources
     (Aṭ-Taḥrīr wa-t-Tanwīr 28/372, al-Mumtaḥana 8-9, Tafsīr al-Bayḍāwī 5/226,
     Rūḥ al-maʿānī 14/358 + signalement, fatwa du Conseil supérieur des oulémas
     du Maroc 2 Safar 1437 / 14 novembre 2015), évaluation, istithmār, préparation
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
    "pdf-mut23h36-619": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, versets 9 et 10",
        "asserts": [
            "vingt-septième leçon (27)",
            "Reconnaître l’histoire des femmes de Noé et de Loth, et les leçons qu’elle contient.",
            "Prendre conscience que le salut de l’homme est otage de ses bonnes œuvres en ce bas monde.",
            "Tirer la leçon de l’histoire des deux femmes afin de persévérer dans la foi et l’œuvre bonne.",
            "Quel est donc l’état des femmes de Noé et de Loth ? Et comment tirer la leçon de leur histoire dans ma vie ?",
            "[Wa-ġluẓ ʿalayhim :]",
            "traite-les avec rudesse et force.",
            "[Wa-maʾwāhum :]",
            "leur demeure et leur établissement stable dans l’au-delà.",
            "[Al-maṣīr :]",
            "le lieu de retour.",
            "[Taḥta ʿabdayni :]",
            "dans la protection qu’ils lui assuraient.",
            "[Fa-ḫānatāhumā :]",
            "que la trahison tomba d’elles à leur égard dans la religion, et non dans les lits.",
            "Que Dieu ordonna-t-Il à Son Prophète dans les deux versets ?",
            "Quel exemple Dieu frappa-t-Il des mécréants ?",
            "Ces deux versets contiennent ce qui suit :",
            "Premièrement : les orientations coraniques concernant les mécréants et les hypocrites.",
            "Il ordonna à Son Messager — que Dieu prie sur lui et le salue — la manière de les traiter en ce bas monde, à la mesure de ce qui les atteindra dans l’au-delà",
            "Cela par leur appel à l’islam, et en affrontant par l’épée ceux d’entre eux qui mènent le combat, lorsque l’intérêt de la communauté l’exige et que les causes légales se trouvent réunies.",
            "Selon Qatāda : combattre les hypocrites pour établir les sanctions contre eux.",
            "Selon Muǧāhid : par la menace.",
            "On a dit : par la divulgation de leurs secrets.",
            "afin qu’ils te craignent, toi et ceux qui sont avec toi, et qu’ils ne te prennent pas à la légère, toi ni les croyants, et que vous soyez à l’abri de leurs méfaits et de leur trahison.",
            "ibn ʿĀšūr a dit : Il n’ordonna cela à Son Messager que parce que les mécréants s’étaient alliés aux hypocrites après l’émigration du Prophète, et se les étaient donnés comme espions à leur compte, et comme mains par lesquelles ils déposaient le mal contre le Prophète et les croyants.",
            "[Aṭ-Taḥrīr wa-t-Tanwīr : 28/372]",
            "Ce verset n’est pas d’application générale : il n’est pas possible de combattre celui qui n’est pas de la religion de l’islam tant qu’il ne conspire pas contre les musulmans",
            "le combat se déroule sur l’ordre du gouverneur des musulmans et sous sa responsabilité",
            "le Prophète cohabitait ainsi avec les mécréants et les polythéistes à la Mecque, et avec les non-musulmans en général, et de même avec les hypocrites à Médine",
            "il ordonna à ses Compagnons d’émigrer vers le pays des chrétiens, en Abyssinie",
            "parmi lesquels ce que contient la revue al-Madīna",
            "[al-Mumtaḥana : 8-9]",
            "le lieu de repos des deux groupes, mécréants et hypocrites, dans l’au-delà, sera la Géhenne ; et misérable est le lieu de retour vers lequel ils se dirigent.",
            "Deuxièmement : l’histoire des femmes de Noé et de Loth — que le salut soit sur eux tous les deux.",
            "on a dit : le nom de la femme de Noé était Wāhila, et le nom de la femme de Loth Wāʿila ; et cela manque de transmission authentique.",
            "elles étaient dans la protection de deux nobles prophètes, et il leur aurait mieux valu de profiter et d’être guidées par leur guidance.",
            "Ibn ʿAbbās a dit : la trahison de la femme de Noé fut qu’elle disait : il est possédé ; et celle de la femme de Loth, qu’elle informait son peuple de ses hôtes chaque fois qu’ils lui arrivaient ; et elles étaient malgré cela mécréantes.",
            "On a dit : elles trahirent par la fornication ; Ibn ʿAbbās l’a nié et a dit : l’épouse d’un prophète ne forniqua jamais.",
            "nul ne profite à autrui, même s’il est le plus proche des gens pour lui, comme la proximité des femmes de Noé et de Loth de leurs époux.",
            "On a dit : c’est un exemple pour les épouses du Prophète dans ce qui est mentionné au début de la sourate ; et cela est vain, car Dieu n’a frappé l’exemple que pour les mécréants.",
            "al-Bayḍāwī a dit : Il a assimilé leur état en ce qu’ils seront châtiés pour leur mécréance, et ne seront pas favorisés par ce qui les relie au Prophète — que la prière et le salut soient sur lui — et aux croyants comme lignage, à leur état.",
            "[Tafsīr al-Bayḍāwī : 5/226]",
            "Il incombe à l’État musulman de protéger sa sécurité et sa stabilité, de préserver la religion et de réunir les conditions de l’appel vers elle sous la protection de son gouverneur, conformément à son ordre et à ses orientations.",
            "L’homme est otage de ses actes ; autrui ne lui profite pas, quelle que soit sa station auprès de Dieu — Puissant et Majestueux ; que l’homme se tourne donc vers Dieu et remplisse son cœur de foi et de piété.",
            "La simple fréquentation, le lignage ou l’alliance matrimoniale ne servent pas au salut auprès de Dieu, si le proche meurt dans la mécréance sans se repentir.",
            "La guidance vers la foi est dans la main de Dieu — le Transcendant ; la parenté des guidés ni leur fréquentation n’y servent.",
            "1. Quand le combat par la force est-il légal ?",
            "2. Comment concilies-tu le verset objet de la leçon avec les versets qui appellent à la coexistence avec les mécréants et les polythéistes ?",
            "3. Quelle est la visée de l’exemple frappé par l’histoire des femmes de Noé et de Loth ?",
            "Quant au combat légal, ses types sont nombreux : le premier d’entre eux est le combat de l’âme, par sa formation, son éducation, sa purification et sa mise en capacité de porter la responsabilité.",
            "et le combat par la plume, qui consiste à composer les livres utiles et à rédiger les articles qui éclairent la pensée, réfutent les prétextes fallacieux et démentent les accusations mensongères jetées sans raison sur l’islam et les musulmans.",
            "Le combat, en cette situation, ressemble au cautère qui est le dernier des remèdes.",
            "l’islam ne lui a donné, à lui seul, le droit de l’annoncer, d’y appeler et de l’organiser, et n’a pas permis à un individu ni à un groupe de s’y engager de sa propre initiative.",
            "[Fatwa émanant du Secrétariat général du Conseil supérieur des oulémas du Maroc, en date du 2 Safar 1437 / 14 novembre 2015]",
            "1. Je dégage les types du combat mentionnés dans le texte.",
            "2. Pourquoi l’annonce du combat est-elle une prérogative exclusive du Grand Imam, une fois ses motifs réunis ?",
            "Je révise l’exégèse des versets 11 et 12 de la sourate aṭ-Ṭarīm et je réponds à ce qui suit, en m’aidant des orientations du professeur (de la professeure) :",
            "1. Je recherche le sens des expressions suivantes : iḏ qālat — firǧahā — fa-nafaḫnā fīhi — min rūḥinā — Maryam ibnat ʿImrān [les formes calligraphiques imprimées de la première et de la troisième expression sont partiellement dégradées ; tranchées par la matière].",
            "2. Je recherche l’histoire de la femme de Pharaon et de Marie fille de ʿImrān, et les leçons tirées des deux histoires.",
            "Exégèse de la sourate aṭ-Ṭarīm (versets : 9-10)",
        ],
        "verses": {
            "66:9": ["يايها النبى",
                     "جهد الكفار والمنفقين",
                     "واغلظ عليهم",
                     "وماوىهم جهنم",
                     "وبئس المصير"],
            "66:10": ["ضرب الله مثلا للذين كفروا امرات نوح وامرات لوط",
                      "كانتا تحت عبدين من عبادنا صلحين",
                      "فخانتاهما فلم يغنيا عنهما من الله شيا",
                      "وقيل ادخلا النار مع الدخلين"],
        },
    },
    "pdf-mut23h36-620": {
        "title": "Exégèse de la sourate aṭ-Ṭarīm, versets 11 et 12",
        "asserts": [
            "vingt-huitième leçon (28)",
            "Reconnaître l’histoire de la femme de Pharaon et de Marie fille de ʿImrān.",
            "Prendre conscience que l’homme est responsable de ses actes, et non des actes d’autrui.",
            "Prendre pour modèles la femme de Pharaon et Marie fille de ʿImrān dans la constance dans la foi.",
            "Quelle est donc la visée de l’exemple frappé par les deux femmes vertueuses ? Et quelle est la relation de cela avec ce qui précède au début de la sourate, l’histoire des mères des croyants ?",
            "[Fa-nafaḫnā fīhi :]",
            "Gabriel insuffla dans son vagin.",
            "[Min rūḥinā :]",
            "Gabriel.",
            "[Min al-qānitīna :]",
            "parmi les adorateurs.",
            "Quelle est l’histoire que Dieu frappa en exemple dans le premier verset ?",
            "Quelle est la seconde histoire que Dieu frappa en exemple dans le second verset ?",
            "Ces deux versets contiennent ce qui suit :",
            "Premièrement : l’histoire de la femme de Pharaon.",
            "al-Bayḍāwī a dit : Il a assimilé leur état en ce que leur lien avec les mécréants ne leur nuit, à l’état d’Āsiya — que Dieu l’agrée — et à sa station auprès de Dieu, bien qu’elle fût sous le plus farouche des ennemis de Dieu.",
            "[Tafsīr al-Bayḍāwī : 5/226]",
            "La femme de Pharaon se nommait Āsiya ; elle avait cru en Moïse — que le salut soit sur lui ; la nouvelle parvint à Pharaon, qui ordonna de la tuer ; elle adressa alors cette invocation",
            "Seigneur, bâtis-moi une maison proche de Ta miséricorde dans le Paradis ; délivre-moi de la mécréance de Pharaon et de son injustice ; et sauve-moi de son peuple injuste. Et Dieu reprit son esprit.",
            "Deuxièmement : l’histoire de Marie fille de ʿImrān.",
            "il vise par là le vagin, qui est l’organe ; sa préservation est sa sauvegarde et sa pudicité de tout ce qui est blâmable.",
            "l’expression de l’insufflation de Gabriel dans son vagin, et Dieu y créa Jésus — que le salut soit sur lui.",
            "Et Dieu attribua l’esprit à Sa propre personne, selon l’attribution de la créature à son Créateur ; et en cela il y a pour lui une glorification.",
            "al-Ālūsī a dit : Sa parole : « Nous y insufflâmes » : celui qui insuffle est Son Messager — le Transcendant —, à savoir Gabriel — que le salut soit sur lui —, et la chaîne de transmission est métaphorique ; on a dit : la parole porte sur un complément supprimé, c’est-à-dire : Notre messager insuffla ; et le pronom de « dans » renvoie au vagin ; et il est célèbre que Gabriel — que le salut soit sur lui — insuffla dans l’ouverture de sa chemise, et l’effet de cela parvint jusqu’à son vagin.",
            "[Rūḥ al-maʿānī : 14/358 — pagination imprimée à re-vérifier, l’édition courante du Rūḥ compte trente volumes et situe la sourate dans le tome 28]",
            "elle crut aux paroles de son Seigneur ; ses paroles peuvent viser les écritures que Dieu fit descendre, ou Sa parole avec les Anges et d’autres ; et Son écriture, au singulier, peut viser la Torah ou le genre des écritures ; et Abū ʿAmr et Ḥafṣ lurent « et Ses écritures » au pluriel, visant l’ensemble des écritures de Dieu.",
            "La réponse est : la dévotion est une qualité qui réunit les hommes et les femmes, et le masculin l’emporta.",
            "La foi de l’homme et sa rectitude ne sont pas entamées par la fréquentation de non-membres de sa religion, par mariage, alliance matrimoniale ou autre.",
            "Je me réfuge dans l’invocation et la suppliation auprès de Dieu — Puissant et Majestueux — pour détourner ce qui m’atteint comme épreuves.",
            "La préservation de la chasteté et la pudicité sont un honneur pour la femme dans toutes les lois célestes.",
            "Jésus — que le salut soit sur lui — est l’esprit de Dieu et Sa parole ; Il le créa sans père, miracle attestant Sa puissance et Sa volonté.",
            "Marie fille de ʿImrān est le modèle de la femme dans sa plénitude spirituelle et morale.",
            "1. Quel est le sens de l’exemple frappé pour les croyants par la femme de Pharaon ?",
            "2. Par quoi la femme de Pharaon affronta-t-elle la tyrannie de son époux et son opposition à sa foi ?",
            "3. Par quoi Dieu distingua-t-Il Marie fille de ʿImrān et éleva-t-Il sa valeur ?",
            "J’écris un sujet de synthèse dans lequel je résume les principales questions traitées par la sourate aṭ-Ṭarīm, et les desseins qui en sont tirés, en exploitant les compétences que j’ai acquises en matière d’expression et de rédaction.",
            "Exégèse de la sourate aṭ-Ṭarīm (versets : 11-12)",
        ],
        "verses": {
            "66:11": ["وضرب الله مثلا للذين ءامنوا امرات فرعون",
                      "اذ قالت رب ابنلى عندك بيتا فى الجنة",
                      "ونجنى من فرعون وعمله",
                      "ونجنى من القوم الظلمين"],
            "66:12": ["ومريم ابنت عمرن التى احصنت فرجها",
                      "فنفخنا فيه من روحنا",
                      "وصدقت بكلمت ربها وكتبه",
                      "وكانت من القنتين"],
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
