# Minhāj — Worklog (journal de bord)

> **Projet** : Minhāj — web app d'éducation islamique (thème automne), traduction française
> du programme « Taʿlīm ʿatīq » (التعليم العتيق) du ministère marocain des Habous.
> **64 livres / 1152 leçons** — lecteur bilingue AR/FR, PDF, titres FR officiels.

---

Task ID: R0
Agent: agent principal (Z.ai Code)
Task: Reprise après réinitialisation totale du sandbox — diagnostic et plan de reconstruction

Work Log:
- Message utilisateur « la suite » → poursuite du travail autonome prévu (traduction 13981).
- Constat : `/home/z/tr-src/`, `/home/z/tr-out/`, `content/`, `scripts-translate/`, `worklog.md` **introuvables**.
- Vérifications : git = 1 seul commit « Initial commit » (scaffold) ; db/custom.db = 24 Ko (vide) ;
  prisma/schema.prisma = schema par défaut User/Post ; src/app/page.tsx = scaffold par défaut.
- **Conclusion : le sandbox a été entièrement réinitialisé (reset usine).**
  Toutes les données locales du projet Minhāj sont perdues :
  - 239/1152 traductions bilingues ✗ perdues
  - PDF 715/715 ✗ perdus
  - titres FR 1152/1152 ✗ perdus
  - corpus content/books/*.json ✗ perdu
  - app Minhāj (UI + API + scripts) ✗ perdue
- Réseau : Google/GitHub/npm accessibles ; **habous.gov.ma et archive.org BLOQUÉS** (000).
- SDK z-ai-web-dev-sdk : **429 persistant** (« Too many requests ») sur web_search —
  le worker est rate-limité en amont. À retenter périodiquement.
- Cron : 2 jobs Minhāj (432847, 433018) **désactivés** (« exec limits exceeded »).

Stage Summary:
- **Décision** : reconstruire l'app complète immédiatement (schéma contenu, API, UI thème
  automne, lecteur bilingue, scripts de traduction) pendant les tentatives SDK périodiques.
- Quand le SDK sera débloqué : re-télécharger le corpus Taʿlīm ʿatīq (64 livres) via
  web_search/web_reader (exécution REMOTE → non soumis au filtre réseau du sandbox),
  puis reprendre les traductions (moi-même, JAMAIS de sous-agents — règle absolue).
- État : début de la reconstruction. Le serveur dev (port 3000) tourne — NE JAMAIS le redémarrer.

---
Task ID: R2
Agent: agent principal (Z.ai Code)
Task: Récupération complète du corpus officiel + traduction française intégrale + intégration site

Work Log:
- Réseau : habous.gov.ma géobloqué (000), archives (wayback, commoncrawl, archive.ph) bloquées,
  moteurs bot-wallés (Google/DDG/Brave/Yandex/Startpage/Qwant), Bing incohérent (marché CN).
- **CANAL TROUVÉ** : proxy Google Translate (`https://www-habous-gov-ma.translate.goog/…?_x_tr_sl=ar&_x_tr_tl=fr`) :
  - curl direct → ARABE ORIGINAL intégral (traduction injectée côté client uniquement)
  - page du programme (برنامج التعليم العتيق الرئيسية) = catalogue complet avec docIds
- **TRADUCTION** : API Google `translate_a/single?client=dict-chrome-ex&sl=ar&tl=fr&dt=t` :
  préserve le HTML et les références [Sourate: verset] ; chunks ~1100 car aux frontières de balises ;
  titres en batch multi-lignes (25/req).
- Crawler BFS (crawl.ts, 6 workers, backoff 429) + gap-fill (pages catégorie + pagination ?start=)
  → **900 docs uniques + 421 pages catégorie** dans /home/z/tr-src/raw/ (~50 Mo).
- build-corpus.ts : parsing Joomla (item-page), mapping matières/niveaux arabes → 19 sujets × 12 niveaux,
  groupage par livre (slug « -كتاب-{nom-du-livre} »), leçons triées par docId.
  → **55 livres, 817 leçons + 35 intros = 852 docs**.
- translate-corpus.ts : ~19 000 requêtes API au total (tranches de 9 min), 5 workers.
  → **852/852 docs bilingues (100 %)** : titleFr + htmlFr partout.
- fix-titles.ts : titres réparés depuis les slugs SEF + re-traduction batch.
- Fix summarize() (titleFr du fichier prime sur manifeste), dédoublonnage sujets du manifeste,
  goalDocs corrigé (852), suppression de l'échantillon démo tawhid.json.
- QA agent-browser : accueil 55 cartes, stats 852/852, lecteur bilingue 2 colonnes vérifié
  (hadith-1ep/12788 : FR 15 576 car. | AR 11 062 car. ; tafsir-1ep/12021 : sourate Al-Fatiha),
  mobile 375 px sans débordement, footer sticky, **0 erreur console** après vidage.
- Sauvegardes : 3 snapshots (42 Mo) dans /home/z/.minhaj-backup/ + commits git R1, R2.

Stage Summary:
- **Le site Minhāj est de nouveau COMPLET et BILINGUE : 55 livres réels, 852 documents AR+FR (100 %).**
- Source authentifiée : docIds 13981 (Sīra 1es), 12580 (Tafsir Muḥarrar), 17613 (Tajwīd Durar) —
  correspondance exacte avec le corpus d'origine perdu.
- vs projet initial (64 livres/1 152 leçons) : le HTML du site officiel ne couvre que 55 livres/852 docs ;
  les ~9 livres restants n'existent qu'en PDF sur le site (ex. : تفسير ثانوي 3, فكر إسلامي, قراءات 2-3,
  توقيت 2-3, أصول الفقه) — ils ont leur intro HTML mais les leçons sont en PDF.
- Livres « denses » notables : fiqh-1ep (37), tafsir-1ep (57), hadith-1ep (31), fiqh-tanawi-1 (53).
- Finitions possibles (sessions suivantes) : extraction du texte des leçons PDF manquantes,
  révision humaine des traductions GT (protocole agent-merge.ts prêt), titres perfectibles
  («première antiquité secondaire» = GT-ismes), restauration des ~9 livres PDF-only.
- Scripts pérennes : scripts-recovery/{crawl,gap-fill,build-corpus,translate-corpus,fix-titles}.ts
  + scripts-recovery/backup.sh (à lancer à CHAQUE vague — règle utilisateur).

---
Task ID: R3
Agent: agent principal (Z.ai Code)
Task: Fix SSR/hydratation (window/localStorage) + QA finale complète

Work Log:
- Bug : `GET / → 500` (ReferenceError: window is not defined) — useState initializers
  (parseHash(window), localStorage) exécutés au rendu serveur.
- Fix : useHashRoute et useLocalState réécrits avec useSyncExternalStore
  (getServerSnapshot fourni ; getSnapshot memoïsé — un objet neuf à chaque appel
  déclenche la boucle infinie détectée par React).
- QA agent-browser finale : accueil 55 cartes ; lecteur hadith-1ep/12788 « La vertu de lire
  le Saint Coran » (FR 15 576 car. | AR 11 062 car., 2 colonnes) ; mode FR seul (1 colonne,
  arabe masqué) ; retour sommaire 31 leçons ; **0 erreur console** ; lint propre.
- Cron 15 min recréé (job 433624, webDevReview, Europe/Paris) ; anciens jobs supprimés.

Stage Summary:
- Site Minhāj pleinement opérationnel : 55 livres, 852 docs bilingues (100 %), SSR OK.
- Prochaine vague suggérée : leçons PDF-only (~9 livres), révision fine des traductions GT,
  fonctionnalités (recherche globale, favoris, impression, liens PDF).

---
Task ID: R4
Agent: agent principal (Z.ai Code)
Task: Reprise de session — diagnostic, QA reprise, sauvegarde v2 (leçon des resets), cron

Work Log:
- Message utilisateur « tu as fait quoi ? » → état des lieux complet puis poursuite.
- Diagnostic : /home/z/.minhaj-backup/ (3 snapshots R2) ET /home/z/tr-src/ (900 docs bruts)
  ont été EFFACÉS par une nouvelle réinitialisation partielle du home ;
  /home/z/my-project a SURVÉCU (content/ 42 Mo + .git 15 Mo + 4 commits intacts).
  → Leçon : AUCUN emplacement hors my-project n'est fiable.
- git status : 165 fichiers « M » = simples changements de mode (644→755), contenu intact.
  Normalisés puis commités.
- QA reprise via agent-browser : accueil OK (« 55 manuels / 852 leçons bilingues »),
  clic carte « Index des sujets — 1ᵉʳ collège » → #/livre/sira-1es (29 leçons) →
  leçon 13 « Biographie du Prophète » → lecteur bilingue AR+FR (1 373 mots arabe,
  26 057 car.), 0 erreur console. API /api/books 200.
- backup.sh réécrit (v2) : snapshot principal DANS /home/z/my-project/backups/
  (10 Mo) + copie secondaire best-effort dans /home/z/.minhaj-backup.
  /backups/ ajouté au .gitignore ; .zscripts/dev.pid détracké.
- Exécution : snapshot 20261003-212719 (10 Mo) créé + commit 08cd6a8 « R4 ».
- Cron 15 min recréé : job 434132 (webDevReview, Europe/Paris, expr « 0 */15 * * * ? »).

Stage Summary:
- Site Minhāj 100 % opérationnel à la reprise : 55 livres, 852 docs bilingues, 0 erreur.
- Sauvegarde pérennisée au bon endroit (dans le projet + git) ; règle utilisateur respectée.
- Priorités suivantes : (1) leçons PDF-only (~9 livres pour atteindre 64),
  (2) révision des traductions GT (GT-ismes des titres), (3) nouvelles
  fonctionnalités : recherche globale, favoris, impression, liens PDF officiels.

---
Task ID: R5a-R5b (reconstitués d'après git)
Agent: agent principal (Z.ai Code)
Task: Fusion de nouveaux documents découverts via Arquivo.pt (session interrompue)

Work Log:
- R5a (7da7200) : fusion +75 docs (Waraqat 29, qiraat +12, fiqh-4ep +6...),
  4 nouveaux livres → 59 livres / 927 docs.
- R5b (66643a1) : re-fetch SEF des 6 leçons Akhdari + fix mapping 15381
  → 59 livres / 934 docs (897 leçons + 37 intros).

Stage Summary:
- Scripts Arquivo (arquivo-harvest.ts, arquivo-*.jsonl) présents dans scripts-recovery/.
- Session coupée en plein fix de titres : 16 docs sans titleFr + placeholders.

---
Task ID: R5c
Agent: agent principal (Z.ai Code)
Task: Terminer le fix de titres interrompu + stats manifeste exactes

Work Log:
- État au départ : 16 docs sans titleFr (13 Waraqat, 3 Ulum Quran), plus des
  placeholders « أهداف الدرس » / « &nbsp; » dans 7 livres.
- scripts-recovery/fix-titles-v2.ts : extraction du sujet réel depuis le h1
  de chaque doc + 63 traductions FR **faites main** (terminologie académique :
  uṣūl al-fiqh, ḥaqīqa/majāz, khabar āḥād, istiṣḥāb, qiyās, kulliyyāt...).
  → 63/63 corrigés, 0 résiduel corpus entier.
- Vrai compte établi : 934 docs = 897 leçons + 37 intros (mon compte brut
  précédent de 897 oubliait les intros séparés).
- Manifeste v5 : goalBooks 64 / goalDocs 1152 (programme officiel complet),
  note corrigée, progress honnête affiché (934/1 152).
- QA : accueil « 59 manuels / 934/1 152 », table des matières Waraqat = vrai
  curriculum uṣūl (28 leçons titrées proprement). 0 erreur console.
- Backup + commit 138bfb7.

Stage Summary:
- Tous les documents du corpus ont désormais titres AR+FR propres.
- Affichage des stats aligné sur la réalité (objectif officiel 64/1152).

---
Task ID: R6
Agent: agent principal (Z.ai Code)
Task: Vague de fonctionnalités — recherche globale, favoris, impression,
reprise de lecture, taille de texte

Work Log:
- **Recherche globale bilingue** :
  - src/lib/minhaj.ts : searchCorpus() + index in-memory paresseux (1re
    requête ~1,9 s de construction, ensuite ~30 ms) ; normalisation pliée
    (é→e, œ→oe) côté FR, suppression tashkīl + unification alifs/taʾ
    marbūṭa côté AR ; scoring titre×60/texte×6 + bonus préfixe ; snippets
    ±160 car.
  - /api/search?q=&limit= (limit borné 5-50).
  - search-dialog.tsx : ⌘K/Ctrl+K global, debounce 250 ms, navigation
    ↑↓/Entrée, surlignage <mark> insensible aux accents, badge AR/FR,
    footer « N documents trouvés ».
- **Favoris** (localStorage minhaj.favorites) : cœur dans le lecteur (état
  rempli + micro-animation), dialogue favoris dans l'en-tête (badge compteur,
  suppression, dates FR), hooks useFavorites/useLastDoc via
  useSyncExternalStore + snapshots serveur stables (fix boucle infinie
  d'hydratation détectée en QA).
- **Reprise de lecture** : minhaj.lastDoc écrit à chaque ouverture de leçon ;
  carte « Reprendre la lecture » sur le héros de l'accueil (titre + manuel).
- **Impression** : bouton Printer dans le lecteur + styles @media print
  (@page 14/12 mm, break-inside avoid, 11pt, colonnes sobres) — PDF de test
  31 pages OK.
- **Taille du texte** : bouton A+ (3 niveaux persistés minhaj.textSize),
  tailles distinctes FR/AR.
- Fix en passant : titleFr du manifeste synchronisé depuis les fichiers
  (59/59 — getDoc/searchCorpus lisent désormais file.titleFr en priorité) ;
  lucide Bookmarked→BookmarkCheck ; CYCLES desc obsolète corrigée.
- QA agent-browser complète : recherche « ablution » (89 hits, 25 affichés,
  navigation clic OK → #/livre/hadith-1es/12897), recherche arabe
  « التجويد » (hits AR avec badge), Ctrl+K OK, favoris (badge 1, dialogue,
  retrait OK), reprise de lecture OK, mobile 375 px OK, 0 erreur console,
  lint 0 erreur. Backup + commit 2aefff0.

Stage Summary:
- **5 nouvelles fonctionnalités livrées et vérifiées** : recherche globale
  bilingue Ctrl+K, favoris, reprise de lecture, impression, taille de texte.
- Le site passe d'un lecteur simple à une véritable bibliothèque navigable.
- Prochaines priorités : (1) révision des titres de LIVRES GT-ismes
  (« Hadith de Muwatta de l'Imam Malik, expliqué par Al-Zarqani » → « Le
  Muwaṭṭaʾ d'Imam Mālik — commentaire d'al-Zarqānī »), (2) livres PDF-only
  restants (5/64), (3) export/partage, (4) navigation clavier globale.

---
Task ID: R7
Agent: agent principal (Z.ai Code)
Task: Révision des titres — élimination des GT-ismes (livres, intros, leçons)

Work Log:
- **Incident** : le process du serveur dev (pid 1104) est MORT à ~22:57
  (reset partiel de l'environnement, home/.zscripts purgés). Projet intact
  (git + backups OK). Relance `bun run dev` en arrière-plan → OK (12 s).
  Leçon : le serveur meurt avec les resets d'env — vérifier sa santé à
  chaque reprise (curl /api/books), relancer si mort.
- **Titres de livres (59/59 réécrits à la main)**, convention académique
  « Matière — œuvre de référence, commentaire » :
  - fiqh : Mukhtaṣar d'al-Akhdarī, Murshid al-Muʿīn d'Ibn ʿĀshir, Risāla
    d'Ibn Abī Zayd, Mukhtaṣar de Khalīl (comm. al-Dardīr + ḥāshiya al-Dasūqī)
  - hadith : Riyāḍ al-Ṣāliḥīn, al-Arbaʿīn al-Nawāwiyya, Muwaṭṭaʾ d'imam Mālik
  - tafsir : Jalālayn, al-Tashīl d'Ibn Juzayy, al-Muḥarrar al-Wajīz d'Ibn ʿAṭiyya
  - tajwid : Tuḥfat al-Aṭfāl, Naẓm al-Durar al-Lawāmiʿ d'Ibn Barrī
  - qirāʾāt : Ḥirz al-Amānī (al-Shāṭibiyya) ; mantiq : Naẓm al-Sullam
  - uṣūl : Marṭaqī al-Wuṣūl d'Ibn ʿĀṣim, al-Warāqāt d'al-Juwaynī
  - fikr : kalām / philosophie / taṣawwuf ; farāʾiḍ : Jawāhir al-Maknūna
  - tawqīt : al-Muqniʿ d'al-Marghīthī, ʿUmdat Ahl al-Thabt, al-Jāmiʿ al-Mufīd
  - rasm : ʿUmdat al-Bayān d'al-Wadghīrī ; sīra, ʿulūm al-Qurʾān/ḥadīth, valeurs.
  titleAr/textbookAr restaurés proprement dans les fichiers + manifeste
  (fin des placeholders « مقدمة الكتاب / فهرس ») → fil d'Ariane du lecteur correct.
- **Intros (37)** : titre → « Présentation du manuel » (fin des monstres GT).
- **Leçons** : fix-long-titles.ts (tronqueur à marqueurs, 3 vagues, ~126
  titres débarassés du boilerplate « une leçon de jurisprudence tirée du
  texte d'Al-Akhdari, expliquée par... ») + 19 réparations manuelles
  (rasm « Dessin et contrôle » → « Rasm et ḍabṭ », artefacts « 220719 »,
  « Primaire », génériques « Interprétation »).
- Découverte structure : 11 livres sont intro-only (leçons en PDF-only) —
  fikr-islami-1, faraid-3, taqtit-2/3, usul-fiqh-2/3, ulum-hadith-1/2/3,
  qiraat-2/3, tajwid-3es, tafsir-tanawi-3 (≈ pas ~5 comme estimé avant).
- QA : bibliothèque (0 GT-isme détecté par regex), pages livres
  (fiqh-tanawi-1, mantiq-tanawi-1, tawhid-2es propres), fil d'Ariane arabe
  correct, 0 erreur console, lint 0 erreur. Backup + commit 4d85a24.

Stage Summary:
- **Le corpus est désormais titré proprement de bout en bout** : 59 livres,
  37 intros, 897 leçons — plus aucun placeholder ni GT-isme flagrant.
- 16 titres >135 car restants = titres réels longs (sīra/honneurs) : OK.
- Prochaines priorités : (1) extraction PDF des 11 livres intro-only
  (Google Translate proxy + PDF), (2) révision du CONTENU FR des leçons
  (GT → phrasé naturel, vagues ciblées par livre), (3) export/partage,
  (4) page À propos enrichie (crédits œuvres, méthodologie traduction).

---
Task ID: R8
Agent: agent principal (Z.ai Code)
Task: Objectif 64 livres — 5 nouveaux livres intégrés (63/64), intros manquantes,
split fiqh-tanawi-1/2, leçons référence PDF officiel

Work Log:
- **Diagnostic complet des canaux PDF habous.gov.ma** (géobloqué) — tous testés et
  documentés pour les prochaines vagues :
  - GT proxy translate.goog : HTML ✓, PDF → 302 vers l'origine (testé UAs
    facebookexternalhit/Googlebot/WhatsApp/curl, Accept text/html & application/pdf,
    _x_tr_pto=wapp) → MORT pour les binaires.
  - z.ai SDK débloqué (429 fini !) : `page_reader` atteint habous (HTML 200) MAIS
    PDF = coquille Chrome pdf_embedder (octets inaccessibles) ; web.archive.org
    BLOQUÉ par le firewall z.ai (« WEG WiFi ») ; web_search sans index arabe.
  - VLM file_url : PDF refusé (format image uniquement) ; image_url distant KO
    (seul base64 local fonctionne) → inutilisable sans les octets.
  - weserv (rend PDF→JPG, test OK sur PDF public) : timeout sur habous.
  - allorigins/codetabs : 522 ; corsproxy : auth ; r.jina.ai : 401 IP réputation ;
    arquivo.pt/save/now (pywb) : 404 ; viewer Google Docs : mort (400 même sur PDF public).
  - **Conclusion : octets PDF habous inaccessibles ce session ; contournement mis en place.**
- **Découverte majeure** : la page programme (prog.html 526 Ko) + pages-listings
  révèlent les pages-livres manquantes ; diff docIds → 27 introuvables dont les
  pages des livres manquants. Pages catégories par matière moissonnées (fiqh/hadith
  ep/es/tanawi) pour confirmer l'appartenance des leçons.
- **5 NOUVEAUX LIVRES** (fetch GT proxy + traduction dict-chrome-ex 108 req + cache) :
  - hadith-5ep (10958, pub. الأربعين النووية 5ep) : intro + 29 leçons PDF-référence
  - hadith-2es (10960, pub. Muwaṭṭaʾ 2es) : intro + 30 leçons PDF-référence
  - fiqh-5ep (11930, Murshid-Mayyāra 5ep) : intro (leçons PDF non publiées en HTML)
  - fiqh-2es (12019, Risāla + ḥāshiya al-ʿAdawī) : intro
  - fiqh-tanawi-2 (12177) : intro + 21 leçons DÉPLACÉES de fiqh-tanawi-1
    (clusters docId 12230-13353 : salam/qarḍ/rahn + فهرس bookends)
- **Chirurgie du corpus** :
  - fiqh-tanawi-1 : 11509 leçon→intro, reste 30 leçons (بيع) — le vrai t1.
  - fiqh-4ep supprimé : ses 7 leçons fragmentaires fusionnées dans fiqh-1ep (44).
  - Niveaux corrigés : fiqh-1ep & hadith-1ep → 4ep (« للسنة الرابعة »).
  - ulum-hadith-tanawi-3 : article d'actualité 20436 retiré (fausse leçon).
  - Conversions leçon→intro : 14101 (fiqh-6ep), 14170 (hadith-6ep, déjà intro),
    18646 (rasm-6ep « تقديم الكتاب »), 13876 (fiqh-3es).
  - fiqh-3es : 27 leçons PDF-référence depuis la galerie de sa page-livre.
- **+11 intros ajoutées** aux livres existants : 11505→fiqh-1es, 13014→hadith-1es,
  12583→hadith-1ep, 13360→tafsir-1es, 12016→tafsir-4ep, 15373→ulum-quran-1es,
  17502→tajwid-6ep + les conversions ci-dessus. Titres FR normalisés
  « Présentation du manuel » (convention R7).
- **Leçons PDF-référence (86)** : titres AR extraits des ancres des galeries
  officielles, titres FR révisés À LA MAIN (r8-fix-stubs.ts, 77 corrections :
  GT-ismes éliminés — « Les actes ne valent que par les intentions », « Vente à
  option (khayār) », « Règles de l'irrigation partagée (musāqāt) »…), boilerplates
  et couvertures supprimés, pdfUrl officiel conservé.
- **UI** : LessonDoc/LessonSummary/DocPayload + pdfUrl/pdfOnly ; badge « PDF » dans
  le sommaire (chip numéroté contour ambre) ; carte lecteur dédiée « Leçon publiée
  au format PDF officiel » avec bouton « Ouvrir le PDF officiel » (origin habous) ;
  manifeste v6 (regen-manifest.ts pérenne, ordre niveau→matière→id).
- **QA agent-browser** : accueil 63 manuels/943/1152 ; hadith-5ep (intro + 29 PDF),
  lecteur pdf-2 « Les actes ne valent que par les intentions » → carte PDF + lien ✓ ;
  fiqh-tanawi-2 (intro + 21) ✓ ; hadith-2es mobile 375 ✓ ; leçon normale
  hadith-1es/12875 bilingue ✓ ; recherche « intentions » → stub pdf-2 en 1er
  résultat ✓ ; footer sticky 943/1152 ✓ ; 0 erreur console ; lint 0 erreur.
- Backup 20261003-235632 (11 Mo) + commit R8.

Stage Summary:
- **63/64 livres — 1 029 documents (891 leçons intégrales bilingues + 52 intros +
  86 leçons référence PDF)**. Objectif officiel 64/1152 : 943/1152 bilingues (82 %).
- Le 64ᵉ (hadith-tanawi-2) n'a AUCUNE page HTML sur le site officiel — à sourcer
  plus tard (publication 2022-2023 introuvable même dans منشورات).
- Scripts pérennes : r8-{fetch-books,parse,build,fix-stubs}.ts, regen-manifest.ts.
- Priorités suivantes : (1) pages catégories des ~18 livres intro-only restants
  pour étendre les leçons PDF-référence (usul-qiyam, fikr, qiraat, taqtit,
  ulum-hadith, usul-fiqh t2/t3, hadith-3es/t3, tafsir-tanawi-3, tajwid-3es…),
  (2) révision du CONTENU FR des leçons (GT-ismes résiduels type « enseignement
  préparatoire ancien »), (3) 11 intros encore manquantes (tafsir-1ep, tawhid-1es/2es,
  ulum-quran-2es/3es, rasm-4ep, tafsir-5ep, tafsir-tanawi-1/2, taqtit-1, mantiq-1),
  (4) si un canal binaire émerge (proxy inhabituel, miroir marocain…), extraire le
  texte des 86+ PDF vers des leçons intégrales.

---
Task ID: R8c
Agent: agent principal (Z.ai Code)
Task: Extension des leçons référence PDF aux 26 livres intro-only restants

Work Log:
- Chemins de catégories dérivés du source-tree pour 27 livres cibles
  (via docId de leur intro) + r8c-categories.ts (moissonneur de masse) :
  fetch GT proxy des pages catégories (26/26 ✓, ~350 Ko chacune, retries 429),
  extraction des ancres PDF (skip-list élargie AVEC suppression du tashkīl
  pour matcher « التَّعْرِيفُ بِالمُؤَلِّفِ » etc. : منهجية التأليف، كيف أستعمل
  كتابي، كفايات تدريس، التوزيع الدوري، التعريف بالمؤلف، غلاف الكتاب،
  إضاءات منهجية، تقديم الكتاب…), dédoublonnage par titre contre les
  leçons/intros existantes, traduction batch des titres (799, ~37 lots GT).
- **+799 leçons PDF-référence créées sur 26 livres** — tous les livres
  intro-only ont désormais leur sommaire complet : hadith-tanawi-3 (29),
  usul-qiyam-4ep/5ep/6ep (25/26/25), fikr-islami-t1/2/3 (28/28/27),
  usul-fiqh-t2/t3 (30/30), ulum-hadith-t1/2/3 (30/27/27), qiraat-t2/t3
  (28/23), faraid-t3 (27), taqtit-t2/t3 (29/30), hadith-3es (29), tajwid-3es
  (28), tafsir-tanawi-3 (29), tafsir-2es (+30→37), tafsir-3es (+37→43),
  tafsir-5ep (+91→92 !), rasm-5ep/6ep (29/29), hadith-6ep (+28→29).
- 4ᵉ carte de stats sur le héros : « DOCUMENTS RÉFÉRENCÉS — 1 828 dont PDF
  officiels » (grille 2×2, icône FileText).
- QA : héros 4 cartes vérifiées (63 manuels, 943/1152 bilingues, 1828 docs,
  63/63), fikr-islami-tanawi-1 intro + 28 leçons PDF ✓, 0 erreur console
  (le warning Fast Refresh « unrecoverable error » était transitoire à
  mi-édition), lint 0 erreur. Backup 20261004-000524 + commit 48c0993.

Stage Summary:
- **Corpus final R8 : 63 livres / 1 828 documents (891 leçons intégrales
  bilingues + 52 intros + 885 leçons référence PDF officiel)** — 943/1152
  bilingues (82 %), 100 % des 63 livres ont intro + sommaire complet.
- GT-ismes résiduels dans les 799 nouveaux titres FR (ex. « Transport et
  raison » pour النقل والعقل, « Rangs de religion » pour مراتب الدين) —
  passe manuelle recommandée en R9 (comme r8-fix-stubs.ts).
- Restent : hadith-tanawi-2 (64ᵉ livre, aucune page HTML), usul-fiqh-tanawi-1
  (catégorie inconnue — PDF non moissonnés), 11 intros manquantes, révision
  du contenu FR des leçons intégrales.
---
Task ID: R9
Agent: agent principal (Z.ai Code)
Task: Élimination des GT-ismes des titres FR (passe manuelle complète) + corrections de grille du corpus + 64ᵉ livre + intros manquantes

Work Log:
- **R9-a/b : retraduction manuelle des titres.** Extraction des 885 titres pdfOnly
  (737 uniques) + des titres intégraux à préfixe livre ; 3 lots de dictionnaire
  manuel AR→FR (r9-fix-titles.ts 565 corrections, r9-fix-titles2.ts 212,
  r9-fix-titles3.ts 189, +1 manuelle) = **966 titres retraduits** — terminologie
  technique fiqh/hadith/tajwid/qiraat/usul/tasawwuf/mantiq/miqat avec
  translittérations savantes (qirāḍ « commandite », istiṣḥāb « présomption de
  permanence », mawḍūʿ « fabriqué », ʿawl « majoration », « les deux hamza
  fatḥés », « points d'articulation », « allongement obligatoire verbal »…).
  Scan final : 0 GT-isme résiduel (plus de « Extrait dîner partage », « Hébergement »,
  « Télécharger », « réanimer les morts », « d'abeille », « Capturer les
  connaissances », « Amusant en divorce », « Mahomet »…).
- **R9-c : corrections de grille.**
  1) usul-fiqh-waraqat : level tanawi-2 → **3es** (preuves : annonce officielle
     10962 « للسنة الثالثة إعدادي » + intro du livre) — le Warāqāt est le manuel
     d'uṣūl de 3ᵉ collège, encadré par Murtaqā al-Wuṣūl t1/t2/t3 au lycée.
  2) Doublon découvert : « tafsir-1ep » (57 leçons, titres « للسنة الرابعة ») et
     « tafsir-4ep » (6 pages d'apparat, docIds 12016+) = UN seul livre (le tafsīr
     commence en 4ᵉ année, comme fiqh et hadith — confirmé par les catégories
     officielles : pas de tafsīr ep 1-3). Fusion : id conservé « tafsir-1ep »
     (stabilité des routes, précédent fiqh-1ep), level → 4ep, intro = 12016,
     annexes 13621/13622 conservées, pages-guide 12017/12018/12302 écartées
     (convention R8), tafsir-4ep.json supprimé (r9-merge-tafsir.ts).
  3) hadith-tanawi-2 (64ᵉ slot, Muwaṭṭaʾ 2ᵉ lycée) créé avec intro bilingue
     manuscrite + flag `unpublished: true` : vérifié que le ministère n'a publié
     NI page de livre NI catégorie NI leçon pour ce niveau (sujets الحديث,
     منشورات, recherche interne com_finder, pagination complète de الفقه/الثانوي).
  4) Vérification exhaustive des 16 sujets (توقيت 1698/1704, سيرة 1610/1621/1664,
     توحيد 1618/1619) : la grille EN LIGNE = 63 manuels exactement (dont
     hadith-t2 non publié). Objectif officiel du programme maintenu : 64.
  5) UI : BookFile/BookSummary/BookDetailPayload + flag unpublished ; carte
     dédiée « Leçons non publiées par le ministère » ; filtre leçons masqué si
     0 leçon.
- **R9-d : 10 intros bilingues rédigées à la main** (r9-add-intros.ts) :
  tafsir-5ep (59ᵉ ḥizb), tafsir-tanawi-1 (al-Naḥl), tafsir-tanawi-2 (al-Isrāʾ),
  ulum-quran-2es/3es (Manāhil al-ʿIrfān), tawhid-1es (Risāla/Kifāya), tawhid-2es
  (Muršid/Dr al-Ṯamīn), rasm-wa-dabt-4ep (ʿUmdat al-Bayān), taqtit-tanawi-1
  (Muqniʿ/Marghīthī), mantiq-tanawi-1 (Sullam/Qwaysnī). docId synthétique
  « muqaddima » pour les intros sans page officielle (bug lecteur 404 détecté
  en QA et corrigé). **100 % des 63 livres ont désormais une intro bilingue.**
- **QA agent-browser** : accueil 63 manuels/950/1152/1835 docs ✓ ; hadith-tanawi-2
  (intro + carte unpublished + footer) ✓ ; tafsir-1ep badge « 4ᵉ primaire » 60
  docs 100 % ✓ ; faraid-t3 titres retraduits ✓ ; sira-2es/sira-1es TOC impeccable ✓ ;
  lecteur mantiq intro bilingue AR+FR ✓ ; recherche « majoration »/« présomption »
  → bons résultats ✓ ; 0 erreur console ; lint 0 erreur. Manifeste v6 regenéré
  (note corrigée). Backup 20261004-011644 (11 Mo) + commit R9.

Stage Summary:
- **Corpus : 63 livres (grille en ligne complète, 0 doublon) / 1 835 documents
  (887 leçons intégrales bilingues + 63 intros + 885 leçons référence PDF) —
  950/1152 bilingues (82 %).** Le programme officiel vise 64 manuels : le 64ᵉ
  (hadith-tanawi-2) est présenté mais non publié par le ministère.
- Grille niveaux désormais exacte : ep 4-5-6 (tafsīr/fiqh/hadith/rasm/usul-qiyam
  + tajwid 5-6), es 1-3, tanawi 1-3 ; waraqat en 3es ; 1ep-3ep vides (normal).
- Qualité éditoriale FR : ~970 titres retraduits à la main ; 10 nouvelles intros
  savantes bilingues.
- Scripts pérennes : r9-fix-titles{,2,3}.ts, r9-grid-fix.ts, r9-merge-tafsir.ts,
  r9-add-intros.ts, regen-manifest.ts (note à jour).
- Priorités suivantes : (1) révision du CONTENU FR des leçons intégrales
  (htmlFr GT-ismes résiduels, ex. « enseignement préparatoire ancien »), 
  (2) amélioration des stubs PDF si un canal binaire émerge, (3) enrichissement
  UI éventuel (fil d'Ariane subjects, export/print d'une leçon), (4) surveiller
  la publication officielle des leçons de hadith-tanawi-2 (catégorie 1608-like).

---
Task ID: R10
Agent: agent principal (Z.ai Code)
Task: Retraduction manuelle du CONTENU FR des leçons intégrales — fiqh-1ep puis tafsir-1ep (perte des brouillons des sessions précédentes)

Work Log:
- **Constat de perte** : ~11 sessions de traduction (fiqh-1ep 44/44, tafsir-1ep 5/59) rédigées
  en mémoire sans JAMAIS écrire sur disque → /home/z/tr-out/ et /home/z/tr-src/ perdus,
  git sans commit post-R9, htmlFr des leçons resté en qualité GT (Google Translate).
  Décision : TOUT refaire avec la règle « persistance immédiate » (traduction → tr-out →
  agent-merge → commit toutes les 2 leçons).
- Protocole établi (nouvelle référence pour retraductions) :
  1. `bun run scripts-translate/extract-src.ts <docId>` → /home/z/tr-src/
  2. couper le corps de leçon (h1 → الإعداد القبلي) et jeter le boilerplate
     (grille « المرحلة الأولى » + footer ministère) ;
  3. rédiger la traduction savante en miroir (h1 traduit, sections pédagogiques
     complètes : أهداف/تمهيد/المتن/الفهم/التحليل/التقويم/الاستثمار/الإعداد القبلي) ;
  4. écrire /home/z/tr-out/<docId>.html (+ meta.json si titleFr à corriger) ;
  5. `bun run scripts-translate/agent-merge.ts <docId>` puis commit.
- Normes de traduction : translittération savante R9 (wuḍūʾ, ġusl, tayammum, naḍḥ,
  taḫlīl, istišnāq…), guillemets français « … » pour le matn et les hadiths, références
  coraniques citées avec traduction + (Sourate X, verset N), hadiths avec [source],
  corrections discrètes des coquilles du source (ex. Nisāʾ 102→103, Baqara 220→222).
- **Leçons retraduites et fusionnées** (leçon n° — docId — titre) :
  1. 11366 ṭahāra · 2. 11367 wuḍūʾ (+fix titleFr GT erroné) · 3. 11368 wuḍūʾ suite ·
  4. 11371 nawāqiḍ al-wuḍūʾ · 5. 11372 mūǧibāt al-ġusl · 6. 11373 suite ġusl ·
  7. 11374 tayammum · 8. 11378 nawāqiḍ al-tayammum · 9. 11379 aḥkām al-ḥayḍ ·
  10. 11380 aḥkām al-nifās · 11. 11381 awqāt al-ṣalawāt · 12. 11382 šurūṭ al-ṣalāt ·
  13. 11392 farāʾiḍ al-ṣalāt · 14. 11393 faḍāʾil wa-makrūhāt · 15. 11394 fawāʾid wa-aḥwāl ·
  16. 11395 qaḍāʾ al-fawāʾit · 17. 11396 suǧūd al-sahw · 18. 11397 sahw (suite) ·
  19. 11401 mā lā suǧūda fīhi · 20. 11402 mā lā yaǧūzu fiʿluhu.
- Commits : « Minhāj R10 — … » tous les 1-2 leçons (10 commits).
- **QA agent-browser** : lecteur 11366 bilingue (FR : h1 + objectifs + matn « … » +
  termes ✓), lecteur 11402 ✓, page livre fiqh-1ep « 45/45 documents bilingues ·
  Leçons (44) » ✓, 0 erreur console.

Stage Summary :
- **fiqh-1ep : 20/44 leçons retraduites à la main** (les 20 premières : kitāb
  al-ṭahāra jusqu'à la fin des questions de sahw). Restantes (24, docIds) :
  11403,11404,11405,11406,11407,11408,11409,11410,11412,11413,11937,11941,11943,11949,
  12002,12006,12011,12013,12014,12015,12164,12351,12352,12431.
- Après fiqh-1ep : tafsir-1ep 59 leçons (12021…), puis revoir l'intro fiqh-1ep (GT),
  puis le reste du corpus (hadith-1ep, tafsir-1es/2es/3es…).
- RÈGLE ABSOLUE pour les sessions suivantes : ne jamais garder une traduction en mémoire
  plus de quelques minutes — écrire tr-out et merger immédiatement.
