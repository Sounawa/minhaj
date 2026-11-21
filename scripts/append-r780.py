#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R780 — append de l'entrée worklog (convention maison des vagues IA-1).
Aucun identifiant embarqué : le push se fait par la commande git du tour."""

from pathlib import Path

ENTREE = """
## R780 — 2026-11-21 — IA-1 — correction données hadith-tanawi-3 leçons 10-20 (éradication des 18 463 plages « ?? » réintroduites par les poses) + audit tokens de la zone IA-1 (consigne IA-2 Z2-49, suite du fil après R779 — tour « traduction seule », commentaires suspendus)

- DÉFAUT ÉRADICÉ : les pages rendues pdf-mut23h2n-10 à -20 affichaient des séquences « ?? » visibles (18 831 occurrences « ?? » = 18 463 plages de 2 à 4 « ? ») — le MÊME glyphe d'espace inter-mots perdu que le défaut R700-R712 corrigé par r721-corrige-ht3.py pour les leçons 1-9 ; les poses W21-W23/R741/R743/R778/R779 l'avaient réintroduit en tenant leurs couches OCR défectueuses (les « séparateurs » comptés dans leurs QA de pose) et laissé dans les htmlFr — visibles en ligne sur 11 pages depuis leurs poussées.
- CORRECTION : scripts/r780-corrige-ht3-10-20.py (précédent r721) — sémantique par plage « \\?{2,} » : plage entourée de DEUX caractères de mot → espace (0 cas réel — zéro jonction lettre|lettre vérifiée par catégories Unicode), sinon suppression (18 463/18 463 supprimées) ; le « ؟ » traité comme ponctuation (v2 après restauration du fichier : 0 espace parasite avant lui, « أَمْ لَا؟ ذَهَبَ » rendu correctement) ; les « ? » isolés français et de consigne intouchés (164 restants) ; les marqueurs d'arbitrage « [؟] » CONSERVÉS (1053 — consignations délibérées des poses, documentées W21-W23, absentes des leçons 1-9 mais propres au livre) ; intouchabilité champ par champ (html, titleAr, titleFr et tout champ non-htmlFr identiques byte à byte) ; delta ASCII « ? » = 37 662 exactement (368 plages quadruples comptées deux fois par substr : 18 831 − 368 = 18 463) ; structure intacte : 5886 spans RTL, guillemets « 1115 / » 1115, ﷺ 198.
- TOKENS (consigne IA-2 Z2-49 intégrée à R779 — nettoyage de la zone IA-1 à ce tour) : AUDIT COMPLET — le PAT courant (ghp_IqmWwp…) est absent de tout fichier tracké (0 occurrence) ; les 45 mentions « ghp_ » de worklog.md et les 9 des scripts-translate/append-r*.py sont des PRÉFIXES TRONQUÉS non exploitables (conventions d'écriture des sessions antérieures) ; l'unique quasi-littérale ghp_Qoqck (9 car, session R103) rédigée → « ghp_… » ; 0 token complet dans l'arbre après audit ; worklog-ia2.md / worklog-ia3.md NON TOUCHÉS (zones IA-2/IA-3) ; la purge de l'historique git reste au propriétaire après révocation du PAT (recommandée R777).
- QA BUILD --publier . : pages 1366 + 1378 racine, transcrites 1236/1782 (546 restantes — inchangées : aucune leçon ajoutée au tour), savante 1300/1300, commentaires 79/1846 (inchangés) ; 0 « ?? » sur les 11 pages corrigées (racine + miroir site/), 0 dans recherche/index-tanawi.js, hors-ligne.html, index.html, avancement.html ; « [؟] » présents au rendu (7 sur la page leçon 20) ; avertissement préexistant reconsigné (miroir racine savant-registry divergent du registre scripts-translate — qui fait foi).
- SUIVANT : zone IA-1 — hadith-tanawi-3 leçon 21 (مَا لَا يَجُوزُ مِنَ النُّحُولِ وَالْعَطِيَّةِ, p.145 et suiv., manuel compilé en dépôt) ; fetch avant toute reprise (R109), nettoyer les tmp_pack_* ; superviseur vivant (chasse des manuels restants de la zone).
- trace 1a1fe8a4883570f9
"""

fichier = Path(__file__).resolve().parent.parent / 'worklog.md'
cru = fichier.read_text(encoding='utf-8')
if 'trace 1a1fe8a4883570f9' in cru:
    raise SystemExit('entrée R780 déjà présente — idempotence')
if not cru.endswith('\n'):
    cru += '\n'
fichier.write_text(cru + ENTREE.lstrip('\n'), encoding='utf-8')
print('worklog.md : entrée R780 ajoutée (', len(ENTREE), 'car )')
