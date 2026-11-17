# PROTOCOLE DE TRAVAIL À DEUX IA NON CONNECTÉES — Minhāj

> Rédigé par l'IA-2 (Z.ai, compte parallèle), 12 nov. 2026, trace `1a1cf6f735b99afd`.
> Complète le protocole de début de session du `worklog.md` (règle utilisateur du 24 oct. 2026).
> Les deux machines ne peuvent pas se parler. La seule chose qu'elles partagent,
> elles la partagent déjà : **le dépôt GitHub**. Le protocole repose uniquement là-dessus.

---

## 1. Principe de base : GitHub = source de vérité unique (inchangé)

```bash
bash /home/z/my-project/scripts-recovery/session-start.sh   # à CHAQUE début de session
git pull --rebase origin main                               # avant CHAQUE push
git push origin main                                        # après CHAQUE leçon livrée
```

Règle de vague inchangée : **1 leçon livrée = 1 commit + push + backup + entrée de journal**.
Jamais plus d'une leçon non poussée. En cas d'échec push (token absent) : commit local +
bundle de sûreté + consignation dans son journal — ne jamais accumuler.

## 2. Le partage : des ZONES statiques, pas des claims dynamiques

Deux machines qui ne se connaissent pas ne peuvent pas se disputer les tâches en temps réel.
On supprime donc le besoin de coordination : **le périmètre de chacune est figé par type de
travail et par niveau scolaire**, de sorte qu'aucun fichier ne soit jamais édité par les deux.

| Zone | IA-1 (session principale, série R) | IA-2 (compte parallèle, série Z) |
|---|---|---|
| **Type de travail** | Extraction PDF → leçons intégrales (pipeline VLM, adjudications, registre) | Révision/qualification FR, QA corpus, tâches app (À propos, export, navigation) |
| **Niveaux** | **collège (es) + lycée (tanawi)** | **primaire (1ep → 6ep, 17 livres)** |
| **Journal** | `worklog.md` (série R, GARDE-DOUBLON) | `worklog-ia2.md` (série Z) |
| **Scripts** | `scripts-translate/`, `scripts-recovery/` | `scripts-ia2/` (namespace séparé) |

Le partage demandé par l'utilisateur (« tu prends le niveau 4 ou 5 du primaire, l'autre prend
le collège ») est élargi en **primaire entier vs secondaire entier** : c'est plus simple à
retenir, et c'est déjà la réalité du terrain (IA-1 est engagée sur `hadith-3es`, front collège).

- IA-1 ne touche **aucun** fichier `content/books/*-ep.json` ni le journal de l'IA-2.
- IA-2 ne touche **aucun** fichier `content/books/*-es.json`, `*-tanawi-*.json`, ni `worklog.md`,
  ni la queue de traduction de IA-1 (`content/agent-queue.json`).
- Si l'une voit un défaut dans la zone de l'autre : **interdit de corriger**. On le consigne
  dans son propre journal (une ligne, livre + docId + symptôme). Le propriétaire corrige.

## 3. Granularité : niveau / livre / document

Trois niveaux, trois usages :

1. **Le niveau scolaire** (4ep, 5es, tanawi-2…) sert à **l'attribution statique des zones** (§2).
   Il ne bouge pas en cours de route. Fini les questions « qui fait quoi ».
2. **Le livre** (`content/books/<id>.json`) est l'**unité de réclamation (claim)**. Avant de
   commencer une passe sur un livre, on vérifie dans l'historique git qu'aucun claim actif
   ne le concerne : `git log --oneline -30 -- content/books/<id>.json` + grep `claim`.
   La réclamation se pose **dans le message de commit** du premier travail sur le livre :
   `claim <bookId> (trace <trace-id>-zN-main)` — même convention que les slots PDF de IA-1.
3. **Le document** (leçon ou intro, `docId`) est l'**unité de livraison** : vague de 1 à 4
   documents par commit maximum (règle de vague), QA avant chaque livraison
   (`scripts-translate/qa-lesson.py` sur le doc, ou `scripts-ia2/qa_corpus.py` pour un scan
   global), commit + push immédiat.

## 4. Coordination asynchrone (les deux machines avancent à des rythmes différents)

Ça ne pose **aucun** problème tant que les zones sont disjointes. Les seuls points de contact :

- **`worklog.md`** : IA-1 l'append à chaque leçon. IA-2 **ne l'écrit jamais** → zéro conflit.
  La queue de worklog reste l'autorité de priorité pour IA-1 ; le tail de `worklog-ia2.md`
  est l'autorité pour IA-2.
- **`savant-registry.json`** : les deux peuvent y ajouter des docIds. Conflit possible mais
  trivial : en cas de rebase conflictuel, on résout en **ré-ajoutant uniquement SES docIds**
  sur la version distante fraîche (jamais en supprimant ceux de l'autre). IA-2 pousse ses
  mises à jour de registre **par livre terminé**, pas par leçon, pour limiter les collisions.
- **`content/manifest.json` / `source-tree.json`** : régénérés seulement si la structure des
  livres change (ajout/suppression de leçons). La révision de `htmlFr` ne les touche pas.
- **Push en concurrence** : si le push est refusé (distante en avance), `git pull --rebase
  origin main` puis re-pusher. **Jamais de force-push. Jamais de reset --hard sur la
  distante d'autrui.** Les commits de l'autre IA sont intangibles.
- **Claims périmés** : un claim sans livraison pendant ~50 min peut être repris (takeover)
  en le documentant, convention existante de IA-1.

## 5. Qualité commune (non négociable, les deux IA)

- Typographie FR : apostrophe typographique ’, guillemets « » appariés, NNBSP U+202F avant
  `; : ! ? »` et après `«`, 0 caractère arabe hors `<span dir="rtl" lang="ar">`.
- Hamza de translittération : ʾ (U+02BE) après voyelle longue en fin de mot
  (`yā</em>ʾ`, `šayʾ`) — convention majoritaire du corpus (167 usages vs 37).
- Toute livraison passe `qa-lesson.py` (ou le scan global) **avant** le commit.
- Translittération scientifique des noms propres, registre « savant », jamais de devinette :
  une incertaine = incertaine, consignée comme telle.

## 6. État des zones au 12 nov. 2026 (mesures IA-2, registre vivant `scripts-translate/`)

- **0 document GT restant** dans tout le corpus : les 999 docs avec texte arabe sont savants.
- Primaire : 389 docs FR **entièrement nettoyés typographiquement** (Z1) — 0 défaut dur.
  Restant : 282 leçons `pdfOnly` sans texte (hadith-5ep 29, hadith-6ep 28, usul-qiyam-4ep 25,
  usul-qiyam-5ep 26, usul-qiyam-6ep 25, rasm-wa-dabt-5ep 29, tafsir-5ep 91… PDF locaux
  disponibles pour hadith-5ep/6ep ; géoblocage habous.gov.ma pour les autres).
- Secondaire (zone IA-1) : 805 docs avec défauts typographiques durs (apostrophes droites)
  signalés dans `worklog-ia2.md` entrée Z1 — rapport seul, non corrigé (règle §2).
- Reste du chantier IA-2 : extraction hadith-5ep puis hadith-6ep (PDF locaux), page À propos,
  export/partage, navigation clavier (liste R9 du worklog).
