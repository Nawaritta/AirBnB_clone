import unittest
from models.amenity import Amenity
"""Module for the Amenity class tests"""


class TestAmenity(unittest.TestCase):
    """Main class for testing Amenity"""

    def test_init(self):
        """
        Tests the attributes of a Amenity instance as well as __init__()
        """
        with self.assertRaises(TypeError) as err:
            Amenity.__init__()

        amenity = Amenity()
        self.assertEqual(amenity.name, "")

        self.assertIsInstance(amenity.name, str)
