/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',      // This creates the /out folder for GitHub
  distDir: 'out',        // Explicitly naming the output folder
  images: {
    unoptimized: true,   // Required for static site hosting
  },
};

module.exports = nextConfig;
