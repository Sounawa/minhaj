#!/usr/bin/env python3
"""R722 — ajoute les commentaires pédagogiques de la leçon 19 (pdf-mut23h2x-408,
les rites du pèlerin au jour du sacrifice) et de la leçon 18 (pdf-mut23h2x-407,
les règles de la bête d'offrande (2)) à content/commentaires/hadith-3es.json.
Vague 6 : remontée du manuel (le SUIVANT de R721).
Même protocole que comm-r721.py : normalisation de la ponctuation FR (U+202F
avant ; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles
seulement — opération idempotente. Rédaction d'après la lecture complète des
deux leçons (htmlFr intégral, extraits /tmp) ; les numéros du Muwaṭṭaʾ et les
āyas sont cités tels qu'ils figurent dans les leçons (règle 2 de LISEZ-MOI.md :
aucune invention). Les formes arabes du vocabulaire sont posées au squelette
standard SANS harakat — ces deux leçons ne portent pas les formes vocalisées
du lexique (seuls des artefacts de transcription vocalisés : tamhīd, fiqh,
noms propres) ; aucune harakat n'est inventée (règle 2)."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_408 = {
    "auteur": "IA-1, tour R722",
    "resume": "Guide de lecture de la leçon 19 (ما يفعله الحاج يوم النحر) : le jour de l’Immolation condense l’ensemble des rites — jet, immolation, rasage, ṭawāf de l’Ifāḍa — ; « agis, nulle gêne » absout l’avancé et le différé ; et la délivrance monte en deux degrés : moindre au jet de la Jamra, majeure au ṭawāf de l’Ifāḍa.",
    "explication": [
        "La page d’ouverture (p.130) fixe trois objectifs : reconnaître les œuvres du jour de l’Immolation, saisir les règles de la délivrance du rite, observer la sunna du Prophète ﷺ dans l’accomplissement de ces œuvres. Le tamhīd nomme ce jour d’un titre coranique : le jour du plus grand pèlerinage — la proclamation d’Allah et de Son Messager aux gens (at-Tawba, imprimé « l’āya 3 ») — et y voit se concentrer l’ensemble des rites, d’où les deux questions qui structurent tout le cours : quelles sont les œuvres du jour de l’Immolation, et quand le muḥrim se délivre-t-il par le rite ?",
        "Les trois textes font chacun une lame. Le premier (n° 1173) pose l’armature du temps : nul rasage avant d’immoler la bête, nulle immolation avant l’aube du jour de l’Immolation — « l’œuvre entière est au jour de l’Immolation : l’abattage, et le port des vêtements, et le rejet de la souillure et le rasage ». Le second (n° 1267) est la clef de voûte du jour : le Prophète ﷺ debout pour les gens à Minā, répondant à chaque inversion d’ordre — rasé avant d’immoler (« immole, nulle gêne »), immolé avant de jeter (« jette, nulle gêne ») — par la même absolution : « agis, nulle gêne ». Le troisième (n° 1169) porte la délivrance différée : Ḥafṣa, en mode de qirān, feutrée la chevelure et collierée la bête, s’étonne de demeurer sacralisée — « je ne me délivre point avant d’immoler » ; la notice de la questionneuse — fille de ʿUmar, sœur d’Ibn ʿUmar, émigrée avec Khunays b. Ḥudhāfa, épousée par le Prophète ﷺ après Uḥud, morte en 41 — selon un autre avis 45 — tient la maison de la délivrance.",
        "La première section déroule les œuvres et leur ordre : jet de la Jamra de ʿAqaba, immolation ou abattage, rasage ou raccourcissement, ṭawāf de l’Ifāḍa. Les savants sont unanimes à absoudre l’avancé et le différé (n° 1267) — mais le prix des exceptions est réglé : Mālik exige le sang (ad-dam) pour le ṭawāf de l’Ifāḍa avancé sur le jet, afin qu’il ne soit pas un chemin vers les femmes ; et l’offrande de réparation pour le rasage avancé, qui fait déjà de l’homme un délivré partiel — à la mesure de celui qui éprouve un mal à sa tête. Les règles de l’immolation suivent : nulle bête avant l’aube ; « tout Minā est lieu d’immolation » (n° 1167) — le geste prophétique sanctifie son point exact et la grâce du jour étend la permission à tout le campement ; la main propre est plus excellente (n° 1170 : le Prophète ﷺ immola une partie de sa bête de sa main, une partie par un autre), la délégation permise — et l’ère moderne en fait la règle : le pèlerin mandate les organismes compétents par le paiement du coût de la bête.",
        "La seconde section donne l’échelle de la délivrance. Le discours de ʿUmar à ʿArafa (n° 1226) la mesure en deux degrés : qui a jeté sur la Jamra, il lui est licite le rejet de la souillure et le port des vêtements — sauf les femmes et le parfum ; nul ne touche ses femmes ni le parfum jusqu’à ce qu’il tourne autour de la Maison. Les femmes demeurent interdites jusqu’au ṭawāf de l’Ifāḍa — point de divergence : c’est la fin de la délivrance ; le parfum demeure selon Ibn ʿUmar, seulement blâmé par Mālik ; le gibier reste interdit par la āya d’al-Māʾida. La fatwā de l’oubli du ṭawāf de l’Ifāḍa (n° 1140, règle connectée) ferme le cas limite : retourner et faire l’Ifāḍa, avec la ʿumra et la bête si les femmes ont été approchées. Enfin la boucle du feutrage se ferme : qui feutre, tresse ou natte sa chevelure — rasage obligatoire, nul raccourcissement (n° 1186) ; ʿUmar n’accorde le raccourcissement qu’au feutré simple, refusé au natteur : « ne ressemblez point aux chevelures feutrées » (n° 1185).",
        "L’évaluation retourne en examen les trois questions du cours, dont le cas vécu : un pèlerin a approché son épouse après le jet et avant le ṭawāf de l’Ifāḍa — le pèlerinage demeure valide (l’acte tombe après la première délivrance), la déficience se répare par la ʿumra et la bête, sur le régulateur des leçons précédentes (n° 1128, n° 1129, n° 1136, n° 1138). L’exploitation donne l’athar du rasage oublié (n° 1183) : celui qui a fait l’Ifāḍa sans raser ni raccourcir, par ignorance, retourne raser ou raccourcir puis revient — l’Ifāḍa accomplie étant acquise ; l’invite fait travailler le texte avec le commentaire d’az-Zarqānī. La préparation annonce la leçon 20 : les deux sortes de délivrance et le statut du rasage et du raccourcissement — le cours a clos le cycle du jour de l’Immolation.",
    ],
    "points": [
        "Fil de révision : trois objectifs → deux questions du tamhīd → trois textes (le temps, l’absolution, la délivrance différée) → deux sections (les œuvres et leur ordre ; la délivrance en deux degrés) → trois questions d’évaluation sur le même fil.",
        "Les quatre œuvres du jour dans l’ordre : jet de la Jamra de ʿAqaba, immolation ou abattage, rasage ou raccourcissement, ṭawāf de l’Ifāḍa — « l’œuvre entière est au jour de l’Immolation », rien avant l’aube (n° 1173).",
        "L’absolution : l’avancé et le différé des œuvres du jour permis par consensus — « agis, nulle gêne » (n° 1267) ; mais Mālik règle le prix : le sang pour le ṭawāf avancé sur le jet (le chemin vers les femmes), l’offrande pour le rasage avancé (la délivrance partielle).",
        "L’immolation : nulle bête avant l’aube (n° 1173) ; tout Minā est lieu d’immolation (n° 1167) ; la main propre est plus excellente, la délégation permise (n° 1170) — devenue règle de l’ère moderne par mandatement des organismes.",
        "La délivrance en deux degrés (n° 1226) : moindre au jet — sauf les femmes, le parfum et le gibier ; majeure au ṭawāf de l’Ifāḍa seul — la fin de la délivrance ; l’oubli du ṭawāf se rattrape au retour (n° 1140).",
        "La chevelure travaillée : qui feutre, tresse ou natte — rasage obligatoire (n° 1186) ; le raccourcissement refusé au natteur : « ne ressemblez point aux chevelures feutrées » (n° 1185) ; et le rasage oublié se rattrape après l’Ifāḍa (n° 1183).",
    ],
    "vocabulaire": [
        {"ar": "النحر", "translit": "an-naḥr", "fr": "l’immolation de la bête — l’œuvre centrale du jour ; elle commande le rasage (n° 1173) et retient la délivrance de Ḥafṣa (n° 1169)"},
        {"ar": "التحلل", "translit": "at-taḥallul", "fr": "la délivrance de la sacralisation — à deux degrés : moindre par le jet, majeure par le ṭawāf de l’Ifāḍa (n° 1226)"},
        {"ar": "التفث", "translit": "at-tafath", "fr": "la souillure de l’iḥrām — cheveux, vêtements, ongles, souillures : l’ensemble que la glose nomme le rejet de la souillure (ilqāʾ at-tafath)"},
        {"ar": "التلبيد", "translit": "at-talbīd", "fr": "le feutrage — la gomme appliquée aux cheveux pour les agglomérer ; le geste de Ḥafṣa, dont la règle impose le rasage entier (n° 1186)"},
        {"ar": "الافاضة", "translit": "al-ifāḍa", "fr": "le ṭawāf de l’Ifāḍa — la quatrième œuvre du jour et la fin de la délivrance : sans lui, femmes et parfum demeurent interdits"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}

E_407 = {
    "auteur": "IA-1, tour R722",
    "resume": "Guide de lecture de la leçon 18 (أحكام الهدي 2) : la bête d’offrande exposée au péril de la route — périe ou égarée, elle se règle selon la nature de l’offrande — et la grande question du pèlerinage manqué : la ʿumra complète délivre, le pèlerinage réparé attend l’année suivante ; puis la casuistique des rapports conjugaux découpe le pèlerinage en trois zones.",
    "explication": [
        "La page d’ouverture (p.124) fixe deux objectifs : reconnaître le statut de celui dont le pèlerinage a été manqué et la manière dont il se délivre de son iḥrām, et reconnaître les règles de la bête d’offrande qui périt avant d’atteindre son lieu. Le tamhīd relit la bête d’offrande dans ses destinations : rite accompli en recherche de la proximité d’Allah, en conformité à Son ordre, en gratitude pour l’achèvement du rite, en honneur aux hôtes du Miséricordieux et en largesse aux pauvres de La Mecque — la āya d’al-Ḥajj (imprimée « l’āya 26 », cache 22 :28) fixe la double destination : « mangez de ces bêtes et nourrissez-en le misérable indigent ». Puis la bête en réparation (jabr) — obligation abandonnée, raffinement du tamattuʿ et du qirān, interdits violés — et enfin la bête exposée au péril de la route : les deux questions d’ouverture.",
        "Les deux textes posent les deux moitiés du cours. Le premier (n° 1121) règle la bête périte : le gardien des bêtes d’offrande du Prophète ﷺ demande « que fais-je de ce qui a péri des bêtes d’offrande ? » — réponse : « immole-la, puis jette son collier dans son sang, puis laisse entre elle et les gens, qu’ils en mangent » : la perte même devient aumône. La glose fixe le seuil du ʿaṭb : non la simple blessure, mais l’atteinte invalidante qui empêche de marcher et dont on craint qu’elle ne fasse périr. Le second (n° 1135) est la matrice de la seconde section : Ḥibbār b. al-Aswad arrive devant ʿUmar le jour de l’Immolation — « nous nous sommes trompés dans le compte : nous tenions ce jour pour le jour de ʿArafa » — et l’ordre déroule le protocole complet de la délivrance : ṭawāf à La Mecque, immolation de l’offrande déjà présentée, rasage ou raccourcissement, retour ; puis le pèlerinage l’année suivante avec l’offrande, ou le jeûne — trois jours dans le pèlerinage, sept une fois rentré — pour qui ne trouve pas. La notice de Sulaymān b. Yasār — le Hachémite de Médine, client de Maymūna (selon d’autres, d’Umm Salama), l’un des sept fuqahāʾ de Médine, mort en 104 — donne au rapport son autorité.",
        "La première section règle la bête. Périe : on l’immole obligatoirement, que l’offrande soit d’obligation ou surérogatoire ; mais le propriétaire et les gens de sa caravane n’en mangent pas si elle était surérogatoire — fermeture de la porte du relâchement dans son immolation avant l’heure — et rien ne lui incombe (n° 1122 : celui qui en a mangé ou en a fait manger compense, gharam) ; l’offrande d’obligation, garantie car rattachée à la charge (dhimma), se remplace (n° 1124, Ibn Chihāb : compensation, vœu ou tamattuʿ frappé en route — le remplacement incombe), et dès lors sa chair s’ouvre au propriétaire et aux gens aisés. Égarée ou morte : la même ligne de partage (n° 1125, Ibn ʿUmar : le vœu se remplace, la surérogatoire laisse l’option) ; la distinction avec le ʿaṭb tient au geste — la bête périe se donne aux mangeurs sur place, l’égarée ne se retrouve pas.",
        "La seconde section règle l’homme. Le pèlerinage manqué sans rapports conjugaux — montures perdues, erreur de compte, maladie, incertitude du croissant, empêchement — se délivre par une ʿumra complète : le ḥajj se refait l’année suivante avec l’offrande, ou le jeûne de trois et sept pour qui ne trouve pas ; l’athar d’Abū Ayyūb al-Anṣārī (n° 1134, les montures perdues à an-Nāziyya sur la route, présenté à ʿUmar : « fais ce que fait celui qui accomplit la ʿumra ; tu es à présent délivré ») et le rapport de Ḥibbār (n° 1135) fondent la règle sur la pratique califale ; le qārin refait pareillement son couplage avec une bête (n° 1136). Par les rapports conjugaux, trois zones : avant le jet de la Jamra — le pèlerinage est corrompu à deux, ils l’achèvent puis le réparent, une bête à chacun (n° 1128, la fatwā de Saʿīd b. al-Musayyib : mener à terme le dessein, l’iḥrām repris du point d’origine) ; entre le départ de ʿArafa et le jet — la bête et le pèlerinage de l’année suivante (n° 1129) ; après le jet et avant le ṭawāf de l’Ifāḍa — le pèlerinage tient, l’acte tombant après la première délivrance, et la déficience se répare par la ʿumra devenue obligatoire et la bête (n° 1138 — la parole qu’Ibn ʿAbbās rend célèbre, celle que Mālik a le plus aimé entendre, n° 1139).",
        "La conclusion relit tout le cours comme une pédagogie du renoncement : la bête abandonnée aux pauvres, le pèlerinage refait, la ʿumra qui répare l’élan fautif — l’école du détachement provisoire en quête de l’agrément d’Allah. L’exploitation clôt par la fatwā de l’oubli du ṭawāf de l’Ifāḍa (n° 1140) — retourner et faire l’Ifāḍa, avec la ʿumra et la bête si les femmes ont été approchées — et deux exercices à preuve : la bête périte (l’imprimé porte « du pèlerinage » : coquille consignée), puis le cas du car maghrébin en panne après le mīqāt, arrivé au matin du jour de l’Immolation : la règle du manqué s’applique mot pour mot. La préparation annonce la leçon 19 : les gloses du rejet de la souillure et du feutrage, et le temps de la délivrance.",
    ],
    "points": [
        "Fil de révision : deux objectifs → deux questions du tamhīd → deux textes (la bête périte ; le pèlerinage manqué par erreur de compte) → deux sections (la bête ; l’homme) → deux exercices à preuve.",
        "La bête périte s’immole sur place : « immole-la, jette son collier dans son sang, laisse entre elle et les gens qu’ils en mangent » (n° 1121) — la perte devient aumône ; le seuil du ʿaṭb : l’atteinte invalidante, non la simple blessure.",
        "Le partage décisif : l’offrande surérogatoire se donne aux mangeurs, rien n’incombe (n° 1122) ; l’offrande d’obligation est garantie — rattachée à la charge — le remplacement s’impose (n° 1124), et sa chair s’ouvre au propriétaire et aux gens aisés.",
        "Égarée ou morte : le vœu se remplace, la surérogatoire laisse l’option (n° 1125) — la même ligne de partage que la bête périte, sans le geste de l’immolation.",
        "Le pèlerinage manqué sans rapports : ʿumra complète de délivrance, ḥajj l’année suivante avec l’offrande, ou jeûne de trois et sept (n° 1134, n° 1135) ; le qārin refait couplage et bête (n° 1136).",
        "Les rapports conjugaux en trois zones : avant le jet — pèlerinage corrompu, achevé puis réparé, une bête chacun (n° 1128) ; entre jet et Ifāḍa — le ḥajj tient, la ʿumra et la bête réparent (n° 1129, n° 1138) ; après l’Ifāḍa — hors du rite.",
    ],
    "vocabulaire": [
        {"ar": "الهدي", "translit": "al-hady", "fr": "la bête d’offrande — rite du pèlerinage : gratitude pour l’achèvement, honneur aux hôtes du Miséricordieux, largesse aux pauvres de La Mecque, et réparation des déficiences"},
        {"ar": "العطب", "translit": "al-ʿaṭb", "fr": "le péril de la bête — l’atteinte invalidante qui empêche de marcher et menace de mort : le seuil qui déclenche l’immolation immédiate"},
        {"ar": "فوات الحج", "translit": "fawāt al-ḥajj", "fr": "le pèlerinage manqué — montures perdues, erreur de compte, maladie, croissant incertain, empêchement : la ʿumra complète délivre"},
        {"ar": "الجبر", "translit": "al-jabr", "fr": "la réparation — la bête qui couvre l’obligation abandonnée, le tamattuʿ et le qirān, les interdits violés, et le pèlerinage corrompu"},
        {"ar": "الضالة", "translit": "aḍ-ḍiyāʾ", "fr": "la bête égarée — le vœu se remplace, la surérogatoire laisse l’option (n° 1125) ; sans le geste de l’immolation sur place"},
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
for docid, entree in (('pdf-mut23h2x-408', E_408), ('pdf-mut23h2x-407', E_407)):
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
for docid in ('pdf-mut23h2x-408', 'pdf-mut23h2x-407'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        # l’arabe entre parenthèses (titres du manuel) est échappé au build
        # en balises RTL (LISEZ-MOI.md §3.3) — hors parenthèses : 0 arabe
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t).replace('ﷺ', '')
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
