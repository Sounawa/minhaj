#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur du site statique complet du Minhaj (المنهج النموذجي للتعليم العتيق).

Lit content/books/*.json (STRICTEMENT en lecture seule — la transcription
htmlFr n'est jamais modifiée) et content/manifest.json, puis produit dans
site/ un site entièrement pré-généré, sans aucun fetch à l'exécution :

  index.html                       accueil : grille des 64 livres + recherche globale
  livres/<slug>/index.html         sommaire du livre (leçons transcrites liées, autres grisées)
  livres/<slug>/introduction.html  présentation du manuel (si une intro existe)
  livres/<slug>/<docId>.html       page de leçon transcrite (htmlFr rendu tel quel)
  assets/style.css                 feuille de style unique — thème « automne »
  recherche.js                     moteur de recherche (JS pur, aucune dépendance)
  recherche-index.js               index de recherche pré-généré (chargé à la demande)
  hors-ligne.html                  variante mono-fichier : tout embarqué, ouvrable en file://
  ancien-lecteur.html              copie de l'ancien lecteur SPA (chemins fetch corrigés)
  404.html, robots.txt, sitemap.xml

Publication (option --publier RACINE) : copie le contenu de site/ à la racine
RACINE du dépôt — la source GitHub Pages détectée est la branche main, chemin /.
À la racine, ancien-lecteur.html garde ses fetch « content/books/… » ; dans
site/, la copie utilise « ../../content/books/… ».

Chemins RELATIFS partout (site servi depuis /minhaj/), UTF-8, Python stdlib.
"""

import argparse
import html as html_mod
import json
import re
import shutil
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xescape

# ---------------------------------------------------------------------------
# Constantes de mise en page
# ---------------------------------------------------------------------------

CSS = r""":root{
--fond:#f7f1e4;--carte:#fffdf8;--carte2:#f1ead6;
--encre:#33291a;--encre2:#6d5f4b;--gris:#7d6f57;
--ocre:#a3671c;--ocre-f:#8a5616;--ocre-p:#f1d9a0;
--olive:#5d6b2f;--olive-f:#49541f;
--ligne:#e3d6bc;--ligne2:#d2c29c;
--naskh:"Noto Naskh Arabic","Amiri","Scheherazade New","Geeza Pro","Traditional Arabic",serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--fond);color:var(--encre);font:17px/1.8 Georgia,"Times New Roman",serif}
a{color:var(--ocre-f);text-decoration:none}
a:hover{text-decoration:underline;color:var(--ocre)}
:focus-visible{outline:3px solid var(--ocre);outline-offset:2px}
.en-tete{background:var(--olive-f);color:#f6f0e2;border-bottom:4px solid var(--ocre)}
.en-tete .interieur{max-width:1080px;margin:0 auto;padding:13px 20px;display:flex;flex-wrap:wrap;gap:4px 18px;align-items:baseline}
.en-tete .marque{font-size:1rem;font-weight:bold}
.en-tete .marque a{color:#f6f0e2}
.en-tete .marque .arabe{font-family:var(--naskh);font-size:1.35rem;line-height:1.4}
.en-tete .sous-marque{font-size:.85rem;color:#e4dbc2}
.en-tete .liens{margin-inline-start:auto;font-size:.85rem}
.en-tete .liens a{color:#ecdfc0}
main{max-width:1080px;margin:0 auto;padding:26px 20px 46px}
main.lecture{max-width:900px}
.pied{border-top:1px solid var(--ligne);color:var(--gris);font-size:.83rem;text-align:center;padding:18px 20px 34px;max-width:1080px;margin:0 auto}
.pied a{color:var(--ocre-f)}
.hors-ecran{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
/* accueil */
.heros{text-align:center;margin:0 auto 26px;max-width:780px}
.heros .surline{color:var(--ocre);letter-spacing:.05em;text-transform:uppercase;font-size:.8rem;margin:0 0 8px}
.heros h1{margin:.1em 0 .35em;font-size:1.5rem;line-height:1.6}
.heros h1 .arabe{font-family:var(--naskh);font-size:1.75rem;color:var(--olive-f)}
.heros .sous{color:var(--encre2);margin:.2em 0}
.prog{max-width:520px;margin:20px auto 0}
.barre{height:12px;background:#ece2c8;border:1px solid var(--ligne2);border-radius:7px;overflow:hidden}
.barre span{display:block;height:100%;background:var(--olive)}
.compte{font-size:.92rem;color:var(--encre2);margin:9px 0 0}
.compte strong{color:var(--encre);font-size:1.05rem}
/* recherche */
.recherche{max-width:780px;margin:0 auto 32px}
.recherche input{width:100%;font:inherit;padding:11px 16px;border:1px solid var(--ligne2);border-radius:10px;background:var(--carte);color:var(--encre)}
.recherche input:focus{border-color:var(--ocre);outline:2px solid var(--ocre-p)}
.statut{color:var(--gris);font-size:.85rem;margin:6px 2px}
.resultats{margin-top:14px}
.resultats ol{list-style:none;margin:0;padding:0}
.resultats li{background:var(--carte);border:1px solid var(--ligne);border-radius:10px;padding:10px 14px;margin-bottom:8px}
.resultats li.r-livre{border-inline-start:4px solid var(--olive)}
.resultats .r-titre{font-weight:bold}
.resultats .r-titre a{display:block}
.resultats .r-livre-n{color:var(--gris);font-size:.82rem;margin-inline-start:8px}
.resultats .r-extrait{margin:6px 0 0;font-size:.92rem;color:var(--encre2);line-height:1.95}
.resultats .r-extrait mark{background:var(--ocre-p);color:var(--encre);padding:0 2px;border-radius:3px}
.resultats .r-compte{color:var(--gris);font-size:.85rem;margin:2px 4px 10px}
/* grille des livres */
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:14px}
.carte{display:block;background:var(--carte);border:1px solid var(--ligne);border-radius:12px;padding:14px 16px;color:inherit;border-top:4px solid var(--ocre)}
.carte:hover{text-decoration:none;box-shadow:0 3px 12px rgba(60,45,20,.13);transform:translateY(-1px);color:inherit}
.carte.fait{border-top-color:var(--olive)}
.carte .eta{font-size:.76rem;color:var(--gris);letter-spacing:.03em;margin:0 0 6px}
.carte .eta b{color:var(--olive-f);font-weight:600}
.carte .t-ar{font-family:var(--naskh);font-size:1.28rem;line-height:1.9;display:block;margin:2px 0}
.carte .t-fr{display:block;font-size:.95rem;line-height:1.5;color:var(--encre2)}
.carte .compte{font-size:.85rem;margin:8px 0 0;padding-top:8px;border-top:1px dashed var(--ligne)}
/* fil d'Ariane */
.fil{font-size:.88rem;color:var(--gris);margin:0 0 18px}
.fil a{color:var(--olive-f)}
.fil .sep{margin:0 7px;color:var(--ligne2)}
/* sommaire de livre */
.livre-tete{max-width:780px;margin:0 auto 24px;text-align:center}
.livre-tete h1{margin:.05em 0;font-size:1.35rem}
.livre-tete h1 .arabe{font-family:var(--naskh);font-size:1.7rem;line-height:1.9;color:var(--olive-f)}
.livre-tete .t-fr{color:var(--encre2);margin:.15em 0}
.livre-tete .meta{font-size:.85rem;color:var(--gris);margin:.3em 0 0}
.lecons{list-style:none;margin:0 auto;max-width:780px;padding:0}
.lecons li{border-bottom:1px solid var(--ligne)}
.lecons li a{display:flex;flex-wrap:wrap;gap:2px 12px;align-items:baseline;padding:11px 6px}
.lecons li a:hover{background:var(--carte);text-decoration:none}
.badge{min-width:30px;text-align:center;background:var(--carte2);border:1px solid var(--ligne2);color:var(--encre2);border-radius:7px;font-size:.8rem;padding:1px 7px}
.lecons .fait .badge{background:var(--olive);border-color:var(--olive);color:#f8f4e6}
.lecons .t-ar{font-family:var(--naskh);font-size:1.18rem;line-height:1.9}
.lecons .t-fr{color:var(--encre2);font-size:.92rem}
.lecons li.a-faire{color:var(--gris)}
.lecons li.a-faire .t-ar,.lecons li.a-faire .t-fr{color:var(--gris)}
.lecons .pdf{font-size:.78rem;color:var(--ocre-f);border:1px solid var(--ligne2);border-radius:6px;padding:1px 8px}
.lecons li.intro-l a{color:var(--ocre-f)}
/* contenu de leçon */
.contenu{max-width:780px;margin:0 auto;background:var(--carte);border:1px solid var(--ligne);border-radius:14px;padding:32px 38px}
.contenu h1{font-size:1.32rem;line-height:1.65;color:var(--ocre-f);border-bottom:2px solid var(--ocre);padding-bottom:.5em;margin:0 0 .9em}
.contenu h2{font-size:1.16rem;color:var(--olive-f);border-bottom:1px solid var(--ligne);padding-bottom:.3em;margin:1.9em 0 .6em}
.contenu h3{font-size:1.05rem;color:var(--olive-f);margin:1.5em 0 .4em}
.contenu h4,.contenu h5{font-size:1rem;color:var(--encre2)}
.contenu p{margin:.95em 0}
.contenu ul,.contenu ol{margin:.9em 0;padding-inline-start:1.7em}
.contenu li{margin:.32em 0}
.contenu dl{margin:.9em 0}
.contenu dt{font-weight:bold;margin-top:.7em}
.contenu dd{margin:.15em 0 .15em 1.4em}
.contenu blockquote{border-inline-start:3px solid var(--ocre);margin:1em 0;padding:.15em 0 .15em 1.1em;color:var(--encre2)}
.contenu table{border-collapse:collapse;margin:1.1em 0;width:100%;font-size:.94em;line-height:1.6}
.contenu th,.contenu td{border:1px solid var(--ligne2);padding:6px 10px;vertical-align:top}
.contenu th{background:var(--carte2)}
.contenu sup{font-size:.72em}
.contenu [lang="ar"]{font-family:var(--naskh);font-size:1.16em;line-height:2.1}
.contenu .intro-arabe{direction:rtl;text-align:right}
.contenu .intro-arabe [lang="ar"]{font-size:1.3em}
/* navigation précédent / suivant */
.pn{display:flex;gap:10px;justify-content:space-between;align-items:stretch;max-width:780px;margin:20px auto 0}
.pn a,.pn span.pn-vide{flex:1;background:var(--carte);border:1px solid var(--ligne);border-radius:10px;padding:10px 14px;font-size:.9rem;line-height:1.5;color:var(--ocre-f)}
.pn a:hover{text-decoration:none;border-color:var(--ocre)}
.pn .pn-suiv{text-align:right}
.pn .pn-sommaire{flex:0 0 auto;background:var(--carte2);color:var(--encre2);text-align:center;min-width:120px}
.pn .pn-vide{color:var(--gris)}
.pn .pn-l{display:block;font-size:.75rem;color:var(--gris)}
/* hors-ligne */
details.lecon{background:var(--carte);border:1px solid var(--ligne);border-radius:10px;margin:10px 0}
details.lecon summary{cursor:pointer;padding:10px 14px;display:flex;flex-wrap:wrap;gap:2px 12px;align-items:baseline;list-style:none}
details.lecon summary::-webkit-details-marker{display:none}
details.lecon summary:before{content:"\25B8";color:var(--ocre);margin-inline-end:8px}
details.lecon[open] summary:before{content:"\25BE"}
details.lecon[open] summary{border-bottom:1px dashed var(--ligne)}
details.lecon .contenu{background:none;border:none;border-radius:0;padding:16px 22px;margin:0;max-width:none}
.section-livre{margin:36px 0}
.section-livre>h2{font-size:1.15rem;color:var(--olive-f);border-bottom:2px solid var(--ligne2);padding-bottom:.3em}
.section-livre>h2 .arabe{font-family:var(--naskh)}
.section-livre .meta-l{font-size:.82rem;color:var(--gris);margin:.2em 0 10px}
.bandeau{background:var(--ocre-p);border-bottom:2px solid var(--ocre);color:var(--encre);text-align:center;font-size:.85rem;padding:7px 14px}
.bandeau a{color:var(--ocre-f);font-weight:bold}
@media (max-width:640px){
body{font-size:16px}
.contenu{padding:20px 16px}
.pn{flex-wrap:wrap}
.pn .pn-sommaire{order:-1;flex:1 1 100%}
.en-tete .liens{margin-inline-start:0}
}
@media print{.en-tete,.pied,.fil,.pn,.recherche,.bandeau{display:none}.contenu{border:0;padding:0}}
"""

RECHERCHE_JS = r"""/* Moteur de recherche du Minhaj — JS pur, aucune dépendance.
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
"""

BANDEAU_CSS = ('<style>.bandeau{background:#f1d9a0;border-bottom:2px solid #a67c00;color:#33291a;'
               'text-align:center;font-size:.85rem;padding:7px 14px;font-family:Georgia,serif}'
               '.bandeau a{color:#8a5616;font-weight:bold}</style>')

# ---------------------------------------------------------------------------
# Extraction de texte
# ---------------------------------------------------------------------------

class ExtracteurTexte(HTMLParser):
    """htmlFr -> texte brut : balises retirées, entités décodées, espaces compactés."""

    BLOCS = ('p', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'li', 'div', 'tr', 'dt', 'dd')

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.morceaux = []
        self.ignorer = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.ignorer += 1
        elif tag in self.BLOCS:
            self.morceaux.append(' ')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            if self.ignorer:
                self.ignorer -= 1
        elif tag in self.BLOCS:
            self.morceaux.append(' ')

    def handle_data(self, data):
        if not self.ignorer:
            self.morceaux.append(data)


def texte_plain(fragment):
    if not fragment:
        return ''
    ex = ExtracteurTexte()
    try:
        ex.feed(fragment)
        ex.close()
    except Exception:
        pass
    return re.sub(r'\s+', ' ', ''.join(ex.morceaux)).strip()


def esc(s):
    return html_mod.escape(str(s), quote=True)


def url_lecon(doc_id):
    """docId -> nom de fichier / segment d'URL (encodage % si nécessaire)."""
    return quote(doc_id, safe='')


# ---------------------------------------------------------------------------
# Chargement des données
# ---------------------------------------------------------------------------

def charger_livres(rep_books, manifest, avertissements):
    sujets = {s.get('id'): s for s in (manifest or {}).get('subjects', [])}
    niveaux = {n.get('id'): n for n in (manifest or {}).get('levels', [])}
    books_manifest = (manifest or {}).get('books', [])
    rang_manifest = {b.get('id'): i for i, b in enumerate(books_manifest)}

    livres = []
    for chemin in sorted(Path(rep_books).glob('*.json')):
        slug = chemin.stem
        try:
            data = json.loads(chemin.read_text(encoding='utf-8'))
        except Exception as e:
            avertissements.append(f'{chemin.name} illisible : {e}')
            continue
        lessons = data.get('lessons', []) if isinstance(data, dict) else data
        intro = (data.get('intro') or {}) if isinstance(data, dict) else {}

        sujet = sujets.get(data.get('subject') or '', {})
        niveau = niveaux.get(data.get('level') or '', {})
        sujet_fr = sujet.get('titleFr') or data.get('subjectAr') or data.get('subject') or ''
        niveau_fr = niveau.get('shortFr') or niveau.get('labelFr') or data.get('levelAr') or ''

        # introduction
        intro_fr = (intro.get('htmlFr') or '').strip()
        intro_ar = (intro.get('html') or '').strip()
        entree_intro = None
        if intro_fr or intro_ar:
            entree_intro = {
                'titreFr': (intro.get('titleFr') or '').strip() or 'Présentation du manuel',
                'titreAr': (intro.get('titleAr') or '').strip(),
                'htmlFr': intro_fr,
                'htmlAr': intro_ar,
                'texte': texte_plain(intro_fr or intro_ar),
                'docId': (intro.get('docId') or '').strip(),
            }

        # leçons
        lecons = []
        vus = set()
        for i, l in enumerate(lessons):
            did = str(l.get('docId') or '').strip()
            if not did:
                avertissements.append(f'{slug} : leçon {i + 1} sans docId — ignorée')
                continue
            if did in vus:
                avertissements.append(f'{slug} : docId en double {did} — seconde occurrence ignorée')
                continue
            vus.add(did)
            fr = l.get('htmlFr') or ''
            ok = bool(fr.strip())
            lecons.append({
                'docId': did,
                'num': i + 1,
                'titleFr': (l.get('titleFr') or '').strip(),
                'titleAr': (l.get('titleAr') or '').strip(),
                'pdfUrl': (l.get('pdfUrl') or '').strip(),
                'ok': ok,
                'htmlFr': fr if ok else '',
                'texte': texte_plain(fr) if ok else '',
            })

        livres.append({
            'slug': slug,
            'ordre': rang_manifest.get(slug, 10_000),
            'titleFr': (data.get('titleFr') or '').strip() or slug,
            'titleAr': (data.get('titleAr') or '').strip(),
            'sujetFr': sujet_fr,
            'niveauFr': niveau_fr,
            'pdfUrl': (data.get('pdfUrl') or '').strip(),
            'non_publie': bool(data.get('unpublished')),
            'intro': entree_intro,
            'lecons': lecons,
        })

    #Collision « introduction » avec un docId de leçon ?
    for b in livres:
        if any(l['docId'] == 'introduction' for l in b['lecons']):
            avertissements.append(f"{b['slug']} : une leçon occupe déjà le nom « introduction »")
    livres.sort(key=lambda b: (b['ordre'], b['slug']))
    return livres


def chaine_navigation(livre):
    """Liste ordonnée des pages navigables : introduction puis leçons transcrites."""
    elements = []
    if livre['intro']:
        elements.append({'type': 'intro', 'url': 'introduction.html', 'label': 'Présentation'})
    for l in livre['lecons']:
        if l['ok']:
            elements.append({'type': 'lecon', 'url': url_lecon(l['docId']) + '.html',
                             'label': f"Leçon {l['num']}", 'lecon': l})
    return elements


# ---------------------------------------------------------------------------
# Gabarits de pages
# ---------------------------------------------------------------------------

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='7' fill='%2349541f'/%3E"
           "%3Ctext x='16' y='23' font-size='19' text-anchor='middle' fill='%23f6f0e2' "
           "font-family='serif'%3E%D9%85%3C/text%3E%3C/svg%3E")


def entete(rel, programme_ar):
    return f"""<header class="en-tete"><div class="interieur">
<span class="marque"><a href="{rel}index.html"><span class="arabe" dir="rtl" lang="ar">{programme_ar}</span></a></span>
<span class="sous-marque">Minhaj — manuels de l’enseignement traditionnel (Maroc)</span>
<span class="liens"><a href="{rel}hors-ligne.html">hors connexion</a> · <a href="https://github.com/Sounawa/minhaj" target="_blank" rel="noopener">dépôt GitHub</a></span>
</div></header>"""


def pied(rel, date_fr):
    return f"""<footer class="pied">Transcription mot à mot et traduction française du curriculum de l’enseignement traditionnel marocain — Ministère des Habous et des Affaires islamiques · site statique généré le {date_fr} · <a href="{rel}ancien-lecteur.html">ancien lecteur</a> · <a href="https://github.com/Sounawa/minhaj" target="_blank" rel="noopener">Sounawa/minhaj</a></footer>"""


BOOTSTRAP_RECHERCHE_RACINE = r"""<script src="recherche.js"></script>
<script>
(function(){
var charge=false;
MinhajRecherche.installerUI({
input:document.getElementById('champ'),
conteneur:document.getElementById('resultats'),
statut:document.getElementById('statut'),
chargerIndex:function(suivant,echec){
if(charge){suivant();return;}
charge=true;
var s=document.createElement('script');
s.src='recherche-index.js';
s.onload=function(){
if(window.MINHAJ_INDEX){MinhajRecherche.definirDonnees(window.MINHAJ_INDEX);window.MINHAJ_INDEX=null;suivant();}
else if(echec)echec('Index illisible.');
};
s.onerror=function(){if(echec)echec();};
document.head.appendChild(s);
}
});
})();
</script>"""


def coquille(titre, description, rel, programme_ar, date_fr, corps, scripts_html=''):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#49541f">
<meta name="generator" content="minhaj-build {date_fr}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/style.css">
</head>
<body>
{entete(rel, programme_ar)}
{corps}
{pied(rel, date_fr)}
{scripts_html}
</body>
</html>
"""


def html_cartes(livres, rel):
    cartes = []
    for b in livres:
        n_total = len(b['lecons'])
        n_ok = sum(1 for l in b['lecons'] if l['ok'])
        pct = round(100 * n_ok / n_total) if n_total else 0
        classe = 'fait' if n_ok else 'a-faire'
        cartes.append(f"""<a class="carte {classe}" href="{rel}livres/{b['slug']}/">
<p class="eta"><b>{esc(b['sujetFr'])}</b> · {esc(b['niveauFr'])}</p>
<span class="t-ar" dir="rtl" lang="ar">{esc(b['titleAr'])}</span>
<span class="t-fr">{esc(b['titleFr'])}</span>
<div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte">{n_ok} / {n_total} leçons transcrites</p>
</a>""")
    return '<section class="grille">\n' + '\n'.join(cartes) + '\n</section>'


def html_recherche():
    return """<section class="recherche" id="recherche">
<label class="hors-ecran" for="champ">Rechercher dans les leçons transcrites</label>
<input id="champ" type="search" autocomplete="off"
       placeholder="Rechercher dans les leçons transcrites — français ou arabe…">
<p id="statut" class="statut" hidden></p>
<div id="resultats" class="resultats" aria-live="polite"></div>
</section>"""


def page_accueil(livres, programme, date_fr):
    n_total = sum(len(b['lecons']) for b in livres)
    n_ok = sum(1 for b in livres for l in b['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    nom_ar = programme.get('nameAr', 'المنهج النموذجي للتعليم العتيق')
    nom_fr = programme.get('nameFr') or 'Programme modèle de l’enseignement traditionnel'
    editeur_fr = programme.get('publisherFr') or 'Ministère des Habous et des Affaires islamiques — Royaume du Maroc'
    corps = f"""<main>
<section class="heros">
<p class="surline">{esc(nom_fr)} — {esc(editeur_fr)}</p>
<h1><span class="arabe" dir="rtl" lang="ar">{esc(nom_ar)}</span></h1>
<p class="sous">Collection de {len(livres)} manuels scolaires marocains d’enseignement traditionnel, transcrits mot à mot en arabe et traduits ou commentés en français, leçon par leçon.</p>
<div class="prog"><div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte"><strong>{n_ok} / {n_total}</strong> leçons transcrites · {len(livres)} livres · mise à jour : {date_fr}</p></div>
</section>
{html_recherche()}
{html_cartes(livres, '')}
</main>"""
    return coquille(
        'Minhaj — manuels de l’enseignement traditionnel (Maroc)',
        'Sommaire des 64 manuels du المنهج النموذجي للتعليم العتيق : leçons transcrites mot à mot en arabe, traduites et commentées en français. Recherche globale en français et en arabe.',
        '', nom_ar, date_fr, corps, BOOTSTRAP_RECHERCHE_RACINE), n_ok, n_total


def html_liste_lecons(livre):
    items = []
    if livre['intro']:
        it = livre['intro']
        ar = f'<span class="t-ar" dir="rtl" lang="ar">{esc(it["titreAr"])}</span>' if it['titreAr'] else ''
        items.append(f"""<li class="intro-l fait"><a href="introduction.html"><span class="badge">✦</span>{ar}<span class="t-fr">{esc(it['titreFr'])}</span></a></li>""")
    for l in livre['lecons']:
        badge = f'<span class="badge">{l["num"]}</span>'
        ar = f'<span class="t-ar" dir="rtl" lang="ar">{esc(l["titleAr"])}</span>' if l['titleAr'] else ''
        fr = f'<span class="t-fr">{esc(l["titleFr"])}</span>' if l['titleFr'] else ''
        pdf = f'<a class="pdf" href="{esc(l["pdfUrl"])}" target="_blank" rel="noopener">PDF officiel</a>' if l['pdfUrl'] else ''
        if l['ok']:
            items.append(f'<li class="fait"><a href="{url_lecon(l["docId"])}.html">{badge}{ar}{fr}</a></li>')
        else:
            items.append(f'<li class="a-faire"><span style="display:flex;flex-wrap:wrap;gap:2px 12px;align-items:baseline;padding:11px 6px">{badge}{ar}{fr}{pdf}</span></li>')
    return '<ol class="lecons">\n' + '\n'.join(items) + '\n</ol>'


def page_sommaire_livre(livre, programme_ar, date_fr):
    n_total = len(livre['lecons'])
    n_ok = sum(1 for l in livre['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    pdf_livre = (f' · <a href="{esc(livre["pdfUrl"])}" target="_blank" rel="noopener">PDF officiel du manuel</a>'
                 if livre['pdfUrl'] else '')
    corps = f"""<main>
<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span><span>{esc(livre['titleFr'])}</span></nav>
<header class="livre-tete">
<h1><span class="arabe" dir="rtl" lang="ar">{esc(livre['titleAr'])}</span></h1>
<p class="t-fr">{esc(livre['titleFr'])}</p>
<p class="meta">{esc(livre['sujetFr'])} · {esc(livre['niveauFr'])}{pdf_livre}</p>
<div class="prog"><div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte"><strong>{n_ok} / {n_total}</strong> leçons transcrites</p></div>
</header>
{html_liste_lecons(livre)}
</main>"""
    description = (f"{livre['titleFr']} ({livre['sujetFr']}, {livre['niveauFr']}) : "
                   f"{n_ok} leçons transcrites sur {n_total}, transcription mot à mot en arabe et traduction française.")
    return coquille(
        f"{livre['titleFr']} — sommaire | Minhaj",
        esc(description), '../../', programme_ar, date_fr, corps)


def html_pn(prec, suiv, url_sommaire):
    def bloc(el, cote):
        if el:
            rel_attr = ' rel="prev"' if cote == 'prec' else ' rel="next"'
            return (f'<a class="pn-{cote}" href="{el["url"]}"{rel_attr}>'
                    f'<span class="pn-l">{"← Précédent" if cote == "prec" else "Suivant →"}</span>{esc(el["label"])}</a>')
        texte = 'Début du livre' if cote == 'prec' else 'Fin des pages transcrites'
        return f'<span class="pn-vide"><span class="pn-l">{"← Précédent" if cote == "prec" else "Suivant →"}</span>{texte}</span>'

    return (f'<nav class="pn">{bloc(prec, "prec")}'
            f'<a class="pn-sommaire" href="{url_sommaire}">Sommaire du livre</a>'
            f'{bloc(suiv, "suiv")}</nav>')


def page_lecon(livre, lecon, prec, suiv, programme_ar, date_fr):
    titre_page = f"Leçon {lecon['num']} — {livre['titleFr']} | Minhaj"
    description = texte_plain(lecon['htmlFr'])[:160].strip()
    fil = (f'<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span>'
           f'<a href="index.html">{esc(livre["titleFr"])}</a><span class="sep">›</span>'
           f'<span>Leçon {lecon["num"]}</span></nav>')
    corps = f"""<main class="lecture">
{fil}
<article class="contenu">
{lecon['htmlFr']}
</article>
{html_pn(prec, suiv, 'index.html')}
</main>"""
    return coquille(esc(titre_page), esc(description), '../../', programme_ar, date_fr, corps)


def page_introduction(livre, suiv, programme_ar, date_fr):
    it = livre['intro']
    if it['htmlFr']:
        contenu = it['htmlFr']
    else:
        contenu = f'<div class="intro-arabe" dir="rtl" lang="ar">\n{it["htmlAr"]}\n</div>'
    fil = (f'<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span>'
           f'<a href="index.html">{esc(livre["titleFr"])}</a><span class="sep">›</span>'
           f'<span>{esc(it["titreFr"])}</span></nav>')
    corps = f"""<main class="lecture">
{fil}
<article class="contenu">
{contenu}
</article>
{html_pn(None, suiv, 'index.html')}
</main>"""
    description = f"Présentation du manuel « {livre['titleFr']} » ({livre['sujetFr']}, {livre['niveauFr']})."
    return coquille(f"{esc(it['titreFr'])} — {esc(livre['titleFr'])} | Minhaj",
                    esc(description), '../../', programme_ar, date_fr, corps)


# ---------------------------------------------------------------------------
# Hors-ligne (mono-fichier)
# ---------------------------------------------------------------------------

def page_hors_ligne(livres, programme, css_texte, recherche_js, date_fr):
    n_total = sum(len(b['lecons']) for b in livres)
    n_ok = sum(1 for b in livres for l in b['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    nom_ar = programme.get('nameAr', 'المنهج النموذجي للتعليم العتيق')

    cartes = []
    for b in livres:
        ok = sum(1 for l in b['lecons'] if l['ok'])
        tot = len(b['lecons'])
        p = round(100 * ok / tot) if tot else 0
        cartes.append(f"""<a class="carte {'fait' if ok else 'a-faire'}" href="#livre-{b['slug']}">
<p class="eta"><b>{esc(b['sujetFr'])}</b> · {esc(b['niveauFr'])}</p>
<span class="t-ar" dir="rtl" lang="ar">{esc(b['titleAr'])}</span>
<span class="t-fr">{esc(b['titleFr'])}</span>
<div class="barre"><span style="width:{p}%"></span></div>
<p class="compte">{ok} / {tot} leçons transcrites</p>
</a>""")

    sections = []
    for b in livres:
        blocs = []
        if b['intro']:
            it = b['intro']
            contenu = it['htmlFr'] or f'<div class="intro-arabe" dir="rtl" lang="ar">\n{it["htmlAr"]}\n</div>'
            blocs.append(f"""<details class="lecon intro-l" id="lec-{b['slug']}-introduction">
<summary><span class="badge">✦</span><span class="t-ar" dir="rtl" lang="ar">{esc(it['titreAr'])}</span><span class="t-fr">{esc(it['titreFr'])}</span></summary>
<div class="contenu">
{contenu}
</div>
</details>""")
        for l in b['lecons']:
            if not l['ok']:
                continue
            blocs.append(f"""<details class="lecon" id="lec-{b['slug']}-{l['docId']}" data-docid="{esc(l['docId'])}" data-titre="{esc(l['titleFr'] or l['titleAr'])}">
<summary><span class="badge">{l['num']}</span><span class="t-ar" dir="rtl" lang="ar">{esc(l['titleAr'])}</span><span class="t-fr">{esc(l['titleFr'])}</span></summary>
<div class="contenu">
{l['htmlFr']}
</div>
</details>""")
        sections.append(f"""<section class="section-livre livre-hl" id="livre-{b['slug']}" data-slug="{b['slug']}" data-titre="{esc(b['titleFr'])}">
<h2><span class="arabe" dir="rtl" lang="ar">{esc(b['titleAr'])}</span> — {esc(b['titleFr'])}</h2>
<p class="meta-l">{esc(b['sujetFr'])} · {esc(b['niveauFr'])} · {sum(1 for l in b['lecons'] if l['ok'])} / {len(b['lecons'])} leçons transcrites · les leçons non transcrites n’apparaissent pas ici (voir le site en ligne).</p>
{''.join(blocs)}
</section>""")

    bootstrap = r"""(function(){
function indexDepuisDOM(){
var livres=[],lecons=[];
var secs=document.querySelectorAll('section.livre-hl');
for(var i=0;i<secs.length;i++){
var sec=secs[i];
livres.push({s:sec.getAttribute('data-slug'),t:sec.getAttribute('data-titre'),u:'#'+sec.id});
var arts=sec.querySelectorAll('details.lecon');
for(var j=0;j<arts.length;j++){
var art=arts[j];
lecons.push({b:i,d:art.getAttribute('data-docid'),t:art.getAttribute('data-titre'),
u:'#'+art.id,x:(art.textContent||'').replace(/\s+/g,' ').trim()});
}
}
return {books:livres,lecons:lecons};
}
MinhajRecherche.installerUI({
input:document.getElementById('champ'),
conteneur:document.getElementById('resultats'),
statut:document.getElementById('statut'),
chargerIndex:function(suivant,echec){
try{MinhajRecherche.definirDonnees(indexDepuisDOM());suivant();}
catch(e){if(echec)echec(String(e&&e.message||e));}
}
});
function ouvrirAncre(){
var id=decodeURIComponent((location.hash||'').slice(1));
if(!id)return;
var el=document.getElementById(id);
if(el){var d=el.closest('details');if(d)d.open=true;}
}
window.addEventListener('hashchange',ouvrirAncre);
document.addEventListener('click',function(ev){
var a=ev.target.closest?ev.target.closest('a[href^="#"]'):null;
if(!a)return;
var el=document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
if(el){var d=el.closest('details');if(d)d.open=true;}
});
ouvrirAncre();
})();"""

    corps = f"""<main>
<section class="heros">
<p class="surline">Consultation hors connexion — fichier unique</p>
<h1><span class="arabe" dir="rtl" lang="ar">{esc(nom_ar)}</span></h1>
<p class="sous">Toute la collection est embarquée dans ce fichier : sommaires, leçons transcrites, recherche. Enregistrez-le et ouvrez-le sans connexion.</p>
<div class="prog"><div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte"><strong>{n_ok} / {n_total}</strong> leçons transcrites · {len(livres)} livres · mise à jour : {date_fr}</p></div>
</section>
{html_recherche()}
{html_cartes_hl(cartes)}
{''.join(sections)}
</main>"""

    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minhaj — consultation hors connexion | {esc(nom_ar)}</title>
<meta name="description" content="Variante mono-fichier du site Minhaj : tous les livres et leçons transcrites embarqués, consultable hors connexion (file://).">
<meta name="theme-color" content="#49541f">
<meta name="generator" content="minhaj-build {date_fr}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{css_texte}
</style>
</head>
<body>
{entete('', nom_ar).replace('href="hors-ligne.html"', 'href="#recherche"').replace('href="index.html"', 'href="#accueil"')}
{corps}
{pied('', date_fr)}
<script>
{recherche_js}
</script>
<script>
{bootstrap}
</script>
</body>
</html>
"""


def html_cartes_hl(cartes):
    return '<section class="grille" id="accueil">\n' + '\n'.join(cartes) + '\n</section>'


# ---------------------------------------------------------------------------
# Ancien lecteur
# ---------------------------------------------------------------------------

def preparer_ancien_lecteur(texte_spa, prefixe_fetch, lien_retour):
    """Copie de l'ancien lecteur : chemins fetch corrigés + bandeau d'archivage."""
    texte = texte_spa.replace("fetch('content/books/", "fetch('" + prefixe_fetch)
    bandeau = (f'<div class="bandeau">Ancien lecteur (archivé) — le '
               f'<a href="{lien_retour}">site statique complet</a> remplace cette page : '
               f'sommaires par livre, leçons transcrites, recherche globale, version hors connexion.</div>')
    texte = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + bandeau, texte, count=1)
    texte = texte.replace('</head>', BANDEAU_CSS + '\n</head>', 1)
    return texte


# ---------------------------------------------------------------------------
# 404 / robots / sitemap
# ---------------------------------------------------------------------------

def page_404(css_texte, nom_ar, date_fr, base_url):
    script = r"""(function(){
var dossier=location.pathname.slice(0,location.pathname.lastIndexOf('/')+1);
var sous=dossier.split('/').filter(function(x){return x.length;});
var i=sous.indexOf('minhaj');
var profondeur=(i===-1)?0:(sous.length-i-1);
var pref=profondeur>0?new Array(profondeur+1).join('../'):'./';
var c=document.getElementById('retour');
if(c)c.href=pref+'index.html';
})();"""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page introuvable — Minhaj</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#49541f">
<link rel="icon" href="{FAVICON}">
<style>
{css_texte}
</style>
</head>
<body>
<div class="bandeau">Erreur 404 — cette adresse n’existe pas sur le site.</div>
<main>
<section class="heros">
<h1><span class="arabe" dir="rtl" lang="ar">{esc(nom_ar)}</span></h1>
<p class="sous">La page demandée est introuvable. Revenir à l’accueil pour retrouver les 64 livres et leurs leçons transcrites.</p>
<p style="margin-top:18px"><a style="display:inline-block;background:var(--carte);border:1px solid var(--ligne);border-radius:10px;padding:10px 18px;color:var(--ocre-f)" id="retour" href="{base_url}">← Accueil du Minhaj</a></p>
</section>
</main>
<script>{script}</script>
</body>
</html>
"""


def robots_txt(base):
    return f"""User-agent: *
Allow: /

Sitemap: {base}sitemap.xml
"""


def sitemap_xml(livres, base, date_str):
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
              f'<url><loc>{xescape(base)}</loc><lastmod>{date_str}</lastmod></url>']
    for b in livres:
        prefixe = f"{xescape(base)}livres/{b['slug']}/"
        lignes.append(f'<url><loc>{prefixe}</loc><lastmod>{date_str}</lastmod></url>')
        if b['intro']:
            lignes.append(f'<url><loc>{prefixe}introduction.html</loc><lastmod>{date_str}</lastmod></url>')
        for l in b['lecons']:
            if l['ok']:
                lignes.append(f'<url><loc>{prefixe}{url_lecon(l["docId"])}.html</loc><lastmod>{date_str}</lastmod></url>')
    lignes.append('</urlset>')
    return '\n'.join(lignes) + '\n'


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------

def mo_octets(n):
    return f'{n / (1024 * 1024):.1f} Mo'


def main():
    parseur = argparse.ArgumentParser(
        description='Génère le site statique complet du Minhaj dans site/ (Python stdlib).')
    parseur.add_argument('--content', default=None, help='répertoire content/books (défaut : déduit du script)')
    parseur.add_argument('--sortie', default=None, help='répertoire de sortie site/ (défaut : déduit)')
    parseur.add_argument('--base-url', default='https://sounawa.github.io/minhaj/',
                         help='URL publique du site (sitemap, robots)')
    parseur.add_argument('--publier', metavar='RACINE', default=None,
                         help='copie aussi le contenu de site/ à la racine RACINE (publication Pages)')
    parseur.add_argument('--sans-nettoyage', action='store_true',
                         help='ne supprime pas site/ avant génération (débogage)')
    opts = parseur.parse_args()

    repertoire_script = Path(__file__).resolve().parent
    depot = repertoire_script.parent
    rep_books = Path(opts.content) if opts.content else depot / 'content' / 'books'
    sortie = Path(opts.sortie) if opts.sortie else depot / 'site'
    base = opts.base_url if opts.base_url.endswith('/') else opts.base_url + '/'

    # date française
    try:
        from zoneinfo import ZoneInfo
        maintenant = datetime.now(ZoneInfo('Europe/Paris'))
    except Exception:
        maintenant = datetime.now()
    date_fr = maintenant.strftime('%d/%m/%Y').lstrip('0').replace('/0', '/')
    date_str = maintenant.strftime('%Y-%m-%d')
    mois_fr = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
               'août', 'septembre', 'octobre', 'novembre', 'décembre']
    date_fr = f"{maintenant.day} {mois_fr[maintenant.month - 1]} {maintenant.year}"

    manifest_path = depot / 'content' / 'manifest.json'
    manifest = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except Exception as e:
            print(f'! manifest.json illisible ({e}) — ordre alphabétique de secours')

    avertissements = []
    livres = charger_livres(rep_books, manifest, avertissements)
    if not livres:
        print('!! aucun livre trouvé dans', rep_books)
        return 1
    programme = manifest.get('program', {})
    nom_ar = programme.get('nameAr', 'المنهج النموذجي للتعليم العتيق')

    # ---- préparation du répertoire
    if sortie.exists() and not opts.sans_nettoyage:
        shutil.rmtree(sortie)
    (sortie / 'assets').mkdir(parents=True, exist_ok=True)

    n_pages = 0
    total_lecons = 0
    total_ok = 0
    total_intro = 0

    # ---- accueil
    page, total_ok, total_lecons = page_accueil(livres, programme, date_fr)
    (sortie / 'index.html').write_text(page, encoding='utf-8')
    n_pages += 1
    total_intro = sum(1 for b in livres if b['intro'])

    # ---- CSS + moteur de recherche
    (sortie / 'assets' / 'style.css').write_text(CSS, encoding='utf-8')
    (sortie / 'recherche.js').write_text(RECHERCHE_JS, encoding='utf-8')

    # ---- index de recherche pré-généré
    entrees_books = []
    entrees_lecons = []
    for ib, b in enumerate(livres):
        entrees_books.append({'s': b['slug'], 't': b['titleFr'], 'ta': b['titleAr'],
                              'u': f"livres/{b['slug']}/"})
        if b['intro']:
            it = b['intro']
            entrees_lecons.append({
                'b': ib, 'd': 'introduction',
                't': it['titreFr'], 'ta': it['titreAr'],
                'u': f"livres/{b['slug']}/introduction.html",
                'x': it['texte'],
            })
        for l in b['lecons']:
            if not l['ok']:
                continue
            entrees_lecons.append({
                'b': ib, 'd': l['docId'],
                't': l['titleFr'] or l['titleAr'] or f"Leçon {l['num']}",
                'ta': l['titleAr'],
                'u': f"livres/{b['slug']}/{url_lecon(l['docId'])}.html",
                'x': l['texte'],
            })
    index_js = ('/* Index de recherche pré-généré par scripts/build-site.py — '
                f'{len(entrees_books)} livres, {len(entrees_lecons)} documents. */\n'
                'window.MINHAJ_INDEX=' +
                json.dumps({'books': entrees_books, 'lecons': entrees_lecons},
                           ensure_ascii=False, separators=(',', ':')) + ';\n')
    (sortie / 'recherche-index.js').write_text(index_js, encoding='utf-8')

    # ---- pages livres / introductions / leçons
    for b in livres:
        rep_livre = sortie / 'livres' / b['slug']
        rep_livre.mkdir(parents=True, exist_ok=True)
        (rep_livre / 'index.html').write_text(page_sommaire_livre(b, nom_ar, date_fr), encoding='utf-8')
        n_pages += 1
        chaine = chaine_navigation(b)
        if b['intro']:
            suiv = chaine[1] if len(chaine) > 1 else None
            (rep_livre / 'introduction.html').write_text(
                page_introduction(b, suiv, nom_ar, date_fr), encoding='utf-8')
            n_pages += 1
        for idx, el in enumerate(chaine):
            if el['type'] != 'lecon':
                continue
            lecon = el['lecon']
            prec = chaine[idx - 1] if idx > 0 else None
            suiv = chaine[idx + 1] if idx + 1 < len(chaine) else None
            (rep_livre / (url_lecon(lecon['docId']) + '.html')).write_text(
                page_lecon(b, lecon, prec, suiv, nom_ar, date_fr), encoding='utf-8')
            n_pages += 1

    # ---- hors-ligne
    page_hl = page_hors_ligne(livres, programme, CSS, RECHERCHE_JS, date_fr)
    (sortie / 'hors-ligne.html').write_text(page_hl, encoding='utf-8')

    # ---- 404 / robots / sitemap
    (sortie / '404.html').write_text(page_404(CSS, nom_ar, date_fr, base), encoding='utf-8')
    (sortie / 'robots.txt').write_text(robots_txt(base), encoding='utf-8')
    (sortie / 'sitemap.xml').write_text(sitemap_xml(livres, base, date_str), encoding='utf-8')
    (sortie / '.nojekyll').touch(exist_ok=True)

    # ---- ancien lecteur (copie de la SPA d'origine, fetch corrigés)
    # Source : scripts/ancien-lecteur.source.html (copie vierge, pour des
    # reconstructions idempotentes même après publication à la racine) ;
    # à défaut, l'index.html courant s'il est encore l'ancien lecteur.
    spa = depot / 'scripts' / 'ancien-lecteur.source.html'
    texte_spa = None
    if spa.exists():
        texte_spa = spa.read_text(encoding='utf-8')
    else:
        idx_racine = depot / 'index.html'
        if idx_racine.exists() and "fetch('content/books/" in idx_racine.read_text(encoding='utf-8'):
            texte_spa = idx_racine.read_text(encoding='utf-8')
            spa.write_text(texte_spa, encoding='utf-8')
    if texte_spa:
        # depuis site/, content/ est à un niveau : ../content/books/
        (sortie / 'ancien-lecteur.html').write_text(
            preparer_ancien_lecteur(texte_spa, '../content/books/', '../'), encoding='utf-8')
    else:
        avertissements.append('ancien lecteur introuvable — site/ancien-lecteur.html absent')

    # ---- publication à la racine du dépôt (source Pages : main, chemin /)
    n_copies = 0
    if opts.publier:
        racine = Path(opts.publier).resolve()
        if not (racine / 'content').is_dir():
            print(f'!! --publier {racine} : pas de content/ ici, publication annulée')
            return 1
        for chemin in sorted(sortie.rglob('*')):
            cible = racine / chemin.relative_to(sortie)
            if chemin.is_dir():
                cible.mkdir(exist_ok=True)
                continue
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(chemin, cible)
            n_copies += 1
        if texte_spa:
            # à la racine, les fetch d'origine (content/books/…) sont déjà corrects
            (racine / 'ancien-lecteur.html').write_text(
                preparer_ancien_lecteur(texte_spa, 'content/books/', './'), encoding='utf-8')
        (racine / '.nojekyll').touch(exist_ok=True)

    # ---- rapport
    taille_index = (sortie / 'recherche-index.js').stat().st_size
    taille_hl = (sortie / 'hors-ligne.html').stat().st_size
    print('=== Génération terminée ===')
    print(f'livres : {len(livres)} | leçons : {total_lecons} ({total_ok} transcrites) | introductions : {total_intro}')
    print(f'pages HTML : {n_pages} | fichiers copiés à la racine : {n_copies}')
    print(f'index de recherche : {len(entrees_lecons)} entrées, {mo_octets(taille_index)} | hors-ligne : {mo_octets(taille_hl)}')
    if avertissements:
        print(f'avertissements ({len(avertissements)}) :')
        for a in avertissements[:20]:
            print('  -', a)
    return 0


if __name__ == '__main__':
    sys.exit(main())
