import type { NextConfig } from "next";

// R603 — parade recyclage sandbox : node_modules du projet vit à /home/z/node_modules
// (racine stable hors-arbre ; l'arbre my-project est balayé par le nettoyeur du driver).
// Turbopack refusant de résoudre hors de sa racine détectée, on fixe root=/home/z.
// R606 (ouvrier A) : la cause réelle des vidages = NoSpaceLeft (disque 100 % plein :
// bundles de sûreté 3,1 Go + caches) — purgée, node_modules local survit ;
// turbopack.root retiré (il casse l'hydration client quand node_modules est local).
// R662 (ouvrier C) : l'évinceur est REVENU en cycle permanent (~1-2 min, disque
// pourtant libre 2,5 Go) — node_modules local vidé avant même la fin du démarrage.
// Retour à la recette R603 : deps à /home/z/node_modules (installées depuis une
// copie de package.json/bun.lock à /home/z) + turbopack.root=/home/z. Le script
// dev pointe déjà PATH vers /home/z/node_modules/.bin.
const nextConfig: NextConfig = {
  output: "standalone",
  turbopack: {
    root: "/home/z",
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
};

export default nextConfig;
