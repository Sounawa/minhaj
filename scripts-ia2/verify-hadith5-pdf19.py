#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-21 — vérification de la livraison hadith-5ep / pdf-19 (Des qualités de la foi)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-19.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-19']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-19 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine)', 8000 <= len(src) <= 15000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 4, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Mise en condition', 'Le texte', 'Notice biographique du transmetteur',
       'La compréhension', 'Glossaire', 'Extraction des contenus', 'L’analyse',
       'Ce qu’il faut retirer du hadīth', 'L’évaluation', 'La valorisation',
       'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-21, pp.104-110 + composites 600 dpi A-G +
#   médaillons m + zooms r/s ×2-×6 + recadrages mot-niveau w/x ×3.5-×6 +
#   couche bbox + sources canoniques web : Jāmiʿ al-ʿUlūm d'Ibn Raǧab ḥadīth 15,
#   Sharḥ al-Arbaʿīn d'Ibn Daqīq al-ʿĪd, al-Ifṣāḥ d'Ibn Hubayra, Ṣaḥīḥ al-Buḫārī) —
for kw in ['<h1>Des qualités de la foi</h1>',
           'min ḫiṣāli l-’īmān', '(مِنْ خِصَالِ الْإِيمَانِ)',
           'quatorzième hadīth des Quarante', 'Dix-neuvième leçon (19) du manuel',
           'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tahyi’a', '(تَهْيِئَة)', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'šarḥ', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl',
           'wamimmā yustafādu mina l-ḥadīṯ', 'at-taqwīm', 'al-istiṯmār',
           'al-’i’dād al-qabliyy',
           # objectifs (r01 ×1.6 letter-analyzed : أتعرف بعض / أُدرك بعض آثار / أُحرّص على التخلق)
           'Que je connaisse certaines des qualités de la foi',
           'Que je saisisse certains des effets des qualités de la foi',
           'Que je m’applique à me parer des qualités de la foi',
           # تهيئة (r02 letter-analyzed : رابطٌ وثيقٌ / يجسده صاحبه / إيمانه ḍamma)
           'un lien étroit',
           'la foi sincère est celle que son détenteur incarne dans des qualités nobles',
           'la retenue de la langue, la bienfaisance envers le voisin et l’honneur fait à l’hôte',
           'dont il se pare et par lesquelles sa foi se traduit en une conduite effective et concrète',
           'au sein de la foi\u202f?',
           'quel est le rapport de ces qualités avec la foi\u202f?',
           # hadith (A2/A3 + x02 : isnad عَنْ أبي هريرة أنّ رسول الله ﷺ قال)
           'D’après Abū Hurayra — que Dieu le Très-Haut soit satisfait de lui —, le Messager d’Allah — prière et salut d’Allah sur lui — a dit',
           '«\u202fQuiconque croit en Dieu et au Jour dernier, qu’il dise du bien ou qu’il se taise\u202f;',
           'quiconque croit en Dieu et au Jour dernier, qu’il honore son voisin\u202f;',
           'quiconque croit en Dieu et au Jour dernier, qu’il honore son hôte\u202f» [Ṣaḥīḥ d’al-Buḫārī et Muslim]',
           # notice (B1 : سبقت ترجمته)
           'Abū Hurayra — qu’Allah soit satisfait de lui —\u202f: sa notice a précédé',
           # glossaire (m04 letter-analyzed : لا ليل بعده ولا يسمى يوما إلا ما أعقبه ليل ;
           #           يصمت بضم الميم وسُمع كسرها وهو القياس كضرب يضرب)
           'al-yawmu l-’āḫir', '(الْيَوْمُ الْآخِرُ)',
           'c’est le Jour de la résurrection',
           'aucune nuit ne vient après lui',
           'l’on ne donne en propre le nom de jour qu’à celui qu’une nuit suit',
           'yaṣmutu', '(يَصْمُتُ)',
           'à la ḍamma du mīm', 'on a entendu aussi son kasra, qui est la forme régulière',
           'ḍaraba yaḍribu', 'aṣ-ṣamt', '(الصَّمْت)',
           'l’abstention de parler alors qu’on en a la capacité',
           # extraction (B2/B3)
           'En quoi le Prophète — prière et salut d’Allah sur lui — a-t-il commandé celui qui croit en Dieu et au Jour dernier\u202f?',
           # analyse — intro (B3 + couche : المتمثلة في) + axes
           'La présente leçon traite de certaines qualités de la foi — incarnées dans la retenue de la langue, la bienfaisance envers le voisin et l’honneur fait à l’hôte — et expose les aspects de leur rapport à la foi',
           '’awwalan\u202f: ḥifẓu l-lisān', '(أَوَّلًا: حِفْظُ اللِّسَانِ)',
           'ṯāniyan\u202f: ’ikrāmu l-ǧāri wa-ḍ-ḍayf', '(ثَانِيًا: إِكْرَامُ الْجَارِ وَالضَّيْفِ)',
           # أولا/1 فضل (s03 letter-analyzed : الإيمان الكامل المنجي من عذاب الله الموصل إلى رضوان الله ;
           #             r07+B4 : رجا ثوابه ; w01+Ibn Rajab : جوارحه التي هي رعاياه وهو مسئول عنها)
           'faḍlu ḥifẓi l-lisān', '(فَضْلُ حِفْظِ اللِّسَانِ)',
           'croit d’une foi complète, délivrante du châtiment de Dieu, conduisant à la satisfaction de Dieu',
           'redoute Sa menace, espère Sa récompense',
           's’applique à faire ce qui lui a été ordonné et à délaisser ce qui lui a été interdit',
           'la maîtrise de ses membres — qui sont ce dont il a la garde et dont il devra répondre',
           '«\u202fL’ouïe, la vue et le cœur\u202f: de chacun d’eux il sera demandé compte\u202f» [al-Isrā’\u202f: 36]',
           'la droiture de la langue relève des qualités de la foi',
           'Mu’āḏ ibn Ǧabal — que Dieu soit satisfait de lui —',
           '«\u202fTu ne cesseras d’être en sûreté tant que tu te tairas\u202f;',
           'dès lors que tu parleras, cela sera inscrit pour toi ou contre toi\u202f» [Fatḥ al-Bārī, qui l’attribue à aṭ-Ṭabarānī]',
           'répandre le salut entre les gens', 'la bonne parole',
           'la transmission au nom de Dieu Très-Haut et de Son messager',
           'réconcilier les gens', 'l’enseignement aux musulmans',
           'commander le bien et réprouver le mal — selon science, avec sagesse, douceur, mansuétude et parole convenable',
           # أولا/2 مخاطر (r08+s04 letter-analyzed : مَخَاطِرُ اللسان ; المتصلة ;
           #              s05 : ارتكابًا للزّلات، يُدخل الإنسان النار؛ أو على مناخرهم ;
           #              w06 : يُكَبُّ passif — déviation vs canonique يكبُّ consignée)
           'maḫāṭiru l-lisān', '(مَخَاطِرُ اللِّسَانِ)',
           'a réservé la langue, dans ce hadith, à l’exclusion des autres membres, en raison de sa gravité continue',
           '«\u202fIl ne prononce pas une parole sans qu’auprès de lui se tienne un observateur prêt\u202f» [Qāf\u202f: 18]',
           'la langue est le membre qui commet le plus de fautes',
           'ce qui fait le plus entrer l’homme dans le Feu',
           '«\u202fLes gens sont-ils précipités dans le Feu, sur leurs visages ou sur leurs narines, pour autre chose que les moissons de leurs langues\u202f?\u202f» [Sunan d’aṭ-Tirmiḏī]',
           'l’abondance de paroles dont on n’a nul besoin conduit à la dureté du cœur',
           'hadith d’Ibn ’Umar — que Dieu soit satisfait de eux deux —, remontant au Prophète',
           '«\u202fN’abondez pas en paroles en dehors de la mention de Dieu',
           'est dureté pour le cœur, et le plus éloigné des hommes de Dieu est le cœur dur\u202f» [Sunan d’aṭ-Tirmiḏī]',
           # ثانيا (C4+m12 letter-analyzed : فيه تعريف لحق الجار والضيف وبرّهما)
           'portent la définition du droit du voisin et de l’hôte, et la bienveillance à leur égard',
           '’ikrāmu l-ǧār', '(إِكْرَامُ الْجَارِ)',
           '’ikrāmu ḍ-ḍayf', '(إِكْرَامُ الضَّيْفِ)',
           # ثانيا/1 إكرام الجار (r11 letter-analyzed : أوصى/إيذائه وإلحاق الضرر ;
           #             r12 : التي لا يكمل الإيمان إلا بها ; s07 : وصية الله لنبيه ورسوله، حتى ظننت أنه سيورثه ;
           #             r14 : المتعلق في عبادته وحدّه وعدم الشرك به / بالحماية تماسك — FR neutre ;
           #             r15 : إسداء ضروب الخير، تفقد أحواله، ما آمن بي من بات شبعان)
           'Dieu — Puissant et Majestueux — a recommandé la bienfaisance envers le voisin dans le Noble Coran',
           'exhortant à honorer le voisin et mettant en garde contre le fait de l’offenser et de lui causer du tort',
           'une attention particulière, qui protège la cohésion de la société et consolide le principe de l’entraide, de la solidarité et de la coexistence',
           'la bienfaisance envers le voisin relève des qualités de la foi sans lesquelles la foi n’est pas parfaite',
           'une injonction de Dieu à Son prophète et messager',
           '’Ā’iša — que Dieu soit satisfait d’elle —',
           '«\u202fǦibrīl n’a cessé de m’enjoindre au sujet du voisin, au point que j’ai pensé qu’il allait le faire hériter\u202f» [Ṣaḥīḥ d’al-Buḫārī]',
           'Son droit propre — l’adoration, l’unicité et le refus de toute association — et le droit du voisin, celui de la bienfaisance envers lui',
           '«\u202fAdorez Dieu et ne Lui associez rien',
           'le voisin parent et le voisin étranger',
           'l’enfant de la route et ce que vos mains droites possèdent',
           'l’orgueilleux, le vantard\u202f» [an-Nisā’\u202f: 36]',
           'lui témoigner toutes sortes de bien, le secourir de ce que l’on possède, l’assister quand il demande aide et prendre de ses nouvelles',
           '«\u202fIl n’a pas foi en moi, celui qui passe la nuit rassasié tandis que son voisin, à son flanc, a faim — et il le sait\u202f» [al-Ǧāmi’ aṣ-ṣaġīr d’as-Suyūṭī]',
           # ثانيا/2 إكرام الضيف (r15/r16 : مكارم الأخلاق وآداب الإسلام وشرائعه وأحكامه / علامات الإيمان ;
           #             s08 letter-analyzed : تنزيله المنزلة اللائقة، تأنيسه بالإقبال، بكریم المحادثة وحسن الاستماع ;
           #             s09+w03+Ibn Daqīq : يضيف غنيًّا، يغيّرها، اليسير، بما فتح الله من غير كلفة — sans لهُ ;
           #             s11 : وقد ضيّف إبراهيم، هل أتاك حديث ضيف إبراهيم المكرمين [الذاريات: 24])
           'Honorer l’hôte relève des caractères généreux et des usages de l’islam, de ses prescriptions et de ses jugements',
           'a compté l’honneur de l’hôte au nombre des signes de la foi',
           'le bon accueil, le recevoir avec un visage ouvert, manifester l’hospitalité',
           'lui donner la place qui lui convient, lui tenir compagnie par l’attention portée à lui',
           'l’honorer d’un entretien aimable et de la bonne écoute',
           'tendre vers lui la main du secours s’il est dans le besoin',
           'Le vizir Ibn Hubayra a dit dans <em>al-Ifṣāḥ ’an ma’ānī aṣ-Ṣiḥāḥ</em>',
           'qu’honorer l’hôte est une adoration, que n’entame pas l’hébergement d’un riche et que n’altère pas le fait de présenter à son hôte le peu de ce qu’il possède',
           's’empresser d’offrir bonne mine à son visage et d’adoucir pour lui l’entretien',
           'Le pilier de l’affaire de l’hospitalité est le don de nourriture',
           's’empresser de ce que Dieu a dispensé, sans coûteuse dépense',
           'l’hospitalité relève des usages des envoyés, et Abraham — sur lui la paix — a offert l’hospitalité',
           '«\u202fT’est-il parvenu le récit des hôtes honorés d’Abraham\u202f?\u202f» [aḏ-Ḏāriyāt\u202f: 24]',
           # يُستفاد (r19 : وعمّا لا نفع فيه ; حثّ/الإسلام — s10/w07 fatha consignée ; تمتين letter-analyzed)
           'La parole de bien vaut mieux que le silence, et le silence vaut mieux que la parole du mal',
           'La purification de l’âme et son affinement passent par la maîtrise de la langue',
           'ce qui rapporte profit à l’individu et à la société',
           'l’éloignement de tout ce qui porte nuisance et de ce qui ne porte aucun profit',
           'la libéralité, à la générosité et à la bienfaisance envers le voisin et l’hôte',
           'se consolident les liens, se renforcent les relations et se répand l’amour entre les gens',
           # تقويم (r20 : دون بقية الجوارح letter-analyzed ; w08/s12/r21 : نوعين أساسيين/الساسيين — coquille consignée ;
           #         s12 : الجيران letter-analyzed ; Q3 أربعة أنواع من الإكرام)
           'a-t-il réservé la langue, en ce hadith, au point d’ordonner sa retenue à l’exclusion du reste des membres\u202f?',
           'Je cite deux types fondamentaux de la bienfaisance envers les voisins',
           'J’expose quatre sortes d’honneur, pour chacun du voisin et de l’hôte',
           # استثمار (r21b letter-analyzed : فليقل qāf sans hamza / ليسكت sīn / فليؤدّ / المعجم الكبير للطبراني)
           'D’après Ibn ’Umar — que Dieu soit satisfait de eux deux —, il a dit\u202f: j’ai entendu le Messager d’Allah',
           'qu’il s’acquitte de la zakāt de son bien',
           'qu’il dise du bien ou qu’il se taise',
           'qu’il honore son hôte\u202f» [al-Mu’ǧam al-kabīr d’aṭ-Ṭabarānī]',
           'J’extrais le rapport de l’acquittement de la zakāt avec la foi',
           'J’expose le rapport de la foi avec l’honneur de l’hôte et la bienfaisance envers le voisin',
           # الإعداد القبلي (G2/G3+couche+VLM p110 : singular — variation vs pdf-16/17/18 القبلية)
           '(الْإِعْدَادُ الْقَبْلِيُّ)',
           'Je lis le texte de la leçon de consolidation et d’application, et je réponds à ses questions',
           ]:
    check(f'contient «\u202f{kw[:60]}\u202f»', kw in src)
# — matière sur le LIVRE POSÉ —
check('htmlFr posé == fichier', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr pré-rempli', (l.get('titleFr') or '').strip() == 'Des qualités de la foi',
      f'({l.get("titleFr")!r})')
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 contient hadith-5ep/pdf-19', 'hadith-5ep/pdf-19' in reg.get('hand', []))

print(f"OK {len(ok)} / ÉCHEC {len(fail)}")
for f_ in fail:
    print('  ÉCHEC:', f_)
sys.exit(1 if fail else 0)
