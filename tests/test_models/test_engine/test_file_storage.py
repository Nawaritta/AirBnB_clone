#!/usr/bin/python3
"""Module for the FileStorage class tests"""
import unittest
from os import path
from models.engine.file_storage import FileStorage
from models import storage



class TestFileStorage(unittest.TestCase):
    """Main class for testing FileStorage"""

    def setUp(self):
        """Set up test resources."""
        self.file_storage = FileStorage()

    def tearDown(self):
        """Clean up test resources."""
        self.file_storage.clear_data()
        self.file_storage.save_data()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_init(self):
        """
        Tests the attributes of a FileStorage instance as well as __init__()
        """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path,
                         'creatd_instances.json')
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.all("exess")
        self.assertEqual(str(err.exception), 'FileStorage.all() takes 1'
                         + ' positional argument but 2 were given')
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_new(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.new()
        self.assertEqual(str(err.exception), 'FileStorage.new() missing 1'
                         + " required positional argument: 'obj'")
        with self.assertRaises(TypeError) as err:
            storage.new("obj", "exess")
        self.assertEqual(str(err.exception), 'FileStorage.new() takes 2'
                         + ' positional arguments but 3 were given')

    def test_save(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.save("exess")
        self.assertEqual(str(err.exception), 'FileStorage.save() takes 1'
                         + ' positional argument but 2 were given')
        storage.save()
        file_name = storage._FileStorage__file_path
        self.assertTrue(path.exists(file_name))

    def test_reload(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.reload("exess")
        self.assertEqual(str(err.exception), 'FileStorage.reload() takes 1'
                         + ' positional argument but 2 were given')

    def test_init_no_args(self):
        """Test that __init__ raises TypeError with no arguments."""
        with self.assertRaises(TypeError) as context:
            self.file_storage = FileStorage.__init__()

        expected_msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(context.exception), expected_msg)

    def test_init_many_args(self):
        """Test that __init__ raises TypeError with many arguments."""
        args = (0, "hello", [1, 2, 3])
        with self.assertRaises(TypeError) as context:
            self.file_storage = FileStorage(*args)

        expected_msg = "object() takes no parameters"
        self.assertEqual(str(context.exception), expected_msg)

    def test_reload_no_args(self):
        """Test that reload() raises TypeError with no arguments."""
        with self.assertRaises(TypeError) as context:
            self.file_storage = FileStorage.reload()

        expected_msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(context.exception), expected_msg)

    def test_reload_excess_args(self):
        """Test that reload() raises TypeError with too many arguments."""
        excessive_arg = 80
        with self.assertRaises(TypeError) as context:
            self.file_storage = FileStorage.reload(self, excessive_arg)

        expected_msg = "reload() takes 1 positional argument but 2 were given"
    self.assertEqual(str(context.exception), expected_msg)


if __name__ == '__main__':
    unittest.main()
