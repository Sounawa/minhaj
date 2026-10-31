#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append-R453.py — apposition contrôlée de l'entrée R453 au worklog (garde incluse)."""
import re, sys

ENTRY = """
---
Task ID: R453
Agent: Z.ai Code (agent principal — session web-394d04d3, fenêtre utilisateur ; directives utilisateur : vérification des crons + mandat d'accélération)
Task: Réponse à la double interrogation utilisateur sur les crons (inactivité apparente) + passage du cron de production en v4 avec mandat d'accélération + livraison de la leçon 325 (« L'enfant à naître et le disparu », al-ḥaml wa-l-mafqūd, dars 27, p.193-201, badge « Leçon 17 / 28 », registre attendu 999). Chaîne complète : percée de décodage bbox → 104 comptes vérifiés → rédaction savante → QA navigateur → commit → push → backup.

Work Log:
- CRONS VÉRIFIÉS ACTIFS (la réponse à « POURQUOI LES CRONS NE SONT PAS ACTIVÉS ? ») : le Job 487303 totalisait 91 exécutions, et le dépôt en porte la preuve — les ticks du matin même avaient livré les leçons 322 (09:52), 323 (10:58) et 324 (11:12), registre 996 → 998, chaque livraison poussée (rev-list 0/0). L'apparence d'inactivité venait du travail en tâche de fond entre les messages : le cœur battait toutes les 15 min.
- CRON v4 CRÉÉ (réponse à « tu dois rajouter dans les crons que ca doit accélérer aussi... toujours améliorer la vitesse sans perdre en qualité... pas rester inactif... finir au plus vite la phase de traduction ») : ancien Job 487303 supprimé, nouveau Job 489875 (mêmes créneaux 0 7/15 * * * ? Europe/Paris, priorité 10) dont le payload porte le MANDAT D'ACCÉLÉRATION : ≥ 2 leçons complètes par tick quand la matière le permet ; passes compressées (recalage + extraction + vérification arithmétique en une seule passe d'écriture, jamais relire ce qui est déjà vérifié, conventions rodées réutilisées sans re-démonstration) ; 0 passe VLM quand la couche texte + l'arbitrage arithmétique suffisent ; QA navigateur une seule passe par leçon ; GARDES INTANGIBLES non compressibles (12k+ car avec N.d.T., versets au cache coranique, chaîne QA dans l'ordre, registre à la main, GARDE-DOUBLON, push 0/0).
- LA PERCÉE DU TOUR — LA RECONSTRUCTION BBOX RTL : la tokenisation par caractère de pdftotext -bbox, triée par abscisse décroissante et regroupée par ligne (arrondi de l'ordonnée), lit le BIDI du print presque parfaitement là où -layout ne rend que du charabia et où le VLM libre hallucine. Sur p.193-201 elle a livré d'un trait : le matn d'ouverture («wa-wuqifa l-qismu li-l-ḥamli wa-mālu l-mafqūdi li-l-ḥukmi bi-mawtihi»), la carte de synthèse p.193 (l'exemple-phare résolu d'avance : 6 et 8 concordantes par 2 → 24, pris 9+4, suspendu 11 distribué 3+8 ou 9+2), le commentaire du Muḫtaṣar p.194 (triple doute, lām de terme, le savant ʿAlī), la définition du disparu p.195, le trilogue du Code de la famille p.195-196 (articles 325, 326, 327 — les numéros ARBITRÉS par convergence bbox + VLM + domaine : la bbox seule donne 325 net), les sept étapes p.196-197, la phrase du wafq p.198 («les huit s'accordent avec les six par la moitié... vingt-quatre») et la distribution des prises. MÉTHODE À GÉNÉRALISER : passe bbox d'abord, VLM en zoom binaire UNIQUEMENT sur les zones qui résistent (ici : les quatre tableaux — tous arbitrés par la somme sur la commune — et trois lignes d'énoncés p.201).
- LE TERMINE AL-ĠARAWAYN (« les deux grevées ») : deux occurrences décodées proprement (« car elle est l'une des deux grevées » ; « la mère, avec le père, relève des deux grevées ») ; rendu au translittéré avec N.d.T. qui ne glose que ce que le print montre (le couple conjoint-mère à fractions fixes prélevées successivement, le tiers maternel sur le reliquat — wa-li-l-ummi ṯulṯu mā baqiya étant explicite dans l'hypothèse de vie).
- LA LEÇON 325 LIVRÉE : 34 410 car ; quatre tableaux soldés (exemple-phare tawāfuq : suspendu 11 ; exemple tamāṯul avec la ligne-mystère résolue — l'oncle paternel prend le reliquat 2/6 dans l'hypothèse de mort, la ligne lue à la loupe après trois duels ; application 1 : quatre frères, commune 12, suspendu 3 ; application 2 : commune 216, suspendu 32) ; les trois exercices corrigés — l'énoncé 1 restitué sous N.d.T. (époux/mère/fille de fils disparue : taʿīl 6→7, disjointes 7×6 = 42, suspendu 18 = 3/7, l'issue de mort touchant au bayt al-māl, le radd n'étant que du conjoint seul), l'énoncé 2 (cinq têtes, commune 20, suspendu 4), l'énoncé 3 (époux/mère/deux frères et une sœur/aïeul disparu : 6 et 30 emboîtées → 30, suspendu 10 = le tiers de l'aïeul, la position mālikite de l'aïeul écartant les siblings étant notée) — le spectre complet des quatre regards (identique, emboîté, disjoint, concordant) exercé d'un bout à l'autre du dars.
- GARDES ET QA : verify-325-mafqud.py : 104 COMPTES EXACTS, 0 échec ; qa-lesson.py : 0 arabe, 0 apostrophe droite, guillemets et balises appariés ; hand-set.py : registre 999 (hand 942 + llm 57) ; navigateur desktop 1280 + mobile 390 : 0 overflow de contenu, 0 erreur console, h1 « L'enfant à naître et le disparu » et badge « Leçon 17 / 28 » au DOM, captures ×2. Les verdicts VLM « PROBLEME » sur les captures ont été ARBITRÉS PAR DOM : le bouton flottant allégué n'existe pas au DOM, le titre arabe « lu » par le VLM est une invention pure (aucun nœud arabe hors branding du site) — doctrine R451/R452 confirmée une CINQUIÈME fois : le VLM libre hallucine, le DOM et la somme arbitrent. 0 verset coranique cité dans ce dars (matn + Mudawana seulement) : la porte verify-quran est passante par vacuité.
- TITRES DU SLOT 15 CORRIGÉS : le pré-câblage portait le doublon obsolète du dars 26 (al-ʿamal fī l-waṣāyā / L'exécution des legs testamentaires) ; remplacés par الحمل والمفقود / L'enfant à naître et le disparu.
- CANARI : PORTE|FERMÉE (bannière de maintenance toujours présente — règle cx'', la production continue sur le miroir).
- PUSH : 5f90b5c..723def3, rev-list 0/0 vérifié APRÈS push ; backup OK (723def3).

Stage Summary:
- Registre : 999 leçons savantes livrées (hand 942 + llm 57). Position : R453 close, push 0/0.
- Leçons du tour : (1) la reconstruction bbox RTL par coordonnées est la nouvelle passe de décodage par défaut — plus rapide ET plus fiable que le VLM pour la prose, le VLM restant l'arbitre de dernier recours en zoom binaire ; (2) l'accélération se fait en comprimant les passes, jamais les gardes — les 104 comptes, la chaîne QA et la double vérité N.d.T. sont restés intacts pendant que le tour tenait en une seule fenêtre ; (3) la carte des slots restants du volume est FAUSSE en ses titres pré-câblés (11 slots vides contre ~4 blocs réels : activités p.202-204, قسمة/قواعد p.205-207, bibliographie p.208-209, فهرس p.210+) — le recalage page à page reste l'ouverture obligée de chaque pièce jusqu'à la clôture du volume.
- Prochaine priorité : (1) LIVRER LA LEÇON 326 après recalage de la structure réelle p.202-204 (le bloc أنشطة الدعم والتثبيت de la troisième unité — son titre de slot pré-câblé est erroné et devra être corrigé comme celui du slot 15) ; (2) puis le bloc قسمة التركة / قواعد القرافي p.205-207, la bibliographie et l'index pour clôturer le volume ; (3) les slots sans contenu réel correspondant seront tranchés au recalage (consolidation ou renvoi) — MIEUX VAUT la vérité de la structure que le remplissage des cases ; (4) puis tafsir-5ep (91 leçons) et hadith-2es ; (5) canari en second à chaque tour ; (6) APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md : balayer le fichier entier, refuser tout ID <= dernier apposé). La règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with open('worklog.md', 'r', encoding='utf-8') as f:
    content = f.read()

ids = [int(m) for m in re.findall(r'Task ID:\s*R(\d+)', content)]
last = max(ids) if ids else 0
if last >= 453:
    print(f"GARDE-DOUBLON REFUSÉ : dernier Task ID = {last} >= 453")
    sys.exit(1)

with open('worklog.md', 'a', encoding='utf-8') as f:
    f.write(ENTRY)
print(f"R453 apposé après R{last} ; worklog → {content.count(chr(10)) + 1 + ENTRY.count(chr(10))} lignes")
