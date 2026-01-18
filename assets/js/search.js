// Fetch level data
async function loadLevelData(level) {
  try {
    const response = await fetch(`/data-engine/api/${level}/data.json`);
    return await response.json();
  } catch (error) {
    console.error('Failed to load data:', error);
    return null;
  }
}

// Example usage: loadLevelData('n5').then(data => console.log(data));
