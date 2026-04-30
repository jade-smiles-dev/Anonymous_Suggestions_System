from database import create_table, add_suggestion, get_all_suggestions, update_suggestion_status, get_new_suggestions
from services import validate_suggestion, VALID_CATEGORIES, VALID_URGENCY, VALID_STATUSES


def submit_suggestion():
    print("\n--- Submit a Suggestion ---")

    text = input("Enter your suggestion: ")

    print("\nChoose a category:")
    for i, category in enumerate(VALID_CATEGORIES, start=1):
        print(f"{i}. {category}")

    try:
        category_choice = int(input("Enter number: "))
        category = VALID_CATEGORIES[category_choice - 1]
    except:
        print("Invalid category choice.")
        return

    print("\nChoose urgency:")
    for i, urgency in enumerate(VALID_URGENCY, start=1):
        print(f"{i}. {urgency}")

    try:
        urgency_choice = int(input("Enter number: "))
        urgency = VALID_URGENCY[urgency_choice - 1]
    except:
        print("Invalid urgency choice.")
        return

    valid, message = validate_suggestion(text, category, urgency)

    if not valid:
        print("Error:", message)
        return

    add_suggestion(text, category, urgency)
    print("Suggestion submitted successfully!")


def view_suggestions():
    suggestions = get_all_suggestions()

    if not suggestions:
        print("\nNo suggestions found.")
        return

    print("\n--- All Suggestions ---")

    for suggestion in suggestions:
        suggestion_id, text, category, urgency, status, priority = suggestion

        print(f"\nID: {suggestion_id}")
        print(f"Text: {text}")
        print(f"Category: {category}")
        print(f"Urgency: {urgency}")
        print(f"Status: {status}")
        print(f"Priority: {priority}")
        print("-" * 30)


def update_status():
    try:
        suggestion_id = int(input("Enter suggestion ID to update: "))
    except:
        print("Invalid ID.")
        return

    print("\nChoose new status:")
    for i, status in enumerate(VALID_STATUSES, start=1):
        print(f"{i}. {status}")

    try:
        status_choice = int(input("Enter number: "))
        new_status = VALID_STATUSES[status_choice - 1]
    except:
        print("Invalid status choice.")
        return

    update_suggestion_status(suggestion_id, new_status)
    print("Status updated successfully!")


def main():
    create_table()

    while True:
        print("1. Submit a suggestion")
        print("2. View all suggestions")
        print("3. View NEW suggestions (priority sorted)")
        print("4. Update suggestion status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            submit_suggestion()
        elif choice == "2":
            view_suggestions()
        elif choice == "3":
            view_new_suggestions()
        elif choice == "4":
            update_status()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def view_new_suggestions():
    suggestions = get_new_suggestions()

    if not suggestions:
        print("\nNo new suggestions found.")
        return

    print("\n--- New Suggestions (Priority Sorted) ---")

    for suggestion in suggestions:
        suggestion_id, text, category, urgency, status, priority = suggestion

        print(f"\nID: {suggestion_id}")
        print(f"Text: {text}")
        print(f"Category: {category}")
        print(f"Urgency: {urgency}")
        print(f"Status: {status}")
        print(f"Priority: {priority}")
        print("-" * 30)

if __name__ == "__main__":
    main()