import os
import json
from datetime import datetime

# CONFIGURATION
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
DATA_ROOT = "data" 
FOLDER_NAME = "Japanese_Language_Learning"

def get_pro_layout(title, desc, content, slug, kanji_char=None, lvl=None, is_hub=False):
    """
    High-End Academic Aesthetic with Glassmorphism and SEO Injection.
    """
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
    <link rel="canonical" href="{BASE_URL}/{slug}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{BASE_URL}/{slug}">
    <meta property="og:type" content="website">
    {schema_json}
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Serif+JP:wght@900&display=swap');
        body {{ font-family: 'Inter', sans-serif; background: #fdfdfd; color: #0f172a; }}
        .kanji-font {{ font-family: 'Noto Serif JP', serif; }}
        .glass-card {{ background: #ffffff; border: 1px solid #f1f5f9; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }}
        .glass-card:hover {{ transform: translateY(-8px); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.08); border-color: #4f46e5; }}
        .badge {{ padding: 4px 12px; border-radius: 99px; font-size: 10px; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; }}
        .shimmer {{ background: linear-gradient(90deg, #f1f5f9 25%, #f8fafc 50%, #f1f5f9 75%); background-size: 200% 100%; animation: shimmer 1.5s infinite; }}
        @keyframes shimmer {{ 0% {{ background-position: 200% 0; }} 100% {{ background-position: -200% 0; }} }}
    </style>
</head>
<body class="selection:bg-indigo-100 selection:text-indigo-900">
    <nav class="sticky top-0 z-50 border-b border-slate-100 bg-white/70 backdrop-blur-xl">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="/" class="text-xl font-extrabold tracking-tighter text-indigo-600 italic">学 KANJITEST</a>
            <div class="hidden md:flex gap-8 text-[11px] font-bold uppercase tracking-widest text-slate-400">
                <a href="/" class="hover:text-indigo-600">Library</a>
                <a href="/n5/" class="hover:text-indigo-600">N5 Level</a>
                <span class="opacity-20">N4 Coming Soon</span>
            </div>
        </div>
    </nav>
    <main class="min-h-screen">{content}</main>
    <footer class="border-t border-slate-100 py-20 bg-slate-50/50">
        <div class="max-w-6xl mx-auto px-6 text-center">
            <p class="text-slate-400 text-[10px] font-bold uppercase tracking-[0.2em]">© {datetime.now().year} {FOLDER_NAME}</p>
        </div>
    </footer>
</body>
</html>"""

def build():
    levels = ['n5'] # Expandable to ['n5', 'n4', etc.]
    all_kanji_data = []
    all_urls = []

    for lvl in levels:
        json_path = os.path.join(DATA_ROOT, lvl, 'kanji', 'data.json')
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        os.makedirs(os.path.join(lvl, 'kanji'), exist_ok=True)

        # 1. GENERATE DYNAMIC HUB (n5/index.html)
        hub_content = f"""
        <div class="max-w-6xl mx-auto px-6 py-24">
            <header class="mb-20">
                <div class="badge bg-indigo-50 text-indigo-600 mb-4">{lvl} Collection</div>
                <h1 class="text-7xl font-black tracking-tighter italic text-slate-900 leading-none">THE N5 <span class="text-indigo-600 underline">VAULT.</span></h1>
            </header>
            <div id="dynamic-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
                <div class="shimmer h-64 rounded-[3rem]"></div>
                <div class="shimmer h-64 rounded-[3rem]"></div>
                <div class="shimmer h-64 rounded-[3rem]"></div>
                <div class="shimmer h-64 rounded-[3rem]"></div>
            </div>
        </div>
        <script>
            async function loadHub() {{
                const res = await fetch('/data/{lvl}/kanji/data.json');
                const d = await res.json();
                const g = document.getElementById('dynamic-grid');
                g.innerHTML = d.kanji_set.map(k => `
                    <div class="glass-card p-10 rounded-[3rem] text-center flex flex-col items-center border border-slate-100">
                        <div class="text-7xl kanji-font mb-6 text-slate-900">${{k.kanji}}</div>
                        <h3 class="font-black uppercase tracking-tighter text-slate-800 text-lg">${{k.meaning}}</h3>
                        <p class="text-[10px] text-slate-400 font-bold tracking-widest uppercase mb-8">${{k.romaji}}</p>
                        <a href="/{lvl}/kanji/${{k.slug}}.html" class="w-full py-4 bg-slate-900 text-white text-[10px] font-black uppercase tracking-[0.2em] rounded-2xl hover:bg-indigo-600 transition-all">View Analytics</a>
                    </div>
                `).join('');
            }}
            window.onload = loadHub;
        </script>"""
        
        with open(f"{lvl}/index.html", "w", encoding="utf-8") as f:
            f.write(get_pro_layout(f"JLPT {lvl} Library", f"Dynamic {lvl} Kanji collection", hub_content, f"{lvl}/index.html", is_hub=True))

        # 2. GENERATE STATIC KANJI PAGES
        for item in data['kanji_set']:
            all_kanji_data.append({**item, "lvl": lvl})
            
            ex_view = "".join([f"""
                <div class="glass-card p-10 rounded-[2.5rem] mb-6">
                    <p class="text-3xl font-black mb-6 kanji-font text-slate-900 leading-relaxed">{ex['japanese']}</p>
                    <div class="flex items-center gap-4 mb-3">
                        <span class="badge bg-indigo-50 text-indigo-600 italic lowercase">{ex['romaji']}</span>
                    </div>
                    <p class="text-slate-500 text-lg leading-relaxed">{ex['english']}</p>
                </div>""" for ex in item['examples']])

            detail_content = f"""
            <div class="max-w-4xl mx-auto px-6 py-20">
                <div class="text-center mb-24">
                    <div class="text-[150px] kanji-font leading-none text-slate-900 mb-6">{item['kanji']}</div>
                    <h1 class="text-6xl font-black uppercase italic tracking-tighter mb-4">{item['meaning']}</h1>
                    <p class="badge bg-slate-100 text-slate-500">{item['romaji']}</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-24">
                    <div class="glass-card p-10 rounded-[2.5rem]">
                        <span class="badge bg-indigo-50 text-indigo-600 mb-4 block w-fit">Onyomi</span>
                        <div class="text-3xl font-black">{"、".join(item['onyomi'])}</div>
                    </div>
                    <div class="glass-card p-10 rounded-[2.5rem]">
                        <span class="badge bg-emerald-50 text-emerald-600 mb-4 block w-fit">Kunyomi</span>
                        <div class="text-3xl font-black">{"、".join(item['kunyomi'])}</div>
                    </div>
                </div>
                <section>
                    <h2 class="text-center text-[10px] font-black text-slate-300 uppercase tracking-[0.5em] mb-12">Grammar Context & Usage Examples</h2>
                    {ex_view}
                </section>
            </div>"""

            slug = f"{lvl}/kanji/{item['slug']}.html"
            with open(slug, "w", encoding="utf-8") as f:
                f.write(get_pro_layout(f"{item['kanji']} Meaning", item['grammar_note'], detail_content, slug, item['kanji'], lvl))
            all_urls.append(f"{BASE_URL}/{slug}")

    # 3. GENERATE GLOBAL LANDING PAGE (index.html)
    home_grid = "".join([f"""
        <a href="/{k['lvl']}/kanji/{k['slug']}.html" class="glass-card p-12 rounded-[4rem] group">
            <div class="text-8xl kanji-font mb-8 group-hover:scale-110 transition-transform duration-700">{k['kanji']}</div>
            <div class="badge bg-slate-900 text-white mb-2">{k['lvl']}</div>
            <div class="text-sm font-black uppercase tracking-widest text-slate-800">{k['meaning']}</div>
        </a>""" for k in all_kanji_data[:4]]) # Limit to first 4 for home preview

    home_content = f"""
    <div class="max-w-6xl mx-auto px-6 py-40">
        <div class="text-center mb-32">
            <h1 class="text-[100px] md:text-[140px] font-black tracking-tighter text-slate-900 leading-[0.8] mb-12 italic">
                PURE <br><span class="text-indigo-600">KANJI.</span>
            </h1>
            <p class="text-2xl text-slate-400 font-medium max-w-xl mx-auto leading-relaxed">The high-authority digital collection for JLPT masters.</p>
            <div class="mt-12">
                <a href="/n5/" class="px-10 py-5 bg-indigo-600 text-white font-black uppercase tracking-widest rounded-full hover:shadow-2xl hover:shadow-indigo-200 transition-all">Enter Library</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">{home_grid}</div>
    </div>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(get_pro_layout("The Kanji Archive", "Professional Japanese Mastery Platform", home_content, "index.html"))

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join([f'<url><loc>{u}</loc></url>' for u in all_urls]) + '</urlset>')

if __name__ == "__main__":
    build()
