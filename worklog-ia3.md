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



