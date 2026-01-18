/**
 * Kanjitest-Online API Engine
 * Handles dynamic fetching for N5-N1 levels
 */
const API_BASE = '/data-engine/api';

async function fetchLevelData(level) {
    try {
        const response = await fetch(`${API_BASE}/${level}/data.json`);
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("API Engine Error:", error);
        return null;
    }
}

// SEO-Friendly Breadcrumb Generator
function initBreadcrumbs() {
    const path = window.location.pathname.split('/').filter(p => p);
    const breadcrumbContainer = document.getElementById('breadcrumbs');
    if (!breadcrumbContainer) return;

    let html = '<a href="/">Home</a>';
    path.forEach((part, index) => {
        const url = '/' + path.slice(0, index + 1).join('/');
        html += ` <span class="mx-2">/</span> <a href="${url}" class="capitalize">${part}</a>`;
    });
    breadcrumbContainer.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', initBreadcrumbs);
