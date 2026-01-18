import os
import json
import random
import uuid

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
LEVELS = ["n5", "n4", "n3", "n2", "n1"]
QUESTIONS_PER_TEST = 10
TESTS_TO_GENERATE = 5  # Generates 5 unique test sets per level

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def generate_kanji_question(kanji_list):
    """
    Creates a single multiple-choice question:
    "What is the meaning of [Kanji]?"
    """
    if len(kanji_list) < 4:
        return None # Not enough data to make options
        
    correct_item = random.choice(kanji_list)
    
    # Select 3 distinct wrong answers
    distractors = random.sample([k for k in kanji_list if k != correct_item], 3)
    
    options = [correct_item['meaning']] + [d['meaning'] for d in distractors]
    random.shuffle(options)
    
    return {
        "id": str(uuid.uuid4())[:8],
        "type": "kanji_meaning",
        "question": f"What is the meaning of {correct_item['character']}?",
        "options": options,
        "correct_index": options.index(correct_item['meaning']),
        "explanation": f"The character {correct_item['character']} means '{correct_item['meaning']}'. Reading: {correct_item.get('onyomi', '')} / {correct_item.get('kunyomi', '')}"
    }

def generate_test_set(level, set_number, data_pool):
    """
    Compiles a list of questions into a full Test Object.
    """
    questions = []
    for _ in range(QUESTIONS_PER_TEST):
        q = generate_kanji_question(data_pool)
        if q:
            questions.append(q)
            
    return {
        "id": f"{level}-kanji-set-{set_number}",
        "title": f"JLPT {level.upper()} Kanji Practice Set {set_number}",
        "slug": f"{level}-kanji-practice-test-{set_number}",
        "description": f"Test your knowledge of {level.upper()} Kanji. {QUESTIONS_PER_TEST} questions with instant scoring.",
        "questions": questions
    }

def main():
    print("🧠 Starting AI Test Generator...")
    
    for level in LEVELS:
        level_dir = os.path.join(PROCESSED_DIR, level)
        kanji_file = os.path.join(level_dir, "kanji.json")
        output_file = os.path.join(level_dir, "tests.json")
        
        kanji_data = load_json(kanji_file)
        
        if not kanji_data:
            print(f"   ⚠️ Skipping {level.upper()} (No Kanji data found)")
            continue
            
        print(f"   ⚡ Generating tests for {level.upper()}...")
        
        test_collection = []
        for i in range(1, TESTS_TO_GENERATE + 1):
            test_set = generate_test_set(level, i, kanji_data)
            test_collection.append(test_set)
            
        # Write the generated tests to tests.json
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(test_collection, f, indent=2, ensure_ascii=False)
            
        print(f"      ✅ Created {len(test_collection)} test sets in {output_file}")

    print("\n🎉 Test Generation Complete!")

if __name__ == "__main__":
    main()
