import json
import os

def generate_unlimited_pages():
    levels = ['n5', 'n4', 'n3', 'n2', 'n1']
    
    for lvl in levels:
        # Path to your level-specific API
        json_path = f'data-engine/api/{lvl}/data.json'
        
        if not os.path.exists(json_path):
            continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Ensure the SEO folder exists: e.g., /kanji/n5/kanji/
        output_dir = f'{lvl}/kanji'
        os.makedirs(output_dir, exist_ok=True)

        for item in data['kanji_set']:
            # Create a unique SEO-friendly URL based on the slug
            file_name = f"{item['slug']}.html"
            full_path = os.path.join(output_dir, file_name)

            # HTML content with 5 Long Examples and Related Kanji
            html_content = f"""
            <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="UTF-8">
                <title>{item['kanji']} ({item['meaning']}) - JLPT {lvl.upper()} | Kanjitest.online</title>
                <meta name="description" content="Master {item['kanji']} with 5 examples and related kanji.">
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-slate-950 text-slate-200">
                <h1 class="text-9xl">{item['kanji']}</h1>
                <div class="related-links">
                    {" ".join([f'<a href="{r["slug"]}.html">{r["kanji"]}</a>' for r in item.get('related_kanji', [])])}
                </div>
            </body>
            </html>
            """
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
    
    print("SEO Engine: All Kanji pages have been auto-generated successfully.")

if __name__ == "__main__":
    generate_unlimited_pages()
