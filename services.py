"""
Services module for the Anonymous Suggestions System.

This module contains:
- Validation logic for user input
- Priority scoring logic
- Predefined constants used across the application

Separating this logic improves maintainability and ensures consistency.
"""

# Predefined valid input options used for validation and user selection
VALID_CATEGORIES = ["Process", "Communication", "Culture", "Wellbeing", "Technical", "Other"]
VALID_URGENCY = ["Low", "Medium", "High"]
VALID_STATUSES = ["New", "Under Review", "Accepted", "Rejected", "Implemented"]


def validate_suggestion(text, category, urgency):
    """
    Validates user input for a suggestion.

    Checks:
    - Suggestion text is not empty
    - Category is within allowed options
    - Urgency is within allowed options

    Returns:
        (bool, str): Tuple indicating whether input is valid and an associated message
    """

    # Ensure suggestion text is not empty or just whitespace
    if not text.strip():
        return False, "Suggestion text cannot be empty."

    # Validate category against the pre defined list
    if category not in VALID_CATEGORIES:
        return False, "Invalid category."

    # Validate urgency level
    if urgency not in VALID_URGENCY:
        return False, "Invalid urgency."

    # All checks passed
    return True, "Valid"


def calculate_priority(urgency, category):
    """
    Calculates a priority score for a suggestion based on urgency and category.

    Higher scores indicate higher priority.

    Parameters:
        urgency (str): Urgency level of the suggestion
        category (str): Category of the suggestion

    Returns:
        int: Calculated priority score
    """

    # Assign numerical weighting to urgency levels
    urgency_scores = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    # Assign weighting scores to categories based on perceived importance
    category_scores = {
        "Process": 3,
        "Technical": 3,
        "Communication": 2,
        "Wellbeing": 2,
        "Culture": 1,
        "Other": 1
    }

    # Combine urgency and category scores to determine overall priority
    # Default value of 1 is used if an unexpected value is encountered
    return urgency_scores.get(urgency, 1) + category_scores.get(category, 1)
