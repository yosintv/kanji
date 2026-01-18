import "./globals.css";
import Link from 'next/link';
import Script from 'next/script';

export const metadata = {
  title: "Kanjitest.online | Master Japanese Kanji",
  description: "Advanced study tools for JLPT N5-N1. Free interactive Kanji lists and mock exams.",
};

export default function RootLayout({ children }) {
  const levels = ['n5', 'n4', 'n3', 'n2', 'n1'];

  return (
    <html lang="en" className="scroll-smooth">
      <head>
        {/* AdSense - Non-blocking for SEO Performance */}
        <Script 
          async 
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_ID" 
          crossOrigin="anonymous"
          strategy="afterInteractive"
        />
      </head>
      <body className="flex flex-col min-h-screen">
        {/* Navigation Bar */}
        <nav className="glass-header">
          <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <Link href="/" className="flex items-center gap-3 group">
              <div className="w-10 h-10 bg-blue-600 rounded-2xl flex items-center justify-center text-white font-black italic shadow-lg shadow-blue-600/30 group-hover:rotate-12 transition-transform">K</div>
              <div className="flex flex-col">
                <span className="text-xl font-black tracking-tighter leading-none uppercase">KANJITEST</span>
                <span className="text-[10px] font-bold text-blue-600 tracking-[0.3em] uppercase mt-1 leading-none">ONLINE</span>
              </div>
            </Link>

            {/* Pill-style Menu */}
            <div className="hidden lg:flex items-center gap-1 bg-slate-100/50 p-1.5 rounded-2xl border border-slate-200/40">
              {levels.map((lvl) => (
                <Link key={lvl} href={`/${lvl}`} className="px-6 py-2 rounded-xl text-[11px] font-black uppercase tracking-widest text-slate-500 hover:text-blue-600 hover:bg-white transition-all">
                  {lvl}
                </Link>
              ))}
            </div>

            <button className="bg-slate-900 text-white px-6 py-2.5 rounded-xl text-sm font-bold hover:bg-blue-600 transition-all shadow-xl shadow-slate-900/10">
              Get Started
            </button>
          </div>
        </nav>

        {/* Content Area */}
        <main className="flex-grow pt-32">
          {children}
        </main>

        {/* Semantic Footer */}
        <footer className="bg-white border-t border-slate-200 pt-24 pb-12">
          <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-12 gap-16 mb-20 text-center md:text-left">
            <div className="md:col-span-6">
              <div className="font-black text-2xl mb-4 tracking-tighter italic uppercase">Kanjitest.online</div>
              <p className="text-slate-500 text-lg leading-relaxed max-w-sm mx-auto md:mx-0">
                The modern standard for Japanese language proficiency tools. Built for the web, optimized for results.
              </p>
            </div>
            <div className="md:col-span-3">
              <h4 className="font-bold text-xs uppercase tracking-widest text-blue-600 mb-6">Resources</h4>
              <ul className="space-y-4 text-sm font-bold text-slate-400">
                {levels.map(l => <li key={l}><Link href={`/${l}`} className="hover:text-slate-950 uppercase">{l} Prep</Link></li>)}
              </ul>
            </div>
            <div className="md:col-span-3">
              <h4 className="font-bold text-xs uppercase tracking-widest text-blue-600 mb-6">Platform</h4>
              <ul className="space-y-4 text-sm font-bold text-slate-400">
                <li><Link href="/privacy" className="hover:text-slate-950">Privacy</Link></li>
                <li><Link href="/terms" className="hover:text-slate-950">Terms</Link></li>
              </ul>
            </div>
          </div>
          <div className="text-center pt-10 border-t border-slate-50">
            <p className="text-[10px] font-black text-slate-400 uppercase tracking-[0.4em]">© 2026 Kanjitest.online • All Systems Operational</p>
          </div>
        </footer>
      </body>
    </html>
  );
}
