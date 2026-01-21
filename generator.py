import os
import json
import shutil
from datetime import datetime

# CONFIGURATION
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
NAV_HEADER = "KanjiTest"
FOLDER_NAME = "Japanese_Language_Learning"

# ADSENSE & SEO ASSETS
AD_CODE = '<div class="max-w-6xl mx-auto px-4 py-4 text-center text-slate-500 text-xs border border-white/5 rounded-2xl my-8">AD REVENUE SLOT</div>'

def get_layout(title, desc, content, level="N5", slug=""):
    """
    The 'Universal' UI Engine. 
    Implements a Premium Dark Bento UI with Glassmorphism.
    """
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {BRAND_NAME}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{BASE_URL}/{slug}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
        body {{ font-family: 'Noto Sans JP', sans-serif; background-color: #020617; color: #f1f5f9; }}
        .bento-card {{ background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(10px); transition: all 0.3s ease; }}
        .bento-card:hover {{ border-color: #3b82f6; transform: translateY(-2px); }}
        .kanji-hero {{ font-size: clamp(5rem, 15vw, 10rem); font-weight: 900; background: linear-gradient(to bottom, #fff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
    </style>
</head>
<body class="antialiased">
    <nav class="sticky top-0 z-50 border-b border-white/5 bg-slate-950/80 backdrop-blur-xl">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <a href="{BASE_URL}/" class="text-2xl font-black tracking-tighter flex items-center gap-2">
                <span class="text-blue-500">学</span> {NAV_HEADER}
            </a>
            <div class="hidden md:flex gap-6 text-sm font-bold uppercase tracking-widest text-slate-400">
                <a href="{BASE_URL}/n5/" class="hover:text-blue-500">N5</a>
                <a href="{BASE_URL}/n4/" class="hover:text-blue-500">N4</a>
                <a href="{BASE_URL}/n3/" class="hover:text-blue-500">N3</a>
            </div>
        </div>
    </nav>

    <main class="min-h-screen">{content}</main>

    <footer class="bg-slate-950 border-t border-white/5 pt-20 pb-10">
        <div class="max-w-7xl mx-auto px-6 text-center">
            <h2 class="text-xl font-black uppercase mb-4 tracking-widest">{BRAND_NAME}</h2>
            <p class="text-slate-500 text-sm max-w-lg mx-auto mb-10">A professional collection of Kanji and Grammar for N5-N1 students. Organized under {FOLDER_NAME}.</p>
            <div class="pt-8 border-t border-white/5 text-[10px] text-slate-600 font-bold uppercase tracking-[0.2em]">
                © {datetime.now().year} {BRAND_NAME} • Built for Excellence
            </div>
        </div>
    </footer>
</body>
</html>"""

def build():
    # Folder Structure Setup
    levels = ['n5', 'n4', 'n3', 'n2', 'n1']
    os.makedirs('docs', exist_ok=True)
    all_urls = []

    # Process Levels
    for lvl in levels:
        json_path = f'data-engine/api/{lvl}/data.json'
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 1. GENERATE LEVEL INDEX PAGE (e.g., n5/index.html)
        os.makedirs(f'docs/{lvl}', exist_ok=True)
        grid_html = f'<div class="max-w-7xl mx-auto px-6 py-20"><h1 class="text-5xl font-black mb-12 uppercase italic">JLPT {lvl} <span class="text-blue-500">Collection</span></h1><div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">'
        
        for k in data['kanji_set']:
            grid_html += f"""
            <a href="{BASE_URL}/{lvl}/kanji/{k['slug']}.html" class="bento-card rounded-3xl p-8 flex flex-col items-center group">
                <span class="text-5xl font-black mb-4 group-hover:scale-110 transition-transform">{k['kanji']}</span>
                <span class="text-[10px] font-black uppercase tracking-widest text-slate-500">{k['meaning']}</span>
            </a>"""
        grid_html += "</div></div>"
        
        with open(f"docs/{lvl}/index.html", "w", encoding="utf-8") as f:
            f.write(get_layout(f"JLPT {lvl} Kanji Set", f"Full list of {lvl} Kanji.", grid_html, lvl, f"{lvl}/index.html"))
        all_urls.append(f"{BASE_URL}/{lvl}/index.html")

        # 2. GENERATE INDIVIDUAL KANJI PAGES (unlimited)
        os.makedirs(f'docs/{lvl}/kanji', exist_ok=True)
        for k in data['kanji_set']:
            # Building 5 Long Examples Logic
            examples_html = ""
            for ex in k['examples']:
                examples_html += f"""
                <div class="bento-card rounded-3xl p-8 mb-6">
                    <p class="text-2xl md:text-3xl font-bold mb-4 leading-relaxed">{ex['japanese']}</p>
                    <p class="text-blue-400 font-mono text-sm mb-2 italic">{ex['romaji']}</p>
                    <p class="text-slate-400 text-base">{ex['english']}</p>
                </div>"""

            # Building 5 Related Kanji Logic
            related_html = ""
            for rel in k.get('related_kanji', []):
                related_html += f"""
                <a href="{BASE_URL}/{lvl}/kanji/{rel['slug']}.html" class="px-6 py-3 bento-card rounded-full text-sm font-bold hover:bg-blue-600 transition-colors">
                    {rel['kanji']} <span class="ml-2 opacity-50">{rel['meaning']}</span>
                </a>"""

            detail_content = f"""
            <div class="max-w-5xl mx-auto px-6 py-20">
                <div class="flex flex-col items-center text-center mb-20">
                    <div class="kanji-hero">{k['kanji']}</div>
                    <h1 class="text-4xl font-black uppercase tracking-tighter mt-4">{k['meaning']}</h1>
                    <p class="text-slate-500 mt-2 font-bold uppercase tracking-widest">{k['romaji']}</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                    <div class="bento-card rounded-3xl p-8">
                        <h3 class="text-xs font-black text-blue-500 uppercase tracking-widest mb-4">Onyomi</h3>
                        <p class="text-2xl font-bold">{"、".join(k['onyomi'])}</p>
                    </div>
                    <div class="bento-card rounded-3xl p-8">
                        <h3 class="text-xs font-black text-emerald-500 uppercase tracking-widest mb-4">Kunyomi</h3>
                        <p class="text-2xl font-bold">{"、".join(k['kunyomi'])}</p>
                    </div>
                </div>

                <div class="mb-20">
                    <h3 class="text-xs font-black text-slate-500 uppercase tracking-widest mb-8 text-center">Context & Study Examples</h3>
                    {examples_html}
                </div>

                <div class="text-center">
                    <h3 class="text-xs font-black text-slate-500 uppercase tracking-widest mb-8">Related Kanji</h3>
                    <div class="flex flex-wrap justify-center gap-4">{related_html}</div>
                </div>
            </div>"""

            with open(f"docs/{lvl}/kanji/{k['slug']}.html", "w", encoding="utf-8") as f:
                f.write(get_layout(f"Kanji {k['kanji']} Meaning", f"Study {k['kanji']} for {lvl}.", detail_content, lvl, f"{lvl}/kanji/{k['slug']}.html"))
            all_urls.append(f"{BASE_URL}/{lvl}/kanji/{k['slug']}.html")

    # 3. ROOT INDEX.HTML (Bento Hub)
    home_content = f"""
    <div class="max-w-7xl mx-auto px-6 py-20 text-center">
        <h1 class="text-7xl md:text-9xl font-black tracking-tighter mb-6 italic">KANJI<span class="text-blue-500">TEST</span></h1>
        <p class="text-slate-500 max-w-2xl mx-auto text-lg mb-20 font-medium">The most comprehensive digital collection of Japanese Kanji for levels N5 through N1. Organized for serious learners.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <a href="{BASE_URL}/n5/" class="bento-card rounded-[3rem] p-12 text-left group">
                <div class="text-blue-500 text-xs font-black uppercase tracking-widest mb-4">Elementary</div>
                <h2 class="text-5xl font-black mb-4 group-hover:translate-x-2 transition-transform">N5 Level →</h2>
                <p class="text-slate-400">Basic Kanji for everyday life and beginner tests.</p>
            </a>
            </div>
    </div>"""
    
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(get_layout("KanjiTest Collection Home", "N5-N1 Japanese Study Collection", home_content, "Home", "index.html"))
    all_urls.append(f"{BASE_URL}/index.html")

    # 4. SITEMAP GENERATION
    sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join([f'<url><loc>{u}</loc></url>' for u in all_urls]) + '</urlset>'
    with open("docs/sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap)
    
    print(f"Deployment successful. {len(all_urls)} pages generated in /docs under {FOLDER_NAME} mode.")

if __name__ == "__main__":
    build()
