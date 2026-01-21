import os
import json
from datetime import datetime

# CONFIGURATION - kanjitest-online/web-platform
BASE_URL = "https://test.singhyogendra.com.np"
BRAND_NAME = "KanjiTest.Online"
DATA_ROOT = "data" 
FOLDER_NAME = "Japanese_Language_Learning"

def get_pro_layout(title, desc, content, slug, kanji_char=None, lvl=None):
    """
    Ultra-Premium Academic Platform with Advanced Glassmorphism, 
    Micro-interactions, and Cutting-Edge Design Patterns
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Serif+JP:wght@400;700;900&display=swap');
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{ 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #f8faff 0%, #fef3f9 100%);
            color: #0f172a;
            overflow-x: hidden;
            position: relative;
            min-height: 100vh;
        }}
        
        /* Animated gradient background */
        body::before {{
            content: '';
            position: fixed;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(168, 85, 247, 0.08) 0%, transparent 50%);
            animation: gradientShift 20s ease infinite;
            z-index: -1;
            pointer-events: none;
        }}
        
        @keyframes gradientShift {{
            0%, 100% {{ transform: translate(0, 0) rotate(0deg); }}
            50% {{ transform: translate(5%, 5%) rotate(5deg); }}
        }}
        
        .kanji-font {{ 
            font-family: 'Noto Serif JP', serif;
            font-weight: 900;
            letter-spacing: -0.02em;
        }}
        
        /* Premium Glass Card */
        .glass-card {{ 
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.04),
                0 1px 3px rgba(0, 0, 0, 0.02),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .glass-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            transition: left 0.7s;
        }}
        
        .glass-card:hover {{
            transform: translateY(-12px) scale(1.02);
            box-shadow: 
                0 32px 64px rgba(99, 102, 241, 0.15),
                0 8px 16px rgba(0, 0, 0, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 1);
            border-color: rgba(99, 102, 241, 0.3);
        }}
        
        .glass-card:hover::before {{
            left: 100%;
        }}
        
        /* Badge Styles */
        .badge {{ 
            padding: 6px 16px;
            border-radius: 100px;
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
        }}
        
        .badge:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}
        
        /* Loading Shimmer */
        .shimmer {{ 
            background: linear-gradient(
                90deg, 
                rgba(241, 245, 249, 0.8) 25%, 
                rgba(248, 250, 252, 0.9) 50%, 
                rgba(241, 245, 249, 0.8) 75%
            );
            background-size: 200% 100%;
            animation: shimmer 2s infinite ease-in-out;
        }}
        
        @keyframes shimmer {{ 
            0% {{ background-position: 200% 0; }} 
            100% {{ background-position: -200% 0; }} 
        }}
        
        /* Navigation Bar */
        nav {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(24px) saturate(180%);
            -webkit-backdrop-filter: blur(24px) saturate(180%);
            border-bottom: 1px solid rgba(226, 232, 240, 0.5);
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.02);
        }}
        
        nav a {{
            position: relative;
            transition: all 0.3s ease;
        }}
        
        nav a::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #6366f1, #a855f7);
            transition: width 0.3s ease;
        }}
        
        nav a:hover::after {{
            width: 100%;
        }}
        
        /* Button Styles */
        .btn-primary {{
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            padding: 16px 32px;
            border-radius: 16px;
            font-weight: 800;
            font-size: 12px;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 
                0 8px 24px rgba(99, 102, 241, 0.25),
                0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        
        .btn-primary::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.5s;
        }}
        
        .btn-primary:hover {{
            transform: translateY(-4px) scale(1.02);
            box-shadow: 
                0 16px 48px rgba(99, 102, 241, 0.35),
                0 8px 16px rgba(0, 0, 0, 0.15);
        }}
        
        .btn-primary:hover::before {{
            left: 100%;
        }}
        
        .btn-primary:active {{
            transform: translateY(-2px) scale(1.01);
        }}
        
        /* Kanji Display Enhancement */
        .kanji-display {{
            position: relative;
            text-shadow: 0 4px 24px rgba(99, 102, 241, 0.15);
            transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .kanji-display:hover {{
            transform: scale(1.08) rotate(2deg);
            text-shadow: 0 8px 32px rgba(99, 102, 241, 0.25);
        }}
        
        /* Reading Cards */
        .reading-card {{
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
            border: 1px solid rgba(226, 232, 240, 0.6);
            transition: all 0.4s ease;
        }}
        
        .reading-card:hover {{
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(240, 247, 255, 0.95) 100%);
            border-color: rgba(99, 102, 241, 0.3);
            box-shadow: 0 12px 32px rgba(99, 102, 241, 0.12);
        }}
        
        /* Example Cards */
        .example-card {{
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(252, 252, 253, 0.9) 100%);
            border-left: 4px solid transparent;
            transition: all 0.4s ease;
        }}
        
        .example-card:hover {{
            border-left-color: #6366f1;
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(245, 243, 255, 0.95) 100%);
            transform: translateX(8px);
        }}
        
        /* Scroll Progress Bar */
        .progress-bar {{
            position: fixed;
            top: 64px;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
            transform-origin: left;
            z-index: 100;
            transition: transform 0.1s ease-out;
        }}
        
        /* Focus States for Accessibility */
        *:focus-visible {{
            outline: 3px solid rgba(99, 102, 241, 0.5);
            outline-offset: 4px;
            border-radius: 4px;
        }}
        
        /* Selection */
        ::selection {{
            background: rgba(99, 102, 241, 0.2);
            color: #1e293b;
        }}
        
        /* Responsive Typography */
        @media (max-width: 768px) {{
            .kanji-display {{ font-size: clamp(4rem, 15vw, 6rem); }}
        }}
        
        /* Smooth Scrolling */
        html {{
            scroll-behavior: smooth;
        }}
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar {{
            width: 12px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: #f1f5f9;
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: linear-gradient(180deg, #6366f1, #a855f7);
            border-radius: 6px;
            border: 2px solid #f1f5f9;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: linear-gradient(180deg, #4f46e5, #9333ea);
        }}
    </style>
</head>
<body class="antialiased">
    <!-- Scroll Progress Bar -->
    <div class="progress-bar" id="progressBar" style="transform: scaleX(0);"></div>
    
    <!-- Navigation -->
    <nav class="sticky top-0 z-50 h-16 flex items-center px-4 md:px-8 justify-between" role="navigation" aria-label="Main navigation">
        <a href="/" class="text-xl md:text-2xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 transition-all duration-300" aria-label="Home">
            学 KANJITEST
        </a>
        <div class="flex gap-6 md:gap-10 text-[10px] md:text-[11px] font-bold uppercase tracking-widest">
            <a href="/" class="text-slate-500 hover:text-indigo-600 transition-all duration-300" aria-label="Library">Library</a>
            <a href="/n5/" class="text-indigo-600 hover:text-indigo-700 transition-all duration-300" aria-label="N5 Hub">N5 Hub</a>
        </div>
    </nav>
    
    <!-- Main Content -->
    <main class="min-h-screen" role="main">{content}</main>
    
    <!-- Footer -->
    <footer class="border-t border-slate-200/60 py-16 md:py-24 bg-gradient-to-b from-slate-50/50 to-white/80 backdrop-blur-sm" role="contentinfo">
        <div class="max-w-6xl mx-auto px-6 text-center">
            <div class="mb-8">
                <div class="text-2xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 mb-4">
                    学 KANJITEST
                </div>
                <p class="text-slate-500 text-sm max-w-md mx-auto leading-relaxed">
                    Premium Japanese language learning platform for JLPT mastery
                </p>
            </div>
            <div class="flex justify-center gap-8 mb-8 text-xs font-semibold text-slate-400">
                <a href="/" class="hover:text-indigo-600 transition-colors">Home</a>
                <a href="/n5/" class="hover:text-indigo-600 transition-colors">N5</a>
                <a href="/about/" class="hover:text-indigo-600 transition-colors">About</a>
            </div>
            <p class="text-slate-400 text-[10px] font-bold uppercase tracking-[0.2em]">
                © {datetime.now().year} {FOLDER_NAME}. All rights reserved.
            </p>
        </div>
    </footer>
    
    <!-- Scroll Progress Script -->
    <script>
        window.addEventListener('scroll', () => {{
            const winScroll = document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height);
            document.getElementById('progressBar').style.transform = `scaleX(${{scrolled}})`;
        }});
        
        // Add smooth scroll behavior to all anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
    </script>
</body>
</html>"""

def build():
    levels = ['n5'] 
    all_kanji_data = []
    all_urls = []

    for lvl in levels:
        json_path = os.path.join(DATA_ROOT, lvl, 'kanji', 'data.json')
        if not os.path.exists(json_path): continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        os.makedirs(os.path.join(lvl, 'kanji'), exist_ok=True)

        # 1. DYNAMIC HUB PAGE WITH ENHANCED UX
        hub_content = f"""
        <div class="max-w-7xl mx-auto px-4 md:px-8 py-12 md:py-24">
            <!-- Hero Section -->
            <header class="mb-16 md:mb-28 text-center md:text-left">
                <div class="inline-flex items-center gap-3 mb-6">
                    <span class="badge bg-gradient-to-r from-indigo-50 to-purple-50 text-indigo-600 border border-indigo-100">
                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/>
                            <path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/>
                        </svg>
                        {lvl.upper()} Collection
                    </span>
                </div>
                <h1 class="text-5xl md:text-8xl font-black tracking-tighter text-slate-900 leading-none mb-6">
                    The N5
                    <span class="block text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600">
                        Collection.
                    </span>
                </h1>
                <p class="text-lg md:text-xl text-slate-500 max-w-2xl leading-relaxed">
                    Master the foundational 80 kanji characters with interactive examples, 
                    comprehensive readings, and real-world usage patterns.
                </p>
            </header>
            
            <!-- Dynamic Grid -->
            <div id="dynamic-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 md:gap-8" role="list" aria-label="Kanji collection">
                <!-- Loading Shimmer -->
                <div class="shimmer h-72 rounded-[2rem] md:rounded-[3rem]" aria-hidden="true"></div>
                <div class="shimmer h-72 rounded-[2rem] md:rounded-[3rem] hidden sm:block" aria-hidden="true"></div>
                <div class="shimmer h-72 rounded-[2rem] md:rounded-[3rem] hidden lg:block" aria-hidden="true"></div>
                <div class="shimmer h-72 rounded-[2rem] md:rounded-[3rem] hidden xl:block" aria-hidden="true"></div>
            </div>
        </div>
        
        <script>
            async function loadHub() {{
                try {{
                    const res = await fetch('/data/{lvl}/kanji/data.json');
                    if (!res.ok) throw new Error('Failed to load data');
                    
                    const d = await res.json();
                    const g = document.getElementById('dynamic-grid');
                    
                    g.innerHTML = d.kanji_set.map(k => `
                        <article class="glass-card p-8 md:p-12 rounded-[2rem] md:rounded-[3rem] group text-center flex flex-col items-center border border-slate-100" role="listitem">
                            <div class="kanji-display text-6xl md:text-8xl mb-6 md:mb-8 text-slate-900">
                                ${{k.kanji}}
                            </div>
                            <div class="mb-8 flex-1">
                                <h2 class="font-black text-lg md:text-xl uppercase tracking-tight text-slate-800 mb-2">
                                    ${{k.meaning}}
                                </h2>
                                <p class="text-[10px] md:text-xs text-slate-400 font-semibold tracking-wider uppercase">
                                    ${{k.romaji}}
                                </p>
                            </div>
                            <a href="/{lvl}/kanji/${{k.slug}}.html" 
                               class="w-full py-4 md:py-5 bg-slate-900 text-white text-[10px] md:text-xs font-black uppercase tracking-[0.15em] rounded-2xl hover:bg-gradient-to-r hover:from-indigo-600 hover:to-purple-600 transition-all duration-500 shadow-lg hover:shadow-2xl hover:shadow-indigo-200 hover:-translate-y-1"
                               aria-label="View details for ${{k.kanji}} - ${{k.meaning}}">
                                View Details
                                <span aria-hidden="true"> →</span>
                            </a>
                        </article>
                    `).join('');
                }} catch (e) {{ 
                    console.error("Fetch Error:", e);
                    document.getElementById('dynamic-grid').innerHTML = `
                        <div class="col-span-full text-center py-20">
                            <p class="text-slate-400 text-lg">Failed to load kanji data. Please refresh the page.</p>
                        </div>
                    `;
                }}
            }}
            
            window.addEventListener('load', loadHub);
        </script>"""
        
        with open(f"{lvl}/index.html", "w", encoding="utf-8") as f:
            f.write(get_pro_layout(
                f"JLPT {lvl.upper()} Kanji Library - Master 80 Essential Characters", 
                f"Complete collection of {lvl.upper()} level kanji with readings, examples, and grammar notes for JLPT preparation", 
                hub_content, 
                f"{lvl}/index.html"
            ))

        # 2. INDIVIDUAL KANJI DETAIL PAGES
        for item in data['kanji_set']:
            all_kanji_data.append({{**item, "lvl": lvl}})
            
            # Enhanced Examples Section
            ex_view = "".join([f"""
                <div class="example-card glass-card p-8 md:p-12 rounded-[2rem] md:rounded-[2.5rem] mb-6 transition-all duration-400">
                    <div class="flex items-start gap-4 mb-6">
                        <span class="badge bg-indigo-600 text-white flex-shrink-0">Example {i+1}</span>
                    </div>
                    <p class="text-2xl md:text-4xl font-black mb-6 kanji-font text-slate-900 leading-relaxed">
                        {ex['japanese']}
                    </p>
                    <div class="space-y-3">
                        <div class="flex items-center gap-3">
                            <svg class="w-5 h-5 text-indigo-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
                            </svg>
                            <span class="text-sm md:text-base font-semibold text-slate-600 italic">
                                {ex['romaji']}
                            </span>
                        </div>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed pl-8">
                            {ex['english']}
                        </p>
                    </div>
                </div>""" for i, ex in enumerate(item['examples'])])

            # Detail Page Content
            detail_content = f"""
            <div class="max-w-5xl mx-auto px-4 md:px-8 py-12 md:py-24">
                <!-- Kanji Hero Section -->
                <div class="text-center mb-20 md:mb-32">
                    <div class="inline-block mb-8">
                        <div class="kanji-display text-[120px] md:text-[200px] leading-none text-transparent bg-clip-text bg-gradient-to-br from-slate-900 via-indigo-900 to-purple-900">
                            {item['kanji']}
                        </div>
                    </div>
                    <h1 class="text-4xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-slate-900">
                        {item['meaning']}
                    </h1>
                    <div class="inline-flex items-center gap-3">
                        <span class="badge bg-gradient-to-r from-slate-100 to-slate-50 text-slate-600 text-sm border border-slate-200">
                            {item['romaji']}
                        </span>
                        <span class="badge bg-gradient-to-r from-indigo-50 to-purple-50 text-indigo-600 border border-indigo-100">
                            {lvl.upper()} Level
                        </span>
                    </div>
                </div>
                
                <!-- Readings Grid -->
                <section class="mb-20 md:mb-32" aria-labelledby="readings-title">
                    <h2 id="readings-title" class="text-center text-xs font-black text-slate-300 uppercase tracking-[0.5em] mb-12">
                        Character Readings
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
                        <div class="reading-card glass-card p-10 md:p-14 rounded-[2rem] md:rounded-[2.5rem] group">
                            <div class="flex items-center gap-3 mb-6">
                                <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                                </svg>
                                <span class="badge bg-indigo-50 text-indigo-600 border border-indigo-100">
                                    On'yomi
                                </span>
                            </div>
                            <div class="text-3xl md:text-4xl font-black text-slate-900 kanji-font group-hover:text-indigo-600 transition-colors">
                                {"、".join(item['onyomi']) if item['onyomi'] else "—"}
                            </div>
                            <p class="text-xs text-slate-400 mt-4 uppercase tracking-wider">Chinese Reading</p>
                        </div>
                        <div class="reading-card glass-card p-10 md:p-14 rounded-[2rem] md:rounded-[2.5rem] group">
                            <div class="flex items-center gap-3 mb-6">
                                <svg class="w-6 h-6 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                </svg>
                                <span class="badge bg-emerald-50 text-emerald-600 border border-emerald-100">
                                    Kun'yomi
                                </span>
                            </div>
                            <div class="text-3xl md:text-4xl font-black text-slate-900 kanji-font group-hover:text-emerald-600 transition-colors">
                                {"、".join(item['kunyomi']) if item['kunyomi'] else "—"}
                            </div>
                            <p class="text-xs text-slate-400 mt-4 uppercase tracking-wider">Japanese Reading</p>
                        </div>
                    </div>
                </section>
                
                <!-- Grammar Note (if exists) -->
                {f'''<section class="mb-20 md:mb-32" aria-labelledby="grammar-title">
                    <div class="glass-card p-10 md:p-14 rounded-[2rem] md:rounded-[2.5rem] border-l-4 border-purple-500">
                        <div class="flex items-center gap-3 mb-6">
                            <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                            </svg>
                            <h2 id="grammar-title" class="text-sm font-black text-purple-600 uppercase tracking-wider">
                                Grammar Insight
                            </h2>
                        </div>
                        <p class="text-lg md:text-xl text-slate-700 leading-relaxed">
                            {item['grammar_note']}
                        </p>
                    </div>
                </section>''' if item.get('grammar_note') else ''}
                
                <!-- Usage Examples -->
                <section aria-labelledby="examples-title">
                    <div class="text-center mb-12 md:mb-16">
                        <h2 id="examples-title" class="text-xs font-black text-slate-300 uppercase tracking-[0.5em] mb-4">
                            Usage Examples
                        </h2>
                        <p class="text-slate-500 text-sm max-w-2xl mx-auto">
                            See how this kanji is used in real Japanese sentences
                        </p>
                    </div>
                    {ex_view}
                </section>
                
                <!-- Navigation Footer -->
                <div class="mt-20 md:mt-32 text-center">
                    <a href="/{lvl}/" 
                       class="btn-primary inline-flex items-center gap-3"
                       aria-label="Return to N5 collection">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
                        </svg>
                        Back to Collection
                    </a>
                </div>
            </div>"""

            slug = f"{lvl}/kanji/{item['slug']}.html"
            with open(slug, "w", encoding="utf-8") as f:
                f.write(get_pro_layout(
                    f"{item['kanji']} - {item['meaning']} | {lvl.upper()} Kanji", 
                    f"Learn {item['kanji']} ({item['meaning']}) - Complete guide with readings, examples and usage. {item.get('grammar_note', '')}", 
                    detail_content, 
                    slug, 
                    item['kanji'], 
                    lvl
                ))
            all_urls.append(f"{BASE_URL}/{slug}")

    # 3. PREMIUM LANDING PAGE
    home_grid = "".join([f"""
        <a href="/{k['lvl']}/kanji/{k['slug']}.html" 
           class="glass-card p-10 md:p-16 rounded-[2.5rem] md:rounded-[4rem] group text-center hover:shadow-2xl hover:shadow-indigo-100 transition-all duration-500"
           aria-label="Learn {k['kanji']} - {k['meaning']}">
            <div class="kanji-display text-6xl md:text-9xl mb-8 md:mb-10 group-hover:scale-110 transition-transform duration-700 text-slate-900">
                {k['kanji']}
            </div>
            <div class="space-y-3">
                <div class="badge bg-gradient-to-r from-slate-900 to-slate-800 text-white shadow-lg">
                    {k['lvl'].upper()}
                </div>
                <div class="text-xs md:text-base font-black uppercase tracking-widest text-slate-800">
                    {k['meaning']}
                </div>
                <div class="text-[10px] text-slate-400 font-semibold tracking-wider">
                    {k.get('romaji', '')}
                </div>
            </div>
        </a>""" for k in all_kanji_data[:8]])

    home_content = f"""
    <!-- Hero Section -->
    <div class="relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 md:px-8 py-24 md:py-40">
            <div class="text-center mb-24 md:mb-40">
                <!-- Animated Badge -->
                <div class="inline-flex items-center gap-3 mb-8 animate-bounce">
                    <span class="badge bg-gradient-to-r from-indigo-50 to-purple-50 text-indigo-600 border border-indigo-100 shadow-lg">
                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"/>
                        </svg>
                        Professional Learning Platform
                    </span>
                </div>
                
                <!-- Main Heading -->
                <h1 class="text-[60px] md:text-[160px] font-black tracking-tighter leading-[0.85] mb-8">
                    <span class="block text-slate-900">PURE</span>
                    <span class="block text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600">
                        KANJI.
                    </span>
                </h1>
                
                <!-- Subtitle -->
                <p class="text-xl md:text-3xl text-slate-500 font-medium max-w-3xl mx-auto leading-relaxed mb-12">
                    The premium archive for <span class="font-bold text-slate-700">JLPT mastery</span>. 
                    Learn kanji with interactive examples, detailed readings, and professional design.
                </p>
                
                <!-- CTA Buttons -->
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="/n5/" class="btn-primary group inline-flex items-center gap-3">
                        <svg class="w-5 h-5 group-hover:rotate-12 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                        </svg>
                        Start with N5
                        <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                        </svg>
                    </a>
                    <a href="#preview" 
                       class="px-8 py-4 bg-white text-slate-700 text-xs font-black uppercase tracking-widest rounded-full border-2 border-slate-200 hover:border-indigo-600 hover:text-indigo-600 transition-all duration-300 shadow-lg hover:shadow-xl">
                        Preview Collection
                    </a>
                </div>
                
                <!-- Stats -->
                <div class="grid grid-cols-3 gap-8 max-w-2xl mx-auto mt-20">
                    <div class="text-center">
                        <div class="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-br from-indigo-600 to-purple-600 mb-2">
                            80+
                        </div>
                        <div class="text-xs text-slate-400 font-semibold uppercase tracking-wider">
                            Kanji
                        </div>
                    </div>
                    <div class="text-center">
                        <div class="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-br from-purple-600 to-pink-600 mb-2">
                            240+
                        </div>
                        <div class="text-xs text-slate-400 font-semibold uppercase tracking-wider">
                            Examples
                        </div>
                    </div>
                    <div class="text-center">
                        <div class="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-br from-pink-600 to-rose-600 mb-2">
                            N5
                        </div>
                        <div class="text-xs text-slate-400 font-semibold uppercase tracking-wider">
                            JLPT Level
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Featured Kanji Preview -->
    <div id="preview" class="max-w-7xl mx-auto px-4 md:px-8 pb-24 md:pb-40">
        <div class="text-center mb-16 md:mb-24">
            <span class="badge bg-slate-100 text-slate-600 mb-4">Featured Characters</span>
            <h2 class="text-4xl md:text-6xl font-black tracking-tighter text-slate-900 mb-6">
                Start Your <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600">Journey</span>
            </h2>
            <p class="text-lg text-slate-500 max-w-2xl mx-auto">
                Explore our curated collection of essential kanji characters
            </p>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8">
            {home_grid}
        </div>
        <div class="text-center mt-16">
            <a href="/n5/" class="inline-flex items-center gap-3 text-indigo-600 font-bold text-sm hover:gap-4 transition-all">
                View Full Collection
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
            </a>
        </div>
    </div>
    
    <!-- Features Section -->
    <div class="bg-gradient-to-b from-slate-50/50 to-white py-24 md:py-32">
        <div class="max-w-7xl mx-auto px-4 md:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-black tracking-tighter text-slate-900 mb-6">
                    Why Choose <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600">KanjiTest</span>
                </h2>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="glass-card p-10 rounded-[2rem] text-center">
                    <div class="w-16 h-16 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-black mb-4 text-slate-900">Complete Readings</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Both On'yomi and Kun'yomi readings with clear explanations and context
                    </p>
                </div>
                <div class="glass-card p-10 rounded-[2rem] text-center">
                    <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-pink-600 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-black mb-4 text-slate-900">Real Examples</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Multiple usage examples with romaji and English translations
                    </p>
                </div>
                <div class="glass-card p-10 rounded-[2rem] text-center">
                    <div class="w-16 h-16 bg-gradient-to-br from-pink-500 to-rose-600 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-black mb-4 text-slate-900">Grammar Insights</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Detailed grammar notes and usage patterns for deeper understanding
                    </p>
                </div>
            </div>
        </div>
    </div>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(get_pro_layout(
            "KanjiTest - Premium Japanese Learning Platform for JLPT Mastery", 
            "Master JLPT kanji with our professional learning platform. Interactive examples, complete readings, and modern design for effective Japanese language learning.", 
            home_content, 
            "index.html"
        ))

    # 4. GENERATE SITEMAP
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        sitemap_content += f'  <url><loc>{BASE_URL}/</loc><priority>1.0</priority></url>\n'
        sitemap_content += f'  <url><loc>{BASE_URL}/n5/</loc><priority>0.9</priority></url>\n'
        for url in all_urls:
            sitemap_content += f'  <url><loc>{url}</loc><priority>0.8</priority></url>\n'
        sitemap_content += '</urlset>'
        f.write(sitemap_content)
    
    print(f"✅ Build Complete!")
    print(f"📄 Generated {len(all_urls)} kanji pages")
    print(f"🗺️  Sitemap created with {len(all_urls) + 2} URLs")

if __name__ == "__main__":
    build
