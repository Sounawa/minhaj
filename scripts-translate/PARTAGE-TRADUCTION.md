# PARTAGE-TRADUCTION — la carte du partage des 555 leçons (traduction seule)

> Instaurée à la demande du propriétaire (R777, 2026-11-21) : **les trois IA
> font UNIQUEMENT de la traduction** — les commentaires pédagogiques sont
> SUSPENDUS jusqu'à nouvel ordre. Cette carte dit QUI traduit QUOI, COMMENT
> retrouver la matière et COMMENT se rendre visible. Elle est versionnée au
> dépôt (survit aux resets). **Règle h : le tail des worklogs reste
> l'autorité de priorité ; cette carte dit le partage.**

## 1. Le partage (555 leçons restantes, livres ATOMIQUES)

| Zone | IA | Manuels (leçons restantes) | Reste |
|---|---|---|---|
| Lycée | **IA-1** | taqtit-tanawi-3 (30), taqtit-tanawi-2 (29), fikr-islami-tanawi-2 (28), fikr-islami-tanawi-3 (27), qiraat-tanawi-2 (28), qiraat-tanawi-3 (23), ulum-hadith-tanawi-3 (27), hadith-tanawi-3 (11) | **203** |
| Préparatoire | **IA-2** | hadith-6ep (21), rasm-wa-dabt-5ep (29), rasm-wa-dabt-6ep (29), usul-qiyam-4ep (25), usul-qiyam-5ep (26), usul-qiyam-6ep (25) | **155** |
| Secondaire | **IA-3** | tajwid-3es (28), fiqh-3es (27), tafsir-3es (25), usul-fiqh-tanawi-2 (30), usul-fiqh-tanawi-3 (30), tafsir-tanawi-3 (29), fikr-islami-tanawi-1 (28) | **197** |
| **Total** | | 21 manuels | **555** |

Chiffres posés au jour du partage (1227/1782 transcrites, 555 restantes) ;
ils baissent à chaque livraison — la VÉRITÉ du moment se lit dans les
compteurs du site et les worklogs.

Règles de la chaîne :

- **un livre = un propriétaire** — JAMAIS deux IA sur le même livre (0 conflit
  git garanti, chaque livre est un fichier JSON distinct) ;
- au sein d'un livre, les leçons se prennent DANS L'ORDRE (num 1, 2, 3…) ;
- **relais** : quand une IA achève sa zone, elle fait `git fetch`, annonce
  l'achèvement dans son worklog, puis prend le livre restant le PLUS AVANCÉ
  d'une autre zone (du plus proche de l'achèvement au moins avancé) ;
- tout changement de propriétaire se consigne dans cette carte ET dans le
  worklog de l'IA qui prend ET dans celui de l'IA qui rend.

## 2. Le chemin d'accès aux documents (la matière)

**Carte mère : `scripts-translate/SOLUTION-OUVRAGES.md`** (établie R458,
revérifiée R773-R776). Résumé opérationnel :

- Le portail **habous.gov.ma** est FERMÉ (404, arborescence rendue) — ne pas
  compter dessus ; le canari `scripts-translate/veille-portail.sh` sonde son
  retour (état : `tr-logs/pipeline-status.json`, pied de page du site).
- **Route A (principale)** — miroir archive.org : collection
  « سلسلة كتب التعليم العتيق المغربي », item **`1_20220304_20220304_2251`**,
  77 PDF complets (primaire → lycée), versions `_text` avec couche OCR :

  ```bash
  # liste des fichiers (cache 24 h : tr-logs/collection-files.json)
  curl -s https://archive.org/metadata/1_20220304_20220304_2251
  # téléchargement d'un manuel (atomique, vérifier l'en-tête %PDF-)
  curl -L -o content/textbooks-src/<slug>.pdf \
    "https://archive.org/download/1_20220304_20220304_2251/<fichier-url-encodé>.pdf"
  ```

- **45 manuels DÉJÀ en dépôt** : `content/textbooks-src/*.pdf` (versionnés) —
  vérifier AVANT tout téléchargement ; le manuel acquis est la source de vérité.
- **Route B** (auxiliaire) : `page_reader` de la SDK côté backend — atteint
  web.archive.org pour les arbres/TDM, PAS les PDF binaires.
- **Route C** (gratuite) : doublons URL-exacts entre livres — renvoi de
  référence, 0 téléchargement (doctrine prouvée, tafsir-5ep 768-797).
- **Superviseur** : `scripts-translate/supervisor.py` (v4, relancé par
  `ensure-supervisor.py` préfixé à `bun run dev`) — sa boucle `hunt_sources()`
  sonde toutes les 30 min : portail → Wayback → collection archive.org, et
  télécharge atomiquement dans `content/textbooks-src/`.

## 3. La signature — VISIBILITÉ des IA (exigence du propriétaire)

Chaque IA est visible sur TROIS plans :

1. **Sujet de commit préfixé** : `IA-1 : Rxxx …` / `IA-2 : Rxxx …` /
   `IA-3 : Rxxx …` — la page Avancement (« Dernières livraisons des trois
   IA ») colore chaque livraison à son agent. Le legacy est reconnu :
   `Z2-*` = IA-2 (59 commits rétro-classés), `W2*` = IA-3.
2. **Registre d'attribution par leçon** — à chaque leçon livrée, ajouter
   l'id qualifié `livre/docId` au registre de SON IA :
   - IA-2 : `scripts-ia2/savant-registry-ia2.json` (déjà en usage, 36 ids) ;
   - IA-3 : `scripts-ia3/savant-registry-ia3.json` (créé R777) ;
   - IA-1 : le registre principal `scripts-translate/savant-registry.json`
     fait foi (miroir racine interdit) ;
   le badge « **Par IA-x** » de chaque page de leçon est rendu par
   `build-site.py` à partir de ces registres (défaut IA-1).
3. **Worklog de l'IA** — entrée à chaque tour : `worklog.md` (IA-1),
   `worklog-ia2.md` (IA-2), `worklog-ia3.md` (IA-3), format
   `## Rxxx — date — IA-x` + trace de session.

## 4. La méthode d'extraction (identique pour les trois IA)

SOLUTION-OUVRAGES.md §4 : carte d'alignement leçons↔pages du manuel **par
ORDRE** (vérifiée contre le registre anti-doublon avant toute extraction) ;
`pdftotext` page par page AVANT tout crop ; zones corrompues → inversion bbox
RTL par coordonnées ; VLM déclassé (dernier recours, arbitrage canonique) ;
**doctrine FR-seule** (0 caractère arabe dans la couche FR, 0 apostrophe
droite, guillemets appariés) ; livraison : JSON du livre + `hand-set.py`
(registre) + QA navigateur 1280/390.

## 5. La discipline git (les trois IA)

- **R109** : `git fetch` du main AVANT toute reprise et tout push ; après
  chaque fetch, `rm -f .git/tmp_pack_*` (disque — incident R776) ;
- pousser RÉGULIÈREMENT (une leçon ou une petite vague par commit) ; jamais de
  force-push ; si le push est refusé (non-fast-forward) : fetch → rebase sur
  origin/main → re-pousser ;
- ne JAMAIS toucher aux fichiers des autres zones : books JSON hors de son
  périmètre, registres d'autrui, `scripts-ia2/` (IA-2), `scripts-ia3/` (IA-3) ;
- l'orchestration du site (`scripts/build-site.py`, CI, compteurs, index,
  recherche) reste à IA-1 — les autres IA proposent en worklog, IA-1 applique ;
- identité git : « Z User <z@container> » ; le token GitHub est fourni par le
  propriétaire dans la conversation (ne JAMAIS le committer dans un fichier).

## 6. Ce qui est SUSPENDU (jusqu'à nouvel ordre du propriétaire)

- les commentaires pédagogiques (s-commentaires, vagues de commentaires) ;
- toute retravaillée du site hors nécessité de build.
- La mission annexe habous (veille, chasse de sources) reste AUTONOME
  (superviseur) — elle n'empiète pas sur les zones de traduction.
