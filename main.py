"""
Main entry point for the Anonymous Suggestions System.

This module provides a command-line interface (CLI) for users to:
- Submit suggestions
- View all suggestions
- View new suggestions (priority sorted)
- Update suggestion statuses

It coordinates user input and interacts with the database and services layers.
"""

from database import create_table, add_suggestion, get_all_suggestions, update_suggestion_status, get_new_suggestions
from services import validate_suggestion, VALID_CATEGORIES, VALID_URGENCY, VALID_STATUSES


def submit_suggestion():
    """
    Handles user input for submitting a new suggestion.

    Prompts the user to:
    - Enter suggestion text
    - Select a category
    - Select an urgency level

    Validates the input before saving to the database.
    """
    print("\n--- Submit a Suggestion ---")

    text = input("Enter your suggestion: ")

    # Display available categories for selection
    print("\nChoose a category:")
    for i, category in enumerate(VALID_CATEGORIES, start=1):
        print(f"{i}. {category}")

    try:
        category_choice = int(input("Enter number: "))
        category = VALID_CATEGORIES[category_choice - 1]
    except:
        # Handles invalid numeric input or out-of-range selection
        print("Invalid category choice.")
        return

    # Display urgency options
    print("\nChoose urgency:")
    for i, urgency in enumerate(VALID_URGENCY, start=1):
        print(f"{i}. {urgency}")

    try:
        urgency_choice = int(input("Enter number: "))
        urgency = VALID_URGENCY[urgency_choice - 1]
    except:
        print("Invalid urgency choice.")
        return

    # Validate user input before storing
    valid, message = validate_suggestion(text, category, urgency)

    if not valid:
        print("Error:", message)
        return

    # Save valid suggestion to the database
    add_suggestion(text, category, urgency)
    print("Suggestion submitted successfully!")


def view_suggestions():
    """
    Retrieves and displays all suggestions stored in the database.

    Outputs suggestion details in a readable format for the user.
    """
    suggestions = get_all_suggestions()

    if not suggestions:
        print("\nNo suggestions found.")
        return

    print("\n--- All Suggestions ---")

    for suggestion in suggestions:
        # Unpack tuple returned from database
        suggestion_id, text, category, urgency, status, priority = suggestion

        print(f"\nID: {suggestion_id}")
        print(f"Text: {text}")
        print(f"Category: {category}")
        print(f"Urgency: {urgency}")
        print(f"Status: {status}")
        print(f"Priority: {priority}")
        print("-" * 30)


def update_status():
    """
    Updates the status of an existing suggestion.

    Prompts the user to:
    - Enter a valid suggestion ID
    - Select a new status from predefined options
    """
    try:
        suggestion_id = int(input("Enter suggestion ID to update: "))
    except:
        print("Invalid ID.")
        return

    # Display available status options
    print("\nChoose new status:")
    for i, status in enumerate(VALID_STATUSES, start=1):
        print(f"{i}. {status}")

    try:
        status_choice = int(input("Enter number: "))
        new_status = VALID_STATUSES[status_choice - 1]
    except:
        print("Invalid status choice.")
        return

    # Update status in database
    update_suggestion_status(suggestion_id, new_status)
    print("Status updated successfully!")


def view_new_suggestions():
    """
    Displays only suggestions with 'New' status, sorted by priority.

    This allows managers to focus on recent and high-priority items.
    """
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


def main():
    """
    Main program loop for the CLI.

    Displays menu options and routes user input to the appropriate function.
    """
    # Ensure database table exists before starting application
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
            # Handles invalid menu selection
            print("Invalid option.")


if __name__ == "__main__":
    # Entry point of the application
    main()