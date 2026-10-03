"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import { useTheme } from "next-themes";
import {
  BookOpenCheck,
  Heart,
  Info,
  Leaf,
  Moon,
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
import { navigate, useHashRoute } from "./hooks";
import { Home } from "./home";
import { BookPage } from "./book-page";
import { Reader } from "./reader";

function ThemeToggle() {
  const { resolvedTheme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);
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

function AboutDialog() {
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
      <DialogContent className="max-w-lg border-amber-800/20 bg-card sm:max-w-lg">
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
              <strong className="text-foreground">64 manuels · 1 152 leçons</strong>, du primaire
              au lycée : monothéisme (tawḥīd), droit rituel (fiqh), biographie prophétique (sīra),
              psalmodie (tajwīd), exégèse (tafsīr), grammaire (naḥw), et bien d&apos;autres
              matières.
            </p>
            <p className="text-muted-foreground">
              Conventions de traduction : vouvoiement, translittération scientifique
              (tawḥīd, waḍūʾ…), versets coraniques en <em>italique</em> avec référence
              [S. x:y], formules prophétiques développées.
            </p>
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}

function Header() {
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
          <AboutDialog />
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
  const [footerStats, setFooterStats] = useState<{ docsFr: number; docsTotal: number } | null>(
    null
  );

  useEffect(() => {
    window.scrollTo({ top: 0 });
  }, [route.view, "bookId" in route ? route.bookId : "", "docId" in route ? route.docId : ""]);

  useEffect(() => {
    let alive = true;
    fetch("/api/books")
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        if (alive && d?.stats) {
          setFooterStats({ docsFr: d.stats.docsFr as number, docsTotal: d.stats.goalDocs as number });
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
      <Header />
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
