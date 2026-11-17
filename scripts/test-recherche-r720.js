#!/usr/bin/env node
// Test de recherche R720 : charge les index comme le navigateur, vérifie
// la présence des nouveaux commentaires dans l'index de recherche.
import { readFileSync } from 'fs';
const shims = {};
for (const f of ['recherche/index-ep.js', 'recherche/index-es.js', 'recherche/index-tanawi.js', 'recherche/index-titres.js']) {
  const txt = readFileSync(f, 'utf8');
  const fn = new Function('window', txt + '; return window;');
  shims[f] = fn({ MINHAJ_INDEX: undefined, MINHAJ_TEXTE: undefined });
}
// titres
const titres = shims['recherche/index-titres.js'].MINHAJ_INDEX;
console.log('titres : livres', titres.books.length);
// textes (fragments push)
const textes = [];
for (const f of ['recherche/index-ep.js', 'recherche/index-es.js', 'recherche/index-tanawi.js']) {
  const fn = new Function('window', readFileSync(f, 'utf8') + '; return window;');
  const w = fn({});
  textes.push(...(w.MINHAJ_TEXTE || []));
}
console.log('fragments texte : cycles', textes.length);
let docs = [];
for (const c of textes) docs.push(...(c.paires || []));
console.log('paires texte :', docs.length);
const hay = d => (d.x || '');
console.log('العمرة →', docs.filter(d => hay(d).includes('العمرة')).length, 'résultats');
console.log('الفدية →', docs.filter(d => hay(d).includes('الفدية')).length, 'résultats');
const d412 = docs.find(d => JSON.stringify(d).includes('412'));
const d411 = docs.find(d => JSON.stringify(d).includes('pdf-mut23h2x-411'));
console.log('411 présent dans l’index texte :', !!d411);
console.log('411 contient شرح الدرس :', d411 ? hay(d411).includes('شرح الدرس') : 'n/a');
console.log('extrait 411 (entête commentaire) :', d411 ? hay(d411).slice(0, 100) : '');
