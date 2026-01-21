import os
import json
from datetime import datetime

# CONFIGURATION
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
DATA_ROOT = "data" 

def get_zen_layout(title, desc, content, slug=""):
    """Modern Light Mode Layout with Zen Aesthetics"""
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {BRAND_NAME}</title>
    <meta name="description" content="{desc}">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&family=Noto+Sans+JP:wght@400;700;900&display=swap');
        body {{ 
            font-family: 'Plus Jakarta Sans', 'Noto Sans JP', sans-serif; 
            background-color: #FFFFFF; 
            color: #1E293B; 
        }}
        .zen-card {{ 
            background: #F8FAFC; 
            border: 1px solid #E2E8F0; 
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
        }}
        .zen-card:hover {{ 
            border-color: #4F46E6; 
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.05);
        }}
        .kanji-display {{
            font-size: clamp(100px, 20vw, 180px);
            font-weight: 900;
            color: #0F172A;
        }}
    </style>
</head>
<body class="antialiased">
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-100">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <a href="/" class="text-xl font-extrabold tracking-tight text-indigo-600">
                KANJI<span class="text-slate-900">TEST</span>
            </a>
            <div class="flex gap-8 text-xs font-bold uppercase tracking-widest text-slate-500">
                <a href="/n5/" class="hover:text-indigo-600">N5 Level</a>
                <span class="opacity-20">/</span>
                <span class="text-slate-300">N4 Coming Soon</span>
            </div>
        </div>
    </nav>
    <main>{content}</main>
    <footer class="py-20 bg-slate-50 border-t border-slate-100 mt-20">
        <div class="max-w-7xl mx-auto px-6 text-center">
            <p class="text-slate-400 text-[10px] font-bold uppercase tracking-[0.4em]">
                © {datetime.now().year} {BRAND_NAME} • Japanese_Language_Learning
            </p>
        </div>
    </footer>
</body>
</html>"""

def build():
    levels = ['n5'] # Starting with N5 for demo
    all_kanji_for_index = []
    all_urls = []

    for lvl in levels:
        json_path = os.path.join(DATA_ROOT, lvl, 'kanji', 'data.json')
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        output_dir = os.path.join(lvl, 'kanji')
        os.makedirs(output_dir, exist_ok=True)

        for item in data['kanji_set']:
            all_kanji_for_index.append({**item, "lvl": lvl})
            
            # Individual SEO Pages
            ex_html = "".join([f"""
                <div class="zen-card p-10 rounded-[2.5rem] mb-6">
                    <p class="text-3xl font-black mb-6 leading-snug text-slate-900">{ex['japanese']}</p>
                    <div class="flex flex-col gap-2">
                        <p class="text-indigo-500 font-bold text-sm tracking-wide">{ex['romaji']}</p>
                        <p class="text-slate-500 text-lg leading-relaxed">{ex['english']}</p>
                    </div>
                </div>""" for ex in item['examples']])

            rel_html = "".join([f"""
                <a href="/{lvl}/kanji/{r['slug']}.html" class="zen-card px-6 py-4 rounded-2xl text-sm font-bold flex items-center gap-3 group">
                    <span class="text-2xl group-hover:scale-125 transition-transform">{r['kanji']}</span>
                    <span class="text-slate-400 uppercase tracking-tighter">{r['meaning']}</span>
                </a>""" for r in item.get('related_kanji', [])])

            content = f"""
            <div class="max-w-5xl mx-auto px-6 py-24">
                <div class="flex flex-col items-center text-center mb-24">
                    <div class="kanji-display mb-8">{item['kanji']}</div>
                    <h1 class="text-6xl font-extrabold text-slate-900 tracking-tight mb-4 uppercase">{item['meaning']}</h1>
                    <p class="text-indigo-600 font-black uppercase tracking-[0.6em] text-sm">{item['romaji']}</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-24">
                    <div class="zen-card p-10 rounded-[2rem]">
                        <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest block mb-4">Onyomi Reading</span>
                        <div class="text-4xl font-black text-slate-800">{"、".join(item['onyomi'])}</div>
                    </div>
                    <div class="zen-card p-10 rounded-[2rem]">
                        <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest block mb-4">Kunyomi Reading</span>
                        <div class="text-4xl font-black text-slate-800">{"、".join(item['kunyomi'])}</div>
                    </div>
                </div>

                <div class="mb-32">
                    <h2 class="text-center text-[10px] font-black text-slate-400 uppercase tracking-[0.5em] mb-12">Grammar & Contextual Usage</h2>
                    {ex_html}
                </div>

                <div class="pt-20 border-t border-slate-100">
                    <h2 class="text-center text-[10px] font-black text-slate-400 uppercase tracking-[0.5em] mb-12">Related Kanji Characters</h2>
                    <div class="grid grid-cols-2 md:grid-cols-5 gap-4">{rel_html}</div>
                </div>
            </div>"""

            slug_path = f"{lvl}/kanji/{item['slug']}.html"
            with open(slug_path, "w", encoding="utf-8") as f:
                f.write(get_zen_layout(f"{item['kanji']} Meaning", item['grammar_note'], content, slug_path))
            all_urls.append(f"{BASE_URL}/{slug_path}")

    # GENERATE MASTER INDEX.HTML (The Landing Page)
    index_cards = "".join([f"""
        <a href="/{k['lvl']}/kanji/{k['slug']}.html" class="zen-card p-10 rounded-[3rem] group">
            <div class="text-6xl font-black mb-6 group-hover:scale-110 transition-transform">{k['kanji']}</div>
            <div class="text-xs font-black uppercase tracking-widest text-slate-400 mb-2">{k['meaning']}</div>
            <div class="text-[10px] font-bold text-indigo-500 uppercase tracking-[0.2em]">{k['lvl']} Collection</div>
        </a>""" for k in all_kanji_for_index])

    home_content = f"""
    <div class="max-w-7xl mx-auto px-6 py-32 text-center">
        <h1 class="text-[80px] md:text-[120px] font-black leading-none tracking-tighter mb-8 text-slate-900">
            Master Every <span class="text-indigo-600 italic">Kanji.</span>
        </h1>
        <p class="max-w-2xl mx-auto text-xl text-slate-500 mb-24 font-medium leading-relaxed">
            The most advanced digital library for Japanese learners. Clean, modern, and built for contextual mastery.
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {index_cards}
        </div>
    </div>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(get_zen_layout("KanjiTest | Premium Learning Library", "Explore our N5-N1 Kanji collection.", home_content, "index.html"))

    # Generate Sitemap
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join([f'<url><loc>{u}</loc></url>' for u in all_urls]) + '</urlset>')

if __name__ == "__main__":
    build()
