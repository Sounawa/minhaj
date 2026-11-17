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

## 6. Ajout R721 — chantier éditorial « intertitres h2 » (audit P1, primaire)

> Ajouté par l’IA-1 (tour R721), sur la recommandation P1 de l’audit complet
> du site (R713, tableau 8) : « intertitres h2 sur les leçons signalées
> (passes éditoriales par livre) — accessibilité/contenu : navigation d’écran
> et sommaires internes ». Le suivi est automatisé : `python3
> scripts/qa-structure.py` imprime à chaque passe la liste des pages sans h2,
> livre par livre — la décroissance de ce compteur sera la preuve du travail
> fait, et la page `avancement.html` du site expose désormais les documents
> faits et restants (demande utilisateur R721).

**Ton périmètre (leçons et introductions sans intertitre h2 au 17 nov. 2026, cycle primaire — 22 pages)** :
tafsir-5ep 5 (pdf-mut23h3c-738, pdf-mut23h3c-797, 14067, pdf-mut23h3c-796, introduction) ;
hadith-1ep 4 (12583, 12866, introduction, 12863) ;
fiqh-1ep 2 (11412, 11413) ;
tajwid-6ep 2 (17597, 17598) ;
fiqh-5ep 2 (12014, 12015) ;
tafsir-6ep 2 (14599, 14600) ;
tafsir-1ep 2 (13622, 13621) ;
rasm-wa-dabt-4ep 1 (introduction) ;
fiqh-6ep 1 (15274) ;
tajwid-5ep 1 (19056).

**Méthode** : lire le htmlFr de chaque leçon, insérer des `<h2>` aux
divisions naturelles du contenu (rubriques du manuel, chapitres, blocs de
texte — JAMAIS un inventé hors du texte) ; aucune autre modification du
document ; pas d’urgence — en fin de vague hadith-5ep / hadith-6ep, ou en
interlude. Ce n’est pas une transcription : c’est un habillage de navigation.
Les pages « introduction » sont incluses dans le périmètre (l’audit les
compte dans les 84). Re-run de `scripts/qa-structure.py` après chaque passe
pour vérifier la décroissance.
