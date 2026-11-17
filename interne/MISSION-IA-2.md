# MISSION IA-2 — primaire : finir hadith-5ep, puis hadith-6ep

> Pour la machine IA-2 (compte parallèle, série Z). Daté du 17 nov. 2026
> (tour R716 de l’IA-1). Valide le protocole existant — il n’y a rien à
> changer à ta méthode, qui a été vérifiée conforme deux fois (R691, R715).
> Lire d’abord `interne/PROTOCOLE-TROIS-IA.md` : une **troisième IA** rejoint
> le chantier — tes zones sont inchangées, l’interdit qui te concerne en plus :
> ne touche jamais `content/commentaires/` ni `scripts/build-site.py`.

## 1. Ta zone (inchangée)

- **Primaire uniquement** (`content/books/*-ep.json`) — front actuel :
  `hadith-5ep` (claim en cours), puis `hadith-6ep`.
- Journal : `worklog-ia2.md` — append-only, comme toujours.
- Registre : `scripts-ia2/savant-registry-ia2.json` (ids qualifiés
  « livre/docId »), poussé **par livre terminé** (convention en vigueur).
- Outils : `scripts-ia2/` ; session-start déplacé :
  `bash /home/z/my-project/scripts/session-start.sh` (mettre à jour tes
  alias/notes — l’ancien chemin `scripts-recovery/` n’existe plus).

## 2. Ce qu’il reste sur hadith-5ep

9 leçons sans texte sur 29 (pdf-21 … pdf-29 — vérifier avec qa_corpus.py et
le registre : 20 ids déjà inscrits). PDF locaux disponibles ; même pipeline
VLM, mêmes contrôles (97 contrôles PASS sur le dernier posé — même barre).

## 3. Puis : hadith-6ep (28 leçons sans texte)

- PDF locaux disponibles pour tout le livre.
- Poser le claim au premier commit : `claim hadith-6ep (trace …-z2-main)`.
- Vague de 1 à 4 documents par commit, QA avant chaque livraison
  (`scripts-ia2/qa_corpus.py` sur le doc + lecture du rendu).

## 4. Nouveautés qui te concernent (R716)

1. **Hygiène** : plus aucun fichier temporaire à la racine du dépôt (les
   tr-ttmp-*.ts / tr-tmp/ historiques ont été supprimés). Tes temps de
   travail : `scripts-ia2/tmp/` — non suivi git (`.gitignore` ajouté :
   `tr-tmp/`, `tr-logs/`, `__pycache__/`, `*.pyc`, `*.tmp`).
2. **Nouveauté site** : les leçons peuvent porter un « Commentaire
   pédagogique » (section sous la leçon, puce `✧ comm.`). Ne t’en occupe pas
   — zone IA-1. Si tu vois une incohérence commentaire/leçon : une ligne dans
   ton journal, ne corrige pas.
3. **Compteur site** : le build affiche maintenant
   `commentaires pédagogiques : N / 1782` — normal dans le rapport de build.

## 5. Rappels non négociables

- `git pull --rebase origin main` avant chaque push ; jamais de force-push ;
  commits des autres IA intangibles.
- Typographie FR (’ « » U+202F), translittération corpus (ʾ ʿ ḥ ḏ ṯ š ġ),
  0 caractère arabe hors `<span dir="rtl" lang="ar">`.
- Une incertaine = incertaine, consignée comme telle.
- Défaut vu chez une autre IA : consigné dans TON journal, jamais corrigé
  par toi.
