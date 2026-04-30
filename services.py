VALID_CATEGORIES = ["Process", "Communication", "Culture", "Wellbeing", "Technical", "Other"]
VALID_URGENCY = ["Low", "Medium", "High"]
VALID_STATUSES = ["New", "Under Review", "Accepted", "Rejected", "Implemented"]


def validate_suggestion(text, category, urgency):
    if not text.strip():
        return False, "Suggestion text cannot be empty."

    if category not in VALID_CATEGORIES:
        return False, "Invalid category."

    if urgency not in VALID_URGENCY:
        return False, "Invalid urgency."

    return True, "Valid"


def calculate_priority(urgency, category):
    urgency_scores = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    category_scores = {
        "Process": 3,
        "Technical": 3,
        "Communication": 2,
        "Wellbeing": 2,
        "Culture": 1,
        "Other": 1
    }

    return urgency_scores.get(urgency, 1) + category_scores.get(category, 1)