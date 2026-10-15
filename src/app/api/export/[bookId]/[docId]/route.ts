import { NextResponse } from "next/server";
import { getDoc } from "@/lib/minhaj";
import {
  xmlEscape,
  xhtmlSanitize,
  xhtmlBalance,
  markQuranQuotes,
  SHARED_CSS,
  STAR_SVG,
  zipStore,
  encUtf8,
  asciiSlug,
  docLabel,
  type DocLike,
} from "@/lib/export-shared";

export const dynamic = "force-dynamic";

/* ————————————————————————————————————————————————————————————————
 * Export d'une leçon : HTML autonome (impression/PDF) ou EPUB 3.
 *  GET /api/export/{bookId}/{docId}?format=html|epub
 * ———————————————————————————————————————————————————————————————— */

/** Fichier HTML autonome, prêt pour l'impression / « Enregistrer en PDF ». */
function buildStandaloneHtml(doc: DocLike): string {
  const meta = [
    docLabel(doc),
    doc.level?.shortFr,
    doc.subject?.titleFr,
    doc.savant ? "traduction savante" : null,
  ]
    .filter(Boolean)
    .map((s) => xmlEscape(String(s)))
    .join('<span class="sep">·</span>');
  const frPane = doc.htmlFr
    ? `<section class="pane pane-fr"><p class="pane-label">Français — traduction${doc.savant ? " savante" : ""}</p><div class="lesson-content">${markQuranQuotes(doc.htmlFr, "fr")}</div></section>`
    : "";
  const arPane = doc.html
    ? `<section class="pane pane-ar"><p class="pane-label">العربية — النص الأصلي</p><div class="lesson-content" lang="ar" dir="rtl">${markQuranQuotes(doc.html, "ar")}</div></section>`
    : "";
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${xmlEscape(doc.titleFr || doc.titleAr)} — Minhāj</title>
<style>${SHARED_CSS}</style>
</head>
<body>
<header>
<h1>${xmlEscape(doc.titleFr || doc.titleAr)}</h1>
<div class="ornament">${STAR_SVG}</div>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(doc.titleAr)}</p>
<p class="meta">${meta}<span class="sep">·</span>${xmlEscape(doc.bookTitleFr)}</p>
</header>
${frPane}
${arPane}
<footer>Minhāj — Taʿlīm ʿatīq · programme officiel du ministère des Habous et des Affaires islamiques (Royaume du Maroc)</footer>
</body>
</html>`;
}

/** EPUB 3 minimal (OCF 3.0) — entrées stockées ; mimetype en tête, sans extra. */
function buildEpub(doc: DocLike): Uint8Array {
  const id = `minhaj-${doc.bookId}-${doc.isIntro ? "intro" : (doc.index ?? 0) + 1}`;
  const title = `${doc.titleFr || doc.titleAr} — ${doc.bookTitleFr}`;
  const lang = doc.htmlFr ? "fr" : "ar";

  const navXhtml = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(title)}</title></head>
<body>
<nav epub:type="toc" id="toc"><h1>Sommaire</h1>
<ol><li><a href="lesson.xhtml">${xmlEscape(title)}</a></li></ol>
</nav>
<nav epub:type="landmarks" hidden=""><ol>
<li><a epub:type="bodymatter" href="lesson.xhtml">Contenu</a></li>
</ol></nav>
</body>
</html>`;

  const contentOpf = `<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="${lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:${id}</dc:identifier>
<dc:title>${xmlEscape(title)}</dc:title>
<dc:language>${lang}</dc:language>
<dc:creator>Ministère des Habous et des Affaires islamiques (Royaume du Maroc)</dc:creator>
<dc:publisher>Minhāj — Taʿlīm ʿatīq</dc:publisher>
<meta property="dcterms:modified">2024-01-01T00:00:00Z</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="css" href="style.css" media-type="text/css"/>
<item id="lesson" href="lesson.xhtml" media-type="application/xhtml+xml"/>
</manifest>
<spine><itemref idref="lesson"/></spine>
</package>`;

  const meta = [docLabel(doc), doc.level?.shortFr, doc.subject?.titleFr]
    .filter(Boolean)
    .map((s) => xmlEscape(String(s)))
    .join(" · ");
  const frPane = doc.htmlFr
    ? `<section class="pane pane-fr" epub:type="chapter"><p class="pane-label">Français — traduction${doc.savant ? " savante" : ""}</p>
<div class="lesson-content">${xhtmlBalance(xhtmlSanitize(markQuranQuotes(doc.htmlFr, "fr")))}</div></section>`
    : "";
  const arPane = doc.html
    ? `<section class="pane pane-ar"><p class="pane-label">العربية — النص الأصلي</p>
<div class="lesson-content" lang="ar" dir="rtl">${xhtmlBalance(xhtmlSanitize(markQuranQuotes(doc.html, "ar")))}</div></section>`
    : "";
  const lessonXhtml = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<header>
<h1>${xmlEscape(doc.titleFr || doc.titleAr)}</h1>
<div class="ornament">${STAR_SVG}</div>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(doc.titleAr)}</p>
<p class="meta">${meta} · ${xmlEscape(doc.bookTitleFr)}</p>
</header>
${frPane}
${arPane}
<footer>Minhāj — Taʿlīm ʿatīq · programme officiel des Habous (Royaume du Maroc)</footer>
</body>
</html>`;

  return zipStore([
    { name: "mimetype", data: encUtf8.encode("application/epub+zip") },
    {
      name: "META-INF/container.xml",
      data: encUtf8.encode(`<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>`),
    },
    { name: "OEBPS/content.opf", data: encUtf8.encode(contentOpf) },
    { name: "OEBPS/nav.xhtml", data: encUtf8.encode(navXhtml) },
    { name: "OEBPS/style.css", data: encUtf8.encode(SHARED_CSS) },
    { name: "OEBPS/lesson.xhtml", data: encUtf8.encode(lessonXhtml) },
  ]);
}

export async function GET(
  req: Request,
  { params }: { params: Promise<{ bookId: string; docId: string }> },
) {
  const { bookId, docId } = await params;
  const format = new URL(req.url).searchParams.get("format") ?? "html";
  try {
    const doc = (await getDoc(bookId, docId)) as DocLike | null;
    if (!doc) {
      return NextResponse.json(
        { error: "not_found", message: `Document ${docId} introuvable dans le manuel ${bookId}.` },
        { status: 404 },
      );
    }
    if (doc.pdfOnly || (!doc.html && !doc.htmlFr)) {
      return NextResponse.json(
        { error: "no_content", message: "Ce document est publié au format PDF officiel uniquement." },
        { status: 415 },
      );
    }
    if (format === "epub") {
      const epub = buildEpub(doc);
      return new NextResponse(epub as unknown as BodyInit, {
        headers: {
          "Content-Type": "application/epub+zip",
          "Content-Disposition": `attachment; filename="minhaj-${asciiSlug(doc.titleFr || doc.titleAr)}.epub"`,
          "Cache-Control": "no-store",
        },
      });
    }
    const html = buildStandaloneHtml(doc);
    return new NextResponse(html, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Disposition": `inline; filename="minhaj-${asciiSlug(doc.titleFr || doc.titleAr)}.html"`,
        "Cache-Control": "no-store",
      },
    });
  } catch (e) {
    return NextResponse.json(
      { error: "export_failed", message: e instanceof Error ? e.message : String(e) },
      { status: 503 },
    );
  }
}
