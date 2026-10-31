# SOLUTION-OUVRAGES — la carte anti-reset du projet Minhāj

> **À LIRE EN PREMIER après tout reset** (compression de contexte, reboot sandbox, rebuild).
> Cette carte est la mémoire de LA SOLUTION POUR LES OUVRAGES, établie au tour R458
> (2026-10-31) et prouvée en production. Elle est inscrite en trois lieux durables :
> (1) ce fichier versionné au dépôt (survit aux rebuilds — les fichiers non suivis sont effacés) ;
> (2) le payload du cron « Minhāj — MÉMOIRE OUVRAGES (anti-reset) » (lisible par `cron list`
> même si le dépôt est injoignable) ; (3) l'entrée worklog R458.
> **Règle h : le tail du worklog reste l'autorité de priorité.** Cette carte dit *comment* ;
> le worklog dit *où on en est*.

## 1. Le problème (pourquoi cette carte existe)

- Le portail **habous.gov.ma** (source officielle des ouvrages) est **FERMÉ** :
  l'arborescence des documents rend 404 (canari `scripts-translate/veille-portail.sh`,
  état exposé dans `tr-logs/pipeline-status.json` et le pied de page du site).
- Les **rebuilds du sandbox effacent les fichiers non suivis** (le piège historique :
  `sources/` était gitignoré et fut effacé au rebuild du 31-10 08:49).
- La production de leçons exige la matière des ouvrages : **828 leçons pdfOnly**
  au moment de la cartographie R458.

## 2. LA SOLUTION — trois routes (toutes prouvées, dans l'ordre d'usage)

### Route A — le miroir archive.org (la route principale)
La collection « سلسلة كتب التعليم العتيق المغربي » — **item archive.org
`1_20220304_20220304_2251`** — 77 PDF : manuels **COMPLETS** du primaire au
secondaire traditionnel, versions `_text` avec couche OCR.
**JOIGNABLE en HTTP direct depuis la sandbox** (testé HTTP 200 — seul
`web.archive.org` est bloqué au niveau réseau).

```bash
# Liste des fichiers de la collection (cache 24 h : tr-logs/collection-files.json)
curl -s https://archive.org/metadata/1_20220304_20220304_2251
# Téléchargement d'un manuel (atomique, vérif en-tête %PDF-)
curl -L -o content/textbooks-src/<slug>.pdf \
  "https://archive.org/download/1_20220304_20220304_2251/<fichier-url-encodé>.pdf"
```

Déjà en dépôt (versionnés — la source de vérité est le manuel lui-même) :
- `content/textbooks-src/tafsir-2-thanawi_text.pdf` (20,7 Mo — **contient Isrāʾ 709-738 + Kahf 739-767**)
- `content/textbooks-src/tafsir-3-thanawi_text.pdf` (23,5 Mo — farāʾiḍ 3e année)
- `content/textbooks-src/hadith-2-iadadi_text.pdf` (8,7 Mo)

### Route B — le backend page_reader de la SDK (route auxiliaire)
`page_reader` (z-ai-web-dev-sdk, côté backend) **atteint web.archive.org** là où le
réseau sandbox échoue — utilisable pour les **arbres/TDM** (snapshot testé : 137 Ko),
**pas les PDF binaires**. Wayback est sondé via
`https://archive.org/wayback/available?url=<pdfUrl>` (journalisé).

### Route C — les doublons URL-exacts (la route gratuite, déjà consommée)
Les slots dont le `pdfUrl` est **identique octet par octet** à un fascicule déjà traduit
se résolvent **sans aucun téléchargement**, par renvoi de référence (doctrine faraid
316/325) — preuve par l'URL. Exemple clos : tafsir-5ep slots 768-797 = fascicules
556-585 de tafsir-2es (30 doublons, commit 781427f). Mystères restants : 798/799
(jumelles probables de tafsir-3es 16850/16833, vérification différée).

## 3. La greffe superviseur — la chasse est AUTONOME

`scripts-translate/supervisor.py` (v4) — **immortel** via
`ensure-supervisor.py` préfixé au script `dev` de package.json :
chaque `bun run dev` (port 3000) relance le superviseur.
Sa boucle `hunt_sources()` (toutes les 30 min) sonde dans l'ordre :
1. l'arbre direct du portail (200 = le portail est revenu) ;
2. Wayback (journal : lampe témoin) ;
3. **la collection archive.org** : segment arabe du pdfUrl → manuel complet
   correspondant (normalisation hamzas/espaces/chiffres, repli matière par ID de
   livre, version `_text` prioritaire), téléchargement atomique dans
   `content/textbooks-src/`, cache 24 h de la liste.

Observabilité : TICK public toutes les 5 min dans `tr-tmp/cron-alive.log`,
état complet dans `tr-logs/pipeline-status.json` (API `/api/pipeline-status`,
voyant « Production autonome » battant dans le pied de page du site).

## 4. La méthode d'extraction (manuel → leçons), inaugurée par la leçon 709

1. **Carte d'alignement** : leçons de l'imprimé ↔ slots du portail **par ordre**
   (exemple : `scripts-translate/isra-map.py` → 28 leçons Isrāʾ + fihris + sources
   sur les slots 709-738 ; p.7-10 = matière liminaire méthodologique, la vraie
   leçon 1 commence p.11). Vérifier la carte contre le REGISTRE des livraisons
   avant toute extraction (garde anti-doublon).
2. **`pdftotext` page par page AVANT tout crop** (les versions `_text` ont la couche OCR).
3. Zones corrompues → **inversion bbox RTL par coordonnées** (lecture ligne à ligne
   en ordre visuel inverse). **VLM déclassé** : six hallucinations documentées —
   dernier recours seulement, arbitrage par sources canoniques web.
4. **FR-seule doctrine** : versets rendus en français, 0 caractère arabe,
   0 apostrophe droite, guillemets appariés (`qa-lesson.py`).
5. Livraison : JSON du livre + `hand-set.py` (registre) + QA navigateur
   (`agent-browser` desktop 1280 + mobile 390, 0 overflow, 0 erreur console).

## 5. L'état à la rédaction de la carte (R458, 2026-10-31 ~17:30 Paris)

- **Registre : 1032 leçons** savantes livrées. tafsir-5ep : **62/122**.
- Leçon 709 (Isrāʾ 1, Ibn ʿAṭiyya) livrée — première leçon de matière miroir.
- **Matière sécurisée en cache** : Isrāʾ 709-738 + Kahf 739-767 (59 leçons,
  les deux manuels _text dans le dépôt).
- Prochaines priorités : (1) **l'extracteur PDF→slot** (manuel complet → pages par
  leçon par correspondance d'ordre avec les slots) ; (2) production Isrāʾ puis Kahf ;
  (3) hadith-2-iadadi (manuel acquis) ; (4) audit doctrinal 310-315 + arbitrage du
  titre faraid ; (5) recherche web du manuel de Rasmūkī (manẓūma 3e année).
- **Le tail du worklog peut être plus récent que cette carte : il commande.**

## 6. Checklist post-reset (2 minutes)

1. `cat scripts-translate/GARDE-DOUBLON.md` — jamais de Task ID ≤ dernier apposé.
2. `tail -80 worklog.md` — la priorité courante (règle h).
3. `pgrep -f supervisor.py || python3 scripts-translate/ensure-supervisor.py`
   (le superviseur doit battre : `tail tr-tmp/cron-alive.log`).
4. `bun run dev` tourne sur le port 3000 (le site : `tail dev.log`).
5. Vérifier la matière : `ls -la content/textbooks-src/` (les manuels versionnés).
6. Si le portail Habous est revenu (canari PORTE|OUVERTE), la chasse s'en charge
   seule ; sinon, les routes A/B/C ci-dessus.
7. Git : `git fetch origin && git rev-list --count origin/main..main` avant push ;
   remote = `https://github.com/Sounawa/minhaj.git` ; backup `scripts-translate/backup.sh`.
8. En cas de doute total : `cron list` — le job « MÉMOIRE OUVRAGES » porte cette
   carte en payload.

## 7. Les gardes non compressibles

- **GARDE-DOUBLON** : scanner le worklog ENTIER avant tout append ; refuser tout
  Task ID ≤ dernier apposé.
- **Registre** : `scripts-translate/hand-set.py` (main + llm) ; jamais deux fois
  la même leçon (vérifier le registre AVANT la carte des pages).
- **QA** : `qa-lesson.py` (0 arabe, 0 apostrophe droite, guillemets/balises appariés),
  `verify-quran` (versets conformes au cache), navigateur 1280/390.
- **Cron plateforme** : le canal agentTurn **NE PORTE PAS** les payloads (verdict R456/R457
  par l'expérience — run_count s'incrémente, zéro exécution). Le moteur vit dans la
  machine (superviseur v4). Le cron « MÉMOIRE OUVRAGES » vaut donc comme STOCKAGE
  DURABLE lisible, et comme sonde de réparation éventuelle du canal.
