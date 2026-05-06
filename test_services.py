"""
Unit tests for the services module.

These tests validate:
- Suggestion input validation
- Error handling for invalid data
- Priority score calculation logic
"""

import unittest
from services import validate_suggestion, calculate_priority


class TestServices(unittest.TestCase):
    """
    Test cases for validation and priority scoring functions.
    """

    def test_valid_suggestion(self):
        """
        Test that a valid suggestion passes validation successfully.
        """
        valid, message = validate_suggestion("Improve meetings", "Process", "High")
        self.assertTrue(valid)

    def test_empty_suggestion(self):
        """
        Test that empty suggestion text fails validation.
        """
        valid, message = validate_suggestion("", "Process", "High")
        self.assertFalse(valid)

    def test_invalid_category(self):
        """
        Test that an invalid category is rejected.
        """
        valid, message = validate_suggestion("Improve meetings", "Invalid", "High")
        self.assertFalse(valid)

    def test_invalid_urgency(self):
        """
        Test that an invalid urgency level is rejected.
        """
        valid, message = validate_suggestion("Improve meetings", "Process", "Urgent")
        self.assertFalse(valid)

    def test_priority_score(self):
        """
        Test that the priority score is calculated correctly.
        """
        score = calculate_priority("High", "Technical")

        # High urgency (3) + Technical category (3) = 6
        self.assertEqual(score, 6)


if __name__ == "__main__":
    # Run unit tests
    unittest.main()