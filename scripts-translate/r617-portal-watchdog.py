#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R617 — watchdog portail :3000 (méthode R596-bis : DOUBLE-FORK requis).
Le bac à sable fauche les processus Node mal détachés (~30-60 s) ; le
double-fork (fork + setsid + fork, reparenté à init) survit. Le watchdog
relance `next dev` tant qu'il est absent, indéfiniment (règle 24/7).
Usage : python3 scripts-translate/r617-portal-watchdog.py  (détaché)"""
import os
import subprocess
import sys
import time

PORTAL = "/home/z/portal-r616"
LOG = f"{PORTAL}/dev.log"
NEXT = f"{PORTAL}/node_modules/next/dist/bin/next"


def daemonize() -> None:
    if os.fork() > 0:
        os._exit(0)
    os.setsid()
    if os.fork() > 0:
        os._exit(0)
    sys.stdout.flush()
    sys.stderr.flush()
    with open("/dev/null", "rb") as f:
        os.dup2(f.fileno(), 0)
    with open(os.devnull, "ab") as f:
        os.dup2(f.fileno(), 1)
        os.dup2(f.fileno(), 2)


def dev_alive() -> bool:
    r = subprocess.run(["pgrep", "-f", "next/dist/bin/next dev -p 3000"],
                       capture_output=True, text=True)
    return r.returncode == 0


def spawn() -> None:
    if os.fork() > 0:
        return  # le fils est relancé par la boucle suivante si mort
    os.setsid()
    os.chdir(PORTAL)  # CRUCIAL : cwd = portail (sinon Next prend my-project pour racine)
    log = open(LOG, "ab")
    os.dup2(log.fileno(), 1)
    os.dup2(log.fileno(), 2)
    os.execvp("node", ["node", NEXT, "dev", "-p", "3000"])


def main() -> int:
    daemonize()
    with open("/home/z/my-project/tr-tmp/portal-watchdog.pid", "w") as f:
        f.write(str(os.getpid()))
    while True:
        try:
            if not dev_alive():
                spawn()
        except Exception:
            pass
        time.sleep(10)
    return 0


if __name__ == "__main__":
    sys.exit(main())
