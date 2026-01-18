import Link from 'next/link';

export default function HomePage() {
  const levels = [
    { id: 'n5', color: 'bg-blue-600', label: 'Beginner' },
    { id: 'n4', color: 'bg-green-600', label: 'Basic' },
    { id: 'n3', color: 'bg-yellow-600', label: 'Intermediate' },
    { id: 'n2', color: 'bg-orange-600', label: 'Advanced' },
    { id: 'n1', color: 'bg-red-600', label: 'Master' },
  ];

  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      {/* SEO Header Section */}
      <header className="text-center mb-16">
        <h1 className="text-5xl font-extrabold text-gray-900 mb-4">
          Master the JLPT Kanji & Grammar
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          Free practice tests, vocabulary lists, and grammar guides for all levels of the Japanese Language Proficiency Test.
        </p>
      </header>

      {/* JLPT Level Grid */}
      <div className="grid grid-cols-1 md:grid-cols-5 gap-6 mb-20">
        {levels.map((level) => (
          <Link key={level.id} href={`/${level.id}`} className="group">
            <div className={`h-40 ${level.color} rounded-2xl shadow-lg flex flex-col items-center justify-center text-white transform transition hover:-translate-y-2 hover:shadow-2xl`}>
              <span className="text-4xl font-black uppercase">{level.id}</span>
              <span className="text-sm font-medium opacity-90">{level.label}</span>
            </div>
          </Link>
        ))}
      </div>

      {/* Content Section (Important for Google Ranking) */}
      <section className="grid md:grid-cols-3 gap-12 text-gray-700">
        <div className="space-y-4">
          <h2 className="text-2xl font-bold text-gray-800">Free Practice Tests</h2>
          <p>Prepare for your exam with our interactive quiz engine. Real JLPT-style questions generated from our database.</p>
        </div>
        <div className="space-y-4">
          <h2 className="text-2xl font-bold text-gray-800">Kanji Database</h2>
          <p>Search thousands of characters with full stroke order, Onyomi, Kunyomi, and example sentences for every N-level.</p>
        </div>
        <div className="space-y-4">
          <h2 className="text-2xl font-bold text-gray-800">SEO Optimized</h2>
          <p>Every grammar point and kanji has its own dedicated page with Romaji slugs to help you find answers fast via Google.</p>
        </div>
      </section>

      {/* AdSense Placeholder Area */}
      <div className="mt-20 p-8 border-2 border-dashed border-gray-200 rounded-lg text-center text-gray-400">
        <p>Sponsored Content</p>
        <div className="h-24 flex items-center justify-center">
          {/* AdSense component will render here */}
        </div>
      </div>
    </div>
  );
}
