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
