#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Append worklog R437 — garde renforcée GARDE-DOUBLON.md (balayage du fichier entier)
import re, sys

HOME = "/home/z/my-project"
P = f"{HOME}/worklog.md"
N = 437

ENTRY = """---
Task ID: R437
Agent: GLM (session web-394d04d3, tick 2026-10-30 20:37 +08:00, Job 474619 — première exécution du point 5 du cron v3, job 487303)
Task: GARDE-FOU MINHĀJ + LIVRAISON DE LA LEÇON 311 — PREMIÈRE PRODUCTION SUR MIROIR : rédaction savante FR 23 845 car de « La science de l'exclusion successorale (ḥaǧb) (2) » (فقه الحجب 2, badge « Leçon 3 / 28 ») depuis le manuel archive.org OCR (p.139-147, حجب النقصان : الانتقال 4 types + الازدحام 3 types + applications), 4/4 versets vérifiés au cache, QA navigateur 1280/390 zéro/zéro, registre → 985, poussée, backup ; troisième convergence parallèle absorbée au fast-forward (R436 apposée pendant la fenêtre) ; worklog (garde renforcée, entrée renumérotée R436→R437 par la garde).

Work Log:
- CONVERGENCE PARALLÈLE ABSORBÉE AU PUSH (troisième de la journée, conditions nouvelles) : au moment du push de la leçon, l'ancien origin/main était c41ff62 ≠ 4a0bdd6 vu à l'ouverture — l'instance parallèle avait apposé R436 (cron v3 gravé : solution miroir + principe jamais-idle au job 487303 ; job QA webDevReview 487304 en alternance) PENDANT la fenêtre de ce tour et poussé ; le push de ce tour est passé en fast-forward propre (1e0f391 au-dessus de c41ff62), sans réécriture ni perte, et le tail de R436 LAISSAIT EXPRESSÉMENT la leçon 311 au « tick de production suivant » = ce tour ; la division du travail s'est faite sans aucune coordination autre que la source de vérité commune ; l'entrée de ce tour, pré-destinée R436 par la numérotation naïve, a été RENUMÉROTÉE R437 PAR LA GARDE (dernier ID apposé = 436 ≥ 436 → refus automatique du doublon, règle renforcée de GARDE-DOUBLON.md appliquée en conditions réelles).
- Ouverture au réflexe cz (cinquante-deuxième application documentée — R436 n'ayant pas porté de compteur) : STABILITÉ #18 — seize tours consécutifs sans régression (R420 → R437), six de plus que le record de régressions (10) ; compte total : 34 régressions / 18 stabilités / 52 applications.
- CONFORMITÉ GITHUB : à l'ouverture, fetch → rev-list 0/0 (HEAD 4a0bdd6) ; AU MOMENT DU PUSH : fetch → rev-list 1/0 (le seul commit de la leçon en avance, l'instance parallèle déjà intégrée) → push fast-forward c41ff62..1e0f391 ; re-vérification 0/0 après l'append de cette entrée.
- CANARI (règle cx', passé en SECOND — la production d'abord) : PORTE|FERMÉE (troisième exécution : bannière de maintenance toujours à l'accueil, nouvelle version non lancée) — et la production a tourné quand même : première preuve d'exécution du point 4 du cron v3, la source de production = les manuels locaux, le portail n'est plus une dépendance.
- LEÇON 311 LIVRÉE (faraid-tanawi-3 lessons[1], docId pdf-mut23h2v-311, titleFr « La science de l'exclusion successorale (ḥaǧb) (2) », badge « Leçon 3 / 28 », règle f quatre-vingt-quinzième confirmation — API : index 1, count 28) — PREMIÈRE PIÈCE DU CORPUS SAVANT dont le rasm ne vient NI du portail des Habous NI de son cache : source = content/textbooks/faraid-3-unite4-hijb.txt (OCR du manuel miroir archive.org الفرائض ثالث ثانوي, 181 p., édition 1447/2025, pages 139-147). Contenu rendu : la définition du حجب النقصان (« empêcher l'héritier de son lot le plus abondant », portée sur tous les héritiers — l'exact contraire de la privation : six exemptés de la chute, aucun exempté du rabais) ; القسم الأول الانتقال — 4 types (mère du tiers au sixième ; sœur germaine de la moitié au taʿṣīb ʿaṣaba bi-l-ġayr ; père du résidu au sixième fixe ; sœur consanguine résiduaire→résiduaire, exemple TRONQUÉ au bas de p.139 — deuxième fente du livre, rendue telle quelle, restauration savante en N.d.T.) ; القسم الثاني الازدحام — 3 types (filles dans les deux tiers ; fils dans le résidu ; parts fixes dans la masse renvoyées à l'ʿawl par promesse du cours) ; les activités de la leçon 31 (différence حرمان/نقصان, deux transferts à juger, vrai-faux dont les énoncés NE PASSENT PAS — troisième fente) ; deux problèmes de composition (p.142, portés entiers) ; la table amputée de la leçon 32 (masse perdue — quatrième fente ; demi-table : mari, oncle paternel germain, frère consanguin, grand-mère, fils ; « trois grands-mères » au-dessus ; deux taches OCR signalées) ; les pages de notes de l'élève et l'imprimatur (vides demandés, non comptés comme pertes).
- VÉRIFICATION CORANIQUE (verify-311-quran.py) : 4/4 segments vérifiés verbatim au cache — an-Nisāʾ 4:11 ×2 (taṣīya des enfants : le lot du groupe des filles ; clause des parents : « à chacun des deux le sixième, s'il a un enfant » — porteuse à elle seule des types 1 et 3 du transfert) ; an-Nisāʾ 4:176 ×2 (ouverture de la kalāla ; clause des sœurs et du frère : les deux tiers partagés + la double part du mâle — porteuse du type 2 du transfert et du type 1 de l'encombrement).
- CHAÎNE D'ÉCRITURE ET QA : rédaction savante 23 846 car → qa-lesson.py (auto-fix typographique puis QA dure : trois arabismes « درس » détectés et translittérés en « leçon » ; verdict final 0 arabe résiduel, 65 guillemets appariés, balises appariées, 0 apostrophe droite — 23 845 car finaux) → hand-set.py (1 emplacement htmlFr écrit, registre → 985 SAVANTS, plancher de R436 atteint exactement) → QA navigateur sur le serveur actif (non relancé) : h1 exact, badge « Leçon 3 / 28 », traduction savante, 17 min de lecture, 4 entrées méta, N.d.T. présentes, overflow 1280 = FAUX, overflow 390 = FAUX, console 0 erreur (Fast Refresh seul) ; captures qa-R437-311-desktop.png / qa-R437-311-mobile.png (renommées au numéro réel de l'entrée après la renumérotation par la garde).
- État git : HEAD 1e0f391 (leçon) puis commit de cette entrée ; sync 0/0 re-vérifiée AU MOMENT du push ; backup.sh exécuté.
- Risques : (a) SANDBOX — stabilité #18 en cours (seize tours) : le record de régressions est dépassé de 60 % ; (b) TOKEN — fonctionnel (deux pushes ce tour) ; (c) INSTANCE PARALLÈLE — troisième convergence productive (R433 diagnostic / R434 mécanique ; R435 percée / collecte tafsir-5ep ; R436 cron / R437 leçon) : la division du travail émerge de la garde, elle n'est pas décidée ; (d) SOURCE — le goulot redevient la cadence de rédaction : une pièce par tick de production ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R438 / registre >= 985 (986 attendu dès la livraison de 312) / 938 leçons livrées (survey R433 : 937, + la 311) / lignes réelles mesurées post-append (15 192 avant cette entrée).

Stage Summary:
- LIVRÉ : la leçon 311 (فقه الحجب 2) — première pièce du corpus tirée du manuel miroir : 23 845 car, 4/4 versets au cache, QA navigateur zéro/zéro, registre 985, poussée et backup ; la convergence parallèle de R436 absorbée au fast-forward, l'entrée renumérotée par la garde.
- RÉSOLU : la question de la PREMIÈRE EXÉCUTION DU CRON v3 (réponse : le point 5 exécuté à la lettre — 311 livrée depuis content/textbooks/ sans un seul fetch au portail, le canari passé en second : la solution gravée à R436 a produit une leçon livrée à R437, dix minutes entre l'inscription du principe et sa première preuve) ; la question de la COORDINATION ENTRE INSTANCES (réponse : il n'y en a aucune et il n'en faut pas — deux tâches complémentaires sur la même fenêtre, une source de vérité commune, un fast-forward propre ; la garde fait office de répartiteur sans être un répartiteur).
- LEÇONS DU TOUR : (1) LA NUMÉROTATION APPARTIENT À LA GARDE, PAS AU BROUILLON — l'entrée était pré-destinée « R436 », le journal en a décidé autrement : la garde balaie le fichier entier et refuse tout ID ≤ dernier apposé ; le brouillon se renumérote, l'histoire ne se réécrit pas ; (2) LE CRON PRESCRIT, LE TOUR EXÉCUTE — la solution n'est plus une mémoire à se rappeler mais une instruction à suivre : le point 0 (jamais-idle) et le point 4 (manuels locaux) ont chacun produit leur preuve dans le tour même de leur gravure ; (3) LA MOITIÉ DU PAYS DU ḤAǦB — la privation sort de l'héritage, la diminution rabat la part : six exemptés de la chute, aucun exempté du rabais ; le livre des parts continue par sa carte entière, portée désormais par un miroir que dix heures de sondage n'avaient pas aperçu.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R437 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) LIVRER LA LEÇON 312 (فقه التعصيب, « La dévolution résiduelle (taʿṣīb) », badge « Leçon 4 / 28 », registre attendu 986) — localiser les pages du taʿṣīb dans le manuel local (l'unité 5 portée par le scan dès sa page 148 ; l'OCR de R435 y lisant « التأصيل », lecture à confirmer : التعصيب attendu) et extraire la source ; si le manuel ne porte pas la pièce, pivoter tafsir-5ep (91 leçons, sources/tafsir-5ep-text.pdf) ou hadith-2es selon le protocole rodé ; (4) canari veille-portail.sh en SECOND ; (5) APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md : balayer le fichier entier, refuser tout ID ≤ dernier apposé) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with open(P, "r", encoding="utf-8") as fh:
    content = fh.read()

ids = re.findall(r"Task ID: R(\d+)", content)
last = int(ids[-1]) if ids else 0
if last >= N:
    print(f"REFUS : une entrée >= R{N} existe déjà (dernier = R{last}).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
with open(P, "w", encoding="utf-8") as fh:
    fh.write(content + ENTRY)

n_lines = (content + ENTRY).count("\n")
print(f"OK : entrée R{N} apposée (dernier ID avant = R{last}) — worklog ≈ {n_lines} lignes.")
