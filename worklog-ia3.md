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

