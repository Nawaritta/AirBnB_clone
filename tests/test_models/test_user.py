import unittest
from models.user import User
"""Module for the User class tests"""


class TestUser(unittest.TestCase):
    """Main class for testing User"""

    def test_init(self):
        """
        Tests the attributes of a User instance as well as __init__()
        """
        with self.assertRaises(TypeError) as err:
            User.__init__()

        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
