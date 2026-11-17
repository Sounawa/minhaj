#!/usr/bin/env python3
"""R721 — ajoute les commentaires pédagogiques des leçons 21 (pdf-mut23h2x-410,
la fidya du pèlerinage) et 20 (pdf-mut23h2x-409, la tonsure et la coupe) à
content/commentaires/hadith-3es.json.
Même protocole que comm-r720.py : normalisation de la ponctuation FR (U+202F
avant ; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles
seulement — opération idempotente. Rédaction d'après la lecture complète des
deux leçons (extraiteur pilote-comm-extrait.py, fenêtres COMM_DEBUT) ; les
numéros du Muwaṭṭaʾ et les āyas sont cités tels qu'ils figurent dans les
leçons (règle 2 de LISEZ-MOI.md : aucune invention). Les formes arabes du
vocabulaire sont posées au squelette standard SANS harakat — ces deux leçons
présentent leur lexique en translittération française et ne portent pas les
formes vocalisées ; aucune harakat n'est inventée."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_410 = {
    "auteur": "IA-1, tour R721",
    "resume": "Guide de lecture de la leçon 21 (أحكام الفدية في الحج) : la table des compensations du tuage dans le ḥaram — du bélier de la hyène à la poignée de nourriture du pou — et le cadre légal de la fidya : le concept, le statut, les trois types et la règle du choix.",
    "explication": [
        "La page d’ouverture (p.141) fixe trois objectifs : reconnaître le concept de la fidya et son statut, distinguer ses types et ce sur quoi elle s’impose, s’imprégner des orientations de la Loi dans ses règles et ses finalités. Le tamhīd nomme les deux racines de l’interdit du sacralisé — l’ornement (at-tazayyun) et le luxe (at-taraff) — et range le tuage des animaux dans le même bloc : quiconque fait un de ces actes doit la fidya. Les deux questions d’ouverture prennent le quand du rachat et le tuage du gibier — les deux moitiés de la recherche légale.",
        "Les six textes construisent la table des compensations. Le premier (n° 1240) pose la quadripartition dʿUmar : le bélier pour la hyène, la chèvre pour la gazelle, la chevrette pour le lièvre, le souriceau pour le gerboise. Le second (n° 1242) ajoute le critère d’espèce : la bête sauvage se couvre de la compensation de la bête domestique qui lui ressemble. Le troisième (n° 1243) change de registre — la colombe de La Mecque, apprivoisée et protégée par la sacralité du lieu, se couvre de la brebis pleine ; le quatrième (n° 1244) étend aux poussins cagés dans la maison du Mecquois — le tuage passe par son fait, une brebis par poussin. Le cinquième (n° 1245) grimpe l’échelle des mesures : l’autruche se couvre du chameau entier. Le sixième (n° 1248) clôt par la règle générale : la fidya ne connaît ni l’âge ni la valeur de la victime — le petit couvre comme le grand — et l’étalonnage est la diya (n° 1262 : comme l’homme libre qui tire dans le ḥaram — le dépérissement est garanti, au délibéré comme au fautif). Les trois gloses — baʾanāq, al-yarbūʿ, bijafra — nomment la basse de la table : les plus petites bêtes d’offrande sur les plus petites bêtes atteintes.",
        "La première section cadre le concept et le statut. En langue, la fidya est le substitut par lequel on libère une chose — l’āya du rachat d’Ismaël par l’immolation généreuse (aṣ-Ṣāffāt 107) en est la première occurrence du Livre ; en terminologie, c’est le substitut qui délivre le responsable de l’interdit franchi. Le statut est posé par consensus : quiconque fait une chose des interdits de la sacralisation — raser la tête, couper les ongles, l’enduit, le parfum, porter la couture — doit une fidya ; et elle ne lave pas le délibéré, qui porte le péché en plus de la compensation. Trois types : l’animal immolé (an-nusk — la brebis, exigée aux conditions de l’aḍḥiyya), l’assiette (nourrir six pauvres, deux mud chacun, de la nourriture dominante du lieu), le jeûne de trois jours (permis en tout temps où le jeûne est permis). Et la règle du choix : au choix, non en ordre (ʿalā at-takhīyr lā ʿalā at-tartīb) — le « ou » de l’āya d’al-Baqara, l’attestation d’Ibn ʿAbbās dans les authentiques, la sentence de Mālik.",
        "La seconde section pose la fidya du gibier et de l’oiseau. Les statuts dʿUmar se règlent sur la proximité de la mesure (li-taqārubihimā fī al-qadr) — la bête de compensation est celle qui s’approche de la bête atteinte par le volume. La colombe porte la brebis pleine pour trois raisons : la sacralité du lieu, l’apprivoisement des colombes, la fréquence du tuage si la compensation descendait plus bas ; l’autruche porte le chameau pour la proximité de la mesure et de la forme. Le cas vécu (n° 1241) donne le modèle du jugement : deux sacralisés en course de chevaux atteignent une antilope — ʿUmar ne tranche pas seul, il s’aide de ʿAbd ar-Raḥmān b. ʿAwf, et une chèvre est immolée sur la bête. La notice d’abū az-Zubayr — le client madois établi à La Mecque, véridique, mort l’an 128 — scelle la voie des statuts.",
        "L’évaluation teste la table et le statut : reconnaître la fidya et ses types ; trancher deux situations avec l’argument — l’autruche tuée après la sacralisation (le chameau, n° 1245) et la colombe (la brebis, n° 1243). L’exploitation descend au plancher : l’encadré du n° 1255 couvre le pou par la poignée de nourriture — la fidya descend jusque sous la brebis, elle ne s’annule jamais ; l’invite fait extraire le statut de la coupe des ongles et des saletés — l’extension de la même règle (n° 1260). La préparation annonce la leçon 22 : la glose contextuelle des trois termes (an-suka bi-chaʾa — jarādāt — qabḍa) et la fidya du tuage du locuste et du rasage de la tête.",
    ],
    "points": [
        "Fil de révision : trois objectifs → deux questions du tamhīd → six textes (la table des compensations) → deux sections (concept, statut, types ; gibier et oiseau) → deux questions d’évaluation sur le même fil.",
        "La table : hyène→bélier, gazelle→chèvre, lièvre→chevrette, gerboise→souriceau (n° 1240) ; la ressemblance d’espèce (n° 1242) ; la colombe de La Mecque→brebis pleine (n° 1243) ; les poussins cagés→une brebis chacun (n° 1244) ; l’autruche→chameau entier (n° 1245) ; le petit comme le grand, étalonnage sur la diya (n° 1248, n° 1262).",
        "Critères : la proximité de la mesure (li-taqārubihimā fī al-qadr), l’espèce qui ressemble, la forme pour l’autruche — la sacralité du lieu et l’apprivoisement relèvent la colombe au-dessus de son équivalent.",
        "Concept : le substitut qui libère — le rachat d’Ismaël (aṣ-Ṣāffāt 107) est la première fidya du Livre ; statut : consensus sur tout interdit de la sacralisation — et la fidya ne lave pas le délibéré, qui porte le péché en plus.",
        "Types et choix : an-nusk, al-iṭʾām (six pauvres, deux mud chacun), aṣ-ṣiyām (trois jours) — au choix, non en ordre ; l’argument triple : l’āya, Ibn ʿAbbās dans les authentiques, la sentence de Mālik.",
        "Le plancher de la fidya : le pou se couvre de la poignée de nourriture (n° 1255) — la compensation descend au plus petit vivant du ḥaram sans jamais disparaître ; la coupe des ongles et les saletés relèvent de la même règle (n° 1260).",
    ],
    "vocabulaire": [
        {"ar": "الفدية", "translit": "al-fidya", "fr": "la compensation — le substitut par lequel on libère une chose ; le rachat d’Ismaël par l’immolation généreuse en est la première occurrence du Livre"},
        {"ar": "النسك", "translit": "an-nusk", "fr": "l’animal immolé — premier type de la fidya ; la brebis exigée aux conditions de l’aḍḥiyya"},
        {"ar": "الإطعام", "translit": "al-iṭʾām", "fr": "l’assiette de nourriture — six pauvres, deux mud chacun, de la nourriture dominante du lieu"},
        {"ar": "الصيام", "translit": "aṣ-ṣiyām", "fr": "le jeûne — troisième type, trois jours permis en tout temps où le jeûne est permis"},
        {"ar": "البدنة", "translit": "al-badana", "fr": "le chameau entier — la compensation de l’autruche, la plus haute de la table"},
        {"ar": "اليربوع", "translit": "al-yarbūʿ", "fr": "le gerboise — la petite bête creuseuse du schème yufʿūl ; sa compensation est le souriceau"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}

E_409 = {
    "auteur": "IA-1, tour R721",
    "resume": "Guide de lecture de la leçon 20 (أحكام الحلق والتقصير) : la tonsure et le raccourcissement posés rite du pèlerinage — l’invocation répétée pour les tondus, l’ordre sans divergence sur le temps, la licence du rasage oublié — puis l’épargne du cheveu et la coupe de la barbe et de la moustache.",
    "explication": [
        "La page d’ouverture (p.136) fixe trois objectifs : reconnaître les règles du ḥalq et du taqṣīr, la cause de la répétition de l’invocation prophétique pour les tondus, et les finalités des deux gestes dans le pèlerinage. Le tamhīd pose le fondement du cours tout entier : la tonsure et le raccourcissement ne sont pas un geste de toilette ajouté au ḥajj — ils sont un rite (nusk), nommé ainsi par la parole d’Allah elle-même (sourate al-Fatḥ, l’āya 27 : « …et les raccourcis »).",
        "Les quatre textes font chacun un travail précis. Le premier (n° 1174) porte le cœur du cours : l’invocation pour les tondus, dite deux fois entière ; à la demande des Compagnons — « et les raccourcis ? » — une troisième l’ajoute, la glose résolvant l’ajout final comme un ʿaṭf sur un mot effacé (wa-l-maqṣadayn : dis « et fais miséricorde aux raccourcis »). Le second (n° 1178) est l’armature légale : l’ordre sans divergence — nul cheveu pris avant la bête immolée, nulle délivrance de la sacralisation hors la tonsure ou la coupe. Le troisième (n° 1184) donne le geste inverse : avant la sacralisation, donc hors de l’état d’iḥrām, Sālim b. ʿAbd Allāh coupe aux deux ciseaux (al-jilmayn — le double de al-jilm, le coupe-choux). Le quatrième (n° 1177) ouvre la licence : la tonsure oubliée à Minā peut être rattrapée à La Mecque — « cela est large » — sans que la précellence du lieu soit abandonnée : « la tonsure à Minā est plus aimée pour moi ».",
        "La première grande section règle le statut, le temps et le lieu. Le statut : la tonsure ou le raccourcissement est une obligation des obligations du pèlerinage — qui l’allonge ou rentre au pays sans l’accomplir porte le sang (ad-dam), l’expiation de la bête ; et la distinction des sexes : la femme n’a pas la tonsure, elle a la sunna du raccourcissement, sur l’athar d’Ibn ʿAbbās porté au prophétique. Le temps est borné par trois repères entrelacés : le lever de l’aube du dix — la même borne qui règle l’immolation (n° 1173 : nul n’immole avant l’aube du jour de l’Immolation) —, le jet de la Jamra dʿAqaba — la première œuvre du matin —, puis la tonsure. Le lieu : Minā ou La Mecque, la précellence à Minā.",
        "La seconde section ouvre l’épargne et la coupe. L’épargne des cheveux est recommandée au prétendant au ḥajj — laisser pousser pour que la tonsure enlève beaucoup — et son versant inverse pour le muʾtamir dont le ḥajj est proche : ne pas se raser, de peur d’arriver sans cheveu à tonsurer ; la relation de Nāfiʾ en donne le modèle — ʿAmr b. ʿAbd Allāh, ayant rompu le jeûne de ramaḍān en vue du ḥajj, suspend toute prise de cheveux. La coupe de la barbe et de la moustache (n° 1180) accompagne la tonsure sans s’identifier à elle : Ibn ʿUmar, à chaque tonsure — en ḥajj comme en ʿumra —, prenait des deux, la prise suspendue dès le début de chawwāl pour leur longueur ; mais cette prise n’appartient pas au parachèvement de la délivrance (tamām at-taḥallul).",
        "L’évaluation reprend les trois items du résumé : la manière et le statut ; la cause de l’invocation triple ; l’épargne des cheveux avec la preuve. L’exploitation règle la délivrance différée : l’athar du muʾtamir de nuit (n° 1175) — ṭawāf et course accomplis la nuit, la tonsure reportée au matin : le report ne rompt pas la délivrance, mais la Maison ne reçoit plus son ṭawāf entre la course et la tonsure, et la Mosquée lui reste ouverte pour le witr, sans approche de la Maison ; l’invite fait extraire le statut du report avec le commentaire d’az-Zarqānī. La préparation annonce la leçon 21 — la fidya du gibier atteint et la fidya de détour du mal : le cours a clos le cycle du corps du pèlerin.",
    ],
    "points": [
        "Fil de révision : trois objectifs → trois items du résumé → deux sections (statut, temps, lieu ; épargne et barbe) → trois questions d’évaluation sur le même fil.",
        "Statut : obligation des obligations du ḥajj — le délaissement engage le sang (ad-dam) ; la femme n’a pas la tonsure, elle a la sunna du raccourcissement (athar d’Ibn ʿAbbās).",
        "Temps et lieu : après l’aube du dix et après la Jamra dʿAqaba ; Minā ou La Mecque — la précellence à Minā (« la tonsure à Minā est plus aimée pour moi »), et le rasage oublié rattrapable (n° 1177, « cela est large »).",
        "L’invocation (n° 1174) : deux fois entière pour les tondus, une troisième inclut les raccourcis sur la demande des Compagnons — la précellence de la tonsure portée par l’insistance : le tondu offre le tout du cheveu, le raccourci en garde une part.",
        "Épargne et barbe : épargner pour la tonsure, et ne pas se raser quand le ḥajj est proche (le modèle de ʿAmr b. ʿAbd Allāh) ; Ibn ʿUmar prenait de la barbe et de la moustache à chaque tonsure (n° 1180) — une prise hors du tamām at-taḥallul.",
        "La délivrance différée (n° 1175) : le muʾtamir de nuit peut tourner et courir la nuit et reporter la tonsure au matin — mais plus de ṭawāf à la Maison entre la course et la tonsure ; le witr reste permis dans la Mosquée.",
    ],
    "vocabulaire": [
        {"ar": "الحلق", "translit": "al-ḥalq", "fr": "la tonsure — le rasage entier de la tête ; l’une des deux voies du rite final du pèlerinage"},
        {"ar": "التقصير", "translit": "at-taqṣīr", "fr": "le raccourcissement — raccourcir les cheveux sans les raser ; la sunna de la femme"},
        {"ar": "التحلل", "translit": "at-taḥallul", "fr": "la délivrance de la sacralisation — elle ne se consomme pas sans la tonsure ou la coupe (n° 1178)"},
        {"ar": "النسك", "translit": "an-nusk", "fr": "le rite — le nom que le tamhīd donne à la tonsure et au raccourcissement, tiré de la parole d’Allah"},
        {"ar": "المحلقين", "translit": "al-muḥalliqīn", "fr": "les tondus — ceux pour qui le Prophète ﷺ a répété l’invocation, précellence sur les raccourcis"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}


def norme_fr(s):
    s = s.replace('\'', '’')
    s = re.sub(r'\s+([;:!?»])', '\u202f\\1', s)
    s = s.replace('« ', '«\u202f')
    return s


def norme_entree(e):
    for cle in ('resume', 'avertissement'):
        if cle in e:
            e[cle] = norme_fr(e[cle])
    e['explication'] = [norme_fr(x) for x in e['explication']]
    e['points'] = [norme_fr(x) for x in e['points']]
    for v in e.get('vocabulaire', []):
        v['fr'] = norme_fr(v['fr'])
    return e


data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
for docid, entree in (('pdf-mut23h2x-410', E_410), ('pdf-mut23h2x-409', E_409)):
    if docid in com:
        print(f'!! {docid} déjà présent — rien de fait')
        raise SystemExit(1)
    com[docid] = norme_entree(entree)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume + ponctuation FR + arabes hors champ ar
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for docid in ('pdf-mut23h2x-410', 'pdf-mut23h2x-409'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        # l’arabe entre parenthèses (titres du manuel) est échappé au build
        # en balises RTL (LISEZ-MOI.md §3.3) — hors parenthèses : 0 arabe
        hors_parenth = re.sub(r'\([^)]*[؀-ۿ][^)]*\)', '()', t).replace('ﷺ', '')
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
