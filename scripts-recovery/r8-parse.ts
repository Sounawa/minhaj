/**
 * Minhāj R8 — Parse des pages moissonnées : titre, contenu intro, leçons PDF (ancres).
 */
import { readFileSync, writeFileSync, readdirSync } from "fs";

const DIR = "/tmp/r8-pages";
const files = readdirSync(DIR).filter(f => f.endsWith(".html"));

function cleanArticleHtml(raw: string): { titleAr: string; html: string } | null {
  const m = raw.match(/<div class="item-page"[^>]*>([\s\S]*?)<\/div>\s*<div class="(?:module|clearfix|pagination|tags)/);
  let inner = m ? m[1] : null;
  if (!inner) {
    const m2 = raw.match(/<div class="item-page"[^>]*>([\s\S]{50,60000}?)<\/article>/);
    inner = m2 ? m2[1] : null;
  }
  if (!inner) return null;
  const tm = inner.match(/<h2[^>]*>([\s\S]*?)<\/h2>/);
  let titleAr = tm ? tm[1].replace(/<[^>]+>/g, "").trim() : "";
  let html = inner.replace(/<h2[^>]*>[\s\S]*?<\/h2>/, "");
  html = html
    .replace(/<script[\s\S]*?<\/script>/gi, "").replace(/<style[\s\S]*?<\/style>/gi, "")
    .replace(/<form[\s\S]*?<\/form>/gi, "").replace(/<iframe[\s\S]*?<\/iframe>/gi, "")
    .replace(/<img[^>]*>/gi, "").replace(/<button[\s\S]*?<\/button>/gi, "").replace(/<input[^>]*>/gi, "")
    .replace(/<!--[\s\S]*?-->/g, "");
  html = html.replace(/\s(?:class|id|style|onclick|onload|data-[a-z-]+)="[^"]*"/gi, "");
  html = html.replace(/<a\s[^>]*href="[^"]*"[^>]*>([\s\S]*?)<\/a>/gi, "$1");
  html = html.replace(/\n{3,}/g, "\n\n").replace(/[ \t]{2,}/g, " ").trim();
  if (html.length < 60) return null;
  return { titleAr, html };
}

function extractPdfLessons(raw: string) {
  const anchors = [...raw.matchAll(/<a\s[^>]*href="([^"]+\.pdf[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi)];
  const seen = new Set<string>();
  const out: { url: string; title: string }[] = [];
  for (const a of anchors) {
    const url = a[1].replace(/&amp;/g, "&");
    const title = a[2].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
    const key = decodeURIComponent(url).split("?")[0];
    if (seen.has(key)) continue;
    seen.add(key);
    if (!title || title.length < 4) continue;
    out.push({ url, title });
  }
  return out;
}

const results: any = {};
for (const f of files) {
  const docId = f.replace(".html", "");
  const raw = readFileSync(`${DIR}/${f}`, "utf-8");
  const art = cleanArticleHtml(raw);
  // breadcrumb: crumbs ou fil d'Ariane
  const crumb = raw.match(/<div class="breadcrumb[^"]*"[^>]*>([\s\S]*?)<\/div>/);
  const crumbText = crumb ? crumb[1].replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim() : "";
  const pdfs = extractPdfLessons(raw);
  results[docId] = {
    titleAr: art?.titleAr ?? null,
    htmlLen: art?.html.length ?? 0,
    html: art?.html ?? null,
    crumb: crumbText.slice(0, 200),
    pdfCount: pdfs.length,
    pdfs: pdfs.slice(0, 60),
  };
  console.log(`${docId} | ${art?.titleAr?.slice(0, 55) ?? "PAS DE CONTENU"} | pdf: ${pdfs.length} | crumb: ${crumbText.slice(0, 80)}`);
}
writeFileSync("/tmp/r8-parsed.json", JSON.stringify(results, null, 1), "utf-8");
console.log("\nsauvé → /tmp/r8-parsed.json");
