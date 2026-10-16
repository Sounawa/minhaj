"use client";

import { useEffect, useState, useSyncExternalStore } from "react";
import Image from "next/image";
import { useTheme } from "next-themes";
import {
  BookMarked,
  BookOpenCheck,
  Heart,
  Info,
  Languages,
  Leaf,
  Moon,
  Search,
  Sun,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Separator } from "@/components/ui/separator";
import { navigate, useFavorites, useHashRoute } from "./hooks";
import { Home } from "./home";
import { BookPage } from "./book-page";
import { Reader } from "./reader";
import { SearchDialog } from "./search-dialog";
import { FavoritesDialog } from "./favorites-dialog";

const emptySubscribe = () => () => {};

function ThemeToggle() {
  const { resolvedTheme, setTheme } = useTheme();
  // Détection de l'hydratation sans setState dans l'effet (règle ESLint).
  const mounted = useSyncExternalStore(
    emptySubscribe,
    () => true,
    () => false
  );
  return (
    <Button
      variant="outline"
      size="icon"
      aria-label={mounted && resolvedTheme === "dark" ? "Passer en thème clair" : "Passer en thème sombre"}
      className="size-10 border-amber-800/20 bg-card/60 text-amber-900 hover:bg-amber-100/70 dark:text-amber-100 dark:hover:bg-amber-900/40"
      onClick={() => setTheme(resolvedTheme === "dark" ? "light" : "dark")}
    >
      {mounted && resolvedTheme === "dark" ? (
        <Sun className="size-4.5" />
      ) : (
        <Moon className="size-4.5" />
      )}
    </Button>
  );
}

interface AboutStats {
  booksTotal: number;
  docsFr: number;
  docsTotal: number;
  docsSavant: number;
}

function AboutDialog({ stats }: { stats: AboutStats | null }) {
  const fmt = (n: number) => n.toLocaleString("fr-FR");
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button
          variant="outline"
          size="icon"
          aria-label="À propos de Minhāj"
          className="size-10 border-amber-800/20 bg-card/60 text-amber-900 hover:bg-amber-100/70 dark:text-amber-100 dark:hover:bg-amber-900/40"
        >
          <Info className="size-4.5" />
        </Button>
      </DialogTrigger>
      <DialogContent className="max-h-[85vh] max-w-lg overflow-y-auto border-amber-800/20 bg-card sm:max-w-lg">
        <DialogHeader>
          <DialogTitle className="font-serif text-xl text-amber-950 dark:text-amber-50">
            À propos de Minhāj
          </DialogTitle>
          <DialogDescription as="div" className="space-y-3 text-left text-sm leading-relaxed">
            <p>
              <strong className="text-foreground">Minhāj</strong> propose la consultation
              bilingue (arabe ↔ français) des manuels du <em>programme modèle de
              l&apos;enseignement traditionnel</em> (المنهاج النموذجي للتعليم العتيق) publié
              par le ministère marocain des Habous et des Affaires islamiques.
            </p>
            <Separator className="bg-amber-800/15" />
            <p>
              <strong className="text-foreground">
                {stats ? `${fmt(stats.booksTotal)} manuels` : "64 manuels"} ·{" "}
                {stats ? `${fmt(stats.docsFr)} / ${fmt(stats.docsTotal)} documents` : "1 853 documents"}
              </strong>
              , du primaire au lycée : monothéisme (tawḥīd), droit rituel (fiqh), biographie
              prophétique (sīra), psalmodie (tajwīd), exégèse (tafsīr), grammaire (naḥw), et bien
              d&apos;autres matières.
            </p>
            <Separator className="bg-amber-800/15" />
            <div className="space-y-2">
              <p className="font-semibold text-foreground">Deux niveaux de traduction</p>
              <p className="flex items-start gap-2.5 rounded-xl border border-amber-500/40 bg-gradient-to-br from-amber-100/80 to-yellow-50/60 p-3 dark:border-amber-400/25 dark:from-amber-900/40 dark:to-amber-800/25">
                <BookMarked className="mt-0.5 size-4 shrink-0 text-amber-700 dark:text-amber-300" aria-hidden="true" />
                <span>
                  <strong className="text-amber-900 dark:text-amber-100">Traduction savante</strong>{" "}
                  — révisée avec soin : terminologie académique translittérée, versets coraniques
                  vérifiés, gloses des termes techniques.
                  {stats && (
                    <span className="mt-0.5 block text-xs text-muted-foreground">
                      {fmt(stats.docsSavant)} documents concernés
                    </span>
                  )}
                </span>
              </p>
              <p className="flex items-start gap-2.5 rounded-xl border border-amber-800/15 bg-card/70 p-3">
                <Languages className="mt-0.5 size-4 shrink-0 text-muted-foreground" aria-hidden="true" />
                <span>
                  <strong className="text-foreground">Traduction automatique</strong> — le texte
                  arabe officiel reste toujours affiché en regard ; la traduction savante remplace
                  progressivement la version automatique, document par document.
                </span>
              </p>
            </div>
            <Separator className="bg-amber-800/15" />
            <p className="text-muted-foreground">
              Conventions : vouvoiement, translittération scientifique (tawḥīd, waḍūʾ…), versets
              coraniques en <em>italique</em> avec référence [S. x:y], formules prophétiques
              développées.
            </p>
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}

function Header({
  onSearch,
  onFavorites,
  aboutStats,
}: {
  onSearch: () => void;
  onFavorites: () => void;
  aboutStats: AboutStats | null;
}) {
  const { favorites } = useFavorites();
  return (
    <header className="no-print sticky top-0 z-40 border-b border-amber-800/15 bg-background/85 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center gap-3 px-4 sm:px-6 lg:px-8">
        <button
          type="button"
          onClick={() => navigate("/")}
          className="group flex min-h-11 items-center gap-3 rounded-xl px-2 py-1.5 text-left transition focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-primary"
          aria-label="Minhāj — retour à l'accueil"
        >
          <Image
            src="/logo.svg"
            alt="Logo Minhāj — étoile à huit branches"
            width={40}
            height={40}
            className="size-9 rounded-lg shadow-sm ring-1 ring-amber-900/10 transition group-hover:scale-105 sm:size-10"
            priority
          />
          <span className="flex flex-col leading-tight">
            <span className="font-serif text-lg font-semibold tracking-wide text-amber-950 dark:text-amber-50 sm:text-xl">
              Minhāj
              <span className="ms-2 hidden align-middle font-arabic text-base font-normal text-primary sm:inline">
                منهاج
              </span>
            </span>
            <span className="text-[11px] font-medium uppercase tracking-[0.14em] text-muted-foreground">
              Taʿlīm ʿatīq · تعليم عتيق
            </span>
          </span>
        </button>
        <div className="ms-auto flex items-center gap-2">
          <Button
            variant="outline"
            onClick={onSearch}
            aria-label="Rechercher dans le corpus (Ctrl+K)"
            className="h-10 gap-2.5 border-amber-800/20 bg-card/60 text-amber-900 hover:bg-amber-100/70 dark:text-amber-100 dark:hover:bg-amber-900/40"
          >
            <Search className="size-4" aria-hidden="true" />
            <span className="hidden text-sm md:inline">Rechercher…</span>
            <kbd className="hidden rounded border border-amber-800/20 bg-amber-100/50 px-1.5 py-0.5 font-mono text-[10px] font-medium text-muted-foreground lg:inline-block dark:bg-amber-900/40">
              Ctrl K
            </kbd>
          </Button>
          <Button
            variant="outline"
            size="icon"
            onClick={onFavorites}
            aria-label={`Mes favoris${favorites.length ? ` (${favorites.length})` : ""}`}
            className="relative size-10 border-amber-800/20 bg-card/60 text-amber-900 hover:bg-amber-100/70 dark:text-amber-100 dark:hover:bg-amber-900/40"
          >
            <Heart className={favorites.length ? "size-4.5 fill-rose-500 text-rose-500" : "size-4.5"} aria-hidden="true" />
            {favorites.length > 0 && (
              <span className="absolute -end-1 -top-1 flex size-4.5 min-w-4.5 items-center justify-center rounded-full bg-rose-600 px-1 text-[10px] font-bold text-white">
                {favorites.length > 9 ? "9+" : favorites.length}
              </span>
            )}
          </Button>
          <AboutDialog stats={aboutStats} />
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}

function Footer({ docsFr, docsTotal }: { docsFr?: number; docsTotal?: number }) {
  return (
    <footer className="no-print mt-auto border-t border-amber-800/15 bg-secondary/60">
      <div className="mx-auto flex max-w-7xl flex-col gap-3 px-4 py-6 sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
        <div className="space-y-1">
          <p className="flex items-center gap-2 font-serif text-sm font-semibold text-amber-950 dark:text-amber-50">
            <Leaf className="size-4 text-primary" aria-hidden="true" />
            Minhāj — Taʿlīm ʿatīq
          </p>
          <p className="text-xs leading-relaxed text-muted-foreground">
            Programme officiel — ministère des Habous et des Affaires islamiques, Royaume du
            Maroc · المنهاج النموذجي للتعليم العتيق
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-muted-foreground sm:flex-col sm:items-end">
          {typeof docsFr === "number" && typeof docsTotal === "number" ? (
            <span className="flex items-center gap-1.5">
              <BookOpenCheck className="size-3.5 text-primary" aria-hidden="true" />
              {docsFr.toLocaleString("fr-FR")} / {docsTotal.toLocaleString("fr-FR")} documents
              bilingues
            </span>
          ) : null}
          <span className="flex items-center gap-1.5">
            <Heart className="size-3.5 text-primary" aria-hidden="true" />
            Traductions françaises soignées, fidèles au programme
          </span>
        </div>
      </div>
    </footer>
  );
}

export function MinhajApp() {
  const route = useHashRoute();
  const [footerStats, setFooterStats] = useState<{
    docsFr: number;
    docsTotal: number;
    booksTotal: number;
    docsSavant: number;
  } | null>(null);
  const [searchOpen, setSearchOpen] = useState(false);
  const [favOpen, setFavOpen] = useState(false);

  // Raccourci clavier global : Ctrl+K / ⌘K → recherche
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setSearchOpen(true);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    window.scrollTo({ top: 0 });
  }, [route.view, "bookId" in route ? route.bookId : "", "docId" in route ? route.docId : ""]);

  useEffect(() => {
    let alive = true;
    fetch("/api/books")
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        if (alive && d?.stats) {
          setFooterStats({
            docsFr: d.stats.docsFr as number,
            docsTotal: d.stats.docsTotal as number,
            booksTotal: d.stats.booksTotal as number,
            docsSavant: d.stats.docsSavant as number,
          });
        }
      })
      .catch(() => undefined);
    return () => {
      alive = false;
    };
  }, [route.view]);

  return (
    <div className="flex min-h-screen flex-col">
      <a
        href="#contenu"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-primary focus:px-4 focus:py-2 focus:text-sm focus:text-primary-foreground"
      >
        Aller au contenu
      </a>
      <Header
        onSearch={() => setSearchOpen(true)}
        onFavorites={() => setFavOpen(true)}
        aboutStats={footerStats}
      />
      {searchOpen && <SearchDialog open={searchOpen} onOpenChange={setSearchOpen} />}
      {favOpen && <FavoritesDialog open={favOpen} onOpenChange={setFavOpen} />}
      <main id="contenu" className="flex-1">
        {route.view === "home" && <Home />}
        {route.view === "book" && <BookPage key={route.bookId} bookId={route.bookId} />}
        {route.view === "reader" && (
          <Reader key={`${route.bookId}/${route.docId}`} bookId={route.bookId} docId={route.docId} />
        )}
      </main>
      <Footer docsFr={footerStats?.docsFr} docsTotal={footerStats?.docsTotal} />
    </div>
  );
}
