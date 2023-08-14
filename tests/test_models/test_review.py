import unittest
from models.review import Review
"""Module for the User class tests"""


class TestReview(unittest.TestCase):
    """Main class for testing Review"""

    def test_init(self):
        """
        Tests the attributes of a Review instance as well as __init__()
        """
        with self.assertRaises(TypeError) as err:
            Review.__init__()

        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
