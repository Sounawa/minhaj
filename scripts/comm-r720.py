#!/usr/bin/env python3
"""R720 — ajoute les commentaires pédagogiques des leçons 23 (pdf-mut23h2x-412,
la ʿumra) et 22 (pdf-mut23h2x-411, la fidya) à content/commentaires/hadith-3es.json.
Même protocole que comm-r718.py / comm-r719.py : normalisation de la ponctuation
FR (U+202F avant ; : ! ? » et après «, apostrophe courbée) sur les entrées
nouvelles seulement — opération idempotente. Les translittérations reprennent
les formes exactes du texte des leçons (règle 4 de LISEZ-MOI.md)."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_412 = {
    "auteur": "IA-1, tour R720",
    "resume": "Guide de lecture de la leçon 23 (أحكام العمرة) : le statut posé sunna confirmée, la précellence tenue dans l’expiation de l’intervalle et dans ramaḍān, le miqāt réglé par la résidence, et le compte serré des trois ʿumra du Prophète ﷺ — quatre textes et deux sections pour la carte complète du petit pèlerinage.",
    "explication": [
        "La page d’ouverture (p.153) fixe trois objectifs : reconnaître les règles de la ʿumra, reconnaître la ʿumra du Prophète ﷺ, saisir sa précellence et son rang dans l’islam. Le tamhīd les ouvre par la définition : la ʿumra est la visite de la Maison d’Allah le Sacrée selon une manière particulière — adoration pour Allah et magnification de la Maison antique — et une mise en valeur de lui ; le rattachement à l’āya (quiconque magnifie les symboles d’Allah, elles proviennent de la piété des cœurs) fait du voyage un acte de vénération ordonné par la parole d’Allah, non un usage pieux privatif. Les deux questions d’ouverture — les règles, la précellence — donnent les deux moitiés du cours.",
        "Les quatre textes font chacun un travail précis. La sentence d’ʿumar b. al-khaṭṭāb (n° 991) — séparez entre vos ḥaǧǧ et vos ʿumra, la ʿumra hors des mois du ḥaǧǧ plus parfaite pour l’un et pour l’autre — fonde la séparation des sacralisations : point d’iḥrām unique pour les deux rites. La femme préparée pour le ḥaǧǧ (n° 990) reçoit le remède converti : fais ta ʿumra en ramaḍān, car une ʿumra en lui vaut un ḥaǧǧ — la précellence posée sur un cas concret, non sur une abstraction. Mālik interrogé (n° 979) fixe le terme de la talbiya : à l’arrivée au ḥaram, la voie d’ʿabd Allāh b. ʿumar. Le compte (n° 974) clôt la série : trois ʿumra — une en chawwāl, deux en dhū l-qaʿda. La notice d’abū bakr b. ʿabd ar-raḥmān (l’un des sept juristes de Médine, le moine de Quraych pour l’abondance de sa prière, aveugle d’un œil, mort l’an 93 ou 94) scelle la voie du second texte.",
        "La première grande section pose le statut à trois étages : la réponse au bédouin (non, et que tu fasses la ʿumra, cela est meilleur pour toi — ḥasan ṣaḥīḥ chez at-tirmidhī), le hadith des cinq piliers qui mentionne le ḥaǧǧ sans la ʿumra, et la parole de Mālik (n° 993) — aucun musulman ne la voit un gâchis dans son abandon. La précellence est double : l’expiation de l’intervalle (n° 989) — bornée aux péchés mineurs et au temps, le hadith sorti comme encouragement à multiplier ; et la ʿumra de ramaḍān — la multiplication des bonnes actions y élève la récompense jusqu’au niveau du ḥaǧǧ. La répétition dans l’année oppose deux voies sans trancher : détestée chez Mālik (n° 994 — le Prophète ﷺ n’en faisait qu’une par an alors qu’il pouvait la répéter), permise chez le général des juristes et beaucoup de Mālikites — l’argument étant l’expiation même. Le miqāt règle la sacralisation par la résidence : celui du ḥaǧǧ pour l’étranger ; le résident de la Mecque sort vers un lieu du ḥill — l’iḥrām combine ḥill et ḥurm —, la sunna étant at-tanʿīm et la précellence aux sites plus lointains, al-jiʿrāna et al-ḥudaybiya (n° 997 : cela suffit, le préféré reste le miqāt fixé par le Prophète ﷺ).",
        "La seconde section compte et date : trois ʿumra sur le saḥīḥ chez Mālik — al-ḥudaybiya (l’an de l’arrêt), al-qaḍiyya (l’an de l’exécution du ḥaǧǧ ajourné), al-jiʿrāna (l’an du butin de ḥunayn) — et quatre chez anas pour qui la conjonction du ḥaǧǧ compte ; les temps suivent : dhū l-qaʿda pour les deux premières, la qaḍiyya divergente (chawwāl soutenu par le n° 974). La ʿumra avant le ḥaǧǧ est permise par consensus (n° 975 — la réponse de Saʿīd b. al-musayyib : oui, il a fait la ʿumra avant de faire le ḥaǧǧ). L’évaluation teste le statut avec l’argument, les péchés que la ʿumra expie, et le nom d’ʿumrat al-qaḍiyya — elle a exécuté le rite retenu par le traité. L’exploitation (n° 976) porte le contre-éclairage : ʿumar b. abī salama autorisé pour une ʿumra de chawwāl, puis retour à sa famille sans ḥaǧǧ — la ʿumra seule dans les mois du ḥaǧǧ est permise ; l’invite renvoie au Charḥ az-Zarqānī. La préparation ouvre le chapitre suivant : l’aḍḥiyya."
    ],
    "points": [
        "Fil de révision : trois objectifs → deux questions du tamhīd → deux grandes sections (les règles : statut, précellence, répétition, miqāt ; les ʿumra du Prophète ﷺ : nombre, temps, avant le ḥaǧǧ) → trois questions d’évaluation sur le même fil.",
        "Statut : sunna confirmée, fondée à trois étages — la réponse au bédouin (non, et meilleur pour toi), les cinq piliers qui mentionnent le ḥaǧǧ sans la ʿumra, la parole de Mālik (aucun gâchis dans son abandon).",
        "Précellence : l’expiation de l’intervalle — péchés mineurs sans les majeurs, bornée au temps, le hadith d’encouragement ; et ramaḍān — la multiplication des bonnes actions y égalise ʿumra et ḥaǧǧ.",
        "Répétition : détestée chez Mālik (une seule par an malgré le pouvoir de répéter) ; permise chez le général des juristes et beaucoup de Mālikites — l’argument est le hadith de l’expiation ; le cours pose les deux voies sans trancher.",
        "Miqāt : celui du ḥaǧǧ pour l’étranger ; le résident sort vers un lieu du ḥill (l’iḥrām combine ḥill et ḥurm) — at-tanʿīm la sunna, al-jiʿrāna et al-ḥudaybiya le préféré.",
        "Les trois ʿumra (al-ḥudaybiya, al-qaḍiyya, al-jiʿrāna) — quatre chez anas ; le nom d’ʿumrat al-qaḍiyya porte l’exécution du devoir ajourné par le traité d’al-ḥudaybiya ; la ʿumra avant le ḥaǧǧ : consensus, attesté par le fait du Prophète ﷺ."
    ],
    "vocabulaire": [
        {"ar": "الْعُمْرَة", "translit": "al-ʿumra", "fr": "le petit pèlerinage — la visite de la Maison selon une manière particulière : iḥrām, tawāf, saʿy, coupe"},
        {"ar": "سُنَّة مُؤَكَّدَة", "translit": "sunna muʾakkada", "fr": "la sunna confirmée — le statut posé pour la ʿumra par les trois arguments du cours"},
        {"ar": "التَّلْبِيَة", "translit": "at-talbiya", "fr": "la formule de consécration répétée — coupée à l’arrivée au ḥaram (n° 979)"},
        {"ar": "التَّنْعِيم", "translit": "at-tanʿīm", "fr": "la mosquée hors du ḥaram — le miqāt de la ʿumra du résident, sanctifié par la consécration du Prophète ﷺ"},
        {"ar": "الْجِعْرَانَة", "translit": "al-jiʿrāna", "fr": "le site de la troisième ʿumra du Prophète ﷺ — plus loin que at-tanʿīm, avec al-ḥudaybiya"},
        {"ar": "عُمْرَة الْقَضِيَّة", "translit": "ʿumrat al-qaḍiyya", "fr": "la ʿumra de l’exécution — elle a exécuté le ḥaǧǧ et la ʿumra suspendus l’an 6 par le traité"},
        {"ar": "الْمُهِلّ", "translit": "al-muhill", "fr": "celui qui est revêtu de l’état de sacralisation — sa talbiya cesse au ḥaram"}
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi."
}

E_411 = {
    "auteur": "IA-1, tour R720",
    "resume": "Guide de lecture de la leçon 22 (من أحكام الفدية) : deux régimes de la fidya du rasage de la tête — pour excuse et sans excuse — et la règle de l’association au gibier : chacun porte sa compensation entière, car la kaffāra ne se partage pas.",
    "explication": [
        "La page d’ouverture (p.147) fixe trois objectifs : reconnaître ce qui s’impose au sacralisé qui a tué un locuste ou rasé sa tête, distinguer ce qui s’impose dans le rasage et dans le tuage du locuste, et s’imprégner des sens tirés de l’interdiction de tuer les animaux dans le ḥaram. Le tamhīd partage les interdits du sacralisé en deux masses — ce qui se rattache à sa personne (raser la tête, couper les ongles) et ce qui se rattache à son entourage (tuer les animaux) —, et les deux questions d’ouverture prennent les deux lames restées : la tête et l’association des mains. La leçon complète ainsi le chapitre de la fidya ouvert à la précédente.",
        "Les deux textes portent chacune des deux questions. Le premier (n° 1252) donne la scène de Kaʿb b. ʿUǧra : le Prophète ﷺ devine le mal — peut-être tes bêtes rampantes t’ont-elles nui ? — et fixe la table de la compensation : rase ta tête, et jeûne trois jours, ou nourris six pauvres, ou immole une brebis. Le second (n° 1263) pose la règle du groupe qui atteint le gibier ensemble : chacun porte sa pleine compensation — à l’image du tuage fautif de l’homme, chaque participant portant l’affranchissement d’un esclave ou le jeûne de deux mois consécutifs. La notice de Kaʿb b. ʿUǧra (l’Auxiliaire de Médine, mort l’an 51) scelle la voie du premier texte ; les gloses résoluent an-suk bi-chaʾa (immole une brebis par laquelle tu te rapproches d’Allah) et qabḍa (la poignée — la vocalisation fixée : fatha sur le qāf).",
        "La première grande section déplie la fidya du rasage. Le rasage recouvre trois manières — le rasoir, les ciseaux, l’arrachement — et le n° 1255 interdit toute atteinte au cheveu avant la libération, sauf l’atteinte de la tête. Pour excuse, le choix triple est fondé sur l’āya d’al-Baqara et précisé par la mesure de l’assiette (n° 1251 — deux mud par pauvre) ; l’herméneutique vient des deux authentiques : l’āya descendue pour un cas particulier vaut pour vous en général — la voie de Mālik : la considération vaut à la généralité du terme, non à la spécificité de la cause. Sans excuse, tous posent la fidya et divergent sur le choix : Mālik le laisse entier (vil est ce qu’il a fait, et la fidya s’impose, et il est donné au choix dans elle), abū ḥanīfa et ach-chāfiʾī le resserrent à la nécessité — l’argument de Mālik (Ibn Baṭṭāl) : la Sunna venue pour la nécessité aurait distingué le contraire, et l’a fortiori achève. Le n° 1256 généralise : le cheveu du nez et de l’aisselle, la pâte dépilatoire, la plaie rasée par nécessité, la nuque rasée au lieu d’un jeûneur — et l’oubli n’excuse pas la compensation, il n’excuse que le péché.",
        "La seconde section tient la règle de l’association : la kaffāra ne se partage pas — chaque main porte la compensation entière, comme si elle avait tué seule, et le choix reste ouvert à chaque participant. Le jugement exige deux équitables, savants du statut, doués de la perspicacité qui distingue les choses les plus ressemblantes — l’assemblée commune recommandée pour la vérification ; le modèle est documenté dans le cours même : ʿumar s’aidant de ʿabd ar-raḥmān b. ʿawf pour l’antilope (n° 1241), l’étonnement du questionneur et la leçon d’ʿumar — lis-tu la sourate al-Māʾida ? — l’āya exige des équitables au pluriel. L’évaluation reprend les deux sections ; l’exploitation (n° 1253) ouvre la question du recueillement : Kaʿb à sa marmite, la tête pleine de poux, et le Prophète ﷺ savait qu’il n’avait pas de quoi immoler — le sacrifice est offert à qui en a la mesure, retiré au pauvre. La préparation ouvre le chapitre de la ʿumra (la leçon 23)."
    ],
    "points": [
        "Fil de révision : trois objectifs → deux questions du tamhīd → deux sections (la fidya du rasage ; l’association au gibier) → deux questions d’évaluation sur le même fil.",
        "Le rasage recouvre le rasoir, les ciseaux et l’arrachement — nulle atteinte au cheveu avant la libération, sauf l’atteinte de la tête (n° 1255).",
        "Pour excuse : le choix triple (jeûner trois jours, nourrir six pauvres, immoler une brebis) ; l’assiette fixée à deux mud par pauvre (n° 1251) ; l’āya du cas vaut en général — la généralité du terme, non la spécificité de la cause.",
        "Sans excuse : la fidya s’impose chez tous ; le choix entier chez Mālik, resserré à la nécessité chez abū ḥanīfa et ach-chāfiʾī — le silence de la Sunna étend, l’a fortiori achève (Ibn Baṭṭāl).",
        "Généralisation (n° 1256) : nez, aisselle, nūra, plaie, nuque du jeûneur — l’oubli n’excuse que le péché, jamais la compensation.",
        "Association : la kaffāra ne se partage pas — chacun entier comme s’il avait tué seul ; deux juges équitables et savants (ʿumar et ʿabd ar-raḥmān b. ʿawf, n° 1241) ; la table de compensation s’adapte à la fortune — le sacrifice retiré au pauvre (n° 1253)."
    ],
    "vocabulaire": [
        {"ar": "الْفِدْيَة", "translit": "al-fidya", "fr": "la compensation — ce qui remplace le rite atteint, par jeûne, aumône ou sacrifice"},
        {"ar": "الْحَوَام", "translit": "al-ḥawām", "fr": "les bêtes rampantes — les poux qui nient la tête de Kaʿb b. ʿUǧra"},
        {"ar": "أَنْسُك", "translit": "ansuk", "fr": "immole — par laquelle tu te rapproches d’Allah, la glose du manuel"},
        {"ar": "قَبْضَة", "translit": "qabḍa", "fr": "la poignée — la mesure la plus basse de l’échelle de la fidya (fatha sur le qāf)"},
        {"ar": "النُّورَة", "translit": "an-nūra", "fr": "la pâte dépilatoire — les mélanges d’arsenic employés pour enlever le cheveu"},
        {"ar": "الْكَفَّارَة", "translit": "al-kaffāra", "fr": "l’expiation — elle ne se partage pas entre les mains associées"},
        {"ar": "مُدّ", "translit": "mudd", "fr": "la mesure de grain — deux mud par pauvre, la répétition portant la généralité"}
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi."
}


def norme_fr(s):
    """Ponctuation FR : U+202F avant ; : ! ? » et après « ; apostrophe ’."""
    s = s.replace("'", "’")
    for p in (';', ':', '!', '?', '»'):
        s = re.sub(r' ' + re.escape(p), '\u202f' + p, s)
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
for docid, entree in (('pdf-mut23h2x-412', E_412), ('pdf-mut23h2x-411', E_411)):
    if docid in com:
        print(f'!! {docid} déjà présent — rien de fait')
        raise SystemExit(1)
    com[docid] = norme_entree(entree)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume + ponctuation FR
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
mauvais = 0
for docid in ('pdf-mut23h2x-412', 'pdf-mut23h2x-411'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']]
    for t in textes:
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
print('contrôle ponctuation FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
