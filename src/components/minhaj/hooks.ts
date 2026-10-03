"use client";

import { useEffect, useRef, useState } from "react";
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
  const [data, setData] = useState<LibraryPayload | null>(() => (memo.get("/api/books") as LibraryPayload) ?? null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(!data);
  const ref = useRef(false);
  useEffect(() => {
    if (ref.current) return;
    ref.current = true;
    fetchJson<LibraryPayload>("/api/books")
      .then(setData)
      .catch((e: Error) => setError(e.message))
      .finally(() => setLoading(false));
  }, []);
  return { data, error, loading };
}

export function useBookDetail(bookId: string | null) {
  const url = bookId ? `/api/books/${bookId}` : null;
  const [data, setData] = useState<BookDetailPayload | null>(
    () => (url ? ((memo.get(url) as BookDetailPayload) ?? null) : null)
  );
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(Boolean(url) && !data);
  useEffect(() => {
    if (!url) return;
    let alive = true;
    setLoading(!memo.has(url));
    setError(null);
    fetchJson<BookDetailPayload>(url)
      .then((d) => alive && setData(d))
      .catch((e: Error) => alive && setError(e.message))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [url]);
  return { data, error, loading };
}

export function useDoc(bookId: string | null, docId: string | null) {
  const url = bookId && docId ? `/api/lessons/${bookId}/${docId}` : null;
  const [data, setData] = useState<DocPayload | null>(
    () => (url ? ((memo.get(url) as DocPayload) ?? null) : null)
  );
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(Boolean(url) && !data);
  useEffect(() => {
    if (!url) return;
    let alive = true;
    setLoading(!memo.has(url));
    setError(null);
    fetchJson<DocPayload>(url)
      .then((d) => alive && setData(d))
      .catch((e: Error) => alive && setError(e.message))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [url]);
  return { data, error, loading };
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
