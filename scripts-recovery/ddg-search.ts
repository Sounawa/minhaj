/**
 * Recherche web via DuckDuckGo HTML (accessible depuis le sandbox).
 * Usage: bun run scripts-recovery/ddg-search.ts "requête" [nombre]
 */
const query = process.argv[2];
const num = parseInt(process.argv[3] || "12", 10);
if (!query) {
  console.error("Usage: bun run scripts-recovery/ddg-search.ts <requête> [nombre]");
  process.exit(1);
}

const url = `https://html.duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
const res = await fetch(url, {
  headers: {
    "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "fr,ar;q=0.8,en;q=0.5",
  },
});
if (!res.ok) {
  console.error(`✗ HTTP ${res.status}`);
  process.exit(1);
}
const html = await res.text();

// Extraction des résultats (liens + titres + extraits)
const results: { title: string; href: string; snippet: string }[] = [];
const linkRe = /<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g;
const snipRe = /<a[^>]+class="result__snippet"[^>]*>([\s\S]*?)<\/a>/g;
const links = [...html.matchAll(linkRe)];
const snips = [...html.matchAll(snipRe)];
const strip = (s: string) =>
  s.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/&#x27;|&#39;/g, "'")
   .replace(/&quot;/g, '"').replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/\s+/g, " ").trim();

// DDG renvoie parfois des redirect links (uddg=)
const decodeHref = (h: string) => {
  const m = h.match(/[?&]uddg=([^&]+)/);
  if (m) return decodeURIComponent(m[1]);
  return h.startsWith("//duckduckgo.com/l/") ? "" : h;
};

for (let i = 0; i < Math.min(links.length, num); i++) {
  const href = decodeHref(links[i][1]);
  if (!href) continue;
  results.push({
    title: strip(links[i][2]),
    href,
    snippet: i < snips.length ? strip(snips[i][1]).slice(0, 220) : "",
  });
}

if (results.length === 0) {
  console.log("(aucun résultat extrait — HTML de", html.length, "octets)");
} else {
  results.forEach((r, i) => {
    console.log(`${i + 1}. ${r.title}`);
    console.log(`   ${r.href}`);
    if (r.snippet) console.log(`   ↳ ${r.snippet}`);
  });
}
