#whatsapp chat analysics

def count_messages(chat_data):
    """Count number of messages by each person"""
    counts = {}
    for name, _ in chat_data:
        counts[name] = counts.get(name, 0) + 1
    return counts


def unique_users(chat_data):
    """Find unique participants in chat"""
    return set(name for name, _ in chat_data)


def longest_message(chat_data):
    """Find who wrote the longest message"""
    longest = max(chat_data, key=lambda x: len(x[1]))
    return longest


def search_keyword(chat_data, keyword):
    """Search messages containing a keyword"""
    results = []
    for name, msg in chat_data:
        if keyword.lower() in msg.lower():
            results.append((name, msg))
    return results


def menu():
    print("\nChoose an analysis option:")
    print("1. Count messages by each user")
    print("2. Show unique users")
    print("3. Find the longest message")
    print("4. Search messages by keyword")
    print("5. Exit")


def main():
    chat_data = []
    n = int(input("Enter the number of messages: "))

    print("\nEnter messages in 'Name: message' format:")
    for _ in range(n):
        entry = input().strip()
        if ":" in entry:
            name, msg = entry.split(":", 1)
            chat_data.append((name.strip(), msg.strip()))
        else:
            print("Invalid format. Skipping...")

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            counts = count_messages(chat_data)
            print("\nMessage Count:")
            for user, count in counts.items():
                print(f"{user}: {count}")

        elif choice == "2":
            users = unique_users(chat_data)
            print("\nUnique Users:")
            print(", ".join(users))

        elif choice == "3":
            user, msg = longest_message(chat_data)
            print(f"\nLongest Message by {user}: {msg}")

        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            results = search_keyword(chat_data, keyword)
            print(f"\nMessages containing '{keyword}':")
            for user, msg in results:
                print(f"{user}: {msg}")

        elif choice == "5":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    
    main()