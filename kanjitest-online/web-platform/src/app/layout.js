import "./globals.css"; // Ensure this file exists in #4 src/app/
import Link from 'next/link';

export const metadata = {
  title: {
    default: "Kanjitest.online | Free JLPT Study Tools",
    template: "%s | Kanjitest.online"
  },
  description: "Free JLPT Kanji, Grammar, and Vocabulary practice tests for N5, N4, N3, N2, and N1 levels.",
  keywords: ["JLPT", "Japanese Test", "Kanji", "N5", "N4", "N3", "N2", "N1", "Japanese Grammar"],
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        {/* Replace YOUR_ID with your real Google AdSense Publisher ID */}
        {/* <script 
          async 
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_ID" 
          crossorigin="anonymous"
        ></script> */}
      </head>
      <body className="bg-slate-50 text-slate-900 min-h-screen flex flex-col">
        {/* #5 Global Header */}
        <nav className="bg-white border-b border-slate-200 sticky top-0 z-50">
          <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
            <Link href="/" className="text-2xl font-black text-blue-600 tracking-tighter">
              KANJITEST<span className="text-slate-400">.ONLINE</span>
            </Link>
            
            <div className="hidden md:flex space-x-6 font-medium text-slate-600">
              <Link href="/n5" className="hover:text-blue-600">N5</Link>
              <Link href="/n4" className="hover:text-blue-600">N4</Link>
              <Link href="/n3" className="hover:text-blue-600">N3</Link>
              <Link href="/n2" className="hover:text-blue-600">N2</Link>
              <Link href="/n1" className="hover:text-blue-600">N1</Link>
            </div>
          </div>
        </nav>

        {/* Main Content Area */}
        <main className="flex-grow">
          {children}
        </main>

        {/* #5 Global Footer */}
        <footer className="bg-white border-t border-slate-200 py-12">
          <div className="max-w-6xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 className="font-bold mb-4">About Kanjitest.online</h3>
              <p className="text-sm text-slate-500">
                The most comprehensive free resource for students preparing for the Japanese Language Proficiency Test.
              </p>
            </div>
            <div>
              <h3 className="font-bold mb-4">Quick Links</h3>
              <ul className="text-sm text-slate-500 space-y-2">
                <li><Link href="/privacy">Privacy Policy</Link></li>
                <li><Link href="/terms">Terms of Service</Link></li>
                <li><Link href="/contact">Contact Us</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold mb-4">Study Level</h3>
              <div className="flex flex-wrap gap-2">
                {['N5', 'N4', 'N3', 'N2', 'N1'].map(lvl => (
                  <span key={lvl} className="px-2 py-1 bg-slate-100 rounded text-xs font-bold">{lvl}</span>
                ))}
              </div>
            </div>
          </div>
          <div className="text-center mt-12 pt-8 border-t border-slate-100 text-xs text-slate-400">
            © 2026 Kanjitest.online. All rights reserved.
          </div>
        </footer>
      </body>
    </html>
  );
}
