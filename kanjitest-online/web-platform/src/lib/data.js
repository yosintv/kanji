import fs from 'fs';
import path from 'path';

// This points to the #3 processed folder in your #2 data-engine
const DATA_ROOT = path.join(process.cwd(), '../data-engine/processed');

/**
 * Fetches all items for a specific level and category (e.g., 'n5', 'kanji')
 */
export async function getLevelData(level, category) {
  try {
    const filePath = path.join(DATA_ROOT, level, `${category}.json`);
    const fileContents = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(fileContents);
  } catch (error) {
    console.error(`Error loading data for ${level}/${category}:`, error);
    return [];
  }
}

/**
 * Finds a specific item by its SEO slug
 */
export async function getItemBySlug(level, category, slug) {
  const data = await getLevelData(level, category);
  return data.find((item) => item.slug === slug) || null;
}

/**
 * Gets a specific test set by its ID
 */
export async function getTestById(level, id) {
  const tests = await getLevelData(level, 'tests');
  return tests.find((test) => test.id === id) || null;
}
