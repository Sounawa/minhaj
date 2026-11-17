#!/usr/bin/env node
/* Test du moteur de recherche Minhaj : index des titres seul, puis
 * enrichissement par fragments de texte (ajouterTexte). Usage :
 *   node scripts/test-recherche.js [repertoire-site]
 * Sortie : résultats FR et AR aux deux étapes + verifications. */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const site = process.argv[2] || path.join(__dirname, '..', 'site');
const ctx = { window: {}, console };
vm.createContext(ctx);
ctx.window = ctx;

function charger(fichier, label) {
  const code = fs.readFileSync(path.join(site, fichier), 'utf8');
  vm.runInContext(code, ctx, { filename: fichier });
  console.log('charge :', fichier, '(' + (code.length / 1024).toFixed(0) + ' Kio)', '-', label);
}

function chercher(q) {
  const r = vm.runInContext('MinhajRecherche.chercher(' + JSON.stringify(q) + ')', ctx);
  return r;
}

function resume(r, limit) {
  const lignes = r.resultats.slice(0, limit || 3).map(x =>
    (x.type === 'livre' ? '[livre] ' : '[leçon] ') + x.titre +
    (x.extrait ? ' | extrait: ' + x.extrait.slice(0, 40).replace(/<[^>]+>/g, '') + '…' : ' | (sans extrait)'));
  return lignes.join('\n');
}

charger('recherche.js', 'moteur');
charger('recherche/index-titres.js', 'index des titres');
vm.runInContext('MinhajRecherche.definirDonnees(window.MINHAJ_INDEX); window.MINHAJ_INDEX=null;', ctx);
console.log('prêt (titres) :', vm.runInContext('MinhajRecherche.pret()', ctx));

let ok = true;
const tests = [
  ['riyad salihin', 'FR', 1],
  ['mukhtasar akhdari', 'FR', 1],
  ['الجلالين', 'AR', 2]
];
for (const [q, langue, minAvant] of tests) {
  const r = chercher(q);
  console.log(`\n== « ${q} » (${langue}) — titres seuls : ${r.total} résultats`);
  console.log(resume(r));
  if (r.total < minAvant) { console.log('!! trop peu de résultats au stade titres'); ok = false; }
}

/* fragment collège chargé en arrière-plan -> enrichissement */
const epAvant = chercher('salihin').total;
charger('recherche/index-es.js', 'fragment collège');
const nb1 = vm.runInContext('(function(){var n=MinhajRecherche.ajouterTexte(window.MINHAJ_TEXTE); window.MINHAJ_TEXTE=null; return n;})()', ctx);
console.log('\najouterTexte(collège) :', nb1, 'documents enrichis');
const r3 = chercher('الجلالين');
console.log(`== « الجلالين » après fragment : ${r3.total} résultats`);
console.log(resume(r3, 2));
if (!r3.total) { console.log('!! aucun résultat arabe'); ok = false; }

/* fragment primaire + lycée : couverture complète */
charger('recherche/index-ep.js', 'fragment primaire');
charger('recherche/index-tanawi.js', 'fragment lycée');
const nb23 = vm.runInContext('(function(){var n=MinhajRecherche.ajouterTexte(window.MINHAJ_TEXTE); window.MINHAJ_TEXTE=null; return n;})()', ctx);
console.log('ajouterTexte(primaire + lycée) :', nb23, 'documents enrichis');
const rTous = chercher('الجلالين');
console.log(`== « الجلالين » avec les 3 fragments : ${rTous.total} résultats (titres seuls : ${chercher('zzz-inexistant-xyz').total})`);
const avecExtrait = rTous.resultats.filter(x => x.type === 'lecon' && x.extrait).length;
console.log('résultats avec extrait :', avecExtrait, '/', rTous.resultats.filter(x => x.type === 'lecon').length);
if (!avecExtrait) { console.log('!! aucun extrait après fragments'); ok = false; }

/* R722 : le contenu des commentaires pédagogiques (شرح الدرس) est indexé —
 * « guide de lecture » n'apparaît que dans les résumés des commentaires. */
const rComm = chercher('guide de lecture');
const nCommLecons = rComm.resultats.filter(x => x.type === 'lecon').length;
console.log(`== « guide de lecture » (contenu des commentaires) : ${rComm.total} résultats, dont ${nCommLecons} leçons`);
if (nCommLecons < 12) { console.log('!! les commentaires pédagogiques ne sont pas indexés'); ok = false; }

console.log('\n' + (ok ? 'TEST RECHERCHE : PASS' : 'TEST RECHERCHE : ECHEC'));
process.exit(ok ? 0 : 1);
