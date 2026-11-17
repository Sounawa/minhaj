#!/usr/bin/env python3
"""Télécharge une fois les polices Google Fonts utilisées par le site
(Amiri, EB Garamond, Noto Naskh Arabic) dans content/fonts/, afin que
scripts/build-site.py puisse les embarquer en base64 dans hors-ligne.html
(la version hors-ligne devient totalement autonome, même sous file://).

Usage : python3 scripts/fetch-polices.py   (accès réseau requis, exécution unique ;
les fichiers sont ensuite versionnés et le build reste hors-ligne).
"""
import re
import sys
import urllib.request
from pathlib import Path

URL_CSS = ('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700'
           '&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600'
           '&family=Noto+Naskh+Arabic:wght@400;500;700&display=swap')
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/120.0.0.0 Safari/537.36')  # UA moderne : woff2 + unicode-range


def main():
    rep = Path(__file__).resolve().parent.parent / 'content' / 'fonts'
    rep.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(URL_CSS, headers={'User-Agent': UA})
    css = urllib.request.urlopen(req, timeout=30).read().decode('utf-8')
    (rep / 'google-fonts.css').write_text(css, encoding='utf-8')
    urls = sorted(set(re.findall(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', css)))
    manquants = []
    for u in urls:
        nom = u.rsplit('/', 1)[-1].split('?')[0]
        cible = rep / nom
        if cible.exists() and cible.stat().st_size > 0:
            continue
        data = urllib.request.urlopen(
            urllib.request.Request(u, headers={'User-Agent': UA}), timeout=30).read()
        cible.write_bytes(data)
    total = 0
    n_ok = 0
    for u in urls:
        nom = u.rsplit('/', 1)[-1].split('?')[0]
        cible = rep / nom
        if cible.exists() and cible.stat().st_size > 0:
            n_ok += 1
            total += cible.stat().st_size
        else:
            manquants.append(nom)
    print(f'polices : {n_ok}/{len(urls)} fichiers, {total} octets dans content/fonts/')
    if manquants:
        print('MANQUANTS :', ', '.join(manquants))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
