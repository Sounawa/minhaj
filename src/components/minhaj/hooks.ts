"use client";

import { useCallback, useEffect, useState, useSyncExternalStore } from "react";
import type { BookDetailPayload, DocPayload, LibraryPayload } from "./types";

// ————————————————————————————————— Routage par hash (#/livre/{bookId}/{docId})

export type Route =
  | { view: "home" }
  | { view: "book"; bookId: string }
  | { view: "reader"; bookId: string; docId: string };

export function parseHash(raw: string): Route {
  const h = raw.replace(/^#\/?/, "").trim();
  if (!h) return { view: "home" };
  const parts = h.split("/").filter(Boolean).map(decodeURIComponent);
  if (parts[0] === "livre" && parts[1]) {
    if (parts[2]) return { view: "reader", bookId: parts[1], docId: parts[2] };
    return { view: "book", bookId: parts[1] };
  }
  return { view: "home" };
}

export function navigate(hash: string) {
  const target = hash.startsWith("#") ? hash : `#${hash}`;
  if (window.location.hash === target) return;
  window.location.hash = target;
}

const HOME_ROUTE: Route = { view: "home" };

function subscribeHash(onChange: () => void) {
  window.addEventListener("hashchange", onChange);
  return () => window.removeEventListener("hashchange", onChange);
}

// getSnapshot DOIT retourner une valeur stable (memoïsée par hash brut).
let hashCacheRaw: string | null = null;
let hashCacheRoute: Route = HOME_ROUTE;

function getHashSnapshot(): Route {
  const raw = window.location.hash;
  if (raw !== hashCacheRaw) {
    hashCacheRaw = raw;
    hashCacheRoute = parseHash(raw);
  }
  return hashCacheRoute;
}

/** Routage par hash, SSR-safe via useSyncExternalStore. */
export function useHashRoute(): Route {
  return useSyncExternalStore(
    subscribeHash,
    getHashSnapshot,
    () => HOME_ROUTE
  );
}

// ————————————————————————————————— Data fetching (avec mini-cache mémoire)

const memo = new Map<string, unknown>();

async function fetchJson<T>(url: string): Promise<T> {
  const cached = memo.get(url);
  if (cached) return cached as T;
  const res = await fetch(url, { headers: { Accept: "application/json" } });
  if (!res.ok) {
    const body = (await res.json().catch(() => ({}))) as { message?: string };
    throw new Error(body.message || `Erreur ${res.status} — ${url}`);
  }
  const data = (await res.json()) as T;
  memo.set(url, data);
  return data;
}

export function invalidateLibraryCache() {
  for (const key of [...memo.keys()]) memo.delete(key);
}

export function useLibrary() {
  const [state, setState] = useState<{
    data: LibraryPayload | null;
    error: string | null;
    loading: boolean;
  }>(() => {
    const cached = memo.get("/api/books") as LibraryPayload | undefined;
    return cached
      ? { data: cached, error: null, loading: false }
      : { data: null, error: null, loading: true };
  });
  useEffect(() => {
    let alive = true;
    fetchJson<LibraryPayload>("/api/books")
      .then((data) => {
        if (alive)
          setState((prev) =>
            prev.data === data && !prev.error && !prev.loading ? prev : { data, error: null, loading: false }
          );
      })
      .catch((e: Error) => {
        if (alive) setState({ data: null, error: e.message, loading: false });
      });
    return () => {
      alive = false;
    };
  }, []);
  return state;
}

export function useBookDetail(bookId: string | null) {
  const url = bookId ? `/api/books/${bookId}` : null;
  const [state, setState] = useState<{
    data: BookDetailPayload | null;
    error: string | null;
    loading: boolean;
  }>(() => {
    if (!url) return { data: null, error: null, loading: false };
    const cached = memo.get(url) as BookDetailPayload | undefined;
    return cached
      ? { data: cached, error: null, loading: false }
      : { data: null, error: null, loading: true };
  });
  useEffect(() => {
    if (!url) return;
    let alive = true;
    fetchJson<BookDetailPayload>(url)
      .then((data) => {
        if (alive)
          setState((prev) =>
            prev.data === data && !prev.error && !prev.loading ? prev : { data, error: null, loading: false }
          );
      })
      .catch((e: Error) => {
        if (alive) setState({ data: null, error: e.message, loading: false });
      });
    return () => {
      alive = false;
    };
  }, [url]);
  return state;
}

export function useDoc(bookId: string | null, docId: string | null) {
  const url = bookId && docId ? `/api/lessons/${bookId}/${docId}` : null;
  const [state, setState] = useState<{
    data: DocPayload | null;
    error: string | null;
    loading: boolean;
  }>(() => {
    if (!url) return { data: null, error: null, loading: false };
    const cached = memo.get(url) as DocPayload | undefined;
    return cached
      ? { data: cached, error: null, loading: false }
      : { data: null, error: null, loading: true };
  });
  useEffect(() => {
    if (!url) return;
    let alive = true;
    fetchJson<DocPayload>(url)
      .then((data) => {
        // Évite le re-rendu (et la réinitialisation d'innerHTML) quand le cache
        // renvoie exactement le même objet : le DOM déjà affiché reste intact.
        if (alive)
          setState((prev) =>
            prev.data === data && !prev.error && !prev.loading ? prev : { data, error: null, loading: false }
          );
      })
      .catch((e: Error) => {
        if (alive) setState({ data: null, error: e.message, loading: false });
      });
    return () => {
      alive = false;
    };
  }, [url]);
  return state;
}

// ————————————————————————————————— Préférences persistées (SSR-safe)

const lsListeners = new Set<() => void>();

function subscribeLs(onChange: () => void) {
  lsListeners.add(onChange);
  window.addEventListener("storage", onChange);
  return () => {
    lsListeners.delete(onChange);
    window.removeEventListener("storage", onChange);
  };
}

function notifyLs() {
  for (const cb of lsListeners) cb();
}

export function useLocalState<T extends string>(key: string, initial: T) {
  const value = useSyncExternalStore(
    subscribeLs,
    () => {
      try {
        return (localStorage.getItem(key) as T | null) ?? initial;
      } catch {
        return initial;
      }
    },
    () => initial
  );
  const setValue = useCallback(
    (v: T) => {
      try {
        localStorage.setItem(key, v);
        notifyLs();
      } catch {
        /* ignore */
      }
    },
    [key]
  );
  return [value, setValue] as const;
}

// ————————————————————————————————— Favoris & reprise de lecture

export interface FavoriteDoc {
  bookId: string;
  docId: string;
  titleFr: string;
  titleAr: string;
  bookTitleFr: string;
  ts: number;
}
export type LastDoc = FavoriteDoc;

const FAVS_KEY = "minhaj.favorites";
const LAST_KEY = "minhaj.lastDoc";

function readJsonList<T>(key: string): T[] {
  try {
    const raw = localStorage.getItem(key);
    if (!raw) return [];
    const v = JSON.parse(raw);
    return Array.isArray(v) ? (v as T[]) : [];
  } catch {
    return [];
  }
}

function writeJsonList(key: string, list: unknown[]) {
  try {
    localStorage.setItem(key, JSON.stringify(list));
    notifyLs();
  } catch {
    /* ignore */
  }
}

const favsCache: { raw: string | null; list: FavoriteDoc[] } = { raw: null, list: [] };
/** Snapshot serveur stable (jamais de nouveau objet à chaque appel). */
const EMPTY_FAVS: FavoriteDoc[] = [];
const NO_LAST_DOC: LastDoc | null = null;

export function getFavorites(): FavoriteDoc[] {
  if (typeof window === "undefined") return [];
  const raw = localStorage.getItem(FAVS_KEY);
  if (raw !== favsCache.raw) {
    favsCache.raw = raw;
    favsCache.list = readJsonList<FavoriteDoc>(FAVS_KEY);
  }
  return favsCache.list;
}

export function useFavorites() {
  const favorites = useSyncExternalStore(subscribeLs, getFavorites, () => EMPTY_FAVS);
  const toggle = useCallback((fav: Omit<FavoriteDoc, "ts">) => {
    const list = getFavorites();
    const i = list.findIndex((f) => f.bookId === fav.bookId && f.docId === fav.docId);
    if (i >= 0) list.splice(i, 1);
    else list.unshift({ ...fav, ts: Date.now() });
    writeJsonList(FAVS_KEY, list);
  }, []);
  const remove = useCallback((bookId: string, docId: string) => {
    const list = getFavorites().filter((f) => !(f.bookId === bookId && f.docId === docId));
    writeJsonList(FAVS_KEY, list);
  }, []);
  const has = useCallback(
    (bookId: string, docId: string) => favorites.some((f) => f.bookId === bookId && f.docId === docId),
    [favorites]
  );
  return { favorites, toggle, remove, has };
}

const lastCache: { raw: string | null; doc: LastDoc | null } = { raw: null, doc: null };

export function getLastDoc(): LastDoc | null {
  if (typeof window === "undefined") return null;
  const raw = localStorage.getItem(LAST_KEY);
  if (raw !== lastCache.raw) {
    lastCache.raw = raw;
    const list = readJsonList<LastDoc>(LAST_KEY);
    lastCache.doc = list[0] ?? null;
  }
  return lastCache.doc;
}

export function setLastDoc(doc: Omit<LastDoc, "ts">) {
  try {
    localStorage.setItem(LAST_KEY, JSON.stringify([{ ...doc, ts: Date.now() }]));
    notifyLs();
  } catch {
    /* ignore */
  }
}

export function useLastDoc() {
  return useSyncExternalStore(subscribeLs, getLastDoc, () => NO_LAST_DOC);
}

// ————————————————————————————————— Surlignages persistants (offsets texte)

export type HlPane = "fr" | "ar";
export type HlRange = [number, number];
type HlStore = Record<string, Partial<Record<HlPane, HlRange[]>>>;

const HL_KEY = "minhaj.highlights.v1";

const hlCache: { raw: string | null; store: HlStore } = { raw: null, store: {} };

function getHighlightsStore(): HlStore {
  if (typeof window === "undefined") return {};
  const raw = localStorage.getItem(HL_KEY);
  if (raw !== hlCache.raw) {
    hlCache.raw = raw;
    try {
      const v = JSON.parse(raw ?? "{}");
      hlCache.store = v && typeof v === "object" ? (v as HlStore) : {};
    } catch {
      hlCache.store = {};
    }
  }
  return hlCache.store;
}

function writeHighlightsStore(store: HlStore) {
  try {
    localStorage.setItem(HL_KEY, JSON.stringify(store));
    hlCache.raw = localStorage.getItem(HL_KEY);
    hlCache.store = store;
    notifyLs();
  } catch {
    /* ignore */
  }
}

const EMPTY_HL: Record<string, HlRange[]> = {};

export function useHighlights(bookId: string, docId: string) {
  const key = `${bookId}/${docId}`;
  const ranges = useSyncExternalStore(
    subscribeLs,
    () => getHighlightsStore()[key] ?? EMPTY_HL,
    () => EMPTY_HL
  );
  const add = useCallback(
    (pane: HlPane, start: number, end: number) => {
      const store = { ...getHighlightsStore() };
      const doc = { ...(store[key] ?? {}) };
      const list = [...(doc[pane] ?? [])];
      // fusion des chevauchements + tri
      list.push([Math.min(start, end), Math.max(start, end)]);
      list.sort((a, b) => a[0] - b[0]);
      const merged: HlRange[] = [];
      for (const r of list) {
        const last = merged[merged.length - 1];
        if (last && r[0] <= last[1] + 1) last[1] = Math.max(last[1], r[1]);
        else merged.push([r[0], r[1]]);
      }
      doc[pane] = merged;
      store[key] = doc;
      writeHighlightsStore(store);
    },
    [key]
  );
  const clearAll = useCallback(() => {
    const store = { ...getHighlightsStore() };
    if (store[key]) {
      delete store[key];
      writeHighlightsStore(store);
    }
  }, [key]);
  const count = (ranges.fr?.length ?? 0) + (ranges.ar?.length ?? 0);
  return { ranges, add, clearAll, count };
}

// ————————————————————————————————— Position de lecture (reprise au scroll)

const POS_KEY = "minhaj.readPos.v1";

export function getReadPos(bookId: string, docId: string): number | null {
  if (typeof window === "undefined") return null;
  try {
    const v = JSON.parse(localStorage.getItem(POS_KEY) ?? "{}");
    const p = v?.[`${bookId}/${docId}`];
    return typeof p === "number" && p > 2 && p < 97 ? p : null;
  } catch {
    return null;
  }
}

export function setReadPos(bookId: string, docId: string, pct: number) {
  if (typeof window === "undefined") return;
  try {
    const v = JSON.parse(localStorage.getItem(POS_KEY) ?? "{}");
    const key = `${bookId}/${docId}`;
    if (pct > 2 && pct < 97) v[key] = Math.round(pct * 10) / 10;
    else if (v[key] !== undefined) delete v[key];
    localStorage.setItem(POS_KEY, JSON.stringify(v));
  } catch {
    /* ignore */
  }
}

// ————————————————————————————————— Divers

/** Valeur retardée (recherche « pendant que je tape »). */
export function useDebouncedValue<T>(value: T, delay = 220): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
}
