"use client";

import { useCallback, useEffect, useState } from "react";
import {
  Search,
  Globe,
  Loader2,
  BookOpenText,
  ExternalLink,
  History,
  Copy,
  X,
  FileText,
} from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

interface SearchResult {
  title: string;
  url: string;
  snippet: string;
  host: string;
  date: string;
}

interface SearchHistoryItem {
  id: string;
  query: string;
  resultCount: number;
  createdAt: string;
}

interface ReadPage {
  title: string;
  url: string;
  publishedTime: string | null;
  text: string;
  tokens: number | null;
}

export default function SearchPanel() {
  const [query, setQuery] = useState("");
  const [searching, setSearching] = useState(false);
  const [results, setResults] = useState<SearchResult[] | null>(null);
  const [history, setHistory] = useState<SearchHistoryItem[]>([]);

  // Reader state
  const [readUrl, setReadUrl] = useState("");
  const [reading, setReading] = useState(false);
  const [page, setPage] = useState<ReadPage | null>(null);

  const loadHistory = useCallback(async () => {
    try {
      const res = await fetch("/api/search");
      const data = await res.json();
      setHistory(data.history || []);
    } catch {
      /* non-fatal */
    }
  }, []);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/search");
        const data = await res.json();
        if (!cancelled) setHistory(data.history || []);
      } catch {
        /* non-fatal */
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  const runSearch = async (q?: string) => {
    const term = (q ?? query).trim();
    if (!term || searching) return;
    setQuery(term);
    setSearching(true);
    setResults(null);
    try {
      const res = await fetch("/api/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: term, num: 8 }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Search failed");
      setResults(data.results || []);
      loadHistory();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Search failed");
    } finally {
      setSearching(false);
    }
  };

  const readPage = async (url?: string) => {
    const target = (url ?? readUrl).trim();
    if (!target || reading) return;
    setReadUrl(target);
    setReading(true);
    setPage(null);
    try {
      const res = await fetch("/api/reader", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: target }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Read failed");
      setPage(data);
      toast.success("Page extracted");
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Failed to read page");
    } finally {
      setReading(false);
    }
  };

  return (
    <Tabs defaultValue="search" className="gap-4">
      <TabsList>
        <TabsTrigger value="search">
          <Search className="size-4" /> Web Search
        </TabsTrigger>
        <TabsTrigger value="reader">
          <BookOpenText className="size-4" /> Page Reader
        </TabsTrigger>
      </TabsList>

      {/* ── Search tab ── */}
      <TabsContent value="search" className="space-y-4">
        <Card>
          <CardContent className="p-4">
            <form
              className="flex gap-2"
              onSubmit={(e) => {
                e.preventDefault();
                runSearch();
              }}
            >
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground" />
                <Input
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search the live web — news, docs, anything…"
                  className="h-11 pl-9"
                  aria-label="Search query"
                />
              </div>
              <Button type="submit" size="lg" className="h-11" disabled={searching || !query.trim()}>
                {searching ? <Loader2 className="size-4.5 animate-spin" /> : <Search className="size-4.5" />}
                Search
              </Button>
            </form>

            {/* History chips */}
            {history.length > 0 && (
              <div className="mt-3 flex items-center gap-1.5 overflow-x-auto pb-1">
                <History className="size-3.5 shrink-0 text-muted-foreground" />
                {history.slice(0, 8).map((h) => (
                  <button
                    key={h.id}
                    onClick={() => runSearch(h.query)}
                    className="shrink-0 rounded-full border bg-muted/40 px-2.5 py-0.5 text-[11px] text-muted-foreground transition-colors hover:border-primary/40 hover:text-foreground"
                  >
                    {h.query.length > 30 ? h.query.slice(0, 30) + "…" : h.query}
                  </button>
                ))}
              </div>
            )}
          </CardContent>
        </Card>

        {searching && (
          <div className="space-y-3">
            {Array.from({ length: 4 }).map((_, i) => (
              <div key={i} className="animate-pulse rounded-xl border p-4">
                <div className="mb-2 h-4 w-1/3 rounded bg-muted" />
                <div className="h-3 w-full rounded bg-muted" />
                <div className="mt-1.5 h-3 w-2/3 rounded bg-muted" />
              </div>
            ))}
          </div>
        )}

        {!searching && results && results.length === 0 && (
          <Card>
            <CardContent className="flex flex-col items-center gap-2 py-12 text-center">
              <Globe className="size-8 text-muted-foreground/40" />
              <p className="text-sm text-muted-foreground">
                No results found — try different keywords.
              </p>
            </CardContent>
          </Card>
        )}

        {!searching && results && results.length > 0 && (
          <div className="space-y-2.5">
            <p className="text-xs text-muted-foreground">
              {results.length} results for <span className="font-medium text-foreground">“{query}”</span>
            </p>
            {results.map((r, i) => (
              <Card key={r.url + i} className="transition-shadow hover:shadow-md">
                <CardContent className="p-4">
                  <div className="flex items-start justify-between gap-3">
                    <div className="min-w-0 flex-1">
                      <p className="flex items-center gap-1.5 text-[11px] text-muted-foreground">
                        {r.favicon ? (
                          // eslint-disable-next-line @next/next/no-img-element
                          <img
                            src={r.favicon}
                            alt=""
                            className="size-3.5 rounded-sm"
                            loading="lazy"
                          />
                        ) : (
                          <Globe className="size-3" />
                        )}
                        <span className="truncate">{r.host}</span>
                        {r.date && <span>· {r.date}</span>}
                      </p>
                      <a
                        href={r.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="mt-1 block font-medium leading-snug text-primary underline-offset-2 hover:underline"
                      >
                        {r.title}
                      </a>
                      <p className="mt-1 line-clamp-2 text-sm leading-relaxed text-muted-foreground">
                        {r.snippet}
                      </p>
                      <div className="mt-2.5 flex gap-2">
                        <Button variant="outline" size="sm" onClick={() => readPage(r.url)}>
                          <BookOpenText className="size-3.5" /> Read page
                        </Button>
                        <Button variant="ghost" size="sm" asChild>
                          <a href={r.url} target="_blank" rel="noopener noreferrer">
                            <ExternalLink className="size-3.5" /> Open
                          </a>
                        </Button>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}

        {!searching && !results && (
          <Card className="border-dashed">
            <CardContent className="flex flex-col items-center gap-3 py-14 text-center">
              <span className="flex size-14 items-center justify-center rounded-2xl bg-accent text-accent-foreground">
                <Globe className="size-7" />
              </span>
              <p className="font-semibold">Search the live web</p>
              <p className="max-w-sm text-sm text-muted-foreground">
                Real-time results from the Web Search skill. Found something interesting?
                Jump straight into the Page Reader with one click.
              </p>
            </CardContent>
          </Card>
        )}
      </TabsContent>

      {/* ── Reader tab ── */}
      <TabsContent value="reader" className="space-y-4">
        <Card>
          <CardContent className="p-4">
            <form
              className="flex gap-2"
              onSubmit={(e) => {
                e.preventDefault();
                readPage();
              }}
            >
              <div className="relative flex-1">
                <FileText className="absolute left-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground" />
                <Input
                  value={readUrl}
                  onChange={(e) => setReadUrl(e.target.value)}
                  placeholder="https://example.com/article — extract clean text from any page"
                  className="h-11 pl-9"
                  aria-label="Page URL"
                />
              </div>
              <Button type="submit" size="lg" className="h-11" disabled={reading || !readUrl.trim()}>
                {reading ? <Loader2 className="size-4.5 animate-spin" /> : <BookOpenText className="size-4.5" />}
                Read
              </Button>
            </form>
          </CardContent>
        </Card>

        {reading && (
          <Card>
            <CardContent className="space-y-3 p-6">
              <div className="h-5 w-2/5 animate-pulse rounded bg-muted" />
              <div className="h-3 w-full animate-pulse rounded bg-muted" />
              <div className="h-3 w-full animate-pulse rounded bg-muted" />
              <div className="h-3 w-4/5 animate-pulse rounded bg-muted" />
            </CardContent>
          </Card>
        )}

        {!reading && page && (
          <Card className="animate-fade-up">
            <CardContent className="p-0">
              <div className="flex flex-wrap items-center justify-between gap-2 border-b px-5 py-3.5">
                <div className="min-w-0">
                  <h3 className="truncate font-semibold">{page.title}</h3>
                  <p className="flex items-center gap-2 text-xs text-muted-foreground">
                    <a
                      href={page.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="truncate text-primary hover:underline"
                    >
                      {page.url}
                    </a>
                    {page.publishedTime && <span>· {page.publishedTime}</span>}
                  </p>
                </div>
                <div className="flex items-center gap-2">
                  {page.tokens && (
                    <Badge variant="secondary" className="tabular-nums">
                      {page.tokens.toLocaleString()} tokens
                    </Badge>
                  )}
                  <Button variant="ghost" size="sm" onClick={() => setPage(null)}>
                    <X className="size-4" /> Clear
                  </Button>
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => {
                      navigator.clipboard.writeText(page.text);
                      toast.success("Text copied");
                    }}
                  >
                    <Copy className="size-4" /> Copy text
                  </Button>
                </div>
              </div>
              <ScrollArea className="max-h-[60vh]">
                <pre className="whitespace-pre-wrap break-words px-5 py-4 font-sans text-sm leading-relaxed">
                  {page.text}
                </pre>
              </ScrollArea>
            </CardContent>
          </Card>
        )}

        {!reading && !page && (
          <Card className="border-dashed">
            <CardContent className="flex flex-col items-center gap-3 py-14 text-center">
              <span className="flex size-14 items-center justify-center rounded-2xl bg-accent text-accent-foreground">
                <BookOpenText className="size-7" />
              </span>
              <p className="font-semibold">Read any web page as clean text</p>
              <p className="max-w-sm text-sm text-muted-foreground">
                Paste a URL (or hit “Read page” on a search result) — the Page Reader
                skill extracts the article, strips the clutter, and saves tokens.
              </p>
            </CardContent>
          </Card>
        )}
      </TabsContent>
    </Tabs>
  );
}
