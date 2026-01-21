import os
import json
from datetime import datetime

# CONFIGURATION
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
DATA_ROOT = "data" # Source: data/n5/kanji/data.json

def get_seo_layout(title, desc, content, slug, kanji_char, level):
    """
    Universal SEO Layout with JSON-LD Schema for rich search results.
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
    <meta property="og:type" content="article">
    <meta property="og:url" content="{BASE_URL}/{slug}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
        body {{ font-family: 'Noto Sans JP', sans-serif; background-color: #020617; color: #f1f5f9; }}
        .bento-card {{ background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(12px); }}
        .kanji-main {{ font-size: clamp(80px, 15vw, 150px); font-weight: 900; color: white; text-shadow: 0 0 40px rgba(59, 130, 246, 0.4); }}
    </style>
</head>
<body class="antialiased">
    <nav class="border-b border-white/5 p-6 flex justify-between items-center sticky top-0 bg-slate-950/80 backdrop-blur-xl z-50">
        <a href="/" class="text-2xl font-black italic uppercase tracking-tighter">
            <span class="text-blue-500">学</span> {BRAND_NAME}
        </a>
        <div class="flex gap-4 text-[10px] font-black uppercase tracking-widest text-slate-500">
            <a href="/n5/" class="hover:text-blue-500">N5</a>
            <a href="/n4/" class="hover:text-blue-500">N4</a>
        </div>
    </nav>

    <main>{content}</main>

    <footer class="p-20 text-center border-t border-white/5 mt-20">
        <p class="text-slate-600 text-[10px] font-black uppercase tracking-[0.3em]">© {datetime.now().year} {BRAND_NAME} • Japanese_Language_Learning</p>
    </footer>
</body>
</html>"""

def build():
    levels = ['n5', 'n4', 'n3', 'n2', 'n1']
    all_urls = []

    for lvl in levels:
        # Correct path as per instructions: data/n5/kanji/data.json
        json_path = os.path.join(DATA_ROOT, lvl, 'kanji', 'data.json')
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Create output folders in root: /n5/kanji/
        output_dir = os.path.join(lvl, 'kanji')
        os.makedirs(output_dir, exist_ok=True)

        for item in data['kanji_set']:
            # 1. Build Long Examples
            ex_html = ""
            for ex in item['examples']:
                ex_html += f"""
                <div class="bento-card p-8 rounded-[2rem] mb-6">
                    <p class="text-2xl md:text-3xl font-bold mb-4 leading-relaxed text-white">{ex['japanese']}</p>
                    <p class="text-blue-400 font-mono text-sm mb-2 italic">{ex['romaji']}</p>
                    <p class="text-slate-400 text-base">{ex['english']}</p>
                </div>"""

            # 2. Build 5 Related Kanji links
            rel_html = ""
            for rel in item.get('related_kanji', []):
                rel_html += f"""
                <a href="/{lvl}/kanji/{rel['slug']}.html" class="px-6 py-4 bento-card rounded-2xl text-sm font-bold hover:border-blue-500 transition-all">
                    <span class="text-xl mr-2 text-blue-500">{rel['kanji']}</span> {rel['meaning']}
                </a>"""

            # 3. Create Unique SEO Meta
            title = f"Kanji {item['kanji']} ({item['meaning']}) - {lvl} Examples & Meaning"
            # Using the grammar note + examples for a rich description
            desc = f"Learn {item['kanji']} ({item['meaning']}). {item['grammar_note'][:120]}... Includes 5 long sentence examples and related Kanji: {', '.join([r['kanji'] for r in item['related_kanji']])}."

            content = f"""
            <article class="max-w-5xl mx-auto px-6 py-20">
                <div class="text-center mb-20">
                    <div class="kanji-main mb-6">{item['kanji']}</div>
                    <h1 class="text-6xl font-black uppercase italic tracking-tighter mb-4 text-white">{item['meaning']}</h1>
                    <div class="flex justify-center gap-10 text-slate-500 font-black uppercase tracking-[0.4em] text-sm">
                        <span>{item['romaji']}</span>
                        <span class="text-blue-500">{lvl}</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-20">
                    <div class="bento-card p-10 rounded-[2.5rem]">
                        <h3 class="text-blue-500 text-[10px] font-black uppercase tracking-widest mb-4">Onyomi Reading</h3>
                        <p class="text-3xl font-bold text-white">{"、".join(item['onyomi'])}</p>
                    </div>
                    <div class="bento-card p-10 rounded-[2.5rem]">
                        <h3 class="text-emerald-500 text-[10px] font-black uppercase tracking-widest mb-4">Kunyomi Reading</h3>
                        <p class="text-3xl font-bold text-white">{"、".join(item['kunyomi'])}</p>
                    </div>
                </div>

                <div class="mb-24">
                    <h2 class="text-xs font-black text-slate-600 uppercase tracking-[0.4em] mb-12 text-center">Contextual Learning (5 Sentences)</h2>
                    {ex_html}
                </div>

                <div class="bento-card p-12 rounded-[3rem] text-center">
                    <h2 class="text-xs font-black text-slate-600 uppercase tracking-[0.4em] mb-10">Related {lvl} Kanji Set</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
                        {rel_html}
                    </div>
                </div>
            </article>"""

            # Save each unique file
            slug_path = f"{lvl}/kanji/{item['slug']}.html"
            with open(slug_path, "w", encoding="utf-8") as f:
                f.write(get_seo_layout(title, desc, content, slug_path, item['kanji'], lvl))
            
            all_urls.append(f"{BASE_URL}/{slug_path}")

    # Generate sitemap.xml for Google indexing
    sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + \
              "".join([f'<url><loc>{u}</loc><lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod></url>' for u in all_urls]) + \
              '</urlset>'
    with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap)

if __name__ == "__main__":
    build()
