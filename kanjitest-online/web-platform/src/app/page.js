import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="max-w-7xl mx-auto px-6 pb-20">
      <section className="text-center py-20">
        <h1 className="text-7xl md:text-9xl font-black tracking-tighter mb-8 leading-none">
          STUDY <span className="text-blue-600 italic">SMARTER.</span>
        </h1>
        <p className="text-xl text-slate-400 max-w-xl mx-auto font-medium uppercase tracking-widest">
          High-performance study tools for the modern Japanese learner.
        </p>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
        <Link href="/n5" className="md:col-span-8 bento-card relative overflow-hidden group min-h-[400px] flex flex-col justify-end">
          <div className="absolute top-0 right-0 p-12 text-[15rem] font-black text-slate-50 group-hover:text-blue-50 transition-colors uppercase select-none">N5</div>
          <span className="text-blue-600 font-bold uppercase tracking-widest text-xs mb-4">Start Here</span>
          <h2 className="text-5xl font-black text-slate-900 mb-4">JLPT N5 Mastery</h2>
          <p className="text-slate-500 max-w-sm text-lg">Build a rock-solid foundation with the first 100 essential Kanji.</p>
        </Link>

        <Link href="/n4" className="md:col-span-4 bg-slate-900 rounded-[2.5rem] p-10 flex flex-col justify-between group hover:bg-blue-600 transition-all text-white shadow-2xl shadow-slate-900/20">
          <h2 className="text-6xl font-black tracking-tighter uppercase leading-none">N4</h2>
          <div>
            <h3 className="text-2xl font-bold mb-2 uppercase">Elementary</h3>
            <p className="text-slate-400 group-hover:text-white/80">Step up to the next level of fluency.</p>
          </div>
        </Link>
      </div>
    </div>
  );
}
