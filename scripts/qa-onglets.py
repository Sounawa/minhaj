#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA navigateur — onglets rétractables (cycles + niveaux imbriqués).

Vérifie, via Playwright (chromium headless) :
  1. accueil : 3 <details class="cycle"> et 9 <details class="niveau"> refermés
     au chargement, 64 cartes dans le DOM, page compacte ;
  2. onglets de la barre collante : clic = ouvre la série demandée, referme les
     autres, marque l'onglet actif, met à jour l'ancre ; la série ouverte ne
     montre que ses 3 sous-onglets niveaux (cartes masquées) ;
  3. sous-onglet niveau : clic = déplie ses cartes (5-9 selon le niveau) ;
  4. bouton « Tout déplier / Tout replier » : cycles ET niveaux ;
  5. ancres #cycle-… et #niveau-… (fil d'Ariane des pages livre/leçon) :
     déplient les ancêtres ;
  6. mémorisation sessionStorage (cycles + niveaux) ;
  7. recherche française et arabe toujours fonctionnelle ;
  8. hors-ligne.html (file://) : 6 cycles et 18 niveaux rétractables,
     carte -> ancre livre (déplie les ancêtres) ;
  9. console sans erreur partout.

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
        n_niveaux = page.locator('details.niveau').count()
        controle('accueil : 9 sous-onglets (details.niveau)', n_niveaux == 9, f'trouvés {n_niveaux}')
        fermes = page.eval_on_selector_all(
            'details.cycle, details.niveau',
            'els => ({t:els.length, f:els.filter(e => !e.open).length})')
        controle('accueil : 12 repliables refermés au chargement',
                 fermes['t'] == 12 and fermes['f'] == 12, str(fermes))
        cartes = page.locator('.carte').count()
        controle('accueil : 64 cartes dans le DOM', cartes == 64, f'cartes {cartes}')
        v0 = visibles(page)
        controle('accueil : 0 carte visible (tout refermé)', v0 == 0, f'visibles {v0}')
        h_collapse = page.evaluate('document.body.scrollHeight')
        controle('accueil : hauteur compacte (< 2600px)', h_collapse < 2600, f'{h_collapse}px')

        # onglet Collège : ouvre la série, mais les niveaux restent refermés
        page.click('.cycle-nav a[data-cible="cycle-es"]')
        page.wait_for_timeout(350)
        etat = page.evaluate('''() => {
          const g=id=>document.getElementById(id);
          const niv=[].slice.call(document.querySelectorAll('#cycle-es details.niveau'));
          return {ep:g('cycle-ep').open, es:g('cycle-es').open, ta:g('cycle-tanawi').open,
                  niv:niv.length, nivFermes:niv.filter(n=>!n.open).length,
                  hash:location.hash,
                  actif:!!document.querySelector('.cycle-nav a[data-cible="cycle-es"][data-ouvert]')};
        }''')
        controle('onglet Collège : ouvre es / referme les autres',
                 etat['es'] and not etat['ep'] and not etat['ta'], str(etat))
        controle('onglet Collège : 3 niveaux dans la série, tous refermés',
                 etat['niv'] == 3 and etat['nivFermes'] == 3, str(etat))
        controle('onglet Collège : onglet marqué actif', etat['actif'])
        controle('onglet Collège : ancre mise à jour', etat['hash'] == '#cycle-es')
        v = visibles(page)
        controle('onglet Collège : 0 carte visible (niveaux fermés)', v == 0, f'visibles {v}')
        sum_niv = page.eval_on_selector_all(
            '#cycle-es details.niveau > summary.niveau-tete .niveau-n',
            'els => els.map(e=>e.textContent.trim())')
        controle('onglet Collège : effectifs affichés (6/7/7)',
                 sum_niv == ['6 manuels', '7 manuels', '7 manuels'], str(sum_niv))

        # sous-onglet niveau : clic = déplie les cartes du niveau
        page.click('#niveau-1es > summary.niveau-tete')
        page.wait_for_timeout(250)
        v1 = visibles(page)
        n1 = page.evaluate("() => document.querySelectorAll('#niveau-1es .carte').length")
        controle('niveau 1ᵉʳ collège : 6 cartes dépliées',
                 v1 == 6 and n1 == 6, f'visibles {v1} / DOM {n1}')
        page.click('#niveau-2es > summary.niveau-tete')
        page.wait_for_timeout(250)
        v2 = visibles(page)
        controle('niveau 2ᵉ collège ajouté : 13 cartes visibles', v2 == 13, f'visibles {v2}')
        page.click('#niveau-1es > summary.niveau-tete')
        page.wait_for_timeout(250)
        v2b = visibles(page)
        controle('replier 1ᵉʳ collège : 7 cartes visibles', v2b == 7, f'visibles {v2b}')
        page.click('#niveau-2es > summary.niveau-tete')
        page.wait_for_timeout(200)

        # onglet Primaire (accordéon entre cycles)
        page.click('.cycle-nav a[data-cible="cycle-ep"]')
        page.wait_for_timeout(350)
        etat2 = page.evaluate('''() => ({
          ep:document.getElementById('cycle-ep').open,
          es:document.getElementById('cycle-es').open})''')
        controle('onglet Primaire : bascule accordéon', etat2['ep'] and not etat2['es'], str(etat2))
        sum_ep = page.evaluate(
            "() => [].map.call(document.querySelectorAll('#cycle-ep details.niveau > summary.niveau-tete .niveau-n'), e=>e.textContent.trim())")
        controle('onglet Primaire : effectifs affichés (5/6/6)',
                 sum_ep == ['5 manuels', '6 manuels', '6 manuels'], str(sum_ep))

        # sommaire (summary) du cycle togglable
        page.click('#cycle-ep > summary.cycle-tete')
        page.wait_for_timeout(200)
        ep_ferme = page.evaluate("() => !document.getElementById('cycle-ep').open")
        controle('bandeau du cycle : clic replie', ep_ferme)
        page.click('#cycle-ep > summary.cycle-tete')
        page.wait_for_timeout(200)

        # tout déplier / replier : cycles ET niveaux
        page.click('#bascule-tout')
        page.wait_for_timeout(350)
        etat3 = page.evaluate('''() => ({
          c:document.querySelectorAll('details.cycle[open]').length,
          n:document.querySelectorAll('details.niveau[open]').length,
          lib:document.getElementById('bascule-tout').textContent,
          pressed:document.getElementById('bascule-tout').getAttribute('aria-pressed')})''')
        controle('« Tout déplier » : 3 cycles + 9 niveaux ouverts',
                 etat3['c'] == 3 and etat3['n'] == 9, str(etat3))
        v3 = visibles(page)
        controle('« Tout déplier » : 64 cartes visibles', v3 == 64, f'visibles {v3}')
        controle('« Tout déplier » : libellé devient « Tout replier »',
                 etat3['lib'] == 'Tout replier' and etat3['pressed'] == 'true')
        page.click('#bascule-tout')
        page.wait_for_timeout(300)
        etat4 = page.evaluate('''() => ({
          c:document.querySelectorAll('details.cycle[open]').length,
          n:document.querySelectorAll('details.niveau[open]').length})''')
        controle('« Tout replier » : 0 cycle + 0 niveau ouverts',
                 etat4['c'] == 0 and etat4['n'] == 0, str(etat4))

        # mémorisation sessionStorage (cycle + niveau)
        page.click('.cycle-nav a[data-cible="cycle-tanawi"]')
        page.wait_for_timeout(300)
        page.click('#niveau-tanawi-2 > summary.niveau-tete')
        page.wait_for_timeout(250)
        # sans l'ancre : la restauration sessionStorage est volontairement
        # éclipsée par le traitement d'ancre quand un hash est présent
        page.evaluate("history.replaceState(null,'','index.html')")
        page.reload(wait_until='networkidle')
        memo = page.evaluate('''() => ({
          ta:document.getElementById('cycle-tanawi').open,
          n2:document.getElementById('niveau-tanawi-2').open,
          ep:document.getElementById('cycle-ep').open})''')
        controle('sessionStorage : Lycée + 2ᵉ lycée rouverts après rechargement',
                 memo['ta'] and memo['n2'] and not memo['ep'], str(memo))

        # ancres depuis les fils d'Ariane : déplient les ancêtres
        # (état vierge : on purge la mémoire pour ne pas cumuler les groupes)
        page.evaluate('sessionStorage.clear()')
        page.reload(wait_until='networkidle')
        page.goto(f'{base}/index.html#niveau-3es', wait_until='networkidle')
        an = page.evaluate('''() => ({
          es:document.getElementById('cycle-es').open,
          n:document.getElementById('niveau-3es').open,
          v:document.getElementById('niveau-3es').checkVisibility({checkVisibilityCSS:true})})''')
        controle('ancre #niveau-3es : cycle es + niveau 3es ouverts, groupe visible',
                 an['es'] and an['n'] and an['v'], str(an))
        v_a = visibles(page)
        controle('ancre #niveau-3es : 7 cartes visibles', v_a == 7, f'visibles {v_a}')

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
        page.click('#niveau-2es > summary.niveau-tete')
        page.wait_for_timeout(400)
        page.screenshot(path=str(shots / 'accueil-college-niveau.png'), full_page=True)

        # page leçon : spot check (h2 + arabe RTL) + fil d'ariane vers l'accueil
        page.goto(f'{base}/livres/hadith-tanawi-3/index.html', wait_until='networkidle')
        fil_ok = page.locator('a[href="../../index.html#cycle-tanawi"]').count() >= 1
        fil_niv = page.locator('a[href="../../index.html#niveau-tanawi-3"]').count() >= 1
        controle('sommaire livre : fil pointe #cycle-tanawi', fil_ok)
        controle('sommaire livre : fil pointe #niveau-tanawi-3', fil_niv)
        page.click('.lecons li.fait a >> nth=1')
        page.wait_for_load_state('networkidle')
        lec = page.evaluate('''() => ({
          h2:document.querySelectorAll('.contenu h2').length,
          rtl:document.querySelectorAll('.contenu span[dir="rtl"]').length,
          titre:document.title.slice(0,40)})''')
        controle('page leçon : h2 + arabe dir=rtl présents',
                 lec['h2'] > 0 and lec['rtl'] > 0, str(lec))

        # ---------- mobile 390 ----------
        ctx_m = navigateur.new_context(viewport={'width': 390, 'height': 844})
        pm = ctx_m.new_page()
        errs_m = []
        pm.on('pageerror', lambda e: errs_m.append(str(e)))
        pm.goto(f'{base}/index.html', wait_until='networkidle')
        pm.click('.cycle-nav a[data-cible="cycle-es"]')
        pm.wait_for_timeout(350)
        v_m = visibles(pm)
        controle('mobile 390 : onglet Collège -> 0 carte (niveaux fermés)', v_m == 0, f'{v_m}')
        pm.click('#niveau-2es > summary.niveau-tete')
        pm.wait_for_timeout(350)
        v_m2 = visibles(pm)
        controle('mobile 390 : niveau 2ᵉ collège -> 7 cartes visibles', v_m2 == 7, f'{v_m2}')
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
          niveaux:document.querySelectorAll('details.niveau').length,
          fermes:document.querySelectorAll('details.cycle, details.niveau').length -
                 document.querySelectorAll('details.cycle[open], details.niveau[open]').length,
          cartes:document.querySelectorAll('.carte').length})''')
        controle('hors-ligne : 6 cycles + 18 niveaux, tous refermés',
                 hl['cycles'] == 6 and hl['niveaux'] == 18 and hl['fermes'] == 24, str(hl))
        controle('hors-ligne : 64 cartes', hl['cartes'] == 64, str(hl['cartes']))
        pl.click('details.cycle > summary.cycle-tete >> nth=0')
        pl.wait_for_timeout(200)
        premier = pl.evaluate("() => document.querySelector('details.cycle').open")
        controle('hors-ligne : clic sur bandeau déplie', premier)
        v_hl = visibles(pl)
        controle('hors-ligne : cycle ouvert -> 0 carte (niveaux fermés)', v_hl == 0, f'{v_hl}')
        pl.click('#niveau-4ep > summary.niveau-tete')
        pl.wait_for_timeout(250)
        v_hl2 = visibles(pl)
        controle('hors-ligne : niveau 4ᵉ primaire -> 5 cartes visibles', v_hl2 == 5, f'{v_hl2}')
        pl.click('.carte >> nth=0')
        pl.wait_for_timeout(600)
        livre_ouvert = pl.evaluate('''() => {
          const el=document.querySelector('[id^="livre-"]');
          const ancetres=[].slice.call(document.querySelectorAll(
            'details.contenu-ouvert, details')).filter(d=>d.open).length;
          return el && el.checkVisibility({checkVisibilityCSS:true}) && ancetres>0;
        }''')
        controle('hors-ligne : carte -> section livre visible (ancêtres dépliés)', livre_ouvert)
        taille_hl = (DEPOT / 'hors-ligne.html').stat().st_size
        controle('hors-ligne : taille > 500 Ko', taille_hl > 500_000,
                 f'{taille_hl / 1e6:.1f} Mo')
        controle('hors-ligne : console sans erreur', not errs_hl, '; '.join(errs_hl[:3]))
        pl.screenshot(path=str(shots / 'hors-ligne.png'))
        ctx.close()
        navigateur.close()

    print('=== QA onglets rétractables (cycles + niveaux) ===')
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
