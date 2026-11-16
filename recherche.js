/* Moteur de recherche du Minhaj — JS pur, aucune dépendance.
 * Recherche par titre et par texte des leçons transcrites, en français
 * comme en arabe : la requête et l'index sont normalisés de la même façon
 * (voyelles courtes arabes retirées, hamzas unifiées, accents français retirés).
 * L'extrait affiché est recadré dans le texte d'origine (arabe vocalisé conservé).
 */
(function (globale) {
'use strict';

/* Normalisation rapide (utilisée sur tout l'index à la première recherche). */
function normaliser(s) {
  return String(s).toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]/g, '')
    .replace(/[\u0623\u0625\u0622\u0671]/g, '\u0627')
    .replace(/\u0649/g, '\u064a')
    .replace(/\u0153/g, 'oe').replace(/\u00e6/g, 'ae')
    .replace(/\s+/g, ' ').trim();
}

/* Normalisation avec carte vers les positions d'origine (pour les extraits).
 * Règles identiques à normaliser() : les positions restent donc alignées. */
function normaliserCarte(s) {
  var t = '', m = [], esp = true;
  for (var i = 0; i < s.length; i++) {
    var d = s.charAt(i).toLowerCase().normalize('NFD');
    for (var j = 0; j < d.length; j++) {
      var c = d.charAt(j), k = d.charCodeAt(j);
      if ((k >= 0x0300 && k <= 0x036f) || (k >= 0x0610 && k <= 0x061a) ||
          (k >= 0x064b && k <= 0x065f) || k === 0x0670 || k === 0x0640 ||
          (k >= 0x06d6 && k <= 0x06ed)) continue;
      var reps;
      if (k === 0x0623 || k === 0x0625 || k === 0x0622 || k === 0x0671) reps = ['\u0627'];
      else if (k === 0x0649) reps = ['\u064a'];
      else if (k === 0x0153) reps = ['o', 'e'];
      else if (k === 0x00e6) reps = ['a', 'e'];
      else reps = [c];
      for (var q = 0; q < reps.length; q++) {
        var rc = reps[q];
        if (/\s/.test(rc)) { if (!esp) { t += ' '; m.push(i); esp = true; } }
        else { t += rc; m.push(i); esp = false; }
      }
    }
  }
  while (t.length && t.charAt(t.length - 1) === ' ') { t = t.slice(0, -1); m.pop(); }
  return { t: t, m: m };
}

function ech(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

var etat = { pret: false, donnees: null };

function preparer(donnees) {
  var livres = (donnees.books || []).map(function (b) {
    return { titre: b.t || '', nt: normaliser((b.t || '') + ' ' + (b.ta || '')), url: b.u || '#' };
  });
  var lecons = (donnees.lecons || []).map(function (l) {
    return {
      b: l.b, docId: l.d, titre: l.t || '', url: l.u || '#', x: l.x || '',
      nt: normaliser((l.t || '') + ' ' + (l.ta || '')), nx: null
    };
  });
  return { books: livres, lecons: lecons };
}

/* Extrait recadré dans le texte d'origine, avec surlignage du terme. */
function extrait(l, termes) {
  var carte = normaliserCarte(l.x);
  var nt = carte.t, m = carte.m, pos = -1, lg = 0;
  for (var k = 0; k < termes.length; k++) {
    var p = nt.indexOf(termes[k]);
    if (p !== -1 && (pos === -1 || p < pos)) { pos = p; lg = termes[k].length; }
  }
  var brut = l.x, d, f;
  if (pos === -1) { d = 0; f = Math.min(180, brut.length); }
  else {
    var rd = m[pos] || 0;
    var rf = (m[Math.min(pos + lg - 1, m.length - 1)] || rd) + 1;
    d = Math.max(0, rd - 80); f = Math.min(brut.length, rf + 110);
  }
  var morceau = brut.slice(d, f).replace(/\s+/g, ' ').trim();
  var cm = normaliserCarte(morceau), im = -1, it = 0;
  for (var k2 = 0; k2 < termes.length; k2++) {
    var p2 = cm.t.indexOf(termes[k2]);
    if (p2 !== -1) { im = p2; it = termes[k2].length; break; }
  }
  if (im !== -1) {
    var jd = cm.m[im] || 0;
    var jf = (cm.m[Math.min(im + it - 1, cm.m.length - 1)] || jd) + 1;
    return ech(morceau.slice(0, jd)) + '<mark>' + ech(morceau.slice(jd, jf)) + '</mark>' + ech(morceau.slice(jf));
  }
  return ech(morceau);
}

function chercher(requete) {
  if (!etat.pret) throw new Error('index non chargé');
  var qn = normaliser(requete).trim();
  var termes = qn ? qn.split(' ') : [];
  if (!termes.length) return { total: 0, resultats: [] };
  var res = [];
  etat.donnees.books.forEach(function (b, i) {
    var ok = termes.every(function (t) { return b.nt.indexOf(t) !== -1; });
    if (ok) res.push({ type: 'livre', score: 60 + (b.nt.indexOf(qn) === 0 ? 25 : 0), i: i });
  });
  etat.donnees.lecons.forEach(function (l, i) {
    if (l.nx === null) l.nx = normaliser(l.x);
    var dt = 0, dx = 0;
    for (var k = 0; k < termes.length; k++) {
      if (l.nt.indexOf(termes[k]) !== -1) dt++;
      if (l.nx.indexOf(termes[k]) !== -1) dx++;
    }
    if (dt + dx < termes.length) return;
    var s = 40 * dt + 26 * dx + ((l.nt.indexOf(qn) !== -1 || l.nx.indexOf(qn) !== -1) ? 30 : 0);
    res.push({ type: 'lecon', score: s, i: i });
  });
  res.sort(function (a, b) { return b.score - a.score; });
  var total = res.length;
  var resultats = res.slice(0, 50).map(function (x) {
    if (x.type === 'livre') {
      var b = etat.donnees.books[x.i];
      return { type: 'livre', titre: ech(b.titre), url: b.url };
    }
    var l = etat.donnees.lecons[x.i];
    var b2 = etat.donnees.books[l.b] || { titre: '' };
    return { type: 'lecon', titre: ech(l.titre), sousTitre: ech(b2.titre), url: l.url, extrait: extrait(l, termes) };
  });
  return { total: total, resultats: resultats };
}

function definirDonnees(d) { etat.donnees = preparer(d); etat.pret = true; }

function installerUI(opts) {
  var input = opts.input, cont = opts.conteneur, statut = opts.statut || null;
  var charge = false, enCours = false, minuteur = null;
  function rendre(r) {
    var h = '<p class="r-compte">' + r.total + ' résultat' + (r.total > 1 ? 's' : '') +
      (r.total > 50 ? ' — les 50 premiers sont affichés' : '') + '</p>';
    if (!r.total) h += '<p class="r-compte">Aucun résultat. Essayer un autre mot — français ou arabe (les voyelles courtes arabes sont ignorées).</p>';
    h += '<ol>';
    r.resultats.forEach(function (x) {
      if (x.type === 'livre') {
        h += '<li class="r-livre"><span class="r-titre"><a href="' + x.url + '">' + x.titre + '</a></span>' +
             '<span class="r-livre-n">livre</span></li>';
      } else {
        h += '<li class="r-lecon"><span class="r-titre"><a href="' + x.url + '">' + x.titre + '</a></span>' +
             '<span class="r-livre-n">' + x.sousTitre + '</span>' +
             '<p class="r-extrait" dir="auto">' + x.extrait + '</p></li>';
      }
    });
    h += '</ol>';
    cont.innerHTML = h;
  }
  function lancer() {
    var q = input.value || '';
    if (q.trim().length < 2) { cont.innerHTML = ''; if (statut) statut.hidden = true; return; }
    if (!charge) { charger(); return; }
    var r;
    try { r = chercher(q); } catch (e) { charger(); return; }
    rendre(r);
  }
  function charger() {
    if (charge || enCours) return;
    enCours = true;
    if (statut) { statut.hidden = false; statut.textContent = 'Chargement de l\u2019index de recherche\u2026'; }
    opts.chargerIndex(function () {
      enCours = false; charge = true;
      if (statut) statut.hidden = true;
      lancer();
    }, function (msg) {
      enCours = false;
      if (statut) { statut.hidden = false; statut.textContent = 'Impossible de charger l\u2019index de recherche.' + (msg ? ' ' + msg : ''); }
    });
  }
  input.addEventListener('focus', charger);
  input.addEventListener('input', function () {
    if (minuteur) clearTimeout(minuteur);
    minuteur = setTimeout(lancer, 150);
  });
  return { lancer: lancer };
}

globale.MinhajRecherche = {
  normaliser: normaliser,
  definirDonnees: definirDonnees,
  pret: function () { return etat.pret; },
  chercher: chercher,
  installerUI: installerUI
};
})(window);
