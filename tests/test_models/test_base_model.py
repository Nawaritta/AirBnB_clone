import unittest
from models.base_model import BaseModel
from datetime import datetime
"""Module for the BaseModel class tests"""


class TestBaseModel(unittest.TestCase):
    """Main class for testing BaseModel"""

    def test_base_model(self):
        """
        Tests the attributes of a BaseModel instance as well as __init__()
        """
        with self.assertRaises(TypeError) as err:
            BaseModel("exess")
        self.assertEqual(str(err.exception), 'BaseModel.__init__() takes 1'
                         + ' positional argument but 2 were given')

        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertIsInstance(base.id, str)

    def test_save(self):
        """Tests the save() method of a BaseModel instance"""
        base = BaseModel()
        with self.assertRaises(TypeError) as err:
            base.save("exess")
        self.assertEqual(str(err.exception), 'BaseModel.save() takes 1'
                         + ' positional argument but 2 were given')

        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() function of a BaseModel instance"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)

        base_dict = base.__dict__.copy()
        base_dict['__class__'] = base.__class__.__name__
        base_dict['created_at'] = (base.created_at
                                   .strftime('%Y-%m-%dT%H:%M:%S.%f'))
        base_dict['updated_at'] = (base.updated_at
                                   .strftime('%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(base.to_dict(), base_dict)

        self.assertEqual(len(base.to_dict()), len(base_dict))

        for key, value in base.to_dict().items():
            self.assertEqual(base_dict[key], value)

        base.name = "My instance name"
        base_dict['name'] = "My instance name"
        self.assertEqual(base.to_dict(), base_dict)

    def test_str(self):
        """Tests the __str__() function return of a BaseModel instance"""
        base = BaseModel()
        self.assertIsInstance(str(base), str)

        expected = f'[{base.__class__.__name__}] ({base.id}) {base.__dict__}'
        self.assertEqual(str(base), expected)

        base.name = "My instance name"
        expected = f'[{base.__class__.__name__}] ({base.id}) {base.__dict__}'
        self.assertEqual(str(base), expected)
