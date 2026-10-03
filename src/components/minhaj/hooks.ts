"use client";

import { useEffect, useState } from "react";
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

export function useHashRoute(): Route {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash));
  useEffect(() => {
    const onChange = () => setRoute(parseHash(window.location.hash));
    window.addEventListener("hashchange", onChange);
    return () => window.removeEventListener("hashchange", onChange);
  }, []);
  return route;
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
        if (alive) setState({ data, error: null, loading: false });
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
        if (alive) setState({ data, error: null, loading: false });
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
        if (alive) setState({ data, error: null, loading: false });
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

// ————————————————————————————————— Préférences persistées

export function useLocalState<T extends string>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    try {
      return (localStorage.getItem(key) as T) || initial;
    } catch {
      return initial;
    }
  });
  useEffect(() => {
    try {
      localStorage.setItem(key, value);
    } catch {
      /* ignore */
    }
  }, [key, value]);
  return [value, setValue] as const;
}
