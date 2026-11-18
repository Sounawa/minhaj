/**
 * Minhāj — Réparation des titres (livres et leçons) depuis les slugs SEF,
 * puis re-traduction française en batch.
 *
 * Le slug Joomla encode : {docId}-{titre-leçon}-كتاب-{nom-du-livre}...
 * Usage: bun run scripts-recovery/fix-titles.ts
 */
import { readFileSync, writeFileSync, readdirSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

const idx: Record<string, string> = JSON.parse(readFileSync("/home/z/tr-src/raw/index.json", "utf-8"));
const slugOf = new Map<string, string>();
for (const [docId, p] of Object.entries(idx)) {
  if (docId.startsWith("cat:")) continue;
  const last = p.split("/").pop() ?? "";
  slugOf.set(docId, last.replace(/\.html$/, ""));
}

const cleanTitle = (s: string) =>
  s.replace(/-/g, " ")
    .replace(/\s*التعليم العتيق\s*/g, " ")
    .replace(/\s*لتعليم العتيق\s*/g, " ")
    .replace(/\s+/g, " ")
    .trim();

async function translate(text: string): Promise<string> {
  const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=ar&tl=fr&dt=t&q=${encodeURIComponent(text)}`;
  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" } });
      if (res.status === 429 || res.status === 503) { await sleep(20000); continue; }
      if (!res.ok) throw new Error("HTTP " + res.status);
      const d = (await res.json()) as any;
      return (d[0] as any[]).map((s) => (s && s[0]) || "").join("");
    } catch (e) {
      if (attempt === 5) throw e;
      await sleep(3000 * attempt);
    }
  }
  return "";
}

const generic = new Set(["المدخل", "المقدمة", "كتاب", "درس"]);

for (const f of readdirSync(BOOKS)) {
  if (!f.endsWith(".json")) continue;
  const p = path.join(BOOKS, f);
  const b = JSON.parse(readFileSync(p, "utf-8"));

  // ——— Titre du livre
  let bookTitleAr = "";
  const introSlug = b.intro ? slugOf.get(b.intro.docId) : undefined;
  if (introSlug) {
    const s = introSlug.replace(/^\d+-/, "");
    bookTitleAr = s.replace(/^كتاب-/, "");
  }
  if (!bookTitleAr && b.lessons?.length) {
    for (const l of b.lessons) {
      const s = slugOf.get(l.docId) ?? "";
      const m = s.match(/^\d+-.+?-كتاب-(.+)$/);
      if (m) { bookTitleAr = m[1]; break; }
    }
  }
  if (!bookTitleAr) {
    // retirer le préfixe كتاب- du slug de la 1re leçon
    const s = (slugOf.get(b.lessons?.[0]?.docId ?? "") ?? "").replace(/^\d+-كتاب-/, "");
    if (s) bookTitleAr = s;
  }
  bookTitleAr = cleanTitle(bookTitleAr || b.titleAr || "");
  const bookNeedsFr = !b.titleFr || b.titleFr.length < 14 || /^(Le livre|Introduction|Exégèse coranique|Jurisprudence|Monothéisme|Logique|Droit)/.test(b.titleFr) === false === false && b.titleFr === "Le livre" || b.titleFr === "Introduction";
  const changedBook = bookTitleAr && bookTitleAr !== b.titleAr;
  if (changedBook) b.titleAr = bookTitleAr;

  // ——— Titres des leçons (depuis le slug : partie avant -كتاب-)
  const toTranslate: Array<() => void> = [];
  for (const l of b.lessons ?? []) {
    const s = slugOf.get(l.docId) ?? "";
    let t = "";
    const m = s.match(/^\d+-(.+?)(?:-كتاب-.+)?$/);
    if (m) t = m[1];
    t = cleanTitle(t);
    if (t && t.length > 3 && !generic.has(t) && t !== l.titleAr) {
      l.titleAr = t;
      l.titleFr = ""; // à retraduire
      toTranslate.push(() => undefined);
    }
  }
  if (b.intro) {
    const s = slugOf.get(b.intro.docId) ?? "";
    const m = s.match(/^\d+-(.+)$/);
    let t = m ? cleanTitle(m[1]) : "";
    if (t.length > 3 && t !== b.intro.titleAr) {
      b.intro.titleAr = t;
      b.intro.titleFr = "";
    }
  }

  // ——— Re-traduction des titres manquants (batch 20 lignes)
  const titles: string[] = [];
  const targets: Array<(v: string) => void> = [];
  if (!b.titleFr || b.titleFr === "Le livre" || b.titleFr === "Introduction") {
    titles.push(b.titleAr);
    targets.push((v) => { b.titleFr = v.replace(/\n+/g, " ").trim(); });
  }
  if (b.intro && !b.intro.titleFr) {
    titles.push(b.intro.titleAr);
    targets.push((v) => { b.intro.titleFr = v.replace(/\n+/g, " ").trim(); });
  }
  for (const l of b.lessons ?? []) {
    if (!l.titleFr) {
      titles.push(l.titleAr);
      targets.push((v) => { l.titleFr = v.replace(/\n+/g, " ").trim(); });
    }
  }
  for (let i = 0; i < titles.length; i += 20) {
    const batch = titles.slice(i, i + 20);
    const res = await translate(batch.join("\n"));
    const lines = res.split("\n").map((x: string) => x.trim());
    if (lines.length === batch.length) {
      for (let j = 0; j < batch.length; j++) targets[i + j](lines[j]);
    } else {
      for (let j = 0; j < batch.length; j++) {
        const one = await translate(batch[j]);
        targets[i + j](one.replace(/\n+/g, " ").trim());
        await sleep(120);
      }
    }
    await sleep(250);
  }
  writeFileSync(p, JSON.stringify(b, null, 2) + "\n", "utf-8");
  console.log(`✓ ${b.id}: livre « ${b.titleFr?.slice(0, 50) ?? "?"} » | ${titles.length} titres (re)traduits`);
}
console.log("\n✅ Titres réparés.");
