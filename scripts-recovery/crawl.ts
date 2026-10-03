/**
 * Minhāj — Crawler du programme Taʿlīm ʿatīq via le proxy Google Translate
 * (translate.goog sert l'ARABE ORIGINAL en accès direct).
 *
 * BFS depuis la page du programme : télécharge toutes les pages du domaine
 * habous.gov.ma appartenant au programme (livres, leçons, catégories).
 * Sauvegarde : /home/z/tr-src/raw/{docId}.html + index.json
 *
 * Usage: bun run scripts-recovery/crawl.ts [limite]
 */
import { mkdirSync, existsSync, writeFileSync, readFileSync, statSync } from "fs";
import { createHash } from "crypto";
import path from "path";

const RAW = "/home/z/tr-src/raw";
const SEEN_DB = "/home/z/tr-src/raw/index.json";
mkdirSync(RAW, { recursive: true });

const LIMIT = parseInt(process.argv[2] || "1500", 10);
const PROGRAM = "برنامج-التعليم-العتيق-الرئيسية";
const BOOKS = "الكتب-المدرسية";
const PROXY = "https://www-habous-gov-ma.translate.goog/";
const QS = "?_x_tr_sl=ar&_x_tr_tl=fr&_x_tr_hl=fr";
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36";

interface QItem { url: string; pathAr: string; docId: string; }

let seen: Record<string, string> = {};
if (existsSync(SEEN_DB)) {
  try { seen = JSON.parse(readFileSync(SEEN_DB, "utf-8")); } catch { /* */ }
}

const queue: QItem[] = [];
const inQueue = new Set<string>();

function pushQueue(item: QItem) {
  if (inQueue.has(item.docId) || seen[item.docId]) return;
  inQueue.add(item.docId);
  queue.push(item);
}

/** Extrait les liens du programme (NE modifie PAS inQueue). */
function extractLinks(html: string): QItem[] {
  const out: QItem[] = [];
  const re = /href="(https:\/\/www-habous-gov-ma\.translate\.goog\/([^"?#]+)(\?[^"]*)?)"/g;
  for (const m of html.matchAll(re)) {
    const url = m[1].replace(/&amp;/g, "&");
    let pathAr: string;
    try { pathAr = decodeURIComponent(m[2]); } catch { continue; }
    const segs = pathAr.split("/").filter(Boolean);
    if (!segs.length) continue;
    if (segs[0] !== PROGRAM && segs[0] !== BOOKS) continue;
    const last = segs[segs.length - 1];
    const query = m[3] || "";
    if (!last.endsWith(".html")) {
      // page de catégorie (avec pagination éventuelle ?start=N)
      out.push({ url: PROXY + m[2] + (query || QS), pathAr, docId: "cat:" + pathAr + query });
      continue;
    }
    if (query && /start=|limitstart=|limit=/.test(query)) {
      // page .html avec pagination → traiter comme catégorie
      out.push({ url, pathAr, docId: "cat:" + pathAr + query });
      continue;
    }
    const mm = last.match(/^(\d{3,6})-.+\.html$/);
    if (!mm) continue;
    out.push({ url, pathAr, docId: mm[1] });
  }
  return out;
}

function fileName(item: QItem): string {
  if (item.docId.startsWith("cat:")) {
    // Hash sha1 court du pathAr+query (évite les collisions du base64 tronqué)
    return "cat-" + createHash("sha1").update(item.docId).digest("hex").slice(0, 20) + ".html";
  }
  return item.docId + ".html";
}

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

let fetched = 0;
let failures = 0;
let activeFetches = 0;

async function fetchPage(item: QItem): Promise<string | null> {
  const dest = path.join(RAW, fileName(item));
  if (existsSync(dest) && statSync(dest).size > 2000) {
    return readFileSync(dest, "utf-8"); // cache disque
  }
  for (let attempt = 1; attempt <= 4; attempt++) {
    try {
      const res = await fetch(item.url, { headers: { "User-Agent": UA, "Accept-Language": "ar,fr;q=0.8,en;q=0.5" } });
      if (res.status === 429 || res.status === 503) {
        console.log(`  ⏳ ${item.docId}: HTTP ${res.status}, attente…`);
        await sleep(20000 * attempt);
        continue;
      }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const html = await res.text();
      if (html.length < 1500) throw new Error("page trop courte: " + html.length);
      writeFileSync(dest, html, "utf-8");
      fetched++;
      return html;
    } catch (e) {
      if (attempt === 4) {
        failures++;
        console.log(`  ✗ ${item.docId} (${(e as Error).message})`);
        return null;
      }
      await sleep(5000 * attempt);
    }
  }
  return null;
}

let saveCounter = 0;
function saveIndex() {
  writeFileSync(SEEN_DB, JSON.stringify(seen, null, 1), "utf-8");
}

// Amorçage
if (!seen["main"]) {
  pushQueue({ url: PROXY + encodeURIComponent(PROGRAM + ".html") + QS, pathAr: PROGRAM + ".html", docId: "main" });
} else {
  // Rescan : extraire les liens de toutes les pages déjà en cache disque
  // (les pages .html sont lues depuis le cache — aucun coût réseau).
  const files = readdirSync(RAW);
  let rescanned = 0;
  for (const f of files) {
    if (!f.endsWith(".html")) continue;
    let html: string;
    try { html = readFileSync(path.join(RAW, f), "utf-8"); } catch { continue; }
    for (const l of extractLinks(html)) pushQueue(l);
    rescanned++;
  }
  console.log(`Rescan: ${rescanned} fichiers en cache → ${queue.length} liens en file.`);
}

console.log(`Départ : ${Object.keys(seen).length} pages déjà vues, ${queue.length} en file.`);

async function worker(id: number) {
  let idleRounds = 0;
  for (;;) {
    if (fetched >= LIMIT) return;
    const item = queue.shift();
    if (!item) {
      // file vide : attendre les autres workers (ils peuvent pousser des liens)
      if (activeFetches === 0) {
        idleRounds++;
        if (idleRounds >= 3) return; // vraiment terminé
      } else {
        idleRounds = 0;
      }
      await sleep(2000);
      continue;
    }
    inQueue.delete(item.docId);
    idleRounds = 0;
    if (seen[item.docId]) continue;
    activeFetches++;
    const html = await fetchPage(item);
    activeFetches--;
    if (html) {
      seen[item.docId] = item.pathAr;
      for (const l of extractLinks(html)) pushQueue(l);
      if (++saveCounter % 20 === 0) {
        saveIndex();
        console.log(`[${new Date().toISOString().slice(11, 19)}] ${fetched} téléchargées (+${saveCounter}), ${queue.length} en file, ${Object.keys(seen).length} vues (w${id})`);
      }
    }
    await sleep(250 + Math.random() * 350);
  }
}

const workers = Array.from({ length: 6 }, (_, i) => worker(i + 1));
await Promise.race([
  Promise.all(workers),
  sleep(1000 * 60 * 90).then(() => { console.log("⏱ limite de temps atteinte (90 min)"); }),
]);

saveIndex();
console.log(`\n✅ Crawl : ${fetched} nouvelles pages, ${failures} échecs, ${Object.keys(seen).length} vues au total, ${queue.length} restantes en file.`);
