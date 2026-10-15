import { NextResponse } from "next/server";
import { getManifest, getBookFile, getSavantIds } from "@/lib/minhaj";
import {
  xmlEscape,
  xhtmlSanitize,
  xhtmlBalance,
  markQuranQuotes,
  SHARED_CSS,
  BOOK_CSS,
  STAR_SVG,
  zipStore,
  encUtf8,
  asciiSlug,
} from "@/lib/export-shared";

export const dynamic = "force-dynamic";

/* ————————————————————————————————————————————————————————————————
 * Export d'un manuel ENTIER (bundle) : HTML autonome multi-documents
 * (sommaire cliquable + impression) ou EPUB 3 (un chapitre par doc).
 *  GET /api/export/{bookId}?format=html|epub
 * Les documents pdfOnly reçoivent une notice « publié au format PDF
 * officiel » — cohérent avec le lecteur en ligne.
 * ———————————————————————————————————————————————————————————————— */

interface BundleDoc {
  docId: string;
  titleAr: string;
  titleFr: string;
  html: string;
  htmlFr: string;
  isIntro: boolean;
  savant: boolean;
  pdfOnly: boolean;
  file: string; // nom de fichier EPUB (intro.xhtml, lecon-01.xhtml…)
  anchor: string; // ancre HTML
  index: number;
  count: number;
}

type FullBundleDoc = BundleDoc;

function docHeading(d: FullBundleDoc): string {
  return d.isIntro ? "Introduction" : `Leçon ${d.index + 1}`;
}

function buildBookHtml(
  bookTitleFr: string,
  bookTitleAr: string,
  metaLine: string,
  docs: FullBundleDoc[],
  autoPrint = false,
): string {
  const tocItems = docs
    .map(
      (d) =>
        `<li><a href="#${d.anchor}">${xmlEscape(d.titleFr || d.titleAr)}</a>${
          d.pdfOnly ? ' <span class="toc-pdf">PDF</span>' : ""
        }</li>`,
    )
    .join("\n");
  const sections = docs
    .map((d) => {
      const meta = [docHeading(d), `${d.index + 1} / ${d.count}`, d.savant ? "traduction savante" : null]
        .filter(Boolean)
        .map((s) => xmlEscape(String(s)))
        .join('<span class="sep">·</span>');
      if (d.pdfOnly || (!d.html && !d.htmlFr)) {
        return `<section class="doc" id="${d.anchor}">
<h2>${xmlEscape(d.titleFr || d.titleAr)}</h2>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(d.titleAr)}</p>
<p class="meta">${meta}</p>
<p class="pdf-note">Leçon publiée au format PDF officiel uniquement — non incluse dans cet export.</p>
</section>`;
      }
      const frPane = d.htmlFr
        ? `<section class="pane pane-fr"><p class="pane-label">Français — traduction${d.savant ? " savante" : ""}</p><div class="lesson-content">${markQuranQuotes(d.htmlFr, "fr")}</div></section>`
        : "";
      const arPane = d.html
        ? `<section class="pane pane-ar"><p class="pane-label">العربية — النص الأصلي</p><div class="lesson-content" lang="ar" dir="rtl">${markQuranQuotes(d.html, "ar")}</div></section>`
        : "";
      return `<section class="doc" id="${d.anchor}">
<div class="doc-header">
<a class="back-toc" href="#sommaire">Sommaire</a>
<h2>${xmlEscape(d.titleFr || d.titleAr)}</h2>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(d.titleAr)}</p>
<p class="meta">${meta}</p>
${frPane}
${arPane}
</div>
</section>`;
    })
    .join("\n");
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${xmlEscape(bookTitleFr)} — Minhāj (manuel complet)</title>
<style>${SHARED_CSS}${BOOK_CSS}</style>
${autoPrint ? '<script>window.addEventListener("load",function(){setTimeout(function(){window.print()},400)})</script>' : ""}
</head>
<body>
<header>
<h1>${xmlEscape(bookTitleFr)}</h1>
<div class="ornament">${STAR_SVG}</div>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(bookTitleAr)}</p>
<p class="meta">${xmlEscape(metaLine)}</p>
</header>
<nav class="toc" id="sommaire" aria-label="Sommaire du manuel">
<h2>Sommaire</h2>
<ol>
${tocItems}
</ol>
</nav>
${sections}
<footer>Minhāj — Taʿlīm ʿatīq · programme officiel du ministère des Habous et des Affaires islamiques (Royaume du Maroc)</footer>
</body>
</html>`;
}

function buildBookEpub(
  bookId: string,
  bookTitleFr: string,
  bookTitleAr: string,
  metaLine: string,
  docs: FullBundleDoc[],
): Uint8Array {
  const id = `minhaj-${bookId}-integral`;
  const hasFr = docs.some((d) => d.htmlFr);
  const lang = hasFr ? "fr" : "ar";

  const navItems = docs
    .map((d) => `<li><a href="${d.file}">${xmlEscape(d.titleFr || d.titleAr)}</a></li>`)
    .join("\n");
  const navXhtml = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(bookTitleFr)}</title></head>
<body>
<nav epub:type="toc" id="toc"><h1>${xmlEscape(bookTitleFr)}</h1>
<ol>
${navItems}
</ol>
</nav>
<nav epub:type="landmarks" hidden=""><ol>
<li><a epub:type="bodymatter" href="${docs[0]?.file ?? "lecon-01.xhtml"}">Contenu</a></li>
</ol></nav>
</body>
</html>`;

  const manifestItems = docs
    .map((d) => `<item id="d-${d.docId}" href="${d.file}" media-type="application/xhtml+xml"/>`)
    .join("\n");
  const spineItems = docs.map((d) => `<itemref idref="d-${d.docId}"/>`).join("\n");
  const contentOpf = `<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="${lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:${id}</dc:identifier>
<dc:title>${xmlEscape(bookTitleFr)}</dc:title>
<dc:language>${lang}</dc:language>
<dc:creator>Ministère des Habous et des Affaires islamiques (Royaume du Maroc)</dc:creator>
<dc:publisher>Minhāj — Taʿlīm ʿatīq</dc:publisher>
<meta property="dcterms:modified">2024-01-01T00:00:00Z</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="css" href="style.css" media-type="text/css"/>
${manifestItems}
</manifest>
<spine>
${spineItems}
</spine>
</package>`;

  const chapters = docs.map((d) => {
    const meta = [docHeading(d), `${d.index + 1} / ${d.count}`, d.savant ? "traduction savante" : null]
      .filter(Boolean)
      .map((s) => xmlEscape(String(s)))
      .join(" · ");
    if (d.pdfOnly || (!d.html && !d.htmlFr)) {
      return `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(d.titleFr || d.titleAr)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<header>
<h1>${xmlEscape(d.titleFr || d.titleAr)}</h1>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(d.titleAr)}</p>
<p class="meta">${meta}</p>
</header>
<p class="pdf-note">Leçon publiée au format PDF officiel uniquement — non incluse dans cet export.</p>
<footer>Minhāj — Taʿlīm ʿatīq</footer>
</body>
</html>`;
    }
    const frPane = d.htmlFr
      ? `<section class="pane pane-fr" epub:type="chapter"><p class="pane-label">Français — traduction${d.savant ? " savante" : ""}</p>
<div class="lesson-content">${xhtmlBalance(xhtmlSanitize(markQuranQuotes(d.htmlFr, "fr")))}</div></section>`
      : "";
    const arPane = d.html
      ? `<section class="pane pane-ar"><p class="pane-label">العربية — النص الأصلي</p>
<div class="lesson-content" lang="ar" dir="rtl">${xhtmlBalance(xhtmlSanitize(markQuranQuotes(d.html, "ar")))}</div></section>`
      : "";
    return `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="${lang}">
<head><meta charset="utf-8"/><title>${xmlEscape(d.titleFr || d.titleAr)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<header>
<h1>${xmlEscape(d.titleFr || d.titleAr)}</h1>
<div class="ornament">${STAR_SVG}</div>
<p class="ar-title" lang="ar" dir="rtl">${xmlEscape(d.titleAr)}</p>
<p class="meta">${meta} · ${xmlEscape(bookTitleFr)}</p>
</header>
${frPane}
${arPane}
<footer>Minhāj — Taʿlīm ʿatīq · programme officiel des Habous (Royaume du Maroc)</footer>
</body>
</html>`;
  });

  const entries: { name: string; data: Uint8Array }[] = [
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
    { name: "OEBPS/style.css", data: encUtf8.encode(SHARED_CSS + BOOK_CSS) },
  ];
  docs.forEach((d, i) => {
    entries.push({ name: `OEBPS/${d.file}`, data: encUtf8.encode(chapters[i]) });
  });
  return zipStore(entries);
}

export async function GET(
  req: Request,
  { params }: { params: Promise<{ bookId: string }> },
) {
  const { bookId } = await params;
  const url = new URL(req.url);
  const format = url.searchParams.get("format") ?? "html";
  const autoPrint = url.searchParams.get("print") === "1";
  try {
    const manifest = await getManifest();
    const bookDef = manifest?.books.find((b) => b.id === bookId);
    const file = await getBookFile(bookId);
    if (!manifest || !bookDef || !file) {
      return NextResponse.json(
        { error: "not_found", message: `Manuel ${bookId} introuvable.` },
        { status: 404 },
      );
    }
    const savantIds = await getSavantIds();
    const level = manifest.levels.find((l) => l.id === bookDef.level);
    const subject = manifest.subjects.find((s) => s.id === bookDef.subject);
    const bookTitleFr = (file.titleFr && file.titleFr.trim()) || bookDef.titleFr;

    const seq: BundleDoc[] = [];
    if (file.intro) {
      seq.push({
        docId: file.intro.docId,
        titleAr: file.intro.titleAr,
        titleFr: file.intro.titleFr || "",
        html: file.intro.html || "",
        htmlFr: file.intro.htmlFr || "",
        isIntro: true,
        savant: savantIds.has(file.intro.docId),
        pdfOnly: false,
        file: "intro.xhtml",
        anchor: "doc-intro",
      });
    }
    let n = 0;
    for (const l of file.lessons ?? []) {
      n += 1;
      seq.push({
        docId: l.docId,
        titleAr: l.titleAr,
        titleFr: l.titleFr || "",
        html: l.html || "",
        htmlFr: l.htmlFr || "",
        isIntro: false,
        savant: savantIds.has(l.docId),
        pdfOnly: Boolean(l.pdfOnly),
        file: `lecon-${String(n).padStart(2, "0")}.xhtml`,
        anchor: `doc-${n}`,
      });
    }
    if (seq.length === 0) {
      return NextResponse.json(
        { error: "no_content", message: "Ce manuel ne contient aucun document exportable." },
        { status: 415 },
      );
    }
    const docs: FullBundleDoc[] = seq.map((d, i) => ({ ...d, index: i, count: seq.length }));
    const metaLine = [level?.shortFr, subject?.titleFr, `${docs.length} documents`, "manuel complet"]
      .filter(Boolean)
      .join(" · ");

    if (format === "epub") {
      const epub = buildBookEpub(bookId, bookTitleFr, file.titleAr, metaLine, docs);
      return new NextResponse(epub as unknown as BodyInit, {
        headers: {
          "Content-Type": "application/epub+zip",
          "Content-Disposition": `attachment; filename="minhaj-${asciiSlug(bookTitleFr, bookId)}-integral.epub"`,
          "Cache-Control": "no-store",
        },
      });
    }
    const html = buildBookHtml(bookTitleFr, file.titleAr, metaLine, docs, autoPrint);
    return new NextResponse(html, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Disposition": `inline; filename="minhaj-${asciiSlug(bookTitleFr, bookId)}-integral.html"`,
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
