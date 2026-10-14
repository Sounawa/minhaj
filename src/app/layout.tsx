import type { Metadata } from "next";
import { Amiri, Lora } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import { ThemeProvider } from "@/components/theme-provider";

const amiri = Amiri({
  variable: "--font-amiri",
  subsets: ["arabic", "latin"],
  weight: ["400", "700"],
  display: "swap",
});

const lora = Lora({
  variable: "--font-lora",
  subsets: ["latin"],
  style: ["normal", "italic"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Minhāj — Taʿlīm ʿatīq · مناهج التعليم العتيق",
  description:
    "L'enseignement traditionnel marocain (Taʿlīm ʿatīq) en arabe et en français : les 64 manuels du programme modèle du ministère des Habous et des Affaires islamiques, dans un lecteur bilingue.",
  keywords: [
    "Minhāj",
    "Taʿlīm ʿatīq",
    "التعليم العتيق",
    "منهاج نموذجي",
    "Habous",
    "Maroc",
    "éducation islamique",
    "bilingue",
    "arabe",
    "français",
  ],
  icons: {
    icon: "/logo.svg",
  },
  openGraph: {
    title: "Minhāj — Taʿlīm ʿatīq",
    description:
      "Les manuels du programme marocain d'enseignement traditionnel, en arabe et en français.",
    siteName: "Minhāj",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="fr" suppressHydrationWarning>
      <body
        className={`${amiri.variable} ${lora.variable} antialiased bg-background text-foreground`}
      >
        {/* CSS Custom Highlight API : `::highlight()` n'est pas encore reconnu par le
            pipeline CSS (lightningcss) — ces règles sont donc servies en CSS brut,
            sans transformation. Les variables --hl-* sont définies dans globals.css. */}
        <style
          dangerouslySetInnerHTML={{
            __html: `::highlight(mnhj-fr){background-color:var(--hl-fr-bg);text-decoration:underline;text-decoration-color:var(--hl-fr-line);text-decoration-thickness:2px;text-underline-offset:3px}
::highlight(mnhj-ar){background-color:var(--hl-ar-bg);text-decoration:underline;text-decoration-color:var(--hl-ar-line);text-decoration-thickness:2px;text-underline-offset:4px}`,
          }}
        />
        <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false} disableTransitionOnChange>
          {children}
          <Toaster />
        </ThemeProvider>
      </body>
    </html>
  );
}
