# PROTOCOLE DE TRAVAIL À TROIS IA NON CONNECTÉES — Minhāj

> Rédigé par l’IA-1 (session principale, série R), 17 nov. 2026, tour R716,
> sur demande explicite de l’utilisateur : « donner des instructions aux deux
> autres IA… la répartition des tâches pour que ni toi ni elles viennent faire
> un doublon ou empiéter sur le travail qu’une autre fait ».
> Remplace le PROTOCOLE-DEUX-IA.md (laissė en place pour l’historique) — les
> règles qui y étaient valables le restent, élargies à trois machines.

---

## 1. Principe de base — inchangé : GitHub = source de vérité unique

```bash
bash /home/z/my-project/scripts/session-start.sh   # à CHAQUE début de session (déplacé de scripts-recovery/)
git pull --rebase origin main                      # avant CHAQUE push
git push origin main                               # après CHAQUE livraison
```

Règle de vague : **1 livraison = 1 commit + push + entrée de journal**.
Jamais plus d’une livraison non poussée. Échec push (token) : commit local +
consignation dans son journal — ne jamais accumuler. **Jamais de force-push.
Jamais de reset --hard sur la distante d’autrui.** Les commits des autres IA
sont intangibles.

## 2. Les ZONES — figées par type de travail et par niveau scolaire

Trois machines qui ne se parlent pas : le périmètre de chacune est figé pour
qu’**aucun fichier ne soit jamais édité par deux IA**.

| Zone | IA-1 (session principale, série R) | IA-2 (compte parallèle, série Z) | IA-3 (nouvelle) |
|---|---|---|---|
| **Mission** | **Commentaires pédagogiques** de chaque leçon (mission spéciale de l’utilisateur) + site : build, style, accueil, QA, publication | Transcription-extraction PDF → leçons intégrales (pipeline VLM) sur le **primaire** | **Secondaire (collège + lycée)** : correction typographique du rapport Z1, puis transcription-extraction si PDF disponibles |
| **Fichiers de contenu** | `content/commentaires/**` (exclusif) | `content/books/*-ep.json` (primaire) | `content/books/*-es.json`, `content/books/*-tanawi-*.json` |
| **Outils/scripts** | `scripts/build-site.py`, `scripts/site-style.css`, `scripts/qa-*.py`, `scripts/session-start.sh`, `site/`, racine publiée, `savant-registry.json` (miroir racine) | `scripts-ia2/` + `scripts-ia2/savant-registry-ia2.json` | `scripts-ia3/` (à créer si besoin) ; écrit ses ids faits main dans `scripts-translate/savant-registry.json` via `hand-set.py` |
| **Journal** | `worklog.md` (série R, append-only) | `worklog-ia2.md` (série Z) | `worklog-ia3.md` (série W, à créer) |

**Interdits absolus pour tout le monde :**
- Modifier un `content/books/*.json` hors de SA zone (et l’IA-1 ne touche à
  AUCUN livre : sa mission commentaires est en lecture seule sur les livres) ;
- Toucher `content/commentaires/` (IA-1 seule) ;
- Toucher `scripts/build-site.py`, `scripts/site-style.css`, `site/` ou les
  fichiers publiés à la racine (IA-1 seule) ;
- Toucher le journal d’une autre IA ;
- Supprimer ou réécrire des commits d’une autre IA.

Défaut vu dans la zone d’une autre : **interdit de corriger** — une ligne dans
son propre journal (livre + docId + symptôme). Le propriétaire corrige.

## 3. Granularité : niveau / livre / document

1. **Le niveau scolaire** fige les zones (§2) — ne bouge pas en cours de route.
2. **Le livre** = unité de claim : avant une passe, `git log --oneline -30 --
   content/books/<id>.json` + grep `claim` ; le claim se pose dans le message
   du premier commit sur le livre : `claim <bookId> (trace <trace-id>)`.
3. **Le document** (`docId`) = unité de livraison : vague de 1 à 4 documents
   par commit maximum, QA avant chaque livraison (`scripts-translate/
   qa-lesson.py` sur le doc, ou `scripts-ia2/qa_corpus.py` en scan global,
   `scripts/qa-liens.py` + `scripts/qa-onglets.py` pour le site), commit +
   push immédiat. Un claim sans livraison ~50 min peut être repris (takeover)
   en le documentant.

## 4. Points de contact et conflits triviaux

- **Journaux** : chacun append dans le SIEN. `worklog.md` reste l’autorité de
  priorité IA-1 ; tail de `worklog-ia2.md` / `worklog-ia3.md` pour les autres.
- **Registres savants** : IA-2 pousse au sous-registre `scripts-ia2/
  savant-registry-ia2.json` par livre terminé ; IA-3 écrit dans
  `scripts-translate/savant-registry.json` (via hand-set.py) par livre terminé.
  En cas de conflit de rebase : ré-ajouter uniquement SES ids sur la version
  distante fraîche, jamais supprimer ceux de l’autre. Le miroir racine
  `savant-registry.json` est resynchronisé par l’IA-1 seule (publication).
- **`content/manifest.json`** : IA-1 seule, seulement si la structure des
  livres change.
- **Push en concurrence** : `git pull --rebase origin main` puis re-pusher.

## 5. Qualité commune (non négociable)

- Typographie FR : ’ typographique, « » appariés, U+202F avant `; : ! ? »`
  et après `«`, 0 caractère arabe hors `<span dir="rtl" lang="ar">`.
- Hamza de translittération : ʾ (U+02BE) après voyelle longue en fin de mot ;
  ʿ (U+02BF) pour le ʿayn — convention majoritaire du corpus.
- Toute livraison passe sa QA avant commit. Registre « savant », jamais de
  devinette : une incertaine = incertaine, consignée comme telle.
- Pour l’IA-1 : schéma et règles de rédaction des commentaires — voir
  `content/commentaires/LISEZ-MOI.md`.

## 6. Hygiène du dépôt (nouveau — demande utilisateur « nettoyage »)

- **Interdiction de committer des fichiers temporaires** à la racine du dépôt
  (les tr-ttmp-*.ts, tr-tmp/… du passé sont supprimés en R716-a). Les temps de
  travail vont dans `<namespace>/tmp/` (ex. `scripts-ia2/tmp/`,
  `scripts-ia3/tmp/`) — non suivi git grâce au `.gitignore`.
- `.gitignore` : `__pycache__/`, `*.pyc`, `tr-tmp/`, `tr-logs/`,
  `qa-shots-onglets/`, `*.tmp`.
- Ce qui est périmé se supprime, consigné au journal (R716-a : tr-tmp 1,1 Go,
  scripts-recovery, tessdata, png QA internes, tailwind.config.ts…).

## 7. État des fronts au 17 nov. 2026 (mesures R716)

- Transcription : **1 202 / 1 782 leçons** (+ 64 intros savantes = 1 266
  documents savants, 100 % des documents traduits ont passé le cap savant).
- Restent sans aucune traduction : **580 leçons** (slots pdfOnly) :
  409 au secondaire (zone IA-3), 171 au primaire (zone IA-2 — dont
  hadith-5ep 9, hadith-6ep 28, usul-qiyam-4/5/6ep 25/26/25,
  rasm-wa-dabt-5/6ep 29/29).
- Commentaires pédagogiques : **2 / 1 782** (pilote hadith-3es 413-414).
- PDF locaux disponibles : hadith-5ep, hadith-6ep ; géoblocage habous.gov.ma
  pour les autres (demander les PDF à l’utilisateur si besoin).
