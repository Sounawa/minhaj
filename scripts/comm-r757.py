#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R757 - commentaire de la lecon 20 hadith-5ep : pdf-20 (da'm wa-t-tatbiq -
consolidation et application : troisieme consolidation du manuel, apres les
lecons 7 et 14 ; aucun hadith nouveau ; page de synthese sur le volet social :
l'homme sociable par nature, les relations organisees par l'islam, la
fraternite des hommes et la piete comme seule noblesse [al-Hujurat 13],
l'amour du bien pour le frere comme signe de la foi (boucle du treizieme
hadith, lecon 18), le beau modele prophetique [al-Qalam 4], la consolante de
Khadija avec ses cinq clauses [Sahih d'al-Bukhari]).
Treizieme vague du livre (SUIVANT de R756 ; hadith-5ep 19/29 au depart).
Redaction d'apres la lecture complete FR de la lecon (extraction non lossy,
/tmp/r757-lecon20-fr.txt, 820 mots) - etat des sources cette vague :
* l'arabe de la lecon 20 n'est pas encore transpose (html vide, pdfOnly),
  comme pour les lecons 14-22 du livre ;
* la verification sur le tirage demandee par le SUIVANT de R756 s'est
  heurtee a deux obstacles consignes : les PDF locaux du chantier ont ete
  emportes par le recyclage du bac a sable (content/textbooks-src absent)
  ET habous.gov.ma repond 404 (nginx) sur les tirages per-lecon testes
  (lecons 19, 20 et 21, chemin /المدرج/) ;
* la verification s'appuie donc sur la traduction savante htmlFr de la
  lecon (produite depuis le tirage, validee au registre savant) ET sur
  recoupements :
  (a) titres ar/fr identiques des lecons 7, 14, 20 : دعم وتطبيق / dmaym
      wa-tatbiq = trois consolidations du manuel ;
  (b) preparation de la lecon 19 : « Je lis le texte de la leçon de
      consolidation et d'application, et je réponds à ses questions » -
      annonce verbatim de la lecon 20 ;
  (c) echo textuel exact : l'ouverture de la lecon 20 (« L'homme est
      sociable par nature ») est reprise mot pour mot par le tamhid de la
      lecon 21, qui en tire la suite (nuisance -> colere) ;
  (d) preparation de la lecon 20 : « Je mémorise le hadīth de la leçon à
      venir, et je recherche les orientations religieuses (التوجيهات
      الشرعية) pour traiter la colère (الغضب) » - conforme au chapeau de la
      lecon 21 : « Autour du hadith d'Abū Hurayra « Ne te mets pas en
      colère » (lā taġḍab) » ;
  (e) matn de la lecon 18 verifie dans htmlFr : « Nul d'entre vous n'a la
      foi tant qu'il n'aime pour son frère ce qu'il aime pour lui-même »
      [Sahih d'al-Bukhari et Muslim], Anas ibn Malik - pour la boucle du
      treizieme hadith que la lecon 20 remonte (« Il a également compté au
      nombre des signes de la foi qui attestent sa perfection le fait que
      l'homme aime pour son frère, du bien, ce qu'il aime pour lui-même ») ;
  (f) Khadija : recherche sur les 29 lecons du livre - la lecon 20 est la
      SEULE a la nommer ; « première occurrence de son nom dans le manuel »
      est donc factuel.
NB de lecture : AUCUN NB a consigner cette vague - les deux references
coraniques du texte (الْحُجُرَات 13 ; الْقَلَم 4) coincident avec les versets
qui portent effectivement ces sens dans le mushaf (Ḥuǧurāt 13 : « ya ayyuha
n-nasu inna khalaqnakum... » ; Qalam 4 : « wa-innaka la-ʿala khuluqin ʿazim »).
Translitteration du commentaire en convention corpus (ʾ U+02BE / ʿ U+02BF),
les lecons htmlFr portant ' U+2019 - precedent R753-R756 (ex. lecon :
« da'm wa-tatbiq », commentaire : « daʿm wa-t-taṭbīq »).
Garde-fous de comm-r756 repris (typographie FR, arabe entre parentheses
seulement, vocab ar sans harakat, guillemets apparies) + fenetre de mots
1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_20 = {
    "auteur": "IA-1, tour R757",
    "resume": "Guide de lecture de la leçon 20 (le soutien et l'application — daʿm wa-t-taṭbīq (دَعْمٌ وَتَطْبِيقٌ)) : la troisième consolidation du manuel — après les leçons 7 et 14, qui portaient le même titre — aucun hadīth nouveau n'y est installé : « leçon-bilan, elle conduit l'élève à mobiliser, dans des situations nouvelles, les acquis des leçons précédentes ». Le texte, page de synthèse consacrée au volet social, ouvre sur « l'homme est sociable par nature » : « il a besoin de vivre au sein d'une communauté à laquelle le rattachent des relations » ; l'islam « a organisé ces relations en tous leurs genres » — beau traitement d'autrui, bienfaisance envers le voisin, honneur fait à l'hôte —, puis « a considéré tous les hommes comme des frères » : « nulle différence entre l'arabe et le non-arabe sinon par la piété » [al-Ḥuǧurāt : 13]. S'y ajoutent le signe de la foi — aimer pour son frère le bien qu'on aime pour soi, boucle du treizième hadīth (leçon 18) —, le beau modèle prophétique (« Et certes, tu es d'une moralité immense » [al-Qalam : 4]) et la consolante de Khadīǧa à la survenue de la révélation, cinq clauses de bienfaisance [Ṣaḥīḥ d'al-Buḫārī]. Trois objectifs de bilan : faire le bilan des acquis, mesurer ses capacités, mettre en pratique dans des situations nouvelles. La préparation de la leçon 19 l'avait annoncée ; la préparation d'aujourd'hui ouvre la leçon 21 : l'interdiction de la colère.",
    "explication": [
        "La leçon 20 est la troisième consolidation du manuel : après les leçons 7 et 14, elle porte de nouveau le titre de soutien et d'application (daʿm wa-t-taṭbīq (دَعْمٌ وَتَطْبِيقٌ)) — « leçon-bilan, elle conduit l'élève à mobiliser, dans des situations nouvelles, les acquis des leçons précédentes ». Aucun hadīth des Quarante n'y est installé ; son texte est, comme pour les consolidations précédentes, une page de synthèse écrite par les auteurs du manuel. La préparation de la leçon 19 l'avait annoncée : « Je lis le texte de la leçon de consolidation et d'application, et je réponds à ses questions. » Trois objectifs de bilan : « Que je fasse le bilan de mes acquis des leçons précédentes », « Que je mesure mes capacités dans l'apprentissage », « Que je mette en pratique ce que j'ai acquis dans des situations nouvelles » — le second demande la mesure de ses capacités dans l'apprentissage (at-taḥṣīl (التَّحْصِيلِ)).",
        "L'orientation diffère de la consolidation précédente. Celle de la leçon 14 partait de l'origine de l'homme — « l'homme est une créature honorée auprès d'Allah le Très-Haut » — et déroulait les grands chantiers doctrinaux ; celle-ci est consacrée au volet social : « L'homme est sociable par nature » : « il a besoin de vivre au sein d'une communauté à laquelle le rattachent des relations » — le sociable par nature se dit ʾiǧtimāʿiyy bi-ṭabʿih (اجْتِمَاعِيٌّ بِطَبْعِهِ). Le parti pris du texte : la vie sociale a besoin d'organisation — « l'islam a organisé ces relations en tous leurs genres et en a pris un soin immense ».",
        "Les preuves par l'exemple suivent immédiatement : « comme le montrent l'exhortation au beau traitement d'autrui, la bienfaisance envers le voisin et l'honneur fait à l'hôte… » — trois gestes qui récapitulent exactement les leçons qui viennent de se succéder : le treizième hadīth, l'amour du bien pour les gens (leçon 18), puis le quatorzième, l'honneur du voisin et de l'hôte (leçon 19). Le catalogue reste ouvert — la suspension finale du texte invite l'élève à en allonger la liste.",
        "Puis la montée en généralité : « L'islam est même allé plus loin encore, lorsqu'il a considéré tous les hommes comme des frères » — des frères se dit ʾiḫwa (إِخْوَةً) — puis « nulle différence entre l'arabe et le non-arabe sinon par la piété ». La preuve coranique : « Ô hommes ! Nous vous avons créés d'un mâle et d'une femelle, et Nous avons fait de vous des peuples et des tribus pour que vous vous connaissiez. Le plus noble d'entre vous, auprès de Dieu, est le plus pieux d'entre vous : certes, Dieu est savant, bien informé » [al-Ḥuǧurāt : 13]. Les peuples et les tribus sont donnés « pour que vous vous connaissiez » ; la noblesse auprès de Dieu se mesure à la seule piété — non au lignage ni à la langue.",
        "Le fil de la foi revient : « Il a également compté au nombre des signes de la foi qui attestent sa perfection le fait que l'homme aime pour son frère, du bien, ce qu'il aime pour lui-même, et déteste pour lui, du mal, ce qu'il déteste pour lui-même. » C'est la boucle exacte de la leçon 18, dont le texte portait : « Nul d'entre vous n'a la foi tant qu'il n'aime pour son frère ce qu'il aime pour lui-même » [Ṣaḥīḥ d'al-Buḫārī et Muslim] — et la formule rejoint le titre même de la leçon 19, des qualités de la foi : l'amour du bien pour le frère est un signe qui atteste la perfection de la foi.",
        "Le modèle humain couronne le développement : « Nous avons, en le Messager d'Allah — prière et salut d'Allah sur lui —, un beau modèle » — le beau modèle se dit ʾuswa ḥasana (أُسْوَةٌ حَسَنَةٌ) — « il fut le modèle suprême dans la bienfaisance envers autrui ». Et Dieu Très-Haut l'a loué pour cela : « Et certes, tu es d'une moralité immense » [al-Qalam : 4] — la même excellence du caractère que l'application redemandera en clôture.",
        "La preuve par le trait : la parole de Khadīǧa. Le texte raconte : « De même, la Mère des croyants Khadīǧa — que Dieu soit satisfait d'elle —, lorsqu'elle voulut apaiser le Prophète — prière et salut d'Allah sur lui — de l'effroi que lui causa la survenue de la révélation, prit pour preuve, dans la bonté de son caractère dont il s'était rendu célèbre avant la prophétie, que Dieu ne l'exposerait jamais au déshonneur » ; et elle dit : « Certes non, par Dieu ! Dieu ne t'exposera jamais au déshonneur : tu maintiens les liens du sang, tu prends en charge le faible, tu procures au démuni, tu honores l'hôte et tu portes secours aux épreuves du droit » [Ṣaḥīḥ d'al-Buḫārī]. C'est la première fois dans le manuel que Khadīǧa est nommée — aucune leçon précédente ne la mentionne : la consolidation y gagne la scène fondatrice de l'annonce de la révélation.",
        "L'argument de Khadīǧa mérite d'être suivi : cinq clauses dessinent le catalogue des vertus sociales — les liens du sang, le faible, le démuni, l'hôte, les épreuves du droit. Et le raisonnement : la bonté de caractère, attestée avant la prophétie, garantit que Dieu ne déshonore pas celui qui fut ainsi — Dieu ne l'exposera « jamais » au déshonneur. Le beau caractère ne se limite pas au matn des hadīth : il se voit, se raconte et se prend pour preuve.",
        "La compréhension (al-fahm (الْفَهْم)) donne deux tâches. D'abord : « Je propose un titre convenable au texte » — reconnaître le thème : l'organisation des relations sociales par l'islam et la bienfaisance envers autrui. Puis cinq explications demandées, tirées de la parole de Khadīǧa : « maintenir les liens du sang » (li-taṣila r-raḥim (لِتَصِلَ الرَّحِمَ)), « prendre en charge le faible » (taḥmilu l-kall (تَحْمِلُ الْكَلَّ)), « procurer au démuni » (tuksibu l-maʿdūm (تُكْسِبُ الْمَعْدُومَ)), « honorer l'hôte » (tuqrā ḍ-ḍayf (تُقْرَى الضَّيْفَ)), « les épreuves du droit » (nawāʾibu l-ḥaqq (نَوَائِبُ الْحَقِّ)) — les cinq clauses de la consolante, reprises une à une comme lexique.",
        "Clefs lexicales de ces clauses. Ar-raḥim — le lien de parenté : le maintenir (ṣilatu r-raḥim), c'est donner à chacun des proches son dû d'affection et d'entraide. Al-kall — celui que l'épuisement accable : « prendre en charge le faible », c'est porter ce que le faible ne peut porter. Al-maʿdūm — le démuni, celui à qui manque (ʿadam) ce dont il a besoin : « procurer au démuni », lui procurer de quoi vivre. Tuqrā ḍ-ḍayf — le verbe de l'hospitalité : pourvoir à l'hôte. Nawāʾib — pluriel de nāʾiba, la calamité, l'événement grave qui frappe : « tu portes secours aux épreuves du droit » ferme la liste.",
        "L'analyse (at-taḥlīl (التَّحْلِيل)) ouvre quatre chantiers. Premier : « Le texte dit que l'islam a organisé toutes les relations de l'homme : je cite trois sortes de ces relations, avec des exemples » — le bilan appelé par les objectifs. Deuxième : « J'établis par des textes scripturaires » ce qui suit : « la bienfaisance envers le voisin — l'honneur fait à l'hôte — l'amour du bien pour les gens » — remonter aux textes que les leçons 18-19 ont installés : le quatorzième hadīth pour le voisin et l'hôte (« Quiconque croit en Dieu et au Jour dernier, qu'il honore son voisin ; quiconque croit en Dieu et au Jour dernier, qu'il honore son hôte » [Ṣaḥīḥ d'al-Buḫārī et Muslim]), le treizième pour l'amour du bien.",
        "Troisième chantier : « J'extrais de la parole de la Mère des croyants Khadīǧa — que Dieu soit satisfait d'elle — les nobles caractères dont se parait le Messager d'Allah — prière et salut d'Allah sur lui. » Quatrième : « Sur quoi ces caractères, dont se parait le Messager d'Allah — prière et salut d'Allah sur lui — avant la descente de la révélation, permettent-ils de conclure ? » — la réponse est dans le texte même : la bonté de caractère antérieure atteste « que Dieu ne l'exposerait jamais au déshonneur ». Le bilan débouche sur l'argument : le beau caractère vérifie la sincérité du prophète.",
        "L'application (at-taṭbīq (التَّطْبِيق)) pose deux situations. La première part d'un constat amer : « L'islam a appelé à l'excellence du caractère » (ḥusn al-ḫuluq (حُسْنِ الْخُلُقِ)), puis « mais, hélas, il arrive que des gens offensent celui qui leur a fait du bien : comment convaincre celui qui fait du bien envers tels gens de ne pas répondre à leur offense par une autre offense, ni même d'interrompre pour autant sa bienfaisance à leur égard ? » — l'ingratitude d'autrui ne légitime ni la représaille ni l'abandon du bien. La seconde rouvre le chantier des leçons précédentes : « J'expose comment il est possible de maîtriser les membres » « en m'appuyant sur les preuves qui m'ont été facilitées » — la maîtrise des membres (ḍabṭ al-ǧawāriḥ (ضَبْطُ الْجَوَارِحِ)) dont la préparation de la leçon 18 demandait le mérite et dont la leçon 19 a déroulé les preuves (« la droiture de la langue relève des qualités de la foi »…).",
        "La préparation de la leçon suivante (al-ʾiʿdād al-qabliyy (الْإِعْدَادُ الْقَبْلِيُّ)) enjoint : « Je mémorise le hadīth de la leçon à venir » et la recherche des orientations religieuses (at-tawǧīhāt aš-šarʿiyya (التَّوْجِيهَاتِ الشَّرْعِيَّةِ)) « pour traiter la colère » (al-ġaḍab (الْغَضَبِ)). La leçon 21 répond : « l'interdiction de la colère » — autour du hadith d'Abū Hurayra « Ne te mets pas en colère » (lā taġḍab (لَا تَغْضَبْ)). Et l'écho est textuel : le chapeau de la leçon 21 reprend l'ouverture même de la consolidation — « l'homme est sociable par nature » — et en tire la suite : « il lui était donc indispensable de fréquenter autrui, et il en reçoit alors quelque nuisance, par une parole ou par un acte : il se met en colère » — la consolidation prépare, par son texte même, la leçon qui suit.",
        "Ce que la consolidation teste : la mémoire du fil — l'homme sociable, les relations organisées par l'islam, la fraternité humaine et la piété comme seule noblesse, l'amour du bien pour le frère comme signe de la foi, le beau modèle prophétique, les cinq clauses de Khadīǧa ; et la capacité de mobiliser — un titre à proposer, des explications à donner, des textes scripturaires à établir, des situations nouvelles à trancher. Le fil est posé : la colère est le premier ennemi du beau caractère — la leçon 21 la traitera ; puis l'excellence en toute chose (iḥsān) viendra avec la leçon 22.",
    ],
    "points": [
        "La place : troisième consolidation du manuel — les leçons 7, 14 puis 20 portent le même titre (daʿm wa-t-taṭbīq) ; aucun hadīth nouveau ; trois objectifs de bilan (bilan des acquis, mesure des capacités, mise en pratique dans des situations nouvelles).",
        "La continuité : la préparation de la leçon 19 l'annonçait — « Je lis le texte de la leçon de consolidation et d'application, et je réponds à ses questions » ; son ouverture, « l'homme est sociable par nature », sera reprise mot pour mot par la leçon 21.",
        "La fraternité : tous les hommes « des frères » — « nulle différence entre l'arabe et le non-arabe sinon par la piété » ; preuve : « Le plus noble d'entre vous, auprès de Dieu, est le plus pieux d'entre vous » [al-Ḥuǧurāt : 13].",
        "Le signe de la foi : « aime pour son frère, du bien, ce qu'il aime pour lui-même, et déteste pour lui, du mal, ce qu'il déteste pour lui-même » — boucle du treizième hadīth (leçon 18) : « Nul d'entre vous n'a la foi tant qu'il n'aime pour son frère ce qu'il aime pour lui-même » [Ṣaḥīḥ d'al-Buḫārī et Muslim].",
        "Le modèle : « un beau modèle » — le beau modèle se dit ʾuswa ḥasana (أُسْوَةٌ حَسَنَةٌ) — « Et certes, tu es d'une moralité immense » [al-Qalam : 4].",
        "Khadīǧa : sa consolante à la survenue de la révélation — cinq clauses (« tu maintiens les liens du sang » … « tu portes secours aux épreuves du droit ») [Ṣaḥīḥ d'al-Buḫārī] ; première occurrence de son nom dans le manuel ; le caractère antérieur atteste l'inviolabilité.",
        "L'analyse remonte aux leçons 18-19 : trois sortes de relations, trois thèmes appuyés de textes scripturaires (voisin — hôte — amour du bien), les nobles caractères de Khadīǧa et leur conclusion ; l'application rouvre ḍabṭ al-ǧawāriḥ avec « les preuves qui m'ont été facilitées ».",
        "La préparation : mémoriser le hadīth à venir et rechercher les orientations religieuses pour traiter la colère — la leçon 21, « l'interdiction de la colère », autour du « Ne te mets pas en colère » d'Abū Hurayra.",
    ],
    "vocabulaire": [
        {"ar": "دعم وتطبيق", "translit": "daʿm wa-t-taṭbīq", "fr": "le soutien et l'application — le titre des consolidations du manuel (leçons 7, 14 et 20) : soutenir les acquis et les appliquer dans des situations nouvelles."},
        {"ar": "اجتماعي بطبه", "translit": "ʾiǧtimāʿiyy bi-ṭabʿih", "fr": "sociable par nature — l'ouverture du texte : l'homme a besoin de vivre au sein d'une communauté à laquelle le rattachent des relations."},
        {"ar": "اخوة", "translit": "ʾiḫwa", "fr": "des frères — l'islam « a considéré tous les hommes comme des frères » : nulle différence entre l'arabe et le non-arabe sinon par la piété."},
        {"ar": "صلة الرحم", "translit": "ṣilatu r-raḥim", "fr": "le maintien des liens du sang — première clause de Khadīǧa : « tu maintiens les liens du sang » (li-taṣila r-raḥim)."},
        {"ar": "تحمل الكل", "translit": "taḥmilu l-kall", "fr": "tu prends en charge le faible — al-kall : celui que l'épuisement accable ; porter ce que le faible ne peut porter."},
        {"ar": "تقري الضيف", "translit": "tuqrā ḍ-ḍayf", "fr": "tu honores l'hôte — le verbe de l'hospitalité : pourvoir à l'hôte ; l'honneur fait à l'hôte, parmi les gestes par lesquels l'islam organise les relations."},
        {"ar": "نوائب الحق", "translit": "nawāʾibu l-ḥaqq", "fr": "les épreuves du droit — nawāʾib, pluriel de nāʾiba : la calamité ; « tu portes secours aux épreuves du droit » ferme la parole de Khadīǧa."},
        {"ar": "حسن الخلق", "translit": "ḥusnu l-ḫuluq", "fr": "l'excellence du caractère — celle que l'islam a appelée à pratiquer et que l'application demande de défendre face à l'offense d'autrui ; « Et certes, tu es d'une moralité immense » [al-Qalam : 4]."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}
ENTREES = [('pdf-20', E_20)]


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
    print(f'!! déjà présent : {bloque} — replacement (passe de correction)')
    for d in bloque:
        del com[d]
for docid, e in ENTREES:
    com[docid] = norme_entree(e)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys(), key=lambda x: int(x.split('-')[1])))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-20',):
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
