import os
import json
from datetime import datetime

# CONFIGURATION
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
DATA_ROOT = "data" 

def get_pro_layout(title, desc, content, slug, kanji_char=None, lvl=None):
    """
    State-of-the-Art Light Mode Layout with full SEO injection.
    """
    # Dynamic Schema for SEO Rich Results
    schema_json = ""
    if kanji_char:
        schema_json = f"""
        <script type="application/ld+json">
        {{
            "@context": "https://schema.org",
            "@type": "EducationalOccupationalCredential",
            "name": "{kanji_char}",
            "description": "{desc}",
            "educationalLevel": "{lvl}",
            "credentialCategory": "Japanese Language Proficiency"
        }}
        </script>
        """

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {BRAND_NAME}</title>
    
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{BASE_URL}/{slug}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{BASE_URL}/{slug}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    
    {schema_json}

    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Serif+JP:wght@900&display=swap');
        :root {{ --indigo-600: #4f46e5; --slate-900: #0f172a; }}
        body {{ font-family: 'Inter', sans-serif; background: #fdfdfd; color: var(--slate-900); }}
        .kanji-font {{ font-family: 'Noto Serif JP', serif; }}
        .glass-card {{ background: #ffffff; border: 1px solid #f1f5f9; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02), 0 2px 4px -2px rgba(0,0,0,0.02); transition: all 0.3s ease; }}
        .glass-card:hover {{ transform: translateY(-5px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.05); border-color: #e2e8f0; }}
        .badge {{ padding: 4px 12px; border-radius: 99px; font-size: 10px; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; }}
    </style>
</head>
<body class="selection:bg-indigo-100 selection:text-indigo-900">
    <nav class="sticky top-0 z-50 border-b border-slate-100 bg-white/70 backdrop-blur-xl">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="/" class="text-xl font-extrabold tracking-tighter text-indigo-600 italic">学 KANJITEST</a>
            <div class="hidden md:flex gap-8 text-[11px] font-bold uppercase tracking-widest text-slate-400">
                <a href="/" class="hover:text-indigo-600">Library</a>
                <a href="/n5/" class="hover:text-indigo-600">N5 Level</a>
                <a href="#" class="opacity-30 pointer-events-none">N4 Level</a>
            </div>
        </div>
    </nav>

    <main class="min-h-screen">{content}</main>

    <footer class="border-t border-slate-100 py-20 bg-slate-50/50">
        <div class="max-w-6xl mx-auto px-6 text-center">
            <h2 class="text-xs font-black uppercase tracking-[0.4em] text-slate-300 mb-4 italic">{BRAND_NAME}</h2>
            <p class="text-slate-400 text-[10px] font-bold uppercase tracking-[0.2em]">© {datetime.now().year} Japanese_Language_Learning • Built for Excellence</p>
        </div>
    </footer>
</body>
</html>"""

def build():
    levels = ['n5'] # Starting with N5 Demo
    all_kanji = []
    all_urls = []

    for lvl in levels:
        json_path = os.path.join(DATA_ROOT, lvl, 'kanji', 'data.json')
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        os.makedirs(os.path.join(lvl, 'kanji'), exist_ok=True)

        for item in data['kanji_set']:
            all_kanji.append({**item, "lvl": lvl})
            
            # UNIQUE PAGE CONTENT
            examples_view = "".join([f"""
                <div class="glass-card p-8 rounded-3xl mb-6">
                    <p class="text-2xl md:text-3xl font-black mb-4 kanji-font text-slate-900 leading-snug">{ex['japanese']}</p>
                    <div class="flex items-center gap-4 text-xs font-bold text-indigo-600 mb-2 italic">
                        <span>{ex['romaji']}</span>
                    </div>
                    <p class="text-slate-500 text-lg">{ex['english']}</p>
                </div>""" for ex in item['examples']])

            content = f"""
            <div class="max-w-4xl mx-auto px-6 py-20">
                <header class="text-center mb-24">
                    <div class="inline-block badge bg-indigo-50 text-indigo-600 mb-6">{lvl} Mastery</div>
                    <h1 class="text-9xl kanji-font mb-4 text-slate-900">{item['kanji']}</h1>
                    <p class="text-5xl font-extrabold tracking-tighter text-slate-800 uppercase italic mb-4">{item['meaning']}</p>
                    <p class="text-slate-400 font-bold uppercase tracking-[0.5em] text-xs">{item['romaji']}</p>
                </header>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-24">
                    <div class="glass-card p-10 rounded-[2.5rem]">
                        <span class="badge bg-slate-50 text-slate-400 mb-4 block w-fit">Onyomi</span>
                        <div class="text-3xl font-black text-slate-800 italic">{"、".join(item['onyomi'])}</div>
                    </div>
                    <div class="glass-card p-10 rounded-[2.5rem]">
                        <span class="badge bg-slate-50 text-slate-400 mb-4 block w-fit">Kunyomi</span>
                        <div class="text-3xl font-black text-slate-800 italic">{"、".join(item['kunyomi'])}</div>
                    </div>
                </div>

                <section class="mb-32">
                    <h2 class="text-center text-[10px] font-black text-slate-300 uppercase tracking-[0.6em] mb-12">Grammar Context & Long Sentence Examples</h2>
                    {examples_view}
                </section>
            </div>"""

            slug = f"{lvl}/kanji/{item['slug']}.html"
            with open(slug, "w", encoding="utf-8") as f:
                f.write(get_pro_layout(f"{item['kanji']} ({item['meaning']}) Meaning", item['grammar_note'], content, slug, item['kanji'], lvl))
            all_urls.append(f"{BASE_URL}/{slug}")

    # MASTER INDEX.HTML (Modern Landing Page)
    index_grid = "".join([f"""
        <a href="/{k['lvl']}/kanji/{k['slug']}.html" class="glass-card p-10 rounded-[3rem] text-center group">
            <div class="text-7xl kanji-font mb-6 group-hover:scale-110 transition-transform duration-500">{k['kanji']}</div>
            <div class="badge bg-indigo-50 text-indigo-600 mb-2">{k['lvl']}</div>
            <div class="text-sm font-black uppercase tracking-tighter text-slate-800">{k['meaning']}</div>
        </a>""" for k in all_kanji])

    home_content = f"""
    <div class="max-w-6xl mx-auto px-6 py-32">
        <div class="text-center mb-32">
            <h1 class="text-7xl md:text-9xl font-extrabold tracking-tighter text-slate-900 leading-none mb-8 italic">THE KANJI <span class="text-indigo-600">ARCHIVE.</span></h1>
            <p class="text-xl text-slate-400 font-medium max-w-xl mx-auto italic">A professional collection of Japanese Kanji for serious learners and educators.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {index_grid}
        </div>
    </div>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(get_pro_layout("Premium Kanji Collection", "High-end Japanese learning platform.", home_content, "index.html"))

if __name__ == "__main__":
    build()
