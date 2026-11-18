#!/usr/bin/env python3
"""R731 — ajoute le commentaire pédagogique de la leçon 1 (pdf-mut23h2x-390,
غسل المحرم للحج — la grande ablution du pèlerin avant l'iḥrām) à
content/commentaires/hadith-3es.json.
Vague 15 (dernière vague) : elle achève hadith-3es 29/29 (le SUIVANT de
R730, slot précisé). Même protocole que comm-r730.py : normalisation de la
ponctuation FR (U+202F avant ; : ! ? » et après «, apostrophe courbée) sur
l'entrée nouvelle seulement — opération idempotente. Rédaction d'après la
lecture complète de la leçon (htmlFr intégral, 41 810 caractères, extraction
non lossy scripts/extrait-r731.py). Les numéros du Muwaṭṭaʾ (901-908), les
citations (définition d'Ibn ʿArafa, « le pèlerinage, c'est ʿArafa », parole à
ʿĀʾicha) et les statuts sont cités tels qu'ils figurent dans la leçon
(règle 2 de LISEZ-MOI.md : aucune invention). Les formes arabes du
vocabulaire sont posées au squelette standard SANS harakat (situation des
vagues 5-14 : les gloses de ces leçons sont rendues en translittération dans
la couche FR) ; aucune harakat n'est inventée (règle 2). Les ʿ et ʾ
(U+02BF / U+02BE) sont posés directement dans les champs FR pour les noms
propres et les fragments de translittération — la normalisation ne les
touche pas."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_390 = {
    "auteur": "IA-1, tour R731",
    "resume": "Guide de lecture de la leçon 1 (غسل المحرم للحج) : la leçon ouvre le livre d'al-Ḥadīth par le cinquième pilier — le ḥajj dans la langue (l'intention et la direction d'un but) et dans la terminologie d'Ibn ʿArafa (« un acte d'adoration à laquelle est inhérente la station à ʿArafa, la nuit du dix de Dhū al-Ḥijja ») — puis son statut : obligation unique dans la vie, connue de la religion par nécessité, due à celui qui a la capacité par son argent et son corps (Āl ʿImrān 97). Le corps de la leçon examine les trois situations de la grande ablution du muḥrim que le chāriḥ ordonne : une sunna confirmée, la plus emphatique des ablutions du ḥajj, pour l'iḥrām — attestée par l'ordre donné à ʿAsmāʾ bint ʿUmayṣ en couches (n° 901, avec sa variante au n° 902) et la triple pratique d'Ibn ʿUmar (n° 903) ; l'unanimité pour la grande impureté, de la femme consacrée en règles ou en couches comprise (n° 907) ; la divergence documentée pour le rafraîchissement, où le récit des ʿAbwāʾ (n° 904) — la divergence d'Ibn ʿAbbās et d'al-Muswar b. Makhrama départagée par le geste d'Abū Ayyūb al-Anṣārī — livre les règles d'herméneutique de la leçon et la règle de l'autorité de la parole du Compagnon. La clôture donne l'ablution d'entrée à La Mecque (n° 906), réservée à qui fera les tours, la sagesse spirituelle de la purification, l'évaluation en quatre items et l'exploitation du texte de Mālik sur le savon après la lance de al-ʿAqaba (n° 908).",
    "explication": [
        "La page d'ouverture (p.10) pose trois objectifs : connaître le sens du ḥajj et son statut juridique, saisir les règles des différentes formes de la grande ablution du pèlerin consacré, et saisir les finalités (maqāṣid) de la grande ablution en vue de l'iḥrām. Le tamhīd pose le décor doctrinal avant les textes : le ḥajj est le cinquième des piliers de l'Islām, et le consensus du jumhūr est qu'il a été prescrit en l'an six de l'Hégire ; il possède une place à part parmi les piliers, car c'est un acte d'adoration fait à la fois d'argent et de corps — il réunit la dépense matérielle du voyage et la peine physique des rites. Les trois questions d'ouverture ordonnent la leçon entière : qu'est-ce que le ḥajj ? quel est son statut ? et quel est le statut de l'ablution que fait le pèlerin en vue de l'iḥrām ? — le bloc de synthèse (istikhlāṣ al-muḍmīn) la ramasse en deux items : la définition du ḥajj dans la langue et la terminologie, puis le statut de l'ablution d'iḥrām et ses finalités.",
        "La définition et le statut répondent à la première question. Dans la langue : al-ḥajj se prononce avec la ḥāʾ portée à la voyelle ouverte ou à la voyelle fermée — l'on a dit que la forme ouverte est le nom et la fermée le nom d'action, et l'on a dit l'inverse ; le sens est l'intention (al-qaṣd) et la direction d'un but. Dans la terminologie, le manuel donne la définition d'Ibn ʿArafa : « un acte d'adoration à laquelle est inhérente la station à ʿArafa, la nuit du dix de Dhū al-Ḥijja » — la restriction à la station exprime la place éminente de ce rite, pilier le plus important du ḥajj d'après la parole du Prophète « le pèlerinage, c'est ʿArafa » (rapportée par al-Bukhārī et Muslim). Le statut suit : le ḥajj est une obligation une fois dans la vie, dont le caractère obligatoire est connu de la religion par nécessité (maʿlūm min ad-dīn bi-ḍarūra) ; il ne devient pas une obligation répétée, par consensus, sauf pour le vœu (an-nadhr) ; le fait qu'il soit dû immédiatement fait divergence ; il n'incombe qu'à celui qui en a la capacité par son argent et son corps — d'après Āl ʿImrān 97 : « Et c'est un devoir envers Allah pour les gens qui ont les moyens, d'aller faire le pèlerinage de la Maison ».",
        "Les textes arment la seconde question. Le n° 901 est la matrice de la première situation : ʿAsmāʾ bint ʿUmayṣ accouche de Muḥammad b. Abī Bakr à al-Bayḍāʾ, Abū Bakr informe le Messager de Dieu, qui ordonne « que l'on lui ordonne de se faire la grande ablution, puis qu'elle se mette en état d'iḥrām » — le mot d'ordre « murhā » est porté tel qu'imprimé, et le chāriḥ en relève la règle : l'ordre, selon le plus répandu, ne s'adresse pas à un tiers absent, sauf comme dans l'affaire d'Ibn ʿUmar où l'ordre fut porté par une autre voix que la sienne ; le n° 902 en porte la variante (« Abū Bakr lui ordonna de se laver puis d'entrer en iḥrām »). Le n° 903 montre l'assiduité d'Ibn ʿUmar : il se lavait en vue de son iḥrām, de même en vue de son entrée à La Mecque, et de même en vue de sa station au soir dʿArafa — la pureté corporelle accompagne chacun des temps forts du pèlerinage. Le n° 906 complète le tableau : Ibn ʿUmar passait la nuit à Dhū Ṭuwā, priait l'aube, entrait par le col qui domine La Mecque, et ne rentrait pas avant de s'être lavé — il ordonnait aussi à ses compagnons de se laver avant d'entrer ; le n° 907 pose la réserve : il ne lavait pas sa tête en état d'iḥrām excepté à l'occasion d'une pollution nocturne (al-iḥtilām) — le lavage de tête du muḥrim est réservé au nécessaire.",
        "Le cœur narratif est le n° 904 : deux Compagnons divergent aux ʿAbwāʾ — Ibn ʿAbbās dit « le muḥrim peut se laver la tête », al-Muswar b. Makhrama dit « le muḥrim ne se lave pas la tête » ; loin d'imposer son avis, Ibn ʿAbbās envoie Ibn Ḥunayn interroger Abū Ayyūb al-Anṣārī, trouvé en train de se laver entre les deux poteaux du puits, se couvrant d'un tissu ; Abū Ayyūb incline le tissu jusqu'à laisser voir sa tête, fait verser l'eau, remue sa tête avec ses mains, portée en avant puis en arrière, puis dit : « c'est ainsi que j'ai vu le Messager de Dieu faire ». Le commentaire relève la licéité de ce lavage tant qu'il ne conduit pas à un défaut du cheveu, et l'exposé en acte, plus éloquent que l'exposé par parole (al-bayān bi-l-fiʿl wa-huwa ablagh min al-qawl) : Abū Ayyūb ne se contente pas de répondre, il refait devant le questionneur le geste même du Prophète. Le n° 905 appuie la même règle : ʿUmar, en iḥrām, demande à Yaʿlā b. Munya « verse sur ma tête » — l'eau ne coûte au pèlerin que des cheveux éparpillés (chaʾthā), rien qui équivaille à arracher le cheveu.",
        "Le fiqh du chāriḥ range les situations en trois. Première : l'ablution en vue de l'iḥrām est une tradition confirmée (sunna muʾakkada) dont on ne dispense qu'en cas d'excuse, et elle est la plus emphatique des ablutions du ḥajj ; du n° 901 le commentaire tire la validité de l'iḥrām de la femme en couches (an-nufsāʾ) et de la menstruée (al-ḥāʾiḍ), à plus forte raison de celle en grande impureté — elles partagent l'étendue du nom d'impureté mineure et s'y ajoutent par l'écoulement du sang : un cas d'émergence du sens (farʿ ẓuhūr al-maʿnā) pour l'analogie dans les actes d'adoration, selon ceux qui l'admettent. Al-Khaṭṭābī ajoute le sens du hadith : la recommandation de ressembler aux gens de mérite et de perfection dans l'espérance d'atteindre leurs rangs ; et il est notoire que le lavage de la menstruée et de la femme en couches ne les purifie pas — il est pour la noblesse du lieu et du temps, la propreté et la disparition de l'odeur pénible, pour écarter leur tort au rassemblement des gens. Deuxième : sur la grande ablution du muḥrim pour la grande impureté il y a unanimité — le muḥrim se lave, et de même la femme consacrée qui a ses règles ou qui est en couches ; sur le lavage pour se rafraîchissement (t-tabarrud), divergence : le corps des savants l'autorise sans détestabilité d'après le n° 904 et le n° 905, d'autres y voient une détestabilité sans texte fermement établi. Troisième : l'ablution d'entrée à La Mecque est recommandée selon la capacité pour quiconque n'est ni menstruée ni en couches — elle est pour les tours (aṭ-ṭawāf) ; c'est pourquoi elle n'est pas recommandée à ces deux dernières, qui n'entrent pas non plus la mosquée, tandis qu'elles se lavent pour l'iḥrām et pour la station — d'après la parole du Prophète à ʿĀʾicha : « fais ce que fait le pèlerin, excepté que tu ne feras pas les tours de la Maison » (Ṣaḥīḥ al-Bukhārī).",
        "Du récit des ʿAbwāʾ le commentaire tire les règles d'herméneutique (al-qawāʿid al-uṣūliyya) qui font de cette leçon une porte sur la méthodologie : le retour des divergents vers celui dont l'on présume qu'il détient la science de ce sur quoi ils divergent ; l'acceptation du rapport isolé (khabar al-wāḥid) — qui était connu (machhūr) parmi les Compagnons, car Ibn ʿAbbās envoya Ibn Ḥunayn interroger Abū Ayyūb ; et la nécessité corrélative d'accepter le rapport d'Abū Ayyūb sur le Prophète, le retour au texte (an-naṣṣ) en cas de divergence, et l'abandon de l'effort d'interprétation et de l'analogie là où le texte existe. Ibn ʿAbd al-Barr tranche le principe : lorsque les Compagnons divergeaient, aucun des deux n'était une preuve (ḥujja) sur l'autre sauf par un indicice — ce qui indique la règle de l'autorité de la parole du Compagnon, dont le domaine d'application dépasse le Compagnon lui-même. L'évaluation en quatre items retourne au fil : produire l'indicice coranique du statut du ḥajj avec le visage de l'indicice ; exposer le statut de l'ablution d'iḥrām et celui de l'ablution pour la grande impureté et le rafraîchissement avec les indices ; extraire les règles d'herméneutique avec leur éclairage par les exemples appropriés ; et trancher deux situations imprimées — l'homme qui s'est consacré sans s'être lavé (son iḥrām demeure valide, la sunna confirmée étant remisée devant l'excuse) et la femme en couches qui ne s'est pas lavée pour l'entrée à La Mecque (rien ne pèse sur elle : l'ablution d'entrée n'étant pas recommandée à celle qui ne fait pas les tours). L'exploitation imprime le texte de Mālik (n° 908) : rien ne reproche à l'homme consacré de laver sa tête avec du savon (al-ghasūl) après la lance de al-ʿAqaba, avant de se raser — après le lancer, il lui est devenu permis de tuer les poux, de se raser les cheveux, de jeter les immondices (al-tafath) et de porter les vêtements : la levée des interdictions partielles l'emporte sur la détestabilité du lavage ; la seconde question demande si le savon prend en son sens ce qui l'équivaut parmi les moyens de purification modernes — l'indicice est dans le commentaire du geste d'Abū Ayyūb et sa restriction « tant que cela ne conduit pas à un défaut du cheveu ». La préparation préalable annonce la leçon 2 (libās al-muḥrim), déjà livrée au registre.",
    ],
    "points": [
        "Fil de révision : trois objectifs (sens et statut du ḥajj ; règles des formes de la grande ablution ; finalités de l'ablution d'iḥrām) → tamhīd (cinquième pilier, prescrit en l'an six, adoration d'argent et de corps) → définition (langue : l'intention ; terminologie : Ibn ʿArafa) → statut du ḥajj (unique dans la vie, capacité — Āl ʿImrān 97) → sept textes (n° 901, 902, 903, 904, 905, 906, 907) → gloses (al-Bayḍāʾ, tahallala, Ṭuwā, chaʾthā, ath-thaniyya) → tarājim (ʿAṭāʾ b. Abī Rabāḥ, Ibn ʿUmar) → charḥ (trois situations) → évaluation en quatre items → exploitation du n° 908 → préparation de la leçon 2.",
        "La définition d'Ibn ʿArafa : la restriction à la station dʿArafa exprime la place éminente du rite — pilier le plus important du ḥajj d'après « le pèlerinage, c'est ʿArafa » (al-Bukhārī et Muslim) ; dans la langue, al-ḥajj veut dire l'intention et la direction d'un but.",
        "Le statut du ḥajj : obligation une fois dans la vie, connue de la religion par nécessité ; pas répétée par consensus, sauf pour le vœu (an-nadhr) ; le caractère immédiat fait divergence ; capacité par argent et corps (Āl ʿImrān 97).",
        "Les trois situations de la grande ablution : sunna confirmée dispensée seulement avec excuse pour l'iḥrām — la plus emphatique (n° 901, 903 ; validité de l'iḥrām de la femme en couches et de la menstruée, farʿ ẓuhūr al-maʿnā) ; unanimité pour la grande impureté, la femme consacrée en règles ou en couches comprise (n° 907) ; divergence pour le rafraîchissement — jumhūr licite sans détestabilité, d'autres détestabilité sans texte fermé (n° 904, 905) ; l'entrée à La Mecque recommandée pour qui fera les tours — pas pour la menstruée ni la femme en couches (n° 906, parole à ʿĀʾicha).",
        "Les règles d'herméneutique du récit des ʿAbwāʾ : le retour des divergents vers qui détient la science de ce sur quoi ils divergent ; l'acceptation du khabar al-wāḥid machhūr parmi les Compagnons ; le retour au naṣṣ en cas de divergence et l'abandon de l'interprétation et de l'analogie là où le texte existe — et la règle d'Ibn ʿAbd al-Barr : aucun des deux divergents n'est ḥujja sur l'autre sauf par un indicice (l'autorité de la parole du Compagnon, dont le domaine dépasse le Compagnon).",
        "L'exposé en acte : Abū Ayyūb ne répond pas par parole seule, il refait devant le questionneur le geste du Prophète — « al-bayān bi-l-fiʿl wa-huwa ablagh min al-qawl » ; la licéité du lavage de tête tient tant qu'il ne conduit pas à un défaut du cheveu (n° 904 ; n° 905 — « verse, l'eau ne fera de toi que des cheveux éparpillés »).",
        "L'évaluation, quatrième item : l'homme consacré qui ne s'est pas lavé — son iḥrām demeure valide, la sunna confirmée remisée devant l'excuse ; la femme en couches sans lavage d'entrée — rien ne pèse sur elle, elle ne fait pas les tours.",
        "L'exploitation (n° 908) : le savon (al-ghasūl) après la lance de al-ʿAqaba est autorisé avant le rasage — la levée des interdictions partielles (tuer les poux, se raser, jeter les immondices, porter les vêtements) l'emporte sur la détestabilité ; l'extension du sens aux moyens de purification modernes reste matière de lecture, l'indicice étant la restriction « tant que cela ne conduit pas à un défaut du cheveu ».",
    ],
    "vocabulaire": [
        {"ar": "غسل المحرم للحج", "translit": "ghusl al-muḥrim li-l-ḥajj", "fr": "la grande ablution du pèlerin consacré en vue du pèlerinage — la leçon en ordonne trois situations : l'iḥrām (sunna confirmée), la grande impureté et le rafraîchissement, l'entrée à La Mecque"},
        {"ar": "البيداء", "translit": "al-Bayḍāʾ", "fr": "la Blanche — une contrée au bord de Dhū al-Ḥulayfa, le point de consécration des gens de Médine, où ʿAsmāʾ bint ʿUmayṣ accoucha de Muḥammad b. Abī Bakr (n° 901)"},
        {"ar": "تحلل", "translit": "tahallala", "fr": "il entra en iḥrām — il se consacra et revêtit les habits de l'iḥrām"},
        {"ar": "شعتها", "translit": "chaʾthā", "fr": "les cheveux dénoués et poussiéreux — ce que coûte à ʿUmar l'eau versée directement sur sa tête (n° 905) : rien qui équivaille à arracher le cheveu"},
        {"ar": "ذو طوى", "translit": "Dhū Ṭuwā", "fr": "une vallée proche de La Mecque — Ibn ʿUmar y passait la nuit avant de prier l'aube et d'entrer par le col (n° 906)"},
        {"ar": "الاحتلام", "translit": "al-iḥtilām", "fr": "la pollution nocturne — la seule occasion pour laquelle Ibn ʿUmar lavait sa tête en état d'iḥrām (n° 907)"},
        {"ar": "النفساء", "translit": "an-nufsāʾ", "fr": "la femme en couches — son iḥrām est valide sans lavage préalable (n° 901), et l'ablution d'entrée à La Mecque ne lui est pas recommandée car elle ne fait pas les tours"},
        {"ar": "الغسول", "translit": "al-ghasūl", "fr": "le savon — rien ne reproche au muḥrim de laver sa tête avec après la lance de al-ʿAqaba, avant de se raser (n° 908)"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

def norme_fr(s):
    s = s.replace('\'', '’')
    s = re.sub(r'\s+([;:!?»])', '\u202f\\1', s)
    s = s.replace('« ', '«\u202f')
    return s

def norme_entree(e):
    e['resume'] = norme_fr(e['resume'])
    e['avertissement'] = norme_fr(e['avertissement'])
    e['explication'] = [norme_fr(x) for x in e['explication']]
    e['points'] = [norme_fr(x) for x in e['points']]
    for v in e.get('vocabulaire', []):
        v['fr'] = norme_fr(v['fr'])
    return e

data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
DOCID = 'pdf-mut23h2x-390'
if DOCID in com:
    print(f'!! {DOCID} déjà présent — rien de fait')
    raise SystemExit(1)
com[DOCID] = norme_entree(E_390)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume + ponctuation FR + arabes hors champ ar + guillemets appariés
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
e = data2['commentaires'][DOCID]
mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
for t in textes:
    hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t).replace('ﷺ', '')
    if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
        mauvais += 1
        print('   ponctuation à revoir dans :', t[:60])
    if motif_ar.search(hors_parenth):
        mauvais += 1
        print('   caractère arabe hors parenthèses :', t[:60])
    if t.count('«') != t.count('»'):
        mauvais += 1
        print('   guillemets non appariés :', t[:60])
for v in e['vocabulaire']:
    if not motif_ar.search(v['ar'].replace(' ', '')):
        mauvais += 1
        print('   vocab ar non arabe :', v['ar'])
    if re.search(r'[\u064B-\u0652\u0670]', v['ar']):
        mauvais += 1
        print('   vocab ar avec harakat :', v['ar'])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
