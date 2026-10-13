/**
 * Minhāj — couche d'accès au contenu (côté serveur uniquement).
 * Source de vérité : le système de fichiers (content/).
 *  - content/manifest.json          → structure du programme (64 livres)
 *  - content/books/{bookId}.json    → manuel téléchargé (intro + leçons, HTML bilingue)
 *  - content/agent-queue.json       → file de traduction
 */
import { promises as fs } from "fs";
import path from "path";

const CONTENT_DIR = path.join(process.cwd(), "content");

// ———————————————————————————————————————— Types publics

export interface ManifestLevel {
  id: string;
  cycle: "ep" | "es" | "tanawi";
  year: number;
  labelAr: string;
  labelFr: string;
  shortFr: string;
}
export interface ManifestSubject {
  id: string;
  labelAr: string;
  titleFr: string;
  translit: string;
  icon: string;
}
export interface ManifestBook {
  id: string;
  subject: string;
  level: string;
  titleAr: string;
  titleFr: string;
  order: number;
  known?: boolean;
  textbookAr?: string;
}
export interface Manifest {
  version: number;
  provisional: boolean;
  note: string;
  program: {
    nameAr: string;
    nameFr: string;
    publisherAr: string;
    publisherFr: string;
    goalBooks: number;
    goalDocs: number;
  };
  levels: ManifestLevel[];
  subjects: ManifestSubject[];
  books: ManifestBook[];
}

export interface LessonDoc {
  docId: string;
  titleAr: string;
  titleFr?: string;
  html: string;
  htmlFr?: string;
  sample?: boolean;
  pdfUrl?: string | null;
  pdfOnly?: boolean;
}
export interface BookFile {
  id: string;
  subject?: string;
  level?: string;
  titleAr: string;
  titleFr?: string;
  pdfUrl?: string | null;
  unpublished?: boolean;
  intro?: {
    docId: string;
    titleAr: string;
    titleFr?: string;
    html: string;
    htmlFr?: string;
    sample?: boolean;
  } | null;
  lessons: LessonDoc[];
}

export interface BookSummary {
  id: string;
  subject: string;
  level: string;
  titleAr: string;
  titleFr: string;
  textbookAr?: string;
  order: number;
  downloaded: boolean;
  unpublished?: boolean;
  hasIntro: boolean;
  introFr: boolean;
  lessonsTotal: number;
  lessonsFr: number;
  docsTotal: number;
  docsFr: number;
  /** Documents de ce livre en traduction savante (registre, avec FR réellement écrit). */
  docsSavant: number;
}

export interface LibraryPayload {
  program: Manifest["program"];
  levels: ManifestLevel[];
  subjects: (ManifestSubject & { booksCount: number })[];
  books: BookSummary[];
  stats: {
    booksTotal: number;
    booksDownloaded: number;
    docsTotal: number;
    docsFr: number;
    goalDocs: number;
    goalBooks: number;
    /** Documents bénéficiant d'une traduction savante (registre). */
    docsSavant: number;
  };
}

export interface DocPayload {
  bookId: string;
  bookTitleAr: string;
  bookTitleFr: string;
  level: ManifestLevel | null;
  subject: ManifestSubject | null;
  docId: string;
  isIntro: boolean;
  titleAr: string;
  titleFr: string;
  html: string;
  htmlFr: string;
  sample: boolean;
  hasFr: boolean;
  /** Traduction savante (registre hand/LLM validé) — sinon qualité machine (GT). */
  savant: boolean;
  index: number;
  count: number;
  pdfUrl: string | null;
  pdfOnly: boolean;
  prev: { docId: string; titleFr: string; titleAr: string } | null;
  next: { docId: string; titleFr: string; titleAr: string } | null;
}

export interface LessonSummary {
  docId: string;
  titleAr: string;
  titleFr: string;
  hasFr: boolean;
  sample: boolean;
  pdfOnly: boolean;
  /** Traduction savante (registre) — sinon qualité machine (GT). */
  savant: boolean;
}
export interface BookDetailPayload {
  program: Manifest["program"];
  book: BookSummary;
  level: ManifestLevel | null;
  subject: ManifestSubject | null;
  intro: LessonSummary | null;
  lessons: LessonSummary[];
}

// ———————————————————————————————————————— Cache mémoire (mtime)

interface CacheEntry<T> {
  mtimeMs: number;
  data: T;
}
const cache = new Map<string, CacheEntry<unknown>>();
const TTL_MS = 30_000;
const stamps = new Map<string, number>(); // clé → dernier accès

async function readJsonCached<T>(relPath: string): Promise<T | null> {
  const abs = path.join(CONTENT_DIR, relPath);
  try {
    const stat = await fs.stat(abs);
    const cached = cache.get(relPath) as CacheEntry<T> | undefined;
    const now = Date.now();
    if (cached && Math.abs(cached.mtimeMs - stat.mtimeMs) < 1 && now - (stamps.get(relPath) || 0) < TTL_MS) {
      return cached.data;
    }
    const raw = await fs.readFile(abs, "utf-8");
    const data = JSON.parse(raw) as T;
    cache.set(relPath, { mtimeMs: stat.mtimeMs, data });
    stamps.set(relPath, now);
    return data;
  } catch {
    return null;
  }
}

// ———————————————————————————————————————— Registre des traductions savantes
// scripts-translate/savant-registry.json — docIds bénéficiant d'une traduction
// révisée (main ou LLM validée). Les autres documents bilingues sont en
// qualité machine (GT). Cache mtime → suivi à chaud des injections.

interface SavantRegistry {
  hand?: string[];
  llm?: Record<string, unknown>;
}
let savantCache: { mtimeMs: number; ids: Set<string> } | null = null;

async function getSavantIds(): Promise<Set<string>> {
  const abs = path.join(process.cwd(), "scripts-translate", "savant-registry.json");
  try {
    const stat = await fs.stat(abs);
    if (savantCache && Math.abs(savantCache.mtimeMs - stat.mtimeMs) < 1) {
      return savantCache.ids;
    }
    const raw = await fs.readFile(abs, "utf-8");
    const reg = JSON.parse(raw) as SavantRegistry;
    const ids = new Set<string>([...(reg.hand ?? []), ...Object.keys(reg.llm ?? {})]);
    savantCache = { mtimeMs: stat.mtimeMs, ids };
    return ids;
  } catch {
    return savantCache?.ids ?? new Set<string>();
  }
}

// ———————————————————————————————————————— Accès

export async function getManifest(): Promise<Manifest | null> {
  return readJsonCached<Manifest>("manifest.json");
}

export async function getBookFile(bookId: string): Promise<BookFile | null> {
  const safe = bookId.replace(/[^a-z0-9-]/gi, "");
  if (!safe || safe !== bookId) return null;
  return readJsonCached<BookFile>(`books/${bookId}.json`);
}

function summarize(
  bookDef: ManifestBook,
  file: BookFile | null,
  savantIds: Set<string> | null,
): BookSummary {
  const lessonsTotal = file?.lessons?.length ?? 0;
  const lessonsFr = file?.lessons?.filter((l) => (l.htmlFr ?? "").trim().length > 0).length ?? 0;
  const hasIntro = Boolean(file?.intro);
  const introFr = Boolean(file?.intro?.htmlFr && file.intro.htmlFr.trim().length > 0);
  // Couche savante : docIds du registre disposant d'un FR réellement écrit.
  const docs = file
    ? ([file.intro, ...(file.lessons ?? [])].filter(Boolean) as Array<{ docId: string; htmlFr?: string }>)
    : [];
  const savantDocs = savantIds ? new Set(docs.filter((d) => savantIds.has(d.docId) && (d.htmlFr ?? "").trim().length > 0).map((d) => d.docId)) : new Set<string>();
  return {
    id: bookDef.id,
    subject: bookDef.subject,
    level: bookDef.level,
    // Le fichier réel prime sur le manifeste (titres traduits en continu)
    titleAr: file?.titleAr || bookDef.textbookAr || bookDef.titleAr,
    titleFr: (file?.titleFr && file.titleFr.trim()) || bookDef.titleFr,
    textbookAr: bookDef.textbookAr,
    order: bookDef.order,
    downloaded: Boolean(file),
    unpublished: Boolean(file?.unpublished),
    hasIntro,
    introFr,
    lessonsTotal,
    lessonsFr,
    docsTotal: lessonsTotal + (hasIntro ? 1 : 0),
    docsFr: lessonsFr + (introFr ? 1 : 0),
    docsSavant: savantDocs.size,
  };
}

export async function getLibrary(): Promise<LibraryPayload> {
  const manifest = await getManifest();
  if (!manifest) {
    throw new Error("manifest.json introuvable dans content/");
  }
  const files = await Promise.all(manifest.books.map((b) => getBookFile(b.id)));
  const savantIdsForBooks = await getSavantIds();
  const books = manifest.books.map((b, i) =>
    summarize(b, files[i] as BookFile | null, savantIdsForBooks),
  );
  const subjects = manifest.subjects.map((s) => ({
    ...s,
    booksCount: manifest.books.filter((b) => b.subject === s.id).length,
  }));
  // Compteur des traductions savantes (registre) sur les docs réellement bilingues.
  // Dédupliqué par docId : certains docIds sont partagés intro/leçon dans un même livre.
  const savantIds = await getSavantIds();
  const savantWithFr = new Set<string>();
  for (const f of files) {
    if (!f) continue;
    const docs = [f.intro, ...(f.lessons ?? [])].filter(Boolean) as Array<{ docId: string; htmlFr?: string }>;
    for (const d of docs) {
      if (savantIds.has(d.docId) && (d.htmlFr ?? "").trim().length > 0) {
        savantWithFr.add(d.docId);
      }
    }
  }
  const docsSavant = savantWithFr.size;
  const stats = {
    booksTotal: manifest.books.length,
    booksDownloaded: books.filter((b) => b.downloaded).length,
    docsTotal: books.reduce((acc, b) => acc + b.docsTotal, 0),
    docsFr: books.reduce((acc, b) => acc + b.docsFr, 0),
    goalDocs: manifest.program.goalDocs,
    goalBooks: manifest.program.goalBooks,
    docsSavant,
  };
  return { program: manifest.program, levels: manifest.levels, subjects, books, stats };
}

export async function getBookDetail(bookId: string): Promise<BookDetailPayload | null> {
  const manifest = await getManifest();
  if (!manifest) return null;
  const bookDef = manifest.books.find((b) => b.id === bookId);
  if (!bookDef) return null;
  const file = await getBookFile(bookId);
  const savantIdsForDetail = await getSavantIds();
  const book = summarize(bookDef, file, savantIdsForDetail);
  const level = manifest.levels.find((l) => l.id === bookDef.level) ?? null;
  const subject = manifest.subjects.find((s) => s.id === bookDef.subject) ?? null;
  const savantIds = savantIdsForDetail;
  const intro: LessonSummary | null = file?.intro
    ? {
        docId: file.intro.docId,
        titleAr: file.intro.titleAr,
        titleFr: file.intro.titleFr || "",
        hasFr: Boolean((file.intro.htmlFr || "").trim()),
        sample: Boolean(file.intro.sample),
        savant: savantIds.has(file.intro.docId),
      }
    : null;
  const lessons: LessonSummary[] = (file?.lessons ?? []).map((l) => ({
    docId: l.docId,
    titleAr: l.titleAr,
    titleFr: l.titleFr || "",
    hasFr: Boolean((l.htmlFr || "").trim()),
    sample: Boolean(l.sample),
    pdfOnly: Boolean(l.pdfOnly),
    savant: savantIds.has(l.docId),
  }));
  return { program: manifest.program, book, level, subject, intro, lessons };
}

// ———————————————————————————————————————— Recherche globale

export interface SearchHit {
  bookId: string;
  bookTitleFr: string;
  bookTitleAr: string;
  levelShortFr: string;
  docId: string;
  isIntro: boolean;
  titleAr: string;
  titleFr: string;
  snippet: string;
  score: number;
  lang: "fr" | "ar" | "both";
  /** Traduction savante (registre) — sinon qualité machine (GT). */
  savant: boolean;
}
export interface SearchPayload {
  query: string;
  total: number;
  truncated: boolean;
  hits: SearchHit[];
}

/** Retire les balises HTML, décode les entités usuelles, compacte les blancs. */
function stripHtml(html: string): string {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&rsquo;/g, "'")
    .replace(/&laquo;/g, "«")
    .replace(/&raquo;/g, "»")
    .replace(/&#(\d+);/g, (_, d: string) => String.fromCodePoint(Number(d)))
    .replace(/\s+/g, " ")
    .trim();
}

/** Pliage des accents français (é→e, œ→oe…). */
function foldFr(s: string): string {
  return s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/œ/g, "oe").replace(/æ/g, "ae").toLowerCase();
}

/** Normalisation arabe : suppression du tashkīl, unification des alifs/taʾ marbūṭa. */
function normAr(s: string): string {
  return s
    .replace(/[\u064B-\u065F\u0670\u06D6-\u06ED]/g, "") // tashkīl + signes coraniques
    .replace(/[أإآٱ]/g, "ا")
    .replace(/ى/g, "ي")
    .replace(/ة/g, "ه")
    .replace(/ـ/g, "") // tatwīl
    .replace(/\s+/g, " ")
    .trim();
}

function normAll(s: string): string {
  return normAr(foldFr(s));
}

interface IndexEntry {
  bookId: string;
  bookTitleFr: string;
  bookTitleAr: string;
  levelShortFr: string;
  docId: string;
  isIntro: boolean;
  titleAr: string;
  titleFr: string;
  /** Titres + texte FR normalisés pour la recherche. */
  nTitleFr: string;
  nTitleAr: string;
  nTextFr: string;
  nTextAr: string;
  /** Texte brut pour l'extrait. */
  plainFr: string;
  plainAr: string;
}

let indexPromise: Promise<IndexEntry[]> | null = null;
let indexStamp = "";

/**
 * Empreinte légère du corpus (mtime + taille du manifeste et de chaque livre).
 * Permet d'invalider l'index de recherche dès qu'un fichier est retraduit,
 * sans redémarrer le serveur.
 */
async function corpusStamp(): Promise<string> {
  try {
    const parts: string[] = [];
    const manifestStat = await fs.stat(path.join(CONTENT_DIR, "manifest.json"));
    parts.push(`manifest:${manifestStat.mtimeMs}:${manifestStat.size}`);
    const booksDir = path.join(CONTENT_DIR, "books");
    const files = (await fs.readdir(booksDir)).filter((f) => f.endsWith(".json")).sort();
    for (const f of files) {
      const st = await fs.stat(path.join(booksDir, f));
      parts.push(`${f}:${st.mtimeMs}:${st.size}`);
    }
    return parts.join("|");
  } catch {
    return "";
  }
}

async function getSearchIndex(): Promise<IndexEntry[]> {
  const stamp = await corpusStamp();
  if (!indexPromise || stamp !== indexStamp) {
    indexStamp = stamp;
    indexPromise = (async () => {
      const manifest = await getManifest();
      if (!manifest) return [] as IndexEntry[];
      const entries: IndexEntry[] = [];
      for (const bookDef of manifest.books) {
        const file = await getBookFile(bookDef.id);
        if (!file) continue;
        const level = manifest.levels.find((l) => l.id === bookDef.level);
        const base = {
          bookId: bookDef.id,
          bookTitleFr: (file.titleFr && file.titleFr.trim()) || bookDef.titleFr,
          bookTitleAr: bookDef.textbookAr || bookDef.titleAr,
          levelShortFr: level?.shortFr ?? "",
        };
        const docs: Array<{ docId: string; titleAr: string; titleFr?: string; html?: string; htmlFr?: string; isIntro: boolean }> = [];
        if (file.intro) docs.push({ ...file.intro, isIntro: true });
        for (const l of file.lessons ?? []) docs.push({ ...l, isIntro: false });
        for (const d of docs) {
          const plainFr = stripHtml(d.htmlFr || "");
          const plainAr = stripHtml(d.html || "");
          entries.push({
            ...base,
            docId: d.docId,
            isIntro: d.isIntro,
            titleAr: d.titleAr,
            titleFr: d.titleFr || "",
            nTitleFr: normAll(d.titleFr || ""),
            nTitleAr: normAr(d.titleAr || ""),
            nTextFr: normAll(plainFr),
            nTextAr: normAr(plainAr),
            plainFr,
            plainAr,
          });
        }
      }
      return entries;
    })();
    // En cas d'échec : on relancera à la prochaine recherche.
    indexPromise.catch(() => {
      indexPromise = null;
    });
  }
  return indexPromise;
}

function makeSnippet(plain: string, nText: string, query: string, max = 160): string {
  const i = nText.indexOf(query);
  if (i === -1) return plain.slice(0, max).trim();
  const start = Math.max(0, i - Math.floor(max / 3));
  const end = Math.min(plain.length, start + max);
  let snippet = plain.slice(start, end).trim();
  if (start > 0) snippet = "… " + snippet;
  if (end < plain.length) snippet = snippet + " …";
  return snippet;
}

export async function searchCorpus(rawQuery: string, limit = 25): Promise<SearchPayload> {
  const query = normAll(rawQuery.trim().replace(/\s+/g, " "));
  if (query.length < 2) return { query: rawQuery, total: 0, truncated: false, hits: [] };
  const [index, savantIds] = await Promise.all([getSearchIndex(), getSavantIds()]);
  const hits: SearchHit[] = [];
  for (const e of index) {
    let score = 0;
    let lang: SearchHit["lang"] = "fr";
    const inTitleFr = e.nTitleFr.includes(query);
    const inTitleAr = e.nTitleAr.includes(query);
    const inTextFr = e.nTextFr.includes(query);
    const inTextAr = e.nTextAr.includes(query);
    if (inTitleFr) score += 60;
    if (inTitleAr) score += 60;
    if (inTextFr) score += 6;
    if (inTextAr) score += 4;
    if (!score) continue;
    if ((inTitleFr || inTextFr) && (inTitleAr || inTextAr)) lang = "both";
    else if (inTitleAr || inTextAr) lang = "ar";
    // Bonus si le titre commence par la requête (motif fort).
    if (e.nTitleFr.startsWith(query) || e.nTitleAr.startsWith(query)) score += 20;
    const snippet =
      inTextFr || inTitleFr
        ? makeSnippet(e.plainFr, e.nTextFr, query)
        : makeSnippet(e.plainAr, e.nTextAr, query);
    hits.push({
      bookId: e.bookId,
      bookTitleFr: e.bookTitleFr,
      bookTitleAr: e.bookTitleAr,
      levelShortFr: e.levelShortFr,
      docId: e.docId,
      isIntro: e.isIntro,
      titleAr: e.titleAr,
      titleFr: e.titleFr || e.titleAr,
      snippet,
      score,
      lang,
      savant: savantIds.has(e.docId),
    });
  }
  hits.sort((a, b) => b.score - a.score || a.titleFr.localeCompare(b.titleFr));
  const total = hits.length;
  return {
    query: rawQuery,
    total,
    truncated: total > limit,
    hits: hits.slice(0, limit),
  };
}

export async function getDoc(bookId: string, docId: string): Promise<DocPayload | null> {
  const manifest = await getManifest();
  if (!manifest) return null;
  const bookDef = manifest.books.find((b) => b.id === bookId);
  if (!bookDef) return null;
  const file = await getBookFile(bookId);
  if (!file) return null;
  const savantIds = await getSavantIds();

  const seq: Array<{ doc: NonNullable<BookFile["intro"]> | LessonDoc; isIntro: boolean }> = [];
  if (file.intro) seq.push({ doc: file.intro, isIntro: true });
  for (const l of file.lessons ?? []) seq.push({ doc: l, isIntro: false });

  const idx = seq.findIndex((s) => s.doc.docId === docId);
  if (idx === -1) return null;
  const cur = seq[idx];
  const prev = idx > 0 ? seq[idx - 1] : null;
  const next = idx < seq.length - 1 ? seq[idx + 1] : null;
  const level = manifest.levels.find((l) => l.id === bookDef.level) ?? null;
  const subject = manifest.subjects.find((s) => s.id === bookDef.subject) ?? null;

  const nav = (s: { doc: { docId: string; titleFr?: string; titleAr: string }; isIntro: boolean } | null) =>
    s ? { docId: s.doc.docId, titleFr: s.doc.titleFr || s.doc.titleAr, titleAr: s.doc.titleAr } : null;

  return {
    bookId,
    bookTitleAr: bookDef.textbookAr || bookDef.titleAr,
    bookTitleFr: (file.titleFr && file.titleFr.trim()) || bookDef.titleFr,
    level,
    subject,
    docId: cur.doc.docId,
    isIntro: cur.isIntro,
    titleAr: cur.doc.titleAr,
    titleFr: cur.doc.titleFr || "",
    html: cur.doc.html || "",
    htmlFr: cur.doc.htmlFr || "",
    sample: Boolean((cur.doc as LessonDoc).sample),
    hasFr: Boolean((cur.doc.htmlFr || "").trim()),
    savant: savantIds.has(cur.doc.docId),
    pdfUrl: ((cur.doc as LessonDoc).pdfUrl as string | null) ?? null,
    pdfOnly: Boolean((cur.doc as LessonDoc).pdfOnly),
    index: idx,
    count: seq.length,
    prev: nav(prev),
    next: nav(next),
  };
}
