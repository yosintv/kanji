import "./globals.css";
import Link from 'next/link';
import Script from 'next/script';

export const metadata = {
  title: "Kanjitest.online | Master Japanese with Free JLPT Mock Exams",
  description: "Advanced study tools for JLPT N5-N1. Interactive Kanji lists, grammar guides, and real-time practice tests.",
};

export default function RootLayout({ children }) {
  const levels = ['n5', 'n4', 'n3', 'n2', 'n1'];

  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <Script 
          async 
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_ID" 
          crossOrigin="anonymous"
          strategy="afterInteractive"
        />
      </head>
      <body className="bg-[#f8fafc] text-[#0f172a] min-h-screen flex flex-col font-sans">
        
        {/* --- NAV BAR: Glassmorphic Design --- */}
        <nav className="fixed top-0 w-full z-[100] bg-white/70 backdrop-blur-xl border-b border-slate-200/60">
          <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            {/* Logo Group */}
            <Link href="/" className="flex items-center gap-3 group">
              <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-blue-500/30 group-hover:rotate-12 transition-transform duration-300">
                <span className="text-xl font-black italic">K</span>
              </div>
              <div className="flex flex-col">
                <span className="text-xl font-black tracking-tighter leading-none">KANJITEST</span>
                <span className="text-[10px] font-bold text-blue-600 tracking-[0.3em] leading-none mt-1">ONLINE</span>
              </div>
            </Link>

            {/* Desktop Menu */}
            <div className="hidden md:flex items-center bg-slate-100/50 p-1.5 rounded-2xl border border-slate-200/50">
              {levels.map((lvl) => (
                <Link 
                  key={lvl} 
                  href={`/${lvl}`} 
                  className="px-6 py-2 rounded-xl text-xs font-black uppercase tracking-widest text-slate-500 hover:text-blue-600 hover:bg-white transition-all"
                >
                  {lvl}
                </Link>
              ))}
            </div>

            {/* CTA / Utility */}
            <div className="flex items-center gap-4">
              <button className="hidden sm:block text-sm font-bold text-slate-600 hover:text-blue-600">Log In</button>
              <button className="bg-slate-900 text-white px-5 py-2.5 rounded-xl text-sm font-bold hover:bg-blue-600 transition-colors shadow-xl shadow-slate-900/10">
                Get Started
              </button>
            </div>
          </div>
        </nav>

        {/* --- CONTENT SPACING --- */}
        <main className="flex-grow pt-20">
          {children}
        </main>

        {/* --- FOOTER: Modern Multi-column --- */}
        <footer className="bg-white border-t border-slate-200 mt-20">
          <div className="max-w-7xl mx-auto px-6 pt-20 pb-10">
            <div className="grid grid-cols-1 md:grid-cols-12 gap-12 mb-20">
              {/* Brand Col */}
              <div className="md:col-span-5">
                <div className="flex items-center gap-2 mb-6">
                  <div className="w-6 h-6 bg-slate-900 rounded flex items-center justify-center text-white text-[10px] font-black italic">K</div>
                  <span className="font-black tracking-tighter uppercase">Kanjitest.online</span>
                </div>
                <p className="text-slate-500 text-sm max-w-sm leading-loose">
                  Elevating Japanese language acquisition through high-performance digital tools. 
                  Our platform provides structured data for N5 through N1 exam preparation.
                </p>
              </div>

              {/* Links Cols */}
              <div className="md:col-span-2">
                <h4 className="font-bold text-xs uppercase tracking-widest text-blue-600 mb-6">Study</h4>
                <ul className="space-y-4 text-sm font-medium text-slate-400">
                  {levels.map(l => <li key={l}><Link href={`/${l}`} className="hover:text-slate-900">{l.toUpperCase()} Kanji</Link></li>)}
                </ul>
              </div>

              <div className="md:col-span-2">
                <h4 className="font-bold text-xs uppercase tracking-widest text-blue-600 mb-6">Company</h4>
                <ul className="space-y-4 text-sm font-medium text-slate-400">
                  <li><Link href="/about" className="hover:text-slate-900">About Us</Link></li>
                  <li><Link href="/privacy" className="hover:text-slate-900">Privacy</Link></li>
                  <li><Link href="/contact" className="hover:text-slate-900">Contact</Link></li>
                </ul>
              </div>

              {/* Newsletter / Social */}
              <div className="md:col-span-3">
                <h4 className="font-bold text-xs uppercase tracking-widest text-slate-900 mb-6">Newsletter</h4>
                <div className="relative">
                  <input type="text" placeholder="Email address" className="w-full bg-slate-100 border-none rounded-xl px-4 py-3 text-sm focus:ring-2 focus:ring-blue-500 transition-all"/>
                  <button className="absolute right-2 top-2 bg-white text-slate-900 p-1.5 rounded-lg shadow-sm font-bold text-xs">Join</button>
                </div>
              </div>
            </div>

            <div className="pt-10 border-t border-slate-100 flex flex-col md:flex-row justify-between items-center gap-6">
              <p className="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em]">
                © 2026 Kanjitest.online • All Systems Operational
              </p>
              <div className="flex gap-8">
                {/* Dummy social icons */}
                <div className="w-4 h-4 bg-slate-200 rounded-full hover:bg-blue-500 transition-colors"></div>
                <div className="w-4 h-4 bg-slate-200 rounded-full hover:bg-blue-500 transition-colors"></div>
                <div className="w-4 h-4 bg-slate-200 rounded-full hover:bg-blue-500 transition-colors"></div>
              </div>
            </div>
          </div>
        </footer>

      </body>
    </html>
  );
}
