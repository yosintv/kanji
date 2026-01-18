// Global search across all levels
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('global-search');
  const resultsContainer = document.getElementById('search-results');
  
  if (!searchInput || !resultsContainer) return;
  
  let searchIndex = []; // Load from JSON or prebuilt
  
  searchInput.addEventListener('input', debounce((e) => {
    const query = e.target.value.toLowerCase();
    if (query.length < 2) {
      resultsContainer.innerHTML = '';
      return;
    }
    
    const matches = searchIndex.filter(item => 
      item.kanji.includes(query) || 
      item.reading.includes(query) || 
      item.meaning.toLowerCase().includes(query)
    );
    
    renderResults(matches.slice(0, 20));
  }, 300));
  
  function renderResults(results) {
    resultsContainer.innerHTML = results.map(item => `
      <a href="${item.url}" class="kanji-card p-4">
        <div class="text-4xl mb-2">${item.kanji}</div>
        <div class="font-semibold">${item.reading}</div>
        <div class="text-sm text-slate-600">${item.meaning}</div>
      </a>
    `).join('');
  }
});

function debounce(fn, delay) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), delay);
  };
}
