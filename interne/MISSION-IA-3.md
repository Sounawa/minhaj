# MISSION IA-3 — secondaire : typographie du rapport Z1, puis transcription

> Pour la **nouvelle** machine IA-3. Daté du 17 nov. 2026 (tour R716 de
> l’IA-1), sur demande de l’utilisateur : répartir le travail entre trois IA
> sans doublon ni empiétement. Lis d’abord `interne/PROTOCOLE-TROIS-IA.md`
> (ton périmètre est le tableau §2, colonne IA-3).

## 1. Ta zone — secondaire (collège + lycée)

- **Livres** : `content/books/*-es.json` et `content/books/*-tanawi-*.json`
  — 45 livres, 1 219 documents, 409 leçons sans aucune traduction aujourd’hui.
- **Journal** : `worklog-ia3.md` — à créer à la racine, append-only, série W
  (`## W1 — …`). Ne jamais écrire dans `worklog.md` ni `worklog-ia2.md`.
- **Outils** : `scripts/session-start.sh` au début de chaque session (exit 0
  obligatoire avant tout travail) ; QA document :
  `scripts-translate/qa-lesson.py` ; scan global : `scripts-ia2/qa_corpus.py`
  (lecture : tu peux l’exécuter, tu ne le modifies pas).
- Si tu as besoin de scripts d’extract PDF/VLM : crée-les dans
  `scripts-ia3/` (ton namespace) — ne touche ni `scripts/`, ni
  `scripts-ia2/`, ni `scripts-translate/` (sauf écriture du registre, §3).

## 2. Mission prioritaire — correction typographique du secondaire

Le scan Z1 (consigné dans `worklog-ia2.md`, entrée du 12 nov.) a relevé
**805 documents du secondaire avec des défauts typographiques durs
(apostrophes droites ’)** — rapport seul, jamais corrigé (règle de zones).
C’est ta première mission : du travail réglé, sans source PDF, à valeur
immédiate sur tout le corpus.

- Procédure : par livre (claim au premier commit : `claim <bookId>
  (trace …-w1)`), par vague de 1 à 4 documents ; apostrophe droite ’ → ’
  typographique **hors** des balises RTL et **hors** commentaires HTML
  (l’outil officiel `qa-lesson.py` fait foi) ; vérifier aussi « » appariés
  et U+202F avant `; : ! ? »`.
- QA avant chaque commit : `qa-lesson.py` sur chaque doc modifié + un
  `qa_corpus.py` global en fin de livre. Message : `IA-3 (W1): typo <docId>
  …`.
- La liste des 805 docIds est dans l’entrée Z1 de `worklog-ia2.md` — refaire
  un scan `qa_corpus.py` au départ : le corpus a bougé depuis le scan.

## 3. Mission suivante — transcription du secondaire (si PDF disponibles)

Après (ou en parallèle calmement réglé avec) la typo : transcription-extraction
des leçons sans texte, même convention que les fronts IA-1/IA-2
(slot PDF, pipeline VLM, htmlFr complet, registre).

- Ordre conseillé (leçons sans texte) : tafsir-tanawi-3 (29), taqtit-tanawi-3
  (30), usul-fiqh-tanawi-2 (30), usul-fiqh-tanawi-3 (30), puis taqtit-tanawi-2,
  fikr-islami-tanawi-1/2, qiraat-tanawi-2, tajwid-3es…
- ⚠️ Sources : géoblocage habous.gov.ma sur la plupart de ces manuels —
  demander les PDF à l’utilisateur (comme les fronts précédents).
- Registre : à chaque leçon posée **faite main**, ajouter le docId dans
  `scripts-translate/savant-registry.json` (via `hand-set.py`, par livre
  terminé) — en cas de rebase conflictuel, ré-ajouter uniquement TES ids.

## 4. Interdits (ton périmètre n’est QUE la colonne IA-3 du protocole)

- `content/books/*-ep.json` (primaire = IA-2) ;
- `content/commentaires/`, `scripts/build-site.py`, `scripts/site-style.css`,
  `site/`, racine publiée, `content/manifest.json` (IA-1) ;
- `scripts-ia2/`, `worklog-ia2.md`, `worklog.md` ;
- le miroir racine `savant-registry.json` (IA-1 le resynchronise) ;
- aucun fichier temporaire à la racine du dépôt — `scripts-ia3/tmp/`
  (non suivi git).

## 5. Qualité (identique aux deux autres IA)

’ typographique, « » appariés, U+202F, 0 caractère arabe hors
`<span dir="rtl" lang="ar">`, ʾ/ʿ en translittération, vague 1-4 documents,
QA avant commit, une incertaine = incertaine consignée, défaut vu chez une
autre IA = consigné chez toi, jamais corrigé par toi.
