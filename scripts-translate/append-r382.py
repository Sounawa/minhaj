#!/usr/bin/env python3
# append-r382.py — entrée R382 au worklog (garde anti-doublon : refuse si R382 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R382
Agent: GLM (session web-394d04d3, tick 2026-10-30 07:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : conformité GitHub, ANTI-RESET vérifié, priorité worklog R381 (re-tester D'ABORD faraid-tanawi-3 lessons[1] pdf-mut23h2v-311, règle cx) — TEST EXÉCUTÉ D'ABORD : INEXÉCUTABLE (cache absent, 404 re-confirmé, 3e tour consécutif) → VEILLE ÉLARGIE par trois voies inédites (Wayback, Common Crawl, chasse à la page mère via l'index du moteur) → canari scripté (règle cy), worklog.

Work Log:
- Ouverture : worklog 14 152 lignes, tail R381, registre 984 (hand 927 + llm 57), fetch origin → rev-list 0/0 (Local = GitHub = 712e5bb) — AUCUNE régression, tous les planchers dépassés (R381 >= R224 ; 984 >= 831 ; 14 152 >= 10 201). Le template cron « hadith-tanawi-1 : 12966, 12967, 12971, 12981… » écarté une VINGT-CINQUIÈME fois — règle h : le tail du worklog est la priorité, et elle y était écrite : RE-TESTER D'ABORD 311.
- Re-test 311 exécuté D'ABORD (règle cx, à la lettre) : cache OCR — ABSENT (content/ocr-cache/ ne porte que pdf-mut23h2v-310 côté série h2v) ; PDF direct 2B0631.PDF — HTTP 404 ; TÉMOIN 117D51.PDF (310, livrée depuis le cache du 15 octobre) — 404 LUI AUSSI : le site a retiré TOUTE la série, pas seulement 311 ; accueil — 200. Troisième tour consécutif de 404 (R380, R381, R382).
- VOIE 4 (inédite) — WAYBACK MACHINE : « The Wayback Machine has not archived that URL » pour 2B0631.PDF (311), 371171.PDF (312), 4F0571.PDF (313) — la tête de la série est HORS ARCHIVE ; la page mère du nouveau chemin — non archivée non plus ; le CDX wildcard (images/2024/*) — timeout depuis la sandbox ET bloqué par le filtre de la plateforme (via WebFetch) : la voie est fermée aux outils présents, le verdict partiel (trois PDF interrogés, zéro capture) est journalisé comme le plus complet obtenu.
- VOIE 5 (inédite) — COMMON CRAWL : l'index le plus récent (CC-MAIN-2026-43, octobre 2026) est joignable via WebFetch mais répond « Html Convert Error » SUR TOUTE REQUÊTE — contrôle positif à l'appui (l'accueil Habous, certainement crawlé, donne LA MÊME erreur) : l'outil est INADAPTÉ au JSONL de l'index, le test est INCONCLUSIF — pas une preuve d'absence ; index.commoncrawl.org est par ailleurs refusé depuis la sandbox (ERR_CONNECTION_REFUSED) comme par le navigateur headless (ERR_CONNECTION_REFUSED). La voie reste OUVERTE en principe, fermée aux outils présents.
- VOIE 6 (inédite, fructueuse en information) — CHASSE À LA PAGE MÈRE : le WebSearch découvre dans l'index du moteur la page mère de la série (« الفرائض الثانوي الثالث عتيق », chemin 1700-المرحلة-الأولى/الفرائض/الفرائض-الثانوي-الثالث-عتيق) dont le snippet liste la série ENTIÈRE : « 1. فقه الحجب (1) ; 2. فقه الحجب (2) ; 3. فقه التعصيب ; 4. تصحيح المسائل وما يعول منها ; 5. تصحيح الانكسار… » — la séquence CONFIRME l'ordre du JSON faraid-tanawi-3 (فقه الحجب (2) = 2e = lessons[1] = 311) ; MAIS l'URL répond 404 en live, et avec elle : la catégorie racine du nouveau chemin, les variantes d'alias, les trois Joomla ID (1700 par option=com_content, /component/content/article/1700), la page listing paginée 1536-الكتب-المدرسية.html?start=10, la page programme 21916 datée 26 déc 2025 dans l'index, la page 896-البرامج — TOUTES 404.
- DIAGNOSTIC (nouveau) : le site est en PLEINE MIGRATION — nginx 1.31.8 en signature des 404, la coquille seule en vie (accueil 6 268 octets, zéro lien dans le HTML brut), l'index du moteur porte encore la structure (crawl récent), aucune archive externe nulle part. Le contenu peut reparaître À TOUT MOMENT, à des URL nouvelles ou anciennes.
- RÈGLE (cy) NOUVELLE : la veille quitte la prose et entre dans l'outillage — scripts-translate/veille-311.sh (canari, 4 sondes : cache OCR, PDF direct, page mère, accueil-témoin ; verdict binaire EXÉCUTABLE/INEXECUTABLE + ACTION explicite) — À EXÉCUTER À CHAQUE TOUR avant tout autre choix ; exécution inaugurale ce tour : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE.
- État git : arbre propre, sync 0/0 à l'ouverture, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — vigilance de mise (les refus réseau aux index externes sont des filtres d'egress, pas des verdicts) ; (b) TOKEN — PAT fonctionnel ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à l'ouverture et au push ; (d) SITE HABOUS en migration — trois tours consécutifs de 404, les archives externes fermées (Wayback : rien ; Common Crawl : invérifiable) — seule issue : la republication, que le canari détectera au tour où elle survient ; (e) le tail du worklog reste l'autorité de priorité à chaque ouverture.
- Plancher suivant : >= R383 / >= 984 (aucun hand-set ce tour — le registre ne bouge que sur livraison) / lignes réelles mesurées post-append (14 152 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de VEILLE ÉLARGIE (aucune leçon — la matière du protocole est ce qui EXISTE, jamais ce qui pourrait exister) : 311 re-testé D'ABORD à la lettre de la règle cx (cache absent, PDF 404, témoin 310 lui aussi 404 — toute la série retirée, 3e tour consécutif) ; SIX voies fermées ou documentées, dont TROIS inédites (Wayback : la tête de la série hors archive, CDX fermé aux outils ; Common Crawl : inconclusif, l'outil ne lit pas l'index — contrôle positif à l'appui ; WebSearch : la page mère découverte dans l'index du moteur, 404 en live) ; le DIAGNOSTIC de migration posé (nginx 1.31.8, coquille seule vivante, index encore peuplé) ; la règle (cy) : le canari devient SCRIPT exécutable (veille-311.sh, 4 sondes, verdict binaire) — exécution inaugurale : INEXECUTABLE.
- RÉSOLU : la question de l'ARCHIVE externe (ni Wayback ni Common Crawl vérifiable ne porte le moindre PDF de la série — côté externe, la perte des rasm est totale aux outils présents) ; la question de la SÉQUENCE (la liste de la page mère au snippet du moteur confirme l'ordre du JSON : فقه الحجب (2) = lessons[1] = 311 — le JSON est juste, le site est absent) ; la question du PROTOCOLE de veille (script canari, 4 sondes, verdict binaire, ACTION explicite — la veille n'est plus une prose à répéter mais un geste à exécuter).
- LEÇONS DU TOUR : (1) L'INDEX DU MOTEUR EST UN SÉDIMENT — le site meurt plus vite que son souvenir : le crawl récent porte la page mère que le serveur ne sert plus ; la veille doit lire le sédiment ET le serveur, jamais l'un sans l'autre. (2) UNE ERREUR N'EST UNE PREUVE QU'AVEC SON CONTRÔLE — le « Html Convert Error » de Common Crawl semblait dire « rien d'archivé » ; le contrôle positif (l'accueil Habous, certainement crawlé, donnant la même erreur) a tranché : l'outil est inadapté, la question reste ouverte — conclure sans contrôle, c'est fabriquer. (3) LA VEILLE EST UN OUTILLAGE, PAS UNE PROSE — trois tours de 404 racontés ; un script de trente lignes transforme la règle en geste : sonde, verdict, ACTION — la continuité du projet se joue dans ces gestes répétables, pas dans leurs récits.
- Prochaine priorité : EXÉCUTER le canari scripts-translate/veille-311.sh À CHAQUE TOUR avant tout autre choix (règles cx-cy) : verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé (le canari et son verdict constituent la matière du tour, avec le diagnostic de migration à actualiser) ; VÉRIFIER rev-list 0/0 + git log frais AVANT tout choix ET AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R382" in tail:
    print("REFUS : R382 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R382 appendé. Worklog : {lines} lignes.")
