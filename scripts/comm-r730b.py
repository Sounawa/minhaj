#!/usr/bin/env python3
"""R730 — ajoute le commentaire pédagogique de la leçon 2 (pdf-mut23h2x-391,
لباس المحرم — le vêtement du pèlerin en état d'iḥrām) à
content/commentaires/hadith-3es.json.
Vague 14 (deuxième livraison) : remontée hadith-3es (le SUIVANT de R729-b,
slot précisé). Même protocole que comm-r730.py (leçon 3) et comm-r729.py :
normalisation de la ponctuation FR (U+202F avant ; : ! ? » et après «,
apostrophe courbée) sur l'entrée nouvelle seulement — opération idempotente.
Rédaction d'après la lecture complète de la leçon (htmlFr intégral,
36 644 caractères, extraction non lossy). Les numéros du Muwaṭṭaʾ et les
formules sont cités tels qu'ils figurent dans la leçon (règle 2 de
LISEZ-MOI.md : aucune invention). Les formes arabes du vocabulaire sont
posées au squelette standard SANS harakat (situation des vagues 5-13 : les
gloses de ces leçons sont rendues en translittération dans la couche FR) ;
aucune harakat n'est inventée (règle 2). Les ʿ et ʾ (U+02BF / U+02BE) sont
posés directement dans les champs FR — la normalisation ne les touche pas."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_391 = {
    "auteur": "IA-1, tour R730",
    "resume": "Guide de lecture de la leçon 2 (لباس المحرم) : un seul hadith-matrice (n° 909) énumère les cinq cousus interdits au pèlerin — la chemise, les turbans, les pantalons, les capes à capuchon, les bottines — ménage l'exception des bottines coupées sous les chevilles pour qui ne trouve pas de sandales, et clôt sur les teintures : « ne portez, des vêtements, rien qu'ait touché le safran ou le wars ». Le fiqh déploie ensuite trois chapitres qui répondent aux trois questions d'ouverture : les sortes de vêtements interdits, avec la règle générale — le Prophète a visé par chaque nom le cousu façonné aux dimensions du corps ou d'un membre ; le statut des vêtements teints et parfumés, étendu à leur genre et au semblant de teinture ; la ceinture et la couverture du visage, où l'école harmonise les deux voies d'Ibn ʿUmar — la répulsion du port apparent, la permission du port dissimulé — et tient le mashhūr : le visage couvert engage l'offrande expiatoire, la tête couverte est interdite par unanimité. La leçon clôt sur le sort du pèlerin décédé (couvert et parfumable, car son œuvre s'achève), la sagesse du décret — l'épreuve par la sortie de l'habit accoutumé, l'égalité proclamée par l'unité du vêtement — et l'exploitation du voile et des gants de la pèlerine.",
    "explication": [
        "La page d'ouverture (p.17) pose trois objectifs : faire connaître ce qu'il n'est pas permis au pèlerin en état de sacralisation de porter, saisir la sagesse de l'interdiction de certains vêtements, et mettre en pratique les règles du vêtement au moment de la sacralisation pour le pèlerinage ou la 'umra. Le tamhīd enracine le tout dans les visées de la Loi : réaliser le dépouillement sensible et spirituel du pèlerin, l'éloignement du superflu et des jouissances du monde, et l'unité des musulmans dans le vêtement — dans l'espoir de l'unité des cœurs. Les trois questions d'ouverture (quelles sortes de vêtements la Loi interdit-elle au pèlerin ? quel en est le dessein ? quel est le statut de la couverture de la tête et de la ceinture ?) donnent au fiqh son plan en trois chapitres, et le bloc de synthèse (istikhlāṣ al-maḍāmīn) les ramasse en trois items : le vêtement interdit, le statut des vêtements teints, la ceinture et le voile de tête.",
        "Les trois textes d'armature. Le n° 909 est la matrice : à la question de l'homme — que peut porter le pèlerin comme vêtements ? — le Messager de Dieu répond « ne portez pas la chemise, ni les turbans, ni les pantalons, ni les capes à capuchon, ni les bottines — sauf celui qui ne trouve pas de sandales : qu'il porte alors des bottines et qu'il les coupe en dessous des chevilles ; et ne portez, des vêtements, rien qu'ait touché le safran ou le wars » : cinq catégories, une exception, et l'ouverture du chapitre des teintures. Le n° 915 porte tout le troisième chapitre en une ligne : ʿAbd Allāh b. ʿUmar réprouvait le port de la ceinture par le pèlerin — la répulsion (karāha) plutôt que l'interdiction franche, et la matière de l'harmonisation avec la permission aussi rapportée de lui. Le n° 918 fixe la formule du visage : « ce qui, de la tête, est au-dessus du menton, le pèlerin en état de sacralisation ne le couvre pas » — le visage défini par son rebord inférieur, et l'interdiction de le couvrir.",
        "Premier chapitre : les sortes interdites, derrière la règle générale du cousu (makhīṭ) façonné aux dimensions du corps. La chemise vise tout cousu porté sur l'emplacement qui lui est dévolu ; la variante du verbe (khabar valant injonction ou jazm) est l'occasion d'une règle des fondements : la forme informative peut valoir injonction. Les turbans et les capes visent tout ce qui couvre la tête — al-Khaṭṭābī : « ni par l'habituel ni par l'inusité », jusqu'au panier (maktal) ; Ibn Ḥajar nuance : la simple pose sur la tête, sans port réel, ne nuit pas, comme l'immersion dans l'eau — et l'interdiction est propre à l'homme par unanimité : la femme porte tout ce qui a été mentionné (Ibn al-Mundhir). Le pantalon vise le cousu façonné aux dimensions d'un membre (le pagne court tabbān, les gants) ; Mālik refuse d'étendre l'exception des bottines au pantalon (n° 910 : « je n'ai pas entendu cela »), et l'école harmonise le hadith d'Ibn ʿAbbās avec celui d'Ibn ʿUmar : découdre le pantalon en pagne est permis, et la nécessité de couvrir la nudité autorise le port tel quel — avec l'offrande expiatoire (fiḍya) selon Mālik et Abū Ḥanīfa, comme pour la tête contrainte : on couvre et l'on expie. Les bottines visent tout ce qui chausse (la chaussette, jawrab) ; le manuel relève la différence de régime entre bottines et chaussettes dans l'ablution : la cause efficiente — la couverture intégrale du membre — existe au complet dans les chaussettes, mais l'essuyage est une dispense (rukhsa) et la dispense ne déborde pas son lieu d'application.",
        "Deuxième chapitre : les teints et parfums. L'interdiction des vêtements touchés par le safran ou le wars (n° 909 repris, n° 911) est étendue à leur genre ; Ibn al-ʿArabī précise : « le wars n'est pas un parfum, mais le Prophète l'a mentionné pour avertir d'éviter le parfum et ce qui lui ressemble en agrément pour l'odorat » — d'où l'interdiction des sortes de parfums au pèlerin, où porte le consensus, et l'extension aux femmes : la règle contredit ce qu'exige l'adoration du pèlerinage — humilité, soumission et dépouillement des jouissances du monde et de sa parure. Le vêtement qui ressemble à la teinture est réprouvé par la scène dʿUmar et de Ṭalḥa (n° 912) : le vêtement teint en rouge sombre (muḍabbaʾ) n'était pas illicite en soi — ʿUmar a réprouvé pour qu'un ignorant ne l'imite pas en s'imaginant la permission du wars et du safran, les gens prenant les imams pour modèles. Quant au rapport d'Asmāʾ (n° 913, vêtements teints à la garance, teints à fond), il s'entend des teintures qui ne s'effritent pas (Ibn Ḥabīb d'après Mālik) ; si la teinture s'effrite, le port est réprouvé pour les hommes et les femmes — ce qui s'en détache ressemble au parfum.",
        "Troisième chapitre : la ceinture et le visage. Pour la ceinture, l'école harmonise les deux voies d'Ibn ʿUmar : la répulsion (n° 915) et la permission aussi rapportée de lui — l'avis de répulsion vaut tant que la ceinture se porte apparente ; portée sous les vêtements, nouée et dissimulée, les deux bouts en lanières (siyūr) selon Saʿīd b. al-Musayyab (n° 916 — « c'est là ce que j'ai le mieux aimé entendre », dit Mālik), elle est permise ; Ibn ʿAbd al-Barr conclut que la répulsion n'a été rapportée que d'Ibn ʿUmar, de qui la permission fut aussi rapportée. Pour le visage, le mashhūr de l'école interdit de le couvrir, avec offrande expiatoire — la tête, elle, ne se couvre pas par unanimité ; les rapports contraires (ʿUthmān vu couvrant son visage, n° 917) sont désapprouvés par Mālik. Le sort du pèlerin décédé tranche le cas limite : Ibn ʿUmar enveloppa son fils Wāqid mort en sacralisation à al-Juḥfa, couvrit sa tête et son visage et dit « si nous n'étions pas en sacralisation, nous l'aurions parfumé » (n° 919) — expliqué par la parole de Mālik « l'homme n'œuvre que tant qu'il vit ; lorsqu'il meurt, son œuvre s'achève » (n° 920) ; le hadith des Deux Ṣaḥīḥ (l'homme tué par sa chamelle : ne couvrez pas sa tête et ne lui approchez pas le parfum, car il sera ressuscité disant labbayk) est un cas particulier motivé — le jugement lui est propre, car la motivation ne se réalise pour personne d'autre que cet homme.",
        "La conclusion de la leçon donne la sagesse d'ensemble : l'adoration du pèlerinage a un vêtement qui lui est propre, conforme à ses visées — l'épreuve de l'homme par la sortie de l'habit accoutumé —, et l'unité du vêtement du pèlerinage proclame l'égalité entre les gens, fussent-ils de lignées différentes. L'évaluation retourne aux items en trois questions : citer les vêtements interdits en précisant le dessein de l'interdiction ; exposer comment les Mālikites ont harmonisé les deux voies sur le statut de la couverture du visage ; trancher deux situations imprimées avec preuve et motivation — la femme consacrée qui porte des vêtements parfumés, et l'homme consacré qui porte une ceinture où il a mis son argent. L'exploitation ouvre le cas de la pèlerine : « que la femme en état de sacralisation ne se voile pas le visage et ne porte pas les gants » (n° 921), avec le récit de Fāṭima bint al-Mundir auprès d'Asmāʾ (n° 922) — deux consignes : consulter az-Zarqānī sur le texte, puis tirer la règle du voile du visage et du port des gants en exposant le mode d'inférence. La préparation préalable annonce la leçon 3 sur le parfum du pèlerin, déjà livrée au registre.",
    ],
    "points": [
        "Fil de révision : trois objectifs (ce qu'il n'est pas permis de porter ; la sagesse de l'interdiction ; la mise en pratique) → tamhīd (dépouillement sensible et spirituel ; unité des musulmans dans le vêtement, espoir de l'unité des cœurs) → trois textes (n° 909, 915, 918) → notice d'Ibn ʿUmar (renvoi) → cinq gloses → fiqh en trois chapitres → conclusion (vêtement propre, égalité) → évaluation en trois items → exploitation du voile et des gants de la pèlerine (n° 921, 922).",
        "Le hadith-matrice (n° 909) : cinq cousus interdits — chemise, turbans, pantalons, capes à capuchon, bottines —, l'exception des bottines coupées sous les chevilles pour qui ne trouve pas de sandales, et l'interdiction des teintures de safran et de wars ; règle générale : le cousu façonné aux dimensions du corps ou d'un membre.",
        "Turbans et capes : tout ce qui couvre la tête, « ni par l'habituel ni par l'inusité » (al-Khaṭṭābī, jusqu'au maktal) ; la simple pose sur la tête ne nuit pas selon Ibn Ḥajar ; l'interdiction est propre à l'homme par unanimité — la femme porte tout ce qui a été mentionné (Ibn al-Mundhir).",
        "Le pantalon : Mālik refuse d'étendre l'exception (n° 910 — « je n'ai pas entendu cela ») ; deux harmonisations avec le hadith d'Ibn ʿAbbās : découdre le pantalon en pagne (permis), ou la nécessité de couvrir la nudité — couvrir et expier, l'offrande due selon Mālik et Abū Ḥanīfa, comme pour la tête contrainte.",
        "Teintures et semblants : safran et wars interdits et leur genre (n° 911) — le wars n'est pas un parfum mais avertit d'éviter le parfum (Ibn al-ʿArabī) ; le semblant de teinture réprouvé pour ne pas induire l'ignorant en tentation (n° 912, Ṭalḥa) ; la teinture qui ne s'effrite pas permise (n° 913, Asmāʾ), celle qui s'effrite réprouvée hommes et femmes — ce qui s'en détache ressemble au parfum.",
        "Ceinture et visage : les deux voies d'Ibn ʿUmar harmonisées — répulsion du port apparent, permission du port dissimulé et noué en lanières (n° 916) ; le mashhūr interdit de couvrir le visage avec offrande expiatoire, la tête par unanimité ; le pèlerin décédé est couvert et parfumable — son œuvre s'achève (n° 919-920) —, le hadith de la chamelle des Deux Ṣaḥīḥ étant un cas particulier motivé.",
    ],
    "vocabulaire": [
        {"ar": "لباس المحرم", "translit": "libās al-muḥrim", "fr": "le vêtement du pèlerin en état de sacralisation — la leçon en fixe les interdits, l'exception des bottines coupées et la sagesse : dépouillement, épreuve de l'habit accoutumé, unité et égalité"},
        {"ar": "العمائم", "translit": "al-ʿamāʾim", "fr": "les turbans, pluriel de ʿimāma — du verbe « envelopper » (taʿummū) : tout ce qui enveloppe la tête est visé par l'interdit, habituel ou inusité"},
        {"ar": "السراويلات", "translit": "as-sarāwīlāt", "fr": "les pantalons, pluriel de sirwāl, mot persan arabisé — le cousu façonné aux dimensions d'un membre, comme le pagne court (tabbān) et les gants"},
        {"ar": "البرانس", "translit": "al-barānīs", "fr": "les capes à capuchon, pluriel de burnus — le bonnet allongé, ou tout vêtement dont le capuchon fait partie, blouse ou jubba"},
        {"ar": "الخفاف", "translit": "al-khifāf", "fr": "les bottines — tout ce qui chausse le pied (la chaussette, jawrab, et ce qui lui ressemble) ; l'exception : coupées sous les chevilles pour qui ne trouve pas de sandales"},
        {"ar": "المنتقة", "translit": "al-mintaqa", "fr": "la ceinture (à la kasra du mīm initial) — ce dont on ceint le milieu du corps ; réprouvée apparente, permise dissimulée sous les vêtements et nouée (n° 915-916)"},
        {"ar": "الورس", "translit": "al-wars", "fr": "la plante jaune à l'odeur agréable dont on tire une teinture — « n'est pas un parfum, mais le Prophète l'a mentionné pour avertir d'éviter le parfum » (Ibn al-ʿArabī)"},
        {"ar": "الفدية", "translit": "al-fiḍya", "fr": "l'offrande expiatoire — due au mashhūr de l'école pour la couverture du visage, et pour le port contraint du pantalon ou la couverture de la tête selon Mālik et Abū Ḥanīfa"},
        {"ar": "الاسيور", "translit": "as-siyūr", "fr": "les lanières — les deux bouts de la ceinture portée sous les vêtements, faits en lanières et noués l'un à l'autre selon Saʿīd b. al-Musayyab (n° 916) : « c'est là ce que j'ai le mieux aimé entendre » (Mālik)"},
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
DOCID = 'pdf-mut23h2x-391'
if DOCID in com:
    print(f'!! {DOCID} déjà présent — rien de fait')
    raise SystemExit(1)
com[DOCID] = norme_entree(E_391)

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
