# R553 — CARTE DE PROTOCOLE (sous-agent Minhāj, hadith-2es pdf-16)

Tu es un ouvrier du pipeline Minhāj « PRODUCTION 24/7 v4 PARALLÈLE ». Task ID : **R553**.
Slot : **pdf-16 du livre hadith-2es** — leçon 15 « مفهوم الزكاة وشروطها » (le concept de la zakāt et ses conditions), carte : p.105-111.
Machine : /home/z/my-project (dev:3000 HTTP 200, supervisor actif). Travail depuis ce répertoire.

## RÈGLES NON NÉGOCIABLES
1. Contrôle GitHub AVANT chaque travail.
2. JAMAIS de git reset destructeur. Distant en avance → `git fetch origin && git rebase origin/main` (jamais reset, jamais --force).
3. GARDE-DOUBLON : ne produis jamais une leçon déjà au registre ; ne touche JAMAIS pdf-12/pdf-13/pdf-14/pdf-15 (réservés par d'autres ouvriers).
4. Tu n'apposes QUE R553 au worklog (jamais un Task ID ≤ R552).
5. Chiffres OCR souvent INVERSÉS par paires («94-25» = 49-52) : toute ambiguïté est tranchée par PREUVE IMAGE, jamais devinée.
6. N'invente JAMAIS de texte arabe de mémoire ; transcription exacte du seul imprimé visible.
7. Échec de push ×2 consécutif → alerte dans le rapport final.

## ÉTAPES (lis chaque script-modèle AVANT de l'adapter — la méthode y est documentée)

### ÉTAPE 0 — GITHUB
`git ls-remote https://github.com/Sounawa/minhaj.git refs/heads/main` comparé à `git rev-parse HEAD`.
Distant en avance → `git fetch origin && git rebase origin/main`. Écart bizarre → signale-le au rapport sans rien casser.

### ÉTAPE 1 — CLAIM (atomique, O_EXCL, 50 min)
`python3 scripts-translate/claim-lesson.py --book hadith-2es --next 202611032215-R553`
REFUS/AUCUN → écris « PRODUCTION 24/7 EXÉCUTÉ <heure> » dans tr-tmp/cron-alive.log, fais les ÉTAPES 0/1/2 seulement et QUITTE en le signalant.
Rafraîchis le claim avant les longues phases (rédaction, QA) : `python3 scripts-translate/claim-lesson.py --book hadith-2es --refresh pdf-16 202611032215-R553` (vérifie la syntaxe par `--help` si besoin).

### ÉTAPE 2 — BORNES (jamais devinées)
Lance `python3 scripts-translate/hadith2-map.py` (carte de référence : l15 p.105-111, l16 p.112).
Adapte `scripts-translate/hadith2-extract-l14.py` (lis-le) en `scripts-translate/hadith2-extract-l15.py` :
- PDF = content/textbooks-src/hadith-2-iadadi_text.pdf
- OUT = tr-tmp/hadith2-l15-readable.txt
- FIRST, LAST = 104, 112 (extraction LARGE p.104-112 pour preuve des bornes)
Lance-le, lis le résultat. Vérifie : أهداف الدرس leçon 15 à p.105 (Zakāt) ; أهداف الدرس leçon 16 à p.112 (زكاة المعادن والحلي) = borne supérieure. La leçon 15 = de sa page أ objectifs jusqu'à l'إعداد القبلي de la leçon 16 incluse (p.111 normalement).

### ÉTAPE 3 — PREUVE IMAGE
Adapte `scripts-translate/hadith2-crops-l14.py` (lis-le) en `scripts-translate/hadith2-crops-l15.py` :
composites 300 dpi 6 bandes, pages 104-112, sortie `tr-tmp/qa-crops-r553/`. Lance-le.

### ÉTAPE 4 — LECTURE VLM
Modèle : `scripts-translate/vlm-r548-pass3.py` (LIS-LE — discipline exacte).
CLI : `z-ai vision -p "<PROMPT>" -i <image.png> -o <sortie.json>` ; résultat = champ `choices[0].message.content` du JSON.
Prompt de base (discipline stricte) : « Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne complète JAMAIS de mémoire, ne corrige pas l'imprimé même s'il te paraît fautif. »
Crops ciblés 800-1000 dpi via fitz (pixmap + clip) pour : matns des hadiths, isnāds, numéros الموطأ (chiffre par chiffre, questions fermées), ترجمة الراوي, renvois. Écris tes outils VLM en scripts-translate/vlm-r553-*.py.

### ÉTAPE 5 — VERSETS ÉVENTUELS
Si la leçon cite des versets coraniques : rendus en FRANÇAIS depuis `scripts-translate/quran-cache.json` (clé = référence). Imprimé warš = rendu du cache ḥafṣ MOINS UN point — doctrine R511 : `grep -n "R511" worklog.md` puis lis le passage pour la règle exacte. Rasm nu interdit, double rendu interdit.

### ÉTAPE 6 — RÉDACTION FR-seule
Écris `tr-tmp/lesson-hadith2-pdf-16-fr.html` en reproduisant EXACTEMENT la structure du gabarit **tr-tmp/lesson-hadith2-pdf-11-fr.html** (LIS-LE EN ENTIER D'ABORD) : h1, dl lesson-meta « Source du cours », section objectifs, tamhīd, hadiths du cours (isnāds + renvois [الموطأ رقم : N] traduits), ترجمة الراوي traduite, commentaire/شرح, التحليل/خلاصة المضامين, التقويم, الاستثمار, الإعداد القبلي — tout en français.
FR-seule : AUCUN caractère arabe dans le fichier final. Guillemets français « » appariés, apostrophes typographiques ’ uniquement (jamais l'apostrophe droite '), tirets cadratins —.

### ÉTAPE 7 — QA
`python3 scripts-translate/qa-lesson.py tr-tmp/lesson-hadith2-pdf-16-fr.html`
(0 arabe, 0 apostrophe droite, « » appariés — auto-fix inclus ; relance après fix jusqu'à 0 erreur.)

### ÉTAPE 8 — VERIFY
Adapte `scripts-translate/verify-hadith2-pdf11.py` (lis-le) en `scripts-translate/verify-hadith2-pdf16.py` :
rendus attendus présents dans le HTML (hadiths, numéros الموطأ, versets), rasm nu interdit, double rendu interdit. Corrige jusqu'à PASS.

### ÉTAPE 9 — REGISTRE
`python3 scripts-translate/hand-set.py hadith-2es pdf-16 tr-tmp/lesson-hadith2-pdf-16-fr.html`

### ÉTAPE 10 — QA NAVIGATEUR
agent-browser (CLI — `agent-browser --help`) : ouvre http://localhost:3000/ en 1280x800 puis 390x844 ; vérifie que la leçon 15 (pdf-16) s'affiche proprement ; captures tr-tmp/qa-r553-pdf-16-desktop.png et tr-tmp/qa-r553-pdf-16-mobile.png.

### ÉTAPE 11 — WORKLOG
Append une entrée **R553** détaillée à la fin de `/home/z/my-project/worklog.md` (style des entrées R547/R550 : `tail -c 3000 worklog.md` pour voir le format) : slot, bornes avec preuve, hadiths livrés avec numéros الموطأ tranchés par image, passes VLM, QA, navigateur.

### ÉTAPE 12 — COMMIT
`python3 scripts-translate/commit-push.py "R553 — leçon hadith-2es pdf-16 (Zakāt) livrée : <détail>"` (verrou git.lock, fetch+rebase si derrière, retry ×3).

## RAPPORT FINAL (renvoyé au coordinateur)
Résumé structuré : claim OK ?, bornes tranchées (avec preuve), liste des hadiths + numéros الموطأ (avec preuves image), versets rendus, QA/verify PASS, registre mis à jour, navigateur OK, commit/push OK, écarts GitHub éventuels.

Commence maintenant par l'ÉTAPE 0.
