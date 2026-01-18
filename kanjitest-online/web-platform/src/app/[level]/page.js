import { getKanjiByLevel } from "@/lib/data";
import Link from 'next/link';

// This generates the static paths for N1, N2, N3, N4, N5 at build time
export async function generateStaticParams() {
  return [
    { level: 'n5' },
    { level: 'n4' },
    { level: 'n3' },
    { level: 'n2' },
    { level: 'n1' },
  ];
}

export default function LevelPage({ params }) {
  const { level } = params;
  const kanjiList = getKanjiByLevel(level);

  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      <header className="mb-12">
        <h1 className="text-4xl font-black text-slate-900 uppercase">
          JLPT {level} <span className="text-blue-600">Kanji List</span>
        </h1>
        <p className="text-slate-500 mt-2">Master these characters to pass your exam.</p>
      </header>

      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
        {kanjiList.map((item) => (
          <div key={item.kanji} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:border-blue-300 transition-colors">
            <div className="text-4xl mb-2 font-japanese">{item.kanji}</div>
            <div className="text-xs font-bold text-blue-600 uppercase tracking-widest">{item.meaning}</div>
            <div className="text-sm text-slate-400 mt-1">{item.onyomi}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
