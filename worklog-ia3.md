# worklog-ia3 — chantier Minhāj (IA-3, secondaire) — série W, append-only

> IA-3 = machine du secondaire (`content/books/*-es.json` et `*-tanawi-*.json`).
> Périmètre et règles : `interne/PROTOCOLE-TROIS-IA.md` §2 + `interne/MISSION-IA-3.md`.
> GitHub = source de vérité unique ; 1 livraison = 1 commit + `git pull --rebase origin main`
> + push + entrée de journal ; vague de 1 à 4 documents ; QA avant chaque livraison.

## W1 — 2026-11-17 — démarrage IA-3, claim fiqh-tanawi-3, typo 15355/16211/16212/19353
Task ID: W1
Trace: 3af9c47be21d8065-w1

- Démarrage : clone frais `--filter=blob:none` depuis github.com/Sounawa/minhaj
  (→ `minhaj-repo/`) ; `git fetch origin main` ; `git rev-list --count HEAD..origin/main`
  = **0** (aligné, HEAD ccef3b5 = R717).
  Note d'environnement : `scripts/session-start.sh` = exit 2 sur le bac IA-1
  (`/home/z/my-project`) — son fetch complet de l'historique (~7 Go, trois
  `tmp_pack_*` abandonnés, nettoyés) ne tient pas sur le disque du bac aux côtés
  des deux clones ; le script a au passage ajouté `origin` au bac IA-1 (effet de
  bord consigné). L'alignement IA-3 est vérifié directement sur le clone (rev-list 0).
- **Aucun token GitHub dans le bac** (GH_PAT absent des variables, `~/.netrc` absent,
  `gh` absent) : push bloqué en attendant l'utilisateur ; le clone public fonctionne
  sans token (lecture seule). Consigne : 1 seule livraison non poussée, jamais plus.
- Scan global `scripts-ia2/qa_corpus.py` (exécuté, non modifié) : rapport complet dans
  `scripts-ia3/tmp/scan-w1.txt` (copie utilisateur : `download/scan-typo-secondaire-w1.txt`)
  — 849 docs à défauts (807 durs) ; secondaire = 351 docs (341 apostrophes droites,
  23 guillemets, 21 balises, 25 « arabe hors span »). Les `*-es` sont propres ; les
  défauts sont concentrés dans les `*-tanawi-*`.
- Choix du 1er livre : **fiqh-tanawi-3** — 32/32 docs à apostrophes droites pures
  (0 autre défaut dur), aucun claim antérieur (`git log` vérifié). Claim posé au
  commit de cette livraison.
- Outils créés (zone IA-3) : `scripts-ia3/fix-typo.py` (’/ʿ/ʾ hors balises, hors
  commentaires HTML, hors spans RTL toutes formes nested-aware ; U+202F avant
  `;:!?»` — entité `&nbsp;` incluse — et après « ; doubles espaces → simple) et
  `scripts-ia3/verify-diff.py` (vérification indépendante du diff). Convention §5
  appliquée avec vérité terrain corpus (17 nov. 2026) : ʾ = hamza après voyelle
  longue (Muwaṭṭaʾ ×39, ḥunafāʾ, al-ḥamrāʾ, ḥayāʾ), ʿ = ʿayn (ʿatīq ×44, ʿArafa) ;
  carte de mots vérifiée dans l'outil ; une incertaine = doc non écrit + consigné.
- **Livraison (vague 1/4)** : 15355 (intro, 23 apos), 16211 (4), 16212 (3), 19353 (2)
  — 32 apostrophes classées : **19 ʿ + 13 ʾ, 0 ’ française** (les élisions françaises
  de ces docs étaient déjà ’), 0 incertaine ; **686 normalisations U+202F**
  (276+95+133+182 : `&nbsp;` avant ponc et `«&nbsp;` → U+202F unique, règles de
  `qa-lesson.py`) ; 0 double espace.
  3 apostrophes de l'inventaire de signes « (ṣ, ḍ, ṭ, ḥ, ') » classées ʾ par
  parallélisme avec « Muwaṭṭaʾ » dans la même phrase (l'expression n'existe que dans
  ce livre) — **incertaine résiduelle consignée** : passable ʿ si le manuel imprimé
  montre l'ʿayn ; à confronter au PDF quand il sera disponible.
- **QA** : `scripts-translate/qa-lesson.py` (outil officiel) sur copie extraite de
  chaque doc → **QA OK ×4** (0 arabe, guillemets appariés, balises appariées, 0
  apostrophe droite). `verify-diff.py` : **0 diff non autorisé** — chaque caractère
  changé est une substitution répertoriée (32 apos + 686 narrow), résidu 0 des deux
  côtés ; zones protégées (spans RTL, balises, commentaires) identiques octet par
  octet ; JSON round-trip indent-2 identique (pas de réarrangement).
- 2 observations consignées (défauts vus chez les autres = jamais corrigés par IA-3) :
  (1) `qa_corpus.py` classe en « arabe_hors_span » des spans RTL imbriqués
  (hadith-tanawi-3 : 9 docs) — artefact de son regex non-greedy ; à confronter au
  cas par cas avant toute correction de ces docs ;
  (2) le fix officiel `qa-lesson.py`, face à « &nbsp;: », insère un U+202F ENTRE
  l'entité et la ponctuation (rendu = double espace) ; nos corrections convertissent
  l'entité en U+202F unique, conforme à l'état des livres propres (0 entité chez eux).
- Push : `git pull --rebase origin main` puis `git push origin main` tentés →
  **échec (aucun token)**. État : 1 livraison locale non poussée (la seule
  autorisée). Dès réception du token : `git push origin main` puis aligner les
  compteurs. `scripts-ia3/tmp/` (scan + extraits QA) volontairement non suivi git.
- **Complément W1 — push vérifié EN LIGNE** : token reçu de l'utilisateur (17 nov.) ;
  `git pull --rebase origin main` (up to date) puis push → `3c45e8b..263f8ca
  HEAD -> main` ; refetch : `rev-list origin/main..HEAD = 0`, origin/main =
  263f8ca. **EN LIGNE vérifié** avant consignation (le point manqué du R716 ne
  sera pas refait).
  Incident d'environnement consigné : un premier push lancé sans `cd` explicite
  est parti sur le bac IA-1 (cwd du tour réinitialisé) et a déclenché un fetch
  complet (~2,9 Go) sur ce bac — tué avant tout rebase/push, `tmp_pack_*`
  supprimés, HEAD du bac IA-1 vérifié intact (1f6be86), livraison IA-3 intacte.
  Règle IA-3 adoptée : toujours `git -C /home/z/my-project/minhaj-repo …` ;
  token uniquement dans les commandes, jamais dans un fichier suivi ni un journal.

## W2 — 2026-11-17 — typo fiqh-tanawi-3 docs 19354, 19367, 19373, 19377 (vague 2/8)
Task ID: W2
Trace: 3af9c47be21d8065-w2

- Vague 2/4 docs du claim fiqh-tanawi-3 : **19354 (27 apos), 19367 (12), 19373
  (51), 19377 (17) = 107 apostrophes** classées **61 ʿ + 45 ʾ + 1 ’** (J'ai →
  J’ai, seule élision française de la vague), 0 incertaine ; **905
  normalisations U+202F** (304+184+239+178) ; 0 double espace.
- Carte de mots enrichie et restructurée dans `fix-typo.py` : les préfixes
  ambigus passent au niveau du **couple (fin du mot avant ', début du mot
  après ')** — taʿlīm/taʿzīr (ʿayn) vs taʾkhīr/taʾbīm (hamza), saʾala hamza vs
  aʿṭā ʿayn, muʿajjal/muʿdim/muʿtādan/muʿğama, maʿlūm, sharʿī, sharīʿa/charīʿa
  (exception à la règle hamza-après-voyelle-longue : الشريعة = ʿayn) ;
  nouveaux finaux : juzʾ, maliʾ, bayʿ, rajaʿa, rābiʿ, Jāmiʿ (précédent corpus
  ×5) ; nouveaux initiaux : ʿUmar, ʿan, ʿalā, ʿalay, ʿusri, ʿadmata, ʿayn,
  ʿaynin, ʿurūḍ, ʿazl, ʿĀdiyāt, ʿamal, ʿarḍin, ʿarḍi, ʿuzila. Outil
  `scripts-ia3/probe-words.py` ajouté (sondages de précédents).
- **Divergence consignée** (défaut vu ailleurs, jamais corrigé par IA-3) :
  le corpus porte **’Umar ×228** (artefact blanket qa-lesson d'autres zones)
  contre **ʿUmar ×51** (livres faits main) — la convention §5 impose ʿUmar
  (عمر) ; mes corrections produisent ʿUmar. Les livres d'autres zones restent
  en l'état (règle de zones) ; leurs propres passe typo devraient converger.
- QA : `qa-lesson.py` **PASS ×4** (0 arabe, guillemets/balises appariés, 0
  apostrophe droite) ; `verify-diff.py` : **0 diff non autorisé** (107 apos +
  905 narrow, résidu 0) ; régression vague 1 vérifiée au dry (0 apos restante).
- Push : `git pull --rebase origin main` + push + refetch → rev-list = 0
  (EN LIGNE vérifié).

## W3 — 2026-11-17 — typo fiqh-tanawi-3 docs 19383, 19388, 19395, 19407 (vague 3/8)
Task ID: W3
Trace: 3af9c47be21d8065-w3

- Vague 3/4 docs : **19383 (36 apos), 19388 (24), 19395 (16), 19407 (40) =
  116 apostrophes** classées **64 ʿ + 52 ʾ + 0 ’**, 0 incertaine ; **901
  normalisations U+202F** (219+209+195+278) ; 0 double espace.
- Carte étendue (toujours couple/mot vérifié) : maʿnā, faʿīl, mafʿūl, raʾs
  (rās vs farʿ — collision évitée), Saʿd, dfaʿū (misprint documenté du
  manuel), waqaʿa/mawqiʿa, maʿdūm/maʿtūh/muʿayyana, ğaʿala, mubaʾbira,
  manāfiʿ, tabaʿ/tatabbaʿ/tabʿ, sābiʿ/ṣāniʿ/waḍʿ, buḍʿ, qiṭʿ, farʿ/farʿī,
  mustaṣnaʾ, ʿiṣma, ʿaqd, ʿinda, ʿAbbās, ʿĀʾicha (ʿ initial + ʾ médial),
  Chāfiʿī. Correction d'un bug de casse : clés de carte désormais toutes
  minuscules (La Muwaṭṭa' → muwaṭṭa matchait plus après .lower()).
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**
  (résidu 0) ; régressions vagues 1-2 vérifiées au dry.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W4 — 2026-11-17 — typo fiqh-tanawi-3 docs 19441, 19448, 19449, 19452 (vague 4/8)
Task ID: W4
Trace: 3af9c47be21d8065-w4

- Vague 4/4 docs : **19441 (45 apos), 19448 (37), 19449 (45), 19452 (35) =
  162 apostrophes** classées **101 ʿ + 61 ʾ + 0 ’**, 0 incertaine ; **908
  normalisations U+202F** (202+189+230+287) ; 0 double espace.
- Carte étendue : rabʿ/rubʿ, Nāfiʿ, ğamʿ, māniʿ, tachaffuʿ, maʿlūl, maʿa
  (مَعَ), maʿrūf, muʾaqqab (hamza), muʿāwaḍa, muʿtamad, muʾakhkhar (hamza),
  charʿī, chafʿa, mustaʿrāʾ, istiʿrāʾ, manfaʿa, ʿaqār, ʿilla, ʿAlīch/ʿAlīsh,
  ʿurf/ʿurfan, ʿimāra, ʿachar, ʿUqbarī, ʿiwaḍ, ʿaraḍ, ʿayb, ʾadam/ʾadaman
  et ibtighāʾ — **nouvelle branche « hamza initiale »** (WORD_INITIAL_HAMZA)
  distinguée des initiales ʿayn.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W5 — 2026-11-17 — typo fiqh-tanawi-3 docs 19456, 19492, 19495, 19496 (vague 5/8) + bug entités réparé
Task ID: W5
Trace: 3af9c47be21d8065-w5

- Vague 5/4 docs : **19456 (23 apos), 19492 (32), 19495 (61), 19496 (58) =
  174 apostrophes** classées **122 ʿ + 52 ʾ + 0 ’**, 0 incertaine ; **1071
  normalisations U+202F** (175+235+248+413) ; 0 double espace.
- Carte étendue : taʾwīl (hamza), iʾdār, yuʾdhiru, aʾdhara (hamza médial),
  waʿd, baʿīr, muʿğam, ṭaʿām, yaʿnī, juʿl, zaʿāma, zaʿīm, Ğāmiʿ, ʿilm, ʿAmr,
  ʾadhara (hamza initiale).
- **Bug trouvé et réparé (attrapé par verify-diff.py, jamais en ligne)** : la
  règle générique U+202F voyait le `;` INTERNE de l'entité `&nbsp;` comme une
  ponctuation française quand l'entité précède une balise (« `&nbsp;</p>` »
  devenait « `&nbsp\u202f;` » — entité cassée). 5 occurrences corrigées dans
  le livre ; `fix_text_segment` protège désormais les entités (comme
  qa-lesson.py) après la conversion `&nbsp;+ponc → \u202f+ponc`. Les vagues
  1-4 ne contiennent aucune occurrence du motif (verify-diff 0 diff à chaque
  livraison) — rien à reprendre côté en ligne.
- QA : `qa-lesson.py` **PASS ×4** (re-vérifié après réparation) ;
  `verify-diff.py` **0 diff non autorisé**, résidu 0.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W6 — 2026-11-17 — typo fiqh-tanawi-3 docs 19500, 19503, 19515, 19517 (vague 6/8)
Task ID: W6
Trace: 3af9c47be21d8065-w6

- Vague 6/4 docs : **19500 (23 apos), 19503 (26), 19515 (21), 19517 (49) =
  119 apostrophes** classées **57 ʿ + 62 ʾ + 0 ’**, 0 incertaine bloquante ;
  **879 normalisations U+202F** (210+270+219+180) ; 0 double espace.
- Carte étendue : tawāṭuʾ, tanāzuʿ, mutaʿaddin, taʿaddud, charʿan, taʿlīl,
  maʿdim, daʿwā, muʿaddī/muʿaddā, ʿadīm, ʿuqba, ʿichrūn, maʾrā,
  ʾastakhliḍ/ʾastakhliṣ.
- **2 incertaines tranchées linguistiquement + consignées** (aucun précédent
  corpus) : (1) « 'astakhliḍ/ṣ » — hamzat **wasl** de استخلف/استخلص citée de
  l'imprimé → rendue ʾ (convention §5) ; passable en non-transcrite selon le
  système du manuel ; (2) « ma'rā » (مَعْرَاء, tache, Mukhtaṣar) → maʾrā
  (hamza). À confronter au PDF quand disponible.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W7 — 2026-11-17 — typo fiqh-tanawi-3 docs 19537, 19544, 19601, 19670 (vague 7/8)
Task ID: W7
Trace: 3af9c47be21d8065-w7

- Vague 7/4 docs : **19537 (21 apos), 19544 (31), 19601 (32), 19670 (37) =
  121 apostrophes** classées **73 ʿ + 48 ʾ + 0 ’**, 0 incertaine ; **814
  normalisations U+202F** (301+180+191+142) ; 0 double espace.
- Carte étendue : niʿma, yaʿqid, tanaʿqid, iʾāra, istaʾlafa, istiʾlāf, maʿīb,
  aqaʾada, taʿaddī, zarʿ, nafʿ, ʿinān (×15 dans 19670), ʿiyāl, ʿadāla,
  ʿAllāma, ʿudhr, et **racines consonantiques** b-ḍ-ʿ / ʿ-n-n (correctif
  word_before : hyphen final de « b-ḍ-' » et hyphen initial de « '-n-n »
  élagués avant la recherche de carte).
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W8 — 2026-11-17 — typo fiqh-tanawi-3 docs 19671, 19744, 19756, 19757 (vague 8/8) — LIVRE TERMINÉ
Task ID: W8
Trace: 3af9c47be21d8065-w8

- Vague 8/4 docs (dont les deux index) : **19671 (18 apos), 19744 (18),
  19756 (88), 19757 (144) = 268 apostrophes** classées **214 ʿ + 54 ʾ + 0 ’**,
  0 incertaine ; **736 normalisations U+202F** (167+193+111+265) ; 0 double
  espace. Carte étendue (index des figures et des sources, noms propres) :
  aqṭaʿa, maʿdin, iʾlām, marāğiʿ, dharāʾiʿ (double signe — word_before
  traverse désormais une apostrophe interne), Muʿīn, ẓamʾān, Rabʿī,
  iʾtirāḍ, istiʾāra, Raʾūf, chāfiʿite, riʾāsa, maʿārif, Marʿab, Taʾrīfāt,
  Jaʿfī, Fuʾād, aʾlām, Achʿath, Chuʿayb, Saʿīd, Yaʿqūb, Muʾassasa, maṭbaʿa,
  saʾāda, Muʿādh, Maʿbad, Thaʿālabī, Jaʿfarī, muʿjam, muʿāṣira, Muwattaʾ,
  Aʿrāb, Naʿīm.
- **Règle générale posée et consignée** (W8) : ' initial de mot = **ʿayn par
  défaut** dans la translittération de ce corpus (ʿAbd, ʿAlī, ʿilm, ʿĪsā,
  ʿulamāʾ, ʿAmir…) ; l'hamza initiale reste l'exception (liste
  WORD_INITIAL_HAMZA : ʾadam, ʾadaman, ibtighāʾ, aʾdhara, ʾastakhliḍ/ṣ).
- **1 incertaine consignée** : « Ru'īnī » (al-Ḥaṭṭāb ar-Ruʾīnī) rendu ʾ
  (hamza) — la lecture ar-Ruwaynī (sans hamza, w) est possible selon la
  source ; à confronter au PDF.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- **BILAN DU LIVRE fiqh-tanawi-3 (claim W1, terminé W8)** : 32/32 leçons
  corrigées (intro déjà propre) — **1099 apostrophes droites classées :
  711 ʿ + 387 ʾ + 1 ’** (somme exacte des vagues W1-W8, dont les 4
  parenthèses d'inventaire de signes classées ʾ par parallélisme
  Muwaṭṭaʾ) et **6900 normalisations U+202F** ; 0 incertaine bloquante ;
  2 incertaines résiduelles consignées (ʾastakhliḍ/ṣ wasl, Ruʾīnī). Scan
  global après livre : **fiqh-tanawi-3 disparu du rapport qa_corpus (0 dur,
  0 soft)** ; corpus global 807 → 775 docs à défauts durs (−32 = ce livre).
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W9 — 2026-11-17 — claim ulum-hadith-tanawi-1 ; typo pdf-mut23h2q-112, 113, 114, 115 (vague 1/8)
Task ID: W9
Trace: 3af9c47be21d8065-w9

- Deuxième livre claimé : **ulum-hadith-tanawi-1** (30 docs à apostrophes
  droites pures, aucun claim antérieur vérifié) — vague 1/4 docs :
  **pdf-mut23h2q-112 (17 apos), 113 (9), 114 (33), 115 (27) = 86
  apostrophes** classées **55 ʿ + 31 ʾ + 0 ’**, 0 incertaine ; **289
  normalisations U+202F** (77+58+82+72).
- Vocabulaire des sciences du hadith cartographié (précédents corpus
  sondés) : **Qurʾān** (ʾ, ×15 en corpus), badʾ (بدء), muʿallal, Achʿarī,
  Maʿālim, naʿlayn, Chuʿba, ḍaʿīf ×1, ḍaʿf, muʿḍal, mutābaʿa, munqaṭiʿ ×2.
- Correctif outil : après la traversée des apostrophes internes
  (dharāʾiʿ), le tail médial peut porter un ' initial — élagué
  (`lstrip("'")`) ; et le vérificateur modélise désormais le
  réordonnancement « + course d'espaces (l'espace fine passe devant les
  entités, équivalent qa-lesson) — motif «&nbsp;&nbsp;\u202f →
  «\u202f&nbsp;\u202f légitimé.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non
  autorisé** ; les 4 docs ont disparu du scan.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W10 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2q-116, 117, 118, 119 (vague 2/8) + correction istiʿāra
Task ID: W10
Trace: 3af9c47be21d8065-w10

- Vague 2/4 docs : **pdf-mut23h2q-116 (95 apos), 117 (55), 118 (36),
  119 (77) = 263 apostrophes** classées **160 ʿ + 103 ʾ + 0 ’**, 0
  incertaine ; **350 normalisations U+202F** (94+70+90+96).
- Carte étendue (tābiʿ/tābiʿūn/mutābaʿa/ʿāt, maqṭūʿ — exception
  long-vowel pour ū, muʿallal, Qurʾān, badʾ, Achʿarī, Maʿālim, naʿlayn,
  Chuʿba, ḍaʿīf/ḍaʿf, muʿḍal, Bardhaʿī, istiʿāna, Aʿraj, Maʿrifa, yuʿtar,
  muʿtazilite, Dhuʿayb, yajʿal, Nasaʿī, yuwammaʾu).
- **Correction de MON propre contenu W7/W8 (livre 1, doc 19756)** : deux
  « istiʾāra » (استعارة = ʿAYN, pas hamza) — posées à tort ʾ par la carte
  ("isti","āra") — réparées en istiʿāra (le mot est scindé par une balise
  <em>, d'où la recherche contiguë manquée au premier passage) ;
  l'entrée de carte est corrigée (« isti », « āra ») → ʿ. istiʾlāf
  (استئلاف, hamza) reste correct. Consigné comme leçon : les mots
  translittérés scindés par balises échappent aux sondages contigus.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).







## W11 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2q-120, 121, 122, 123 (vague 3/8)
Task ID: W11
Trace: 3af9c47be21d8065-w11

- Vague 3/4 docs (la leçon du muʾannan/muʿanʿan) : **pdf-mut23h2q-120 (37
  apos), 121 (126), 122 (46), 123 (95) = 304 apostrophes** classées
  **208 ʿ + 96 ʾ + 0 ’**, 0 incertaine ; **458 normalisations U+202F**
  (87+104+149+118).
- Carte étendue : muʾannan/mouʾannanoun (ʾ, glose du doc), muʿanʿan
  (ʿ,ʿ), tābiʿ/tābiʿūn, maqṭūʿ (exception long-vowel ū), Hāniʾ/Hāniʾin,
  iʿnana, ʿanʿana, rakaʿa, samiʿat, Shuʿba, Samʿānī, Bardhaʿī, istiʿāna,
  Aʿraj, Maʿrifa, yuʿtar, muʿtazilite, Dhuʿayb, yaʿlū, murtafiʿ, bisabʿ,
  yabdaʾ, yuwammaʾu, yajʿal.
- **1 incertaine consignée** : « mu''an » (double signe du corpus, forme
  abrégée) rendu **muʾʾan** par parallélisme avec la glose du document
  (« mou'annanoun » = muʾannanoun, hamza) — lecture muʿʿan possible ; à
  confronter au PDF. Le tri des couples passe aux préfixes les plus longs
  d'abord (mu'an'an avant mu'an) ; tail médial élagué des apostrophes
  bordantes (strip).
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W12 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2q-124, 125, 126, 127 (vague 4/8)
Task ID: W12
Trace: 3af9c47be21d8065-w12

- Vague 4/4 docs : **pdf-mut23h2q-124 (59 apos), 125 (62), 126 (130),
  127 (172) = 423 apostrophes** classées **312 ʿ + 111 ʾ + 0 ’**, 0
  incertaine ; **532 normalisations U+202F** (95+98+174+165).
- Carte étendue : fiʿlin, tābiʿīn/ī, jawāmiʿ, rafʾan/rafʾ, yarfaʾuhu,
  shāfiʿītes, Masʿūd, Aʿmach, Ṣanʿānī, chaʾīrin, qiṭʿatun, yamnaʿu,
  aʾyāhu/aʾḍalahu, ḍuʿafāʾ, iʾḍāl, iʾrsāl, yaʾjal, yuʿraf, munqaṭiʿs,
  kānatimraʾatī (amalgame d'imprimé), iʾdād, abʿadakanna (print),
  muʿḍila, yumʿiʾaḥadukum (double signe), aʿmālu, yaʿqqu, Chaʿbī,
  tajtamiʾu, ḍaʾāmahu (lecture récusée du doc — consignée), yuʾmar,
  istiʾdhān, yasmaʿ, ṭaʿ.
- Initiales hamza consignées au fil : ʾaw, ʾaḥadukum, ʾilā, ʾabīhi,
  ʾinnī, ʾinnamā, ʾab'adakanna.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W13 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2q-128, 129, 130, 131 (vague 5/8)
Task ID: W13
Trace: 3af9c47be21d8065-w13

- Vague 5/4 docs : **pdf-mut23h2q-128 (67 apos), 129 (52), 130 (32),
  131 (119) = 270 apostrophes** classées **207 ʿ + 63 ʾ + 0 ’**, 0
  incertaine ; **644 normalisations U+202F** (245+89+146+164).
- Carte étendue : taʿammud/taʾammul, taʿlamu/taʿlama, nawʿāni, Maʿmar,
  iʾlāl, jamʿin/jamʿ, mutaʿammidan, yatabawwaʾa, maqʿadahu, yanʿarif,
  rakʿa/rakaʾa, yataʿarraf, Luhayʾa, ṣanaʾta, samiʿtu, mutābiʿ, wuqūʿ
  (exception long-vowel ū), ʾaḥadkumu, ʾidhā (hamza initiale), rukʿatayni.
- **1 incertaine consignée** : « mu'aḍḍal » rendu muʾaḍḍal (hamza) —
  lecture muʿḍal possible ; à confronter au PDF.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W14 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2q-132, 133, 134, 135 (vague 6/8)
Task ID: W14
Trace: 3af9c47be21d8065-w14

- Vague 6/4 docs : **pdf-mut23h2q-132 (35 apos), 133 (134), 134 (44),
  135 (92) = 305 apostrophes** classées **210 ʿ + 95 ʾ + 0 ’**, 0
  incertaine ; **620 normalisations U+202F** (131+200+118+171).
- Carte étendue : saʾaltu, Aʿwar, maʿnan, chiʾta, baʿḍi, aʾimmati,
  muṭṭaliʿīna, Ḍabbaʿī, naʿlam, faqʿud/tafʿud (récusan), yuʿtaqad,
  aʿqābi, yuṭʾima, maʿak, jiʾtuhum, baʿda, Ṣanʿāʾ (double : ʿ puis ʾ),
  Muʿāwiya, rufʾahu, yaqaʿu, yaʾkhudhna, muʾtalif, tajʾala/tajʾalū,
  raʾaytu, ruʾūs, muḍaʿṭaf, aʿẓamu, yaʿtaqidu, taʿlamūn, taqʿuda,
  yatawaḍḍaʾ.
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W15 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2r-136, 137, 138, 139 (vague 7/8)
Task ID: W15
Trace: 3af9c47be21d8065-w15

- Vague 7/4 docs : **pdf-mut23h2r-136 (82 apos), 137 (71), 138 (74),
  139 (106) = 333 apostrophes** classées **198 ʿ + 135 ʾ + 0 ’**, 0
  incertaine ; **654 normalisations U+202F** (173+100+167+214).
- Carte étendue : taʿaṣṣub, Juʿfī, taʿdīl, yaʿrifhu, khaṭaʾuhu,
  Sabīʿī, taʿṣīm, chayʾi, waḍaʾū, iʾtibār, raʾnu (OCR tronqué),
  ajmaʿū, ḍaʾfihī, mutaʿabbidīn, mustaʿmal, Shuʿab, Zurʾa, taʿmīm,
  maʾidatu, waḍʿi/waḍʿu, arbaʿa/arbaʿin, yaqiʿu, yaqṭaʿuhā, iʿjām,
  aʿrāḍi, ṭaʿn, taʿālā, yaʿtuddu, Tibiʿī (forme fautive citée),
  mukhtaraʾ, yatabawwaʾ, mawḍūʿ et ṣanūʿ (exceptions long-vowel).
- **2 lectures consignées** : « ya'hadu » rendu yaʿhadu (يعهد supposé,
  print douteux) ; « ya'idu » rendu yaʾidu (token OCR récusé par le doc).
- QA : `qa-lesson.py` **PASS ×4** ; `verify-diff.py` **0 diff non autorisé**.
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## W16 — 2026-11-17 — typo ulum-hadith-tanawi-1 pdf-mut23h2r-140, 141 (vague 8/8) — LIVRE 2 TERMINÉ
Task ID: W16
Trace: 3af9c47be21d8065-w16

- Vague 8/2 docs (bibliographie du livre) : **pdf-mut23h2r-140 (110 apos),
  141 (171) = 281 apostrophes** classées **224 ʿ + 57 ʾ + 0 ’**, 0
  incertaine ; **372 normalisations U+202F** (149+223).
- Carte étendue : Arnaʾūṭ, al-Bayyiʿ, marājiʿ (graphie j), Munʿim,
  Maṭbaʿa, muʾminīn, Qawāṭiʿ, Malʾ (ملء), Muʿṭī, Qalʿajī, maʿānī,
  Muʿaẓẓam, Yaʿlā, al-amʾan (المأمن, print), wāqiʿayn, muʿall, ʾandād
  (hamza initiale).
- QA : `qa-lesson.py` **PASS ×2** ; `verify-diff.py` **0 diff non autorisé**.
- **BILAN DU LIVRE 2 ulum-hadith-tanawi-1 (claim W9, terminé W16)** :
  30/30 leçons corrigées — **2265 apostrophes droites classées**
  (somme exacte W9-W16) et **3919 normalisations U+202F** ; 0 incertaine
  bloquante ; incertaines résiduelles déjà consignées (muʾʾan, yaʿhadu,
  yaʾidu, ḍaʾāmahu, muʾaḍḍal — tokens d'imprimé/OCR douteux, à confronter
  au PDF). Scan global après livre : **ulum-hadith-tanawi-1 disparu du
  rapport qa_corpus (0 dur, 0 soft)** ; corpus global 775 → 745 docs à
  défauts durs (−30 = ce livre).
- Push : pull --rebase + push + refetch → rev-list = 0 (EN LIGNE vérifié).

## BILAN DE SESSION IA-3 (W1-W16, 17 nov. 2026)
Task ID: W-bilan
Trace: 3af9c47be21d8065-w16

- **2 livres terminés, 62 documents corrigés, tout EN LIGNE** (aucune
  livraison non poussée) :
  - fiqh-tanawi-3 : 32/32 leçons — 1099 apostrophes (711 ʿ + 387 ʾ + 1 ’)
    + 6900 U+202F (W1-W8) ;
  - ulum-hadith-tanawi-1 : 30/30 leçons — 2265 apostrophes (W9-W16)
    + 3919 U+202F.
  - Total : **3364 apostrophes droites classées + 10 819 normalisations
    U+202F** sur 62 docs, QA qa-lesson PASS à chaque doc, verify-diff 0
    diff non autorisé à chaque livraison, corpus global 807 → 745 docs à
    défauts durs (−62 = ces deux livres).
- Reste du rapport Z1 à couvrir (13 livres, ~289 docs à défauts durs) :
  tafsir-tanawi-1 (32, avec guillemets/balises/arabe à trier), fiqh-tanawi-1
  (31), hadith-tanawi-1 (30), mantiq-tanawi-1 (30), taqtit-tanawi-1 (28),
  ulum-hadith-tanawi-2 (27), qiraat-tanawi-1 (22), fiqh-tanawi-2 (21),
  tafsir-tanawi-2 (21, 19 arabes hors span à examiner), faraid-tanawi-3 (19),
  faraid-tanawi-2 (17), hadith-tanawi-2 (1), + les 2 corrections de contenu
  déjà faites (entités &nbsp; wave 5, istiʿāra W10) consignées.
- Outils livrés dans scripts-ia3/ : fix-typo.py (règles + carte de mots
  vérifiée, protège entités, traverse apostrophes internes), verify-diff.py
  (vérification indépendante de chaque livraison), probe-words.py (sondages
  de précédents) ; tmp/ non suivi git.
- Incertaines résiduelles cumulées consignées (à confronter au PDF) :
  muʾʾan, ʾastakhliḍ/ṣ (wasl), maʾrā, Ruʾīnī, muʾaḍḍal, yaʿhadu, yaʾidu,
  ḍaʾāmahu, al-āfiʾī, inventaire de signes (ṣ,ḍ,ṭ,ḥ,ʾ) ×4.

## W17 — 2026-11-17 — typo fiqh-tanawi-1, 31/31 docs (LIVRE 3 TERMINÉ) — récupération de la session perdue R714-R715d
Task ID: W17
Trace: 1a1d675aa095fb41-w17

- Contexte : reprise post-recyclage — les vagues W1-W5 de la session
  R714-R715d (livres entiers ft3/ft1/ft2/far3/1es, commits b455a2f,
  3f1934b, b44cef2, 93a64d3 jamais poussés) étaient perdues avec le clone ;
  l'arbitrage a survécu sous scripts/ hors dépôt (w1-map.json 921 formes +
  w2-ft1-supp.json 244 formes ft1). Réconciliation position par position de
  ces cartes contre fix-typo.py : **810 accords**, 245 divergences examinées
  une à une (40 élisions françaises du doc-intro 11509 jamais traitées par
  R714-R715d, ~130 incertaines résolues par la carte session, ~20 conflits
  sémantiques arbitrés au tour même).
- Livraison : **31/31 docs fiqh-tanawi-1 — 1055 apostrophes droites
  classées** : **746 ʿ + 265 ʾ + 41 ’** (élisions du doc-intro 11509) +
  **3 bat'an → battan** (باتًّا, tāʾ géminé — consigné R714) ;
  **7552 normalisations U+202F** + doubles espaces.
- Carte étendue : ~60 couples médiaux (dharīʿa, mufāʿala, jamāʿa, maqlūʿan,
  bīʿuhā, mubāʿa, raḍāʿa, shufʿa, mubāyaʿa, midāfaʿa, jaʿala, Shuʿayb,
  (a)sh-Shāfiʿī/ites, al-Rabaʿī, al-Maʿāfirī, Ṣaʿīdī, Maʿdān, Muṣʿar,
  Yanaʿqidu, iʿtāna, tataʿayyana, taʿjal/taʿjīl, rābiʿan, nafʿan, ka-bayʿihi,
  al-bayʿāt, ṣanʿa, baʿd, kaʿk, baʿnī, maʿqūd, kalaʾa/kilāʾa/raduʾa (racine
  ك-ل-أ), tabiʿā, muʿāṭāʾa, taʾbīd, taʾdīb, al-muʾna, ḍaʾn (ضأن), abʿad,
  istiʾmān, ruʾya, raʾīnī, élisions dʾal-Dardīr/al-Dasūqī…) + 16 finales
  (tawābiʿ, silaʿ, tāsiʿ, majmaʿ, mawāniʿ, tabiʿ, taqṭaʿ, ḍaʿ, ḍarʿ, dafʿ,
  judhʿ, sharʿ, labaʾ, istiqraʾ, saʾ) + **WORD_FINAL_LONG_AYN** (ijtimāʿ,
  ijmāʿ, dhirāʿ, intifāʿ, madfūʿ, bayūʿ, buyūʿ, mabīʿ, maklūʿ — la règle
  ā/ī/ū→ʾ suspendue pour ces racines en ʿ) + initiales hamza (ʾaṭaytuk,
  ʾujjila, ʾalif) + règle dédiée bat'an (→ battan) avec autorisation
  verify-diff bornée au contexte bat|an ; règle U+202F passée en
  lookahead-only (remplace les espaces existants, n'insère jamais — cas
  »» et «« des fermetures imbriquées de 11905).
- Révisions de la carte session (consignées — supplantent R714-R715d) :
  ʿanhā = عنها (al-manhī ʿanhā, ʿayn), ʿubbirat = عُبِّرَت (palme fécondée,
  ʿayn), li-abʿad = أبعد (ʿayn), Ṣanʿāʾ = صنعاء (ʿ puis ʾ — la carte
  ʾʾ de R714 était fautive), al-aʿlām = الأعلام (hamza),
  muʿāṭāʾa = المعاطاة (ʿʿ de R714 révisé en ʿʾ).
- Décisions session confirmées par le texte même : kalīʾ = « de kalaʾa
  ad-dayn — il a différé » (racine ك-ل-أ) ; an-Nasāʾī, an-Nisāʾ, masāʾil,
  khaṣāʾ, ṣāʾigh hamza ; al-intifāʿ = الإنتفاع (ʿayn) ; taʿjīl تعجيل (ʿ)
  mais muʾajjal المؤجل (ʾ) — mots distincts. Arbaʾūn (11980 ×2) gardé ʾ tel
  qu'imprimé — parallèle arbaʾa aqsām / bi-arbaʾin vérifiés à l'image
  (W9-W16).
- Réparation structurelle consignée au commit W17a (6adb9c0) :
  11905/11909/11912 finissaient sur des balises vides suspendues
  (transcriptions tronquées déjà à HEAD) + un » manquant (11905) — réparé
  (pile contrôlée, guillemets appariés, qa-lesson PASS ×3) sinon la vague ne
  pouvait écrire ces 3 docs ; + correction consignée fiqh-tanawi-3 :
  al-muʾajjal bi-l-mawt (المؤجل — erreur latente de la carte (mu,ajja),
  1 occurrence, parallèle CORRECTION W10 istiʿāra).
- QA : qa-lesson **PASS ×31** (0 arabe, guillemets appariés, balises
  appariées, 0 apostrophe droite à chaque doc) ; **verify-diff 0 diff non
  autorisé** ; comptes 746 ʿ + 265 ʾ + 41 ’ + 3 battan = 1055 = total exact
  des ' du livre (1006 leçons + 49 intro) ; **fiqh-tanawi-1 disparu du scan
  (0 dur)** — corpus global **745 → 714 docs à défauts durs** (31 livres
  restants, ~42 800 ' dont hadith-3es/2es ~7 000, taqtit-tanawi-1 2 870,
  hadith-tanawi-1 2 537).
- Push : commits locaux W17a (6adb9c0) + W17 — GH_PAT absent du sandbox
  recyclé ; poussée au prochain tour avec token réinjecté.


## W18 — 2026-11-17 — typo fiqh-tanawi-2, 22/22 docs (LIVRE 4 TERMINÉ) — cartes R714-R715d récupérées
Task ID: W18
Trace: 1a1d675aa095fb41-w18

- Livraison : **22/22 docs fiqh-tanawi-2 — 641 apostrophes droites classées**
  : **458 ʿ + 183 ʾ** (5 ʿ + 2 ʾ préexistants dans le livre) + **2608
  U+202F** ; 0 élision nouvelle (le ’ français préexistant, 3850, couvre le
  texte). R715-R715d annonçait 485 ʿ + 156 ʾ — l'écart (~27 formes) vient
  des révisions consignées ci-dessous et de la convention elisions/’ de
  l'outillage actuel.
- Arbitrage : dry 578 classées + 63 incertaines → 60 résolues par
  w2-ft2-supp.json + w1-map.json (arbitrage R714-R715d retrouvé), 3
  seconds-signes luʾluʾ/luʾluʾa/laʾālīʾ arbitrés au tour (hamza لؤلؤ/لألئ).
- Révisions consignées (supplantent le supp R714-R715d) : **al-Ashʿath**
  (الأشعث, ʿayn — le supp ʾ était fautif ; père d'Abū Dāwūd),
  **al-Aṣmaʿī** (الأصمعي, ʿayn — canon ; aṣmaʾ الأصماء reste ʾ, mot
  distinct), **al-Aʿẓamī** (الأعظمي, ʿayn — la valeur héritée ʾʿ était une
  incohérence 2-chars/1-signe ; forme réelle « al-A'<em>ẓamī</em> »).
- Décisions supp confirmées : al-Ḥaṭṭāb al-**Ruʾaynī** (الرُّؤَيْنِي hamza,
  d. 954 H — parallèle Ruʾīnī W8 ; le corpus porte aussi Ruʿaynī ailleurs,
  autre savant) ; **Diʿāma** conservé ʿ tel qu'imprimé دِعامة (canon
  دِئامة consigné) ; al-muʿlim (المعلّم, print) ; iʿmār (الإعمار) ;
  taʿajjala تعجّل ʿ (≠ taʾajjala) ; yarduʾa/arḍaʾ (ر-ض-أ) ;
  ḍayʾa (ضَيْئة, loss) ; al-mubaṭʾ (المُبَطْأ, ب-ط-أ) ; Luʾluʾ/luʾluʾa
  (لؤلؤ, hamza).
- Carte étendue : 38 couples médiaux + 14 finales + chaîne luʾluʾ (clé
  finale avec ' interne). Précédent corpus noté pour W19 : tabāyin (ulum-2)
  soutient la conversion at-tabā'in → at-tabāyin (' → y, valeur carte
  «=y» héritée) avec autorisation verify-diff bornée à ajouter.
- QA : qa-lesson **PASS ×22**, **verify-diff 0 diff non autorisé**, comptes
  458+183 = 641 = total exact ; **fiqh-tanawi-2 disparu du scan (0 dur)** —
  corpus global **714 → 693 docs à défauts durs** (30 livres restants,
  ~42 100 ').
- Push : commit local — poussé au tour même avec le token réinjecté
  (credential-helper one-shot, zéro trace disque ; W17a+W17 poussés juste
  avant : a190eea, rev-list 0 vérifié).


## W19 — 2026-11-17 — typo faraid-tanawi-3, 20/20 docs (LIVRE 5 TERMINÉ) — cartes R714-R715d récupérées
Task ID: W19
Trace: 1a1d675aa095fb41-w19

- Livraison : **20/20 docs faraid-tanawi-3 — 696 apostrophes droites
  classées** : **445 ʿ + 249 ʾ** + **2 tabā'in → tabāyun** (' → y,
  التَّبَايُن, yāʾ radical — consigné R715, parallèle at-tabāyun déjà écrit
  ×5 dans le livre ; autorisation verify-diff bornée au contexte
  «tabā|in» incl. la frontière de balise «at-tabā</em>'in») + **4004
  U+202F** (356→4360). docIds pdf-mut23h2v/w-* (format sans chiffres seuls
  — builder W715 déjà corrigée pour ce format).
- Arbitrage : dry 532 classées + 164 incertaines → **164/164 résolues** par
  w2-far3-supp.json (l'arbitrage R715-R715d couvrait tout le livre), 0 à
  arbitrer.
- Révisions consignées (supplantent le supp) : **rubuʿ** ×3 (الرُّبْع, le
  quart — Nisāʾ 4:12 «fa-lakumu r-rubuʿu» ; le supp ʾ était fautif, canon
  ʿayn sans précédent corpus).
- Décisions supp conservées et consignées : **taʿīl** (التعييل — lecture du
  tirage ʿ conservée, canon attendu taʾyīl التأييل — image à confirmer au
  prochain passage PDF) ; masʾala(tayn), yasʾalūnaka, imruʾun, yaʾtī,
  chayʾu/chāʾiʾin (graphie ch), Qorʾān (graphie q), daʿm, joumʿa/āt,
  jāmiʿa, majmaʿ, maʿāda, muʿtabar, muʿtiq, muʿūnat, mutaʿaddid, taʿmalu,
  taʿmīr(i), taʿṣīb/taʿṣīl, wadaʿat, yaʿūdu/yaʿūlu, bacharīna, manaʿ,
  khurqaʾ (supp).
- Carte étendue : 31 couples médiaux + 2 finales + règles spéciales
  tabā'in/bat'an (' → y/t, autorisations verify-diff bornées).
- QA : qa-lesson **PASS ×20**, **verify-diff 0 diff non autorisé** (après
  correction de la borne balise), comptes 445+249+2 = 696 = total exact ;
  **faraid-tanawi-3 disparu du scan (0 dur)** — corpus global
  **693 → 674 docs à défauts durs** (29 livres restants, ~41 400 ').
- Push : commit local poussé au tour même (credential-helper one-shot,
  zéro trace disque).


## W20 — 2026-11-17 — typo fiqh-1es, 31/31 docs (LIVRE 6 TERMINÉ) — la récupération R715-R715d est complète
Task ID: W20
Trace: 1a1d675aa095fb41-w20

- Livraison : **31/31 docs fiqh-1es — 1700 apostrophes droites classées**
  : **1265 ʿ + 436 ʾ** (7 ʿ + 1 ʾ préexistants) + **4536 U+202F**
  (535→5071) ; **al-kuʿʿ ×2** (11421, 11428 — double apostrophe du tirage
  conservée, canon al-kuʿ الكُوع consigné ; clé finale « ku » ajoutée).
- Arbitrage : dry 1454 classées + 238 incertaines → **229 résolues par
  w2-1es-supp.json** (convention école française du livre) + 9
  seconds-signes arbitrés au tour : Ṣaʿṣaʿa (صعصة, ×2 ʿ), duʿāʾ (الدُّعاء,
  ʿ+ʾ auto-finale), shaʿāʾir (الشَّعائر, ʿayn 1er signe), al-kuʿʿ.
- **BUG DÉCOUVERT ET CORRIGÉ — docIds homonymes** : fiqh-1es porte DEUX
  docs « 11505 » (l'intro et une leçon) ; la sélection
  `[x for x in docs if str(docId)==did][0]` prenait toujours le premier —
  la leçon homonyme n'a jamais été traitée (le livre semblait fini à 8 '
  près). Correctif dans fix-typo.py : dédup par identité d'objet
  (seen_ids), bloc « ⚠ introuvable ou déjà traité » — les tours futurs avec
  des docIds dupliqués sont protégés. Comptes re-vérifiés après correctif :
  0 ' résiduel.
- Révisions/consignations du supp : al-kuʿʿ (print), le reste du supp 314
  formes validé tel quel (convention école française : 'a élide + 'a ayn
  — 314 formes, cf. R715).
- Carte étendue : 98 couples médiaux + 21 finales (émis par
  w17-arbitre.py --supp, insérés par w20-carte-patch.py).
- QA : qa-lesson **PASS ×31**, **verify-diff 0 diff non autorisé**, comptes
  1265+436 = 1701 − 8 préexistants = 1700 = total exact ; **fiqh-1es
  disparu du scan (0 dur)** — corpus global **674 → 644 docs à défauts
  durs** (29 livres restants, ~41 100 ').
- BILAN RÉCUPÉRATION R715-R715d : les 5 livres arbitrés de la session
  perdue (fiqh-tanawi-1/2, faraid-tanawi-3, fiqh-1es + ft3 déjà couvert
  par W1-W16) sont NORMALISÉS ET EN LIGNE (W17-W20) — 4037 + 1114 = 5151
  ' récupérées. Reste 29 livres (~41 100 '), aucun arbitrage conservé :
 hadith-3es 3551, hadith-2es 3467, taqtit-tanawi-1 2870, hadith-tanawi-1
  2537, tajwid-2es 2002, ulum-hadith-tanawi-2 1879, ulum-quran-2es 1808,
  hadith-1es 1783, qiraat-tanawi-1 1774…
- Push : commit local poussé au tour même (credential-helper one-shot,
  zéro trace disque).


## W21 — 2026-11-19 — tentative de traduction hadith-tanawi-3 pdf-mut23h2n-16 (القضاء في المياه وأحكام القسمة) — POSE BLOQUÉE PAR GARDE-DOUBLON, TRAVAIL SAUVÉ

- Recyclage du sandbox : clone repo-417 vide → re-cloné (6,4 G) depuis origin/main 0545bae5 (aucune pose concurrente L16 au fetch).
- Transcription complète pp.112-119 : couche texte extraite (download/ht3-5/couche-p110-122.txt), rendus 200 dpi ×8 pages (pages/), 16 moitiés transcrits via CLI z-ai vision (vlm/w21-t*.txt, 16/16 OK), 18 zooms ×2-2,5 (zooms/).
- TRANCHAGES (couche + VLM + zooms lus en direct + canon web) : titre médaillon = القضاء في المياه وأحكام القسمة badge 16 (désavoue la lecture القسامة du iʿdād L15) ; objectifs ×3 (3e = أن أتمثل المعاني المستخلصة من أحكام المياه والقسمة) ; tamhīd 1 verset [الأنبياء: 30] ; hadiths n° 2174 (سيل مهزور ومذينيب) / 2176 (نقيع بئر, chaîne أبي الرجال عن أمه عمرة) / 2181 (دار أو أرض) / 2182 (البعل والنضح) — décodage bidi de la couche (4712/6712/1812/2812 → série 21XX) confirmé NUM chiffre par chiffre, canon ʿAbd al-Bāqī : seil = 1429 ; hadith Abū Hurayra n° 2175 + Ibn Ḥibbān « لا تمنعوا فضل الماء ولا تمنعوا الكلأ فيهزل المال ويجوع العيال » (canon az-Zurqānī ✓, chaîne أبي سعيد مولى بني غفار) ; mort ʿAbd Allāh ibn Abī Bakr ibn Ḥazm = 135 H (imprimé, canon 94 à consigner) ; ʿAmra bint ʿAbd ar-Raḥmān « توفيت قبل المائة ويقال بعدها » ; Thawr ad-Dīlī 135 H (couche 531 bidi).
- htmlFr rédigé en 5 fragments (download/ht3-5/n16-part1..5.html, assemblé n16-htmlfr.html, 60 259 car, format modèle L15 : arabe vocalisé + ?? + consignes d'arbitrage) — QA typo PASS (balises équilibrées, guillemets 29/29 après fix d'un » manquant, spans RTL, zéro marqueur).
- POSE REFUSÉE par hand-set.py GARDE-DOUBLON : « pdf-mut23h2n-16 possède déjà une htmlFr livrée (42055 car) différente — livrie par un autre ouvrier » ; content/books du clone montrait htmlFr: 0 au fetch — divergence non résolue (peut-être la page livrée du site) ; PAS de --force (règle reprise documentée), aucune zone d'autre IA touchée.
- Reste pour la reprise : identifier le propriétaire de la htmlFr 42055 (git log content/books/hadith-tanawi-3.json + la page site), décider --force documenté OU abandon, puis registre savant (hand-register.py/hand-set), QA double porte, push. Tout le matériel est dans download/ht3-5/ (fragments + couche + transcriptions + zooms).

## W21-b — 2026-11-19 — leçon 16 hadith-tanawi-3 POSÉE (commit local 44fb79f6) — push BLOQUÉ par PAT révoqué

- Instruction du faux doublon R622 : le « 42055 car d'un autre ouvrier » était MA propre pose v1 écrite par la tentative 1 d'hier (set_book_doc s'exécute AVANT acquire_lock — l'écriture réussit, le registre échouait) ; 42055 vs 42057 = différence octets (wc -c) vs caractères Python (arabe vocalisé ~3 o/car). Aucune pose concurrente : l'historique du json ne montre que L5-L15.
- Pose réussie (idempotente) : 1 emplacement htmlFr écrit (42057 car = version fixée), registre savant +1 (1237). Verrou R622 : le RuntimeError trompeur venait du répertoire HOME/scripts-translate absent du workspace recyclé (ENOENT retenté 40×) — corrigé par lien symbolique scripts-translate → clone.
- Commit local 44fb79f6 : json L16 + registre. PUSH REFUSÉ : « Invalid username or token » — le PAT fourni (ghp_IqmW…) a été révoqué depuis hier (lecture anonyme OK = dépôt public, écriture impossible).
- Sauvegarde portable : download/ht3-5/w21-b.bundle (base a4fb79c8, git bundle verify ✓) + w21-b.diff. Pour pousser : git clone/pull origin main puis git bundle unbundle download/ht3-5/w21-b.bundle (ou demande à l'IA un PAT write frais et repose via hand-set depuis download/ht3-5/n16-htmlfr.html).
- Complément W21-b : lissage vocalique الِاِرتِفَاق (2 occurrences sukūn→kasra, forme dominante) via re-pose --force documentée (reprise du propre commit local non poussé 44fb79f6, cas prévu par le garde R622) ; commit amendé 44fb79f6, bundle w21-b (base 86282f73) + diff régénérés. QA matière finale : 15/15 checks ✓ (titre+badge, hadiths 2174/2175/2176/2181/2182, Ibn Ḥibbān, morts 135 H, Anbiyā 30, Nisāʾ 58, Ibn ʿArafa 373, taqwīm, istiṯmār Bukhārī, iʿdād irtifāq, balises, guillemets 29/29).

## W22 — 2026-11-19 — leçon 17 hadith-tanawi-3 أحكام الارتفاق (pdf-mut23h2n-17, pp.119-126) POSÉE

- Pipeline complet : couche pp.119-127 (pdftotext), rendus 200 dpi ×7 pages (pp.120-126), 14 moitiés transcrits via CLI z-ai vision (14/14 OK après fix du chemin image t{tag}.png — le « verrou occupé trompeur » du workspace recyclé venait de HOME/scripts-translate absent, corrigé par lien symbolique ; les échecs détachés venaient de l'env perdu), 22 zooms ×2 lus en direct, canon web (ayaquran.com riwāyat Yaḥyā : 2177/2178/2179 مرسل/2180 intégraux ; dorar : variantes Sunan ; sunnah.com/islamweb bloqués ou vides via curl).
- TRANCHAGES : renvois NUM bidi confirmés chiffre par chiffre (7712→2177, 8712→2178, .9→2179, 0812→2180) ; 2178 chaîne عن الأغرّ عن أبي هريرة (VLM confabulait ابن شهاب — désavoué) + matn «عنها معرضين… لأرمِنَّ بها» ; 2179 matn long riwāyat Yaḥyā avec crochets éditoriaux [والله]/[ولو] ; 2180 «كان في حائط جده ربيع لعبد الرحمن بن عوف…» ; الكهف 16 (مِرْفَقًا — couche 61 palindrome bidi) ; الأنبياء 78 (zoom 77/couche 7 — canon 78) ; mort أبي هريرة 57 هـ ; المختصر الوجيز لابن عطية ; Bayhaqī باب تحريم الغصب (zoom القصب — désavoué).
- htmlFr 5 fragments (43 269 car, format L15/L16), QA typo PASS (guillemets 22/22 après 3 fixes : « manquant au 2179, »» laser artifact, lang="arg"→ar), pose hand-set réussie (1 emplacement, 43268 car, registre → 1238), QA matière 18/18 ✓.
- Points non résolus consignés dans le texte : حذف تقديره «لا حوق أو إلحاقا» + «إجازة اللقاء» ; «لتبخ الحكماء على تركه» ; «متجردا أضراره خفيفا» ; prov. «تتدول الأنام أقضية» ; fin 2180 «بتخويله» (canon «بتحويله», zoom «بالتحول») ; «في رهن الأصل» ; آت القرطبي ; ضمير/صمير dans la glose de «لأرمِنَّ».

## W23 — 2026-11-19 — leçon 18 hadith-tanawi-3 القضاء في ضمان ما أتلفت المواشي (pdf-mut23h2n-18) : SOURCE BLOQUÉE — pose reportée

- Préparation : L18 dans le JSON (htmlFr vide, titleAr القضاء في ضمان ما أتلفت المواشي, pdfOnly) ; iʿdād déjà connu (consigné en W22 p.126) : حكم ضمان ما أتلفتها البهائم / ما الواجب على من قتل بهيمة / المحرر الوجيز لابن عطية sur الأنبياء 78 (داود وسليمان).
- **BLOCAGE SOURCE (documenté)** : le PDF officiel de la leçon (pdfUrl JSON : 18BA701.PDF) et tout le dossier `images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الحديث-الثالثة-ثانوي/` ont été **retirés de habous.gov.ma** entre W22 (hier, téléchargements OK) et aujourd'hui — le site a été refait (nouvelle racine minimaliste, assets/docs/, l'ancien CMS Joomla et ses pages الكتب المدرسية sont morts : 404 nginx sur toutes les pages catalogue testées + 522 Cloudflare transitoire en milieu de session).
- Pistes épuisées avec codes : 29/29 pdfUrl JSON → 404 (y compris 16FD121.PDF de la L16 posée hier) ; pages CMS ancien/‑v2 → 404 ; sitemap → 404 ; Wayback available + CDX (habous.gov.ma/images/2024*, 2000 lignes) → 0 capture du dossier (ni des pages catalogue) ; scribd (doc 762256064) → 403 ; facebook taalim.al.aatik → auth requise ; r.jina.ai → IP bloquée ; archive.org (1_20220304...) → rien de pertinent ; ebook.univeyes.com → traité académique de Baṣfar sur ضمان ما أتلفته البهائم (source de fond canonique possible pour L18, pas le livre scolaire) ; drives → non indexés.
- **Retenu** : le PDF L17 d'hier venait d'un chemin qui n'existe plus ; l'URL de téléchargement n'était pas journalisée → **LEÇON : consigner l'URL source au téléchargement dans le journal** (corriger dès la reprise).
- Artefact local : download/ht3-l18/ (vide, source.pdf = page 404 nginx de 153 o).
- Reprise possible si : (a) un utilisateur fournit le PDF L18 (téléchargement manuel depuis une copie locale), ou (b) habous restaure le dossier images/2024 (migrations parfois réversibles), ou (c) une copie du livre « الحديث الثانوي الثالث 2023/2024 » trouvée plus tard (recherches à refaire périodiquement).
- Rien de posé pour L18 — aucun risque de doublon ; le garde R622 reste applicable.

## W23-b — 2026-11-19 — leçon 18 hadith-tanawi-3 القضاء في ضمان ما أتلفت المواشي (pdf-mut23h2n-18, pp.127-132) POSÉE — source retrouvée

- **SOURCE RETROUVÉE** : le « blocage » W23 était un faux blocage — le livre complet est EN DÉPÔT depuis toujours : `content/textbooks-src/hadith-3-thanawi_text.pdf` (200 p., worklog.md:17676 « SOURCE DE PRODUCTION = LES MANUELS LOCAUX (content/textbooks/ + sources/) — le portail habous.gov.ma N'EST PLUS une dépendance »). Consigné au journal pour ne plus jamais dépendre du portail.
- Pipeline : couche pdftotext pp.127-133 (raw) ; rendus 200 dpi ×6 pages (127-132) ; 12 moitiés transcrits via CLI z-ai vision (12/12 OK) ; 9 zooms serrés + 5 Read fins (versets p.129, العماء p.130, matn 2186 p.131+128, tarjama p.128) ; canon web (dorar snippets 2183 version « الحوائط…أفسدت » attestée ; éditions web numérotant le hadith الجمل 2181 contre l'imprimé 2186 du livre ; Muslim « العجماء جرحها جبار » باب جرح العجماء والمعدن والبئر جبار ; Ḥarām b. Saʿd généalogie confirmée, mort 113 non vérifiée — consignée).
- TRANCHAGES couche : « مقرر عند الفقهاء » (tamhīd sans verset) ; PAS de 2184 (saut de numérotation du livre) ; « لِتَفْرِيطِهِ » (désavoue لِتَقْرِيرِعَيْبِهِ) ; « يُغْلَبُ عَنِ الظَّنِّ أَنَّهَا لَا تَرْجِعُ لَهُ » ; « إيجاب النقصان » (désavoue التفصان) ; « وبه قال أبو حنيفة… رُبْعُ ثَمَنِهَا » (désavoue اللباث) ; « وهو ما رواه يحيى عن مالك في الموطأ » (désavoue بيدي) ; « الفتوى على مذهب الإمام مالك » (désavoue القووى).
- htmlFr 5 fragments (41 955 car, format L15-L17), QA typo PASS (guillemets 16/16 après 2 fixes de consignes tronquées), pose hand-set réussie (1 emplacement, 41 954 car, registre → 1239), QA matière 18/18 ✓.
- Points non résolus consignés : renvoi الأنبياء 77 imprimé (canon 78) ; verset 2 bidi illisible + renvoi الأنعام 91 imprimé (canon contexte الأنعام 90 اقْتَدِهْ) ; العَمَاء/العَجْماء (orthographe d'impression) ; « فَإِنْ كَانَتْ لَهُ بَيِّنَةٌ » contre canon sans fāʾ ; NUM 2186 (éditions 2181) ; mort 113 non vérifiée ; « زَرْعَ شُونِيَّةً » lecture ; « مَا تُقُولُ لَكُمْ » contre canon « مَا قُولُكُمْ ».

## W24 — 2026-11-21 — IA-3 — nouvelle zone (partage R777, 197 leçons) : fiqh-3es leçon 1 البيع والربا في الطعام (pdf-1) POSÉE

- Zone reçue du propriétaire (carte PARTAGE-TRADUCTION R777) : tajwid-3es (28), fiqh-3es (27 restantes), tafsir-3es (25), usul-fiqh-tanawi-2 (30), usul-fiqh-tanawi-3 (30), tafsir-tanawi-3 (29), fikr-islami-tanawi-1 (28) — traduction SEULE, commentaires suspendus.
- Carte d'acquisition des 7 livres vérifiée contre la collection archive.org (metadata via backend page_reader, 563 fichiers) et le dépôt : manuels EN DÉPÔT pour fiqh-3es (fiqh-3-iadadi_text.pdf), tafsir-3es (tafsir-3-iadadi_text.pdf), tafsir-tanawi-3 (tafsir-3-thanawi_text.pdf) ; ABSENTS pour tajwid-3es (aucun livre التجويد dans la collection — confirmé au titre d'ouvrage par la liste complète, + portail mort + R170 l'avait déjà écarté « PDF non extraits »), usul-fiqh-tanawi-2 (أصول الفقه 2 ثانوي absent), fikr-islami-tanawi-1 (absent) → ordre d'exécution ajusté : fiqh-3es d'abord, les trois livres bloqués consignés et repris si une source apparaît.
- Incident source : archive.org en 429/000 depuis la sandbox pendant ~40 min (IP partagée) ; contournement : metadata + recherche par le backend page_reader (200) — la liste réelle de la collection acquise ainsi.
- Pipeline L1 (pp.11-17 du manuel fiqh-3-iadadi_text.pdf extrait par git cat-file, sparse-checkout préservé) : couche pdftotext p.1-17 + rendus 160 dpi ×7 pages + 13 passes VLM (moitiés + 6 zooms 300 dpi) + canon web (الرسالة shamela 7441/517 + الثمر الداني usul.ai ×6 : « لا يجوز الجنس منه بجنسه » — le الجدس de la couche = erreur OCR désavouée ; عبادة b. الصامت « فإذا اختلفت هذه الأصناف فبيعوا كيف شئتم إذا كان يدًا بيد » مسلم ✓ ; la numérotation du verset imprimée 274 contre canonique 275 — consignée).
- htmlFr FR-seule (18 775 car, doctrine R777 : 0 caractère arabe, guillemets appariés 34, balises 12) : objectifs, مدخل, متن de la Risāla traduit, الفهم glossaire, استخلاص ×3, التحليل deux axes (البيع définition/hukm/arkān + الربا تعريف/hukm/ستة أقسام + علتان), مقاصد, تقويم ×3, الاستثمار الباجي [المنتقى 4/32], إعداد قبلية ×2. Renvois arbités : [المختصر الفقهي 5/79], [أحكام القرآن 1/320], [حاشية العدوي 2/143 — le 341 de la couche = artefact bidi], [شرح الزرقاني 3/379], [المغني 3/480 ×2 passes], [المنتقى 4/32]. Points consignés dans le texte : le nom d'espèce imprimé « ربا النساء » (canon : النسيئة) aux 4 emplacements ; le bāb de Bukhārī défiguré (recopié avec réserve, sans le nom) ; la fin du bāb de Muslim (تفاضلا canon / نقدا passe) ; la liste alimentaire de الباجي (2 maillons résiduels).
- Pose : hand-set fiqh-3es/pdf-1 (1 emplacement, 18 775 car — registre principal : pdf-1 déjà présent au fil, aucune écriture nouvelle) ; registre IA-3 → fiqh-3es/pdf-1 (badge). qa-lesson PASS.
- SUIVANT : fiqh-3es L2 (pdf-2 أجناس الطعام وبيع الطعام قبل قبضه, ~pp.17-22) puis vague suivante ; retour tajwid-3es si manuel acquis.
- Complément W24-b : fiqh-3es leçon 2 أجناس الطعام وبيع الطعام قبل قبضه (pdf-2, pp.18-24) POSÉE — pipeline identique (couche + 14 passes VLM 160 dpi), htmlFr FR-seule 15 897 car QA PASS (0 arabe, guillemets 33, balises 12) : متن الرسالة traduit (الجنس الواحد: الزبيب/التمر/الحبوب/اللحوم + بيع قبل قبضه 6 حالات + البيوع الفاسدة 8) ; الفهم glossaire (الجزاف، الشركة، التولية، الإقالة، التدليس، الغش، الخلابة) ; التحليل 3 axes ; hadith ابن عمر [البخاري، باب défiguré — réserve consignée] ; العدوي [حاشيته على شرح الخليلية 2/148] ; الاستثمار = عبادة (matn intégral, مسلم — le bāb imprimé «نقدًا» contre canon «تفاضلًا», renvoyé au N.d.T. de L1) ; إعداد ×2. Pose hand-set (1 emplacement, registre principal → 1240) ; registre IA-3 → pdf-2.
- Correctif W24-c : L1 re-posée --force (reprise documentée, cas R622) pour un terme français défectueux («conclavation» → «échange tacite» pour المعاطاة) ; 18 766 car, QA PASS.

## W25 — 2026-11-21 — IA-3 — fiqh-3es leçon 3 بيع الخيار والبيع الفاسد (pdf-3) POSÉE

- Reprise W24 : clone frais `--filter=blob:none --sparse` (PDF exclus, disque) ; manuel fiqh-3-iadadi_text.pdf extrait par `git cat-file` (200 p., 9,99 Mo) ; alignement : L3 = pp.25-30 (objectifs p.25, التقويم p.29, الاستثمار pp.29-30), L4 commence pp.30-31.
- Pipeline : couche pdftotext pp.25-30 (très corrompue pp.26/29) + 12 passes VLM 160 dpi (moitiés) + 7 zooms 300 dpi + 8 microcrops adjudicatifs (×1,8-×4) + extraction du mot-tête rouge par masque de pixels + canon web (Risāla : shamela 7441/524+527, kitāb 11373/128, ablibrary 5256/506 ; Mawāhib al-Jalīl shamela 784/1081 pour la définition d'Ibn ʿArafa ; Muwaṭṭaʾ hadith «المتبايعان… إلا بيعَ الخيار» confirmé mot à mot ; كفاية الطالب = Abū al-Ḥasan al-Manūfī, archive.org Kivayat_talib — identité du «قال أبو الحسن» du manuel).
- ARBITRAGES PAR LE CANON (couche désavouée) : «ولا في المواضعة بشرط» présent au 2e tirage du matn (p.28) — absent du 1er (p.25, points de suspension de l'imprimé reproduits) ; «أو تغيّر في بدنه» (canon) contre «في يديه» (couche/VLM) ; «ولا تُفيت الرِّباع حوالة الأسواق» (canon «يُفيت») ; «ففي الأصول بالشهر» (couche) contre «بالنظر» (VLM) ; «تفريط المشتري في حفظه» (couche) contre «تقرير قبض» (VLM) ; «المقوّمات» (couche) contre «المنقولات» (VLM) ; «من المبيعات» / «مثليًّا عقارًا» / «مفيتات المبيع» / «وبماذا تفوت البيوع» / «ما يفوت به المبيع» (couche) ; «يفوز المشتري بغُلّتها» (couche «يفو») ; hadith : [الموطأ كتاب البيوع، باب بيع الخيار] (couche + zoom 300 dpi ; la passe 160 dpi avait lu «البخاري» — désavouée).
- ARBITRAGES PAR LE SENS/CANON LEXICAL : définition d'Abū al-Ḥasan «بيعٌ وُقِفَ بَتُّهُ أولاً على إمضاءٍ يُتوقَّعُ» — «بَتُّهُ» retenu contre les lectures «بنه/بنته/بناه» (motif : la phrase explicative du manuel emploie «وهو بَتُّ البيع وإمضاؤه») ; définition d'Ibn ʿArafa : «لنقصه عن حالة بيع عليها غيرُ قلةٍ كمِّيَّته قبل ضمان مبتاعه» — canon Mawāhib al-Jalīl («غير قلة كميته»), les lectures VLM «غير قليلة كثيرة» désavouées ; entrée glossaire 3 : mot-tête illisible après 8 passes (بُثِرَ/يُثْبِرُ/بُنَّر…) — lecture rétablie «athghara» (أثغر : «سقطت رواضعه فإن نبتت أسنانه بعد السقوط قيل أثغر», Lisān مادة ثغر), N.d.T. posé dans la leçon ; «الغُلَّة… من رَيْع الأرض أو أُجرتها» (رَيْع canon lexical contre «ربع/ربيع» VLM).
- Points imprimés consignés dans la leçon : verset [البقرة : 274 imprimé / 275 canon Ḥafṣ] — écart déjà consigné L1, renvoi posé ; titre «٥- النفقة والضمان في الخيار» imprimé SANS corps (vérifié 4 sources concordantes : couche + 3 VLM) — reproduit avec N.d.T. ; «مثليًّا عقارًا» (4 lectures concordantes couche+VLM, imprimé tel quel, traduit tel quel).
- htmlFr FR-seule 13 124 car (13 125 avant pose), QA typo PASS (0 arabe, guillemets 15/15, balises 12, 0 apostrophe droite) ; mise en page calquée sur L1/L2 (objectifs ×4, تمهيد 5 questions, متن avec les points de suspension de l'imprimé, glossaire ×6, استخلاص ×3, التحليل 2 axes — notion/règle/condition/espèces + titre 5, corruption/garantie/péremption —, تقويم ×3, استثمار العدوي 2/161-162 + questions ×2, إعداد ×2 renvoyant à L4 القرض).
- Pose : hand-set fiqh-3es/pdf-3 (1 emplacement, 13 124 car — registre principal → 1241) ; registre IA-3 → fiqh-3es/pdf-3 (badge). Rendu : poussée données seules, la CI « Rendu du site » reconstruit site/ + racine publiée à chaque push (rendu.yml lu et vérifié).
- SUIVANT : fiqh-3es L4 أحكام القرض وبعض البيوع المنهي عنها (pdf-4, pp.30-38) puis vague suivante.
- W26 : fiqh-3es leçon 4 أحكام القرض وبعض البيوع المنهي عنها (pdf-4, pp.31-38) POSÉE — pipeline identique (couche + 20 passes VLM 160 dpi), htmlFr FR-seule 18 599 car QA PASS : متن الرسالة traduit (السلف يجر منفعة/بيع وسلف/الوضيعة والتأخير والتعجيل/رد أكثر عددا أشهب-ابن القاسم/بيع العمر والحبل/الأنهار والبرك/حبل الحبلة/الكلب/اللحم بالحيوان/بيعتان في بيعة) ; الفهم glossaire ×4 ; التحليل 2 axes (القرض: مفهوم/حكم/حكمة/ممنوع فيه ×6/ما يجوز — الفاسد: 6 ventes) ; آيات (المائدة 245-11 قرضا حسنا — verset défiguré identifié par glose) ; hadith أبو رائف [الموطأ باب ما يجري من السلف] + جابر [البخاري، باب الصلاة إذا قدم من سفر] + ابن سيرين [المصنف 1465] + الغرر والسلف وبيعتين [الموطأ ×3 bāb défigurés — réserves consignées] + شعر ابن عاصم [حاشيته بشرح المحلى 2/75-76] ; الاستثمار القاضي عبد الوهاب [التقنين 2/150-151 بتصرف] ; إعداد ×3 (الثمار/الغائب/السلم = leçon suivante). Pose hand-set ; registre IA-3 → pdf-4.

## W26-b — 2026-11-21 — IA-3 — COLLISION W26 consignée (livraison parallèle pdf-4) — L5 REVENDIQUÉE par cette session

- INCIDENT DE PARALLÉLISME : une seconde session IA-3 a livré fiqh-3es/pdf-4 (commit 0d17570, 18 599 car, W26 en bullet) pendant que cette session préparait la même leçon ; rebase refusé en conflit, ABORTÉ ; GARDE-DOUBLON (R622) appliquée : la livraison 0d17570 FAIT FOI, la version parallèle de cette session (19 571 car, préparée en本地 dans work/l4/) est ÉCARTÉE sans pose — aucun --force, aucun écrasement.
- MATIÈRE CANONIQUE CONSIGNÉE POUR ARBITRAGE ULTÉRIEUR (IA-1/propriétaire) — cette session a mené le pipeline complet (12 passes VLM + 12 microcrops 300 dpi calés bbox + canon shamela 11373/128-129, risāla intégrale du passage) ; constats divergents de la livraison en place, proposés pour correctif documenté le cas échéant :
  1. Référence du texte du القاضي عبد الوهاب : l'imprimé porte «التلقين في الفقه المالكي 2/150-151 بتصرف» (lecture zoom lettre à lettre ; l'ouvrage du juge ʿAbd al-Wahhāb est bien «التلقين») — la livraison en place a «التقنين».
  2. Hadith أبو رافع : [الموطأ كتاب البيوع، باب ما يجوز من السلف] (bbox + zoom ; la couche «العرطاكناباللبوع») — en place : «ما يجري من السلف».
  3. Référence ابن سيرين : [المصنف لعبد الرزاق برقم 14657] (deux zooms concordants) — en place : 1465.
  4. Vers des chiens : [تحفة ابن عاصم بشرح التسولي 2/75-76] (bbox net) — en place : «بشرح المحلى» ; le commentateur reçu de la Tuḥfa est at-Tasūlī.
  5. Crochet مسلم : imprimé «باب النهي عن بيع الثمار قبل بدو صلاحها بغير شرط القطع», titre canonique «إلا بشرط القطع» (écart à consigner, non tranché).
  6. Canon du matn (shamela 11373/128-129) : «إلا في ضراب الفضة» (couche shamela corrompue «الجوافي وكذلك تراب الفضة») ; «ولا التأخير به على الزيادة فيه» ; «ومن رد في القرض أكثر عددا في مجلس القضاء… إذا لم يكن فيه شرط ولا عادة» ; «وإن تخللت نخلة من نخيل كثيرة» ; «وأما من قتله فعليه قيمته» ; l'imprimé élidé «ولا بيع الآبق» et «ولا بيع الجنين في بطن أمه» par «…».
  7. Vers des «عقود ستة» : source canonique مواهب الجليل (الخطاب, باب عدم الجمع بين العقود) — «عقود منعناها مع البيع ستة / ويجمعها في اللفظ [؟] / فجعل وصرف والمساقاة شركة / نكاح قراض منع هذا محقق» — le 2e hémistiche du 1er vers résiste dans toutes les sources.
  8. L'āya «قرضا حسنا» du حكم القرض : canon البقرة 245 («من ذا الذي يقرض الله قرضا حسنا») — le W26 en place note «المائدة 245-11» : numéro/sourate à réviser.
- CLAIM (règle h, tail du worklog = autorité de priorité) : **fiqh-3es leçon 5 بيع الثمار والشيء الغائب وبيع السلم (pdf-5, pp.39-45)** prise par CETTE session — l'autre session est priée de reprendre à pdf-6 (الكالئ بالكالئ, pp.46-…).
- W28 : fiqh-3es leçon 6 الكالئ بالكالئ والآجال والجزاف والبرنامج (pdf-6, pp.46-53) POSÉE — pipeline identique (couche + 16 passes VLM 160 dpi), htmlFr FR-seule QA PASS : متن الرسالة traduit (دين بدين/تأخير رأس المال/فسخ دين في دين/بيع ما ليس عندك/بيع السلعة المؤجلة وأشكاله ×3 + المقاصة/الجزاف وشروطه ×10/النخل المؤبرة/البرنامج/السوم على السوم/انعقاد البيع بالكلام) ; الفهم glossaire ×4 ; التحليل 3 axes ; حديث ابن عمر [الدارقطني 4/40] + جزاف [أبو داود، باب بيع الطعام قبل استيفائه] + سوم [مسلم، كتاب النكاح — bāb cité tel quel] + آية القصاص 274 imprimé/40 canon consigné ; ابن عرفة [شرح الرسالة ص259 formule défigurée consignée] ; الاستثمار النفراوي/خليل «فقد منحي عنه إلا الدليل» [الفواكه الدواني 2/109 — 901 redressé] ; إعداد ×3 (الإجارة/الجعل/الكراء/الضمان = leçon suivante) ; canon: قارب الذهب tenu contre couche, التذكير/التحكير réserve consignée ; fix guillemet orphelin (hadith جزاف) re-pose --force. Pose hand-set ; registre IA-3 → pdf-6.
- W28 (session continue) : fiqh-3es leçon 6 الكالئ بالكالئ والآجال والجزاف والبرنامج (pdf-6, pp.46-53) POSÉE — pipeline identique (couche + 16 passes VLM 160 dpi), htmlFr FR-seule 18057 car QA PASS (28/28 guillemets) : متن الرسالة traduit (دين بدين/تأخير رأس المال/فسخ دين في دين/بيع المؤجل وأشكاله ×3 + المقاصة/الجزاف وشروطه ×10/النخل المؤبرة/البرنامج/السوم على السوم/انعقاد البيع بالكلام) ; الفهم glossaire ×4 ; التحليل 3 axes ; حديث ابن عمر [الدارقطني 4/40] + جزاف [أبو داود] + سوم [مسلم، bāb cité tel quel] + آية القصاص 274 imprimé/40 canon consignée ; ابن عرفة [شرح الرسالة ص259 — formule défigurée consignée] ; الاستثمار النفراوي/خليل «فقد منحي عنه إلا الدليل» [الفواكه الدواني 2/109 — 901 redressé] ; إعداد ×3 (الإجارة/الجعل/الكراء/الضمان) ; canon: قارب الذهب tenu contre couche, التذكير/التحكير réserve ; fix guillemet orphelin (hadith جزاف) + re-pose --force. Pose hand-set ; registre IA-3 → pdf-6 (union avec pdf-5 parallèle).

## W29 — 2026-11-21 — IA-3 — COLLISION W28 consignée (livraison parallèle pdf-6 par la seconde session) — L7 REVENDIQUÉE par cette session

- INCIDENT DE PARALLÉLISME : la seconde session IA-3 a livré fiqh-3es/pdf-6 (commits 228b684 + 7b8cdad «W28-fix», 18 056 car) conformément au CLAIM W26-b («l'autre session est priée de reprendre à pdf-6»). Cette session a repris sur la base d'un résumé de contexte périmé (état «zéro», reprise à pdf-6) et n'a relu le tail du worklog qu'APRÈS son pipeline — elle a donc travaillé pdf-6 en parallèle alors que le CLAIM W26-b l'attribuait à l'autre session. Responsabilité de coordination de cette session, consignée.
- GARDE-DOUBLON (R622) appliquée : la livraison 228b684 FAIT FOI ; la version parallèle de cette session (20 254 car, préparée dans work/l6/pdf-6.html, pipeline complet pp.46-53 : couche pdftotext + 8 passes VLM 160 dpi + 20 bandes 300 dpi + 14 microcrops 600 dpi ×1,5-4,5 + canon web shamela 11373/131-132 (matn intégral, dont les deux élisions de l'imprimé : «الرقيق و» avant الثياب et «ومن باع عبدا وله مال» après خروجه من الأرض), shamela 14297/2215 (Ibn ʿArafa via مواهب الجليل), islamweb/bukhari.lna.io/hdith/فتح الباري (hadiths)) est ÉCARTÉE sans pose — aucun --force, aucun écrasement, aucune écriture dans le JSON ni le registre par cette session pour pdf-6.
- MATIÈRE CANONIQUE CONSIGNÉE POUR ARBITRAGE ULTÉRIEUR (IA-1/propriétaire) — constats divergents de la livraison en place :
  1. آية الجزاف (p.50) : l'imprimé porte ﴿وأحل الله البيع وحرم الربا﴾ [سورة البقرة: الآية ٢٧٤] (deux zooms 600 dpi concordants ×1,8-×2,2 ; dalīl = généralité de la permission de la vente ; même écart 274 imprimé/275 canon Ḥafṣ que L1 et L3) — la livraison en place a le verset du talion [canon 40].
  2. صورة بيع الدين بالدين (p.48) : l'imprimé porte «فتبيعه من شخص آخر بألف درهم إلى أجل» — mille ET mille (couche + 160 dpi + 600 dpi concordants) — la livraison a «deux mille».
  3. «ثلاثة» (p.48) : «ولا يتصور في أقل من ثلاثة» = trois PERSONNES (canon أسهل المدارك, shamela 17682/767 : «لا يتصور في أقل من ثلاثة أشخاص أو أربعة») — la livraison a «[échéances]».
  4. Hadith أبو داود (p.50) : canon (أبو داود seule recension à porter «جزافا» — طرح التثريب) : «كانوا يتبايعون الطعام جزافا بأعلى السوق فنهاهم أن يبيعوه حتى ينقلوه» ; bāb imprimé lisible : «باب في بيع الطعام قبل أن يستوفي» — la livraison a «au hasard contre [du tas] au hasard… jusqu'à ce qu'elle se mesure» (جزافا = au forfait, titre même de l'axe ; ينقلوه = avant déplacement).
  5. «الثياب جزافا» (matn p.47 + citation p.50) : l'imprimé ET le canon shamela 11373/131 portent «ولا يجوز شراء [الرقيق و]الثياب جزافا» (cinq lectures VLM concordantes aux deux emplacements) — la livraison a «récipient fermé» ; l'ʿidl n'apparaît dans le matn qu'à la clause du البرنامج («ما في العدل»).
  6. مفهوم الكالئ (p.48) : l'imprimé est lisible au zoom : «هو بالهمز النسيئة بالنسيئة، مأخوذ من الكلأ وهو الحفظ؛ لأن كل واحد من المتبايعين يكلؤه صاحبه أي يحفظه لما له عنده» — la livraison a «al-kaʾd… la retenue… le retient muet» (avec N.d.T. propre à la livraison).
  7. التأبير (p.51) : canon shamela 11373/132 : «والإبار التذكير» = la pollinisation (tadhkīr) des palmiers ; l'imprimé : «أن يجعل على الثمرة دقيقٌ يكون في فحل النخل لئلا تسقط ثمرتها» (la poussière du palmier mâle placée sur le régime) — la livraison rend الإبار par «empoussièrement», أُبرت par «dont la floraison s'est levée», مؤبرة par «empoussiérés», et place la poussière «sur la fleur mâle».
  8. «كالعنب والزيتون» (p.51) : العنب = la vigne/le raisin — la livraison a «la grenade».
  9. ليل مظلم / الدابة (matn p.47) : canon shamela 11373/132 : «أو في ليل مظلم لا يتأملانه ولا يعرفان ما فيه وكذلك الدابة في ليل مظلم» — la livraison a «pâte sombre» et «l'obligation».
  10. ضابط الآجال, fin (p.50) : «فإنه ينظر إلى التي سبقت بالعطاء، فإن دُفعت قبل وعاد إليها كثير فالمنع وإلا فالجواز» (trois passes concordantes sur le segment) — la livraison a «la main précédente avec amabilité : si elle a donné avec acceptation et consentement abondant, elle perd [la préférence]».
  11. «لأنهما دخلتا في سلف بزيادة» (p.49) = elles revêtent la forme d'un prêt à surcroît (سَلَف) — la livraison a «elles entrent dans ce qui précède avec augmentation».
  12. Référence Ibn ʿArafa (p.49) : l'imprimé porte [شرح حدود ابن عرفة للرصاع ص: 259] (lectures 300 et 600 dpi concordantes) — la livraison a «le commentaire d'Ibn ʿArafa de la Risāla». Canon de la 2e moitié de la définition (shamela 14297/2215) : «والثاني لقبٌ لمتكرر بيعُ عاقدَيْه الأولُ ولو بغير عين قبل اقتضائه».
  13. Citation النفراوي/خليل (p.53) : «وفسد مَنهيٌّ عنه إلا لدليل» = «et se corrompt ce qui fut prohibé [la vente], sauf preuve» — le sujet de la corruption est la vente prohibée ; la livraison a «et s'est corrompu l'interdit, sauf avec preuve» (sujet inversé). Référence 2/109 concordante.
- POINTS CONCORDANTS (relevés pour mémoire, aucun constat) : نقار الذهب (lingots) ; le troisième exemple à 150 dirhams à deux mois ; la citation الموطأ du hadith du palmier ; الدارقطني 4/40 ; le bāb مسلم (عمتها أو خالتها, modulo «tante maternelle» pour خالة) ; التذكير tenu (canon 132 le confirme).
- CLAIM (règle h, tail du worklog = autorité de priorité) : **fiqh-3es leçon 7 أحكام الإجارة والجعل والكراء (pdf-7, pp.54-…)** prise par CETTE session — l'autre session est priée de reprendre à pdf-8 (أحكام الشركة, pp.63-…) après vérification du tail.
- SUIVANT (cette session) : pdf-7 — matn الإجارة déjà en canon (shamela 11373/132, récupéré en W29).

## W30 — 2026-11-21 — IA-3 — fiqh-3es leçon 7 أحكام الإجارة والجعل والكراء (pdf-7, pp.54-61) POSÉE (claim W29 honorée)

- Pipeline : manuel fiqh-3-iadadi_text.pdf pp.54-61 (L8 الشركة s'ouvre p.62) ; couche pdftotext + 8 passes VLM 160 dpi (8/8 OK) + 16 bandes 300 dpi + 17 microcrops 600 dpi (×1,8-3,5) + canon web : shamela 11373/132-133 (matn intégral de la leçon via backend — جواز الإجارة إذا ضربا لها أجلا… حتى ولا كراء له إلا على البلاغ), فتح الباري/islamweb + bukhari.lna.io (bāb-s), quran.ksu (تفسير الطبري يوسف 72).
- ARBITRAGES CANON (matn, shamela 133) : «كراء مضمونا» (canon) tenu contre la lecture «مضغوما» ; «وليكتروا مكانه غيره» (canon) contre «غرة» ; «لما غابوا عليه عملوه» ; «الحذاق» et «البرء» ; «بيده وهو مصدق إلا أن يتبين كذبه» ; «صاحب السفينة» et «إلا على البلاغ». L'imprimé porte «غنم الرعائية/الرعاية» — shamela 133 porte aussi «غنم الرعاية» : rendu par le sens («troupeau en pâture»).
- VARIANTES TENUES SÉPARÉMENT (imprimées toutes deux, non confondues) : le matn p.54 porte «أو بيع ثوب ونحوه» (canon shamela 132) tandis que la citation du شرح p.57 porte «أو بناء حائط ونحوه» (lecture 600 dpi lettre à lettre, ×2) — chaque leçon traduite telle qu'imprimée.
- RÉSOLUTIONS CLÉS : آية الجعل = ﴿ولمن جاء به حمل بعير وأنا به زعيم﴾ [يوسف 72] (زعيم net ×2 ; canon + تفسير «من باب الجعالة») ; le verset lu «ولا تقتلوا أولادكم…» par une passe = hallucination désavouée ; آيات الإجارة : [الطلاق 6] queue ﴿فإن أرضعن لكم فآتوهن أجورهن﴾ et [القصص 27] ﴿قال إني أريد أن أنكحك إحدى ابنتي هاتين على أن تأجرني ثماني حجج﴾ — queues frustes reconstituées d'après le canon (consigné ici) ; hadith أبو هريرة [البخاري كتاب البيوع، باب إثم من منع أجر الأجير — intitulé fruste, leçon canonique adoptée, N.d.T.] ; hadith ابن عباس «أحق ما أخذتم عليه أجرا كتاب الله» [البخاري كتاب الإجارة، باب ما يعطى في الرقية على أحياء العرب بفاتحة الكتاب] — décodé contre فتح الباري (islamweb) : «أجباع العرب» = «أحياء العرب», «بقنترة الكتاب» = «بفاتحة الكتاب» ; النفراوي «في سائر الأقطار على توالي الأعصار» [الفواكه الدواني 2/111] (lectures «الأفعار/الأعمار» désavouées) ; العدوي [حاشيته على كفاية الطالب 2/200] (مستعير tenu, «قيمة ملكه على تقدير وجوده») ; تمهيد «بيع الذوات… بيع المنافع» (الذوات lu à 600 dpi contre «الذرات/الذمم» — dichotomie classique, canon doctrinal) ; matn passif «إذا ضُرِب لها أجلٌ وسُمِّيَ الثمنُ» (lettre à lettre ×2 ; shamela : ضربا/سميا — la forme passive de l'imprimé tenue) ; صورة أ : «فاستُحقّت الدابة أو السيارة… بقيمة أخرى ولا يلتفت إلى الكراء الأول؛ لأنه قد يرخص أو يغلو» (couche + 600 dpi concordants ; la lecture «فاستؤجرت» désavouée au bénéfice de la couche) ; السفينة : «بسبب مدّ أو عباب أو موج أو ريح… كحمل طعام أو نحوه مما يُثقلها» (مدّ/عباب/طعام/يُثقلها, lettre à lettre) ; التقويم ×5 («والبيع» confirmé au 5e item) ; «الغرم على الضامن… للمضمون له» ; أركان : العاقدان (التمييز والتكليف), الأجرة (critère du prix), المنفعة («وأن تبقى العين بعد استيفائها أو أن تنتفي العين باستهلاكها كالطعام») ; شروط الإجارة ×3 ; «قاله أبو الحسن» = al-Manūfī (كفاية الطالب, précédent L3) ; استخلاص item 3 «أبيّن انطلاقا من المتن من يضمن ومتى يضمن» (couche : «أبدين»).
- Points consignés DANS la leçon (N.d.T.) : élision de «آبق» après «في رد…» (canon shamela 132) ; dernier mot de la liste du الماعون fruste ; deux intitulés de bāb frustes recopiés d'après la leçon canonique.
- Points consignés ici seulement : «الحذاق… أن يحذق المعلم القرآن» imprimé (l'usage reçu : حذق المتعلم) — rendu par le sens sans N.d.T. ; queues des deux آيات reconstituées per canon ; «متاع البيت» dans le glossaire الماعون (600 dpi ×3,5 contre la couche «منافع»).
- htmlFr FR-seule 17 622 car (17 623 avant pose), QA typo PASS (0 arabe, guillemets 33/33, 0 apostrophe droite, 0 imbrication) ; structure calquée sur L1-L6 (objectifs ×3, تمهيد, متن, glossaire ×3, استخلاص ×3, 3 axes : الإجارة notion/règle/arkān-shurūṭ + الجعل notion/règle/shurūṭ ×3 — الكراء notion/règle/فرق/صور ×3 — الضمان ماعون/صناع/حمام/سفينة, تقويم ×5, استثمار العدوي + questions ×2, إعداد → L8 الشركة).
- Pose : hand-set fiqh-3es/pdf-7 (1 emplacement, 17 622 car — registre principal → 1243) ; registre IA-3 → fiqh-3es/pdf-7 (badge).
- SUIVANT : fiqh-3es L8 أحكام الشركة وبعض أنواعها (pdf-8, pp.62-…) — matn الشركة déjà en canon (shamela 11373/133 : «ولا بأس بالشركة بالأبدان… والقراض جائز بالدنانير والدراهم…», récupéré en W30).

## W31 — 2026-11-22 — IA-3 — fiqh-3es leçon 8 أحكام الشركة وبعض أنواعها (pdf-8, pp.62-69) POSÉE (suite W30, aucun incident de parallélisme)

- Pipeline : manuel fiqh-3-iadadi_text.pdf pp.62-69 (L9 المساقاة s'ouvre p.70) ; couche pdftotext (très corrompue pp.64/66/69) + 8 passes VLM pleine page 150 dpi + 15 bandes 300 dpi + 14 microcrops 600 dpi (×1,8-4) + 12 ultra-zooms 1200 dpi ciblés par bbox + reconstruction des lignes RTL par pdftotext -bbox (inventaires de lettres décisifs) + canon web : shamela 11373/133-134 (matn intégral), shamela 21589/540 (الفواكه الدواني، باب الشركة/القراض : citation النفراوي + أركان القراض + النقار), islamweb (أبو داود كتاب البيوع باب في الشركة), ketabonline (Fawākih j2 p.540).
- MATN CONFORME AU CANON (shamela 11373/133-134, lettre à lettre) : «ولا بأس بالشركة بالأبدان إذا عملا في موضع واحد عملا واحدا أو متقاربا... ولا يقتسمان الربح حتى ينض رأس المال» — tranchant les doutes : «له بالٌ» (pas بلاغ ; canon + 2 zooms 600/1200 dpi + شرح «أن يكون المال له بال فلا نفقة في المال اليسير») ; «حتى ينض» (ḍād ; canon + entrée du glossaire ينض «من نض ينض إذا صار ذهبا أو فضة») ; «ويكون إن نزل أجيرا في بيعها وعلى قراض مثله في الثمن» (canon + Fawākih : «أي عامل القراض إن نزل العقد بالعروض أجيرا في بيعها»).
- ARBITRAGES PAR LE CANON (الفواكه الدواني, shamela 21589/540) : أركان القراض «والجزء المَجْعُولُ للعامل» (canon exact) — lectures VLM المعقول/المعضول/المقصود/الممول désavouées, la couche «مول» est la queue de المجعول ; citation النفراوي de l'الاستثمار : l'OUVERTURE imprimée est fruste (ligne y≈0.74 : OCR «23333», passes VLM divergentes-hallucinées dont «التاء والخاء والظاء من حروف الجدو») — restituée per canon : «الشريك أمين فيقبل قوله في دعوى التلف أو الخسار أو أخذ شيء يناسبه من مأكل ومشرب...» ; référence [الفواكه الدواني 2/122 بتصرف] confirmée (le «2/221» de la couche brute est un artefact bidi ; 2 lectures zoom 1200 dpi + inversion du run de chiffres → 2/122) ; «لأن المالك قطع للعامل قطعة» (imprimé, passé — canon قطع) contre la passe 600 dpi «يقطع» ; «على الخروج به في التجارة» (couche + pleine page) contre «الخِراج» (600 dpi).
- VARIANTES CONSIGNÉES DANS LA LEÇON (N.d.T.) : [سورة المزمل: 18] imprimé (bidi couche «81» + 2 zooms → 18) contre canon [المزمل: 20] — le Fawākih lui-même cite 20 ; le verset ﴿وآخرون يضربون في الأرض﴾ est canoniquement au v. 20.
- VARIANTES CONSIGNÉES ICI SEULEMENT : verset [النساء: 12] imprimé fruste — queue «وهم شركاء في الثلث» letter-confirmée à 1200 dpi, la tête restituée per canon ﴿فإن كانوا أكثر من ذلك فهم شركاء في الثلث﴾ (4 passes divergentes sur la tête, dont une hallucination «يا أيها الذين آمنوا إذا تداينتم» et «اليتامى والمساكين» — désavouées) ; glose «أي إذن كل واحد من المتشاركين لصاحبه في التصرف في متاعه ونصيبه في متاع الآخر ونصيبه» (1200 dpi ; lectures 300/600 dpi متاعه لنفسه ولنفس الآذن/مناعه/نصيبه وفي المتاع الذي دخل فيه désavouées) — rendue par le sens ; «وجاهة البائع المذكور» (bbox ذ-ك-و-ر) conservé tel quel bien que le référent de المذكور soit flou ; «نض» du شرح de la قسمة («فيقول له اقتسم هذا الذي نض») lu à la fois نض/نص par le VLM — tenu نض (canon lexical + contexte).
- RÉSOLUTIONS PAR INVENTAIRE DE LETTRES BBOX : تعريف اصطلاحا «عرفها أبو الحسن رحمه الله» (1200 dpi letter à lettre : ا-ل-ح-س-ن, ح sans point — la couche «آبو النسين يكوله» désavouée ; أبو الحسن = al-Manūfī, كفاية الطالب, précédents L3/L7) ; شركة وجوه : «أن فيه تدليسا» (inventaire د-ل-ي-س sans غ — la lecture 600 dpi تغريرا désavouée) + «يرغبون في الشراء من الأملياء — وجهاء — السوق» (1200 dpi ×2 avec tirets, la passe 1200 sans tirets minorisée 2:1) ; أبدان : «يجهز الغزل للنسج والآخر ينسج» (2 passes concordantes 300+600 dpi ; «يغزل» pleine page désavoué) ; مفاوضة : «أن يتصرف في الغيبة والحضور» (×1,8 letter à lettre غ-ي-ب-ة ; lectures العينة/الغنيمة désavouées) + «ولذلك سميت مفاوضة» (pas مقاوضية) ; عنان : «على أنه لا يبيع أحدُهما إلا بإذن الآخر» (2 passes concordantes ; couche «دلابهيُعمَا» ambiguë) + référence [شرح حدود ابن عرفة للرصاع 1/326 بتصرف] (bidi couche «623» = ٣٢٦ résolu) ; نفقة : «يتوهم كون الكسوة» (×2,5 : ي-ت-و-ه-ه-م ; la lecture «يتَّهم» désavouée) + «أي الذي تخلق فيه الثياب» (inventaire bbox ت-خ-ل-ق SANS ع ; lectures تُخلع (×2 hallucinations VLM) et يُتخلق désavouées) ; إعداد item 2 «معنى: زريعة البياض — الضفيرة» (bbox ز-ر-ي-ع-ة letter à lettre + canon L9 shamela 11373/134 «وعليه زريعة البياض اليسير» et «إصلاح الضفيرة» — lectures زراعة/زريبة/النياض/الضفية toutes désavouées).
- Autres hallucinations VLM consignées et désavouées : deuxième verset de المشروعية lu «وأينما كنتم فتولوا فثم وجه الله» [البقرة 115] (le canon imprimé/lu à 1200 dpi est ﴿وإن كثيرا من الخلطاء ليبغي بعضهم على بعض﴾ [سورة ص: 24]) ; «حروف الجدو» dans la citation النفراوي ; «الزيادة المادة الحياة» pour زريعة البياض ; diverses vocalisations fantaisistes. Le hadith qudsî [سنن أبي داود كتاب البيوع باب في الشركة] confirmé par islamweb (n° 3383).
- htmlFr FR-seule 17 017 car (17 016 après pose), QA typo PASS (0 arabe, guillemets 33/33, 0 apostrophe droite, 0 imbrication, 0 « ?? ») ; structure calquée sur L1-L7 (objectifs ×2, تمهيد, متن, glossaire ×2 [بنقار/ينض], استخلاص ×3, 2 axes : أحكام الشركة [تعريف لغة/اصطلاحا أبو الحسن+خليل، حكم، مشروعية : آيتا النساء 12 وص 24 + hadith أبو هريرة + إجماع] ; أنواع [وجوه + أبدان : النفراوي وشروط ×5 + أموال : مفاوضة/عنان/المضاربة-القراض : آيتا النساء 101 والمزمل + أركان ×5 + شروط ×7 + نزول بالعرض + نفقة بشرطين + قسمة الربح]), تقويم ×3, استثمار النفراوي + exercice ×3, إعداد ×3 renvoyant à L9 المساقاة).
- Pose : hand-set fiqh-3es/pdf-8 (1 emplacement, 17 016 car — compteur savants 1243, main hand 1186) ; registre IA-3 → fiqh-3es/pdf-8 (badge « Par IA-3 »). Livre 10/29 posés (pdf-1..pdf-8 + 2 index).
- SUIVANT : fiqh-3es L9 أحكام المساقاة (pdf-9, pp.70-…) — matn déjà en canon (shamela 11373/134 : «والمساقاة جائزة في الأصول على ما تراضيا عليه من الأجزاء... وإصلاح الضفيرة وهي مجتمع الماء من غير أن ينشئ بناءها... وعليه زريعة البياض اليسير...»).

## W32 — 2026-11-22 — IA-3 — fiqh-3es leçon 9 أحكام المساقاة (pdf-9, pp.70-76) POSÉE (suite W31, aucun incident)

- Pipeline : manuel fiqh-3-iadadi_text.pdf pp.70-76 (L10 المزارعة s'ouvre p.77) ; couche pdftotext + 7 passes VLM pleine page 150 dpi + 13 bandes 300 dpi + 11 microcrops 600 dpi + 6 salves 1200 dpi ciblées + reconstruction bbox (lignes RTL, inventaires de lettres) + canon web : shamela 11373/134 (matn المساقاة déjà récupéré en W31), شرح الزرقاني sur Muwaṭṭaʾ (islamweb 77/2906) + islam.museum (Muwaṭṭaʾ 2056) pour la citation مالك, alukah (citation ابن جزي), shamela 150969/785 (الصاوي, أصول أربعة).
- VARIANTE MAJEURE CONSIGNÉE PAR N.d.T. : le matn imprimé porte «إلا ما لا بال له من سَدِّ الحُفرة» (3 lectures letter-confirmées 300/600/1200 dpi : س sans point, ف point dessous) contre le canon shamela 11373/134 «مِن شَدِّ الحَظيرة» — la citation du شرح p.75 «من شد الحظيرة وإصلاح الضفيرة كما سبق» (couche nette) suit le canon : les deux leçons imprimées rendues chacune telle quelle, N.d.T. posé après le matn.
- MATN sinon conforme au canon : «والمساقاة جائزة في الأصول على ما تراضيا عليه من الأجزاء والعمل على المساقي... ولا يقتسمان الربح حتى ينض رأس المال» — l'imprimé OMET «كله» après «والعمل» (bbox net) ; l'ordre imprimé des clauses après «والتذكير على العامل» est : إصلاح مسقط الماء من الغرب، ثم تنقية منابع/مناقع الشجر، ثم تنقية العين (canon : مناقع قبل مسقط) — order imprimé suivi ; «مناقع الشجر» tenu (couche ×2 + canon) contre les lectures VLM السرج/السحر ; «يُلغى» (غ, canon + zoom) ; «وهو أحله» ; «غراس» (bbox + canon الزرقاني) contre «غرس».
- ARBITRAGES PAR LE CANON : ابن جزي «وهي جائزة مستثناة من أصلين ممنوعين» — bbox (م-م-ن-و-ع-ي-ن) + canon القوانين (alukah) tranchent contre la lecture 600 dpi «معنويين» ; [القوانين الفقهية ص:184] (bidi «481» résolu) ; citation مالك (الاستثمار) : «شد الحظار وخم العين وسرو الشرب وإبار النخل وقطع الجريد» conformes au Muwaṭṭaʾ (الزرقاني : وخم = تنقيتها, وسرو = كنس) contre les lectures VLM وخرم العيون/وسقي الشراب ; «وإنما ذلك بمنزلة» (canon + 600 dpi) ; «تعظم فيها نفقته» (canon + 600 dpi نفته) contre «منفعته» (pleine page).
- VARIANTES CONSIGNÉES ICI SEULEMENT : «وجد الثمر» (1200 dpi letter-read : د sans point, الثمر confirmé) contre canon الزرقاني «وجذ الثمر» et lectures VLM وجد/وجذ الفرض — rendu par le sens (la cueillette du fruit) ; «على أن المساقي شطر الثمر» (2 letter-reads sans لام) contre canon «على أن للمساقي شطر الثمر» — rendu par le sens ; «أو اغرس لي عملا» imprimé (2 letter-reads 600/1200 dpi : غ-ر-س avec analyse des points) contre canon الزرقاني «أو اعمل لي عملا» — traduit fidèlement («plante-moi un ouvrage»), écart consigné ; «وينعها» (bbox + couche ع) contre «وينقلها» (VLM) et «وينجها» (1200 dpi) — fruste, rendu «les amasser», consigné ; «أصول أربعة معنوية» (band 300 dpi letter-read) conservé — les formules parallèles classiques portent «ممنوعة» (الصاوي : من أصول أربعة كل واحد منها يدل على المنع ; ابن رشد : الأصول الممنوعة), écart proposé à l'arbitrage ; «أم لا» confirmé (pas de «شك فيه») ; [الفواكه الدواني 2/124] (bidi «24/2» résolu).
- RÉSOLUTIONS PAR BBOX/COUCHE : تمهيد «ممن هو بحاجة وله خبرة بذلك» (bbox : 2 lignes concaténées) + «جريا على سنة التسخير» (bbox + 2 VLM) + «وما شرطها؟» (SINGULIER, bbox) ; glossaire «المساقي: بفتح القاف وهو العامل» (bbox) ; تقويم ×4 : «مع التعليل» (items 2-3), «مع الاستشهاد» (item 4, bbox ...اد + VLM) ; «لقلته» (bbox : ل-ق-ل-ت-ه) contre les lectures VLM لقيمته/لقائته ; «وغيرهم» (band + couche) ; حكمها : hadith ابن عمر «عامل أهل خيبر بشطر ما يخرج منها من ثمر أو زرع» [صحيح البخاري كتاب الشروط باب الشروط في الغنيمة] (couche + VLM pleine page ; la référence dorar 2328 variant selon les éditions, transcrit tel qu'imprimé) ; أهداف ×4, استخلاص ×3, شروط ×8 (أ-ح), ثالثا ×4+2 — tous confirmés croisés.
- Hallucinations VLM consignées et désavouées : «يا أيها الذين...» (déjà W31), «التاء والخاء والظاء من حروف الجدو» (W31), passes L9 : «صنع الفلاح» (pour صيغ المفاعلة), «لخم» sans راison, «الفتاوى الهندية 1/190» (pour الفواكه الدواني 2/124 !), «وجد الثمر» lu «في غلاء الثمر على سيرة الموالي», «وينجها» — toutes écartées par bbox/canon/croisements.
- htmlFr FR-seule 14 231 car (14 230 après pose), QA typo PASS (0 arabe, guillemets 15/15, 0 apostrophe droite, 0 imbrication, 0 « ?? ») ; structure calquée sur L1-L8 (objectifs ×4, تمهيد, متن + N.d.T. سد الحفرة, glossaire ×4 [الأصول/المساقي بفتح القاف/الحائط/التذكير], استخلاص ×3, 3 axes : أحكام المساقاة [تعريف لغة-اصطلاحا، حكم : hadith خيبر + ابن جزي + قيل أصول أربعة + sagesse, شروط ×8 avec citations ×4] + الفرق [musāqāt vs إجارة : travail vs vente ; vs كراء الأرض بما تنبت : terre non louée] + ما يتناوله [×4 : تذكير/تنقية وإصلاح/جذ الثمار/تهيئة الجرين, avec citations] et ما لا يتناوله [×2]), تقويم ×4, استثمار مالك [الموطأ كتاب المساقاة باب ما جاء في المساقاة] + exercice ×2, إعداد ×2 → L10 المزارعة).
- Pose : hand-set fiqh-3es/pdf-9 (1 emplacement, 14 230 car) après rebase sur le commit CI 0ef590d ; registre IA-3 → fiqh-3es/pdf-9 (badge). Livre 11/29 posés.
- SUIVANT : fiqh-3es L10 أحكام المزارعة (pdf-10, pp.77-…) — L10 s'ouvre p.77 (أهداف ×4 aperçus : مفهوم المزارعة / ما يجوز فيها / الجائحة وأنواعها وأحكامها / مقاصد الشرع) ; matn «والشركة في الزرع جائزة...» à récupérer sur shamela 11373/134-135 (queue déjà en W31 : «والشركة في الزرع جائزة إذا كانت الزريعة منهما جميعا والربح بينهما»).

## W33 — 2026-11-21 — IA-3 — traduction fiqh-3es leçon 11 أحكام الشفعة والتبرعات (pdf-11, pp.84-92, suite W32)

- POSE puis RE-POSE : le commit initial 810749e (W33, jamais poussé — push bloqué avant passation) a été perdu au recyclage du sandbox (clone vidé, eb6e12b) ; htmlFr reconstruit à l'identique depuis la conversation, QA rejouée (17365 car, 0 arabe, guillemets appariés, 0 apostrophe droite, balises équilibrées, 9 h2, 1 dl), slot pdf-11 vérifié vide au fetch-avant-pose (origin 3c3c858).
- متن الرسالة traduit (letter pp.84-85) : «وإنما الشفعة في المشاع ولا شفعة في المذكور ولا للجار ولا في الطريق ولا في عرصة دار وقسمت ديارها ولا في عهل النخل ولا في البئر إذا قُسم النخل أو الأرض ولا شفعة إلا في الأرض وما لاحقها من العمران والشجر ولا شفعة للحاضر بعد السائل وللغائب شفعته وإن طالت غيبته والضمان على المشتري والشفيع ينتظر فيما أخذ أو ترك ولا توهب الشفعة ولا تبيع وتُقسم بين الشركاء على قدر الأنساب ولا تتم هبة ولا صدقة ولا حبس إلا بالحيازة فإن مات قبل أن يحيزها كان من التركة إلا أن تكون في المرض فيكون في الثلث إن كانت لغير وارث والموهوب للقريب أو للفقير كالصدقة لا رجعة فيه ومن تصدق على ولده فلا رجعة له ولحق له أن يرجع فيما وهبه لولده صغيرا أو كبيرا ما لم يتزوج عليه أو يترتب عليه دين أو يطرأ على الهبة تغيير وأم ترد ما دام الأب حيا إذا مات لم ترد ولا يُرَدُّ على اليتيم ويتيمه يكون في حياة أبيه وما وهبه لولده الصغير حيزته حلّة له إن لم يسكنه أو ألبسه إن كان ثوبا ولا حلّ له إلا ما عرفته بالعين فالأكبير لا تحل له حيزته ولا يرجع الرجل من صدقته ولا ترد عليه إلا بالميراث ولا بأس أن يشرب من لبن ما تصدق عليه ولا أن يشتري ما تصدق عليه والموهوب للعوض إما أثاب القيمة أو رد الهبة وذلك إذا كان يرى أنه أراد الثواب من الموهوب له».
- Écarts canon : «السائل» (2 lectures 400 dpi concordantes) vs canon shamela 11373/140 «السنة» — N.d.T. consigné ; queue «الثواب من الموهوب له» imprimée, absente du canon shamela (11373 s'arrête à «القيمة أو رد الهبة») — consignée.
- Canon fetché : shamela 11373/140-141 (4 passages WebFetch) + الثمر الداني shamela 7441/572 (dérivation الشفع/الوتر + définition Ibn al-Ḥājib «أخذ الشريك نصيبا من نصيب شريكه بيعا» corrobore).
- Renvois letter confirmés : [جامع الأمهات ١/٤١٦] / [البخاري كتاب الشفعة باب الشفعة فيما لم يقسم إذا أُقيمت العلامات وأنفرجت الطرق فلا شفعة] / [الفواكه الدواني ٢/١٥٣] / [البخاري كتاب الزكاة باب الصدقة من كسب طيب] / [المصباح المنير مادة عصر] / [شرح حدود ابن عرفة ص٤٢٧ — lexie douteuse consignée] / [الموطأ كتاب الشفعة باب ما لا تقع فيه الشفعة].
- Registre IA-3 → pdf-11. SUIVANT pdf-12 الحبس وهبة الثواب pp.93+ (متن aperçu p.93 : «ويكره أن يهب لبعض ولده ماله كله… ومن وهب هبة فلم يحزها الموهوب له حتى مرض الواهب أو أفلس…» + الحبس «ومن حبس دارا فهي على ما جعلها عليه إن حيزت قبل موته…») — canon shamela 11373/141-142 pré-fetchable.

## W34 — 2026-11-21 — IA-3 — traduction fiqh-3es leçon 10 أحكام المزارعة (pdf-10, pp.77-83, suite W33) — RE-PRISE après passation v2 (URL dépôt + PAT fournis ; clone repo-417 réparé après checkout incomplet «no space left on device» — index reconstruit par git reset --mixed, checkout complété par git restore ; ht3-mirror (656 Mo PDFs wadod recouvrables) libéré)

- ORDRE DU PROPRIÉTAIRE R777 APPLIQUÉ : traduction SEULE (s-commentaires suspendus — la recommandation §8 de la passation v2 «s-commentaire L24 hadith-5ep» est PÉRIMÉE) ; carte PARTAGE-TRADUCTION : fiqh-3es = zone IA-3 (197), leçons DANS L'ORDRE → pdf-10 (slot du SUIVANT W32, sa session parallèle perdue) avant pdf-12 ; W33 (pdf-11 الشفعة والتبرعات) re-posé et poussé ce tour (commit d23e9860, re-pose du livrable reconstruit après recyclage).
- MATIÈRE : content/textbooks-src/fiqh-3-iadadi_text.pdf pp.77-83 par couche pdftotext pp.76-84 + 14 lectures VLM 150 dpi (2 moitiés × 7 pages, 2+ passes) + 14 zooms 600-1200 dpi + 4 re-zooms ciblés (clause هـ p.80, hadith أبو الزبير p.82) ; leçon délimitée : استثمار L9 + إعداد p.76, متن pp.77-78, الفهم/استخلاص p.78, التحليل 2 axes pp.79-82, التقويم/استثمار خليل p.83, إعداد الشفعة p.83.
- CANON : shamela 11373/134-135 fetché (fin المزارعة → المساقاة → الشركة في الزرع → الجائحة : règle du tiers, exclusions, البقول, خلاص, 5 أوسق) ; Mukhtaṣar Khalīl shamela 11355/245 (ص180 = renvoi imprimé ✓) + شرح الزرقاني 14297/2710 corroboration ; aliftaa.jo ResearchId=221 (الجوائح عند المالكية, as-Ṣayfī) pour définitions et البقول.
- ARBITRAGES : متن — البذر imprimé (3 lectures letter) vs canon الزرع (variante d'édition consignée) ; نخلات imprimé (3 letter) vs canon خلاص (consigné) ; تقاربت tranché (zoom 600 + canon contre VLM 150 تفاوتا) ; ينقد maintenu (couche+canon contre zoom ينقطع) ; أصاب الثلث فأكثر maintenu (canon+sens contre lectures corrompues أجيح/أجاب/قبل) ; البقول «ما لا تطول مدته» tranché (zoom+VLM+canon aliftaa — pas d'écart) ; جذاذ maintenu (2 letter+canon contre zoom الجناب) ; جنانه maintenu (2+canon contre zoom جنوبه) ; clause هـ = الإكنان من عندهما (couche letter + zoom fin «كان من عندهما» contre VLM «خطأ البائع») ; أهليتا الشركة والإجارة (VLM bas+sens contre corruptions) ; بناء renvoi الدواني 2/127 tranché (couche bidi 2/721→127 + VLM ×2) ; ابن عرفة [المختصر الفقهي 6/189] tranché (couche bidi 981/6→189 + VLM+zoom) ; définition أبو الحسن «كالبرد والريح والجيش» — 2 letter concordantes maintenues vs aliftaa «الحشيش» (N.d.T. consigné) ; clause 1 الشروط «أن تكون الثمرة من بيع لا إن كانت من مهر ولا من هبة ولا صدقة» — structure imprimée portée telle quelle (3 letter), canon aliftaa (achat indépendant de l'origine) consigné ; خليل : «لم يبذ/يبذر» letter vs variante 11355 «لم يبذر» vs éditions courantes «لم ينتفض» — N.d.T. ; «بممنوع/تساونا/لتبرع» letter-major imprimé vs canon fetché consigné ; hadith أبو الزبير : canon Muslim «وهو يأخذ» vs imprimé «هتأخذ» — N.d.T. ; renvoi [صحيح مسلم كتاب المساقاة باب فضل الغرس والزرع] ✓ 3 concordances ; [صحيح مسلم ... باب وضع الجوائح] ✓ 3 concordances ; zoom j-asbab vide (marge de page) — zone couverte par j-islah.
- POSE : hand-set w34-pose-f3l10.py — QA PASS (balises équilibrées, guillemets appariés, 0 apostrophe droite, 0 arabe, 9 h2, 1 dl, 2 ul, 1 ol) ; registre IA-3 → pdf-10 ; worklog W34.
- SUIVANT : pdf-12 الحبس وهبة الثواب (leçon 12, pp.93+, متن aperçu p.93 — canon shamela 11373/141-142 pré-fetchable) ; pdf-11 déjà posé (W33) ; la séquence ordre de la carte est rétablie.

## W35 — 2026-11-22 — IA-3 — COLLISION W34 consignée (livraison parallèle pdf-10 par la session W34, 896089f fait foi — reprise de cette session sur un état antérieur au fetch, responsabilité de cette session) — version locale pdf-10 (16 306 car FR-seule) ÉCARTÉE sans re-pose (R622, aucun --force)

- Chronologie : cette session a posé pdf-10 en local (16 306 car, QA PASS, commit 29bde5f) mais le push a révélé 4 commits distants : d23e986 (W33 parallèle : pdf-11 الشفعة والتبرعات, re-pose après recyclage) + 896089f (W34 parallèle : pdf-10 المزارعة, 16 115 car annoncés / 17 362 posés) + 2 rendus CI ; rebase effectué, les JSON distants repris tels quels (pdf-10 + pdf-11 livrés par la session parallèle font foi), cette entrée remplace l'entrée W33 locale (redondante).
- TRAVAIL SAUVÉ (non posé, à disposition de l'arbitre) : htmlFr pdf-10 complet 16 306 car dans work/l10/pdf-10.html + bbox RTL reconstruit (5 651 mots-lettres pp.77-83) + couche + ~60 crops/passes VLM (150/600/1200 dpi, passes 1-7) + canon fetchés (shamela 11373/134-135, 11355/245, Muslim 1552-1554 ×4 sources web).
- 6 CONSTATS PROPOSÉS À L'ARBITRAGE (écarts letter-reads entre la livraison W34 posée et les preuves de cette session) :
  1. matn/citation «فإن أجيح قدر الثلث فأكثر» — couche ×2 (p.78 matn + p.82 citation : أ-ج-ي-ح) + VLM 600 dpi ×2 + canon shamela 11373/135 «فإن أجيح» ; W34 livré «فإن أصاب الثلث» (maintenu per canon+sens contre lectures corrompues — constat : la couche porte أجيح deux fois, أصاب n'y apparaît pas).
  2. عرية : «ومن أعرى ثمر نخلات لرجل من جنانه» — أعرى letter-confirmé ×3 (ع, point unique suscrit, boucle ouverte) contre أغرس ; ثمر (ث couche+canon, نمر = comptage de points VLM non fiable) ; canon shamela 11373/135 fetché par cette session porte «ومن أعرى ثمر نخلات» — PAS «الزرع/خلاص» que consigne W34 (éditions shamela divergentes ? à arbitrer).
  3. clause هـ- des شروط : «خلط البذر إن كان من عندهما» — letter-confirmé 600 dpi (khāʾ-lām-ṭā, boucle fermée + 2 dents) + cohérent avec خليل «وخلط بذر إن كان» ; W34 livré «الإكنان من عندهما» (couche letter + zoom) — les deux lectures viennent du même scramble de couche «إكنان من عندهما ذر بلط», à arbitrer.
  4. hadith أبو الزبير : «بم تأخذ مال أخيك بغير حق؟» — bbox letter (ب-م + ت-أ-خ-ذ) + canon Muslim (dorar/بلوغ المرام «بم تأخذ») ; W34 livré «هتأخذ» avec N.d.T. vs canon «وهو يأخذ» — les trois leçons (بم/هـ/وهو) existent selon les éditions, à arbitrer.
  5. خليل «إن لم يبذر» — crop 600 dpi net de cette session (لم يبذر = canon shamela 11355/245) ; W34 consigne «لم يبذ/يبذر letter» — lecture identique in fine, écart de description seulement.
  6. أسباب الجوائح : cette session lit «...والعرق والسموم والغبار، وغير ذلك من كل ما لا يستطاع دفعه» (والغبار 600 dpi + corroboration islamweb : بداية المجتهد/التبصرة «والسموم والغبار») — W34 ne mentionne pas الغبار (أسباب ×10 sans suite ?) ; à arbitrer.
- Points CONCORDANTS relevés : فأصابها برد (imprimé vs canon فأجيح ببرد — les deux sessions l'ont posé, W34 sans N.d.T. apparemment) ; تقاربت / ينقد / اشتري / توضع جائحة البقول / فأقل / إلا بالعين والعرض / أزهت / الجذاذ / جنانه / معجوز / المختصر الفقهي 6/189 / الفواكه الدواني 2/127 / مختصر خليل ص:180 / hadith du غرس avec «وما أكلت الطير فهو له صدقة» (= canon Muslim) / أهلية الشركة والإجارة / كالطعام / أبو الحسن ثمانية مسائل / شروط الجائحة ×4 incl. «من بيع لا إن كانت من مهر» anacoluthe.
- Pose : AUCUNE cette session (l'écart est la consigne) ; registres inchangés (pdf-10 + pdf-11 déjà inscrits par la session parallèle, 11 ids).
- SUIVANT : pdf-12 أحكام الحبس وهبة الثواب (pp.93+, canon shamela 11373/141-142 pré-fetchable) — AUCUN CLAIM de cette session (contexte consommé par le pipeline pdf-10 écarté) ; la leçon reprend selon le SUIVANT W34, priorité au tail du worklog.
## W35 — 2026-11-21 — IA-3 — traduction fiqh-3es leçon 12 أحكام الحبس وهبة الثواب (pdf-12, pp.93-99, suite W34)

- ORDRE DU PROPRIÉTAIRE R777 APPLIQUÉ (traduction seule, zone IA-3 fiqh-3es, leçons dans l'ordre) ; fetch-avant-pose : origin d9fc2b6d (CI après W34 896089f1), slot pdf-12 vérifié vide, ff-only local.
- MATIÈRE : content/textbooks-src/fiqh-3-iadadi_text.pdf pp.93-99 par couche pdftotext pp.92-101 + 14 lectures VLM 150 dpi + 9 zooms 600-1200 dpi ; leçon délimitée : متن pp.93-94 (2 p.), glossaire ×4 (سائع, أفلس, انقرض, يكلب), استخلاص ×3, التحليل 2 axes (أولا : هبة المال الكثير/اليسير/ما تبطل به + الصدقة بكل المال + الحيازة في التبرعات ; ثانيا : تعريف/حكم/أركان ×4/شرط الحبس/انقراض عقب/وفاة بعض المحبسين/بيع الحبس ×2), التقويم ×4 (incl. صورة العمل), استثمار ابن رشد [بداية المجتهد 4/711], إعداد الرهن والعارية والوديعة ; L13 démarre p.100 (متن الرهن dès p.100).
- CANON : shamela 11373/141-142 fetché (142 par miroir ftp.shamela.ws — shamela.ws timeout ×2 consigné) — le canon CONFIRME le متن composé du tirage : «ومن أعمر رجلا حياته دارا رجعت بعد موت الساكن ملكا لربها وكذلك إن أعمر عقبه فانقضى بخلاف الحبس فإن مات المعمر يومئذ كانت لورثته يوم موته ملكا» (clause العمرى, ×3 letter concordantes) ; «ويؤثر في الحبس أهل الحاجة بالسكنى والغلة» (الغلة tranché ×3 contre couche العلة) ; «ومن سكن فلا يخرج لغيره إلا أن يكون في أصل الحبس شرط فيمضي» (fimmadhi tranché ×3+canon contre zoom نصب فيصير) ; «ولا يباع الحبس وإن خرّب» ✓ ; «ويباع الفرس [الم]حبس يكلب ويجعل ثمنه في مثله أو يعان به فيه» ✓ (canon «الفرس الحبس», tirage المحبس — variante consignée).
- ARBITRAGES : سائع imprimé (×2 : متن+glossaire letter) vs canon سائغ — N.d.T. ; فلم يحزها tranché ×3+canon contre فلم ياخذه/فلحزها ; الإشهاد tranché (couche+VLM bas) contre الإنهاء/الإنشاد — canon Bukhārī ✓ ; عُقوق الباقين tranché letter-major contre عوق/عرق corruptions ; التوادر والزيادات 12/210 tranché (bidi 012//21 + VLM ×2) ; vers ابن عاصم «والحوز شرط صحة التخبيس قبل حدوث موت أو إفلاس» + clause التسولي «سائر التبرعات من هبة أو صدقة أو نحلة» — ينعقد/يتعقد/ينفذ lectures divergentes, letter porté translittéré neutralisé en «sauf le contrat de mariage constitué sur elle» (sens canon) ; البهجة في شرح التحفة 2/379 tranché (bidi 973/2 + VLM ×2) ; لغة الحبس «حبيس والجمع حبس مثل بريد وبرد» tranché ×2 ; الصحابة «كعمر بن الخطاب وعثمان وعلي وطلحة والزبير» tranché zoom600+v150 contre couche corrompue ; أركان ×4 letter (الواقف أهل التبرع / الصيغة / الموقوف مملوكا ذاتا أو منفعة «دارا» / الموقوف عليه أهلا للتملك حكما كالمسجد أو حكما كالأدمي) ; شرط الحبس «إن حيزت قبل موته» + إذن الوقف على معين vs غير معين كالمسجد letter ✓ ; بيع الحبس «ولا يباع الحبس ولا أُنفاضه إذا شرط الوقف عدم بيعه» — letter ×2 (أنفاضه/أقفاصه divergents) porté «ni ce qui en est désaffecté» sens-consigne ; يكلب بفتح الياء واللام + الهرم والمرض + الموقوفة لتسليكها أو لعملها tranché ×2-3 ; الجهاد tranché (couche letter) contre VLM الجهاز ; موطأ ابن وهب «بيع داثر وبئر تعطل ويعوض به ربع» — letter couche maintenu avec sens neutralisé en français (citerne/puits dont l'usage s'est arrêté) ; ابن رشد citation conforme canon بداية المجتهد (letter-renvoi 4/711 maintenu contre VLM corrompues بدائع الصنائع/إرادة الصحيح — N.d.T.) ; التقويم item 2 «أعرف بالوقف» letter couche+zoom contre أعرض VLM ; أهداف أتعرف ×3 letter couche+convention série contre أعرف VLM150/zoom.
- POSE : hand-set w35-pose-f3l12.py — QA PASS (balises équilibrées, guillemets appariés, 0 apostrophe droite, 0 arabe, 9 h2, 1 dl, 2 ul, 1 ol) ; registre IA-3 → pdf-12 ; worklog W35.
- SUIVANT : pdf-13 أحكام الرهن والعارية والوديعة (leçon 13, pp.100-107 — متن الرهن dès p.100 déjà aperçu couche pp.92-101 ; canon shamela 11373/142-144).

## W36 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 13 أحكام الرهن والعارية والوديعة (pdf-13, pp.100-108, suite W35) POSÉE

- FETCH-AVANT-POSE : origin 174cbec (CI après W35-2 9b9c004 pdf-12), slot pdf-13 vérifié vide, ff-only local, aucune collision.
- INCIDENT OUTIL : API VLM indisponible toute la session (429 « Too many requests » persistant > 2 h, ~10 tentatives espacées 2-20 min, dernière à 22 h 40 env.) — PIVOT méthodologique conforme SOLUTION-OUVRAGES §4 (VLM = dernier recours) : extraction par TRIANGULATION de trois couches indépendantes — (1) couche pdftotext -layout + pdftotext -bbox (reconstruction RTL des lignes, scripts/l13-bbox-reconstruct.py, 209 lignes pp.99-108) ; (2) tesseract ara tessdata_best 12,6 Mo téléchargé, 300 dpi pleine page ×10 + 600/1200/2400 dpi microcrops (scripts/l13-crops.py, l13-c1200.py, l13-c1200b.py, inventaires de lettres scripts/l13-inv.py) + binarisation PIL (seuils 110-190) + passe eng pour les chiffres ; (3) canon shamela fetché en direct (11373/142-144 par ftp.shamela.ws ; 11355/228-231 pour l'ouverture du رهن de خليل ; dorar/hadithprophet pour le hadith de صفوان). Résolution des divergences par letter-majorité + canon + sens, méthode W32/W34.
- MATIÈRE : work/fiqh3.pdf pp.100-108 (L13 = أهداف ×3 p.100, تمهيد, متن pp.100-101, شرح (glossaire ×3) + استخلاص ×3 p.101, أولا الرهن pp.101-103 [تعريف/حكم/أركان ×4/ما يتم به/ضمان أ-ب/غلة], ثانيا العارية pp.104-105 [تعريف ابن الحاجب/أركان ×4/حكم + hadith صفوان + hadith أبي أمامة + منحة + وجوه التعدي], ثالثا الوديعة pp.105-107 [تعريف/حكم + آيتان + hadith أبي هريرة + النفراوي/أركان ×3/تصرف المودع عنده ×4], تقويم ×4 p.107, استثمار ابن عسكر + أتأمل ×3 + إعداد ×2 p.108 ; L14 démarre p.109).
- متن الرسالة (letter, couche+tess 300/1200) : «والرهن جائز ولا يتم إلا بالحيازة ولا تنفع الشهادة في حيازته إلا بمعاينة البينة وضمان الرهن من المرتهن فيما يغاب عليه ولا يضمن ما لا يغاب عليه وثمرة النخل الرهن للراهن وكذلك غلة الدور … وما هلك بيد أمين فهو من الراهن والعارية مؤداة يضمن ما يغاب عليه ولا يضمن ما لا يغاب عليه من عبد أو دابة إلا أن يتعدى والمودع إن قال رددت الوديعة إليك صدق إلا أن يكون قبضها بإشهاد وإن قال ذهبت فهو مصدق بكل حال والعارية لا يصدق في هلاكها فيما يغاب عليه ومن تعدى على وديعة ضمنها وإن كانت دنانير أو دراهم فردها في صرتها ثم هلكت فقد اختلف في تضمينه ومن اتجر بوديعة فذلك مكروه والربح له إن كانت عينا وإن باع الوديعة وهي عرض فربها مخير في الثمن أو القيمة يوم التعدي».
- VARIANTE MAJEURE CONSIGNÉE (N.d.T.) : l'imprimé SUSPEND le matn par points de suspension «…» après «وكذلك غلة الدور» (couche ×2 : littéral «الدور ... »), omettant la clause canonique shamela 11373/142 «والولد رهن مع الأمة الرهن تلده بعد الرهن ولا يكون مال العبد رهنا إلا بشرط» — rendue par «[…]» + N.d.T. ; «أو دراهم» imprimé (tess 300 + citation du شرح p.106) vs canon 11373/143 «دنانير» seuls — N.d.T.
- يُغاب/يُعاب RÉSOLU : 5 positions dans le matn (رهن ×2, عارية ×2, لا يصدق ×1) — tesseract 1200 dpi lit يغاب uniforme (+ canon يغاب ×5 + glossaire imprimé يغاب ×2 à 1200 dpi + شرح «فيما يغاب عليه» ×2) ; les lectures يُعاب (couche IA et tess 300 isolés) sont désavouées comme bruit OCR غ/ع — aucun N.d.T., worklog seul.
- ARBITRAGES : «ولا تنفع الشهادة» tranché (tess 300+1200 avec ت ; couche sans ت = lettre perdue) ; «مؤداة» (شدة, couche) ; hadith عائشة «اشترى من يهودي طعاما إلى أجل ورهنه درعا له من حديد» (tess 1200 ×2 ; «الذي هو البينة فيه» tess ×2 contre couche «أو بينة حفيظة» fragments non restitués — consigné ici) ; [صحيح البخاري كتاب الرهن باب من رهن درعه] tess 1200 ; «مأبورة» (fécondées) ; titre 6 «مستحق غلة الرهن» rendu par sens («Le droit au revenu du gage») ; «قاله مالك» (tess ×2) + [كفاية الطالب الرباني 2/248] bidi 248/2→2/248 ; hadith صفوان : isnād «عن أمية بن صفوان بن أمية عن أبيه» (tess 1200), «أغصبا يا محمد» (tess 300 + canon dorar/hadithprophet contre couche أغضبا), «فضاع بعضها» (reconstruction tess 1200 فضاح/couche فصاع = فضاعت/فضاع, canon dorar «فضاع بعضها»), «أنا اليوم في الإسلام أرغب» ✓ ; n° [مسند أحمد رقم: 15302] — numéro partiellement illisible à travers 6 passes (fragments «15…», «42», «107», «6153209»), complété d'après l'édition ar-Risāla (hadithprophet : «وهو في مسند أحمد (١٥٣٠٢)») + N.d.T. ; hadith أبي أمامة الباهلي (tess 1200 «أبي أَمَامَة البَاهلي» — corrige ma première reconstruction حماد) خطبة عام حجة الوداع «العارية مؤداة والمنحة مردودة والدين مقضي والزعيم غارم» (الزعيم tess 1200 + canon Tirmidhī/Nasāʾī/Ibn Mājah 2714 contre couche الرعي) [سنن الترمذي أبواب الوصايا باب ما جاء لا وصية لوارث] ; transition «ثم قال» (fragment «….ث» ×2 couches, canon) ; المنحة «الشاة أو نحوها تعار لأخذ لبنها» (tess 1200 «الشاة أو نحْوها تَعَارُ لأخذ لِبَنها») ; تعدي : «الزيادة في الحمل، الزيادة في المسافة، وكذلك يضمن في صورة أخرى وهي أن يتبين كذبه كما إذا قال تلفت في موضع كذا ولم يسمع أحد من الرفقة بتلفها» (assemblage couche+tess, «الرفقة بتلفها» résolu par concaténation des fragments pp.105) ; آيات : البقرة 282 imprimée ×2 (tess 1200 ×2 + couche, contre numérotation standard 283 — transcrit tel qu'imprimé, convention de l'édition), النساء 57 (tess 1200 ; std 58), الحج 75 «وافعلوا الخير» (tess 1200 ; std 77), الضحى 3 ✓ ; 2e citation البقرة p.106 = «فإن أمن بعضكم بعضا فليؤد الذي اؤتمن أمانته» (résolu par fragments croisés ×4 passes — بعضكم/بعضا + فليؤد/ائتمن أمانته — + sens wadīʿa + même verset que p.102 ; police coranique ornée illisible aux moteurs, consigné ici) ; «والقراض» (tess 300 + couche concordants ; sens : le mudārib est cru comme le dépositaire) ; hadith أبي هريرة «أد الأمانة إلى من ائتمنك ولا تخن من خانك» [سنن الترمذي أبواب البيوع باب 38] (tess 1200) ; النفراوي «وأداء الأمانة من علامات الإيمان ومن عمل المؤمنين، وأما الخيانة فهي من علامات النفاق وعمل الفساق، وأجمعت الأمة على حسن الإيداع» [الفواكه الدواني 2/170] (tess 1200, الخيانة/الحياءة résolu) ; استثمار ابن عسكر [إرشاد السالك إلى أشرف المسالك في فقه الإمام مالك ص: 97-98] — citation reconstruite croisée (tess 300+1200+couche) : «العارية تمليك المنفعة المباحة وضمانها كالرهن فإن أعار إلى أجل فلا رجوع قبله وإن أطلق فحتى ينتفع بها انتفاع مثلها وللمستعير أن يعير وإذا عين منفعة لم يكن له مجاوزتها والمودع أمين فيقبل في الرد والتلف فإن قبضها ببينة لم يقبل ردها بغيرها وله إيداعها عند زوجته وخادمه ويضمن لغيرهما كالسفر بها إلا أن يتعذر ردها ولا يجد ثقة فإن استودعها فيه فعرضت له إقامة فله إرسالها مع ثقة ولا ضمان كنقلها إلى حرز».
- LEXIE DOUTEUSE CONSIGNÉE (N.d.T.) : إعداد item 2 «2- …الضمان وحكمه» — la tête (premier mot) est illisible à travers toutes les passes (couche «رتك», tesseract 2400 «أحكام الضمان» partiel «االاصحمعماك», binarisation «ابر») ; la fin «الضمان وحكمه» est ferme ; «les règles de» restitué par fragments + objectifs L14 («أدرك أحكام الضمان والغلة في الغصب») ; N.d.T. posée.
- Définitions خليل p.101 : «الرهن بذل من له البيع ما يباع أو غررا ولو اشترط في العقد وثيقة بحق» [مختصر العلامة خليل ص: 166] — citation elliptique telle qu'imprimée ; l'édition électronique shamela 11355/229 porte EXACTEMENT la même leçon («الرَّهْنُ: بَذْلُ مَنْ لَهُ الْبَيْعُ مَا يُبَاعُ أَوْ غَرَرًا…») — concordance vérifiée, N.d.T. courte posée.
- Renvois letter : [المختصر الفقهي لابن عرفة 6/319] (bidi 319/6), [جامع الأمهات 1/401] et [1/404] (bidi 401/1, 404/1), [كفاية الطالب الرباني 2/248], [الفواكه الدواني 2/170], [صحيح البخاري كتاب الرهن باب من رهن درعه], [مسند أحمد رقم: 15302 complété], [سنن الترمذي أبواب الوصايا باب ما جاء لا وصية لوارث], [سنن الترمذي أبواب البيوع باب 38], [إرشاد السالك إلى أشرف المسالك في فقه الإمام مالك ص: 97-98].
- Imbrication de guillemets ×2 dans le matn (discours direct «رددت الوديعة إليك»/«ذهبت») — précédent pdf-5 (question dans hadith) ; tous les autres guillemets appariés simples.
- htmlFr FR-seule 22 217 car, QA typo PASS (0 arabe, guillemets appariés, 0 apostrophe droite, balises équilibrées, 9 h2, 1 h1, 1 dl, 2 ul, 1 ol, 4 h3, 4 N.d.T.) ; structure calquée sur L1-L12 (objectifs ×3, تمهيد ×2, متن + N.d.T. ×2, glossaire ×3, استخلاص ×3, 3 axes : الرهن [تعريف/حكم/أركان ×4/ما يتم به/ضمان أ-ب/غلة] + العارية [تعريف/أركان ×4/حكم avec 2 hadiths + منحة + تعدي] + الوديعة [تعريف/حكم avec 2 آيات + hadith + النفراوي/أركان ×3/تصرف ×4], تقويم ×4, استثمار ابن عسكر + أتأمل ×3, إعداد ×2 → L14).
- POSE : hand-set w36-pose-f3l13.py (1 emplacement) ; registre IA-3 → fiqh-3es/pdf-13 (13 ids). Livre 14/29 posés (pdf-1..pdf-13 + 2 index).
- SUIVANT : fiqh-3es L14 أحكام اللقطة والغصب (pdf-14, pp.109-…, متن «ومن وجد لقطة فليعرفها سنة بموضع يرجو التعريف بها…» déjà aperçu p.109 ; canon shamela 11373/143-144 déjà fetché en W36).
- Trace 1a1fff8f52c31769.

## W36-b — 2026-11-22 — IA-3 — COLLISION R622 pdf-13 : pose parallèle 9ae5af3 ADOPTÉE, contre-vérifiée par le matériel indépendant de la session recyclée

- Au re-clone (sparse, filter=blob:none, 65 Mo — recyclage du sandbox avait perdu le clone complet), fetch révèle pdf-13 DÉJÀ POSÉ par la session IA-3 parallèle (9ae5af3, «VLM INDISPONIBLE 429», extraction couche-bbox + tesseract) + CI b94b088. Règle R622 appliquée : PAS de re-pose, adoption amont.
- Le matériel parallèle de la session recyclée (hors dépôt, download/f3-l13/ : VLM 150 dpi 9/9 pages réussies + 20 zooms VLM 600-1200 dpi + canon shamela 11373/142-144 fetché indépendamment + htmlFr FR-seule 22 222 car QA PASS, n13-htmlfr.html) sert de CONTRE-VÉRIFICATION de la pose 9ae5af3 — concordance de substance vérifiée sur :
  * متن intégral (الحيازة / بمعاينة البينة / يغاب ×5 / ثمرة النخل + suspension […] / بيد أمين / مؤداة / إلا أن يتعدى / إشهاد / ذهبت / ضمنها / دنانير / اتجر مكروه / مخير في الثمن أو القيمة) ;
  * N.d.T. «canon 11373/143 دنانير seuls» CONFIRMÉE par le canon fetché de la session recyclée («دنانير فردها في صرتها», canon-143.txt) ;
  * renvois : المختصر الفقهي 6/319 ✓, مختصر خليل ص166 ✓, كفاية الطالب 2/248 ✓, جامع الأمهات 1/401 ✓, 1/404 ✓, الفواكه الدواني 2/170 ✓, إرشاد السالك ص97-98 ✓, مسند أحمد 15 302 + N.d.T. ✓, الترمذي أبواب الوصايا ✓, أبواب البيوع باب 38 ✓, an-Nafrāwī ✓ ; آyat numérotation de l'édition transcrite telle quelle ✓ ;
  * json : 23 612 car, 9 h2, 0 arabe, guillemets 51/51, 0 apostrophe droite — QA structurelle PASS.
- OBSERVATIONS consignées (non bloquantes, pour future vague de retouches) :
  1. «والربح له إن كانت عينا» rendu «s'il était une monnaie» — lexie عين = corps certain / chose en elle-même (le متن l'oppose à عرض «marchandise») ; «monnaie» est une restriction indue (l'عين peut être un livre, un ustensile) — suggéré «une chose en elle-même».
  2. Méthode canon-first (مخير, رددت traduits d'après le canon sans N.d.T. de la letter) vs convention letter-major+N.d.T. de la série (pdf-10/11/12) — choix documenté dans le commit 9ae5af3 ; la letter imprimée porte «فربها مخلطا في النفذ أو القيمة» (VLM 150 + zoom 600 concordants) et «رد الوديعة إليك» (couche+VLM 150) — pour mémoire.
  3. p.106 2ᵉ āyāt : la session recyclée lisait par zoom 1200 un AUTRE fragment du même verset البقرة 282 («وَإِذَا حَكَمْتُمْ بَيْنَ النَّاسِ…») que la reconstruction 9ae5af3 («فإن أمن بعضكم بعضا…») — les deux lectures sont des fragments du même verset, aucune contradiction de substance.
- Inventaire parallèle complet + arbitrages détaillés : download/f3-l13/REPRISE.md (workspace). SUIVANT inchangé : pdf-14 أحكام اللقطة والغصب pp.109+ (canon shamela 11373/143-144 déjà fetché des deux côtés).
- RAPPEL PAT : l'utilisateur doit RÉVOQUER le PAT (re-fourni en clair dans la passation).

## W37 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 14 أحكام اللقطة والغصب (pdf-14, pp.109-115, suite W36) POSÉE

- FETCH-AVANT-POSE : origin f0669149 (CI après W36-b df29d7f0), slot pdf-14 vérifié vide, ff-only local, aucune collision.
- INCIDENT OUTIL : VLM toujours indisponible (429 ×2 en début de session, consigné) — pivot méthodologique W36 reconduit : TRIANGULATION (1) couche pdftotext -layout + -bbox (dumps mots-glyphes avec coordonnées) ; (2) tesseract ara tessdata_best 300 dpi pleine page ×7 + microcrops 1200/2400/3600 dpi ciblés par bbox (scripts/l14-*.py : crops, dump, micro, micro2, micro3, fin, x, last) + binarisation PIL (seuils 110-190) + autocontrast + grossissements ×2-×3 + passes eng pour les chiffres ; (3) canon web fetché en direct : shamela 11373/143-144 (Risāla, par ftp.shamela.ws/ajax/pageContent/11373/N — l'URL de page /book/11373/N renvoie une coquille AJAX), Muwatta islamweb 7/1609 (athar 1454 معاوية) + islamweb 93/3033 (hadith 1453 زيد بن خالد), شرح الزرقاني shamela 14297/2836 + منح الجليل islamweb 24/5279 (définition ابن عرفة du غصب), hadithprophet (Bukhārī 3196), archive.org MajalisKadaa (définition ابن عرفة de la لقطة d'après شرح الحدود). Résolution letter-majorité + canon + sens, méthode W32/W34/W36.
- MATIÈRE : work/fiqh3.pdf pp.109-115 (L14 = أهداف ×3 p.109, تمهيد + questions ×3, متن pp.109-110, الشرح glossaire ×4 (العفاص، الوكاء، ضالة، بفيفاء), استخلاص ×3, أولا تعريف اللقطة والغصب [1- تعريف اللقطة لغة/اصطلاحا ; 2- أحكام اللقطة : أ- ماذا يفعل واجد اللقطة + hadith زيد بن خالد + التافه/فوق التافه/ما يفسد بالتأخير ; 3- محل التعريف ; 4- حكم اللقطة بعد التعريف ; 5- هلاك اللقطة بيد الملتقط ; 6- إذا عرف طالبها العفاص والوكاء (أصبغ/ابن القاسم وأشهب + الغنم بالغرم) ; 7- أخذ ضالة الحيوان ; 8- إتلاف العرض أو المكيل أو الموزون (أ- الباجي عن مالك ; ب- كالبيض)], ثانيا أحكام الغصب [1- تعريفه (لغة [الصحاح مادة غصب] + اصطلاحا ابن عرفة) ; 2- حكمه (آيتا البقرة + hadith البخاري + ابن عبد السلام) ; 3- من أحكام الغصب (أ- ضمان الغاصب ; ب- وقت الضمان وأحوال المغصوب) ; 4- غلة المغصوب وربحه (أشهب وابن زياد/الفاكهاني/المدونة) ; 5- تصرف الغاصب في المال المغصوب (الآبي الأزهري, الثمر الداني 568)], تقويم ×4 (incl. الخراج بالضمان), استثمار أثر معاوية بن عبد الله بن بدر الجهني + أتأمل ×3, إعداد ×2 ; L15 أحكام الأقضية والشهادات démarre bas p.115/116).
- متن الرسالة CONFORME CANON shamela 11373/143-144 MOT À MOT (vérifié clause par clause) : «ومن وجد لقطة فليعرفها سنة بموضع يرجو التعريف بها فإن تمت سنة ولم يأت لها أحد فإن شاء حبسها وإن شاء تصدق بها وضمنها لربها إن جاء وإن انتفع بها ضمنها وإن هلكت قبل السنة أو بعدها بغير تحريك لم يضمنها وإذا عرف طالبها العفاص والوكاء أخذها ولا يأخذ الرجل ضالة الإبل من الصحراء وله أخذ الشاة وأكلها إن كانت بفيفاء لا عمارة فيها ومن استهلك عرضا فعليه قيمته وكل ما يوزن أو يكال فعليه مثله والغاصب ضامن لما غصب فإن رد ذلك بحاله فلا شيء عليه وإن تغير في يده فربه مخير بين أخذه بنقصه أو تضمينه القيمة ولو كان النقص بتعديه خير أيضا في أخذه وأخذ ما نقصه وقد اختلف في ذلك ولا غلة للغاصب ويرد ما أكل من غلة أو انتفع … ولا يطيب لغاصب المال ربحه حتى يرد رأس المال على ربه ولو تصدق بالربح كان أحب إلى بعض أصحاب مالك وفي باب الأقضية شيء من هذا المعنى».
- VARIANTE MAJEURE CONSIGNÉE (N.d.T.) : l'imprimé SUSPEND après «أو انتفع» par des points de suspension (couche «...» + tesseract 300/1200 littéraux — points imprimés, non artefact), omettant la clause canonique 11373/144 «وعليه الحد إن وطئ وولده رقيق لرب الأمة» — rendue par «[…]» + N.d.T. (précédent W36 L13 «وكذلك غلة الدور ...»).
- ARBITRAGES : بفيفاء tranché (tess 2400 dpi mot isolé «إن كانت بفيفاء لا عمارة فيها» + t300 matn + glossaire imprimé «بالمَد») contre lectures بقفاء/بقيقاء/قيفاء = bruit OCR ف/ق (comptage de points non fiable, précédent W34) — canon «بفيفاء» ✓ ; «والغاصب ضامن لما غصب» tranché (t300 + tess 2400 + canon) contre العاصب/عصب de la couche (bruit غ/ع) ; «ناطقا» tranché ×5 passes contre «ضائعا» (couche) — canon شرح الحدود «ليس حيوانا ناطقا ولا نعما» ✓ (الحيوان الناطق = l'humain) ; «أخذ مال غير منفعة ظلما وقهرا لا بخوف قتال» letter (tess ×3) — canon الزرقاني/منح الجليل mot à mot ✓ ; «لا تعتدوا» (tess 2400 ×2) contre تَعتك/تجتخ ; «لربها إن جاء» ×3+canon contre «لبها» ; «أجمع كل الملل على حرمته» (tess 2400 autocontrast «أَجْمَعَ كل الملل») contre «كل امل» t300 ; «ثم عرفها سنة» (tess 2400) = canon Muwatta 1453 ✓ ; «فضالة الغنم» contre «العْن» (tess + canon) ; ordre غنم/إبل du hadith = Muwatta 1453 (écart des versions Bukhārī/Muslim où l'ordre est inverse) — imprimé = canon ✓.
- RENVOIS LETTER : [شرح حدود ابن عرفة للرصاع ص: 429] (tess ×4 ; le bidi couche «9341» écarté — l'édition fait 558 p.) ; [المختصر الفقهي 7/253] (tess ara ×4 «7/253» + eng visuel «[253» — les 4 chiffres {7,2,5,3} présents dans le bbox multicouche ; format j/ص comme W36 6/319) ; [الصحاح مادة: غصب] ; [الموطأ كتاب الأقضية باب القضاء في اللقطة] ×2 — CONCORDANCE CANON INTÉGRALE : hadith 1453 زيد بن خالد («جاء رجل إلى رسول الله ﷺ فسأله عن اللقطة فقال اعرف عفاصها ووكاءها ثم عرفها سنة فإن جاء صاحبها وإلا فشأنك بها قال فضالة الغنم يا رسول الله قال وهي لك أو لأخيك أو للذئب قال فضالة الإبل قال ما لك ولها معها سقاؤها وحذاؤها ترد الماء وتأكل الشجر حتى يلقاها ربها» — l'imprimé porte «هي لك» sans le و du canon, écart sans portée consigné ici) ; athar 1454 معاوية بن عبد الله بن بدر الجهني («أن أباه أخبره أنه نزل منزل قوم بطريق الشام فوجد صرة فيها ثمانون دينارا فذكرها لعمر بن الخطاب فقال له عمر عرفها على أبواب المساجد واذكرها لكل من يأتي من الشام سنة فإذا مضت السنة فشأنك بها») mot à mot — l'isnad بن بدر الجهني confirmé par le canon contre toute autre lecture ; [صحيح البخاري كتاب بدء الخلق باب ما جاء في سبع أرضين] (canon 3196 «من أخذ شيئا من الأرض بغير حقه خسف به يوم القيامة إلى سبع أرضين» ✓ intégral) ; [الثمر الداني شرح رسالة ابن أبي زيد القيرواني ص: 568] (bidi couche 865→568, tess ✓).
- VERSETS : البقرة 187 imprimée («ولا تأكلوا أموالكم بينكم بالباطل» — numérotation standard 188, transcrit tel qu'imprimé, convention de l'édition, cf. W36) ; «ولا تعتدوا» [البقرة: 190] — numéro ILLISIBLE par fragments à travers toutes les passes (traces «…0» + glyphes épars dans la couche ; le «4» de la couche identifié comme le guillemet de clôture déplacé), complété d'après le canon + N.d.T. (précédent W36 مسند أحمد 15302).
- LEXIE DOUTEUSE CONSIGNÉE (N.d.T.) : إعداد item 2 «2- ما شروط القضاء؟» — tesseract ×3 (2400 + autocontrast) lit «ما شروط القضاء؟» ferme, suivi d'un court signe illisible (traces «0») ; le bbox multicouche porte des glyphes épars (ة، ن) suggérant une fin plus longue («والشهادة؟» selon les objectifs L15) — transcrit tel que lu + N.d.T. renvoyant aux objectifs de la leçon suivante.
- POINTS CONSIGNÉS AU WORKLOG SEUL : glossaire العفاص — tête et note vocalique lues «الع?اص: بكسر العين وال?اف والصاد المهملة» (ف/ق non tranchés : tess ×3 lit ق dans la tête ET la note, mais le matn ×3 + le canon (الموطأ/البخاري عفاصها) portent ف — comptage de points non fiable ; rendu français «kasra sur le ʿayn et le fāʾ» suivant le canon, la graphie arabe ne paraissant pas dans la couche FR) ; «فعن زيد بن خالد الجهني [؟] أنه قال» — fragment «َه» non résolu entre الجهني et أنه (peut-être رضي الله عنه), rendu sans éponyme ; «سورة البقرة: 187» — le «1» et le «7» épars dans la couche (digits RTL inversés, phénomène bidi W36), le nombre 187 confirmé par tess 300+2400 ×3.
- htmlFr FR-seule 18 862 car, QA typo PASS (0 arabe, guillemets appariés 36/36, 0 apostrophe droite, balises équilibrées, 9 h2, 1 h1, 3 h3, 1 dl, 2 ul, 1 ol, 3 N.d.T.) ; structure calquée sur L1-L13 (objectifs ×3, introduction ×2 ¶, متن + N.d.T., glossaire ×4, استخلاص ×3, 2 axes : أولا [1-8 avec a/b] + ثانيا [1-5 avec a/b], تقويم ×4, استثمار + أتأمل ×3, إعداد ×2 + N.d.T. → L15) ; imbrications guillemets ×6 dans le hadith زيد (dialogue), précédent pdf-5/W36.
- POSE : hand-set w37-pose-f3l14.py (1 emplacement, slot vérifié vide au fetch-avant-pose) ; registre IA-3 → fiqh-3es/pdf-14 (14 ids). Livre 15/29 posés (pdf-1..pdf-14 + 2 index).
- SUIVANT : fiqh-3es L15 أحكام الأقضية والشهادات (pdf-15, pp.115-122 env., متن «والبينة على المدعي واليمين على من أنكر ولا يمين حتى تثبت الخطة أو الظنة...» déjà aperçu pp.116-117 ; canon shamela 11373/145 déjà récupéré ce tour, 146 à fetcher).
- Trace 1a202581e4d5071d-w37.
## W37-b — 2026-11-22 — IA-3 — COLLISION R622 pdf-14 : pose parallèle feb7384 ADOPTÉE, contre-vérifiée par le matériel indépendant de la session recyclée

- Fetch-avant-pose de la session recyclée (après transcription complète hors dépôt : VLM 150 dpi 9/9 pages + 15 zooms 600 dpi + 15 micro-zooms + 11 crops-mots 1200 dpi + canon shamela 11373/143-144 fetché W36 + canon web : Muwaṭṭa bāb al-qaḍāʾ fī l-luqaṭa, al-Isṭidhkār, Bukhārī 2454, الفواكه الدواني) révèle pdf-14 DÉJÀ POSÉ par la session IA-3 parallèle (feb7384, 18 862 car, méthode couche+tesseract W36 reconduite, VLM 429 chez elle) + CI c595791. R622 appliqué : PAS de re-pose, adoption amont.
- CONVERGENCES majeures des deux chaînes indépendantes (matériel recyclé vs pose 9ae5af3-style) : hadith زيد بن خالد en FORME DIALOGUÉE (فضالة الغنم avant فضالة الإبل — les attributions nominatives «العمري/الأريلي» du premier VLM désavouées par canon+zoom600) ; «لأخيك» ✓ ; clôture «فشأنك بها» ✓ (canon الاستذكار) ; البقرة 187 tel qu'imprimé ✓ ; أثر صرة «ثمانون دينارا» ✓ + «فشأنك بها» ✓ ; بفيفاء ✓ ; الباجي عن مالك ✓ ; الصحاح ✓ ; شرح حدود ابن عرفة للرصاع ص429 ✓ ; المختصر الفقهي 7/253 ✓ ; الخراج-الغنم بالغرم ✓ ; كراؤها (contre كفاراتها) ✓ ; matn conforme canon 143-144 ✓.
- OBSERVATIONS consignées (non bloquantes, pour future vague) :
  1. matn : la pose amont suit la suspension imprimée «…» après «أو انتفع» (clause canonique وعليه الحد إن وطئ وولده رقيق لرب الأمة omise, N.d.T.) — la variante recyclée traduisait le canon intégral (clause incluse) ; conforme à la convention R777 «coller au tirage» chez l'amont, divergence de méthode documentée.
  2. 2ᵉ āyāt : l'amont porte «ولا تعتدوا» [البقرة: 190 complétée canon N.d.T.] — mieux ancré que la lecture recyclée «لا تأكلوا» [النساء: 189] ; pour mémoire (le n° du tirage est illisible des deux côtés).
  3. «أجمع كل الملل» (amont, tess2400 autocontrast) vs «المسلمين» (recyclé, z113) — 1v1 chacun, l'amont a la preuve lettre haute-résolution.
  4. إعداد q2 : amont «ما شروط القضاء؟» (tess ×3 + N.d.T. signe résiduel) vs recyclé «ما شروط القضاء والشهادة؟» (couche) — pour mémoire.
  5. Renvoi «الثمر الداني ص: 568» gardé tel qu'imprimé chez l'amont — la variante recyclée l'avait normalisé «al-Fawākih ad-Dawānī» (le titre réel du commentaire) sans N.d.T. ; la convention R777 favorise l'amont.
- Variantes recyclées conservées HORS dépôt : download/f3-l14/n14-htmlfr.html (22 128 car, QA double porte PASS : 0 arabe, 37/37, 9 h2 + 2 h3, 8 N.d.T., alternance guillemets PASS) + trace vlm/zooms/m-crops + couche RTL pp.109-115. SUIVANT inchangé : L15 أحكام الأقضية والشهادات pdf-15 pp.115+ (canon 11373/145 fetché côté amont, 146 à fetcher).

## W38 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 15 أحكام الصلاح في المرض والإبراح (pdf-15, pp.115-120) POSÉE

- ENVIRONNEMENT recyclé entre W37-b et W38 : repo-417 et work/ perdus → re-clone sparse --filter=blob:none (51 Mo) + sparse-checkout add scripts scripts-ia3 content/books ; tirage fiqh-3-thanawi_text.pdf récupéré par BLOB-FETCH (git cat-file blob HEAD:content/textbooks-src/..., 226 p., 10,9 Mo) ; scripts W37 réutilisés/adaptés (w38-couche-rtl, w38-render, w38-vlm-halves, w38-zoom, w38-micro, w38-qa, w38-pose).
- BORNES RÉELLES corrigeant le catalogage initial : la leçon suivant اللقطة والغصب pp.109-115 = **أحكام الصلاح في المرض والإبراح** (titre imprimé p.115 + médaillon [14] + bandeau الرُّبْعُ الرَّابع) pp.115-120, PUIS أحكام صلح أحد الورثين/الشريكين pp.121-128 (titre + médaillon [15] p.121), puis أحكام العولة p.129. L'annonce de W37 «SUIVANT L15 أحكام الأقضية والشهادات» (extrapolée du catalogue) était FAUSSE — الأقضية والشهادات est plus loin dans le livre. Le titleAr/titleFr pré-existants du catalogue pdf-15 («أحكام الأقضية والشهادات» / «Règles des jugements et des témoignages») corrigés à la pose : «أحكام الصلاح في المرض والإبراح» / «Les jugements de la paix dans la maladie et l'hémorragie» ; les docIds pdf-16+ sont À RÉALIGNER sur le tirage par les vagues suivantes (pdf-16 catalogué «من تمنع شهادتهم» = en réalité صلح الورثين/الشركاء pp.121-128).
- MATIÈRE : متن = **المختصر للخليل** («قال الشيخ خليل رحمه الله» — PAS la Risāla qu'attendait le catalogage) bab الدماء : 4 clauses [وإن قتل جماعة أو قطعوا اجْزاءً صلح كل والعفو عنه / وإن صالح مقطوعًا ثم نزف فمات له رده / القتل بقسامة كأخذهم الدية في الخطإ / وإن وجب لمرض على رجل جرح عمدا فصالحه في مرضه برضاه أو غيره ثم مات من مرضه جاز ولزم + وهل مطلقا + وإن صالح أحد وليين فلا آخر الدخول معه + وإن صالح مقرب خطأ بماله لزمه + وخلف فرد إن طلب به مطلقا أو طلبه ووجد] + الفهم glossaire ×3 (نزفى, قسامة بفتح القاف = خمسون يمنى بالتوالي [concord canon Risāla 11373/145 «يقسم الولاة خمسين يمينا»], أرشه) + استخلاص ×4 + تحليل 2 axes (أولا صلح الجماعة عن الدم : 2 صور [الصفح والعفو لكل واحد / المقطوع الذي نزف فمات : رد المال أو القتل بقسامة + الدية كاملة بعد القسامة في جرح الخطإ] ; ثانيا صلح المريض وأحد ولييْن والمقرِّب : 1- المريض [جاز ولزم ابتداء وبعد وقوعه + تأويلان أرجحهما الثاني] 2- أحد ولييْن [لا آخر الدخول + جبرا + متابعة القاتل بحصته] 3- المقرِّب [صورتان : لزوم المال المصالح به + العاقلة لا تحمل الاعتراف (المشهور) أو تحمله بقسامة ; أو جعل + خلف + فرد إن طلب به مطلقا أو طلبه ووجد — كالمغلوب على صلاحه, كالثابت على صدقة]) + قاعدة فقهية (مسألة الْقَاطِع يرجع فيها بما غلط في قيمته دون فوّاته — lecture image 1200 ; la couche portait «مسائل الغلط» bruité, consigné) + القيمة (التكافل الاجتماعي + حرمة الدماء) + تقويم ×4 + استثمار citation المالك/ابن القاسم [التاج والإكليل لمختصر خليل للمواق 7/13-17] + مهام ×3 + إعداد ×3 → صلح أحد الورثين/الشريكين.
- INCIDENTS OUTIL consignés : VLM 429 (quota épuisé après 28 moitiés + 4 zooms ; la parallèle IA-2 travaille en même temps) → pivot : LECTURE DIRECTE des microcrops 1200-2400 dpi par l'agent (multimodal) ×9 + recals ×3 ; canon web du Mukhtaṣar de Khalīl INACCESSIBLE (shamela.ws + al-maktaba.org derrière CAPTCHA ; islamweb reCAPTCHA ; التاج والإكليل 21611 balayé 3424-3479 sans la clause ; منح الجليل 21614 dichotomie interrompue) — la preuve lettre du متن = lecture directe 1200/2400 dpi ×2 + couche + passes VLM ; le canon Risāla 11373/145-148 fetché reste la concordance du GLOSSAIRE (قسامة/أرش).
- ARBITRAGES consignés : «برضاه أو غيره» tranché ×2400 contre l'hallucination VLM «بأرشه أو عوض» ; «فلا آخَرَ الدُّخُولِ معه» (couche+zoom) contre «فلا للآخر» ; التافه... ; titre de leçon : dernier mot «والإبْرَاح» (image 150 + zoom 600 concordants) contre «والجراح» de la couche ICU (bruit de points) — N.d.T. الإبراح = النَّزْف (l'hémorragie), cf. glossaire نزفى ; «مسألة القاطع» (image) vs «مسائل الغلط» (couche) — transcrit «la question du mutilateur...» + consigné ; citation استثمار المالك reconstruite letter-majorité (VLM p119-b + couche p119/p120 : «فلمت أن الدية تلازم مني دون العاقلة فذلك له ويوضع عنه ويلزم أولياء المقتول العاقلة» — «ويلزم» contre «وينبع» bruit VLM, sens + clause خليل).
- htmlFr FR-seule 14 848 car, QA double porte PASS ×2 (0 arabe y compris N.d.T. translittérés, apostrophes typographiques 100 %, balises 21/21 p + h1 ×1 + h2 ×10 + h3 ×2, guillemets «» 26/26, N.d.T. ×4) ; h1 «Leçon 15 — Les jugements de la paix dans la maladie et l'hémorragie».
- POSE : hand-set w38-pose-f3l15.py, slot vérifié VIDE au fetch-avant-pose (origin 1f372f6 = CI après Z2-51 IA-2, pas de collision fiqh-3es) ; htmlFr + titleAr/titleFr corrigés (catalogue désaligné, ci-dessus) ; registre IA-3 → fiqh-3es 17/29 posés.
- SUIVANT : fiqh-3es leçon suivante du tirage = أحكام صلح أحد الورثين أو الشريكين pp.121-128 (docId pdf-16 à réaligner ; متن خليل «وإن صالح أحد ولدين وارتيين...» pp.121-124 + المفاضى/الإعذار pp.124-126 + التحليل p.127 + إعداد p.128 → العولة) — couches pp.121-128 déjà extraites dans download/f3-l15/.

## W39 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 16 أحكام صلح أحد الورثين أو الشريكين (pdf-16 réaligné, pp.121-128) POSÉE

- MATÉRIALISATION : recycle post-W38 → tirage fiqh-3-thanawi_text.pdf re-fetché par blob (10,9 M, offset PDF/livre = 0) ; couches pp.121-140 déjà dans download/f3-l15/ ; 16 moitiés VLM pp.121-128 déjà traitées (pré-429 W38) ; microcrops 600/1200 dpi par bandes pdftoppm -x/-y/-W/-H (w39-micro.py) ; canon web UNE fois de plus ÉCHOUÉ (GitHub code/repo search 0 résultats arabes, web_search 429, shamela/al-maktaba CAPTCHA connus) — la preuve lettre = lecture directe 1200 dpi ×2 (m1/m2 pp.121-122) + couches + passes VLM pp.121-128.
- MATIÈRE : متن = **المختصر للخليل**, suite du bab الدماء, فصل الورثين/الشريك (clause وإن صالح أحد ولدين وارثين... ~10 segments : الدخول مع المصالح فيما صالح به سواء ذهابا أو فضلة أو عرضا + استثناء الطعام تردد في المدونة + يشخص ويؤذر إليه في الخروج أو الوكالة فمتنع + إن لم يكن غير المقتضى أو بكتابين وفيما لا يُكسلهما به + لا رجوع إن اختارا معا على العارض وإن هلك + صلح على عشرين من خمسينه فللآخر إسلامه أو أدخل خمسة ويرجع بخمسة وأربعين وياخذ أو يحذ الآخر خمسة + بمؤخر عن مستهلك لم يجر إلا أدراهم كقيمته أو أقل وهو مما يباح به + بشق عن موضحتين عمدا وخطأ فالشفعة بنصف قيمة الشقس وبديّة الموضحة + هل ذلك إن اختلف الجرح؟ تأويلان) + الفهم glossaire ×5 (يشخص, يؤذر, الوكالة, الشقص, الموضحة) + استخلاص ×2 + تحليل 3 axes (أولا مصالحة أحد ورثين : 2 situations الدخول + 3 situations الدفيع [السفر بنفسه/الحق المشترك بصفة واحدة أو كتابين/لكل منهما خاص معا بثمن واحد] + تفصيل الاختلاف في الجنس والصفة والقدر [الدسوقي] ; ثانيا رجوع أحد الشريكين : 2 situations [يختار ما على الغريم فلا رجوع + يخير بين الدخول والترك — مثال المائة على مدين، ورجوع بخمسة وأربعين] ; ثالثا : المستهلك بمؤخر [منع لأنه سلف جُرنفعًا + الطعام الكيل فسخ دين في دين] + الموضحتين عمد وخطأ [الشفعة نصف قيمة الشقص + دية الموضحة — المثال 20/10/50 + تأويلان عند اختلاف الجرح]) + قاعدة + القيمة (التعايش السلمي الآمن) + تقويم ×4 + استثمار ابن القاسم [التاج والإكليل للمواق 7/20] + إعداد ×3 → أحكام الحوالة.
- ARBITRAGES consignés : citation ابن القاسم p.127 reconstruite letter-majorité (VLM p127-b + couche : « من صالح عن موضحة عمد وموضحة خطأ فالشفعة بديّة الموضحة الخطأ وبنصف قيمة الشقس؛ لأنّا قسّمنا الشقس على الموضعتين وإحداهما معلومة والأخرى مجهولة » — un fragment court «على…» tronqué des DEUX lectures, consigné en N.d.T.) ; متن : «fa-aṣ-ṣāḥibu-hu l-dukhūl» (lecture directe) contre canon «fa-li-ṣāḥibi-hā l-dukhūl» consigné ; «ka-ḥaqqi la-humā fī kitābin» (print) consigné ; «al-muqtaḍā» (couche) vs «al-muftaḍā» (VLM) ; «wa-fīmā laysa la-humā yuksalu bi-hi» (lecture directe) consigné — le canon du Mukhtaṣar restant inaccessible, la transcription FR rend la lettre du tirage avec N.d.T. sur les 4 segments.
- htmlFr FR-seule 17 116 car, QA double porte PASS ×2 (0 arabe y compris N.d.T. translittérés, apostrophes typographiques, balises 27/27 p + h1 ×1 + h2 ×10 + h3 ×3, N.d.T. ×7, guillemets «» 30/30) ; h1 «Leçon 16 — Les jugements de la paix de l'un de deux héritiers ou de l'un de deux associés».
- POSE : hand-set w39-pose-f3l16.py, slot vérifié VIDE au fetch-avant-pose (origin 1afcb05) ; titleAr/titleFr RÉALIGNÉS sur le tirage («أحكام صلح أحد الورثين أو الشريكين» / «Les jugements de la paix de l'un de deux héritiers ou de l'un de deux associés» — le catalogage initial portait «من تمنع شهادتهم» = faux, suivant la chaîne du bab الدماء) ; registre IA-3 → fiqh-3es 18/29 posés.
- SUIVANT : أحكام الحوالة pp.129-136 (docId pdf-17 à réaligner — le catalogage portait من تمنع شهادتهم ; متن خليل «وحوالة مديون دينه إلى مدين آخر...» + شرح 3 axes + إعداد → أحكام المقاصات) — couches pp.129-140 déjà dans download/f3-l15/.

## W40 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 17 أحكام الحوالة (pdf-17 réaligné, pp.129-136) POSÉE

- MATÉRIALISATION : recycle post-W39 → couches pp.129-140 déjà dans download/f3-l15/ ; VLM pp.129-136 ABSENTS (429 persistant) et pages/p-129..136.png absentes → preuve lettre = couches pp.129-136 complètes + microcrops 1200 dpi ×4 par bandes pdftoppm (w40 : m1/m2 p.129 y 7800-13200, m3/m4 p.130 y 100-3400) LUES DIRECTEMENT ; canon web non retenté (3 tours d'échecs consignés W38-W39).
- MATIÈRE : متن = **المختصر للخليل**, bab الحوالة, clause des شروط (« شرط الحوالة رضى المحيل والمحال فقط وتبدو الدين لازمًا فاعلم به بعد محوله وشروط البراءة صحيحة وهل إلا فإن يفلس وتتأولان وصيغته أو يخلّو للمحال به وإن كتابة لا عليه وتساوى الديتين قدرًا وصفة وفي تحوله على الأدنى ورددوا أن لا يكون طعامًا من بيع، فقط وحلف على نفيه إن ظن به علمًا فلو أو استحق لم تنفسخ واختير خلافه والقول عليه لا في دعواه وكالته أو سلفا » — lecture directe m1-m4) + الفهم glossaire ×3 (الحوالة : نقل الدين من ذمة إلى أخرى / البراءة : السلامة من العيوب / يفلس : يحكم عليه القاضي بالفلوس) + استخلاص ×2 + تحليل 3 axes (أولا تعريف الحوالة وحكمها وأركانها : لغة + اصطلاحا الدردِر [نقل الدين من ذمة بمثله إلى أخرى وأوله الأولى] + الدسوقي شرح + الباجي [الحوالة ليست من باب الدين بالدين؛ تبرأ ذمته بنفس الإحالة فهي من باب النقد + الخيار بين يستحيل على غريمه غريمه أو يطلب غريمه — المنتقى 5/66] + أركان ×5 [محيل / محال / محال عليه / الدين المحال به / الصيغة إشارة أو كتابة] ; ثانيا شروط الحوالة : الرضا + العداوة السابقة [لا تصح حينئذ على المشهور] + ثبوت الدين لازم [يحترز عن دنصبي ويجيه بغير إذن وليه] + الذهب والورق إلا حالًا يقبضه قبل التفرق مثل الصرف + القدر والصفة [الزرقاني 6/34] + التحويل على الأدنى تردد المتأخرين [6/191] + لا يكون طعامًا من بيع ; ثالثا صحة الحوالة وعدم رجوع المحال : ليس من شروطها أن يعرف المحال عن حال المحال عليه [المحال أفقر بلا تضبط — المذهب] + إلا أن يعلم المحيل إفلاس المحال عليه فقط [غلّظها] + حلف على نفي العلم إن ظن به العلم + المصنف [القول للمحيل لا في دعواه وكالته أو مسافا + القول للقابض بيمينه إن أشبه مثله داين المحيل وإلا قول رب المال أنه وكالة أو سلف]) + قاعدة + القيمة (تأمينًا للأموال وقضاء لحاجة الإنسان — المقصد الحقوقي والجودي) + تقويم ×3 (avec la صورة أحال مدين طعامًا ثلاثة آلاف درهم على مدين له بألف) + استثمار ابن عبد البر [الكافي في فقه أهل المدينة 2/797, fragment médian tronqué de la couche, consigné] + إعداد ×2 → أحكام الضمان.
- ARBITRAGES consignés (N.d.T. ×3) : « wa-tabdū d-dayna lāziman fa-ʿlam bi-hi baʿda maḥwali-hi » (lecture directe m1) contre « wa-tabaddū… baʿda mḥawwali-hi » attendu ; « al-qawlu ʿalayhi » (lecture directe m3) contre « al-qawlu la-hu » attendu par le شرح p.134 (« القول للمُحيل », translittéré al-qawlu li-l-muḥīl) ; citation ابن عبد البر : fragment médian tronqué de la couche p.135 (« فيحيل الطالب له على الذي… » → « ولمن يكون عليه منه تبعًا »).
- htmlFr FR-seule 15 393 car, QA double porte PASS ×2 (61/61 matière, 0 arabe y compris N.d.T. translittérés [matn, šarḥ], apostrophes typographiques, balises 27/27, h1 ×1 + h2 ×10 + h3 ×3, N.d.T. ×3, guillemets «») ; h1 «Leçon 17 — Les jugements de la cession de dette».
- POSE : hand-set w40-pose-f3l17.py, slot vérifié VIDE au fetch-avant-pose (origin 94c45bb) ; titleAr/titleFr RÉALIGNÉS sur le tirage («أحكام الحوالة» / «Les jugements de la cession de dette» — le catalogage initial portait من تمنع شهادتهم = faux) ; registre IA-3 → fiqh-3es 19/29 posés.
- SUIVANT : أحكام الضمان pp.137-142 (docId pdf-18 à réaligner) — couches pp.137-140 déjà extraites ; puis المستحقة من الحول اللازم pp.143+.

## W41 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 18 أحكام الضمان (pdf-18 réaligné, pp.137-146) POSÉE

- MATÉRIALISATION : double recycle du tour (repo-417 perdu 2×, re-clone full ×2, 3,0-4,4 Go) ; tirage fiqh3.pdf (work/) survécu ; couches pdftotext pp.115-143 déjà dans download/f3-l15/, p.144-145-146 extraites au tour ; preuve lettre = microcrops 1200 dpi ×5 par bandes pdftoppm (m1/m2/m5 p.137, m3 p.138 ; m4 = frise décorative) LUES DIRECTEMENT (multimodal).
- CANON ACCESSIBLE cette fois (après les échecs consignés W38-W40) : web_search « الضمان شغل ذمّة أخرى بالحق » → šarḥ al-kabīr d'Abū al-Barakāt, vol.3 (hz.turathalanbiaa.com/public/1622.pdf, 559 p., texte en forme B Unicode → NFKC) pp.329-333 = commentaire intégral de la clause Khalīl du bab الضمان (citations متن : وصح/من أهل التبرع/أو لم يوسر/بدين لازم/أو آئل إليه/لا كتابة/داين فلانا/ولزم/فيما ثبت/وهل يقيد/بما يعامل/الرجوع/قبل المعاملة/بخلاف/احلف/وأنا ضامن/قبل المعاملة أي قبل تمامها) + shamela.ws/book/11355/240 fetché (WebFetch) = clause complète aux ellipses (كمكاتب ومأذون أذن سيدهما وزوجة / واتباع ذي الرق به إن عتق وليس للسيد جبره عليه / وعن الميت خلفه الفلس).
- MATIÈRE : متن = **المختصر للخليل**, bab الضمان (clause à 3 ellipses imprimées p.137 : الضمان شغل ذمّة أخرى بالحق، صح من أهل التبرع...ومريض بثلث الثلث...وعن المميت المفلس، والضامن والمؤجل حالا إن كان مما يعجل، وعكسه إن أيسر غريمه أو لم يوسر في الأجل، وبالموسر أو بالمُعسِر لا الجميع، بدين لازم أو آئل إليه لا كتابة بل كجعل، ودَّين فلان، ولزم فيما ثُبِّت، وهل يُقيَّد بما يعامل به ؟ تأويلان، وله الرجوع قبل المعاملة بخلاف «احلف وأنا ضامن به»، إن أمكن استيفاؤه من ضامنه، وإن جهل أو من له وبغير إذنه : كأدائه رفقًا لا عنتًا فيرد : كشرائه، وهل إن علم ببائعه وهو الأظهر ؟ تأويلان) + الفهم glossaire ×3 (2 gloses dégradées consignées) + استخلاص ×3 + تحليل 2 axes (أولا تعريف الضمان وأركانه وحكمه وأنواعه : لغة الفيومي/المصباح المنير + المازري [réf. 6/196 fragment dégradé] + الصاوي + Ṣād 23 ; اصطلاحا المصنف «شغل ذمّة بالحق» — le šarḥ : 3 types [الوجه/الهريب/التفريط] — + ابن عرفة [المختصر الفقهي 6/488] ; أركان ×5 ابن الحاجب [جامع الأمهات ص 392 تصرف] ; حكمه : جائز + الكتاب Yūsuf 72/ابن عباس + السنة hadith Abū Umāma [Sunan Abī Dāwūd, البيوع, باب ضمان العارية] + Ijmaʿ ; أنواعه ×3 : المال/الوجه [أهل الوجاهة]/الطلب) ; ثانيا أحكام الضامن والمضمون (1- الضامن : المريض au-delà du tiers يصح ولا يلزم + الورثة رد ما جاوز الثلث + الإجازة الجميع + المميت المفلس/الموسر + الحي موسرًا أو معسرًا يرجع الضامن ; ضمان الضامن تسلسل ; 2- المضمون ×8 : الموجل حالا إن كان مما يعجل [le bien tout le temps, denrée et nourriture de prêt pas de vente — canon 3/331] + وعكسه إن أيسر غريمه أو لم يوسر في الأجل [الوقت الحالي + البقرة 280] + وبالموسر أو بالمُعسِر لا الجميع [سلف جد نفعًا] + بدين لازم أو آئل إليه لا في معين [الوديعة/العارية/القرض/الشركة — القيمة en تعدٍّ/تفريط + les marchés] + بل كجعل ولو قبل الشروع [le jʿala de l'esclave fugitif — canon 3/332] + ودَّين فلان وعد بالضمان يجلب الوفاء + ولزم فيما ثُبِّت بيّنة/إقرار + وهل يُقيَّد بما يعامل به [exemple 1000/20 dirhams] + وله الرجوع قبل المعاملة أي قبل تمامها بخلاف القول لمدعى «احلف...وأنا ضامن» [canon 3/333] + وأن استيفاؤه من ضامنه [المعينات والحدود والتعازير والقتل والجراح] + وإن جهل...كأدائه رفقًا لا عنتًا فيرد كشرائه + وهل إن علم ببائعه وهو الأظهر عند ابن يونس]) + القيمة + تقويم ×3 + استثمار ابن رشد [المقدمات الممهدات 2/873] + المازري [6/2] + مهام (أتأمل النصين ×2) + إعداد ×1 → أحكام ضمان الغائب (pp.146-147).
- ARBITRAGES consignés : 3 ellipses imprimées p.137 (canon : كمكاتب ومأذون أذن سيدهما وزوجة / واتباع ذي الرق به إن عتق وليس للسيد جبره عليه) ; « المميت المفلس » (tirage ×3 couches + m2/m5) contre « الميت خلفه الفلس » (canon shamela 11355/240) — la leçon du tirage tenue ; « إن أيسرَ غريمه » (canon + couche) contre « يُسَرَّ/يُبسَرَ » lectures crops ; « آئلٍ إليه » (canon بهمزتين « كبائع وبائس », Šarḥ 3/332) contre couches « آيِل له/آجل » ; « بخلاف «احلف وأنا ضامن به» » canon contre couches « إحلافه/القحلف » ; « كأدائِهِ رِفْقًا لا عَنْتًا فيرَدَّ : كشِرائِهِ » (canon shamela + couche p.144) contre « قال عبد النافع كشرائه » couche p.138 (bruit) ; couche p.138 L1 RTL bruitée remplacée par canon + m3.
- htmlFr FR-seule 19 003 car, QA double porte PASS ×2 (balises 43/43, h1 ×1 + h2 ×10 + h3 ×2, guillemets 42/42, 0 arabe, N.d.T. ×3 + 3 glossaires, 0 placeholder/résidu) ; h1 « Leçon 18 — Les jugements de la garantie ».
- POSE : hand-set w41-pose-f3l18.py, slot vérifié VIDE au fetch-avant-pose (origin 48e331a7) ; titleAr/titleFr RÉALIGNÉS sur le tirage (« أحكام الضمان » / « Les jugements de la garantie » — le catalogage initial portait أحكام الوكالة والصلح والاستح = faux) ; registre IA-3 → fiqh-3es 20/29 posés.
- SUIVANT : أحكام ضمان الغائب pp.146+ (docId pdf-19 à réaligner — le catalogage initial portait مسائل من المنازعات في العقار = faux ; objectifs p.147 « تعرف أحكام ضمان الغائب / إدراك ما يرجع به الضامن إذا غرم / تمثل مكانة الضمان ومسؤوليته في المعاملات ») — couches p.147+ non extraites au tour.

## W42 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 19 أحكام ضمان الغائب (pdf-19 réaligné, pp.147-152) POSÉE

- ENVIRONNEMENT survivant au recycle (repo-417 + fiqh3.pdf intacts) ; registre à jour (origin 8adb2a8e, IA-2 rien de nouveau) ; slot pdf-19 vérifié VIDE avant pose.
- BORNES RÉELLES : L19 أحكام ضمان الغائب = pp.147-152 (6 pages) ; le متن du tirage s'arrête à « والقول له في ملائه » (vérifié microcrop m4 p.148) — le canon continue par des segments hors tirage (وافاد شرط أخذ أيهما شاء... / أو إن مات كشرط ذي الوجه... / التصديق في الإحضار / وله طلب المستحق بتخليصه), consignés hors leçon. L20 = **الاشتراك في الضمان ومبطلاتُهُ** (p.153, objectifs : تعرف مايفيد من الشروط في الضمان وما لايفيد / تعرف مبطلات الضمان / تمثل أحكام الاشتراك في معاملات) — docId pdf-20 À RÉALIGNER.
- MATÉRIALISATION : couches pdftotext pp.147-156 standard + microcrops 1200 dpi ×11 (m1/m4 p.148 متن fin + الفهم, m2/m5/m6/m7/m9/m10 p.150 شرح لا عكسه + ثانيا تعجيل, m3/tail p.151 تقويم ×3, m8 p.151 مطالبة صاحب الدين, m11 p.147 questions ×3) LUES DIRECTEMENT (multimodal).
- **CANON RÉCUPÉRÉ CETTE FOIS : l'édition المختصر للخليل d'al-Mawāq** (hz.turathalanbiaa.com/public/1639.pdf, 340 p., forme B Unicode → NFKC en python — même site que le Šarḥ al-Kabīr 1622) — la lettre du متن L19 correspond canon lettre à lettre (« لا إن ادعى عليه غائب فضمّن ثم أنكر، أو قال لمدع على منكر إن لم آتك به لغد فأنا ضامن ولم يأت به / إن لم يثبت حقه بيّنة وهل بإقراره تأويلان كقول المدعي عليه أجلني اليوم فإن لم أوفك غدا فالذي تدعيه علي حق / ورجع بما أدى ولو مقوّما إن ثبت الدفع / وجاز صلحه عنه بما جاز للغريم على الأصح / ورجع بالأقل منه أو قيمة / وإن برئ الأصل برئ لا عكسه / وعجل بموت الضامن ورجع وارثه بعد أجله أو الغريم إن تركه ولا يطالب إن حضر الغريم موسرا / والقول له في ملائه ») — shamela 11355/240 et islamweb bloqués (curl 5 Ko sans contenu / CAPTCHA), ablibrary 18484 = le Kharšī (bab témoignage à cette page).
- MATIÈRE : متن = suite clause Khalīl bab الضمان (le fragment du غائب+المنكر : la garantie du réclamé absent qui nie à son retour ne charge plus le garanteur ; l'option du créancier حاضر ou absent ; « إن لم آتك به لغد فأنا ضامن » au niant ; بيّنة vs إقرار تأويلان ; كقول المدعي عليه أجلني اليوم ; ورجع بما أدى ولو مقوّما إن ثبت الدفع ; وجاز صلحه عنه بما جاز للغريم على الأصح ; ورجع بالأقل منه أو قيمته ; برئ الأصل برئ لا عكسه ; عجل بموت الضامن ; ورجع وارثه بعد أجله أو الغريم إن تركه ; ولا يطالب إن حضر الغريم موسرا ; والقول له في ملائه) + الفهم glossaire ×3 (مقوَّم glose à moitié lisible consignée / الأصل=المدِّين / ملائه=قدرته على التسديد) + استخلاص ×3 + تحليل 2 axes (أولا ضمان الغائب ورجوع الضامن : 1- ضمان الغائب والمنكر [فلا يلزم الضامن شيء لثبوت الضمان + وإذا بطل الأصل بطل الفرع كما هو مقرر عند الفقهاء + وقول المصنف وهل بإقراره راجع للمسألة الثانية فقط + التهمة التواطؤ] ; 2- الرجوع بما أدى ولو مقوّما [كالمسلف مثليا كعين وطعام أو مقوّما + بيّنة أو إقرار صاحب الحق + وجاز صلحه + ورجع بالأقل منه أو قيمته = بأقل الأمرين + برئ الأصل برئ = طلبه فرع ثبوت الدَّين + لا عكسه = كبراءة الضامن بانقضاء مدة ضمانه/وهب رب الدين دينه للضامن كما قال الدردير + fragment dégradé راجع للصورتين فإن مات المدَّين ولم يترك الأجل]) ; ثانيا أحكام تعجيل الدين المضمون (1- بماذا يعجّل الدين المؤجّل [أولهما موت الضامن + détail dégradé consigné] ; 2- مطالبة صاحب الدين للضامن [صورتين : حضر الغريم موسرا / غاب الغريم ولم يعد إثباته — على الطالب أن يُيسَّر الطلب والاستيفاء بلا مشقة شديدة عرفا] ; 3- أحكام التنازع بين رب الدين والضامن [القول له في ملائه : ادعى رب الدين المدين معدم / ادعى الضامن مليء التكسيب فليس لرب الدين مطالبة الضامن لتصديقه في دعوى غنى المدين ولا مطالبة المدين لأنه أقر بعدمه إلا أن يقيم بيّنة بالعدم أو يتجدد مال فله مطالبته وهذا ظاهر]) + القيمة (الاحتياط والاحتراز في أموال الناس أمر معتبر — وسيلة حفظ الحقوق من التلاعب والعبث — قِوام الحياة) + تقويم ×3 + استثمار الماوردّي [réf. fragmentée 9/48 المدونة consignée] + مهام ×2 (أقارن النص بكلام المصنف / أبين مَّن السائل والمجيب) + إعداد ×1 (أقرأ متن الدرس القادم).
- ARBITRAGES consignés : le fragment « وهل بإقراره » (tirage « 0 ايوم » dégradé) rendu par canon ; « إن تركه » tirage vs canon ✓ identique ; le canon post-« ملائه » hors tirage consigné hors leçon ; l'استثمار الماوردّي référence fragmentée [9/48 المدونة] consignée ; les fragments p.150 fin (بعضًا فهو راجع للصورتين فإن مات المدَّين ولم يترك الأجل... و لكن لا يعدل) et le détail du sous-item 1 (تعجيل الدين المؤجّل) dégradés consignés.
- htmlFr FR-seule 12 809 car, QA double porte PASS ×2 (balises h1+h2 ×10+p/ul/ol/li/strong/em équilibrées, guillemets équilibrés, 0 placeholder, couverture complète 20/20 mots-clés) ; h1 « Leçon 19 — Les jugements de la garantie de l'absent ».
- POSE : hand-set w42-pose-f3l19.py, slot vérifié VIDE (origin 8adb2a8e) ; titleAr/titleFr RÉALIGNÉS sur le tirage (« أحكام ضمان الغائب » / « Les jugements de la garantie de l'absent » — le catalogage initial portait مسائل من المنازعات في العقار وما يتصل به = faux) ; registre IA-3 → fiqh-3es 21/29 posés.
- SUIVANT : **الاشتراك في الضمان ومبطلاتُهُ** pp.153+ (docId pdf-20 à réaligner — le catalogage initial à vérifier) ; متن probable = la clause « ولا(? ) إن(? ) عيَّن(? ) [؟]... » suite (le canon al-Mawāq 1639.pdf continue après « ملائه ») ; couches p.153-156 extraites au tour (la fin de L19 = p.152 ; p.153-156 = début L20 à purifier).

## W43 — 2026-11-22 — IA-3 — traduction fiqh-3es leçon 20 الاشتراط في الضمان ومِبَطَلاته (pdf-20 réaligné, pp.153-160) POSÉE

- ENVIRONNEMENT : RECYCLE DUR en cours de séance — repo-417 vidé (clone perdu) MAIS tout restauré par re-clone du remote (74b89536, fiqh-3es.json 21/29 avec pdf-19 posé ✓, worklog, pages) ; les artefacts locaux survivent (work/fiqh3.pdf, download/f3-l15 couches + canon-daman/mkhl.pdf + REPRISE-W42). Registre à jour (origin = HEAD, IA-2 rien de nouveau).
- BORNES RÉELLES : L20 الاشتراط في الضمان ومِبَطَلاته = pp.153-160 (8 pages) ; médaillon manuel N°19 ; **TITRE TRANCHÉ AU ZOOM 2400 dpi** : « الاشتراط » (ط net — le catalogage initial أحكام الحوالة والقسمة = FAUX, réaligné) ; متن du tirage s'arrête à « كقرضهما على الأصح » (le canon continue par « وإن تعدد حمالته أتبع كل بحصته إلا أن يشترط حمالة بعضهم عن بعض كترتبهم... » + la clause du رجوع, consignés hors leçon — pour L21). La fin du الإعداد L20 annonce la suite : تعدد الحملاء + القسمة في الحمالة ✓.
- MATÉRIALISATION : microcrops 1200-2400 dpi ×11 (n1/n3/n4/n7 p.153 titre+تمهيد+questions+متن début, n2 p.154 متن fin+الفهم, n5/n6 p.153 questions ×2+متن début « وأفاد شرط أخذ أيهما شاء », n8/n9/n10/n11 p.154 glossaire+استخلاص ×3+محور 1) — le W42 avait FAUX classé « وأفاد شرط أخذ أيهما شاء... التصديق في الإحضار... بتخليصه » hors tirage : c'est le début du متن L20 ✓ (corrigé).
- CANON : al-Mawāq 1639.pdf (mkhl-norm.txt) — la lettre du متن L20 correspond canon lettre à lettre (« وأفاد شرط أخذ أيهما شاء وتقديمه أو إن مات كشرط ذي الوجه أو رب الدين التصديق في الاحضار وله طلب المستحق بتخليصه / عند أجله لا بتسليم المال إليه / وضمنه إن اقتضاه لا أرسل به / ولزمه تأخير ربه المعسر أو الموسر إن سكت أو لم يعلم إن حلف أنه لم يؤخره مسقطا وإن أنكر حلف أنه لم يسقط ولزمه وتأخر غريمه بتأخيره إلا أن يحلف / وبطل إن فسد متحمل به أو فسدت كبجعل من غير ربه لمدينه وإن ضمان مضمونه إلا في اشتراء شيء بينهما أو بيعه كقرضهما على الأصح »). Variante tirage « إلا أن يخلف » (1200 dpi) rendue par canon « إلا أن يحلف » (consignée).
- MATIÈRE : متن = suite clause Khalīl bab الضمان (l'اشتراط : أخذ أيهما شاء + تقديم الحمِيل + أو إن مات كشرط ذي الوجه أو رب الدين + التصديق في الإحضار + طلب المستحق بتخليصه عند أجله لا بتسليم المال إليه + وضمنه إن اقتضاه لا أرسل به + ولزمه تأخير ربه المعسر أو الموسر إن سكت أو لم يعلم + إن حلف... وإن أنكر... + وتأخر غريمه بتأخيره إلا أن يحلف ; les invalidants : وبطل إن فسد متحمل به أو فسدت كبجعل من غير ربه لمدينه + وإن ضمان مضمونه إلا في اشتراء شيء بينهما أو بيعه كقرضهما على الأصح) + الفهم glossaire (المستحق = رب الدين ✓ / قرضهما = القرض : ما تعطيه غيرك من المال لتقضاه ✓ / une glose dégradée consignée) + استخلاص ×3 (أستخلص متى يفيد الاشتراط من رب الحق والضامن / أحكام الضامن / مِبَطَلات الضمان ✓ crop n9) + تحليل (أولا ما يفيد من الشروط في الضمان ✓ crop n11 : 1- اشتراط رب الدين [التصديق في الإحضار يفيد رب الدين اشتراط الأخذ من المدين أو الحمِيل شاء + الفائدة للحمِيل + خلاف الشرط المتقدم ولا يطالب إن حضر الغريم موسرا — وهنا يطالب مطلقا ثم إن اختار الأخذ من الحمِيل سقطت مطالبته للمدين + اشتراط تقديم الحمِيل على خلاف الأصل سواء اشترط براءة المدين أم لاء + إن اختار مع عدم البراءة تقديمه فليس له مطالبة المدين إلا عند التعذر] ; 2- اشتراط الضامن [أو إن مات كشرط ذي الوجه... إذا اشترط الضامن أن يُؤخذ منه الحق إلا إن مات المضمون معدمًا + أقوال إن جحد أو إن [؟]عمل بشرطه + وشبَّه المصنف : كشرط ذي الوجه أو رب الدين التصديق في الإحضار إذا اشترط رب الدين [؟]أمنه صدق في إحضار المضمون بلا يمين أو بيمين فيعمل بشرطه + المدين أو تخلصني من الضمان + للضامن طلب المضمون بدفع ما عليه عند أجله وإن لم يُطالَب رب الدين + مفهوم «عند أجله» ليس له قبل حلول الأجل] ; 3- [التأخير, titre dégradé consigné] : [الوجه الأول إذا أخر رب الدين المدين المعسر وأمهله مدة أخرى فيلزم الضامن إذ التأخير رفق بالحمِيل + وهذا إن كان المدين معسرا فإن كان موسرا] ; الوجه الثاني : أن لا يُخيَّر رب الدين حتى يحل الأجل الثاني وقد أعسر الغريم فالضمان لازم للحمِيل إن حلف رب الدين حينئذ أنه لم يؤخره مَقطَعًا + إذا نكل سقط الضمان ; الوجه الثالث : أن يعلم الضامن بتأخير رب الدين للغريم ولا يرضى به ويقول تأخيرك للمدين إبراء لي من الضمان فإنه يحلف أنه لم يقصد بتأخير المدين إسقاط الضمان ويلزم الضامن الضمان ويسقط التأخير عن الضامن فيؤخذ منه الحق عاجلا ويرجع به عند حلول أجل التأخير على المدين + فإن نكل سقط + وإلى هذا الوجه أشار المصنف بقوله «ولزمه» + [ولم تكلم المصنف على تأخير المدين تكلم على تأخير الحمِيل فقال وتأخَّر غريمه + فليس للدائن طلب الغريم إلا بعد حلول أجل التأخير إلا أن يحلف أنه لم يقصد بتأخير الحمِيل تأخير الغريم فله طلب الغريم وإن نكل لزمه تأخير الغريم أيضًا]) ; ثالثا مبطلات الضمان (1- فساد المتحمل به : إذا كان الدين المتحمل به فاسدًا بضمانه فلا يلزم الضامن شيء كما لو كان ربا مثل أن يقول شخص لآخر ادفع لهذا ألف درهم في ألفين [fragment dégradé] ; 2- فساد الحمالة بسبب جعل للضامن : إذا فسدت الحمالة [بفسادها شرعًا] بقوله كبجعل من غير ربه لمدينه أي بأن يكون الجُعل من رب الدين أو من المدِّين أو من أجنبي للضامن وعلم رب الدين به أو لم يعلم ولم يردده الحمِيل حتى علم ربه به فلا يجوز لأنه إذا غرم رجع بما غرمه مع زيادة الجعل وذلك لا يجوز لِأ... ولأن الضمان أحد الثلاثة التي [؟]تكون إلا لله — ثانيها القرض وثالثها الجاه [fragment dégradé consigné] + فإن رد الحمِيل الجعل للأجنبي قبل علم رب الدين به لم تفسد عند ابن القاسم وغيره + وبالغ المصنف على بطلان الضمان بالجعل فقال وإن ضمان مضمونه إلا في اشتراء شيء بينهما أو بيعه كقرضهما على الأصح أي وإن كان الجعل الواصل للضامن ضمانًا مضمون الضامن وذلك كأن يتداين رجلان دينًا من رجل أو رجلين ويضمن كل منهما صاحبه فيما عليه لرب الدين فيمنع — وهذا إذا دخلا على ذلك بالشرط — إلا في اشتراء شيء معين بينهما شركة ويضمن كل منهما الآخر في قدر ما ضمنه فيه فإنه جائز — أو بيع شيء معين بينهما كما لو [؟]شخص في شيء وتضامنا فيه كقرضهما أي تسلفهما نقدا أو عرضا أو غير ذلك بينهما على أن كل واحد حَمِيل لصاحبه فيجوز على الأصح عند ابن عبد السلام]) + القيمة (يتبيَّن من خلال هذا الدرس أن الشريعة السمحة تقصد المحافظة على حقوق الآخرين وصيانتها من الضياع والتلف أو السطو والعدوان عليها بما تضع من قيود وشروط وضوابط [fragment dégradé] مما يؤكد أهمية فقه الأموال) + تقويم ×3 (أبين ما يفيد الاشتراط من رب الحق والضامن / أذكر أحكام الضامن / item 3 dégradé consigné — porte sur les invalidants) + استثمار [حاشية الدسوقي 3/933 ✓ référence lisible : أقسام [fragment] الإرسال / يتنازع المدين والضامن في أنه على وجه الاقتضاء أو الإرسال أو [؟]لمن الأولى الضامن ويُغار القبض عن القَرينَين الدائنتين على الاقتضاء أو الإرسال أو الوكالة فقول [fragment] فلا [؟]قول المدِّين وكذا [؟]إذا انبهم الأمر لعدم القرينة وقوله «لا أرسل به» [؟]أحقاقة المدِّين وقوله «وضمنه» أي [؟]لمن قبضه + «إن اقتضاه» ومعلوم أن غريم الغريم غريم فيعزم الأصيل [فله أن يعزم] [؟]لحات المُدونة وغيره + [؟]الضامن نيابة عن المدِّين كما صرَّح بذلك الرَّافِعي [fragment] + ويُفهم من التوضيح أن رب الدين إذا رجع على الأصيل كالنأصيل الرجوع على الكفيل — حاشية الدسوقي 3/933] + مهام ×3 (أستخرج صور قبض الضامن للدين / أبين متى يكون الضامن غريمًا / أوضح معنى قول الفقهاء غريم الغريم غريم ✓) + إعداد ×2 (أبحث عن باقي أحكام الضمان / أبحث عن ما يترتب على تعدد الحملاء وعن كيفية القسمة في الحمالة ✓).
- ARBITRAGES consignés : le متن tirage s'arrête à « كقرضهما على الأصح » (le canon post-أصح hors tirage consigné) ; « ضمنه » pronom ه = le débiteur d'après le شرح « فهو متعد في قبضه » (corrigé dans le htmlFr — « son harm » éliminé) ; « ربه » = le créancier (le شرح إذا أخر رب الدين المدين المعسر) ; les fragments dégradés consignés : la glose [؟] du glossaire, le détail de l'اشتراط du ضaman, le « أقوال إن جحد », le fragment « ضار مة م », l'item 3 du تقويم, les passages de l'استثمار, « الضمان أحد الثلاثة التي [؟]تكون إلا لله — ثانيها القرض وثالثها الجاه ».
- htmlFr FR-seule 15 674 car, QA double porte PASS ×2 (balises h1+h2 ×10+p/ul/ol/li/strong/em équilibrées, guillemets équilibrés, 0 placeholder, couverture 20/20 mots-clés, « son harm » corrigé) ; h1 « Leçon 20 — Le conditionnement dans la garantie et ses invalidants ».
- POSE : hand-set w43-pose-f3l20.py, slot vérifié VIDE (origin = HEAD) ; titleAr/titleFr RÉALIGNÉS sur le tirage (« الاشتراط في الضمان ومِبَطَلاته » / « Le conditionnement dans la garantie et ses invalidants » — le catalogage initial أحكام الحوالة والقسمة = faux) ; registre IA-3 → fiqh-3es 22/29 posés ; trace e13d18fe0d18e021-w43.
- SUIVANT : **L21 أحكام الحمالة متعددة وقسمتها (?) pp.161+ (docId pdf-21)** — le متن probable = « وإن تعدد حمالته أتبع كل بحصته إلا أن يشترط حمالة بعضهم عن بعض كترتبهم... » (le canon al-Mawāq continue après « كقرضهما على الأصح ») + la clause du رجوع « ورجع به... » ; l'الإعداد L20 annonce exactement ces deux recherches ✓.

- POUSSÉE EFFECTUÉE (W43, complément) : le token GitHub fourni par l''utilisateur a permis le push 74b8953..fc57840 main (les 2 commits W43 : pose pdf-20 + pages rendues) ; la CI de rendu synchrone est déclenchée ; vérification page en ligne à suivre. Le fichier de token a été purgé immédiatement après le push.

## W44 — 2026-11-23 — IA-3 — traduction fiqh-3es leçon 21 أحكام تعدد الحملاء (pdf-21 réaligné, pp.161-166) POSÉE

- ENVIRONNEMENT : re-clone minhaj après recycle (repo-417 vidé) — origin/main = b4468ba ([ci] rendu synchrone après le push W43) ; registre à jour (pdf-18 posé ✓ 19 003 car — le reliquat W41 de la todo était obsolète ; pdf-19/pdf-20 posés ✓) ; IA-2 rien de nouveau.
- BORNES RÉELLES : L21 أحكام تعدد الحملاء = pp.161-166 (6 pages, médaillon manuel N°20) ; **TITRE TRANCHÉ AU CROP 1200 dpi ×2** : « أحكام تَعَدُّدِ الحَمَلاءِ » (le catalogage initial أحكام الوصية والحيازة = FAUX, réaligné) ; متن du tirage = le canon « وإن تعدد حمالته أتبع كل بحصته إلا أن يشترط حمالة بعضهم عن بعض كترتبهم ورجع المؤدي بغير المؤدى عن نفسه بكل ما على الملقي ثم ساواه فإن اشترى ستة بمائة بالحمالة فلقي أحدهم أخذ منه الجميع ثم إن لقي أحدهم أخذه بمائة ثم بمائتين فإن لقي أحدهما ثالثا أخذه بخمسين وبخمسة وسبعين فإن لقي الثالث رابعا أخذه بخمسة وعشرين وبمثلها ثم باثني عشر ونصف وبستة وربع وهل لا يرجع بما يخصه أيضا إذا كان الحق على غيرهم أولا وعليه الأكثر تأويلان » (le tirage s'arrête à « تأويلان » — le canon post-تأويلان « وصح بالوجه وللزوج رده من زوجته... » = HORS tirage = le متن de L22 ✓ vérifié p.167).
- MATÉRIALISATION : microcrops 1200 dpi ×2 (n12/n13 p.161 titre + médaillon « 20 ») + couches p.161-167 extraites.
- CANON : al-Mawāq 1639.pdf (mkhl-norm.txt, pos وصح بالوجه @208057) — la lettre du متن L21 correspond canon lettre à lettre ✓ ; le bab suivant dans le canon = « باب الشركة » (pour les leçons ultérieures du livre).
- MATIÈRE : متن (la pluralité des porteurs : أتبع كل بحصته / إلا أن يشترط حمالة بعضهم عن بعض كترتبهم / ورجع المؤدي بغير المؤدى عن نفسه بكل ما على الملقي ثم ساواه / l'exemple des six pour six cents / وهل لا يرجع بما يخصه أيضا... تأويلان) + الفهم glossaire ×2 (حمَلاء : جمع حميل وهو الضامن الكفيل ✓ / بحصته : نصيبه وسهمه ✓) + استخلاص ×3 (أحدد أحكام تعدد الحُملاء / أستخرج حكم رجوع الغارم [؟] / أستخلص متى يرجع الحمِيل بما يخصه ومتى لا) + تحليل (أولا تعدد الحملاء : 1- [غير الغرماء] إذا تعددوا في آن واحد اتبع رب الدين كل واحد بحصته فقط بقسمه على عددهم وليس بعضهم حميلا عن بعض فلا يؤخذ مليء عن معدم ولا حاضر عن غائب + كأن يقول كل واحد ضمانه علينا ويوافقه أصحابه أو أتضمنون زيدا فيقول كل واحد نعم أو يتنطق الجميع دفعة واحدة ; 2- تعدد الحملاء الغرماء : [citation dégradée] إلا أن يشترط رب الدين في عقد الحمالة حمالة بعضهم عن بعض فيتبع كل واحد بالجميع مع حضور غيره مليئا وأولى إن غاب أو مات + إن قال أيكم شئت أخذت بحقي وإلا أتبع البعض بالجميع + [فليعلم الموت أو الغيبة فقط — fragment dégradé]) ; ثانيا رجوع بعض الحملاء الغرماء على غيره من الحملاء (ورجع المؤدي... ثم ساواه + فإن المؤدي يرجع على من لقاه بما عليه خاصة ولا يأخذ منه ما أداه عن نفسه + بدليل تمثيله + شرط حمالة بعضهم عن بعض على أحد التأويلين وسواء في القسمين + مثال حملاء غرماء : ثلاثة أنفار سلعة بثلاثمائة على كل واحد مائة وكل حميل عن بعض فإذا لقي البائع أحدهم أخذ منه الجميع مائة عن نفسه ومائتين عن صاحبه فإذا وجد الغارم أحدهما أخذه بمائة وبخمسين نصف ما على الثالث + مثال حملاء غير غرماء : رجل سلعة بثلاثمائة وضمنه ثلاثة رجال وشرط البائع حمالة بعضهم عن بعض فإذا حل الأجل ووجد واحدا أخذ منه الثلاثمائة وإذا وجد الغارم واحدا من صاحبيه رجع عليه بمائة وخمسين وإذا لقي أحدهما الثالث رجع عليه بخمسين على أحد التأويلين + أوضح ذلك المصنف بمثال المدونة الذي أفرده... إن اشترى ستة بستمائة بالحمالة [fragment dégradé]) ; ثالثا رجوع بعض الحملاء غير الغرماء (وهل لا يرجع بما حصه أيضا إذا كان الحق على غيرهم أولا وعليه الأكثر تأويلان + تقديره : أو يرجع الغارم على من لقيه من أصحابه بنصف ما غرمه أم مطلقا لافرق بين ما غرمه عن نفسه أو غرمه عن أصحابه تأويلان فلو تحمل ثلاثة عن شخص بثلاثمائة وغرم أحدهم جميعها ثم لقي آخر فعلى الأول يقاسمه فيمائتين على كل مائة + الأول على الثالث بمائة وعلى الثاني + أنا أدَّيت ثلثمائة أنت حميل معي بها ثم على الثاني يرجع كل على الثالث بخمسين + وفائدة الخلاف لوقبض رب الدين من أحدهم مائة لكونه لم يجد معه غيرها ثم وجد هذا أحد الكفلاء هل يرجع عليه بنصف المائة أو لا يرجع عليه بشء منها؟) + القيمة (من خلال هذا الدرس يتبين أن الشرع الحكيم يروم الضبط في الأمور وخصوصا فيما يتعلق بحقوق الآدميين كما يربي أتباعه على الوفاء بالعهود والالتزام بالعقود ويرسخ فيهم احترامها وتقدير خطورتها وهذا يحقق المقصد الحقوقي) + تقويم ×2 (أُحدد من المتن أحكام تعدد الحملاء إذا تعددوا / أوضح متى يرجع الحملاء ومتى لا يرجعون) + استثمار [Ibn Rushd ✓ : فإن تحمل بالمال حملاء في صفقة واحدة فيلزم كل واحد منهم ما ينوبه منه على عددهم إلا أن يشترط أن كل واحد منهم حميل عن صاحبه أو عن أصحابه قال بجميع المال أي ولا... بعدم الغريم ويأخذ أيهم شاء على أحد قولي مالك وعلى كليهما إذ اشترط أن يأخذ أيهم شاء فإن أخذ أحدهم بما ينوبه من المال فاختلف هل للمأخوذ منه ذلك أن يرجع على... ووجد من أصحابه حتى يساويه في ذلك فقيل إن ذلك [؟] لى هذا ذهب أبو إسحاق [التونسي] وقيل إن ذلك ليس له وهو الصواب لأن ما ينوبه من المال فإنما أداه عن نفسه لا رجوع له به كما لو ثبت عليه من أصل دين — référence imprimée dégradée « ...2/183-283 », le titre de l'ouvrage cité n'est pas lisible dans le tirage] + مهام ×2 (أستخرج من النص [؟]ما تعدد الحملاء وأقارن ذلك بكلام المصنف / أستخرج من النص متى لا يرجع بعض الحملاء على غيره) + إعداد (أقرأ متن الدرس الآتي [fragment dégradé] : 1- ما أنواع الضمان؟ وما حكم كل نوع منها؟ / items 2-3 dégradés consignés).
- ARBITRAGES consignés : le متن tirage s'arrête à « تأويلان » (le canon post-تأويلان = متن L22 ✓ p.167 أنواع الضمان وأحكامها) ; le titre du 1er sous-item du 1er محور dégradé (reconstruit « la pluralité des porteurs non-guarantees » d'après le شرح إذا تعدد الحملاء غير [الغرماء] في آن واحد) ; la référence de l'استثمار dégradée (« الملقدامتهدات 2/183-283 » — Ibn Rushd cité, titre illisible) ; les items 2-3 de l'إعداد dégradés ; « ثم يساويه فيغرم مادفعه عن غيره » fragment dégradé (reconstruit « il l'égalise dans ce qu'il a payé pour un autre » d'après le متن ثم ساواه) ; le fragment « ثم كل من وجد الآخر أخذه [؟]تكمسين » dégradé.
- htmlFr FR-seule 12 684 car, QA double porte PASS ×2 (balises h1+h2 ×10+h3 ×3+p/ul/ol/li/strong/em équilibrées, guillemets 28/28 — 1 fermant de citation Ibn Rushd manquant CORRIGÉ, 0 placeholder, couverture 22/22 mots-clés) ; h1 « Leçon 21 — Les jugements de la pluralité des porteurs ».
- POSE : hand-set w44-pose-f3l21.py, slot vérifié VIDE (origin = HEAD) ; titleAr/titleFr RÉALIGNÉS sur le tirage (« أحكام تعدد الحملاء » / « Les jugements de la pluralité des porteurs » — le catalogage initial أحكام الوصية والحيازة = faux) ; registre IA-3 → fiqh-3es 23/29 posés ; trace a0dc594079faa7d6-w44.
- SUIVANT : **L22 أنواع الضمان وأحكامها pp.167+ (docId pdf-22)** — le متن L22 = le canon « وصح بالوجه وللزوج رده من زوجته وبرئ بتسليمه له وإن بسجن أو بتسليمه نفسه إن أمره به إن حل الحق وبغير مجلس الحكم إن لم يشترط وبغير بلده إن كان به حاكم ولو عديما وإلا أغرم بعد خفيف تلوم إن قربت غيبة غريمه... » ✓ (vérifié p.167 : objectifs ×3 ضمان الوجه + إدراك أحكام الضامن والمضمون + تمثل خطورة الضمان).

## W45 — 2026-11-23 — IA-3 — traduction fiqh-3es leçon 22 أنواع الضمان وأحكامها (pdf-22 réaligné, pp.167-173) POSÉE

- ENVIRONNEMENT : pas de recyclage (repo-417, fiqh3.pdf, canon OK) ; ff origin 259b6d08 ([ci] après IA-2 Z2-54 hadith-6ep) — 2788 fichiers de site régénérés localement au W44 non commités DISCARDÉS (la CI d'origin fait foi) ; registre : pdf-22 slot vide, titleAr catalogué « جملة من الفرائض والآداب » = FAUX (réaligné).
- BORNES : L22 أنواع الضمان وأحكامها = pp.167-172 (médaillon manuel N°21) + الإعداد p.173 ; p.173 = début L23 الشركة ; متن du tirage = le canon « وصح بالوجه وللزوج رده من زوجته وبرئ بتسليمه له وإن بسجن أو بتسليمه نفسه إن أمره به إن حل الحق وبغير مجلس الحكم إن لم يشترط وبغير بلده إن كان به حاكم ولو عديما وإلا أغرم بعد خفيف تلوم إن قربت غيبة غريمه كاليوم ولا يسقط الغرم بإحضاره إن حكم به لا إن أثبت عدمه أو موته في غيبته ولو بغير بلده ورجع به وبالطلب وإن في قصاص كأن حميل بطلبه أو اشترط نفي المال أو قال لا أضمن إلا وجهه وطلبه بما يقوى عليه وحلف ما قصر وغرم إن فرط أو هربه وعوقب وحمل في مطلق: أنا حميل وزعيم وأذين وقبيل وعندي وإلي وشبهه على المال على الأرجح والأظهر لا إن اختلفا ولم يجب وكيل للخصومة ولا كفيل بالوجه بالدعوى إلا بشاهد وإن ادعى بينة [ب]كالسوق أوقفه القاضي عنده » = la FIN du bab الضمان dans le canon (pos وصح بالوجه @208057 → أوقفه القاضي عنده @2087xx) ; le canon enchaîne sur « باب الشركة » = متن L23 ✓ ; le fragment canon « وإن ادعى بينة بكالسوق » rendu « بالسوق » (support ad-Dasūqī « حاضرة بالسوق »), variante consignée.
- MATIÈRE : الفهم glossaire ×6 (الوجه: الذات فهو مجاز مرسل بإطلاق البعض وإرادة الكل / عديما: لا مال له / الطلب: التفتيش والبحث / زعيم: من الزعامة وهي السيادة لغة / أذين: من الإذن وهو الإعلام أو من الإذانة بمعنى الإيجاب / قبيل: من القبالة وهي الحفظ ولذا سمي الصك قبالا لأنه يحفظ الحق) + استخلاص ×3 (أستخلص أنواع الضمان / أبين حكم كل نوع / أوضح أحكام تنازع الضامن والمضمون) + تحليل 3 axes : أولا ضمان الوجه (1- تعريفه: التزام الضامن الإتيان بالغريم الذي عليه الدين وقت الحاجة إليه / 2- حكمه: يصح فقط حيث كان على المضمون دين لا في قصاص ونحوه كحد وتعزير ولذا حذفه المصنف هنا وذكره في ضمان الطلب / 3- ضمان الزوجة بالوجه: للزوج رده من زوجته ولو كان الدين لا يبلغ ثلثه؛ لأنه يقول قد تحبس إذا عاجزت أن تعتني بالمدين أو تخرج للخصومة وذلك معرة علي، ومثل ضمانها للوجه ضمان الطلب فللزوج رده وأما ضمانها للمال فقد مر / 4- براءة الضامن بالوجه: بتسليمه للمضمون له في مكان يقدر رب الدين على خلاصه أو بغير مجلس الحكم إن لم يشترط أو إن أمره الضامن بالتسليم أو بغير بلد الضمان إن كان به حاكم) ; ثانيا ضمان الطلب (1- تعريفه [dégradé, sens canonique: réclamation de l'adversaire sans salaire] / 2- حكمه: يصح وإن في قصاص ونحوه من الحقوق البدنية من حدود وتعزيرات / 3- صيغته: كأن حميل بطلبه + أو اشترط نفي المال [fragments dégradés consignés]) ; ثالثا غرم ضامن الوجه (يغرم إن فرط تفريطا خاصا بأن وجده وتركه بحيث لم يتمكن رب الدين من أخذه منه + وعوقب من غير غرم في نوع آخر مغاير [fragments dégradés consignés]) + اختلاف الضامن والطالب (قال الدسوقي: هذا مخرج من مقدر أي ولزم ذلك أي المال لا إن اختلفا أي في الشرط أو الإرادة فلا يلزمه ذلك + يطرد في اختلاف جنس المضمون وقدره وفي الضمان وعدمه: أنا ضامن زيدا وقال زيد لم يكن ضمنتا لي فالقول قول الضامن لا قول زيد) + مسائل الوكيل والكفيل ×3 (لا يجب وكيل للخصومة لأن للقاضي سماع بينته في غيبة المطلوب ولو أقام المدعي شاهدا بالحق ولم يحلف معه وهو ظاهر / لا يجب كفيل بالوجه بالدعوى مجردة إلا بشاهد واحد لتقوى دعواه / وإن ادعى الطالب بينة حاضرة بالسوق أو من بعض القبائل أوقفه ولا يسجنه فإن جاء ببينة عمل بمقتضاها وإلا خلى سبيل المدعى عليه) + القيمة [fragment dégradé consigné: la Loi sage ouvre le champ à ceux qui ont les intentions bonnes...] + تقويم ×3 (أعرف بضمان الوجه وضمان الطلب وأبين حكمهما / أذكر متى يغرم الضامن ومتى يبرأ / أوضح أحكام اختلاف الضامن والطالب) + استثمار [passage ad-Dardīr/ad-Dasūqī dégradé + ابن القاسم قال مالك ليس عليه إلا وجهه أبدًا وإن أجلته آجالا كثيرة وشرط الحمِيل جائز — البيان والتحصيل 11/373 ✓] + إعداد L23 (مفهوم الشركة / حكمها وشروطها / أحكامها وآثارها / أنواع الشركات + قاعدتا حرية الإثبات وافتراض التضامن).
- ARBITRAGES consignés : القيمة dégradée (1 phrase reconstructée + suite illisible consignée) ; تعريف ضمان الطلب dégradé (sens canonique consigné) ; صيغته fragments dégradés ; غرم الضامن fragments dégradés ; « بكالسوق » → « بالسوق » ; la glose de la 3e مسألة très dégradée ; الاستثمار p.173 : le passage « ويشترط عليه أنه ليس عليه إلا وجهه... » rendu en La mise en valeur avec référence البيان والتحصيل 11/373 (le titre de l'ouvrage cité « ال ره هات » fragment dégradé consigné — ad-Dardīr probablement).
- htmlFr FR-seule 14 356 car, QA double porte PASS ×2 (balises h1+h2 ×10+h3 ×3+p/ul/ol/li/strong/em équilibrées, guillemets équilibrés, 0 placeholder, couverture 25/25 mots-clés) ; h1 « Leçon 22 — Les types de la garantie et leurs jugements ».
- POSE : hand-set w45-pose-f3l22.py, slot vérifié VIDE (origin = HEAD = 259b6d08) ; titleAr/titleFr RÉALIGNÉS sur le tirage (« أنواع الضمان وأحكامها » / « Les types de la garantie et leurs jugements » — le catalogage initial جملة من الفرائض والآداب = faux) ; registre IA-3 → fiqh-3es 24/29 posés ; trace 7bbe855419e362a2-w45.
- SUIVANT : **L23 الشركة pp.173+ (docId pdf-23)** — le متن L23 = le canon « باب الشركة: الشركة إذن في التصرف لهما مع أنفسهما وإنما تصح من أهل التوكيل والتوكل ولزمت بما يدل عرفا: كاشتركنا بذهبين أو ورقين اتفق صرفهما وبهما منهما وبعين وبعرض وبعرضين مطلقا وكل بالقيمة يوم أحضر لا فات إن صحت إن خلطا ولو حكما... » (p.173 : objectifs ×4 du الإعداد déjà lus : مفهوم الشركة / حكمها وشروطها / أحكامها وآثارها / أنواع الشركات + قاعدتا حرية الإثبات وافتراض التضامن) — le titleAr catalogué pdf-23 « جملة من مكارم الأخلاق » est probablement FAUX aussi.

## W46 — 2026-11-23 — IA-3 — URGENCE CI réparée + traduction fiqh-3es leçon 23 من يعقد الشركة وما تنتعقد به (pdf-23 réaligné, pp.173-182) POSÉE

- URGENCE CI (demande utilisateur : « all jobs have failed, run failed depuis plusieurs jours ») : DIAGNOSTIC via API REST Actions (gh absent du sandbox) — les runs rouges des 21-23 nov (5 occurrences : W28-fix, W37-b, W39, W43, W44) = le step 5 « Commettre et pousser le rendu s'il change » de rendu.yml : après un push rejeté (non-fast-forward), le `git pull --rebase origin main` CONFLICTE sur le commit [ci] quand une poussée concurrente d'une autre IA est arrivée pendant le rendu (log job 137506849674 : « error: could not apply 3d94d8f... [ci] rendu du site synchrone des données ») — chaque échec était suivi d'un run vert, le site n'a jamais été cassé, mais des emails « Run failed » à répétition. FIX : plus de rebase — reprise HARD sur origin/main (fetch + reset --hard) + régénération complète du rendu à chaque nouvelle tentative (jamais de conflit possible, rendu toujours synchrone des dernières données, convergence garantie par la boucle ×3). Commit 15999658 poussé — le run du fix lui-même VERT (45128353238 success, rendu [ci] c1f86d0 poussé, pages build déployées) ✓.
- DISQUE : sandbox à 385 MB libres (96%) — cause : repo-417/.git = 5.3 GB (historique des builds CI accumulés) + miroirs hadith obsolètes (ht3-mirror 656 MB, ht3-l19 193 MB) + images de travail f3-l15 (~30 MB). Nettoyage : miroirs + images supprimés (850 MB) ; repo-417 remplacé par un clone léger --depth 3 --filter=blob:none + sparse-checkout EXCLUANT content/textbooks-src/ et content/textbooks/ (~430 MB de PDF sources inutiles localement, les manuels sources sont déjà en local : work/fiqh3.pdf etc.) — LE CHECKOUT COMPLET NE TENAIT JAMAIS (les builds échouaient sur content/textbooks) ; d'abord 2 échecs de clone (checkout partiel) puis rm du vieux repo AVANT le checkout du nouveau (vieux repo vérifié CLEAN : 0 non-tracké, 0 modifié, tout poussé) → disque 5.7 GB libres (40%) ✓ ; repo main = c1f86d0 (rendu CI le plus récent), clean.
- pdf-18 : RELIQUAT OBSOLÈTE une fois de plus — déjà posé sur origin (titleAr أحكام الضمان ✓) ; non posés : pdf-23..pdf-27 → cible réelle pdf-23.
- BORNES L23 : médaillon N°22 « من يعقد الشركة وما تنتعقد به » pp.173-181 + الإعداد p.181 ; p.182 = début L24 أحكام شركة المفاوضة (متن canon « ثم إن أطلقا التصرف وإن بنوع فمفاوضة... ») ; titleAr catalogué « جملة من مكارم الأخلاق » = FAUX → réaligné « من يعقد الشركة وما تنتعقد به » (médaillon N°22 zoomé + sommaire du manuel complet fiqh-3-thanawi.pdf ligne 402 concordante à une lettre près : « ما تنعقد » vs médaillon « ما تنتعقد » — le médaillon fait foi) ; متن L23 = le canon du باب الشركة de « الشركة إذن في التصرف لهما مع أنفسهما » (pos 208720) à « لا بذهب وبورق وبطعامين ولو اتفقا » — lettre à lettre vérifié par les couches (فالتالف من ربه / فبينهما / وعلى المتلف نصف الثمن / وهل إلا أن يعلم بالتلف فله وعليه / أو مطلقا إلا أن يدعي الاخذ له تردد ✓).
- MATIÈRE : objectifs ×3 du médaillon ZOOMÉS (تعرف مفهوم الشركة ومن تصح منه وما تنتعقد به / إدراك الآثار المترتبة على عقد الشركة / تمثل أحكام الشركة في معاملاتي المالية) + تمهيد + الفهم glossaire ×6 ZOOMÉ (التوكيل: الإنابة بأن يجعل غيره قائما مقامه في العقود والتصرفات / التوكُّل: قبول الوكالة والالتزام بأحكامها / العرف: ما استقرت النفوس عليه بشهادة العقول وتلقته الطبائع بالقبول / الصرف: بيع عملة بأخرى كبيع الدينار بالدراهم أو مبادلة نقد بنقد عددا أو وزنا / التالف: الذاهب الضائع / نَقْد: النقد في البيع خلاف الأسِّيَة ويطلق بمعنى مقابل العرض — l'OCR « التسيئة » corrigé en « الأسِّيَة » par zoom) + استخلاص ×3 + الشرح 3 axes : أولا مفهوم الشركة وحكمها وشروطها (تعريفها لغة: ابن فارس الشين والراء والكاف أصلان + الآية واشركه في أمري [طه 32] — le « طه 13 » du tirage = OCR de 32, vérifié islamweb معجم مقاييس اللغة باب الشين والراء surano=20 ayano=32 — + جمع شريك على شركاء وأشراك ; اصطلاحا: إذن في التصرف لهما مع أنفسهما كالجنس يشمل الوكالة والقراض وقوله لهما كالفصل مخرج للوكالة من الجانبين وقوله مع أنفسهما يخرج بعض صور القراض ; ولا مفهوم للتثنية بل قد تكون أكثر من اثنين) ; حكمها الجواز في الجملة + أدلتها الكتاب والسنة والإجماع (من الكتاب: شركاء [النساء 12] + ثانية dégradée consignée ; من السنة: القدسي أنا ثالث الشريكين ما لم يخن أحدهما صاحبه — سنن أبي داود كتاب البيوع + المناوي فيض القدير 2/803 + الطيبي ; الإجماع: أجمع المسلمون على جواز الشركة في الجملة) ; وإنما تصح من أهل التوكيل والتوكل = البالغ الرشيد فلا تصح شركة الصبي ولا المجنون ولا السفيه ; صيغها ×5 (الذهبان: بشرط اتفاق صرفها ولا يضر الاكتلاف في الصرف بعد العقد + اتفق وزنهما وجودتهما أو رداءتهما → اتفاق قيمتهما سواء اتحدت سكتهما أم لا ; الذهب والفضة: وبهما منهما مساواة ذهب أحدهما لذهب الآخر نصابا وقيمة ; العينان: وبعين وبعرض وأراد بهما يشمل الطعام ; العرضان: مطلقا اتفقا جنسا أو اختلفا فدخل فيه ما كان أحدهما عرضا والآخر طعاما ; الثقال: وكل بالقيمة يوم أحضر لا فات + التوفية وما يكال ويوزن ويكيل + الغائب غيبة قريبة قيمته يوم دخوله في ضمانه في البيع دون يوم دخوله في ضمان الشركة) ; ثانيا ضمان مال الشركة (إن خلطا ولو حكما: يضمن مال الشركة من الشريكين إن خلطا ماليهما حقيقة بأن لم يتميز أحدهما من الآخر بل ولو حكما بأن يكون كل واحد من المالين في صرة منفردة وجعلاهما في حوز أجنبي أو أحد منهما ; وإلا فالتالف من ربه + ما ابتيع بغيره فبينهما: العرض المشترى للتجارة مشترك بينهما إن ربح فلهماء وإن خسر فعليهما على ما دخلا عليه للزوم الشركة بالعقد + وعلى المتلف نصف الثمن: ثمن المشترى بالسالم إن كانت الشركة بالنصف وإلا ضمن حصته فقط ; وهل إلا أن يعلم بالتلف فله وعليه أو مطلقا إلا أن يدعي الأخذ له تردد: إذا علم بالتلف واشترى بالسالم بعد علمه فله ربح ما اشتراه وعليه خسره وإن اشترى قبل علمه فبينهما وبعده يخير ذو التالف إلا أن يدعي ذو السالم الأخذ له لنفسه فيختص به ولا خيار لشريكه) ; ثالثا ما تصح به وما لا تصح به (ولو غاب نقد أحدهما إن لم يبعد كاليومين ولم يتجر بالحاضر قبل قبض الغائب ; لا بذهب وبورق ولو عجل كل ما أخرجه لصاحبه ; وبطعامين ولو اتفقا: اختلفا نوعا وصفة وقدرا بل ولو اتفقا لأنه يؤدي إلى بيع الطعام قبل قبضه) + القيمة (الشركة من سبب البركة ونماء المال إذا قامت على الصدق والأمانة + حاجة المجتمع إليها في المشاريع الكبرى الصناعية والعمرانية والتجارية والزراعية — fin dégradée consignée) + تقويم ×3 (مفهوم الشركة / أحكام ضمان مال الشركة / شروط الشركة — items dégradés consignés) + الاستثمار الموطأ (باب ما جاء في الشركة والتولية والإقالة: قال مالك في الرجل يقول اشتر هذه السلعة بيني وبينك وانقد عني وأنا أبيعها لك إن ذلك لا يصلح وإنما ذلك سلف يسلفه إياه على أن يبيعها له + أشركني بنصف هذه السلعة وأنا أبيعها لك جميعا حلال لا بأس به بيع جديد باعه نصف السلعة على أن يبيع له النصف الآخر ✓) + أتأمل ×2 (2e dégradée consignée) + إعداد L24 (قسما من أقسام الشركة ومفهومه / ما حكم تصرف أحد الشريكين دون إذن شريكه).
- ARBITRAGES consignés : 15 fragments dégradés (2e citation du Livre + sa ref ; شرح الثقال fin ; شروع ما تصح به ; القيمة fin ; تقويم items 1 et 3 ; أتأمل item 2 ; الشرح du اصطلاحا fin) ; « طه 13 » → « طه 32 » (web vérifié) ; « التسيئة » → « الأسِّيَة » (zoom) ; « تسيئة » des couches OCR corrigées ; le canon « ولو اتفقا » fin du متن ✓.
- htmlFr FR-seule 18 566 car (la plus longue posée), QA double porte PASS ×2 (balises h1+h2 ×10+h3 ×3+p/ul/ol/li/strong/em équilibrées, guillemets équilibrés, 0 placeholder, couverture 30/30 mots-clés, ordre des sections OK, 15 fragments consignés).
- POSE : hand-set w46-pose-f3l23.py, slot vérifié VIDE (origin = HEAD = c1f86d0) ; titleAr/titleFr RÉALIGNÉS ; registre IA-3 → fiqh-3es 25/29 posés ; trace a17d619389e21a2f-w46.
- SUIVANT : **L24 أحكام شركة المفاوضة pp.182+ (docId pdf-24, médaillon N°23)** — متن du canon « ثم إن أطلقا التصرف وإن بنوع فمفاوضة ولا يفسدها انفراد أحدهما بشئ وله أن يتبرع إن استأنف به أو خف كإعارة آلة ودفع كسرة ويبضع ويقارض ويودع لعذر وإلا ضمن ويشارك في معين ويقيل ويولى ويقبل المغيب وإن أبى الآخر ويقر بدين لمن لا يتهم عليه ويبيع بالدين لا الشراء به ككتابة وعتق على مال وإذن لعبد في تجارة أو مفاوضة واستبد آخذ قراض ومستعير دابة بلا إذن وإن للشركة ومتجر بوديعة بالربح والخسر إلا أن يعلم شريكه بتعديه في الوديعة وكل وكيل فيرد على حاضر لم يتول كالغائب إن بعدت غيبته وإلا انتظر والربح والخسر بقدر المالين وتفسد بشرط التفاوت ولكل أجر عمله للآخر » (d'après la fenêtre canon + p.182) — le titleAr catalogué pdf-24 probablement faux aussi (sommaire : أحكام شركة المفاوضة).

## W47 — 2026-11-23 — IA-3 — recyclage sandbox + traduction fiqh-3es leçon 24 أحكام شركة المفاوضة (pdf-24 réaligné, pp.182-188) POSÉE

- RECYCLAGE SANDBOX au milieu de la séance (bash ENOENT ×4, conteneur perdu) : le shell est rétabli au nouveau conteneur ; l'utilisateur a fourni un PAT GitHub pour le push (utilisé en ligne de commande uniquement, jamais écrit dans un fichier persistant). Scripts de reprise w47-reclone.sh + w47-couches.sh (écrits avant la coupure) exécutés ✓.
- REPRISE : reclone sparse OK — origin/main = a6584ee (un commit [ci] rendu du site synchrone des donnée concurrent au-dessus de mes 2 commits W46 ; rien à refaire, W46 bien en ligne) ; registre origin = 25/29, non posés pdf-24..27 ; titleAr catalogué pdf-24 toujours le faux du médaillon N°22 (خصال الفطرة وبعض الآداب).
- BORNES L24 : médaillon N°23 « أحكام شركة المفاوضة » pp.182-188 + الإعداد p.188 ; p.189 = début L25 (متن canon « وكل وكيل يرد على حاضر لم يتول كالغائب إن بعدت غيبته وإلا انتظر... ») ; titleAr catalogué FAUX → réaligné « أحكام شركة المفاوضة » (médaillon N°23 zoomé 200dpi + sommaire du manuel ligne 403 concordant) ; متن L24 = canon du باب الشركة de « ثم إن أطلقا التصرف » (pos 208720) à « إلا أن يعلم شريكه بتعديه في الوديعة » — NB consigné : le découpage en leçons du tirage recoupe le paragraphe canonique AVANT sa fin : L24 = marqaz 178-187 sans « وكل وكيل » ; L25 reprend « وكل وكيل يرد على حاضر » et va jusqu'à « ولكل أجر عمله للآخر » (fenêtre canon 209100-210650 imprimée ✓).
- MATIÈRE (couches pdftotext pp.182-189 + 20 zooms 200-400dpi, budget image exact) : objectifs ×3 ZOOMÉS (1- تعرف مفهوم شركة المفاوضة [item masqué à W46, dézoomé ✓] / 2- إدراك أحكام شركة المفاوضة / 3- تمثل أحكام بعض أقسام الشركة في المعاملات) + تمهيد (merchant propose l'association sur la base de l'absolu du droit de disposition ; fragment final du tirage bruité, phrase tronquée proprement — consigné) + متن canon lettre à lettre + الشرح glossaire ×6 (فمفاوضة / ويبضع / ويقارض / ويودع / ويقيل / ويولي) + استخلاص ×2 ZOOMÉ (تعريف شركة المفاوضة / بعض تصرفات أحد الشريكين) + التطبيق = 3 محاور du cours : 1) تعريف شركة المفاوضة وأنواعها (عامة : absolu dans tous les types / خاصة : dans un type) ; 2) تصرفات أحد شريكي المفاوضة ×10 ZOOMÉS (تبرع si استأنف ou خف : إعارة آلة ودفع كسرة لفقير ; أبضاع بضاعة معلومة من بلد كذا يرسلها أو يقدم بها للشريكين ; قراض si اتسع المال وإلا امتنع ; ودع seulement avec excuse et sans crainte sur le bien — sinon dépôt obligatoire et il garantit — et il convient d'être véridique dans la revendication d'excuse car associé de confiance ; مشاركة un étranger dans une part déterminée sans que sa main circule dans la totalité ; إقيل : rendre au prix auquel lui ou son associé l'a vendue ; إيال : vendre à son semblable de prix si crainte de déclin sinon il doit la part du profit ; قبول المعيب rendu après vente, si l'associé agrée — et « وإن أبى الآخر » porte le retour à tout depuis التبرع ou seulement au précédent ; إقرار avant séparation et mort d'une dette pour qui on ne le soupçonne pas, et elle oblige l'associé ; بيع بالدين sans autorisation — non l'achat à crédit — sinon on donne le choix à l'associé entre acceptation et rendu, le prix à la charge de l'acheteur seul) ; 3) حكم الاستبداد ×3 (آخذ قراض : muḍāraba même avec autorisation — il est un loué qui a loué sa personne pour une part du profit, rien à l'associé ; مستعير دابة : le « et » de situation et « dût » superflu, leur suppression première — réservé le profit qui est le loyer et à la perte la garantie ; متجر بوديعة : dépôt chez eux deux ou l'un des deux, au profit et à la perte dût-il mélangé au bien de négoce, comme dans la Mudawwana) + يلاحظ (la Loi a autorisé mais obligé de supporter les suites profit/perte — « الشريعة الغراء وسعت دائرة المعاملات باستجلاب الزبناء واستمالة قلوب المستفدين » — lecture zoomée complète).
- القيمة ×3 ZOOMÉE (مفهوم وحكمها / ما يجوز من تصرفات أحد شريكي / أين يستبد به أحد الشريكين وأثر ذلك) + الاستثمار Ibn Rushd al-Jadd (Bidāyat al-mujtahid) citation complète : « ولا يكون الرجل شريكا للرجل إلا إذا شاركه في رقاب الأموال على الإشاعة... فكل شريك خليط وليس كل خليط شريكا والخلطة أعم من الشركة » + versets : الخليط = Ṣād 22-23 du tirage [ص: 22-23] (les deux adversaires de Dāwūd, خُلَطَاء — API Coran vérifiée) + la 3e ligne calligraphique = début Ṣād 24 en VARIANTE WARSH « بِسُؤَالِ نَعْجَتِهِ عَلَىٰ نِصَابِهِ » (vs Hafs « نَعْجَتِكَ إِلَىٰ نِعَاجِهِ » — API tranche la lecture Hafs, le tirage est en Warsh ✓ consigné) ; الشركة = az-Zumar 29 « ضَرَبَ اللَّهُ مَثَلًا رَجُلًا فِيهِ شُرَكَاءُ مُتَشَاكِسُونَ وَرَجُلًا سَلَمًا لِرَجُلٍ... » API vérifié — tirage annoté [الزمر: 28] (décalage Warsh −1, pattern W762) ; ثم قال تعالى = an-Nisā 8 API vérifié ; فسماهم الله تعالى خلطاء لما لم يشتركوا في أعيان النعاج (passage retrouvé par les snippets du manuel ancien habous.gov.ma — le site lui-même bloque le fetch : 404 sur toutes les URLs, même curl) ; source du tirage [المقدمات الممهات 3/ 33 – 34 بتصرف] (zoom 400dpi net).
- ARBITRAGES consignés : le النص de la الوضعية n'existe pas ailleurs dans le tirage (frise p.188 vide, bas p.187 vide) — c'est le texte d'Ibn Rushd de l'الاستثمار (renvoi explicite consigné dans le htmlFr) ; تمهيد fragment final tronqué proprement ; le tirage lit « فإن فعل خير شريكه بين القبول والرد » — rendu « on donne le choix à son associé » (le sens exige خيَّرَ, consigné) ; la ref du tirage [ص: 22-23] couvre les deux lignes citées alors que la 3e calligraphique porte le Ṣād 24 (consigné dans le N.d.T.).
- htmlFr FR-seule 16 553 car, QA double porte PASS ×2 (script w47-qa-f3l24.py : 10 h2 conventionnelles exactes, objectifs ×3, 9 segments متن canon lettre à lettre [comparaison lettres-arabes-seules : tatweel retiré, 0670=alef réel, hamzas unifiées, yeh farsi unifié], 10 dispositions du 2e axe, 3 items du 3e axe, 5 versets API quran-simple confirmés + 2 anchors Warsh inline dans le bloc ar, balises h1/h2×10/h3×3/p/ul/ol/li équilibrées, 0 placeholder, slot vide) + relecture ligne à ligne contre les 20 zooms.
- POSE : hand-set w47-pose-f3l24.py, slot vérifié VIDE ; titleAr/titleFr RÉALIGNÉS (أحكام شركة المفاوضة / Les jugements de la société de mufāwaḍa) ; registre IA-3 → fiqh-3es 26/29 posés ; trace W47.
- SUIVANT : **L25 (docId pdf-25) — le متن canon commence à « وكل وكيل يرد على حاضر لم يتول » (p.189) et le tirage l'étend jusqu'à « ولكل أجر عمله للآخر » puis poursuit « وله التبرع والسلف والهبة بعد العقد... » (fenêtre canon) ; le titleAr catalogué pdf-25 تطبيقات على مسائل فقهية = probablement le faux du médaillon suivant (à zoomer) ; l'إعداد de L24 pose 3 questions sur la mufāwaḍa → matière déjà en main pour les bornes**.

## W48 — 2026-11-23 — IA-3 — traduction fiqh-3es leçon 25 تصرفات شريك المفاوضة وأحكام التنازع (pdf-25 réaligné, pp.189-196) POSÉE + FIX identité du livre + fix convention des sections pdf-24

- REPRISE post-recyclage : repo-417 disparu au nouveau conteneur → reclone (origin = ffbf22e, rendu [ci] au-dessus du fix 029d8a0 de W47 ✓) ; session W48 déjà amorcée avant la coupure (scripts w48-couches.sh/w48-zooms.py + couches c-p190..194 + zooms z1-z10) : complétée (c-p189 régénéré, couches p.195-198, zooms z11-z15 via w48-zooms2.py).
- BORNES L25 : médaillon N°24 « تصرفات شريك المفاوضة وأحكام التنازع » (2 LIGNES — zoom 200dpi ; la couche OCR tronquait la seconde) pp.189-196 ; p.197 = début L26 « أحكام شركة العنان » ; متن L25 = canon du باب الشركة de « وكل وكيل » à « وإلا ببينة على: » — NB consigné : le tirage coupe au MILIEU de la clause canonique ; la suite (« كإرثه وإن قالت لا نعلم… وألغيت نفقتهما وكسوتهما… وإن ببلدين مختلفي السعر… ») est reprise clause par clause dans le cours (axe رابعا) ; titleAr catalogué « تطبيقات على مسائل فقهية » = FAUX → réaligné « تصرفات شريك المفاوضة وأحكام التنازع ».
- MATIÈRE : objectifs ×3 (1- تعرف بعض أحكام شركة المفاوضة [zoom] / 2- إدراك تصرفات شريكي المفاوضة / 3- تمثل أحكام شركة المفاوضة في بعض الوضعيات المالية) + تمهيد (association comme-agence, profit/perte, différends, القضاء حسما للنزاع) + متن canon lettre à lettre (11 segments vérifiés script QA) + الشرح ×4 (الخسر: ضد الربح / التبرع: الإعطاء بلا عوض / لائق: مناسب / التلف: تلف الشيء تفانهلك فهو تالف) + استخلاص ×3 + cours 4 axes : أولا أحكام الشريكين في الشركة ×3 (وكالة : كل واحد كالوكيل عن الآخر في البيع والشراء والأخذ والإعطاء والكراء والاكتراء والقيام بالاستحقاق والعين — لا أن له وكالة حقيقية إذ هو شريك والشريك غير الوكيل ; الرد : على حاضر لم يتول كالغائب إن بعدت غيبته وإلا انتظر — لأنه أقدر بأمر المبيع لعل له حجة، ولا يرد على الحاضر وأولى إذا كانا حاضرين ; الفساد : بشرط التفاوت = اشتراط أحدهما التفاوت في قسمة الربح والخسر بغير قدر العمال + ولكل أجر عمله للآخر = إن اطلع على الفساد قبل العمل فسخ العقد وإلا قسم الربح على قدر المالين — مثال الثلث/الثلثين avec retour du سدس du profit et أجرة سدس de l'œuvre) ; ثانيا التبرع والسلف والهبة بعد العقد (السلف : يجوز لأحد الشريكين أن يسلف شريكه شيئا ; الهبة : يجوز أيضا أن يهب شيئا لشريكه ; الثلاث بعد العقد لا في العقد — لأن التبرع والهبة على التفاوت أو التهمة… فكأنه مشترط لجر النفع في السلف فإن لم يجر نفعا جاز في العقد أيضا — وظاهر قوله بعد العقد ولو بأثره بناء على أن اللاحق للعقود ليس كالواقع فيها) ; ثالثا أحكام التنازع ×6 (1- التلف والخسر : القول لمدعي التلف — وهو ما نشأ لا عن تحريك — والخسر — وهو ما نشأ عن تحريك — لأنه أمين في مال الشركة ; cela si son mensonge n'apparaît pas par preuve ou indices ; sinon il garantit et il est gage — الأمين يضمن إذا فرط ; 2- اللائق : القول بلا يمين لمدعي شراء لائق — مشبه مناسبه — به وبعياله من طعام ولباس فقط وأما غير الطعام واللباس واللائق منهما فلا يصدق ويرد الشركة ; 3- النصف : فالقول لمدعي النصف بيمين وحمل الاشتراك على الشريكين في كون شركتهما بالنصف أو غيره ; 4- الاختصاص : القول لمدعي الاشتراك فيما بيد أحدهما إلا لبينة أقامها الحائز على كإرثه — الأقسام ثلاثة (لا نعلم تقدمه لها / نعلم تقدمه على الشركة فيكون بينهما / لا نعلم تقدمه ولا تأخره اختص به) + محل كون القول لمدعي الاشتراك إن شهد بالمفاوضة وأولى إن شهد بوقوع الشركة بينهما على وجه المفاوضة ; 5- البقاء عند ميت : القول للمقيم بينة على شريكه الميت بأخذ مائة أنها باقية إن أشهد بها عند الأخذ أو قصرت المدة — وأما الحي المنكر للأخذ إذا أقيمت عليه بالبينة فإن دعواه الرد لمال الشركة تقبل؟ consigné tel quel du tirage [zoom p.194] ; 6- صداق : القول للدافع في أنه من المفاوضة لتمسكه بالأصل إلا أن يطول كسنة ثم القول لمدعي أنه من ماله الخاص لأن عدم مطالبته يدل على صدقه — وما قيم بينة لمدعي الاختصاص فلا تسقط بطول كسنة بل تقبل بينته) ; رابعا من تصرفات شريكي المفاوضة ×2 (إقرار بعد تفرق أو موت فهو شاهد في غير نصيبه — المقر مبرز في العدالة يحلف معه المقر له ويستحق وأما في نصيبه فيؤاخذ به ولو لم يتهم عليه ; ألغيت نفقتهما وكسوتهما وإن ببلدين مختلفي السعر كعيالهما إن تقاربا وإلا حسبا كانفراد أحدهما به — لأن كل واحد إنما عقد للتجر مؤنة كل واحد فاستحل اختلاف السعرين + أسقط شرطا وهو كون المال بينهما مناصفة في مسألة العيال فقط) + يتجلى من الدرس (الشريعة المباركة لم تترك ذلك إلى هوى النفوس بل وضعت ضوابط وقيودا تنتظم بها المعاملات على أحسن الأحوال…).
- الاستثمار : العلامة بهرام رحمه الله (تجر بوديعة تعديا اختص إن لم يعلم الآخر… والربح والعمل على قدر ماليهما… وفسدت بشرط التفاضل… واختير إن ربح فله الأقل منه… وصدق مدعي تلف وخسارة… وقسم السدس بينهما وقيل يحلفان وينصف) — tirage annote [الشامل في فقه الإمام مالك 2/ 697] (zoom 200dpi net, la couche OCR lisait 7962) + الوضعية ×3 (أتعرف على العلامة بهرام وكتابه الشامل) + التقويم ×3 + الإعداد ×3 (préparent L26 العنان ✓).
- FIX IDENTITÉ DU LIVRE : couverture p.1 zoomée 300dpi (z16) = « الفقه / من متن الشيخ خليل بشرح الدردير ومحاشية الدسوقي / للسنة الثالثة من التعليم الثانوي العتيق » + web (habous.gov.ma : « الفقه من مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي » pour les années secondaires) → titleAr/titleFr du LIVRE réalignés : « الفقه من متن الشيخ خليل بشرح الدردير ومحاشية الدسوقي للسنة الثالثة من التعليم الثانوي العتيق » / « Fiqh — le Mukhtaṣar de l’imam Khalīl, comm. al-Dardīr + ḥāshiya al-Dasūqī (3ᵉ collège) » (l’ancien « la Risāla d’Ibn Abī Zayd » était le faux du schéma fiqh-1es/2es) ; les 10 intros htmlFr contenant le commentaire inexistant « Kifāyat al-ʿaynī al-māʿī » corrigées en « commentaire al-Dardīr, marginales al-Dasūq » ; NB consigné : les titleAr des livres fiqh-1es/fiqh-2es (Risāla) à auditer séparément (hors périmètre).
- FIX CONVENTION DES SECTIONS (pattern pdf-22/23 vérifié dans le registre) : le يلاحظ-texte de synthèse → « La valeur de la leçon » ; التقويم-questions → « L’évaluation » ; الوضعité intégrée EN FIN de « La mise en valeur » (pdf-22 : « Regarde: examine ce passage… ») ; DONC pdf-24 CORRIGÉ (script w48-fix-pdf24.py : يلاحظ déplacé de la fin de L’analyse vers La valeur de la leçon, التقويم sous L’évaluation, الوضعية intégrée à la fin de La mise en valeur — 10 h2 conventionnels ✓) ; pdf-25 structuré de même (يلاحظ/التقويم/وضعité-intégrée) — la convention reste à vérifier pour pdf-1..19 lors d’un audit futur.
- ARBITRAGES consignés : متن canon Daman « وكل وكيل، فيرد » (avec فا) vs tirage OCR قَبْرَدُ — le N.d.T. cite la lettre canon du tirage sans le فا ambigu (segment QA scindé) ; « وأما الحي المنكر للأخذ… » (p.194) : couche très bruitée, transcrit d’après le zoom 200dpi tel quel.
- htmlFr FR-seule 20 355 car, QA double porte PASS ×2 (script w48-qa-f3l25.py : 10 h2 conventionnelles, objectifs ×3, 11 segments متن canon lettre à lettre, N.d.T. vérifié, 8 rubriques de cours présentes, évaluation ×3, وضعité ×3 dans la mise en valeur, préparation ×3, الاستثمار بهرام + ref [الشامل 2/697], balises équilibrées, 0 placeholder, slot vide) + relecture contre 14 zooms (budget image respecté).
- POSE : hand-set w48-pose-f3l25.py, slot vérifié VIDE ; registre IA-3 → fiqh-3es 27/29 posés ; trace W48.
- SUIVANT : **pdf-26 (L26 أحكام شركة العنان pp.197+) — متن « وإن اشترطا في الاستبداد فعنان وجاز لذي طير وذي طيرة أن يتفقا على الشركة في الفراخ واشتر لي ولك فوكالة وجار وانقد عني إن لم يقل وأبيعها لك وليس له حبسها إلا أن يقول واحبسها فكالرهن وإن أشلف… » (couches p.197-198 déjà prises ✓) ; puis pdf-27 (فهرس وتراجم الأعلام / المصادر والمراجع) — FIN DU LIVRE.**

## W49 — 2026-11-23 — IA-3 — traduction fiqh-3 leçons 26-27 (pdf-26 العنان pp.197-201, pdf-27 الجبر والعمل pp.202-208) POSÉES — REGISTRE fiqh-3es COMPLET 29/29

- REPRISE post-recyclage (repo-417 recloné, 3,2 GB binaires) ; couches p.199-213 extraites du PDF source local (work/fiqh3.pdf, 226 pages).
- BORNES : L26 = médaillon N°25 « أحكام شركة العنان » pp.197-201 ; L27 = médaillon N°26 « أحكام شركة الجبر وشركة العمل » pp.202-208 ; L28 « شركة الذمم » pp.209-213 (titleAr catalogué « المصادر والمراجع » = FAUX, comme فهرس/تراجم pour pdf-26) ; puis تراجم الأعلام pp.215-219 + المصادر/فهرس pp.220-226 — LA LEÇON 28 (الذمم) ET LES INDEX NE SONT PAS CATALOGUÉS DANS LE REGISTRE (29 slots pdf-1..27 + 12351/12352) : consigné, hors périmètre de ce slot-count.
- pdf-26 العنان : متن canon Daman vérifié (11 segments : « وإن اشترطا نفي الاستبداد فعنان… وليس له أن يحبسها فكالرهن… وإن أسلف عير المشترى جاز إلا ليصير المشترى ») — NB consignés : (1) le tirage omet « إلا أن يقول واحبسها » (réapparaît dans le cours clause 3, même pattern de découpage que L25) ; (2) canon Daman OCR « إلا لكبصيرة المشتري » défectueux, tirage correct « إلا ليصير المشترى » ; cours 4 clauses (اتفاق الرفع sur les poussins / التوكيل « اشتر لي ولك فوكالة » / أنقد عني مع حبسها=كالرهن وضمان الرهن / السلف غير المشترى) + يلاحظ (النظر إلى المآلات معتبر شرعا) + التقويم ×2 + الاستثمار Ibn Rushd (Sahnūn/ibn al-Qāsim/Mālik) [البَيان والتحصيل 5/12] + الإعداد ×2 ; refs tranchées au 300 dpi : [الفتاوى المهدية 3/37] (couche OCR « الفقدهات المههبات ») + [المختصر الفقهي لابن عرفة 7/17 بتصرف] ; « من المنشركة » tranché par la couche PDF.
- pdf-27 الجبر والعمل : متن canon vérifié (10 segments : « وأجبر عليها إن اشترى شيئا بسوقه لا لكسف وقنية… وجازت بالعمل إن اتحد… وفي جواز إخراج كل آلة واستئجاره من الآخر أو لا بد من ملك أو كراء تأويلان… ولم يستحق وارثه بقيته وأقطعه الإمام… وألغي مرض كيومين وغيبتهما لا إن كثر وفسدت باشتراطه ككثير الآلة وهل يلغى اليومان كالصحيحة تردد ») ; cours 2 axes : أولا الجبر (مفهوم : إلزام المشتري إشراك غيره / حكم : لازمة، قضى بها عمر وقالها مالك / أهميتها : خصوصية مالكية تغليب مصلحة الفرد / شروطها ستة : سوق-تجارة-بلد-حضور-تاجر-سكوت + مسألة الزقاق قولان أرجحهما عدم الجبر) ; ثانيا العمل (تعريف : اشتراك عاملين فأكثر في عمل أجرة بينهما / حكم : تجوز ولا تلزم بالعقد / شروط : اتحد-تلازما-تساويا-تقاربا-تعاون وإن بمكانين + الآلة ملك أو كراء تأويلان + أمثلة طبيبين/صائدين/حافرين / ما يلزم : العمل معه فيما يقبل + ضمان ما يقبله وإن تفاضلا وألغي مرض كيومين لا إن كثر / ما يفسد : باشتراط إلغاء كثير المرض، ويحسن الإعطاء بلا اشتراط + مسألة إلغاء اليومين تردد) ; التقويم ×3 + الاستثمار Ibn Rushd شركة الأبدان (ash-Shaibānī/ibn Ḥibān/ash-Shāfiʿī/Abū Ḥanīfa) [الفتاوى المهدية 3/37-38] + الإعداد القبلي ×2 (prépare L28 الذمم) ; L27 sans يلاحظ-texte → 9 h2 (fidèle au manuel).
- NB « وإن تفاضلا » clause cours (p.206) : m18 NET mais lexique technique dense — transcription fidèle littérale consignée (pas de fragment dégradé).
- QA double porte PASS ×2 (scripts w49-qa-f3l26.py : 10 h2, objectifs ×2, 6 segments متن canon, N.d.T., 4 clauses, refs ; w49-qa-f3l27.py : 9 h2, objectifs ×2, 10 segments متن canon, 2 axes, التقويم ×3, الإعداد ×2, refs) + relecture contre 20 zooms 200-300 dpi (budget image respecté).
- POSE : pdf-26 posé (11 012 car, titleAr « أحكام شركة العنان ») → 28/29 ; pdf-27 posé (16 396 car, titleAr « أحكام شركة الجبر وشركة العمل ») → **29/29 REGISTRE fiqh-3es COMPLET** ; trace W49.
- SUIVANT : hors registre — L28 شركة الذمم pp.209-213 + تراجم الأعلام pp.215-219 + المصادر/الفهرس pp.220-226 (extension du registre à décider) ; audit des titleAr fiqh-1es/fiqh-2es (Risāla) ; vérif pages en ligne pdf-26/pdf-27 après CI.

## W50 — 2026-11-23 — IA-3 — traduction fiqh-3 leçon 28 (pdf-28 شركة الذمم والوجوه pp.209-215) POSÉE — EXTENSION DU REGISTRE fiqh-3es À 30 ENTRÉES

- W49 vérifié post-recyclage : pages pdf-26/pdf-27 en ligne (HTTP 200, titres corrects), CI success — registre 29/29 confirmé.
- EXTENSION DU REGISTRE : la leçon 28 (médaillon N°27 « أحكام شركة الذمم والوجوه », pp.209-215) n'était PAS cataloguée dans les 29 slots (erreur du catalogueur initial : les slots pdf-26/pdf-27 portaient des titlesAr de fin de matière « فهرس وتراجم الأعلام »/« المصادر والمراجع », repurposés W49 pour les vraies leçons 26-27). Entrée pdf-28 créée en fin de registre (même pdfUrl/pdfOnly que pdf-27) — 30 entrées, 30 posées.
- L28 الذمم والوجوه : متن canon vérifié contre Daman (8 segments : « وباشتراكهما بالذمم أن يشتريا بلا مال وهو بينهما… وكبيع وجيه مال خامل بجزء من ربحه… وكذي رحى وذي بيت وذي دابة ليعملا… وترادوا الأكرية… وقضي على شريك فيما لا ينقسم… وإن أقام أحدهم رحى إذ أبيا فالغلة لهم ويستوفي منها ما أنفق ») — NB consignés : (1) la condition d'ouverture « إن كنا معلومين بالضمانة » ABSENTE du tirage ET du canon Daman (le متن enchaîne directement après la fin L27) ; (1bis) forme hésitante lam yatasāwa/tatasāwa — canon Daman « إن لم يتساو » retenu (sujet masculin الكراء) ; (2) متن du tirage s'arrête à « ويستوفون منها ما أنفق » (pluriel vs canon singulier « ويستوفي ») — le canon enchaîne avec le باب الجوار (الاذن/القسمة/الساتر… jusqu'à « تردد ») : découpage hors slot consigné ; (3) « فالغلة له » canon vs lettre hésitante du tirage — sens confirmé par Dasūqī.
- Cours 2 axes : أولا (تعريف/hكم شركة الذمم : société sur le ذمم sans capital, conditions الضمان/الجاه + définition الوجوه d'Ibn ʿAref [المختصر الفقهي 7/136] + interprétation du القاضي أبو محمد + حكمها « وكبيع وجيه مال خامل » avec القرافي/ابن القصار/الشافعي/أبو حنيفة [الذخيرة 8/29] + وكذي رحى) ; ثانيا القضاء ×5 (تراد الأكرية avec l'exemple 1000/2000/3000 dirhams + اشترط عمل رب الدابة + فيما لا ينقسم كذي سفل + الأملاك المشتركة التعليق/السقف/المرحاض/لا سلم + السقف للأِسفل عند التنازع avec [الزخرف: 32] — le texte du verset encadré n'est pas attestable graphiquement, ref seule consignée — + الغلة للشركاء وإن أقام أحدهم رحى إذ أبيا, exemple des trois associés dans la عرضة, ابن عبد السلام).
- يلاحظ-texte présent (سد الدراجع أصل من أصول مذهب مالك… منع التعامل بالمخاطرة والغرر) → 9 sections h2 avec « La valeur de la leçon » ; PAS d'الإعداد القبلي (dernière leçon du livre) ; التقويم ×3 ; الاستثمار Ibn Rushd coupé p.214 bas → suite tranchée en haut p.215 (وقال أبو حنيفة: شركة الوجوه جائزة وهي تنعقد على الوكالة…) + ref [المقدمات الممهدات 3/39] — cohérent avec les 3/37-38 de L27.
- QA double porte PASS (script w50-qa-f3l28.py : 9 h2, objectifs ×2, 8 segments متن canon, N.d.T. ×6 fragments, 2 axes + القضاء ×5, refs ×4, التقويم ×3, balises) + 11 zooms 200-300 dpi relus (budget image ~11/20).
- SUIVANT : fin de matière hors registre — تراجم الأعلام pp.215-219 + المصادر/الفهرس pp.220-226 (décision à prendre : extension en entrées « annexes » ou hors périmètre) ; audit des titleAr fiqh-1es/fiqh-2es (Risāla) ; vérif page pdf-28 en ligne après CI.

## W51 — 2026-11-23 — IA-3 — fin de matière fiqh-3es : ANNEXES pdf-29 (فهرس الأعلام, pp.216-218) + pdf-30 (فهرس المصادر والمراجع, pp.219-223) POSÉES — registre fiqh-3es → 32 ENTRÉES

- Décision consignée W50 tranchée : la fin de matière est intégrée au registre (l'index p.224 et pp.225-226 vides restent hors périmètre — l'index des leçons est couvert par le registre lui-même).
- 11 zooms 200 dpi lus (pp.216-218 = فهرس الأعلام 11 biographies ; pp.219-223 = فهرس المصادر والمراجع 33 références — les couches OCR annonçaient ~29 refs et des chiffres faux, tous corrigés par zoom : المتوفى 370 (ref 4), الثامنة (ref 21), 354هـ (ref 32)…). Budget image séance ~19/20 — plus aucun Read d'image.
- pdf-29 فهرس الأعلام : 11 notices (Ibn ʿĀchir 1040, Ibn Ghāzī 919, al-Badr ad-Damyāṭī/ibn ad-Damāmīnī 827, at-Tūnisī 734, aṣ-Ṣāwī 1241, aṭ-Ṭabībī 743, ʿAlīsh 1299, al-Manāwī 1031, ad-Damīrī 805, al-Qarāfī 684, Ibn ʿAbd as-Salām 749) — titre réel du médaillon : فهرس الأعلام (pas تراجم الأعلام) — NB consigné.
- pdf-30 فهرس المصادر والمراجع : 33 références letter-level avec NB consignés : ref 7 « الفرفر » coquille du tirage (titre connu : التوضيح في شرح مختصر ابن الحاجب) ; ref 19 « ببيد الرؤوف » coquille probable pour بْعَبْدِ الرؤوف (bio p.217 nette « عبد الرؤوف ») ; ref 25 crochet errant « بيروت[ » ; ref 30 fragment « 5/32 » hésitant ; ref 33 nnisba الوَرغمي/الروغمي hésitante → الروغمي consignée + « مؤسسة خلف أحمد الختور » selon la lettre du tirage.
- QA double porte PASS (w51-qa-annexes.py : 11 h3 pdf-29 avec dates toutes vérifiées ; 33 li pdf-30 avec titres arabes tous présents ; balises équilibrées ; artefact « ? non » de l'intro pdf-30 corrigé avant pose).
- SUIVANT : audit des titleAr fiqh-2es (2 entrées seulement — registre à compléter) ; vérif pages pdf-29/30 en ligne après CI.

### W51 bis — vérif pages en ligne
- pdf-29 et pdf-30 EN LIGNE (HTTP 200, فهرس الأعلام / المصادر présents) après rebase sur [ci] 135bccfd puis push af124fee.
- Micro-écart cosmétique consigné : le template du site préfixe automatiquement « Leçon N — » aux titleFr de toutes les entrées — pour les annexes pdf-29/30 ce préfixe est inexact (ce ne sont pas des leçons ; le titleFr porte « annexe »). Modification du template hors périmètre IA-3 cette séance.

## W52 — 2026-11-23 — IA-3 — audit des registres fiqh voisins + DÉPLACEMENT des annexes Waraqāt mal affectées

- Re-clone du dépôt (sandbox recyclé : repo-417 perdu, 6,4 G, historique intact jusqu'à [ci] 7ea39f35). fiqh-3es 32/32 confirmé.
- AUDIT : les entrées 12351 (فهرس الأعلام, 9 figures) et 12352 (فهرس المصادر والمراجع, 23 refs) posées dans fiqh-3es.json portent le contenu du livre des WARAQĀT avec le commentaire d'al-Ḥaṭṭāb (uṣūl al-fiqh, enseignement collégial traditionnel) — texte d'intro des deux entrées : « le livre des fondements du droit tiré des Waraqāt de l'imam des Deux Sanctuaires, avec le commentaire d'al-Ḥaṭṭāb » ; figures : Ibn al-Hidda (m. 1197 H.), Ibn Juzayy (m. 741 H.), Ibn al-ʿArabī… ; refs : Qurrat al-ʿayn, Iḥkām al-fuṣūl et al-Ishāra d'al-Bājī, al-Aʿlām de Ziriklī… Le registre usul-fiqh-waraqat (28 entrées 11800-11926, toutes posées) n'a AUCUNE entrée d'annexe → annexes du livre Waraqāt affectées par erreur au registre fiqh-3es (Mukhtaṣar Khalīl/Dardīr).
- DÉPLACEMENT : 12351/12352 retirées de fiqh-3es (→ 30 entrées : pdf-1..28 + pdf-29/30 annexes Khalīl posées en W51 — plus aucun conflit de titres فهرس) et ajoutées à la fin d'usul-fiqh-waraqat (→ 30 entrées, 30 posées). DocIds conservés (liens du lecteur).
- NETTOYAGE consigné : fragment de journal de génération « Lundi 31 décembre 2018 » (<dl><dt></dt><dd>…</dd></dl>) retiré du htmlFr des deux entrées (déchet IA-1/IA-2, sans substance documentaire).
- URLs du site : livres/fiqh-3es/12351.html et 12352.html (HTTP 200 aujourd'hui) deviendront 404 après rendu — contenu faux de livre de toute façon ; le relais : livres/usul-fiqh-waraqat/12351.html et 12352.html. À vérifier après CI.
- AUDIT fiqh-2es consigné : registre = 2 entrées seulement (12164 فهرس الأعلام 16 569 car avec sections imams/traditionnistes/jurisconsultes + 12431 فهرس المصادر 9 147 car) — les annexes de la Risāla 2es sont posées mais la MATIÈRE du milieu manque (registre à compléter : identifier le PDF habous du livre فقه 2es — Risāla d'Ibn Abī Zayd, suite — puis cycle couches→متن→zooms→htmlFr→QA→pose). fiqh-1es : 30/30 conforme (matière + لائحة الأعلام + لائحة المصادر + كتاب الفقه, titlesAr complets avec le nom du livre et du commentaire).

### W52 bis — vérif post-déplacement
- Nouvelles URLs EN LIGNE : livres/usul-fiqh-waraqat/12351.html et 12352.html (HTTP 200, contenu nettoyé — « Lundi 31 décembre » absent, title « Uṣūl al-fiqh — al-Warāqāt d'al-Juwaynī, comm. d'al-Ḥaṭṭāb ») ✓.
- RÉSIDU DE RENDU consigné : le générateur de rendu est add-only — il n'a pas purgé les anciennes pages livres/fiqh-3es/12351.html et 12352.html (encore HTTP 200 avec contenu Waraqāt). Contenu identique et correct, donc aucun risque documentaire ; simple doublon d'URL jusqu'à purge par l'infrastructure. pdf-29/pdf-30 toujours 200 ✓.

## W53 — 2026-11-23 — IA-3 — SOURCE DU LIVRE fiqh-2es RETROUVÉE (236 p., édition ministérielle) + roadmap

- Contexte : le PDF officiel fiqh-3es du registre (…/الفقه-الثالث-إعدادي/26.المصادر_والمراجع.pdf) est DÉSORMAIS 404 — le dossier images/2024 a été retiré de habous.gov.ma (même blocage que W47 l.616 pour الحديث-الثالثة-ثانوي) ; le CMS 2018 (pages leçons 12019/12032/12107…) est mort (404 nginx, CMS refait) ; archive.org bloqué au niveau réseau du bac (ECONNREFUSED, sandbox + fetcher).
- SOURCE RETROUVÉE : la porte « بوابة ابن العربي عتيق » (sites.google.com/view/ibnarabi02, page الفقه-2-إعدادي) héberge le livre sur Google Drive (ID 1d0gjskFIfIgFrFzoiqhB4G3sw21h_AN3, 59 Mo, 236 pages, PDF 1.3 SANS couche texte = scan) — couverture vérifiée visuellement : « الفقه — مرسلة ابن أبي زيد القيرواني بشرح كفاية الطالب الرباني لأبي الحسن — السنة الثانية من التعليم الاعدادي العتيق — كتاب التلميذ والتلميذة » (وزارة الأوقاف). Copie locale : work/fiqh2.pdf + download/fiqh-2-thanawi-2024.pdf (pour l'utilisateur). URL source consignée (leçon du worklog W47 l.618 : journaliser l'URL au téléchargement ✓).
- PÉRIMÈTRE du livre (intro p.5, lue par OCR) : « الزكاة والحج والأضاحي وذبائح أهل الكتاب والأيمان والنذور والنكاح والطلاق وتوابعه » — la 2e moitié de la Risāla ; registre fiqh-2es = 2 annexes posées (12164 فهرس الأعلام 29 figures, 12431 فهرس المصادر 23 entrées) ; la MATIÈRE (~30 leçons sur 236 p.) reste à poser — slots pdf-1..pdf-N à créer en suivant le patron fiqh-3es (pdfOnly:true, pdfUrl → Drive ID consigné).
- PIPELINE : le PDF étant un scan, le cycle des séances suivantes = couches tesseract (work/tessdata/ara + tessdata_best déjà en place) + pdftoppm zooms → découpage leçons (bandeaux الدرس) → traduction → QA double porte → pose → push (clone SPARSE du dépôt désormais utilisé — 25 Mo vs 6,4 G, checkout content/books + worklog).
- SUIVANT : W54 = OCR des bandeaux الدرس sur les 236 pages (découpage définitif du registre) + première leçon complète (la zakāt des denrées, pp.6-8 env.).

## W54 — 2026-11-23 — IA-3 — fiqh-2es : ToC officielle transcrite + MAP DES 28 LEÇONS (scan OCR des 236 pages)

- ToC officielle pp.9-10 (zooms 150 dpi lus) transcrite → download/f2-map/toc-transcribe.md : 34 semaines = 28 leçons réelles + 4 فرض محروس + 1 تقويم تشخيصي + 1 تعزيز — MÊME PATRON que fiqh-3es (28 leçons + annexes).
- Scan OCR tesseract (ara, psm 4, 100 dpi) des bandeaux/أهداف sur les 236 pages → download/f2-map/lessons-scan.json : 96 pages avec hits, 28 débuts de leçons réels (faux positif p.6 = page d'orientation « كيف أستعمل كتابي ») : p.11 زكاة العين والحرث ; p.20 عروض التجارة ; p.27 الدين والمال المستفاد ; p.34 الماشية ; p.42 الخلطاء ; p.50 الظهر ; p.57 أحكام الحج ; p.65 مناسك الحج ; p.73 طواف الإفاضة ورمي الجمار (تتمة) ; p.81 أنواع الإحرام ; p.89 أحكام الأضحية ; p.96 أوقات وآداب الذبح (تتمة) ; p.103 الذكاة ; p.111 طعام أهل الكتاب ; p.118 الأيمان ; p.127 النذر ; p.135 الزواج ; p.145 المحرمات من النساء ; p.153 ما يحرم من الرضاع ; p.159 النفقة ; p.166 أنواع الطلاق ; p.176 الخلع ; p.183 عيوب النكاح ; p.190 الإيلاء والظهار واللعان ; p.199 العدة ; p.206 الإحداد والاستبراء ; p.212 السكنى والنفقة للمعتدة ; p.218 الإرضاع والحضانة والنفقة ; fin de matière p.224+.
- DIVERGENCE consignée : ToC semaine 23 « أحكام الذقّة ونكاح التفويض والتحليل والمحرم والمريض » vs leçon réelle p.159 « حكم النفقة وشروطها » (2 hits OCR concordants pp.158-159) — titres finaux à trancher par zooms des bandeaux réels lors du travail leçon par leçon (les hits des أهداف font foi pour le CONTENU, la ToC pour la NUMÉROTATION du programme).
- pp.6-8 = paratexte (orientation + كفايات تدريس) hors registre ; les leçons réelles démarrent p.11 (ToC semaine 2 — le ToC semaine 1 تقويم تشخيصي n'a pas de leçon imprimée détectée).
- SUIVANT (W54 en séance dédiée) : leçon 1 = pp.11-19 زكاة العين والحرث (9 pages, méthode IA-2 R562 : lectures d'images directes 150-300 dpi + tesseract, le PDF est un scan SANS couche texte) → gabarit fiqh-3es (أهداف/تمهيد/متن/شرح/استخلاص/تقويم/استثمار/إعداد) → pose slot pdf-1 (avant les annexes 12164/12431, registre → 31 entrées) puis leçons suivantes.

## W55 — 2026-11-23 — IA-3 — fiqh-2es : LEÇON 1 POSÉE (pdf-1, « زكاة العين والحرث », pp.11-19, registre → 3 entrées)

- LEÇON 1 LUE ENTIÈREMENT (zooms 150 dpi ×9 pages + micro-zooms 900-1200 dpi) : أهداف ×3 / تمهيد / متن (passage zakāt de la Risāla, pp.11-12, vocalisé) + 4 gloses lexicales / الشرح (حكم الزكاة 2 versets + hadith Bukhārī + ijmaʿ ; الأموال العين-الحرث-الماشية ; شروط وجوب ×6 + إجزاء ×4) / ثانيا أنصبة (Mālik + Mūwaṭṭaʾ ; hadith Muslim 5 awsuq + 653 kg actuels ; ضم الأصناف) / مقادير (hadiths ʿAlī Abū Dāwūd + Musnad Aḥmad ; ʿushr/nadḥ Bukhārī) / ثالثا مقاصد ×4 (droits-adoration, existentiel, éducatif, social + Tawba + hadith Muʿādh) / التقويم ×4 / الاستثمار (al-ʿAdawī 1/511) / الإعداد القبلي ×3.
- TRANCHAGES machine (tesseract 600-1200 dpi + canon shamela 11373/80-81 fetched direct, variante éd. دار الفكر) : (1) titleAr « زكاة العين والحرث » — 4 témoins machine (objectifs ×2 W54+W55, متن, ToC p.9) + canon, contre lecture oculaire divergente du bandeau calligraphique (« العرض ») écartée et consignée ; (2) متن = variante shamela : « والماشية » (non المانحة) , « فليزك ذلك » , « أصناف القطنية » , « والذرة » , « ستة أقفزة وربع قفيز » , « أخرج من زيته » , « ولا زكاة في الفواكه والخضر » , « أعني أن السبعة داننيق » (canon ; le livre ي-lire داننيق/دنانير : retenu canon) ; (3) « الجلجلان وحب الفجل من زبيه » — DIVERGENCE canon (ed. shamela « من زيته ») tranchée par lecture oculaire 1200 dpi (point du ب net) + tesseract z3 : le livre imprime « من زبيه », consigné ; (4) « فمن كان له مائة درهم وعشرة دنانير فليخرج من كل مائة ربع عشره » — canon « من كل مال ربع عشره » : le livre imprime « مائة » (lecture 1200 dpi), consigné ; (5) citations du شرح = متن verbatim (« وزكاة العين والحرث والماشية فريضة » tesseract 1100 dpi — lecture oculaire « المانيبة » écartée) ; (6) RÉSERVE consignée : le fragment canonique « في نبات الحواشي… من غير كلفة ولا في الثمار المائلة لحصادها » entre « ولا زكاة » (fin p.11) et « من الحب والتمر » (p.12) non confirmé lettre à lettre (transition inter-pages non lue au niveau requis) — htmlFr rend le passage conservateur sans ce fragment.
- DEUX COQUILLES CORANIQUES DU TIRAGE corrigées documentées INLINE (pattern corpus) : renvoi « [سورة البقرة الآية 42] » pour « وأقيموا الصلاة… » (réel 43) ; renvoi « [سورة التوبة الآية 104] » p.13 pour « مَثَلَ الَّذِينَ يُنفِقُونَ أَمْوَالَهُمْ… » (réel البقرة 261 — le 104 se rapporte au verset « خذ من أموالهم صدقة… » cité p.17, renvoi là aussi imprimé 104 pour le réel 103) ; le muṣḥaf du livre imprime « مِئَةُ حَبَّةٍ » (muṣḥaf : مِّائَةُ) — orthographe du tirage consignée.
- POSE : fiqh-2es.json → [pdf-1, 12164, 12431] (leçons avant annexes, patron fiqh-3es) ; pdfUrl = URL Google Drive du livre (ID 1d0gjskFIfIgFrFzoiqhB4G3sw21h_AN3, consignée W53) ; pdfOnly:true ; htmlFr 18 286 car (h1 + 7 h2 + 3 h3 + 5 h4 + 33 p + 19 li) ; hand-set.py : registre savants 1242 → 1243 ; miroir /home/z/my-project/content/books/ (layout HOME du hand-set) restauré et resynchronisé vers le repo avant commit.
- QA : interne (0 arabe, guillemets 24/24, 0 apostrophe droite, balises appariées) + verify-f2-l1.py créé : 27/27 PASS (structure, mutun, 5 awsuq/60 ṣāʿ/20 dinars/200 dirhams/quart de centaine, 2 renvois coraniques corrigés, hadiths pilier+quart dîme+ʿushr/nadḥ+Muʿādh, Mālik/Muwaṭṭaʾ, 653 kg, ʿAdawī 1/511, maqṣirī, ʿatharī, glossaire متن, conditions 6+4, ouverture leçon 2).
- ENVIRONNEMENT : recycle du sandbox en cours de séance — repo-417 re-cloné SPARSE (content/books + scripts-translate + worklog, ~30 Mo) ; fiqh2.pdf + lessons-scan.json + toc-transcribe.md survivus.

## W56 — 2026-11-24 — IA-3 — fiqh-2es : LEÇON 2 POSÉE (pdf-2, « زكاة عروض التجارة », pp.20-26, registre → 4 entrées)

- LEÇON 2 LUE ENTIÈREMENT (150 dpi ×7 pages + 14 microcrops 900-1200 dpi + 12 requêtes snippets) : أهداف ×3 / تمهيد / متن (passage عروض التجارة de la Risāla pp.20-21, vocalisé, avec ellipse « (…) » réelle du tirage) + 4 gloses lexicales / الشرح (أولا العروض التجارية : القنية/المحتكر/المدير + hadith Samura Abū Dāwūd ; ثانيا كيفية الإخراج : procédure chiffrée 40000+10000+70000−10000 + حول الأرباح وَحَوْلُ رِبْحِ المالِ حَوْلُ أَصْلِه + exemple سلفة 10000→40000) / ثالثا مراعاة الإسلام ×3 / مقاصد (الخالق والخلوق + مستخلفون + مقصد الجود) / التقويم ×3 / الاستثمار al-Qayrawānī [الخلاصة الفقهية لمحمد العربي القروي 1/186] / الإعداد القبلي ×3.
- TRANCHAGES machine : متن = canon de la Risāla confirmé par 5 témoins snippets + zooms 1200 dpi : « فإذا بعثها بعد حول فأكثر من يوم أحْدَثْتَها أو زَكَّيْتَها، فهي فيها الزكاة لحول واحد » ✓ ; « إلا أن تكون مديرًا لا يستقر بيدك عين ولا عرض، فإنك تقوّم عروضك كل عام وتزكي ذلك مع ما بيدك من العين » ✓ ; « حسب بذاته فيها بيده » ✓ ; « ولا يسقط الدين زكاة حب ولا تمر ولا ماشية » ✓ (3 témoins) ; الشرح : « عروض القنية بضم القاف وكسرها أي الاقتناء » ✓ (2 témoins habous.gov.ma — éd. en ligne du MÊME manuel retrouvée) ; « وصاحبها إما مدير وإما محتكر » ✓ ; « وقبض الثمن وأن يكون الثمن عينا... بعروض أخرى » ✓ ; « ومستخلفون فيه » ✓ ; « وبذله لمن هو في حاجة إليه » ✓ ; « بمثال المعين في الموضوع » ✓ ; « بمتن الرسالة » ✓ ; « أوقات أداء » ✓ ; « القنية-الرباع-الحلي » ✓.
- COQUILLES DU TIRAGE consignées + corrigées INLINE : (1) « سيزكي 11000 درهم أي : 120000 − 10000 = 11000 » = coquille arithmétique ×2 (le correct = 110000, vérifié par code) ; (2) « الحنف » ×2 (pp.22-23) pour « خليل » (le متن cité = celui de Khalīl) ; (3) hadith Samura « نُعدُّه للنَّبيع » pour le canon « نعد للبيع » (2 témoins) ; (4) « ياطع حكم المتوع » pour « يأخذ حكم المتوابع » ; « العدوم يبْطئ » (canon يمنع, variante consignée) ; (5) fragment p.24 « فجبند نافذُه الزكاة » dégradé → canon probable « فتضم إلى بذاته الزكاة » ; (6) « فمجمم الجمع الإدارة » dégradé (canon probable فأثَّل الجماع الإدارة) ; (7) « فريه » pour « فرضًا » ; (8) « زَكَي رِبَهُ » pour « زُكِّيَ ربحُه » ; (9) glose « عقار : دار » (le متن = « عقار » — la forme « رِبَاع » du tirage consignée) ; (10) renvoi « باب ما يجِب فيه الزكاة » ✓ net au zoom (le يجيب du 150 dpi = bruit).
- POSE : fiqh-2es.json → [pdf-1, pdf-2, 12164, 12431] ; titleAr « زكاة عروض التجارة » (bandeau p.20 + numéro 2 + map W54 p.20 concordants) ; pdfUrl = même Drive que pdf-1 ; htmlFr 13 421 car (h1 + 7 h2 + 3 h3 + 2 h4 + p/ul/ol/li équilibrés) ; hand-set registre savants (1243).
- QA : interne + verify-f2-l2 (0 arabe, guillemets 6/6, 0 apostrophe droite, ellipses متن conservées, 15/15 PASS) + ARITHMÉTIQUE vérifiée par code (40000+10000+70000=120000 ✓ ; 120000−10000=110000 ✓ ; 40000−10000=30000 ✓).
- ENVIRONNEMENT : shamela.ws derrière Cloudflare ce tour (résolu par snippets ×12) ; habous.gov.ma 404 au fetch (comme W47, snippets utilisés) ; work/lessons-scan.json + toc-transcribe.md perdus au recyclage (récupérés du worklog W54 committé).

## W57 — 2026-11-24 — IA-3 — fiqh-2es : LEÇON 3 POSÉE (pdf-3, « زكاة الكبير والمال المستفاد », pp.27-33, registre → 5 entrées)

- LEÇON 3 LUE ENTIÈREMENT (150 dpi ×7 pages + 10 microcrops 900-1600 dpi + 6 requêtes snippets) : أهداف ×3 / تمهيد (3 catégories de biens : reviennent/merités/profités) / متن (Risāla : dettes pp.27 + mineurs-minéraux-héritages p.28, vocalisé, avec ellipses d'édition « … » ×2 : passage sur l'esclave omis + tronçon ميراث conservé) + 3 gloses (القنية/الرباع=الدور والأراضي/الأصاغر=غير البالغ) / الشرح (أولا الدين والمستفاد : définitions + moment + 4 applications dont 15000+20000=35000 ; ثانيا المغصوب والمعادن et الأصاغر avec Muwaṭṭa' ×3) / حكمة ربط الزكاة بالوقت ×3 / التقويم ×4 / الاستثمار al-ʿAdawī [حاشية العدوي على كفاية الطالب الرباني 1/431] / الإعداد القبلي ×3 (نور-جدعة-ثنية-بتت مخاص = termes de la L4).
- CANON TRANCHÉ : متن = canon دار الفكر confirmé par snippets (p.338 !) : « من ورث عرضا أو وهب له أو رفع من أرضه زرعا فزكاه... حتى يباع ويستقبل به حولا من يوم يقبض ثمنه » ✓ (3 témoins) ; « وفيما يخرج من المعدن... عشرين دينارا أو خمس أواق فضة ففي ذلك ربع العشر يوم خروجه » ✓ (3 témoins) ; « وعلى الأصاغر الزكاة في أموالهم في العين والحرث والماشية وزكاة الفطر » ✓ (5 témoins) ; « ولا زكاة عليه في دين حتى يقبضه » (2 témoins) vs le TIRAGE « حَتَّى يَقْضَه... بما يقضيه منه » = variante d'édition ×2 consistante (contexte dette, consignée) ; Muwaṭṭa' : « ومن أفات ذهبا أو ورقا » ✓ + « السُّنَّة عندنا أنه لا تجب على وارد » ✓ + « كُنت أنا وأخا لي يتيمين في حجر عائشة فكانت تخرج من أموالنا الزكاة » ✓ (canon).
- COQUILLES DU TIRAGE consignées : (1) « خَمْسَةَ أَوَاقٍ » vs canon « خمس أواق » ×3 ; (2) « فَفي ذلك رُبْعُ العُشْرِ » = canon ✓ (la lecture 150 dpi « فَيَى » était du bruit) ; (3) « للثُّيَاسِ من الحُلِّيِّ » vs canon « للباس من الحلي » (variante consignée) ; (4) « ويستقبِلَ... يقبض ثمنه » = canon ✓ (mes lectures « ويستقيل/يقضيه » du bruit) ; (5) « زَرْعًا فَزَكَاهُ » = canon ✓ (« عَزَقَاهُ » du bruit) ; (6) « فكانت نخرج » → canon « تُخرِج » ; (7) « مُتَّخَذًا للعافية » (canon العدوي « بنية التجارة... ») ; (8) fragments p.27 تمهيد (تعيب) + p.29 (عليه فيها بيده/المحوط/غلته) + p.32 مقاصd (دإشعار/لييادير/تبييرا/يدانون/يُعَظَّى/يتتين/والجانين/السنة كلها) + p.33 fin العدوي : dégradés → rendus par le SENS avec N.d.T. (11 arbitrages) ; (9) « آفات » Muwaṭṭa' = « أَفَاتَ » ✓ ; renvoi « باب زكاة أموال اليتامى » ✓ ; « باب الزكاة على أصناف » consigné tel quel.
- POSE : fiqh-2es.json → [pdf-1, pdf-2, pdf-3, 12164, 12431] ; titleAr « زكاة الكبير والمال المستفاد » (bandeau p.27 + numéro 3 + map W54 concordants) ; htmlFr 13 861 car (h1 + 7 h2 + 2 h3 + 8 h4 + 4 applications chiffrées) ; hand-set registre (1243).
- QA : interne + verify (0 arabe, guillemets 11/11, Muwaṭṭa' ×3, al-ʿAdawī 1/431, ellipses conservées, 15/15 PASS) + ARITHMÉTIQUE vérifiée par code (15000+20000=35000 ≥ seuil 20 dinars ✓).
- ENVIRONNEMENT : canon darulfikr retrouvé par snippets (p.338 de متن الرسالة دار الفكر = l'édition de référence du corpus ✓) ; p.34 (L4) extraite non lue (économie) ; borne L3/L4 confirmée par map W54 + إعداد L3 (les termes نور/جدعة/ثنية/بنت مخاض).
## W58 — 2026-11-24 — IA-3 — fiqh-2es : LEÇON 4 POSÉE (pdf-4, « زكاة الماشية », pp.34-41) + réparation du registre IA-3

- LECTURE ET RÉDACTION TERMINÉES (150 dpi ×8 pages pp.34-41 + microcrops 900-1600 dpi + snippets canon) : htmlFr FR-seule 17 157 car QA double porte PASS (0 arabe, 0 marqueur, arithmétique vérifiée par code : 17 ناقة→3 brebis ; 200 بقرة→5 مسنّة ; 80→2 ; 60→2 tabiʿ). Structure conforme L1-L3 (work/f2-l3/part1.html : h1 → objectifs → intro → متن+glossaire → extraction → analyse h3/h4 → مقاصد → تقويم → إعداد → préparation).
- CONTENU COUVERT : متن pp.34-35 (أنصبة الإبل/البقر/الغنم + الأوقاص + جمع الأنواع) rendu intégralement ; tables du manuel ×3 (أنصبة الإبل 11 rangées p.38 ; البقر 30/40 p.39 ; الغنم 40→per 100 p.39) ; glossaire ×9 (pp.35-36) ; شرح (سائمة/بحت/عرب/متهما p.37 + ضم البخت للعرب + الجواميس/الأبقر + الضّان/العِز p.37b) ; المقاصد (p.40, يتجلّى ×3) ; التقويم ×4 (bas p.40 + haut p.41) ; الاستثمار Ibn ʿArafa [المختصر الفقهي 1/523] ; أتأمل ×2 ; أسئلة الاستعداد (الخضان/السخلة/الفصال + الخلطة + المواشي non soumises → L5).
- ARBITRAGES L4 consignés (7) : (1) canon darulfikr tranché par snippets : « ففيها شاة جذعة أو ثنية من جل غنم أهل ذلك البلد من ضان أو معز إلى تسع » (×3 témoins), « ثم في ست وسبعين بنتا لبون إلى تسعين، ثم في إحدى وتسعين حقتان إلى عشرين ومائة » (×8 témoins — « بنتا لبون » ≠ « تسعة لبون »), « والبخت والعِراب » (شرح حطاب) ; (2) variantes du tirage consignées : p.34 « الأَيِّلُ في الخامسة » (canon « الإبلُ »), « فيقيها » (canon « ففيها » ×3), p.37 « والجواميسُ والأَبِقَرُ » (canon « والبَقَرُ ») rendue telle quelle ; (3) table الغنم p.39 rangée 301-399 → 3 brebis (hadith d'Anas) vs متن « فما زاد ففي كل مائة شاة » — divergence rendue avec N.d.T. ; (4) citation متن p.39 « عجل جدَّع قد أوفى سنتين » vs متن p.35 « عجل جَدَّ قد أوَّى في سنتين » — rendue selon p.35, variante consignée ; (5) p.37 « سواء أكانت بحتًا أم عربًا أو متهما » rendu par le contexte du manuel (doctrine سائمة/الحمول/العين/البخت = L5) — à re-vérifier contre le شرح à la pose L5 ; (6) âges à la convention « dans sa Nᵉ année » d'après les glosses du manuel (بنت مخاض = 2 accomplis ; بنت لبون = 3ᵉ ; حِقة = 4ᵉ ; جذعة = 5ᵉ) ; (7) مثال عددي du التقويم (70 شاة / 200 بقرة / 17 ناقة) laissé non résolu dans le html (question d'évaluation) ; réponses vérifiées par code : 1 brebis / 5 مسنّة / 3 brebis.
- ENVIRONNEMENT : recyclage sandbox en fin de session — clone/PAT perdus APRÈS rédaction (REPRISE-W58) ; POSÉE PAR LA SESSION W59 SUIVANTE depuis le re-clone (consignée REPRISE-W59). Garde-doublon R622 re-vérifiée à la reprise (2026-11-26) : htmlFr pdf-4 sur origin = la rédaction de cette session au caractère près (diff 9 lignes = vides finales) — aucun doublon, aucun écrasement, la pose fait foi ; le commit journalisé est bcd7069 « IA-3 : fiqh-2es leçon 4 posée : pdf-4 … » (REPRISE-W59 notait 0ab8dd1 en local ; le hash poussé diffère — rebase probable — le contenu lui-même est identique) ; CI verte, page en ligne savante.
- REGISTRE IA-3 RÉPARÉ (dette de traçabilité, 2026-11-26) : les mises à jour du registre IA-3 annoncées par les sessions W55-W72 (« registre → 3/4/5… 19 entrées ») n'ont JAMAIS atteint origin (recyclages successifs) — origin ne contenait que fiqh-3es/pdf-1..14 (14 entrées). Ce commit ajoute fiqh-2es/pdf-1..pdf-19 (19 docIds qualifiés — 19 commits IA-3 vérifiés au journal git : 7210c4a W55 L1, 406fb39 W56 L2, d72d30f W57 L3, bcd7069 L4, 927df8d L5, 4c1a01a L6, d20fdd8 L7 (+dded336 fix QA), 00763cd L8, 6e4d42d L9, 43a95f6 L10 … 4e4c477 W72 L19) → badge « Par IA-3 » restauré sur les 19 pages ; registre IA-3 → 33 entrées. La couche savante effective (registre fait foi) était déjà correcte — aucun changement de contenu.
- SUIVANT : L5 « زكاة الخطاء » (pp.42-44 déjà lues en W59, REPRISE-W59) puis leçons 5-28 de la map W54 ; re-vérifier l'arbitrage (5) contre le شرح à la pose L5.

## W59 — 2026-11-24 — IA-3 — fiqh-2es : reprise post-recyclage — POSE pdf-4 exécutée (commit bcd7069, push rétabli ultérieurement) + début L5

- RE-CLONE PUBLIC rétabli (lecture sans auth) ; origin/main = ed101af à l'époque (la branche IA-2 avait poussé hadith-6ep leçon 21 entre-temps) — pas de collision sur le slot pdf-4 (convention R622 respectée).
- POSE pdf-4 exécutée d'après REPRISE-W58 (procédure 5 étapes) : couche préparatoire du slot remplacée par la rédaction savante 17 157 car ; ordre [pdf-1, pdf-2, pdf-3, pdf-4, 12164, 12431] ; titleAr « زكاة الماشية », titleFr « La zakāt du bétail (les troupeaux) » ; commit local 0ab8dd1 consigné — poussé ultérieurement sous bcd7069 (contenu vérifié identique).
- PUSH initialement BLOQUÉ (PAT jamais stocké — R103) ; vérifié poussé sur origin à la reprise du 2026-11-26 : CI « Rendu du site » verte, livres/fiqh-2es/pdf-4.html en ligne, statut savant correct (badge « Par IA-3 » restauré le même jour — voir W58, registre IA-3).
- L5 « زكاة الخطاء » : pp.42-44 LUES (suite en cours) — à terminer puis poser à la prochaine vague ; artefacts de rejeu dans download/f2-map/ (REPRISE-W58/W59, patches, toc-transcribe.md, lessons-scan.json).
