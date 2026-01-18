import "./globals.css";
import Script from 'next/script';
import Link from 'next/link';

export const metadata = {
  title: {
    default: "Kanjitest.online | Free JLPT Study Tools & Mock Exams",
    template: "%s | Kanjitest.online"
  },
  description: "Master the JLPT with free interactive Kanji lists and practice tests. Optimized for N5, N4, N3, N2, and N1 levels.",
  keywords: ["JLPT", "Japanese Test", "Kanji", "N5", "N4", "N3", "N2", "N1", "Japanese Grammar"],
  metadataBase: new URL('https://kanjitest.online'),
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        {/* Lazy-loaded AdSense for SEO performance */}
        <Script 
          async 
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_ID" 
          crossOrigin="anonymous"
          strategy="afterInteractive"
        />
      </head>
      <body className="bg-[#fcfcfc] text-slate-900 min-h-screen flex flex-col font-sans antialiased">
        {/* Modern Glassmorphic Header */}
        <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-100">
          <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
            <Link href="/" className="flex items-center gap-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold italic">K</div>
              <span className="text-xl font-black tracking-tighter uppercase">Kanjitest<span className="text-blue-600">.online</span></span>
            </Link>
            
            <div className="hidden md:flex items-center gap-8 text-xs font-black uppercase tracking-widest text-slate-500">
              {['n5', 'n4', 'n3', 'n2', 'n1'].map(lvl => (
                <Link key={lvl} href={`/${lvl}`} className="hover:text-blue-600 transition-colors">{lvl}</Link>
              ))}
            </div>
          </div>
        </nav>

        <main className="flex-grow">
          {children}
        </main>

        {/* Semantic Footer for SEO Authority */}
        <footer className="bg-white border-t border-slate-100 pt-16 pb-8">
          <div className="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-4 gap-12">
            <div className="md:col-span-2">
              <div className="font-black text-lg mb-4">KANJITEST.ONLINE</div>
              <p className="text-slate-500 text-sm max-w-sm leading-relaxed">
                The most comprehensive open-source resource for JLPT preparation. 
                Built for students, by developers.
              </p>
            </div>
            <div>
              <h4 className="font-bold text-sm uppercase mb-4 tracking-widest text-blue-600">Resources</h4>
              <ul className="text-sm text-slate-400 space-y-3">
                <li><Link href="/privacy">Privacy Policy</Link></li>
                <li><Link href="/terms">Terms of Service</Link></li>
                <li><Link href="/sitemap.xml">Sitemap</Link></li>
              </ul>
            </div>
          </div>
          <div className="max-w-7xl mx-auto px-4 mt-16 pt-8 border-t border-slate-50 text-[10px] text-slate-400 text-center uppercase tracking-[0.2em]">
            © 2026 Kanjitest.online • Powered by Next.js 15
          </div>
        </footer>
      </body>
    </html>
  );
}
