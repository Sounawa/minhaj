#!/usr/bin/env python3
"""Serve le dépôt Minhaj sous /minhaj/ (simulation GitHub Pages) pour la QA headless."""
import http.server
import functools
import sys

RACINE = sys.argv[1] if len(sys.argv) > 1 else '/home/z/my-project/minhaj'
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8788


class Gestionnaire(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # retire le préfixe /minhaj/ et sert depuis la racine du dépôt
        if path.startswith('/minhaj/'):
            path = path[len('/minhaj'):]
        elif path == '/minhaj':
            path = '/'
        return super().translate_path(path)

    def log_message(self, fmt, *args):
        pass


handler = functools.partial(Gestionnaire, directory=RACINE)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), handler).serve_forever()
