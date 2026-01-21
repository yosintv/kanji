import os
import json
from datetime import datetime
 
# CONFIGURATION - kanjitest-online/web-platform
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
DATA_ROOT = "data" 
FOLDER_NAME = "Japanese_Language_Learning"

def get_seo_layout(title, desc, content, slug, kanji_char, level):
    # (Same layout as before remains identical)
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {BRAND_NAME}</title>
    <meta name="description" content="{desc}">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
        body {{ font-family: 'Noto Sans JP', sans-serif; background-color: #020617; color: #f1f5f9; }}
        .bento-card {{ background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(12px); }}
    </style>
</head>
<body><nav class="p-6 border-b border-white/5 font-black tracking-tighter italic">学 {BRAND_NAME}</nav>
<main>{content}</main>
<footer class="p-10 text-center text-[10px] text-slate-600 font-bold uppercase tracking-[0.3em]">© {datetime.now().year} {FOLDER_NAME}</footer>
</body></html>"""

def build():
    levels = ['n5', 'n4', 'n3', 'n2', 'n1']
    all_urls = []

    for lvl in levels:
        json_path = os.path.join(DATA_ROOT, lvl, 'kanji', 'data.json')
        
        # 🛡️ SAFETY CHECK 1: Does file exist?
        if not os.path.exists(json_path):
            print(f"ℹ️ Skipping {lvl}: Path {json_path} not found.")
            continue

        # 🛡️ SAFETY CHECK 2: Is the file empty?
        if os.path.getsize(json_path) == 0:
            print(f"⚠️ Warning: {json_path} is empty. Skipping to avoid crash.")
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            # 🛡️ SAFETY CHECK 3: Is the JSON formatted correctly?
            print(f"❌ Error decoding {json_path}: {e}")
            continue

        print(f"✅ Processing Level: {lvl} ({len(data.get('kanji_set', []))} kanji found)")

        # Create output folders in root: /n5/kanji/
        output_dir = os.path.join(lvl, 'kanji')
        os.makedirs(output_dir, exist_ok=True)

        for item in data['kanji_set']:
            # Building Long Examples (SEO Focused)
            ex_html = "".join([f'<div class="bento-card p-8 rounded-[2rem] mb-4"><p class="text-2xl font-bold mb-2 text-white">{ex["japanese"]}</p><p class="text-blue-400 text-sm mb-2 font-mono italic">{ex["romaji"]}</p><p class="text-slate-400">{ex["english"]}</p></div>' for ex in item['examples']])
            
            # Building 5 Related Kanji (KanjiTest Logic)
            rel_html = "".join([f'<a href="/{lvl}/kanji/{r["slug"]}.html" class="p-4 bento-card rounded-2xl text-xs font-bold hover:border-blue-500">{r["kanji"]} {r["meaning"]}</a>' for r in item.get('related_kanji', [])])

            title = f"Kanji {item['kanji']} ({item['meaning']}) - {lvl} Examples"
            desc = f"Learn {item['kanji']} for {lvl}. Includes {len(item['examples'])} long sentences and {len(item.get('related_kanji', []))} related kanji."

            content = f"""
            <article class="max-w-4xl mx-auto px-6 py-20 text-center">
                <div class="text-[120px] font-black text-white mb-4">{item['kanji']}</div>
                <h1 class="text-5xl font-black uppercase italic mb-10">{item['meaning']}</h1>
                <div class="space-y-4 mb-20">{ex_html}</div>
                <div class="flex flex-wrap justify-center gap-3">{rel_html}</div>
            </article>"""

            slug_path = f"{lvl}/kanji/{item['slug']}.html"
            with open(slug_path, "w", encoding="utf-8") as f:
                f.write(get_seo_layout(title, desc, content, slug_path, item['kanji'], lvl))
            
            all_urls.append(f"{BASE_URL}/{slug_path}")

    # Generate sitemap.xml
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join([f'<url><loc>{u}</loc></url>' for u in all_urls]) + '</urlset>')

if __name__ == "__main__":
    build()
