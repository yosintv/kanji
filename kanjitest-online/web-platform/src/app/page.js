import Link from 'next/link';

export default function HomePage() {
  const levels = [
    { id: 'n5', label: 'Beginner', count: '100+', color: 'bg-emerald-50 text-emerald-600' },
    { id: 'n4', label: 'Elementary', count: '180+', color: 'bg-blue-50 text-blue-600' },
    { id: 'n3', label: 'Intermediate', count: '300+', color: 'bg-indigo-50 text-indigo-600' },
    { id: 'n2', label: 'Advanced', count: '600+', color: 'bg-orange-50 text-orange-600' },
    { id: 'n1', label: 'Expert', count: '1200+', color: 'bg-rose-50 text-rose-600' },
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 py-20">
      {/* 2026 Typography Hero */}
      <section className="text-center mb-24">
        <h1 className="text-7xl md:text-9xl font-black tracking-tighter text-slate-900 mb-8">
          STUDY <span className="text-blue-600 italic">SMARTER.</span>
        </h1>
        <p className="text-xl text-slate-400 max-w-2xl mx-auto font-medium">
          Free interactive Kanji lists, vocabulary tools, and JLPT mock exams designed for the modern learner.
        </p>
      </section>

      {/* Bento Selection Grid */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-6 h-auto md:h-[600px]">
        {/* N5 Focus Card */}
        <Link href="/n5" className="md:col-span-8 bg-slate-900 rounded-[2rem] p-10 flex flex-col justify-end relative overflow-hidden group">
           <div className="absolute top-10 right-10 text-8xl font-black text-white/5 group-hover:scale-110 transition-transform duration-700">N5</div>
           <span className="text-blue-400 font-bold uppercase tracking-[0.3em] text-xs mb-2">Most Popular</span>
           <h2 className="text-4xl font-bold text-white mb-2">JLPT N5 Master List</h2>
           <p className="text-slate-400">The perfect starting point for your Japanese journey.</p>
        </Link>

        {/* N4 Card */}
        <Link href="/n4" className="md:col-span-4 bg-blue-600 rounded-[2rem] p-10 flex flex-col justify-center text-white hover:bg-blue-700 transition-colors">
          <h2 className="text-6xl font-black mb-2 tracking-tighter">N4</h2>
          <p className="font-bold opacity-80 uppercase text-xs tracking-widest">Elementary Level</p>
        </Link>

        {/* Smaller Bento Items */}
        {levels.slice(2).map(lvl => (
          <Link key={lvl.id} href={`/${lvl.id}`} className="md:col-span-4 bg-white border border-slate-100 rounded-[2rem] p-8 hover:shadow-2xl hover:shadow-blue-500/5 transition-all flex items-center justify-between">
            <div>
              <h3 className="text-2xl font-black uppercase tracking-tighter">{lvl.id}</h3>
              <p className="text-xs text-slate-400 font-bold uppercase tracking-widest">{lvl.label}</p>
            </div>
            <div className={`w-12 h-12 rounded-2xl ${lvl.color} flex items-center justify-center font-bold`}>→</div>
          </Link>
        ))}
      </div>
    </div>
  );
}
