/**
 * Global Real-Time Search Logic
 * Optimized for low latency across thousands of entries
 */
let searchIndex = [];

async function buildGlobalIndex() {
    const levels = ['n5', 'n4', 'n3', 'n2', 'n1'];
    const promises = levels.map(lvl => fetchLevelData(lvl));
    const results = await Promise.all(promises);
    
    results.forEach((data, index) => {
        if (data) {
            const levelName = levels[index];
            data.kanji_set.forEach(k => {
                searchIndex.push({
                    ...k,
                    level: levelName,
                    url: `/${levelName}/kanji/${k.slug}.html`
                });
            });
        }
    });
}

function handleSearch(query) {
    if (query.length < 1) return [];
    const q = query.toLowerCase();
    
    // SEO-UX: Search by Kanji, Meaning, or Romaji
    return searchIndex.filter(item => 
        item.kanji.includes(q) || 
        item.meaning.toLowerCase().includes(q) || 
        item.romaji.toLowerCase().includes(q)
    ).slice(0, 10); // Limit to top 10 for performance
}

// Initializing the engine
buildGlobalIndex();
