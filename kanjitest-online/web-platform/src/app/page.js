import Link from 'next/link';

export default function HomePage() {
  const levels = [
    { id: 'n5', title: 'Beginner', count: '100+' },
    { id: 'n4', title: 'Elementary', count: '180+' },
    { id: 'n3', title: 'Intermediate', count: '300+' },
    { id: 'n2', title: 'Advanced', count: '600+' },
    { id: 'n1', title: 'Mastery', count: '1200+' },
  ];

  return (
    <div className="max-w-7xl mx-auto px-6 pb-24">
      {/* 2026 Kinetic Hero */}
      <section className="text-center py-20 mb-16">
        <h1 className="text-7xl md:text-[10rem] font-black leading-[0.8] mb-8 tracking-tighter text-slate-950 uppercase italic">
          Study<br /><span className="text-blue-600">Smarter.</span>
        </h1>
        <p className="text-xl text-slate-400 font-medium max-w-xl mx-auto uppercase tracking-[0.2em] leading-relaxed">
          High-performance study tools for the modern Japanese learner.
        </p>
      </section>

      {/* Modern Bento Grid Structure */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-8 h-auto md:h-[650px]">
        {/* Primary Focus Card (N5) */}
        <Link href="/n5" className="md:col-span-8 bento-card relative overflow-hidden group flex flex-col justify-end">
          <div className="absolute -top-10 -right-10 text-[18rem] font-black text-slate-50 group-hover:text-blue-50 transition-colors pointer-events-none select-none">N5</div>
          <div className="relative z-10">
            <span className="inline-block px-4 py-1 bg-blue-600 text-white rounded-full text-[10px] font-black uppercase tracking-widest mb-4">Popular Start</span>
            <h2 className="text-5xl font-black mb-4 tracking-tighter uppercase">JLPT N5 Mastery</h2>
            <p className="text-slate-500 max-w-md text-lg leading-relaxed font-medium">
              Establish a rock-solid foundation with the first 100 essential Kanji and basic vocabulary.
            </p>
          </div>
        </Link>

        {/* Secondary Focus Card (N4) */}
        <Link href="/n4" className="md:col-span-4 bg-slate-900 rounded-[2.5rem] p-10 flex flex-col justify-between group hover:bg-blue-600 transition-all text-white shadow-2xl shadow-slate-900/20">
          <h2 className="text-7xl font-black tracking-tighter">N4</h2>
          <div>
            <h3 className="text-2xl font-bold uppercase mb-2 tracking-tight">Elementary</h3>
            <p className="text-slate-400 group-hover:text-white/80 text-sm italic font-medium tracking-widest uppercase">Expand Your Fluency →</p>
          </div>
        </Link>

        {/* Tertiary Card (N3) */}
        <Link href="/n3" className="md:col-span-4 bento-card flex items-center justify-between group">
           <div>
              <h3 className="text-3xl font-black uppercase tracking-tighter">N3 Level</h3>
              <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mt-1">Intermediate</p>
           </div>
           <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center font-black group-hover:bg-blue-600 group-hover:text-white transition-all">→</div>
        </Link>

        {/* Placeholder for Data Scaling (N2/N1) */}
        <div className="md:col-span-8 bg-slate-100 rounded-[2.5rem] border-2 border-dashed border-slate-200 flex items-center justify-center p-8">
           <p className="text-slate-400 font-bold uppercase tracking-[0.3em] text-xs">Processing N2 & N1 Data Streams...</p>
        </div>
      </div>
    </div>
  );
}
