#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R752 — commentaire de la leçon 15 hadith-5ep : pdf-15 (الحلال وإجابة الدعاء
— le licite et l'exaucement de l'invocation : le dixième hadīth des Quarante
« Certes Allah, le Très-Haut, est bon et n'accepte que ce qui est bon » —
causes de l'exaucement, lien du gain licite, empêchements, scène de Sa'd).
Huitième vague du livre (SUIVANT de R751-b ; hadith-5ep 14/29 au départ).
Rédaction d'après la lecture complète FR de la leçon (extraction non lossy
extrait-r752-lecon15.py) ET du tirage arabe du livre
(content/textbooks-src/hadith-5-ibtidai_text.pdf — le matn de la leçon 15
se trouve vers l'offset 61 000 du texte extrait, rubrique الحديث).
Aucune invention (règle 2) : hadiths, versets, citations et attributions
tels que la leçon les donne.
VIGILANCE R751-b RÉSOLUE : R751-b craignait que la notice du transmetteur du
tirage (Abū Hurayra) diverge des recueils usuels (Abū Masʿūd al-Anṣārī) ;
le tirage arabe du manuel porte bien « عن أبي هريرة رضي الله عنه » dans le
matn de la leçon 15 (vérifié pdftotext), en accord avec les Quarante de
al-Nawawī (dixième hadīth rapporté par Abū Hurayra) et avec la traduction FR
du livre — aucune divergence dans la leçon ; le commentaire suit le tirage.
NB de lecture consigné (langage lecteur, comme R742/R747/R749/R750/R751) :
les références imprimées du tirage portent al-Baqara 171 (dans le matn),
266 (deux fois) et 167 (istiṯmār) — les versets qui portent ces paroles sont
le 172, le 267 et le 168, vérifiés web (api.alquran.cloud, après délais
d'expiration de quran.com) : « Ô vous qui croyez, mangez des excellentes
choses que Nous vous avons attribuées » = al-Baqara 172 ; « dépensez des
choses excellentes que vous avez gagnées » + « Et ne visez pas le vil pour
en faire dépense » = al-Baqara 267 ; « Ô gens, mangez de ce qui est licite
et excellent sur terre » = al-Baqara 168. Corrects dans le tirage : Ġāfir
60, al-Muʾminūn 52 — aucune NB.
Le NB du matn (171) est porté HORS des guillemets du hadīth (le matn entier
est cité verbatim, référence imprimée comprise — le NB suit la citation).
Garde-fous de comm-r747/comm-r749/comm-r750/comm-r751 repris (typographie FR,
arabe entre parenthèses seulement, vocab ar sans harakat, guillemets
appariés) + fenêtre de mots 1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_15 = {
    "auteur": "IA-1, tour R752",
    "resume": ("Guide de lecture de la leçon 15 (le licite et l'exaucement de l'invocation — "
               "al-ḥalāl wa-ijābatu d-duʿāʾ (الْحَلَالُ وَإِجَابَةُ الدُّعَاءِ)) : le dixième hadīth "
               "des Quarante de l'imam al-Nawawī, rapporté par Abū Hurayra ʿAbd ar-Raḥmān ibn Ṣaḫr "
               "— qu'Allah soit satisfait de lui — : « Certes Allah, le Très-Haut, est bon et "
               "n'accepte que ce qui est bon » [Ṣaḥīḥ de Muslim]. Le tamhīd pose la promesse — "
               "« Implorez-Moi, Je vous répondrai » (Ġāfir 60) — et le constat de ceux qui "
               "insistent sans voir l'effet ; trois objectifs répondent : connaître les causes de "
               "l'exaucement, discerner le lien du gain licite avec lui, éviter ses empêchements "
               "et mettre en pratique ses règles de bienséance, « jusqu'à être un homme dont "
               "l'invocation est exaucée ». L'analyse déroule les causes (obligatoire : le gain "
               "licite ; recommandées : les règles de bienséance de l'invocation), puis les "
               "empêchements (l'illicite, l'insouciance), et l'exploitation donne au principe sa "
               "scène : « Ô Saʿd, purifie ce que tu manges : ton invocation sera exaucée »."),
    "explication": [
        ("La leçon 15 ouvre le dixième hadīth des Quarante : le chapeau la déclare « consacrée au "
         "licite et à l'exaucement de l'invocation », « le commentaire du dixième hadīth des "
         "Quarante de l'imam al-Nawawī, rapporté par Abū Hurayra ʿAbd ar-Raḥmān ibn Ṣaḫr — qu'Allah "
         "soit satisfait de lui ». La consolidation de la leçon 14 avait déjà annoncé le chantier : "
         "« Je mentionne le rapport entre la consommation du licite et l'invocation » — voilà le "
         "rapport tenu. Trois objectifs le précisent : « Que je connaisse les causes de "
         "l'exaucement de l'invocation », « Que je discerne le lien du gain licite avec "
         "l'exaucement de l'invocation », « Que j'évite les empêchements de l'exaucement de "
         "l'invocation et que je mette en pratique ses règles de bienséance, jusqu'à être un homme "
         "dont l'invocation est exaucée. » — le troisième vise l'aboutissement, pas le simple "
         "savoir."),
        ("Le tamhīd pose le fondement : l'invocation est ordonnée et son exaucement promis — « Et "
         "votre Seigneur a dit : Implorez-Moi, Je vous répondrai ; ceux qui, par orgueil, "
         "dédaignent de M'adorer entreront bientôt dans la Géhenne, humiliés » (Sourate Ġāfir — "
         "verset 60). Le constat qui suit donne à la leçon sa raison : « certaines personnes "
         "insistent dans l'invocation sans voir l'effet de l'exaucement, du fait de leur "
         "insouciance des empêchements de l'exaucement de l'invocation et de ses causes. » Deux "
         "questions en découlent — « Quelles sont donc les causes de l'exaucement de "
         "l'invocation ? Et quels sont ses empêchements ? » — et l'analyse y répond en deux "
         "sections."),
        ("Le texte rend le hadīth entier [Ṣaḥīḥ de Muslim] : « Certes Allah, le Très-Haut, est bon "
         "et n'accepte que ce qui est bon ; et certes Allah a ordonné aux croyants ce qu'Il a "
         "ordonné aux Messagers : le Très-Haut a dit : Ô Messagers, mangez des choses excellentes "
         "et œuvrez avec droiture (Sourate al-Muʾminūn — verset 52) ; et le Très-Haut a dit : Ô "
         "vous qui croyez, mangez des excellentes choses que Nous vous avons attribuées (Sourate "
         "al-Baqara — verset 171). Puis il mentionna l'homme qui prolonge le voyage, ébouriffé, "
         "couvert de poussière, tendant ses deux mains vers le ciel — Seigneur ! Seigneur ! —, "
         "alors que sa nourriture est illicite, sa boisson illicite, son vêtement illicite, et "
         "qu'il a été nourri d'illicite : comment donc serait-il exaucé ? » La notice du "
         "transmetteur renvoie en arrière : « sa notice biographique a été donnée précédemment » "
         "— la leçon 13 l'a développée en entier (ʿAbd ar-Raḥmān ibn Ṣaḫr ad-Dawsī, « le Compagnon "
         "— qu'Allah soit satisfait d'eux — qui mémorisa le mieux le hadīth prophétique »)."),
        ("NB de lecture : la seconde āya du matn est celle-ci — « Ô vous qui croyez, mangez des "
         "excellentes choses que Nous vous avons attribuées » (Sourate al-Baqara — la référence "
         "imprimée porte le verset 171 ; le verset qui porte ces paroles est le 172)."),
        ("Le glossaire déplie les six clés du hadīth. « certes Allah est bon » (ṭayyib) — « le bon "
         "est le contraire du vil ; quand on qualifie ainsi Allah le Très-Haut, on entend par là "
         "qu'Il est transcendant au-dessus des imperfections et des défauts » ; « ce qui est bon » "
         "(ṭayyiban) — « ce qui est bon parmi les biens : ce qui est exempt d'illicite ; et parmi "
         "les actions : ce qui est exempt de ce qui corrompt » : la double mesure, dans le gain et "
         "dans l'acte. Viennent les mots de la scène : « couvert de poussière » (aġbar) — « dont "
         "le teint est altéré par l'effet de la poussière sur le corps et le vêtement, à cause de "
         "la longueur du voyage » ; « tend ses deux mains » (yamuddu yadayhi) — « les élève, par "
         "l'invocation, vers Allah » ; « a été nourri » (ġuḏiya) — « son corps s'est nourri "
         "d'illicite » ; et la question finale : « comment donc serait-il exaucé » "
         "(fa-annā yustajābu li-ḏālika) — « de quelle manière serait-il exaucé, lui ? Le sens "
         "est : il n'est pas digne d'être exaucé. »"),
        ("L'extraction annonce les deux chantiers : « J'extrais du hadīth les causes de "
         "l'exaucement de l'invocation » et « J'expose, à partir du hadīth, les empêchements de "
         "l'exaucement de l'invocation. » L'analyse ouvre : « L'exaucement de l'invocation a ses "
         "causes, dont certaines sont obligatoires et d'autres recommandées ; les réunir au "
         "moment de l'invocation est ce qu'il y a de plus excellent et de plus indiqué. » La "
         "cause obligatoire tient au hadīth lui-même : « Certes Allah, le Très-Haut, est bon et "
         "n'accepte que ce qui est bon » — « Le hadīth exhorte au gain tiré du licite excellent "
         "et à la dépense qui en provient, et proscrit le gain tiré de l'illicite vil ainsi que "
         "la dépense qui en provient : ce qui est mangé, bu et porté, et les choses semblables, "
         "doit être tout entier licite, pur, sans aucun soupçon. »"),
        ("Les deux āyāt de la dépense appuient la cause obligatoire : « Ô vous qui croyez, "
         "dépensez des choses excellentes que vous avez gagnées, et de ce que Nous avons fait "
         "sortir pour vous de la terre » (Sourate al-Baqara — la référence imprimée porte le "
         "verset 266 ; le verset qui porte ces paroles est le 267), et la proscription de la "
         "dépense de l'illicite vil : « Et ne visez pas le vil pour en faire dépense » (Sourate "
         "al-Baqara — la référence imprimée porte le verset 266 ; le verset qui porte ces paroles "
         "est le 267)."),
        ("La suite du hadīth lie les deux publics : « certes Allah a ordonné aux croyants ce "
         "qu'Il a ordonné aux Messagers » — le Très-Haut a dit : « Ô Messagers, mangez des "
         "choses excellentes et œuvrez avec droiture » (Sourate al-Muʾminūn — verset 52) —, et le "
         "tirage tire la conséquence : « le Prophète — prière et salut d'Allah sur lui — a ainsi "
         "montré qu'Allah a ordonné aux croyants de manger du licite, de même qu'Il l'a ordonné "
         "aux Messagers. » Le licite n'est pas un conseil de perfection : c'est un ordre, le "
         "même pour les Messagers et pour les croyants — l'œuvre droite commence dans "
         "l'assiette."),
        ("Au nombre des causes recommandées figurent les règles de bienséance que comporte le "
         "hadīth : « élever les deux mains vers le ciel au moment de l'invocation », conformément "
         "à sa parole — prière et salut d'Allah sur lui — : « il tend ses deux mains vers le "
         "ciel » ; et l'exemple prophétique — « élevait les mains dans la prière de demande de "
         "pluie, au point que l'on voyait le blanc de ses aisselles » [Ṣaḥīḥ de al-Buḫārī]. Puis "
         "l'adab de la parole : « l'insistance auprès d'Allah le Très-Haut par la louange qui Lui "
         "est adressée, et l'évocation de la faveur de Sa générosité et de Ses bienfaits », sur le "
         "modèle de sa parole — prière et salut d'Allah sur lui — : « Seigneur ! Seigneur ! »"),
        ("Deuxièmement — les empêchements, qui font obstacle à l'exaucement « même lorsque les "
         "règles de bienséance précédentes sont réunies ». Premier empêchement : « consommer de "
         "l'illicite par la nourriture, la boisson ou l'habillement » — d'où la question du "
         "matn : « sa nourriture est illicite, sa boisson est illicite, son vêtement est illicite, "
         "et il a été nourri d'illicite : comment donc serait-il exaucé ? » La nuance du tirage "
         "est capitale : « C'est là tenir l'exaucement de son invocation pour improbable, non le "
         "tenir pour impossible : il se peut en effet qu'Allah le Très-Haut l'exauce par pure "
         "faveur, par ménagement et par générosité, ou bien à titre d'épreuve et d'istidrāǧ — "
         "l'amenée insidieuse du châtiment » — l'exaucement n'est jamais annulé ; il peut même "
         "devenir l'instrument de l'épreuve. Second empêchement : « l'insouciance d'Allah le "
         "Très-Haut » — « comme il apparaît dans le Ǧāmiʿ de at-Tirmiḏī d'après Abū Hurayra » : "
         "« Implorez Allah en ayant la certitude de l'exaucement, et sachez qu'Allah n'exauce pas "
         "l'invocation proférée par un cœur insoucieux et distrait » [Sunan de at-Tirmiḏī]."),
        ("Ce qu'il faut retirer du hadīth en trois bénéfices : « L'avertissement de la nécessité "
         "de réunir les causes de l'exaucement de l'invocation et ses règles de bienséance — au "
         "premier chef desquelles la consommation du licite » ; « Le recours à Allah, l'humilité "
         "suppliante et l'insistance dans l'invocation comptent parmi les causes de "
         "l'exaucement » ; « Le gain licite relève de la conduite des Messagers et des serviteurs "
         "vertueux d'Allah. » L'évaluation pose deux questions de bilan : « Quel est le lien du "
         "gain licite avec l'exaucement de l'invocation ? » et « Je mentionne certaines des "
         "règles de bienséance de l'invocation. »"),
        ("L'exploitation donne au principe sa scène la plus saisissante [al-Muʾǧam al-awsaṭ de "
         "aṭ-Ṭabarānī] : d'après Ibn ʿAbbās — qu'Allah soit satisfait de lui et de son père —, "
         "« ce verset fut récité devant le Messager d'Allah — prière et salut d'Allah sur lui » : "
         "« Ô gens, mangez de ce qui est licite et excellent sur terre » (Sourate al-Baqara — la "
         "référence imprimée porte le verset 167 ; le verset qui porte ces paroles est le 168). "
         "Saʿd ibn Abī Waqqāṣ se leva alors : « Ô Messager d'Allah, implore Allah qu'Il me fasse "
         "l'un de ceux dont l'invocation est exaucée. » Réponse : « Ô Saʿd, purifie ce que tu "
         "manges : ton invocation sera exaucée. Par Celui qui détient l'âme de Muḥammad en Sa "
         "main, le serviteur qui jette dans son ventre une bouchée d'illicite, nulle action "
         "n'est acceptée de lui pendant quarante jours ; et tout serviteur dont la chair s'est "
         "développée d'un bien illicitement acquis (suḥt), le Feu a plus de droit sur lui » — la "
         "prière de l'exaucé commence dans l'assiette : les quarante jours d'œuvres refusées et "
         "le Feu plus de droit sur la chair nourrie de suḥt portent le hadīth de la leçon à son "
         "terme le plus concret."),
        ("La préparation tourne la page : « Je mémorise le hadīth de la leçon qui vient », et "
         "deux recherches — « Je recherche la notice biographique de al-Ḥasan ibn ʿAlī — qu'Allah "
         "soit satisfait de lui et de son père » et « Je recherche le sens des choses ambiguës "
         "(šubuhāt) et leur statut » — le chantier de la leçon suivante, le onzième hadīth des "
         "Quarante, transmis par al-Ḥasan ibn ʿAlī : le hadīth du scrupule (waraʿ), où les "
         "šubuhāt que la leçon 10 a définies — le non-tranché entre le licite évident et "
         "l'illicite évident — deviennent le seuil de garde du gain."),
    ],
    "points": [
        ("La continuité exacte : la consolidation de la leçon 14 demandait « Je mentionne le "
         "rapport entre la consommation du licite et l'invocation » — la leçon 15 est ce rapport, "
         "dans le dixième hadīth des Quarante (Abū Hurayra, Ṣaḥīḥ de Muslim)."),
        ("Le fondement : Ġāfir 60 — l'invocation ordonnée, l'exaucement promis ; le défaut n'est "
         "pas dans la promesse mais dans l'insouciance — « du fait de leur insouciance des "
         "empêchements de l'exaucement de l'invocation et de ses causes »."),
        ("Le hadīth en trois mouvements : le principe (« Allah, le Très-Haut, est bon et "
         "n'accepte que ce qui est bon »), la continuité des ordres (aux Messagers — al-Muʾminūn "
         "52 ; aux croyants — al-Baqara 172), la scène de l'homme du voyage nourri d'illicite."),
        ("La double mesure du ṭayyib : dans le bien (exempt d'illicite) et dans l'action (exempt "
         "de ce qui corrompt) — le gain et la dépense, la bouche et la main."),
        ("Causes obligatoires (le gain licite et la dépense licite) et causes recommandées "
         "(élever les deux mains, l'insistance par la louange) : « les réunir au moment de "
         "l'invocation est ce qu'il y a de plus excellent et de plus indiqué »."),
        ("Les empêchements : la consommation d'illicite et l'insouciance — « Allah n'exauce pas "
         "l'invocation proférée par un cœur insoucieux et distrait » [Sunan de at-Tirmiḏī]."),
        ("La précision qui protège la doctrine : l'illicite rend l'exaucement improbable, non "
         "impossible — Allah peut exaucer « par pure faveur, par ménagement et par générosité, "
         "ou bien à titre d'épreuve et d'istidrāǧ »."),
        ("L'aboutissement : la leçon veut « un homme dont l'invocation est exaucée » — "
         "l'exploitation de Saʿd donne la clef (« purifie ce que tu manges ») ; la préparation "
         "annonce al-Ḥasan ibn ʿAlī et les šubuhāt (la leçon 16, le onzième hadīth)."),
    ],
    "vocabulaire": [
        {"ar": "الحلال وإجابة الدعاء", "translit": "al-ḥalāl wa-ijābatu d-duʿāʾ",
         "fr": "le licite et l'exaucement de l'invocation — le titre de la leçon et son couple "
               "de principe : ce que l'on mange porte ce que l'on demande."},
        {"ar": "طيب", "translit": "ṭayyib",
         "fr": "le bon — « le contraire du vil » ; qualifié pour Allah le Très-Haut : "
               "transcendant au-dessus des imperfections et des défauts."},
        {"ar": "طيبا", "translit": "ṭayyiban",
         "fr": "ce qui est bon — parmi les biens, ce qui est exempt d'illicite ; parmi les "
               "actions, ce qui est exempt de ce qui corrompt : la double mesure du hadīth."},
        {"ar": "أغبر", "translit": "aġbar",
         "fr": "couvert de poussière — le teint altéré par la poussière sur le corps et le "
               "vêtement, à cause de la longueur du voyage : le visage de l'invocateur du matn."},
        {"ar": "يمد يديه", "translit": "yamuddu yadayhi",
         "fr": "il tend ses deux mains — les élève, par l'invocation, vers Allah : première des "
               "règles de bienséance recommandées."},
        {"ar": "غذي", "translit": "ġuḏiya",
         "fr": "a été nourri — son corps s'est nourri d'illicite : la cause profonde du blocage "
               "de l'exaucement."},
        {"ar": "استدراج", "translit": "istidrāǧ",
         "fr": "l'amenée insidieuse du châtiment — avec l'épreuve, ce qui peut accompagner "
               "l'exaucement du consommateur d'illicite : être exaucé n'est pas toujours une "
               "preuve d'honneur."},
        {"ar": "سحت", "translit": "suḥt",
         "fr": "le bien illicitement acquis — « tout serviteur dont la chair s'est développée "
               "d'un bien illicitement acquis (suḥt), le Feu a plus de droit sur lui » "
               "[al-Muʾǧam al-awsaṭ de aṭ-Ṭabarānī]."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-15', E_15)]


def norme_fr(s):
    s = s.replace('\'', '\u2019')
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
bloque = [d for d, _ in ENTREES if d in com]
if bloque:
    print(f'!! déjà présent : {bloque} — rien de fait')
    raise SystemExit(1)
for docid, e in ENTREES:
    com[docid] = norme_entree(e)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys()))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-15',):
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    fenetre = 'PASS' if 1700 <= mots <= 2400 else 'HORS FENETRE'
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])} — fenêtre 1700-2400 : {fenetre}')
    if fenetre != 'PASS':
        mauvais += 1
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] \
             + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t)
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
        if motif_ar.search(v['fr']):
            mauvais += 1
            print('   vocab fr contient de l arabe :', v['fr'][:60])
        if not re.search(r'[\u02BE\u02BF]', v['translit']):
            print('   note : translit sans ʾ/ʿ :', v['translit'])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
if mauvais:
    sys.exit(1)
