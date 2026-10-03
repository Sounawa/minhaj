"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { BookOpen, CornerDownLeft, FileText, Loader2, Search, SearchX } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { cn } from "@/lib/utils";
import { navigate, useDebouncedValue } from "./hooks";

export interface SearchHitClient {
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
}
interface SearchResponse {
  query: string;
  total: number;
  truncated: boolean;
  hits: SearchHitClient[];
}

/** Surligne les occurrences de la requête (insensible casse/accents simples). */
function Highlight({ text, query }: { text: string; query: string }) {
  const q = query.trim();
  if (!q || q.length < 2) return <>{text}</>;
  // Échapper les caractères spéciaux regex
  const esc = q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  // Autoriser une lettre accentuée à matcher sa version pliée
  const pattern = esc
    .replace(/[eE]/g, "[eèéêëEÈÉÊË]")
    .replace(/[aA]/g, "[aàâäAÀÂÄ]")
    .replace(/[iI]/g, "[iîïIÎÏ]")
    .replace(/[oO]/g, "[oôöOÔÖ]")
    .replace(/[uU]/g, "[uûüùUÛÜÙ]")
    .replace(/[cC]/g, "[cçCÇ]");
  let parts: Array<string | { m: string }> = [];
  try {
    const re = new RegExp(pattern, "gi");
    let last = 0;
    for (const match of text.matchAll(re)) {
      const idx = match.index ?? 0;
      if (idx > last) parts.push(text.slice(last, idx));
      parts.push({ m: match[0] });
      last = idx + match[0].length;
    }
    if (last < text.length) parts.push(text.slice(last));
  } catch {
    parts = [text];
  }
  return (
    <>
      {parts.map((p, i) =>
        typeof p === "string" ? (
          <span key={i}>{p}</span>
        ) : (
          <mark key={i} className="rounded-sm bg-amber-200/80 px-0.5 text-inherit dark:bg-amber-400/30">
            {p.m}
          </mark>
        )
      )}
    </>
  );
}

export function SearchDialog({ open, onOpenChange }: { open: boolean; onOpenChange: (o: boolean) => void }) {
  const [query, setQuery] = useState("");
  const [state, setState] = useState<
    { status: "idle" } | { status: "loading" } | { status: "error"; message: string } | { status: "done"; data: SearchResponse }
  >({ status: "idle" });
  const [active, setActive] = useState(0);
  const debounced = useDebouncedValue(query, 250);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLDivElement>(null);
  const qTrim = query.trim();
  const showIdle = qTrim.length < 2;

  // Focus initial à l'ouverture (effet DOM pur, sans setState)
  useEffect(() => {
    if (open) {
      const t = setTimeout(() => inputRef.current?.focus(), 60);
      return () => clearTimeout(t);
    }
  }, [open]);

  // Requête débouncée (setState uniquement dans les callbacks asynchrones)
  useEffect(() => {
    const q = debounced.trim();
    if (!open || q.length < 2) return;
    let alive = true;
    const ctrl = new AbortController();
    const t = setTimeout(() => {
      fetch(`/api/search?q=${encodeURIComponent(q)}&limit=25`, { signal: ctrl.signal })
        .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`Erreur ${r.status}`))))
        .then((data: SearchResponse) => {
          if (alive) {
            setState({ status: "done", data });
            setActive(0);
          }
        })
        .catch((e: Error) => {
          if (alive && e.name !== "AbortError") setState({ status: "error", message: e.message });
        });
    }, 0);
    return () => {
      alive = false;
      ctrl.abort();
      clearTimeout(t);
    };
  }, [debounced, open]);

  const hits = state.status === "done" ? state.data.hits : [];

  const openHit = useCallback(
    (hit: SearchHitClient) => {
      onOpenChange(false);
      navigate(`/livre/${hit.bookId}/${hit.docId}`);
    },
    [onOpenChange]
  );

  // Navigation clavier ↑ ↓ Entrée
  const onKeyDown = (e: React.KeyboardEvent) => {
    if (!hits.length || showIdle) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActive((a) => (a + 1) % hits.length);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive((a) => (a - 1 + hits.length) % hits.length);
    } else if (e.key === "Enter" && hits[active]) {
      e.preventDefault();
      openHit(hits[active]);
    }
  };

  // Suivre l'élément actif
  useEffect(() => {
    listRef.current?.querySelector<HTMLElement>("[data-active='true']")?.scrollIntoView({ block: "nearest" });
  }, [active, hits.length]);

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent
        className="top-[12%] max-h-[76vh] translate-y-0 gap-0 overflow-hidden border-amber-800/20 bg-card p-0 sm:max-w-2xl"
        onKeyDown={onKeyDown}
      >
        <DialogHeader className="border-b border-amber-800/15 px-5 pb-4 pt-5">
          <DialogTitle className="flex items-center gap-2 font-serif text-lg text-amber-950 dark:text-amber-50">
            <Search className="size-4.5 text-primary" aria-hidden="true" />
            Rechercher dans le corpus
          </DialogTitle>
          <DialogDescription className="text-left">
            934 documents bilingues — titres et contenus, arabe et français.
          </DialogDescription>
        </DialogHeader>

        <div className="px-5 pt-4">
          <div className="relative">
            <Search className="pointer-events-none absolute start-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground" aria-hidden="true" />
            <input
              ref={inputRef}
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ex. : ablution, تلاوة, istikhara, jeûne…"
              aria-label="Terme de recherche"
              className="h-12 w-full rounded-xl border border-amber-800/20 bg-background/70 ps-10 pe-4 text-base text-foreground shadow-inner outline-none transition placeholder:text-muted-foreground/70 focus-visible:ring-2 focus-visible:ring-primary/50"
            />
          </div>
        </div>

        <div ref={listRef} className="min-h-[120px] flex-1 overflow-y-auto px-3 py-3" role="listbox" aria-label="Résultats de recherche">
          {showIdle && state.status !== "loading" && state.status !== "done" && (
            <div className="flex h-full flex-col items-center justify-center gap-2 py-8 text-center">
              <BookOpen className="size-7 text-primary/50" aria-hidden="true" />
              <p className="text-sm text-muted-foreground">
                Saisissez au moins 2 caractères — français ou arabe.
              </p>
              <p className="text-xs text-muted-foreground/70">
                Astuce : la recherche ignore accents et diacritiques (تَجويد = تجويد).
              </p>
            </div>
          )}
          {state.status === "loading" && !showIdle && (
            <div className="flex items-center justify-center gap-2 py-10 text-muted-foreground">
              <Loader2 className="size-5 animate-spin text-primary" aria-hidden="true" />
              <p className="text-sm">Recherche en cours…</p>
            </div>
          )}
          {state.status === "error" && (
            <div className="flex flex-col items-center justify-center gap-2 py-8 text-center">
              <SearchX className="size-7 text-destructive/70" aria-hidden="true" />
              <p className="text-sm text-muted-foreground">{state.message}</p>
            </div>
          )}
          {state.status === "done" && hits.length === 0 && (
            <div className="flex flex-col items-center justify-center gap-2 py-8 text-center">
              <SearchX className="size-7 text-muted-foreground/60" aria-hidden="true" />
              <p className="font-serif text-base text-amber-950 dark:text-amber-50">Aucun résultat</p>
              <p className="max-w-sm text-sm text-muted-foreground">
                Aucun document ne contient «&nbsp;{state.data.query}&nbsp;». Essayez un autre terme
                ou une autre graphie.
              </p>
            </div>
          )}
          {hits.map((hit, i) => (
            <button
              key={`${hit.bookId}/${hit.docId}`}
              type="button"
              role="option"
              aria-selected={i === active}
              data-active={i === active}
              onMouseEnter={() => setActive(i)}
              onClick={() => openHit(hit)}
              className={cn(
                "mb-1 flex w-full items-start gap-3 rounded-xl border px-3 py-2.5 text-left transition",
                i === active
                  ? "border-amber-700/30 bg-amber-100/70 shadow-sm dark:border-amber-200/20 dark:bg-amber-900/40"
                  : "border-transparent hover:bg-amber-100/40 dark:hover:bg-amber-900/25"
              )}
            >
              <FileText className="mt-1 size-4 shrink-0 text-primary" aria-hidden="true" />
              <span className="min-w-0 flex-1">
                <span className="flex flex-wrap items-center gap-1.5">
                  <span className="font-serif text-[15px] font-semibold leading-snug text-amber-950 dark:text-amber-50">
                    <Highlight text={hit.titleFr} query={query} />
                  </span>
                  {hit.isIntro && (
                    <Badge className="rounded-full bg-amber-800/15 px-1.5 text-[10px] text-amber-900 dark:bg-amber-200/15 dark:text-amber-100">
                      intro
                    </Badge>
                  )}
                  {hit.lang === "ar" && (
                    <Badge variant="outline" className="rounded-full border-amber-800/20 px-1.5 text-[10px] text-muted-foreground">
                      AR
                    </Badge>
                  )}
                </span>
                <span className="mt-0.5 flex items-center gap-1.5 text-xs text-muted-foreground">
                  <span className="truncate">{hit.bookTitleFr || hit.bookTitleAr}</span>
                  {hit.levelShortFr && (
                    <>
                      <span aria-hidden="true">·</span>
                      <span className="shrink-0">{hit.levelShortFr}</span>
                    </>
                  )}
                </span>
                <span dir="auto" className="mt-1 line-clamp-2 block text-[13px] leading-snug text-foreground/70">
                  <Highlight text={hit.snippet} query={query} />
                </span>
              </span>
              {i === active && <CornerDownLeft className="mt-1 size-3.5 shrink-0 text-muted-foreground/60" aria-hidden="true" />}
            </button>
          ))}
        </div>

        {state.status === "done" && state.data.total > 0 && !showIdle && (
          <div className="flex flex-wrap items-center justify-between gap-2 border-t border-amber-800/15 px-5 py-2.5 text-xs text-muted-foreground">
            <span>
              {state.data.total.toLocaleString("fr-FR")} document{state.data.total > 1 ? "s" : ""} trouvé
              {state.data.total > 1 ? "s" : ""}
              {state.data.truncated ? " — 25 premiers affichés" : ""}
            </span>
            <span className="flex items-center gap-3">
              <span className="hidden items-center gap-1 sm:flex">
                <kbd className="rounded border border-amber-800/20 bg-amber-100/50 px-1.5 py-0.5 font-mono text-[10px] dark:bg-amber-900/40">↑↓</kbd>
                naviguer
              </span>
              <span className="flex items-center gap-1">
                <kbd className="rounded border border-amber-800/20 bg-amber-100/50 px-1.5 py-0.5 font-mono text-[10px] dark:bg-amber-900/40">↵</kbd>
                ouvrir
              </span>
            </span>
          </div>
        )}
      </DialogContent>
    </Dialog>
  );
}
