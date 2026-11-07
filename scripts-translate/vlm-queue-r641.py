# -*- coding: utf-8 -*-
"""Minhāj — File VLM résiliente R641 : boucle infinie par image (backoff cap 240 s),
continue la file uniquement sur succès. Budget : 12 images."""
import json, os, subprocess, sys, time
DIR = "/home/z/my-project/tr-tmp/qa-crops-r641"
import importlib.util
spec = importlib.util.spec_from_file_location("hadith3vlm", "/home/z/my-project/scripts-translate/hadith3-vlm-read-r641.py")
_m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_m)
PROMPTS = _m.PROMPTS

QUEUE = ["p65-a-banniere-l9","p58-a-titre","p58-b-tamhid","p58-c-quote","p59-a-1024",
         "p59-b-ext","p59-d-1028","p59-e-bio","p61-a-thania-1027","p62-mid","p63-mid","p64-mid"]

def attempt(name):
    out = f"{DIR}/_read-{name}.json"
    r = subprocess.run(["z-ai","vision","-p",PROMPTS[name],"-i",f"{DIR}/{name}.png","-o",out],
                       capture_output=True, text=True, timeout=200)
    if r.returncode == 0 and os.path.exists(out):
        try:
            d = json.load(open(out, encoding="utf-8"))
            if d.get("content"): return True
        except Exception: pass
    return False

i = 0
while i < len(QUEUE):
    name = QUEUE[i]
    out = f"{DIR}/_read-{name}.json"
    if os.path.exists(out):
        try:
            if json.load(open(out, encoding="utf-8")).get("content"):
                print(f"[{time.strftime('%H:%M:%S')}] {name} déjà lu — skip", flush=True)
                i += 1; continue
        except Exception: pass
    if attempt(name):
        print(f"[{time.strftime('%H:%M:%S')}] OK {name}", flush=True)
        i += 1
        time.sleep(20)  # espace entre lectures
    else:
        print(f"[{time.strftime('%H:%M:%S')}] KO {name} — nouvelle tentative dans 100 s", flush=True)
        time.sleep(100)
print("FILE TERMINEE", flush=True)
