#!/usr/bin/env python3
"""R776 — append de l'entrée worklog sous garde anti-doublon renforcée
(GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé
et tout doublon de l'ID nouveau)."""
import re, sys

CHEMIN = 'worklog.md'
ID = 'R776'

ENTREE = """## R776 — 2026-11-21 — IA-1 — commentaires hadith-tanawi-1 13124 (leçon 21 عدة المتوفى عنها زوجها — la viduité de la femme dont l'époux est décédé, la vingt-unième du livre, étiquetée leçon 24 par la couche du CMS (الدرس 24) — étiquette CONCORDANTE au badge imprimé الدرس 24 (page 132) — suite du fil après R775)

- REPRISE : fetch GitHub avant le push (règle R109) — la vague a été rédigée sur la base 496a1662 (R775) poussée ce même tour ; bac intact, production SOLO (« continue la traduction solo ») — IA-2 et IA-3 restent détachées.
- MISSION ANNEXE DE L'UTILISATEUR (chemin de récupération des documents du portail habous) : revérifiée intacte — scripts-translate/SOLUTION-OUVRAGES.md (R458) + fetch-habous-page.py + 45 manuels content/textbooks-src/ — le manuel hadith-1-thanawi_text.pdf sert à la vérification des badges (page 132 lue) ; rien à réécrire.
- DISQUE : sandbox de nouveau plein (100 %, 0 disponible) — causé par un tmp_pack orphelin de 636 Mo laissé par le fetch de R775 (comme le 688 Mo de R774) — libération : tmp_pack supprimé, cache puppeteer (617 Mo), git prune-packed (.git/objects 1,8 → 1,2 Go) ; LEÇON consignée : après chaque fetch/push, vérifier et supprimer .git/objects/pack/tmp_pack_* — les fetch créent des tmp packs qui restent orphelins si le disque se remplit.
- RÉDACTION : comm-r776-c21.py — 4787 mots (resume+explication+points ; échelle du livre 4000-4800 respectée — leçon de 22 090 car débalisés), vocab 8 sans harakat (العدة، المبتوتة، النفاس، وضع الحمل، قد حللت، دفن، أقصى الأجلين، العزل — lemmes de la couche arabe), 135 citations verbatim 0 manquant (corpus htmlFr débalisé), recoupements 6/6 PASS (13122 contraint [précédente immédiate] ; 13124 mubtūta [leçon même] ; 13115 Fatima [le logement de la mubtūta] ; 13117 mubtūta [le recueil] ; 13114 cycles ; 13121 Rushd [le petit-fils — la leçon distingue al-Jadd]) ; clef = la retraite du décès, la plus simple au compte et la plus grave au sens (quatre mois et dix par le Livre, la Sunna et l'ijmāʿ — la mise au monde pour l'enceinte, fût-elle survenue avant même la sépulture — « le droit de la femme se joue sur le fait naturel, non sur la cérémonie ») et la demeure comme courtoisie et non comme saisie (« la retraite du décès se tient dans la maison du deuil, non par saisie, mais par une courtoisie que le droit et le naturel d'accord imposent ») ; appareil : 1866 (la double fatwa Ibn ʿUmar + ʿUmar via l'homme des Anṣār — la glose de la cassure du qāf), 1867 (Subayʿa al-Aslamiyya via al-Miswar ibn Makhrama par Hishām ibn ʿUrwa et son père — trois moments : mise au monde, purification des lochies, licence), 1873 (la coutume d'Ibn ʿUmar — la veuve et la mubtūta), 1887 (le deuil trois nuits, l'époux quatre mois et dix — « le deuil et la retraite se recouvrent chez la veuve en un même terme »), 1869 (al-Furayʿa bint Mālik ibn Sinān, sœur d'Abū Saʿīd al-Khudrī — « Demeure dans ta maison, jusqu'à ce que le Livre atteigne son terme » — ʿUthmān « il le suivit et jugea par lui »), 1865 et 1868 (les voies multiples de Subayʿa — Umm Salama + le sceau de Mālik) ; Ibn ʿAbd al-Barr (le hadith dit de Saʿīd ibn Isḥāq, célèbre du Ḥijāz et de l'Irāq — Mālik, ash-Shāfiʿī, Abū Ḥanīfa, ath-Thawrī, al-Awzāʾī, al-Layth, Aḥmad — la demeure « à elle ou à son époux »), le hadith des palmiers (Muslim de Jābir) et le qāḍī ʿIyāḍ (la sortie de jour — « l'émondage (jidār) n'a lieu que de jour ») ; la sagesse triple (adoration, droit de l'époux, pureté du sein barāʾat ar-raḥim) ; l'exploitation d'Ibn Rushd al-Jadd (les Préliminaires exhaustives 1/513, édition at-Tajkānī — le grand-père, distinct du petit-fils) : trois lectures (la mise au monde seule — l'école ; l'abrogation refusée par la règle des sources ; Ibn ʿAbbās — le plus long des deux termes) ; compteur site 78 → 79/1846.
- RECTIFICATION DU REGISTRE DES ÉCARTS D'ÉTIQUETAGE (découverte majeure) : le comptage canonique est celui de la chaîne de traduction (commits d'octobre 2026, vérifiés dans l'historique git) : n°44-46 (13114 — b653ff5c), n°47-49 (13117 — 37420fe2), n°50-52 (13124 — 1b9cea5b : 2:232 imprimé ×3 → 2:234), n°53-54 (13136 — a8ab06fd), n°55 (13624 — 78d615ba) — cumul canonique 55 ; les entrées R772-R774 du worklog (« le registre demeure 49 écarts ») ne voyaient que les leçons qu'elles commentaient ; l'entrée R775 avait numéroté la divergence « verset : 227 » de 13122 « 50ᵉ écart » PAR COLLISION (le rang 50 était déjà pris) ; RECTIFIÉ : la divergence 227 (une divergence d'étiquette, répétée à trois emplacements) occupe les rangs 56ᵉ-58ᵉ ; le TEXTE ÉDITORIAL du commentaire 13122 (explication 4) corrigé en conséquence par comm-r776-c21.py (notre propre texte, non le corpus — aucune donnée de leçon modifiée) ; les vérifications futures porteront le cumul canonique 55 + rangs suivants.
- NB consignés sans correction : l'étiquette de la couche CMS (الدرس 24) pour la vingt-unième du livre est CONCORDANTE au badge imprimé (الدرس 24, page 132 du PDF) — la série des étiquettes CMS (22-26 pour les leçons 16-20, toutes +3) revient au badge pour cette leçon ; le duplicata « vingt-quatrième » (13117 et 13124 portent la même étiquette CMS) vient donc des étiquettes de la couche CMS, non des badges imprimés (21 et 24 au PDF) — raffine la vérification R775 et la note du traducteur de la leçon (« la compilation du manuel mêle deux séries d'origine et double ses numéros ») ; les écarts coraniques de la leçon DÉJÀ CONSIGNÉS par ses propres notes du traducteur (2:232 imprimé ×3 → 2:234 restauré — écarts 50ᵉ-52ᵉ canoniques ; aṭ-Ṭalāq 4 ×2 concordantes — vérifiées au cache) — le commentaire les rapporte sans nouvelle vérification ; l'en-tête porte « enseignement préparatoire traditionnel » là où les leçons voisines portent « secondaire » (déjà noté par la leçon elle-même) ; le titleAr du CMS tronqué (عدة المتوفى عنها زوجها, sans من كتاب الحديث…) — le h1 arabe porte le titre plein ; la numérotation du Muwaṭṭaʾ (1866, 1867, 1873, 1887, 1869, 1865, 1868) portée par la leçon — concordante ; 0 coquille FR nouvelle relevée.
- QA : build --publier . : 1357 pages + 1369 racine, traduction savante 1291/1291 (0 en attente), commentaires 79/1846, transcrites 1227/1782 (inchangées) ; qa-liens 1360×24866 PASS (0 404) ; qa-onglets 43/43 PASS (hors-ligne 30,2 Mo, console sans erreur) ; qa-apparat 2724 PASS (données intouchées) ; qa-structure h1 PASS (chantier h2 préexistant) ; recherche : contenu 13124 présent dans recherche/index-tanawi.js et miroir site ; miroir racine octet pour octet (13124.html, 13122.html, index.html identiques site↔racine) ; page leçon 13124 Commentaire pédagogique + « IA-1, tour R776 » + Furayʿa présents ; page leçon 13122 porte la rectification (56ᵉ-58ᵉ) ; page du livre « ✧ 21 commentaires pédagogiques rédigés dans ce manuel » ; accueil « 79 / 1782 » ; avancement « 79 commentaires » ; avertissement build préexistant reconsigné (miroir racine savant-registry divergent du registre scripts-translate) ; scripts/comm-r776-c21.py ; worklog R776 ; trace 1a1fde04c594b579
- SUIVANT : hadith-tanawi-1 21/30 — reste 9 leçons (13135 — le chapitre du retrait, l'ʿazl [annoncé par la préparation de 13124], puis 13136, 13623, 13624, 13625, 13649, 13740, 13758, 13768) ; l'ensemble des zones reste sous IA-1 (production solo) ; surveiller toute pose concurrente ; fetch GitHub avant toute reprise (règle R109) et nettoyer les tmp_pack_* après chaque fetch.
- trace 1a1fde04c594b579
"""

def main() -> None:
    with open(CHEMIN, encoding='utf-8') as f:
        contenu = f.read()
    ids = re.findall(r'^## (R\d+[a-z]?)', contenu, flags=re.M)
    if not ids:
        raise SystemExit('!! aucun ID trouvé — garde bloquée')
    if re.search(r'^## ' + ID + r'\b', contenu, flags=re.M):
        raise SystemExit(f'!! {ID} déjà apposé — garde bloquée')
    dernier = ids[-1]
    n_dernier = int(re.match(r'R(\d+)', dernier).group(1))
    n_nouveau = int(re.match(r'R(\d+)', ID).group(1))
    print('dernier ID apposé :', dernier, '| nouveau :', ID)
    if n_nouveau <= n_dernier:
        raise SystemExit(f'!! {ID} ≤ {dernier} — garde bloquée')
    if not contenu.endswith('\n'):
        contenu += '\n'
    with open(CHEMIN, 'a', encoding='utf-8') as f:
        f.write(ENTREE)
    print('append OK —', ENTREE.splitlines()[0][:110])

if __name__ == '__main__':
    main()
