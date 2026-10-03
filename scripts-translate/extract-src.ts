/**
 * Minhāj — Extraction d'une source à traduire vers /home/z/tr-src/{docId}.html
 * + {docId}.meta.json (bookId, titleFr officiel s'il existe déjà).
 *
 * L'agent principal lit ensuite la source, traduit en HTML miroir (placeholders
 * {{U1}}…{{Un}} pour href/src), et écrit /home/z/tr-out/{docId}.html.
 *
 * Usage: bun run scripts-translate/extract-src.ts <docId>
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync } from "fs";
import path from "path";

const CONTENT = path.join(process.cwd(), "content");
const TR_SRC = "/home/z/tr-src";

const docId = process.argv[2];
if (!docId) {
  console.error("Usage: bun run scripts-translate/extract-src.ts <docId>");
  process.exit(1);
}

const booksDir = path.join(CONTENT, "books");
for (const f of readdirSync(booksDir)) {
  if (!f.endsWith(".json")) continue;
  const abs = path.join(booksDir, f);
  let data: any;
  try {
    data = JSON.parse(readFileSync(abs, "utf-8"));
  } catch {
    continue;
  }
  let kind: "intro" | "lesson" | null = null;
  let doc: any = null;
  if (data?.intro?.docId === docId && data.intro.html) {
    kind = "intro";
    doc = data.intro;
  } else {
    doc = (data?.lessons ?? []).find((l: any) => l.docId === docId && l.html);
    if (doc) kind = "lesson";
  }
  if (!kind) continue;

  mkdirSync(TR_SRC, { recursive: true });
  const html = doc.html as string;
  writeFileSync(path.join(TR_SRC, `${docId}.html`), html, "utf-8");
  writeFileSync(
    path.join(TR_SRC, `${docId}.meta.json`),
    JSON.stringify(
      {
        docId,
        bookId: data.id,
        kind,
        titleAr: doc.titleAr ?? "",
        titleFr: doc.titleFr ?? "",
        extractedAt: new Date().toISOString(),
      },
      null,
      2
    ) + "\n",
    "utf-8"
  );
  // Liste les URLs uniques (pour le protocole placeholders {{U1}}…{{Un}})
  const urls = [...html.matchAll(/(?:href|src)="([^"]+)"/g)].map((m) => m[1]);
  const unique = [...new Set(urls)];
  console.log(`✅ Source extraite : /home/z/tr-src/${docId}.html (${kind}, ${Math.round(html.length / 1024)} Ko)`);
  console.log(`   meta  : /home/z/tr-src/${docId}.meta.json (bookId=${data.id})`);
  if (unique.length) {
    console.log(`   ${unique.length} URL(s) à préserver via placeholders :`);
    unique.forEach((u, i) => console.log(`   {{U${i + 1}}} = ${u.slice(0, 100)}`));
  } else {
    console.log("   Aucune URL à préserver.");
  }
  process.exit(0);
}
console.error(`✗ docId ${docId} introuvable (ou HTML vide) dans content/books/*.json`);
process.exit(1);
