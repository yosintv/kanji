import "./globals.css";
import Link from 'next/link';

export const metadata = {
  title: "Kanjitest.online | JLPT Mastery",
  description: "Interactive Kanji study tools for N5-N1 levels.",
};

export default function RootLayout({ children }) {
  const levels = ['n5', 'n4', 'n3', 'n2', 'n1'];

  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen">
        <nav className="glass-nav">
          <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <Link href="/" className="flex items-center gap-3">
              <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center text-white font-black italic shadow-lg shadow-blue-600/20">K</div>
              <span className="text-xl font-black tracking-tighter uppercase">Kanjitest<span className="text-blue-600">.online</span></span>
            </Link>

            <div className="hidden md:flex items-center gap-2 bg-slate-100/50 p-1.5 rounded-2xl border border-slate-200/50">
              {levels.map((lvl) => (
                <Link key={lvl} href={`/${lvl}`} className="px-5 py-2 rounded-xl text-xs font-black uppercase tracking-widest text-slate-500 hover:text-blue-600 hover:bg-white transition-all">
                  {lvl}
                </Link>
              ))}
            </div>

            <button className="bg-slate-900 text-white px-6 py-2.5 rounded-xl text-sm font-bold hover:bg-blue-600 transition-all shadow-xl shadow-slate-900/10">
              Get Started
            </button>
          </div>
        </nav>

        <main className="flex-grow pt-32">{children}</main>

        <footer className="bg-white border-t border-slate-200 py-20 mt-20">
          <div className="max-w-7xl mx-auto px-6 text-center">
             <p className="text-[10px] font-bold text-slate-400 uppercase tracking-[0.3em]">© 2026 Kanjitest.online • Elevating Japanese Studies</p>
          </div>
        </footer>
      </body>
    </html>
  );
}
