import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_base_model(self):
        with self.assertRaises(TypeError) as err:
            BaseModel("exess")
        self.assertEqual(str(err.exception), 'BaseModel.__init__() takes 1 positional argument but 2 were given')
        
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
    
    def test_save(self):
        base = BaseModel()
        with self.assertRaises(TypeError) as err:
            base.save("exess")
        self.assertEqual(str(err.exception), 'BaseModel.save() takes 1 positional argument but 2 were given')

        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
    
    def test_to_dict(self):
        pass
    
    def test_str(self):
        base = BaseModel()
        expected = f'[{base.__class__.__name__}] ({base.id}) {base.__dict__}'
        self.assertEqual(str(base), expected)
