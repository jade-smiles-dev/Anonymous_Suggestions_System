import unittest
from services import validate_suggestion, calculate_priority


class TestServices(unittest.TestCase):

    def test_valid_suggestion(self):
        valid, message = validate_suggestion("Improve meetings", "Process", "High")
        self.assertTrue(valid)

    def test_empty_suggestion(self):
        valid, message = validate_suggestion("", "Process", "High")
        self.assertFalse(valid)

    def test_invalid_category(self):
        valid, message = validate_suggestion("Improve meetings", "Invalid", "High")
        self.assertFalse(valid)

    def test_invalid_urgency(self):
        valid, message = validate_suggestion("Improve meetings", "Process", "Urgent")
        self.assertFalse(valid)

    def test_priority_score(self):
        score = calculate_priority("High", "Technical")
        self.assertEqual(score, 6)


if __name__ == "__main__":
    unittest.main()