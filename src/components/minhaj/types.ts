/** Types côté client — miroir des payloads API (src/lib/minhaj.ts). */

export interface Level {
  id: string;
  cycle: "ep" | "es" | "tanawi";
  year: number;
  labelAr: string;
  labelFr: string;
  shortFr: string;
}
export interface Subject {
  id: string;
  labelAr: string;
  titleFr: string;
  translit: string;
  icon: string;
  booksCount: number;
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
  program: {
    nameAr: string;
    nameFr: string;
    publisherAr: string;
    publisherFr: string;
    goalBooks: number;
    goalDocs: number;
  };
  levels: Level[];
  subjects: Subject[];
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
export interface LessonSummary {
  docId: string;
  titleAr: string;
  titleFr: string;
  hasFr: boolean;
  sample: boolean;
}
export interface BookDetailPayload {
  program: LibraryPayload["program"];
  book: BookSummary;
  level: Level | null;
  subject: Omit<Subject, "booksCount"> | null;
  intro: LessonSummary | null;
  lessons: LessonSummary[];
}
export interface DocPayload {
  bookId: string;
  bookTitleAr: string;
  bookTitleFr: string;
  level: Level | null;
  subject: Omit<Subject, "booksCount"> | null;
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

export type CycleId = "all" | "ep" | "es" | "tanawi";

export const CYCLES: { id: CycleId; label: string; desc: string }[] = [
  { id: "all", label: "Tous les cycles", desc: "Les 64 manuels" },
  { id: "ep", label: "Primaire", desc: "الابتدائي العتيق — 6 niveaux" },
  { id: "es", label: "Collège", desc: "الإعدادي العتيق — 3 niveaux" },
  { id: "tanawi", label: "Lycée", desc: "التأهيلي العتيق — 3 niveaux" },
];
