/**
 * Minhāj — Construction de la file de traduction (content/agent-queue.json).
 *
 * Parcourt tous les manuels téléchargés (content/books/*.json) et liste les
 * documents dont htmlFr est absent : introductions d'abord, puis leçons par
 * taille croissante (les plus courtes d'abord pour maximiser l'avancement).
 *
 * Usage: bun run scripts-translate/build-queue.ts
 */
import { readFileSync, writeFileSync, existsSync } from "fs";
import { readdirSync } from "fs";
import path from "path";

const CONTENT = path.join(process.cwd(), "content");

interface QueueItem {
  docId: string;
  bookId: string;
  kind: "intro" | "lesson";
  titleAr: string;
  size: number; // taille de l'HTML arabe en octets
  status: "pending" | "done";
}

const booksDir = path.join(CONTENT, "books");
if (!existsSync(booksDir)) {
  console.error("✗ Dossier content/books introuvable.");
  process.exit(1);
}

const items: QueueItem[] = [];
for (const f of readdirSync(booksDir)) {
  if (!f.endsWith(".json")) continue;
  const bookId = f.replace(/\.json$/, "");
  let data: any;
  try {
    data = JSON.parse(readFileSync(path.join(booksDir, f), "utf-8"));
  } catch (e) {
    console.warn(`⚠︎ ${f} illisible (${e instanceof Error ? e.message : e}) — ignoré`);
    continue;
  }
  if (data?.intro?.html && !(data.intro.htmlFr || "").trim()) {
    items.push({
      docId: data.intro.docId,
      bookId,
      kind: "intro",
      titleAr: data.intro.titleAr ?? "",
      size: Buffer.byteLength(data.intro.html, "utf-8"),
      status: "pending",
    });
  }
  for (const l of data?.lessons ?? []) {
    if (l?.html && !(l.htmlFr || "").trim()) {
      items.push({
        docId: l.docId,
        bookId,
        kind: "lesson",
        titleAr: l.titleAr ?? "",
        size: Buffer.byteLength(l.html, "utf-8"),
        status: "pending",
      });
    }
  }
}

// Introductions d'abord, puis par taille croissante.
items.sort((a, b) => {
  if (a.kind !== b.kind) return a.kind === "intro" ? -1 : 1;
  return a.size - b.size;
});

const queue = {
  version: 3,
  generatedAt: new Date().toISOString(),
  note: "File de traduction Minhāj — l'agent principal traduit lui-même chaque document (règle absolue : aucun sous-agent). 1 intro ≤ 28 Ko ou 2-4 leçons par vague.",
  items,
};

const outPath = path.join(CONTENT, "agent-queue.json");
writeFileSync(outPath, JSON.stringify(queue, null, 2) + "\n", "utf-8");
console.log(`✅ agent-queue.json : ${items.length} document(s) à traduire.`);
for (const it of items.slice(0, 10)) {
  console.log(`   ${it.kind === "intro" ? "★" : "•"} ${it.docId} (${it.bookId}, ${Math.round(it.size / 1024)} Ko)`);
}
if (items.length > 10) console.log(`   … et ${items.length - 10} autres.`);
