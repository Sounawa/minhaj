# Minhāj — Worklog IA-2 (compte parallèle, série Z)

> Journal de l'IA-2. **IA-1 (série R) n'écrit jamais ici ; IA-2 n'écrit jamais dans `worklog.md`.**
> Référentiel de règles : `PROTOCOLE-DEUX-IA.md`. GitHub main = source de vérité unique.
> Début de session obligatoire : `bash /home/z/my-project/scripts-recovery/session-start.sh`.

---

## Z1 — 2026-11-12 ~11h00-12h30 UTC+8 (trace 1a1cf6f735b99afd-z1-main)

Task ID: Z1
Agent: IA-2 (Z.ai, compte parallèle)
Task: Ouverture du front primaire — protocole deux machines + QA typographique complète de la zone

Work Log:
- Session ouverte sur un bac neuf : clone sparse `--depth 1 --filter=blob:none` de
  `github.com/Sounawa/minhaj` (018348b, R690), dossiers lourds exclus (textbooks-src,
  ocr-cache, generated-*, qa-*.png). Lecture du protocole de session du worklog.md,
  de GARDE-DOUBLON.md et des 40 derniers commits (conventions claim/trace de IA-1).
- Cartographie du travail réel croisée avec le registre vivant
  `scripts-translate/savant-registry.json` (hand 1156 / llm 57 — le registre à la racine
  est périmé : 496/36, ne pas s'y fier) : **0 document GT restant dans tout le corpus** ;
  le chantier restant est (a) les 862 leçons pdfOnly sans texte extrait, (b) la QA
  typographique des htmlFr existants, (c) les chantiers app (R9).
- Constat clé : `qa-lesson.py` (« 0 apostrophe droite ») n'a été appliqué qu'aux livraisons
  récentes. Scan global (`scripts-ia2/qa_corpus.py`, règles reprises de qa-lesson.py) :
  primaire = 380 docs à défauts durs (≈ 22 140 apostrophes droites dont 10 308 hamzas
  translittérées après voyelle longue `…</em>'`), 6 guillemets non appariés sur 5 docs ;
  secondaire (zone IA-1) = 805 docs à défauts durs — **signalé, non touché** (règle §2
  du protocole).
- Correction appliquée à la zone primaire UNIQUEMENT (`scripts-ia2/fix_typo_ep.py`,
  réplique exacte de l'auto-fix de qa-lesson.py + normalisation de la hamza ʾ U+02BE
  après voyelle longue, convention majoritaire du corpus 167 vs 37) : 13 livres ep
  modifiés, 380 documents corrigés.
- 6 guillemets orphelins refermés manuellement, ancre par ancre, avec décision
  éditoriale documentée (`scripts-ia2/fix_guillemets.py`, idempotent, ancres uniques) :
  fiqh-5ep/12011 (fermant doublé retiré), tafsir-5ep/13915 (hadith englobant refermé
  après la référence du verset), 16743 (citation Ibn ʿĀshūr refermée), 16757 (citation
  Ibn Kathīr refermée), 16767 ×2 (citation al-Jalālayn refermée avant le crochet de
  source ; hadith at-Tirmidhī refermé après la 3e référence de verset).
- Re-scan final : **0 défaut dur sur le primaire** (35 docs avec flags soft
  paren_espaces uniquement — hors périmètre de qa-lesson.py, laissé tel quel).
- JSON des 13 livres revalidés (roundtrip json.dumps ensure_ascii=False indent=2 fidèle,
  mêmes options que le dépôt). Aucun autre fichier touché.

Stage Summary:
- **Primaire : 389 docs FR nettoyés typographiquement, 0 défaut dur.** 1 commit, 0 push
  (token absent du bac) — bundle de sûreté fourni à l'utilisateur.
- Le partage en deux zones (primaire vs collège+lycée) est consigné dans
  `PROTOCOLE-DEUX-IA.md` : zéro fichier en commun, claims par livre, vague = 1-4 documents.
- Prochaines passes IA-2 (Z2+) : extraction leçons hadith-5ep (PDF local
  `content/textbooks-src/hadith-5-ibtidai_text.pdf` — couche texte garblée, lectures VLM
  requises, méthode IA-1), puis hadith-6ep (PDF local), puis les books à PDF géobloqués
  quand l'utilisateur fournira un canal, puis chantiers app R9 (À propos, export).
- Zone IA-1 intacte : aucun fichier es/tanawi, worklog.md et agent-queue.json non touchés.

---
Task ID: Z2-1
Agent: IA-2 (Z.ai, compte parallèle, session web-db9f75eb, trace 1a1cf927aa091245, tick 2026-11-12)
Task: LIVRAISON leçon 1 hadith-5ep (pdf-1 — « Présentation de l'auteur et de l'ouvrage », التعريف بالمؤلف والمؤلف, PDF pp. 13-17) — premier chantier Z2 après restauration des deps (recette R603) et push du commit Z1.

Work Log:
- Ouverture de séance : token GitHub fourni par l'utilisateur → push du commit Z1 (018348b..d5b9c0c) — le bundle de sûreté minhaj-Z1-primaire.bdl devient obsolète ; deps restaurées (bun install 842 paquets + prisma generate, recette R603) ; site non relancé (priorité traductions).
- BORNAGE : leçon pdf-1 = pages 13-17 du PDF local content/textbooks-src/hadith-5-ibtidai_text.pdf (167 p.) — la leçon 2 démarre p.18 (lecture VLM) ; la borne « أهداف الدرس » du text-layer en p.23 était trompeuse (OCR garblé, mots réinversés).
- MÉTHODE : 10 lectures VLM pleine-page (glm-5v-turbo, 150 dpi) + 10 adjudications demi-page (300 dpi) + 10 micro-crops de bandes — puis ADJUDICATION FINALE PAR LECTURE DIRECTE de l'agent sur les pages et crops (plus fiable que le VLM sur les points lettres à lettres). Pages tranchées : p13 (objectifs ×3 dont العناية, tamhīd avec فأقبلوا على شرح أحاديثه وبيان معانيه بين مختصر ومطوّل, encadré النص = texte canonique de l'intro des Quarante), p14 (rubrique الفهم ; gloses ×3 dont الأداب = الفضائل والخصال المحمودة ; استخلاص ×2 dont أبرز ; التحليل يشتمل ; bio al-Nawawī : né Muḥarram 631 à Nawā plaine de Ḥawrān, Damas 649 âgé de 19 ans, madrasa ar-Rawāḥiyya, 12 leçons/jour), p15 (professeurs : الرضيان البرهان، شيخ الشيوخ عبد العزيز بن محمد الأنصاري، زين الدين عبد الدائم ; élèves : الحافظ صدر الدين سليمان الجعفري، شهاب الدين أحمد بن جعوان، علاء الدين العطار ; œuvres : شرح صحيح مسلم، رياض الصالحين، الأذكار، الأربعون، روضة الطالبين، المجموع، التيان/التبيان في آداب حملة القرآن ; mort à Nawā le 24 Raǧab 676 âgé de 45 ans ; bio Ibn Daqīq al-'Īd : محمد بن علي بن وهب بن مطيع، أبو الفتح تقي الدين القشيري القوصي المصري نزيل القاهرة، né Ša'bān 625 près de Yanbu' au Ḥiǧāz sur la côte de la mer Rouge, نشأ بقوص وسأل بمصر ورحل لدمشق ثم استقر بالقاهرة، قضاء الديار المصرية 695, mort 702 ; œuvres : إحكام الأحكام، الإلمام، الاقتراح، شرح الأربعين للنووي، شرح مقدمة المطرزي), p16 (ثانيا مكانة الأربعين ×5 puces : matière ; chaque hadith une grande règle ; التزام الصحة/معظمها في صحيح البخاري ومسلم ; hadith « من حفظ على أمتي أربعين حديثا من أمر دينها » + riwāyāt « بعثه الله فقيها عالما » et « وفي رواية أبي الدرداء: وكنت له يوم القيامة شافعا وشهيدا » [شعب الإيمان للبيهقي] ; تلقي الناس شرقا وغربا) + وما يستفاد ×3 ; p17 (التقويم ×3 ; encadré الاستثمار = passage de l'intro des Quarante avec la liste des compilateurs : عبد الله بن المبارك، محمد بن أسلم الطوسي العالم الرباني، الحسن بن سفيان النسائي، أبو بكر الأجري، أبو بكر بن إبراهيم الأصفهاني، الدارقطني، الحاكم، أبو نعيم، أبو عبد الرحمن السلمي، أبو سعيد الماليني، أبو عثمان الصابوني، عبد الله بن محمد الأنصاري، أبو بكر البيهقي، وخلفهم لا يحصون ; question اذكر ثلاثة من المؤلفين ; الأعداد القبلية : أحفظ حديث إنما الأعمال بالنيات ×3).
- RÉDACTION : scripts-ia2/livraisons/hadith-5ep/pdf-1.html (10 678 car) — structure fidèle au manuel, conventions rubriques de hadith-1ep (Objectifs/Exorde/Le texte/La compréhension/Glossaire/Extraction des contenus/Analyse/Évaluation/Investissement/La préparation) + translittération scientifique (š ǧ ḥ ḫ ṣ ḍ ṭ ẓ, hamza ʾ U+02BE après voyelle longue, 'ayn → ' U+2019).
- OUTILS IA-2 : hand-set-ia2.py créé (réplique de hand-set.py adaptée au chemin repo-minhaj, mêmes garanties : garde-doublon, lecture fraîche, écriture atomique, registre — registre IA-2 SÉPARÉ scripts-ia2/savant-registry-ia2.json, zéro écriture dans les fichiers d'IA-1) ; verify-hadith5-pdf1.py (garde-doublon + matière).
- QA : qa-lesson.py PASS (auto-fix NNBSP/apostrophes) — 10 678 car, 0 arabe hors spans, 7 guillemets appariés, 0 apostrophe droite. VERIF : 21 contrôles OK / 0 échec (garde-doublon vide avant pose, matière Nawawī/Ibn Daqīq/dates/ouvrages/hadith/riwāyāt, htmlFr posé == source).
- POSE : hand-set-ia2.py hadith-5ep pdf-1 → 1 emplacement, 10 678 car, registre IA-2 → 1. hadith-5ep : 1/29 leçons FR.
- INCERTITUDES CONSIGNÉES (une incertaine = incertaine) : (1) professeur « ar-Raḍyān al-Burhān » p15 — lecture convergente sur 3 rendus, identification historique non vérifiée ; (2) élève « al-Ja'farī » (lectures concordantes) vs الجعبري attendu par l'histoire ; (3) fin de bio p14 « عن شيوخه درسا وتصحيحا » — شيوخه/شيخه et تصحيحا/تصديرا (FR neutre « auprès de ses maîtres — une leçon et une correction ») ; (4) naissance Ibn Daqīq « بقرْبِ ينبعٍ من الحجاز » vs « قرية ينبع » (FR rendu « près de Yanbu' ») ; (5) « شرح مقدمة المطرزي » — forme imprimée conservée ; (6) puce 3 p16 « الصحة » (avec/بدون بال) ; (7) hadith « بعثه الله/بُعث الله » (FR neutre compatible) ; (8) النشوع/النشء p16 (FR neutre « la jeunesse »).
- Sync git : fetch + rev-list avant production ; push immédiat après livraison (règle de vague).

Stage Summary:
- LIVRÉ : leçon 1 hadith-5ep « Présentation de l'auteur et de l'ouvrage » (pdf-1, pp. 13-17, 10 678 car, registre IA-2 → 1) — hadith-5ep 1/29.
- MÉTHODE CONSOLIDÉE IA-2 : lectures VLM → adjudications de bandes → RELECTURE DIRECTE par l'agent (tranchante sur les points contestés) ; outils de pose dupliqués dans scripts-ia2/ (zéro empiètement sur IA-1).
- Prochaine priorité : slot pdf-2 (leçon 2 — الأعمال بالنيات, hadith 1 des Quarante, pp. 18-22) ; git fetch 0/0 avant production ; PARALLÈLE : 1.

---
Task ID: Z2-2
Agent: IA-2 (Z.ai, compte parallèle, session web-db9f75eb, trace 1a1cfcf35bf8e685, tick 2026-11-12)
Task: LIVRAISON leçon 2 hadith-5ep (pdf-2 — « Les actes ne valent que par les intentions », الأعمال بالنيات, hadith 1 des Quarante, PDF pp. 18-22) — sync git 0/0 avant production.

Work Log:
- BORNAGE confirmé : leçon pdf-2 = pages 18-22 ; leçon 3 (الإسلام والإيمان, hadith de Jibrīl) démarre p.23.
- MÉTHODE Z2 consolidée (réutilisée) : lectures VLM pleine-page Z2-1 déjà disponibles pour p.18-22 + ADJUDICATION FINALE PAR LECTURE DIRECTE de l'agent : p18 (titre الأعمال بالنيات ; objectifs ×3 ; tamhīd لما لها من أثر بليغ في صحة العمل وبطلانه، الفيصل الأساس بين العبادات والعدات; hadith 1 des Quarante INTÉGRAL, texte canonique muttaqun 'alayhi), p19 (ترجمة الراوي 'Umar : أبو حفص عمر بن الخطاب بن نفيل العدوي، أسلم سنة 6 قبل الهجرة، شهد المشاهد كلها، مات شهيدا سنة 23 ; gloses الأعمال=الأفعال/النيات=القصد والعزم ; استخلاص ; التحليل : متفق على صحته، أحد الأحاديث التي عليها مدار الإسلام ; quote أ Ahmad + Šāfi'ī « يدخل في حديث الأعمال بالنيات ثلث العلم » + la cause (كسب العبد بقلبه ولسانه وجوارحه) ; quote 'Abd ar-Raḥmān ibn Mahdī « ينبغي لكل من صنف كتابا أن يبدأ فيه بهذا الحديث تتبعا للطالب على تصحيح النية »), p20 (أولا النية وأثرها في تقويم الأعمال : التمييز بين العادة والعبادة + 3 exemples : الجلوس في المسجد/تنظيف البيت ; أربع ركعات عن صلاة الظهر/عن السنة ; الأكل قوة على العبادة/الاقتداء برسول الله ; النية شرط في تعيين المفروض + ولولا هذا اللفظ), p21 (ثانيا إخلاص النية : خالصا لله موافقا للهدى النبوي أدعى للقبول وإن كان قليلا / رياء الناس أو شائبة شرك مردود وإن كان كثيرا ; الإخلاص يرقي بالعمل إلى شرف القبول + تقوية لمراتب الأعمال ; فمن هاجر ابتغاء وجه الله... ومن هاجر لقصد دنيوي فإنما حظه... ولا حظ له في الآخرة ; سبب ورود الحديث : هاجر رجل ليتزوج أم قيس، مهاجر أم قيس [المعجم الكبير للطبراني] ; وما يستفاد ×4), p22 (التقويم ×4 ; الاستثمار : hadith Abū Hurayra « إن الله لا ينظر إلى صوركم وأموالكم ولكن ينظر إلى قلوبكم وأعمالكم » [صحيح مسلم] + 2 questions ; الأعداد القبلية : أحفظ حديث الدرس المقبل — أشرح: طلع علينا، أثر السفر + ما هي أركان الإيمان؟).
- ZOOMS TRANCHÉS : p20 exemple 2 = « عن صلاة الظهر / عن السنة » (la lecture الظهر du VLM confirmée par crop 280%) ; p21 « ومن هاجر لقصد دنيوي فإنما حظه » ; p22 التقويم n°4 = « التي لحقت بالإخلاص من خلال الحديث » ; p22 الأعداد item 1 = « أشرح: طلع علينا – أثر السفر » (vocabulaire préparatoire au hadith de Jibrīl — résolu par le contexte du hadith à venir).
- RÉDACTION : scripts-ia2/livraisons/hadith-5ep/pdf-2.html (9 890 car) — 10 sections h2 dont nouvelle rubrique « Notice biographique du transmetteur » (ترجمة الراوي, présente dans ce manuel) ; hadith traduit intégralement ; conventions hadith-1ep + translit scientifique.
- QA : qa-lesson.py PASS — 9 890 car, 0 arabe hors spans, 6 guillemets appariés, 0 apostrophe droite. VERIF : verify-hadith5-pdf2.py — 25 contrôles OK / 0 échec (garde-doublon vide avant pose, matière 'Umar/Nufayl/muttaqun/i'tikāf/ẓuhr/Umm Qays/Ṭabarānī/Abū Hurayra/ṣaḥīḥ Muslim/23 AH, htmlFr posé == source).
- POSE : hand-set-ia2.py hadith-5ep pdf-2 → 1 emplacement, 9 890 car, registre IA-2 → 2. hadith-5ep : 2/29 leçons FR.
- INCERTITUDES CONSIGNÉES (mineures) : (1) p19 استخلاص n°1 « أحدد/أحد موضوع الحديث » — FR rendu « J'identifie le sujet du hadīth » ; (2) p21 « والإخلاص تقوية لمراتب الأعمال وفضائلها » — adjudiqué par le contexte grammatical (variantes VLM : يرفع/تنقطع) ; (3) p21 « فإنما حظه » (lecture convergente) ; (4) p20 « ولولا هذا اللفظ لاقتصى اللفظ الأول » — forme finale lاقتصى/لاقتصر incertaine, FR neutre (« la première aurait suffi ») ; (5) rubrique p22 القبلية/المقبليّة — FR identique (« La préparation »).
- Sync git : fetch + rev-list 0/0 avant production ; push immédiat après livraison (règle de vague).

Stage Summary:
- LIVRÉ : leçon 2 hadith-5ep « Les actes ne valent que par les intentions » (pdf-2, pp. 18-22, 9 890 car, registre IA-2 → 2) — hadith-5ep 2/29.
- MÉTHODE : le pair « lecture directe de l'agent » tranche désormais systématiquement les points lettres à lettres (les crops 280% confirment/réfutent le VLM : الظهر confirmé, لحقت confirmé).
- Prochaine priorité : slot pdf-3 (leçon 3 — الإسلام والإيمان, hadith de Jibrīl, pp. 23-27) ; git fetch 0/0 avant production ; PARALLÈLE : 1.

---
Task ID: Z2-3
Agent: IA-2 (Z.ai, compte parallèle, session web-db9f75eb, trace 1a1d0485336fb965, tick 2026-11-12)
Task: LIVRAISON leçon 3 hadith-5ep (pdf-3 — « L'islam et la foi », الإسلام والإيمان, hadith de Jibrīl, 2ᵉ hadith des Quarante, PDF pp. 23-30) — 8 pages, la plus longue leçon du manuel.

Work Log:
- Reprise de séance : lectures VLM pleine-page p.23-30 déjà produites (glm-5v-turbo, 150 dpi) + planches s3-* / crops z3-* générés en séance précédente → ADJUDICATION FINALE PAR LECTURE DIRECTE de l'agent (planches s3-023, 023b, 024, 024b, 025, 026, 027, 028, 029, 030 + micro-crops ciblés ×3 à ×8) : p23 (tamhīd : لَا يَكُونُ الْعَبْدُ مُسْلِمًا حَقًّا إِلَّا إِذَا اسْتَقَرَّ عَلَى أَرْكَانِ الإِسْلَامِ وَالإِيمَانِ عِلْمًا وَاعْتِقَادًا وَعَمَلًا وَسْلُوكًا... — l'« استقرب » du VLM tranché « استقرَّ » ; objectif 3 فِي وُجْدَانِي وَسْلُوكِي), p24 (fin du hadith canonique + glossaire : طَلَعَ عَلَيْنَا=أَيْ ظَهَرَ لَنَا ; رَجُلٌ=جِبْرِيلُ...فِي صُورَةِ رَجُلٍ لَا يَعْرِفُونَهُ ; أَثَرُ السَّفَرِ=عَلَامَةُ السَّفَرِ وَهَيْئَتُهُ ; فَعَجِبَنَا لَهُ وَيُصَدِّقُهُ=...سُؤَالَ الْعَارِفِ الْمُحَقِّقِ الْمُصَدِّقِ ; الإِيمَانُ=التَّصْدِيقُ وَالاسْتِسْلَامُ وَقَبُولُ الشَّرِيعَةِ — le tā entre les deux sīn tranché au ×3), p25 (تحليل : حَدِيثٌ عَظِيمٌ...فَهُوَ كَالأُمِّ لِلسُّنَّةِ كَمَا سُمِّيَتِ الفَاتِحَةُ أُمَّ القُرْآنِ ; مَرَاتِبُ ثَلَاثٌ لِلدِّينِ ; فَالإِسْلَامُ مُدْخَلٌ وَأَرْكَانٌ مَحْدُودَةٌ ; وَالإِحْسَانُ كَمَالٌ فِي الاِنْفَاذِ وَرُسُوخٌ فِي حُضُورِ الْجَنَانِ ; وَهَذَا بَيَانٌ مَا يَتَضَمَّنُهُ الْمَقْطَعُ الأَوَّلُ... ; الإسلام في اللغة/الشرع + أركانه خمسة + « وسيأتي في حديث: بُنِيَ الإسلامُ على خمسٍ » — reconstruction de la fin de phrase, hors zones plated), p26 (الإيمَانُ: التَّصْدِيقُ الجَازِمُ...دُونَ أَنْ يُخَالِطُهُ شَكٌّ أَوْ تَرَدُّدٌ ; هُوَ وَحْدَهُ الْوَاجِبُ الْوُجُودِ — le « الجُود » du VLM tranché ; مُتَصَرِّفٌ فِيهَا بِمَشِيئَتِهِ ; يَفْعَلُ فِي مُلْكِهِ مَا يُرِيدُ ; الْمَنْشَأُ الأَصْلِيُّ لِكُلِّ عَقَائِدِ الإِيمَانِ وَأَعْمَالِهِ ; يُبْنَى عَلَيْهِ الاِعْتِدَادُ بِالأَعْمَالِ ; يجبُ الإيمانُ بالملائكةِ...عبادُ الله مكرمونَ + versets), p27 (كُلَّ لَحَظَةٍ بِإِذْنِ اللهِ مِنْ كُلِّ مَكْرُوهٍ — لَحَظَة et non حَفَظَة ; وَيَسْتَحْضِرُ كَذَلِكَ مَقَامَ مَنْ عَنْ يَمِينِهِ وَشِمَالِهِ... ; الْكُتُبُ السَّمَاوِيَّةُ...لِيُبَلِّغُوهَا لِلنَّاسِ ; فَلَا يَكْمُلُ إِيمَانُ الْعَبْدِ حَتَّى يُصَدِّقَ بِأَنَّهَا كَلَامُ اللهِ ; الرُّسُلُ: جَمْعُ رَسُولٍ؛ وَهُوَ: مَنْ أُوحِيَ إِلَيْهِ بِشَرِيعَةٍ وَأُمِرَ بِتَبْلِيغِهَا ; verset البقرة sur لَا يُفَرِّقُ بَيْنَ أَحَدٍ مِنْ رُسُلِهِ), p28 (اليَومُ الآخِرُ هُوَ: يَومُ القِيامَةِ؛ وَسُمِّيَ بِاليَومِ الآخِرِ لِأَنَّهُ لَا يَومَ بَعْدَهُ ; دَارُ ثَوَابٍ وَجَزَاءٍ لِلْمُحْسِنِينَ وَالْمُفْسِدِينَ ; وأخبرَ به النبيُّ الأمينُ ; اليَقِينُ بِأَنَّ الجَزَاءَ عَلَى العَمَلِ وَاقِعٌ لَا مَحَالَةَ ; فَلَنْ يَضِيعَ عَمَلًا لِعَامِلِهِ وَلَا حَقَّ لِصَاحِبِهِ ; الإيمانُ بالقَدَرِ هُوَ: التَّصديقُ الجازمُ بأنَّ اللهَ تَعَالَى خَالِقُ الأشياءِ ومُقَدِّرُ المُقادِيرِ...وَلَا يَخْرُجُ شَيْءٌ عَنْ إِرَادَتِهِ وَتَدْبِيرِهِ ; verset الصَّافَّات: 96 — le « الصفّ » du VLM corrigé), p29 (bullet التنبيهُ إلى أنَّ السُّؤَالَ مِنْ أَسْبَابِ تَحْصِيلِ العِلْمِ + verset النَّحْل: 43 — le « الشُّعَرَاء » du VLM corrigé ; بِلِسَانٍ سُؤُولٍ، وَقَلْبٍ عَقُولٍ), p30 (استثمار : verset الأنفال: 2 + عَنْ أَبِي صَالِحٍ عَنْ أَبِي هُرَيْرَةَ + الإيمانُ بضْعٌ وسبعونَ شُعْبَةً — شُعْبَة maintenu contre « بَابًا » du VLM, convergent avec l'استخلاص « شُعَبٌ مُتَعَدِّدَةٌ »).
- DÉCISION ÉDITORIALE : citations coraniques normalisées à la convention du corpus (hadith-1ep/12797…) « … » (Sourate X — verset N) — les parenthèses ornementales ﴿﴾ étant rejetées par qa-lesson (plage arabique U+FD3E/FD3F) ; outil consigné scripts-ia2/fix_versets-h5-03.py (idempotent, 2 passes + dédoublonnage).
- RÉDACTION : scripts-ia2/livraisons/hadith-5ep/pdf-3.html (17 004 car) — 9 h2 / 5 h3 (même profil que pdf-2) ; hadith de Jibrīl traduit INTEGRALEMENT ; les 6 piliers de la foi en sous-sections fortes ; conventions hadith-1ep + translit scientifique.
- QA : qa-lesson.py PASS — 17 004 car, 0 arabe hors spans, 12 guillemets appariés, 0 apostrophe droite. VERIF : verify-hadith5-pdf3.py — 38 contrôles OK / 0 échec (garde-doublon, matière Jibrīl/'Umar/9 références coraniques/Tirmiḏī/Fatḥ al-Bārī/soixante et quelques branches/salaf-khalaf, htmlFr posé == source).
- POSE : hand-set-ia2.py hadith-5ep pdf-3 → 1 emplacement, 17 004 car, registre IA-2 → 3. hadith-5ep : 3/29 leçons FR.
- INCERTITUDES CONSIGNÉES : (1) p25 « ظَلَائِفِ الأَعْمَالِ » — lecture directe ×5 ظلائف, variantes VLM وظائف/ظوائف/ظواهر ; FR « formes vertueuses des actes » ; (2) p25 السَّمِحُ/السَّمَاحُ — FR identique (« tolérante ») ; (3) p25 « الْمَقْطَعُ الأَوَّلُ » conservé (la leçon 4 traitera la 2ᵉ section) ; (4) p26 ref imprimée [الأنبياء: 26-27] avec le texte de Taḥrīm 6 (convergent VLM+planche) — conservé tel imprimé ; (5) p27 ref [البقرة: 284] imprimée pour un texte de 285 — conservée ; (6) p28 [الḤadīd] : 22 imprimé selon la logique du texte (VLM 21, non vérifiable au niveau du chiffre) ; (7) p27 « وَأَلَّا يُجْتَرَمُهُمُ وَتَوْقِيرُهُمْ » — forme imprécise, FR neutre (« inviolabilité et vénération respectées ») ; (8) p28 « إِنْ خَيِّرًا وَإِنْ شَرَّا فَشَرَّ » — FR neutre (« le bien par le bien, le mal par le mal ») ; (9) p27 « الْكَائِنَاتِ الَّذِينَ يُكَتِّبُونَ » — accord nominatif/verbe incohérent, FR neutre ; (10) p29 source de la citation Ibn 'Abbās « فتح الباري – تحرير المتن – المسند للإمام أحمد » — lecture directe, identification bibliographique de « تحرير المتن » non vérifiée ; (11) p27 قُدْوَةً بِشَرِيعَةٍ مُتَتَالِيَةٍ/مُتَالِيَةٍ — FR identique ; (12) p25 fin « وَسَيَأْتِي فِي حَدِيثٍ: بُنِيَ الإِسْلَامُ عَلَى خَمْسٍ » — reconstruction contextuelle (hors zones plated).
- Sync git : fetch en cours de production (IA-1 a poussé 27b417d, zone tr-tmp/vlm-413 — zéro fichier commun) ; rebase puis push immédiat (règle de vague).

Stage Summary:
- LIVRÉ : leçon 3 hadith-5ep « L'islam et la foi » (pdf-3, pp. 23-30, 17 004 car, registre IA-2 → 3) — hadith-5ep 3/29.
- MÉTHODE : lecture directe de l'agent sur planches ×2 et micro-crops ×3-×8 — le VLM s'est trompé 4 fois sur des lettres/références décisives (استقرَّ, الواجب الوجود, الصافّات, النحل) : la règle « le pair direct tranche » se confirme.
- OUTIL : fix_versets-h5-03.py consigné pour la convention « … » (Sourate X — verset N) sur les futures leçons coraniques.
- Prochaine priorité : slot pdf-4 (leçon 4 — الإحسان وأمارات الساعة, suite du hadith de Jibrīl, pp. 31-35 env.) ; git fetch 0/0 avant production ; PARALLÈLE : 1.
