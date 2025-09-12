# News article categories
import os
import re

# Categories and keywords
categories = {
    "Politics": ["election", "government", "parliament", "minister", "policy"],
    "Sports": ["match", "tournament", "player", "goal", "cricket", "football"],
    "Technology": ["AI", "software", "technology", "computer", "robotics"],
    "Health": ["doctor", "vaccine", "health", "hospital", "medicine"]
}

ARTICLES_DIR = "articles"

# Ensure directory exists
os.makedirs(ARTICLES_DIR, exist_ok=True)

def analyze_article(filename):
    try:
        with open(os.path.join(ARTICLES_DIR, filename), "r") as f:
            content = f.read().lower()
        
        found_categories = []
        for category, keywords in categories.items():
            for word in keywords:
                if re.search(rf"\b{word.lower()}\b", content):
                    found_categories.append(category)
                    break
        
        if not found_categories:
            print(f"'{filename}' does not match any category.")
        else:
            print(f"'{filename}' belongs to categories: {', '.join(found_categories)}")
    
    except FileNotFoundError:
        print("File not found.")

def create_article():
    filename = input("Enter new article filename: ") + ".txt"
    content = input("Enter article content:\n")
    with open(os.path.join(ARTICLES_DIR, filename), "w") as f:
        f.write(content)
    print(f"Article '{filename}' created successfully.")

def modify_article():
    filename = input("Enter article filename to modify: ") + ".txt"
    try:
        with open(os.path.join(ARTICLES_DIR, filename), "a") as f:
            content = input("Enter content to add:\n")
            f.write("\n" + content)
        print(f"Article '{filename}' updated successfully.")
    except FileNotFoundError:
        print("Article not found.")

def report():
    summary = {cat: 0 for cat in categories}
    for filename in os.listdir(ARTICLES_DIR):
        with open(os.path.join(ARTICLES_DIR, filename), "r") as f:
            content = f.read().lower()
            for cat, keywords in categories.items():
                if any(re.search(rf"\b{word.lower()}\b", content) for word in keywords):
                    summary[cat] += 1
    print("\n--- Categorization Report ---")
    for cat, count in summary.items():
        print(f"{cat}: {count} articles")

def main():
    while True:
        print("\n--- News Article Categorizer ---")
        print("1. Analyze Article")
        print("2. Analyze All Articles")
        print("3. Create New Article")
        print("4. Modify Existing Article")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            filename = input("Enter article filename: ") + ".txt"
            analyze_article(filename)
        elif choice == "2":
            for filename in os.listdir(ARTICLES_DIR):
                analyze_article(filename)
        elif choice == "3":
            create_article()
        elif choice == "4":
            modify_article()
        elif choice == "5":
            report()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()