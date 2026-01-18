import os
import json
import csv
import re
import shutil

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Points to /data-engine
RAW_DIR = os.path.join(BASE_DIR, "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
LEVELS = ["n5", "n4", "n3", "n2", "n1"]

# --- HELPER FUNCTIONS ---

def create_slug(text):
    """
    Converts '日本 Sun' -> 'nihon-sun' for SEO URLs.
    Removes special characters, lowers case, and replaces spaces with dashes.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf\s-]', '', text) # Keep JP chars
    text = re.sub(r'[\s]+', '-', text)
    return text.strip('-')

def ensure_directory(path):
    """Creates the folder if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

# --- DATA PROCESSORS ---

def process_kanji(level_path):
    """
    Reads kanji.csv (Format: Character, Meaning, Onyomi, Kunyomi)
    Returns a list of dicts with SEO slugs.
    """
    file_path = os.path.join(level_path, "kanji.csv")
    data = []
    
    if not os.path.exists(file_path):
        print(f"⚠️  Warning: {file_path} not found. Skipping.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Create a rich SEO slug: "character + meaning"
            # Example: /n5/kanji/hi-sun-day
            slug_base = f"{row['reading_romaji']}-{row['meaning']}" if 'reading_romaji' in row else row['meaning']
            
            entry = {
                "character": row.get('character', ''),
                "meaning": row.get('meaning', ''),
                "onyomi": row.get('onyomi', ''),
                "kunyomi": row.get('kunyomi', ''),
                "examples": [], # You can expand this logic to parse examples
                "slug": create_slug(slug_base) 
            }
            data.append(entry)
    return data

def process_grammar(level_path):
    """
    Reads grammar.csv (Format: Title, Structure, Meaning)
    """
    file_path = os.path.join(level_path, "grammar.csv")
    data = []

    if not os.path.exists(file_path):
        print(f"⚠️  Warning: {file_path} not found. Skipping.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Example: /n5/grammar/wa-particle
            entry = {
                "title": row.get('title', ''),
                "structure": row.get('structure', ''),
                "meaning": row.get('meaning', ''),
                "slug": create_slug(row.get('title', ''))
            }
            data.append(entry)
    return data

def process_vocabulary(level_path):
    """
    Reads vocab.csv (Format: Word, Reading, Meaning)
    """
    file_path = os.path.join(level_path, "vocab.csv")
    data = []

    if not os.path.exists(file_path):
        print(f"⚠️  Warning: {file_path} not found. Skipping.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Example: /n5/vocabulary/taberu-to-eat
            slug_text = f"{row.get('reading_romaji', '')}-{row.get('meaning', '')}"
            entry = {
                "word": row.get('word', ''),
                "reading": row.get('reading', ''),
                "meaning": row.get('meaning', ''),
                "slug": create_slug(slug_text)
            }
            data.append(entry)
    return data

def process_tests(level_path):
    """
    Reads tests.json (assuming you write tests manually or generate them)
    If no file exists, returns an empty list.
    """
    file_path = os.path.join(level_path, "tests.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# --- MAIN EXECUTION ---

def main():
    print("🚀 Starting Data Engine Build Process...")
    
    # 1. Clean and Recreate Processed Directory
    if os.path.exists(PROCESSED_DIR):
        shutil.rmtree(PROCESSED_DIR)
    ensure_directory(PROCESSED_DIR)

    # 2. Loop through all levels (N5 -> N1)
    for level in LEVELS:
        print(f"📂 Processing Level: {level.upper()}...")
        
        raw_level_path = os.path.join(RAW_DIR, level)
        processed_level_path = os.path.join(PROCESSED_DIR, level)
        ensure_directory(processed_level_path)

        # 3. Process each category
        kanji_data = process_kanji(raw_level_path)
        grammar_data = process_grammar(raw_level_path)
        vocab_data = process_vocabulary(raw_level_path)
        test_data = process_tests(raw_level_path)

        # 4. Save to JSON files
        with open(os.path.join(processed_level_path, "kanji.json"), "w", encoding='utf-8') as f:
            json.dump(kanji_data, f, indent=2, ensure_ascii=False)
            
        with open(os.path.join(processed_level_path, "grammar.json"), "w", encoding='utf-8') as f:
            json.dump(grammar_data, f, indent=2, ensure_ascii=False)

        with open(os.path.join(processed_level_path, "vocabulary.json"), "w", encoding='utf-8') as f:
            json.dump(vocab_data, f, indent=2, ensure_ascii=False)
            
        with open(os.path.join(processed_level_path, "tests.json"), "w", encoding='utf-8') as f:
            json.dump(test_data, f, indent=2, ensure_ascii=False)
            
        print(f"   ✅ {level.upper()} Complete: {len(kanji_data)} Kanji, {len(grammar_data)} Grammar")

    print("\n✨ Build Complete! JSON files are ready in /processed/")

if __name__ == "__main__":
    main()
