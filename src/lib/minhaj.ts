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
}
export interface BookFile {
  id: string;
  subject?: string;
  level?: string;
  titleAr: string;
  titleFr?: string;
  pdfUrl?: string | null;
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
  hasIntro: boolean;
  introFr: boolean;
  lessonsTotal: number;
  lessonsFr: number;
  docsTotal: number;
  docsFr: number;
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
  index: number;
  count: number;
  prev: { docId: string; titleFr: string; titleAr: string } | null;
  next: { docId: string; titleFr: string; titleAr: string } | null;
}

export interface LessonSummary {
  docId: string;
  titleAr: string;
  titleFr: string;
  hasFr: boolean;
  sample: boolean;
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

// ———————————————————————————————————————— Accès

export async function getManifest(): Promise<Manifest | null> {
  return readJsonCached<Manifest>("manifest.json");
}

export async function getBookFile(bookId: string): Promise<BookFile | null> {
  const safe = bookId.replace(/[^a-z0-9-]/gi, "");
  if (!safe || safe !== bookId) return null;
  return readJsonCached<BookFile>(`books/${bookId}.json`);
}

function summarize(bookDef: ManifestBook, file: BookFile | null): BookSummary {
  const lessonsTotal = file?.lessons?.length ?? 0;
  const lessonsFr = file?.lessons?.filter((l) => (l.htmlFr ?? "").trim().length > 0).length ?? 0;
  const hasIntro = Boolean(file?.intro);
  const introFr = Boolean(file?.intro?.htmlFr && file.intro.htmlFr.trim().length > 0);
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
    hasIntro,
    introFr,
    lessonsTotal,
    lessonsFr,
    docsTotal: lessonsTotal + (hasIntro ? 1 : 0),
    docsFr: lessonsFr + (introFr ? 1 : 0),
  };
}

export async function getLibrary(): Promise<LibraryPayload> {
  const manifest = await getManifest();
  if (!manifest) {
    throw new Error("manifest.json introuvable dans content/");
  }
  const files = await Promise.all(manifest.books.map((b) => getBookFile(b.id)));
  const books = manifest.books.map((b, i) => summarize(b, files[i] as BookFile | null));
  const subjects = manifest.subjects.map((s) => ({
    ...s,
    booksCount: manifest.books.filter((b) => b.subject === s.id).length,
  }));
  const stats = {
    booksTotal: manifest.books.length,
    booksDownloaded: books.filter((b) => b.downloaded).length,
    docsTotal: books.reduce((acc, b) => acc + b.docsTotal, 0),
    docsFr: books.reduce((acc, b) => acc + b.docsFr, 0),
    goalDocs: manifest.program.goalDocs,
    goalBooks: manifest.program.goalBooks,
  };
  return { program: manifest.program, levels: manifest.levels, subjects, books, stats };
}

export async function getBookDetail(bookId: string): Promise<BookDetailPayload | null> {
  const manifest = await getManifest();
  if (!manifest) return null;
  const bookDef = manifest.books.find((b) => b.id === bookId);
  if (!bookDef) return null;
  const file = await getBookFile(bookId);
  const book = summarize(bookDef, file);
  const level = manifest.levels.find((l) => l.id === bookDef.level) ?? null;
  const subject = manifest.subjects.find((s) => s.id === bookDef.subject) ?? null;
  const intro: LessonSummary | null = file?.intro
    ? {
        docId: file.intro.docId,
        titleAr: file.intro.titleAr,
        titleFr: file.intro.titleFr || "",
        hasFr: Boolean((file.intro.htmlFr || "").trim()),
        sample: Boolean(file.intro.sample),
      }
    : null;
  const lessons: LessonSummary[] = (file?.lessons ?? []).map((l) => ({
    docId: l.docId,
    titleAr: l.titleAr,
    titleFr: l.titleFr || "",
    hasFr: Boolean((l.htmlFr || "").trim()),
    sample: Boolean(l.sample),
  }));
  return { program: manifest.program, book, level, subject, intro, lessons };
}

export async function getDoc(bookId: string, docId: string): Promise<DocPayload | null> {
  const manifest = await getManifest();
  if (!manifest) return null;
  const bookDef = manifest.books.find((b) => b.id === bookId);
  if (!bookDef) return null;
  const file = await getBookFile(bookId);
  if (!file) return null;

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
    bookTitleFr: bookDef.titleFr,
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
    index: idx,
    count: seq.length,
    prev: nav(prev),
    next: nav(next),
  };
}
