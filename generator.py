import os 
import json
from datetime import datetime

# CONFIGURATION - kanjitest-online/web-platform
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
NAV_HEADER = "KanjiTest"
FOLDER_NAME = "Japanese_Language_Learning"

def get_universal_layout(title, desc, content, slug=""):
    """
    Universal HTML Shell for test.singhyogendra.com.np
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
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
        body {{ font-family: 'Noto Sans JP', sans-serif; background-color: #020617; color: #f1f5f9; }}
        .bento-card {{ background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(12px); }}
        .kanji-glow {{ text-shadow: 0 0 30px rgba(59, 130, 246, 0.5); font-size: 120px; }}
    </style>
</head>
<body class="antialiased">
    <nav class="border-b border-white/5 p-6 flex justify-between items-center bg-slate-950/50 sticky top-0 z-50 backdrop-blur-md">
        <a href="/" class="text-2xl font-black tracking-tighter italic uppercase">
            <span class="text-blue-500">学</span> {NAV_HEADER}
        </a>
        <div class="flex gap-6 text-xs font-bold uppercase tracking-widest text-slate-400">
            <a href="/n5/" class="hover:text-blue-500">N5 Level</a>
            <a href="/n4/" class="hover:text-blue-500">N4 Level</a>
        </div>
    </nav>
    <main>{content}</main>
    <footer class="p-20 text-center border-t border-white/5 mt-20">
        <p class="text-slate-600 text-[10px] font-black uppercase tracking-[0.3em]">© {datetime.now().year} {BRAND_NAME} • {FOLDER_NAME}</p>
    </footer>
</body>
</html>"""

def build_platform():
    levels = ['n5', 'n4', 'n3', 'n2', 'n1']
    all_urls = []

    for lvl in levels:
        json_path = f'data-engine/api/{lvl}/data.json'
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 1. Level Index (e.g., /n5/index.html)
        os.makedirs(lvl, exist_ok=True)
        grid_items = "".join([f'<a href="/{lvl}/kanji/{k["slug"]}.html" class="bento-card p-10 rounded-[2rem] text-center hover:scale-105 transition-transform"><div class="text-6xl mb-4">{k["kanji"]}</div><div class="text-[10px] font-bold text-slate-500 uppercase">{k["meaning"]}</div></a>' for k in data['kanji_set']])
        
        level_html = f'<div class="max-w-7xl mx-auto px-6 py-20"><h1 class="text-6xl font-black mb-12 italic uppercase">JLPT {lvl}</h1><div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">{grid_items}</div></div>'
        
        with open(f"{lvl}/index.html", "w", encoding="utf-8") as f:
            f.write(get_universal_layout(f"JLPT {lvl} Study Set", f"Master {lvl} Kanji", level_html, f"{lvl}/index.html"))
        
        # 2. Individual Kanji (e.g., /n5/kanji/go-five.html)
        kanji_dir = f"{lvl}/kanji"
        os.makedirs(kanji_dir, exist_ok=True)
        
        for k in data['kanji_set']:
            # Building 5 LONG EXAMPLES
            ex_html = "".join([f'<div class="bento-card p-8 rounded-3xl mb-4"><p class="text-2xl mb-4 font-bold">{ex["japanese"]}</p><p class="text-blue-400 text-sm italic mb-2">{ex["romaji"]}</p><p class="text-slate-400">{ex["english"]}</p></div>' for ex in k['examples']])
            
            # Building 5 RELATED KANJI
            rel_html = "".join([f'<a href="/{lvl}/kanji/{r["slug"]}.html" class="px-6 py-3 bento-card rounded-full text-xs font-bold hover:bg-blue-600">{r["kanji"]} {r["meaning"]}</a>' for r in k.get('related_kanji', [])])

            content = f"""
            <div class="max-w-4xl mx-auto px-6 py-20">
                <div class="text-center mb-20">
                    <div class="kanji-glow mb-6">{k['kanji']}</div>
                    <h1 class="text-5xl font-black uppercase italic">{k['meaning']}</h1>
                    <p class="text-slate-500 tracking-[0.5em] mt-4 uppercase font-bold">{k['romaji']}</p>
                </div>
                <div class="mb-20">
                    <h3 class="text-[10px] font-black text-slate-600 uppercase tracking-widest mb-8 text-center">Contextual Mastery (5 Long Examples)</h3>
                    {ex_html}
                </div>
                <div class="text-center">
                    <h3 class="text-[10px] font-black text-slate-600 uppercase tracking-widest mb-8">Related Japanese Kanji</h3>
                    <div class="flex flex-wrap justify-center gap-3">{rel_html}</div>
                </div>
            </div>"""
            
            with open(f"{kanji_dir}/{k['slug']}.html", "w", encoding="utf-8") as f:
                f.write(get_universal_layout(f"Study {k['kanji']}", f"Meaning of {k['kanji']}", content, f"{lvl}/kanji/{k['slug']}.html"))
            
            all_urls.append(f"{BASE_URL}/{lvl}/kanji/{k['slug']}.html")

    # Final Sitemap
    with open("sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join([f'<url><loc>{u}</loc></url>' for u in all_urls]) + '</urlset>')

if __name__ == "__main__":
    build_platform()
