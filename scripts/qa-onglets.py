#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA navigateur — onglets rétractables de l'accueil + hors-ligne.

Vérifie, via Playwright (chromium headless) :
  1. accueil : 3 <details class="cycle"> refermés au chargement, 64 cartes dans le DOM ;
  2. onglets : clic sur un onglet de la barre collante = ouvre la série demandée,
     referme les autres, marque l'onglet actif, met à jour l'ancre ;
  3. bouton « Tout déplier / Tout replier » ;
  4. ancres #cycle-… et #niveau-… (fil d'Ariane des pages livre/leçon) ;
  5. mémorisation sessionStorage ;
  6. recherche française et arabe toujours fonctionnelle ;
  7. hors-ligne.html (file://) : cycles rétractables, carte -> ancre livre ;
  8. console sans erreur partout.

Usage : python3 scripts/qa-onglets.py
"""

import http.server
import os
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

DEPOT = Path(__file__).resolve().parent.parent
PORT = 8777


class Serveur(socketserver.TCPServer):
    allow_reuse_address = True


def demarrer_serveur():
    os.chdir(DEPOT)
    handler = http.server.SimpleHTTPRequestHandler
    srv = Serveur(('127.0.0.1', PORT), handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    return srv


def visibles(page, sel='.carte'):
    # NB : offsetParent reste non nul dans un <details> fermé (slotting) —
    # checkVisibility() tient compte du contenu masqué par details fermé.
    return page.eval_on_selector_all(
        sel, '''els => els.filter(e => {
          if (e.checkVisibility) return e.checkVisibility({checkVisibilityCSS: true});
          const r = e.getBoundingClientRect();
          return r.width > 0 && r.height > 0;
        }).length''')


def main():
    erreurs = []
    ok = []

    def controle(nom, cond, detail=''):
        (ok if cond else erreurs).append(f'{nom}{(" — " + detail) if detail else ""}')

    demarrer_serveur()
    base = f'http://127.0.0.1:{PORT}'

    with sync_playwright() as pw:
        navigateur = pw.chromium.launch()
        ctx = navigateur.new_context(viewport={'width': 1280, 'height': 900})

        # ---------- accueil (racine publiée) ----------
        page = ctx.new_page()
        console_msgs = []
        page.on('console', lambda m: console_msgs.append(m.text) if m.type == 'error' else None)
        page.on('pageerror', lambda e: console_msgs.append(str(e)))
        page.goto(f'{base}/index.html', wait_until='networkidle')

        n_details = page.locator('details.cycle').count()
        controle('accueil : 3 onglets (details.cycle)', n_details == 3, f'trouvés {n_details}')
        fermes = page.eval_on_selector_all(
            'details.cycle', 'els => els.filter(e => !e.open).length')
        controle('accueil : 3 onglets refermés au chargement', fermes == 3, f'fermés {fermes}')
        cartes = page.locator('.carte').count()
        controle('accueil : 64 cartes dans le DOM', cartes == 64, f'cartes {cartes}')
        h_collapse = page.evaluate('document.body.scrollHeight')
        controle('accueil : hauteur compacte (< 2600px)', h_collapse < 2600, f'{h_collapse}px')

        # onglet Collège
        page.click('.cycle-nav a[data-cible="cycle-es"]')
        page.wait_for_timeout(350)
        etat = page.evaluate('''() => {
          const g=id=>document.getElementById(id);
          return {ep:g('cycle-ep').open, es:g('cycle-es').open, ta:g('cycle-tanawi').open,
                  hash:location.hash,
                  actif:!!document.querySelector('.cycle-nav a[data-cible="cycle-es"][data-ouvert]')};
        }''')
        controle('onglet Collège : ouvre es / referme les autres',
                 etat['es'] and not etat['ep'] and not etat['ta'], str(etat))
        controle('onglet Collège : onglet marqué actif', etat['actif'])
        controle('onglet Collège : ancre mise à jour', etat['hash'] == '#cycle-es')
        v = visibles(page)
        controle('onglet Collège : 20 cartes visibles', v == 20, f'visibles {v}')

        # onglet Primaire (accordéon)
        page.click('.cycle-nav a[data-cible="cycle-ep"]')
        page.wait_for_timeout(350)
        etat2 = page.evaluate('''() => ({
          ep:document.getElementById('cycle-ep').open,
          es:document.getElementById('cycle-es').open})''')
        controle('onglet Primaire : bascule accordéon', etat2['ep'] and not etat2['es'], str(etat2))
        v2 = visibles(page)
        controle('onglet Primaire : 17 cartes visibles', v2 == 17, f'visibles {v2}')

        # sommaire (summary) togglable
        page.click('#cycle-ep > summary.cycle-tete')
        page.wait_for_timeout(200)
        ep_ferme = page.evaluate("() => !document.getElementById('cycle-ep').open")
        controle('bandeau du cycle : clic replie', ep_ferme)
        page.click('#cycle-ep > summary.cycle-tete')
        page.wait_for_timeout(200)

        # tout déplier / replier
        page.click('#bascule-tout')
        page.wait_for_timeout(350)
        etat3 = page.evaluate('''() => ({
          n:document.querySelectorAll('details.cycle[open]').length,
          lib:document.getElementById('bascule-tout').textContent,
          pressed:document.getElementById('bascule-tout').getAttribute('aria-pressed')})''')
        controle('« Tout déplier » : 3 ouverts', etat3['n'] == 3, str(etat3))
        v3 = visibles(page)
        controle('« Tout déplier » : 64 cartes visibles', v3 == 64, f'visibles {v3}')
        controle('« Tout déplier » : libellé devient « Tout replier »',
                 etat3['lib'] == 'Tout replier' and etat3['pressed'] == 'true')
        page.click('#bascule-tout')
        page.wait_for_timeout(300)
        etat4 = page.evaluate("() => document.querySelectorAll('details.cycle[open]').length")
        controle('« Tout replier » : 0 ouverts', etat4 == 0, f'ouverts {etat4}')

        # mémorisation sessionStorage
        page.click('.cycle-nav a[data-cible="cycle-tanawi"]')
        page.wait_for_timeout(300)
        page.reload(wait_until='networkidle')
        memo = page.evaluate('''() => ({
          ta:document.getElementById('cycle-tanawi').open,
          ep:document.getElementById('cycle-ep').open})''')
        controle('sessionStorage : Lycée rouvert après rechargement',
                 memo['ta'] and not memo['ep'], str(memo))

        # ancres depuis les fils d'Ariane
        page.goto(f'{base}/index.html#niveau-3es', wait_until='networkidle')
        an = page.evaluate('''() => ({
          es:document.getElementById('cycle-es').open,
          n:document.getElementById('niveau-3es').checkVisibility({checkVisibilityCSS:true})})''')
        controle('ancre #niveau-3es : cycle es ouvert, groupe visible',
                 an['es'] and an['n'], str(an))

        page.goto(f'{base}/index.html#cycle-ep', wait_until='networkidle')
        an2 = page.evaluate("() => document.getElementById('cycle-ep').open")
        controle('ancre #cycle-ep : cycle ouvert', an2)

        # recherche française + arabe
        page.goto(f'{base}/index.html', wait_until='networkidle')
        page.fill('#champ', 'voisin')
        page.wait_for_timeout(1600)
        res_fr = page.locator('#resultats li').count()
        controle('recherche française (voisin) : résultats', res_fr > 0, f'{res_fr} résultats')
        page.fill('#champ', 'الشفعة')
        page.wait_for_timeout(1600)
        res_ar = page.locator('#resultats li').count()
        controle('recherche arabe (الشفعة) : résultats', res_ar > 0, f'{res_ar} résultats')

        controle('accueil : console sans erreur', not console_msgs,
                 '; '.join(console_msgs[:3]))

        # captures
        shots = DEPOT / 'qa-shots-onglets'
        shots.mkdir(exist_ok=True)
        page.goto(f'{base}/index.html', wait_until='networkidle')
        page.evaluate('sessionStorage.clear()')
        page.reload(wait_until='networkidle')
        page.screenshot(path=str(shots / 'accueil-replie.png'))
        page.click('.cycle-nav a[data-cible="cycle-es"]')
        page.wait_for_timeout(400)
        page.screenshot(path=str(shots / 'accueil-college.png'))

        # page leçon : spot check + fil d'ariane vers l'accueil
        page.goto(f'{base}/livres/hadith-tanawi-3/index.html', wait_until='networkidle')
        fil_ok = page.locator('a[href="../../index.html#cycle-tanawi"]').count() >= 1
        controle('sommaire livre : fil pointe #cycle-tanawi', fil_ok)

        # ---------- mobile 390 ----------
        ctx_m = navigateur.new_context(viewport={'width': 390, 'height': 844})
        pm = ctx_m.new_page()
        errs_m = []
        pm.on('pageerror', lambda e: errs_m.append(str(e)))
        pm.goto(f'{base}/index.html', wait_until='networkidle')
        pm.click('.cycle-nav a[data-cible="cycle-es"]')
        pm.wait_for_timeout(350)
        v_m = visibles(pm)
        controle('mobile 390 : onglet Collège -> 20 cartes visibles', v_m == 20, f'{v_m}')
        pm.screenshot(path=str(shots / 'accueil-mobile.png'), full_page=True)
        controle('mobile 390 : console sans erreur', not errs_m, '; '.join(errs_m[:2]))
        ctx_m.close()

        # ---------- hors-ligne (file://) ----------
        pl = ctx.new_page()
        errs_hl = []
        pl.on('pageerror', lambda e: errs_hl.append(str(e)))
        pl.goto(f'file://{DEPOT}/hors-ligne.html', wait_until='load')
        pl.wait_for_timeout(800)
        hl = pl.evaluate('''() => ({
          cycles:document.querySelectorAll('details.cycle').length,
          fermes:document.querySelectorAll('details.cycle').length -
                 document.querySelectorAll('details.cycle[open]').length,
          cartes:document.querySelectorAll('.carte').length})''')
        controle('hors-ligne : 6 onglets, refermés', hl['cycles'] == 6 and hl['fermes'] == 6, str(hl))
        controle('hors-ligne : 64 cartes', hl['cartes'] == 64, str(hl['cartes']))
        pl.click('details.cycle > summary.cycle-tete >> nth=0')
        pl.wait_for_timeout(200)
        premier = pl.evaluate("() => document.querySelector('details.cycle').open")
        controle('hors-ligne : clic sur bandeau déplie', premier)
        pl.click('.carte >> nth=0')
        pl.wait_for_timeout(600)
        livre_ouvert = pl.evaluate('''() => {
          const el=document.querySelector('[id^="livre-"]');
          return el && el.checkVisibility({checkVisibilityCSS:true});
        }''')
        controle('hors-ligne : carte -> section livre visible', livre_ouvert)
        taille_hl = (DEPOT / 'hors-ligne.html').stat().st_size
        controle('hors-ligne : taille > 500 Ko', taille_hl > 500_000,
                 f'{taille_hl / 1e6:.1f} Mo')
        controle('hors-ligne : console sans erreur', not errs_hl, '; '.join(errs_hl[:3]))
        pl.screenshot(path=str(shots / 'hors-ligne.png'))
        ctx.close()
        navigateur.close()

    print('=== QA onglets rétractables ===')
    for o in ok:
        print('  PASS', o)
    if erreurs:
        for e in erreurs:
            print('  FAIL', e)
        return 1
    print(f'{len(ok)} contrôles PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
