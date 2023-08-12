import unittest
from models.state import State
"""Module for the State class tests"""


class TestState(unittest.TestCase):
    """Main class for testing State"""

    def test_init(self):
        """
        Tests the attributes of a State instance as well as __init__()
        """
        state = State()
        self.assertEqual(state.name, "")
